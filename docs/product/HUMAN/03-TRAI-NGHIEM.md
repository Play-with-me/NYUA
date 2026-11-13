# Các lần sử dụng và phác thảo màn hình

Phác thảo nghiệp vụ, chưa phải UI đã được duyệt. Giữ màu/chữ/khoảng cách từ DESIGN.md khi triển khai; không biến trang cài đặt thành bảng chỉ số tâm trạng.

## 1. Mở lần đầu

Bạn cài app → đặt tên cô ấy → chọn có khởi động cùng Windows không → xem mức máy được đề xuất → bắt đầu với bản nhẹ. Gói nâng cao chỉ tải khi chọn và biết dung lượng thực. Bước cấp quyền có thể thực hiện sau: cô ấy vẫn sinh hoạt khi chưa cho xem app nào. Không bắt kết nối tài khoản/AI ngoài để dùng cơ bản.

```text
┌ Lần đầu gặp nhau ────────────────────────────┐
│ Tên của cô ấy: [...........................] │
│ [ ] Mở cùng Windows                         │
│ Mức phù hợp được đề xuất: [sau kiểm tra máy] │
│ [Bắt đầu sinh hoạt]  [Xem hai mức]           │
└─────────────────────────────────────────────┘
```

Thiết kế số bước onboarding, giới hạn ký tự tên và cách kiểm tra tên còn là chi tiết thiết kế cần rà, không đã chốt bằng phác thảo này.

## 2. Nơi mở cài đặt

Bấm biểu tượng khay hệ thống mở thẳng cửa sổ cài đặt đầy đủ. Windows quyết định biểu tượng nằm ngoài hay trong phần mũi tên; app không hứa ép được vị trí đó. Chuột trái vào cô ấy để phản ứng; chuột phải mở menu nhỏ **Đồ ăn / Dọn đồ**.

```text
Cài đặt nhân vật
├─ Nhân vật: tên, kích thước, màn hình, hiện/ẩn
├─ Mức hoạt động: cơ bản/nâng cao, gói và kiểm tra máy
├─ Quyền: ứng dụng, website, nguồn video đã chỉ
├─ Bài học và hàng đợi
├─ Ký ức: xem, sửa, xóa, ghim
├─ Quan hệ: lãng mạn tùy chọn; không bảng chỉ số
├─ Hồ sơ và xuất/nhập sao lưu
├─ Lịch sử thao tác: xem/xóa, tự xóa sau 30 ngày
└─ Khởi động, cập nhật, hướng dẫn và các nút dừng
```

Đây là cách nhóm màn hình đề xuất, các hành vi bên trong giữ theo yêu cầu gốc.

## 3. Cho cô ấy đọc một website

Bạn bật Đọc cho Chrome/Edge rồi dán link và bật Đọc cho website. Nếu bật Điều khiển trước Đọc, app giải thích cần Đọc, không tự bật thay. Nếu website chưa có quyền, cô ấy không tự cấp vì vừa thấy bạn mở nó.

```text
┌ Quyền truy cập ─────────────────────────────────┐
│ Ứng dụng                   Đọc     Điều khiển   │
│ Google Chrome              [ ]     [ ]          │
│ Microsoft Edge             [ ]     [ ]          │
│ Website [Dán địa chỉ................] [Thêm]    │
│ website bạn đã thêm         [ ]     [ ]          │
│ Giải thích: cần quyền ở cả trình duyệt và web.  │
└─────────────────────────────────────────────────┘
```

Khi không chắc đã loại hết thông tin nhạy cảm: báo lý do, không đọc cửa sổ; cô ấy vẫn sinh hoạt. Bạn xử lý rồi bấm **Thử đọc lại**. Đổi cửa sổ hoặc hết thời gian không tự vượt chốt chặn.

## 4. Chăm sóc và sắp xếp desktop

Chuột phải → Đồ ăn → chọn món chính/ăn nhẹ/đồ uống → kéo từng món hoặc khay tới cô ấy. Có thể thích hoặc từ chối tùy sở thích/tâm trạng. Không mua đồ ăn bằng tiền thật.

Đồ ảo có thể nằm trên cửa sổ, tối đa 5 món để lại. Bạn kéo từng món hoặc gọi Dọn đồ. Nút nhanh cũng gọi cô ấy dọn bằng hoạt ảnh, không xóa tức thì. Cô ấy có thể trì hoãn theo tâm trạng; nếu vướng việc bạn vẫn có thể di chuyển đồ hoặc ẩn nhân vật/đồ.

