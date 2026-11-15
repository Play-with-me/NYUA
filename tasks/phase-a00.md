# A00 task cards

Generated from docs/product/AI/backlog.json. Grouping is navigation only; dependencies below determine dispatch. No phase-level edges. All future work requires separate authorization.

## [A00-02] Rà đề cương và phạm vi phép thử D-02

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

finalreview

**Mã yêu cầu:**

SP09, BH06

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md; docs/unity-windows/SPEC.md; docs/unity-windows/TEST_PLAN.md; docs/unity-windows/SOURCES.md

**Đầu ra:**

Gate đề cương D-02; không phải nghiệm thu kết quả

**Phụ thuộc:**

R00-02

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/decisions/D-02-resolution.md

**Các bước cụ thể:**

1. Đọc đề cương R00-02 và DECISIONS D-02; ghi rõ đây là rà trước phép thử, không nghiệm thu kết quả.
2. Renderer mất kết nối khi việc đang chạy → không input lên app khác; phục hồi → vẫn tạm dừng và hỏi; từ chối → giữ dừng; thu hồi quyền trước tiếp tục → chặn; callback cũ không dùng generation mới. Generation reset/transport là thiết kế phải thử, không quyết định đã duyệt.
3. Ghi finding và phạm vi được đề xuất trong docs/decisions/D-02-resolution.md; để mở mọi bằng chứng chưa có, chuyển yêu cầu sản phẩm mới cho người dùng thay vì tự chọn.

**Tiêu chí nghiệm thu:**

- [ ] AT-A00-02-01: Rà đề cương D-02: đủ đầu vào giả, task tạo bằng chứng, giới hạn quyền, timeout/cleanup, whitelist dự kiến và rủi ro; không yêu cầu bằng chứng do task bị chặn bởi gate này tạo ra.
- [ ] AT-A00-02-02: Không duyệt lại câu trả lời đã chốt. Nếu đề cương đổi trải nghiệm/chi phí/quyền thì ghi câu hỏi và chờ người dùng; nếu chỉ kiểm chứng kỹ thuật thì reviewer ghi phạm vi thử, không tự cấp quyền production. Kết quả còn phải nghiệm thu sau phép thử.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py and Python312 docs/product/AI/validate_dossier.py: existing documentation consistency checks only; manual scoped review of named output remains required.

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "NOT_APPLICABLE_DOCUMENT_REVIEW", "owner": null, "command": null, "gate": "Document/research/proposal/checkpoint review has no executable bootstrap prerequisite. Entry requires available source docs, explicit documentation scope and predecessor documents. Use existing dossier/task validators for consistency; runtime evidence, if needed for checkpoint completion, belongs to listed producer dependencies, never an entry prerequisite for proposing a probe."}

**Chủ nhiệm chuẩn bị công cụ:**

This is a planning/research/checkpoint task; any executable probe still requires scoped authorization and an established bounded command.

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [A00-03] Rà đề cương và phạm vi phép thử D-03

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

finalreview

**Mã yêu cầu:**

Enabler; linked predecessors define bounded output.

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md; docs/unity-windows/SPEC.md; docs/unity-windows/TEST_PLAN.md; docs/unity-windows/SOURCES.md

**Đầu ra:**

Gate đề cương D-03; không phải nghiệm thu kết quả

**Phụ thuộc:**

R00-03

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/decisions/D-03-resolution.md

**Các bước cụ thể:**

1. Đọc đề cương R00-03 và DECISIONS D-03; ghi rõ đây là rà trước phép thử, không nghiệm thu kết quả.
2. Đối chiếu từng điều đã chốt của D-03 với lựa chọn kỹ thuật còn mở; đề cương phải có nhánh thành công, lỗi/không rõ và gián đoạn; không bổ sung default.
3. Ghi finding và phạm vi được đề xuất trong docs/decisions/D-03-resolution.md; để mở mọi bằng chứng chưa có, chuyển yêu cầu sản phẩm mới cho người dùng thay vì tự chọn.

**Tiêu chí nghiệm thu:**

- [ ] AT-A00-03-01: Rà đề cương D-03: đủ đầu vào giả, task tạo bằng chứng, giới hạn quyền, timeout/cleanup, whitelist dự kiến và rủi ro; không yêu cầu bằng chứng do task bị chặn bởi gate này tạo ra.
- [ ] AT-A00-03-02: Không duyệt lại câu trả lời đã chốt. Nếu đề cương đổi trải nghiệm/chi phí/quyền thì ghi câu hỏi và chờ người dùng; nếu chỉ kiểm chứng kỹ thuật thì reviewer ghi phạm vi thử, không tự cấp quyền production. Kết quả còn phải nghiệm thu sau phép thử.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py and Python312 docs/product/AI/validate_dossier.py: existing documentation consistency checks only; manual scoped review of named output remains required.

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "NOT_APPLICABLE_DOCUMENT_REVIEW", "owner": null, "command": null, "gate": "Document/research/proposal/checkpoint review has no executable bootstrap prerequisite. Entry requires available source docs, explicit documentation scope and predecessor documents. Use existing dossier/task validators for consistency; runtime evidence, if needed for checkpoint completion, belongs to listed producer dependencies, never an entry prerequisite for proposing a probe."}

**Chủ nhiệm chuẩn bị công cụ:**

This is a planning/research/checkpoint task; any executable probe still requires scoped authorization and an established bounded command.

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [A00-04] Rà đề cương và phạm vi phép thử D-04

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

