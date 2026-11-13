# Kiểm tra bộ hồ sơ 0.1

Ngày: 2026-11-13. Đối tượng kiểm tra là **tài liệu**, không phải phần mềm production. Người thực hiện: cùng AI tạo hồ sơ, chưa phải rà độc lập.

## Đã kiểm tra

- Registry có109 mục:100 mã nguồn và9 hàng bảng hai mức. Mỗi mã nguồn hiện hành được giữ nguyên câu chữ trong registry/SRS/danh mục người đọc.
- Source hash khớp; SRS và bản người đọc đều có đủ mục; RTM.csv khớp metadata registry.
- Có7 module specs,18 usecases,52 taskproposal, mỗi task có đầu ra/tiêu chí/verify/dependencies/fileboundary/blockers.
- Taskgraph không có cycle hoặc dependency không tồn tại. Không có requirement bảnđầu thiếu task; directfile-reader được đánh dấu deferred.
- Không biến acceptanceinterpretation hoặc taskproposal thành approved/completed. Active E02a tasks không bị ghi đè.
- LocalMarkdownlinks/fences, module/usecase/task/decision references, PNGdimensions và XML SVG parse được kiểm tra bằng validate_dossier.py.
- Đã thử3 negativecontrols trong bộ nhớ: sourcehash sai, taskselfcycle và link không tồn tại đều bị từ chối; không thay artifact thật để tạo lỗi.
-15 nguồn Mermaid + atlas;4 PNG/SVG (kiến trúc, quyền, dữ liệu, quy trình). Đã nhìn trực tiếp PNG, sửa một nhãn bị che ở sơ đồ dữ liệu và kiểm lại.
- Dữ liệu JSON/schema là file machine-readable; schema JSON được parse như JSON, chưa chạy trình kiểm JSON Schema độc lập vì máy chưa có thư viện đó.
- Không sửa appcode, cài công cụ mới, chạy benchmark hoặc bật quyền hệ thống trong đợt làm hồ sơ.

## Chưa được coi là đạt chỉ từ kiểm tra này

- User chưa rà/chấp nhận từng bản đặc tả và task toàn sản phẩm.
- Không xác nhận15 file Mermaid đã được render bằng Mermaid engine; có nguồn sửa được và4 bản hình xuất riêng bằng công cụ vẽ local.
- Không xác nhận physicalschema/IPC/model/crypto/plugins/versions/configbudgets đã chốt; xem DECISIONS và các task có blocker.
- Không xác nhận feasibility/privacy production hoặc đạt targetAI<1s/8h. Bằng chứng53tests/35fixtures chỉ thuộc E02a và vẫn có UI/useracceptance mở.
- Không có chứng nhận tiêu chuẩn ISO/IEEE, legalclearance nhãn hiệu hoặc audit an ninh độc lập.

## Cách kiểm lại

```powershell
python docs/product/AI/sync_requirements.py
python docs/product/AI/sync_backlog.py
python docs/product/diagrams/build_diagrams.py
python docs/product/AI/validate_dossier.py
```

Pillow đã có trên máy, dùng cho ảnh. Các script chỉ phục vụ hồ sơ, không phải command build/test app production. Khi source thay, sync rồi rà diễn giải acceptance và narrative thủ công; validator không tự hiểu mọi thay đổi ý nghĩa.
