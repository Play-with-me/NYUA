# Đặc tả đề xuất phép thử Godot Engine – Windows

Revision **GW-DOC-2026-11-15-r1** — **DRAFT_FOR_REVIEW / chưa được phép thực thi (`NOT_AUTHORIZED`)**.  
Chuyển hướng chính thức từ Unity sang **Godot Engine** theo quyết định người dùng ngày `2026-11-15`. Xem [Kế hoạch kiểm](TEST_PLAN.md) và [Nguồn chính thức](SOURCES.md).

> [!IMPORTANT]
> Tài liệu này thay thế `docs/unity-windows/SPEC.md` (nay đã chuyển thành trang chuyển hướng `SUPERSEDED`). Các kết quả lịch sử của mẫu `E02a` (`53/53` MSTest, `35/35` UI case, nghiệm thu trải nghiệm `C3`) và lịch sử PR #1/#2 vẫn được giữ nguyên vẹn; **không** có phép thử Godot nào đã chạy (`UW01–UW30` đều **`NOT RUN`**).

## Phần dành cho người đọc

Mục tiêu là chuẩn bị bản thiết kế rõ ràng cho phép thử nhỏ bằng **Godot Engine** để kiểm chứng xem nhân vật hiển thị trên desktop Windows 11 có cản chuột, sai vị trí qua các màn hình/tỷ lệ phóng hay tự chạy lại việc cũ sau lỗi hay không. **Chưa cài Godot, chưa tải SDK, chưa tạo project/code thử nghiệm và chưa chạy phép thử trong lượt tài liệu này.**

| Hiện tại | Trải nghiệm muốn kiểm sau khi được cho phép riêng |
|---|---|
| `E02a` đã kiểm quy tắc bằng dữ liệu giả (người dùng đã chấp nhận trải nghiệm `C3`; `T05` kỹ thuật còn mở) | Hình thử của riêng demo hiển thị qua **Godot Engine** và cửa sổ quản lý Windows |
| Chưa biết độ trong suốt, click xuyên vùng trống và nhiều DPI trên Godot Windows có đạt không (`NOT VERIFIED`) | Vùng hình nhận tương tác, chỗ trống để chuột đi thẳng xuống cửa sổ thử ở dưới |
| Đã chốt hành vi phục hồi sau lỗi (`D-02`: dừng khi lỗi, hỏi trước khi tiếp tục) | Hình lỗi thì dừng ngay; khi hình trở lại vẫn tạm dừng và hỏi bạn trước khi tiếp tục |

```text
[Wireframe UX mục tiêu cho tầng WPF Host sau này (src/Desktop.Wpf/ — ngoài phạm vi code P02-01..05, BLOCKED tới khi có task WPF)]
[Chuẩn bị] [Chưa chạy / Đang kết nối / Tạm dừng / Lỗi / Có bằng chứng]
  Hình thử: [vùng có thể kéo]      nền trống → cửa sổ thử của chính nhóm
  Trạng thái: Không có quyền đọc/điều khiển ứng dụng thật
  [Dừng phép thử]  [Xem lý do]  [Kết nối lại]  [Cho tiếp tục sau lỗi]  [Giữ tạm dừng]
```

Hành trình tương lai (gồm hai chặng tách bạch, **không phải hướng dẫn chạy ngay**):
1. **Chặng probe kỹ thuật headless (`P02-01..05`):** Mở cửa sổ nền `WindowSurface.exe` và `CompanionRenderer.exe` (export từ Godot .NET) với dữ liệu giả → kéo/chọn trong vùng hình của `OverlayProbe.cs` → kiểm tra vùng trống đi thẳng xuống `WindowSurface.exe` → kiểm tra kênh Named Pipe + `Host.Geometry` + state machine **headless** `ConnectionLifecycle` (`PausedAfterFault`, không tự chạy lại sau lỗi).
2. **Chặng UI tương tác WPF Host (`src/Desktop.Wpf/` — hiện `BLOCKED`, ngoài whitelist `P02-01..05`):** Các hộp thoại `[Dừng phép thử]` / `[Kết nối lại]` / `[Cho tiếp tục sau lỗi]` / `[Giữ tạm dừng]` bằng bàn phím và màn hình WPF thật thuộc phạm vi task có `src/Desktop.Wpf/` (`P10`/`P40`/`P50`), **không** nằm trong `P02-01..05` và **không** mượn `labs/policy-native`.

### Quyết định của người dùng đã chốt (Giữ nguyên qua chuyển đổi sang Godot)