finalreview

**Mã yêu cầu:**

Enabler; linked predecessors define bounded output.

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Gate đề cương D-04; không phải nghiệm thu kết quả

**Phụ thuộc:**

R00-04

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/decisions/D-04-resolution.md

**Các bước cụ thể:**

1. Đọc đề cương R00-04 và DECISIONS D-04; ghi rõ đây là rà trước phép thử, không nghiệm thu kết quả.
2. Đối chiếu từng điều đã chốt của D-04 với lựa chọn kỹ thuật còn mở; đề cương phải có nhánh thành công, lỗi/không rõ và gián đoạn; không bổ sung default.
3. Ghi finding và phạm vi được đề xuất trong docs/decisions/D-04-resolution.md; để mở mọi bằng chứng chưa có, chuyển yêu cầu sản phẩm mới cho người dùng thay vì tự chọn.

**Tiêu chí nghiệm thu:**

- [ ] AT-A00-04-01: Rà đề cương D-04: đủ đầu vào giả, task tạo bằng chứng, giới hạn quyền, timeout/cleanup, whitelist dự kiến và rủi ro; không yêu cầu bằng chứng do task bị chặn bởi gate này tạo ra.
- [ ] AT-A00-04-02: Không duyệt lại câu trả lời đã chốt. Nếu đề cương đổi trải nghiệm/chi phí/quyền thì ghi câu hỏi và chờ người dùng; nếu chỉ kiểm chứng kỹ thuật thì reviewer ghi phạm vi thử, không tự cấp quyền production. Kết quả còn phải nghiệm thu sau phép thử.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py and Python312 docs/product/AI/validate_dossier.py: existing documentation consistency checks only; manual scoped review of named output remains required.

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "NOT_APPLICABLE_DOCUMENT_REVIEW", "owner": null, "command": null, "gate": "Document/research/proposal/checkpoint review has no executable bootstrap prerequisite. Entry requires available source docs, explicit documentation scope and predecessor documents. Use existing dossier/task validators for consistency; runtime evidence, if needed for checkpoint completion, belongs to listed producer dependencies, never an entry prerequisite for proposing a probe."}

**Chủ nhiệm chuẩn bị công cụ:**

This is a planning/research/checkpoint task; any executable probe still requires scoped authorization and an established bounded command.

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [A00-13] Rà đề cương và phạm vi phép thử D-13

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

finalreview

**Mã yêu cầu:**

Enabler; linked predecessors define bounded output.

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md; docs/unity-windows/SPEC.md; docs/unity-windows/TEST_PLAN.md; docs/unity-windows/SOURCES.md

**Đầu ra:**

Gate đề cương D-13; không phải nghiệm thu kết quả

**Phụ thuộc:**

R00-13

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/decisions/D-13-resolution.md

**Các bước cụ thể:**

1. Đọc đề cương R00-13 và DECISIONS D-13; ghi rõ đây là rà trước phép thử, không nghiệm thu kết quả.
2. Đối chiếu từng điều đã chốt của D-13 với lựa chọn kỹ thuật còn mở; đề cương phải có nhánh thành công, lỗi/không rõ và gián đoạn; không bổ sung default.
3. Ghi finding và phạm vi được đề xuất trong docs/decisions/D-13-resolution.md; để mở mọi bằng chứng chưa có, chuyển yêu cầu sản phẩm mới cho người dùng thay vì tự chọn.

**Tiêu chí nghiệm thu:**

- [ ] AT-A00-13-01: Rà đề cương D-13: đủ đầu vào giả, task tạo bằng chứng, giới hạn quyền, timeout/cleanup, whitelist dự kiến và rủi ro; không yêu cầu bằng chứng do task bị chặn bởi gate này tạo ra.
- [ ] AT-A00-13-02: Không duyệt lại câu trả lời đã chốt. Nếu đề cương đổi trải nghiệm/chi phí/quyền thì ghi câu hỏi và chờ người dùng; nếu chỉ kiểm chứng kỹ thuật thì reviewer ghi phạm vi thử, không tự cấp quyền production. Kết quả còn phải nghiệm thu sau phép thử.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py and Python312 docs/product/AI/validate_dossier.py: existing documentation consistency checks only; manual scoped review of named output remains required.

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "NOT_APPLICABLE_DOCUMENT_REVIEW", "owner": null, "command": null, "gate": "Document/research/proposal/checkpoint review has no executable bootstrap prerequisite. Entry requires available source docs, explicit documentation scope and predecessor documents. Use existing dossier/task validators for consistency; runtime evidence, if needed for checkpoint completion, belongs to listed producer dependencies, never an entry prerequisite for proposing a probe."}

**Chủ nhiệm chuẩn bị công cụ:**

This is a planning/research/checkpoint task; any executable probe still requires scoped authorization and an established bounded command.

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [A00-01] Rà đề cương và phạm vi phép thử D-01

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

finalreview

**Mã yêu cầu:**

Enabler; linked predecessors define bounded output.

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md; docs/unity-windows/SPEC.md; docs/unity-windows/TEST_PLAN.md; docs/unity-windows/SOURCES.md

**Đầu ra:**

Gate đề cương D-01; không phải nghiệm thu kết quả

**Phụ thuộc:**

R00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/decisions/D-01-resolution.md

**Các bước cụ thể:**

