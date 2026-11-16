# Báo cáo Day 7 — Agentic RAG

**Họ tên:** Trần Xuân Lộc · **MSSV:** 2A202603951 · **Lớp:** L3B

## 1. Dữ liệu và cách làm

Em sử dụng lại đồ án Au@Ag của em và dữ liệu Day 6: 54 trang nội dung trong PDF 70 trang, chia thành 237 đoạn, mỗi đoạn tối đa 500 ký tự và chồng lấp 50 ký tự. Em dùng embedding `intfloat/multilingual-e5-small`, 384 chiều, chuẩn hóa L2; dữ liệu lưu trong PostgreSQL/pgvector. Model, phiên bản và nguồn được ghi trong [provenance](../../data/day6/provenance.json).

Agent sử dụng Anthropic `claude-haiku-5-5` để chọn câu truy vấn và quyết định trả lời hay tìm tiếp. Em so sánh dense retrieval, TF-IDF và hybrid RRF. RRF kết hợp thứ hạng của 10 kết quả từ mỗi phương pháp, với hằng số 60. Context được loại trùng, giữ nguồn và giới hạn theo ký tự. Agent trả lời kèm citation hoặc từ chối khi thiếu bằng chứng. Chương trình chỉ kiểm tra ID citation; việc nguồn có hỗ trợ câu trả lời được chấm riêng.

Bộ câu hỏi có 24 câu: dev gồm 15 câu có đáp án và 2 câu thiếu bằng chứng; test gồm 5 câu có đáp án và 2 câu thiếu bằng chứng. Em dùng dev để chọn cấu hình rồi khóa trước test. Gold chỉ dùng để chấm, không đưa vào agent. Các câu yêu cầu chương được áp cùng filter ở mọi phương pháp. [Benchmark](../../benchmark/questions.json) và [cấu hình đã chọn](../../results/selection.json) được lưu để kiểm tra lại.

## 2. Thực nghiệm và lựa chọn

Em thử hybrid với context lớn hơn để giảm việc bỏ sót bằng chứng. Cấu hình dense mở rộng tăng top-k và số lượt tìm để kiểm tra khả năng tìm lại. Các thay đổi này được thử cùng nhau nên chưa tách được tác động riêng của từng tham số.

| Cấu hình | top-k / context ký tự / search tối đa | Tập | Hit@1 | Hit@3 | Context đủ gold | Thời gian, gồm retry (s) | API USD ước tính |
|---|---|---|---|---|---|---|---|
| Dense baseline | 3 / 800 / 1 | dev | 12/15 (80%) | 14/15 (93,33%) | 8/15 (53,33%) | 66,12 | 0,007557 |
| TF-IDF | 3 / 800 / 1 | dev | 12/15 (80%) | 13/15 (86,67%) | 10/15 (66,67%) | 137,37 | 0,008318 |
| Hybrid RRF | 3 / 2400 / 3 | dev | 13/15 (86,67%) | 14/15 (93,33%) | 15/15 (100%) | 172,19 | 0,011436 |
| Dense mở rộng | 5 / 3600 / 3 | dev | 12/15 (80%) | 14/15 (93,33%) | 9/15 (60%) | 311,23 | 0,009869 |
| Dense baseline | 3 / 800 / 1 | test | 2/5 (40%) | 4/5 (80%) | 1/5 (20%) | 28,71 | 0,003326 |
| Hybrid RRF | 3 / 2400 / 3 | test | 2/5 (40%) | 4/5 (80%) | 4/5 (80%) | 32,87 | 0,005466 |

Hit@1/3 kiểm tra đoạn gold đúng nguồn và trang sau chuẩn hóa khoảng trắng. Context đủ gold xét các đoạn thực sự gửi model, cho phép ghép các đoạn liên tục. Mẫu số chỉ gồm câu có đáp án. Đây là phép đo tự động, có thể bỏ sót bằng chứng tương đương về ý nghĩa.

