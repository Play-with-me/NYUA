# Quy tắc nghiệp vụ và ngoại lệ

Các bảng này giải thích yêu cầu đã chốt. Phần đề xuất xử lý lỗi kỹ thuật sẽ được ghi riêng, không coi là quyền người dùng đã cấp.

## 1. Quy tắc nào được ưu tiên?

Nếu một hành động có nhiều lý do để được làm nhưng có một điều kiện cấm đang có hiệu lực, hành động vẫn bị chặn. Ví dụ, đã cấp Điều khiển cho website nhưng bạn vừa dùng chuột thì cô ấy phải nhường; đã được bạn giao việc nhưng tác vụ gửi tin nhắn vẫn bị cấm.

Thứ tự kiểm tra nghiệp vụ: điều bị cấm → chế độ dừng/ẩn/quan sát → quyền nguồn → nguồn và mục tiêu còn đúng → người dùng đang thao tác hay không → điều kiện của việc → tâm trạng và cách thể hiện. Tâm trạng không được mở rộng quyền.

## 2. Các nút dừng khác nhau ra sao?

| Tình huống | Đọc nội dung | Điều khiển app | Sinh hoạt | Việc đang chạy | Việc chưa chạy |
|---|---|---|---|---|---|
| Bạn thao tác chuột/phím | Theo quyền | Nhường ngay; sau 60 giây xét tiếp | Vẫn sinh hoạt, tránh vùng làm việc | Tạm nhường, kiểm tra lại mới tiếp | Chờ đủ điều kiện |
| Dừng khẩn cấp | Theo quyền | Tắt đến khi bạn bật lại | Vẫn sinh hoạt | Hủy | Tạm dừng |
| Tắt quan sát | Tắt | Tắt | Có, chỉ biết hình học cửa sổ | Hủy | Tạm dừng |
| Bạn ẩn nhân vật | Tắt | Tắt | Ẩn cả cô ấy/đồ | Hủy | Tạm dừng |
| Cô ấy tự ẩn vì tổn thương | Tắt | Tắt | Chỉ giữ trạng thái riêng | Hủy | Tạm dừng |
| Thoát app | Tắt vì không chạy | Tắt | Không chạy | Báo rõ rồi hủy | Báo rõ rồi hủy |
| Đổi hồ sơ | Hồ sơ cũ ngừng | Hồ sơ cũ ngừng | Hồ sơ cũ đóng băng | Báo rõ rồi hủy | Báo rõ rồi hủy |

Sau các nút dừng/ẩn, bật lại hoặc cô ấy xuất hiện chưa đủ: người dùng phải bấm **Tiếp tục hàng đợi**. Việc đã hủy không tự sống lại. Tắt quan sát khác với ngừng mọi thông tin: ngoại lệ hình học đã được bạn cho phép để cô ấy đi trên cạnh cửa sổ.

## 3. Những đồng hồ độc lập

| Mốc | Dùng để làm gì | Không được hiểu thành |
|---|---|---|
| 60 giây không chuột/phím thật | Xét tiếp điều khiển bị người dùng giành lại; ngừng cộng thiếu quan tâm | Chắc chắn người dùng rời máy hoặc đã cho mở nhạc |
| 5 phút mặc định, chỉnh được | Nâng cao được xét tự mở phim/nhạc nếu không có nội dung đang phát | Cho phép ngắt phim/nhạc của người dùng |
| Hai lần rủ, nghỉ ít nhất 30 phút | Hạn chế rủ chơi và nghịch để gây chú ý | Mất quan hệ vì bạn đang làm việc |
| Phim ít nhất 20 phút | Một tín hiệu để học gu | Chắc chắn thích phim hoặc còn xem từng giây |
| Nhạc lặp lại/nhiều bài cùng kiểu | Một tín hiệu học gu, dựa thao tác chọn/chuyển của bạn | Cho phép thu âm/phân tích âm thanh |
| 48–72 giờ thao tác đủ điều kiện | Bắt đầu buồn vì thiếu quan tâm ở nâng cao | 3 ngày lịch, thời gian máy mở hoặc thời gian xem phim thụ động |
| 30 ngày | Tự xóa lịch sử thao tác | Xóa ký ức/tình cảm sau 30 ngày |

Thao tác mở khóa riêng không đặt lại thời gian chờ; thao tác tiếp theo trong desktop mới đặt lại. Input do cô ấy tạo không được giả thành input của người dùng.

## 4. Đọc, nhớ và gửi ra ngoài

| Nguồn | Đọc được khi | Được nhớ gì | Được gửi ngoài? |
|---|---|---|---|
| App/web | Phần đang nhìn thấy, đủ quyền, không riêng tư/nhạy cảm | Theo quy tắc nguồn và quản lý ký ức | Chỉ chữ đã lọc, khi bạn chủ động yêu cầu và duyệt từng lần |
| Tài liệu mở trên màn hình | Như app đã cấp quyền | Chỉ tên/chủ đề, không chi tiết nội dung | Không tự coi là được gửi chi tiết vì đã nhìn thấy |
| Windows + V | Bảng lịch sử đang mở và điều kiện an toàn đạt | Không ký ức lâu dài | Không tự gửi |
| Tập tin/thư mục trực tiếp | Chức năng đã hoãn | Chưa triển khai | Không |
| Cửa sổ chưa cho Đọc | Chỉ vị trí/kích thước | Không tiêu đề/nội dung | Không |

Chi tiết chữ nào của tài liệu/clipboard có thể xuất hiện trong phần xem trước gửi AI chưa chốt đầy đủ; để chặn ở thiết kế cho đến khi rõ, không mặc định quyền đọc là quyền gửi.

## 5. Các ví dụ quyết định

- Cấp quyền website chính không tự cấp toàn bộ website chứa video nhúng. Ngoại lệ chỉ cho đúng khung video trong trang được phép; quảng cáo không kế thừa.
- Website tự lưu lịch sử xem được chấp nhận. Tự mở email làm thành đã đọc không được chấp nhận; không thử rồi mới kiểm hậu quả.
- Khi bài học lỗi bước 2, dừng bài đó và nhờ dạy lại. Bài khác ở hàng đợi chỉ chạy nếu tự đủ điều kiện, không dựa giả định bước 2 đã xong.
- Chỉnh nội dung ký ức không tính lại quan hệ. Chủ động xóa ký ức có thể điều chỉnh phần đóng góp; quên tự nhiên giữ sự thân thiết đã hình thành.
- Tắt lãng mạn có quyền chọn giữ/xóa ký ức liên quan; giữ thì cô ấy có thể buồn tạm, không níu kéo hoặc tự bật lại.
- Cô ấy tự ẩn không làm mất quyền mở cài đặt hoặc quyền reset của bạn. Chăm sóc tốt vẫn có thể làm lành mọi mức.

## 6. Chỗ chưa được phép đoán

Một “buổi” làm lành dài bao lâu; phím chuyển vị trí; các loại trái cây/thú bông; ngưỡng chuyển sang tự ẩn; cấu hình tối thiểu; tỷ lệ nhận diện đúng; model và dung lượng gói; chi tiết định dạng backup và công nghệ kết nối Godot vẫn cần chốt/đo. Xem [sổ điểm mở](../AI/DECISIONS.md).
