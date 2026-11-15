# Đặc tả đề xuất phép thử Unity–Windows

Revision **UW-DOC-2026-11-15-r4** — **DRAFT_FOR_REVIEW / chưa được phép thực thi**.
Nguồn quyền phạm vi: yêu cầu chỉ tài liệu ngày 2026-11-15. [Kế hoạch kiểm](TEST_PLAN.md), [nguồn chính thức](SOURCES.md).

## Phần dành cho người đọc

Mục tiêu là chuẩn bị bản thiết kế rõ ràng cho phép thử nhỏ để biết nhân vật hiển thị trên desktop Windows 11 có cản chuột, sai vị trí qua các màn hình/tỷ lệ phóng hay tự chạy lại việc cũ sau lỗi hay không. **Chưa cài Unity, chưa tạo project/code thử nghiệm và chưa chạy phép thử trong lượt tài liệu này.**

| Hiện tại | Trải nghiệm muốn kiểm sau khi được cho phép riêng |
|---|---|
| E02a đã kiểm quy tắc bằng dữ liệu giả (người dùng đã chấp nhận trải nghiệm C3) | Hình thử của riêng demo hiển thị qua Unity và cửa sổ quản lý Windows |
| Chưa biết độ trong suốt, click xuyên vùng trống và nhiều DPI có dùng được không | Vùng hình nhận tương tác, chỗ trống để chuột đi thẳng xuống cửa sổ thử ở dưới |
| Đã chốt hành vi phục hồi sau lỗi (dừng khi lỗi, hỏi trước khi tiếp tục) | Hình lỗi thì dừng ngay; khi hình trở lại vẫn tạm dừng và hỏi bạn trước khi tiếp tục |

```text
[Wireframe UX mục tiêu cho tầng WPF Host sau này (src/Desktop.Wpf/ — ngoài phạm vi code P02-01..05, BLOCKED tới khi có task WPF)]
[Chuẩn bị] [Chưa chạy / Đang kết nối / Tạm dừng / Lỗi / Có bằng chứng]
  Hình thử: [vùng có thể kéo]      nền trống → cửa sổ thử của chính nhóm
  Trạng thái: Không có quyền đọc/điều khiển ứng dụng thật
  [Dừng phép thử]  [Xem lý do]  [Kết nối lại]  [Cho tiếp tục sau lỗi]  [Giữ tạm dừng]
```

Hành trình tương lai (gồm hai chặng tách bạch, **không phải hướng dẫn chạy ngay**):
1. **Chặng probe kỹ thuật headless (`P02-01..05`):** Mở cửa sổ nền `WindowSurface.exe` và `CompanionRenderer.exe` với dữ liệu giả → kéo/chọn trong vùng hình của `OverlayProbe` → kiểm tra vùng trống đi thẳng xuống `WindowSurface.exe` → kiểm tra kênh Named Pipe + `Host.Geometry` + state machine **headless** `ConnectionLifecycle` (`PausedAfterFault`, không tự chạy lại sau lỗi).
2. **Chặng UI tương tác WPF Host (`src/Desktop.Wpf/` — hiện `BLOCKED`, ngoài whitelist `P02-01..05`):** Các hộp thoại `[Dừng phép thử]` / `[Kết nối lại]` / `[Cho tiếp tục sau lỗi]` / `[Giữ tạm dừng]` bằng bàn phím và màn hình WPF thật thuộc phạm vi task có `src/Desktop.Wpf/` (`P10`/`P40`/`P50`), **không** nằm trong `P02-01..05` và **không** mượn `labs/policy-native`.

### Quyết định của người dùng đã chốt cho Unity–Windows (`r4`)

Các lựa chọn kỹ thuật thuần túy (phiên bản Unity đã vá, pipeline dựng hình, .NET/IPC, cấu trúc file dự kiến) đã được AI chốt đề xuất theo tài liệu chính thức ở phần kỹ thuật bên dưới. 3 điểm thuộc quyền kinh doanh/giấy phép/ngân sách/trải nghiệm đã được người dùng chốt rõ như sau:

1. **Gói Unity & dự án cá nhân (`P00-04` / `D-13`):** Đây là **dự án cá nhân, không kinh phí** → sử dụng gói miễn phí **Unity Personal**. (Chủ dự án vẫn phải tự xác minh đáp ứng điều kiện doanh thu/tài chính & non-Industry theo điều khoản Unity tại thời điểm cài đặt và ghi nhận trong `P00-04`.)
2. **Ngân sách công cụ giai đoạn thử (`SP06` / `D-13`):** Giai đoạn thử **chỉ dùng 100% công cụ miễn phí (`$0`)** — không mua bản quyền trả phí, không dùng dịch vụ hay chứng thư ký số trả phí ở bản thử đầu. Mọi chi phí phát hành công khai hoặc signing ngoài giai đoạn thử (nếu phát sinh sau này) vẫn phải hỏi riêng.
3. **Giữ nguyên yêu cầu `NV08` & trạng thái thiếu phần cứng (`D-01` / `NV08`):** **Giữ nguyên yêu cầu `NV08`** (không hạ chuẩn hay thu hẹp yêu cầu sản phẩm); các ca kiểm chứng **nhiều màn hình (`UW11`, `UW12`)** và **toàn màn hình độc quyền (exclusive fullscreen)** được đánh dấu **`NOT RUN` / chờ thiết bị thật** cho bản thử đầu.

