# Code

Phần triển khai Day 7 đã nối model Anthropic và vector store Day 6:

- `anthropic_api.py`: Models/Messages API, lỗi và DNS retry có giới hạn.
- `day6_bridge.py`: E5-small đúng revision và pgvector strategy A, kết nối chỉ đọc.
- `retrieval.py`: TF-IDF, dense và hybrid RRF.
- `agent.py`: vòng lặp model gọi search/finish, context, citation, abstention và trace.
- `run.py`: chạy một câu hỏi.
- `experiment.py`: benchmark dev/test với manifest, split lock, resume và giữ trace retry.
- `evaluation.py`: retrieval/context evidence proxy, usage, latency và thống kê lỗi.
- `pricing.py`: ước tính chi phí từ usage và bảng giá có ngày kiểm tra.

- `bonus.py`: chuẩn bị index toàn bộ PDF, truy xuất text, đọc ảnh trang/vùng và chạy phần nâng cao.

Xem [hướng dẫn chạy](../docs/RUNNING.md) và [báo cáo](../report/individual/2A202603951_TranXuanLoc.md). Starter gốc giữ để đối chiếu; test mock chỉ kiểm tra hành vi code.
