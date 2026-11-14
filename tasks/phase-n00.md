# N00 task cards

Generated from docs/product/AI/backlog.json. Grouping is navigation only; dependencies below determine dispatch. No phase-level edges. All future work requires separate authorization.

## [N00-01] Authorization at use time, no forbidden data to consumers

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

Enabler; linked predecessors define bounded output.

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Measured evidence: NFR-01

**Phụ thuộc:**

P10-03, B00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/NFR-01.md

**Các bước cụ thể:**

1. Đóng băng đề cương NFR-01: Authorization at use time, no forbidden data to consumers; giữ ngưỡng Mandatory deny invariants; universal detection not proven, để mở số chưa quyết định.
2. Thiết kế phép đo riêng theo E02 + IT-01/02/03: fixture có quyền dùng, đồng hồ/tài nguyên, điều kiện chạy và case âm; ghi lệnh do bootstrap B00-01 cung cấp.
3. Sau khi được cho chạy, ghi toàn bộ mẫu, lỗi và kết quả trong docs/acceptance/NFR-01.md; so với ngưỡng không đổi, ghi NOT RUN khi chưa chạy và không dùng thời gian giả thay phiên 8 giờ thật.

**Tiêu chí nghiệm thu:**

- [ ] AT-N00-01-01: Authorization at use time, no forbidden data to consumers; Mandatory deny invariants; universal detection not proven; use E02 + IT-01/02/03. Record actual measurement, environment and failing/unsupported cases; no target promoted into achieved result.
- [ ] AT-N00-01-02: Approve thresholds only from confirmed requirements or explicit evidence-backed user choice; unknown numeric budgets remain blocked. Record positive/negative cases and real command from bootstrap owner before Ready.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-01", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-01

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

NFR-01

## [N00-02] Reaction latency measured end-to-end under actual combined load

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

Enabler; linked predecessors define bounded output.

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Measured evidence: NFR-02

**Phụ thuộc:**

P03-03, B00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/NFR-02.md

**Các bước cụ thể:**

1. Đóng băng đề cương NFR-02: Reaction latency measured end-to-end under actual combined load; giữ ngưỡng XP02 target<1s clear attended scenes; pass-rate/accuracy open D-04, để mở số chưa quyết định.
2. Thiết kế phép đo riêng theo E04 + IT-10: fixture có quyền dùng, đồng hồ/tài nguyên, điều kiện chạy và case âm; ghi lệnh do bootstrap B00-01 cung cấp.
3. Sau khi được cho chạy, ghi toàn bộ mẫu, lỗi và kết quả trong docs/acceptance/NFR-02.md; so với ngưỡng không đổi, ghi NOT RUN khi chưa chạy và không dùng thời gian giả thay phiên 8 giờ thật.

**Tiêu chí nghiệm thu:**

- [ ] AT-N00-02-01: Reaction latency measured end-to-end under actual combined load; XP02 target<1s clear attended scenes; pass-rate/accuracy open D-04; use E04 + IT-10. Record actual measurement, environment and failing/unsupported cases; no target promoted into achieved result.
- [ ] AT-N00-02-02: Approve thresholds only from confirmed requirements or explicit evidence-backed user choice; unknown numeric budgets remain blocked. Record positive/negative cases and real command from bootstrap owner before Ready.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-01", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-01

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

NFR-02

## [N00-03] Stability with both modes and daily-use mix

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

Enabler; linked predecessors define bounded output.

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Measured evidence: NFR-03

**Phụ thuộc:**

P60-03, B00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/NFR-03.md

**Các bước cụ thể:**

1. Đóng băng đề cương NFR-03: Stability with both modes and daily-use mix; giữ ngưỡng About8h required; CPU/RAM/VRAM budgets open D-04, để mở số chưa quyết định.
2. Thiết kế phép đo riêng theo E05 + IT-19: fixture có quyền dùng, đồng hồ/tài nguyên, điều kiện chạy và case âm; ghi lệnh do bootstrap B00-01 cung cấp.
3. Sau khi được cho chạy, ghi toàn bộ mẫu, lỗi và kết quả trong docs/acceptance/NFR-03.md; so với ngưỡng không đổi, ghi NOT RUN khi chưa chạy và không dùng thời gian giả thay phiên 8 giờ thật.

**Tiêu chí nghiệm thu:**

- [ ] AT-N00-03-01: Stability with both modes and daily-use mix; About8h required; CPU/RAM/VRAM budgets open D-04; use E05 + IT-19. Record actual measurement, environment and failing/unsupported cases; no target promoted into achieved result.
- [ ] AT-N00-03-02: Approve thresholds only from confirmed requirements or explicit evidence-backed user choice; unknown numeric budgets remain blocked. Record positive/negative cases and real command from bootstrap owner before Ready.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-01", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-01

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

NFR-03

## [N00-04] Core/local content offline after packages installed

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

Enabler; linked predecessors define bounded output.

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Measured evidence: NFR-04

**Phụ thuộc:**

P60-03, B00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/NFR-04.md

**Các bước cụ thể:**

