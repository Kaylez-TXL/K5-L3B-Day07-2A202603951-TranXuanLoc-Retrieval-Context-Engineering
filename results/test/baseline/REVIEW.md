# Phiếu kiểm tra câu trả lời và nguồn

Đối chiếu PDF gốc theo số trang. Nhãn phải do người chấm kiểm tra; không suy ra chất lượng chỉ từ citation ID.

## day7-t01

**Câu hỏi:** Theo mức độ giới hạn không gian, tài liệu chia plasmon thành ba loại nào?

**Loại:** Có đáp án

**Đáp án chuẩn / lý do thiếu:** Plasmon khối, plasmon bề mặt và plasmon bề mặt cục bộ.

**Kết quả (answered):** Theo mức độ giới hạn không gian, tài liệu chia plasmon thành ba loại: plasmon khối, plasmon bề mặt và plasmon bề mặt cục bộ (LSPR) [30de5529dcc998d2460ca63b40c8137c5641ad4b5cae3835c34526fe8cdc8c1d].

**Gold (chỉ dùng chấm, không được gửi vào agent):**

```json
[
  {
    "source_id": "auag-thesis-2026",
    "page": 23,
    "evidence": "Dựa trên mức độ giới hạn không gian, plasmon có thể được chia thành\nplasmon khối , plasmon bề mặt, và plasmon bề mặt cục bộ."
  }
]
```

**Context cuối:**

```text
[30de5529dcc998d2460ca63b40c8137c5641ad4b5cae3835c34526fe8cdc8c1d | data/raw/22022101_TranXuanLoc.pdf | page 23]
các electron tự
do trong kim loại. Dựa trên mức độ giới hạn không gian, plasmon có thể được chia thành
plasmon khối , plasmon bề mặt, và plasmon bề mặt cục bộ. Trong đó, hiện tượng cộng
hưởng plasmon bề mặt cục bộ LSPR là một hiệu ứng quang học đặc trưng, xảy ra khi
```

**Nguồn citation:**

- `30de5529dcc998d2460ca63b40c8137c5641ad4b5cae3835c34526fe8cdc8c1d` — trang PDF 23, ký tự 1350–1616.

**Trace:** `records.json`, query_id `day7-t01`.

## day7-t02

**Câu hỏi:** Điều kiện chuẩn Lorentz có tác dụng gì đối với các phương trình cho thế vectơ và thế vô hướng?

**Loại:** Có đáp án

**Đáp án chuẩn / lý do thiếu:** Giúp tách rời các biến thành các phương trình sóng độc lập cho A và Φ, vẫn tương đương hệ Maxwell ban đầu.

**Kết quả (answered):** Theo corpus, nhờ tính bất biến chuẩn (gauge invariance) của trường điện từ, ta có thể chọn các thế sao cho thỏa điều kiện chuẩn Lorentz: ∇·A + εc ∂Φ/∂t = 0 [5b7856b0cf26c4d42e9a7b9065594c48633ba0b54c224708ba375dd2e1352827]. Việc áp dụng điều kiện này giúp tách rời (decouple) các phương trình của thế vectơ và thế vô hướng; đoạn văn bị cắt ngay tại đó nên tôi không có đủ bằng chứng để mô tả chi tiết dạng phương trình sau khi tách.

**Gold (chỉ dùng chấm, không được gửi vào agent):**

```json
[
  {
    "source_id": "auag-thesis-2026",
    "page": 23,
    "evidence": "Việc áp dụng điều kiện chuẩn Lorentz giúp tách r ời các biến, dẫn đến hệ phương\ntrình sóng hoàn toàn đ ộc lập cho 𝐴 và Φ nhưng vẫn tương đương v ới hệ phương trình\nMaxwell ban đ ầu."
  }
]
```

**Context cuối:**

```text
[5b7856b0cf26c4d42e9a7b9065594c48633ba0b54c224708ba375dd2e1352827 | data/raw/22022101_TranXuanLoc.pdf | page 23]
ông, nó luôn có th ể được viết dưới dạng toán tử xoáy của
một trường vectơ khác ở đây là 𝐴. Điều này được minh chứng qua đồng nhất thức:
𝛻 ⋅ 𝐵 = 𝛻 ⋅ (𝛻 × 𝐴) = 0 (9𝑏)
Mặt khác, điện trường và từ trường luôn tồn tại mối liên hệ mật thiết và không độc
lập với nhau. Bằng cách khai thác tính bất biến chuẩn (gauge invariance) của các trường
điện từ, ta có thể tự do lựa chọn các thế sao cho chúng thỏa mãn điều kiện chuẩn Lorentz:
𝛻 ⋅ 𝐴 + 𝜀𝑐 𝜕𝛷𝜕𝑡 = 0 (10)
Việc áp dụng điều kiện chuẩn Lorentz giúp tách r
```

**Nguồn citation:**

- `5b7856b0cf26c4d42e9a7b9065594c48633ba0b54c224708ba375dd2e1352827` — trang PDF 23, ký tự 450–950.

**Trace:** `records.json`, query_id `day7-t02`.

