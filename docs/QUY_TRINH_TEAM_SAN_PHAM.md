# Quy trình team sản phẩm áp dụng cho dự án nhân vật desktop

Ngày: 2026-11-13. Đây là bộ quy trình làm việc được chuẩn bị theo yêu cầu của người dùng; không phải bằng chứng sản phẩm đã hoàn thành các bước.

## 1. Cách dùng với một người và một AI

Bạn giữ vai trò người quyết định sản phẩm: mục tiêu, trải nghiệm, phạm vi, chi phí và chấp nhận kết quả dùng thử. AI đảm nhiệm phân tích, đề xuất thiết kế, kỹ thuật, kiểm thử và ghi chép. Một AI đổi vai không tạo thành nhiều người rà soát độc lập. Trước phát hành, việc rà soát độc lập các phần nhạy cảm cần được bố trí thật và ghi rõ ai đã thực hiện; không tự ghi đã có chuyên gia duyệt.

Mỗi thay đổi đi qua một vòng: hiểu yêu cầu → mô tả hành vi và điều kiện đúng → làm một phần nhỏ → kiểm tra → bạn dùng thử khi cần → lưu mốc và bàn giao. Không xin duyệt từng dòng code; chỉ đưa bạn quyết định khi thay đổi phạm vi, trải nghiệm, chi phí hoặc đánh đổi chất lượng chưa được chấp nhận.

## 2. Chúng ta đang ở đâu?

| Trước khi có quy trình | Cách làm tiếp |
|---|---|
| Phỏng vấn dài, có nguy cơ hỏi lại hoặc bỏ sót | Dùng yêu cầu có mã, câu hỏi mở và lịch sử quyết định |
| Có đề cương thử nhưng chưa có bằng chứng | Làm phép thử hẹp, ghi kết quả từng tình huống và giới hạn |
| Có thể viết code theo danh sách tính năng | Chia trách nhiệm trước, đặc tả phần cần làm rồi mới tạo việc thực thi |
| “Xong” có thể chỉ nghĩa là AI báo chạy được | Hoàn thành phải có bằng chứng kỹ thuật, kiểm tra nghiệp vụ và dùng thử phù hợp |

```text
[Yêu cầu đã hiểu] ← sửa khi bạn đổi ý
       ↓
[Chia trách nhiệm] → [Bạn rà ranh giới]
       ↓
[Đặc tả phép thử nhỏ] → [Kiểm chứng khả thi]
       ↓                         │ không đạt
[Đặc tả phần sản phẩm] ← [Bạn quyết định đánh đổi]
       ↓
[Thiết kế + kế hoạch việc nhỏ]
       ↓
[Code → kiểm thử → rà soát → bạn dùng thử]
       ↓
[Tích hợp → thử 8 giờ → nghiệm thu phát hành]
       ↓
[Phát hành có kiểm soát → hỗ trợ → cải tiến]
```

Mẫu thử nội bộ được phép chỉ làm một khả năng. Bản dùng thử có ý nghĩa và bản phát hành vẫn phải kết hợp đủ những phần người dùng đã yêu cầu; không âm thầm đổi định nghĩa sản phẩm.

## 3. Vai trò và đầu ra

| Vai trò | Công việc trong dự án này | Người chịu trách nhiệm hiện tại |
|---|---|---|
| Chủ sản phẩm | Quyết định ưu tiên, chi phí, thay đổi yêu cầu và nghiệm thu trải nghiệm | Bạn |
| Phân tích nghiệp vụ | Chuẩn hóa quy tắc, ngoại lệ, trạng thái và ví dụ; nối yêu cầu với kiểm thử | AI, bạn xác nhận ý nghĩa |
| Thiết kế trải nghiệm/hình ảnh | Luồng sử dụng, phác thảo, năm trạng thái giao diện, mẫu pixel/hoạt ảnh | AI đề xuất, bạn duyệt trải nghiệm/gu |
| Kỹ thuật Windows và trình duyệt | Khảo sát nguồn chính thức, thiết kế ranh giới, làm mẫu và triển khai | AI; chưa có kiến trúc được chọn |
| AI cục bộ | Bộ cảnh thử, giấy phép, số đo chất lượng/độ trễ/tài nguyên | AI; bạn quyết định chất lượng chấp nhận |
| Kiểm thử | Thiết kế trường hợp đúng/sai, thử hồi quy, ghi lỗi có bằng chứng | AI kiểm kỹ thuật; bạn dùng thử |
| Bảo mật và dữ liệu | Rà nguồn không tin cậy, quyền, lưu dữ liệu, backup/cập nhật | AI rà ban đầu; rà độc lập trước phát hành chưa bố trí |
| Phát hành/hỗ trợ | Bộ cài, phiên bản, hướng dẫn, khôi phục khi lỗi và tiếp nhận phản hồi | AI chuẩn bị, bạn quyết định công bố |

