# Việc thực hiện E02a native

Ngày: 2026-11-13. **Bản chia việc đề xuất cùng kế hoạch, chờ duyệt trước thực thi.** Chủ trách nhiệm kỹ thuật: AI; người dùng quyết định thay đổi phạm vi và nghiệm thu trải nghiệm. [Kế hoạch](plan.md), [đặc tả đã duyệt](../SPEC-policy.md).

## T00 — Chuẩn bị công cụ và mốc phiên bản

- [ ] Kiểm tra/cài .NET SDK từ nguồn chính thức, ghi phiên bản thật; không có khoản chi hoặc công cụ không cần thiết.
- [ ] Kiểm tra trạng thái thư mục rồi thiết lập Git, ignore output build/test và giữ mốc tài liệu hiện có; không push, không đổi Git config toàn máy.
- [ ] Có global.json ghim SDK và ghi cách chạy; chưa đánh dấu code/test hoàn tất.

Phụ thuộc: kế hoạch được duyệt. File: labs/policy-native/global.json, .gitignore, labs/policy-native/README.md; metadata .git do Git tạo. Kiểm chứng: dotnet --info, git status, rà file chuẩn bị trước commit. Phạm vi: nhỏ; nếu cài cần thao tác của người dùng, chỉ yêu cầu đúng thao tác đó.

## T01 — Quyết định quyền cho một nguồn giả

- [ ] Core có hợp đồng có kiểu, input không hợp lệ bị chặn; payload không được dùng để thay quyền.
- [ ] Cho phép/chặn theo app, web hai tầng, hiển thị, riêng tư và vùng nhạy cảm; toàn vùng nhạy cảm không gọi phân tích.
- [ ] Kiểm thử đơn vị đối chiếu kỳ vọng độc lập và kiểm tra đầu ra không chứa payload cấm.

Phụ thuộc: T00. File: PolicyLab.Core/PolicyLab.Core.csproj, Contracts.cs, PolicyEvaluator.cs; PolicyLab.Tests/PolicyLab.Tests.csproj, PolicyEvaluatorTests.cs (đều trong labs/policy-native). Kiểm chứng: dotnet test với project Tests, tập trung các rule A01–A09/A16 và B01/B02/B06. Phạm vi: vừa, tối đa 5 file.

## T02 — Lượt đọc bị hủy và Thử đọc lại

- [ ] Coordinator hủy dữ liệu chờ nếu revision nguồn/quyền/quan sát đổi; điểm giao dữ liệu cuối đồng bộ và receiver nhận tối đa một lần mỗi attempt.
- [ ] SafetyHold chỉ được kiểm tra lại qua Thử đọc lại, thất bại giữ chốt; metadata sinh hoạt không chứa tiêu đề/nội dung.
- [ ] Có test hủy, bật/tắt nhanh, callback muộn, gọi trùng và lỗi receiver; ERROR không thành BLOCK đạt.

Phụ thuộc: T01. File: Core/ReadCoordinator.cs, Core/Contracts.cs, Tests/ReadCoordinatorTests.cs. Kiểm chứng: dotnet test, receiver spy, revision/attempt lifecycle theo A10–A15/B03–B05. Phạm vi: vừa, 3 file.

### Checkpoint C1 — Ranh giới core

- [ ] Test core liên quan đạt; dữ liệu cấm không ở receiver/diagnostic; không có stub/suppression để che lỗi.
- [ ] Rà hợp đồng so SPEC-policy.md; chưa nói đạt E02a vì chưa có đủ fixture/UI.

## T03 — Danh mục tình huống và bộ chạy

- [ ] Catalog đủ A01–A16, tách từng biến thể được đặc tả, kèm B01–B06; định nghĩa expected tách thuật toán.
- [ ] Runner khởi tạo trạng thái mới cho từng case, có điểm chờ điều khiển được; cùng core cho UI và test.
- [ ] Báo từng case/biến thể, receiver count và dữ liệu safe nhận được; thiếu case hoặc ERROR không thể báo toàn bộ đạt.

Phụ thuộc: T02. File: Scenarios/PolicyLab.Scenarios.csproj, ScenarioCatalog.cs, ScenarioRunner.cs, Tests/ScenarioTests.cs, Tests/PolicyLab.Tests.csproj. Kiểm chứng: dotnet test toàn project Tests; inventory case/biến thể và kiểm tra không rò dấu cấm. Phạm vi: vừa, 5 file.

