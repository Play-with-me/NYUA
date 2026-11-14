# P50 task cards

Generated from docs/product/AI/backlog.json. Grouping is navigation only; dependencies below determine dispatch. No phase-level edges. All future work requires separate authorization.

## [P50-01] Chốt storage và transaction/persistence

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

distribution

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

core

**Mã yêu cầu:**

CD01

**Quyết định / rào cản:**

D-07, D-08, D-10

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Versioned local storage

**Phụ thuộc:**

P00-02, P00-04, B00-07, A00-07, A00-08, A00-10

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

src/Host/Storage/ProfileRepository.cs; src/Host/Storage/SchemaVersion.cs; tests/Integration/StorageTests.cs

**Các bước cụ thể:**

1. Đối chiếu SP09 và phạm vi enabler với mục tiêu: Chốt storage và transaction/persistence. Đọc quyết định D-07, D-08, D-10; khóa lại phạm vi đầu ra Versioned local storage.
2. Thực hiện lát có thể nghiệm thu riêng trong src/Host/Storage/ProfileRepository.cs; src/Host/Storage/SchemaVersion.cs; tests/Integration/StorageTests.cs sau khi được cho phép: Logicalentity/provenance ownership và state commit transactional, no hiddenbackup. Nếu cần thêm file hoặc thay hợp đồng, chia lát và cập nhật whitelist trước Ready.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: Corrupt/interruptedwrite handling preservesexisting or reportsfailure; no fake recovery. Không dùng kết quả mẫu giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap: DATA review + durabilityfixtures, licensecheck of engine. Lệnh chính xác do B00-07 xác minh; lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P50-01-01: Logicalentity/provenance ownership và state commit transactional, no hiddenbackup.
- [ ] AT-P50-01-02: Corrupt/interruptedwrite handling preservesexisting or reportsfailure; no fake recovery.
- [ ] AT-P50-01-03: AT-CD01 — D-10: Mở lại app giữ việc đang dở tạm dừng, hỏi trước tiếp tục; không tự chạy lại, vẫn kiểm quyền/an toàn hiện hành. Crash ghi dữ liệu/cập nhật còn cần khảo sát. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-07", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "DATA review + durabilityfixtures, licensecheck of engine."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-07

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

CD01

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [P50-02] Profile import/switch/reset semantics

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

distribution

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

core

**Mã yêu cầu:**

QD03, HS01, HS02, HS03

**Quyết định / rào cản:**

D-10

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Profile lifecycle

**Phụ thuộc:**

P50-01, P10-01, B00-07, A00-10

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

src/Host/Storage/ProfileLifecycle.cs; src/Desktop.Wpf/ProfilesView.xaml; tests/Integration/ProfileLifecycleTests.cs

**Các bước cụ thể:**

1. Đối chiếu QD03, HS01, HS02, HS03 với mục tiêu: Profile import/switch/reset semantics. Đọc quyết định D-10; khóa lại phạm vi đầu ra Profile lifecycle.
2. Thực hiện lát có thể nghiệm thu riêng trong src/Host/Storage/ProfileLifecycle.cs; src/Desktop.Wpf/ProfilesView.xaml; tests/Integration/ProfileLifecycleTests.cs sau khi được cho phép: Onlyimportadds, exactlyoneactive, inactiveallfreeze and sharedmachinegrants. Nếu cần thêm file hoặc thay hợp đồng, chia lát và cập nhật whitelist trước Ready.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: Resetcurrent clearsstate/memory/relation/lessons, preserveothers; switch cancelsunfinished. Không dùng kết quả mẫu giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap: UC-16 IT-12/15 collision/loadfailure cases. Lệnh chính xác do B00-07 xác minh; lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P50-02-01: Onlyimportadds, exactlyoneactive, inactiveallfreeze and sharedmachinegrants.
- [ ] AT-P50-02-02: Resetcurrent clearsstate/memory/relation/lessons, preserveothers; switch cancelsunfinished.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-07", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "UC-16 IT-12/15 collision/loadfailure cases."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-07

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

QD03, HS01, HS02, HS03

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [P50-03] Manualexport password/recovery format

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

distribution

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

core

**Mã yêu cầu:**

SL01, SL02

**Quyết định / rào cản:**

D-07, D-09

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Reviewed encrypted archive export

**Phụ thuộc:**

P50-01, P00-04, B00-07, A00-07, A00-09

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

src/Host/Storage/ProfileExporter.cs; src/Desktop.Wpf/ExportView.xaml; tests/Integration/ExportTests.cs

**Các bước cụ thể:**

