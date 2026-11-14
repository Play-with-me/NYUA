# Yêu cầu hiện hành — nhân vật sống trên desktop

Cập nhật: 2026-11-14. Trạng thái: **hợp nhất kết quả phỏng vấn để rà soát**, chưa phải đặc tả kỹ thuật đã duyệt hoặc cam kết mọi khả năng đều khả thi.

Đã có mẫu E02a C# + WPF trên dữ liệu giả, chưa có ứng dụng nhân vật đầy đủ. Người dùng hiện yêu cầu bộ hồ sơ toàn sản phẩm riêng cho người đọc và AI, gồm SRS, sơ đồ và task chi tiết. Tài liệu mới ở docs/product là baseline để rà, không tự cho triển khai các phần chưa kiểm chứng.

## 1. Cách sử dụng tài liệu

- Đây là nơi tra yêu cầu hiện hành. Ghi chép phỏng vấn và JSON gốc giữ làm lịch sử.
- Quyết định cụ thể mới hơn thay quyết định cũ về cùng vấn đề. Nội dung chưa xác định được ghi ở [Điểm chưa chắc](DIEM_CHUA_CHAC.md), không tự điền thành yêu cầu.
- [Đề cương kiểm chứng](KE_HOACH_KIEM_CHUNG.md) phân biệt từng phép thử; E02a có kết quả kỹ thuật hẹp, còn kiểm tra UI/nghiệm thu. Không có bằng chứng đã đạt các phép thử toàn sản phẩm.
- Những quyền mô tả ở đây dành cho sản phẩm tương lai, không phải giấy phép cho AI hiện tại truy cập hoặc điều khiển máy.
- Không tự chốt tên chính thức, chi tiết công nghệ/phiên bản, mô hình AI, cấu hình tối thiểu, thời hạn phát hành hay chi phí. Hướng công cụ đã thống nhất ở SP09 không chứng minh mọi chi tiết đã khả thi.

## 2. Mục tiêu, đối tượng và phạm vi phát hành

| Mã | Yêu cầu đã chốt |
|---|---|
| SP01 | Tạo cảm giác một người bạn có cá tính sống trên máy: hoạt bát, tò mò, tinh nghịch, tự chọn hoạt động theo nhu cầu, tâm trạng, sở thích và ký ức; có thể đổi ý có lý do. Không phải cam kết có ý thức thật. |
| SP02 | Bản dùng thử có ý nghĩa phải kết hợp sinh hoạt/ghi nhớ, hiểu màn hình và chuyển động/tương tác tự nhiên. Chỉ hoạt ảnh đi lại chưa đủ. |
| SP03 | Phát hành công khai cho nhiều người trên Windows 11, giao diện tiếng Việt và thị trường Việt Nam trước; quốc tế để sau. Miễn phí bản đầu; chỉ phát hành ứng dụng, chưa công khai mã nguồn. |
| SP04 | Không tài khoản riêng của ứng dụng; dữ liệu trên máy. Người dùng tự kết nối và trả chi phí AI ngoài nếu dùng. |
| SP05 | Không hạn phát hành cố định. Cả cơ bản và nâng cao phải ổn định trước phát hành công khai; có thể kiểm chứng bằng bản thử nội bộ trước. |
| SP06 | Ưu tiên công cụ/dịch vụ miễn phí; mọi khoản chi phát triển phải hỏi trước. Chưa có ngân sách số cụ thể hoặc quyền tự chi. |
| SP07 | Ở nâng cao, tính cách phát triển qua trải nghiệm/cách đối xử: từ làm trước nghĩ sau dần biết cân nhắc. Luôn giữ tò mò, tinh nghịch và ý muốn riêng; thay đổi cách thể hiện, không xóa các nét cốt lõi này. Cơ bản giữ tính cách ban đầu, vẫn đổi tâm trạng. Không phải quyền tự sửa code. |
| SP08 | Học cách hành xử qua tương tác và trải nghiệm, không thêm nút đánh giá hành vi. Không tự đánh đồng người dùng bận/không đáp lời rủ với phê bình; chế độ làm mẫu thao tác ứng dụng vẫn là chức năng riêng. |
| SP09 | Hướng đã thống nhất để tiếp tục: Unity phụ trách hiển thị/hoạt ảnh nhân vật; C# + WPF phụ trách phần ứng dụng, điều phối và quản lý; AI local phân tích ngữ cảnh/cảm xúc. Phiên bản, cách kết nối, topology tiến trình, hiệu năng và độ tin cậy còn cần thiết kế/kiểm chứng. Không xây giao diện sản phẩm bằng web theo đề xuất cũ. Quyết định 2026-11-14 D-02: Hình ảnh lỗi thì tạm dừng thao tác lên app khác; phục hồi vẫn tạm dừng và hỏi trước tiếp tục, kiểm quyền/an toàn mới. Không phát lại mù quáng; hợp đồng kết nối/mất kết nối còn mở. |

## 3. Ngoại hình và chuyển động

