# Quy trình vibe code từ số 0

Bạn quyết định app giúp ai, làm gì và dùng thử. AI phân tích, giải thích, viết code và kiểm tra kỹ thuật. AI có thể sai; kết quả cần được kiểm chứng.

**Nhịp làm việc:** nói rõ một việc → xem cách hoạt động → AI làm → AI kiểm tra → bạn dùng thử → lưu mốc → học một chút → làm tiếp.

## 1. Chọn một việc nhỏ

Điền `Y_TUONG_APP.md` trong cùng thư mục. Chọn nhu cầu bạn hiểu và có thể tự kiểm tra, chẳng hạn ghi chú hoặc theo dõi thói quen.

Mặc định đề xuất app chạy trong trình duyệt, chưa cần đăng nhập, thanh toán hay nhiều dịch vụ. Đây là lựa chọn khởi đầu để thảo luận, chưa phải quyết định kỹ thuật.

**Nhắn AI:**

> Chưa viết code. Đọc mô tả app, giúp tôi làm rõ ý tưởng và đề xuất bản đầu nhỏ nhất. Hỏi từng câu bằng ngôn ngữ dễ hiểu. Phân biệt điều đã thống nhất và điều bạn đang giả định.

**Đi tiếp khi:** bạn nói được app dành cho ai, làm được gì và những gì để sau.

## 2. Xem trước cách dùng

**Nhắn AI:**

> Mô tả một lần sử dụng từ lúc mở app đến khi hoàn thành. Vẽ màn hình bằng chữ. Giải thích lúc chưa có dữ liệu, đang chờ, đang làm dở, thành công và có lỗi. Chưa viết code.

Ví dụ minh họa, không bắt buộc xây app này:

```text
┌─────────────────────────────────┐
│ Công việc hôm nay               │
│ [Nhập việc cần làm............] │
│ [Thêm công việc]                │
│ □ Đọc sách                      │
│ ☑ Tập thể dục                   │
└─────────────────────────────────┘
```

Bạn kiểm tra: biết bấm đâu chưa, bấm xong có gì, nhập sai thì sao, đóng rồi mở lại có cần giữ dữ liệu không?

**Đi tiếp khi:** bạn hiểu và đồng ý luồng sử dụng; những câu hỏi ảnh hưởng đến kết quả đã được giải quyết.

## 3. Chuẩn bị nơi làm việc

**Nhắn AI:**

> Kiểm tra thư mục và công cụ hiện có trước. Đề xuất cách xây đơn giản cho phạm vi đã chốt. Nói rõ cần cài gì, để làm gì và có phí không. Việc bạn làm được thì thực hiện; việc tôi phải làm thì hướng dẫn từng bước, kèm kết quả tôi sẽ thấy.

> Chuẩn bị cách lưu mốc bằng Git và hướng dẫn mở app, kiểm tra, khôi phục phiên bản. Kiểm tra thay đổi hiện có trước khi sửa. Không ghi mật khẩu hoặc khóa truy cập vào code, tài liệu hay lịch sử Git.

Git là công cụ lưu lịch sử thay đổi. Lưu mốc trên máy chưa đồng nghĩa với có bản sao lưu ở nơi khác. Nhờ AI giải thích phương án sao lưu phù hợp trước khi cần.

**Đi tiếp khi:** mở được màn hình ban đầu; có hướng dẫn chạy thật đã kiểm tra; biết yêu cầu quay lại mốc hoạt động trước. AI phải giữ lại công việc chưa lưu trước khi khôi phục, tránh mất thay đổi.

## 4. Làm từng phần nhỏ

### A. Yêu cầu một hành vi rõ ràng

Ví dụ:

> Làm chức năng thêm công việc. Nhập tên và bấm “Thêm công việc” thì mục mới xuất hiện. Để trống thì có lời nhắc và không tạo mục trống. Chưa thêm chức năng khác.

### B. Xem mô tả trước khi sửa

> Nói ngắn gọn bạn sẽ thay đổi gì và tôi kiểm tra bằng cách nào. Nếu có mâu thuẫn thì hỏi lại. Với phần nhỏ đã rõ, tiếp tục làm trong phạm vi đã thống nhất.

### C. AI kiểm tra kỹ thuật

