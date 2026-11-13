# Đề cương kiểm chứng trước khi xây toàn bộ

Cập nhật: 2026-11-13. **Chỉ là kế hoạch phép thử, chưa chạy và chưa có kết quả đạt.**

Nguồn: [Yêu cầu hiện hành](YEU_CAU_HIEN_HANH.md), [Điểm chưa chắc](DIEM_CHUA_CHAC.md).

Sau khi người dùng đồng ý rà yêu cầu và chuẩn bị phép thử: chọn E02a làm lát thử đầu tiên, chi tiết tại [Phép thử đầu tiên](PHEP_THU_DAU_TIEN.md). E02a chỉ dùng nguồn giả để kiểm tra cổng quyền; không thay E02 đầy đủ. E01 vẫn cần duyệt ngoại hình, E04 vẫn cần đo khả thi AI. Chưa chạy bất kỳ phép thử nào.

## 1. Dành cho người dùng: sẽ kiểm tra điều gì?

| Hiện tại | Sau bước kiểm chứng mong muốn |
|---|---|
| Đã mô tả cô ấy trông thế nào nhưng chưa có mẫu được duyệt | Có mẫu đứng và chuyển động ngắn để bạn xác nhận đúng gu |
| Đã chọn ranh giới quyền nhưng chưa có cơ chế chạy thật | Có bằng chứng nguồn cấm không đi vào phân tích và thao tác bị chặn đúng |
| Muốn cô ấy tới nút, bấm và học chuỗi nhưng chưa biết độ tin cậy | Có một luồng mẫu làm được và tình huống sai phải dừng |
| Muốn hiểu phim tiếng Việt nhanh ngay trên máy | Có số đo tốc độ/độ đúng/tài nguyên và giới hạn thực tế |
| Muốn dùng ổn định 8 giờ | Có hồ sơ thử dài trên cấu hình xác định, gồm lỗi và giới hạn còn lại |

```text
[Duyệt mẫu nhân vật]
         |
[Kiểm chứng quyền đọc] --> [Kiểm chứng thao tác và nhường input]
         |                              |
[Thử hiểu cảnh cục bộ] ------------------+
         |
[Thử cảm xúc, hồ sơ và sao lưu bằng dữ liệu giả]
         |
[Phiên tích hợp 8 giờ] --> [Bạn xem bằng chứng và chốt phạm vi]
```

Hành trình dự kiến: xem mẫu → dùng tình huống thử đã nêu → xem kết quả thật và phần không đạt → quyết định giữ yêu cầu, đổi phương án hoặc thu hẹp phạm vi bằng lựa chọn rõ ràng.

## 2. Bản đồ khả năng đề xuất — chưa phải kiến trúc đã duyệt

| Mã khả năng | Trách nhiệm | Phụ thuộc đề xuất |
|---|---|---|
| policy | Quyền nguồn, ranh giới tác động, dừng/ẩn, thứ tự ưu tiên người dùng | — |
| desktop-body | Hiển thị nhân vật/đồ, input tương tác, bề mặt, nhiều màn hình | policy |
| perception | Thu nội dung được phép, che, OCR, ngữ cảnh và cảm xúc cảnh | policy |
| life-state | Nhu cầu, tâm trạng, ký ức, quan hệ, lựa chọn hoạt động | — |
| task-execution | Dạy/chạy bài học, tự khám phá, bấm/gõ đúng phạm vi | policy, perception, desktop-body |
| companion | Kết hợp đời sống, chú ý, cơ thể và tác vụ | life-state, perception, desktop-body, task-execution |
| distribution | Hồ sơ, sao lưu, cài đặt, gói nâng cao, cập nhật/gỡ cài | policy, life-state |

Các phụ thuộc là hướng chuẩn bị phép thử, không quyết định framework, module code, API/types hoặc schema. Chưa viết đặc tả từng module trước khi ranh giới được rà soát. Khi triển khai thực tế còn phải tách ghi dữ liệu riêng khỏi quyền sửa dữ liệu người dùng.

## 3. Các phép thử nhỏ và bằng chứng phải thu

### E01 — Mẫu ngoại hình và chuyển động

