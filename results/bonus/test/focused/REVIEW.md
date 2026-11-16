# Phiếu đánh giá phần nâng cao

**Trạng thái:** Trần Xuân Lộc đã xác nhận kết quả chấm toàn bộ 30 câu. Nhãn và lý do do AI hỗ trợ, được sinh viên xác nhận; kết quả giữ nguyên 28/30, bt16 và bt17 không đạt.

Chấm đạt khi đúng và đủ, đúng đơn vị/điều kiện, nguồn thực sự hỗ trợ; câu lỗi tính không đạt. Đối chiếu PDF gốc theo trang và vùng, không chỉ đọc đáp án chuẩn.

## bt01 — table

**Kết quả chấm đã xác nhận:** Đạt. Đúng 43% [34–60], GHG năm 2030 so với 2019; số CO2 bổ sung 48% [36–69] cũng khớp bảng trang 37.

**Câu hỏi:** In Table SPM.1, for 1.5°C (>50%) pathways with no or limited overshoot, give the median GHG reduction in 2030 and the 5–95 percentile interval relative to 2019.

**Đáp án / hành vi chuẩn:** 43% [34–60%].

**Kết quả (answered):** In Table SPM.1, for 1.5°C (>50%) with no or limited overshoot, the GHG emissions reduction from 2019 levels by 2030 is a median of 43% with a 5–95 percentile range of 34–60%. (Under the same scenario, the CO2 reduction is 48% [36–69%].)

**Vùng bằng chứng chuẩn để kiểm tra:**

```json
[
  {
    "page": 37,
    "bbox": [
      0.06,
      0.03,
      0.94,
      0.25
    ],
    "location": "Table SPM.1, 1.5°C GHG row, 2030 column"
  }
]
```

**Citation của agent:**

```json
[
  {
    "region_id": "p037-r1",
    "location": "Table SPM.1, row 'Limit warming to 1.5°C (>50%) with no or limited overshoot', GHG row, 2030 column: 43 [34-60]",
    "page": 37,
    "bbox": [
      0,
      0,
      1,
      0.5
    ],
    "source": "https://www.ipcc.ch/report/ar6/syr/downloads/report/IPCC_AR6_SYR_FullVolume.pdf"
  }
]
```

## bt02 — table

**Kết quả chấm đã xác nhận:** Đạt. Đúng 73% [55–90], CO2 năm 2050, kịch bản 2°C >67%, so với 2019; đúng hàng/cột trang 37.

**Câu hỏi:** Read Table SPM.1: for 2°C (>67%) pathways, what are the median and 5–95 percentile CO2 reductions in 2050 relative to 2019?

**Đáp án / hành vi chuẩn:** 73% [55–90%].

**Kết quả (answered):** For 2°C (>67%) pathways, CO2 emissions in 2050 are reduced by a median of 73% relative to 2019, with a 5–95 percentile range of 55–90%.

**Vùng bằng chứng chuẩn để kiểm tra:**

```json
[
  {
    "page": 37,
    "bbox": [
      0.06,
      0.03,
      0.94,
      0.25
    ],
    "location": "Table SPM.1, 2°C CO2 row, 2050 column"
  }
]
```

**Citation của agent:**

```json
[
  {
    "region_id": "p037-r1",
    "location": "Table SPM.1, row 'Limit warming to 2°C (>67%)', CO2 row, 2050 column: 73 [55-90]",
    "page": 37,
    "bbox": [
      0,
      0,
      1,
      0.5
    ],
    "source": "https://www.ipcc.ch/report/ar6/syr/downloads/report/IPCC_AR6_SYR_FullVolume.pdf"
  }
]
```

## bt03 — table

**Kết quả chấm đã xác nhận:** Đạt. Đúng 57 [52–60] GtCO2-eq/năm, chính sách đến cuối 2020, năm 2030; bảng 2.2 trang 74.

**Câu hỏi:** In Table 2.2, give the median and min–max global emissions in 2030 implied by policies implemented by the end of 2020, including units.

**Đáp án / hành vi chuẩn:** 57 [52–60] GtCO2-eq/year.

**Kết quả (answered):** Table 2.2 gives a median projected global emission in 2030 implied by policies implemented by the end of 2020 of 57 GtCO2-eq/yr, with a min–max range of 52–60 GtCO2-eq/yr.

**Vùng bằng chứng chuẩn để kiểm tra:**

```json
[
  {
    "page": 74,
    "bbox": [
      0.05,
      0.36,
      0.95,
      0.85
    ],
    "location": "Table 2.2, first data row, implemented-policies column"
  }
]
```

**Citation của agent:**

```json
[
  {
    "region_id": "p074-r1",
    "location": "Table 2.2, first data column 'Implied by policies implemented by the end of 2020 (GtCO2-eq/yr)', row 'Median projected global emissions (min–max)': 57 [52–60]",
    "page": 74,
    "bbox": [
      0,
      0,
      1,
      1
    ],
    "source": "https://www.ipcc.ch/report/ar6/syr/downloads/report/IPCC_AR6_SYR_FullVolume.pdf"
  }
]
```

## bt04 — table

**Kết quả chấm đã xác nhận:** Đạt. Đúng 16–23 GtCO2-eq/năm; hàng 1.5°C hành động ngay và cột NDC có điều kiện, trang 74.

**Câu hỏi:** In Table 2.2, what is the emissions gap between conditional NDCs and 1.5°C (>50%, no/limited overshoot) pathways with immediate action? Include units.

**Đáp án / hành vi chuẩn:** 16–23 GtCO2-eq/year.

