# Ghi nhận dùng thử E02a — người dùng đã chấp nhận ngày 2026-11-15

## Bước 1 — tìm bản chạy cũ

Người dùng báo chưa tìm thấy cửa sổ hoặc file chạy E02a. Lúc đó phạm vi chỉ cho tìm bản có sẵn, không xây lại. Đã tìm các thư mục có thể truy cập trên ổ C: nhưng không thấy PolicyLab EXE/DLL hoặc tiến trình đang chạy. Gói hồ sơ ZIP không có binary; thư mục không đọc được được bỏ qua. Chưa đánh dấu mục UI/nghiệm thu nào đạt.

## Demo mới trên máy hiện tại

Người dùng sau đó giải thích bản cũ được thử trên máy khác và cho phép tạo demo mới, xử lý phần kỹ thuật còn lại. Đã build mã E02a hiện có, không sửa source; tạo bản self-contained ở thư mục artifact E02a-demo/app. Kiểm thử mới: 53/53 MSTest, 35/35 tình huống trong UI đạt. A05 chỉ nhận SAFE-A; tắt quan sát xóa đầu vào cũ, không tự chạy lại.

Blocker thiếu bản chạy đã được giải quyết. Xem docs/E02a-CURRENT-MACHINE-RESULTS.md cho bằng chứng và giới hạn. Resize tối thiểu, toàn bộ keyboard/focus/screen reader và phản hồi người dùng trên bản mới vẫn còn mở. Không thay checkbox tasks/todo.md; C3 chưa đóng. Không dùng kết quả giả để tuyên bố capture/Unity/AI đã đạt.
## Phản hồi người dùng — 2026-11-15

- Sau hướng dẫn thu nhỏ cửa sổ đến giới hạn và quan sát chữ/nút/thanh cuộn, người dùng phản hồi: “Đã ổn rồi”.
- Ghi nhận: người dùng báo bước đổi kích thước ổn. Chưa có mô tả chi tiết riêng từng điểm hoặc kích thước đo được; không suy ra full keyboard, screen reader hay toàn E02a đã đạt.
- Không đổi checkbox tasks/todo.md hoặc đóng C3. Bước tiếp: kiểm di chuyển focus bằng Tab/Shift+Tab, chưa kích hoạt nút.


## Nghiệm thu trải nghiệm — 2026-11-15

- Phản hồi trước về thu nhỏ cửa sổ: “Đã ổn rồi”.
- Phản hồi về Tab/Shift+Tab và quyết định: “Có nhìn rõ và không có chỗ nào bị kẹt, có thể đóng nghiệm thu E02a rồi”.
- Quyết định trực tiếp: người dùng chấp nhận trải nghiệm demo E02a dữ liệu giả và cho đóng nghiệm thu trải nghiệm C3. Không phải AI tự chấm đạt.
- Phạm vi bằng chứng mới: người dùng báo đổi kích thước ổn, nhìn rõ focus và không kẹt khi điều hướng bằng Tab/Shift+Tab theo hướng dẫn. Không có kích thước đo riêng hoặc bằng chứng mới về screen reader, activation bằng Enter/Space, mọi DPI/màn hình.
- Kết quả kỹ thuật đã chạy trước: 53/53 MSTest và35/35 tình huống giả qua UI, A05 safe-only và tắt quan sát xóa receiver; không chạy lại trong lượt ghi nhận này.
- Nghiệm thu trải nghiệm ĐÃ ĐÓNG theo người dùng; các kiểm tra mở rộng chưa có bằng chứng vẫn ghi CHƯA KIỂM, không biến thành PASS. T05 compound checklist giữ mở nếu còn điều chưa chứng minh.
- Không nghiệm thu production/capture thật/Unity/AI hoặc phiên8h; không cho phép triển khai sản phẩm, push/PR hay release bởi quyết định nghiệm thu này.