1. Đối chiếu SL01, SL02 với mục tiêu: Manualexport password/recovery format. Đọc quyết định D-07, D-09; khóa lại phạm vi đầu ra Reviewed encrypted archive export.
2. Thực hiện lát có thể nghiệm thu riêng trong src/Host/Storage/ProfileExporter.cs; src/Desktop.Wpf/ExportView.xaml; tests/Integration/ExportTests.cs sau khi được cho phép: Requiredpassword/recovery separate, auditedprimitive and boundedformat. Nếu cần thêm file hoặc thay hợp đồng, chia lát và cập nhật whitelist trước Ready.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: Whitelist excludesgrants/keys/rawsources/queue; no autoarchives. Không dùng kết quả mẫu giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap: SL01/02 IT-15 ciphertext/credential/exportscope tests. Lệnh chính xác do B00-07 xác minh; lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P50-03-01: Requiredpassword/recovery separate, auditedprimitive and boundedformat.
- [ ] AT-P50-03-02: Whitelist excludesgrants/keys/rawsources/queue; no autoarchives.
- [ ] AT-P50-03-03: AT-SL01 — D-09: Sao lưu không kèm gói AI nâng cao; máy mới tải lại khi cần, không thêm tùy chọn kèm gói mỗi lần xuất. Giữ dữ liệu nhân vật/ký ức/thiết lập thuộc phạm vi; quyền máy/khóa AI ngoài không mang sang. Whitelist/tài nguyên khác/tương thích còn phải đặc tả. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-07", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "SL01/02 IT-15 ciphertext/credential/exportscope tests."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-07

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

SL01, SL02

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [P50-04] Validate/import archive thành hồ sơ riêng

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

distribution

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

core

**Mã yêu cầu:**

Enabler; linked predecessors define bounded output.

**Quyết định / rào cản:**

D-07, D-09

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Transactional import

**Phụ thuộc:**

P50-03, P50-02, B00-07, A00-07, A00-09

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

src/Host/Storage/ProfileImporter.cs; src/Desktop.Wpf/ImportView.xaml; tests/Integration/ImportTests.cs

**Các bước cụ thể:**

1. Đối chiếu SP09 và phạm vi enabler với mục tiêu: Validate/import archive thành hồ sơ riêng. Đọc quyết định D-07, D-09; khóa lại phạm vi đầu ra Transactional import.
2. Thực hiện lát có thể nghiệm thu riêng trong src/Host/Storage/ProfileImporter.cs; src/Desktop.Wpf/ImportView.xaml; tests/Integration/ImportTests.cs sau khi được cho phép: Wrongpassword/code/corrupt/pathtraversal/unknownschema boundedreject. Nếu cần thêm file hoặc thay hợp đồng, chia lát và cập nhật whitelist trước Ready.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: Successnewprofile no merge/foreigngrants, existingdata preserved onfailure. Không dùng kết quả mẫu giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap: IT-15 maliciousarchive/partialwrite/collision cases. Lệnh chính xác do B00-07 xác minh; lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P50-04-01: Wrongpassword/code/corrupt/pathtraversal/unknownschema boundedreject.
- [ ] AT-P50-04-02: Successnewprofile no merge/foreigngrants, existingdata preserved onfailure.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-07", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "IT-15 maliciousarchive/partialwrite/collision cases."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-07

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [P50-05] Local actionhistory và expiry30days

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

distribution

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

core

**Mã yêu cầu:**

BH13

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Sanitized history pipeline

**Phụ thuộc:**

P50-01, B00-07

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

src/Host/Storage/ActionHistory.cs; src/Desktop.Wpf/HistoryView.xaml; tests/Integration/HistoryTests.cs

**Các bước cụ thể:**

1. Đối chiếu BH13 với mục tiêu: Local actionhistory và expiry30days. Đọc quyết định liên quan trong DECISIONS; khóa lại phạm vi đầu ra Sanitized history pipeline.
2. Thực hiện lát có thể nghiệm thu riêng trong src/Host/Storage/ActionHistory.cs; src/Desktop.Wpf/HistoryView.xaml; tests/Integration/HistoryTests.cs sau khi được cho phép: Time/source/action/outcome only, no raw/privatepayload/screenshots; no telemetry. Nếu cần thêm file hoặc thay hợp đồng, chia lát và cập nhật whitelist trước Ready.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: Userdelete and30days expiry actual, history separatememory. Không dùng kết quả mẫu giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap: IT-17 errorpaths/clockedge/retentionfixtures. Lệnh chính xác do B00-07 xác minh; lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P50-05-01: Time/source/action/outcome only, no raw/privatepayload/screenshots; no telemetry.
- [ ] AT-P50-05-02: Userdelete and30days expiry actual, history separatememory.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-07", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "IT-17 errorpaths/clockedge/retentionfixtures."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-07

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

BH13

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [P50-06] Bộ cài và startup opt-in

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

distribution

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

core

**Mã yêu cầu:**

SP03, CD01

**Quyết định / rào cản:**

D-13

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Native install package