**Kết quả (answered):** In Table 2.2, the emissions gap between NDCs including conditional elements and pathways limiting warming to 1.5°C (>50%) with no or limited overshoot and immediate action is 16–23 GtCO2-eq/yr in 2030.

**Vùng bằng chứng chuẩn để kiểm tra:**

```json
[
  {
    "page": 74,
    "bbox": [
      0.05,
      0.36,
      0.95,
      0.85
    ],
    "location": "Table 2.2, last row, including conditional elements column"
  }
]
```

**Citation của agent:**

```json
[
  {
    "region_id": "p074-r1",
    "location": "Table 2.2, row 'Emissions gap between NDCs and pathways that limit warming to 1.5°C (>50%) with no or limited overshoot with immediate action', column 'Including conditional elements (GtCO2-eq/yr)': 16–23",
    "page": 74,
    "bbox": [
      0,
      0,
      1,
      1
    ],
    "source": "https://www.ipcc.ch/report/ar6/syr/downloads/report/IPCC_AR6_SYR_FullVolume.pdf"
  }
]
```

## bt05 — table

**Kết quả chấm đã xác nhận:** Đạt. Đúng C1 và xác suất >50%; định nghĩa overshoot và SSP1-1.9 bổ sung khớp bảng tương đương ở trang 81. Bảng này không ghi RCP cho C1.

**Câu hỏi:** In Box SPM.1 Table 1, give the complete description of category C1, including probability and overshoot.

**Đáp án / hành vi chuẩn:** Limit warming to 1.5°C (>50%) with no or limited overshoot.

**Kết quả (answered):** Category C1 (Box SPM.1, Table 1): "limit warming to 1.5°C (>50%) with no or limited overshoot." Probability is >50%. "Limited overshoot" means exceeding 1.5°C global warming by up to about 0.1°C, for up to several decades. GHG emissions scenario: Very low (SSP1-1.9); RCP: the RCP2.6 entry in the table is for the Low (SSP1-2.6) row, so no RCP is listed for C1.

**Vùng bằng chứng chuẩn để kiểm tra:**

```json
[
  {
    "page": 26,
    "bbox": [
      0.06,
      0.03,
      0.94,
      0.43
    ],
    "location": "Box SPM.1 Table 1, C1 row"
  }
]
```

**Citation của agent:**

```json
[
  {
    "region_id": "p081-r1",
    "location": "Panel b table, row C1 (category description 'limit warming to 1.5°C (>50%) with no or limited overshoot'; GHG scenario 'Very low (SSP1-1.9)'); footnote *** defining limited overshoot as up to about 0.1°C for up to several decades",
    "page": 81,
    "bbox": [
      0,
      0,
      1,
      1
    ],
    "source": "https://www.ipcc.ch/report/ar6/syr/downloads/report/IPCC_AR6_SYR_FullVolume.pdf"
  }
]
```

## bt06 — table

**Kết quả chấm đã xác nhận:** Đạt. Đúng C6, 3°C >50%, SSP2-4.5 và RCP4.5; bảng trang 26.

**Câu hỏi:** In Box SPM.1 Table 1, what temperature limit and probability describe category C6?

**Đáp án / hành vi chuẩn:** Limit warming to 3°C (>50%).

**Kết quả (answered):** Category C6 is described as "limit warming to 3°C (>50%)", i.e., a temperature limit of 3°C with a probability greater than 50%. It corresponds to the Intermediate (SSP2-4.5) scenario and RCP 4.5.

**Vùng bằng chứng chuẩn để kiểm tra:**

```json
[
  {
    "page": 26,
    "bbox": [
      0.06,
      0.03,
      0.94,
      0.43
    ],
    "location": "Box SPM.1 Table 1, C6 row"
  }
]
```

**Citation của agent:**

```json
[
  {
    "region_id": "p026-r1",
    "location": "Box SPM.1, Table 1, row C6: category description 'limit warming to 3°C (>50%)'; GHG scenario column 'Intermediate (SSP2-4.5)'; RCPy column 'RCP 4.5'",
    "page": 26,
    "bbox": [
      0,
      0,
      1,
      0.5
    ],
    "source": "https://www.ipcc.ch/report/ar6/syr/downloads/report/IPCC_AR6_SYR_FullVolume.pdf"
  }
]
```

## bt07 — image

**Kết quả chấm đã xác nhận:** Đạt. Đúng hai nhãn Low emissions / Low climate risk; crop nửa phải trang 41 chứa vòng tròn xanh.

**Câu hỏi:** In the upper green outcome circle of Figure SPM.6, what labels describe emissions and climate risk?

**Đáp án / hành vi chuẩn:** Low emissions and low climate risk.

**Kết quả (answered):** In the upper green outcome circle of Figure SPM.6, the emissions label is "Low emissions" and the climate risk label is "Low climate risk."

**Vùng bằng chứng chuẩn để kiểm tra:**

```json
[
  {
    "page": 41,
    "bbox": [
      0.69,
      0.16,
      0.9,
      0.31
    ],
    "location": "Figure SPM.6, upper green outcome circle"
  }
]
```

**Citation của agent:**

```json
[
  {
    "region_id": "p041-r1",
    "location": "Figure SPM.6, right panel, upper green circle 'Outcomes characterising development pathways': 'Low emissions' (first label) and 'Low climate risk' (fourth label)",
    "page": 41,
    "bbox": [
      0.5,
      0.0,
      1.0,
      1.0
    ],
    "source": "https://www.ipcc.ch/report/ar6/syr/downloads/report/IPCC_AR6_SYR_FullVolume.pdf"
  }
]
```

