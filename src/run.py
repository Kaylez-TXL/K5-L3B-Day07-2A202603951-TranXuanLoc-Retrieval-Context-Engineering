"""Run one real agent question; smoke runs do not read benchmark gold."""
import argparse
import json
import os
from pathlib import Path
from dotenv import load_dotenv
from src.agent import run_agent
from src.anthropic_api import AnthropicClient
from src.day6_bridge import Day6Retriever, ROOT
from src.retrieval import LexicalRetriever, HybridRetriever


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--question', required=True)
    parser.add_argument('--method', choices=['tfidf', 'dense', 'hybrid'], default='dense')
    parser.add_argument('--top-k', type=int, default=3)
    parser.add_argument('--budget', type=int, default=2400, help='Context characters, including source headers')
    parser.add_argument('--max-searches', type=int, default=3)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    if args.output.exists():
        parser.error('Output exists; choose another path to preserve trace')
    load_dotenv(ROOT / '.env')
    model = os.environ.get('ANTHROPIC_MODEL', '').strip()
    if not model:
        parser.error('Set ANTHROPIC_MODEL in .env')
    client = AnthropicClient()
    if model not in {m['id'] for m in client.models()}:
        parser.error('Configured model is not in the account model list')
    chunks = json.loads((ROOT / 'data/day6/chunks.json').read_text(encoding='utf-8'))
    lexical = LexicalRetriever(chunks)
    dense = None
    try:
        if args.method != 'tfidf':
            provenance = json.loads((ROOT / 'data/day6/provenance.json').read_text(encoding='utf-8'))
            dense = Day6Retriever(os.environ.get('DAY6_PATH', provenance['day6_path']), os.environ['DATABASE_URL'])
            dense.verify_snapshot()
        retriever = {'tfidf': lexical, 'dense': dense, 'hybrid': HybridRetriever(dense, lexical)}[args.method]
        trace = run_agent(args.question, client, retriever, model=model, top_k=args.top_k,
                          budget=args.budget, max_searches=args.max_searches)
        trace.update(method=args.method, run_kind='single_question')
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(trace, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        print(json.dumps({k: trace[k] for k in ('status', 'answer', 'citations', 'usage', 'elapsed_ms')}, ensure_ascii=False, indent=2))
        if trace['status'] == 'error':
            print(json.dumps(trace['error']))
            raise SystemExit(1)
    finally:
        if dense is not None:
            dense.close()


if __name__ == '__main__':
    main()
