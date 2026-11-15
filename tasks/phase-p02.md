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

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md; docs/godot-windows/SPEC.md; docs/godot-windows/TEST_PLAN.md; docs/godot-windows/SOURCES.md

**Đầu ra:**

Pinned Godot probe

**Phụ thuộc:**

P00-02, P00-04, B00-02, A00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

godot/CompanionRenderer/project.godot; godot/CompanionRenderer/CompanionRenderer.csproj; godot/CompanionRenderer/scenes/Probe.tscn; godot/CompanionRenderer/export_presets.cfg; godot/CompanionRenderer/scripts/ProbeBuild.gd

**Các bước cụ thể:**

1. Đối chiếu SP09 và phạm vi enabler với mục tiêu: Chọn và dựng renderer thử tối thiểu. Đọc quyết định D-01 và SPEC GW-DOC-2026-11-15-r1; khóa ứng viên Godot 4.7.2 – .NET dưới giấy phép MIT ($0, không cần tài khoản/seat), backend Godot Windows renderer (Compatibility/Vulkan/D3D12, NOT VERIFIED), và C# (.NET).
2. Thực hiện lát có thể nghiệm thu riêng đúng whitelist: godot/CompanionRenderer/project.godot; godot/CompanionRenderer/CompanionRenderer.csproj; godot/CompanionRenderer/export_presets.cfg; godot/CompanionRenderer/scenes/Probe.tscn; godot/CompanionRenderer/scripts/ProbeBuild.gd sau khi được cho phép: ghim cấu hình/platform/preset export Windows Desktop, nhân vật chỉ placeholder, biên dịch C# qua CompanionRenderer.csproj (Godot.NET.Sdk).
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: Export Windows Desktop (--headless --path godot/CompanionRenderer --export-release "Windows Desktop" <TEMP>/p02-01-player/CompanionRenderer.exe) thoát 0 và nhánh âm (scripts/ProbeBuild.gd -- --probe-neg) thoát khác 0 dưới supervisor 120s; không input/capture/network authority.
4. Chuẩn bị và chạy sau bootstrap B00-02: Godot editor/export smoke và inventory dependency (UW03); lưu build log, exported binary hash, exit code và revision vào TEMP/báo cáo, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P02-01-01: Version/platform/renderpipeline và license được ghi; nhân vật chỉ placeholder.
- [ ] AT-P02-01-02: Build Windows chạy được, không input/capture/network authority.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-02", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "Godot editor/build smoke và inventory dependency."}

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

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md; docs/godot-windows/SPEC.md; docs/godot-windows/TEST_PLAN.md; docs/godot-windows/SOURCES.md

**Đầu ra:**

Overlay/hit test report

**Phụ thuộc:**

P02-01, B00-01, B00-02, A00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

godot/CompanionRenderer/scripts/OverlayProbe.cs; tests/Fixtures/WindowSurface.csproj; tests/Fixtures/WindowSurface.cs; docs/experiments/overlay.md

**Các bước cụ thể:**

1. Đối chiếu SP09 và phạm vi enabler với mục tiêu: Thử transparent overlay và hit regions. Đọc quyết định D-01; khóa phạm vi đầu ra Overlay/hit test report.
2. Thực hiện lát có thể nghiệm thu riêng trong godot/CompanionRenderer/scripts/OverlayProbe.cs; tests/Fixtures/WindowSurface.csproj; tests/Fixtures/WindowSurface.cs; docs/experiments/overlay.md sau khi được cho phép: OverlayProbe biên dịch qua CompanionRenderer.csproj (Godot.NET.Sdk, P02-01) và xuất marker nạp script trong Godot log; WindowSurface là fixture .NET 10 độc lập đo hit/click-through.
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

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md; docs/godot-windows/SPEC.md; docs/godot-windows/TEST_PLAN.md; docs/godot-windows/SOURCES.md

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
2. Thực hiện lát có thể nghiệm thu riêng trong src/Host/Geometry/Host.Geometry.csproj; src/Host/Geometry/CoordinateMap.cs; tests/Integration/CoordinateMap.Tests.csproj; tests/Integration/CoordinateMapTests.cs; docs/experiments/coordinates.md sau khi được cho phép: CoordinateMap.Tests.csproj đặt EnableDefaultCompileItems=false để chỉ biên dịch CoordinateMapTests.cs; phân biệt physical/DIP/Godot units và bind layoutGeneration.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: Move/scale/monitorchange (kể cả tọa độ âm) làm vô hiệu target cũ; thiếu phần cứng 2-monitor giữ NOT RUN, không dùng kết quả mẫu giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap B00-01 & B00-02: dotnet test CoordinateMap.Tests.csproj (--filter IT-05/UW10..UW12) kết hợp đo anchor Player từ P02-02; lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P02-03-01: Phân biệt physical/DIP/Godot units và bind layoutgeneration.
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

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md; docs/godot-windows/SPEC.md; docs/godot-windows/TEST_PLAN.md; docs/godot-windows/SOURCES.md

**Đầu ra:**

IPC probe

**Phụ thuộc:**

P02-01, P00-02, B00-01, A00-03

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

src/Host/Transport/Host.Transport.csproj; src/Host/Transport/RendererChannel.cs; godot/CompanionRenderer/scripts/HostChannel.cs; tests/Integration/RendererChannel.Tests.csproj; tests/Integration/RendererChannelTests.cs

**Các bước cụ thể:**

1. Đối chiếu SP09 và phạm vi enabler với mục tiêu: Thử kết nối typed host-renderer. Đọc quyết định D-03 và SPEC GW-DOC-2026-11-15-r1; khóa phạm vi đầu ra IPC probe (Named Pipe CurrentUserOnly + framing JSON 32-bit length prefix).
2. Thực hiện lát có thể nghiệm thu riêng trong src/Host/Transport/Host.Transport.csproj; src/Host/Transport/RendererChannel.cs; godot/CompanionRenderer/scripts/HostChannel.cs; tests/Integration/RendererChannel.Tests.csproj; tests/Integration/RendererChannelTests.cs sau khi được cho phép: HostChannel biên dịch qua CompanionRenderer.csproj (Godot.NET.Sdk), RendererChannel.Tests.csproj đặt EnableDefaultCompileItems=false; handshake role/version/session và bounded message validate.
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

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md; docs/godot-windows/SPEC.md; docs/godot-windows/TEST_PLAN.md; docs/godot-windows/SOURCES.md

**Đầu ra:**

Failure state report

**Phụ thuộc:**

P02-04, P02-03, B00-01, A00-02, A00-10

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

src/Host/Transport/ConnectionLifecycle.cs; tests/Integration/ConnectionLifecycle.Tests.csproj; tests/Integration/ConnectionLifecycleTests.cs; docs/experiments/disconnect.md

**Các bước cụ thể:**

1. Đối chiếu SP09 và phạm vi enabler với mục tiêu: Thử mất kết nối và khôi phục an toàn. Đọc quyết định D-02, D-10 và SPEC GW-DOC-2026-11-15-r1; khóa phạm vi đầu ra Failure state report.
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
