# P40 task cards

Generated from docs/product/AI/backlog.json. Grouping is navigation only; dependencies below determine dispatch. No phase-level edges. All future work requires separate authorization.

## [P40-01] Onboarding/tray/settings shell

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-4-hydrogen-low"}

**Vai trò:**

ui-features

**Mã yêu cầu:**

SP04, NV06

**Quyết định / rào cản:**

D-14

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Native management UI

**Phụ thuộc:**

P02-04, P50-01, B00-01, A00-14

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

src/Desktop.Wpf/OnboardingView.xaml; src/Desktop.Wpf/SettingsShell.xaml; src/Desktop.Wpf/TrayController.cs

**Các bước cụ thể:**

1. Đối chiếu SP04, NV06 với mục tiêu: Onboarding/tray/settings shell. Đọc quyết định D-14; khóa lại phạm vi đầu ra Native management UI.
2. Thực hiện lát có thể nghiệm thu riêng trong src/Desktop.Wpf/OnboardingView.xaml; src/Desktop.Wpf/SettingsShell.xaml; src/Desktop.Wpf/TrayController.cs sau khi được cho phép: Firstprofile/name/startupchoice, tray opensfullsettings, no signupgate. Nếu cần thêm file hoặc thay hợp đồng, chia lát và cập nhật whitelist trước Ready.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: Namesize/modes/monitors and stop routes accessible independentofmood. Không dùng kết quả mẫu giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap: UC-01/02 and IT-20 native UI states. Lệnh chính xác do B00-01 xác minh; lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P40-01-01: Firstprofile/name/startupchoice, tray opensfullsettings, no signupgate.
- [ ] AT-P40-01-02: Namesize/modes/monitors and stop routes accessible independentofmood.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-01", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "UC-01/02 and IT-20 native UI states."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-01

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

SP04, NV06

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [P40-02] UI grants và chosenbrowser

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-4-hydrogen-low"}

**Vai trò:**

ui-features

**Mã yêu cầu:**

QD02, XP16

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

App/site permission UI

**Phụ thuộc:**

P40-01, P10-01, B00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

src/Desktop.Wpf/PermissionsView.xaml; src/Desktop.Wpf/PermissionsViewModel.cs; tests/NativeUI/PermissionFlows.md

**Các bước cụ thể:**

1. Đối chiếu QD02, XP16 với mục tiêu: UI grants và chosenbrowser. Đọc quyết định liên quan trong DECISIONS; khóa lại phạm vi đầu ra App/site permission UI.
2. Thực hiện lát có thể nghiệm thu riêng trong src/Desktop.Wpf/PermissionsView.xaml; src/Desktop.Wpf/PermissionsViewModel.cs; tests/NativeUI/PermissionFlows.md sau khi được cho phép: Scannedapps+pastedwebsites separategrants with explanatorylabels, alloff. Nếu cần thêm file hoặc thay hợp đồng, chia lát và cập nhật whitelist trước Ready.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: Chrome/Edge selectedbrowser doesnot grantpermissions; revoke routescorrectly. Không dùng kết quả mẫu giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap: AT-QD02/XP16 native UI+policyintegration. Lệnh chính xác do B00-01 xác minh; lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P40-02-01: Scannedapps+pastedwebsites separategrants with explanatorylabels, alloff.
- [ ] AT-P40-02-02: Chrome/Edge selectedbrowser doesnot grantpermissions; revoke routescorrectly.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-01", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "AT-QD02/XP16 native UI+policyintegration."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-01

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

QD02, XP16

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [P40-03] Dạy/review/manage lesson và searchparameters

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

task-execution

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-4-hydrogen-low"}

**Vai trò:**

ui-features

**Mã yêu cầu:**

BH01, BH02, BH11, BH12

**Quyết định / rào cản:**

D-17

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Lesson definition workflow

**Phụ thuộc:**

P10-03, P40-01, P50-01, B00-06, A00-17

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

src/Host/Tasks/LessonRecorder.cs; src/Desktop.Wpf/LessonReview.xaml; tests/Integration/LessonRecordingTests.cs

