# V00 task cards

Generated from docs/product/AI/backlog.json. Grouping is navigation only; dependencies below determine dispatch. No phase-level edges. All future work requires separate authorization.

## [V00-001] Clause acceptance: SP01

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

SP01

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-SP01

**Phụ thuộc:**

P30-02, B00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/SP01.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của SP01 từ source_text trong requirements.json vào bảng case cho AT-SP01; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P30-02 với tiêu chí: Qua kịch bản chăm sóc, nghỉ và thay đổi chú ý, quyết định hoạt động có nguyên nhân từ trạng thái; không chỉ lặp một playlist hoạt ảnh. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-01, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/SP01.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-001-01: Qua kịch bản chăm sóc, nghỉ và thay đổi chú ý, quyết định hoạt động có nguyên nhân từ trạng thái; không chỉ lặp một playlist hoạt ảnh.
- [ ] AT-V00-001-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

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

See linked requirement / prerequisite scope.

## [V00-002] Clause acceptance: SP02

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

SP02

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-SP02

**Phụ thuộc:**

P60-01, B00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/SP02.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của SP02 từ source_text trong requirements.json vào bảng case cho AT-SP02; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P60-01 với tiêu chí: Dùng thử một luồng kết hợp sinh hoạt, ghi nhớ, hiểu ngữ cảnh và chuyển động; từng demo riêng không thay nghiệm thu luồng kết hợp. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-01, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/SP02.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-002-01: Dùng thử một luồng kết hợp sinh hoạt, ghi nhớ, hiểu ngữ cảnh và chuyển động; từng demo riêng không thay nghiệm thu luồng kết hợp.
- [ ] AT-V00-002-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

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

See linked requirement / prerequisite scope.

## [V00-003] Clause acceptance: SP03

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

SP03

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-SP03

**Phụ thuộc:**

P50-06, B00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/SP03.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của SP03 từ source_text trong requirements.json vào bảng case cho AT-SP03; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P60-04 với tiêu chí: Cài/chạy bản tiếng Việt trên Windows11; checklist phát hành ghi miễn phí bản đầu và không công khai source; chưa suy ra hỗ trợ OS khác. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-01, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/SP03.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-003-01: Cài/chạy bản tiếng Việt trên Windows11; checklist phát hành ghi miễn phí bản đầu và không công khai source; chưa suy ra hỗ trợ OS khác.
- [ ] AT-V00-003-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

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

See linked requirement / prerequisite scope.

## [V00-004] Clause acceptance: SP04

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

SP04

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-SP04

**Phụ thuộc:**

P40-01, B00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/SP04.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của SP04 từ source_text trong requirements.json vào bảng case cho AT-SP04; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P40-01 với tiêu chí: Cài mới dùng được không đăng ký; kiểm data local và dịch vụ AI ngoài chỉ dùng thông tin kết nối người dùng cung cấp. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-01, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/SP04.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-004-01: Cài mới dùng được không đăng ký; kiểm data local và dịch vụ AI ngoài chỉ dùng thông tin kết nối người dùng cung cấp.
- [ ] AT-V00-004-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

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

See linked requirement / prerequisite scope.

## [V00-005] Clause acceptance: SP05

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

SP05

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-SP05

**Phụ thuộc:**

P60-03, B00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/SP05.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của SP05 từ source_text trong requirements.json vào bảng case cho AT-SP05; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P60-03 với tiêu chí: Không đóng cổng phát hành nếu một trong hai mức chưa đạt tiêu chí; bản nội bộ được dán nhãn khác bản công khai. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-01, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/SP05.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-005-01: Không đóng cổng phát hành nếu một trong hai mức chưa đạt tiêu chí; bản nội bộ được dán nhãn khác bản công khai.
- [ ] AT-V00-005-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

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

See linked requirement / prerequisite scope.

## [V00-006] Clause acceptance: SP06

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

SP06

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-SP06

**Phụ thuộc:**

P00-04, B00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/SP06.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của SP06 từ source_text trong requirements.json vào bảng case cho AT-SP06; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P00-04 với tiêu chí: Danh mục công cụ ghi chi phí/giấy phép; khoản phí không được mua hoặc kích hoạt khi chưa có quyết định người dùng. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-01, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/SP06.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-006-01: Danh mục công cụ ghi chi phí/giấy phép; khoản phí không được mua hoặc kích hoạt khi chưa có quyết định người dùng.
- [ ] AT-V00-006-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

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

See linked requirement / prerequisite scope.

## [V00-007] Clause acceptance: SP07

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

SP07

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-SP07

**Phụ thuộc:**

P30-06, B00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/SP07.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của SP07 từ source_text trong requirements.json vào bảng case cho AT-SP07; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P30-06 với tiêu chí: Cùng trải nghiệm qua thời gian tạo cách biểu hiện cân nhắc hơn ở nâng cao; vẫn có tò mò/tinh nghịch/ý muốn riêng, cơ bản không tiến hóa tính cách. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-01, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/SP07.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-007-01: Cùng trải nghiệm qua thời gian tạo cách biểu hiện cân nhắc hơn ở nâng cao; vẫn có tò mò/tinh nghịch/ý muốn riêng, cơ bản không tiến hóa tính cách.
- [ ] AT-V00-007-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

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

See linked requirement / prerequisite scope.

## [V00-008] Clause acceptance: SP08

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

SP08

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-SP08

**Phụ thuộc:**

P30-02, B00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/SP08.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của SP08 từ source_text trong requirements.json vào bảng case cho AT-SP08; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P30-02 với tiêu chí: Không có nút đánh giá hành vi; bỏ qua lời rủ không thành lời phê bình; learning-demo chỉ ghi khi user bật. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-01, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/SP08.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-008-01: Không có nút đánh giá hành vi; bỏ qua lời rủ không thành lời phê bình; learning-demo chỉ ghi khi user bật.
- [ ] AT-V00-008-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

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

See linked requirement / prerequisite scope.

## [V00-009] Clause acceptance: SP09

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

SP09

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-SP09

**Phụ thuộc:**

P00-02, B00-01, P02-05, P40-05

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/SP09.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của SP09 từ source_text trong requirements.json vào bảng case cho AT-SP09; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P00-02 với tiêu chí: Rà phân công Unity/host/WPF/localAI; không đưa web UI làm nền sản phẩm hoặc coi IPC/model đã chứng minh từ sơ đồ. Kiểm cả nhánh cho phép và từ chối: Hình ảnh lỗi thì tạm dừng thao tác lên app khác; phục hồi vẫn tạm dừng và hỏi trước tiếp tục, kiểm quyền/an toàn mới. Không phát lại mù quáng; hợp đồng kết nối/mất kết nối còn mở. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-01, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/SP09.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-009-01: Rà phân công Unity/host/WPF/localAI; không đưa web UI làm nền sản phẩm hoặc coi IPC/model đã chứng minh từ sơ đồ. Kiểm cả nhánh cho phép và từ chối: Hình ảnh lỗi thì tạm dừng thao tác lên app khác; phục hồi vẫn tạm dừng và hỏi trước tiếp tục, kiểm quyền/an toàn mới. Không phát lại mù quáng; hợp đồng kết nối/mất kết nối còn mở.
- [ ] AT-V00-009-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

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

See linked requirement / prerequisite scope.

## [V00-010] Clause acceptance: NV01

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

desktop-body

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

NV01

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-NV01

**Phụ thuộc:**

P20-01, B00-02

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/NV01.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của NV01 từ source_text trong requirements.json vào bảng case cho AT-NV01; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P20-01 với tiêu chí: Duyệt mẫu nữ trưởng thành chibi đầu lớn người nhỏ; cài mới các user có cùng ngoại hình đã duyệt. Kiểm cả nhánh cho phép và từ chối: Nhân vật chính chủ yếu hình người về mặt/dáng/đi đứng, không mõm cáo/bàn chân động vật. Chỉ đôi tai cáo trên đầu, không tai người; tai trắng bạc lòng hồng nhạt; một đuôi cáo trắng bạc. Giữ nữ trưởng thành chibi anime pixel 128x128, tóc trắng bạc ngang eo/mái thưa, mắt đỏ hồng, da sáng ấm, áo len rộng cổ tròn hồng nhạt, váy xếp ly xám đậm trên gối, chân trần, kẹp tim đỏ rượu bên phải nhân vật. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-02, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/NV01.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-010-01: Duyệt mẫu nữ trưởng thành chibi đầu lớn người nhỏ; cài mới các user có cùng ngoại hình đã duyệt. Kiểm cả nhánh cho phép và từ chối: Nhân vật chính chủ yếu hình người về mặt/dáng/đi đứng, không mõm cáo/bàn chân động vật. Chỉ đôi tai cáo trên đầu, không tai người; tai trắng bạc lòng hồng nhạt; một đuôi cáo trắng bạc. Giữ nữ trưởng thành chibi anime pixel 128x128, tóc trắng bạc ngang eo/mái thưa, mắt đỏ hồng, da sáng ấm, áo len rộng cổ tròn hồng nhạt, váy xếp ly xám đậm trên gối, chân trần, kẹp tim đỏ rượu bên phải nhân vật.
- [ ] AT-V00-010-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-02", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-02

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-011] Clause acceptance: NV02

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

desktop-body

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

NV02

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-NV02

**Phụ thuộc:**

P20-01, B00-02

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/NV02.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của NV02 từ source_text trong requirements.json vào bảng case cho AT-NV02; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P20-01 với tiêu chí: So mẫu front/side với tóc bạc ngang eo, mái thưa, mắt đỏ hồng và da sáng ấm; ghi sửa nếu lệch. Kiểm cả nhánh cho phép và từ chối: Giữ tóc/mắt/da đã chốt; tai trắng bạc lòng hồng nhạt và một đuôi trắng bạc đồng bộ tóc. Chỉ tai cáo, không tai người; không thay ngoại hình đã duyệt. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-02, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/NV02.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-011-01: So mẫu front/side với tóc bạc ngang eo, mái thưa, mắt đỏ hồng và da sáng ấm; ghi sửa nếu lệch. Kiểm cả nhánh cho phép và từ chối: Giữ tóc/mắt/da đã chốt; tai trắng bạc lòng hồng nhạt và một đuôi trắng bạc đồng bộ tóc. Chỉ tai cáo, không tai người; không thay ngoại hình đã duyệt.
- [ ] AT-V00-011-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-02", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-02

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-012] Clause acceptance: NV03

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

