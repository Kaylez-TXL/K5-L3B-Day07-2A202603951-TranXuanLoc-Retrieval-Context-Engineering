"""Check benchmark locks, saved trace invariants and accidental key inclusion."""
import hashlib
import json
from pathlib import Path
from dotenv import dotenv_values
from src.day6_bridge import ROOT
from src.experiment import save, sha


def check_bonus():
    """Validate saved runs and export source pointers without full IPCC pages."""
    cases = json.loads((ROOT / 'benchmark/bonus.json').read_text(encoding='utf-8'))
    lock = json.loads((ROOT / 'benchmark/bonus.lock.json').read_text(encoding='utf-8'))
    assert sha(ROOT / 'benchmark/bonus.json') == lock['sha256']
    assert len({q['id'] for q in cases}) == len(cases)
    for split, positive, negative in [('dev', 15, 3), ('test', 24, 6)]:
        qs = [q for q in cases if q['split'] == split]
        assert sum(q['answerable'] for q in qs) >= positive
        assert sum(not q['answerable'] for q in qs) >= negative
    for group, minimum in dict(table=6, image=5, chart=5, multihop=4, text=4).items():
        assert sum(q['split']=='test' and q['group']==group for q in cases) >= minimum
    selection = json.loads((ROOT / 'results/bonus/selection.json').read_text(encoding='utf-8'))
    assert selection['code_sha256'] == sha(ROOT / 'src/bonus.py'), 'Frozen bonus code changed'
    assert selection['benchmark_sha256'] == lock['sha256']
    local = ROOT / 'data/bonus/pages.json'
    pages = {p['page']: p['text'] for p in json.loads(local.read_text(encoding='utf-8'))['pages']} if local.exists() else {}

    def pointers(value):
        if isinstance(value, list):
            return [pointers(v) for v in value]
        if not isinstance(value, dict):
            return value
        result = {k: pointers(v) for k, v in value.items() if not (k=='text' and 'page' in value)}
        if 'page' in value and 'text' in value:
            content = value['text']
            start = pages.get(value['page'], '').find(content)
            result['text_ref'] = dict(sha256=hashlib.sha256(content.encode('utf-8')).hexdigest(),
                                    characters=len(content), extraction='pdfium_bounded' if 'bbox' in value else 'normalized_page_slice')
            if 'bbox' not in value:
                assert start >= 0, 'Cannot reconstruct retrieval context'
                result['text_ref'].update(char_start=start, char_end=start+len(content))
        return result

    checks = []
    for manifest_path in sorted((ROOT / 'results/bonus').glob('*/*/manifest.json')):
        folder = manifest_path.parent
        manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
        raw = folder / 'records.json'
        if raw.exists():
            records = json.loads(raw.read_text(encoding='utf-8'))
            digest = sha(raw)
            save(folder / 'trace.json', dict(source_records_sha256=digest,
                 context_policy='Original IPCC context stays local. Reconstruct search text from normalized PDF page char offsets, and read text/image from page+bbox using src.bonus.Index.image. Preserve model outputs and tool parameters unchanged.',
                 records=pointers(records)))
        else:
            exported = json.loads((folder / 'trace.json').read_text(encoding='utf-8'))
            records, digest = exported['records'], exported['source_records_sha256']
        assert {r['query_id'] for r in records} == set(manifest['query_ids'])
        assert len(records) == len(manifest['query_ids'])
        if manifest['split'] == 'test':
            for key in ['code_sha256', 'benchmark_sha256', 'source_sha256', 'model', 'preset']:
                assert manifest[key] == selection[key], f'Test selection differs: {key}'
        labels = json.loads((folder / 'reviews.json').read_text(encoding='utf-8'))
        assert {r['query_id'] for r in labels} == set(manifest['query_ids'])
        assert all(r['trace_sha256']==digest and type(r['passed']) is bool and r['reason'] for r in labels)
        summary = json.loads((folder / 'summary.json').read_text(encoding='utf-8'))
        assert summary['passed'] == sum(r['passed'] for r in labels)
        assert summary['total'] == len(records)
        assert summary['human_review_complete'] == all(r['review_status']=='human_confirmed' and r['original_pdf_checked'] for r in labels)
        for r in records:
            regions = {v['region_id']: v for v in r['regions']}
            for citation in r['citations']:
                region = regions[citation['region_id']]
                assert citation['page']==region['page'] and citation['bbox']==region['bbox']
            if r['status']=='answered':
                assert r['citations']
        checks.append(dict(run=str(folder.relative_to(ROOT)), cases=len(records),
                           passed=summary['passed'], review_status=summary['review_status']))
    setup = ROOT / 'results/bonus/dev/setup-errors.json'
    if setup.exists():
        save(setup.with_name('setup-errors.trace.json'), dict(source_records_sha256=sha(setup),
             data=pointers(json.loads(setup.read_text(encoding='utf-8')))))
    return checks