**Các bước cụ thể:**

1. Đối chiếu BH01, BH02, BH11, BH12 với mục tiêu: Dạy/review/manage lesson và searchparameters. Đọc quyết định D-17; khóa lại phạm vi đầu ra Lesson definition workflow.
2. Thực hiện lát có thể nghiệm thu riêng trong src/Host/Tasks/LessonRecorder.cs; src/Desktop.Wpf/LessonReview.xaml; tests/Integration/LessonRecordingTests.cs sau khi được cho phép: Explicitrecording sameapp/site, reviewconfirm then saveversion. Nếu cần thêm file hoặc thay hợp đồng, chia lát và cập nhật whitelist trước Ready.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: Manage/reteach, searchparameters and firstresult/exactmeaning clear; illegaltyping denied. Không dùng kết quả mẫu giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap: UC-08 draft/cancel/crossscope/editcases. Lệnh chính xác do B00-06 xác minh; lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P40-03-01: Explicitrecording sameapp/site, reviewconfirm then saveversion.
- [ ] AT-P40-03-02: Manage/reteach, searchparameters and firstresult/exactmeaning clear; illegaltyping denied.
- [ ] AT-P40-03-03: AT-BH02 — D-17: Sửa/xóa bài học dừng việc đang dùng và hủy lượt chờ dùng bài học đó; người dùng giao lại, không chuyển lượt cũ sang phiên bản mới, không hủy việc không liên quan hoặc hoàn tác thao tác đã xong. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-06", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "UC-08 draft/cancel/crossscope/editcases."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-06

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

BH01, BH02, BH11, BH12

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [P40-04] Embodied execution và postconditionverify

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

task-execution

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

core

**Mã yêu cầu:**

NV10, BH03, BH04, BH05

**Quyết định / rào cản:**

D-03, D-05

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Verified step runner

**Phụ thuộc:**

P40-03, P10-07, P20-02, B00-06, A00-03, A00-05

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

src/Host/Tasks/StepRunner.cs; src/Host/Tasks/ActionAdapter.cs; tests/Integration/StepRunnerTests.cs

**Các bước cụ thể:**

1. Đối chiếu NV10, BH03, BH04, BH05 với mục tiêu: Embodied execution và postconditionverify. Đọc quyết định D-03, D-05; khóa lại phạm vi đầu ra Verified step runner.
2. Thực hiện lát có thể nghiệm thu riêng trong src/Host/Tasks/StepRunner.cs; src/Host/Tasks/ActionAdapter.cs; tests/Integration/StepRunnerTests.cs sau khi được cho phép: Approach→reobserve→finalpermit→singleaction→postcondition, targetchange stops. Nếu cần thêm file hoặc thay hợp đồng, chia lát và cập nhật whitelist trước Ready.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: Human yield60s/resume/reteach, no forbiddenwrites/forms/payments; directrequestdelayonce. Không dùng kết quả mẫu giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap: E03/IT-03/14 with fakeinput then ownedsurfaces. Lệnh chính xác do B00-06 xác minh; lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P40-04-01: Approach→reobserve→finalpermit→singleaction→postcondition, targetchange stops.
- [ ] AT-P40-04-02: Human yield60s/resume/reteach, no forbiddenwrites/forms/payments; directrequestdelayonce.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-06", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "E03/IT-03/14 with fakeinput then ownedsurfaces."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-06

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

NV10, BH03, BH04, BH05

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [P40-05] Hàng đợi, priority và stop lifecycle

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

task-execution

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

core

**Mã yêu cầu:**

BH06, BH07, BH08, BH09, BH10, SP09, BH02, CD01

**Quyết định / rào cản:**

D-02, D-10, D-17

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Queue state machine

**Phụ thuộc:**

P40-04, P30-03, B00-06, A00-02, A00-10, A00-17

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

src/Host/Tasks/QueueScheduler.cs; src/Desktop.Wpf/QueueView.xaml; tests/Integration/QueueTests.cs

**Các bước cụ thể:**