desktop-body

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

NV03

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-NV03

**Phụ thuộc:**

P20-01, B00-02

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/NV03.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của NV03 từ source_text trong requirements.json vào bảng case cho AT-NV03; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P20-01 với tiêu chí: Kiểm áo len rộng cổ tròn hồng nhạt, váy xếp ly xám đậm trên gối, không tất/giày ở mọi hướng. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-02, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/NV03.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-012-01: Kiểm áo len rộng cổ tròn hồng nhạt, váy xếp ly xám đậm trên gối, không tất/giày ở mọi hướng.
- [ ] AT-V00-012-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-02", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-02

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-013] Clause acceptance: NV04

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

desktop-body

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

NV04

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-NV04

**Phụ thuộc:**

P20-01, B00-02

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/NV04.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của NV04 từ source_text trong requirements.json vào bảng case cho AT-NV04; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P20-01 với tiêu chí: Front view kẹp ở trái ảnh, thuộc bên phải nhân vật; sprite lật không làm sai bên giải phẫu; nét thường ngày tươi. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-02, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/NV04.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-013-01: Front view kẹp ở trái ảnh, thuộc bên phải nhân vật; sprite lật không làm sai bên giải phẫu; nét thường ngày tươi.
- [ ] AT-V00-013-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-02", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-02

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-014] Clause acceptance: NV05

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

desktop-body

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

NV05

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-NV05

**Phụ thuộc:**

P20-02, B00-02

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/NV05.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của NV05 từ source_text trong requirements.json vào bảng case cho AT-NV05; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P20-02 với tiêu chí: Kiểm asset nguồn128x128 và chuyển động ở nhiều tỉ lệ; không kết luận mượt chỉ từ kích thước file. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-02, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/NV05.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-014-01: Kiểm asset nguồn128x128 và chuyển động ở nhiều tỉ lệ; không kết luận mượt chỉ từ kích thước file.
- [ ] AT-V00-014-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-02", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-02

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-015] Clause acceptance: NV06

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

desktop-body

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

NV06

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-NV06

**Phụ thuộc:**

P40-01, B00-02

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/NV06.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của NV06 từ source_text trong requirements.json vào bảng case cho AT-NV06; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P40-01 với tiêu chí: Lần đầu128; kéo64–384; mở lại giữ lựa chọn; đặt tên qua onboarding. Giới hạn ký tự cần quyết định riêng. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-02, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/NV06.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-015-01: Lần đầu128; kéo64–384; mở lại giữ lựa chọn; đặt tên qua onboarding. Giới hạn ký tự cần quyết định riêng.
- [ ] AT-V00-015-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-02", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-02

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-016] Clause acceptance: NV07

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

desktop-body

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

NV07

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-NV07

**Phụ thuộc:**

P20-02, B00-02

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/NV07.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của NV07 từ source_text trong requirements.json vào bảng case cho AT-NV07; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P20-02 với tiêu chí: Di chuyển/thu nhỏ/đóng cửa sổ đang làm bề mặt: theo cửa sổ hoặc rơi đúng bề mặt kế tiếp, không đứng lơ lửng. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-02, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/NV07.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-016-01: Di chuyển/thu nhỏ/đóng cửa sổ đang làm bề mặt: theo cửa sổ hoặc rơi đúng bề mặt kế tiếp, không đứng lơ lửng.
- [ ] AT-V00-016-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-02", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-02

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-017] Clause acceptance: NV08

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

desktop-body

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

NV08

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-NV08

**Phụ thuộc:**

P20-05, B00-02

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/NV08.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của NV08 từ source_text trong requirements.json vào bảng case cho AT-NV08; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P20-05 với tiêu chí: Chỉ xuất hiện trên monitor cho phép; fullscreen ở mép; ghi rõ trường hợp exclusive không hỗ trợ sau thử, không tự hứa mọi game. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-02, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/NV08.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-017-01: Chỉ xuất hiện trên monitor cho phép; fullscreen ở mép; ghi rõ trường hợp exclusive không hỗ trợ sau thử, không tự hứa mọi game.
- [ ] AT-V00-017-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-02", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-02

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-018] Clause acceptance: NV09

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

desktop-body

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

NV09

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-NV09

**Phụ thuộc:**

P20-03, B00-02

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/NV09.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của NV09 từ source_text trong requirements.json vào bảng case cho AT-NV09; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P20-03 với tiêu chí: Phân biệt click/pet/hold-drag/slow-release/fast-release; quăng có đà và rơi/đứng dậy; ngưỡng đo trước chốt. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-02, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/NV09.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-018-01: Phân biệt click/pet/hold-drag/slow-release/fast-release; quăng có đà và rơi/đứng dậy; ngưỡng đo trước chốt.
- [ ] AT-V00-018-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-02", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-02

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-019] Clause acceptance: NV10

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

desktop-body

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

NV10

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-NV10

**Phụ thuộc:**

P40-04, B00-02

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/NV10.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của NV10 từ source_text trong requirements.json vào bảng case cho AT-NV10; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P40-04 với tiêu chí: Input thật chỉ xảy ra sau body approach và revalidate; có dụng cụ ảo khi thiếu bề mặt và bàn phím ảo lúc gõ. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-02, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/NV10.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-019-01: Input thật chỉ xảy ra sau body approach và revalidate; có dụng cụ ảo khi thiếu bề mặt và bàn phím ảo lúc gõ.
- [ ] AT-V00-019-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-02", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-02

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-020] Clause acceptance: NV11

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

desktop-body

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

NV11

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-NV11

**Phụ thuộc:**

P20-03, B00-02

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/NV11.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của NV11 từ source_text trong requirements.json vào bảng case cho AT-NV11; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P20-03 với tiêu chí: Modifier-drag di chuyển ngay cả refusal-lift, không quăng và không giảm relation; phím Shift đã chốt, không thêm tùy chọn phím. Kiểm cả nhánh cho phép và từ chối: Giữ Shift rồi kéo chuyển vị trí kể cả khi từ chối nhấc; không chơi/quăng hay ảnh hưởng quan hệ, không thêm tùy chọn phím; ngưỡng cử chỉ còn phải đo. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-02, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/NV11.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-020-01: Modifier-drag di chuyển ngay cả refusal-lift, không quăng và không giảm relation; phím Shift đã chốt, không thêm tùy chọn phím. Kiểm cả nhánh cho phép và từ chối: Giữ Shift rồi kéo chuyển vị trí kể cả khi từ chối nhấc; không chơi/quăng hay ảnh hưởng quan hệ, không thêm tùy chọn phím; ngưỡng cử chỉ còn phải đo.
- [ ] AT-V00-020-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-02", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-02

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-021] Clause acceptance: MC01

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

MC01

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-MC01

**Phụ thuộc:**

P03-04, B00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/MC01.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của MC01 từ source_text trong requirements.json vào bảng case cho AT-MC01; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P03-04 với tiêu chí: Cài mới không tải gói nâng cao ngầm; user chọn mới tải, lỗi tải không báo gói đã sẵn sàng. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-01, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/MC01.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-021-01: Cài mới không tải gói nâng cao ngầm; user chọn mới tải, lỗi tải không báo gói đã sẵn sàng.
- [ ] AT-V00-021-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

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

See linked requirement / prerequisite scope.

## [V00-022] Clause acceptance: MC02

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

MC02

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-MC02

**Phụ thuộc:**

P03-04, B00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/MC02.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của MC02 từ source_text trong requirements.json vào bảng case cho AT-MC02; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P03-04 với tiêu chí: Máy yếu vẫn có lựa chọn thử sau cảnh báo; simulated overload hỏi giảm/tiếp tục và không đổi mode tự động. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-01, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/MC02.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-022-01: Máy yếu vẫn có lựa chọn thử sau cảnh báo; simulated overload hỏi giảm/tiếp tục và không đổi mode tự động.
- [ ] AT-V00-022-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

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

See linked requirement / prerequisite scope.

## [V00-023] Clause acceptance: MC03

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

MC03

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-MC03

**Phụ thuộc:**

P30-06, B00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/MC03.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của MC03 từ source_text trong requirements.json vào bảng case cho AT-MC03; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P30-06 với tiêu chí: Nâng cao→cơ bản→nâng cao bảo toàn memory/relation/personality; cơ bản không tích lũy neglect sâu. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-01, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/MC03.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-023-01: Nâng cao→cơ bản→nâng cao bảo toàn memory/relation/personality; cơ bản không tích lũy neglect sâu.
- [ ] AT-V00-023-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

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

See linked requirement / prerequisite scope.

## [V00-024] Clause acceptance: MC04

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

MC04

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-MC04

**Phụ thuộc:**

P03-04, B00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/MC04.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của MC04 từ source_text trong requirements.json vào bảng case cho AT-MC04; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P03-04 với tiêu chí: Recommendation có dựa measured workload/hardware capability; user override được; không chỉ dựa tên GPU. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-01, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/MC04.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-024-01: Recommendation có dựa measured workload/hardware capability; user override được; không chỉ dựa tên GPU.
- [ ] AT-V00-024-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

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

See linked requirement / prerequisite scope.

## [V00-025] Clause acceptance: SH01

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

life-state

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

SH01

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-SH01

**Phụ thuộc:**

