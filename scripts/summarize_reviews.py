"""Aggregate explicitly supplied labels while preserving their review provenance."""
import argparse
import json
from pathlib import Path
from starter.agent_metrics import aggregate
from src.day6_bridge import ROOT
from src.experiment import save, sha


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run', required=True, type=Path)
    parser.add_argument('--reviews', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    records = json.loads((args.run / 'records.json').read_text(encoding='utf-8'))
    labels = json.loads(args.reviews.read_text(encoding='utf-8'))
    ids = {r['query_id'] for r in records}
    cases = [q for q in json.loads((ROOT / 'benchmark/questions.json').read_text(encoding='utf-8')) if q['id'] in ids]
    if {r['query_id'] for r in labels} != ids:
        raise ValueError('One review per case is required')
    by_id = {r['query_id']: r for r in labels}
    for case in cases:
        label = by_id[case['id']]
        if label.get('trace_sha256') and label['trace_sha256'] != sha(args.run / 'records.json'):
            raise ValueError('Review refers to a different trace file')
        if not label.get('reason') or not label.get('reviewer') or label.get('review_status') not in ('ai_provisional', 'human_confirmed'):
            raise ValueError('Reviewer, provenance and reason are required; do not aggregate blank labels')
        if case['answerable'] and label.get('context_grade') not in (0, 1, 2):
            raise ValueError('Answerable case requires context grade 0/1/2')
        if len(label.get('citation_reasons', [])) != len(label.get('citation_support', [])) or any(not reason for reason in label.get('citation_reasons', [])):
            raise ValueError('Every citation label requires its own reason')
    traces = [r['agent'] for r in records]
    summary = aggregate(cases, traces, labels)
    grades = [by_id[q['id']]['context_grade'] for q in cases if q['answerable']]
    summary.update(context_grades={str(i): grades.count(i) for i in (0, 1, 2)},
                   context_mean=sum(grades)/len(grades) if grades else None,
                   review_provenance={status: sum(r['review_status'] == status for r in labels) for status in ['ai_provisional', 'human_confirmed']},
                   label_source=str(args.reviews),
                   citation_label_origins=sorted({r.get('citation_label_origin', 'Explicit per-citation AI draft') for r in labels}),
                   warning=('Contains AI-provisional labels, not author confirmation.' if any(r['review_status'] == 'ai_provisional' for r in labels)
                            else 'Author case-level grades recorded from chat. Citation booleans derived from the supplied source-support assessment; partial support is not counted as fully valid.'))
    save(args.output, summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