Không cần tuyển đủ tám người để bắt đầu. Cần thực hiện đủ trách nhiệm liên quan, và ghi rõ phần chưa có năng lực/bằng chứng thay vì bỏ qua.

## 4. Các bước và điều kiện chuyển bước

| Bước | Đầu ra cần có | Được đi tiếp khi | Tình trạng hiện tại |
|---|---|---|---|
| Hiểu sản phẩm | Mục tiêu, người dùng, hai mức, phạm vi và quy tắc | Những ý nghĩa ảnh hưởng bước kế đã rõ | Đã phỏng vấn/hợp nhất; còn câu hỏi riêng từng phần |
| Chia trách nhiệm | Bản đồ khả năng và phụ thuộc | Bạn rà ranh giới, không có phần nghiệp vụ vô chủ | Bản đề xuất tại CAPABILITY_MAP.md |
| Kiểm chứng rủi ro | Đặc tả phép thử, dữ liệu thử, báo cáo thật | Có bằng chứng hoặc bạn chấp nhận giới hạn rõ ràng | E02a mới có đề cương; chưa chạy |
| Đặc tả phần sản phẩm | Hành vi, trạng thái, ngoại lệ, tiêu chí nghiệm thu, hợp đồng giữa phần | Bạn rà hành vi; thông tin kỹ thuật đủ để làm | Chưa viết/chưa duyệt |
| Thiết kế và chia việc | Phác thảo, quyết định công nghệ có lý do, việc nhỏ có kiểm chứng | Phạm vi và phương án được rà; việc đủ điều kiện bắt đầu | Chưa làm |
| Thực thi từng lát | Code, kiểm thử, bằng chứng chạy thật, ghi thay đổi | Đạt tiêu chí việc và tiêu chuẩn hoàn thành | Chưa có app native |
| Tích hợp/nghiệm thu | Luồng kết hợp, offline, hai mức, 8 giờ, ma trận máy | Không còn lỗi chặn; giới hạn được công bố/chấp nhận | Chưa làm |
| Phát hành/vận hành | Bộ cài, bản phát hành, quyền sử dụng tài sản, hướng dẫn, xử lý sự cố | Người chịu trách nhiệm duyệt công bố; phương án quay lại đã kiểm tra | Chưa làm |

Một bảng trạng thái không phải kế hoạch thực thi mọi chức năng. Chỉ chia việc chi tiết cho phần đã có đặc tả được rà. Không ước tính ngày phát hành khi rủi ro AI/quyền vẫn chưa đo được.

## 5. Cách viết đúng nghiệp vụ

Mỗi quy tắc phải trả lời: ai khởi động, điều kiện nào cho phép, điều gì thay đổi, lúc nào phải dừng, kết quả nhìn thấy và dữ liệu được giữ gì. Gắn mã yêu cầu hiện có; không tạo nguồn yêu cầu thứ hai.

Ví dụ kiểm tra DK04 và BH08:

| Trước thao tác | Sự kiện | Kết quả cần đúng |
|---|---|---|
| Đang đọc và chạy việc A, việc B chưa chạy | Người dùng bấm Tắt quan sát | Dừng đọc/điều khiển, hủy A, giữ B tạm dừng; vẫn biết hình học cửa sổ để sinh hoạt |
| Quan sát đã tắt, B đang tạm dừng | Người dùng bật quan sát lại | Chưa chạy B |
| B tạm dừng, quyền và nguồn hợp lệ | Người dùng bấm Tiếp tục hàng đợi | Xét điều kiện hiện tại rồi mới thực hiện B; A không sống lại |

Đây là ví dụ tiêu chí, chưa phải kết quả kiểm thử. Với một nút hoặc luồng mới phải rà các trạng thái: ban đầu/trống, đang xử lý, đang dở, lỗi/bị chặn, hoàn tất. Mô tả rõ chữ thông báo, cách hủy/thử lại và điều gì không tự khôi phục.

