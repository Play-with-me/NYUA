# Kế hoạch xây mẫu E02a — C# + WPF

Ngày: 2026-11-13. Trạng thái: **đã được người dùng duyệt, đã triển khai mẫu; xem todo.md và RESULTS.md cho phần đã kiểm chứng/còn mở**. [Đặc tả](../SPEC-policy.md) đã được người dùng duyệt. Đã cài SDK riêng workspace, tạo project và chạy kiểm thử. Các mô tả dự kiến bên dưới giữ làm kế hoạch gốc; lệnh/môi trường thực tế ở labs/policy-native/README.md.

## Phần dành cho người dùng

### Kết quả của đợt này

Một ứng dụng thử Windows cho bạn chọn tình huống, đổi quyền, xem phần dữ liệu giả được nhận và lý do bị chặn. Không đọc nội dung máy thật, không điều khiển chuột/phím thật và không cần mô hình AI hoặc hình nhân vật chính thức.

| Hiện tại | Khi hoàn thành đợt xây mẫu |
|---|---|
| Có đặc tả đã duyệt, chưa có chương trình | Có cửa sổ thử native mở được trên Windows |
| Chưa có kết quả thực thi quyền | Có kết quả A01–A16, các biến thể và B01–B06 với bằng chứng |
| Chưa kiểm chứng thu hồi quyền khi xử lý dở | Có điểm chờ để đổi quyền, hủy và kiểm tra dữ liệu cũ không được gửi |

```text
┌────────────────────────────────────────────────┐
│ Mẫu kiểm tra quyền — dữ liệu giả               │
│ Tình huống [Thu hồi quyền giữa chừng        ▼] │
│ Mong đợi: không gửi nội dung đang chờ          │
│                                                │
│ Nguồn A: [✓ Đọc] [□ Điều khiển]                │
│ Trạng thái: Chờ bạn đổi quyền                  │
│ [Thu hồi quyền] [Tiếp tục kiểm tra] [Hủy lượt]  │
│                                                │
│ Bộ nhận thực tế: trống                         │
│ Kết quả: chưa chạy / đạt / chưa đạt            │
│ [Thử đọc lại] [Tắt quan sát] [Đặt lại mẫu]       │
└────────────────────────────────────────────────┘
```

Bạn mở mẫu → chọn tình huống → xem điều mong đợi → chạy → đổi quyền tại điểm chờ nếu có → xem kết quả thật → đặt lại hoặc chạy tình huống tiếp. Nếu có lỗi, giữ trạng thái chưa đạt và sửa nguyên nhân.

### Công cụ và chi phí

- **C# + WPF:** logic và cửa sổ thử Windows. XAML mô tả giao diện native, không phải HTML/CSS hoặc trình duyệt nhúng.
- **.NET 10 SDK:** công cụ xây/chạy dự kiến; dùng nhánh LTS còn hỗ trợ, xác minh và ghi đúng phiên bản SDK khi cài. Chưa thấy dotnet trong PATH hoặc hai thư mục cài chuẩn đã kiểm tra; không khẳng định đã quét mọi chỗ trên máy.
- **MSTest:** kiểm tra tự động logic và đường giao dữ liệu. Gói cần được tải lần chuẩn bị; ghi phiên bản thực, không dùng số phiên bản ví dụ từ tài liệu làm mặc định.
- **Git:** đã có trên máy, thư mục này chưa có kho Git. Thiết lập lưu mốc trước sửa code, không tự đẩy lên mạng.
- Không cần mua công cụ, cài Unity hoặc tải model để thực hiện E02a. Không bắt buộc cài cả Visual Studio để dùng các lệnh SDK. Nếu phát sinh khoản phí, phải hỏi trước.

Tải SDK/gói kiểm thử cần mạng trong lúc chuẩn bị. Khi chạy phép thử, ứng dụng không gọi mạng và không tải tài nguyên ngoài. Chưa cài đặt hoặc tải gì trong lượt lập kế hoạch.

### Phần sẽ làm sau E02a

Hướng sản phẩm là Unity cho nhân vật, C# + WPF cho ứng dụng và AI local cho hiểu ngữ cảnh. E02a chỉ làm phần quyền C# và giao diện thử WPF. Phải đặc tả và thử riêng kết nối Unity/C#, cửa sổ trong suốt, nhận chuột đúng vùng, mất kết nối và hiệu năng trước khi chốt triển khai toàn sản phẩm. Chưa coi việc nhúng Unity hay chạy hai tiến trình là quyết định đã duyệt.