## bt08 — image

**Kết quả chấm đã xác nhận:** Đạt. Đúng ký hiệu shock làm gián đoạn phát triển; chú giải và caption trang 41 hỗ trợ cả ví dụ bổ sung.

**Câu hỏi:** In Figure SPM.6, what does the lightning-like shock symbol represent, according to its legend?

**Đáp án / hành vi chuẩn:** An illustrative shock that disrupts development.

**Kết quả (answered):** According to the Figure SPM.6 legend, the lightning-like shock symbol represents an illustrative 'shock' that disrupts development (e.g., climatic and non-climatic events such as droughts, floods or pandemics).

**Vùng bằng chứng chuẩn để kiểm tra:**

```json
[
  {
    "page": 41,
    "bbox": [
      0.72,
      0.43,
      0.93,
      0.48
    ],
    "location": "Figure SPM.6, shock symbol legend"
  }
]
```

**Citation của agent:**

```json
[
  {
    "region_id": "p041-r1",
    "location": "Figure SPM.6 legend at bottom right of the right panel: 'Illustrative 'shock' that disrupts development' with lightning-like symbol; caption text on shocks from droughts, floods or pandemics",
    "page": 41,
    "bbox": [
      0,
      0,
      1,
      1
    ],
    "source": "https://www.ipcc.ch/report/ar6/syr/downloads/report/IPCC_AR6_SYR_FullVolume.pdf"
  }
]
```

## bt09 — image

**Kết quả chấm đã xác nhận:** Đạt. Đúng chú giải Adverse and positive impacts của vòng tròn sọc; hình SPM.1(a), trang 23.

**Câu hỏi:** In the key of Figure SPM.1(a), what does the diagonally striped red-and-green circle mean?

**Đáp án / hành vi chuẩn:** Adverse and positive impacts.

**Kết quả (answered):** In the Figure SPM.1(a) key, the diagonally striped red-and-green circle means "Adverse and positive impacts" (observed increase in climate impacts to human systems and ecosystems assessed at global level).

**Vùng bằng chứng chuẩn để kiểm tra:**

```json
[
  {
    "page": 23,
    "bbox": [
      0.64,
      0.13,
      0.88,
      0.33
    ],
    "location": "Figure SPM.1(a), icon key"
  }
]
```

**Citation của agent:**

```json
[
  {
    "region_id": "p023-r1",
    "location": "Figure SPM.1(a), Key box (top right): striped red-and-green circle labeled 'Adverse and positive impacts'",
    "page": 23,
    "bbox": [
      0,
      0,
      1,
      1
    ],
    "source": "https://www.ipcc.ch/report/ar6/syr/downloads/report/IPCC_AR6_SYR_FullVolume.pdf"
  }
]
```

## bt10 — image

**Kết quả chấm đã xác nhận:** Đạt. Đúng nhãn 2100 & beyond ở đầu phải trục thời gian; hình SPM.6 trang 41.

**Câu hỏi:** In the pathway diagram of Figure SPM.6, what is the rightmost time label on the horizontal axis?

**Đáp án / hành vi chuẩn:** 2100 and beyond.

**Kết quả (answered):** The rightmost time label on the horizontal axis of the pathway diagram in Figure SPM.6 is "2100 & beyond".

**Vùng bằng chứng chuẩn để kiểm tra:**

```json
[
  {
    "page": 41,
    "bbox": [
      0.62,
      0.42,
      0.74,
      0.48
    ],
    "location": "Figure SPM.6, right end of horizontal time axis"
  }
]
```

**Citation của agent:**

```json
[
  {
    "region_id": "p041-r1",
    "location": "Figure SPM.6, pathway diagram (centre panel), horizontal time axis at bottom-right: rightmost label '2100 & beyond' (after '2030')",
    "page": 41,
    "bbox": [
      0,
      0,
      1,
      1
    ],
    "source": "https://www.ipcc.ch/report/ar6/syr/downloads/report/IPCC_AR6_SYR_FullVolume.pdf"
  }
]
```

## bt11 — image

**Kết quả chấm đã xác nhận:** Đạt. Đúng hai mục Upper ocean acidification và Increase in hot extremes; nhóm Virtually certain, trang 23.

**Câu hỏi:** In Figure SPM.1(b), name the two observed changes placed in the Virtually certain group.

**Đáp án / hành vi chuẩn:** Upper ocean acidification and increase in hot extremes.

**Kết quả (answered):** The two observed changes in the "Virtually certain" group of Figure SPM.1(b) are "Upper ocean acidification (pH)" and "Increase in hot extremes."

**Vùng bằng chứng chuẩn để kiểm tra:**

```json
[
  {
    "page": 23,
    "bbox": [
      0.48,
      0.38,
      0.63,
      0.49
    ],
    "location": "Figure SPM.1(b), rightmost two icons"
  }
]
```

**Citation của agent:**

```json
[
  {
    "region_id": "p023-r1",
    "location": "Figure SPM.1(b), 'Virtually certain' column (rightmost group): 'Upper ocean acidification' (pH icon) and 'Increase in hot extremes' (thermometer icon)",
    "page": 23,
    "bbox": [
      0,
      0,
      1,
      1
    ],
    "source": "https://www.ipcc.ch/report/ar6/syr/downloads/report/IPCC_AR6_SYR_FullVolume.pdf"
  }
]
```

## bt12 — chart

**Kết quả chấm đã xác nhận:** Đạt. Đúng Electricity 73% trước điện khí hóa bổ sung; các giá trị so sánh trong citation đều khớp hình trang 43.