| Mã | Yêu cầu đã chốt |
|---|---|
| NV01 | Nữ trưởng thành kiểu chibi, đầu lớn người nhỏ, phong cách anime đời thường. Một mẫu ngoại hình trong bản đầu cho mọi người dùng. Quyết định 2026-11-14 D-14: Nhân vật chính chủ yếu hình người về mặt/dáng/đi đứng, không mõm cáo/bàn chân động vật. Chỉ đôi tai cáo trên đầu, không tai người; tai trắng bạc lòng hồng nhạt; một đuôi cáo trắng bạc. Giữ nữ trưởng thành chibi anime pixel 128x128, tóc trắng bạc ngang eo/mái thưa, mắt đỏ hồng, da sáng ấm, áo len rộng cổ tròn hồng nhạt, váy xếp ly xám đậm trên gối, chân trần, kẹp tim đỏ rượu bên phải nhân vật. |
| NV02 | Tóc trắng bạc buông ngang eo, mái thưa ngang trán; mắt đỏ hồng; da sáng tông ấm. Quyết định 2026-11-14 D-14: Giữ tóc/mắt/da đã chốt; tai trắng bạc lòng hồng nhạt và một đuôi trắng bạc đồng bộ tóc. Chỉ tai cáo, không tai người; không thay ngoại hình đã duyệt. |
| NV03 | Áo len rộng cổ tròn hồng nhạt; chân váy xếp ly xám đậm trên gối; chân trần, không tất/giày. |
| NV04 | Kẹp tóc nhỏ hình trái tim đỏ rượu ở bên phải nhân vật, tức phía trái khi nhìn chính diện. Nét mặt thường ngày cười tươi, nhiều năng lượng. |
| NV05 | Ảnh gốc pixel 128×128; giữ nét pixel, chuyển động mượt mềm mại. Chưa chốt số khung hình, nguồn ảnh hoặc kỹ thuật tạo hoạt ảnh. |
| NV06 | Thanh kéo kích thước tự do 64×64–384×384; ban đầu 128×128, nhớ kích thước người dùng chỉnh. Người dùng tự đặt tên khi mở lần đầu. |
| NV07 | Sống tự do trên desktop, đi/leo/ngồi trên cạnh cửa sổ. Theo cửa sổ khi di chuyển; mất chỗ đứng vì cửa sổ đóng/thu nhỏ thì rơi xuống bề mặt bên dưới, đứng dậy. |
| NV08 | Người dùng chọn các màn hình được xuất hiện; nhân vật tự qua lại trong phạm vi đó. Toàn màn hình vẫn hiện sát mép, tránh vùng giữa. |
| NV09 | Bấm trái nhận biểu cảm/cử chỉ; rê qua đầu nhiều lần để vuốt; giữ kéo để nhấc. Kéo nhẹ đổi chỗ; kéo nhanh thả bay theo đà; thả giữa khoảng trống thì rơi. |
| NV10 | Để bấm nút thật phải đến vị trí nút trước, chấp nhận thời gian di chuyển; dùng thang/dụng cụ ảo khi thiếu chỗ tiếp cận. Khi gõ thật có hoạt ảnh bàn phím nhỏ trên tay. |
| NV11 | Giữ một phím rồi kéo là chế độ chuyển vị trí, dùng được cả khi cô ấy đang từ chối cho nhấc; không tính chơi/quăng hoặc làm xấu quan hệ. Phím đã chốt là Shift. Quyết định 2026-11-14 D-05: Giữ Shift rồi kéo chuyển vị trí kể cả khi từ chối nhấc; không chơi/quăng hay ảnh hưởng quan hệ, không thêm tùy chọn phím; ngưỡng cử chỉ còn phải đo. |

## 4. Phân chia hai mức

| Khả năng | Cơ bản | Nâng cao |
|---|---|---|
| Sinh hoạt | Đi lại, leo/ngồi cửa sổ, ăn uống, ngủ/nghỉ, vuốt ve và nhấc thả | Có cơ bản và thêm hoạt động dưới đây |
| Sở thích bằng hoạt ảnh | Các hoạt động cơ bản | Đọc sách, vẽ, thú bông, máy game ảo, ca hát không tiếng, khối xếp hình; sofa xem phim |
| Nội dung sách/tranh/game | Không yêu cầu | Chỉ hoạt ảnh; không tạo sách/tranh thật hoặc chơi game thật |
| Hiểu màn hình | App, chữ, nút; ngữ cảnh đơn giản | Hiểu cảnh phim/cảm xúc sâu hơn |
| Điều khiển ứng dụng | Chỉ bài học người dùng trực tiếp gọi | Có tự khám phá trong quyền cấp; bài học vẫn chỉ gọi bằng yêu cầu |
| Tự mở phim/nhạc | Không | Có, theo điều kiện mục 8 |
| Cảm xúc/quan hệ | Tâm trạng, thân thiết; phản đối và từ chối nhấc | Quan hệ sâu, tổn thương lâu dài, tự ẩn vì xa cách; lãng mạn tùy chọn |
| Phát triển tính cách | Giữ tính cách ban đầu, vẫn đổi tâm trạng | Tính cách phát triển lâu dài theo SP07 |
| Mất Internet | Hoạt động với nội dung cục bộ | Sau tải đủ gói vẫn hoạt động với nội dung cục bộ |

