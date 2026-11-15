# P02 task cards

Generated from docs/product/AI/backlog.json. Grouping is navigation only; dependencies below determine dispatch. No phase-level edges. All future work requires separate authorization.

## [P02-01] Chọn và dựng renderer thử tối thiểu

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

desktop-body

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

core

**Mã yêu cầu:**

Enabler; linked predecessors define bounded output.

**Quyết định / rào cản:**

D-01

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md; docs/unity-windows/SPEC.md; docs/unity-windows/TEST_PLAN.md; docs/unity-windows/SOURCES.md

**Đầu ra:**

Pinned Unity probe

**Phụ thuộc:**

P00-02, P00-04, B00-02, A00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

unity/CompanionRenderer/ProjectSettings/ProjectVersion.txt; unity/CompanionRenderer/Packages/manifest.json; unity/CompanionRenderer/Assets/Probe.unity; unity/CompanionRenderer/Assets/Runtime/CompanionRenderer.Runtime.asmdef; unity/CompanionRenderer/Assets/Editor/ProbeBuild.cs

**Các bước cụ thể:**

1. Đối chiếu SP09 và phạm vi enabler với mục tiêu: Chọn và dựng renderer thử tối thiểu. Đọc quyết định D-01 và SPEC UW-DOC-2026-11-15-r4; khóa ứng viên Unity 6.3 LTS (6000.3.28f1) dưới gói Unity Personal ($0 dự án cá nhân), backend D3D11 + URP 2D/Core, và .NET Standard 2.1.
2. Thực hiện lát có thể nghiệm thu riêng trong unity/CompanionRenderer/ProjectSettings/ProjectVersion.txt; unity/CompanionRenderer/Packages/manifest.json; unity/CompanionRenderer/Assets/Probe.unity; unity/CompanionRenderer/Assets/Runtime/CompanionRenderer.Runtime.asmdef; unity/CompanionRenderer/Assets/Editor/ProbeBuild.cs sau khi được cho phép: ghim version/platform/renderpipeline/license, nhân vật chỉ placeholder, asmdef biên dịch mọi script dưới Assets/Runtime và ProbeBuild là static editor build entry.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: Build Windows (ProbeBuild.BuildWindowsProbe) thoát 0 và nhánh âm (ProbeBuild.VerifyNegative) thoát khác 0 dưới supervisor 120s; không input/capture/network authority.
4. Chuẩn bị và chạy sau bootstrap B00-02: Unity editor/build smoke và inventory dependency (UW03); lưu build log, Player hash, exit code và revision vào TEMP/báo cáo, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P02-01-01: Version/platform/renderpipeline và license được ghi; nhân vật chỉ placeholder.
- [ ] AT-P02-01-02: Build Windows chạy được, không input/capture/network authority.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-02", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "Unity editor/build smoke và inventory dependency."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-02

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [P02-02] Thử transparent overlay và hit regions

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

desktop-body

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

core

**Mã yêu cầu:**

Enabler; linked predecessors define bounded output.

**Quyết định / rào cản:**

D-01

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md; docs/unity-windows/SPEC.md; docs/unity-windows/TEST_PLAN.md; docs/unity-windows/SOURCES.md

**Đầu ra:**

Overlay/hit test report

**Phụ thuộc:**

P02-01, B00-01, B00-02, A00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

unity/CompanionRenderer/Assets/Runtime/OverlayProbe.cs; tests/Fixtures/WindowSurface.csproj; tests/Fixtures/WindowSurface.cs; docs/experiments/overlay.md

**Các bước cụ thể:**