**Câu hỏi:** In Figure SPM.7(b), which sector has the largest annotated percentage reduction before additional electrification, and what is that percentage?

**Đáp án / hành vi chuẩn:** Electricity, 73% before additional electrification.

**Kết quả (answered):** Electricity has the largest annotated reduction before additional electrification: 73% (by 2050, shown in Figure SPM.7(b)).

**Vùng bằng chứng chuẩn để kiểm tra:**

```json
[
  {
    "page": 43,
    "bbox": [
      0.1,
      0.73,
      0.9,
      0.88
    ],
    "location": "Figure SPM.7(b), Electricity bar"
  }
]
```

**Citation của agent:**

```json
[
  {
    "region_id": "p043-r1",
    "location": "Figure SPM.7(b), Electricity row: \"73% reduction (before additional electrification)\" with additional electrification (+60%) marked; other annotated values are Land transport 67%, Buildings 66%, Industry 29%, Food 44%.",
    "page": 43,
    "bbox": [
      0,
      0,
      1,
      1
    ],
    "source": "https://www.ipcc.ch/report/ar6/syr/downloads/report/IPCC_AR6_SYR_FullVolume.pdf"
  }
]
```

## bt13 — chart

**Kết quả chấm đã xác nhận:** Đạt. Đúng Buildings 66%, Food 44%, chênh 22 điểm phần trăm; hình trang 43.

**Câu hỏi:** Using the labelled percentages in Figure SPM.7(b), how many percentage points higher is Buildings demand-side reduction potential than Food? Show both values.

**Đáp án / hành vi chuẩn:** Buildings 66%, Food 44%, difference 22 percentage points.

**Kết quả (answered):** Buildings demand-side reduction potential is 66% and Food is 44% (Figure SPM.7(b), 2050), so Buildings is 22 percentage points higher (66% − 44% = 22 percentage points).

**Vùng bằng chứng chuẩn để kiểm tra:**

```json
[
  {
    "page": 43,
    "bbox": [
      0.1,
      0.73,
      0.9,
      0.88
    ],
    "location": "Figure SPM.7(b), Buildings and Food bars"
  }
]
```

**Citation của agent:**

```json
[
  {
    "region_id": "p043-r2",
    "location": "Figure SPM.7 panel (b), Food row (44%) and Buildings row (66%), 2050 demand-side mitigation potential",
    "page": 43,
    "bbox": [
      0,
      0,
      1,
      1
    ],
    "source": "https://www.ipcc.ch/report/ar6/syr/downloads/report/IPCC_AR6_SYR_FullVolume.pdf"
  }
]
```

## bt14 — chart

**Kết quả chấm đã xác nhận:** Đạt. Đúng khoảng 2400 GtCO2 trong dung sai đã khóa; cột lịch sử và thanh bất định hỗ trợ trên hình 3.5(a), trang 99.

**Câu hỏi:** Read the historical bar in Figure 3.5(a). Approximately how much cumulative CO2 was emitted in 1850–2019? Include units; allow graphical reading within ±100 GtCO2.

**Đáp án / hành vi chuẩn:** Approximately 2400 GtCO2 (acceptable 2300–2500 for graph reading).

**Kết quả (answered):** Reading the historical bar in Figure 3.5(a), cumulative CO2 emissions for 1850–2019 are about 2400 GtCO2 (the bar ends near the 2000–2500 region on the historical axis; the report text gives 2400 ± 240 GtCO2, which is consistent with the graphical reading).

**Vùng bằng chứng chuẩn để kiểm tra:**

```json
[
  {
    "page": 99,
    "bbox": [
      0.11,
      0.16,
      0.85,
      0.29
    ],
    "location": "Figure 3.5(a), historical emissions bar"
  }
]
```

**Citation của agent:**

```json
[
  {
    "region_id": "p099-r1",
    "location": "Figure 3.5(a), 'Historical emissions 1850-2019' bar, read against the cumulative CO2 emissions (GtCO2) historical axis (0–2000 scale, bar ends just left of the 2020 line)",
    "page": 99,
    "bbox": [
      0,
      0,
      1,
      1
    ],
    "source": "https://www.ipcc.ch/report/ar6/syr/downloads/report/IPCC_AR6_SYR_FullVolume.pdf"
  }
]
```

## bt15 — chart

**Kết quả chấm đã xác nhận:** Đạt. Đúng khoảng 500 và 1150 GtCO2, chênh 650; phân biệt đúng thanh 2°C 83% khoảng 900, trang 99.

**Câu hỏi:** In Figure 3.5(a), compare remaining carbon budgets since 2020 for 1.5°C (>50%) and 2°C (>67%). Read approximate central values from the axis, within ±50 GtCO2.

**Đáp án / hành vi chuẩn:** About 500 GtCO2 and 1150 GtCO2 respectively; the 2°C (>67%) budget is larger.

**Kết quả (answered):** From Figure 3.5(a), the remaining carbon budget since 2020 is approximately 500 GtCO2 for 1.5°C (>50% chance) and approximately 1150 GtCO2 for 2°C (>67% chance), so the 2°C budget is about 650 GtCO2 larger (1150 − 500 = 650). The 2°C (83% chance) bar is about 900 GtCO2, as a separate reference.

**Vùng bằng chứng chuẩn để kiểm tra:**

```json
[
  {
    "page": 99,
    "bbox": [
      0.11,
      0.16,
      0.85,
      0.36
    ],
    "location": "Figure 3.5(a), 1.5°C and 2°C (67%) remaining-budget bars"
  }
]
```

**Citation của agent:**