1. Đóng băng đề cương NFR-04: Core/local content offline after packages installed; giữ ngưỡng No silent network/cloud dependency, để mở số chưa quyết định.
2. Thiết kế phép đo riêng theo IT-11: fixture có quyền dùng, đồng hồ/tài nguyên, điều kiện chạy và case âm; ghi lệnh do bootstrap B00-01 cung cấp.
3. Sau khi được cho chạy, ghi toàn bộ mẫu, lỗi và kết quả trong docs/acceptance/NFR-04.md; so với ngưỡng không đổi, ghi NOT RUN khi chưa chạy và không dùng thời gian giả thay phiên 8 giờ thật.

**Tiêu chí nghiệm thu:**

- [ ] AT-N00-04-01: Core/local content offline after packages installed; No silent network/cloud dependency; use IT-11. Record actual measurement, environment and failing/unsupported cases; no target promoted into achieved result.
- [ ] AT-N00-04-02: Approve thresholds only from confirmed requirements or explicit evidence-backed user choice; unknown numeric budgets remain blocked. Record positive/negative cases and real command from bootstrap owner before Ready.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-01", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-01

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

NFR-04

## [N00-05] Durable local state and authenticated export/import

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

Enabler; linked predecessors define bounded output.

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Measured evidence: NFR-05

**Phụ thuộc:**

P50-04, B00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/NFR-05.md

**Các bước cụ thể:**

1. Đóng băng đề cương NFR-05: Durable local state and authenticated export/import; giữ ngưỡng No corruption/data loss in defined recovery cases; format/crypto open D-07/09, để mở số chưa quyết định.
2. Thiết kế phép đo riêng theo IT-14/15: fixture có quyền dùng, đồng hồ/tài nguyên, điều kiện chạy và case âm; ghi lệnh do bootstrap B00-01 cung cấp.
3. Sau khi được cho chạy, ghi toàn bộ mẫu, lỗi và kết quả trong docs/acceptance/NFR-05.md; so với ngưỡng không đổi, ghi NOT RUN khi chưa chạy và không dùng thời gian giả thay phiên 8 giờ thật.

**Tiêu chí nghiệm thu:**

- [ ] AT-N00-05-01: Durable local state and authenticated export/import; No corruption/data loss in defined recovery cases; format/crypto open D-07/09; use IT-14/15. Record actual measurement, environment and failing/unsupported cases; no target promoted into achieved result.
- [ ] AT-N00-05-02: Approve thresholds only from confirmed requirements or explicit evidence-backed user choice; unknown numeric budgets remain blocked. Record positive/negative cases and real command from bootstrap owner before Ready.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-01", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-01

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

NFR-05

## [N00-06] Clear accessible UI and retained input priority

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

Enabler; linked predecessors define bounded output.

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Measured evidence: NFR-06

**Phụ thuộc:**

P40-01, B00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/NFR-06.md

**Các bước cụ thể:**

1. Đóng băng đề cương NFR-06: Clear accessible UI and retained input priority; giữ ngưỡng Vietnamese, focus and cancel semantics; native accessibility matrix to measure, để mở số chưa quyết định.
2. Thiết kế phép đo riêng theo IT-06/20: fixture có quyền dùng, đồng hồ/tài nguyên, điều kiện chạy và case âm; ghi lệnh do bootstrap B00-01 cung cấp.
3. Sau khi được cho chạy, ghi toàn bộ mẫu, lỗi và kết quả trong docs/acceptance/NFR-06.md; so với ngưỡng không đổi, ghi NOT RUN khi chưa chạy và không dùng thời gian giả thay phiên 8 giờ thật.

**Tiêu chí nghiệm thu:**

- [ ] AT-N00-06-01: Clear accessible UI and retained input priority; Vietnamese, focus and cancel semantics; native accessibility matrix to measure; use IT-06/20. Record actual measurement, environment and failing/unsupported cases; no target promoted into achieved result.
- [ ] AT-N00-06-02: Approve thresholds only from confirmed requirements or explicit evidence-backed user choice; unknown numeric budgets remain blocked. Record positive/negative cases and real command from bootstrap owner before Ready.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-01", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-01

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

NFR-06

## [N00-07] Maintainable module boundaries and reproducible builds

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

Enabler; linked predecessors define bounded output.

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Measured evidence: NFR-07

**Phụ thuộc:**

P00-02, B00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/NFR-07.md

**Các bước cụ thể:**

1. Đóng băng đề cương NFR-07: Maintainable module boundaries and reproducible builds; giữ ngưỡng Pinned real versions, no suppressions to hide failure; CI not installed, để mở số chưa quyết định.
2. Thiết kế phép đo riêng theo P00-02/P60-02: fixture có quyền dùng, đồng hồ/tài nguyên, điều kiện chạy và case âm; ghi lệnh do bootstrap B00-01 cung cấp.
3. Sau khi được cho chạy, ghi toàn bộ mẫu, lỗi và kết quả trong docs/acceptance/NFR-07.md; so với ngưỡng không đổi, ghi NOT RUN khi chưa chạy và không dùng thời gian giả thay phiên 8 giờ thật.

