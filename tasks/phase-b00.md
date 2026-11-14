# B00 task cards

Generated from docs/product/AI/backlog.json. Grouping is navigation only; dependencies below determine dispatch. No phase-level edges. All future work requires separate authorization.

## [B00-01] Bootstrap verified tooling and fixtures: companion

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

Bộ chạy kiểm tra và dữ liệu giả tối thiểu cho companion; phiên bản/giấy phép và lệnh có bằng chứng

**Phụ thuộc:**

P00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/experiments/bootstrap-companion.md; tests/bootstrap/companion/Bootstrap.Tests.csproj; tests/bootstrap/companion/BootstrapTests.cs; tools/verify/companion.ps1

**Các bước cụ thể:**

1. Khảo sát công cụ thực có cho companion: Get-Command dotnet, python; ghi phiên bản bằng dotnet --info / python --version nếu tìm thấy. Đây là kiểm tra môi trường, không phải test sản phẩm.
2. Sau khi được cho phép riêng, chọn công cụ phù hợp đã xác minh giấy phép; tạo duy nhất fixture/project và tools/verify/companion.ps1 trong whitelist. Renderer phải chọn phiên bản Unity qua D-01; không mặc định MSTest kiểm được Unity.
3. Thiết lập script có timeout hữu hạn, không tải dữ liệu thật, giữ exit code; thêm fixture dương và fixture âm cố ý sai. Với C# dùng dotnet test <project-thực-tế> --configuration Release --no-restore sau bước restore có kiểm soát; renderer ghi đúng lệnh batch của phiên bản Unity đã chọn.
4. Chạy powershell -NoProfile -File tools/verify/companion.ps1 cho fixture dương; bật chế độ âm đã ghi trong script và kiểm exit khác 0. Lưu lệnh, version, seed, timeout, cleanup và kết quả trong docs/experiments/bootstrap-companion.md; chỉ sau đó mở gate cho task phụ thuộc.

**Tiêu chí nghiệm thu:**

- [ ] AT-B00-01-01: Record exact executable/version, license and bounded build/test invocation for companion; run one passing fixture and one deliberately failing fixture, retain exit codes and explain unsupported environment.
- [ ] AT-B00-01-02: Document fixture rights, no personal data, explicit cleanup/stop plan, actual/proposed file map and recovery checkpoint; obtain scoped approval before creating product infrastructure.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": null, "command": null, "gate": "Bootstrap entry requires only separately approved fixture scope, tooling/license discovery and no unresolved infrastructure choice. It does not require a pre-existing successful runner. Completion requires creating and executing the bounded positive/negative runner in this whitelist."}

**Chủ nhiệm chuẩn bị công cụ:**

This is a planning/research/checkpoint task; any executable probe still requires scoped authorization and an established bounded command.

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [B00-02] Bootstrap verified tooling and fixtures: desktop-body

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

desktop-body

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

Unity fixture bootstrap cô lập và lệnh batch có timeout; không phụ thuộc project renderer sản phẩm

**Phụ thuộc:**

P00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/experiments/bootstrap-desktop-body.md; tests/bootstrap/desktop-body/UnityFixture/ProjectSettings/ProjectVersion.txt; tests/bootstrap/desktop-body/UnityFixture/Packages/manifest.json; tests/bootstrap/desktop-body/UnityFixture/Assets/Editor/BootstrapBuild.cs; tests/bootstrap/desktop-body/UnityFixture/Assets/Bootstrap.unity

**Các bước cụ thể:**

