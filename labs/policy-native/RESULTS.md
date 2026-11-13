# Kết quả E02a native — dữ liệu giả

Ngày: 2026-11-13. **Bản mẫu đã triển khai và có kiểm chứng kỹ thuật; chờ người dùng dùng thử.** Không phải chứng nhận bảo vệ dữ liệu trên mọi ứng dụng Windows.

## Kết quả tự động

- MSTest Release: 53/53 đạt, failed=0, không bỏ qua test.
- Danh mục A01–A16 và B01–B06 có 35 trường hợp/biến thể. Kỳ vọng khai báo độc lập; receiver spy kiểm số lần gọi và nội dung safe.
- TRX gốc: PolicyLab.Tests/TestResults/policy-lab.trx (local, ignored). Không sao chép tên tài khoản/máy từ TRX vào bản tóm tắt.
- Build Debug trước UI: 0 warnings/0 errors. Publish Release win-x64 self-contained thành công sau thay đổi cuối.
- SDK 10.0.404, runtime 10.0.15, Windows 11 build 26300 x64. Không benchmark AI/Unity hoặc phiên 8 giờ.

| Trường hợp | Mong đợi | Thực tế | Lần gọi receiver | Test |
|---|---|---|---|---|
| A01 | Block/AppReadDenied | Block/AppReadDenied | 0 | PASS |
| A02 | Allow/Allowed | Allow/Allowed | 1 | PASS |
| A03 | Block/SiteReadDenied | Block/SiteReadDenied | 0 | PASS |
| A04 | Block/AppReadDenied | Block/AppReadDenied | 0 | PASS |
| A05 | Allow/Allowed | Allow/Allowed | 1 | PASS |
| A06-background | Block/SourceNotVisible | Block/SourceNotVisible | 0 | PASS |
| A06-hidden | Block/SourceNotVisible | Block/SourceNotVisible | 0 | PASS |
| A06-minimized | Block/SourceNotVisible | Block/SourceNotVisible | 0 | PASS |
| A07 | Block/PrivateSource | Block/PrivateSource | 0 | PASS |
| A08-card | Allow/Allowed | Allow/Allowed | 1 | PASS |
| A08-otp | Allow/Allowed | Allow/Allowed | 1 | PASS |
| A08-password | Allow/Allowed | Allow/Allowed | 1 | PASS |
| A09 | Block/SafetyUnknown | Block/SafetyUnknown | 0 | PASS |
| A10-revoke | Cancel/StaleAttempt | Cancel/StaleAttempt | 0 | PASS |
| A10-source | Cancel/StaleAttempt | Cancel/StaleAttempt | 0 | PASS |
| A11-hide | Cancel/StaleAttempt | Cancel/StaleAttempt | 0 | PASS |
| A11-off | Cancel/StaleAttempt | Cancel/StaleAttempt | 0 | PASS |
| A12 | Block/SafetyUnknown | Block/SafetyUnknown | 0 | PASS |
| A13 | Block/RetryRequired | Block/RetryRequired | 0 | PASS |
| A14 | Allow/Allowed | Allow/Allowed | 1 | PASS |
| A15 | Block/ObservationOff | Block/ObservationOff | 0 | PASS |
| A16 | Block/ReadRequiredForControl | Block/ReadRequiredForControl | 0 | PASS |
| B01-app | Block/AppReadDenied | Block/AppReadDenied | 0 | PASS |
| B01-geometry | Block/InvalidInput | Block/InvalidInput | 0 | PASS |
| B01-id | Block/InvalidInput | Block/InvalidInput | 0 | PASS |
| B01-kind | Block/InvalidInput | Block/InvalidInput | 0 | PASS |
| B01-privacy | Block/PrivacyUnknown | Block/PrivacyUnknown | 0 | PASS |
| B01-region | Block/InvalidInput | Block/InvalidInput | 0 | PASS |
| B02 | Allow/Allowed | Allow/Allowed | 1 | PASS |
| B03-cancel | Cancel/UserCancelled | Cancel/UserCancelled | 0 | PASS |
| B03-repeat | Allow/Allowed | Allow/Allowed | 1 | PASS |
| B04-observation | Cancel/StaleAttempt | Cancel/StaleAttempt | 0 | PASS |
| B04-permission | Cancel/StaleAttempt | Cancel/StaleAttempt | 0 | PASS |
| B05 | Error/ReceiverError | Error/ReceiverError | 1 | PASS |
| B06 | Block/NoSafeRegions | Block/NoSafeRegions | 0 | PASS |

