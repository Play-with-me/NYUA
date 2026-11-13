# Từng công việc dành cho người đọc

Đây là 52 việc dự kiến của toàn sản phẩm, chưa phải 52 việc đã được cho bắt đầu. Tên mã giúp nối với bản kỹ thuật; bạn không cần đọc tên file hoặc chọn thư viện. Những việc còn phụ thuộc phép thử/ý kiến phải giải quyết trước. Mẫu E02a đang làm vẫn được theo dõi riêng.

## P00-01 — Rà baseline và giải quyết mâu thuẫn phạm vi

Đọc lại toàn bộ yêu cầu với bạn để tìm chỗ hiểu sai. Kết quả là danh sách đã rõ và chỗ còn thiếu, không tự bổ sung ý tưởng thay bạn.

**Làm sau:** Rà yêu cầu hiện tại trước.

## P00-02 — Rà ranh giới và hợp đồng hybrid

Chia rõ ai quản lý quyền, ai làm nhân vật và ai hiểu màn hình. Cần thấy rằng cô ấy không thể tự bấm máy chỉ vì phần hoạt ảnh hoặc AI muốn làm.

**Làm sau:** P00-01

## P00-03 — Chốt tiêu chuẩn chất lượng sau đo

Thống nhất cách đánh giá chất lượng sau khi có số đo: nhanh, đúng và nhẹ đến đâu. Không đặt con số đẹp nhưng chưa kiểm tra được.

**Làm sau:** P00-01

## P00-04 — Lập danh mục giấy phép và chi phí

Kiểm tra quyền sử dụng của hình ảnh, Unity, AI và các thư viện; ghi chi phí nếu có. Tên sản phẩm và quyền dùng từng thành phần được kiểm tra riêng.

**Làm sau:** P00-01

## P01-01 — Khép kiểm tra UI còn mở của E02a

Dùng lại mẫu quyền đã có, thử cửa sổ nhỏ và bàn phím rồi nhận phản hồi của bạn. Chưa thử xong không đánh dấu nghiệm thu xong.

**Làm sau:** P00-01

## P02-01 — Chọn và dựng renderer thử tối thiểu

Tạo một nhân vật đại diện đơn giản trong Unity, chạy được trên Windows. Chưa cần tạo tất cả hoạt ảnh hoặc ngoại hình chính thức.

**Làm sau:** P00-02, P00-04

## P02-02 — Thử transparent overlay và hit regions

Cho hình nhân vật hiện trên desktop với nền trong suốt. Bạn phải bấm được các ứng dụng phía dưới ở những chỗ không có nhân vật/đồ vật.

**Làm sau:** P02-01

## P02-03 — Thử tọa độ qua monitor và DPI

Thử khi cửa sổ di chuyển, màn hình phóng lớn hoặc có nhiều màn hình. Cô ấy phải hiểu đúng vị trí, không bấm nhầm vì lệch tọa độ.

**Làm sau:** P02-02

## P02-04 — Thử kết nối typed host-renderer

Nối nhân vật với ứng dụng quản lý bằng một ví dụ nhỏ. Gửi lệnh lặp hoặc sai không được làm cô ấy tự bấm hoặc đổi quyền.

**Làm sau:** P02-01, P00-02

## P02-05 — Thử mất kết nối và khôi phục an toàn

Cố tình làm phần nhân vật mất kết nối để xem app có dừng an toàn không. Nối lại không được tự chạy việc cũ ngoài điều bạn đã cho phép.

**Làm sau:** P02-04, P02-03

## P03-01 — Sàng lọc model/runtime local có quyền phân phối

So sánh các mô hình AI chạy trên máy và quyền phân phối của chúng. Chưa chọn chỉ vì mô hình có chữ miễn phí hoặc bản nhẹ.

**Làm sau:** P00-04

## P03-02 — Dựng benchmark dữ liệu cảnh an toàn

Chuẩn bị các cảnh phim có phụ đề Việt được phép dùng để thử, với đáp án đã rà trước. Không chỉ chọn những cảnh AI trả lời đúng.

**Làm sau:** P03-01, P01-01