```json
[
  {
    "region_id": "p099-r1",
    "location": "Figure 3.5(a), 'Remaining carbon budgets' bars: 1.5°C (>50% chance) bar ends at ~500 GtCO2 on the since-2020 axis; 2°C (>67% chance) grey bar ends at ~1150 GtCO2; 2°C (83% chance) green bar ends at ~900 GtCO2",
    "page": 99,
    "bbox": [
      0,
      0,
      1,
      1
    ],
    "source": "https://www.ipcc.ch/report/ar6/syr/downloads/report/IPCC_AR6_SYR_FullVolume.pdf"
  },
  {
    "region_id": "p099-r2",
    "location": "Figure 3.5(a) axis 'Cumulative CO2 emissions (GtCO2) since 2020' and 'Carbon budgets' labels for 1.5°C (>50%) and 2°C (83%) dashed lines at ~500 and ~900 GtCO2",
    "page": 99,
    "bbox": [
      0.1,
      0.15,
      0.85,
      0.45
    ],
    "source": "https://www.ipcc.ch/report/ar6/syr/downloads/report/IPCC_AR6_SYR_FullVolume.pdf"
  }
]
```

## bt16 — chart

**Kết quả chấm đã xác nhận:** Không đạt. Không đạt: SSP5-8.5 đúng, nhưng tự thêm SSP2-4.5 khoảng 3300 GtCO2 năm 2050. Hình 3.5(b) trang 99 cho điểm cuối SSP2-4.5 khoảng 3750; chỉ SSP1-2.6 gần 3300. Evidence không hỗ trợ toàn bộ câu trả lời.

**Câu hỏi:** In Figure 3.5(b), which labelled SSP scenario lies furthest to the right, representing the largest cumulative CO2 emissions by 2050?

**Đáp án / hành vi chuẩn:** SSP5-8.5.

**Kết quả (answered):** SSP5-8.5 lies furthest to the right in Figure 3.5(b), with the largest cumulative CO2 emissions by 2050 (its curve extends to about 4,200 GtCO2 since 1850, against about 3,300 GtCO2 for SSP1-2.6 and SSP2-4.5 at the 2050 dashed line).

**Vùng bằng chứng chuẩn để kiểm tra:**

```json
[
  {
    "page": 99,
    "bbox": [
      0.1,
      0.46,
      0.9,
      0.83
    ],
    "location": "Figure 3.5(b), upper right scenario labels"
  }
]
```

**Citation của agent:**

```json
[
  {
    "region_id": "p099-r1",
    "location": "Figure 3.5(b), lower panel: 'SSP5-8.5' label (top-right, red/dark red) and its coloured curve/range extending furthest right on the cumulative CO2 emissions (GtCO2) since 1850 axis",
    "page": 99,
    "bbox": [
      0,
      0,
      1,
      1
    ],
    "source": "https://www.ipcc.ch/report/ar6/syr/downloads/report/IPCC_AR6_SYR_FullVolume.pdf"
  }
]
```

## bt17 — multihop

**Kết quả chấm đã xác nhận:** Không đạt. Không đạt theo cách chấm thận trọng: hai ý chính 0.71°C và GHG 64% đúng, nhưng câu bổ sung gọi 73% là CO2 equivalent median. Bảng trang 37 ghi 73% cho CO2, còn GHG quy đổi CO2-eq là 64%. Cần sinh viên kiểm tra cách diễn đạt này; chưa coi toàn bộ câu trả lời chính xác.

**Câu hỏi:** Combine A.1.1 and Table SPM.1: calculate the difference between central land and ocean warming in 2011–2020 relative to 1850–1900, and give the median GHG reduction by 2050 for 2°C (>67%) pathways.

**Đáp án / hành vi chuẩn:** 1.59−0.88=0.71°C; GHG reduction 64% by 2050 relative to 2019.

**Kết quả (answered):** Land minus ocean warming in 2011–2020 vs 1850–1900: 1.59°C − 0.88°C = 0.71°C (central estimates). Median GHG reduction from 2019 levels by 2050 for limiting warming to 2°C (>67%) is 64% (5–95 percentile range 53–77%); the CO2 equivalent median is 73%.

**Vùng bằng chứng chuẩn để kiểm tra:**

```json
[
  {
    "page": 20,
    "bbox": [
      0.05,
      0.04,
      0.95,
      0.93
    ],
    "location": "A.1.1"
  },
  {
    "page": 37,
    "bbox": [
      0.06,
      0.03,
      0.94,
      0.25
    ],
    "location": "Table SPM.1, 2°C GHG row, 2050 column"
  }
]
```

**Citation của agent:**

```json
[
  {
    "region_id": "p020-r2",
    "location": "A.1.1, central values: land 1.59 [1.34 to 1.83]°C and ocean 0.88 [0.68 to 1.01]°C, 2011–2020 vs 1850–1900",
    "page": 20,
    "bbox": [
      0,
      0,
      1,
      0.5
    ],
    "source": "https://www.ipcc.ch/report/ar6/syr/downloads/report/IPCC_AR6_SYR_FullVolume.pdf"
  },
  {
    "region_id": "p037-r1",
    "location": "Table SPM.1, row 'Limit warming to 2°C (>67%)', GHG row, 2050 column: 64 [53-77]",
    "page": 37,
    "bbox": [
      0,
      0,
      1,
      1
    ],
    "source": "https://www.ipcc.ch/report/ar6/syr/downloads/report/IPCC_AR6_SYR_FullVolume.pdf"
  }
]
```

## bt18 — multihop