Em chọn hybrid theo số câu đủ gold trong context trên dev; các tiêu chí tiếp theo là hành vi trả lời/từ chối, Hit@3, chi phí và thời gian. Dense mở rộng có 7 câu lỗi nên không được chọn. TF-IDF có 4 lượt lỗi và hybrid có 2 lượt lỗi trước khi chạy lại thành công; mọi lần lỗi đều được giữ trong trace. Hai lượt test không có lỗi hệ thống và không chạy lại.

## 3. Đánh giá câu trả lời trên test

Em chấm câu trả lời và context theo mức 0/1/2. Nguồn hỗ trợ một phần không được tính là hỗ trợ đầy đủ trong chỉ số citation. Đánh giá nguồn được ghi ở cấp câu hỏi rồi áp cho các ID citation cuối của câu đó; đây là giới hạn của cách chấm.

| Chỉ số | Baseline | Hybrid |
|---|---|---|
| Câu trả lời: số câu mức 0/1/2 | 3 / 1 / 1 | 1 / 1 / 3 |
| Điểm câu trả lời trung bình /2 | 0,60 | 1,40 |
| Context: số câu mức 0/1/2 | 3 / 1 / 1 | 0 / 2 / 3 |
| Điểm context trung bình /2 | 0,60 | 1,60 |
| Citation hỗ trợ đầy đủ | 1/3 | 4/6 |
| Câu trả lời có citation | 3/3 | 4/4 |
| Từ chối đúng câu thiếu bằng chứng | 2/2 | 2/2 |
| Từ chối nhầm câu có đáp án | 2/5 (40%) | 1/5 (20%) |
| Có gọi retrieval tool | 7/7 | 7/7 |

Baseline dùng một lượt search cho mỗi câu test. Hybrid dùng một lượt ở 5 câu và ba lượt ở 2 câu. Ví dụ, hybrid trả đúng hai giả định “cục bộ và đẳng hướng” ở t04; cả hai cấu hình từ chối u03 về giới hạn phát hiện glucose lâm sàng. Ở t05, hybrid tìm được đoạn liên quan ma trận nhưng đầu ra cuối vẫn từ chối do citation không khớp.

Nhãn, lý do và nguồn từng câu nằm trong [phiếu baseline](../../results/test/baseline/REVIEW.md), [phiếu hybrid](../../results/test/hybrid/REVIEW.md) và `reviews.json` bên cạnh. Kết quả gọi model/tool đầy đủ nằm trong `records.json` của từng lượt chạy.

## 4. Phân tích lỗi và giới hạn

Hai lỗi dev chính là q05 và q08. Ở q05, baseline tìm thấy gold trong top-3 nhưng context 800 ký tự chỉ giữ đoạn khác, khiến agent từ chối; hybrid giữ được bằng chứng và trả lời. Ở q08, query gốc tìm đúng nhưng query model viết lại làm kết quả lệch chủ đề; hybrid tìm được bằng chứng phù hợp hơn.

Hybrid cải thiện context và điểm trả lời nhưng vẫn có câu trả lời lệch trọng tâm hoặc bị từ chối do định dạng citation. Trích xuất văn bản có thể mất dấu trong công thức. Chỉ có 7 câu test trên cùng một tài liệu nên em chưa thể khái quát kết quả cho tài liệu khác. Em không chỉnh pipeline theo lỗi test.