1. Khảo sát Unity Editor thực có và nguồn chính thức/giấy phép cho Windows batch build; đề xuất phiên bản trong báo cáo. Chỉ sau cho phép thử riêng mới tạo project fixture cô lập, không dùng project sản phẩm P02-01.
2. Tạo đúng năm đường dẫn whitelist: báo cáo; ProjectVersion.txt ghim editor; manifest.json chỉ package tối thiểu có quyền dùng; scene Bootstrap.unity chỉ primitive giả; BootstrapBuild.cs là editor-only entry cho phép thử. Không avatar/input/capture/network hay nội dung cá nhân. Library/Temp/log/build output là working material tự sinh, không authored file whitelist và không commit.
3. Đề xuất entry BootstrapBuild.Verify và nhánh deliberately-failing trong editor script sau khi đối chiếu API của phiên bản đã ghim. Entry dương kiểm scene fixture/build smoke thật, âm trả exit code khác 0 có chủ đích; log/outputs vào TEMP. Không cần project hay bằng chứng P02-01 để bootstrap chạy.
4. Ghi executable Unity thực, dùng mẫu batch -batchmode -nographics -quit -projectPath tests/bootstrap/desktop-body/UnityFixture -executeMethod BootstrapBuild.Verify -logFile <TEMP>. Dùng supervisor tiến trình với WaitForExit(120000), kill tiến trình thử nếu timeout; timeout là lỗi. Chạy nhánh dương/âm và lưu lệnh exact, code, log, editor/package version và cleanup. Chưa chạy trong phiên tài liệu; chỉ sau bằng chứng này P02-01 mới có runner để Ready.

**Tiêu chí nghiệm thu:**

- [ ] AT-B00-02-01: Project Unity fixture tối thiểu nằm đúng whitelist năm file; editor/package ghim phiên bản có license evidence, scene giả không quyền input/capture/network; không đọc hoặc yêu cầu project P02-01 để tạo fixture.
- [ ] AT-B00-02-02: Batch dương chạy đúng scene/build fixture, trả 0; nhánh âm cố ý sai trả khác 0; supervisor dừng sau tối đa 120 giây mỗi lượt. Báo cáo giữ exact executable/arguments/log/version/cleanup và NOT RUN cho đến khi có phép thử thực; không coi đọc file là test.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": null, "command": null, "command_template": "<verified Unity Editor executable> -batchmode -nographics -quit -projectPath tests/bootstrap/desktop-body/UnityFixture -executeMethod BootstrapBuild.Verify -logFile <TEMP log>; supervisor WaitForExit(120000), timeout -> terminate owned probe and fail", "gate": "Bootstrap entry requires separately approved fixture scope and editor/license discovery; it does not require a pre-existing successful runner or the P02-01 product project. This task owns all five fixture paths. Completion requires real bounded positive/negative batch evidence before dependent executable tasks become Ready."}

**Chủ nhiệm chuẩn bị công cụ:**

This is a planning/research/checkpoint task; any executable probe still requires scoped authorization and an established bounded command.

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [B00-03] Bootstrap verified tooling and fixtures: perception

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

perception

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

Bộ chạy kiểm tra và dữ liệu giả tối thiểu cho perception; phiên bản/giấy phép và lệnh có bằng chứng

**Phụ thuộc:**

P00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/experiments/bootstrap-perception.md; tests/bootstrap/perception/Bootstrap.Tests.csproj; tests/bootstrap/perception/BootstrapTests.cs; tools/verify/perception.ps1

**Các bước cụ thể:**

1. Khảo sát công cụ thực có cho perception: Get-Command dotnet, python; ghi phiên bản bằng dotnet --info / python --version nếu tìm thấy. Đây là kiểm tra môi trường, không phải test sản phẩm.
2. Sau khi được cho phép riêng, chọn công cụ phù hợp đã xác minh giấy phép; tạo duy nhất fixture/project và tools/verify/perception.ps1 trong whitelist. Renderer phải chọn phiên bản Unity qua D-01; không mặc định MSTest kiểm được Unity.
3. Thiết lập script có timeout hữu hạn, không tải dữ liệu thật, giữ exit code; thêm fixture dương và fixture âm cố ý sai. Với C# dùng dotnet test <project-thực-tế> --configuration Release --no-restore sau bước restore có kiểm soát; renderer ghi đúng lệnh batch của phiên bản Unity đã chọn.
4. Chạy powershell -NoProfile -File tools/verify/perception.ps1 cho fixture dương; bật chế độ âm đã ghi trong script và kiểm exit khác 0. Lưu lệnh, version, seed, timeout, cleanup và kết quả trong docs/experiments/bootstrap-perception.md; chỉ sau đó mở gate cho task phụ thuộc.

