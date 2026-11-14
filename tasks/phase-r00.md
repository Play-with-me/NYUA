# R00 task cards

Generated from docs/product/AI/backlog.json. Grouping is navigation only; dependencies below determine dispatch. No phase-level edges. All future work requires separate authorization.

## [R00-02] Resolve residual evidence: D-02

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

research

**Mã yêu cầu:**

SP09, BH06

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Đề cương phép thử còn mở D-02

**Phụ thuộc:**

P00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/experiments/D-02.md

**Các bước cụ thể:**

1. Đọc đúng phần D-02 trong DECISIONS và nguồn append nguyên văn; trích riêng hành vi đã chốt, không hỏi lại.
2. Lập bảng lựa chọn cho phần dư của D-02: nguồn chính thức cần tra, dữ liệu giả, kết quả cần đo và trường hợp phải chặn.
3. Viết đề cương tại docs/experiments/D-02.md với đầu vào/đầu ra, bootstrap chịu trách nhiệm và phép thử tương ứng trong P02/P03/P10/P30/P40/P50; ghi chưa chạy, không đòi bằng chứng tương lai để duyệt đề cương.

**Tiêu chí nghiệm thu:**

- [ ] AT-R00-02-01: Phân loại câu hỏi còn mở của D-02 trong DECISIONS: bằng chứng hiện có, điều đã chốt, lựa chọn kỹ thuật và điều cần hỏi người dùng; không yêu cầu kết quả của phép thử chưa được chạy.
- [ ] AT-R00-02-02: Đề cương ghi fixture, quan sát mong đợi, điều kiện dừng, bootstrap owner và task sẽ tạo bằng chứng; không chốt API/model/threshold hoặc chi phí khi thiếu bằng chứng.

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

## [R00-03] Resolve residual evidence: D-03

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

Đề cương phép thử còn mở D-03

**Phụ thuộc:**

P00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/experiments/D-03.md

**Các bước cụ thể:**

1. Đọc đúng phần D-03 trong DECISIONS và nguồn append nguyên văn; trích riêng hành vi đã chốt, không hỏi lại.
2. Lập bảng lựa chọn cho phần dư của D-03: nguồn chính thức cần tra, dữ liệu giả, kết quả cần đo và trường hợp phải chặn.
3. Viết đề cương tại docs/experiments/D-03.md với đầu vào/đầu ra, bootstrap chịu trách nhiệm và phép thử tương ứng trong P02/P03/P10/P30/P40/P50; ghi chưa chạy, không đòi bằng chứng tương lai để duyệt đề cương.

**Tiêu chí nghiệm thu:**

- [ ] AT-R00-03-01: Phân loại câu hỏi còn mở của D-03 trong DECISIONS: bằng chứng hiện có, điều đã chốt, lựa chọn kỹ thuật và điều cần hỏi người dùng; không yêu cầu kết quả của phép thử chưa được chạy.
- [ ] AT-R00-03-02: Đề cương ghi fixture, quan sát mong đợi, điều kiện dừng, bootstrap owner và task sẽ tạo bằng chứng; không chốt API/model/threshold hoặc chi phí khi thiếu bằng chứng.

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

## [R00-04] Resolve residual evidence: D-04

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

Đề cương phép thử còn mở D-04

**Phụ thuộc:**

P00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/experiments/D-04.md

**Các bước cụ thể:**

1. Đọc đúng phần D-04 trong DECISIONS và nguồn append nguyên văn; trích riêng hành vi đã chốt, không hỏi lại.
2. Lập bảng lựa chọn cho phần dư của D-04: nguồn chính thức cần tra, dữ liệu giả, kết quả cần đo và trường hợp phải chặn.
3. Viết đề cương tại docs/experiments/D-04.md với đầu vào/đầu ra, bootstrap chịu trách nhiệm và phép thử tương ứng trong P02/P03/P10/P30/P40/P50; ghi chưa chạy, không đòi bằng chứng tương lai để duyệt đề cương.

**Tiêu chí nghiệm thu:**

- [ ] AT-R00-04-01: Phân loại câu hỏi còn mở của D-04 trong DECISIONS: bằng chứng hiện có, điều đã chốt, lựa chọn kỹ thuật và điều cần hỏi người dùng; không yêu cầu kết quả của phép thử chưa được chạy.
- [ ] AT-R00-04-02: Đề cương ghi fixture, quan sát mong đợi, điều kiện dừng, bootstrap owner và task sẽ tạo bằng chứng; không chốt API/model/threshold hoặc chi phí khi thiếu bằng chứng.

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