Chi phí trong bảng được ước tính từ token theo [bảng giá Anthropic](https://platform.claude.com/docs/en/about-claude/pricing), không gồm máy local, thuế và request lỗi chưa trả usage. Cách chạy, dữ liệu cần chuẩn bị và phiên bản thư viện nằm trong [hướng dẫn](../../docs/RUNNING.md) và `requirements-lock.txt`.

## 5. Thử thách nâng cao

Em dùng [*Climate Change 2023: Synthesis Report* — IPCC](https://www.ipcc.ch/report/sixth-assessment-report-cycle/2023/), gồm 186 trang PDF, 184 trang đánh số. PDF và index toàn văn giữ local theo [điều kiện sử dụng](https://www.ipcc.ch/copyright/); bài nộp có nguồn và lệnh tái tạo.

Em chia toàn bộ văn bản thành 1.217 đoạn, mỗi đoạn 700 ký tự, bước 580, embedding bằng E5. Có 6 trang không trích được text; cả 186 trang vẫn đọc được qua ảnh gốc. Agent tìm trang bằng hybrid RRF, dùng tool `read` để xem trang/crop, rồi trả lời bằng `finish`. Citation giữ trang PDF, bbox và vị trí hàng/cột hoặc panel. Em chưa dùng OCR hay sửa layout thủ công; hình không có từ khóa trong text có thể khó tìm.

[Benchmark nâng cao](../../benchmark/bonus.json) có dev 18 câu (15 có đáp án, 3 thiếu bằng chứng), test 30 câu (24 có đáp án, 6 thiếu bằng chứng), khóa trước thực nghiệm. Em thử ba cấu hình trên dev:

| Cấu hình / tập | Đạt | Câu lỗi cuối lượt | Thời gian gồm retry (s) | API USD ước tính |
|---|---|---|---|---|
| Compact / dev | 6/18 (33,33%) | 9 | 454,59 | 0,039073 |
| Thorough / dev | 15/18 (83,33%) | 0 | 144,52 | 0,057381 |
| Focused / dev | 17/18 (94,44%) | 0 | 366,07 | 0,058373 |
| Focused / test | 28/30 (93,33%) | 0 | 258,82 | 0,105507 |

Em chọn focused trước test: top-10 trang, ưu tiên caption khớp nhãn Figure/Table trong query; tối đa 6 vùng ảnh, cạnh 1.560 px, 10 lượt model và 2 lần thử lại lỗi mạng mỗi câu. So với thorough, focused yêu cầu trả lời ngắn bằng tiếng Anh và đúng các ý được hỏi. Các thay đổi được thử theo cấu hình tổng hợp. Chín lỗi schema trong giai đoạn thiết lập được lưu riêng; không thay thế kết quả của lượt dev/test đã công bố.

| Nhóm test | Đạt / tổng | Tỷ lệ |
|---|---|---|
| Bảng | 6/6 | 100% |
| Ảnh, sơ đồ | 5/5 | 100% |
| Biểu đồ | 4/5 | 80% |
| Multi-hop | 3/4 | 75% |
| Text | 4/4 | 100% |
| Thiếu bằng chứng | 6/6 | 100% |
| **Toàn bộ** | **28/30** | **93,33%** |

Ở bt16, agent chọn đúng SSP5-8.5 nhưng thêm số liệu SSP2-4.5 không khớp biểu đồ. Ở bt17, hai ý chính đúng nhưng câu bổ sung dùng “CO2 equivalent” cho mức giảm của CO2; em tính không đạt theo tiêu chí toàn bộ câu trả lời phải chính xác. Trên dev, bd08 cũng lỗi vì thêm ước lượng CCS ngoài yêu cầu. Em không chỉnh pipeline theo test.

Em đã xác nhận nhãn chấm toàn bộ 30 câu bonus sau bước AI hỗ trợ đối chiếu. Kết quả **28/30 (93,33%)**, vượt ngưỡng 90%; em nộp kèm bằng chứng để giảng viên xem xét 15 điểm bonus. Nhãn dev trong bảng vẫn là kết quả AI hỗ trợ chấm sơ bộ. [Phiếu đối chiếu 30 câu](../../results/bonus/test/focused/REVIEW.md), [nhãn và lý do](../../results/bonus/test/focused/reviews.json), [trace](../../results/bonus/test/focused/trace.json) và [metrics](../../results/bonus/test/focused/summary.json) được lưu để kiểm tra. Trace công khai giữ tham chiếu trang/vùng và hash context; toàn văn context giữ local, có thể tái tạo từ PDF.

Em dùng Codex hỗ trợ lập trình và tổng hợp kết quả. Nhãn phần cơ bản do em cung cấp; nhãn test bonus do AI hỗ trợ và đã được em xác nhận.
