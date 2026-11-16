# Phiếu kiểm tra câu trả lời và nguồn

Đối chiếu PDF gốc theo số trang. Nhãn phải do người chấm kiểm tra; không suy ra chất lượng chỉ từ citation ID.

## day7-t01

**Câu hỏi:** Theo mức độ giới hạn không gian, tài liệu chia plasmon thành ba loại nào?

**Loại:** Có đáp án

**Đáp án chuẩn / lý do thiếu:** Plasmon khối, plasmon bề mặt và plasmon bề mặt cục bộ.

**Kết quả (answered):** Theo mức độ giới hạn không gian, plasmon được chia thành ba loại: plasmon khối, plasmon bề mặt và plasmon bề mặt cục bộ (LSPR) [30de5529dcc998d2460ca63b40c8137c5641ad4b5cae3835c34526fe8cdc8c1d].

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

[dc27644d07a3d5baa2fd65f1eb1d2fada579ce87e331249fb9e77a5dfa19be0f | data/raw/22022101_TranXuanLoc.pdf | page 20]
t quang học của các hệ nano plasmon phức tạp – đặc biệt
là các mảng hạt nano với nhiều thông số hình học – truyền thống dựa vào các phương
pháp giải số phương trình Maxwell như phương pháp Phần tử Biên - BEM, phương pháp
Phần tử Hữu hạn – FEM, hay phương pháp Sai phân H ữu hạn trong miền thời gian–
FDTD. M ặc dù các phương pháp này cho k ết qu ả chính xác cao, chúng đòi h ỏi tài
nguyên tính toán lớn và thời gian thực thi kéo dài – đặc biệt khi cần quét một không gian
tham số rộng trong bài toán 

[83769d03c275c7998aa36edd3d4a0fb462af6de4c183780d6f3315e6a3fe9e46 | data/raw/22022101_TranXuanLoc.pdf | page 18]
 [34]. Trường evanescent phát sinh từ dao động
plasmon của hạt này sẽ kích thích và làm bi ến dạng phân bố điện tích trên b ề mặt hạt
lân c ận, d ẫn đ ến s ự lai hóa c ủa các mode plasmon theo mô hình lai hóa plasmon
(plasmon hybridization model) [35], trong đó tương tác gi ữa các h ạt tạo ra mode liên
kết có năng lượng thấp hơn và mode phản liên kết có năng lượng cao hơn so với mode
cộng hưởng của hạt đơn ban đầu. Hệ quả quan trọng nhất của tương tác này là s ự hình
thành các vùng tập trung trư
```

**Nguồn citation:**

- `30de5529dcc998d2460ca63b40c8137c5641ad4b5cae3835c34526fe8cdc8c1d` — trang PDF 23, ký tự 1350–1616.

**Trace:** `records.json`, query_id `day7-t01`.

## day7-t02

**Câu hỏi:** Điều kiện chuẩn Lorentz có tác dụng gì đối với các phương trình cho thế vectơ và thế vô hướng?

**Loại:** Có đáp án

**Đáp án chuẩn / lý do thiếu:** Giúp tách rời các biến thành các phương trình sóng độc lập cho A và Φ, vẫn tương đương hệ Maxwell ban đầu.

**Kết quả (answered):** Điều kiện chuẩn Lorentz là ∇·A + εc ∂Φ/∂t = 0 (phương trình 10). Nhờ việc chọn thế thỏa mãn điều kiện này (tận dụng tính bất biến chuẩn), các biến được tách rời, cho ra hệ phương trình sóng độc lập cho A và Φ, nhưng vẫn tương đương với hệ Maxwell ban đầu [5b7856b0cf26c4d42e9a7b9065594c48633ba0b54c224708ba375dd2e1352827] [265747326223c561d78ce9e74a2f6e4d601f26c62ef09fa2822f4cb3ca5c6519]. Trong miền tần số, các phương trình này trở thành phương trình Helmholtz: ∇²Φ + k²εΦ = −4πρ (11a) và ∇²A + k²εA = −(4π/c)j (11b) [265747326223c561d78ce9e74a2f6e4d601f26c62ef09fa2822f4cb3ca5c6519].

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

[5019cd7da8589fb92a4e6e3e7040f454b791135677343177293c55c77fe55d66 | data/raw/22022101_TranXuanLoc.pdf | page 31]
ℎ2 = 𝐴2𝑒 − 𝐴1𝑒 (38)
Trong đó, 𝐺1 và 𝐺2 là các toán tử hàm Green tương ứng với môi trường bên trong
(𝑗 = 1) và bên ngoài ( 𝑗 = 2) ranh giới. Tương tự, 𝜎1,2 và ℎ1,2⃗⃗⃗⃗⃗⃗ lần lượt là sự phân bố
của mật độ điện tích mặt (vô hướng) và mật độ dòng điện mặt (vectơ) tại hai môi trường
này; Φ𝑗𝑒 và 𝐴𝑗𝑒⃗⃗⃗⃗ là các thành phần thế vô hướng và thế vectơ của trường kích thích ngoài.
Bằng cách k ết hợp điều kiện chuẩn Lorentz v ới điều kiện liên t ục của các thành
phần điện từ trường (thành phần tiếp tuyến của

[265747326223c561d78ce9e74a2f6e4d601f26c62ef09fa2822f4cb3ca5c6519 | data/raw/22022101_TranXuanLoc.pdf | page 23]
)
Việc áp dụng điều kiện chuẩn Lorentz giúp tách r ời các biến, dẫn đến hệ phương
trình sóng hoàn toàn đ ộc lập cho 𝐴 và Φ nhưng vẫn tương đương v ới hệ phương trình
Maxwell ban đ ầu. Trong mi ền t ần s ố, chúng đư ợc bi ết đ ến là các phương trình
Helmholtz cho hệ thế điện từ:
𝛻2𝛷 + 𝑘2𝜀𝛷 = −4𝜋𝜌 (11𝑎)
𝛻2𝐴 + 𝑘2𝜀𝐴 = − 4𝜋𝑐 𝑗 (11𝑏)
3.2. Hiện tượng cộng hưởng plasmon bề mặt cục bộ (LSPR)
Về mặt bản chất, "plasmon" là sự dao động tập thể của mạng lưới các electron tự
do trong kim loại. Dựa trên mức độ
```