1. **Giấy phép & Ngân sách (`P00-04` / `D-13` / `SP06`):** Dự án cá nhân, không kinh phí, giai đoạn thử **chỉ dùng 100% công cụ miễn phí (`$0`)**. Dùng **Godot Engine** giấy phép **MIT** (không cần tài khoản Unity, không cần Unity Personal, không có trần doanh thu `200.000 USD` của Unity). Vẫn phải lập `docs/licenses/INVENTORY.md` cho MIT + third-party notices của official export templates + `.NET SDK` / NuGet (`MIT`).
2. **Giữ nguyên yêu cầu `NV08` & trạng thái thiếu phần cứng (`D-01` / `NV08`):** **Giữ nguyên yêu cầu `NV08`** (không hạ chuẩn); các ca kiểm chứng **nhiều màn hình (`UW11`, `UW12`)** và **toàn màn hình độc quyền (exclusive fullscreen)** được đánh dấu **`NOT RUN` — chờ thiết bị thật** cho bản thử đầu.
3. **UX phục hồi sau lỗi (`D-02` / `D-10`):** Giữ nguyên `[Kết nối lại]` → `[Cho tiếp tục sau lỗi]` / `[Giữ tạm dừng]`.

## 1. Baseline E02a và nghĩa của “đã nghiệm thu”

- **C3 nghiệm thu trải nghiệm demo** đã được người dùng cho đóng ngày 2026-11-15 ([E02a-USER-ACCEPTANCE.md](../../tasks/E02a-USER-ACCEPTANCE.md)).
- **`P01-01` human gate `OBTAINED` chỉ áp dụng cho trải nghiệm này; `P01-01` CHƯA được coi Done kỹ thuật** (`T05` còn mở).
- Số liệu `53/53` MSTest và `35/35` UI case là bằng chứng lịch sử. Các gate `P20-01` và `P60-04`/`P60-05` vẫn là `NOT_OBTAINED`.

## 2. Scope, giả định và cổng trước thực thi

- **Nghiêm cấm trong lượt tài liệu này:** cài đặt Godot/SDK/export templates, tạo project/fixture/`.cs`/`.gd`/`.tscn`, chạy Godot/native probe, sửa mã nguồn sản phẩm, commit/push/PR/deploy. Mọi kết quả runtime giữ **`NOT RUN`**.
- Giữ nguyên ngoại hình nhân vật đã chốt (tai cáo/đuôi bạc/quà thỏ/táo/nước cam).

### Thứ tự canonical — không chu trình và không deadlock ngữ nghĩa

Registry duy nhất: `docs/product/AI/backlog.json`:

```text
P00-01 → R00-01 → A00-01              (D-01 đề cương / rà đề cương)
        → R00-02 → A00-02 ┐
        → R00-03 → A00-03 ┴→ P00-02  (hợp đồng)
        → R00-13 → A00-13 → P00-04  (giấy phép/chi phí MIT + .NET + notices)
        → R00-10 → A00-10           (D-10 khôi phục sau crash)
        → B00-02                    (bootstrap Godot fixture cô lập, không chờ P02-01)
        → B00-01                    (bootstrap .NET host/runner cô lập)
P00-02 + P00-04 + B00-02 + A00-01 → P02-01 (godot/CompanionRenderer + export preset)
P02-01 + B00-01 + B00-02 + A00-01 → P02-02 (OverlayProbe.cs + WindowSurface.csproj)
P02-02 + B00-01 + B00-02 + A00-01 → P02-03 (Host.Geometry.csproj + CoordinateMap.Tests.csproj)
P02-01 + P00-02 + B00-01 + A00-03 → P02-04 (Host.Transport.csproj + HostChannel.cs + RendererChannel.Tests.csproj)
P02-04 + P02-03 + B00-01 + A00-02 + A00-10 → P02-05 (ConnectionLifecycle.cs + ConnectionLifecycle.Tests.csproj)
```

<details><summary>Phần kỹ thuật đề xuất — Godot Engine .NET (NOT VERIFIED trên Windows 11)</summary>

## 3. Stack và lựa chọn kiến trúc (ứng viên đề xuất)

### 3.1. Phiên bản Godot và giấy phép

- **Ứng viên đề xuất:** **Godot Engine `4.7.2 – .NET`** (Windows x64, `S01`, `S03`), giấy phép **MIT** (`S02`).
- **Không dùng lại khái niệm Unity:** Bỏ hoàn toàn `.asmdef`, `ProjectSettings/ProjectVersion.txt`, `Packages/manifest.json`, URP, và điều kiện `Unity Personal` / tài khoản Unity.

### 3.2. Ngôn ngữ kịch bản & khả năng thích ứng (`C#` vs `GDScript`)