P30-01, B00-05, P10-03

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/SH01.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của SH01 từ source_text trong requirements.json vào bảng case cho AT-SH01; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P30-01 với tiêu chí: Test logical clock/click khi ngủ: phản ứng tùy fatigue, nhịp có naps; chưa tự đặt sleep schedule cố định. Kiểm cả nhánh cho phép và từ chối: Khi nhân vật ngủ dừng quan sát; thức dậy chỉ tiếp tục trong quyền hiện hành, không vượt SafetyHold/Thử đọc lại. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-05, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/SH01.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-025-01: Test logical clock/click khi ngủ: phản ứng tùy fatigue, nhịp có naps; chưa tự đặt sleep schedule cố định. Kiểm cả nhánh cho phép và từ chối: Khi nhân vật ngủ dừng quan sát; thức dậy chỉ tiếp tục trong quyền hiện hành, không vượt SafetyHold/Thử đọc lại.
- [ ] AT-V00-025-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-05", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-05

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-026] Clause acceptance: SH02

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

life-state

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

SH02

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-SH02

**Phụ thuộc:**

P30-01, B00-05

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/SH02.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của SH02 từ source_text trong requirements.json vào bảng case cho AT-SH02; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P30-01 với tiêu chí: Bận/vắng không disease/progress-loss; khi hoạt động có reserve food; không yêu cầu chăm như nghĩa vụ liên tục. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-05, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/SH02.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-026-01: Bận/vắng không disease/progress-loss; khi hoạt động có reserve food; không yêu cầu chăm như nghĩa vụ liên tục.
- [ ] AT-V00-026-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-05", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-05

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-027] Clause acceptance: SH03

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

life-state

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

SH03

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-SH03

**Phụ thuộc:**

P30-01, B00-05

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/SH03.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của SH03 từ source_text trong requirements.json vào bảng case cho AT-SH03; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P30-01 với tiêu chí: Reopen cập nhật elapsed state nhưng không thêm fake memories/events; inactive profile dùng freeze khác appclose. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-05, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/SH03.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-027-01: Reopen cập nhật elapsed state nhưng không thêm fake memories/events; inactive profile dùng freeze khác appclose.
- [ ] AT-V00-027-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-05", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-05

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-028] Clause acceptance: SH04

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

life-state

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

SH04

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-SH04

**Phụ thuộc:**

P20-04, B00-05

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/SH04.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của SH04 từ source_text trong requirements.json vào bảng case cho AT-SH04; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P20-04 với tiêu chí: Đủ6 món miễn phí, chọn ghép bữa, kéo lẻ/cả khay; preference/refusal có trạng thái và không bán bằng tiền. Kiểm cả nhánh cho phép và từ chối: Trong sáu món đã chốt, trái cây là táo, nước trái cây là nước cam; không thêm món thứ bảy. Thú bông thỏ là đồ vật/quà riêng, không nhân vật chính. Màu/chi tiết thú bông, dụng cụ/hình mẫu còn chờ duyệt. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-05, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/SH04.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-028-01: Đủ6 món miễn phí, chọn ghép bữa, kéo lẻ/cả khay; preference/refusal có trạng thái và không bán bằng tiền. Kiểm cả nhánh cho phép và từ chối: Trong sáu món đã chốt, trái cây là táo, nước trái cây là nước cam; không thêm món thứ bảy. Thú bông thỏ là đồ vật/quà riêng, không nhân vật chính. Màu/chi tiết thú bông, dụng cụ/hình mẫu còn chờ duyệt.
- [ ] AT-V00-028-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-05", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-05

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-029] Clause acceptance: SH05

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

life-state

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

SH05

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-SH05

**Phụ thuộc:**

P20-03, B00-05

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/SH05.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của SH05 từ source_text trong requirements.json vào bảng case cho AT-SH05; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P20-03 với tiêu chí: Pet có thể được nhận/né theo mood; không có thoại, tiếng hoặc numeric dashboard; functional error text vẫn rõ. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-05, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/SH05.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-029-01: Pet có thể được nhận/né theo mood; không có thoại, tiếng hoặc numeric dashboard; functional error text vẫn rõ.
- [ ] AT-V00-029-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-05", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-05

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-030] Clause acceptance: SH06

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

life-state

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

SH06

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-SH06

**Phụ thuộc:**

P30-02, B00-05

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/SH06.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của SH06 từ source_text trong requirements.json vào bảng case cho AT-SH06; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P30-02 với tiêu chí: Invitation/tease chung2 attempts và>=30min cooldown; ignore rồi self-play; không drag cursor/window thật. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-05, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/SH06.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-030-01: Invitation/tease chung2 attempts và>=30min cooldown; ignore rồi self-play; không drag cursor/window thật.
- [ ] AT-V00-030-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-05", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-05

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-031] Clause acceptance: SH07

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

life-state

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

SH07

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-SH07

**Phụ thuộc:**

P20-04, B00-05

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/SH07.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của SH07 từ source_text trong requirements.json vào bảng case cho AT-SH07; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P20-04 với tiêu chí: Left props không vượt5; held/in-use không tính; đầy thì cất bằng animation trước thêm; cleanup không instantdelete. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-05, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/SH07.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-031-01: Left props không vượt5; held/in-use không tính; đầy thì cất bằng animation trước thêm; cleanup không instantdelete.
- [ ] AT-V00-031-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-05", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-05

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-032] Clause acceptance: SH08

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

life-state

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

SH08

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-SH08

**Phụ thuộc:**

P20-04, B00-05

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/SH08.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của SH08 từ source_text trong requirements.json vào bảng case cho AT-SH08; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P20-04 với tiêu chí: Cleanup mood delay không chặn user move/hide; gift dùng food/plush đã có, không thêm economy riêng. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-05, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/SH08.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-032-01: Cleanup mood delay không chặn user move/hide; gift dùng food/plush đã có, không thêm economy riêng.
- [ ] AT-V00-032-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-05", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-05

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-033] Clause acceptance: QD01

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

policy

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

QD01

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-QD01

**Phụ thuộc:**

P10-01, B00-04

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/QD01.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của QD01 từ source_text trong requirements.json vào bảng case cho AT-QD01; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P10-01 với tiêu chí: Fresh install grants off; read/control độc lập; bật control khi thiếu read bị từ chối không auto grant. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-04, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/QD01.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-033-01: Fresh install grants off; read/control độc lập; bật control khi thiếu read bị từ chối không auto grant.
- [ ] AT-V00-033-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-04", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-04

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-034] Clause acceptance: QD02

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

policy

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

QD02

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-QD02

**Phụ thuộc:**

P40-02, B00-04

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/QD02.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của QD02 từ source_text trong requirements.json vào bảng case cho AT-QD02; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P40-02 với tiêu chí: List app scan không tự cấp; pasted site được normalize; browser+site grants và subdomain test không substring. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-04, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/QD02.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-034-01: List app scan không tự cấp; pasted site được normalize; browser+site grants và subdomain test không substring.
- [ ] AT-V00-034-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-04", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-04

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-035] Clause acceptance: QD03

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

policy

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

QD03

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-QD03

**Phụ thuộc:**

P50-02, B00-04

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/QD03.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của QD03 từ source_text trong requirements.json vào bảng case cho AT-QD03; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P50-02 với tiêu chí: New source defaultdeny; switch profile dùng installation grants; archive không apply foreign grants. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-04, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/QD03.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-035-01: New source defaultdeny; switch profile dùng installation grants; archive không apply foreign grants.
- [ ] AT-V00-035-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-04", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-04

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-036] Clause acceptance: QD04

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

policy

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

QD04

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-QD04

**Phụ thuộc:**

P10-02, B00-04, P30-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/QD04.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của QD04 từ source_text trong requirements.json vào bảng case cho AT-QD04; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P10-02 với tiêu chí: Split-screen chỉ vùng visible+allowed; tab nền/minimized/occluded không cấp nội dung vào consumer. Kiểm cả nhánh cho phép và từ chối: Nhân vật ngủ dừng quan sát; thức dậy không tự cấp quyền hoặc bỏ qua SafetyHold/Thử đọc lại. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-04, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/QD04.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-036-01: Split-screen chỉ vùng visible+allowed; tab nền/minimized/occluded không cấp nội dung vào consumer. Kiểm cả nhánh cho phép và từ chối: Nhân vật ngủ dừng quan sát; thức dậy không tự cấp quyền hoặc bỏ qua SafetyHold/Thử đọc lại.
- [ ] AT-V00-036-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-04", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-04

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-037] Clause acceptance: QD05

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

policy

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

QD05

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-QD05

**Phụ thuộc:**

P10-03, B00-04

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/QD05.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của QD05 từ source_text trong requirements.json vào bảng case cho AT-QD05; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P10-03 với tiêu chí: Sentinel vùng cấm/private/secret không vào OCR/model/memory/network; unknown-region chặn nguồn, không chỉ overlay che. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-04, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/QD05.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-037-01: Sentinel vùng cấm/private/secret không vào OCR/model/memory/network; unknown-region chặn nguồn, không chỉ overlay che.
- [ ] AT-V00-037-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-04", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-04

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-038] Clause acceptance: QD06

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

policy

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

QD06

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-QD06

**Phụ thuộc:**

P10-02, B00-04

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/QD06.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của QD06 từ source_text trong requirements.json vào bảng case cho AT-QD06; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P10-02 với tiêu chí: Đọc qua UI được phép không account connector; không tự mở thư/tin gây marked-read. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-04, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/QD06.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-038-01: Đọc qua UI được phép không account connector; không tự mở thư/tin gây marked-read.
- [ ] AT-V00-038-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-04", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-04

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-039] Clause acceptance: QD07

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

policy

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

QD07

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-QD07

**Phụ thuộc:**

P00-01, B00-04

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/QD07.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của QD07 từ source_text trong requirements.json vào bảng case cho AT-QD07; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task DEFERRED với tiêu chí: Scope kiểm tra không có direct file/folder reader bản đầu; không tạo task parser như chức năng đã duyệt. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-04, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/QD07.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-039-01: Scope kiểm tra không có direct file/folder reader bản đầu; không tạo task parser như chức năng đã duyệt.
- [ ] AT-V00-039-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-04", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-04

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-040] Clause acceptance: QD08

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

policy

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

QD08

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-QD08

**Phụ thuộc:**