## [R00-13] Resolve residual evidence: D-13

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

Đề cương phép thử còn mở D-13

**Phụ thuộc:**

P00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/experiments/D-13.md

**Các bước cụ thể:**

1. Đọc đúng phần D-13 trong DECISIONS và nguồn append nguyên văn; trích riêng hành vi đã chốt, không hỏi lại.
2. Lập bảng lựa chọn cho phần dư của D-13: nguồn chính thức cần tra, dữ liệu giả, kết quả cần đo và trường hợp phải chặn.
3. Viết đề cương tại docs/experiments/D-13.md với đầu vào/đầu ra, bootstrap chịu trách nhiệm và phép thử tương ứng trong P02/P03/P10/P30/P40/P50; ghi chưa chạy, không đòi bằng chứng tương lai để duyệt đề cương.

**Tiêu chí nghiệm thu:**

- [ ] AT-R00-13-01: Phân loại câu hỏi còn mở của D-13 trong DECISIONS: bằng chứng hiện có, điều đã chốt, lựa chọn kỹ thuật và điều cần hỏi người dùng; không yêu cầu kết quả của phép thử chưa được chạy.
- [ ] AT-R00-13-02: Đề cương ghi fixture, quan sát mong đợi, điều kiện dừng, bootstrap owner và task sẽ tạo bằng chứng; không chốt API/model/threshold hoặc chi phí khi thiếu bằng chứng.

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

## [R00-01] Resolve residual evidence: D-01

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

Đề cương phép thử còn mở D-01

**Phụ thuộc:**

P00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/experiments/D-01.md

**Các bước cụ thể:**

1. Đọc đúng phần D-01 trong DECISIONS và nguồn append nguyên văn; trích riêng hành vi đã chốt, không hỏi lại.
2. Lập bảng lựa chọn cho phần dư của D-01: nguồn chính thức cần tra, dữ liệu giả, kết quả cần đo và trường hợp phải chặn.
3. Viết đề cương tại docs/experiments/D-01.md với đầu vào/đầu ra, bootstrap chịu trách nhiệm và phép thử tương ứng trong P02/P03/P10/P30/P40/P50; ghi chưa chạy, không đòi bằng chứng tương lai để duyệt đề cương.

**Tiêu chí nghiệm thu:**

- [ ] AT-R00-01-01: Phân loại câu hỏi còn mở của D-01 trong DECISIONS: bằng chứng hiện có, điều đã chốt, lựa chọn kỹ thuật và điều cần hỏi người dùng; không yêu cầu kết quả của phép thử chưa được chạy.
- [ ] AT-R00-01-02: Đề cương ghi fixture, quan sát mong đợi, điều kiện dừng, bootstrap owner và task sẽ tạo bằng chứng; không chốt API/model/threshold hoặc chi phí khi thiếu bằng chứng.

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

## [R00-10] Resolve residual evidence: D-10

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

research

**Mã yêu cầu:**

CD01, BH06

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Đề cương phép thử còn mở D-10

**Phụ thuộc:**

P00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/experiments/D-10.md

**Các bước cụ thể:**

1. Đọc đúng phần D-10 trong DECISIONS và nguồn append nguyên văn; trích riêng hành vi đã chốt, không hỏi lại.
2. Lập bảng lựa chọn cho phần dư của D-10: nguồn chính thức cần tra, dữ liệu giả, kết quả cần đo và trường hợp phải chặn.
3. Viết đề cương tại docs/experiments/D-10.md với đầu vào/đầu ra, bootstrap chịu trách nhiệm và phép thử tương ứng trong P02/P03/P10/P30/P40/P50; ghi chưa chạy, không đòi bằng chứng tương lai để duyệt đề cương.

**Tiêu chí nghiệm thu:**

- [ ] AT-R00-10-01: Phân loại câu hỏi còn mở của D-10 trong DECISIONS: bằng chứng hiện có, điều đã chốt, lựa chọn kỹ thuật và điều cần hỏi người dùng; không yêu cầu kết quả của phép thử chưa được chạy.
- [ ] AT-R00-10-02: Đề cương ghi fixture, quan sát mong đợi, điều kiện dừng, bootstrap owner và task sẽ tạo bằng chứng; không chốt API/model/threshold hoặc chi phí khi thiếu bằng chứng.

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