B05 cố ý phát sinh lỗi bộ nhận: assertion đạt vì lỗi được báo ERROR và nội dung không bị giữ/log. ERROR vẫn là thao tác không thành công, không được đổi thành Block/Allow để chấm đạt.

## Đã quan sát trong cửa sổ native

- Khởi động bản Debug rồi bản self-contained; hiện nhãn dữ liệu giả và mặc định chưa cấp quyền.
- Chạy toàn bộ trong UI: 35/35 trường hợp giả đạt kiểm chứng.
- A01: bị chặn, receiver trống. A05: chờ rồi hoàn tất chỉ nhận SAFE-A.
- Tắt quan sát sau giao dữ liệu: đầu vào cũ bị xóa, hình học vẫn hiển thị riêng.
- A09: thử lại khi chưa sửa vẫn chặn; sửa vùng chưa tự đọc; bấm thử lại và hoàn tất mới nhận SAFE-A.
- A10-revoke: áp dụng thu hồi quyền tại điểm chờ rồi hoàn tất trả Cancel/StaleAttempt, receiver=0.
- Đã sửa tương phản chữ nút chính và tên accessibility của item; đã quan sát lại cửa sổ sau sửa. Phần thử tùy chỉnh không được chấm theo kỳ vọng kịch bản gốc.

Các luồng đại diện trên đã quan sát ở bản build trước khi đóng gói; bản self-contained cuối đã kiểm tra khởi động. Lượt 35/35 trong UI được ghi trước thay đổi cuối chỉ về dòng tổng kết; lần chạy bộ trường hợp trên bản cuối nhường lại vì phát hiện người dùng đang thao tác. Chưa gọi đây là E2E tự động đầy đủ mọi nút.

## Rà mã và phụ thuộc

- Rà ranh giới: Core không phụ thuộc UI; App/Tests dùng cùng Core và Scenarios. Metadata không mang payload; vùng safe được chọn trước receiver; revision và attemptId vô hiệu callback cũ; lỗi receiver không lộ exception text.
- A02 có coordinator/receiver riêng cho nguồn B cấm, kiểm không có dữ liệu/call phát sinh. Đây vẫn là nguồn giả.
- Mã C# sở hữu của Core/Scenarios/App không dùng System.Net/HttpClient/Socket, Clipboard, DllImport, Microsoft.Win32 hoặc API đọc tập tin. Định nghĩa fixture chứa dấu bí mật giả để thử lọc, không phải bí mật thật.
- Audit NuGet test project gồm phụ thuộc gián tiếp: không phát hiện vulnerable package trong nguồn advisory hiện có tại lần chạy. App/Core/Scenarios không thêm gói bên thứ ba ngoài framework.
- Snapshot tiến trình khi chạy: TCP=0, UDP=0. Đây là quan sát tại một thời điểm và rà mã, không phải giám sát gói mạng liên tục hoặc chứng minh mọi hành vi framework/OS.
- JSON quyền gốc so với bản Downloads vẫn cùng hash. Chưa cài Unity/model hoặc tác động dữ liệu người dùng.
- Rà do cùng AI thực hiện, không phải rà độc lập bởi người thứ hai.

## Chưa kiểm chứng / chưa nghiệm thu

- Người dùng chưa dùng thử; checkpoint C3 còn mở.
- Resize xuống kích thước tối thiểu và toàn bộ điều hướng bàn phím/screen reader chưa có bằng chứng đủ. Cố thử kéo biên/Tab qua công cụ không xác nhận được kết quả, không ghi đạt.
- Chưa kiểm nhiều DPI/màn hình, clipboard, capture/OCR, private browsing thật, video nhúng, Unity/IPC, AI local hoặc phiên 8 giờ.
- Chưa có audit bảo mật production, cơ chế cập nhật/backup hoặc bộ cài ký số.

## Nhận dạng bản chạy

- File: artifacts/app/PolicyLab.App.exe
- SHA-256 của apphost: `ab06d718d8e6d0514234408d6b1cce5b69056fa52889a34974a5f0a7084f6bc6`. Apphost đi cùng DLL/runtime; hash này riêng lẻ không xác nhận toàn bộ gói.