## 5. Dạy và gọi một việc

Bạn bật chế độ hướng dẫn → tự làm mẫu một chuỗi trong cùng app/website → xem tóm tắt → chọn ý nghĩa cú bấm kết quả tìm kiếm nếu có → xác nhận lưu. Chưa xác nhận thì chưa có bài học được dùng.

```text
┌ Bài học: mở nội dung tìm kiếm ─────────────────┐
│ Phạm vi: [app / website đã xác định]           │
│ 1. Tìm ô tìm kiếm                             │
│ 2. Gõ [nội dung được đổi mỗi lần]              │
│ 3. Chọn: ( ) Kết quả đầu  ( ) Đúng mục đã chỉ │
│ [Xác nhận lưu bài học]  [Dạy lại]              │
└───────────────────────────────────────────────┘
```

Chọn bài học, nhập chữ tìm kiếm lần này rồi bấm Thực hiện. Cô ấy có thể trì hoãn một lần; yêu cầu lại thì làm nếu đủ quyền. Khi bạn dùng chuột/phím, cô ấy nhường; sau 60 giây im lặng mới xét tiếp. Gặp UI khác thì dừng bước lỗi, nhờ dạy lại; các việc khác độc lập có thể tiếp tục.

Hàng đợi hiển thị thứ tự và hủy từng việc. Sau Dừng khẩn cấp/Tắt quan sát/Ẩn phải bấm **Tiếp tục hàng đợi** riêng; bật chức năng lại chưa chạy việc cũ.

## 6. Xem cùng và tự chọn nội dung

Cô ấy có thể mang sofa/bắp ngô xem cùng, thay đổi nét mặt theo cảnh hiểu được. Nếu không nhìn được cảnh thì tự chọn ở lại hoặc đi chơi/ăn. Không tự ngắt phim của bạn. Bạn tự di chuyển cô ấy/sofa khi che phụ đề.

Ở nâng cao, sau mặc định 5 phút không thao tác, không có nhạc/video đang phát và đủ quyền, cô ấy được mở tab riêng trong trình duyệt bạn chọn. Giữ nguyên tab của bạn. Khi bạn quay lại, nội dung tiếp tục phát; cô ấy chỉ nhường điều khiển.

Đòi đăng nhập/trả tiền/xác minh thì tìm nội dung miễn phí khác, tối đa 3 nội dung. Tab quảng cáo không chắc thì không đóng; quay về tab phim. Nhận dạng nguồn video không chắc thì nhờ bạn chỉ và xác nhận.

## 7. Khi cô ấy tránh bạn

Vắng mặt hoặc tắt app không phạt quan hệ. Thiếu quan tâm chỉ tích lũy khi bạn thực sự thao tác, cô ấy hiện ở nâng cao; sau 60 giây không thao tác ngừng tính. Khoảng 48–72 giờ đủ điều kiện mới bắt đầu buồn tùy tin tưởng/tổn thương.

Giận nặng có thể tự ẩn, ngừng đọc/điều khiển. Bạn mở cài đặt để **Mời cô ấy ra** hoặc để đồ ăn/thú bông. Cô ấy có thể chưa nhận; làm lành cần vài buổi và cách đối xử tốt, không spam quà. Cài đặt/reset vẫn truy cập được.

## 8. Sao lưu và đổi hồ sơ

Bạn chủ động bấm xuất → đặt mật khẩu → cất mã khôi phục riêng. Bản xuất không chứa khóa AI hoặc quyền có thể tự áp ở máy mới. Không có backup tự động.

Nhập sao lưu tạo hồ sơ riêng, không trộn ký ức. Chỉ một cô ấy hoạt động; hồ sơ khác đóng băng hoàn toàn. Đổi hồ sơ báo rõ và hủy việc chưa xong. Reset chỉ hồ sơ đang chọn, gồm ký ức/quan hệ/trạng thái/bài học; giữ quyền chung và hồ sơ khác.

## 9. Điều người dùng luôn phải thấy rõ

Mỗi luồng có trạng thái chưa có dữ liệu, đang xử lý có hủy, đang dở, lỗi/bị chặn và hoàn tất. Nút phải nêu việc sẽ làm; lý do bị chặn phải chỉ được bước xử lý. Không ghi thành công khi chưa xác minh kết quả. Các lời giải thích chức năng có chữ; không thêm lời thoại sinh hoạt cho cô ấy.