## [R00-15] Resolve residual evidence: D-15

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

Đề cương phép thử còn mở D-15

**Phụ thuộc:**

P00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/experiments/D-15.md

**Các bước cụ thể:**

1. Đọc đúng phần D-15 trong DECISIONS và nguồn append nguyên văn; trích riêng hành vi đã chốt, không hỏi lại.
2. Lập bảng lựa chọn cho phần dư của D-15: nguồn chính thức cần tra, dữ liệu giả, kết quả cần đo và trường hợp phải chặn.
3. Viết đề cương tại docs/experiments/D-15.md với đầu vào/đầu ra, bootstrap chịu trách nhiệm và phép thử tương ứng trong P02/P03/P10/P30/P40/P50; ghi chưa chạy, không đòi bằng chứng tương lai để duyệt đề cương.

**Tiêu chí nghiệm thu:**

- [ ] AT-R00-15-01: Phân loại câu hỏi còn mở của D-15 trong DECISIONS: bằng chứng hiện có, điều đã chốt, lựa chọn kỹ thuật và điều cần hỏi người dùng; không yêu cầu kết quả của phép thử chưa được chạy.
- [ ] AT-R00-15-02: Đề cương ghi fixture, quan sát mong đợi, điều kiện dừng, bootstrap owner và task sẽ tạo bằng chứng; không chốt API/model/threshold hoặc chi phí khi thiếu bằng chứng.

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

## [R00-16] Resolve residual evidence: D-16

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

research

**Mã yêu cầu:**

AI01, XP05

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Đề cương phép thử còn mở D-16

**Phụ thuộc:**

P00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/experiments/D-16.md

**Các bước cụ thể:**

1. Đọc đúng phần D-16 trong DECISIONS và nguồn append nguyên văn; trích riêng hành vi đã chốt, không hỏi lại.
2. Lập bảng lựa chọn cho phần dư của D-16: nguồn chính thức cần tra, dữ liệu giả, kết quả cần đo và trường hợp phải chặn.
3. Viết đề cương tại docs/experiments/D-16.md với đầu vào/đầu ra, bootstrap chịu trách nhiệm và phép thử tương ứng trong P02/P03/P10/P30/P40/P50; ghi chưa chạy, không đòi bằng chứng tương lai để duyệt đề cương.

**Tiêu chí nghiệm thu:**

- [ ] AT-R00-16-01: Phân loại câu hỏi còn mở của D-16 trong DECISIONS: bằng chứng hiện có, điều đã chốt, lựa chọn kỹ thuật và điều cần hỏi người dùng; không yêu cầu kết quả của phép thử chưa được chạy.
- [ ] AT-R00-16-02: Đề cương ghi fixture, quan sát mong đợi, điều kiện dừng, bootstrap owner và task sẽ tạo bằng chứng; không chốt API/model/threshold hoặc chi phí khi thiếu bằng chứng.

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

## [R00-07] Resolve residual evidence: D-07

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

Đề cương phép thử còn mở D-07

**Phụ thuộc:**

P00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/experiments/D-07.md

**Các bước cụ thể:**

1. Đọc đúng phần D-07 trong DECISIONS và nguồn append nguyên văn; trích riêng hành vi đã chốt, không hỏi lại.
2. Lập bảng lựa chọn cho phần dư của D-07: nguồn chính thức cần tra, dữ liệu giả, kết quả cần đo và trường hợp phải chặn.
3. Viết đề cương tại docs/experiments/D-07.md với đầu vào/đầu ra, bootstrap chịu trách nhiệm và phép thử tương ứng trong P02/P03/P10/P30/P40/P50; ghi chưa chạy, không đòi bằng chứng tương lai để duyệt đề cương.

**Tiêu chí nghiệm thu:**

- [ ] AT-R00-07-01: Phân loại câu hỏi còn mở của D-07 trong DECISIONS: bằng chứng hiện có, điều đã chốt, lựa chọn kỹ thuật và điều cần hỏi người dùng; không yêu cầu kết quả của phép thử chưa được chạy.
- [ ] AT-R00-07-02: Đề cương ghi fixture, quan sát mong đợi, điều kiện dừng, bootstrap owner và task sẽ tạo bằng chứng; không chốt API/model/threshold hoặc chi phí khi thiếu bằng chứng.

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