1. Đọc đề cương R00-01 và DECISIONS D-01; ghi rõ đây là rà trước phép thử, không nghiệm thu kết quả.
2. Đối chiếu từng điều đã chốt của D-01 với lựa chọn kỹ thuật còn mở; đề cương phải có nhánh thành công, lỗi/không rõ và gián đoạn; không bổ sung default.
3. Ghi finding và phạm vi được đề xuất trong docs/decisions/D-01-resolution.md; để mở mọi bằng chứng chưa có, chuyển yêu cầu sản phẩm mới cho người dùng thay vì tự chọn.

**Tiêu chí nghiệm thu:**

- [ ] AT-A00-01-01: Rà đề cương D-01: đủ đầu vào giả, task tạo bằng chứng, giới hạn quyền, timeout/cleanup, whitelist dự kiến và rủi ro; không yêu cầu bằng chứng do task bị chặn bởi gate này tạo ra.
- [ ] AT-A00-01-02: Không duyệt lại câu trả lời đã chốt. Nếu đề cương đổi trải nghiệm/chi phí/quyền thì ghi câu hỏi và chờ người dùng; nếu chỉ kiểm chứng kỹ thuật thì reviewer ghi phạm vi thử, không tự cấp quyền production. Kết quả còn phải nghiệm thu sau phép thử.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py and Python312 docs/product/AI/validate_dossier.py: existing documentation consistency checks only; manual scoped review of named output remains required.

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "NOT_APPLICABLE_DOCUMENT_REVIEW", "owner": null, "command": null, "gate": "Document/research/proposal/checkpoint review has no executable bootstrap prerequisite. Entry requires available source docs, explicit documentation scope and predecessor documents. Use existing dossier/task validators for consistency; runtime evidence, if needed for checkpoint completion, belongs to listed producer dependencies, never an entry prerequisite for proposing a probe."}

**Chủ nhiệm chuẩn bị công cụ:**

This is a planning/research/checkpoint task; any executable probe still requires scoped authorization and an established bounded command.

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [A00-10] Rà đề cương và phạm vi phép thử D-10

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

finalreview

**Mã yêu cầu:**

CD01, BH06

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md; docs/unity-windows/SPEC.md; docs/unity-windows/TEST_PLAN.md; docs/unity-windows/SOURCES.md

**Đầu ra:**

Gate đề cương D-10; không phải nghiệm thu kết quả

**Phụ thuộc:**

R00-10

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/decisions/D-10-resolution.md

**Các bước cụ thể:**

1. Đọc đề cương R00-10 và DECISIONS D-10; ghi rõ đây là rà trước phép thử, không nghiệm thu kết quả.
2. Đối chiếu từng điều đã chốt của D-10 với lựa chọn kỹ thuật còn mở; đề cương phải có nhánh thành công, lỗi/không rõ và gián đoạn; không bổ sung default.
3. Ghi finding và phạm vi được đề xuất trong docs/decisions/D-10-resolution.md; để mở mọi bằng chứng chưa có, chuyển yêu cầu sản phẩm mới cho người dùng thay vì tự chọn.

**Tiêu chí nghiệm thu:**

- [ ] AT-A00-10-01: Rà đề cương D-10: đủ đầu vào giả, task tạo bằng chứng, giới hạn quyền, timeout/cleanup, whitelist dự kiến và rủi ro; không yêu cầu bằng chứng do task bị chặn bởi gate này tạo ra.
- [ ] AT-A00-10-02: Không duyệt lại câu trả lời đã chốt. Nếu đề cương đổi trải nghiệm/chi phí/quyền thì ghi câu hỏi và chờ người dùng; nếu chỉ kiểm chứng kỹ thuật thì reviewer ghi phạm vi thử, không tự cấp quyền production. Kết quả còn phải nghiệm thu sau phép thử.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py and Python312 docs/product/AI/validate_dossier.py: existing documentation consistency checks only; manual scoped review of named output remains required.

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "NOT_APPLICABLE_DOCUMENT_REVIEW", "owner": null, "command": null, "gate": "Document/research/proposal/checkpoint review has no executable bootstrap prerequisite. Entry requires available source docs, explicit documentation scope and predecessor documents. Use existing dossier/task validators for consistency; runtime evidence, if needed for checkpoint completion, belongs to listed producer dependencies, never an entry prerequisite for proposing a probe."}

**Chủ nhiệm chuẩn bị công cụ:**

This is a planning/research/checkpoint task; any executable probe still requires scoped authorization and an established bounded command.

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [A00-15] Rà đề cương và phạm vi phép thử D-15

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

finalreview

**Mã yêu cầu:**

Enabler; linked predecessors define bounded output.

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Gate đề cương D-15; không phải nghiệm thu kết quả

**Phụ thuộc:**

R00-15

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/decisions/D-15-resolution.md

**Các bước cụ thể:**

1. Đọc đề cương R00-15 và DECISIONS D-15; ghi rõ đây là rà trước phép thử, không nghiệm thu kết quả.
2. Đối chiếu từng điều đã chốt của D-15 với lựa chọn kỹ thuật còn mở; đề cương phải có nhánh thành công, lỗi/không rõ và gián đoạn; không bổ sung default.
3. Ghi finding và phạm vi được đề xuất trong docs/decisions/D-15-resolution.md; để mở mọi bằng chứng chưa có, chuyển yêu cầu sản phẩm mới cho người dùng thay vì tự chọn.

**Tiêu chí nghiệm thu:**