- **MC01:** cài bản nhẹ trước; chỉ tải gói nâng cao khi người dùng chọn. Dung lượng và yêu cầu máy phải được khảo sát trước khi công bố.
- **MC02:** máy chưa đạt cấu hình đã kiểm chứng vẫn được bật thử sau cảnh báo rõ; không tự đổi mức. Khi nâng cao làm máy chậm/nóng thì báo và hỏi giảm mức hay tiếp tục.
- **MC03:** hạ về cơ bản giữ ký ức/quan hệ và phần tính cách đã phát triển, tạm ngừng biểu hiện nâng cao. Bật lại tiếp nối tính cách đã phát triển, không bắt đầu từ đầu. Tương tác ở cơ bản vẫn duy trì quan hệ; thiếu tương tác ở cơ bản không làm giảm quan hệ sâu.
- **MC04:** kiểm tra cấu hình máy người dùng để đề xuất mức cơ bản/nâng cao phù hợp với AI cục bộ. Cách xếp mức và cấu hình tối thiểu cần dựa vào phép đo; không chỉ tên GPU. Giữ quyền chọn/bật thử sau cảnh báo và không tự đổi mức theo MC02.

## 5. Sinh hoạt, thức ăn và đồ vật

- **SH01:** ngủ theo giờ trong ngày và mức mệt, có ngủ trưa. Mở máy có thể ngái ngủ, chào rồi ngủ tiếp hoặc thức. Bấm lúc ngủ có thể hé mắt, trở mình hoặc thức tùy mệt. Quyết định 2026-11-14 D-12: Khi nhân vật ngủ dừng quan sát; thức dậy chỉ tiếp tục trong quyền hiện hành, không vượt SafetyHold/Thử đọc lại.
- **SH02:** người dùng cho ăn/vuốt, cô ấy tự nghỉ. Khi vắng mặt hoặc app đóng, không bệnh/mất tiến độ; có thể hơi đói/nhớ, tự có đồ dự phòng khi hoạt động.
- **SH03:** đóng app/tắt máy không mô phỏng sự kiện, không tự kể đã làm gì. Mở lại tính thời gian đã qua để cập nhật trạng thái; nguôi giận có tính thời gian app đóng, không tạo tương tác giả.
- **SH04:** 6 món miễn phí không giới hạn: cơm nắm, mì; trái cây, bắp ngô; sữa, nước trái cây. Chọn riêng để ghép bữa; kéo từng món hoặc cả khay. Có món thích/không thích, đôi khi từ chối, người dùng khám phá qua phản ứng. Quyết định 2026-11-14 D-14/H08: Trong sáu món đã chốt, trái cây là táo, nước trái cây là nước cam; không thêm món thứ bảy. Thú bông thỏ là đồ vật/quà riêng, không nhân vật chính. Màu/chi tiết thú bông, dụng cụ/hình mẫu còn chờ duyệt.
- **SH05:** thường thích vuốt nhưng có thể né/ra dấu đủ rồi. Biểu đạt bằng cử chỉ, nét mặt, biểu tượng nhỏ; không lời thoại/chữ sinh hoạt, không tiếng; không bảng chỉ số đói/mệt/thân thiết. Thông báo chức năng vẫn có chữ.
- **SH06:** rủ chơi/gây chú ý có thể ghé con trỏ, thò đầu hoặc ôm con trỏ bằng hoạt ảnh. Không kéo chuột thật/chuyển cửa sổ để nghịch. Hai lần không đáp thì tự chơi và chờ ít nhất 30 phút; trò nghịch và rủ dùng chung giới hạn. Không thêm chế độ tập trung riêng.
- **SH07:** tối đa 5 món đồ ảo để lại trên màn hình, không tính đồ cô ấy đang cầm/sử dụng. Khi đủ giới hạn, tự cất bớt đồ cũ bằng hoạt ảnh trước khi để thêm món mới. Đồ đều hiện trên cửa sổ; người dùng/cô ấy kéo từng món được, có lệnh dọn. Nút dọn nhanh và yêu cầu dọn đều gọi hoạt ảnh thu dọn, không biến mất ngay.
- **SH08:** tùy tâm trạng có thể chán, trì hoãn hoặc từ chối dọn; người dùng tự di chuyển hoặc ẩn cả nhân vật/đồ được. Quà dỗ là đồ ăn và thú bông đã có, không hệ thống quà mới.

## 6. Quyền đọc và bảo vệ dữ liệu