*(UX phục hồi sau lỗi giữ nguyên theo `D-02` / `D-10` đã xác nhận: `[Kết nối lại]` → `[Cho tiếp tục sau lỗi]` / `[Giữ tạm dừng]`; mọi nút tùy chọn khác như hủy hàng đợi được hoãn, không tự thêm khi chưa duyệt.)*

## 1. Baseline E02a và nghĩa của “đã nghiệm thu”

- **C3 nghiệm thu trải nghiệm demo** đã được người dùng cho đóng ngày 2026-11-15. Nguyên văn:
  “Có nhìn rõ và không có chỗ nào bị kẹt, có thể đóng nghiệm thu E02a rồi”. Trước đó về đổi kích thước: “Đã ổn rồi”.
  Xem [bằng chứng](../../tasks/E02a-USER-ACCEPTANCE.md), [tracker](../../tasks/todo.md) và [kết quả máy hiện tại](../E02a-CURRENT-MACHINE-RESULTS.md).
- **P01-01 human gate `OBTAINED` chỉ áp dụng cho trải nghiệm này; P01-01 CHƯA được coi Done kỹ thuật.**
  Danh sách kiểm tra kỹ thuật `T05` vẫn còn mở: chưa có bằng chứng đầy đủ cho kích hoạt toàn bộ điều khiển bằng `Enter`/`Space`, mọi trạng thái `disabled`/`error`, trình đọc màn hình (screen reader), số đo kích thước tối thiểu độc lập hoặc ma trận đa DPI. Không suy ra PASS kỹ thuật từ nhận xét trải nghiệm.
- Số liệu `53/53` MSTest và `35/35` UI case là bằng chứng lịch sử đã ghi trước đó, không chạy lại ở đợt tài liệu này.
  Các gate người dùng cho mỹ thuật (`P20-01`) và phát hành (`P60-04`/`P60-05`) vẫn là `NOT_OBTAINED`. Không đóng `C-PROBE` hoặc toàn sản phẩm.

## 2. Scope, giả định và cổng trước thực thi

Được phép trong lượt này: chỉ chỉnh sửa/rà soát bộ tài liệu kế hoạch này cùng canonical registry/generated/context liên quan trong `nyua-4`.
**Nghiêm cấm trong lượt này:** cài đặt Unity/SDK/package, tạo project/fixture/`.cs`/`.unity`, chạy Editor/Player/native probe, đọc/điều khiển app thật, sửa mã nguồn sản phẩm, commit/push/PR/deploy. Mọi kết quả runtime trong [TEST_PLAN](TEST_PLAN.md) giữ nguyên **`NOT RUN`**.

Phép thử tương lai chỉ dùng hình khối/nhãn giả trong cửa sổ do nhóm sở hữu. Không thay ngoại hình nhân vật đã chốt bằng placeholder; không mở rộng giấy phép art/AI. Các quyết định ngoại hình (tai cáo/đuôi bạc/quà thỏ/táo/nước cam) giữ nguyên.

### Thứ tự canonical — không chu trình và không deadlock ngữ nghĩa

Registry duy nhất: `docs/product/AI/backlog.json`. Bảng ở §8 đồng bộ nguyên văn direct dependencies và proposed files.

```text
P00-01 → R00-01 → A00-01              (D-01 đề cương / rà đề cương)
        → R00-02 → A00-02 ┐
        → R00-03 → A00-03 ┴→ P00-02  (hợp đồng)
        → R00-13 → A00-13 → P00-04  (giấy phép/chi phí)
        → R00-10 → A00-10           (D-10 khôi phục sau crash)
        → B00-02                    (bootstrap Unity fixture cô lập, không chờ P02-01)
        → B00-01                    (bootstrap .NET host/runner cô lập)
P00-02 + P00-04 + B00-02 + A00-01 → P02-01 (project Unity + Assets/Runtime.asmdef + Editor ProbeBuild)
P02-01 + B00-01 + B00-02 + A00-01 → P02-02 (Assets/Runtime/OverlayProbe.cs + WindowSurface.csproj)
P02-02 + B00-01 + B00-02 + A00-01 → P02-03 (Host.Geometry.csproj + CoordinateMap.Tests.csproj)
P02-01 + P00-02 + B00-01 + A00-03 → P02-04 (Host.Transport.csproj + Assets/Runtime/HostChannel.cs + RendererChannel.Tests.csproj)
P02-04 + P02-03 + B00-01 + A00-02 + A00-10 → P02-05 (ConnectionLifecycle.cs + ConnectionLifecycle.Tests.csproj)
```

- `B00-01`/`B00-02` chỉ đòi `P00-01` và quyền mở phạm vi fixture riêng, không đòi runner sẵn có trước khi bootstrap chạy.
- `R00-*`/`A00-*` là `document_review`, không có prerequisite thực thi; chúng không đòi bằng chứng do `P02-*` tạo ra.
- `P01-01` không nằm trên đường dependency của `P02-*`; giữ nguyên ranh giới giữa E02a demo và phép thử Unity.

<details><summary>Phần kỹ thuật đề xuất — đã chốt ứng viên theo nguồn chính thức, chưa kiểm chứng runtime</summary>

## 3. Stack và lựa chọn kiến trúc (ứng viên đề xuất)

### 3.1. Phiên bản Unity đã vá và căn cứ nguồn có ngày