## [R00-08] Resolve residual evidence: D-08

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

Đề cương phép thử còn mở D-08

**Phụ thuộc:**

P00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/experiments/D-08.md

**Các bước cụ thể:**

1. Đọc đúng phần D-08 trong DECISIONS và nguồn append nguyên văn; trích riêng hành vi đã chốt, không hỏi lại.
2. Lập bảng lựa chọn cho phần dư của D-08: nguồn chính thức cần tra, dữ liệu giả, kết quả cần đo và trường hợp phải chặn.
3. Viết đề cương tại docs/experiments/D-08.md với đầu vào/đầu ra, bootstrap chịu trách nhiệm và phép thử tương ứng trong P02/P03/P10/P30/P40/P50; ghi chưa chạy, không đòi bằng chứng tương lai để duyệt đề cương.

**Tiêu chí nghiệm thu:**

- [ ] AT-R00-08-01: Phân loại câu hỏi còn mở của D-08 trong DECISIONS: bằng chứng hiện có, điều đã chốt, lựa chọn kỹ thuật và điều cần hỏi người dùng; không yêu cầu kết quả của phép thử chưa được chạy.
- [ ] AT-R00-08-02: Đề cương ghi fixture, quan sát mong đợi, điều kiện dừng, bootstrap owner và task sẽ tạo bằng chứng; không chốt API/model/threshold hoặc chi phí khi thiếu bằng chứng.

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

## [R00-18] Resolve residual evidence: D-18

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

research

**Mã yêu cầu:**

AI02

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Đề cương phép thử còn mở D-18

**Phụ thuộc:**

P00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/experiments/D-18.md

**Các bước cụ thể:**

1. Đọc đúng phần D-18 trong DECISIONS và nguồn append nguyên văn; trích riêng hành vi đã chốt, không hỏi lại.
2. Lập bảng lựa chọn cho phần dư của D-18: nguồn chính thức cần tra, dữ liệu giả, kết quả cần đo và trường hợp phải chặn.
3. Viết đề cương tại docs/experiments/D-18.md với đầu vào/đầu ra, bootstrap chịu trách nhiệm và phép thử tương ứng trong P02/P03/P10/P30/P40/P50; ghi chưa chạy, không đòi bằng chứng tương lai để duyệt đề cương.

**Tiêu chí nghiệm thu:**

- [ ] AT-R00-18-01: Phân loại câu hỏi còn mở của D-18 trong DECISIONS: bằng chứng hiện có, điều đã chốt, lựa chọn kỹ thuật và điều cần hỏi người dùng; không yêu cầu kết quả của phép thử chưa được chạy.
- [ ] AT-R00-18-02: Đề cương ghi fixture, quan sát mong đợi, điều kiện dừng, bootstrap owner và task sẽ tạo bằng chứng; không chốt API/model/threshold hoặc chi phí khi thiếu bằng chứng.

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

## [R00-05] Resolve residual evidence: D-05

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

research

**Mã yêu cầu:**

NV11, QH05

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Đề cương phép thử còn mở D-05

**Phụ thuộc:**

P00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/experiments/D-05.md

**Các bước cụ thể:**

1. Đọc đúng phần D-05 trong DECISIONS và nguồn append nguyên văn; trích riêng hành vi đã chốt, không hỏi lại.
2. Lập bảng lựa chọn cho phần dư của D-05: nguồn chính thức cần tra, dữ liệu giả, kết quả cần đo và trường hợp phải chặn.
3. Viết đề cương tại docs/experiments/D-05.md với đầu vào/đầu ra, bootstrap chịu trách nhiệm và phép thử tương ứng trong P02/P03/P10/P30/P40/P50; ghi chưa chạy, không đòi bằng chứng tương lai để duyệt đề cương.

**Tiêu chí nghiệm thu:**

- [ ] AT-R00-05-01: Phân loại câu hỏi còn mở của D-05 trong DECISIONS: bằng chứng hiện có, điều đã chốt, lựa chọn kỹ thuật và điều cần hỏi người dùng; không yêu cầu kết quả của phép thử chưa được chạy.
- [ ] AT-R00-05-02: Đề cương ghi fixture, quan sát mong đợi, điều kiện dừng, bootstrap owner và task sẽ tạo bằng chứng; không chốt API/model/threshold hoặc chi phí khi thiếu bằng chứng.

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

## [R00-11] Resolve residual evidence: D-11

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