| Mã | Quy tắc hiện hành |
|---|---|
| QD01 | Người mới cài chỉ có sinh hoạt; quyền truy cập mặc định tắt. Mỗi app/website tách Đọc và Điều khiển; phải bật Đọc trước mới bật Điều khiển, không tự cấp Đọc. |
| QD02 | Quét app trên máy để hiện danh sách; website do người dùng dán link. Cấp cho website gồm tên miền phụ; website khác cần riêng. Chrome/Edge cần quyền ở cả trình duyệt và website. |
| QD03 | App/website mới không tự kế thừa. Quyền chung cho ứng dụng, dùng chung các hồ sơ trên máy; không nhập quyền từ file sao lưu. |
| QD04 | Đọc nội dung các cửa sổ cùng đang nhìn thấy nếu đều được phép; không đọc cửa sổ/tab bị che hoặc thu nhỏ. Đọc toàn bộ không còn được hiểu là đọc nền mọi nơi. Quyết định 2026-11-14 D-12: Nhân vật ngủ dừng quan sát; thức dậy không tự cấp quyền hoặc bỏ qua SafetyHold/Thử đọc lại. |
| QD05 | Che vùng không được cấp trước phân tích; không đọc/điều khiển cửa sổ ẩn danh, kể cả website có quyền. Mật khẩu/OTP/thẻ thanh toán bị loại khỏi đọc/nhớ/gửi AI. Khả năng che chưa kiểm chứng. |
| QD06 | Email/tin nhắn/lịch/danh bạ chỉ qua giao diện được phép, không kết nối tài khoản riêng. Không tự mở theo cách đánh dấu tin/email đã đọc. |
| QD07 — hoãn | Đọc tập tin/thư mục chọn riêng để bản cập nhật sau, không thuộc bản đầu. Các quyết định cũ về thư mục con và chỉ hiểu tức thời được giữ làm lịch sử, không triển khai hoặc tiếp tục hỏi chi tiết ở giai đoạn hiện tại. Đọc app không tự cho đọc ổ đĩa; không sửa tài liệu cá nhân. |
| QD08 | Chỉ khi mở Windows + V mới được đọc toàn lịch sử trong bảng, không chỉ mục đang hiện. Chỉ để hiểu lúc đó, không tạo ký ức lâu dài. Quy tắc thông tin nhạy cảm vẫn áp dụng. |
| QD09 | Thu hồi quyền dừng truy cập mới ngay, cho chọn giữ/xóa ký ức từ nguồn đó. |
| QD10 | Được biết riêng vị trí/kích thước cửa sổ chưa cấp quyền Đọc để đi/ngồi trên cạnh; không đọc tiêu đề hoặc nội dung. Đây không phải quyền Điều khiển. |
| QD11 | Tài liệu hiện trong ứng dụng (ví dụ Word) chỉ được ghi nhớ tên hoặc chủ đề người dùng đang đọc, không lưu chi tiết nội dung. Quyền ghi nhớ màn hình không vượt giới hạn này; nội dung tập tin đọc trực tiếp vẫn chỉ dùng tức thời theo QD07. Thông tin nhạy cảm bị cấm vẫn phải loại trừ. |
| QD12 | Chấp nhận cài tiện ích hỗ trợ trên Chrome/Edge khi bật tương tác website, nếu phương án được kiểm chứng; tiện ích không bắt buộc cho sinh hoạt cơ bản và không tự cấp quyền mọi website. Chưa có tiện ích hoặc phương án kỹ thuật được cài/chọn. |
| QD13 | Trong trang phim đã cấp quyền, được dùng riêng khung video nhúng từ website khác theo quyền đọc/điều khiển tương ứng của trang phim. Không cấp quyền mở/khám phá toàn website nguồn; không mở rộng ngoại lệ sang quảng cáo hoặc khung khác. Không chắc khung nào là video thì nhờ người dùng chỉ, chỉ dùng sau xác nhận. Phải kiểm chứng nhận diện đúng khung phát video. |
| QD14 | Được nhớ cách nhận diện ô video đã được chỉ trên đúng trang; lần sau kiểm tra lại, nếu giao diện/nguồn không khớp thì hỏi tiếp. Không bấm theo tọa độ cũ; đây không phải tự kích hoạt bài học thao tác đã lưu. |
| QD15 | Chưa xác định chắc đã loại vùng nhạy cảm thì ngừng đọc cửa sổ đó, báo lý do để người dùng xử lý sau; vẫn sinh hoạt bình thường. Không điều khiển cửa sổ khi không thể đọc an toàn, theo quy tắc Đọc trước Điều khiển. Chỉ thử đọc lại khi người dùng bấm Thử đọc lại, vẫn kiểm tra an toàn trước khi tiếp tục; không bỏ qua bộ lọc. |

Không mặc định cấp tài khoản, vượt màn hình bảo vệ hoặc hỗ trợ mọi app chỉ vì quét thấy. Chrome và Edge là hai trình duyệt hỗ trợ đầy đủ được yêu cầu; phạm vi app khác còn cần khảo sát.

## 7. Điều khiển, dừng và bài học

