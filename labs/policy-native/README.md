# Mẫu native kiểm tra quyền — E02a

Đây là ứng dụng thử C# + WPF trên **dữ liệu giả**, không đọc màn hình/clipboard, không điều khiển máy, không có Unity hoặc AI. [Đặc tả](../../SPEC-policy.md) và [kế hoạch](../../tasks/plan.md) giữ nguyên phạm vi.

## Mở để dùng thử

Nhấp đúp [PolicyLab.App.exe](artifacts/app/PolicyLab.App.exe). Đây là bản self-contained win-x64 đã build tại máy này, không cần cài .NET toàn máy. Giữ nguyên các file đi cùng trong thư mục artifacts/app; chưa phải bộ cài hoặc bản phát hành có chữ ký.

1. Bấm **Chạy toàn bộ kiểm chứng**: mong đợi 35/35 trường hợp giả đạt kiểm chứng.
2. Chọn **A10-revoke — Thu hồi quyền lúc chờ**. Bấm **Kiểm tra tình huống** → **Áp dụng thay đổi mẫu** → **Tiếp tục kiểm tra**. Mong đợi lượt đã hủy và bộ nhận trống.
3. Chọn **A09 — Không chắc vùng an toàn**, chạy rồi bấm **Thử đọc lại**: vẫn chặn. Bấm **Sửa vùng giả thành an toàn**: chưa tự đọc. Bấm **Thử đọc lại** → **Tiếp tục kiểm tra**: chỉ nhận SAFE-A.

Thay đổi tự do bằng checkbox/nút sẽ được ghi là **thử tùy chỉnh**, không chấm theo kỳ vọng gốc. Đặt lại tình huống để quay về kịch bản chuẩn. A14 mô tả sẵn một lần thử lại sau sửa vùng; khi chạy kịch bản gốc, nó thực hiện lượt thử lại đã khai báo.

**Đạt kiểm chứng** nghĩa là kết quả khớp với tình huống, kể cả tình huống phải chặn/hủy. B05 cố ý làm bộ nhận lỗi: test đạt nếu lỗi được báo ERROR và không giữ dữ liệu; không có nghĩa thao tác đó thành công.

Đóng bằng nút X. Mẫu không lưu trạng thái, quyền hay dữ liệu thử qua lần mở. Không có chức năng cấp quyền Windows thật. Nếu chữ hoặc nút bị che khi đổi kích thước, báo kích thước cửa sổ và thao tác; đừng xem build thành công là bằng chứng mọi kích thước đều ổn.

## Công cụ thực tế

- SDK **10.0.404** ở `C:\Pet\.tools\dotnet`, runtime **10.0.15**. SDK cài riêng cho workspace từ script chính thức Microsoft, không đổi PATH/registry toàn máy. Chữ ký dotnet.exe được kiểm tra là Valid. Script phù hợp môi trường công cụ cục bộ; môi trường phát triển lâu dài có thể chuyển sang bộ cài chính thức sau.
- global.json trong thư mục mẫu ghim SDK; chạy CLI từ thư mục này để SDK resolver đọc đúng file.
- Core/Scenarios: net10.0; App: net10.0-windows; nullable và warnings-as-errors bật.
- Tests: Microsoft.NET.Test.Sdk 17.14.1; MSTest.TestAdapter/MSTest.TestFramework 3.8.3, đã restore thực tế từ NuGet. Không lấy phiên bản mới nhất theo suy đoán.
- Git cục bộ đã có mốc trước code. Không có remote/push được tạo trong đợt này.

## Lệnh đã dùng

Trong PowerShell:

```powershell
Set-Location C:\Pet\labs\policy-native
$env:DOTNET_CLI_TELEMETRY_OPTOUT = '1'
& C:\Pet\.tools\dotnet\dotnet.exe test .\PolicyLab.Tests\PolicyLab.Tests.csproj --configuration Release --logger 'trx;LogFileName=policy-lab.trx'
& C:\Pet\.tools\dotnet\dotnet.exe publish .\PolicyLab.App\PolicyLab.App.csproj --configuration Release --runtime win-x64 --self-contained true --output .\artifacts\app
& C:\Pet\.tools\dotnet\dotnet.exe list .\PolicyLab.Tests\PolicyLab.Tests.csproj package --vulnerable --include-transitive
```

Các lần restore/publish/audit cần Internet để tải SDK/package/advisory khi chưa có cache. **Ứng dụng thử khi chạy không có đường gọi mạng trong mã nguồn của mẫu**. Không đồng nhất mạng của công cụ chuẩn bị với việc gửi dữ liệu nguồn.

File TRX thực tế ở PolicyLab.Tests/TestResults/policy-lab.trx, bỏ khỏi Git vì có thông tin môi trường máy. [RESULTS.md](RESULTS.md) là tóm tắt kết quả, không chứa payload cấm hoặc tên tài khoản máy.

## Giới hạn đã biết

- Chỉ một luồng owner được tuần tự hóa. Chưa có IPC, thu hồi quyền giữa tiến trình hoặc nhận dạng nguồn Windows thật.
- Vùng safe/sensitive/unknown, riêng tư và tọa độ do fixture xác định; không phải bộ phát hiện mật khẩu/OTP/thẻ hoặc bộ lọc ảnh thật. Các tọa độ vùng nhỏ là giả lập, không phải tọa độ screenshot.
- Chưa xác minh toàn bộ bàn phím/screen reader, kích thước tối thiểu, DPI hoặc nhiều màn hình. Các kiểm tra runtime đại diện không thay bộ kiểm tra UI đầy đủ.
- Chưa có nghiệm thu dùng thử từ người dùng; không ghi E02a đã nghiệm thu toàn bộ hoặc sản phẩm sẵn sàng phát hành.