## P03-03 — Đo phản ứng toàn luồng dưới tải kết hợp

Đo từ lúc cảnh xuất hiện tới khi cô ấy bắt đầu phản ứng, trong khi Unity cũng đang chạy. Bạn xem cả độ đúng, độ trễ và mức máy bị ảnh hưởng.

**Làm sau:** P03-02, P02-04

## P03-04 — Đề xuất hai mức và luồng gói nâng cao

Dựa vào kết quả đo để đề xuất hai mức và hiển thị gói nâng cao cần tải. Bạn vẫn tự chọn; app không âm thầm đổi mức.

**Làm sau:** P03-03, P00-03

## P10-01 — Triển khai grants mặc định tắt và read/control

Làm quyền Đọc và Điều khiển riêng, ban đầu tắt. Chọn điều khiển không được tự bật quyền đọc thay bạn.

**Làm sau:** P00-02, P01-01

## P10-02 — Nhận dạng nguồn và vùng đang hiển thị

Chỉ nhận nội dung thực sự đang nhìn thấy và được phép. Những app không hỗ trợ phải được báo rõ, không thử bấm để đoán.

**Làm sau:** P10-01, P02-03

## P10-03 — Lọc sensitive/private và retry hold trên nguồn thật

Thử lọc nội dung nhạy cảm trên nguồn thật được kiểm soát. Nếu chưa chắc thì chặn cửa sổ, và nút thử lại vẫn phải kiểm tra an toàn.

**Làm sau:** P10-02

## P10-04 — Kiểm chứng clipboard history đúng Win+V scope

Kiểm tra khả năng đọc lịch sử sao chép chỉ lúc bảng Windows + V đang mở. Đóng bảng phải dừng, không lưu thành ký ức.

**Làm sau:** P10-03

## P10-05 — Luồng AI ngoài có preview và consent mỗi lần

Làm luồng bạn chủ động nhờ AI bên ngoài, xem chữ sắp gửi và xác nhận từng lần. Không tự gửi ảnh, ký ức hoặc khóa truy cập.

**Làm sau:** P10-03, P50-01

## P10-06 — Bridge trình duyệt và ngoại lệ khung video

Làm phần hỗ trợ Chrome/Edge khi bạn bật dùng website. Ô video khác nguồn chỉ được dùng trong đúng phạm vi đã chỉ, không kéo theo quyền quảng cáo.

**Làm sau:** P10-03, P00-04

## P10-07 — Input arbitration và các nút dừng

Thử nhường chuột/phím và các nút dừng/ẩn/tắt quan sát. Mỗi nút phải có tác dụng đã chốt, không tự chạy lại sau khi dừng.

**Làm sau:** P10-01, P02-05

## P20-01 — Duyệt model sheet nhân vật gốc

Tạo mẫu ngoại hình để bạn duyệt tóc, mắt, trang phục, kẹp tóc, tỉ lệ và nét pixel. Chỉ sau đó mới làm cả bộ hình chuyển động.

**Làm sau:** P00-04

## P20-02 — Di chuyển và bề mặt cửa sổ

Cho cô ấy đi, ngồi, leo và rơi theo cạnh cửa sổ. Di chuyển hoặc đóng cửa sổ thì cô ấy phải theo hoặc rơi hợp lý.

**Làm sau:** P20-01, P02-03, P02-05

## P20-03 — Pet/lift/throw và chuyển vị trí an toàn

Làm bấm, vuốt, nhấc, thả và quăng khác nhau rõ ràng. Cách giữ phím để đổi chỗ không được tính là quăng hoặc làm cô ấy buồn.

**Làm sau:** P20-02, P30-02

## P20-04 — Foodtray, đồ vật và animatedcleanup

Làm khay sáu món, kéo từng món/cả khay và các đồ vật. Không vượt năm món để lại; khi dọn phải có hoạt ảnh như đã chọn.

**Làm sau:** P20-02, P30-01

## P20-05 — Placement nhiều màn hình và fullscreen

Thử cô ấy xuất hiện đúng các màn hình được chọn và ở mép khi toàn màn hình. Ghi rõ trường hợp không hỗ trợ thay vì hứa mọi game.