- **Ứng viên chọn:** **Unity 6.3 LTS — phiên bản `6000.3.28f1`**, Windows 11 x64 (`S01`, `S02`, `S15`, `S16`, `S19`).
- **Căn cứ chọn:**
  - Nhánh `6.3 LTS` (`6000.3.0f1` phát hành ngày **2025-12-03**, bài công bố **2025-12-04** `S02`) có hỗ trợ chuẩn 2 năm tới **12/2027** (`S01`), tránh nhánh `6.0 LTS` hết hỗ trợ chuẩn **10/2026**.
  - Bản `6000.3.28f1` phát hành ngày **2026-11-03** (`S16`), nằm trên **cả hai sàn bản vá bảo mật chính thức**:
    - **`CVE-2025-59489`** (CVSS `8.4`, `CWE-426` Untrusted Search Path / Argument Injection, phát hiện **2025-06-04** *(Date Discovered)*, công bố advisory & bản vá **2025-10-02** `S15`, tối thiểu `6000.3.0b4` và bắt buộc build lại Player từ Editor đã vá).
    - **Đợt advisory tháng 10/2026 (`S19`):** `CVE-2026-111497` (Brotli decoder out-of-bounds write trong UPM/class libraries, cần rebuild Player) và `CVE-2026-111943` (thu hồi intermediate CA eMudhra), mốc vá nhánh 6.3 từ **`6000.3.27f2`** **kèm điều kiện máy Windows phải cập nhật Windows OS root trust store mới nhất**.
  - Bản `6000.3.28f1` cũng cập nhật Licensing Client `v1.19.0` và sửa nhiều lỗi 2D/Shadow.
  - **Giới hạn đã biết của `6000.3.28f1` (`S16`):** `UUM-142550` (chuột polling rate >1000 Hz có thể tụt FPS trong Editor Play Mode), `UUM-156125` (lặp `SceneManager.LoadSceneAsync`), `UUM-158166` (rút/cắm USB audio). Khi chạy `B00-02`/`P02-01` vẫn phải kiểm checksum bộ cài thật, xác minh Windows OS root trust update (`S19`) và rà lại xem có advisory mới hơn sau ngày 2026-11-15 hay không.

### 3.2. Render backend, pipeline và cấu hình sở hữu trên đĩa

- **Ứng viên chọn:** **Direct3D 11 (`D3D11`, feature level 11_0+)** kết hợp **Universal Render Pipeline (URP 2D / Core)** với Surface Type `Transparent` (Alpha / Premultiply blending, `S18`).
- **Quyền sở hữu cấu hình URP & D3D11 trong `P02-01`:**
  - `unity/CompanionRenderer/Packages/manifest.json` (do `P02-01` sở hữu) ghim gói `com.unity.render-pipelines.universal` đúng phiên bản tương thích `6000.3.28f1` (kèm `packages-lock.json` sinh kiểm soát khi restore/import, đưa vào `P00-04`).
  - `unity/CompanionRenderer/Assets/Editor/ProbeBuild.cs` (do `P02-01` sở hữu, chạy lúc build Player) gọi tường minh `PlayerSettings.SetUseDefaultGraphicsAPIs(BuildTarget.StandaloneWindows64, false)` và `PlayerSettings.SetGraphicsAPIs(BuildTarget.StandaloneWindows64, new[] { GraphicsDeviceType.Direct3D11 })`, đồng thời khởi tạo/ràng buộc hoặc assert `GraphicsSettings.defaultRenderPipeline` (`UniversalRenderPipelineAsset`) trước `BuildPipeline.BuildPlayer` và ghi trạng thái vào `UW03-build.log` (sai pipeline hoặc thiếu URP ⇒ fail build exit `!= 0`). Các file cấu hình `.asset` do Unity Editor tạo tự động (`ProjectSettings/ProjectSettings.asset`, `GraphicsSettings.asset`, URP asset) không chỉnh tay ngoài kiểm soát của `ProbeBuild.cs`.
- **Phương án dự phòng có kiểm soát:** Nếu phép thử `UW04` chứng minh swapchain URP + `D3D11` không phối hợp sạch kênh alpha với Win32/DWM (`DwmExtendFrameIntoClientArea` `MARGINS = -1` hoặc `WS_EX_LAYERED` `S11`/`S18`), chỉ chuyển sang đối chứng **Built-in Render Pipeline** hoặc **D3D12** sau khi ghi thất bại thực tế của `UW04` và sửa đề cương D-01, không tự đổi giữa chừng.
- **Không hứa trước:** `-popupwindow` chỉ bỏ viền cửa sổ (`S05`), không tự tạo nền trong suốt hoặc click-through xuyên process (`S11`, `S12`).

### 3.3. Host, .NET runtime và Unity scripting profile