Chuỗi truy vết phải giữ được: **mã yêu cầu → tiêu chí → việc thực hiện → kiểm thử → bằng chứng → bản phát hành**. Chỉ điền đường dẫn thật khi tài liệu/code/kết quả tồn tại. Không tạo số hiệu commit hoặc ảnh chứng minh giả.

## 6. Một việc được phép bắt đầu khi nào?

- Có mục tiêu hẹp và mã yêu cầu; phạm vi không làm được cũng nêu rõ.
- Có dữ liệu đầu vào, tình huống đúng/sai và kết quả mong đợi; câu hỏi chặn đã được giải quyết.
- Phụ thuộc đã sẵn sàng hoặc được thay bằng mẫu giả được ghi rõ.
- Có cách kiểm tra, các file dự kiến thay đổi và phương án giữ mốc đang hoạt động.

Mẫu việc: mã/tên; chủ trách nhiệm; yêu cầu gốc; điều kiện trước; phạm vi; tối đa vài tiêu chí nghiệm thu rõ; cách kiểm tra; phụ thuộc; file; bằng chứng; trạng thái. Việc quá lớn để kiểm tra trong một phiên phải tách tiếp. Khi có đặc tả được duyệt mới ghi kế hoạch thực thi vào tasks/plan.md và tasks/todo.md; không tạo backlog code suy đoán lúc này.

## 7. Tiêu chuẩn hoàn thành và xử lý lỗi

- Có thay đổi đúng phạm vi, không thêm quyền hoặc chức năng ngầm.
- Đã chạy kiểm tra phù hợp; ghi lệnh/thao tác, kết quả và phần chưa kiểm chứng. Đạt trên nguồn giả phải ghi là nguồn giả.
- Đã thử tình huống lỗi quan trọng và hồi quy phần bị ảnh hưởng. Không bỏ kiểm thử hoặc giảm tiêu chí để báo đạt.
- Đã rà tính đúng, dễ hiểu, ranh giới, dữ liệu và hiệu năng liên quan. Rà cùng một AI không gọi là rà độc lập.
- Với thay đổi trải nghiệm, người dùng đã dùng thử hoặc trạng thái vẫn là chờ dùng thử; không ghi nghiệm thu thay người dùng.
- Đã lưu mốc phù hợp và cập nhật bộ nhớ/cách mở/tiến độ. Git hiện chưa thiết lập; phải thiết lập trước thay đổi code, không giả có commit.

Lỗi cần có: thao tác tái hiện, mong đợi, thực tế, môi trường, bằng chứng không chứa dữ liệu riêng và mức ảnh hưởng. Lộ nội dung bị cấm, thao tác ngoài quyền, không dừng được hoặc sai dữ liệu là lỗi chặn luồng/phát hành liên quan. Lỗi hình ảnh nhỏ ghi riêng, không đánh đồng với lỗi quyền.

Không tự sao lưu dữ liệu nhân vật để phục vụ quy trình. Quản lý phiên bản mã nguồn khác sao lưu dữ liệu người dùng. Rollback code/bộ cài không mặc nhiên khôi phục hoặc hạ phiên bản được dữ liệu; cần kiểm thử tương thích trước.

## 8. Khi có thay đổi yêu cầu

Ghi yêu cầu mới và lý do → chỉ ra quy tắc/luồng/phép thử bị ảnh hưởng → đưa phương án và đánh đổi → bạn chốt điểm sản phẩm chưa rõ → cập nhật nguồn hiện hành → sửa việc/kiểm thử liên quan. Giữ quyết định cũ ở lịch sử. Đổi framework hay định dạng dữ liệu có chi phí đảo ngược lớn phải có bản ghi quyết định, nguồn tham khảo và trạng thái đề xuất/đã chấp nhận.

## 9. Chuẩn bị phát hành đúng với app desktop

Chỉ chuẩn bị công bố sau khi cả hai mức ổn định theo yêu cầu. Thử nội bộ có kiểm soát trước không được gọi là bản phát hành công khai đã đạt.