P10-04, B00-04

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/QD08.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của QD08 từ source_text trong requirements.json vào bảng case cho AT-QD08; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P10-04 với tiêu chí: Fake clipboard history chỉ truy cập khi Win+V open evidence; close mid-flight hủy; không persist/memory. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-04, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/QD08.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-040-01: Fake clipboard history chỉ truy cập khi Win+V open evidence; close mid-flight hủy; không persist/memory.
- [ ] AT-V00-040-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-04", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-04

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-041] Clause acceptance: QD09

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

policy

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

QD09

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-QD09

**Phụ thuộc:**

P30-04, B00-04

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/QD09.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của QD09 từ source_text trong requirements.json vào bảng case cho AT-QD09; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P30-04 với tiêu chí: Revocation chặn ngay đường mới; keep/delete memories là quyết định riêng, không chờ quyết định mới revoke. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-04, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/QD09.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-041-01: Revocation chặn ngay đường mới; keep/delete memories là quyết định riêng, không chờ quyết định mới revoke.
- [ ] AT-V00-041-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-04", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-04

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-042] Clause acceptance: QD10

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

policy

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

QD10

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-QD10

**Phụ thuộc:**

P20-02, B00-04

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/QD10.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của QD10 từ source_text trong requirements.json vào bảng case cho AT-QD10; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P20-02 với tiêu chí: Nguồn chưa read chỉ xuất geometry; consumer sinh hoạt không nhận title/text, không sinh control grant. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-04, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/QD10.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-042-01: Nguồn chưa read chỉ xuất geometry; consumer sinh hoạt không nhận title/text, không sinh control grant.
- [ ] AT-V00-042-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-04", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-04

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-043] Clause acceptance: QD11

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

policy

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

QD11

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-QD11

**Phụ thuộc:**

P30-04, B00-04

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/QD11.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của QD11 từ source_text trong requirements.json vào bảng case cho AT-QD11; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P30-04 với tiêu chí: Document observation chỉ memory name/topic; không detailed summary hoặc raw content trong memory/index. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-04, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/QD11.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-043-01: Document observation chỉ memory name/topic; không detailed summary hoặc raw content trong memory/index.
- [ ] AT-V00-043-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-04", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-04

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-044] Clause acceptance: QD12

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

policy

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

QD12

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-QD12

**Phụ thuộc:**

P10-06, B00-04

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/QD12.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của QD12 từ source_text trong requirements.json vào bảng case cho AT-QD12; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P10-06 với tiêu chí: Core life không extension; web enable hướng dẫn install rõ, không tự grant mọi host permissions. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-04, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/QD12.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-044-01: Core life không extension; web enable hướng dẫn install rõ, không tự grant mọi host permissions.
- [ ] AT-V00-044-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-04", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-04

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-045] Clause acceptance: QD13

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

policy

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

QD13

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-QD13

**Phụ thuộc:**

P10-06, B00-04

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/QD13.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của QD13 từ source_text trong requirements.json vào bảng case cho AT-QD13; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P10-06 với tiêu chí: Thirdparty player chỉ frame đã cho phép trong parent; ad/frame khác không kế thừa; uncertain phải point+confirm. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-04, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/QD13.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-045-01: Thirdparty player chỉ frame đã cho phép trong parent; ad/frame khác không kế thừa; uncertain phải point+confirm.
- [ ] AT-V00-045-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-04", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-04

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-046] Clause acceptance: QD14

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

policy

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

QD14

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-QD14

**Phụ thuộc:**

P10-06, B00-04

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/QD14.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của QD14 từ source_text trong requirements.json vào bảng case cho AT-QD14; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P10-06 với tiêu chí: Frame recognition scoped đúng site; layout/source đổi hỏi lại, không replay tọa độ và không gọi bài học tự động. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-04, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/QD14.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-046-01: Frame recognition scoped đúng site; layout/source đổi hỏi lại, không replay tọa độ và không gọi bài học tự động.
- [ ] AT-V00-046-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-04", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-04

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-047] Clause acceptance: QD15

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

policy

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

QD15

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-QD15

**Phụ thuộc:**

P10-03, B00-04

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/QD15.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của QD15 từ source_text trong requirements.json vào bảng case cho AT-QD15; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P10-03 với tiêu chí: Unsafe window giữ hold; fix/đổi cửa sổ không tự đọc; explicit retry kiểm mới, unsafe vẫn chặn. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-04, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/QD15.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-047-01: Unsafe window giữ hold; fix/đổi cửa sổ không tự đọc; explicit retry kiểm mới, unsafe vẫn chặn.
- [ ] AT-V00-047-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-04", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-04

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-048] Clause acceptance: DK01

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

policy

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

DK01

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-DK01

**Phụ thuộc:**

P10-07, B00-04

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/DK01.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của DK01 từ source_text trong requirements.json vào bảng case cho AT-DK01; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P10-07 với tiêu chí: Human mouse/key làm yield; injected input không reset idle; sau60s revalidate mới resume. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-04, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/DK01.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-048-01: Human mouse/key làm yield; injected input không reset idle; sau60s revalidate mới resume.
- [ ] AT-V00-048-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-04", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-04

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-049] Clause acceptance: DK02

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

policy

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

DK02

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-DK02

**Phụ thuộc:**

P10-07, B00-04

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/DK02.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của DK02 từ source_text trong requirements.json vào bảng case cho AT-DK02; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P10-07 với tiêu chí: Action allowlist chặn write/delete/send/pay/markread; chỉ search/navigation typing; watchhistory incidental được giữ. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-04, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/DK02.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-049-01: Action allowlist chặn write/delete/send/pay/markread; chỉ search/navigation typing; watchhistory incidental được giữ.
- [ ] AT-V00-049-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-04", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-04

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-050] Clause acceptance: DK03

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

policy

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

DK03

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-DK03

**Phụ thuộc:**

P10-07, B00-04

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/DK03.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của DK03 từ source_text trong requirements.json vào bảng case cho AT-DK03; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P10-07 với tiêu chí: Emergency cancels running/pauses pending; observation/body tiếp theo quyền; no60s autoresume; enable+ResumeQueue. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-04, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/DK03.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-050-01: Emergency cancels running/pauses pending; observation/body tiếp theo quyền; no60s autoresume; enable+ResumeQueue.
- [ ] AT-V00-050-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-04", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-04

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-051] Clause acceptance: DK04

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

policy

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

DK04

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-DK04

**Phụ thuộc:**

P10-07, B00-04

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/DK04.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của DK04 từ source_text trong requirements.json vào bảng case cho AT-DK04; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P10-07 với tiêu chí: ObservationOff/Hide matrix đúng, geometry exception chỉ observationoff; cancelled job không sống lại khi show. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-04, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/DK04.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-051-01: ObservationOff/Hide matrix đúng, geometry exception chỉ observationoff; cancelled job không sống lại khi show.
- [ ] AT-V00-051-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-04", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-04

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-052] Clause acceptance: BH01

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

task-execution

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

BH01

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-BH01

**Phụ thuộc:**

P40-03, B00-06

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/BH01.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của BH01 từ source_text trong requirements.json vào bảng case cho AT-BH01; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P40-03 với tiêu chí: Demo bắt đầu do user, cùng app/site; summary đầy đủ và confirm trước lưu; cancel không thành lesson. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-06, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/BH01.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-052-01: Demo bắt đầu do user, cùng app/site; summary đầy đủ và confirm trước lưu; cancel không thành lesson.
- [ ] AT-V00-052-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-06", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-06

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-053] Clause acceptance: BH02

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

task-execution

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

BH02

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-BH02

**Phụ thuộc:**

P40-03, B00-06, P40-05

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/BH02.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của BH02 từ source_text trong requirements.json vào bảng case cho AT-BH02; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P40-03 với tiêu chí: Manage steps/name/enabled/delete/reteach; execution chỉ explicit request ở cả2mode, không auto invoke. Kiểm cả nhánh cho phép và từ chối: Sửa/xóa bài học dừng việc đang dùng và hủy lượt chờ dùng bài học đó; người dùng giao lại, không chuyển lượt cũ sang phiên bản mới, không hủy việc không liên quan hoặc hoàn tác thao tác đã xong. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-06, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/BH02.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-053-01: Manage steps/name/enabled/delete/reteach; execution chỉ explicit request ở cả2mode, không auto invoke. Kiểm cả nhánh cho phép và từ chối: Sửa/xóa bài học dừng việc đang dùng và hủy lượt chờ dùng bài học đó; người dùng giao lại, không chuyển lượt cũ sang phiên bản mới, không hủy việc không liên quan hoặc hoàn tác thao tác đã xong.
- [ ] AT-V00-053-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-06", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-06

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-054] Clause acceptance: BH03

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

task-execution

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

BH03

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-BH03

**Phụ thuộc:**

P40-04, B00-06

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/BH03.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của BH03 từ source_text trong requirements.json vào bảng case cho AT-BH03; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P40-04 với tiêu chí: Direct request bypass initial60s; mood delay tối đa một lần; secondrequest không bypass grants; pending không bị mất. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-06, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/BH03.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-054-01: Direct request bypass initial60s; mood delay tối đa một lần; secondrequest không bypass grants; pending không bị mất.
- [ ] AT-V00-054-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-06", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-06

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-055] Clause acceptance: BH04

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

task-execution

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

BH04

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-BH04

**Phụ thuộc:**

P40-04, B00-06

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/BH04.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của BH04 từ source_text trong requirements.json vào bảng case cho AT-BH04; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P40-04 với tiêu chí: Human interrupt→60s→reobserve/refocus đúng allowed scope; không replay tọa độ cũ. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-06, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/BH04.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-055-01: Human interrupt→60s→reobserve/refocus đúng allowed scope; không replay tọa độ cũ.
- [ ] AT-V00-055-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-06", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-06

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-056] Clause acceptance: BH05

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

task-execution

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

BH05

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-BH05

**Phụ thuộc:**

