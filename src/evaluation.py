"""Evidence proxy metrics; gold is used after retrieval, never by the agent."""
import re


def normalized(text):
    return re.sub(r'\s+', ' ', text).strip()


def evidence_hit(chunk, gold):
    return any(chunk['source_id'] == g['source_id'] and chunk['page'] == g['page']
               and normalized(g['evidence']) in normalized(chunk['text']) for g in gold)


def context_has_evidence(chunks, gold):
    """Join only source-contiguous chunks using verified original offsets.

    Evidence alternatives use OR. This benchmark has single-excerpt questions;
    this function is not a general multi-hop evidence-group scorer.
    """
    for g in gold:
        relevant = sorted([c for c in chunks if c['source_id'] == g['source_id'] and c['page'] == g['page']],
                          key=lambda c: c['metadata']['char_start'])
        text, end = '', -1
        for c in relevant:
            start, stop = c['metadata']['char_start'], c['metadata']['char_end']
            if stop - start != len(c['text']):
                raise ValueError('Chunk offsets do not match text')
            if start > end:
                text = c['text']
            elif stop > end:
                text += c['text'][max(0, end-start):]
            end = max(end, stop)
            if normalized(g['evidence']) in normalized(text):
                return True
    return False


def ratio(n, total):
    return dict(n=n, N=total, rate=n/total if total else None)


def summarize(records):
    good = [r for r in records if r['agent']['status'] != 'error']
    answerable = [r for r in records if r['answerable']]
    unanswerable = [r for r in records if not r['answerable']]
    all_attempts = [attempt for r in records for attempt in r.get('previous_attempts', []) + [r]]
    calls = [call for r in all_attempts for call in r['agent']['model_calls']]
    return dict(cases=len(records), errors=len(records)-len(good),
                first_attempt_errors=sum((r.get('previous_attempts', []) or [r])[0]['agent']['status'] == 'error' for r in records),
                previous_attempt_errors=sum(sum(a['agent']['status'] == 'error' for a in r.get('previous_attempts', [])) for r in records),
                attempt_count=len(all_attempts),
                original_hit1=ratio(sum(bool(r.get('original_hit1')) for r in answerable), len(answerable)),
                original_hit3=ratio(sum(bool(r.get('original_hit3')) for r in answerable), len(answerable)),
                original_context_evidence=ratio(sum(bool(r.get('original_context_evidence')) for r in answerable), len(answerable)),
                agent_context_evidence=ratio(sum(r['agent']['status'] != 'error' and bool(r.get('agent_context_evidence')) for r in answerable), len(answerable)),
                tool_use=ratio(sum(any(e['event'] == 'search' for e in r['agent']['events']) for r in good), len(good)),
                false_abstention_status=ratio(sum(r['agent']['status'] == 'abstain' for r in answerable), len(answerable)),
                unanswerable_abstention_status=ratio(sum(r['agent']['status'] == 'abstain' for r in unanswerable), len(unanswerable)),
                # Status alone does not certify semantic correctness.
                decision_status_correct=sum((r['agent']['status'] == 'answered' if r['answerable'] else r['agent']['status'] == 'abstain') for r in records),
                search_call_distribution={str(n): sum(sum(e['event'] == 'search' for e in r['agent']['events']) == n for r in records)
                                          for n in sorted({sum(e['event'] == 'search' for e in r['agent']['events']) for r in records})},
                input_tokens=sum(c.get('usage', {}).get('input_tokens', 0) for c in calls),
                output_tokens=sum(c.get('usage', {}).get('output_tokens', 0) for c in calls),
                estimated_cost_usd=sum(r['agent']['cost_usd'] or 0 for r in all_attempts),
                agent_elapsed_ms=sum(r['agent']['elapsed_ms'] for r in records),
                elapsed_ms_including_retries=sum(r['agent']['elapsed_ms'] for r in all_attempts),
                metric_note='Evidence metrics are normalized exact-excerpt proxies; statuses are behavior proxies. Semantic grounding and citation support require separate review. Errors retained in evidence/status denominators and reported separately.')
