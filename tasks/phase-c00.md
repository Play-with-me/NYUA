# C00 task cards

Generated from docs/product/AI/backlog.json. Grouping is navigation only; dependencies below determine dispatch. No phase-level edges. All future work requires separate authorization.

## [C00-01] Baseline checkpoint

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

Baseline evidence checkpoint

**Phụ thuộc:**

P00-01, P00-02, P00-03, P00-04

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/checkpoints/C00-01.md

**Các bước cụ thể:**

1. Read the linked requirement clauses and confirmed decision limits; enumerate observable positive, negative and interruption cases for this single output.
2. Produce only the named output inside the proposed whitelist after a scoped authorization; record unresolved alternatives instead of inventing contracts.
3. Capture case-by-case expected/actual evidence and reviewer result; stop on a failed invariant and update traceability without approving human gates.

**Tiêu chí nghiệm thu:**

- [ ] AT-C00-01-01: Every listed predecessor has actual accepted evidence at its recorded revision; missing, failed or NOT RUN evidence blocks this checkpoint.
- [ ] AT-C00-01-02: Record exact local revision, unresolved limitations and required user acceptance separately; this checkpoint grants no publishing or production authorization.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": null, "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

This is a planning/research/checkpoint task; any executable probe still requires scoped authorization and an established bounded command.

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [C00-02] Probes checkpoint

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

Probes evidence checkpoint

**Phụ thuộc:**

P01-01, P02-05, P03-03

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/checkpoints/C00-02.md

**Các bước cụ thể:**

1. Read the linked requirement clauses and confirmed decision limits; enumerate observable positive, negative and interruption cases for this single output.
2. Produce only the named output inside the proposed whitelist after a scoped authorization; record unresolved alternatives instead of inventing contracts.
3. Capture case-by-case expected/actual evidence and reviewer result; stop on a failed invariant and update traceability without approving human gates.

**Tiêu chí nghiệm thu:**

- [ ] AT-C00-02-01: Every listed predecessor has actual accepted evidence at its recorded revision; missing, failed or NOT RUN evidence blocks this checkpoint.
- [ ] AT-C00-02-02: Record exact local revision, unresolved limitations and required user acceptance separately; this checkpoint grants no publishing or production authorization.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": null, "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

This is a planning/research/checkpoint task; any executable probe still requires scoped authorization and an established bounded command.

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [C00-03] Integrated slice checkpoint

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

Integrated slice evidence checkpoint

**Phụ thuộc:**

P60-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/checkpoints/C00-03.md

**Các bước cụ thể:**

1. Read the linked requirement clauses and confirmed decision limits; enumerate observable positive, negative and interruption cases for this single output.
2. Produce only the named output inside the proposed whitelist after a scoped authorization; record unresolved alternatives instead of inventing contracts.
3. Capture case-by-case expected/actual evidence and reviewer result; stop on a failed invariant and update traceability without approving human gates.

**Tiêu chí nghiệm thu:**

- [ ] AT-C00-03-01: Every listed predecessor has actual accepted evidence at its recorded revision; missing, failed or NOT RUN evidence blocks this checkpoint.
- [ ] AT-C00-03-02: Record exact local revision, unresolved limitations and required user acceptance separately; this checkpoint grants no publishing or production authorization.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": null, "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

This is a planning/research/checkpoint task; any executable probe still requires scoped authorization and an established bounded command.

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [C00-04] Full acceptance checkpoint

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

Full acceptance evidence checkpoint

**Phụ thuộc:**

V00-001, V00-002, V00-003, V00-004, V00-005, V00-006, V00-007, V00-008, V00-009, V00-010, V00-011, V00-012, V00-013, V00-014, V00-015, V00-016, V00-017, V00-018, V00-019, V00-020, V00-021, V00-022, V00-023, V00-024, V00-025, V00-026, V00-027, V00-028, V00-029, V00-030, V00-031, V00-032, V00-033, V00-034, V00-035, V00-036, V00-037, V00-038, V00-039, V00-040, V00-041, V00-042, V00-043, V00-044, V00-045, V00-046, V00-047, V00-048, V00-049, V00-050, V00-051, V00-052, V00-053, V00-054, V00-055, V00-056, V00-057, V00-058, V00-059, V00-060, V00-061, V00-062, V00-063, V00-064, V00-065, V00-066, V00-067, V00-068, V00-069, V00-070, V00-071, V00-072, V00-073, V00-074, V00-075, V00-076, V00-077, V00-078, V00-079, V00-080, V00-081, V00-082, V00-083, V00-084, V00-085, V00-086, V00-087, V00-088, V00-089, V00-090, V00-091, V00-092, V00-093, V00-094, V00-095, V00-096, V00-097, V00-098, V00-099, V00-100, V00-101, V00-102, V00-103, V00-104, V00-105, V00-106, V00-107, V00-108, V00-109, N00-01, N00-02, N00-03, N00-04, N00-05, N00-06, N00-07, N00-08, N00-09, N00-10

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/checkpoints/C00-04.md

**Các bước cụ thể:**

1. Read the linked requirement clauses and confirmed decision limits; enumerate observable positive, negative and interruption cases for this single output.
2. Produce only the named output inside the proposed whitelist after a scoped authorization; record unresolved alternatives instead of inventing contracts.
3. Capture case-by-case expected/actual evidence and reviewer result; stop on a failed invariant and update traceability without approving human gates.

**Tiêu chí nghiệm thu:**

- [ ] AT-C00-04-01: Every listed predecessor has actual accepted evidence at its recorded revision; missing, failed or NOT RUN evidence blocks this checkpoint.
- [ ] AT-C00-04-02: Record exact local revision, unresolved limitations and required user acceptance separately; this checkpoint grants no publishing or production authorization.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": null, "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

This is a planning/research/checkpoint task; any executable probe still requires scoped authorization and an established bounded command.

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [C00-05] Release review checkpoint

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

Release review evidence checkpoint

**Phụ thuộc:**

C00-04, P60-04, P60-05, C00-01, C00-02, C00-03

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/checkpoints/C00-05.md

**Các bước cụ thể:**

1. Read the linked requirement clauses and confirmed decision limits; enumerate observable positive, negative and interruption cases for this single output.
2. Produce only the named output inside the proposed whitelist after a scoped authorization; record unresolved alternatives instead of inventing contracts.
3. Capture case-by-case expected/actual evidence and reviewer result; stop on a failed invariant and update traceability without approving human gates.

**Tiêu chí nghiệm thu:**

- [ ] AT-C00-05-01: Every listed predecessor has actual accepted evidence at its recorded revision; missing, failed or NOT RUN evidence blocks this checkpoint.
- [ ] AT-C00-05-02: Record exact local revision, unresolved limitations and required user acceptance separately; this checkpoint grants no publishing or production authorization.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": null, "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

This is a planning/research/checkpoint task; any executable probe still requires scoped authorization and an established bounded command.

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.
