# P60 task cards

Generated from docs/product/AI/backlog.json. Grouping is navigation only; dependencies below determine dispatch. No phase-level edges. All future work requires separate authorization.

## [P60-01] Lát tích hợp đầu: hiện→đọc an toàn→phản ứng→dừng

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

D-01, D-15

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

One complete product path

**Phụ thuộc:**

P40-01, P20-02, P30-02, P10-03, B00-01, A00-01, A00-15

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

tests/Integration/FirstSliceTests.cs; docs/acceptance/first-slice.md

**Các bước cụ thể:**

1. Đối chiếu SP02 với mục tiêu: Lát tích hợp đầu: hiện→đọc an toàn→phản ứng→dừng. Đọc quyết định D-01, D-15; khóa lại phạm vi đầu ra One complete product path.
2. Thực hiện lát có thể nghiệm thu riêng trong tests/Integration/FirstSliceTests.cs; docs/acceptance/first-slice.md sau khi được cho phép: Không dùng cannedlabel thay realperception; life/render/grants cùng chạy. Nếu cần thêm file hoặc thay hợp đồng, chia lát và cập nhật whitelist trước Ready.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: Stop/revoke actualconsumers, E02afakeproof không được promote. Không dùng kết quả mẫu giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap: SP02 walkthrough + end-to-end sentinelcapture. Lệnh chính xác do B00-01 xác minh; lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P60-01-01: Không dùng cannedlabel thay realperception; life/render/grants cùng chạy.
- [ ] AT-P60-01-02: Stop/revoke actualconsumers, E02afakeproof không được promote.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-01", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "SP02 walkthrough + end-to-end sentinelcapture."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-01

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

SP02

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [P60-02] Hồi quy hai mức và toàn bộ nghiệp vụ

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

MODE01, MODE02, MODE03, MODE04, MODE05, MODE06, MODE07, MODE08, MODE09

**Quyết định / rào cản:**

D-04

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Full RTM evidence

**Phụ thuộc:**

P60-01, P30-06, P40-07, P50-04, P50-05, B00-01, A00-04

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

tests/acceptance/manifest.json; docs/acceptance/rtm-evidence.csv; docs/acceptance/regression.md

**Các bước cụ thể:**

1. Đối chiếu MODE01, MODE02, MODE03, MODE04, MODE05, MODE06, MODE07, MODE08, MODE09 với mục tiêu: Hồi quy hai mức và toàn bộ nghiệp vụ. Đọc quyết định D-04; khóa lại phạm vi đầu ra Full RTM evidence.
2. Thực hiện lát có thể nghiệm thu riêng trong tests/acceptance/manifest.json; docs/acceptance/rtm-evidence.csv; docs/acceptance/regression.md sau khi được cho phép: Allscope requirements mapped to test/results, deferredseparate; modefeatures correct. Nếu cần thêm file hoặc thay hợp đồng, chia lát và cập nhật whitelist trước Ready.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: Negativepaths/keyboard/DPI/privacy/state tested, no skippedcriteria. Không dùng kết quả mẫu giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap: QA IT-01..20 and AT registry; native runtime. Lệnh chính xác do B00-01 xác minh; lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P60-02-01: Allscope requirements mapped to test/results, deferredseparate; modefeatures correct.
- [ ] AT-P60-02-02: Negativepaths/keyboard/DPI/privacy/state tested, no skippedcriteria.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-01", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "QA IT-01..20 and AT registry; native runtime."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-01

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

MODE01, MODE02, MODE03, MODE04, MODE05, MODE06, MODE07, MODE08, MODE09

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [P60-03] Phiên8h/offline và ma trận cấu hình

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

D-04

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Real8h soak report

**Phụ thuộc:**

P60-02, P03-04, B00-01, A00-04

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

tools/bench/SoakObserver.cs; docs/acceptance/soak.md; docs/acceptance/hardware-matrix.csv

**Các bước cụ thể:**

