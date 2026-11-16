"""Create and freeze Day 7 benchmark before retrieval experiments."""
import argparse
import hashlib
import json
import re
from pathlib import Path
from scripts.prepare_day6 import ROOT, write_json


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--day6', required=True, type=Path)
    args = parser.parse_args()
    target = ROOT / 'benchmark/questions.json'
    lock_path = ROOT / 'benchmark/split_lock.json'
    if target.exists() or lock_path.exists():
        raise FileExistsError('Benchmark already exists. Do not silently replace a frozen split.')
    pages = {p['page']: p['text'] for p in map(json.loads, (args.day6 / 'data/processed/pages.jsonl').read_text(encoding='utf-8').splitlines())}
    cases = json.loads((ROOT / 'benchmark/dev_answerable.json').read_text(encoding='utf-8'))
    definitions = [
        ('t01', 23, 'Theo mức độ giới hạn không gian, tài liệu chia plasmon thành ba loại nào?',
         'Plasmon khối, plasmon bề mặt và plasmon bề mặt cục bộ.',
         'Dựa trên mức độ giới hạn không gian, plasmon có thể được chia thành plasmon khối , plasmon bề mặt, và plasmon bề mặt cục bộ.'),
        ('t02', 23, 'Điều kiện chuẩn Lorentz có tác dụng gì đối với các phương trình cho thế vectơ và thế vô hướng?',
         'Giúp tách rời các biến thành các phương trình sóng độc lập cho A và Φ, vẫn tương đương hệ Maxwell ban đầu.',
         'Việc áp dụng điều kiện chuẩn Lorentz giúp tách r ời các biến, dẫn đến hệ phương trình sóng hoàn toàn đ ộc lập cho 𝐴 và Φ nhưng vẫn tương đương v ới hệ phương trình Maxwell ban đ ầu.'),
        ('t03', 24, 'Điều kiện về tần số nào làm xuất hiện cộng hưởng LSPR?',
         'Tần số ánh sáng tới trùng tần số dao động tự nhiên của đám mây electron.',
         'Khi tần số của ánh sáng t ới trùng khớp với tần số dao động tự nhiên của đám mây electron, hi ện tượng cộng hưởng LSPR diễn ra.'),
        ('t04', 29, 'Trong khuôn khổ BEM mô tả ở đồ án, hàm điện môi của mỗi hạt nano được giả định có hai tính chất nào?',
         'Cục bộ và đẳng hướng.',
         'mỗi hạt nano được đặc trưng bởi hàm điện môi cục bộ và đẳng hướng'),
        ('t05', 32, 'Vì sao bộ giải BEM đầy đủ chậm hơn bộ giải tựa tĩnh xét theo cấu trúc ma trận?',
         'Phải thiết lập và nghịch đảo ma trận phức đặc kích thước tỷ lệ N × N khi bề mặt có N phần tử.',
         'giả sử bề mặt hạt được chia lưới thành 𝑁 phần tử, bộ giải đầy đủ cần phải thiết lập và thực hiện các phép nghịch đảo cho các ma trận phức đặc có kích thước tỷ lệ thuận với 𝑁 × 𝑁'),
    ]
    for cid, page, question, answer, excerpt in definitions:
        match = re.search(r'\s+'.join(re.escape(w) for w in excerpt.split()), pages[page])
        if match is None:
            raise ValueError(f'Evidence absent on page {page}: {cid}')
        cases.append(dict(id='day7-' + cid, split='test', answerable=True, question=question,
                          expected_answer=answer, gold=[dict(source_id='auag-thesis-2026', page=page, evidence=match.group())],
                          provenance='New Day 7 question; not a paraphrase of Day 6 benchmark'))
    missing = [
        ('u01', 'dev', 'Quy trình tổng hợp hóa học Au@Ag trong đồ án giữ phản ứng ở nhiệt độ bao nhiêu độ C và trong bao nhiêu phút?',
         ['nhiệt độ', 'hóa chất'], 'Corpus describes numerical simulation; no experimental synthesis temperature/time protocol was found.'),
        ('u02', 'dev', 'Bộ dữ liệu mô phỏng của đồ án được công bố với mã DOI chính xác nào?',
         ['doi'], 'No dataset DOI found in the indexed main text.'),
        ('u03', 'test', 'Cảm biến Au@Ag của đồ án có giới hạn phát hiện glucose trong thử nghiệm lâm sàng là bao nhiêu mmol/L?',
         ['glucose', 'mmol'], 'No glucose clinical experiment or corresponding detection limit found.'),
        ('u04', 'test', 'Mã nguồn mô hình học máy của đồ án được phát hành tại URL GitHub nào và commit hash nào?',
         ['github', 'commit'], 'No published GitHub repository URL or commit identifier found.'),
    ]
    corpus = '\n'.join(pages.values()).casefold()
    for cid, split, question, terms, reason in missing:
        cases.append(dict(id='day7-' + cid, split=split, question=question, answerable=False,
                          expected_behavior='search_and_abstain', absence_reason=reason,
                          absence_check=dict(scope='All 54 indexed extracted pages, PDF pages 12–65',
                                             term_counts={term: corpus.count(term) for term in terms},
                                             limitation='Text-only inspection; original PDF/figures still require author review.')))
    for case in cases:
        case['review_status'] = 'AI-prepared; author source review pending'
    write_json(target, cases)
    write_json(lock_path, dict(benchmark_sha256=hashlib.sha256(target.read_bytes()).hexdigest(),
                               dev_ids=[c['id'] for c in cases if c['split'] == 'dev'],
                               test_ids=[c['id'] for c in cases if c['split'] == 'test'],
                               frozen_before_day7_retrieval=True,
                               author_review='pending; no claim of human verification',
                               policy='Tune on dev only. Changes after test inspection require a new held-out test.'))
    print('Created 17 dev and 7 test cases; source review pending. No benchmark retrieval was run.')


if __name__ == '__main__':
    main()
