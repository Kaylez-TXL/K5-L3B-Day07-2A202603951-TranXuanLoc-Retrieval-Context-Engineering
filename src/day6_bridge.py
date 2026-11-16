"""Read-only connection to the original Day 6 pgvector index."""
import json
import os
from pathlib import Path

from scripts.prepare_day6 import load_day6

ROOT = Path(__file__).resolve().parents[1]


class Day6Retriever:
    def __init__(self, day6_path, database_url, *, offline=True):
        load_day6(Path(day6_path))
        from day6_source.embeddings import MyEmbedder
        from day6_source.store import PgVectorStore
        self.embedder = MyEmbedder(local_files_only=offline)
        self.store = PgVectorStore(database_url, self.embedder.dimensions)
        # No schema creation, ingestion, update or delete is allowed here.
        self.store.connection.execute('SET default_transaction_read_only = on')

    def search(self, query, *, filters=None, top_k=3):
        rows = self.store.search('A', self.embedder.embed_query(query), top_k=top_k, filters=filters)
        return [dict(id=r['chunk_id'], source_id=r['document_id'], source=r['source'],
                     page=r['page'], text=r['text'], metadata=r['metadata'],
                     score=r['score'], strategy='dense') for r in rows]

    def verify_snapshot(self):
        expected = json.loads((ROOT / 'data/day6/chunks.json').read_text(encoding='utf-8'))
        with self.store.connection.cursor() as cur:
            cur.execute("SELECT chunk_id, document_id, source, page, text, metadata FROM day6_chunks WHERE strategy=%s ORDER BY chunk_id", ('A',))
            actual = [dict(zip(('id', 'source_id', 'source', 'page', 'text', 'metadata'), row)) for row in cur.fetchall()]
        if actual != sorted(expected, key=lambda c: c['id']):
            raise ValueError('Day 6 database A differs from reproduced chunks; investigate before benchmarking.')
        return dict(chunks=len(actual), exact_database_match=True)

    def close(self):
        self.store.close()


def main():
    from dotenv import load_dotenv
    load_dotenv(ROOT / '.env', override=False)
    provenance = json.loads((ROOT / 'data/day6/provenance.json').read_text(encoding='utf-8'))
    retriever = Day6Retriever(os.environ.get('DAY6_PATH', provenance['day6_path']),
                             os.environ['DATABASE_URL'])
    try:
        report = retriever.verify_snapshot()
        # Generic smoke query, independent of benchmark/test gold.
        hits = retriever.search('Hạt nano Au@Ag gồm những kim loại nào?', top_k=3)
        report.update(model=retriever.embedder.model_name, revision=retriever.embedder.revision,
                      dimensions=retriever.embedder.dimensions, smoke_query_hits=len(hits),
                      smoke_results=[dict(id=c['id'], page=c['page'], score=c['score']) for c in hits])
        output = ROOT / 'results/checkpoint1/connection.json'
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        print(json.dumps(report, ensure_ascii=False))
    finally:
        retriever.close()


if __name__ == '__main__':
    main()
