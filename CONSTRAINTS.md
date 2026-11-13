# Tiêu chuẩn chất lượng dự án

Ngày: 2026-11-13. **Mức hiện tại: quy tắc bằng văn bản; chưa có pipeline kiểm tra tự động.** Không coi một con số trong tài liệu là cơ chế thực thi đã hoạt động.

## Nền tảng áp dụng ngay

- Không chứa mật khẩu, khóa AI hay dữ liệu cá nhân thật trong mã nguồn, dữ liệu thử hoặc bằng chứng.
- Không tắt kiểm tra, xóa assertion, thêm skip/suppression hoặc hạ tiêu chí để che lỗi. Ngoại lệ phải nêu nguyên nhân, phạm vi, người quyết định và điều kiện kết thúc.
- Không báo chức năng hoàn tất khi còn giả lập hoặc stub; bản mẫu phải được dán nhãn và giới hạn rõ.
- Không thay đổi yêu cầu bằng cách sửa tiêu chuẩn chất lượng. Không biến quyền sản phẩm tương lai thành quyền của công cụ hiện tại.
- Không ghi đã duyệt, đã chạy, đã đo hoặc đã có rà độc lập nếu chưa có bằng chứng tương ứng.
- Rà phần thay đổi và kiểm tra phù hợp trước khi kết luận; không mặc định tài liệu chỉ có chữ là đủ chứng minh phần mềm chạy đúng.

## Tiêu chí đã có nguồn, chưa có số đo

| Tiêu chí | Nguồn | Cách sẽ kiểm chứng | Trạng thái |
|---|---|---|---|
| Dữ liệu nguồn bị cấm không tới phân tích/nhớ/gửi ngoài | QD05/QD15 | E02a trước, E02 nguồn thật sau | Chưa chạy |
| Các việc không tự chạy lại sau dừng/ẩn khi chưa tiếp tục | DK03–DK04/BH08–BH09 | E03 kiểm vòng đời và input | Chưa chạy |
| Cảnh rõ đang chú ý bắt đầu phản ứng dưới 1 giây, cảnh khó ưu tiên hiểu đúng | XP02 | E04 đo toàn luồng; tỷ lệ đúng/đạt còn cần quyết định sau số đo | Chưa đo |
| Hai mức ổn định trong phiên khoảng 8 giờ | SP05 và yêu cầu phiên 8 giờ | E05 trên cấu hình ghi rõ | Chưa chạy |
| Lịch sử thao tác tự xóa sau 30 ngày, không ảnh/nội dung riêng | BH13 | Kiểm đồng hồ thử, dữ liệu lưu và xóa | Chưa triển khai |

Không tự đặt mức coverage, RAM/GPU tối đa, tỷ lệ đúng hoặc cấu hình tối thiểu. Khi có stack và phép đo, chốt từng chiều chất lượng cần thực thi; ghi lệnh chạy thật, môi trường, giới hạn thời gian và điều kiện chặn. Kiểm tra vi phạm mẫu phải thất bại, mẫu sạch phải đạt, lỗi công cụ không được thành đạt trước khi gọi cơ chế là tự động thực thi.

## Sổ ngoại lệ

Chưa có ngoại lệ nào được phê duyệt. Mỗi ngoại lệ tương lai cần mã, quy tắc, phạm vi, lý do, người quyết định, thời điểm/điều kiện hết hiệu lực và cách kiểm lại. Không có ngoại lệ ngầm cho lộ dữ liệu hoặc thao tác vượt quyền.

## Trước thay đổi code đầu tiên

Đọc file này và yêu cầu liên quan; kiểm tra trạng thái thư mục, thiết lập Git phù hợp, chọn công cụ kiểm tra theo stack đã chọn. Chưa có app/native test runner/CI nên chưa cài hàng loạt công cụ, chưa khai báo lệnh build hoặc tỷ lệ coverage giả.
