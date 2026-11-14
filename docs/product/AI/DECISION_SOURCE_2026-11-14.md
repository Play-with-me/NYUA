# Exact user decision evidence — 2026-11-14

Historical append sequence: later clarification overrides earlier uncertainty. This is evidence, not a second requirements registry. Source originals preserved.

## Quyết định trực tiếp của người dùng — 2026-11-14 (ghi chú điều phối)

- D-12 đã chốt: Khi nhân vật ngủ thì dừng quan sát; thức dậy mới tiếp tục trong phạm vi quyền đã cấp. Không cấp thêm quyền hoặc bỏ qua SafetyHold/Thử đọc lại.
- D-10 chốt phần trải nghiệm khôi phục việc: Khi mở lại ứng dụng, giữ việc đang dở tạm dừng và hỏi người dùng có muốn tiếp tục; không tự chạy lại. Tiếp tục vẫn phải kiểm tra quyền và điều kiện an toàn hiện hành. Các vấn đề crash khi ghi dữ liệu/cập nhật chưa được quyết định bởi câu trả lời này.
- Đây là ghi nhận quyết định, không phải tính năng đã triển khai/kiểm chứng. Cần đồng bộ vào yêu cầu hiện hành, registry, DECISIONS và tiêu chí task; chưa báo đồng bộ xong. Cập nhật worker qua kênh thông thường đang bị SESSION_COMPOSER_BUSY.

## Quyết định trực tiếp của người dùng — D-17 — 2026-11-14

- Đã chốt: Khi người dùng sửa hoặc xóa bài học, dừng việc đang làm sử dụng bài học đó và hủy các lượt chờ dùng bài học đó. Muốn chạy tiếp người dùng sẽ giao lại; không tự chạy lại hoặc chuyển lượt cũ sang phiên bản mới.
- Phạm vi chỉ các việc dùng bài học bị sửa/xóa; không suy ra hủy các việc không liên quan. Không tuyên bố hoàn tác được những thao tác đã hoàn thành.
- Ghi nhận điều phối; chưa triển khai/kiểm chứng. Cần đồng bộ yêu cầu hiện hành, DECISIONS D-17, registry và task/tiêu chí nghiệm thu liên quan.

## Quyết định trực tiếp của người dùng — D-06 — 2026-11-14

- Đã chốt: Sau 3 nội dung phim/nhạc không mở được, nhân vật về sinh hoạt, chờ người dùng thao tác trở lại rồi chỉ thử tìm trong đợt vắng mặt tiếp theo. Không tự lặp tìm trong cùng đợt vắng mặt và không dùng bộ đếm chờ đơn thuần để mở lại lượt tìm.
- Đợt tiếp theo vẫn chịu điều kiện chờ, quyền và quy tắc không làm gián đoạn nội dung đang phát đã chốt; không tự mở rộng quyền. Giữ quy tắc hiện hành về thao tác người dùng và mở khóa máy.
- Ghi nhận điều phối; chưa triển khai/kiểm chứng. Cần đồng bộ yêu cầu hiện hành, DECISIONS D-06, registry và task/tiêu chí nghiệm thu liên quan.

## Quyết định trực tiếp của người dùng — D-11 — 2026-11-14

- Đã chốt: Không tính thời gian máy ngủ vào thời gian chờ tự mở phim/nhạc. Khi máy thức, bộ đếm tiếp tục phần thời gian còn lại, không tính thời gian ngủ và không tự đặt lại từ đầu chỉ vì máy thức.
- Chỉ quyết định bộ đếm chờ mở nội dung; các điều kiện quyền, khóa máy, nội dung đang phát và thao tác người dùng vẫn áp dụng như đã chốt. Không đồng nhất máy ngủ với nhân vật ngủ.
- Ghi nhận điều phối; chưa triển khai/kiểm chứng. Cần đồng bộ yêu cầu hiện hành, DECISIONS D-11, registry và task/tiêu chí nghiệm thu liên quan.

## Quyết định trực tiếp của người dùng — D-18 — 2026-11-14