- **DK01:** chuột/phím người dùng ưu tiên; nhân vật nhường khi họ thao tác, sau 60 giây không thao tác mới được tự trở lại; không tính chuột/phím do nhân vật tạo.
- **DK02:** không sửa/xóa/di chuyển dữ liệu cá nhân, gửi tin, đăng bài hoặc trả tiền; không dùng quyền nhấp/phím để vượt cấm. Chấp nhận lịch sử xem tự cập nhật; không tự đánh dấu thư/tin đã đọc. Gõ thật chỉ ô tìm kiếm/điều hướng, không tài liệu/chat/biểu mẫu gửi dữ liệu.
- **DK03:** Dừng khẩn cấp qua phím tắt tùy chỉnh/nút chỉ dừng điều khiển, vẫn quan sát/sinh hoạt theo quyền; hủy việc đang chạy, giữ các việc chưa chạy ở trạng thái tạm dừng. Chỉ người dùng bật lại, không tự vượt sau 60 giây.
- **DK04:** Tắt quan sát dừng đọc nội dung và điều khiển ứng dụng, vẫn sinh hoạt; ngoại lệ đã chốt: được biết vị trí/kích thước cửa sổ để đi/ngồi/bám cạnh, không đọc nội dung bên trong. Chủ động ẩn dừng đọc/điều khiển, ẩn cả nhân vật và đồ đến khi hiện lại. Cả hai thao tác hủy việc đang chạy, giữ việc chưa chạy ở trạng thái tạm dừng. Thoát app là trạng thái riêng.
- **BH01:** chủ động bật hướng dẫn rồi làm mẫu chuỗi trong cùng app/website; cô ấy tóm tắt việc, nơi áp dụng và các bước, người dùng xác nhận mới lưu. Không ghi mọi thao tác thường ngày.
- **BH02:** cài đặt xem bước, đổi tên, bật/tắt, xóa, dạy lại; chọn bài và bấm Thực hiện. Không tự gọi bài học ở cả hai mức; tự khám phá là cơ chế khác. Quyết định 2026-11-14 D-17: Sửa/xóa bài học dừng việc đang dùng và hủy lượt chờ dùng bài học đó; người dùng giao lại, không chuyển lượt cũ sang phiên bản mới, không hủy việc không liên quan hoặc hoàn tác thao tác đã xong.
- **BH03:** yêu cầu trực tiếp được bắt đầu ngay, không chờ 60 giây, trừ khi cô ấy trì hoãn một lần vì tâm trạng. Nếu không yêu cầu lại, vẫn giữ việc chờ và tự làm sau khi xong hoạt động hiện tại, đã kiểm tra quyền/giao diện/điều kiện. Yêu cầu lần hai thì thực hiện nếu đủ điều kiện; không vượt lỗi/giới hạn vì yêu cầu lần hai.
- **BH04:** người dùng thao tác thì nhường; 60 giây sau được kiểm tra quyền/giao diện và quay về nơi cũ tiếp tục. Không làm tiếp máy móc theo tọa độ đã lưu.
- **BH05:** sai giao diện/không tìm mục tiêu thì dừng tại bước lỗi, nhờ chỉ lại; không bấm thử hay chạy lại cả chuỗi.
- **BH06:** có hàng đợi nhiều yêu cầu; người dùng xem thứ tự và hủy từng việc riêng. Khi một việc lỗi thì dừng việc đó, không tự chạy lại hoặc coi đã xong; tiếp tục các việc sau nếu từng việc đủ quyền/điều kiện. Quyết định 2026-11-14 D-02/D-10/D-17: Renderer lỗi thì tạm dừng thao tác app khác; hình ảnh phục hồi hoặc mở lại app giữ việc tạm dừng và hỏi trước tiếp tục, kiểm quyền/an toàn mới, không phát lại mù quáng. Sửa/xóa bài học dừng việc đang dùng và hủy lượt chờ dùng bài học đó, phải giao lại; không hủy việc không liên quan hoặc hoàn tác việc đã xong.
- **BH07:** thoát ứng dụng hoặc đổi hồ sơ phải báo rõ và hủy các việc chưa hoàn thành; mở lại không tự thực hiện hàng đợi cũ, không chuyển việc sang hồ sơ khác. Bài học đã lưu vẫn giữ.
- **BH08:** sau Dừng khẩn cấp/Tắt quan sát/Ẩn, bật lại chức năng hoặc hiện nhân vật không tự chạy các việc cũ. Phải bấm Tiếp tục hàng đợi riêng; chỉ việc chưa chạy còn giữ được tiếp tục, không khôi phục việc đã hủy. Mọi điều kiện/quyền vẫn được kiểm tra.
- **BH09:** tự ẩn vì buồn/tổn thương cũng hủy việc đang chạy, giữ việc chưa chạy ở trạng thái tạm dừng. Sau khi cô ấy trở lại, người dùng phải bấm Tiếp tục hàng đợi riêng; không tự khôi phục việc đã hủy.
- **BH10:** khi người dùng yêu cầu thực hiện bài học trong lúc cô ấy tự tìm phim/khám phá ứng dụng, ưu tiên việc người dùng giao, dừng việc tự khám phá; vẫn áp dụng quyền trì hoãn một lần theo tâm trạng đã chốt.
- **BH11:** bài học có bước tìm kiếm cho phép người dùng đổi nội dung tìm kiếm trước mỗi lần bấm Thực hiện; giữ nguyên các bước đã dạy. Không mở rộng quyền gõ ngoài ô tìm kiếm/điều hướng đã cho phép.
- **BH12:** khi lưu bài học có bước chọn kết quả tìm kiếm, cho người dùng chọn rõ chọn kết quả đầu tiên hoặc đúng nội dung đã chỉ. Không tự suy ra ý nghĩa từ cú bấm mẫu; lựa chọn không bỏ qua quyền và kiểm tra an toàn của mục tiêu.
- **BH13:** có lịch sử thao tác trong cài đặt, chỉ lưu trên máy; người dùng xem và xóa được. Ghi ngắn gọn thời điểm, app/website, loại thao tác và kết quả; không lưu ảnh màn hình hoặc nội dung riêng tư. Tách lịch sử này khỏi ký ức nhân vật. Giữ 30 ngày rồi tự xóa; người dùng có thể xóa sớm.

## 8. Xem phim, nhạc và dịch vụ AI

