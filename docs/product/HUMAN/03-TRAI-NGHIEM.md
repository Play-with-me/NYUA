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

<!-- CONFIRMED-2026-11-14 -->
## Quyết định hiện hành 2026-11-14 — ưu tiên hơn wording nháp cũ

Sinh từ registry; chỉ phần sau nhãn quyết định là bổ sung đã xác nhận. Chưa triển khai/chưa nghiệm thu; chi tiết kỹ thuật còn mở trong DECISIONS.

- **SP09:** D-02: Hình ảnh lỗi thì tạm dừng thao tác lên app khác; phục hồi vẫn tạm dừng và hỏi trước tiếp tục, kiểm quyền/an toàn mới. Không phát lại mù quáng; hợp đồng kết nối/mất kết nối còn mở.
- **NV01:** D-14: Nhân vật chính chủ yếu hình người về mặt/dáng/đi đứng, không mõm cáo/bàn chân động vật. Chỉ đôi tai cáo trên đầu, không tai người; tai trắng bạc lòng hồng nhạt; một đuôi cáo trắng bạc. Giữ nữ trưởng thành chibi anime pixel 128x128, tóc trắng bạc ngang eo/mái thưa, mắt đỏ hồng, da sáng ấm, áo len rộng cổ tròn hồng nhạt, váy xếp ly xám đậm trên gối, chân trần, kẹp tim đỏ rượu bên phải nhân vật.
- **NV02:** D-14: Giữ tóc/mắt/da đã chốt; tai trắng bạc lòng hồng nhạt và một đuôi trắng bạc đồng bộ tóc. Chỉ tai cáo, không tai người; không thay ngoại hình đã duyệt.
- **NV11:** D-05: Giữ Shift rồi kéo chuyển vị trí kể cả khi từ chối nhấc; không chơi/quăng hay ảnh hưởng quan hệ, không thêm tùy chọn phím; ngưỡng cử chỉ còn phải đo.
- **SH01:** D-12: Khi nhân vật ngủ dừng quan sát; thức dậy chỉ tiếp tục trong quyền hiện hành, không vượt SafetyHold/Thử đọc lại.
- **SH04:** D-14/H08: Trong sáu món đã chốt, trái cây là táo, nước trái cây là nước cam; không thêm món thứ bảy. Thú bông thỏ là đồ vật/quà riêng, không nhân vật chính. Màu/chi tiết thú bông, dụng cụ/hình mẫu còn chờ duyệt.
- **QD04:** D-12: Nhân vật ngủ dừng quan sát; thức dậy không tự cấp quyền hoặc bỏ qua SafetyHold/Thử đọc lại.
- **BH02:** D-17: Sửa/xóa bài học dừng việc đang dùng và hủy lượt chờ dùng bài học đó; người dùng giao lại, không chuyển lượt cũ sang phiên bản mới, không hủy việc không liên quan hoặc hoàn tác thao tác đã xong.
- **BH06:** D-02/D-10/D-17: Renderer lỗi thì tạm dừng thao tác app khác; hình ảnh phục hồi hoặc mở lại app giữ việc tạm dừng và hỏi trước tiếp tục, kiểm quyền/an toàn mới, không phát lại mù quáng. Sửa/xóa bài học dừng việc đang dùng và hủy lượt chờ dùng bài học đó, phải giao lại; không hủy việc không liên quan hoặc hoàn tác việc đã xong.
- **XP05:** D-16: Được kiểm trạng thái đang phát/không phát ở nền tối thiểu để tránh mở chồng; không đọc tên/nội dung hoặc suy gu. Lỗi/không xác định không coi là không phát; API/độ tin cậy cần kiểm chứng.
- **XP07:** D-06: Sau 3 nội dung không mở được về sinh hoạt; chờ người dùng thao tác trở lại rồi chỉ tìm trong đợt vắng mặt tiếp theo. Không tìm lặp cùng đợt hoặc chỉ dùng bộ đếm để mở lại tìm kiếm; quyền/chờ/không gián đoạn vẫn áp dụng.
- **XP08:** D-11: Máy ngủ không cộng thời gian chờ mở phim/nhạc; máy thức tiếp tục phần còn lại, không reset chỉ vì thức. Giữ quyền/khóa/input/phát đã chốt, máy ngủ khác nhân vật ngủ.
- **AI01:** D-16: Chỉ kiểm tra trạng thái đang phát/không phát ở nền để tránh mở chồng; không tên bài/phim/hình/âm thanh/lịch sử hoặc suy gu; lỗi/không rõ không coi là không phát. Cách lấy/độ tin cậy cần kiểm chứng.
- **AI02:** D-18: Gửi chữ lỗi/chưa rõ thành công thì báo lỗi và chờ bấm thử lại; xem/duyệt chữ trước mỗi lần gửi mới kể cả chữ không đổi. Không tự gửi lại, không coi timeout là chưa nhận, không mở rộng loại dữ liệu/quyền.
- **QH05:** D-05/H03: Buổi làm lành có thể cùng ngày nếu có khoảng nghỉ và tương tác thật; đóng/mở app hoặc quà liên tục không là buổi mới. Không tự đặt số phút/số buổi hoặc quà lập tức xóa tổn thương.
- **SL01:** D-09: Sao lưu không kèm gói AI nâng cao; máy mới tải lại khi cần, không thêm tùy chọn kèm gói mỗi lần xuất. Giữ dữ liệu nhân vật/ký ức/thiết lập thuộc phạm vi; quyền máy/khóa AI ngoài không mang sang. Whitelist/tài nguyên khác/tương thích còn phải đặc tả.
- **CD01:** D-10: Mở lại app giữ việc đang dở tạm dừng, hỏi trước tiếp tục; không tự chạy lại, vẫn kiểm quyền/an toàn hiện hành. Crash ghi dữ liệu/cập nhật còn cần khảo sát.