**Làm sau:** P20-02, P02-02

## P30-01 — Needs/sleep/rest và elapsed reconciliation

Làm nhịp ăn/ngủ/nghỉ và cách tiếp nối khi mở app lại. Không bịa sự kiện khi máy tắt, không làm cô ấy bị bệnh vì bạn bận.

**Làm sau:** P00-02, P50-01

## P30-02 — Lựa chọn hoạt động, mood và attention limits

Làm cô ấy chọn việc theo tâm trạng và nhu cầu, có thể đổi ý. Rủ hai lần không đáp thì tự chơi và nghỉ ít nhất ba mươi phút trước khi rủ tiếp.

**Làm sau:** P30-01

## P30-03 — Quan hệ sâu, neglect và làm lành

Làm sự thân thiết, giận, tự ẩn và làm lành có diễn biến. Phân biệt bạn vắng mặt với việc đang dùng máy nhưng không quan tâm.

**Làm sau:** P30-02, P30-04

## P30-04 — Memory provenance, pin/fade/edit/delete

Làm ký ức xem/sửa/xóa/ghim được và giữ đúng giới hạn riêng tư. Quên tự nhiên, sửa và chủ động xóa có tác động quan hệ khác nhau.

**Làm sau:** P50-01, P10-01

## P30-05 — Học gu từ user media evidence

Học gu từ phim/nhạc bạn thực sự lựa chọn và dùng đủ lâu. Không coi nội dung cô ấy tự phát khi bạn vắng là bằng chứng bạn thích.

**Làm sau:** P30-04, P10-02

## P30-06 — Mode preservation, personality và romance opt-in

Làm chuyển hai mức mà không mất dữ liệu sâu; tính cách và lãng mạn chỉ biểu hiện đúng mức. Tắt lãng mạn phải tôn trọng lựa chọn giữ/xóa ký ức của bạn.

**Làm sau:** P30-03, P03-04

## P40-01 — Onboarding/tray/settings shell

Làm lần mở đầu và cửa sổ cài đặt từ khay hệ thống. Dù cô ấy đang giận hoặc ẩn, bạn vẫn mở được quản lý và các nút dừng.

**Làm sau:** P02-04, P50-01

## P40-02 — UI grants và chosenbrowser

Làm danh sách ứng dụng, dán website, hai ô quyền và chọn Chrome/Edge. Chữ giải thích phải giúp bạn biết đang cấp gì, không chỉ có ô tick.

**Làm sau:** P40-01, P10-01

## P40-03 — Dạy/review/manage lesson và searchparameters

Làm chế độ dạy một chuỗi rồi xem lại trước khi lưu. Bạn chọn ý nghĩa kết quả tìm kiếm và đổi chữ cần tìm mỗi lần chạy được.

**Làm sau:** P10-03, P40-01, P50-01

## P40-04 — Embodied execution và postconditionverify

Cho cô ấy đi tới nút, kiểm tra lại rồi mới bấm thật. Nếu nút đổi, bạn giành chuột hoặc chưa rõ kết quả thì phải dừng/nhường đúng cách.

**Làm sau:** P40-03, P10-07, P20-02

## P40-05 — Hàng đợi, priority và stop lifecycle

Làm hàng đợi xem thứ tự và hủy từng việc. Dừng/ẩn xử lý việc đang làm và việc chưa chạy khác nhau, không làm việc đã hủy sống lại.

**Làm sau:** P40-04, P30-03

## P40-06 — Xem cùng và phản ứng cảm xúc

Cho cô ấy xem cùng và đổi biểu cảm tự nhiên theo cảnh hiểu được. Không tự ngắt phim; không hiểu được thì có thể chuyển sang sinh hoạt riêng.

**Làm sau:** P03-03, P10-03, P30-02, P20-04

## P40-07 — Tự tìm/mở nội dung trong quyền

Cho nâng cao tự mở nội dung miễn phí khi bạn vắng đủ thời gian và chưa có nhạc/phim phát. Dùng tab riêng, không sửa tab của bạn, thử tối đa ba nội dung khi bị chặn.