- **XP01:** xem cùng, buồn theo cảnh buồn, hứng thú tùy độ hấp dẫn cảnh hành động; reo hò bằng hoạt ảnh, không tiếng. Cảm xúc chuyển tự nhiên, không bật tắt mỗi khung hình.
- **XP02:** khi đang chú ý đến cảnh rõ, mục tiêu bắt đầu phản ứng dưới 1 giây; cảnh khó chờ để hiểu đúng. Chưa đo/đạt. Không giới hạn loại phim; ưu tiên phụ đề tiếng Việt, ngôn ngữ khác sau.
- **XP03:** tự chọn điểm chú ý theo tâm trạng/sở thích khi nhiều cửa sổ cùng hiển thị; không bắt buộc thấy mọi cảnh. Hiểu sai thì tiếp tục điều chỉnh theo cảnh sau, không tính năng sửa cảm xúc bằng tay.
- **XP10:** khi không nhìn được hình ảnh phim, cô ấy tự chọn tiếp tục ngồi xem hoặc chuyển sang chơi, ăn uống hay hoạt động khác tùy tâm trạng; không bắt buộc tiếp tục xem và không coi nội dung không nhìn được là đã hiểu.
- **XP11:** khi tự chọn phim/nhạc, cô ấy chủ yếu học và chọn theo gu của người dùng từ nội dung người dùng chủ động mở và xem/nghe lâu trong phạm vi được phép quan sát. Không tự đọc lịch sử trình duyệt; việc mở thử chưa đủ để kết luận thích. Không mở rộng sang nghe/phân tích âm thanh đang hoãn.
- **XP12:** nội dung cô ấy tự mở cũng có thể góp phần học gu nếu người dùng quay lại và tiếp tục xem/nghe đủ lâu; không coi thời gian tự phát khi người dùng vắng mặt là dấu hiệu yêu thích. Dựa vào thao tác chọn/chuyển nội dung thật của người dùng theo XP14.
- **XP13:** dấu hiệu đủ lâu để góp phần học gu: phim ít nhất 20 phút; nhạc được nghe lặp lại hoặc nhiều bài cùng kiểu. Đây là tín hiệu, không kết luận chắc thích. Dùng dấu hiệu thao tác theo XP14; không dùng quy tắc 60 giây thiếu quan tâm để tự suy ra hiện diện.
- **XP14:** dùng thao tác người dùng chủ động chuyển tập, chuyển kênh/video hoặc chọn nhạc làm dấu hiệu đang xem/nghe để học gu; không thêm nút xác nhận. Phân biệt thao tác người dùng với tự chuyển/phát tiếp của website hoặc nhân vật; việc không thao tác không tự chứng minh còn hiện diện.
- **XP15:** khi tự mở phim/nhạc lúc người dùng vắng mặt, mở tab riêng; giữ nguyên các tab người dùng đang mở, không điều hướng thay nội dung của chúng.
- **XP16:** người dùng chọn Chrome hoặc Edge trong cài đặt làm trình duyệt tự mở phim/nhạc. Lựa chọn này không tự cấp quyền đọc/điều khiển trình duyệt hay website.
- **XP09:** khi nhân vật hoặc sofa che phụ đề, người dùng tự kéo nhân vật/đồ vật sang chỗ khác; không yêu cầu tự phát hiện và né phụ đề. Quy tắc không gián đoạn phim vẫn áp dụng.
- **XP04:** phim đang phát không tự ngắt/cuộn/chuyển cửa sổ gây gián đoạn; được chuyển tập khi hết trong quyền cho phép. Không chắc thì ra dấu/gợi ý, không bấm thử.
- **XP05:** tự mở phim/nhạc chỉ nâng cao, sau mặc định 5 phút không thao tác (chỉnh được); không khi nhạc/video đang phát. Toàn màn hình không tự là dấu hiệu đang bận. Người dùng quay lại chỉ nhường điều khiển, giữ nội dung phát. Quyết định 2026-11-14 D-16: Được kiểm trạng thái đang phát/không phát ở nền tối thiểu để tránh mở chồng; không đọc tên/nội dung hoặc suy gu. Lỗi/không xác định không coi là không phát; API/độ tin cậy cần kiểm chứng.
- **XP06:** YouTube được tìm nội dung miễn phí trong quyền cấp. Website khác chỉ ghi nhớ/mở lại sau chọn Cho phép cô ấy dùng website này; được tìm phim bất kỳ miễn phí trong trang đó.
- **XP07:** được đóng quảng cáo; tab mới không chắc quảng cáo thì để nguyên và quay lại tab phim. Không coi tải/cài/cấp quyền/trả tiền là đóng quảng cáo. Đòi đăng nhập/trả tiền/xác minh thì bỏ, tối đa 3 nội dung mỗi lần tìm rồi về sinh hoạt nếu vẫn không được. Quyết định 2026-11-14 D-06: Sau 3 nội dung không mở được về sinh hoạt; chờ người dùng thao tác trở lại rồi chỉ tìm trong đợt vắng mặt tiếp theo. Không tìm lặp cùng đợt hoặc chỉ dùng bộ đếm để mở lại tìm kiếm; quyền/chờ/không gián đoạn vẫn áp dụng.
- **XP08:** máy khóa không tự mở nội dung mới; mở khóa được tiếp tục nếu trước đó đủ chờ. Riêng thao tác mở khóa không đặt lại mốc 60 giây/5 phút; thao tác chuột/phím tiếp theo trong desktop mới đặt lại, người dùng vẫn ưu tiên. Quyết định 2026-11-14 D-11: Máy ngủ không cộng thời gian chờ mở phim/nhạc; máy thức tiếp tục phần còn lại, không reset chỉ vì thức. Giữ quyền/khóa/input/phát đã chốt, máy ngủ khác nhân vật ngủ.
- **AI01:** nghe/phân tích âm thanh, micro/camera và nhảy theo nhịp để sau. Chỉ mở/phát nhạc và dùng trạng thái phát cần thiết; chưa có thu âm thanh cho nhân vật trong phạm vi hiện tại. Quyết định 2026-11-14 D-16: Chỉ kiểm tra trạng thái đang phát/không phát ở nền để tránh mở chồng; không tên bài/phim/hình/âm thanh/lịch sử hoặc suy gu; lỗi/không rõ không coi là không phát. Cách lấy/độ tin cậy cần kiểm chứng.
- **AI02:** AI bên ngoài chỉ khi người dùng chủ động yêu cầu; xem và duyệt chữ gửi mỗi lần, từ chối thì vẫn dùng khả năng cục bộ. Chưa cho gửi ảnh/âm thanh/tập tin/ký ức hoặc tự gửi báo cáo. Nhà cung cấp chưa chọn. Quyết định 2026-11-14 D-18: Gửi chữ lỗi/chưa rõ thành công thì báo lỗi và chờ bấm thử lại; xem/duyệt chữ trước mỗi lần gửi mới kể cả chữ không đổi. Không tự gửi lại, không coi timeout là chưa nhận, không mở rộng loại dữ liệu/quyền.
- **AI03:** người dùng xác nhận hướng chạy AI local nhẹ để xử lý cảm xúc nhanh; hai mức cần phù hợp khả năng máy. Chưa chọn mô hình/runtime, số mô hình hoặc cơ chế suy luận; không coi nhãn nhẹ/local là bằng chứng đạt độ trễ XP02. Việc kiểm tra cấu hình không mở rộng quyền đọc nội dung riêng tư.