- [ ] AT-A00-15-01: Rà đề cương D-15: đủ đầu vào giả, task tạo bằng chứng, giới hạn quyền, timeout/cleanup, whitelist dự kiến và rủi ro; không yêu cầu bằng chứng do task bị chặn bởi gate này tạo ra.
- [ ] AT-A00-15-02: Không duyệt lại câu trả lời đã chốt. Nếu đề cương đổi trải nghiệm/chi phí/quyền thì ghi câu hỏi và chờ người dùng; nếu chỉ kiểm chứng kỹ thuật thì reviewer ghi phạm vi thử, không tự cấp quyền production. Kết quả còn phải nghiệm thu sau phép thử.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py and Python312 docs/product/AI/validate_dossier.py: existing documentation consistency checks only; manual scoped review of named output remains required.

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "NOT_APPLICABLE_DOCUMENT_REVIEW", "owner": null, "command": null, "gate": "Document/research/proposal/checkpoint review has no executable bootstrap prerequisite. Entry requires available source docs, explicit documentation scope and predecessor documents. Use existing dossier/task validators for consistency; runtime evidence, if needed for checkpoint completion, belongs to listed producer dependencies, never an entry prerequisite for proposing a probe."}

**Chủ nhiệm chuẩn bị công cụ:**

This is a planning/research/checkpoint task; any executable probe still requires scoped authorization and an established bounded command.

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [A00-16] Rà đề cương và phạm vi phép thử D-16

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

finalreview

**Mã yêu cầu:**

AI01, XP05

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Gate đề cương D-16; không phải nghiệm thu kết quả

**Phụ thuộc:**

R00-16

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/decisions/D-16-resolution.md

**Các bước cụ thể:**

1. Đọc đề cương R00-16 và DECISIONS D-16; ghi rõ đây là rà trước phép thử, không nghiệm thu kết quả.
2. Đối chiếu từng điều đã chốt của D-16 với lựa chọn kỹ thuật còn mở; đề cương phải có nhánh thành công, lỗi/không rõ và gián đoạn; không bổ sung default.
3. Ghi finding và phạm vi được đề xuất trong docs/decisions/D-16-resolution.md; để mở mọi bằng chứng chưa có, chuyển yêu cầu sản phẩm mới cho người dùng thay vì tự chọn.

**Tiêu chí nghiệm thu:**

- [ ] AT-A00-16-01: Rà đề cương D-16: đủ đầu vào giả, task tạo bằng chứng, giới hạn quyền, timeout/cleanup, whitelist dự kiến và rủi ro; không yêu cầu bằng chứng do task bị chặn bởi gate này tạo ra.
- [ ] AT-A00-16-02: Không duyệt lại câu trả lời đã chốt. Nếu đề cương đổi trải nghiệm/chi phí/quyền thì ghi câu hỏi và chờ người dùng; nếu chỉ kiểm chứng kỹ thuật thì reviewer ghi phạm vi thử, không tự cấp quyền production. Kết quả còn phải nghiệm thu sau phép thử.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py and Python312 docs/product/AI/validate_dossier.py: existing documentation consistency checks only; manual scoped review of named output remains required.

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "NOT_APPLICABLE_DOCUMENT_REVIEW", "owner": null, "command": null, "gate": "Document/research/proposal/checkpoint review has no executable bootstrap prerequisite. Entry requires available source docs, explicit documentation scope and predecessor documents. Use existing dossier/task validators for consistency; runtime evidence, if needed for checkpoint completion, belongs to listed producer dependencies, never an entry prerequisite for proposing a probe."}

**Chủ nhiệm chuẩn bị công cụ:**

This is a planning/research/checkpoint task; any executable probe still requires scoped authorization and an established bounded command.

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [A00-07] Rà đề cương và phạm vi phép thử D-07

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

finalreview

**Mã yêu cầu:**

Enabler; linked predecessors define bounded output.

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Gate đề cương D-07; không phải nghiệm thu kết quả

**Phụ thuộc:**

R00-07

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/decisions/D-07-resolution.md

**Các bước cụ thể:**

1. Đọc đề cương R00-07 và DECISIONS D-07; ghi rõ đây là rà trước phép thử, không nghiệm thu kết quả.
2. Đối chiếu từng điều đã chốt của D-07 với lựa chọn kỹ thuật còn mở; đề cương phải có nhánh thành công, lỗi/không rõ và gián đoạn; không bổ sung default.
3. Ghi finding và phạm vi được đề xuất trong docs/decisions/D-07-resolution.md; để mở mọi bằng chứng chưa có, chuyển yêu cầu sản phẩm mới cho người dùng thay vì tự chọn.

**Tiêu chí nghiệm thu:**

- [ ] AT-A00-07-01: Rà đề cương D-07: đủ đầu vào giả, task tạo bằng chứng, giới hạn quyền, timeout/cleanup, whitelist dự kiến và rủi ro; không yêu cầu bằng chứng do task bị chặn bởi gate này tạo ra.
- [ ] AT-A00-07-02: Không duyệt lại câu trả lời đã chốt. Nếu đề cương đổi trải nghiệm/chi phí/quyền thì ghi câu hỏi và chờ người dùng; nếu chỉ kiểm chứng kỹ thuật thì reviewer ghi phạm vi thử, không tự cấp quyền production. Kết quả còn phải nghiệm thu sau phép thử.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py and Python312 docs/product/AI/validate_dossier.py: existing documentation consistency checks only; manual scoped review of named output remains required.

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "NOT_APPLICABLE_DOCUMENT_REVIEW", "owner": null, "command": null, "gate": "Document/research/proposal/checkpoint review has no executable bootstrap prerequisite. Entry requires available source docs, explicit documentation scope and predecessor documents. Use existing dossier/task validators for consistency; runtime evidence, if needed for checkpoint completion, belongs to listed producer dependencies, never an entry prerequisite for proposing a probe."}

