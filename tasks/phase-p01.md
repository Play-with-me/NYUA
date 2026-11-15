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

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md; docs/unity-windows/SPEC.md; docs/unity-windows/TEST_PLAN.md; docs/unity-windows/SOURCES.md

**Đầu ra:**

E02a technical-closure checklist/evidence, separated from user-obtained demo experience acceptance

**Phụ thuộc:**

P00-01, B00-04

**File thực có trong phạm vi dự kiến:**

labs/policy-native/RESULTS.md; tasks/todo.md

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

labs/policy-native/RESULTS.md; tasks/todo.md

**Các bước cụ thể:**

1. Đọc tasks/E02a-USER-ACCEPTANCE.md và quyết định chấp nhận trải nghiệm ngày2026-11-15; giữ quote/ngày/scope và không hỏi lại nghiệm thu đã được user cho đóng.
2. Đối chiếu tasks/todo.md T04/T05 và docs/E02a-CURRENT-MACHINE-RESULTS.md; tách resize/focus user-confirmed khỏi số đo minimum size,full activation/screenreader và disabled/error coverage chưa kiểm.
3. Sau scope thực thi riêng và B00-04 cần thiết, thu bằng chứng thật cho từng mục kỹ thuật còn mở; đợt chuẩn bị tài liệu hiện tại không chạy lại product test hoặc UI, không sửa labs.
4. Ghi expected/actual/NOT RUN và giới hạn cho technical-closure checklist; task vẫn DRAFT_NOT_AUTHORIZED,không lấy human gate obtained để gọi P01 Done hoặc gateUnity/production đã đạt.

**Tiêu chí nghiệm thu:**

- [ ] AT-P01-01-01: Kiểm minimumresize có số đo, keyboard activation/focus và phần T05 còn mở trên mẫu hiện có bằng bằng chứng thật; mục chưa kiểm vẫn NOT RUN, không dùng quote trải nghiệm để tự đánh dấu kỹ thuật đạt.
- [ ] AT-P01-01-02: Human experience gate E02a đã OBTAINED ngày2026-11-15 theo phản hồi nguyên văn; C3 experience đóng theo người dùng. Hoàn tất kỹ thuật của P01-01 vẫn chờ mọi tiêu chí bắt buộc có evidence; T05 extended checks chưa đủ không được tự đóng.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-04", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "Theo tasks/todo.md và lab RESULTS; không rerun test không đổi chỉ để yên tâm."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-04

**Gate nghiệm thu người dùng:**

{"required": true, "status": "OBTAINED", "evidence": "tasks/E02a-USER-ACCEPTANCE.md", "date": "2026-11-15", "scope": "E02a fake-demo experience only; remaining technical checklist not automatically passed", "user_statement": "Có nhìn rõ và không có chỗ nào bị kẹt, có thể đóng nghiệm thu E02a rồi", "condition": "Explicit user accepted resize/focus experience. Does not complete remaining technical checks or authorize production."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.
