# P01 task cards

Generated from docs/product/AI/backlog.json. Grouping is navigation only; dependencies below determine dispatch. No phase-level edges. All future work requires separate authorization.

## [P01-01] Khép kiểm tra UI còn mở của E02a

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

policy

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

Lab acceptance evidence

**Phụ thuộc:**

P00-01, B00-04

**File thực có trong phạm vi dự kiến:**

labs/policy-native/RESULTS.md; tasks/todo.md

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

labs/policy-native/RESULTS.md; tasks/todo.md

**Các bước cụ thể:**

1. Đối chiếu SP09 và phạm vi enabler với mục tiêu: Khép kiểm tra UI còn mở của E02a. Đọc quyết định liên quan trong DECISIONS; khóa lại phạm vi đầu ra Lab acceptance evidence.
2. Thực hiện lát có thể nghiệm thu riêng trong labs/policy-native/RESULTS.md; tasks/todo.md sau khi được cho phép: Kiểm minimumresize/keyboard/focus trên mẫu hiện có bằng bằng chứng thật. Nếu cần thêm file hoặc thay hợp đồng, chia lát và cập nhật whitelist trước Ready.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: Người dùng dùng thử; C3 chỉ đóng khi các tiêu chí bắt buộc đạt. Không dùng kết quả mẫu giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap: Theo tasks/todo.md và lab RESULTS; không rerun test không đổi chỉ để yên tâm. Lệnh chính xác do B00-04 xác minh; lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P01-01-01: Kiểm minimumresize/keyboard/focus trên mẫu hiện có bằng bằng chứng thật.
- [ ] AT-P01-01-02: Người dùng dùng thử; C3 chỉ đóng khi các tiêu chí bắt buộc đạt.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-04", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "Theo tasks/todo.md và lab RESULTS; không rerun test không đổi chỉ để yên tâm."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-04

**Gate nghiệm thu người dùng:**

{"required": true, "status": "NOT_OBTAINED", "evidence": null, "condition": "Actual user response on the exact reviewed artifact/revision is mandatory; automated or AI review cannot satisfy this gate."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.
