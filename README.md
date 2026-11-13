# Dự án nhân vật sống trên desktop

## Đọc trước — trạng thái hiện hành

1. [Yêu cầu hiện hành](docs/YEU_CAU_HIEN_HANH.md): các quyết định đã hợp nhất và những lựa chọn cũ được thay thế.
2. [Điểm chưa chắc](docs/DIEM_CHUA_CHAC.md): tách việc cần hỏi người dùng, khảo sát và chạy thử.
3. [Đề cương kiểm chứng](docs/KE_HOACH_KIEM_CHUNG.md): sáu phép thử nhỏ trước khi xây toàn bộ; chưa chạy.
4. [Phép thử đầu tiên](docs/PHEP_THU_DAU_TIEN.md): ranh giới quan sát trên dữ liệu giả, 16 tình huống và tiêu chí đánh giá; mới chuẩn bị, chưa chạy.

Đang chuẩn bị và rà soát yêu cầu. Chưa chọn công nghệ hoặc viết ứng dụng nhân vật. Windows 11, tiếng Việt, hai mức cơ bản/nâng cao; công khai miễn phí bản đầu, chưa công khai mã nguồn.

## Quy trình làm sản phẩm

- [Quy trình team](docs/QUY_TRINH_TEAM_SAN_PHAM.md): trách nhiệm, đầu ra, điều kiện chuyển bước và cách làm mỗi buổi.
- [Bản đồ khả năng](CAPABILITY_MAP.md): ranh giới đề xuất cần rà trước đặc tả từng phần.
- [Đặc tả phép thử quyền hạn](SPEC-policy.md): E02a trên dữ liệu giả đã được duyệt; chưa có code hoặc kết quả chạy.
- [Kế hoạch xây mẫu native](tasks/plan.md) và [danh sách việc](tasks/todo.md): C# + WPF, đang chờ rà trước triển khai; đặc tả E02a đã được duyệt.
- [Tiêu chuẩn chất lượng](CONSTRAINTS.md): quy tắc bằng văn bản và các kiểm chứng chưa chạy.

## Trang chọn quyền nhân vật — bản lịch sử

Mở `permissions.html` bằng trình duyệt (nhấp đúp tập tin). Tick quyền, ghi điều kiện rồi bấm **Tải bản lựa chọn (.json)** để lưu và gửi lại cho AI. Trang chạy độc lập, không cần cài thư viện hoặc máy chủ; đây chỉ là bản yêu cầu, không cấp quyền hệ thống. Lựa chọn được thử lưu trong trình duyệt; tải JSON để có bản sao chắc chắn hơn.

**Lưu ý:** trang HTML và [JSON đã chọn](docs/quyen-nhan-vat-da-chon.json) là lịch sử phỏng vấn. Những quyết định mới trong bản yêu cầu hiện hành chưa được cập nhật vào giao diện hoặc JSON; không dùng trực tiếp làm cấu hình quyền có hiệu lực.

## Tài liệu học

Bộ hướng dẫn dành cho một người mới học cùng một AI.

1. Đọc [Quy trình từng bước](docs/QUY_TRINH_VIBE_CODE.md).
2. [Mẫu mô tả app đầu tiên](docs/Y_TUONG_APP.md) là tài liệu học, không thay bản yêu cầu đã hợp nhất.
3. Với dự án này, đọc ba tài liệu hiện hành ở trên trước khi tiếp tục; không bắt đầu phỏng vấn lại từ đầu.

Chưa có lệnh chạy/build/test cho ứng dụng nhân vật. Các ví dụ app công việc trong hướng dẫn học không phải yêu cầu của dự án.

Tiến độ và quyết định được lưu tại [Bộ nhớ dự án](.agents/PROJECT_MEMORY.md).