**Nguồn citation:**

- `5b7856b0cf26c4d42e9a7b9065594c48633ba0b54c224708ba375dd2e1352827` — trang PDF 23, ký tự 450–950.
- `265747326223c561d78ce9e74a2f6e4d601f26c62ef09fa2822f4cb3ca5c6519` — trang PDF 23, ký tự 900–1400.

**Trace:** `records.json`, query_id `day7-t02`.

## day7-t03

**Câu hỏi:** Điều kiện về tần số nào làm xuất hiện cộng hưởng LSPR?

**Loại:** Có đáp án

**Đáp án chuẩn / lý do thiếu:** Tần số ánh sáng tới trùng tần số dao động tự nhiên của đám mây electron.

**Kết quả (answered):** Cộng hưởng LSPR xuất hiện khi phần thực của hằng số điện môi kim loại thỏa điều kiện ε1(λ) = −2ε_m, trong đó ε_m là hằng số điện môi của môi trường xung quanh; đây là điều kiện cộng hưởng Fröhlich, tức tiết diện tắt dần cực đại khi mẫu số đạt cực tiểu [97e3c6317bd542ae942ff77f9eb142dfeb15e3b50cec9ab907e572d590560151]. Ví dụ, với hạt nano vàng trong nước (ε_m ≈ 1.7), bước sóng để điều kiện này xảy ra khoảng 520 nm [97e3c6317bd542ae942ff77f9eb142dfeb15e3b50cec9ab907e572d590560151]. Điều kiện này có tính chất lý thuyết, phụ thuộc vào môi trường điện môi xung quanh [97e3c6317bd542ae942ff77f9eb142dfeb15e3b50cec9ab907e572d590560151]; theo phần trình bày về độ phân cực, hiện tượng này xảy ra khi phần thực của ε_in + 2ε_out thỏa một hệ thức, với giả thiết phần ảo nhỏ hoặc biến thiên chậm [32a5e4dbe516baf8e598c01a797441b1d9ce0c73f266e5652e9a8cd612b6b548].

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
[97e3c6317bd542ae942ff77f9eb142dfeb15e3b50cec9ab907e572d590560151 | data/raw/22022101_TranXuanLoc.pdf | page 26]
n mang lại giá trị tham khảo tốt cho các hạt lớn hơn.
Từ phương trình tiết diện tắt dần , có thể nhận thấy 𝜎𝑒𝑥𝑡 sẽ đạt giá trị cực đại khi
mẫu số tiến tới giá trị cực tiểu. Điều kiện này đạt được khi:
𝜖1(𝜆) = −2𝜖𝑚 (16)
Đây chính là điều kiện cộng hưởng lý thuyết giải thích sự phụ thuộc của đỉnh LSPR
vào môi trường điện môi xung quanh. Chẳng hạn, đối với hạt nano vàng đặt trong môi
trường nước (𝜖𝑚 ≈ 1.7), bước sóng kỳ vọng để điều kiện 𝜖1 = −2𝜖𝑚 xảy ra là khoảng
520 nm. Điều này hoàn toàn phù hợp

