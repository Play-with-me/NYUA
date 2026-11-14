# Bắt đầu đọc và giao việc — hồ sơ phục hồi 2026-11-14

**Chỉ tài liệu, không cho phép xây sản phẩm hoặc công bố.** Mẫu E02a còn nghiệm thu người dùng/resize/keyboard trong [todo.md](todo.md); bản này không đánh dấu hoàn thành thay người dùng.

Đọc [yêu cầu hiện hành](../docs/YEU_CAU_HIEN_HANH.md), [bản người đọc](../docs/product/HUMAN/README.md), [SRS](../docs/product/AI/SRS.md), [quyết định](../docs/product/AI/DECISIONS.md), rồi [backlog](../docs/product/AI/BACKLOG.md). Registry duy nhất cho task: `docs/product/AI/backlog.json`; không sửa thẻ sinh tự động. Có 219 task dự kiến: 52 lát đầu ra gốc, 7 bootstrap, 18 đề cương nghiên cứu, 18 rà đề cương, 109 bảng nghiệm thu theo mã nguồn (QD07 hoãn), 10 kiểm phi chức năng, 5 checkpoint. Các bảng V00 bổ sung bằng chứng cho owner triển khai, không thay việc triển khai.

## Trình tự giao việc

1. Rà P00-01 và nguồn quyết định; yêu cầu hiện hành thắng chi tiết nháp. Chỉ giao phạm vi tài liệu đã cho phép.
2. Với lát được chọn, đọc dependencies trong registry; chạy `python tasks/dispatch.py` để xem thứ tự topo. Thứ tự nhóm/pha không tạo dependency.
3. R00 lập đề cương cho phần kỹ thuật chưa biết; A00 rà đề cương trước phép thử. Đây không phải chốt kết quả chưa đo và không hỏi lại quyết định đã xác nhận.
4. B00 tạo fixture/runner trong whitelist đề xuất sau khi có phép riêng. B00 không cần runner đã chạy để bắt đầu; B00-02 tự sở hữu fixture Unity riêng với năm đường dẫn tường minh, không đợi project P02-01; hoàn thành cần fixture dương chạy đạt và fixture âm trả lỗi, timeout/cleanup hữu hạn. Chỉ khi đó mới ghi lệnh thực vào task con; không task con nào Ready trước bootstrap.
5. Khi có phép thực thi riêng, giao từng P-task theo dependencies và file boundary; các V-task kiểm từng điều khoản sau owner triển khai. N-task kiểm ngưỡng thực; số chưa chốt giữ Blocked. Dùng bản nháp/NOT RUN khi chưa có kết quả.
6. C00-04 gom mọi V/N; P60-04 và P60-05 nằm sau gate này. Nghiệm thu E02a, mẫu hình/hoạt ảnh và nghiệm thu toàn sản phẩm cần phản hồi người dùng thật. Checkpoint không cấp quyền triển khai/công bố.

Không dispatch song song task có đường dẫn ghi giao nhau; validator kiểm thứ tự các writer. Các bước render, capture, AI, lưu dữ liệu, cài/cập nhật đều chưa chạy trong phiên tài liệu này. Nếu bước quá lớn cho một lát nghiệm thu hoặc vượt whitelist thì tách ID con trước Ready, không tự giảm tiêu chí.

## Mẫu prompt giao việc

```text
Đọc task <ID> trong backlog.json và thẻ sinh tương ứng, PROJECT_MEMORY, CONSTRAINTS, yêu cầu/DECISIONS liên quan.
Phạm vi hiện tại: chỉ tài liệu. Không product implementation, không push/PR, không tự cấp quyền chạy phép thử.
Vai trò/mô hình đúng execution của task: research/memory/QA = agy gemini-3.8-flash; UI/features = agy gemini-4-hydrogen-low; core/bug/finalreview = codex gpt-6.1-sol effort low.
Đọc dependencies và blocker; báo rõ chưa có bằng chứng/không có runner. Không hỏi lại câu đã chốt.
Chỉ sửa file đã được phép thực tế. Proposed path không tự là quyền tạo sản phẩm.
Khi được cho thực thi riêng: kiểm scope bootstrap, expected/actual từng acceptance ID, case âm/gián đoạn, version/lệnh/exit-code và revision; human gate chỉ đóng với phản hồi thật.
Kết thúc: báo thay đổi, kiểm thật đã chạy, còn NOT RUN, blocker và checkpoint; đồng bộ registry và thẻ, không đánh dấu sản phẩm sẵn sàng phát hành.
```

## Kiểm hồ sơ thực có

PowerShell, từ gốc repository hoặc gốc ZIP đã giải nén:

```powershell
$py = 'C:/Users/phamp/AppData/Local/Programs/Python/Python312/python.exe'
& $py docs/product/AI/sync_requirements.py
& $py docs/product/AI/sync_decisions.py
& $py docs/product/AI/sync_backlog.py
& $py tasks/validate_tasks.py --negative-controls
& $py docs/product/AI/validate_dossier.py
```

`$py` là interpreter thực dùng trong phiên này, có Pillow; máy khác cần Python có Pillow để đọc container ảnh. `python` mặc định trên máy này là MSYS thiếu Pillow. Không chạy Get-Content thay test. JSON Schema độc lập chưa chạy vì không có jsonschema. Không có lệnh build/test production đã chứng minh; chúng do B00 thiết lập và chặn trước Ready.

Task document_review (P00/R00/A00/checkpoint) không có prerequisite runner thực thi; chỉ cần nguồn và kiểm hồ sơ thực có. Checkpoint completion vẫn đòi bằng chứng các producer dependencies.

Dossier controls có thể chạy lại an toàn bằng Python312 docs/product/AI/check_dossier_controls.py; script chỉ sửa bản sao TEMP rồi tự dọn.