<details>
<summary>Phương án kỹ thuật và phạm vi thực thi</summary>

## Cơ sở và quyết định

- Native là lựa chọn người dùng đã nêu; web/Node chỉ là đề xuất cũ chưa được duyệt, không tạo project web.
- Core không phụ thuộc WPF hoặc Unity. WPF chỉ hiển thị trạng thái và gửi ý định; không tự tính một bản quyền khác trong UI.
- Dùng thư viện chuẩn .NET cho core, MSTest cho test; chưa thêm thư viện MVVM, DI, logging hoặc IPC khi chưa cần. UI dùng binding/ViewModel mỏng, không đặt logic cấp quyền trong event handler.
- Chọn net10.0 cho core/test và net10.0-windows với UseWPF cho app thử. SDK chính xác sẽ ghim trong global.json của mẫu sau khi cài/xác nhận. Đây là cấu hình mẫu đề xuất; không mặc định Unity có thể nạp trực tiếp cùng assembly hoặc dùng cùng phiên bản .NET.
- Không có database, telemetry, cloud, localStorage hoặc kho dữ liệu lâu dài. Nội dung thử tồn tại trong bộ nhớ. Báo cáo chỉ ghi khi người dùng chọn xuất; log test trên đĩa chỉ dùng dấu giả và chẩn đoán đã lọc.
- Mọi cập nhật trạng thái và lần giao dữ liệu cuối được tuần tự hóa trong coordinator. Kiểm tra revision cuối và gọi bộ nhận đồng bộ, không có await ở khoảng giữa. WPF Dispatcher không được coi là giải pháp thu hồi quyền giữa các tiến trình của app tương lai.

## Cấu trúc dự kiến

```text
labs/policy-native/
  global.json
  PolicyLab.Core/
    PolicyLab.Core.csproj
    Contracts.cs
    PolicyEvaluator.cs
    ReadCoordinator.cs
  PolicyLab.Scenarios/
    PolicyLab.Scenarios.csproj
    ScenarioCatalog.cs
    ScenarioRunner.cs
  PolicyLab.App/
    PolicyLab.App.csproj
    App.xaml + App.xaml.cs
    MainWindow.xaml + MainWindow.xaml.cs
    LabViewModel.cs
  PolicyLab.Tests/
    PolicyLab.Tests.csproj
    PolicyEvaluatorTests.cs
    ReadCoordinatorTests.cs
    ScenarioTests.cs
  README.md
  RESULTS.md
```

Scenarios phụ thuộc Core; App phụ thuộc Core/Scenarios; Tests phụ thuộc Core/Scenarios. Không vòng và không tham chiếu Unity. Không cố tạo một solution toàn sản phẩm khi mới làm mẫu.

## Phạm vi file