**Kết quả chấm đã xác nhận:** Đạt. Đúng 59 × (1−0.43) ≈ 33.6 GtCO2-eq, nêu rõ phép tính minh họa không phải dự báo model hài hòa; crop trang 20 chứa A.1.4 và bảng trang 37.

**Câu hỏi:** For an illustrative arithmetic exercise, combine the central 2019 GHG estimate in A.1.4 with the 2030 median percentage reduction for 1.5°C pathways in Table SPM.1. What emissions remain? State that this is a calculation using the observed estimate, not the harmonised model projection.

**Đáp án / hành vi chuẩn:** 59×(1−0.43)=33.63 GtCO2-eq/year, illustrative only; observed 2019 estimate differs from harmonised model baselines.

**Kết quả (answered):** Illustrative calculation only, using the observed 2019 estimate (not the harmonised model projection): 59 GtCO2-eq × (1 − 0.43) = 33.6 GtCO2-eq remaining in 2030, where 43% is the median reduction from 2019 for 1.5°C (>50%) with no or limited overshoot (GHG, 5–95 percentile range 34–60%). Equivalently, 59 × 0.57 ≈ 33.6 GtCO2-eq.

**Vùng bằng chứng chuẩn để kiểm tra:**

```json
[
  {
    "page": 20,
    "bbox": [
      0.05,
      0.04,
      0.95,
      0.93
    ],
    "location": "A.1.4"
  },
  {
    "page": 37,
    "bbox": [
      0.06,
      0.03,
      0.94,
      0.25
    ],
    "location": "Table SPM.1, 1.5°C GHG row, 2030 column"
  }
]
```

**Citation của agent:**

```json
[
  {
    "region_id": "p020-r2",
    "location": "Paragraph A.1.4: 59 ± 6.6 GtCO2-eq in 2019 (central estimate)",
    "page": 20,
    "bbox": [
      0,
      0,
      1,
      0.6
    ],
    "source": "https://www.ipcc.ch/report/ar6/syr/downloads/report/IPCC_AR6_SYR_FullVolume.pdf"
  },
  {
    "region_id": "p037-r1",
    "location": "Table SPM.1, row 'Limit warming to 1.5°C (>50%) with no or limited overshoot', GHG row, 2030 column: 43 [34-60]",
    "page": 37,
    "bbox": [
      0,
      0,
      1,
      0.5
    ],
    "source": "https://www.ipcc.ch/report/ar6/syr/downloads/report/IPCC_AR6_SYR_FullVolume.pdf"
  }
]
```

## bt19 — multihop

**Kết quả chấm đã xác nhận:** Đạt. Đúng 3.7 [3.2–4.2] mm/năm, 2006–2018, và 0.28–0.55 m năm 2100 với SSP1-1.9, so với 1995–2014; đủ hai vùng trang 21/34.

**Câu hỏi:** Use A.2.1 and B.3.1: state the observed mean sea-level rise rate in 2006–2018, then the likely 2100 rise range under SSP1-1.9, keeping their different reference periods and units.

**Đáp án / hành vi chuẩn:** 3.7 [3.2–4.2] mm/year in 2006–2018; 0.28–0.55 m by 2100 relative to 1995–2014 under SSP1-1.9.

**Kết quả (answered):** Observed average rate of global mean sea level rise was 3.7 [3.2 to 4.2] mm yr⁻¹ between 2006 and 2018 (A.2.1). Relative to 1995–2014, the likely global mean sea level rise under SSP1-1.9 is 0.28–0.55 m by 2100 (B.3.1). The two figures use different reference periods and units: a rate over 2006–2018 in mm/yr, versus a cumulative rise relative to 1995–2014 in metres.

**Vùng bằng chứng chuẩn để kiểm tra:**

```json
[
  {
    "page": 21,
    "bbox": [
      0.05,
      0.04,
      0.95,
      0.93
    ],
    "location": "A.2.1"
  },
  {
    "page": 34,
    "bbox": [
      0.05,
      0.04,
      0.95,
      0.93
    ],
    "location": "B.3.1"
  }
]
```

**Citation của agent:**

```json
[
  {
    "region_id": "p021-r1",
    "location": "A.2.1 text, sentence 'further increasing to 3.7 [3.2 to 4.2] mm yr-1 between 2006 and 2018'",
    "page": 21,
    "bbox": [
      0,
      0.4,
      1,
      0.7
    ],
    "source": "https://www.ipcc.ch/report/ar6/syr/downloads/report/IPCC_AR6_SYR_FullVolume.pdf"
  },
  {
    "region_id": "p034-r2",
    "location": "B.3.1 text, sentence 'Relative to 1995–2014, the likely global mean sea level rise under the SSP1-1.9 ... 0.28–0.55 m by 2100'",
    "page": 34,
    "bbox": [
      0,
      0.2,
      1,
      0.8
    ],
    "source": "https://www.ipcc.ch/report/ar6/syr/downloads/report/IPCC_AR6_SYR_FullVolume.pdf"
  }
]
```

## bt20 — multihop

**Kết quả chấm đã xác nhận:** Đạt. Đúng 85%−55%=30 điểm phần trăm và land transport 67%; trang 69/43 hỗ trợ. Tên mục A.4.2 trong citation trang 69 chưa đúng nhưng đoạn và trang vẫn tìm được chính xác.

**Câu hỏi:** Combine A.4.2 and Figure SPM.7(b): how much more did solar unit costs fall than wind costs in 2010–2019 (percentage points), and what percentage demand-side potential is shown for Land transport in 2050?

**Đáp án / hành vi chuẩn:** Solar fell 85%, wind 55%, difference 30 percentage points; Land transport 67%.

