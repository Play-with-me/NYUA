# P00 task cards

Generated from docs/product/AI/backlog.json. Grouping is navigation only; dependencies below determine dispatch. No phase-level edges. All future work requires separate authorization.

## [P00-01] Rà baseline và giải quyết mâu thuẫn phạm vi

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

research

**Mã yêu cầu:**

Enabler; linked predecessors define bounded output.

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Baseline/review log

**Phụ thuộc:**

None

**File thực có trong phạm vi dự kiến:**

docs/product/AI/DECISIONS.md; docs/product/AI/requirements.json

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/product/AI/DECISIONS.md; docs/product/AI/requirements.json

**Các bước cụ thể:**

1. Đối chiếu SP09 và phạm vi enabler với mục tiêu: Rà baseline và giải quyết mâu thuẫn phạm vi. Đọc quyết định liên quan trong DECISIONS; khóa lại phạm vi đầu ra Baseline/review log.
2. Thực hiện lát có thể nghiệm thu riêng trong docs/product/AI/DECISIONS.md; docs/product/AI/requirements.json sau khi được cho phép: Đối chiếu toàn bộ sourceIDs/mode rows với SRS và xác nhận phần hoãn. Nếu cần thêm file hoặc thay hợp đồng, chia lát và cập nhật whitelist trước Ready.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: Ghi user decision hoặc blocker cho mỗi mâu thuẫn; không tự dùng default. Không dùng kết quả mẫu giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap: Review SRS/registry/RTM và validate_dossier.py. Lệnh chính xác do owner đề cương xác minh; lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P00-01-01: Đối chiếu toàn bộ sourceIDs/mode rows với SRS và xác nhận phần hoãn.
- [ ] AT-P00-01-02: Ghi user decision hoặc blocker cho mỗi mâu thuẫn; không tự dùng default.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": null, "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "Review SRS/registry/RTM và validate_dossier.py."}

**Chủ nhiệm chuẩn bị công cụ:**

This is a planning/research/checkpoint task; any executable probe still requires scoped authorization and an established bounded command.

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [P00-02] Rà ranh giới và hợp đồng hybrid

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

research

**Mã yêu cầu:**

SP09

**Quyết định / rào cản:**

D-02, D-03

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Module/contract baseline

**Phụ thuộc:**

P00-01, A00-02, A00-03

**File thực có trong phạm vi dự kiến:**

docs/product/AI/INTERFACES.md

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

contracts/README.md; docs/product/AI/INTERFACES.md

**Các bước cụ thể:**

1. Đối chiếu SP09 với mục tiêu: Rà ranh giới và hợp đồng hybrid. Đọc quyết định D-02, D-03; khóa lại phạm vi đầu ra Module/contract baseline.
2. Thực hiện lát có thể nghiệm thu riêng trong contracts/README.md; docs/product/AI/INTERFACES.md sau khi được cho phép: Thống nhất host authority, renderer/model chỉ ý định và dữ liệu đã lọc. Nếu cần thêm file hoặc thay hợp đồng, chia lát và cập nhật whitelist trước Ready.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: DTO/error/generation ownership rõ; không vòng dependency hoặc transport tự chốt. Không dùng kết quả mẫu giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap: Review INTERFACES/ARCHITECTURE và negative message examples. Lệnh chính xác do owner đề cương xác minh; lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P00-02-01: Thống nhất host authority, renderer/model chỉ ý định và dữ liệu đã lọc.
- [ ] AT-P00-02-02: DTO/error/generation ownership rõ; không vòng dependency hoặc transport tự chốt.
- [ ] AT-P00-02-03: AT-SP09 — D-02: Hình ảnh lỗi thì tạm dừng thao tác lên app khác; phục hồi vẫn tạm dừng và hỏi trước tiếp tục, kiểm quyền/an toàn mới. Không phát lại mù quáng; hợp đồng kết nối/mất kết nối còn mở. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": null, "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "Review INTERFACES/ARCHITECTURE và negative message examples."}

**Chủ nhiệm chuẩn bị công cụ:**

This is a planning/research/checkpoint task; any executable probe still requires scoped authorization and an established bounded command.

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

SP09

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [P00-03] Chốt tiêu chuẩn chất lượng sau đo

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

research

**Mã yêu cầu:**

Enabler; linked predecessors define bounded output.

**Quyết định / rào cản:**

D-04

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Quality budget proposal

**Phụ thuộc:**

P00-01, A00-04

**File thực có trong phạm vi dự kiến:**

CONSTRAINTS.md; docs/product/AI/QA.md

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

CONSTRAINTS.md; docs/product/AI/QA.md

**Các bước cụ thể:**

1. Đối chiếu SP09 và phạm vi enabler với mục tiêu: Chốt tiêu chuẩn chất lượng sau đo. Đọc quyết định D-04; khóa lại phạm vi đầu ra Quality budget proposal.
2. Thực hiện lát có thể nghiệm thu riêng trong CONSTRAINTS.md; docs/product/AI/QA.md sau khi được cho phép: Phân biệt target user đã chốt với ngưỡng còn phải đo. Nếu cần thêm file hoặc thay hợp đồng, chia lát và cập nhật whitelist trước Ready.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: Mỗi gate có phép đo/command thực tế khi triển khai, không coverage/perf giả. Không dùng kết quả mẫu giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap: Rà CONSTRAINTS và positive/negative control kế hoạch. Lệnh chính xác do owner đề cương xác minh; lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P00-03-01: Phân biệt target user đã chốt với ngưỡng còn phải đo.
- [ ] AT-P00-03-02: Mỗi gate có phép đo/command thực tế khi triển khai, không coverage/perf giả.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": null, "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "Rà CONSTRAINTS và positive/negative control kế hoạch."}

**Chủ nhiệm chuẩn bị công cụ:**

This is a planning/research/checkpoint task; any executable probe still requires scoped authorization and an established bounded command.

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [P00-04] Lập danh mục giấy phép và chi phí

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

distribution

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

research

**Mã yêu cầu:**

SP06

**Quyết định / rào cản:**

D-13

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

License/cost bill

**Phụ thuộc:**

P00-01, A00-13

**File thực có trong phạm vi dự kiến:**

docs/product/AI/DECISIONS.md

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/licenses/INVENTORY.md; docs/product/AI/DECISIONS.md

**Các bước cụ thể:**

1. Đối chiếu SP06 với mục tiêu: Lập danh mục giấy phép và chi phí. Đọc quyết định D-13; khóa lại phạm vi đầu ra License/cost bill.
2. Thực hiện lát có thể nghiệm thu riêng trong docs/licenses/INVENTORY.md; docs/product/AI/DECISIONS.md sau khi được cho phép: Ghi source/terms/redistribution của Unity/plugin/model/art/runtime. Nếu cần thêm file hoặc thay hợp đồng, chia lát và cập nhật whitelist trước Ready.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: Tên NYUA và signing/distribution còn mở được ghi riêng, khoản phí phải hỏi. Không dùng kết quả mẫu giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap: Đối chiếu primary terms và lưu evidence/version. Lệnh chính xác do owner đề cương xác minh; lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P00-04-01: Ghi source/terms/redistribution của Unity/plugin/model/art/runtime.
- [ ] AT-P00-04-02: Tên NYUA và signing/distribution còn mở được ghi riêng, khoản phí phải hỏi.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": null, "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "Đối chiếu primary terms và lưu evidence/version."}

**Chủ nhiệm chuẩn bị công cụ:**

This is a planning/research/checkpoint task; any executable probe still requires scoped authorization and an established bounded command.

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

SP06

**Mã phi chức năng:**

See linked requirement / prerequisite scope.
