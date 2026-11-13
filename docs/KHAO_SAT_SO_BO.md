# Khảo sát sơ bộ — trình duyệt và giao diện Windows

Ngày: 2026-11-13. Chỉ đọc tài liệu chính thức; chưa viết code, cài phần mềm hoặc đo khả năng thực tế. Chưa chọn stack hoặc kết luận phương án thắng.

## Kết quả có nguồn

| Nguồn | Điều tài liệu hỗ trợ | Chưa được suy ra |
|---|---|---|
| [Chrome content scripts](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts) | Tiện ích có thể đọc thông tin trang qua DOM; môi trường script được tách với trang; truy cập cần quyền tương ứng | Không tự bảo đảm chỉ đọc phần nhìn thấy, lọc bí mật, nhận diện cảm xúc hoặc thao tác đúng |
| [Chrome declare permissions](https://developer.chrome.com/docs/extensions/develop/concepts/declare-permissions) | Có quyền tùy chọn và quyền website cấp khi dùng | Không đồng nghĩa hai ô Đọc/Điều khiển của sản phẩm tự được trình duyệt thực thi; vẫn cần thiết kế và kiểm chứng |
| [Edge native messaging](https://learn.microsoft.com/en-us/microsoft-edge/extensions/developer-guide/native-messaging) | Tiện ích trao đổi với app Win32 đã cài qua native messaging, cần permission/host tương ứng | Không phải AI cloud; cũng không phải quyền tự cài tiện ích/host cho người dùng hoặc cam kết hoạt động mọi website |
| [Microsoft UI Automation overview](https://learn.microsoft.com/en-us/windows/win32/winauto/uiauto-uiautomationoverview) | Windows có cơ chế truy cập phần tử giao diện; framework dựa vào provider và có giới hạn giao tiếp | Không được kết luận mọi app/nút đều được hỗ trợ; cần thử và kiểm tra ranh giới quyền |

## Hướng khảo sát tiếp — chưa chọn kiến trúc

- So sánh đường tiện ích + ứng dụng desktop với đường Windows UI Automation/OCR cho thông tin website và nút.
- Chỉ dùng thông tin nguồn được phép; khả năng đọc DOM không cấp quyền đọc nội dung nền hoặc ẩn.
- Điều khiển thật vẫn phải đi theo yêu cầu nhân vật tới nút rồi thao tác chuột/phím; không tự thay bằng script click chỉ vì tiện ích có thể sửa DOM.
- Chưa kiểm chứng tab riêng tư, nội dung nhúng khác nguồn, phân vùng nhạy cảm hoặc tương quan tọa độ/DPI.
- Người dùng đã chấp nhận bước cài tiện ích khi bật khả năng website; sinh hoạt cơ bản không bắt buộc có tiện ích. Đây là lựa chọn trải nghiệm, chưa phải quyết định API/framework hoặc quyền tự cài.

Không có phụ thuộc/runtime/model cụ thể được chọn từ lần khảo sát này. Tiếp tục theo K01–K09 trong DIEM_CHUA_CHAC.md, ghi riêng điều đã đọc và điều chỉ phép thử mới biết.

## K04 — lịch sử clipboard: khảo sát tài liệu ban đầu

- [GetHistoryItemsAsync](https://learn.microsoft.com/en-us/uwp/api/windows.applicationmodel.datatransfer.clipboard.gethistoryitemsasync) mô tả lấy danh sách mục lịch sử.
- [ClipboardHistoryItemsResultStatus](https://learn.microsoft.com/en-us/uwp/api/windows.applicationmodel.datatransfer.clipboardhistoryitemsresultstatus) mô tả Success, AccessDenied, ClipboardHistoryDisabled. Không được dùng dữ liệu khi thao tác bị từ chối.
- [IsHistoryEnabled](https://learn.microsoft.com/en-us/uwp/api/windows.applicationmodel.datatransfer.clipboard.ishistoryenabled) kiểm tra lịch sử có bật không; không phải quyền tự bật thiết lập hệ thống.
- Các trang API trên chưa chứng minh cơ chế nhận biết chính xác bảng Windows + V mở/đóng hoặc khả năng gọi API theo đúng điều kiện ứng dụng của sản phẩm. Không khẳng định đã giải quyết foreground/background bằng tài liệu này.
- Chưa gọi API, đọc clipboard thật hoặc đổi thiết lập người dùng. Cần E02 với dữ liệu giả, thử đóng bảng trong lúc xử lý và bảo đảm không tạo ký ức lâu dài.

## Nhận diện ô mật khẩu — giới hạn bằng chứng

- [Microsoft IsPasswordProperty](https://learn.microsoft.com/en-us/dotnet/api/system.windows.automation.automationelement.ispasswordproperty) cung cấp thuộc tính Boolean về nội dung được bảo vệ của phần tử UI Automation.
- Đây không phải bằng chứng có thể nhận diện mọi mật khẩu/OTP/thông tin thẻ nằm trong văn bản, ảnh hoặc ứng dụng không khai báo đúng. Chưa chạy thử cơ chế lọc.
- Không lấy việc không có cờ mật khẩu làm bằng chứng toàn cửa sổ an toàn. Cần làm rõ UX khi không xác định được vùng an toàn, sau đó thử bằng dữ liệu giả theo E02.