- Triển khai: chỉ labs/policy-native/**, cấu hình Git tại workspace phù hợp, .gitignore nếu cần, tasks/plan.md, tasks/todo.md, SPEC-policy.md phần công cụ/trạng thái, README.md, CONSTRAINTS.md trạng thái kiểm tra và .agents/PROJECT_MEMORY.md.
- Mẫu đọc DESIGN.md để giữ màu/chữ/khoảng cách, chuyển các nguyên tắc sang XAML. Không sửa DESIGN.md chỉ để vừa implementation.
- Giữ nguyên permissions.html và JSON quyền gốc; không sửa yêu cầu người dùng khi gặp test lỗi.
- Graphify chưa có, code app chưa tồn tại; chưa có God Node/call edge trích xuất. Core dự kiến nhạy cảm với mọi luồng quyền, phải rà mọi caller khi thay đổi.

## Trạng thái UI phải bao phủ

| Trạng thái | Hiển thị và hành vi |
|---|---|
| Ban đầu | Dữ liệu giả, quyền tắt, bộ nhận trống; chưa chạy khác đạt |
| Đang kiểm tra | Thể hiện đang xử lý, có hủy; không đứng hình UI |
| Đang dở | Điểm chờ đổi quyền có nhãn; Tiếp tục không tự gỡ chốt an toàn |
| Bị chặn/hủy/lỗi | Phân biệt rõ lý do; thử lại đúng loại; lỗi runtime không thành chặn đúng |
| Hoàn tất | Hiện dữ liệu thực bộ nhận nhận được và kết quả so kỳ vọng độc lập |

Layout Grid có hàng hành động riêng, nội dung cuộn và co được, chuỗi dài xuống dòng. Nút có nhãn cụ thể, focus/Tab/Space/Enter dùng được, không dùng màu làm dấu hiệu duy nhất. Không sao chép các class CSS vào XAML. Không 3D hoặc animation nặng.

## Lệnh dự kiến — chưa thực thi, chỉ hợp lệ sau khi tạo đúng project

Chạy từ C:\Pet:

```powershell
dotnet --info
dotnet restore .\labs\policy-native\PolicyLab.App\PolicyLab.App.csproj
dotnet restore .\labs\policy-native\PolicyLab.Tests\PolicyLab.Tests.csproj
dotnet build .\labs\policy-native\PolicyLab.App\PolicyLab.App.csproj --configuration Debug --no-restore
dotnet test .\labs\policy-native\PolicyLab.Tests\PolicyLab.Tests.csproj --configuration Debug --no-restore
dotnet run --project .\labs\policy-native\PolicyLab.App\PolicyLab.App.csproj --configuration Debug --no-build
```

Khi tạo template, kiểm tra MSTest runner thực tế và ghi lệnh đúng với phiên bản được dùng. Nếu mẫu dùng runner cần cấu hình bổ sung, sửa lệnh/kế hoạch trước khi kết luận; không đổi framework chỉ để báo đạt. Build/test có thời hạn giám sát, không chạy benchmark nền vô hạn. Chưa chọn ngưỡng coverage hoặc ngân sách thời gian kiểm tra thay người dùng.

## Kiểm chứng và mốc dừng

- Danh sách việc và checkpoint duy nhất: [todo.md](todo.md). Hiện mọi việc thực thi đều chưa bắt đầu.
- Test kỳ vọng không gọi hàm đang test để tính expected. Kiểm tra dữ liệu tới receiver spy và diagnostic thật, không chỉ outcome UI.
- Test thất bại trước sửa logic tương ứng; giữ kiểm tra có ý nghĩa cho quyền, revision, retry và gọi trùng. Không dùng test chỉ kiểm tra nhãn/caseId như bằng chứng nghiệp vụ.
- Rà runtime bằng công cụ native được hỗ trợ. Trước dùng công cụ đọc skill computer-use. Nếu chưa quan sát được runtime/network, giữ chưa kiểm chứng; build thành công không thay kiểm tra UI.
- Kiểm tra mã/runtime không có đường mạng và không truy cập dữ liệu hệ thống; nếu cần công cụ quan sát thêm phải đánh giá phạm vi trước. Không tắt kết nối toàn máy người dùng để chứng minh offline.
- Checkpoint kỹ thuật sau T02 và T04; checkpoint dùng thử sau T06. Các kiểm tra kỹ thuật trong phạm vi đã duyệt tự thực hiện, không hỏi duyệt từng dòng code.
- Khi logic an toàn không đạt, dừng mở rộng luồng đó, giữ lỗi và sửa. Không âm thầm bỏ A/B hoặc thay expected.

## Rủi ro

| Rủi ro | Cách xử lý |
|---|---|
| SDK chưa có hoặc cài đặt cần tương tác quyền hệ thống | Xác nhận nguồn/cách cài chính thức, ưu tiên phương án hạn chế thay đổi máy; báo rõ nếu cần người dùng thao tác. Không cài trong lượt Plan |
| Restore phụ thuộc không được hoặc phiên bản runner khác ví dụ | Ghi lỗi và cấu hình thật; không báo test đã chạy |
| UI treo hoặc callback tới muộn | Coordinator có điểm chờ/hủy rõ, revision và attemptId, test receiver count |
| Mẫu giả tạo cảm giác an toàn sai | Báo cáo nêu rõ chưa capture/OCR/ẩn danh thật; E02 nguồn thật còn riêng |
| Unity và AI chiếm tài nguyên/khác môi trường .NET | Phép thử tích hợp và E04/E05 riêng; không hứa tái dùng assembly hoặc phản ứng dưới 1 giây |

## Nguồn đã khảo sát

- [WPF overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/overview/): C#/XAML và framework UI Windows.
- [.NET support policy](https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core): chọn nhánh .NET 10 LTS còn hỗ trợ; xác minh patch/SDK tại lúc cài.
- [MSTest C# tutorial](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-csharp-with-mstest): cấu trúc class library/test và dotnet test; tài liệu nhấn mạnh version template phụ thuộc SDK.

Các nguồn chứng minh công cụ có khả năng tương ứng, không phải bằng chứng mẫu E02a đã chạy.

</details>