**Chủ nhiệm chuẩn bị công cụ:**

This is a planning/research/checkpoint task; any executable probe still requires scoped authorization and an established bounded command.

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [A00-08] Rà đề cương và phạm vi phép thử D-08

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

finalreview

**Mã yêu cầu:**

Enabler; linked predecessors define bounded output.

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Gate đề cương D-08; không phải nghiệm thu kết quả

**Phụ thuộc:**

R00-08

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/decisions/D-08-resolution.md

**Các bước cụ thể:**

1. Đọc đề cương R00-08 và DECISIONS D-08; ghi rõ đây là rà trước phép thử, không nghiệm thu kết quả.
2. Đối chiếu từng điều đã chốt của D-08 với lựa chọn kỹ thuật còn mở; đề cương phải có nhánh thành công, lỗi/không rõ và gián đoạn; không bổ sung default.
3. Ghi finding và phạm vi được đề xuất trong docs/decisions/D-08-resolution.md; để mở mọi bằng chứng chưa có, chuyển yêu cầu sản phẩm mới cho người dùng thay vì tự chọn.

**Tiêu chí nghiệm thu:**

- [ ] AT-A00-08-01: Rà đề cương D-08: đủ đầu vào giả, task tạo bằng chứng, giới hạn quyền, timeout/cleanup, whitelist dự kiến và rủi ro; không yêu cầu bằng chứng do task bị chặn bởi gate này tạo ra.
- [ ] AT-A00-08-02: Không duyệt lại câu trả lời đã chốt. Nếu đề cương đổi trải nghiệm/chi phí/quyền thì ghi câu hỏi và chờ người dùng; nếu chỉ kiểm chứng kỹ thuật thì reviewer ghi phạm vi thử, không tự cấp quyền production. Kết quả còn phải nghiệm thu sau phép thử.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py and Python312 docs/product/AI/validate_dossier.py: existing documentation consistency checks only; manual scoped review of named output remains required.

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "NOT_APPLICABLE_DOCUMENT_REVIEW", "owner": null, "command": null, "gate": "Document/research/proposal/checkpoint review has no executable bootstrap prerequisite. Entry requires available source docs, explicit documentation scope and predecessor documents. Use existing dossier/task validators for consistency; runtime evidence, if needed for checkpoint completion, belongs to listed producer dependencies, never an entry prerequisite for proposing a probe."}

**Chủ nhiệm chuẩn bị công cụ:**

This is a planning/research/checkpoint task; any executable probe still requires scoped authorization and an established bounded command.

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [A00-18] Rà đề cương và phạm vi phép thử D-18

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

finalreview

**Mã yêu cầu:**

AI02

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Gate đề cương D-18; không phải nghiệm thu kết quả

**Phụ thuộc:**

R00-18

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/decisions/D-18-resolution.md

**Các bước cụ thể:**

1. Đọc đề cương R00-18 và DECISIONS D-18; ghi rõ đây là rà trước phép thử, không nghiệm thu kết quả.
2. Đối chiếu từng điều đã chốt của D-18 với lựa chọn kỹ thuật còn mở; đề cương phải có nhánh thành công, lỗi/không rõ và gián đoạn; không bổ sung default.
3. Ghi finding và phạm vi được đề xuất trong docs/decisions/D-18-resolution.md; để mở mọi bằng chứng chưa có, chuyển yêu cầu sản phẩm mới cho người dùng thay vì tự chọn.

**Tiêu chí nghiệm thu:**

- [ ] AT-A00-18-01: Rà đề cương D-18: đủ đầu vào giả, task tạo bằng chứng, giới hạn quyền, timeout/cleanup, whitelist dự kiến và rủi ro; không yêu cầu bằng chứng do task bị chặn bởi gate này tạo ra.
- [ ] AT-A00-18-02: Không duyệt lại câu trả lời đã chốt. Nếu đề cương đổi trải nghiệm/chi phí/quyền thì ghi câu hỏi và chờ người dùng; nếu chỉ kiểm chứng kỹ thuật thì reviewer ghi phạm vi thử, không tự cấp quyền production. Kết quả còn phải nghiệm thu sau phép thử.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py and Python312 docs/product/AI/validate_dossier.py: existing documentation consistency checks only; manual scoped review of named output remains required.

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "NOT_APPLICABLE_DOCUMENT_REVIEW", "owner": null, "command": null, "gate": "Document/research/proposal/checkpoint review has no executable bootstrap prerequisite. Entry requires available source docs, explicit documentation scope and predecessor documents. Use existing dossier/task validators for consistency; runtime evidence, if needed for checkpoint completion, belongs to listed producer dependencies, never an entry prerequisite for proposing a probe."}

**Chủ nhiệm chuẩn bị công cụ:**

This is a planning/research/checkpoint task; any executable probe still requires scoped authorization and an established bounded command.

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [A00-05] Rà đề cương và phạm vi phép thử D-05

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

