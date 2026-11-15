# Kết quả demo E02a trên máy hiện tại

Ngày 2026-11-14, Windows build26300 x64, SDK10.0.404/runtime10.0.15. Dùng source E02a hiện có, không sửa code. SDK riêng data/tools/nyua-dotnet; chữ ký dotnet.exe Valid, không đổi PATH toàn máy.

Đã chạy thật: MSTest Release53/53 PASS, failed0, skipped0, xác nhận từ TRX mới. Publish win-x64 self-contained thành công. Cửa sổ native mở được; nút Chạy toàn bộ kiểm chứng báo35/35. A05 qua UI: chờ thì receiver trống, Tiếp tục nhận safe: SAFE-A, receiver1. Tắt quan sát xóa receiver, không tự chạy lại, geometry còn riêng. Dòng kết quả cũ là lịch sử, không đại diện trạng thái quan sát hiện tại. Nút Start/Retry/RunAll vô hiệu khi chờ, Continue/Cancel bật khi chờ. Tab chuyển focus vào ô nhận read-only. NuGet Tests audit include-transitive không phát hiện vulnerable packages theo api.nuget.org tại lần chạy.

Còn mở: resize tối thiểu760x600 chưa xác nhận qua công cụ; full keyboard/focus/screen reader chưa kiểm đủ. Chưa có phản hồi dùng thử bản mới từ người dùng, C3 còn mở. Không chứng minh capture/clipboard/input thật, Unity/AI/IPC hoặc phiên8h. Không thay checkbox nghiệm thu người dùng. Không push/PR/công bố.

Lệnh đã dùng từ labs/policy-native, dotnet tại C:/Users/phamp/.ao/data/tools/nyua-dotnet/dotnet.exe:
- test ./PolicyLab.Tests/PolicyLab.Tests.csproj --configuration Release --artifacts-path TEMP/nyua-e02a-build --results-directory TEMP/nyua-e02a-results --logger trx;LogFileName=e02a-current-machine.trx
- publish ./PolicyLab.App/PolicyLab.App.csproj --configuration Release --runtime win-x64 --self-contained true --artifacts-path TEMP/nyua-e02a-build --output TEMP/nyua-e02a-demo/app
- list ./PolicyLab.Tests/PolicyLab.Tests.csproj package --vulnerable --include-transitive
TEMP trong mô tả trên là thư mục tạm của Windows, đã dùng biến môi trường PowerShell khi chạy. TRX nguyên gốc giữ ở TEMP/nyua-e02a-results, không đóng gói metadata máy.


## Cập nhật nghiệm thu người dùng — 2026-11-15

Người dùng báo thu nhỏ cửa sổ “Đã ổn rồi”; về bàn phím: “Có nhìn rõ và không có chỗ nào bị kẹt, có thể đóng nghiệm thu E02a rồi”. Đã chấp nhận/đóng nghiệm thu trải nghiệm demo C3. Kết quả kỹ thuật phía trên là lịch sử đã chạy, không chạy lại trong lượt này. Screen reader/full activation/mọi DPI và số đo resize độc lập chưa được kiểm đầy đủ; không đánh dấu PASS thay bằng chứng. Không nghiệm thu hoặc triển khai sản phẩm thật. Chi tiết: tasks/E02a-USER-ACCEPTANCE.md.