- Mục tiêu: chứng minh phong cách đúng, trước khi làm cả bộ sprite.
- Đề xuất mẫu tối thiểu: một tư thế đứng chính diện, đi, phản ứng khi bấm và rơi/đứng dậy; đây là mẫu thử, không phải danh sách hoạt ảnh cuối.
- Hiển thị ở 64, 128, 192 và 384 pixel để kiểm tra pixel, tỷ lệ, chiều kẹp và chân trần; kiểm tra phóng tự do không làm mất nhận diện.
- Bạn xác nhận ngoại hình, mức chibi và cảm giác chuyển động. Không báo đạt chỉ vì ảnh sinh ra đúng kích thước.
- Bằng chứng: ảnh/đoạn preview, nhận xét của bạn, danh sách sửa. Chưa tạo mẫu trong lượt chuẩn bị này.

### E02 — Ranh giới quan sát trước khi phân tích

- Phụ thuộc: H04/H16 đã chốt hành vi; khảo sát K01/K03/K04 trước đường tích hợp thật. Dùng cửa sổ giả và dữ liệu thử, không dùng tài khoản riêng của người dùng.
- Tình huống: hai cửa sổ đều phép; một phép/một cấm; tab nền/thu nhỏ; ẩn danh; nhiều màn hình; chuyển tab giữa lúc chụp; các vùng thử mật khẩu/OTP/thẻ.
- Quan sát dữ liệu đầu vào thật của OCR/model, nhật ký và mọi đường mạng; không chỉ ảnh xem trước. Dữ liệu thử vùng cấm không được xuất hiện ở các nơi này.
- Kiểm tra quyền ở cả trình duyệt và website, tên miền phụ, thu hồi quyền, tắt quan sát, ẩn và hồ sơ đổi.
- Clipboard: chỉ bắt đầu đọc lịch sử khi Windows + V mở; đóng thì dừng; không tạo ký ức clipboard. Khảo sát khả năng thật trước, không giả vờ có API hỗ trợ.
- Đạt phép thử: mọi tình huống cấm trong bộ thử đều bị chặn; nếu không phân vùng chắc chắn thì dừng lấy nội dung của tình huống đó và báo giới hạn.
- Bằng chứng: bộ dữ liệu giả, cấu hình quyền, dữ liệu sau lọc, kiểm tra mạng/log và lỗi cụ thể. Đạt bộ thử không phải bảo đảm lọc hoàn hảo mọi màn hình ngoài thực tế.

### E03 — Một chuỗi học, đi đến nút và nhường thao tác

- Phụ thuộc: E02, K01–K03; bắt đầu bằng trang mô phỏng nút xem phim trên máy, sau đó kiểm tra Chrome và Edge với nội dung hợp lệ được phép.
- Luồng hẹp: người dùng làm mẫu → tóm tắt và duyệt → gọi bài → nhân vật đến nút → bấm → xác minh trạng thái thành công.
- Tình huống: di chuyển cửa sổ/đổi DPI, nút đổi vị trí, nút biến mất, người dùng dùng chuột/phím giữa bước, hết 60 giây, chuyển app, thu hồi quyền, dừng khẩn cấp, tắt quan sát.
- Kiểm tra vòng đời hàng đợi theo BH06–BH08: lỗi dừng riêng, việc sau đủ điều kiện được tiếp; Dừng khẩn cấp/Tắt quan sát/Ẩn hủy việc đang chạy, giữ việc chưa chạy tạm dừng. Bật lại chức năng không chạy việc cũ khi chưa bấm Tiếp tục hàng đợi; thoát/đổi hồ sơ báo rõ và hủy tất cả việc chưa xong.
- Thử đi đến vị trí chưa có chỗ đứng bằng dụng cụ ảo. Không click theo tọa độ cũ nếu UI đổi; không click vào chính lớp nhân vật hoặc cửa sổ khác.
- Thử lệnh có thể trì hoãn một lần theo tâm trạng, nhưng lần hai không bỏ qua thiếu quyền hoặc lỗi.
- Đạt phép thử: chuỗi đúng được xác minh kết quả, các tình huống mất quyền/không chắc dừng trước thao tác sai; input thật khiến nhường. Đo độ trễ nhường thực tế trước khi chốt ngưỡng nghiệm thu.
- Thử ngoại lệ phim/nhạc trên trang mô phỏng: 5 phút vắng, đã có media thì không mở thêm, người dùng trở lại vẫn phát, tối đa 3 nội dung, tab lạ giữ nguyên/quay lại phim.
- Bằng chứng: chuỗi đã duyệt, video thao tác dùng dữ liệu giả, trạng thái từng bước, latency input và các trường hợp không hỗ trợ.