## 9. Ký ức, quan hệ và ranh giới

- **KN01:** ký ức có thể xem/sửa/xóa/ghim. Cô ấy tự đánh giá quan trọng; vụn vặt phai theo độ quan trọng/nhắc lại, không mốc cố định. Ghim không phai; không ghi lại dữ liệu nhạy cảm đã cấm.
- **KN02:** quên tự nhiên giữ mức thân thiết đã hình thành. Sửa nội dung ký ức chỉ đổi thông tin, không đổi mức thân thiết. Chủ động xóa ký ức có thể điều chỉnh quan hệ nếu nó từng đóng góp.
- **QH01:** dần thân thiết, chào/phản ứng riêng; mặc định bạn bè. Nâng cao có lãng mạn chỉ khi chủ động bật, không lập tức thành người yêu; thể hiện ngượng/đỏ mặt/đến gần/cử chỉ trái tim có ranh giới, không bổ sung nội dung tình dục.
- **QH02:** tắt lãng mạn cho chọn giữ/xóa ký ức lãng mạn; giữ thì có thể buồn tạm, không níu kéo/tự bật lại, tôn trọng chuyển về bạn bè.
- **QH03:** người dùng vắng/tắt app không giảm quan hệ hay làm tự ẩn. Mốc cũ 3 ngày lịch đã thay: cộng khoảng 48–72 giờ dùng máy khi nhân vật nâng cao hiện diện mà không tương tác; sau 60 giây không thao tác thì ngừng cộng. Không tính sleep, mở chốc lát rồi tắt, hoạt động do nhân vật, mức cơ bản hoặc hồ sơ không hoạt động.
- **QH04:** đang tin tưởng/thân thiết chịu được lâu hơn, gần 72 giờ; đang tổn thương gần 48 giờ. Bấm/vuốt/cho ăn ngắt chuỗi thiếu tương tác, không xóa ngay nỗi buồn đã có.
- **QH05:** vượt ngưỡng thì buồn/ít chủ động trước, tiếp diễn lâu hơn mới tự ẩn. Làm lành mọi mức được, nặng qua vài buổi, cần thời gian/đối xử tốt; không phải một thao tác hoặc nhiều quà lập tức hết buồn. Nguôi giận tính cả app đóng nhưng vẫn cần tương tác thật. Quyết định 2026-11-14 D-05/H03: Buổi làm lành có thể cùng ngày nếu có khoảng nghỉ và tương tác thật; đóng/mở app hoặc quà liên tục không là buổi mới. Không tự đặt số phút/số buổi hoặc quà lập tức xóa tổn thương.
- **QH06:** quăng lần đầu giật mình/ra dấu không thích, chưa hại lâu dài. Tiếp tục sau phản đối thì tạm không cho nhấc, vẫn nhận vuốt/ăn; bình tĩnh và có tương tác tốt, ra dấu sẵn sàng mới cho nhấc lại. Giận nhẹ không có thời gian từ chối cố định, tùy tâm trạng và cách được dỗ. Nâng cao có thể tổn thương lâu dài nếu liên tục bất chấp ranh giới.
- **QH07:** tự ẩn vì xa cách thì ngừng cả quan sát/điều khiển, giữ trạng thái riêng; có thể chưa đồng ý ra. Mời ra/để đồ ăn hoặc thú bông từ cửa sổ khay hệ thống hoặc biểu tượng nhỏ tại chỗ ẩn. Cô ấy tự quyết định nhận/xuất hiện; cài đặt và reset luôn mở được.

## 10. Hồ sơ, sao lưu, cài đặt và cập nhật