## T04 — Cửa sổ WPF mở được

- [ ] Có cửa sổ native, nhãn dữ liệu giả, bố cục theo DESIGN.md và các vùng kết quả; không WebView/browser/server.
- [ ] Core/Scenarios được tham chiếu đúng, app build/chạy không đọc máy hoặc gọi mạng.
- [ ] Cửa sổ mở/đóng và resize được, nội dung dài cuộn/xuống dòng; không dùng screenshot như bằng chứng nghiệp vụ đã đạt.

Phụ thuộc: T03. File: App/PolicyLab.App.csproj, App.xaml, App.xaml.cs, MainWindow.xaml, MainWindow.xaml.cs. Kiểm chứng: dotnet build App, mở app native và quan sát runtime. Phạm vi: vừa, 5 file.

### Checkpoint C2 — Logic và cửa sổ

- [ ] Test catalog/core đạt, app build và mở được; cập nhật lệnh thực tế trong README mẫu.
- [ ] Rà sự khác biệt giữa fixture giả và khả năng hệ thống thật; chưa đóng E02a khi chưa dùng được đầy đủ luồng UI.

## T05 — Dùng thử quyền và kết quả trong cửa sổ

- [ ] Chọn case/chỉnh quyền/chạy/chờ/hủy/thử lại/đặt lại đều nối cùng coordinator; không hardcode kết quả theo nhãn case.
- [ ] UI phản ánh đúng năm trạng thái; bộ nhận thực tế trống khi chưa giao; tắt/thu hồi xóa payload hiển thị cũ, giữ diagnostic đã lọc.
- [ ] Keyboard/focus, nút có lý do vô hiệu và thông báo lỗi đúng; nội dung giống HTML/lệnh chỉ được hiển thị như văn bản.

Phụ thuộc: T04. File: App/LabViewModel.cs, App/MainWindow.xaml, App/MainWindow.xaml.cs, Tests/ScenarioTests.cs. Kiểm chứng: test hồi quy và thao tác native các luồng đại diện A05, A09–A15, A16, B02–B05. Phạm vi: vừa, 4 file. Nếu cần tách thêm test ViewModel, chia task trước khi vượt 5 file.

## T06 — Bằng chứng và bàn giao dùng thử

- [ ] Chạy trọn test, build và thử runtime; báo riêng chưa kiểm chứng về mạng/UI nếu công cụ không cung cấp bằng chứng đủ.
- [ ] Báo cáo lưu mã/biến thể, expected/actual, môi trường, lệnh thật và giới hạn; chưa chạy khác chưa đạt, không có bí mật/dữ liệu thật.
- [ ] Có hướng dẫn mở/dừng/chạy test, cập nhật tiến độ và mốc Git sau rà; người dùng có mẫu để dùng thử.

Phụ thuộc: T05. File: labs/policy-native/RESULTS.md, README.md, tasks/todo.md, .agents/PROJECT_MEMORY.md, CONSTRAINTS.md (chỉ trạng thái kiểm tra thật, không hạ tiêu chí). Kiểm chứng: các lệnh trong plan, rà mã đường dữ liệu/log/mạng, quan sát runtime; rà diff trước commit. Phạm vi: vừa, 5 file.

### Checkpoint C3 — Nghiệm thu E02a

- [ ] A01–A16 với mọi biến thể và B01–B06 đạt, không rò dữ liệu thử bị cấm.
- [ ] Có bằng chứng runtime/log/đường dữ liệu; phần chưa kiểm chứng được ghi rõ và không đóng phép thử nếu là tiêu chí bắt buộc.
- [ ] Người dùng đã dùng thử và phản hồi; chỉ sau đó mới ghi nghiệm thu trải nghiệm.
- [ ] Không kết luận đã đạt capture thật, tích hợp Unity hoặc AI cục bộ. Bước sau phải quay lại phạm vi/phép thử tương ứng.

## Việc kế tiếp ngoài đợt này

Chưa tạo task code cho Unity hoặc AI. Sau rà kế hoạch: đặc tả phép thử kết nối riêng (WPF/C#, Unity, transparency, vùng nhận chuột, mất kết nối và tài nguyên), rồi mới chia việc. Không nhét thêm tích hợp Unity/AI vào T00–T06.