Phải kiểm tra: cài mới/cập nhật/gỡ; khởi động Windows theo lựa chọn; tắt/ẩn/dừng; quyền hai tầng; offline; hồ sơ; xuất/nhập mật khẩu và mã khôi phục; dữ liệu không mất khi cập nhật; hai trình duyệt; nhiều màn hình/DPI; phiên 8 giờ. Ghi rõ máy và phiên bản thực sự thử.

Trước công bố phải có nguồn/giấy phép hình ảnh, runtime, model; kết quả rà thương hiệu; hướng dẫn quyền/dữ liệu/chi phí AI; danh sách giới hạn; hướng dẫn gặp lỗi và quay lại bản phù hợp. Vấn đề pháp lý cần tra nguồn hiện hành và đánh giá đúng phạm vi lúc đó; tài liệu này không xác nhận tuân thủ pháp luật hoặc tên NYUA an toàn.

Không thêm telemetry/cloud crash report. Hiện chỉ có lịch sử thao tác cục bộ 30 ngày theo BH13. Nếu cần nhận báo cáo từ người dùng phải thiết kế nội dung và xin phép riêng; không tự tải log/ảnh/khóa lên mạng.

## 10. Cách bạn làm việc mỗi buổi

1. AI đọc bộ nhớ, yêu cầu và việc đang làm; báo ngắn đang ở đâu, điều gì chặn.
2. Chọn một đầu ra kiểm chứng được. Nếu cần bạn quyết định, hỏi một câu về sản phẩm; AI tự khảo sát phần kỹ thuật.
3. AI thực hiện trong phạm vi được giao và báo bằng chứng; bạn dùng thử khi có thứ để dùng.
4. Nếu đạt thì lưu mốc, cập nhật tiến độ và học một khái niệm liên quan. Nếu lỗi thì tìm nguyên nhân trước khi mở rộng.
5. Cuối buổi ghi phần xong/chưa xong, kiểm tra đã chạy, câu hỏi mở và bước tiếp theo.

## 11. Skill được dùng ở đâu?

| Thời điểm | Skill | Đầu ra thực tế |
|---|---|---|
| Làm rõ trải nghiệm còn thiếu | interview-me | Một câu hỏi mỗi lần, quyết định được ghi lại |
| Chia trách nhiệm, mô tả điều kiện đúng | spec-driven-development | Bản đồ được rà, rồi đặc tả đúng phạm vi |
| Chuẩn chất lượng | constraint-driven-development | CONSTRAINTS.md; phân biệt quy tắc viết với kiểm tra tự động thật |
| Chia việc sau đặc tả | planning-and-task-breakdown | Kế hoạch phụ thuộc, việc nhỏ có nghiệm thu |
| Ghi lý do/tiến độ | documentation-and-adrs | Quyết định có trạng thái, tài liệu và bộ nhớ đồng bộ |
| Thiết kế/làm giao diện | strict-architect-coder, ui-ux-design-master | Hai lớp kế hoạch, DESIGN.md, trạng thái UI và kiểm tra dùng thật |
| Triển khai từng phần | incremental-implementation, test-driven-development, git-workflow-and-versioning | Lát hoạt động được, kiểm thử và mốc phiên bản |
| Khảo sát/rà kỹ thuật | source-driven-development, code-review-and-quality, security-and-hardening | Nguồn chính thức, phát hiện có bằng chứng, xử lý trước tích hợp |
| Phát hành | shipping-and-launch | Checklist desktop phù hợp, bộ cài và phương án xử lý sự cố |

Đọc và áp dụng skill đúng lúc; không coi việc liệt kê tên skill là đã chạy quy trình đó. Không áp mặc định kiểm tra website/server cho ứng dụng Windows khi không liên quan.

<details>
<summary>Phạm vi lượt tổ chức quy trình</summary>

- File: tài liệu này, CAPABILITY_MAP.md, CONSTRAINTS.md, README.md, .agents/PROJECT_MEMORY.md.
- Không thay yêu cầu sản phẩm, permissions.html, JSON gốc hoặc DESIGN.md. Không triển khai mẫu thử, app native hoặc cài dependency.
- Graphify chưa tồn tại, chưa có code app để suy ra God Node/call edge. Bản đồ khả năng là trách nhiệm đề xuất, không phải graph trích xuất code.
- Kiểm tra: liên kết nội bộ, chu trình phụ thuộc của bản đồ, trạng thái đề xuất/chưa chạy; không có build/test native để báo.

</details>