## day7-t03

**Câu hỏi:** Điều kiện về tần số nào làm xuất hiện cộng hưởng LSPR?

**Loại:** Có đáp án

**Đáp án chuẩn / lý do thiếu:** Tần số ánh sáng tới trùng tần số dao động tự nhiên của đám mây electron.

**Kết quả (abstain):** Không đủ bằng chứng trong tài liệu để trả lời câu hỏi này.

**Gold (chỉ dùng chấm, không được gửi vào agent):**

```json
[
  {
    "source_id": "auag-thesis-2026",
    "page": 24,
    "evidence": "Khi tần số\ncủa ánh sáng t ới trùng khớp với tần số dao động tự nhiên của đám mây electron, hi ện\ntượng cộng hưởng LSPR diễn ra."
  }
]
```

**Context cuối:**

```text
[19d8d60bcd18bd04b4f47ecf2bc381cdb1349d1b97a7181a0e4c9cc37f2c1767 | data/raw/22022101_TranXuanLoc.pdf | page 26]
m loại phải cung cấp một giá trị ϵ1 âm hơn, điều này tương ứng với mức
năng lượng thấp hơn. Kết quả là, đỉnh cộng hưởng LSPR sẽ dịch chuyển về phía bước
sóng dài hơn. Đây chính là cơ chế vật lý cốt lõi làm nền tảng cho sự hoạt động của các
cảm biến chiết suất.
3.4. Hiệu ứng tăng cường trường gần - Near-field Enhancement
Hiệu ứng tăng cường trường gần là một trong những đặc trưng quang học cốt lõi
của các hạt nano kim loại. Trạng thái cộng hưởng đạt được khi tần số dao động tự nhiên
```

**Nguồn citation:**


**Trace:** `records.json`, query_id `day7-t03`.

## day7-t04

**Câu hỏi:** Trong khuôn khổ BEM mô tả ở đồ án, hàm điện môi của mỗi hạt nano được giả định có hai tính chất nào?

**Loại:** Có đáp án

**Đáp án chuẩn / lý do thiếu:** Cục bộ và đẳng hướng.

**Kết quả (answered):** Theo đồ án, vì hạt nano làm từ vật liệu kim loại nên hàm điện môi ϵ_in không phải là hằng số thực mà là hàm phức phụ thuộc tần số góc ω: ϵ(ω) = ϵ′(ω) + iϵ′′(ω) [f5aa4e5e59cd1435f998fad12911cfd106826a4fa6d1ff5a82eb0a901f0e694f]. Hai thành phần này là phần thực ϵ′ và phần ảo ϵ′′, liên hệ với chiết suất n và hệ số tắt dần κ theo ϵ′ = n² − κ² và ϵ′′ = 2nκ [f5aa4e5e59cd1435f998fad12911cfd106826a4fa6d1ff5a82eb0a901f0e694f].

Lưu ý: đoạn trích chỉ nêu tính chất "phức và phụ thuộc tần số" một cách tổng quát; tôi không tìm thấy câu nào liệt kê đúng "hai tính chất" theo cách diễn đạt của câu hỏi, nên câu trả lời trên là cách hiểu gần nhất dựa trên bằng chứng.

**Gold (chỉ dùng chấm, không được gửi vào agent):**

```json
[
  {
    "source_id": "auag-thesis-2026",
    "page": 29,
    "evidence": "mỗi hạt nano được đặc trưng bởi hàm điện môi cục bộ và\nđẳng hướng"
  }
]
```

**Context cuối:**

```text
[f5aa4e5e59cd1435f998fad12911cfd106826a4fa6d1ff5a82eb0a901f0e694f | data/raw/22022101_TranXuanLoc.pdf | page 28]
g tức thời của đám mây điện tử:
𝛼 = 4𝜋𝑅3 𝜖𝑖𝑛 − 𝜖𝑜𝑢𝑡
𝜖𝑖𝑛 + 2𝜖𝑜𝑢𝑡
(24)
Vì hạt nano được cấu tạo từ vật liệu kim loại, hàm điện môi 𝜖𝑖𝑛 không phải là một
hằng số thực mà là một hàm phức phụ thuộc mạnh vào tần số góc 𝜔 của ánh sáng tới:
𝜖(𝜔) = 𝜖′(𝜔) + 𝑖𝜖′′(𝜔) (25)
Các thành phần thực (𝜖′) và ảo (𝜖′′) này có mối liên hệ trực tiếp với các hằng số
quang học đặc trưng của hệ vật liệu, bao gồm chiết suất 𝑛 và hệ số tắt dần 𝜅:
𝜖′ = 𝑛2 − 𝜅2 (26)
𝜖′′ = 2𝑛𝜅 (27)
Phân tích biểu thức của độ phân cực 𝛼 ở phương
```

**Nguồn citation:**

- `f5aa4e5e59cd1435f998fad12911cfd106826a4fa6d1ff5a82eb0a901f0e694f` — trang PDF 28, ký tự 900–1400.

**Trace:** `records.json`, query_id `day7-t04`.