**Tiêu chí nghiệm thu:**

- [ ] AT-B00-03-01: Record exact executable/version, license and bounded build/test invocation for perception; run one passing fixture and one deliberately failing fixture, retain exit codes and explain unsupported environment.
- [ ] AT-B00-03-02: Document fixture rights, no personal data, explicit cleanup/stop plan, actual/proposed file map and recovery checkpoint; obtain scoped approval before creating product infrastructure.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": null, "command": null, "gate": "Bootstrap entry requires only separately approved fixture scope, tooling/license discovery and no unresolved infrastructure choice. It does not require a pre-existing successful runner. Completion requires creating and executing the bounded positive/negative runner in this whitelist."}

**Chủ nhiệm chuẩn bị công cụ:**

This is a planning/research/checkpoint task; any executable probe still requires scoped authorization and an established bounded command.

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [B00-04] Bootstrap verified tooling and fixtures: policy

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

policy

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

Bộ chạy kiểm tra và dữ liệu giả tối thiểu cho policy; phiên bản/giấy phép và lệnh có bằng chứng

**Phụ thuộc:**

P00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/experiments/bootstrap-policy.md; tests/bootstrap/policy/Bootstrap.Tests.csproj; tests/bootstrap/policy/BootstrapTests.cs; tools/verify/policy.ps1

**Các bước cụ thể:**

1. Khảo sát công cụ thực có cho policy: Get-Command dotnet, python; ghi phiên bản bằng dotnet --info / python --version nếu tìm thấy. Đây là kiểm tra môi trường, không phải test sản phẩm.
2. Sau khi được cho phép riêng, chọn công cụ phù hợp đã xác minh giấy phép; tạo duy nhất fixture/project và tools/verify/policy.ps1 trong whitelist. Renderer phải chọn phiên bản Unity qua D-01; không mặc định MSTest kiểm được Unity.
3. Thiết lập script có timeout hữu hạn, không tải dữ liệu thật, giữ exit code; thêm fixture dương và fixture âm cố ý sai. Với C# dùng dotnet test <project-thực-tế> --configuration Release --no-restore sau bước restore có kiểm soát; renderer ghi đúng lệnh batch của phiên bản Unity đã chọn.
4. Chạy powershell -NoProfile -File tools/verify/policy.ps1 cho fixture dương; bật chế độ âm đã ghi trong script và kiểm exit khác 0. Lưu lệnh, version, seed, timeout, cleanup và kết quả trong docs/experiments/bootstrap-policy.md; chỉ sau đó mở gate cho task phụ thuộc.

**Tiêu chí nghiệm thu:**

- [ ] AT-B00-04-01: Record exact executable/version, license and bounded build/test invocation for policy; run one passing fixture and one deliberately failing fixture, retain exit codes and explain unsupported environment.
- [ ] AT-B00-04-02: Document fixture rights, no personal data, explicit cleanup/stop plan, actual/proposed file map and recovery checkpoint; obtain scoped approval before creating product infrastructure.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": null, "command": null, "gate": "Bootstrap entry requires only separately approved fixture scope, tooling/license discovery and no unresolved infrastructure choice. It does not require a pre-existing successful runner. Completion requires creating and executing the bounded positive/negative runner in this whitelist."}

**Chủ nhiệm chuẩn bị công cụ:**

This is a planning/research/checkpoint task; any executable probe still requires scoped authorization and an established bounded command.

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [B00-05] Bootstrap verified tooling and fixtures: life-state

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