- **`B00-02` (Bootstrap fixture tối giản):** Dùng `scripts/BootstrapVerify.gd` (`GDScript`) trong bộ 5 file whitelist để kiểm tra Editor CLI `--headless`, load scene `Bootstrap.tscn` và nhánh âm exit `!= 0` mà không phình file `.csproj`/`.sln` ngoài whitelist.
- **`P02-01..05` (Probe & IPC):** Dùng **Godot C# (`.NET`)** (`godot/CompanionRenderer/CompanionRenderer.csproj` + `Godot.NET.Sdk`) phối hợp scene `Probe.tscn` và script `OverlayProbe.cs`, `HostChannel.cs`.
  - **Lý do kỹ thuật:** Cùng dùng `.NET` nên `HostChannel.cs` có thể dùng trực tiếp `NamedPipeClientStream` và `System.Text.Json` (vẫn kiểm chặt `MaxDepth=16`, unknown field, duplicate key, UTF-8 nghiêm ngặt ở `UW16–UW17`), loại bỏ hẳn rào cản `.NET Standard 2.1` của Unity.
  - **Giữ kiến trúc dễ chuyển đổi:** Giao thức IPC và `Host.Geometry` / `Host.Transport` nằm hoàn toàn phía Host (`src/Host/*`), tách biệt tiến trình với `CompanionRenderer.exe`.

### 3.3. Dựng hình, trong suốt & click-through trên Windows (`NOT VERIFIED`)

- **Cơ chế theo tài liệu Godot 4 (`S05`):**
  - `project.godot`: bật `display/window/per_pixel_transparency/allowed = true`, `display/window/size/transparent = true`, borderless (`display/window/size/borderless = true`), `always_on_top = true`.
  - Runtime: `GetViewport().TransparentBg = true`, `DisplayServer.WindowSetFlag(DisplayServer.WindowFlags.Transparent, true)`, và `DisplayServer.WindowSetMousePassthrough(polygon)` cho vùng nhận chuột.
- **Điểm `NOT VERIFIED` bắt buộc đo ở `UW04–UW09`:**
  1. Hành vi DWM alpha compositing trên Windows 11 giữa renderer **Compatibility (OpenGL 3)** vs **Forward+ / Mobile (Vulkan / D3D12)** — phải ghi nhận thực tế ở `UW04` (không mặc định chạy sạch).
  2. **Rủi ro cắt hình của `SetWindowRgn` (`S05`):** Trên Windows, `DisplayServer.WindowSetMousePassthrough` dùng Win32 **`SetWindowRgn`**, nên **mọi phần hình/đồ vật vẽ ngoài đa giác passthrough bị cắt/ẩn hoàn toàn**. Cần kiểm chứng trực tiếp ở `UW04–UW06` xem biên đa giác động có đủ bao trùm nhân vật/đồ vật mà không che nhầm nền, hoặc có cần phương án Win32 `WS_EX_LAYERED` / đa cửa sổ bổ trợ hay không.
  3. Kéo `Shift + drag` khi mất focus/capture (`UW08–UW09`), tọa độ âm đa màn hình / mixed DPI (`UW10–UW12`), và borderless fullscreen foreground (`UW13`).

### 3.4. Topology tiến trình

- **Chọn thử chính:** Hai tiến trình tách biệt — **Godot Player (`CompanionRenderer.exe`)** + **Host libraries (`Host.Geometry`/`Host.Transport`, `.NET 10 LTS`)**. Tách crash lifecycle và giữ Host làm authority (`ADR-002`).
- **Không nhúng vào WPF (`HwndHost`):** Giữ nguyên quyết định tránh rủi ro airspace/focus (`S07`).

### 3.5. Cô lập output `.NET` & working material của Godot `.NET`

- **Cô lập `.NET` theo dependency closure (`S12`):** Cấm đặt `BaseIntermediateOutputPath`, `MSBuildProjectExtensionsPath`, hoặc `BaseOutputPath` trong `.csproj` (tránh xung đột SDK); mọi lệnh `dotnet restore`, `dotnet build --no-restore`, `dotnet test --no-restore` và `dotnet msbuild -getProperty:TargetPath` phải truyền cùng `--artifacts-path "<TEMP>/<task>/dotnet-artifacts"` (hoặc `-p:ArtifactsPath=...`) nhất quán theo dependency closure và lưu hash `project.assets.json`.
- **Working material của Godot `.NET`:**
  - `Godot.NET.Sdk` (`4.7.2`) lấy từ `GodotSharp/Tools/nupkgs` đi kèm bản Godot `.NET` (hoặc NuGet.org, phải ghi nguồn/hash vào `docs/licenses/INVENTORY.md` ở `P00-04`).
  - Khi mở/export project Godot `.NET`, engine tự sinh `.godot/`, `.godot/mono/` và có thể sinh `CompanionRenderer.sln` (nằm ngoài whitelist 5 file của `P02-01`). Các thư mục/tệp tự sinh này là working material — **không** được commit vào Git (phải có `.gitignore` cho `.godot/` và kiểm tra cleanup sạch).

</details>