### E04 — Hiểu phim tiếng Việt cục bộ

- Phụ thuộc: K05 và đường nội dung E02 an toàn. Không gửi ảnh lên AI ngoài để đạt hộ chỉ tiêu cục bộ.
- Chọn trước bộ cảnh có quyền sử dụng: anime/người đóng, buồn/vui/hành động/trung tính, có phụ đề Việt; cảnh rõ và khó được phân loại trước khi chạy.
- Người dùng rà bộ nhãn cảm xúc và thời điểm bắt đầu sự kiện. Không chọn lại cảnh sau đo chỉ để có kết quả đẹp.
- Ghi cấu hình máy, runtime/model, phiên bản, mạng đã ngắt hay không, thời gian khởi động và đã làm nóng.
- Đo từ sự kiện hiện trên màn hình đến khởi đầu hoạt ảnh cảm xúc: thời gian lấy ảnh → lọc → đọc chữ → suy luận → quyết định → hiển thị. Báo độ trễ từng mẫu và phân bố, không chỉ trung bình.
- Mục tiêu người dùng: dưới 1 giây với cảnh rõ khi đang chú ý; cảnh khó chờ hiểu đúng. Ghi riêng đúng/sai/không chắc/không quan sát; tránh đổi cảm xúc liên tục khi chuyển cảnh.
- Độ chính xác chấp nhận được và tỷ lệ mẫu cần dưới 1 giây **chưa chốt**; cần kết quả đo để bàn H14, không tự đặt con số thay người dùng.
- Bằng chứng: bảng nhãn so kết quả, độ trễ toàn luồng, CPU/RAM/GPU, giật video nếu có, kích thước gói và giấy phép. Không đạt thì trình phương án, không tự hạ mục tiêu hoặc đổi sang cloud.

### E05 — Phiên tích hợp 8 giờ và offline

- Chỉ chạy sau các phép thử hẹp đạt hoặc giới hạn đã được người dùng chấp nhận; đây chưa phải lệnh chạy benchmark nền.
- Một phiên có lịch và thời hạn rõ: làm việc, không đáp lời rủ, chăm sóc, nghỉ, media, sleep/wake, đổi mức/hồ sơ/màn hình và thao tác hủy. Không ngồi polling vô hạn.
- Kiểm tra cả hai mức trên cấu hình ghi rõ. Ghi lỗi, độ tăng bộ nhớ, CPU/GPU, phản hồi giao diện, giật video, mất trạng thái, quyền và traffic ngoài dự kiến.
- Ngắt mạng sau tải đủ gói: sinh hoạt, ký ức, hiểu nội dung cục bộ vẫn hoạt động; web/AI ngoài/cập nhật báo không có mạng thay vì treo.
- Tải nâng cao không vừa máy: cảnh báo, cho chọn bật thử, không âm thầm đổi mức. Gói tải lỗi chưa được coi là nâng cao đã sẵn sàng.
- Kết quả: báo cáo 8 giờ thực tế và ma trận máy được thử. Không kết luận “mọi máy Windows 11” chỉ từ máy phát triển; chốt thêm H14 theo số đo.

### E06 — Kịch bản cảm xúc, hồ sơ và bản xuất