- Đã chốt: Nếu gửi chữ tới AI bên ngoài bị lỗi hoặc chưa rõ thành công, báo lỗi và chờ người dùng bấm thử lại. Người dùng phải xem và duyệt chữ trước mỗi lần gửi mới; không tự gửi lại, kể cả nội dung không đổi.
- Không tự coi timeout là dịch vụ chưa nhận. Quyết định này chốt hành vi thử lại và duyệt từng lần gửi chữ; không mở rộng loại dữ liệu được gửi hoặc quyền dùng dịch vụ bên ngoài.
- Ghi nhận điều phối; chưa triển khai/kiểm chứng. Cần đồng bộ yêu cầu hiện hành, DECISIONS D-18, registry và task/tiêu chí nghiệm thu liên quan.

## Quyết định trực tiếp của người dùng — D-16 — 2026-11-14

- Đã chốt: Cho phép kiểm tra riêng trạng thái đang phát/không phát ở nền để tránh mở chồng nội dung; không đọc tên bài/phim, hình ảnh hay âm thanh.
- Quyền kiểm tra tối thiểu này chỉ phục vụ điều kiện tránh mở chồng, không cấp quyền đọc nội dung cửa sổ nền, suy ra sở thích, lịch sử nghe/xem hoặc phân tích âm thanh. Cách lấy trạng thái và độ tin cậy cần kiểm chứng; không coi lỗi/không xác định là chắc chắn không phát.
- Ghi nhận điều phối; chưa triển khai/kiểm chứng. Cần đồng bộ yêu cầu hiện hành, DECISIONS D-16, registry và task/tiêu chí nghiệm thu liên quan.

## Quyết định trực tiếp của người dùng — D-05 (phím chuyển vị trí) — 2026-11-14

- Đã chốt: Giữ Shift rồi kéo để chuyển vị trí nhân vật, kể cả khi nhân vật đang từ chối cho nhấc. Không tính là chơi/quăng và không ảnh hưởng quan hệ.
- Không suy ra bổ sung mục tự chọn phím. Chỉ chốt phím và ý nghĩa thao tác; ngưỡng cử chỉ, nhịp mời tương tác và các phần còn lại của D-05 chưa được chốt bởi câu trả lời này.
- Ghi nhận điều phối; chưa triển khai/kiểm chứng. Cần đồng bộ NV11 trong yêu cầu hiện hành, DECISIONS D-05, registry và task/tiêu chí nghiệm thu liên quan.

## Quyết định trực tiếp của người dùng — D-02 (phục hồi hình ảnh) — 2026-11-14

- Đã chốt: Nếu hình ảnh nhân vật bị lỗi rồi phục hồi, giữ việc đang dở tạm dừng và hỏi người dùng trước khi tiếp tục; không tự chạy lại.
- Trong lúc hình ảnh lỗi, các thao tác lên ứng dụng khác tạm dừng theo tình huống đã hỏi. Khi được người dùng cho tiếp tục vẫn phải kiểm tra quyền/điều kiện an toàn hiện hành; không phát lại thao tác cũ một cách mù quáng.
- Chỉ chốt trải nghiệm phục hồi việc sau lỗi hình ảnh; không tự coi toàn bộ hợp đồng kết nối, hàng đợi và xử lý mất kết nối D-02 đã hoàn tất.
- Ghi nhận điều phối; chưa triển khai/kiểm chứng. Cần đồng bộ yêu cầu hiện hành, DECISIONS D-02, registry và task/tiêu chí nghiệm thu liên quan.

## Quyết định trực tiếp của người dùng — D-09 (gói AI trong sao lưu) — 2026-11-14

- Đã chốt: Không kèm gói AI nâng cao trong bản sao lưu; máy mới tải lại khi cần.
- Không suy ra loại bỏ dữ liệu nhân vật, ký ức hoặc thiết lập đã thuộc phạm vi sao lưu. Không thêm lựa chọn kèm gói AI vào mỗi lần xuất. Quyền trên máy và khóa AI bên ngoài vẫn không mang sang theo quy tắc hiện hành.
- Chỉ chốt phần gói AI nâng cao; danh sách thiết lập, tài nguyên khác và tương thích phiên bản trong D-09 vẫn cần đặc tả riêng.
- Ghi nhận điều phối; chưa triển khai/kiểm chứng. Cần đồng bộ yêu cầu hiện hành, DECISIONS D-09, registry và task/tiêu chí nghiệm thu liên quan.