[19d8d60bcd18bd04b4f47ecf2bc381cdb1349d1b97a7181a0e4c9cc37f2c1767 | data/raw/22022101_TranXuanLoc.pdf | page 26]
m loại phải cung cấp một giá trị ϵ1 âm hơn, điều này tương ứng với mức
năng lượng thấp hơn. Kết quả là, đỉnh cộng hưởng LSPR sẽ dịch chuyển về phía bước
sóng dài hơn. Đây chính là cơ chế vật lý cốt lõi làm nền tảng cho sự hoạt động của các
cảm biến chiết suất.
3.4. Hiệu ứng tăng cường trường gần - Near-field Enhancement
Hiệu ứng tăng cường trường gần là một trong những đặc trưng quang học cốt lõi
của các hạt nano kim loại. Trạng thái cộng hưởng đạt được khi tần số dao động tự nhiên

[32a5e4dbe516baf8e598c01a797441b1d9ce0c73f266e5652e9a8cd612b6b548 | data/raw/22022101_TranXuanLoc.pdf | page 28]
27)
Phân tích biểu thức của độ phân cực 𝛼 ở phương trình (24), có thể thấy 𝛼 sẽ cộng
hưởng và đạt giá trị cực đại khi độ lớn của mẫu số |𝜖𝑖𝑛 + 2𝜖𝑜𝑢𝑡| tiến tới cực tiểu. Giả
thiết rằng thành phần ảo Im[𝜖𝑖𝑛] có giá trị nhỏ hoặc biến thiên rất chậm quanh vùng tần
số cộng hưởng, hiện tượng cộng hưởng plasmon (điều kiện Fröhlich) sẽ xảy ra khi phần
thực thỏa mãn hệ thức:
```

**Nguồn citation:**

- `97e3c6317bd542ae942ff77f9eb142dfeb15e3b50cec9ab907e572d590560151` — trang PDF 26, ký tự 900–1400.
- `32a5e4dbe516baf8e598c01a797441b1d9ce0c73f266e5652e9a8cd612b6b548` — trang PDF 28, ký tự 1350–1718.

**Trace:** `records.json`, query_id `day7-t03`.

## day7-t04

**Câu hỏi:** Trong khuôn khổ BEM mô tả ở đồ án, hàm điện môi của mỗi hạt nano được giả định có hai tính chất nào?

**Loại:** Có đáp án

**Đáp án chuẩn / lý do thiếu:** Cục bộ và đẳng hướng.

**Kết quả (answered):** Theo đồ án, trong khuôn khổ BEM, mỗi hạt nano được đặc trưng bởi hàm điện môi cục bộ và đẳng hướng ε(ω) (tức là hàm điện môi có tính cục bộ và đẳng hướng), và các ranh giới phân cách giữa các vùng vật liệu khác nhau được xác định rõ ràng và sắc nét [aaf006f93e82f1213934f9d4f927fc3f8a718baf9cbf577a3042546086454414].

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
[aaf006f93e82f1213934f9d4f927fc3f8a718baf9cbf577a3042546086454414 | data/raw/22022101_TranXuanLoc.pdf | page 29]
áp phần tử biên vi phân (Boundary Element Method - BEM)
3.5.1. Lý thuyết
Phương pháp Phần tử Biên là một trong những phương pháp số được sử dụng rộng
rãi nhất để mô phỏng tính chất quang học của các hạt nano điện môi và kim loại. Trong
khuôn khổ phương pháp này, mỗi hạt nano được đặc trưng bởi hàm điện môi cục bộ và
đẳng hướng 𝜀(𝜔), với các ranh gi ới phân cách gi ữa các vùng vật liệu khác nhau đư ợc
xác định rõ ràng và sắc nét. Về mặt cấu trúc, hệ thống BEM bao gồm các thành phần cơ
bản: các mi

[7e6e3257db9cbf0671600190c37b7de7cb7fdd48f8ec75450823c098708cbdd2 | data/raw/22022101_TranXuanLoc.pdf | page 32]
trong không gian, làm cơ sở vững chắc để trích xuất các phổ tiết diện quang học (tán xạ,
hấp thụ, tiêu quang) của hệ hạt nano một cách chính xác.
3.5.2. Công cụ mô phỏng MNPBEM Toolbox trên Matlab
MNPBEM là m ột bộ công cụ mạnh mẽ trên nền tảng MATLAB, đư ợc thiết kế
chuyên biệt để mô phỏng các tính chất quang học của hạt nano kim loại dựa trên phương
pháp BEM[43], [44]. Về mặt nền tảng, công cụ này giải hệ phương trình Maxwell cho
các thực thể vật liệu nằm trong m ột môi trư ờng điện môi. Thu ậ

[9f5100afaea654d650d7d484c26f8be6e31dcce43a04fe31aab705390fdfad78 | data/raw/22022101_TranXuanLoc.pdf | page 30]
 𝑠 đại diện cho tọa độ
chạy trên mặt biên 𝜕𝑉𝑗, với 𝑑𝑎 là phần tử diện tích vi phân. Các đ ại lượng 𝜎𝑗 và ℎ𝑗 lần
lượt là mật độ điện tích mặt và mật độ dòng điện mặt, đóng vai trò là các ngu ồn tương
đương sinh ra trường tán xạ.
Về mặt tính toán số, cốt lõi của phương pháp phần tử biên (BEM) là quá trình rời
rạc hóa các phương trình tích phân mặt này. Bề mặt biên của hạt nano sẽ được chia lưới
thành các phần tử nhỏ. Thuật toán sau đó sẽ chuyển đổi hệ phương trình tích phân liên
```

