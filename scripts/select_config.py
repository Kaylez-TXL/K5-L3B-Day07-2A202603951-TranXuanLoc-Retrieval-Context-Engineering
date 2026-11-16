"""Freeze the best eligible dev configuration using the predeclared rule."""
from datetime import datetime, timezone
import json
from src.day6_bridge import ROOT
from src.experiment import save, sha


def main():
    output = ROOT / 'results/selection.json'
    if output.exists():
        raise FileExistsError('Selection already frozen; do not replace after inspecting test')
    configs = json.loads((ROOT / 'config/experiments.json').read_text(encoding='utf-8'))
    rows, manifests, ineligible = {}, {}, {}
    for name in configs:
        folder = ROOT / 'results/dev' / name
        m = json.loads((folder / 'manifest.json').read_text(encoding='utf-8'))
        s = json.loads((folder / 'summary.json').read_text(encoding='utf-8'))
        if s['cases'] != len(m['query_ids']):
            raise ValueError(f'{name}: dev run incomplete')
        if s['errors']:
            ineligible[name] = 'Final run contains provider/runtime errors'
        if m['experiments_sha256'] != sha(ROOT / 'config/experiments.json'):
            raise ValueError('Configuration file changed during experiments')
        rows[name], manifests[name] = s, m
    reference = manifests['baseline']
    for m in manifests.values():
        for key in ('benchmark_sha256', 'corpus_sha256', 'prompt_sha256', 'selection_rule_sha256', 'model', 'query_ids'):
            if m[key] != reference[key]:
                raise ValueError(f'Incomparable dev runs: {key}')
    ranking = sorted((name for name in rows if name not in ineligible), key=lambda name: (-rows[name]['agent_context_evidence']['n'],
                                            -rows[name]['decision_status_correct'],
                                            -rows[name]['original_hit3']['n'],
                                            rows[name]['estimated_cost_usd'], rows[name]['agent_elapsed_ms'], name))
    if not ranking:
        raise ValueError('No eligible configuration')
    save(output, dict(selected_config=ranking[0], ranking=ranking, ineligible=ineligible,
                      selected_at=datetime.now(timezone.utc).isoformat(), selected_before_test=True,
                      benchmark_sha256=reference['benchmark_sha256'], corpus_sha256=reference['corpus_sha256'],
                      prompt_sha256=reference['prompt_sha256'], model=reference['model'],
                      experiments_sha256=sha(ROOT / 'config/experiments.json'),
                      runtime_code_sha256={name: sha(ROOT / 'src' / name) for name in ['agent.py', 'retrieval.py', 'day6_bridge.py', 'anthropic_api.py', 'pricing.py']},
                      rule=json.loads((ROOT / 'config/selection_rule.json').read_text(encoding='utf-8')),
                      dev_summaries=rows))
    print('Selected on dev, frozen before test:', ranking[0])


if __name__ == '__main__':
    main()
