"""Reproduce Day 6 A chunks without writing to the original project/database."""
import argparse
import hashlib
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_day6(path):
    spec = importlib.util.spec_from_file_location(
        'day6_source', path / 'starter/src/__init__.py',
        submodule_search_locations=[str(path / 'starter/src')])
    package = importlib.util.module_from_spec(spec)
    sys.modules['day6_source'] = package
    spec.loader.exec_module(package)
    from day6_source.chunking import fixed_size
    from day6_source.models import DocumentPage
    return fixed_size, DocumentPage


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--day6', required=True, type=Path)
    args = parser.parse_args()
    day6 = args.day6.resolve()
    manifest = json.loads((day6 / 'data/manifest.json').read_text(encoding='utf-8'))
    source = day6 / manifest['source_path_or_url']
    digest = hashlib.sha256(source.read_bytes()).hexdigest()
    if digest != manifest['sha256']:
        raise ValueError('Day 6 PDF checksum differs from manifest')
    fixed_size, DocumentPage = load_day6(day6)
    pages = [json.loads(line) for line in (day6 / 'data/processed/pages.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
    chunks = []
    for row in pages:
        page = DocumentPage(**{k: row[k] for k in ('document_id', 'source', 'page', 'text', 'metadata')})
        for chunk in fixed_size(page, 500, 50):
            chunks.append(dict(id=chunk.chunk_id, source_id=chunk.document_id,
                               source=chunk.source, page=chunk.page, text=chunk.text,
                               metadata={**chunk.metadata,
                                         'embedding_model': 'intfloat/multilingual-e5-small',
                                         'embedding_revision': '614241f622f53c4eeff9890bdc4f31cfecc418b3'}))
    # Import only old dev. Old test results have been inspected; do not reuse as held out.
    questions = []
    for line in (day6 / 'benchmark/questions.jsonl').read_text(encoding='utf-8').splitlines():
        q = json.loads(line)
        if q['split'] != 'dev':
            continue
        gold = dict(source_id=q['gold_source_id'], page=q['gold_page'], evidence=q['evidence_quote'])
        original_page = next(p['text'] for p in pages if p['document_id'] == gold['source_id'] and p['page'] == gold['page'])
        # Preserve the exact page excerpt (including PDF line breaks). A gold may
        # span two chunks: keep it, rather than removing difficult questions.
        match = re.search(r'\s+'.join(re.escape(w) for w in gold['evidence'].split()), original_page)
        if match is None:
            raise ValueError(f"Evidence missing from original page: {q['id']}")
        gold['evidence'] = match.group()
        questions.append(dict(id='day7-' + q['id'], split='dev', question=q['question'],
                              answerable=True, expected_answer=q['expected_answer'], gold=[gold],
                              filter=q.get('filter', {}), provenance='Day 6 dev; reused'))
    write_json(ROOT / 'data/day6/chunks.json', chunks)
    write_json(ROOT / 'benchmark/dev_answerable.json', questions)
    write_json(ROOT / 'data/day6/provenance.json', dict(
        day6_path=str(day6), source_sha256=digest, source_id=manifest['source_id'],
        permission=manifest['license_or_permission'], pages=len(pages), chunks=len(chunks),
        chunking=dict(strategy='A', size=500, overlap=50),
        embedding=dict(model='intfloat/multilingual-e5-small',
                       revision='614241f622f53c4eeff9890bdc4f31cfecc418b3',
                       dimensions=384, query_prefix='query: ', document_prefix='passage: ',
                       normalize_embeddings=True),
        vector_store=dict(type='pgvector', table='day6_chunks', strategy='A', port=55433),
        limitations=['Chunks reproduced from Day 6 code; verify database equality with src.day6_bridge.',
                     'Text extraction does not interpret figures.',
                     'This export contains only old dev answerable questions; build full Day 7 benchmark separately.']))
    print(json.dumps(dict(pages=len(pages), chunks=len(chunks), dev_answerable=len(questions), pdf_checksum='verified')))


if __name__ == '__main__':
    main()