**Tiêu chí nghiệm thu:**

- [ ] AT-N00-07-01: Maintainable module boundaries and reproducible builds; Pinned real versions, no suppressions to hide failure; CI not installed; use P00-02/P60-02. Record actual measurement, environment and failing/unsupported cases; no target promoted into achieved result.
- [ ] AT-N00-07-02: Approve thresholds only from confirmed requirements or explicit evidence-backed user choice; unknown numeric budgets remain blocked. Record positive/negative cases and real command from bootstrap owner before Ready.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-01", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-01

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

NFR-07

## [N00-08] Trustworthy installs/updates and explicit costs

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

Enabler; linked predecessors define bounded output.

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Measured evidence: NFR-08

**Phụ thuộc:**

P50-07, B00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/NFR-08.md

**Các bước cụ thể:**

1. Đóng băng đề cương NFR-08: Trustworthy installs/updates and explicit costs; giữ ngưỡng Signature/distribution choice open D-13; user consent before install/restart, để mở số chưa quyết định.
2. Thiết kế phép đo riêng theo IT-16: fixture có quyền dùng, đồng hồ/tài nguyên, điều kiện chạy và case âm; ghi lệnh do bootstrap B00-01 cung cấp.
3. Sau khi được cho chạy, ghi toàn bộ mẫu, lỗi và kết quả trong docs/acceptance/NFR-08.md; so với ngưỡng không đổi, ghi NOT RUN khi chưa chạy và không dùng thời gian giả thay phiên 8 giờ thật.

**Tiêu chí nghiệm thu:**

- [ ] AT-N00-08-01: Trustworthy installs/updates and explicit costs; Signature/distribution choice open D-13; user consent before install/restart; use IT-16. Record actual measurement, environment and failing/unsupported cases; no target promoted into achieved result.
- [ ] AT-N00-08-02: Approve thresholds only from confirmed requirements or explicit evidence-backed user choice; unknown numeric budgets remain blocked. Record positive/negative cases and real command from bootstrap owner before Ready.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-01", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-01

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

NFR-08

## [N00-09] Minimal local diagnostic data

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

Enabler; linked predecessors define bounded output.

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Measured evidence: NFR-09

**Phụ thuộc:**

P50-05, B00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/NFR-09.md

**Các bước cụ thể:**

1. Đóng băng đề cương NFR-09: Minimal local diagnostic data; giữ ngưỡng BH13 retention30days, no secrets/raw screen, no auto telemetry, để mở số chưa quyết định.
2. Thiết kế phép đo riêng theo IT-17: fixture có quyền dùng, đồng hồ/tài nguyên, điều kiện chạy và case âm; ghi lệnh do bootstrap B00-01 cung cấp.
3. Sau khi được cho chạy, ghi toàn bộ mẫu, lỗi và kết quả trong docs/acceptance/NFR-09.md; so với ngưỡng không đổi, ghi NOT RUN khi chưa chạy và không dùng thời gian giả thay phiên 8 giờ thật.

**Tiêu chí nghiệm thu:**

- [ ] AT-N00-09-01: Minimal local diagnostic data; BH13 retention30days, no secrets/raw screen, no auto telemetry; use IT-17. Record actual measurement, environment and failing/unsupported cases; no target promoted into achieved result.
- [ ] AT-N00-09-02: Approve thresholds only from confirmed requirements or explicit evidence-backed user choice; unknown numeric budgets remain blocked. Record positive/negative cases and real command from bootstrap owner before Ready.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-01", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-01

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

NFR-09

## [N00-10] Correct coordinates and visuals across chosen monitors/DPI

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

Enabler; linked predecessors define bounded output.

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Measured evidence: NFR-10

**Phụ thuộc:**

P20-05, B00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/NFR-10.md

**Các bước cụ thể:**

1. Đóng băng đề cương NFR-10: Correct coordinates and visuals across chosen monitors/DPI; giữ ngưỡng No assumed universal fullscreen; support matrix after E-INT, để mở số chưa quyết định.
2. Thiết kế phép đo riêng theo IT-04/05: fixture có quyền dùng, đồng hồ/tài nguyên, điều kiện chạy và case âm; ghi lệnh do bootstrap B00-01 cung cấp.
3. Sau khi được cho chạy, ghi toàn bộ mẫu, lỗi và kết quả trong docs/acceptance/NFR-10.md; so với ngưỡng không đổi, ghi NOT RUN khi chưa chạy và không dùng thời gian giả thay phiên 8 giờ thật.

**Tiêu chí nghiệm thu:**

- [ ] AT-N00-10-01: Correct coordinates and visuals across chosen monitors/DPI; No assumed universal fullscreen; support matrix after E-INT; use IT-04/05. Record actual measurement, environment and failing/unsupported cases; no target promoted into achieved result.
- [ ] AT-N00-10-02: Approve thresholds only from confirmed requirements or explicit evidence-backed user choice; unknown numeric budgets remain blocked. Record positive/negative cases and real command from bootstrap owner before Ready.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-01", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-01

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

NFR-10
