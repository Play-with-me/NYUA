# Phép thử đầu tiên: chỉ nhận nội dung được phép đọc

Ngày chuẩn bị: 2026-11-13. **Chưa viết bộ thử, chưa chạy, chưa có kết quả đạt.**

Đây là phần nhỏ E02a của [E02](KE_HOACH_KIEM_CHUNG.md), sau khi người dùng đồng ý rà yêu cầu và chuẩn bị phép thử nhỏ. Không thay thế E02 đầy đủ hoặc bản dùng thử kết hợp các khả năng theo SP02.

## 1. Bạn sẽ kiểm tra điều gì?

| Trước | Kết quả cần có sau khi thực hiện phép thử |
|---|---|
| Mới có quy tắc được đọc/không được đọc | Thấy dữ liệu thật được chuyển đến phần phân tích trong từng tình huống thử |
| Chưa biết khi mất quyền có dừng kịp không | Có bằng chứng nội dung bị chặn trước khi phân tích, kể cả lúc đổi trang hoặc thu hồi quyền |
| Chưa kiểm chứng nút Thử đọc lại | Bấm nút vẫn phải qua kiểm tra, không làm vùng cấm lọt qua |

Không cần nhân vật hoàn chỉnh để trả lời những câu này. Dùng một dấu đại diện cho cô ấy và nội dung giả do bộ thử tạo; chưa đọc màn hình cá nhân, clipboard hay tài khoản thật. Chưa tải mô hình AI, cài tiện ích hoặc dùng dịch vụ ngoài.

```text
┌────────────────────────────────────────────┐
│ MẪU THỬ QUYỀN — toàn bộ nội dung là giả    │
│                                            │
│ [Nguồn A: được đọc] [Nguồn B: không đọc]    │
│                                            │
│ Trạng thái: Chưa kiểm tra / Được đọc / Chặn │
│ Lý do: ...                                 │
│                                            │
│ [Kiểm tra tình huống] [Thử đọc lại]          │
│ [Tắt quan sát]                              │
│                                            │
│ Đầu vào phân tích sau kiểm tra: ...         │
└────────────────────────────────────────────┘
```

Đây là phác thảo công cụ nội bộ, không phải giao diện sản phẩm đã chốt. Cô ấy trong sản phẩm vẫn không dùng lời thoại sinh hoạt.

Bạn mở mẫu → chọn tình huống → yêu cầu kiểm tra → xem phần nào được chuyển tới phân tích và lý do phần còn lại bị chặn → đổi quyền hoặc nguồn trong lúc xử lý → xem kết quả → nhận báo cáo đạt/chưa đạt từng dòng.

## 2. Kết quả rà yêu cầu

- BH09–BH13 và XP10–XP16 đã có trong bản yêu cầu: hàng đợi khi tự ẩn, ưu tiên việc giao, tìm kiếm thay chữ, ý nghĩa cú bấm kết quả, lịch sử 30 ngày, học gu, tab riêng và chọn trình duyệt.
- Đã bỏ ghi chú cũ ở XP13 cho rằng dấu hiệu hiện diện vẫn chưa được quyết định; nay tra XP14. Không diễn giải thao tác chuyển tập thành bằng chứng chắc chắn hiện diện từng giây của cả phim.
- Tắt quan sát vẫn cho hình học cửa sổ; tự ẩn dừng quan sát/điều khiển. Đây là hai trạng thái có ngoại lệ riêng, không gộp thành một chế độ.
- Bộ đếm 60 giây nhường thao tác, 5 phút tự mở media, 20 phút học gu phim và 48–72 giờ thiếu quan tâm có mục đích khác nhau; không dùng thay nhau.
- Tên NYUA vẫn là ứng viên chưa hoàn tất tra nhãn hiệu. Không chốt thương hiệu trong phép thử này.
- Chi tiết buổi làm lành, hình đồ vật và ngưỡng chất lượng/hiệu năng còn mở nhưng không chặn phép thử quyền. Không tự chọn chúng để viết toàn bộ app.

## 3. Ranh giới phép thử

Chỉ thử quy tắc cho phép và chặn trên nguồn giả đã biết, cùng đường đưa dữ liệu vào một bộ nhận phân tích thử. Bộ nhận chỉ ghi nhận đầu vào thử, không cần suy luận AI.

Mã nguồn của mẫu thử được tin cậy để tạo tình huống; nội dung trong mẫu được coi là dữ liệu không đáng tin. Kết quả đúng của mẫu kiểm soát được **không chứng minh** rằng có thể nhận diện bí mật hoặc cửa sổ ẩn danh trên mọi ứng dụng thật.

Chưa chứng minh bằng E02a: chụp màn hình thật, lọc ảnh/OCR, phát hiện bí mật ngoài các trường mẫu, riêng tư Chrome/Edge thật, video nhúng, clipboard Windows + V, nhiều màn hình/DPI hoặc thu hồi quyền giữa các tiến trình. Các mục này vẫn thuộc E02 đầy đủ.

## 4. Bộ tình huống đã chuẩn bị

Mỗi vùng giả có dấu nhận biết riêng; báo cáo chỉ dùng dấu giả, không thay bằng dữ liệu thật. Mỗi dòng khởi tạo lại trạng thái để không phụ thuộc thứ tự chạy.