life-state

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

Bộ chạy kiểm tra và dữ liệu giả tối thiểu cho life-state; phiên bản/giấy phép và lệnh có bằng chứng

**Phụ thuộc:**

P00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/experiments/bootstrap-life-state.md; tests/bootstrap/life-state/Bootstrap.Tests.csproj; tests/bootstrap/life-state/BootstrapTests.cs; tools/verify/life-state.ps1

**Các bước cụ thể:**

1. Khảo sát công cụ thực có cho life-state: Get-Command dotnet, python; ghi phiên bản bằng dotnet --info / python --version nếu tìm thấy. Đây là kiểm tra môi trường, không phải test sản phẩm.
2. Sau khi được cho phép riêng, chọn công cụ phù hợp đã xác minh giấy phép; tạo duy nhất fixture/project và tools/verify/life-state.ps1 trong whitelist. Renderer phải chọn phiên bản Unity qua D-01; không mặc định MSTest kiểm được Unity.
3. Thiết lập script có timeout hữu hạn, không tải dữ liệu thật, giữ exit code; thêm fixture dương và fixture âm cố ý sai. Với C# dùng dotnet test <project-thực-tế> --configuration Release --no-restore sau bước restore có kiểm soát; renderer ghi đúng lệnh batch của phiên bản Unity đã chọn.
4. Chạy powershell -NoProfile -File tools/verify/life-state.ps1 cho fixture dương; bật chế độ âm đã ghi trong script và kiểm exit khác 0. Lưu lệnh, version, seed, timeout, cleanup và kết quả trong docs/experiments/bootstrap-life-state.md; chỉ sau đó mở gate cho task phụ thuộc.

**Tiêu chí nghiệm thu:**

- [ ] AT-B00-05-01: Record exact executable/version, license and bounded build/test invocation for life-state; run one passing fixture and one deliberately failing fixture, retain exit codes and explain unsupported environment.
- [ ] AT-B00-05-02: Document fixture rights, no personal data, explicit cleanup/stop plan, actual/proposed file map and recovery checkpoint; obtain scoped approval before creating product infrastructure.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": null, "command": null, "gate": "Bootstrap entry requires only separately approved fixture scope, tooling/license discovery and no unresolved infrastructure choice. It does not require a pre-existing successful runner. Completion requires creating and executing the bounded positive/negative runner in this whitelist."}

**Chủ nhiệm chuẩn bị công cụ:**

This is a planning/research/checkpoint task; any executable probe still requires scoped authorization and an established bounded command.

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [B00-06] Bootstrap verified tooling and fixtures: task-execution

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

task-execution

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

Bộ chạy kiểm tra và dữ liệu giả tối thiểu cho task-execution; phiên bản/giấy phép và lệnh có bằng chứng

**Phụ thuộc:**

P00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/experiments/bootstrap-task-execution.md; tests/bootstrap/task-execution/Bootstrap.Tests.csproj; tests/bootstrap/task-execution/BootstrapTests.cs; tools/verify/task-execution.ps1

**Các bước cụ thể:**

1. Khảo sát công cụ thực có cho task-execution: Get-Command dotnet, python; ghi phiên bản bằng dotnet --info / python --version nếu tìm thấy. Đây là kiểm tra môi trường, không phải test sản phẩm.
2. Sau khi được cho phép riêng, chọn công cụ phù hợp đã xác minh giấy phép; tạo duy nhất fixture/project và tools/verify/task-execution.ps1 trong whitelist. Renderer phải chọn phiên bản Unity qua D-01; không mặc định MSTest kiểm được Unity.
3. Thiết lập script có timeout hữu hạn, không tải dữ liệu thật, giữ exit code; thêm fixture dương và fixture âm cố ý sai. Với C# dùng dotnet test <project-thực-tế> --configuration Release --no-restore sau bước restore có kiểm soát; renderer ghi đúng lệnh batch của phiên bản Unity đã chọn.
4. Chạy powershell -NoProfile -File tools/verify/task-execution.ps1 cho fixture dương; bật chế độ âm đã ghi trong script và kiểm exit khác 0. Lưu lệnh, version, seed, timeout, cleanup và kết quả trong docs/experiments/bootstrap-task-execution.md; chỉ sau đó mở gate cho task phụ thuộc.