finalreview

**Mã yêu cầu:**

NV11, QH05

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Gate đề cương D-05; không phải nghiệm thu kết quả

**Phụ thuộc:**

R00-05

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/decisions/D-05-resolution.md

**Các bước cụ thể:**

1. Đọc đề cương R00-05 và DECISIONS D-05; ghi rõ đây là rà trước phép thử, không nghiệm thu kết quả.
2. Đối chiếu từng điều đã chốt của D-05 với lựa chọn kỹ thuật còn mở; đề cương phải có nhánh thành công, lỗi/không rõ và gián đoạn; không bổ sung default.
3. Ghi finding và phạm vi được đề xuất trong docs/decisions/D-05-resolution.md; để mở mọi bằng chứng chưa có, chuyển yêu cầu sản phẩm mới cho người dùng thay vì tự chọn.

**Tiêu chí nghiệm thu:**

- [ ] AT-A00-05-01: Rà đề cương D-05: đủ đầu vào giả, task tạo bằng chứng, giới hạn quyền, timeout/cleanup, whitelist dự kiến và rủi ro; không yêu cầu bằng chứng do task bị chặn bởi gate này tạo ra.
- [ ] AT-A00-05-02: Không duyệt lại câu trả lời đã chốt. Nếu đề cương đổi trải nghiệm/chi phí/quyền thì ghi câu hỏi và chờ người dùng; nếu chỉ kiểm chứng kỹ thuật thì reviewer ghi phạm vi thử, không tự cấp quyền production. Kết quả còn phải nghiệm thu sau phép thử.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py and Python312 docs/product/AI/validate_dossier.py: existing documentation consistency checks only; manual scoped review of named output remains required.

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "NOT_APPLICABLE_DOCUMENT_REVIEW", "owner": null, "command": null, "gate": "Document/research/proposal/checkpoint review has no executable bootstrap prerequisite. Entry requires available source docs, explicit documentation scope and predecessor documents. Use existing dossier/task validators for consistency; runtime evidence, if needed for checkpoint completion, belongs to listed producer dependencies, never an entry prerequisite for proposing a probe."}

**Chủ nhiệm chuẩn bị công cụ:**

This is a planning/research/checkpoint task; any executable probe still requires scoped authorization and an established bounded command.

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [A00-11] Rà đề cương và phạm vi phép thử D-11

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

finalreview

**Mã yêu cầu:**

XP08

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Gate đề cương D-11; không phải nghiệm thu kết quả

**Phụ thuộc:**

R00-11

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/decisions/D-11-resolution.md

**Các bước cụ thể:**

1. Đọc đề cương R00-11 và DECISIONS D-11; ghi rõ đây là rà trước phép thử, không nghiệm thu kết quả.
2. Đối chiếu từng điều đã chốt của D-11 với lựa chọn kỹ thuật còn mở; đề cương phải có nhánh thành công, lỗi/không rõ và gián đoạn; không bổ sung default.
3. Ghi finding và phạm vi được đề xuất trong docs/decisions/D-11-resolution.md; để mở mọi bằng chứng chưa có, chuyển yêu cầu sản phẩm mới cho người dùng thay vì tự chọn.

**Tiêu chí nghiệm thu:**

- [ ] AT-A00-11-01: Rà đề cương D-11: đủ đầu vào giả, task tạo bằng chứng, giới hạn quyền, timeout/cleanup, whitelist dự kiến và rủi ro; không yêu cầu bằng chứng do task bị chặn bởi gate này tạo ra.
- [ ] AT-A00-11-02: Không duyệt lại câu trả lời đã chốt. Nếu đề cương đổi trải nghiệm/chi phí/quyền thì ghi câu hỏi và chờ người dùng; nếu chỉ kiểm chứng kỹ thuật thì reviewer ghi phạm vi thử, không tự cấp quyền production. Kết quả còn phải nghiệm thu sau phép thử.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py and Python312 docs/product/AI/validate_dossier.py: existing documentation consistency checks only; manual scoped review of named output remains required.

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "NOT_APPLICABLE_DOCUMENT_REVIEW", "owner": null, "command": null, "gate": "Document/research/proposal/checkpoint review has no executable bootstrap prerequisite. Entry requires available source docs, explicit documentation scope and predecessor documents. Use existing dossier/task validators for consistency; runtime evidence, if needed for checkpoint completion, belongs to listed producer dependencies, never an entry prerequisite for proposing a probe."}

**Chủ nhiệm chuẩn bị công cụ:**

This is a planning/research/checkpoint task; any executable probe still requires scoped authorization and an established bounded command.

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [A00-14] Rà đề cương và phạm vi phép thử D-14

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

finalreview

**Mã yêu cầu:**

NV01, NV02, SH04

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Gate đề cương D-14; không phải nghiệm thu kết quả

**Phụ thuộc:**

R00-14

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/decisions/D-14-resolution.md

**Các bước cụ thể:**

1. Đọc đề cương R00-14 và DECISIONS D-14; ghi rõ đây là rà trước phép thử, không nghiệm thu kết quả.
2. Đối chiếu từng điều đã chốt của D-14 với lựa chọn kỹ thuật còn mở; đề cương phải có nhánh thành công, lỗi/không rõ và gián đoạn; không bổ sung default.
3. Ghi finding và phạm vi được đề xuất trong docs/decisions/D-14-resolution.md; để mở mọi bằng chứng chưa có, chuyển yêu cầu sản phẩm mới cho người dùng thay vì tự chọn.