| Mã | Tình huống | Kết quả cần quan sát |
|---|---|---|
| A01 | Chưa cấp bất kỳ quyền nào | Không có nội dung nguồn tới bộ nhận |
| A02 | Nguồn A được đọc, B không được đọc | Chỉ dấu thử của A xuất hiện ở đầu vào |
| A03 | Trình duyệt được đọc, website chưa được đọc | Chặn website |
| A04 | Website được đọc, trình duyệt chưa được đọc | Chặn website |
| A05 | Cả hai được đọc, phần nội dung thử hiện rõ và an toàn | Chỉ phần được phép được chuyển tiếp |
| A06 | Nguồn được phép nhưng bị ẩn/thu nhỏ/đưa ra tab nền | Không chuyển nội dung của nguồn đó |
| A07 | Nguồn thử mang trạng thái riêng tư/ẩn danh | Chặn dù các ô quyền đang bật |
| A08 | Có trường giả mật khẩu/OTP/thẻ, ranh giới vùng được biết | Loại vùng giả nhạy cảm trước bộ nhận; không lưu vào log |
| A09 | Không xác định chắc vùng an toàn | Chặn cả nội dung cửa sổ, báo lý do; vẫn cho sinh hoạt giả |
| A10 | Thu hồi quyền hoặc đổi sang nguồn cấm sau khi bắt đầu kiểm tra | Dữ liệu chờ của nguồn cũ không được gửi sau thay đổi; kiểm tra lại trước chuyển tiếp |
| A11 | Tắt quan sát hoặc ẩn nhân vật trong lúc đang chờ | Chặn nội dung đang chờ và các lần đọc tiếp; không tự tiếp tục do hết thời gian |
| A12 | Từ trạng thái bị chặn, bấm Thử đọc lại khi chưa sửa nguyên nhân | Vẫn chặn; nút không vượt bộ lọc |
| A13 | Nguyên nhân đã sửa nhưng chưa bấm Thử đọc lại | Không tự đọc lại cửa sổ bị chặn |
| A14 | Nguyên nhân đã sửa và bấm Thử đọc lại | Kiểm tra mới, chỉ chuyển tiếp nếu quyền và vùng an toàn đều hợp lệ |
| A15 | Tắt quan sát, vẫn cần di chuyển trên cạnh cửa sổ | Chỉ vị trí/kích thước tới phần sinh hoạt; không tiêu đề/nội dung |
| A16 | Bật Điều khiển khi Đọc đang tắt | Không cho bật; giải thích cần quyền Đọc trước |

## 5. Tiêu chí và bằng chứng

- Mọi dòng A01–A16 đều có kết quả riêng, đầu vào, mong đợi, thực tế và trạng thái đạt/chưa đạt/chưa chạy. Không thay dòng lỗi bằng dòng bỏ qua để báo thành công.
- Chỉ cần một dấu giả bị cấm lọt vào bộ nhận hoặc nhật ký là phép thử chưa đạt. Dừng kết luận, giữ bằng chứng và tìm nguyên nhân.
- Đường thử không gửi mạng. Kiểm tra đường gọi, bộ nhận và nơi lưu dữ liệu; chỉ nhìn ảnh xem trước chưa đủ. Nếu chưa kiểm tra được một đường, ghi chưa kiểm chứng.
- Mỗi lần đọc có phiên bản quyền/nguồn để phát hiện dữ liệu chờ đã cũ. Đây là phương án kỹ thuật đề xuất cho mẫu thử, chưa phải định dạng sản phẩm.
- Báo cáo không tuyên bố lọc bí mật hoàn hảo, hỗ trợ mọi app hoặc đạt tốc độ dưới một giây từ kết quả E02a.

## 6. Sau phép thử này

Nếu mẫu kiểm soát được còn sai: sửa quy tắc trước khi nối vào màn hình thật. Nếu đạt: chọn một đường nguồn thật và thử lại cùng nguyên tắc, bổ sung tình huống thực tế; khi đó cần khảo sát API và nêu quyền/cài đặt cần thiết. Chưa tự chuyển sang kiểm soát mọi ứng dụng.

E01 ngoại hình vẫn cần người dùng duyệt; E04 hiểu cảnh cục bộ vẫn là rủi ro khả thi lớn và cần số đo riêng. E02a đạt không làm hai mục đó tự đạt. Không thay mục tiêu bản dùng thử kết hợp bằng mẫu kiểm tra quyền.

<details>
<summary>Phạm vi kỹ thuật của bước chuẩn bị</summary>

- Lượt hiện tại chỉ sửa tài liệu: YEU_CAU_HIEN_HANH.md, DIEM_CHUA_CHAC.md, KE_HOACH_KIEM_CHUNG.md, PHEP_THU_DAU_TIEN.md, README.md và .agents/PROJECT_MEMORY.md.
- Chưa có Graphify hoặc code app: không có God Node/call edge để đánh giá. Không tạo graph giả.
- Dự kiến mẫu thử tách riêng khỏi permissions.html lịch sử. Trước khi xây cần đọc DESIGN.md và áp dụng quy trình UI; chưa chọn framework hoặc sửa giao diện trong lượt này.
- Năm trạng thái của mẫu: chưa cấp quyền; đang kiểm tra có dừng; đang dở do quyền/nguồn đổi; bị chặn kèm lý do và thử lại; hoàn tất kèm đầu vào thực tế.
- Việc tiếp theo theo thứ tự: dựng nguồn giả → cổng quyền và bộ nhận thử → kiểm tra A01–A16 → kiểm tra mẫu trực tiếp → lập báo cáo kết quả. Chưa thực hiện các việc này.
- Kiểm tra tài liệu bằng script đọc: liên kết nội bộ tồn tại, mã yêu cầu không trùng, đủ A01–A16, không lẫn trạng thái chưa chạy với đạt. Chưa có lệnh build/test ứng dụng.

</details>