P40-04, B00-06

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/BH05.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của BH05 từ source_text trong requirements.json vào bảng case cho AT-BH05; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P40-04 với tiêu chí: Missing/mismatched target dừng bước lỗi, nhờ reteach; không blindclick hoặc rerun từ đầu. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-06, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/BH05.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-056-01: Missing/mismatched target dừng bước lỗi, nhờ reteach; không blindclick hoặc rerun từ đầu.
- [ ] AT-V00-056-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-06", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-06

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-057] Clause acceptance: BH06

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

task-execution

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

BH06

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-BH06

**Phụ thuộc:**

P40-05, B00-06, P02-05, P40-03

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/BH06.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của BH06 từ source_text trong requirements.json vào bảng case cho AT-BH06; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P40-05 với tiêu chí: Queue nhiều việc có order/cancel; failed job stop riêng; later job chỉ chạy khi đủ prerequisites độc lập. Kiểm cả nhánh cho phép và từ chối: Renderer lỗi thì tạm dừng thao tác app khác; hình ảnh phục hồi hoặc mở lại app giữ việc tạm dừng và hỏi trước tiếp tục, kiểm quyền/an toàn mới, không phát lại mù quáng. Sửa/xóa bài học dừng việc đang dùng và hủy lượt chờ dùng bài học đó, phải giao lại; không hủy việc không liên quan hoặc hoàn tác việc đã xong. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-06, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/BH06.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-057-01: Queue nhiều việc có order/cancel; failed job stop riêng; later job chỉ chạy khi đủ prerequisites độc lập. Kiểm cả nhánh cho phép và từ chối: Renderer lỗi thì tạm dừng thao tác app khác; hình ảnh phục hồi hoặc mở lại app giữ việc tạm dừng và hỏi trước tiếp tục, kiểm quyền/an toàn mới, không phát lại mù quáng. Sửa/xóa bài học dừng việc đang dùng và hủy lượt chờ dùng bài học đó, phải giao lại; không hủy việc không liên quan hoặc hoàn tác việc đã xong.
- [ ] AT-V00-057-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-06", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-06

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-058] Clause acceptance: BH07

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

task-execution

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

BH07

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-BH07

**Phụ thuộc:**

P40-05, B00-06

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/BH07.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của BH07 từ source_text trong requirements.json vào bảng case cho AT-BH07; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P40-05 với tiêu chí: Exit/switch cảnh báo và cancel unfinished; reopen không auto-run; saved lessons vẫn giữ. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-06, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/BH07.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-058-01: Exit/switch cảnh báo và cancel unfinished; reopen không auto-run; saved lessons vẫn giữ.
- [ ] AT-V00-058-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-06", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-06

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-059] Clause acceptance: BH08

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

task-execution

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

BH08

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-BH08

**Phụ thuộc:**

P40-05, B00-06

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/BH08.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của BH08 từ source_text trong requirements.json vào bảng case cho AT-BH08; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P40-05 với tiêu chí: Re-enable/show chưa resume pending; riêng ResumeQueue mới xét tiếp, cancelled vẫn cancelled. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-06, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/BH08.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-059-01: Re-enable/show chưa resume pending; riêng ResumeQueue mới xét tiếp, cancelled vẫn cancelled.
- [ ] AT-V00-059-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-06", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-06

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-060] Clause acceptance: BH09

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

task-execution

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

BH09

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-BH09

**Phụ thuộc:**

P40-05, B00-06

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/BH09.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của BH09 từ source_text trong requirements.json vào bảng case cho AT-BH09; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P40-05 với tiêu chí: Relationshiphide cùng cancel-running/pause-pending; voluntary return chưa tự chạy. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-06, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/BH09.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-060-01: Relationshiphide cùng cancel-running/pause-pending; voluntary return chưa tự chạy.
- [ ] AT-V00-060-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-06", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-06

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-061] Clause acceptance: BH10

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

task-execution

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

BH10

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-BH10

**Phụ thuộc:**

P40-05, B00-06

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/BH10.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của BH10 từ source_text trong requirements.json vào bảng case cho AT-BH10; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P40-05 với tiêu chí: Requested job preempts autonomous discovery nhưng vẫn mood delay1; không tự bỏ quyền để ưu tiên. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-06, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/BH10.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-061-01: Requested job preempts autonomous discovery nhưng vẫn mood delay1; không tự bỏ quyền để ưu tiên.
- [ ] AT-V00-061-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-06", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-06

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-062] Clause acceptance: BH11

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

task-execution

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

BH11

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-BH11

**Phụ thuộc:**

P40-03, B00-06

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/BH11.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của BH11 từ source_text trong requirements.json vào bảng case cho AT-BH11; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P40-03 với tiêu chí: Search parameter đổi mỗi run, không thay target scope hoặc cho gõ chat/document. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-06, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/BH11.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-062-01: Search parameter đổi mỗi run, không thay target scope hoặc cho gõ chat/document.
- [ ] AT-V00-062-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-06", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-06

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-063] Clause acceptance: BH12

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

task-execution

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

BH12

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-BH12

**Phụ thuộc:**

P40-03, B00-06

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/BH12.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của BH12 từ source_text trong requirements.json vào bảng case cho AT-BH12; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P40-03 với tiêu chí: Teach review phân biệt first-result và exact-content; selection persists/revalidate, không suy từ x/y. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-06, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/BH12.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-063-01: Teach review phân biệt first-result và exact-content; selection persists/revalidate, không suy từ x/y.
- [ ] AT-V00-063-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-06", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-06

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-064] Clause acceptance: BH13

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

task-execution

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

BH13

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-BH13

**Phụ thuộc:**

P50-05, B00-06

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/BH13.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của BH13 từ source_text trong requirements.json vào bảng case cho AT-BH13; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P50-05 với tiêu chí: History local cótime/source/action/outcome, no privatepayload/screenshots;30days expiry và userdelete; tách memory. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-06, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/BH13.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-064-01: History local cótime/source/action/outcome, no privatepayload/screenshots;30days expiry và userdelete; tách memory.
- [ ] AT-V00-064-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-06", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-06

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-065] Clause acceptance: XP01

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

XP01

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-XP01

**Phụ thuộc:**

P40-06, B00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/XP01.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của XP01 từ source_text trong requirements.json vào bảng case cho AT-XP01; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P40-06 với tiêu chí: Annotated scene sad/action→biểu cảm phù hợp/intensity có lý do, silent; transition dịu không flicker. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-01, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/XP01.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-065-01: Annotated scene sad/action→biểu cảm phù hợp/intensity có lý do, silent; transition dịu không flicker.
- [ ] AT-V00-065-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

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

See linked requirement / prerequisite scope.

## [V00-066] Clause acceptance: XP02

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

XP02

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-XP02

**Phụ thuộc:**

P03-03, B00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/XP02.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của XP02 từ source_text trong requirements.json vào bảng case cho AT-XP02; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P03-03 với tiêu chí: Measure display-event→animation-start toàn luồng; report từng mẫu rõ/khó/uncertain và quality, chưa tự đặt pass-rate. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-01, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/XP02.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-066-01: Measure display-event→animation-start toàn luồng; report từng mẫu rõ/khó/uncertain và quality, chưa tự đặt pass-rate.
- [ ] AT-V00-066-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

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

See linked requirement / prerequisite scope.

## [V00-067] Clause acceptance: XP03

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

XP03

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-XP03

**Phụ thuộc:**

P30-02, B00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/XP03.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của XP03 từ source_text trong requirements.json vào bảng case cho AT-XP03; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P30-02 với tiêu chí: Attention chooses safe visible source theo preference/mood, không claim mọi cảnh; wrongscene không cần correctionUI. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-01, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/XP03.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-067-01: Attention chooses safe visible source theo preference/mood, không claim mọi cảnh; wrongscene không cần correctionUI.
- [ ] AT-V00-067-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

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

See linked requirement / prerequisite scope.

## [V00-068] Clause acceptance: XP10

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

XP10

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-XP10

**Phụ thuộc:**

P30-02, B00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/XP10.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của XP10 từ source_text trong requirements.json vào bảng case cho AT-XP10; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P30-02 với tiêu chí: Capture unavailable không giả hiểu; activity selector cho staywatch hoặc play/eat theo mood. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-01, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/XP10.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-068-01: Capture unavailable không giả hiểu; activity selector cho staywatch hoặc play/eat theo mood.
- [ ] AT-V00-068-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

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

See linked requirement / prerequisite scope.

## [V00-069] Clause acceptance: XP11

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

XP11

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-XP11

**Phụ thuộc:**

P30-05, B00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/XP11.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của XP11 từ source_text trong requirements.json vào bảng case cho AT-XP11; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P30-05 với tiêu chí: Taste inference chủ yếu theo guuser, only allowed visible evidence; không đọc browserhistory hoặc recordaudio. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-01, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/XP11.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-069-01: Taste inference chủ yếu theo guuser, only allowed visible evidence; không đọc browserhistory hoặc recordaudio.
- [ ] AT-V00-069-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

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

See linked requirement / prerequisite scope.

## [V00-070] Clause acceptance: XP12

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

XP12

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-XP12

**Phụ thuộc:**

P30-05, B00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/XP12.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của XP12 từ source_text trong requirements.json vào bảng case cho AT-XP12; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P30-05 với tiêu chí: Self-open content chỉ học gu khi có userreturn/continuedwatch evidence, không tính unattended runtime. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-01, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/XP12.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-070-01: Self-open content chỉ học gu khi có userreturn/continuedwatch evidence, không tính unattended runtime.
- [ ] AT-V00-070-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

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

See linked requirement / prerequisite scope.

## [V00-071] Clause acceptance: XP13

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

XP13

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-XP13

**Phụ thuộc:**

P30-05, B00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/XP13.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của XP13 từ source_text trong requirements.json vào bảng case cho AT-XP13; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P30-05 với tiêu chí: Movie>=20min hoặc musicrepeat/similarsongs là tín hiệu, chưa chắc thích; không gom với neglecttimer. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-01, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/XP13.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-071-01: Movie>=20min hoặc musicrepeat/similarsongs là tín hiệu, chưa chắc thích; không gom với neglecttimer.
- [ ] AT-V00-071-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

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