**Tiêu chí nghiệm thu:**

- [ ] AT-A00-14-01: Rà đề cương D-14: đủ đầu vào giả, task tạo bằng chứng, giới hạn quyền, timeout/cleanup, whitelist dự kiến và rủi ro; không yêu cầu bằng chứng do task bị chặn bởi gate này tạo ra.
- [ ] AT-A00-14-02: Không duyệt lại câu trả lời đã chốt. Nếu đề cương đổi trải nghiệm/chi phí/quyền thì ghi câu hỏi và chờ người dùng; nếu chỉ kiểm chứng kỹ thuật thì reviewer ghi phạm vi thử, không tự cấp quyền production. Kết quả còn phải nghiệm thu sau phép thử.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py and Python312 docs/product/AI/validate_dossier.py: existing documentation consistency checks only; manual scoped review of named output remains required.

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "NOT_APPLICABLE_DOCUMENT_REVIEW", "owner": null, "command": null, "gate": "Document/research/proposal/checkpoint review has no executable bootstrap prerequisite. Entry requires available source docs, explicit documentation scope and predecessor documents. Use existing dossier/task validators for consistency; runtime evidence, if needed for checkpoint completion, belongs to listed producer dependencies, never an entry prerequisite for proposing a probe."}

**Chủ nhiệm chuẩn bị công cụ:**

This is a planning/research/checkpoint task; any executable probe still requires scoped authorization and an established bounded command.

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [A00-12] Rà đề cương và phạm vi phép thử D-12

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

finalreview

**Mã yêu cầu:**

SH01, QD04

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Gate đề cương D-12; không phải nghiệm thu kết quả

**Phụ thuộc:**

R00-12

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/decisions/D-12-resolution.md

**Các bước cụ thể:**

1. Đọc đề cương R00-12 và DECISIONS D-12; ghi rõ đây là rà trước phép thử, không nghiệm thu kết quả.
2. Đối chiếu từng điều đã chốt của D-12 với lựa chọn kỹ thuật còn mở; đề cương phải có nhánh thành công, lỗi/không rõ và gián đoạn; không bổ sung default.
3. Ghi finding và phạm vi được đề xuất trong docs/decisions/D-12-resolution.md; để mở mọi bằng chứng chưa có, chuyển yêu cầu sản phẩm mới cho người dùng thay vì tự chọn.

**Tiêu chí nghiệm thu:**

- [ ] AT-A00-12-01: Rà đề cương D-12: đủ đầu vào giả, task tạo bằng chứng, giới hạn quyền, timeout/cleanup, whitelist dự kiến và rủi ro; không yêu cầu bằng chứng do task bị chặn bởi gate này tạo ra.
- [ ] AT-A00-12-02: Không duyệt lại câu trả lời đã chốt. Nếu đề cương đổi trải nghiệm/chi phí/quyền thì ghi câu hỏi và chờ người dùng; nếu chỉ kiểm chứng kỹ thuật thì reviewer ghi phạm vi thử, không tự cấp quyền production. Kết quả còn phải nghiệm thu sau phép thử.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py and Python312 docs/product/AI/validate_dossier.py: existing documentation consistency checks only; manual scoped review of named output remains required.

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "NOT_APPLICABLE_DOCUMENT_REVIEW", "owner": null, "command": null, "gate": "Document/research/proposal/checkpoint review has no executable bootstrap prerequisite. Entry requires available source docs, explicit documentation scope and predecessor documents. Use existing dossier/task validators for consistency; runtime evidence, if needed for checkpoint completion, belongs to listed producer dependencies, never an entry prerequisite for proposing a probe."}

**Chủ nhiệm chuẩn bị công cụ:**

This is a planning/research/checkpoint task; any executable probe still requires scoped authorization and an established bounded command.

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [A00-17] Rà đề cương và phạm vi phép thử D-17

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

finalreview

**Mã yêu cầu:**

BH02, BH06

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Gate đề cương D-17; không phải nghiệm thu kết quả

**Phụ thuộc:**

R00-17

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/decisions/D-17-resolution.md

**Các bước cụ thể:**

1. Đọc đề cương R00-17 và DECISIONS D-17; ghi rõ đây là rà trước phép thử, không nghiệm thu kết quả.
2. Đối chiếu từng điều đã chốt của D-17 với lựa chọn kỹ thuật còn mở; đề cương phải có nhánh thành công, lỗi/không rõ và gián đoạn; không bổ sung default.
3. Ghi finding và phạm vi được đề xuất trong docs/decisions/D-17-resolution.md; để mở mọi bằng chứng chưa có, chuyển yêu cầu sản phẩm mới cho người dùng thay vì tự chọn.

**Tiêu chí nghiệm thu:**

- [ ] AT-A00-17-01: Rà đề cương D-17: đủ đầu vào giả, task tạo bằng chứng, giới hạn quyền, timeout/cleanup, whitelist dự kiến và rủi ro; không yêu cầu bằng chứng do task bị chặn bởi gate này tạo ra.
- [ ] AT-A00-17-02: Không duyệt lại câu trả lời đã chốt. Nếu đề cương đổi trải nghiệm/chi phí/quyền thì ghi câu hỏi và chờ người dùng; nếu chỉ kiểm chứng kỹ thuật thì reviewer ghi phạm vi thử, không tự cấp quyền production. Kết quả còn phải nghiệm thu sau phép thử.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py and Python312 docs/product/AI/validate_dossier.py: existing documentation consistency checks only; manual scoped review of named output remains required.

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "NOT_APPLICABLE_DOCUMENT_REVIEW", "owner": null, "command": null, "gate": "Document/research/proposal/checkpoint review has no executable bootstrap prerequisite. Entry requires available source docs, explicit documentation scope and predecessor documents. Use existing dossier/task validators for consistency; runtime evidence, if needed for checkpoint completion, belongs to listed producer dependencies, never an entry prerequisite for proposing a probe."}