**Kết quả (answered):** Solar unit costs fell 85% and wind unit costs fell 55% from 2010–2019 (Section A.4.2), so solar fell 30 percentage points more than wind. Figure SPM.7(b) shows a demand-side mitigation potential of 67% (percentage of possible reduction) for Land transport by 2050.

**Vùng bằng chứng chuẩn để kiểm tra:**

```json
[
  {
    "page": 27,
    "bbox": [
      0.05,
      0.04,
      0.95,
      0.93
    ],
    "location": "A.4.2 continuation: technology costs"
  },
  {
    "page": 43,
    "bbox": [
      0.1,
      0.73,
      0.9,
      0.88
    ],
    "location": "Figure SPM.7(b), Land transport bar"
  }
]
```

**Citation của agent:**

```json
[
  {
    "region_id": "p069-r2",
    "location": "Section A.4.2 text (page 53 of report): solar energy unit costs decreased by 85%, wind energy by 55%, 2010–2019",
    "page": 69,
    "bbox": [
      0,
      0,
      1,
      1
    ],
    "source": "https://www.ipcc.ch/report/ar6/syr/downloads/report/IPCC_AR6_SYR_FullVolume.pdf"
  },
  {
    "region_id": "p043-r1",
    "location": "Figure SPM.7(b), 'Potential of demand-side mitigation options by 2050': Land transport bar labelled 67%",
    "page": 43,
    "bbox": [
      0,
      0,
      1,
      1
    ],
    "source": "https://www.ipcc.ch/report/ar6/syr/downloads/report/IPCC_AR6_SYR_FullVolume.pdf"
  }
]
```

## bt21 — text

**Kết quả chấm đã xác nhận:** Đạt. Đúng nhóm 10% đóng góp 34–45% và nhóm 50% thấp nhất 13–15%, phát thải hộ gia đình theo tiêu dùng; A.1.5 trang 21.

**Câu hỏi:** According to A.1.5, what shares of consumption-based household GHG emissions come from the top 10% and bottom 50% of households ranked by per-capita emissions?

**Đáp án / hành vi chuẩn:** Top 10%: 34–45%; bottom 50%: 13–15%.

**Kết quả (answered):** According to A.1.5, the 10% of households with the highest per capita emissions contribute 34–45% of global consumption-based household GHG emissions, and the bottom 50% contribute 13–15%.

**Vùng bằng chứng chuẩn để kiểm tra:**

```json
[
  {
    "page": 21,
    "bbox": [
      0.05,
      0.04,
      0.95,
      0.93
    ],
    "location": "A.1.5"
  }
]
```

**Citation của agent:**

```json
[
  {
    "region_id": "p021-r1",
    "location": "Section A.1.5, final sentences of the paragraph (SPM page 21): 'The 10% of households with the highest per capita emissions contribute 34–45%... while the bottom 50% contribute 13–15%.'",
    "page": 21,
    "bbox": [
      0,
      0,
      1,
      0.5
    ],
    "source": "https://www.ipcc.ch/report/ar6/syr/downloads/report/IPCC_AR6_SYR_FullVolume.pdf"
  }
]
```

## bt22 — text

**Kết quả chấm đã xác nhận:** Đạt. Đúng 3.3–3.6 tỷ người; A.2.2 trang 21.

**Câu hỏi:** According to A.2.2, approximately how many people live in contexts highly vulnerable to climate change?

**Đáp án / hành vi chuẩn:** 3.3–3.6 billion people.

**Kết quả (answered):** According to A.2.2, approximately 3.3 to 3.6 billion people live in contexts that are highly vulnerable to climate change.

**Vùng bằng chứng chuẩn để kiểm tra:**

```json
[
  {
    "page": 21,
    "bbox": [
      0.05,
      0.04,
      0.95,
      0.93
    ],
    "location": "A.2.2"
  }
]
```

**Citation của agent:**

```json
[
  {
    "region_id": "p021-r1",
    "location": "Summary for Policymakers, page 5 (PDF p.21), paragraph A.2.2, first sentence",
    "page": 21,
    "bbox": [
      0,
      0,
      1,
      1
    ],
    "source": "https://www.ipcc.ch/report/ar6/syr/downloads/report/IPCC_AR6_SYR_FullVolume.pdf"
  }
]
```

## bt23 — text

**Kết quả chấm đã xác nhận:** Đạt. Đúng ít nhất 170 quốc gia và nhiều thành phố; A.3.1 trong crop trang 24.

**Câu hỏi:** In A.3.1, at least how many countries include adaptation in climate policies and planning processes?

**Đáp án / hành vi chuẩn:** At least 170 countries.

**Kết quả (answered):** At least 170 countries (plus many cities) have included adaptation in their climate policies and planning processes (high confidence), per A.3.1.

**Vùng bằng chứng chuẩn để kiểm tra:**

```json
[
  {
    "page": 24,
    "bbox": [
      0.05,
      0.04,
      0.95,
      0.93
    ],
    "location": "A.3.1"
  }
]
```

**Citation của agent:**

```json
[
  {
    "region_id": "p024-r4",
    "location": "A.3.1 text, Summary for Policymakers page 8 (PDF page 24), sentence 'resulted in at least 170 countries and many cities including adaptation in their climate policies and planning processes'",
    "page": 24,
    "bbox": [
      0,
      0,
      1,
      0.6
    ],
    "source": "https://www.ipcc.ch/report/ar6/syr/downloads/report/IPCC_AR6_SYR_FullVolume.pdf"
  }
]
```

## bt24 — text