**Phụ thuộc:**

P00-04, P40-01, P20-05, B00-07, A00-13

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

packaging/README.md; packaging/installer-project; tests/NativeUI/InstallFlows.md

**Các bước cụ thể:**

1. Đối chiếu CD01 với mục tiêu: Bộ cài và startup opt-in. Đọc quyết định D-13; khóa lại phạm vi đầu ra Native install package.
2. Thực hiện lát có thể nghiệm thu riêng trong packaging/README.md; packaging/installer-project; tests/NativeUI/InstallFlows.md sau khi được cho phép: Actualcompatible host/renderer/runtime components pinned and installtested. Nếu cần thêm file hoặc thay hợp đồng, chia lát và cập nhật whitelist trước Ready.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: Startup userchoice, basic works without optionalAIpack/extension/account. Không dùng kết quả mẫu giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap: IT-16 cleanWindowsinstall/startup flows. Lệnh chính xác do B00-07 xác minh; lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P50-06-01: Actualcompatible host/renderer/runtime components pinned and installtested.
- [ ] AT-P50-06-02: Startup userchoice, basic works without optionalAIpack/extension/account.
- [ ] AT-P50-06-03: AT-CD01 — D-10: Mở lại app giữ việc đang dở tạm dừng, hỏi trước tiếp tục; không tự chạy lại, vẫn kiểm quyền/an toàn hiện hành. Crash ghi dữ liệu/cập nhật còn cần khảo sát. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-07", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "IT-16 cleanWindowsinstall/startup flows."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-07

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

SP03, CD01

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [P50-07] Own update check/download/install confirmation

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

distribution

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

core

**Mã yêu cầu:**

CD02

**Quyết định / rào cản:**

D-10, D-13

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Authenticated update flow

**Phụ thuộc:**

P50-06, P50-04, B00-07, A00-10, A00-13

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

src/Host/Distribution/UpdateController.cs; src/Desktop.Wpf/UpdateView.xaml; tests/Integration/UpdateTests.cs

**Các bước cụ thể:**

1. Đối chiếu CD02 với mục tiêu: Own update check/download/install confirmation. Đọc quyết định D-10, D-13; khóa lại phạm vi đầu ra Authenticated update flow.
2. Thực hiện lát có thể nghiệm thu riêng trong src/Host/Distribution/UpdateController.cs; src/Desktop.Wpf/UpdateView.xaml; tests/Integration/UpdateTests.cs sau khi được cho phép: Ownupdatesource/download verified, userconfirm before install/restart. Nếu cần thêm file hoặc thay hợp đồng, chia lát và cập nhật whitelist trước Ready.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: Invalidsignature/migration stops, no otherappupdate or auto backup; rollback compatibility explicit. Không dùng kết quả mẫu giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap: IT-16 declining/corrupt/migrationfailure scenarios. Lệnh chính xác do B00-07 xác minh; lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P50-07-01: Ownupdatesource/download verified, userconfirm before install/restart.
- [ ] AT-P50-07-02: Invalidsignature/migration stops, no otherappupdate or auto backup; rollback compatibility explicit.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-07", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "IT-16 declining/corrupt/migrationfailure scenarios."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-07

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

CD02

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [P50-08] Uninstall giữ/xóa và manualexport reminder

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

distribution

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

core

**Mã yêu cầu:**

CD03

**Quyết định / rào cản:**

D-13

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Uninstall data workflow

**Phụ thuộc:**

P50-06, P50-03, B00-07, A00-13

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

packaging/uninstall-workflow; tests/NativeUI/UninstallFlows.md; docs/help/uninstall.md

**Các bước cụ thể:**

1. Đối chiếu CD03 với mục tiêu: Uninstall giữ/xóa và manualexport reminder. Đọc quyết định D-13; khóa lại phạm vi đầu ra Uninstall data workflow.
2. Thực hiện lát có thể nghiệm thu riêng trong packaging/uninstall-workflow; tests/NativeUI/UninstallFlows.md; docs/help/uninstall.md sau khi được cho phép: Explicitretain/deleteappdata, remindmanualexport, jobswarncancel. Nếu cần thêm file hoặc thay hợp đồng, chia lát và cập nhật whitelist trước Ready.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: No search/delete manuallyexported archives outsideowneddata. Không dùng kết quả mẫu giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap: IT-16 retain/reinstall/delete scenarios withfakedata. Lệnh chính xác do B00-07 xác minh; lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P50-08-01: Explicitretain/deleteappdata, remindmanualexport, jobswarncancel.
- [ ] AT-P50-08-02: No search/delete manuallyexported archives outsideowneddata.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-07", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "IT-16 retain/reinstall/delete scenarios withfakedata."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-07

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

CD03

**Mã phi chức năng:**

See linked requirement / prerequisite scope.