1. Đối chiếu BH06, BH07, BH08, BH09, BH10 với mục tiêu: Hàng đợi, priority và stop lifecycle. Đọc quyết định D-02, D-10, D-17; khóa lại phạm vi đầu ra Queue state machine.
2. Thực hiện lát có thể nghiệm thu riêng trong src/Host/Tasks/QueueScheduler.cs; src/Desktop.Wpf/QueueView.xaml; tests/Integration/QueueTests.cs sau khi được cho phép: Runningcancel/pendingpause/resumeexplicit/exitcancel matches matrix. Nếu cần thêm file hoặc thay hợp đồng, chia lát và cập nhật whitelist trước Ready.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: Jobfailed stopsalone, nextindependent runs; directrequest preemptsdiscovery, no doublejob. Không dùng kết quả mẫu giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap: IT-06/14 with stale/duplicate/switch/selfhidecases. Lệnh chính xác do B00-06 xác minh; lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P40-05-01: Runningcancel/pendingpause/resumeexplicit/exitcancel matches matrix.
- [ ] AT-P40-05-02: Jobfailed stopsalone, nextindependent runs; directrequest preemptsdiscovery, no doublejob.
- [ ] AT-P40-05-03: AT-SP09 — D-02: Hình ảnh lỗi thì tạm dừng thao tác lên app khác; phục hồi vẫn tạm dừng và hỏi trước tiếp tục, kiểm quyền/an toàn mới. Không phát lại mù quáng; hợp đồng kết nối/mất kết nối còn mở. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate.
- [ ] AT-P40-05-04: AT-BH02 — D-17: Sửa/xóa bài học dừng việc đang dùng và hủy lượt chờ dùng bài học đó; người dùng giao lại, không chuyển lượt cũ sang phiên bản mới, không hủy việc không liên quan hoặc hoàn tác thao tác đã xong. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate.
- [ ] AT-P40-05-05: AT-BH06 — D-02/D-10/D-17: Renderer lỗi thì tạm dừng thao tác app khác; hình ảnh phục hồi hoặc mở lại app giữ việc tạm dừng và hỏi trước tiếp tục, kiểm quyền/an toàn mới, không phát lại mù quáng. Sửa/xóa bài học dừng việc đang dùng và hủy lượt chờ dùng bài học đó, phải giao lại; không hủy việc không liên quan hoặc hoàn tác việc đã xong. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate.
- [ ] AT-P40-05-06: AT-CD01 — D-10: Mở lại app giữ việc đang dở tạm dừng, hỏi trước tiếp tục; không tự chạy lại, vẫn kiểm quyền/an toàn hiện hành. Crash ghi dữ liệu/cập nhật còn cần khảo sát. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-06", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "IT-06/14 with stale/duplicate/switch/selfhidecases."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-06

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

SP09, BH02, BH06, BH07, BH08, BH09, BH10, CD01

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [P40-06] Xem cùng và phản ứng cảm xúc

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-4-hydrogen-low"}

**Vai trò:**

ui-features

**Mã yêu cầu:**

XP01, XP04

**Quyết định / rào cản:**

D-04, D-12

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Attended media response

**Phụ thuộc:**

P03-03, P10-03, P30-02, P20-04, B00-01, A00-04, A00-12

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

src/Host/Companion/MediaAttention.cs; src/Host/Companion/AffectSmoother.cs; tests/Integration/MediaReactionTests.cs

**Các bước cụ thể:**

1. Đối chiếu XP01, XP04 với mục tiêu: Xem cùng và phản ứng cảm xúc. Đọc quyết định D-04, D-12; khóa lại phạm vi đầu ra Attended media response.
2. Thực hiện lát có thể nghiệm thu riêng trong src/Host/Companion/MediaAttention.cs; src/Host/Companion/AffectSmoother.cs; tests/Integration/MediaReactionTests.cs sau khi được cho phép: Safeobservations drive smoothaffect, silentreactions; hard/uncaptured nofakeunderstanding. Nếu cần thêm file hoặc thay hợp đồng, chia lát và cập nhật whitelist trước Ready.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: Usermovie not interrupted, nextended target rechecked; no subtitleautoavoid requirement. Không dùng kết quả mẫu giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap: IT-09/10 with bothcontenttypes Vietsubs. Lệnh chính xác do B00-01 xác minh; lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P40-06-01: Safeobservations drive smoothaffect, silentreactions; hard/uncaptured nofakeunderstanding.
- [ ] AT-P40-06-02: Usermovie not interrupted, nextended target rechecked; no subtitleautoavoid requirement.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-01", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "IT-09/10 with bothcontenttypes Vietsubs."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-01

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