research

**Mã yêu cầu:**

XP08

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Đề cương phép thử còn mở D-11

**Phụ thuộc:**

P00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/experiments/D-11.md

**Các bước cụ thể:**

1. Đọc đúng phần D-11 trong DECISIONS và nguồn append nguyên văn; trích riêng hành vi đã chốt, không hỏi lại.
2. Lập bảng lựa chọn cho phần dư của D-11: nguồn chính thức cần tra, dữ liệu giả, kết quả cần đo và trường hợp phải chặn.
3. Viết đề cương tại docs/experiments/D-11.md với đầu vào/đầu ra, bootstrap chịu trách nhiệm và phép thử tương ứng trong P02/P03/P10/P30/P40/P50; ghi chưa chạy, không đòi bằng chứng tương lai để duyệt đề cương.

**Tiêu chí nghiệm thu:**

- [ ] AT-R00-11-01: Phân loại câu hỏi còn mở của D-11 trong DECISIONS: bằng chứng hiện có, điều đã chốt, lựa chọn kỹ thuật và điều cần hỏi người dùng; không yêu cầu kết quả của phép thử chưa được chạy.
- [ ] AT-R00-11-02: Đề cương ghi fixture, quan sát mong đợi, điều kiện dừng, bootstrap owner và task sẽ tạo bằng chứng; không chốt API/model/threshold hoặc chi phí khi thiếu bằng chứng.

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

## [R00-14] Resolve residual evidence: D-14

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

research

**Mã yêu cầu:**

NV01, NV02, SH04

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Đề cương phép thử còn mở D-14

**Phụ thuộc:**

P00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/experiments/D-14.md

**Các bước cụ thể:**

1. Đọc đúng phần D-14 trong DECISIONS và nguồn append nguyên văn; trích riêng hành vi đã chốt, không hỏi lại.
2. Lập bảng lựa chọn cho phần dư của D-14: nguồn chính thức cần tra, dữ liệu giả, kết quả cần đo và trường hợp phải chặn.
3. Viết đề cương tại docs/experiments/D-14.md với đầu vào/đầu ra, bootstrap chịu trách nhiệm và phép thử tương ứng trong P02/P03/P10/P30/P40/P50; ghi chưa chạy, không đòi bằng chứng tương lai để duyệt đề cương.

**Tiêu chí nghiệm thu:**

- [ ] AT-R00-14-01: Phân loại câu hỏi còn mở của D-14 trong DECISIONS: bằng chứng hiện có, điều đã chốt, lựa chọn kỹ thuật và điều cần hỏi người dùng; không yêu cầu kết quả của phép thử chưa được chạy.
- [ ] AT-R00-14-02: Đề cương ghi fixture, quan sát mong đợi, điều kiện dừng, bootstrap owner và task sẽ tạo bằng chứng; không chốt API/model/threshold hoặc chi phí khi thiếu bằng chứng.

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

## [R00-12] Resolve residual evidence: D-12

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

research

**Mã yêu cầu:**

SH01, QD04

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Đề cương phép thử còn mở D-12

**Phụ thuộc:**

P00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/experiments/D-12.md

**Các bước cụ thể:**

1. Đọc đúng phần D-12 trong DECISIONS và nguồn append nguyên văn; trích riêng hành vi đã chốt, không hỏi lại.
2. Lập bảng lựa chọn cho phần dư của D-12: nguồn chính thức cần tra, dữ liệu giả, kết quả cần đo và trường hợp phải chặn.
3. Viết đề cương tại docs/experiments/D-12.md với đầu vào/đầu ra, bootstrap chịu trách nhiệm và phép thử tương ứng trong P02/P03/P10/P30/P40/P50; ghi chưa chạy, không đòi bằng chứng tương lai để duyệt đề cương.

**Tiêu chí nghiệm thu:**

- [ ] AT-R00-12-01: Phân loại câu hỏi còn mở của D-12 trong DECISIONS: bằng chứng hiện có, điều đã chốt, lựa chọn kỹ thuật và điều cần hỏi người dùng; không yêu cầu kết quả của phép thử chưa được chạy.
- [ ] AT-R00-12-02: Đề cương ghi fixture, quan sát mong đợi, điều kiện dừng, bootstrap owner và task sẽ tạo bằng chứng; không chốt API/model/threshold hoặc chi phí khi thiếu bằng chứng.

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