> Chạy kiểm tra phù hợp. Báo rõ đã chạy gì, kết quả và phần chưa kiểm chứng. Không bỏ hoặc làm yếu kiểm tra để báo thành công.

### D. Bạn dùng thử

| Tình huống ví dụ | Kết quả mong đợi |
|---|---|
| Nhập tên hợp lệ | Mục mới xuất hiện đúng. |
| Để trống | Có lời nhắc, không tạo mục trống. |
| Thêm nhiều mục | Danh sách vẫn hoạt động đúng. |
| Tải lại trang | Dữ liệu còn nếu đã thống nhất phải lưu. |

Mỗi chức năng cần tình huống kiểm tra riêng. AI kiểm tra đạt không thay thế việc bạn dùng thử.

### E. Lưu mốc

> Phần này tôi đã dùng thử và đạt. Lưu mốc phiên bản cho phần đã làm, cập nhật tiến độ và đề xuất bước nhỏ tiếp theo.

**Đi tiếp khi:** phần hiện tại đạt, hoặc bạn chủ động đồng ý để phần chưa đạt sang sau và ghi rõ giới hạn.

## 5. Xử lý lỗi

Sao chép và điền:

> Tôi đang ở: [...].
> Tôi làm lần lượt: [...].
> Tôi mong đợi: [...].
> Thực tế: [...].
> Thông báo lỗi/ảnh chụp: [...].
> Tìm nguyên nhân trước khi sửa, giữ các phần đang hoạt động và kiểm tra lại tình huống này sau khi sửa.

Nếu sửa nhiều lần vẫn lỗi:

> Dừng thêm thay đổi. Tóm tắt những gì đã thử, bằng chứng và điều chưa biết. Kiểm tra lại nguyên nhân hoặc đề xuất quay về mốc hoạt động gần nhất, giữ lại công việc hiện tại trước khi khôi phục.

Không cần tự đoán nguyên nhân. Không chạy lệnh hoặc xóa file khi chưa hiểu mục đích; hỏi AI giải thích lệnh tác động đến đâu.

## 6. Vừa học vừa ghi tiến độ

Sau mỗi phần:

> Giải thích phần này hoạt động thế nào, một khái niệm mới quan trọng nhất và một chi tiết nhỏ tôi có thể tự thay đổi để luyện tập. Hướng dẫn cách kiểm tra và hoàn tác bài tập.

Cuối buổi:

> Cập nhật .agents/PROJECT_MEMORY.md: mục tiêu, quyết định, phần đã làm, kiểm tra thực tế, lỗi còn lại, cách mở app và bước tiếp theo. Phân biệt AI đã kiểm tra với tôi đã dùng thử. Cho tôi đoạn bàn giao ngắn.

Đầu buổi sau:

> Đọc hướng dẫn và bộ nhớ dự án, kiểm tra trạng thái hiện tại, tóm tắt chúng ta đang ở đâu. Tiếp tục bước nhỏ tiếp theo; đừng làm lại phần đã hoàn thành.

## 7. Trước khi cho người khác dùng

> Kiểm tra mức sẵn sàng phát hành: các luồng chính, lỗi, dữ liệu, quyền truy cập, thông tin bí mật, chi phí, sao lưu và cách phục hồi. Báo rõ bằng chứng đã kiểm tra và điều chưa xác minh. Chuẩn bị bản có thể xem xét trước khi thực hiện thao tác phát hành cần tôi quyết định.

Với tài khoản, thanh toán hoặc thông tin nhạy cảm, tăng mức kiểm chứng và cân nhắc người có chuyên môn rà soát. Bắt đầu cho một nhóm nhỏ dùng rồi thu nhận phản hồi.

## Bảng tự kiểm tra mỗi vòng

- [ ] Tôi hiểu mục tiêu của thay đổi.
- [ ] AI giữ đúng phạm vi, ghi rõ giả định.
- [ ] Có kết quả kiểm tra và giới hạn kiểm chứng.
- [ ] Tôi dùng thử tình huống bình thường và tình huống lỗi.
- [ ] Đã lưu mốc và cập nhật tiến độ khi đạt.
- [ ] Tôi hiểu thêm ít nhất một điều, hoặc đã ghi câu hỏi để học sau.