- **Phạm vi project .NET trong `P02`:** `P02-02..05` chỉ sở hữu các thư viện/fixture **headless** và cửa sổ nền thử nghiệm (`tests/Fixtures/WindowSurface.csproj`, `src/Host/Geometry/Host.Geometry.csproj`, `src/Host/Transport/Host.Transport.csproj` và 3 `.Tests.csproj` tích hợp), target **`.NET 10 LTS` (`net10.0-windows` / `net10.0`)** (`S09`). Các màn hình **WPF Host tương tác** (`src/Desktop.Wpf/*.xaml` như `QueueView.xaml`, `ExternalAIView.xaml`...) thuộc các task `P10`/`P40`/`P50`, **không** nằm trong whitelist `P02` và **không** mượn `labs/policy-native` làm Host thay thế.
- **Unity scripting API profile (`.NET Standard 2.1`, `S08`):** Không phải do `.asmdef` tự đặt; cấu hình chuẩn của Unity thuộc `PlayerSettings`. Trong `P02-01`, `Assets/Editor/ProbeBuild.cs` bắt buộc gọi `PlayerSettings.SetApiCompatibilityLevel(NamedBuildTarget.Standalone, ApiCompatibilityLevel.NET_Standard_2_1)` và assert giá trị này trước khi build Player (`.asmdef` chỉ ghim platform include `WindowsStandalone64` và `overrideReferences: false`).
- **Restore & đóng băng gói `.NET`:** Mọi `.csproj` của `P02-02..05` đều phải chạy bước `dotnet restore "<exact.csproj>"` có kiểm soát cho từng project, với phiên bản NuGet test/SDK ghim cứng (không dùng floating wildcard `*`, khớp `docs/licenses/INVENTORY.md` ở `P00-04`) và lưu hash `project.assets.json` / `packages.lock.json` **trước** khi chạy `dotnet build/test --no-restore`.
- **Ranh giới nhị phân:** **Cấm** giả định nạp trực tiếp DLL `net10.0` của Host vào Unity Player. Hai phía tách biệt hoàn toàn về runtime, chỉ giao tiếp qua schema JSON có phiên bản trên kênh IPC.

### 3.4. Topology tiến trình (đề xuất chính thức cho phép thử D-01/D-02/D-03)

| Phương án | Điểm thuận | Rủi ro phải đo | Quyết định đề xuất cho phép thử |
|---|---|---|---|
| **Unity Player process riêng (`CompanionRenderer.exe`) + Host libraries (`Host.Geometry`/`Host.Transport`)** | Tách crash/render lifecycle và authority (ADR-002/003); kiểm thử headless `ConnectionLifecycle` tách rời khỏi `src/Desktop.Wpf/` UI tương lai | IPC framing, alpha/click-through trên cửa sổ riêng, đồng bộ DPI | **CHỌN THỬ CHÍNH (`P02-01..05` — headless + owned probes)**; UI WPF tương tác (`UW21-UI`/`UW22-UI`/`UW28`) giữ **`BLOCKED`** tới khi có owner `src/Desktop.Wpf/` |
| Embed Player bằng `-parentHWND` | Ít cửa sổ top-level hơn | WPF/Win32 airspace, cướp focus, crash lan sang Host (`S05`, `S10`) | **KHÔNG CHỌN** ở lượt đầu; chỉ giữ làm tham chiếu nếu separate process tắc |
| Unity as a Library / native plugin | Chia sẻ bề mặt trong cùng tiến trình | Phụ thuộc ABI/C++, tăng diện tấn công và phạm vi bản quyền (`S06`) | **LOẠI KHỎI PHẠM VI LƯỢT NÀY** |

- **Giấy phép (`S04`):** Theo quyết định người dùng (`r4`), đây là dự án cá nhân không kinh phí dùng **Unity Personal** và giai đoạn thử chỉ dùng **100% công cụ miễn phí (`$0`)**. Trước khi cài Editor/build thật, `P00-04`/`D-13` vẫn phải lập `docs/licenses/INVENTORY.md` và xác nhận thực tế điều kiện gói Personal (`<200.000 USD` Total Finances / non-Industry); signing/phát hành công khai ngoài bản thử đầu tiếp tục mở.

## 4. Authority và Secure IPC — đề xuất D-02/D-03

- **Phân định quyền:** Host C#/WPF giữ toàn quyền policy, `permissionGeneration`, `SafetyHold`, `layoutGeneration`, hàng đợi và bộ phát input (trong phép thử này nối vào **fake sink**; số lần gọi input/capture thật phải bằng `0` trong mọi case). Unity Renderer chỉ vẽ hình giả, nhận cử chỉ trên cửa sổ của chính nó và gửi event/intent đã gắn epoch.
- **Kênh truyền đề xuất:** **Windows Named Pipe cục bộ** (`NamedPipeServerStream` / `NamedPipeClientStream`, byte stream, **`PipeOptions.CurrentUserOnly | PipeOptions.Asynchronous`**, `S14`).
  - Host tạo server pipe với tên ngẫu nhiên theo phiên (`nyua-probe-<runId>`) và sinh `sessionNonce` 256-bit bằng CSPRNG, truyền qua kênh khởi tạo tiến trình con do Host mở (tuyệt đối **không** ghi nonce/token vào file log, command line public log hay diagnostic).
  - **Giới hạn đe dọa trung thực (`S14`):** `PipeOptions.CurrentUserOnly` chặn tài khoản khác và tiến trình khác mức elevation (ví dụ tiến trình thường không kết nối được pipe elevated và ngược lại), kết hợp xác thực handshake `role` + `protocolVersion` + `sessionId` + `sessionNonce` (constant-time compare). Tuy nhiên, `CurrentUserOnly` **không** chống được mã độc chạy cùng user và cùng mức elevation; tài liệu không tuyên bố sandbox chống malware cùng tài khoản.