## Quyết định trực tiếp của người dùng — H03 / D-05 (buổi làm lành) — 2026-11-14

- Đã chốt: Các buổi làm lành có thể diễn ra trong cùng một ngày nếu có khoảng nghỉ và tương tác thật; đóng/mở app hoặc tặng quà liên tục không tính là buổi mới.
- Không bắt buộc qua nhiều ngày lịch. Không suy ra số phút nghỉ, số buổi cố định, hoặc một tương tác/quà lập tức xóa tổn thương; các tham số còn lại cần đề xuất và kiểm chứng trải nghiệm.
- Ghi nhận điều phối; chưa triển khai/kiểm chứng. Cần đồng bộ yêu cầu hiện hành QH05, DIEM_CHUA_CHAC H03, DECISIONS D-05, registry và task/tiêu chí nghiệm thu liên quan.

## Mô tả trực tiếp của người dùng — người cáo — 2026-11-14

- Nguyên ý người dùng: Là người cáo, khuôn mặt, đi đứng, dáng người, đa số là người, chỉ một số như đuôi, tai cáo thôi.
- Đã ghi nhận mô tả hình thái chủ yếu là người với tai/đuôi cáo. Chưa xác định đối tượng: câu hỏi trước là thú bông, nhưng mô tả có đi đứng/dáng người có thể chỉ nhân vật chính. Phải hỏi rõ trước khi sửa ngoại hình NV hoặc chốt thú bông H08/D-14.
- Không tự thay các quyết định ngoại hình cũ, không tự suy ra mặt/mõm cáo, bàn chân động vật hay thay trang phục. Chưa triển khai hoặc đồng bộ thành yêu cầu ngoại hình đã chốt.

## Quyết định trực tiếp của người dùng — nhân vật chính người cáo — 2026-11-14

- Đã làm rõ: Mô tả người cáo ở lượt trước dành cho nhân vật chính sống trên desktop, không phải thú bông. Người dùng yêu cầu kết hợp với các phần ngoại hình đã chốt trong dự án.
- Nhân vật chính chủ yếu giống người về khuôn mặt, dáng người và cách đi đứng; bổ sung tai cáo và đuôi cáo. Không tự biến thành cáo toàn thân hoặc thêm mõm cáo/bàn chân động vật.
- Giữ các lựa chọn hiện hành: nữ trưởng thành chibi anime pixel, ảnh gốc 128x128, tóc trắng bạc ngang eo/mái thưa, mắt đỏ hồng, da sáng ấm, áo len rộng hồng nhạt, váy xếp ly xám đậm trên gối, chân trần, kẹp tim đỏ rượu bên phải nhân vật. Các mô tả màu/số lượng đuôi và cấu trúc tai chưa được chốt.
- Ghi chú trước về đối tượng chưa rõ đã được giải quyết. Loại thú bông H08/D-14 vẫn chưa chốt; không lấy mô tả nhân vật này làm lựa chọn thú bông.
- Ghi nhận điều phối; chưa triển khai/kiểm chứng. Cần đồng bộ NV trong yêu cầu hiện hành, ART, registry, HUMAN và task tài sản/tiêu chí nghiệm thu liên quan.

## Quyết định trực tiếp của người dùng — màu tai/đuôi cáo — 2026-11-14

- Đã chốt: Tai và đuôi cáo của nhân vật chính màu trắng bạc, lòng tai hồng nhạt, đồng bộ với tóc.
- Giữ nguyên các phần ngoại hình đã chốt, gồm hình người là chủ yếu, nữ trưởng thành chibi anime pixel 128x128, tóc trắng bạc ngang eo/mái thưa, mắt đỏ hồng, da sáng ấm, áo len rộng hồng nhạt, váy xếp ly xám đậm, chân trần và kẹp tim đỏ rượu bên phải nhân vật.
- Không tự suy ra số đuôi, kích thước đuôi hoặc bổ sung màu/chóp đuôi khác. Các phần này chưa được người dùng chốt.
- Ghi nhận điều phối; chưa triển khai/kiểm chứng. Cần đồng bộ yêu cầu hiện hành, ART, registry, HUMAN và task tài sản/tiêu chí nghiệm thu liên quan.

