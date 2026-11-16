# Hướng dẫn chạy

## 1. Cài đặt

Cần Python 3.11+, repo Day 6 với model E5 đã tải và database pgvector đã ingest. Từ thư mục gốc Day 7:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-lock.txt
```

Tạo `.env` từ `.env.example` nếu chưa có. Điền `DAY6_PATH`, `DATABASE_URL`, `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`. Không ghi đè `.env` đã có key và không commit file này.

Bật Docker Desktop; chạy `docker compose -p day6_student_starter up -d --wait` từ `starter/` của Day 6 nếu database đang dừng. Day 7 chỉ đọc bảng `day6_chunks`, strategy A. Embedding dùng đúng E5 revision của Day 6; không tự thay model khi chạy.

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
.\.venv\Scripts\python.exe -m src.day6_bridge
.\.venv\Scripts\python.exe -m scripts.check_submission
```

## 2. Phần cơ bản

Chạy một câu hỏi mới, chọn output chưa tồn tại:

```powershell
.\.venv\Scripts\python.exe -m src.run --method hybrid --question 'Trong cấu trúc Au@Ag, lõi và vỏ làm từ kim loại nào?' --output results/my-run.json
```

Ba phương pháp là `tfidf`, `dense`, `hybrid`. Câu hỏi và context liên quan được gửi tới Anthropic; embedding và database chạy local.

Cấu hình thực nghiệm nằm trong `config/experiments.json`. Các lượt chạy và nhãn đã nộp nằm trong `results/dev/` và `results/test/`. Lệnh tái lập một cấu hình:

```powershell
.\.venv\Scripts\python.exe -m src.experiment --split dev --config baseline --output results/dev/baseline
```

Thay `baseline` bằng `lexical`, `hybrid` hoặc `dense_wide`. Output đã có chỉ tiếp tục câu chưa chạy. `--retry-errors` chỉ chạy lại câu lỗi và giữ các lần cũ; `--continue-on-error` hoàn tất split, giữ câu lỗi trong mẫu số. Dùng thư mục output khác nếu cần một lần chạy độc lập.

Chọn cấu hình bằng `python -m scripts.select_config` sau khi hoàn tất dev. Script từ chối ghi đè selection đã khóa. Test chỉ chấp nhận baseline và cấu hình đã chọn, với đúng hash benchmark, model, corpus, prompt và code. Không chỉnh bằng test rồi báo cùng test là độc lập.

Nhãn test ở `reviews.json`; tổng hợp bằng:

```powershell
.\.venv\Scripts\python.exe -m scripts.summarize_reviews --run results/test/hybrid --reviews results/test/hybrid/reviews.json --output results/test/hybrid/agent_metrics_confirmed.json
```

`REVIEW.md` giúp đối chiếu câu trả lời và nguồn. Điểm context/answer là 0–2. Nguồn hỗ trợ một phần không được tính là hỗ trợ đầy đủ trong chỉ số citation nhị phân. Nhãn nguồn phần cơ bản được chấm ở cấp câu hỏi, áp cho các ID cuối của câu đó.

## 3. Phần nâng cao