See linked requirement / prerequisite scope.

## [V00-072] Clause acceptance: XP14

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

XP14

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-XP14

**Phụ thuộc:**

P30-05, B00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/XP14.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của XP14 từ source_text trong requirements.json vào bảng case cho AT-XP14; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P30-05 với tiêu chí: User contentchange khác autoplay/agentinput; không thêm nút xác nhận hoặc camera theo dõi hiện diện. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-01, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/XP14.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-072-01: User contentchange khác autoplay/agentinput; không thêm nút xác nhận hoặc camera theo dõi hiện diện.
- [ ] AT-V00-072-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

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

See linked requirement / prerequisite scope.

## [V00-073] Clause acceptance: XP15

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

XP15

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-XP15

**Phụ thuộc:**

P40-07, B00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/XP15.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của XP15 từ source_text trong requirements.json vào bảng case cho AT-XP15; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P40-07 với tiêu chí: Autonomous media dùng own tab, giữ existing user tabs và nội dung của chúng. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-01, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/XP15.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-073-01: Autonomous media dùng own tab, giữ existing user tabs và nội dung của chúng.
- [ ] AT-V00-073-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

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

See linked requirement / prerequisite scope.

## [V00-074] Clause acceptance: XP16

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

XP16

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-XP16

**Phụ thuộc:**

P40-02, B00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/XP16.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của XP16 từ source_text trong requirements.json vào bảng case cho AT-XP16; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P40-02 với tiêu chí: Chosen browser setting quyết định Chrome/Edge cho automedia; grants vẫn phải đủ. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-01, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/XP16.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-074-01: Chosen browser setting quyết định Chrome/Edge cho automedia; grants vẫn phải đủ.
- [ ] AT-V00-074-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

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

See linked requirement / prerequisite scope.

## [V00-075] Clause acceptance: XP09

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

XP09

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-XP09

**Phụ thuộc:**

P20-04, B00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/XP09.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của XP09 từ source_text trong requirements.json vào bảng case cho AT-XP09; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P20-04 với tiêu chí: Không tự yêu cầu né subtitles; user move avatar/sofa được, không điều hướng phim để dọn vị trí. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-01, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/XP09.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-075-01: Không tự yêu cầu né subtitles; user move avatar/sofa được, không điều hướng phim để dọn vị trí.
- [ ] AT-V00-075-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

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

See linked requirement / prerequisite scope.

## [V00-076] Clause acceptance: XP04

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

XP04

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-XP04

**Phụ thuộc:**

P40-06, B00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/XP04.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của XP04 từ source_text trong requirements.json vào bảng case cho AT-XP04; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P40-06 với tiêu chí: Usermedia không tự pause/scroll/refocus; next chỉ khi ended và target chắc; uncertain không click. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-01, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/XP04.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-076-01: Usermedia không tự pause/scroll/refocus; next chỉ khi ended và target chắc; uncertain không click.
- [ ] AT-V00-076-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

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

See linked requirement / prerequisite scope.

## [V00-077] Clause acceptance: XP05

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

XP05

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-XP05

**Phụ thuộc:**

P40-07, B00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/XP05.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của XP05 từ source_text trong requirements.json vào bảng case cho AT-XP05; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P40-07 với tiêu chí: Advanced idledefault5m+nomedia mới autoopen; userreturn giữ playback/yield control, fullscreen không active evidence. Kiểm cả nhánh cho phép và từ chối: Được kiểm trạng thái đang phát/không phát ở nền tối thiểu để tránh mở chồng; không đọc tên/nội dung hoặc suy gu. Lỗi/không xác định không coi là không phát; API/độ tin cậy cần kiểm chứng. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-01, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/XP05.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-077-01: Advanced idledefault5m+nomedia mới autoopen; userreturn giữ playback/yield control, fullscreen không active evidence. Kiểm cả nhánh cho phép và từ chối: Được kiểm trạng thái đang phát/không phát ở nền tối thiểu để tránh mở chồng; không đọc tên/nội dung hoặc suy gu. Lỗi/không xác định không coi là không phát; API/độ tin cậy cần kiểm chứng.
- [ ] AT-V00-077-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

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

See linked requirement / prerequisite scope.

## [V00-078] Clause acceptance: XP06

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

XP06

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-XP06

**Phụ thuộc:**

P40-07, B00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/XP06.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của XP06 từ source_text trong requirements.json vào bảng case cho AT-XP06; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P40-07 với tiêu chí: YouTube search free trong grants; other site phải explicit allow, không tự nhớ mọi visitedsite thành grant. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-01, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/XP06.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-078-01: YouTube search free trong grants; other site phải explicit allow, không tự nhớ mọi visitedsite thành grant.
- [ ] AT-V00-078-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

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

See linked requirement / prerequisite scope.

## [V00-079] Clause acceptance: XP07

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

XP07

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-XP07

**Phụ thuộc:**

P40-07, B00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/XP07.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của XP07 từ source_text trong requirements.json vào bảng case cho AT-XP07; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P40-07 với tiêu chí: Ambiguous adtab giữ/quay về phim; login/pay/verify skip; max3 candidates per session, không click download/install/notify. Kiểm cả nhánh cho phép và từ chối: Sau 3 nội dung không mở được về sinh hoạt; chờ người dùng thao tác trở lại rồi chỉ tìm trong đợt vắng mặt tiếp theo. Không tìm lặp cùng đợt hoặc chỉ dùng bộ đếm để mở lại tìm kiếm; quyền/chờ/không gián đoạn vẫn áp dụng. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-01, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/XP07.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-079-01: Ambiguous adtab giữ/quay về phim; login/pay/verify skip; max3 candidates per session, không click download/install/notify. Kiểm cả nhánh cho phép và từ chối: Sau 3 nội dung không mở được về sinh hoạt; chờ người dùng thao tác trở lại rồi chỉ tìm trong đợt vắng mặt tiếp theo. Không tìm lặp cùng đợt hoặc chỉ dùng bộ đếm để mở lại tìm kiếm; quyền/chờ/không gián đoạn vẫn áp dụng.
- [ ] AT-V00-079-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

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

See linked requirement / prerequisite scope.

## [V00-080] Clause acceptance: XP08

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

XP08

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-XP08

**Phụ thuộc:**

P10-07, B00-01, P40-07

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/XP08.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của XP08 từ source_text trong requirements.json vào bảng case cho AT-XP08; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P10-07 với tiêu chí: Locked noopen; unlocked có thể tiếp nếu chờ đã đủ; unlock event riêng không reset, desktopinput kế reset. Kiểm cả nhánh cho phép và từ chối: Máy ngủ không cộng thời gian chờ mở phim/nhạc; máy thức tiếp tục phần còn lại, không reset chỉ vì thức. Giữ quyền/khóa/input/phát đã chốt, máy ngủ khác nhân vật ngủ. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-01, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/XP08.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-080-01: Locked noopen; unlocked có thể tiếp nếu chờ đã đủ; unlock event riêng không reset, desktopinput kế reset. Kiểm cả nhánh cho phép và từ chối: Máy ngủ không cộng thời gian chờ mở phim/nhạc; máy thức tiếp tục phần còn lại, không reset chỉ vì thức. Giữ quyền/khóa/input/phát đã chốt, máy ngủ khác nhân vật ngủ.
- [ ] AT-V00-080-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

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

See linked requirement / prerequisite scope.

## [V00-081] Clause acceptance: AI01

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

perception

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

AI01

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-AI01

**Phụ thuộc:**

P03-01, B00-03, P40-07

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/AI01.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của AI01 từ source_text trong requirements.json vào bảng case cho AT-AI01; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P03-01 với tiêu chí: Không mic/camera/audio-analysis/dancebeat; playback bình thường không bị gọi là cô ấy nghe hiểu. Kiểm cả nhánh cho phép và từ chối: Chỉ kiểm tra trạng thái đang phát/không phát ở nền để tránh mở chồng; không tên bài/phim/hình/âm thanh/lịch sử hoặc suy gu; lỗi/không rõ không coi là không phát. Cách lấy/độ tin cậy cần kiểm chứng. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-03, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/AI01.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-081-01: Không mic/camera/audio-analysis/dancebeat; playback bình thường không bị gọi là cô ấy nghe hiểu. Kiểm cả nhánh cho phép và từ chối: Chỉ kiểm tra trạng thái đang phát/không phát ở nền để tránh mở chồng; không tên bài/phim/hình/âm thanh/lịch sử hoặc suy gu; lỗi/không rõ không coi là không phát. Cách lấy/độ tin cậy cần kiểm chứng.
- [ ] AT-V00-081-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-03", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-03

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-082] Clause acceptance: AI02

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

perception

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

AI02

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-AI02

**Phụ thuộc:**

P10-05, B00-03

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/AI02.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của AI02 từ source_text trong requirements.json vào bảng case cho AT-AI02; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P10-05 với tiêu chí: Explicit request→preview sanitized text→confirm mỗi send; deny vẫn local; không image/audio/file/memory upload. Kiểm cả nhánh cho phép và từ chối: Gửi chữ lỗi/chưa rõ thành công thì báo lỗi và chờ bấm thử lại; xem/duyệt chữ trước mỗi lần gửi mới kể cả chữ không đổi. Không tự gửi lại, không coi timeout là chưa nhận, không mở rộng loại dữ liệu/quyền. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-03, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/AI02.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-082-01: Explicit request→preview sanitized text→confirm mỗi send; deny vẫn local; không image/audio/file/memory upload. Kiểm cả nhánh cho phép và từ chối: Gửi chữ lỗi/chưa rõ thành công thì báo lỗi và chờ bấm thử lại; xem/duyệt chữ trước mỗi lần gửi mới kể cả chữ không đổi. Không tự gửi lại, không coi timeout là chưa nhận, không mở rộng loại dữ liệu/quyền.
- [ ] AT-V00-082-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-03", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-03

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-083] Clause acceptance: AI03

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

perception

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

AI03

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-AI03