1. Đối chiếu SP09 và phạm vi enabler với mục tiêu: Thử transparent overlay và hit regions. Đọc quyết định D-01; khóa phạm vi đầu ra Overlay/hit test report.
2. Thực hiện lát có thể nghiệm thu riêng trong unity/CompanionRenderer/Assets/Runtime/OverlayProbe.cs; tests/Fixtures/WindowSurface.csproj; tests/Fixtures/WindowSurface.cs; docs/experiments/overlay.md sau khi được cho phép: OverlayProbe biên dịch qua CompanionRenderer.Runtime.asmdef (P02-01) và xuất marker nạp script trong Player log; WindowSurface là fixture .NET 10 độc lập đo hit/click-through.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: Focus/topmost/fullscreen modes và fake Shift gesture probe (UW08/UW09 trong OverlayProbe, không hoàn tất P20-03) đo và ghi unsupported, không bypass hay dùng kết quả giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap B00-02 & B00-01: UW04–UW09 trên Windows với WindowSurface và CompanionRenderer.exe; lưu expected/actual từng case, PID/counters, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P02-02-01: Avatar/prop nhận chuột đúng vùng; vùng rỗng không chặn app phía dưới.
- [ ] AT-P02-02-02: Focus/topmost/fullscreen modes đo và ghi unsupported, không bypass.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-02", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "E-INT native runtime trên Windows với fixtureapp."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-02

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [P02-03] Thử tọa độ qua monitor và DPI

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

desktop-body

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

core

**Mã yêu cầu:**

Enabler; linked predecessors define bounded output.

**Quyết định / rào cản:**

D-01

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md; docs/unity-windows/SPEC.md; docs/unity-windows/TEST_PLAN.md; docs/unity-windows/SOURCES.md

**Đầu ra:**

Coordinate contract/tests

**Phụ thuộc:**

P02-02, B00-01, B00-02, A00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

src/Host/Geometry/Host.Geometry.csproj; src/Host/Geometry/CoordinateMap.cs; tests/Integration/CoordinateMap.Tests.csproj; tests/Integration/CoordinateMapTests.cs; docs/experiments/coordinates.md

**Các bước cụ thể:**

1. Đối chiếu SP09 và phạm vi enabler với mục tiêu: Thử tọa độ qua monitor và DPI. Đọc quyết định D-01; khóa phạm vi đầu ra Coordinate contract/tests.
2. Thực hiện lát có thể nghiệm thu riêng trong src/Host/Geometry/Host.Geometry.csproj; src/Host/Geometry/CoordinateMap.cs; tests/Integration/CoordinateMap.Tests.csproj; tests/Integration/CoordinateMapTests.cs; docs/experiments/coordinates.md sau khi được cho phép: CoordinateMap.Tests.csproj đặt EnableDefaultCompileItems=false để chỉ biên dịch CoordinateMapTests.cs; phân biệt physical/DIP/Unity units và bind layoutGeneration.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: Move/scale/monitorchange (kể cả tọa độ âm) làm vô hiệu target cũ; thiếu phần cứng 2-monitor giữ NOT RUN, không dùng kết quả mẫu giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap B00-01 & B00-02: dotnet test CoordinateMap.Tests.csproj (--filter IT-05/UW10..UW12) kết hợp đo anchor Player từ P02-02; lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P02-03-01: Phân biệt physical/DIP/Unity units và bind layoutgeneration.
- [ ] AT-P02-03-02: Move/scale/monitorchange làm vô hiệu target cũ.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-01", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "IT-05 với mixedDPI/negativecoords/testrects."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-01

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [P02-04] Thử kết nối typed host-renderer

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

core

**Mã yêu cầu:**

Enabler; linked predecessors define bounded output.

**Quyết định / rào cản:**

D-03

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md; docs/unity-windows/SPEC.md; docs/unity-windows/TEST_PLAN.md; docs/unity-windows/SOURCES.md

**Đầu ra:**

IPC probe

**Phụ thuộc:**

P02-01, P00-02, B00-01, A00-03

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

src/Host/Transport/Host.Transport.csproj; src/Host/Transport/RendererChannel.cs; unity/CompanionRenderer/Assets/Runtime/HostChannel.cs; tests/Integration/RendererChannel.Tests.csproj; tests/Integration/RendererChannelTests.cs

**Các bước cụ thể:**