**Tiêu chí nghiệm thu:**

- [ ] AT-B00-06-01: Record exact executable/version, license and bounded build/test invocation for task-execution; run one passing fixture and one deliberately failing fixture, retain exit codes and explain unsupported environment.
- [ ] AT-B00-06-02: Document fixture rights, no personal data, explicit cleanup/stop plan, actual/proposed file map and recovery checkpoint; obtain scoped approval before creating product infrastructure.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": null, "command": null, "gate": "Bootstrap entry requires only separately approved fixture scope, tooling/license discovery and no unresolved infrastructure choice. It does not require a pre-existing successful runner. Completion requires creating and executing the bounded positive/negative runner in this whitelist."}

**Chủ nhiệm chuẩn bị công cụ:**

This is a planning/research/checkpoint task; any executable probe still requires scoped authorization and an established bounded command.

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [B00-07] Bootstrap verified tooling and fixtures: distribution

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

distribution

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

Bộ chạy kiểm tra và dữ liệu giả tối thiểu cho distribution; phiên bản/giấy phép và lệnh có bằng chứng

**Phụ thuộc:**

P00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/experiments/bootstrap-distribution.md; tests/bootstrap/distribution/Bootstrap.Tests.csproj; tests/bootstrap/distribution/BootstrapTests.cs; tools/verify/distribution.ps1

**Các bước cụ thể:**

1. Khảo sát công cụ thực có cho distribution: Get-Command dotnet, python; ghi phiên bản bằng dotnet --info / python --version nếu tìm thấy. Đây là kiểm tra môi trường, không phải test sản phẩm.
2. Sau khi được cho phép riêng, chọn công cụ phù hợp đã xác minh giấy phép; tạo duy nhất fixture/project và tools/verify/distribution.ps1 trong whitelist. Renderer phải chọn phiên bản Unity qua D-01; không mặc định MSTest kiểm được Unity.
3. Thiết lập script có timeout hữu hạn, không tải dữ liệu thật, giữ exit code; thêm fixture dương và fixture âm cố ý sai. Với C# dùng dotnet test <project-thực-tế> --configuration Release --no-restore sau bước restore có kiểm soát; renderer ghi đúng lệnh batch của phiên bản Unity đã chọn.
4. Chạy powershell -NoProfile -File tools/verify/distribution.ps1 cho fixture dương; bật chế độ âm đã ghi trong script và kiểm exit khác 0. Lưu lệnh, version, seed, timeout, cleanup và kết quả trong docs/experiments/bootstrap-distribution.md; chỉ sau đó mở gate cho task phụ thuộc.

**Tiêu chí nghiệm thu:**

- [ ] AT-B00-07-01: Record exact executable/version, license and bounded build/test invocation for distribution; run one passing fixture and one deliberately failing fixture, retain exit codes and explain unsupported environment.
- [ ] AT-B00-07-02: Document fixture rights, no personal data, explicit cleanup/stop plan, actual/proposed file map and recovery checkpoint; obtain scoped approval before creating product infrastructure.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": null, "command": null, "gate": "Bootstrap entry requires only separately approved fixture scope, tooling/license discovery and no unresolved infrastructure choice. It does not require a pre-existing successful runner. Completion requires creating and executing the bounded positive/negative runner in this whitelist."}

**Chủ nhiệm chuẩn bị công cụ:**

This is a planning/research/checkpoint task; any executable probe still requires scoped authorization and an established bounded command.

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.