## day7-t05

**Câu hỏi:** Vì sao bộ giải BEM đầy đủ chậm hơn bộ giải tựa tĩnh xét theo cấu trúc ma trận?

**Loại:** Có đáp án

**Đáp án chuẩn / lý do thiếu:** Phải thiết lập và nghịch đảo ma trận phức đặc kích thước tỷ lệ N × N khi bề mặt có N phần tử.

**Kết quả (abstain):** Không đủ bằng chứng có nguồn hợp lệ để trả lời.

**Gold (chỉ dùng chấm, không được gửi vào agent):**

```json
[
  {
    "source_id": "auag-thesis-2026",
    "page": 32,
    "evidence": "giả\nsử bề mặt hạt được chia lưới thành 𝑁 phần tử, bộ giải đầy đủ cần phải thiết lập và thực\nhiện các phép nghịch đảo cho các ma trận phức đặc có kích thước tỷ lệ thuận với 𝑁 × 𝑁"
  }
]
```

**Context cuối:**

```text
[fca088aa74108223aec8ec0b432b4b7e81cdaab61def7daa3311e4063aaf553c | data/raw/22022101_TranXuanLoc.pdf | page 32]
i dải bước sóng kh ả kiến và c ận
hồng ngoại (400 nm - 900 nm) các hiệu ứng động lực học như độ trễ pha và suy hao bức
xạ bắt đầu chi phối mạnh mẽ. Lúc này, bộ giải BEM đầy đủ bắt buộc phải được sử dụng.
Bộ giải này gi ải quyết hệ phương trình Maxwell hoàn ch ỉnh có xét đ ến hiệu ứng trễ.
Mặc dù kết quả trả về có độ chính xác vật lý cực kỳ cao, tốc độ tính toán sẽ chậm hơn
đáng kể so với bộ giải tựa tĩnh. Nguyên nhân là do c ấu trúc toán học phức tạp hơn: giả
sử bề mặt hạt được chia lưới thành 𝑁
```

**Nguồn citation:**


**Trace:** `records.json`, query_id `day7-t05`.

## day7-u03

**Câu hỏi:** Cảm biến Au@Ag của đồ án có giới hạn phát hiện glucose trong thử nghiệm lâm sàng là bao nhiêu mmol/L?

**Loại:** Thiếu bằng chứng

**Đáp án chuẩn / lý do thiếu:** No glucose clinical experiment or corresponding detection limit found.

**Kết quả (abstain):** Không đủ bằng chứng trong tài liệu để trả lời câu hỏi này.

**Gold (chỉ dùng chấm, không được gửi vào agent):**

```json
[]
```

**Context cuối:**

```text
[29b234572a49fc9c0ae0d88ad68ff093bee52d5f44f6989eebf17b45ae8cbd08 | data/raw/22022101_TranXuanLoc.pdf | page 64]
- Định hướng ứng dụng cảm biến sinh học đặc hiệu: Cấu hình mảng 3x3 Au@Ag
với độ nhạy 724 nm/RIU cung cấp một nền tảng linh hoạt để phát triển các cảm
biến chẩn đoán y sinh. Các nghiên c ứu thực nghiệm trong tương lai có th ể tiến
hành chức năng hóa bề mặt vỏ Ag bằng các kháng thể chọn lọc để phát hiện các
dấu ấn sinh học nồng độ thấp, hướng tới việc tự động hóa quá trình phân tích tín
hiệu cảm biến thông qua chính các thuật toán học máy đã được phát triển.
```

**Nguồn citation:**


**Trace:** `records.json`, query_id `day7-u03`.

## day7-u04

**Câu hỏi:** Mã nguồn mô hình học máy của đồ án được phát hành tại URL GitHub nào và commit hash nào?

**Loại:** Thiếu bằng chứng

**Đáp án chuẩn / lý do thiếu:** No published GitHub repository URL or commit identifier found.

**Kết quả (abstain):** Không đủ bằng chứng trong tài liệu để trả lời câu hỏi này.

**Gold (chỉ dùng chấm, không được gửi vào agent):**

```json
[]
```

**Context cuối:**

```text
[a43445b6bfd9c8f5e735b7533f5c0042c1bb8b769c6a89047daf32b2916e803a | data/raw/22022101_TranXuanLoc.pdf | page 21]
erative Adversarial Network – GAN), M ạng t ự mã hóa bi ến phân (Variational
Autoencoder – V AE), hoặc Mạng nơ-ron đảo nghịch (Invertible Neural Network – INN).
Trong phạm vi đồ án này, bài toán thuận được lựa chọn làm mục tiêu, cụ thể là xây
dựng mô hình dự đoán phổ quang học của mảng hạt nano Au@Ag từ các thông số hình
học đầu vào.
2.2.3. Tình hình nghiên cứu hiện tại
Trong những năm gần đây, đã có nhiều công trình nghiên cứu tiên phong ứng dụng
học máy vào bài toán dự đoán và tối ưu hóa tính 
```

**Nguồn citation:**


**Trace:** `records.json`, query_id `day7-u04`.