**Nguồn citation:**

- `aaf006f93e82f1213934f9d4f927fc3f8a718baf9cbf577a3042546086454414` — trang PDF 29, ký tự 450–950.

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

[028603ce46e5adab14955b82ffe62e1b850259a55232b979db2bc3b471729a51 | data/raw/22022101_TranXuanLoc.pdf | page 32]
ị Gauss, trong đó mọi thông số kích thước
hình học và bư ớc sóng ánh sáng λ trong chân không đ ều được chuẩn hóa v ề đơn vị
nanomet (nm) .
Tùy thuộc vào tương quan giữa kích thước hạt và bước sóng ánh sáng, MNPBEM
cung cấp hai nhóm bộ giải chính:
Một là bộ giải tựa tĩnh. Nhóm bộ giải này hoạt động dựa trên phép g ần đúng tựa
tĩnh, trong đó bài toán đư ợc đơn gi ản hóa b ằng cách gi ải phương trình Poisson ho ặc
Laplace cho các thế điện từ thay vì phương trình sóng Helmholtz. Phương pháp này loại

[9a2370a4f3eab144c6feb4b20bade1623af16e8f1cee1f34338756810ce2e49e | data/raw/22022101_TranXuanLoc.pdf | page 32]
 tạp hơn: giả
sử bề mặt hạt được chia lưới thành 𝑁 phần tử, bộ giải đầy đủ cần phải thiết lập và thực
hiện các phép nghịch đảo cho các ma trận phức đặc có kích thước tỷ lệ thuận với 𝑁 × 𝑁,
đòi hỏi khả năng xử lý mạnh mẽ từ hệ thống máy tính.
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

[489d30c8822aac34c68713a34b931dba985fa5d1bccda25f41d8869cdd2bfaa5 | data/raw/22022101_TranXuanLoc.pdf | page 20]
lâm sàng, công nghệ này cho phép phát hiện các dấu ấn sinh học, kháng nguyên, kháng
thể và axit nucleic ở nồng độ cực thấp mà không yêu c ầu bước gắn nhãn huỳnh quang
phức tạp, từ đó tối ưu hóa và rút ng ắn đáng k ể quy trình xét nghi ệm. Trong lĩnh v ực
giám sát môi trường và an toàn thực phẩm, cảm biến LSPR được tích hợp để nhận diện
nhanh các ion kim lo ại nặng, dư lư ợng thuốc bảo vệ thực vật, hóa ch ất ô nhi ễm hoặc
mầm bệnh vi sinh. Đặc biệt, với xu hướng tiến tới các thiết bị y tế tinh gọ