- Phần cảm xúc bắt đầu bằng kịch bản có thể rà bằng tay; sau đó mới kiểm tra thực thi. Dùng đồng hồ thử điều khiển được để không phải chờ 72 giờ cho mỗi lần thử.
- Chuỗi ví dụ: chơi bình thường → quăng đầu phản đối → tiếp diễn từ chối nhấc → dỗ và bình tĩnh → cho nhấc lại; thiếu quan tâm đủ điều kiện → buồn → tiếp diễn → tự ẩn → mời/quà → làm lành qua vài buổi.
- Bộ đếm: active-user-only, 60 giây dừng; 48–72 giờ theo tin tưởng/tổn thương; không cộng sleep, app đóng/vắng, cơ bản, input nhân vật hoặc hồ sơ đóng băng. Tương tác ngắt chuỗi nhưng không xóa buồn ngay.
- Kiểm tra cô ấy chọn hoạt động có lý do, không phạt người dùng vắng mặt; rủ/nghịch chung hai lần và 30 phút nghỉ. Trạng thái nội bộ kiểm thử được, không hiển thị bảng điểm cho người dùng.
- Phần dữ liệu: chỉ xuất thủ công, mật khẩu và mã khôi phục đều mở được bản thử; sai mật khẩu/mã bị từ chối; không chứa khóa AI hoặc quyền có thể tự áp trên máy mới.
- Nhập thành hồ sơ riêng, không trộn. Hồ sơ khác đóng băng; quyền dùng chung trên máy. Thu hồi quyền cho chọn xóa ký ức theo nguồn; xóa không tự phục hồi từ bản cũ.
- Kịch bản gỡ/reset phải dùng dữ liệu giả; không thử xóa dữ liệu cá nhân. Kiểm chứng phân biệt lưu trạng thái thường ngày và tạo backup tự động bị cấm.
- Bằng chứng: bảng trước/sau, kịch bản người dùng duyệt, kết quả test dữ liệu, kiểm tra file xuất và giới hạn chưa xử lý.

## 4. Thứ tự thực hiện đề xuất

1. Rà bản hợp nhất; chỉ hỏi điểm còn mở khi ảnh hưởng phép thử sắp làm. H04/H05 đã chốt, không hỏi lại. E02a đã có đề cương cụ thể; chưa có kết quả thực thi.
2. Khảo sát K01–K05/K09 bằng nguồn chính thức; đề xuất phương án thử, quyền/cài đặt cần thêm và chi phí nếu có. Không cài tiện ích/model hay dùng dịch vụ có phí chỉ vì đề cương nhắc đến.
3. E01 và E02 trước; E03/E04 khi đường quyền đủ an toàn; E06 phần kịch bản có thể rà sớm, phần dữ liệu cần khảo sát K07.
4. E05 cuối, chỉ sau khi các luồng hẹp có kết quả. Dừng nếu có hành động ngoài quyền hoặc lộ dữ liệu thử bị chặn; sửa nguyên nhân trước đo tiếp.
5. Trình bằng chứng và điểm không đạt cho người dùng. Rồi mới hoàn thiện cấu hình mục tiêu, tiêu chí nghiệm thu định lượng, đặc tả từng khả năng và kế hoạch xây sản phẩm.

<details>
<summary>Ghi chú kỹ thuật và kiểm chứng của lượt chuẩn bị</summary>

- Phạm vi lượt này: tài liệu Markdown, README và bộ nhớ; không đổi permissions.html/JSON gốc, không viết code nhân vật.
- Workspace hiện chưa có code app hoặc Graphify, nên chưa có God Node/call edge để báo. Không giả lập graph hoặc tự tạo schema/framework.
- Không có public API/types thực thi được thêm/sửa. Mã SP/NV/SH/QD/DK/BH/XP/AI/KN/QH/HS/SL/CD là mã yêu cầu tài liệu, không wire format.
- Ma trận tình huống UI cần kiểm chứng sau: ban đầu chưa cấp quyền; đang tải/thực hiện có dừng; đang dở vì người dùng giành input; lỗi/thiếu quyền; xong có xác minh kết quả. Không coi ma trận là UI đã xây.
- Kiểm tra hiện tại: đường dẫn tài liệu nội bộ, tính duy nhất mã yêu cầu, tham chiếu H/K/T/E, JSON gốc và trạng thái chưa chạy. Chưa có lệnh build/test ứng dụng để liệt kê.

</details>
