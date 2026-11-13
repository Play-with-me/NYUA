# Entry point cho AI/kỹ thuật

Snapshot tài liệu 0.1 — 2026-11-13. **Không bắt đầu production implementation chỉ vì bộ hồ sơ này tồn tại.** Người dùng yêu cầu cả đặc tả/task trong cùng đợt: chúng được chuẩn bị đầy đủ để rà, chưa đồng nghĩa từng thiết kế đã được chấp nhận.

## Đọc theo thứ tự

1. ../../.. /.agents/PROJECT_MEMORY.md tại workspace (đường dẫn thật: [PROJECT_MEMORY](../../../.agents/PROJECT_MEMORY.md)); [CONSTRAINTS](../../../CONSTRAINTS.md); [CAPABILITY_MAP](../../../CAPABILITY_MAP.md).
2. [SRS](SRS.md), [registry](requirements.json), [BUSINESS_RULES](BUSINESS_RULES.md), [USE_CASES](USE_CASES.md).
3. [ARCHITECTURE](ARCHITECTURE.md), [INTERFACES](INTERFACES.md), [DATA](DATA.md), [SECURITY](SECURITY.md), [AI_LOCAL](AI_LOCAL.md).
4. [Module specs](modules/README.md), [UX](UX.md), [ART](ART.md), [QA](QA.md), [RELEASE](RELEASE.md).
5. [DECISIONS](DECISIONS.md), [BACKLOG](BACKLOG.md), [RTM](TRACEABILITY.csv), [quy trình team](TEAM.md).

## Protocol

- Source requirement IDs SP/NV/MC/SH/QD/DK/BH/XP/AI/KN/QH/HS/SL/CD giữ nguyên. `SRS-<source>` là ID trong hồ sơ; `AT-<source>` là tiêu chí kiểm tra được đề xuất, chưa phải test đã chạy.
- NFR dùng mã NFR-xx; task toàn sản phẩm dùng Pxx-yy; ca tích hợp dùng IT-xx; mã D-xx là quyết định/điểm mở. Không ghi completed cho task chỉ có tài liệu.
- `requirements.json` là bản trích có source hash; thay đổi nghiệp vụ phải sửa nguồn hiện hành trước rồi tái đồng bộ hai bản. Không tái dùng file JSON quyền gốc như policy hiệu lực.
- Danh sách thực thi vẫn ở [tasks/todo.md](../../../tasks/todo.md). Backlog mới là proposal, chuyển từng lát đã được duyệt sang tracker, không bulk-close task cũ.
- Hướng đã thống nhất: Unity rendering, C#/WPF host, local AI. Runtime topology/IPC/model/storage/schema/budgets production còn đề xuất. C# Unity không mặc định tương thích assembly .NET10 của host.
- Không có Graphify production/call edge để suy ra; sơ đồ ở đây là design. Khi có code, graph trích xuất phải khác nhãn với graph đề xuất.
- Đọc `DECISIONS` trước khi gặp một giá trị chưa biết. Không thay D-xx bằng default do AI nghĩ hợp lý.

## Cách bắt đầu một task

Tìm task → đọc requirement/spec/AT/dependency → xác nhận Ready và file scope → nêu thay đổi/cách kiểm → thực hiện nhỏ → kiểm thử/rà/runtime → cập nhật trạng thái/bằng chứng. Tác vụ chưa Ready thì giải quyết đúng blocker, không mở rộng tùy ý.

Không có lệnh build app production. Lệnh đã tồn tại chỉ cho [mẫu native](../../../labs/policy-native/README.md). Lệnh tương lai phải được ghi sau khi project/tool có thật.