- **HS01:** nhiều hồ sơ chỉ qua nhập sao lưu, không nút tạo thêm mới. Chỉ một hồ sơ hoạt động; không trộn ký ức. Hồ sơ không chọn đóng băng hoàn toàn, chọn lại tiếp từ trạng thái cũ (khác đóng app).
- **HS02:** quyền của ứng dụng trên máy dùng chung hồ sơ; file nhập không đem quyền sang. Máy chưa có quyền thì vẫn mặc định tắt.
- **HS03:** Đặt lại nhân vật xóa ký ức, quan hệ, trạng thái và toàn bộ bài học của hồ sơ đang chọn để bắt đầu lại; giữ các hồ sơ khác và quyền chung.
- **SL01:** chỉ sao lưu khi bấm xuất, không bản phục hồi tự động. Xuất nhân vật/ký ức/thiết lập; không khóa truy cập AI, máy mới kết nối AI lại. Quyết định 2026-11-14 D-09: Sao lưu không kèm gói AI nâng cao; máy mới tải lại khi cần, không thêm tùy chọn kèm gói mỗi lần xuất. Giữ dữ liệu nhân vật/ký ức/thiết lập thuộc phạm vi; quyền máy/khóa AI ngoài không mang sang. Whitelist/tài nguyên khác/tương thích còn phải đặc tả.
- **SL02:** mỗi bản xuất bắt buộc mật khẩu, thêm mã khôi phục người dùng tự giữ riêng. Chưa chọn cơ chế bảo vệ; không lưu mã mở khóa chung trong bản cần bảo vệ.
- **CD01:** hỏi bật/tắt khởi động cùng Windows trong thiết lập đầu; không tự bật ngầm. Dữ liệu được lưu qua lần đóng/mở app, không phải bản sao lưu tự động. Quyết định 2026-11-14 D-10: Mở lại app giữ việc đang dở tạm dừng, hỏi trước tiếp tục; không tự chạy lại, vẫn kiểm quyền/an toàn hiện hành. Crash ghi dữ liệu/cập nhật còn cần khảo sát.
- **CD02:** tự kiểm tra/tải cập nhật chính app nhân vật; hỏi trước cài/khởi động lại. Không cập nhật phần mềm khác.
- **CD03:** gỡ app hỏi giữ dữ liệu để cài lại hay xóa tất cả, nhắc xuất sao lưu trước. File xuất ngoài vùng ứng dụng phải được giải thích riêng, không tự quét/xóa.

## 11. Quyết định cũ đã được thay thế

| Trước | Hiện hành |
|---|---|
| Quyền JSON: 69/132 bật | Chỉ là ảnh chụp lịch sử lựa chọn; phỏng vấn sau đó mới là yêu cầu hiện hành, không tái dùng số đếm như cấu hình hiệu lực |
| B03 chưa bật | Có phím tắt dừng riêng, không cho đọc nội dung gõ |
| I03 gửi chữ toàn quyền | Chỉ khi chủ động yêu cầu, xem/duyệt từng lần |
| D06/D07 chưa bật | Nâng cao được mở nội dung trong trang cho phép, có ngoại lệ đóng quảng cáo; tab không chắc thì giữ và quay lại phim |
| Đọc toàn bộ, có thể hiểu là nền | Chỉ cửa sổ/tab thực sự nhìn thấy, đã có quyền; nguồn file và Windows + V có quy tắc riêng |
| Có thể tự dùng lại bài học | Bài học chỉ chạy khi yêu cầu ở cả hai mức |
| Chuột phải mở khay ăn ngay | Menu nhỏ Đồ ăn / Dọn đồ |
| Thiếu quan tâm sau 3 ngày lịch | 48–72 giờ hoạt động đủ điều kiện, ngừng sau 60 giây không thao tác |
| Chỉ reset/xóa ký ức mới làm lành | Có thể làm lành mọi mức qua thời gian và đối xử tốt |
| Một hồ sơ trên máy | Hồ sơ bổ sung qua nhập; một hoạt động; quyền chung; hồ sơ khác đóng băng |
| Tự sao lưu từng được chọn H13 | Chỉ xuất thủ công; không bản phục hồi tự động |

## 12. Những gì chưa làm hoặc không thuộc bản đầu

- Chưa có code nhân vật hoặc ảnh mẫu được duyệt. Đã có mẫu E02a native với 53 kiểm thử đạt và 35 tình huống giả; còn kiểm tra UI/nghiệm thu. Chưa đo hiệu năng AI/Unity hoặc thử nguồn màn hình thật.
- Không đưa vào bản đầu: đọc tập tin/thư mục chọn riêng, hệ điều hành khác, ngôn ngữ khác, nhiều ngoại hình, tạo thêm hồ sơ bằng nút mới, tài khoản/đồng bộ cloud, trò chuyện, phân tích âm thanh/micro/camera/nhảy nhịp, nội dung sách/tranh/game thật, giao dịch thật, công khai mã nguồn.
- Hướng công cụ theo SP09, mẫu E02a dùng .NET10/WPF/MSTest. Chưa chốt stack/API/types/định dạng dữ liệu production hoặc mô hình AI và các giới hạn chưa hỏi. Lệnh có thật của mẫu không được ghi thành lệnh toàn sản phẩm.
- Phiên ổn định 8 giờ là yêu cầu kiểm chứng, chưa phải bằng chứng đã đạt; cấu hình, độ chính xác, tỷ lệ lỗi và chi phí cần khảo sát theo [đề cương kiểm chứng](KE_HOACH_KIEM_CHUNG.md).