**Chủ nhiệm chuẩn bị công cụ:**

This is a planning/research/checkpoint task; any executable probe still requires scoped authorization and an established bounded command.

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [A00-06] Rà đề cương và phạm vi phép thử D-06

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

finalreview

**Mã yêu cầu:**

XP07

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Gate đề cương D-06; không phải nghiệm thu kết quả

**Phụ thuộc:**

R00-06

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/decisions/D-06-resolution.md

**Các bước cụ thể:**

1. Đọc đề cương R00-06 và DECISIONS D-06; ghi rõ đây là rà trước phép thử, không nghiệm thu kết quả.
2. Đối chiếu từng điều đã chốt của D-06 với lựa chọn kỹ thuật còn mở; đề cương phải có nhánh thành công, lỗi/không rõ và gián đoạn; không bổ sung default.
3. Ghi finding và phạm vi được đề xuất trong docs/decisions/D-06-resolution.md; để mở mọi bằng chứng chưa có, chuyển yêu cầu sản phẩm mới cho người dùng thay vì tự chọn.

**Tiêu chí nghiệm thu:**

- [ ] AT-A00-06-01: Rà đề cương D-06: đủ đầu vào giả, task tạo bằng chứng, giới hạn quyền, timeout/cleanup, whitelist dự kiến và rủi ro; không yêu cầu bằng chứng do task bị chặn bởi gate này tạo ra.
- [ ] AT-A00-06-02: Không duyệt lại câu trả lời đã chốt. Nếu đề cương đổi trải nghiệm/chi phí/quyền thì ghi câu hỏi và chờ người dùng; nếu chỉ kiểm chứng kỹ thuật thì reviewer ghi phạm vi thử, không tự cấp quyền production. Kết quả còn phải nghiệm thu sau phép thử.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py and Python312 docs/product/AI/validate_dossier.py: existing documentation consistency checks only; manual scoped review of named output remains required.

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "NOT_APPLICABLE_DOCUMENT_REVIEW", "owner": null, "command": null, "gate": "Document/research/proposal/checkpoint review has no executable bootstrap prerequisite. Entry requires available source docs, explicit documentation scope and predecessor documents. Use existing dossier/task validators for consistency; runtime evidence, if needed for checkpoint completion, belongs to listed producer dependencies, never an entry prerequisite for proposing a probe."}

**Chủ nhiệm chuẩn bị công cụ:**

This is a planning/research/checkpoint task; any executable probe still requires scoped authorization and an established bounded command.

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [A00-09] Rà đề cương và phạm vi phép thử D-09

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

finalreview

**Mã yêu cầu:**

SL01

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Gate đề cương D-09; không phải nghiệm thu kết quả

**Phụ thuộc:**

R00-09

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/decisions/D-09-resolution.md

**Các bước cụ thể:**

1. Đọc đề cương R00-09 và DECISIONS D-09; ghi rõ đây là rà trước phép thử, không nghiệm thu kết quả.
2. Đối chiếu từng điều đã chốt của D-09 với lựa chọn kỹ thuật còn mở; đề cương phải có nhánh thành công, lỗi/không rõ và gián đoạn; không bổ sung default.
3. Ghi finding và phạm vi được đề xuất trong docs/decisions/D-09-resolution.md; để mở mọi bằng chứng chưa có, chuyển yêu cầu sản phẩm mới cho người dùng thay vì tự chọn.

**Tiêu chí nghiệm thu:**

- [ ] AT-A00-09-01: Rà đề cương D-09: đủ đầu vào giả, task tạo bằng chứng, giới hạn quyền, timeout/cleanup, whitelist dự kiến và rủi ro; không yêu cầu bằng chứng do task bị chặn bởi gate này tạo ra.
- [ ] AT-A00-09-02: Không duyệt lại câu trả lời đã chốt. Nếu đề cương đổi trải nghiệm/chi phí/quyền thì ghi câu hỏi và chờ người dùng; nếu chỉ kiểm chứng kỹ thuật thì reviewer ghi phạm vi thử, không tự cấp quyền production. Kết quả còn phải nghiệm thu sau phép thử.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py and Python312 docs/product/AI/validate_dossier.py: existing documentation consistency checks only; manual scoped review of named output remains required.

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "NOT_APPLICABLE_DOCUMENT_REVIEW", "owner": null, "command": null, "gate": "Document/research/proposal/checkpoint review has no executable bootstrap prerequisite. Entry requires available source docs, explicit documentation scope and predecessor documents. Use existing dossier/task validators for consistency; runtime evidence, if needed for checkpoint completion, belongs to listed producer dependencies, never an entry prerequisite for proposing a probe."}

**Chủ nhiệm chuẩn bị công cụ:**

This is a planning/research/checkpoint task; any executable probe still requires scoped authorization and an established bounded command.

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.