[c95d89b2694256f3f95cd02f31dee556bc223d02a04917b52c83cf3cead7d2f5 | data/raw/22022101_TranXuanLoc.pdf | page 46]
iện toàn diện các tham số cảm biến cốt lõi: đẩy độ nhạy lên 𝑆 =
256 nm/RIU và FoM lên d ải 5.8–7.3, vượt trội hơn h ẳn so v ới nanocube Ag đơn l ẻ
(𝑆 = 243 nm/RIU, FoM = 5 .3–7.1). Quan tr ọng hơn, dư ới góc đ ộ thực nghiệm hóa
học, lõi Au giữ vai trò như một hạt mầm bền vững để kiểm soát chính xác hình thái hình
học và độ đồng đều khi phát triển lớp vỏ Ag, đồng thời tăng cường độ ổn định hóa học
cho cấu trúc tổng thể nhờ cơ chế hút electron từ vỏ Ag, hạn chế tối đa các phản ứng oxy
hóa và phản 
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
[277e6b73706d9cb9e77ece74de0a56fdfcbff163dbb6f78a3b4864762894c2c7 | data/raw/22022101_TranXuanLoc.pdf | page 21]
hợp mô ph ỏng BEM và mô hình h ọc sâu v ẫn còn
hạn chế. Đây chính là khoảng trống khoa học mà đồ án này hướng tới lấp đầy, thông qua
việc xây dựng một pipeline hoàn chỉnh từ sinh dữ liệu mô phỏng, huấn luyện mô hình
1D-CNN, đến đánh giá khả năng dự đoán phổ quang học của mảng nanocube Au@Ag
trong không gian tham số rộng.

[c77147086f9ec599a6ab568c0f315720f4544651d50dafd5ea439b886070cd2f | data/raw/22022101_TranXuanLoc.pdf | page 36]
thử thách nhất định cho mô hình nội suy ở các dải
phổ phức tạp.
3.6.2. Sử dụng mạng Nơ-ron Tích chập 1 Chiều (1D-CNN) để dự đoán phổ
Đầu ra của bài toán là các phổ tiết diện quang học trải dài qua 251 điểm bước sóng
liên tục. Bản chất của dữ liệu quang ph ổ là dữ liệu chuỗi, nơi mà giá tr ị cường độ tại
một bước sóng có mối tương quan không gian chặt chẽ với các điểm lân cận để tạo thành
hình dáng của các đỉnh cộng hưởng. Do đó, 1D-CNN được lựa chọn làm kiến trúc cốt
lõi thay vì mạng nơ-ron kết 

[f155dadd8aaffa068733a0d6465ceb79bbd7461a1149fdfec4708ca772e5dcc4 | data/raw/22022101_TranXuanLoc.pdf | page 56]
4.3. Kết quả mô hình 1D-CNN
4.3.1. Quá trình hội tụ và chống quá khớp (Overfitting)

Hình 4.10. Đường cong hội tụ của hàm suy hao L1 (L1 Loss) trong quá trình hu ấn luyện
mạng 1D-CNN.
Quá trình huấn luyện mô hình được thực hiện trong 3000 chu kỳ (epochs). Đồ thị
hàm suy hao (Hình 4.10) thể hiện rõ đặc tính tối ưu hóa của hàm L1 Loss. Trong khoảng
1900 chu k ỳ đầu tiên, đ ồ thị có sự dao động cục bộ lớn do thu ật toán Adam c ập nhật
trọng số với tốc độ học khởi tạo 0.001, giúp mô hình thoát kh ỏi

[b3493074c57101f6e4781841b7fa37bffd48f958d1ab4119e0391bf970e49382 | data/raw/22022101_TranXuanLoc.pdf | page 61]
Nhìn chung, kết quả đối chiếu trực quan khẳng định mạng 1D-CNN đề xuất đã học
được bản chất vật lý của sự tương tác điện từ trong mảng hạt nano lõi-vỏ. Mô hình không
chỉ phản hồi chính xác s ự dịch chuyển đỉnh phổ theo sự thay đổi tinh tế của chiết suất
môi trường, mà còn giải mã thành công các hiệu ứng hình học phức tạp để bảo toàn chất
lượng (FoM) của các đỉnh Fano phục vụ cho cảm biến LSPR.
4.3.5. Đánh giá hiệu năng và tốc độ tính toán
Đóng góp thực tiễn lớn nhất của mô hình học máy nằm ở khả
```

**Nguồn citation:**


**Trace:** `records.json`, query_id `day7-u04`.