**Làm sau:** P40-05, P40-06, P10-06

## P50-01 — Chốt storage và transaction/persistence

Chọn cách lưu dữ liệu bền vững và thử khi ghi bị lỗi. Không lén tạo các bản sao lưu tự động để giải quyết việc bảo vệ dữ liệu.

**Làm sau:** P00-02, P00-04

## P50-02 — Profile import/switch/reset semantics

Làm đổi hồ sơ, đóng băng hồ sơ không dùng và reset đúng hồ sơ đang chọn. Giữ các hồ sơ khác và quyền chung trên máy.

**Làm sau:** P50-01, P10-01

## P50-03 — Manualexport password/recovery format

Làm xuất sao lưu bằng tay, có mật khẩu và mã khôi phục cất riêng. Bạn phải biết rõ file gồm gì và không có khóa AI/quyền hiệu lực.

**Làm sau:** P50-01, P00-04

## P50-04 — Validate/import archive thành hồ sơ riêng

Làm nhập file thành hồ sơ riêng; sai mật khẩu hoặc file lỗi không phá hồ sơ đang có. Không trộn ký ức hoặc tự cấp quyền từ file nhập.

**Làm sau:** P50-03, P50-02

## P50-05 — Local actionhistory và expiry30days

Làm lịch sử thao tác trên máy, xem và xóa được. Tự xóa sau ba mươi ngày, không chứa ảnh màn hình hoặc chữ riêng tư.

**Làm sau:** P50-01

## P50-06 — Bộ cài và startup opt-in

Làm bộ cài đủ các phần cần thiết và thử cài mới. Người dùng tự chọn mở cùng Windows; không bắt cài gói AI nâng cao để sinh hoạt cơ bản.

**Làm sau:** P00-04, P40-01, P20-05

## P50-07 — Own update check/download/install confirmation

Làm kiểm tra/tải cập nhật của chính app rồi hỏi trước khi cài và khởi động lại. Cập nhật lỗi không được làm mất hồ sơ hoặc tự cập nhật app khác.

**Làm sau:** P50-06, P50-04

## P50-08 — Uninstall giữ/xóa và manualexport reminder

Làm gỡ ứng dụng có lựa chọn giữ/xóa dữ liệu và nhắc xuất trước. Không tìm xóa những file sao lưu bạn đã tự cất ở nơi khác.

**Làm sau:** P50-06, P50-03

## P60-01 — Lát tích hợp đầu: hiện→đọc an toàn→phản ứng→dừng

Ghép một lần dùng thật từ mở app, thấy cô ấy, cấp quyền, hiểu ngữ cảnh tới phản ứng và dừng. Các video minh họa rời rạc chưa đủ thay kết quả này.

**Làm sau:** P40-01, P20-02, P30-02, P10-03

## P60-02 — Hồi quy hai mức và toàn bộ nghiệp vụ

Rà tất cả yêu cầu ở cả hai mức, gồm tình huống lỗi. Mỗi dòng phải có kết quả thật, phần chưa thử không được đánh dấu đạt.

**Làm sau:** P60-01, P30-06, P40-07, P50-04, P50-05

## P60-03 — Phiên8h/offline và ma trận cấu hình

Chạy phiên thật khoảng tám giờ và thử mất mạng sau cài đủ gói. Bạn xem máy có giật, dữ liệu có mất và nhân vật có vượt quyền không.

**Làm sau:** P60-02, P03-04

## P60-04 — Rà độc lập, thương hiệu và release gate

Rà bảo mật, dữ liệu, giấy phép, tên sản phẩm và giới hạn trước công khai. Ghi ai rà thật, không gọi một AI tự đọc lại là kiểm tra độc lập.

**Làm sau:** P60-03, P50-07, P50-08, P00-04

## P60-05 — Chuẩn bị công bố và hỗ trợ có kiểm soát

Chuẩn bị bản phát hành, hướng dẫn tiếng Việt và cách báo lỗi không lộ riêng tư. Chỉ công bố bản cụ thể khi bạn quyết định, không tự đăng từ kế hoạch này.

**Làm sau:** P60-04
