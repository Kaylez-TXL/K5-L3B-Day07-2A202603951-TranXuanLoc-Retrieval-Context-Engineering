"""Export offline evidence and label sheets; never infer semantic grades from IDs."""
import argparse
import json
from pathlib import Path
from src.day6_bridge import ROOT
from src.experiment import save


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run', required=True, type=Path)
    args = parser.parse_args()
    records = json.loads((args.run / 'records.json').read_text(encoding='utf-8'))
    ids = {r['query_id'] for r in records}
    cases = {q['id']: q for q in json.loads((ROOT / 'benchmark/questions.json').read_text(encoding='utf-8')) if q['id'] in ids}
    chunks = {c['id']: c for c in json.loads((ROOT / 'data/day6/chunks.json').read_text(encoding='utf-8'))}
    labels, lines = [], ['# Phiếu kiểm tra câu trả lời và nguồn', '',
                         'Đối chiếu PDF gốc theo số trang. Nhãn phải do người chấm kiểm tra; không suy ra chất lượng chỉ từ citation ID.', '']
    for record in records:
        q, trace = cases[record['query_id']], record['agent']
        lines += [f'## {q["id"]}', '', f'**Câu hỏi:** {q["question"]}', '',
                  f'**Loại:** {"Có đáp án" if q["answerable"] else "Thiếu bằng chứng"}', '',
                  f'**Đáp án chuẩn / lý do thiếu:** {q.get("expected_answer", q.get("absence_reason"))}', '',
                  f'**Kết quả ({trace["status"]}):** {trace["answer"]}', '',
                  '**Gold (chỉ dùng chấm, không được gửi vào agent):**', '',
                  '```json', json.dumps(q.get('gold', []), ensure_ascii=False, indent=2), '```', '',
                  '**Context cuối:**', '', '```text', trace['context'], '```', '',
                  '**Nguồn citation:**', '']
        for cid in trace['citations']:
            c = chunks[cid]
            lines += [f'- `{cid}` — trang PDF {c["page"]}, ký tự {c["metadata"]["char_start"]}–{c["metadata"]["char_end"]}.']
        lines += ['', f'**Trace:** `records.json`, query_id `{q["id"]}`.', '']
        labels.append(dict(query_id=q['id'], answer_grade=None if q['answerable'] else None,
                           context_grade=None if q['answerable'] else None,
                           citation_support=[None for _ in trace['citations']],
                           abstention_correct=None, reason='', citation_reasons=['' for _ in trace['citations']],
                           reviewer='', review_status='pending'))
    (args.run / 'REVIEW.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    target = args.run / 'reviews.json'
    if not target.exists():
        save(target, labels)
    print(f'Exported {len(records)} cases for review; existing reviews.json was preserved')


if __name__ == '__main__':
    main()
