# Module spec index — toàn sản phẩm, draft

| ID đã duyệt | Spec production để rà | Tình trạng bằng chứng |
|---|---|---|
| policy | [policy](policy.md) | Chỉ E02a nguồn giả có code/test; [SPEC-policy gốc](../../../../SPEC-policy.md) vẫn là spec mẫu đã duyệt |
| life-state | [life-state](life-state.md) | Chưa implement |
| desktop-body | [desktop-body](desktop-body.md) | Chưa asset/Unity/overlay proof |
| perception | [perception](perception.md) | Chưa real-source filter/OCR/model proof |
| task-execution | [task-execution](task-execution.md) | Chưa input/demo/queue production |
| companion | [companion](companion.md) | Chưa luồng tích hợp |
| distribution | [distribution](distribution.md) | Chưa persistence/backup/installer production |

Mỗi module dùng requirement IDs từ registry, DTO từ INTERFACES và quan hệ DATA. Phần thuật toán/runtime/file path production là đề xuất; không chuyển trạng thái sang approved chỉ vì có spec.

Command/structure/style áp dụng chung: chưa có production commands; đề xuất cấu trúc ở ARCHITECTURE, thực thi phải tạo lệnh thật trong task scope. C# core không phụ thuộc UI/Unity, validate tại boundary, không stub thành công; write tests cho invariant trước sửa hành vi. Spec không lặp lệnh .NET mẫu thành lệnh app thật.
