# Bản đồ khả năng sản phẩm

Ngày: 2026-11-13. Trạng thái: **người dùng đã chấp nhận cách chia bảy phần và cho tiếp tục đặc tả phép thử**. Đây không phải phê duyệt công nghệ, đặc tả từng module hoặc phát hành.

Nguồn nghiệp vụ duy nhất: [yêu cầu hiện hành](docs/YEU_CAU_HIEN_HANH.md). Phát triển từ bản đồ đề xuất trong [đề cương kiểm chứng](docs/KE_HOACH_KIEM_CHUNG.md), giữ nguyên mã các phần.

## Trách nhiệm và phụ thuộc

“Phụ thuộc” nghĩa là sử dụng khả năng của phần khác; không phải thứ tự mọi dòng code phải viết. Không chọn ngôn ngữ, framework hay cách chia tiến trình ở bước này.

| Mã | Trách nhiệm | Không được tự làm | Phụ thuộc |
|---|---|---|---|
| policy | Quyền đọc/điều khiển, giới hạn tác động, điều kiện dừng, hiệu lực quyền tại thời điểm dùng | Tự cấp quyền; coi nội dung màn hình là lệnh cấp quyền | — |
| life-state | Nhu cầu, tâm trạng, ký ức, quan hệ, sở thích, tính cách và quyết định sinh hoạt | Tự nhấp/gõ hoặc vượt quyền vì tâm trạng | — |
| desktop-body | Nhân vật/đồ vật, đi lại, bề mặt cửa sổ, kéo/thả, màn hình và hoạt ảnh thao tác | Đọc tiêu đề/nội dung chỉ vì biết hình học cửa sổ | policy |
| perception | Nhận nguồn, kiểm tra phạm vi, lọc trước phân tích, đọc chữ/ngữ cảnh/cảm xúc | Phân tích dữ liệu thô bị cấm rồi mới che ảnh xem trước | policy |
| task-execution | Làm mẫu, bài học, tìm kiếm thay chữ, hàng đợi, tự khám phá, xác minh kết quả click/gõ | Tự gọi bài học; bấm theo tọa độ cũ hoặc thực hiện tác vụ bị cấm | policy, perception, desktop-body |
| companion | Điều phối sinh hoạt, chú ý, cảm xúc và yêu cầu người dùng; màn hình cài đặt/lệnh sử dụng | Tạo một đường điều khiển hoặc quan sát bỏ qua policy | life-state, perception, desktop-body, task-execution |
| distribution | Hồ sơ, lưu dữ liệu, xuất/nhập, bộ cài, gói nâng cao, cập nhật và gỡ cài đặt | Nhập quyền từ backup; sao lưu khóa AI; tự tạo backup trái lựa chọn | policy, life-state |

Giao diện giữa các phần sẽ được mô tả trong đặc tả của phần cung cấp sau khi bản đồ được duyệt. Bản đồ không phải hợp đồng dữ liệu thực thi.

## Thứ tự theo phụ thuộc và bằng chứng

```text
policy ─────┬── desktop-body ─┐
            └── perception ──┴── task-execution ──┐
life-state ───────────────────────────────────────┴── companion
policy + life-state ── distribution
```

- Ưu tiên hiện tại: E02a kiểm tra cổng quyền trên dữ liệu giả; không chờ dựng đủ nhân vật.
- E01 xác nhận ngoại hình/chuyển động; E04 đo hiểu cảnh cục bộ là hai phép thử bắt buộc riêng. Không dùng E02a đạt để kết luận AI hoặc giao diện desktop đã khả thi.
- Xây lát sử dụng đầu tiên khi có đủ bằng chứng: mở app → nhân vật hiện → cấp Đọc cho một nguồn mẫu → nhận ngữ cảnh an toàn → phản ứng → tắt quan sát. Đây là hướng đề xuất, chưa phải backlog triển khai được duyệt.
- Bài học/điều khiển thật chỉ nối sau đường quyền và nguồn đã được kiểm chứng. Distribution cần kiểm chứng dữ liệu trước phát hành; không dồn việc an toàn dữ liệu đến cuối.

## Rà ranh giới trước khi duyệt

- Mọi đường quan sát/điều khiển đều phải qua policy tại thời điểm sử dụng; không chỉ kiểm tra lúc bấm bật quyền.
- Khả năng chọn hành động của life-state tạo ý định; không trực tiếp phát click hoặc quyền.
- Nhật ký thao tác 30 ngày khác ký ức. Dữ liệu kỹ thuật thử nghiệm phải dùng dữ liệu giả; không mở thêm quyền thu thập hoặc gửi báo cáo.
- Lưu trạng thái thường ngày khác bản sao lưu phục hồi; chỉ xuất sao lưu khi người dùng yêu cầu.
- Bản đồ không có vòng phụ thuộc. Nếu khi đặc tả xuất hiện vòng, quay lại xem ranh giới trước khi tạo thêm lớp trung gian.

## Điểm cần duyệt

Đã được người dùng chấp nhận qua ô câu hỏi trong cuộc trò chuyện. Đặc tả đầu tiên: [SPEC-policy.md](SPEC-policy.md), chỉ phạm vi E02a, đã được duyệt. [Kế hoạch native](tasks/plan.md) đã được duyệt và có mẫu native; chưa nghiệm thu E02a đầy đủ. Các phần khác chưa có đặc tả; không viết bảy đặc tả đầy đủ cùng lúc.