## [R00-17] Resolve residual evidence: D-17

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

research

**Mã yêu cầu:**

BH02, BH06

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Đề cương phép thử còn mở D-17

**Phụ thuộc:**

P00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/experiments/D-17.md

**Các bước cụ thể:**

1. Đọc đúng phần D-17 trong DECISIONS và nguồn append nguyên văn; trích riêng hành vi đã chốt, không hỏi lại.
2. Lập bảng lựa chọn cho phần dư của D-17: nguồn chính thức cần tra, dữ liệu giả, kết quả cần đo và trường hợp phải chặn.
3. Viết đề cương tại docs/experiments/D-17.md với đầu vào/đầu ra, bootstrap chịu trách nhiệm và phép thử tương ứng trong P02/P03/P10/P30/P40/P50; ghi chưa chạy, không đòi bằng chứng tương lai để duyệt đề cương.

**Tiêu chí nghiệm thu:**

- [ ] AT-R00-17-01: Phân loại câu hỏi còn mở của D-17 trong DECISIONS: bằng chứng hiện có, điều đã chốt, lựa chọn kỹ thuật và điều cần hỏi người dùng; không yêu cầu kết quả của phép thử chưa được chạy.
- [ ] AT-R00-17-02: Đề cương ghi fixture, quan sát mong đợi, điều kiện dừng, bootstrap owner và task sẽ tạo bằng chứng; không chốt API/model/threshold hoặc chi phí khi thiếu bằng chứng.

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

## [R00-06] Resolve residual evidence: D-06

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

research

**Mã yêu cầu:**

XP07

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Đề cương phép thử còn mở D-06

**Phụ thuộc:**

P00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/experiments/D-06.md

**Các bước cụ thể:**

1. Đọc đúng phần D-06 trong DECISIONS và nguồn append nguyên văn; trích riêng hành vi đã chốt, không hỏi lại.
2. Lập bảng lựa chọn cho phần dư của D-06: nguồn chính thức cần tra, dữ liệu giả, kết quả cần đo và trường hợp phải chặn.
3. Viết đề cương tại docs/experiments/D-06.md với đầu vào/đầu ra, bootstrap chịu trách nhiệm và phép thử tương ứng trong P02/P03/P10/P30/P40/P50; ghi chưa chạy, không đòi bằng chứng tương lai để duyệt đề cương.

**Tiêu chí nghiệm thu:**

- [ ] AT-R00-06-01: Phân loại câu hỏi còn mở của D-06 trong DECISIONS: bằng chứng hiện có, điều đã chốt, lựa chọn kỹ thuật và điều cần hỏi người dùng; không yêu cầu kết quả của phép thử chưa được chạy.
- [ ] AT-R00-06-02: Đề cương ghi fixture, quan sát mong đợi, điều kiện dừng, bootstrap owner và task sẽ tạo bằng chứng; không chốt API/model/threshold hoặc chi phí khi thiếu bằng chứng.

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

## [R00-09] Resolve residual evidence: D-09

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

research

**Mã yêu cầu:**

SL01

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Đề cương phép thử còn mở D-09

**Phụ thuộc:**

P00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/experiments/D-09.md

**Các bước cụ thể:**

1. Đọc đúng phần D-09 trong DECISIONS và nguồn append nguyên văn; trích riêng hành vi đã chốt, không hỏi lại.
2. Lập bảng lựa chọn cho phần dư của D-09: nguồn chính thức cần tra, dữ liệu giả, kết quả cần đo và trường hợp phải chặn.
3. Viết đề cương tại docs/experiments/D-09.md với đầu vào/đầu ra, bootstrap chịu trách nhiệm và phép thử tương ứng trong P02/P03/P10/P30/P40/P50; ghi chưa chạy, không đòi bằng chứng tương lai để duyệt đề cương.

**Tiêu chí nghiệm thu:**

- [ ] AT-R00-09-01: Phân loại câu hỏi còn mở của D-09 trong DECISIONS: bằng chứng hiện có, điều đã chốt, lựa chọn kỹ thuật và điều cần hỏi người dùng; không yêu cầu kết quả của phép thử chưa được chạy.
- [ ] AT-R00-09-02: Đề cương ghi fixture, quan sát mong đợi, điều kiện dừng, bootstrap owner và task sẽ tạo bằng chứng; không chốt API/model/threshold hoặc chi phí khi thiếu bằng chứng.

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