- **Framing và phân tách JSON parser theo runtime (không polymorphic type, không `Assets/Plugins/` DLL ngoài whitelist):**
  - Khung nhị phân: **4-byte little-endian unsigned length prefix + UTF-8 JSON envelope**.
  - Kiểm tra `length` trước khi cấp phát buffer (`1 <= length <= 65536` bytes = `64 KiB`); nếu `length == 0` hoặc `> 65536` hoặc invalid UTF-8 thì đóng kết nối ngay, ghi lỗi đã lọc.
  - **Phía `.NET 10` Host (`Host.Transport.csproj`):** Dùng `System.Text.Json` sẵn có trong `.NET 10` BCL với `JsonDocumentOptions` / `JsonSerializerOptions { MaxDepth = 16, AllowTrailingCommas = false, CommentHandling = JsonCommentHandling.Disallow }`, từ chối unknown fields/kind/protocolVersion, số `NaN`/`Infinity` và tọa độ vượt biên vô lý; cấm `TypeNameHandling` hay command shell.
  - **Phía Unity `.NET Standard 2.1` (`Assets/Runtime/HostChannel.cs`):** Vì `.NET Standard 2.1` trong Unity **không** có sẵn `System.Text.Json` và `JsonUtility` không kiểm soát được depth/unknown fields, `HostChannel.cs` dùng **parser UTF-8 JSON đệ quy giới hạn hữu hạn tự viết (zero external DLL/NuGet)** thực thi đúng cùng hợp đồng (`MaxDepth = 16`, `<= 64 KiB`, reject unknown fields/duplicate keys/invalid UTF-8/`NaN`/`Infinity`); **không** thả NuGet DLL chưa khai báo vào `Assets/Plugins/` và **không** thêm dependency ngoài trừ khi `P00-04`/`P02-01` duyệt riêng. Tập test trong `RendererChannelTests` (`P02-04`) bắt buộc bao gồm kiểm tương đương roundtrip `.NET 10 System.Text.Json` ↔ Unity `HostChannel.cs` và vector âm cho: Unicode escapes & lone surrogates (`\uD800` không có cặp low surrogate), duplicate keys, numeric overflow/underflow, trailing tokens sau `}` và chuỗi lồng `depth > 16`.
  - Giới hạn vận hành đề xuất cho probe (chưa phải ngưỡng sản phẩm cố định): `pending queue <= 32`, `handshake timeout <= 10s`, `incomplete frame read timeout <= 2s`, `heartbeat interval = 1s` / **`3 misses` (`3s` mất peer)**.
- **Chống replay và phát lại trễ:** Mỗi frame mang `protocolVersion`, `messageId`, `sessionId`, `connectionEpoch`, `layoutGeneration`, `permissionGeneration`, `kind`, `payload`. Host lưu `HashSet`/cửa sổ `messageId` đã xử lý trong phiên để khử trùng lặp; mọi frame/ACK mang `sessionId`, `connectionEpoch`, `layoutGeneration` hoặc `permissionGeneration` cũ đều bị loại bỏ trước dispatch (`fake_sink_count` không tăng).

## 5. Hình học, chuột, alpha và focus

- **Alpha & click-through (`UW04`–`UW06`):** Dùng cửa sổ layered/DWM (`WS_EX_LAYERED` / `DwmExtendFrameIntoClientArea`, `S11`, `S18`) và hit-test theo vùng hình avatar/prop (`WM_NCHITTEST` hoặc region mask, `S12`). Vùng rỗng phải cho chuột đi tự nhiên xuống cửa sổ nền `WindowSurface.exe` (tiến trình khác, `UW06`: 20 click ngoài vùng hình → `WindowSurface` đếm 20, `OverlayProbe` đếm 0, **không** dùng `SendInput` chuyển tiếp giả). Nếu một chế độ fullscreen/DWM không chứng minh được xuyên process, đánh `BLOCKED / unsupported`, cấm bypass.
- **Fake Shift+drag probe (`UW08`–`UW09`):** Chỉ nằm trong `OverlayProbe.cs` khi tương tác trên cửa sổ riêng của probe, dùng fake refusal flag và fake counters (`throw=0`, `play=0`, `hurt=0`). Thả Shift hoặc mất focus/capture giữa chừng phải hủy drag trung tính. **Không** cài global keyboard hook; **không** hoàn tất `P20-03` hoặc nghiệm thu `NV11` sản phẩm.
- **Tọa độ đa màn hình & DPI (`UW10`–`UW12`):** Tách rõ screen physical px có dấu (hỗ trợ monitor bên trái origin âm, `S12`), WPF DIP và Unity local units. Mỗi `WM_DPICHANGED` (`S13`), di chuyển cửa sổ hoặc detach/reconnect monitor đều tăng `layoutGeneration` và vô hiệu mục tiêu cũ. Ngưỡng sai số đối chiếu fixture đề xuất `<= 1 physical px` ở điểm neo (chờ đo trong `P02-03`).
- **Focus (`UW07`, `UW28`):** Overlay (`CompanionRenderer.exe`) mặc định không cướp foreground của `WindowSurface.exe` khi idle/reconnect (`UW07`, chạy trong `P02-02`). Riêng yêu cầu điều hướng bàn phím `Tab`/`Shift+Tab`/`Enter`/`Space` trên hộp thoại Settings/Stop/Resume của WPF Host (`UW28`) giữ trạng thái **`BLOCKED / DEFERRED`** ngoài cụm `P02-01..05` tới khi có task sở hữu `src/Desktop.Wpf/`.

## 6. Vòng đời Fault / Restart và 5 trạng thái UI

