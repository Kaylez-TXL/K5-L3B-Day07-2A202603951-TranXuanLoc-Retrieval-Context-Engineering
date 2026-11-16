"""Reproducible dev/test runs with immutable metadata and per-case checkpoints."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import time
from dotenv import load_dotenv
from starter.baseline import pack_context
from src.agent import run_agent, SYSTEM, SEARCH, FINISH
from src.anthropic_api import AnthropicClient
from src.day6_bridge import Day6Retriever, ROOT
from src.evaluation import evidence_hit, context_has_evidence, summarize
from src.retrieval import LexicalRetriever, HybridRetriever


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(path, data):
    # Replace one small local result file atomically, never discard completed cases.
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    temporary.replace(path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--split', choices=['dev', 'test'], required=True)
    parser.add_argument('--config', required=True)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--retry-errors', action='store_true', help='Retry failed cases only; preserve original error records under previous_attempts')
    parser.add_argument('--continue-on-error', action='store_true', help='Complete the planned split, retaining error cases in the denominator')
    args = parser.parse_args()
    configurations = json.loads((ROOT / 'config/experiments.json').read_text(encoding='utf-8'))
    if args.config not in configurations:
        parser.error('Unknown configuration')
    config = configurations[args.config]
    lock = json.loads((ROOT / 'benchmark/split_lock.json').read_text(encoding='utf-8'))
    benchmark_path = ROOT / 'benchmark/questions.json'
    if sha(benchmark_path) != lock['benchmark_sha256']:
        parser.error('Benchmark changed after split lock')
    if args.split == 'test':
        selection = json.loads((ROOT / 'results/selection.json').read_text(encoding='utf-8'))
        if args.config not in ('baseline', selection['selected_config']) or selection['benchmark_sha256'] != sha(benchmark_path):
            parser.error('Test requires a matching frozen dev selection and baseline/selected config')
        if selection['experiments_sha256'] != sha(ROOT / 'config/experiments.json'):
            parser.error('Configurations changed after selection')
        for name, digest in selection['runtime_code_sha256'].items():
            if sha(ROOT / 'src' / name) != digest:
                parser.error(f'Runtime code changed after selection: {name}')
    # Filter before inspecting evidence. Only selected split is passed to scoring.
    questions = [q for q in json.loads(benchmark_path.read_text(encoding='utf-8')) if q['split'] == args.split]
    chunks = json.loads((ROOT / 'data/day6/chunks.json').read_text(encoding='utf-8'))
    by_id = {c['id']: c for c in chunks}
    prompt_hash = hashlib.sha256(json.dumps([SYSTEM, SEARCH, FINISH], ensure_ascii=False, sort_keys=True).encode()).hexdigest()
    load_dotenv(ROOT / '.env')
    model = os.environ['ANTHROPIC_MODEL']
    if args.split == 'test':
        for key, value in [('model', model), ('prompt_sha256', prompt_hash),
                           ('corpus_sha256', sha(ROOT / 'data/day6/chunks.json'))]:
            if selection[key] != value:
                parser.error(f'{key} changed after selection; independent test is not valid')
    client = AnthropicClient()
    if not model.strip():
        parser.error('ANTHROPIC_MODEL is empty')
    # Model availability was checked during setup. Messages API validates it;
    # do not add an unrelated Models API dependency to every resumed batch.
    manifest = dict(split=args.split, name=args.config, config=config, model=model,
                    benchmark_sha256=sha(benchmark_path), corpus_sha256=sha(ROOT / 'data/day6/chunks.json'),
                    prompt_sha256=prompt_hash, selection_rule_sha256=sha(ROOT / 'config/selection_rule.json'),
                    experiments_sha256=sha(ROOT / 'config/experiments.json'),
                    query_ids=[q['id'] for q in questions])
    args.output.mkdir(parents=True, exist_ok=True)
    manifest_path = args.output / 'manifest.json'
    if manifest_path.exists():
        old = json.loads(manifest_path.read_text(encoding='utf-8'))
        if any(old.get(k) != v for k, v in manifest.items()):
            parser.error('Cannot resume: run metadata changed')
    else:
        save(manifest_path, {**manifest, 'started_at': datetime.now(timezone.utc).isoformat()})
    records_path = args.output / 'records.json'
    records = json.loads(records_path.read_text(encoding='utf-8')) if records_path.exists() else []
    previous = {r['query_id']: r for r in records if r['agent']['status'] == 'error'} if args.retry_errors else {}
    done = {r['query_id'] for r in records if r['query_id'] not in previous}
    lexical = LexicalRetriever(chunks)
    dense = None
    try:
        if config['method'] != 'tfidf':
            provenance = json.loads((ROOT / 'data/day6/provenance.json').read_text(encoding='utf-8'))
            dense = Day6Retriever(os.environ.get('DAY6_PATH', provenance['day6_path']), os.environ['DATABASE_URL'])
            dense.verify_snapshot()
        retriever = {'tfidf': lexical, 'dense': dense, 'hybrid': HybridRetriever(dense, lexical)}[config['method']]
        for q in questions:
            if q['id'] in done:
                continue
            # Only public question/filter enter retrieval and model. Gold is scored afterwards.
            filters = q.get('filter') or None
            started = time.perf_counter()
            ranking = retriever.search(q['question'], filters=filters, top_k=max(3, config['top_k']))
            original_ms = (time.perf_counter() - started) * 1000
            context, ids = pack_context(ranking[:config['top_k']], budget=config['budget'])
            original_components = getattr(retriever, 'last_components', {}).copy()
            agent = run_agent(q['question'], client, retriever, model=model, filters=filters,
                              top_k=config['top_k'], budget=config['budget'], max_searches=config['max_searches'])
            agent['query_id'] = q['id']
            record = dict(query_id=q['id'], split=args.split, answerable=q['answerable'],
                          original_query=q['question'], filter=filters,
                          filter_provenance='Explicit chapter requested in original user question; reused Day 6 annotation, never inferred from gold',
                          original_ranking=ranking, original_components=original_components,
                          original_context=context, original_context_ids=ids, original_elapsed_ms=original_ms, agent=agent)
            if q['answerable']:
                gold = q['gold']
                record.update(original_hit1=bool(ranking and evidence_hit(ranking[0], gold)),
                              original_hit3=any(evidence_hit(c, gold) for c in ranking[:3]),
                              original_context_evidence=context_has_evidence([by_id[i] for i in ids], gold),
                              agent_context_evidence=agent['status'] != 'error' and context_has_evidence([by_id[i] for i in agent['context_ids']], gold))
            if q['id'] in previous:
                old = previous[q['id']]
                record['previous_attempts'] = old.get('previous_attempts', []) + [{k: v for k, v in old.items() if k != 'previous_attempts'}]
                records = [r for r in records if r['query_id'] != q['id']]
            records.append(record)
            save(records_path, records)
            save(args.output / 'summary.json', summarize(records))
            print(f'{args.config}/{args.split} {len(records)}/{len(questions)} {q["id"]}: {agent["status"]}', flush=True)
            if agent['status'] == 'error':
                # Stop billing further calls after an error; preserve partial results.
                print(json.dumps(agent['error']), flush=True)
                if not args.continue_on_error:
                    raise SystemExit(1)
        print(json.dumps(summarize(records), ensure_ascii=False), flush=True)
    finally:
        if dense:
            dense.close()


if __name__ == '__main__':
    main()