XP01, XP04

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [P40-07] Tự tìm/mở nội dung trong quyền

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

task-execution

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

core

**Mã yêu cầu:**

XP15, XP05, XP06, XP07, XP08, AI01

**Quyết định / rào cản:**

D-06, D-11, D-16

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Bounded autonomous media

**Phụ thuộc:**

P40-05, P40-06, P10-06, B00-06, A00-06, A00-11, A00-16

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

src/Host/Tasks/AutonomousMedia.cs; src/BrowserBridge/MediaStatus.cs; tests/Integration/AutonomousMediaTests.cs

**Các bước cụ thể:**

1. Đối chiếu XP15, XP05, XP06, XP07 với mục tiêu: Tự tìm/mở nội dung trong quyền. Đọc quyết định D-06, D-11, D-16; khóa lại phạm vi đầu ra Bounded autonomous media.
2. Thực hiện lát có thể nghiệm thu riêng trong src/Host/Tasks/AutonomousMedia.cs; src/BrowserBridge/MediaStatus.cs; tests/Integration/AutonomousMediaTests.cs sau khi được cho phép: Advancedidle5m+unlocked+nomedia, owntab/chosenbrowser, preserveusertabs/playback. Nếu cần thêm file hoặc thay hợp đồng, chia lát và cập nhật whitelist trước Ready.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: Skiplogin/pay/verify max3; uncertainadkeep; allowedframe scoped. Không dùng kết quả mẫu giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap: UC-11 IT-09 with redirects/autoplay/returninput. Lệnh chính xác do B00-06 xác minh; lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P40-07-01: Advancedidle5m+unlocked+nomedia, owntab/chosenbrowser, preserveusertabs/playback.
- [ ] AT-P40-07-02: Skiplogin/pay/verify max3; uncertainadkeep; allowedframe scoped.
- [ ] AT-P40-07-03: AT-XP05 — D-16: Được kiểm trạng thái đang phát/không phát ở nền tối thiểu để tránh mở chồng; không đọc tên/nội dung hoặc suy gu. Lỗi/không xác định không coi là không phát; API/độ tin cậy cần kiểm chứng. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate.
- [ ] AT-P40-07-04: AT-XP07 — D-06: Sau 3 nội dung không mở được về sinh hoạt; chờ người dùng thao tác trở lại rồi chỉ tìm trong đợt vắng mặt tiếp theo. Không tìm lặp cùng đợt hoặc chỉ dùng bộ đếm để mở lại tìm kiếm; quyền/chờ/không gián đoạn vẫn áp dụng. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate.
- [ ] AT-P40-07-05: AT-XP08 — D-11: Máy ngủ không cộng thời gian chờ mở phim/nhạc; máy thức tiếp tục phần còn lại, không reset chỉ vì thức. Giữ quyền/khóa/input/phát đã chốt, máy ngủ khác nhân vật ngủ. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate.
- [ ] AT-P40-07-06: AT-AI01 — D-16: Chỉ kiểm tra trạng thái đang phát/không phát ở nền để tránh mở chồng; không tên bài/phim/hình/âm thanh/lịch sử hoặc suy gu; lỗi/không rõ không coi là không phát. Cách lấy/độ tin cậy cần kiểm chứng. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-06", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "UC-11 IT-09 with redirects/autoplay/returninput."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-06

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

XP15, XP05, XP05, XP06, XP07, XP08, AI01

**Mã phi chức năng:**

See linked requirement / prerequisite scope.