| Trạng thái UI | Điều kiện vào | Hiển thị / nút khả dụng | Điều kiện rời |
|---|---|---|---|
| **Initial** | Chưa khởi tạo phiên renderer | Nhãn `Chưa chạy (dữ liệu giả)`, nút `[Bắt đầu phép thử]` (chỉ sau ủy quyền tương lai), `[Dừng phép thử]` luôn sẵn sàng | Bắt đầu phiên sau khi có ủy quyền thực thi |
| **Pending** | Đang mở `CompanionRenderer.exe`, chờ pipe handshake hoặc layout đầu tiên | Model state `Pending / Connecting`, deadline `<= 10s`; ở bản headless `P02-05` chưa có cửa sổ WPF | Handshake + layout epoch hợp lệ → sẵn sàng; hoặc timeout/lỗi → `Error` |
| **Partial** | Có kết nối nhưng thiếu layout epoch mới, thiếu case bắt buộc, thiếu phần cứng 2-monitor hoặc thiếu WPF Host UI (`P10`/`P40`) | `Chưa đủ bằng chứng — mọi tác động bị khóa`, nêu rõ hạng mục thiếu/BLOCKED | Bổ sung đủ bằng chứng đúng revision hoặc bấm Dừng |
| **Error (PausedAfterFault)** | Renderer crash/exit, mất 3 heartbeat (`3s`), frame lỗi/quá hạn, hoặc stale epoch | State `PausedAfterFault` + mã lỗi đã lọc; headless test (`P02-05`) kiểm chứng `Reconnect` → `Paused/Ask` → `ConfirmResume`/`KeepPaused`; nút WPF UI `[Kết nối lại]` / `[Cho tiếp tục sau lỗi]` / `[Giữ tạm dừng]` chờ `src/Desktop.Wpf/` | Lệnh `Reconnect` tạo `connectionEpoch` mới → vẫn giữ hàng đợi ở trạng thái **chờ xác nhận (`Paused/Ask`)** |
| **Success (EvidenceRecorded)** | Toàn bộ case trong phạm vi được chạy có đủ log/counter/exit code hợp lệ | Bảng kết quả từng case + danh sách case `NOT RUN` (thiếu phần cứng nếu có), **không** dán nhãn cả sản phẩm đạt | Đóng phiên hoặc đổi binary/config khiến kết quả hết hiệu lực |

### Quy tắc chuyển trạng thái vòng đời bắt buộc (D-02 / D-10 / CD01 / BH07 / DK03 / DK04 / BH08)

1. **Lỗi Renderer (`D-02`):** Khi pipe đứt, process thoát, frame sai schema hoặc miss 3 heartbeat liên tiếp (`3s`), Host chuyển tức thì sang `Error (PausedAfterFault)`, khóa fake sink (`0` hành động mới), hủy bước đang chạy và **giữ các việc chờ ở trạng thái tạm dừng**. **Không** tự khởi động lại renderer theo vòng lặp ngầm (crash-loop).
2. **Phục hồi Renderer (`D-02`):** Khi người dùng bấm `[Kết nối lại]` và phiên renderer mới handshake thành công với `connectionEpoch` tăng dần, Host **không tự chạy tiếp**. Host giữ nguyên UX phục hồi đã xác nhận (`[Cho tiếp tục sau lỗi]` / `[Giữ tạm dừng]`; mọi nút tùy chọn hủy hàng đợi mới đều bị hoãn chưa đưa vào sản phẩm). Chỉ khi người dùng bấm `[Cho tiếp tục sau lỗi]`, Host mới kiểm tra lại `permissionGeneration`, `SafetyHold` và `layoutGeneration` hiện hành; từ chối hoặc kiểm tra fail → giữ `Paused` và không dùng ACK/intent từ epoch trước lỗi.
3. **Host crash / khởi động lại (`D-10` / `CD01`):** Khi Host mở lại sau crash giả lập trên synthetic state fixture, mọi việc chưa hoàn thành chuyển về `Paused / Ask`, không tự chạy lại. Ghi chú residual D-10: crash giữa lúc ghi file trạng thái/atomic journal vẫn là mục mở cần thiết kế riêng trước production storage (`P50-01`), fixture `UW24` ghi rõ giới hạn nếu gặp trạng thái corrupt.
4. **Thoát có kiểm soát / đổi hồ sơ (`BH07`):** Cảnh báo và **hủy (terminal Cancelled)** các việc chưa hoàn thành; khởi động lại hoặc đổi lại hồ sơ không được hồi sinh việc đã hủy.
5. **Dừng khẩn cấp / Tắt quan sát / Ẩn nhân vật (`DK03` / `DK04` / `BH08`):** Hủy việc đang chạy, giữ việc chờ tạm dừng; **không** tự tiếp tục sau 60s; bật lại/hiện lại chỉ cho phép tiếp tục khi người dùng gọi `ResumeQueue` riêng và mọi điều kiện quyền/layout mới đều hợp lệ.

## 7. Tuyến biên dịch Unity, sở hữu `.csproj` và giải quyết deadlock

Mọi planning blocker trước đây đã được giải quyết trực tiếp trong canonical `docs/product/AI/backlog.json`:

1. **Đường dẫn script Unity hợp pháp (`S17`):** Toàn bộ script runtime Unity (`OverlayProbe.cs`, `HostChannel.cs` ở P02 và `SurfaceWorld.cs`, `BodyMotion.cs`, `Gestures.cs`, `PropWorld.cs`, `Placement.cs` ở P20) đã được chuyển từ `unity/CompanionRenderer/Runtime/` vào **`unity/CompanionRenderer/Assets/Runtime/`**.
2. **Tuyến biên dịch, Profile & Assembly Definition (`P02-01`):** `P02-01` sở hữu **`unity/CompanionRenderer/Assets/Runtime/CompanionRenderer.Runtime.asmdef`** (ghim platform `WindowsStandalone64`, `overrideReferences: false`). Mọi script đặt trong `Assets/Runtime/` tự động được biên dịch thành `CompanionRenderer.Runtime.dll` và đóng gói vào Player. Riêng `ApiCompatibilityLevel.NET_Standard_2_1`, `GraphicsDeviceType.Direct3D11` và `UniversalRenderPipelineAsset` được `Assets/Editor/ProbeBuild.cs` cấu hình/assert qua `PlayerSettings` & `GraphicsSettings` trước khi build Player (không phải do `.asmdef` thiết lập). Khi thực thi tương lai, mỗi chặng sửa `Assets/Runtime/` (`P02-02` thêm `OverlayProbe.cs`, `P02-04` thêm `HostChannel.cs`) đều bắt buộc rebuild Player ra thư mục riêng của chặng đó và có **cả** build log lẫn runtime marker trong Player log.
3. **Editor Build Entry (`P02-01`):** `P02-01` sở hữu **`unity/CompanionRenderer/Assets/Editor/ProbeBuild.cs`** (nằm trong special folder `Editor` nên loại khỏi Player build `S17`), cung cấp static `-executeMethod` `ProbeBuild.BuildWindowsProbe` (nhánh dương, thoát `0`, xuất Player vào `<TEMP>/p02-01-player/`) và `ProbeBuild.VerifyNegative` (nhánh âm cố ý lỗi, thoát khác `0`). Không trộn với `BootstrapBuild.cs` của `B00-02` tại `tests/bootstrap/desktop-body/UnityFixture/`.
4. **Phân định `.csproj` .NET 10 không xung đột giữa các nhánh song song:**
   - `P02-02` sở hữu `tests/Fixtures/WindowSurface.csproj` (`net10.0-windows`, WPF/Win32 test window độc lập) và phụ thuộc cả `B00-01` (`.NET` toolchain) lẫn `B00-02` (Unity toolchain).
   - `P02-03` sở hữu `src/Host/Geometry/Host.Geometry.csproj` và `tests/Integration/CoordinateMap.Tests.csproj` (`bootstrap_owner: B00-01`, đồng thời phụ thuộc `P02-02` và `B00-02`).
   - `P02-04` sở hữu `src/Host/Transport/Host.Transport.csproj` và `tests/Integration/RendererChannel.Tests.csproj` (`bootstrap_owner: B00-01`).
   - `P02-05` biên dịch `ConnectionLifecycle.cs` trong `Host.Transport.csproj` (của tổ tiên `P02-04`) và sở hữu `tests/Integration/ConnectionLifecycle.Tests.csproj` (`bootstrap_owner: B00-01`).
   - **Cô lập output theo từng lượt/task:** Chỉ dùng `--artifacts-path "<TEMP>/<task-run>/dotnet-artifacts"`, cùng root tuyệt đối trên mọi restore/build/test trong một dependency closure. SDK tự chia `bin/<ProjectName>/<pivot>` và `obj/<ProjectName>/`; không khai báo `BaseIntermediateOutputPath`, `MSBuildProjectExtensionsPath`, `BaseOutputPath` trong SDK-style `.csproj` để tránh MSB3539 và ghi ngược vào repo. Restore test project bao gồm ProjectReference; không restore Host riêng với root khác rồi test `--no-restore`. Các lượt song song dùng root riêng. Lưu hash `obj/<ProjectName>/project.assets.json`, evaluated TargetPath, build log và kiểm mọi output nằm dưới TEMP root trước launch. `EnableDefaultCompileItems=false` vẫn cần để chọn đúng file nguồn; không thay quy tắc output. Xem nguồn S20 và TEST_PLAN§5.

## 8. Whitelist tương lai theo canonical (chưa cấp quyền tạo)

<!-- CANONICAL-DEPENDENCIES-AND-FILES -->