def main():
    questions = json.loads((ROOT / 'benchmark/questions.json').read_text(encoding='utf-8'))
    lock = json.loads((ROOT / 'benchmark/split_lock.json').read_text(encoding='utf-8'))
    assert sha(ROOT / 'benchmark/questions.json') == lock['benchmark_sha256'], 'Benchmark hash differs'
    selection = json.loads((ROOT / 'results/selection.json').read_text(encoding='utf-8'))
    for filename, digest in selection['runtime_code_sha256'].items():
        assert sha(ROOT / 'src' / filename) == digest, f'Frozen basic code changed: {filename}'
    assert len({q['id'] for q in questions}) == len(questions), 'Duplicate question IDs'
    for split, positive, negative in [('dev', 15, 2), ('test', 5, 2)]:
        qs = [q for q in questions if q['split'] == split]
        assert sum(q['answerable'] for q in qs) >= positive
        assert sum(not q['answerable'] for q in qs) >= negative
    checks = []
    for records_path in sorted((ROOT / 'results').glob('*/*/records.json')):
        records = json.loads(records_path.read_text(encoding='utf-8'))
        manifest = json.loads((records_path.parent / 'manifest.json').read_text(encoding='utf-8'))
        assert len({r['query_id'] for r in records}) == len(records), 'Duplicate result IDs'
        assert set(r['query_id'] for r in records) == set(manifest['query_ids']), f'Incomplete run: {records_path.parent}'
        for record in records:
            trace = record['agent']
            assert len(trace['context']) <= trace['config']['budget_chars'], 'Context exceeds budget'
            if trace['status'] == 'answered':
                assert trace['citations'] and set(trace['citations']) <= set(trace['context_ids'])
            assert record['query_id'] == trace['query_id']
        checks.append(dict(run=str(records_path.parent.relative_to(ROOT)), cases=len(records),
                           errors=sum(r['agent']['status'] == 'error' for r in records)))
    key = dotenv_values(ROOT / '.env').get('ANTHROPIC_API_KEY', '')
    leaked = []
    for folder in ['src', 'scripts', 'tests', 'docs', 'config', 'benchmark', 'results', 'report', 'data']:
        for path in (ROOT / folder).rglob('*'):
            if path.is_file() and path.suffix in ('.json', '.jsonl', '.md', '.py', '.txt'):
                if key and key.encode() in path.read_bytes():
                    leaked.append(str(path.relative_to(ROOT)))
    assert not leaked, f'API key found in artifact files: {leaked}'
    author_labels = []
    for name in ['baseline', 'hybrid']:
        path = ROOT / 'results/test' / name / 'reviews.json'
        if path.exists():
            author_labels.extend(json.loads(path.read_text(encoding='utf-8')))
    bonus_checks = check_bonus()
    result = dict(benchmark_lock='passed', split_counts='passed', trace_invariants='passed',
                  api_key_scan='passed (key value never printed)', runs=checks,
                  bonus_runs=bonus_checks,
                  author_case_reviews=sum(r.get('review_status') == 'human_confirmed' for r in author_labels),
                  human_review='Basic case-level grades are human-confirmed; citation booleans are derived conservatively. Bonus review status is reported per run; dev AI labels remain provisional. This check does not certify semantic correctness.')
    save(ROOT / 'results/submission_check.json', result)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