**Kết quả chấm đã xác nhận:** Đạt. Đúng methane giảm 34% [21–57] năm 2030 so với 2019, 1.5°C >50% không/vượt ít; B.6.2 trang 37.

**Câu hỏi:** According to B.6.2, by what median percentage and interval do 1.5°C (>50%, no/limited overshoot) pathways reduce global methane emissions by 2030 relative to 2019?

**Đáp án / hành vi chuẩn:** 34% [21–57%].

**Kết quả (answered):** In modelled pathways limiting warming to 1.5°C (>50%) with no or limited overshoot, global methane emissions are reduced by a median of 34% by 2030 relative to 2019, with a 5–95 percentile range of 21–57%.

**Vùng bằng chứng chuẩn để kiểm tra:**

```json
[
  {
    "page": 37,
    "bbox": [
      0.05,
      0.04,
      0.95,
      0.93
    ],
    "location": "B.6.2 below Table SPM.1"
  }
]
```

**Citation của agent:**

```json
[
  {
    "region_id": "p037-r1",
    "location": "Section B.6.2 text (SPM p.21): 'global methane emissions are reduced by 34 [21–57]% by 2030 relative to 2019' for 1.5°C (>50%) with no or limited overshoot",
    "page": 37,
    "bbox": [
      0,
      0,
      1,
      1
    ],
    "source": "https://www.ipcc.ch/report/ar6/syr/downloads/report/IPCC_AR6_SYR_FullVolume.pdf"
  }
]
```

## bt25 — unanswerable

**Kết quả chấm đã xác nhận:** Đạt. Từ chối, không suy đoán. Rà toàn bộ text không thấy Viet Nam/Vietnam; báo cáo tổng hợp toàn cầu không cung cấp tổng CO2 quốc gia chính xác năm 2031.

**Câu hỏi:** What exact 2031 CO2 emissions total in tonnes does this report forecast for Viet Nam?

**Đáp án / hành vi chuẩn:** No exact national 2031 total for Viet Nam.

**Kết quả (abstain):** Không đủ bằng chứng trong báo cáo để trả lời chính xác.

**Vùng bằng chứng chuẩn để kiểm tra:**

```json
[]
```

**Citation của agent:**

```json
[]
```

## bt26 — unanswerable

**Kết quả chấm đã xác nhận:** Đạt. Từ chối, không suy đoán. Rà toàn bộ text không thấy District 7/Ho Chi Minh; không có độ sâu ngập quận 7 năm 2050.

**Câu hỏi:** What exact 2050 flood-water depth in metres does the report give for District 7, Ho Chi Minh City?

**Đáp án / hành vi chuẩn:** No District 7 specific flood-depth value for 2050.

**Kết quả (abstain):** Không đủ bằng chứng trong báo cáo để trả lời chính xác.

**Vùng bằng chứng chuẩn để kiểm tra:**

```json
[]
```

**Citation của agent:**

```json
[]
```

## bt27 — unanswerable

**Kết quả chấm đã xác nhận:** Đạt. Từ chối, không suy đoán. Rà toàn bộ text không thấy Hanoi/Ha Noi; không có tổng mưa Hà Nội năm 2037.

**Câu hỏi:** What exact rainfall total in millimetres does the report give for Hanoi in 2037?

**Đáp án / hành vi chuẩn:** No Hanoi 2037 rainfall total.

**Kết quả (abstain):** Không đủ bằng chứng trong báo cáo để trả lời chính xác.

**Vùng bằng chứng chuẩn để kiểm tra:**

```json
[]
```

**Citation của agent:**

```json
[]
```

## bt28 — unanswerable

**Kết quả chấm đã xác nhận:** Đạt. Từ chối đúng. Không có SSP6-12.0 trong toàn bộ text; đối chiếu danh sách kịch bản bảng trang 26/81.

**Câu hỏi:** What exact median 2100 global warming is reported for a scenario named SSP6-12.0?

**Đáp án / hành vi chuẩn:** This named scenario is not provided in the report.

**Kết quả (abstain):** Không đủ bằng chứng trong báo cáo để trả lời chính xác.

**Vùng bằng chứng chuẩn để kiểm tra:**

```json
[]
```

**Citation của agent:**

```json
[]
```

## bt29 — unanswerable

**Kết quả chấm đã xác nhận:** Đạt. Từ chối đúng. Bảng SPM.1 trang 37 chỉ có các cột 2030/2035/2040/2050, không có 2032; không nội suy.

**Câu hỏi:** In Table SPM.1, what exact 2032 median GHG reduction is explicitly tabulated for 1.5°C pathways? Do not interpolate.

**Đáp án / hành vi chuẩn:** No 2032 column; 2030, 2035, 2040 and 2050 are tabulated.

**Kết quả (abstain):** Không đủ bằng chứng trong báo cáo để trả lời chính xác.

**Vùng bằng chứng chuẩn để kiểm tra:**

```json
[]
```

**Citation của agent:**

```json
[]
```

## bt30 — unanswerable

**Kết quả chấm đã xác nhận:** Đạt. Từ chối, không suy đoán. Rà toàn bộ text không thấy Hue/Huế; tài liệu không cung cấp địa chỉ sơ tán cụ thể tại Huế năm 2050.

**Câu hỏi:** What street address does the report specify as the evacuation destination for residents of Hue during a 2050 climate flood?

**Đáp án / hành vi chuẩn:** No street-level evacuation destination in Hue for a 2050 flood.

**Kết quả (abstain):** Không đủ bằng chứng trong báo cáo để trả lời chính xác.

**Vùng bằng chứng chuẩn để kiểm tra:**

```json
[]
```

**Citation của agent:**

```json
[]
```