| Task | Direct dependencies exact | Bootstrap owner | Proposed files exact — chưa cho tạo |
|---|---|---|---|
| `P00-01` | Không | — | `docs/product/AI/DECISIONS.md`<br>`docs/product/AI/requirements.json` |
| `R00-01` | `P00-01` | — | `docs/experiments/D-01.md` |
| `A00-01` | `R00-01` | — | `docs/decisions/D-01-resolution.md` |
| `R00-02` | `P00-01` | — | `docs/experiments/D-02.md` |
| `A00-02` | `R00-02` | — | `docs/decisions/D-02-resolution.md` |
| `R00-03` | `P00-01` | — | `docs/experiments/D-03.md` |
| `A00-03` | `R00-03` | — | `docs/decisions/D-03-resolution.md` |
| `R00-10` | `P00-01` | — | `docs/experiments/D-10.md` |
| `A00-10` | `R00-10` | — | `docs/decisions/D-10-resolution.md` |
| `R00-13` | `P00-01` | — | `docs/experiments/D-13.md` |
| `A00-13` | `R00-13` | — | `docs/decisions/D-13-resolution.md` |
| `P00-02` | `P00-01`, `A00-02`, `A00-03` | — | `contracts/README.md`<br>`docs/product/AI/INTERFACES.md` |
| `P00-04` | `P00-01`, `A00-13` | — | `docs/licenses/INVENTORY.md`<br>`docs/product/AI/DECISIONS.md` |
| `B00-01` | `P00-01` | — | `docs/experiments/bootstrap-companion.md`<br>`tests/bootstrap/companion/Bootstrap.Tests.csproj`<br>`tests/bootstrap/companion/BootstrapTests.cs`<br>`tools/verify/companion.ps1` |
| `B00-02` | `P00-01` | — | `docs/experiments/bootstrap-desktop-body.md`<br>`tests/bootstrap/desktop-body/UnityFixture/ProjectSettings/ProjectVersion.txt`<br>`tests/bootstrap/desktop-body/UnityFixture/Packages/manifest.json`<br>`tests/bootstrap/desktop-body/UnityFixture/Assets/Editor/BootstrapBuild.cs`<br>`tests/bootstrap/desktop-body/UnityFixture/Assets/Bootstrap.unity` |
| `P01-01` | `P00-01`, `B00-04` | `B00-04` | `labs/policy-native/RESULTS.md`<br>`tasks/todo.md` |
| `P02-01` | `P00-02`, `P00-04`, `B00-02`, `A00-01` | `B00-02` | `unity/CompanionRenderer/ProjectSettings/ProjectVersion.txt`<br>`unity/CompanionRenderer/Packages/manifest.json`<br>`unity/CompanionRenderer/Assets/Probe.unity`<br>`unity/CompanionRenderer/Assets/Runtime/CompanionRenderer.Runtime.asmdef`<br>`unity/CompanionRenderer/Assets/Editor/ProbeBuild.cs` |
| `P02-02` | `P02-01`, `B00-01`, `B00-02`, `A00-01` | `B00-02` | `unity/CompanionRenderer/Assets/Runtime/OverlayProbe.cs`<br>`tests/Fixtures/WindowSurface.csproj`<br>`tests/Fixtures/WindowSurface.cs`<br>`docs/experiments/overlay.md` |
| `P02-03` | `P02-02`, `B00-01`, `B00-02`, `A00-01` | `B00-01` | `src/Host/Geometry/Host.Geometry.csproj`<br>`src/Host/Geometry/CoordinateMap.cs`<br>`tests/Integration/CoordinateMap.Tests.csproj`<br>`tests/Integration/CoordinateMapTests.cs`<br>`docs/experiments/coordinates.md` |
| `P02-04` | `P02-01`, `P00-02`, `B00-01`, `A00-03` | `B00-01` | `src/Host/Transport/Host.Transport.csproj`<br>`src/Host/Transport/RendererChannel.cs`<br>`unity/CompanionRenderer/Assets/Runtime/HostChannel.cs`<br>`tests/Integration/RendererChannel.Tests.csproj`<br>`tests/Integration/RendererChannelTests.cs` |
| `P02-05` | `P02-04`, `P02-03`, `B00-01`, `A00-02`, `A00-10` | `B00-01` | `src/Host/Transport/ConnectionLifecycle.cs`<br>`tests/Integration/ConnectionLifecycle.Tests.csproj`<br>`tests/Integration/ConnectionLifecycleTests.cs`<br>`docs/experiments/disconnect.md` |

Các đường dẫn `P20-02` (`SurfaceWorld.cs`, `BodyMotion.cs`), `P20-03` (`Gestures.cs`), `P20-04` (`PropWorld.cs`) và `P20-05` (`Placement.cs`) cũng đã được đồng bộ sang `unity/CompanionRenderer/Assets/Runtime/` trong `backlog.json`.
File `.meta` do Unity sinh tự động và `Packages/packages-lock.json` chưa tự là source whitelist; mọi thư mục làm việc `Library/`, `Temp/`, `bin/`, `obj/`, build output và log phải cô lập hoặc không commit bừa trước khi rà scope.

## 9. Cổng quyết định hiện hành

- Tài liệu thiết kế/kế hoạch **`UW-DOC-2026-11-15-r4`** đã ghi nhận đủ 3 quyết định của người dùng (Unity Personal cho dự án cá nhân không kinh phí, giai đoạn thử 100% công cụ miễn phí, giữ nguyên yêu cầu `NV08` với kiểm chứng nhiều màn hình & toàn màn hình độc quyền đánh dấu `NOT RUN` chờ thiết bị thật) cùng các sửa lỗi cấu trúc/đường dẫn/sở hữu `.csproj`/JSON/profile từ rà soát trước đó, và **KHÔNG phải bằng chứng chạy thực**.
- Các gate `R00-*`/`A00-*`, `P00-02`, `P00-04`, `B00-01`, `B00-02`, `P02-01..05` đều giữ nguyên `DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION`.
- **Future build / install / fixture creation / runtime execution authorization: `NOT_OBTAINED`.**
- Toàn bộ 30 case `UW01–UW30` trong [TEST_PLAN](TEST_PLAN.md) đều ở trạng thái **`NOT RUN`** (trong đó kiểm chứng nhiều màn hình `UW11`/`UW12` và toàn màn hình độc quyền giữ **`NOT RUN` — chờ thiết bị thật** cho bản thử đầu theo `NV08`; phần WPF UI `UW07`/`UW21`/`UW22` và toàn bộ `UW28` giữ **`BLOCKED`** do thiếu owner `src/Desktop.Wpf/` trong cụm `P02`).

</details>