**Phụ thuộc:**

P03-02, B00-03

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/AI03.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của AI03 từ source_text trong requirements.json vào bảng case cho AT-AI03; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P03-02 với tiêu chí: Local inference measured với renderer cùng chạy; nhẹ không đồng nghĩa đã đạt subsecond; no silent cloud fallback. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-03, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/AI03.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-083-01: Local inference measured với renderer cùng chạy; nhẹ không đồng nghĩa đã đạt subsecond; no silent cloud fallback.
- [ ] AT-V00-083-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-03", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-03

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-084] Clause acceptance: KN01

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

life-state

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

KN01

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-KN01

**Phụ thuộc:**

P30-04, B00-05

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/KN01.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của KN01 từ source_text trong requirements.json vào bảng case cho AT-KN01; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P30-04 với tiêu chí: Inspect/edit/delete/pin từngmemory, importance fade theo reinforcement; pinned không tựfade; no forbidden payload. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-05, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/KN01.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-084-01: Inspect/edit/delete/pin từngmemory, importance fade theo reinforcement; pinned không tựfade; no forbidden payload.
- [ ] AT-V00-084-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-05", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-05

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-085] Clause acceptance: KN02

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

life-state

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

KN02

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-KN02

**Phụ thuộc:**

P30-04, B00-05

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/KN02.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của KN02 từ source_text trong requirements.json vào bảng case cho AT-KN02; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P30-04 với tiêu chí: Edit không relationrecalc; naturalfade giữ closeness; explicitdelete contribution adjust đúng một lần. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-05, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/KN02.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-085-01: Edit không relationrecalc; naturalfade giữ closeness; explicitdelete contribution adjust đúng một lần.
- [ ] AT-V00-085-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-05", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-05

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-086] Clause acceptance: QH01

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

life-state

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

QH01

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-QH01

**Phụ thuộc:**

P30-03, B00-05

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/QH01.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của QH01 từ source_text trong requirements.json vào bảng case cho AT-QH01; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P30-03 với tiêu chí: Friends default; optinadvanced romance không instantpartner; behaviors trong ranh giới không sexualfeature. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-05, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/QH01.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-086-01: Friends default; optinadvanced romance không instantpartner; behaviors trong ranh giới không sexualfeature.
- [ ] AT-V00-086-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-05", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-05

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-087] Clause acceptance: QH02

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

life-state

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

QH02

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-QH02

**Phụ thuộc:**

P30-06, B00-05

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/QH02.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của QH02 từ source_text trong requirements.json vào bảng case cho AT-QH02; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P30-06 với tiêu chí: Romanceoff choosekeep/delete; retainedmemory buồntạm không pressure/re-enable. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-05, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/QH02.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-087-01: Romanceoff choosekeep/delete; retainedmemory buồntạm không pressure/re-enable.
- [ ] AT-V00-087-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-05", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-05

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-088] Clause acceptance: QH03

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

life-state

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

QH03

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-QH03

**Phụ thuộc:**

P30-03, B00-05

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/QH03.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của QH03 từ source_text trong requirements.json vào bảng case cho AT-QH03; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P30-03 với tiêu chí: Neglect activeadvancedvisible only, freeze/off/basic/sleep/idle excluded; không calendar3days. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-05, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/QH03.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-088-01: Neglect activeadvancedvisible only, freeze/off/basic/sleep/idle excluded; không calendar3days.
- [ ] AT-V00-088-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-05", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-05

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-089] Clause acceptance: QH04

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

life-state

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

QH04

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-QH04

**Phụ thuộc:**

P30-03, B00-05

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/QH04.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của QH04 từ source_text trong requirements.json vào bảng case cho AT-QH04; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P30-03 với tiêu chí: Trust→threshold gần72h, hurt gần48h; intentionalclick/pet/feed ngắtstreak nhưng sadness không resetinstant. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-05, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/QH04.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-089-01: Trust→threshold gần72h, hurt gần48h; intentionalclick/pet/feed ngắtstreak nhưng sadness không resetinstant.
- [ ] AT-V00-089-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-05", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-05

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-090] Clause acceptance: QH05

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

life-state

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

QH05

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-QH05

**Phụ thuộc:**

P30-03, B00-05

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/QH05.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của QH05 từ source_text trong requirements.json vào bảng case cho AT-QH05; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P30-03 với tiêu chí: Sad→withdraw progression; severerepair qua nhiềusessions+care, offlinecooling allowed; gifts không instantfix. Kiểm cả nhánh cho phép và từ chối: Buổi làm lành có thể cùng ngày nếu có khoảng nghỉ và tương tác thật; đóng/mở app hoặc quà liên tục không là buổi mới. Không tự đặt số phút/số buổi hoặc quà lập tức xóa tổn thương. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-05, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/QH05.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-090-01: Sad→withdraw progression; severerepair qua nhiềusessions+care, offlinecooling allowed; gifts không instantfix. Kiểm cả nhánh cho phép và từ chối: Buổi làm lành có thể cùng ngày nếu có khoảng nghỉ và tương tác thật; đóng/mở app hoặc quà liên tục không là buổi mới. Không tự đặt số phút/số buổi hoặc quà lập tức xóa tổn thương.
- [ ] AT-V00-090-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-05", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-05

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-091] Clause acceptance: QH06

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

life-state

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

QH06

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-QH06

**Phụ thuộc:**

P30-03, B00-05

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/QH06.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của QH06 từ source_text trong requirements.json vào bảng case cho AT-QH06; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P30-03 với tiêu chí: Firstthrow startle/no lastinghurt; repeatedafterprotest refuse lift nhưng pet/feed; readinesssignal before liftreturn. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-05, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/QH06.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-091-01: Firstthrow startle/no lastinghurt; repeatedafterprotest refuse lift nhưng pet/feed; readinesssignal before liftreturn.
- [ ] AT-V00-091-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-05", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-05

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-092] Clause acceptance: QH07

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

life-state

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

QH07

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-QH07

**Phụ thuộc:**

P30-03, B00-05

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/QH07.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của QH07 từ source_text trong requirements.json vào bảng case cho AT-QH07; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P30-03 với tiêu chí: Selfhide shutsread/control; invite/leavegift accessible withoutavatar, can decline, reset/settings remain reachable. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-05, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/QH07.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-092-01: Selfhide shutsread/control; invite/leavegift accessible withoutavatar, can decline, reset/settings remain reachable.
- [ ] AT-V00-092-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-05", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-05

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-093] Clause acceptance: HS01

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

distribution

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

HS01

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-HS01

**Phụ thuộc:**

P50-02, B00-07

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/HS01.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của HS01 từ source_text trong requirements.json vào bảng case cho AT-HS01; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P50-02 với tiêu chí: Import thêmprofile khôngmerge/createbutton; activeone; inactive state/clocks frozen until selected. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-07, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/HS01.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-093-01: Import thêmprofile khôngmerge/createbutton; activeone; inactive state/clocks frozen until selected.
- [ ] AT-V00-093-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-07", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-07

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-094] Clause acceptance: HS02

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

distribution

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

HS02

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-HS02

**Phụ thuộc:**

P50-02, B00-07

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/HS02.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của HS02 từ source_text trong requirements.json vào bảng case cho AT-HS02; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P50-02 với tiêu chí: All profiles dùng machinegrants, importedprofile không áp importedpermissions. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-07, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/HS02.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-094-01: All profiles dùng machinegrants, importedprofile không áp importedpermissions.
- [ ] AT-V00-094-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-07", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-07

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-095] Clause acceptance: HS03

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

distribution

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

HS03

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-HS03

**Phụ thuộc:**

P50-02, B00-07

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/HS03.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của HS03 từ source_text trong requirements.json vào bảng case cho AT-HS03; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P50-02 với tiêu chí: Reset active memories/relation/state/lessons, preserveotherprofiles và installationgrants. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-07, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/HS03.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-095-01: Reset active memories/relation/state/lessons, preserveotherprofiles và installationgrants.
- [ ] AT-V00-095-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-07", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-07

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-096] Clause acceptance: SL01

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

distribution

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

SL01

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-SL01

**Phụ thuộc:**

P50-03, B00-07

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/SL01.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của SL01 từ source_text trong requirements.json vào bảng case cho AT-SL01; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P50-03 với tiêu chí: Export only useraction; no autoarchive/recoverybackup; keys excluded; reconnect AI onnewmachine. Kiểm cả nhánh cho phép và từ chối: Sao lưu không kèm gói AI nâng cao; máy mới tải lại khi cần, không thêm tùy chọn kèm gói mỗi lần xuất. Giữ dữ liệu nhân vật/ký ức/thiết lập thuộc phạm vi; quyền máy/khóa AI ngoài không mang sang. Whitelist/tài nguyên khác/tương thích còn phải đặc tả. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-07, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/SL01.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-096-01: Export only useraction; no autoarchive/recoverybackup; keys excluded; reconnect AI onnewmachine. Kiểm cả nhánh cho phép và từ chối: Sao lưu không kèm gói AI nâng cao; máy mới tải lại khi cần, không thêm tùy chọn kèm gói mỗi lần xuất. Giữ dữ liệu nhân vật/ký ức/thiết lập thuộc phạm vi; quyền máy/khóa AI ngoài không mang sang. Whitelist/tài nguyên khác/tương thích còn phải đặc tả.
- [ ] AT-V00-096-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-07", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-07

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-097] Clause acceptance: SL02

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

distribution

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

SL02

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-SL02

**Phụ thuộc:**

P50-03, B00-07

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/SL02.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của SL02 từ source_text trong requirements.json vào bảng case cho AT-SL02; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P50-03 với tiêu chí: Passwordrequired perexport + separatelyheldrecoverycode; both correct paths open authenticateddata, bad creds reject. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-07, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/SL02.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-097-01: Passwordrequired perexport + separatelyheldrecoverycode; both correct paths open authenticateddata, bad creds reject.
- [ ] AT-V00-097-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-07", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-07

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-098] Clause acceptance: CD01

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

distribution

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

