# Hồ sơ sản phẩm — nhân vật đồng hành desktop

Phiên bản tài liệu: 0.1, ngày 2026-11-14. **Bản tổng hợp để rà trước xây toàn sản phẩm**, không phải toàn bộ đã được duyệt hoặc mọi rủi ro đã được giải quyết. Tên NYUA vẫn là ứng viên, chưa hoàn tất tra nhãn hiệu.

## Bắt đầu ở đâu?

| Người đọc | Bắt đầu | Mục đích |
|---|---|---|
| Chủ sản phẩm/người mới | [Bộ dành cho người đọc](HUMAN/README.md) | Hiểu sản phẩm, màn hình, cách dùng, lộ trình và điều cần quyết định |
| AI/kỹ thuật/QA | [Bộ dành cho AI](AI/README.md) | SRS, ranh giới module, hợp đồng, dữ liệu, test, task và truy vết |
| Cả team | [Sổ quyết định và điểm mở](AI/DECISIONS.md) | Phân biệt đã chốt, đề xuất và chưa có bằng chứng |
| Người muốn xem hình | [Bản đồ tổng quan](diagrams/architecture.png), [luồng phát triển](diagrams/delivery.png) | Sơ đồ đã vẽ, xem cùng giải thích trong tài liệu |

## Nguồn và cách giữ hai bộ không lệch nhau

1. [Yêu cầu hiện hành](../YEU_CAU_HIEN_HANH.md) cùng câu trả lời trực tiếp của người dùng là nguồn ý nghĩa nghiệp vụ. JSON quyền và phỏng vấn cũ là lịch sử, không tự lấy lại quyền đã thay.
2. [requirements.json](AI/requirements.json) trích từng mã nguồn, giữ nguyên nội dung, kèm chủ trách nhiệm và tiêu chí kiểm tra để rà. [SRS](AI/SRS.md), [danh mục dễ đọc](HUMAN/02-YEU-CAU.md) và [truy vết](AI/TRACEABILITY.csv) được sinh từ cùng registry. Tiêu chí diễn giải chưa phải người dùng đã duyệt từng test.
3. Kiến trúc chi tiết, dữ liệu và giao diện giữa phần là **đề xuất kỹ thuật**, dù hướng Unity + C# + WPF + AI local đã được thống nhất để tiếp tục. Từng lựa chọn công nghệ cần phép thử, phiên bản và giấy phép thật.
4. Các task toàn sản phẩm ở [backlog](AI/BACKLOG.md) là bản phân rã dự kiến, không phải lệnh thực thi hoặc lịch cam kết. [tasks/todo.md](../../tasks/todo.md) vẫn là danh sách thực thi hiện tại của mẫu E02a; không ghi đè các việc chưa xong.
5. Mỗi thay đổi phải cập nhật yêu cầu/registry và các phần phụ thuộc, chạy [kiểm tra hồ sơ](AI/validate_dossier.py), ghi lịch sử. Không sửa chỉ bản người đọc hoặc chỉ bản AI rồi để hai bên khác ý nghĩa.

## Tình trạng thực tế

- Có mẫu E02a native, 53 test tự động đạt và 35 tình huống giả. [Bằng chứng](../../labs/policy-native/RESULTS.md).
- Mẫu còn kiểm tra UI và người dùng dùng thử. Không phải app nhân vật hoàn chỉnh.
- Chưa có bộ nhân vật chính thức, Unity overlay/IPC, AI/model, quyền nguồn thật, backup mã hóa hoặc bộ cài production được kiểm chứng.
- SRS toàn sản phẩm và backlog mới ở trạng thái rà soát. Có tài liệu đầy đủ về **phạm vi** không đồng nghĩa đủ bằng chứng để bắt đầu mọi task.

## Tiêu chuẩn đọc trạng thái

**ĐÃ CHỐT:** người dùng đã nêu/chấp nhận. **ĐỀ XUẤT:** phương án thiết kế để rà. **CẦN ĐO:** chỉ phép thử mới quyết định. **CHƯA CHỐT:** cần quyết định người dùng/kỹ thuật. **HOÃN:** không thuộc bản đầu. **ĐÃ THỬ HẸP:** chỉ có bằng chứng trong phạm vi thử đã ghi.

Không tuyên bố hồ sơ được chứng nhận theo một tiêu chuẩn ISO/IEEE nào. SRS dùng cấu trúc yêu cầu, ràng buộc, giao diện, nghiệm thu và truy vết phù hợp dự án này.

Xem [báo cáo kiểm tra hồ sơ](QUALITY_REPORT.md) để biết đã kiểm được gì và giới hạn còn lại. Hồ sơ không thay quyết định phê duyệt của người dùng hoặc bằng chứng chạy thật.


[Task cards và trình tự giao việc](../../tasks/README.md) · [Audit phục hồi](RECOVERY_AUDIT.md).
