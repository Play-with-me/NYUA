# Ghi chép phỏng vấn dự án nhân vật desktop

> Ghi chép lịch sử. Tra [Yêu cầu hiện hành](YEU_CAU_HIEN_HANH.md) trước; một số dòng “chưa chốt” và điểm tiếp tục dưới đây đã được thay thế.

Cập nhật: 2026-11-13. Người dùng yêu cầu lưu tiến độ rồi tiếp tục hỏi.
Đây là ghi chép giữa buổi, chưa phải tuyên bố mục tiêu đã xác nhận cuối cùng hoặc đặc tả sẵn sàng triển khai.

## Cách làm việc

- Người dùng mới học vibe code, vừa làm vừa học với AI.
- Dùng interview-me: hỏi qua ô câu hỏi, mỗi lần một câu, chờ trả lời rồi hỏi tiếp; kèm giả thuyết để người dùng sửa, không biến giả thuyết thành yêu cầu.
- Hỏi tới khi thật sự hiểu; chưa tự chọn chi tiết còn thiếu hoặc bắt đầu xây app nhân vật.
- Người dùng chọn tự quyết từng chi tiết ngoại hình trước khi tạo mẫu.

## Mục tiêu trải nghiệm đã mô tả

- Một nhân vật anime pixel 128×128 sống trong máy, tạo cảm giác như một người bạn thực sự hiện diện.
- Hoạt bát, tò mò, tinh nghịch, tự chú ý và chọn hành động tùy hoàn cảnh; không mặc định phải có ý thức thật như con người.
- Ví dụ mong muốn: mở máy thì ngái ngủ, vẫy chào, tùy lúc ngủ thêm hoặc thức luôn; kéo sofa và bắp ngô ra xem phim cùng người dùng; leo giao diện để bấm tập tiếp theo.
- Trò chuyện có thể bỏ qua. Ví dụ nhảy theo nhạc từng được nêu, nhưng âm thanh đã được tạm gác về sau.
- Sống tự do trên desktop, leo và đứng trên cạnh cửa sổ, không chỉ trong phòng hoặc cửa sổ riêng.
- Khi người dùng làm việc: vẫn đi lại, sinh hoạt bằng hoạt ảnh, tránh con trỏ và vùng đang gõ, không giành điều khiển.

## Ngoại hình đã chọn

| Thuộc tính | Lựa chọn |
|---|---|
| Nhân vật | Nữ trưởng thành |
| Tỷ lệ | Chibi, đầu lớn, người nhỏ |
| Đồ họa | Pixel 128×128; kích thước hiển thị và cách phóng chưa hỏi |
| Chủ đề | Đời thường, trang phục thoải mái |
| Tóc | Trắng bạc, dài buông ngang eo |
| Tóc mái | Mái thưa ngang trán |
| Mắt | Đỏ hồng |
| Áo | Áo len rộng, hồng nhạt |
| Váy | Chân váy xám đậm |
| Chân | Chân trần, không tất, không giày |

Chưa chọn màu da, dáng chi tiết áo/váy, phụ kiện, tên và bộ biểu cảm. Chưa tạo ảnh mẫu.

## Nguồn lựa chọn quyền

- File người dùng cung cấp: C:/Users/kyuu4/Downloads/quyen-nhan-vat-2026-11-12.json, schemaVersion 4.
- Bản sao nguyên gốc trong dự án: quyen-nhan-vat-da-chon.json (cùng thư mục ghi chép này).
- File gốc có 132 quyền: 69 bật (59 full, 10 limited), 63 chưa bật; không có quyền đã bật ở chế độ ask.
- Đây là cấu hình yêu cầu cho app tương lai, không cấp quyền cho AI hiện tại truy cập hoặc điều khiển máy.
- Các quyết định người dùng nói sau khi gửi file được ưu tiên hơn file. Chưa sửa trang permissions.html hoặc JSON gốc theo các quyết định mới.

## Quyết định mới về quyền — ưu tiên áp dụng