CD01

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-CD01

**Phụ thuộc:**

P50-06, B00-07, P40-05, P50-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/CD01.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của CD01 từ source_text trong requirements.json vào bảng case cho AT-CD01; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P50-06 với tiêu chí: Firstsetup hỏi startup choice; normalstate persistence works and distinctfrombackup. Kiểm cả nhánh cho phép và từ chối: Mở lại app giữ việc đang dở tạm dừng, hỏi trước tiếp tục; không tự chạy lại, vẫn kiểm quyền/an toàn hiện hành. Crash ghi dữ liệu/cập nhật còn cần khảo sát. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-07, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/CD01.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-098-01: Firstsetup hỏi startup choice; normalstate persistence works and distinctfrombackup. Kiểm cả nhánh cho phép và từ chối: Mở lại app giữ việc đang dở tạm dừng, hỏi trước tiếp tục; không tự chạy lại, vẫn kiểm quyền/an toàn hiện hành. Crash ghi dữ liệu/cập nhật còn cần khảo sát.
- [ ] AT-V00-098-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-07", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-07

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-099] Clause acceptance: CD02

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

distribution

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

CD02

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-CD02

**Phụ thuộc:**

P50-07, B00-07

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/CD02.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của CD02 từ source_text trong requirements.json vào bảng case cho AT-CD02; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P50-07 với tiêu chí: Check/download ownupdate, confirm beforeinstall/restart; no otherappupdate. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-07, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/CD02.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-099-01: Check/download ownupdate, confirm beforeinstall/restart; no otherappupdate.
- [ ] AT-V00-099-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-07", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-07

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-100] Clause acceptance: CD03

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

distribution

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

CD03

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-CD03

**Phụ thuộc:**

P50-08, B00-07

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/CD03.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của CD03 từ source_text trong requirements.json vào bảng case cho AT-CD03; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P50-08 với tiêu chí: Uninstall choosekeep/delete và reminder export; không hunt/delete unrelated exported archives. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-07, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/CD03.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-100-01: Uninstall choosekeep/delete và reminder export; không hunt/delete unrelated exported archives.
- [ ] AT-V00-100-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-07", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-07

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [V00-101] Clause acceptance: MODE01

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

MODE01

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-MODE01

**Phụ thuộc:**

P60-02, B00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/MODE01.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của MODE01 từ source_text trong requirements.json vào bảng case cho AT-MODE01; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P60-02 với tiêu chí: Chạy cùng kịch bản sinh hoạt ở hai mức; chỉ biểu hiện khả năng được cho phép ở mức đó; downgrade/upgrade giữ dữ liệu theo MC03. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-01, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/MODE01.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-101-01: Chạy cùng kịch bản sinh hoạt ở hai mức; chỉ biểu hiện khả năng được cho phép ở mức đó; downgrade/upgrade giữ dữ liệu theo MC03.
- [ ] AT-V00-101-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

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

See linked requirement / prerequisite scope.

## [V00-102] Clause acceptance: MODE02

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

MODE02

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-MODE02

**Phụ thuộc:**

P60-02, B00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/MODE02.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của MODE02 từ source_text trong requirements.json vào bảng case cho AT-MODE02; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P60-02 với tiêu chí: Chạy cùng kịch bản sở thích bằng hoạt ảnh ở hai mức; chỉ biểu hiện khả năng được cho phép ở mức đó; downgrade/upgrade giữ dữ liệu theo MC03. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-01, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/MODE02.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-102-01: Chạy cùng kịch bản sở thích bằng hoạt ảnh ở hai mức; chỉ biểu hiện khả năng được cho phép ở mức đó; downgrade/upgrade giữ dữ liệu theo MC03.
- [ ] AT-V00-102-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

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

See linked requirement / prerequisite scope.

## [V00-103] Clause acceptance: MODE03

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

MODE03

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-MODE03

**Phụ thuộc:**

P60-02, B00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/MODE03.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của MODE03 từ source_text trong requirements.json vào bảng case cho AT-MODE03; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P60-02 với tiêu chí: Chạy cùng kịch bản nội dung sách/tranh/game ở hai mức; chỉ biểu hiện khả năng được cho phép ở mức đó; downgrade/upgrade giữ dữ liệu theo MC03. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-01, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/MODE03.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-103-01: Chạy cùng kịch bản nội dung sách/tranh/game ở hai mức; chỉ biểu hiện khả năng được cho phép ở mức đó; downgrade/upgrade giữ dữ liệu theo MC03.
- [ ] AT-V00-103-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

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

See linked requirement / prerequisite scope.

## [V00-104] Clause acceptance: MODE04

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

MODE04

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-MODE04

**Phụ thuộc:**

P60-02, B00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/MODE04.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của MODE04 từ source_text trong requirements.json vào bảng case cho AT-MODE04; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P60-02 với tiêu chí: Chạy cùng kịch bản hiểu màn hình ở hai mức; chỉ biểu hiện khả năng được cho phép ở mức đó; downgrade/upgrade giữ dữ liệu theo MC03. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-01, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/MODE04.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-104-01: Chạy cùng kịch bản hiểu màn hình ở hai mức; chỉ biểu hiện khả năng được cho phép ở mức đó; downgrade/upgrade giữ dữ liệu theo MC03.
- [ ] AT-V00-104-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

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

See linked requirement / prerequisite scope.

## [V00-105] Clause acceptance: MODE05

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

MODE05

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-MODE05

**Phụ thuộc:**

P60-02, B00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/MODE05.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của MODE05 từ source_text trong requirements.json vào bảng case cho AT-MODE05; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P60-02 với tiêu chí: Chạy cùng kịch bản điều khiển ứng dụng ở hai mức; chỉ biểu hiện khả năng được cho phép ở mức đó; downgrade/upgrade giữ dữ liệu theo MC03. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-01, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/MODE05.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-105-01: Chạy cùng kịch bản điều khiển ứng dụng ở hai mức; chỉ biểu hiện khả năng được cho phép ở mức đó; downgrade/upgrade giữ dữ liệu theo MC03.
- [ ] AT-V00-105-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

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

See linked requirement / prerequisite scope.

## [V00-106] Clause acceptance: MODE06

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

MODE06

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-MODE06

**Phụ thuộc:**

P60-02, B00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/MODE06.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của MODE06 từ source_text trong requirements.json vào bảng case cho AT-MODE06; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P60-02 với tiêu chí: Chạy cùng kịch bản tự mở phim/nhạc ở hai mức; chỉ biểu hiện khả năng được cho phép ở mức đó; downgrade/upgrade giữ dữ liệu theo MC03. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-01, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/MODE06.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-106-01: Chạy cùng kịch bản tự mở phim/nhạc ở hai mức; chỉ biểu hiện khả năng được cho phép ở mức đó; downgrade/upgrade giữ dữ liệu theo MC03.
- [ ] AT-V00-106-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

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

See linked requirement / prerequisite scope.

## [V00-107] Clause acceptance: MODE07

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

MODE07

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-MODE07

**Phụ thuộc:**

P60-02, B00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/MODE07.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của MODE07 từ source_text trong requirements.json vào bảng case cho AT-MODE07; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P60-02 với tiêu chí: Chạy cùng kịch bản cảm xúc/quan hệ ở hai mức; chỉ biểu hiện khả năng được cho phép ở mức đó; downgrade/upgrade giữ dữ liệu theo MC03. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-01, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/MODE07.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-107-01: Chạy cùng kịch bản cảm xúc/quan hệ ở hai mức; chỉ biểu hiện khả năng được cho phép ở mức đó; downgrade/upgrade giữ dữ liệu theo MC03.
- [ ] AT-V00-107-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

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

See linked requirement / prerequisite scope.

## [V00-108] Clause acceptance: MODE08

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

MODE08

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-MODE08

**Phụ thuộc:**

P60-02, B00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/MODE08.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của MODE08 từ source_text trong requirements.json vào bảng case cho AT-MODE08; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P60-02 với tiêu chí: Chạy cùng kịch bản phát triển tính cách ở hai mức; chỉ biểu hiện khả năng được cho phép ở mức đó; downgrade/upgrade giữ dữ liệu theo MC03. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-01, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/MODE08.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-108-01: Chạy cùng kịch bản phát triển tính cách ở hai mức; chỉ biểu hiện khả năng được cho phép ở mức đó; downgrade/upgrade giữ dữ liệu theo MC03.
- [ ] AT-V00-108-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

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

See linked requirement / prerequisite scope.

## [V00-109] Clause acceptance: MODE09

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

MODE09

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Case matrix and evidence for AT-MODE09

**Phụ thuộc:**

P60-02, B00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/acceptance/MODE09.md

**Các bước cụ thể:**

1. Tách từng điều độc lập của MODE09 từ source_text trong requirements.json vào bảng case cho AT-MODE09; giữ giới hạn/ngoại lệ, không thêm hành vi.
2. Đối chiếu đầu ra task P60-02 với tiêu chí: Chạy cùng kịch bản mất internet ở hai mức; chỉ biểu hiện khả năng được cho phép ở mức đó; downgrade/upgrade giữ dữ liệu theo MC03. Ghi rõ case dương, phủ định, restart/revoke/cancel nếu liên quan.
3. Sau bootstrap B00-01, gắn từng case với lệnh/fixture thực có; lưu vào docs/acceptance/MODE09.md với revision, expected, actual hoặc NOT RUN, giới hạn và người duyệt. Không tự xác nhận người dùng đã thử.

**Tiêu chí nghiệm thu:**

- [ ] AT-V00-109-01: Chạy cùng kịch bản mất internet ở hai mức; chỉ biểu hiện khả năng được cho phép ở mức đó; downgrade/upgrade giữ dữ liệu theo MC03.
- [ ] AT-V00-109-02: Enumerate every independently observable clause in the exact requirement, including forbidden behavior and lifecycle interruption. Assign case IDs, expected results, actual result or NOT RUN and evidence path; zero omitted clauses; unresolved expectations block acceptance.

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

See linked requirement / prerequisite scope.