Nguồn: [IPCC, Climate Change 2023: Synthesis Report](https://www.ipcc.ch/report/sixth-assessment-report-cycle/2023/), [PDF](https://www.ipcc.ch/report/ar6/syr/downloads/report/IPCC_AR6_SYR_FullVolume.pdf). Có 186 trang PDF, gồm 184 trang đánh số. [Điều kiện sử dụng](https://www.ipcc.ch/copyright/): dùng cho học tập cá nhân, phi thương mại và ghi nguồn. Bản PDF và index toàn văn giữ local; repo cung cấp nguồn, cấu hình và lệnh tái tạo.

```powershell
.\.venv\Scripts\python.exe -m src.bonus prepare
.\.venv\Scripts\python.exe -m src.bonus run --split dev --preset compact
.\.venv\Scripts\python.exe -m src.bonus run --split dev --preset thorough
.\.venv\Scripts\python.exe -m src.bonus run --split dev --preset focused
```

`prepare` tải PDF khi chưa có, index toàn bộ trang bằng E5, lưu `data/bonus/pages.json` và `vectors.npz` local. Thông tin nguồn/index ở `data/bonus/manifest.json`. Mỗi trang đều có thể render để đọc hình; không dùng vùng gold khi truy xuất.

Benchmark nâng cao gồm 18 dev và 30 test, ở `benchmark/bonus.json`, khóa bằng `bonus.lock.json`. Compact dùng top-6, tối đa 3 vùng ảnh, 7 lượt model, cạnh ảnh 1200 px. Thorough dùng top-10, 6 vùng ảnh, 10 lượt model, cạnh ảnh 1560 px; ưu tiên trang có chú thích Figure/Table khớp nhãn trong query và cho tối đa 2 lần thử lại lỗi mạng mỗi câu. Focused giữ truy xuất như thorough nhưng yêu cầu trả lời ngắn bằng tiếng Anh, đúng các ý được hỏi. Đây là thay đổi tổng hợp, không tách riêng tác động từng biến.

Agent dùng search, read và finish. Bbox là [x0,y0,x1,y1] chuẩn hóa theo góc trên trái. Citation lưu trang PDF, bbox và vị trí bảng/hình. Ảnh không lưu base64 trong trace; có thể tái tạo từ PDF và bbox. Các request lỗi đều được ghi; số lỗi trong summary là số câu kết thúc bằng lỗi, không phải số request lỗi đã phục hồi.

`records.json` của bonus chứa context gốc nên giữ local và được Git bỏ qua. `python -m scripts.check_submission` xuất `trace.json` để nộp: giữ nguyên câu hỏi, ranking, tool call, đầu ra model, citation, usage, lỗi và thời gian; thay text nguồn bằng hash và tham chiếu. Với search, lấy lát cắt `[char_start:char_end]` từ text trang đã chuẩn hóa trong `data/bonus/pages.json`. Với read, dùng `Index.image(page, bbox, edge)` trong `src/bonus.py` để tái tạo text và ảnh, kiểm tra hash. `source_records_sha256` liên kết trace công khai với file local mà nhãn đánh giá đã chấm. Nếu chỉ tải repo, có thể đọc trace và nhãn; để chạy lại các lệnh chấm cần có lượt chạy local tương ứng. Lỗi schema lúc thiết lập được giữ trong `results/bonus/dev/setup-errors.trace.json`.

Tạo phiếu và chấm từng câu dev trước khi chọn:

```powershell
.\.venv\Scripts\python.exe -m src.bonus review --split dev --preset compact
.\.venv\Scripts\python.exe -m src.bonus score --split dev --preset compact
.\.venv\Scripts\python.exe -m src.bonus select
```

Làm tương tự cho thorough và focused. `score` yêu cầu nhãn và lý do đầy đủ. `select` ưu tiên số câu dev đạt, rồi số lỗi và chi phí; từ chối thay selection đã khóa. Chạy test bằng preset đã chọn:

```powershell
.\.venv\Scripts\python.exe -m src.bonus run --split test --preset focused
.\.venv\Scripts\python.exe -m src.bonus review --split test --preset focused
.\.venv\Scripts\python.exe -m src.bonus score --split test --preset focused
```

Đổi preset tương ứng với `results/bonus/selection.json` nếu chọn cấu hình khác. Mọi câu test đều tính vào mẫu số; câu kết thúc bằng lỗi/timeout là không đạt. Câu có đáp án chỉ đạt khi đúng đủ, giữ đơn vị/điều kiện/phép tính và có nguồn hỗ trợ. Nhãn AI phải ghi `ai_provisional`; chỉ ghi `human_confirmed` và `original_pdf_checked=true` sau khi sinh viên thực sự đối chiếu PDF. Không kết luận đạt bonus khi chưa đủ điều kiện của `ADVANCED.md`.

Kết quả đã lưu: focused test 28/30 (93,33%), được Trần Xuân Lộc xác nhận toàn bộ nhãn test; nhãn dev vẫn là AI sơ bộ. Phiếu đối chiếu nằm ở `results/bonus/test/focused/REVIEW.md`; mọi nhãn có lý do trong `reviews.json`. Sau khi kiểm tra từng câu với PDF, ghi người chấm, sửa nhãn nếu cần, đổi trạng thái của câu đã kiểm tra rồi chạy lại `score`. Không chạy `review` lại nếu muốn giữ phần nhận xét chấm sơ bộ đã bổ sung vào phiếu.

## 4. Kết quả và chi phí

Trace lưu query, ranking, model/tool call, context hoặc vùng ảnh, câu trả lời, citation, lỗi, usage và thời gian. Gold chỉ dùng trong bước đánh giá. Giá API được ước tính từ usage theo [Anthropic](https://platform.claude.com/docs/en/about-claude/pricing), không gồm máy local, thuế hoặc request lỗi không trả usage. Model thật và test code/mock được báo riêng.