1. Đối chiếu SP05 với mục tiêu: Phiên8h/offline và ma trận cấu hình. Đọc quyết định D-04; khóa lại phạm vi đầu ra Real8h soak report.
2. Thực hiện lát có thể nghiệm thu riêng trong tools/bench/SoakObserver.cs; docs/acceptance/soak.md; docs/acceptance/hardware-matrix.csv sau khi được cho phép: Frozen8h schedule, measuredresource/faults on definedmachines. Nếu cần thêm file hoặc thay hợp đồng, chia lát và cập nhật whitelist trước Ready.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: Offlineworks afterinstall, no unapprovedautodowngrade/cloud; actual8h notsimclock. Không dùng kết quả mẫu giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap: E05/IT-11/19 logs/profiles/rendering observations. Lệnh chính xác do B00-01 xác minh; lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P60-03-01: Frozen8h schedule, measuredresource/faults on definedmachines.
- [ ] AT-P60-03-02: Offlineworks afterinstall, no unapprovedautodowngrade/cloud; actual8h notsimclock.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-01", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "E05/IT-11/19 logs/profiles/rendering observations."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-01

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

SP05

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [P60-04] Rà độc lập, thương hiệu và release gate

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

distribution

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

finalreview

**Mã yêu cầu:**

Enabler; linked predecessors define bounded output.

**Quyết định / rào cản:**

D-13

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Release readiness packet

**Phụ thuộc:**

P60-03, P50-07, P50-08, P00-04, B00-07, A00-13, P03-01, C00-04

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/release/readiness.md; docs/licenses/INVENTORY.md; docs/release/limitations.md

**Các bước cụ thể:**

1. Đối chiếu SP03 với mục tiêu: Rà độc lập, thương hiệu và release gate. Đọc quyết định D-13; khóa lại phạm vi đầu ra Release readiness packet.
2. Thực hiện lát có thể nghiệm thu riêng trong docs/release/readiness.md; docs/licenses/INVENTORY.md; docs/release/limitations.md sau khi được cho phép: Bothmodesstable, security/data/license/name issues resolved or explicitapprovedscope. Nếu cần thêm file hoặc thay hợp đồng, chia lát và cập nhật whitelist trước Ready.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: Actualreviewer/owner recorded; no pretendingAIselfreview independent. Không dùng kết quả mẫu giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap: RELEASE checklist, independentreview findings and closure. Lệnh chính xác do B00-07 xác minh; lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P60-04-01: Bothmodesstable, security/data/license/name issues resolved or explicitapprovedscope.
- [ ] AT-P60-04-02: Actualreviewer/owner recorded; no pretendingAIselfreview independent.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-07", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "RELEASE checklist, independentreview findings and closure."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-07

**Gate nghiệm thu người dùng:**

{"required": true, "status": "NOT_OBTAINED", "evidence": null, "condition": "Actual user response on the exact reviewed artifact/revision is mandatory; automated or AI review cannot satisfy this gate."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [P60-05] Chuẩn bị công bố và hỗ trợ có kiểm soát

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

distribution

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

qa

**Mã yêu cầu:**

Enabler; linked predecessors define bounded output.

**Quyết định / rào cản:**

D-13

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

User-facing release/runbook

**Phụ thuộc:**

P60-04, B00-07, A00-13

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/help/start.md; docs/release/runbook.md; docs/release/changelog.md

**Các bước cụ thể:**

1. Đối chiếu SP09 và phạm vi enabler với mục tiêu: Chuẩn bị công bố và hỗ trợ có kiểm soát. Đọc quyết định D-13; khóa lại phạm vi đầu ra User-facing release/runbook.
2. Thực hiện lát có thể nghiệm thu riêng trong docs/help/start.md; docs/release/runbook.md; docs/release/changelog.md sau khi được cho phép: User approves actualpublicartifact/costs/communication, notjustplan. Nếu cần thêm file hoặc thay hợp đồng, chia lát và cập nhật whitelist trước Ready.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: Vietnamesehelp/privacy/AIcosts/localhistory/support/redactedbugtemplate ready. Không dùng kết quả mẫu giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap: Install smoke onexactartifact and rollbackrunbookdryrun. Lệnh chính xác do B00-07 xác minh; lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P60-05-01: User approves actualpublicartifact/costs/communication, notjustplan.
- [ ] AT-P60-05-02: Vietnamesehelp/privacy/AIcosts/localhistory/support/redactedbugtemplate ready.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-07", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "Install smoke onexactartifact and rollbackrunbookdryrun."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-07

**Gate nghiệm thu người dùng:**

{"required": true, "status": "NOT_OBTAINED", "evidence": null, "condition": "Actual user response on the exact reviewed artifact/revision is mandatory; automated or AI review cannot satisfy this gate."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.