1. Được đọc và hiểu toàn bộ nội dung trong phạm vi được cấp. Quyền đọc không cấp quyền thao tác. Sau đó người dùng chọn giới hạn theo app/website, nên không hiểu là được đọc mọi app mặc định.
2. Mỗi ứng dụng có hai ô riêng: được đọc / được điều khiển.
3. Trình duyệt có hai quyền tương tự cho từng website. Quan hệ giữa quyền trình duyệt và website cần hỏi thêm trước triển khai.
4. App/website mới mặc định tắt cả hai; người dùng tự bật trong menu, không tự kế thừa.
5. Menu sẽ kiểm tra ứng dụng hiện có trên máy và đưa vào danh sách tick. Nguồn danh bạ, email, lịch, tập tin vẫn chưa chọn cụ thể.
6. Khi có nội dung được đọc lẫn nội dung không được đọc, chỉ phân tích vùng được phép; phần còn lại bị che trước phân tích.
7. Khi người dùng chủ động dùng chuột hoặc bàn phím, nhân vật nhường điều khiển. Được trở lại thao tác sau 60 giây không có thao tác người dùng; thao tác nhân vật không tính là thao tác người dùng.
8. Gõ phím/dùng chuột liên tiếp khoảng một phút được người dùng mô tả là làm việc liên tục. Không cần đợi đủ một phút mới nhường điều khiển khi họ vừa thao tác.
9. Cấm tác vụ thay đổi dữ liệu, gửi tin nhắn, mua gói tốn tiền hoặc tác động tương tự; quyền chuột/phím không vượt giới hạn này. Phạm vi “thay đổi dữ liệu” cần phân biệt với lưu dữ liệu riêng, ghi chú hay cập nhật app trước khi triển khai.
10. Tạm gác âm thanh khỏi phạm vi hiện tại; không suy ra đây là quyết định cấm vĩnh viễn.
11. Trước mỗi lần gửi chữ tới AI bên ngoài: cho người dùng xem nội dung và hỏi, từ chối thì không gửi. Thay lựa chọn full trước đó ở I03.
12. Nhân vật được tự cập nhật ứng dụng của mình; ứng dụng khác người dùng tự xử lý. Cách thông báo và xác nhận cập nhật chưa hỏi chi tiết.

## Tóm tắt file quyền gốc để tra cứu

| Nhóm | Đã bật | Nội dung chính |
|---|---:|---|
| A | 10/10 | Quan sát màn hình và giao diện |
| B | 11/14 | Chuột, thao tác bàn phím, đọc bộ nhớ tạm; B03/B04/B14 chưa bật |
| C | 2/8 | C01/C02 bật trong file; sau đó âm thanh tạm gác |
| D | 9/14 | Đọc và điều khiển trang có giới hạn; không mở/đóng tab, tải lên/xuống hoặc đọc cookie |
| E | 6/16 | E01–E06; ghi dữ liệu riêng và đọc nguồn đã chọn |
| F | 12/28 | F01–F10, F17/F18; F07–F10 có điều kiện |
| G | 6/12 | G01–G06; không gửi, đăng, giao dịch hoặc đọc kho mật khẩu |
| H | 9/13 | H01–H05, H10–H13; không lưu ảnh/âm thanh/camera gốc |
| I | 4/17 | I01/I03/I16/I17; I03 và cập nhật đã được làm rõ sau file |

Các điều kiện gốc: B11 gõ trong app được tick; B13 chỉ đọc bộ nhớ tạm khi người dùng mở; D03 chỉ đọc nội dung hiển thị nhưng đã có yêu cầu đọc toàn bộ cần xét cùng phạm vi mới; D05 không tác động mua hàng/dữ liệu; F10 chỉ mở app được tick. Cách hiểu “mở bộ nhớ tạm” vẫn chưa hỏi rõ.

## Còn cần phỏng vấn

- Ngoại hình: màu da, kiểu áo/váy và phụ kiện theo nhu cầu người dùng.
- Trải nghiệm: tương tác trực tiếp, mức tự chủ, ký ức, menu, giới hạn làm phiền, tên nhân vật.
- Phạm vi bản đầu, thành công là gì, thứ tự ưu tiên, đối tượng sử dụng và nhu cầu phát hành.
- Thiết bị/hệ điều hành đích, cấu hình, ngân sách và lựa chọn AI; chưa tự chọn công nghệ.
- Chốt các ranh giới quyền còn mơ hồ nêu trên; chưa xem là đặc tả kỹ thuật hoàn chỉnh.

## Điểm tiếp tục

Đã hỏi tới tóc ngang eo. Câu tiếp theo đề xuất: màu da nhân vật. Sau khi các yêu cầu trọng yếu đủ rõ, tổng kết ý định bằng lời người dùng và xin xác nhận theo interview-me; không coi ghi chép này là xác nhận cuối.