1. Đối chiếu SP09 và phạm vi enabler với mục tiêu: Thử kết nối typed host-renderer. Đọc quyết định D-03 và SPEC UW-DOC-2026-11-15-r4; khóa phạm vi đầu ra IPC probe (Named Pipe CurrentUserOnly + framing JSON 32-bit length prefix).
2. Thực hiện lát có thể nghiệm thu riêng trong src/Host/Transport/Host.Transport.csproj; src/Host/Transport/RendererChannel.cs; unity/CompanionRenderer/Assets/Runtime/HostChannel.cs; tests/Integration/RendererChannel.Tests.csproj; tests/Integration/RendererChannelTests.cs sau khi được cho phép: HostChannel biên dịch qua CompanionRenderer.Runtime.asmdef (.NET Standard 2.1), RendererChannel.Tests.csproj đặt EnableDefaultCompileItems=false; handshake role/version/session và bounded message validate.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: Duplicate/unknown/reordered/oversize/wrong-elevation messages bị từ chối trước dispatch, không phát input fake sink hoặc đổi grants. Không dùng kết quả mẫu giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap B00-01: dotnet test RendererChannel.Tests.csproj (UW14–UW19 / IT-04 contract/abuse tests); lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P02-04-01: Handshake role/version/session và boundedmessage validate.
- [ ] AT-P02-04-02: Duplicate/unknown/reordered messages không phát input hoặc đổi grants.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-01", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "IT-04 contract/abuse tests, peercompatibility."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-01

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

Không phải task triển khai; xem predecessor.

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [P02-05] Thử mất kết nối và khôi phục an toàn

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

core

**Mã yêu cầu:**

SP09

**Quyết định / rào cản:**

D-02, D-10

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md; docs/unity-windows/SPEC.md; docs/unity-windows/TEST_PLAN.md; docs/unity-windows/SOURCES.md

**Đầu ra:**

Failure state report

**Phụ thuộc:**

P02-04, P02-03, B00-01, A00-02, A00-10

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

src/Host/Transport/ConnectionLifecycle.cs; tests/Integration/ConnectionLifecycle.Tests.csproj; tests/Integration/ConnectionLifecycleTests.cs; docs/experiments/disconnect.md

**Các bước cụ thể:**

1. Đối chiếu SP09 và phạm vi enabler với mục tiêu: Thử mất kết nối và khôi phục an toàn. Đọc quyết định D-02, D-10 và SPEC UW-DOC-2026-11-15-r4; khóa phạm vi đầu ra Failure state report.
2. Thực hiện lát có thể nghiệm thu riêng trong src/Host/Transport/ConnectionLifecycle.cs; tests/Integration/ConnectionLifecycle.Tests.csproj; tests/Integration/ConnectionLifecycleTests.cs; docs/experiments/disconnect.md sau khi được cho phép: ConnectionLifecycle biên dịch trong Host.Transport.csproj (P02-04); ConnectionLifecycle.Tests.csproj đặt EnableDefaultCompileItems=false; mất renderer/latecallback không cho lệnh click vượt generation.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: Reconnect queue UX theo quyết định người dùng (paused + hỏi lại, revalidate toàn bộ, không silent replay); thiếu atomicity write của D-10 giữ BLOCKED/hỏi rõ, không giả thành công.
4. Chuẩn bị và chạy sau bootstrap B00-01: dotnet test ConnectionLifecycle.Tests.csproj (UW20–UW29 / IT-04 reconnect/kill/stop); lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P02-05-01: Mất renderer/latecallback không cho lệnh click vượt generation.
- [ ] AT-P02-05-02: Reconnect queue UX theo quyết định người dùng, không silent replay.
- [ ] AT-P02-05-03: AT-SP09 — D-02: Hình ảnh lỗi thì tạm dừng thao tác lên app khác; phục hồi vẫn tạm dừng và hỏi trước tiếp tục, kiểm quyền/an toàn mới. Không phát lại mù quáng; hợp đồng kết nối/mất kết nối còn mở. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-01", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "Kill/restart fakepeer, delayedack and reconnect IT-04."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-01

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

SP09

**Mã phi chức năng:**

See linked requirement / prerequisite scope.