## Quyết định trực tiếp của người dùng — số đuôi cáo — 2026-11-14

- Đã chốt: Nhân vật chính có một đuôi cáo trắng bạc. Giữ nguyên toàn bộ phần ngoại hình đã chốt trước đó.
- Tổng hợp phần bổ sung: hình người là chủ yếu; tai cáo trắng bạc, lòng tai hồng nhạt; một đuôi cáo trắng bạc đồng bộ với tóc. Không tự thêm đuôi hoặc thay tóc, mắt, da, trang phục, kẹp tóc, chân trần và phong cách chibi anime pixel hiện hành.
- Ghi nhận điều phối; chưa triển khai/kiểm chứng. Cần đồng bộ yêu cầu hiện hành, ART, registry, HUMAN và task tài sản/tiêu chí nghiệm thu liên quan.

## Quyết định trực tiếp của người dùng — cấu trúc tai — 2026-11-14

- Đã chốt: Nhân vật chính chỉ có đôi tai cáo trên đầu, không có tai người. Tai trắng bạc, lòng tai hồng nhạt như đã chốt.
- Giữ nguyên toàn bộ ngoại hình còn lại: chủ yếu hình người, một đuôi cáo trắng bạc, nữ trưởng thành chibi anime pixel, tóc/mắt/da/trang phục/kẹp tóc/chân trần theo quyết định hiện hành.
- Ghi nhận điều phối; chưa triển khai/kiểm chứng. Cần đồng bộ yêu cầu hiện hành, ART, registry, HUMAN và task tài sản/tiêu chí nghiệm thu liên quan. Thú bông vẫn là lựa chọn riêng chưa chốt.

## Quyết định trực tiếp của người dùng — H08 / D-14 (thú bông) — 2026-11-14

- Đã chốt: Chọn thú bông thỏ làm mẫu thú bông cho bản đầu. Đây là đồ vật/quà tặng riêng để nhân vật ôm, không thay đổi nhân vật chính.
- Giữ nguyên ngoại hình nhân vật đã chốt: chủ yếu hình người; chỉ đôi tai cáo trên đầu, không tai người; tai trắng bạc/lòng tai hồng nhạt; một đuôi cáo trắng bạc; các phần tóc, mắt, da, trang phục, kẹp tóc, chân trần và phong cách chibi anime pixel hiện hành không đổi.
- Chưa chốt màu/chi tiết thú bông, loại trái cây/đồ uống/dụng cụ khác trong H08/D-14. Không coi toàn bộ danh mục tài sản đã duyệt.
- Ghi nhận điều phối; chưa triển khai/kiểm chứng. Cần đồng bộ yêu cầu hiện hành, ART, registry, HUMAN và task tài sản/tiêu chí nghiệm thu liên quan.

## Quyết định trực tiếp của người dùng — H08 / D-14 (trái cây) — 2026-11-14

- Đã chốt: Chọn táo làm món trái cây cho bản đầu, cụ thể hóa mục trái cây trong sáu món SH04; không thêm món thứ bảy.
- Giữ nguyên thú bông thỏ, toàn bộ ngoại hình nhân vật và các lựa chọn sản phẩm đã chốt. Chưa chốt loại nước trái cây hoặc toàn bộ chi tiết tài sản khác trong H08/D-14.
- Ghi nhận điều phối; chưa triển khai/kiểm chứng. Cần đồng bộ yêu cầu hiện hành SH04, ART, registry, HUMAN và task tài sản/tiêu chí nghiệm thu liên quan.

## Quyết định trực tiếp của người dùng — H08 / D-14 (nước trái cây) — 2026-11-14

- Đã chốt: Chọn nước cam cho bản đầu, cụ thể hóa mục nước trái cây trong sáu món SH04; không thêm món mới ngoài danh mục đã chốt.
- Giữ nguyên táo, thú bông thỏ, toàn bộ ngoại hình nhân vật người cáo và các lựa chọn sản phẩm đã chốt. Không suy ra các chi tiết hình vẽ chưa được duyệt là chính thức.
- Ghi nhận điều phối; chưa triển khai/kiểm chứng. Cần đồng bộ yêu cầu hiện hành SH04, ART, registry, HUMAN và task tài sản/tiêu chí nghiệm thu liên quan.
