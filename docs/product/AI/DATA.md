# Dữ liệu và vòng đời — logical design, chưa physical schema

Chưa chọn DB/storage engine, thuật toán mã hóa hoặc layout file production. Các entity dưới đây là đề xuất để bảo đảm nghiệp vụ; không có migration chạy trên dữ liệu thật trong đợt tài liệu.

## 1. Logical entities

| Entity | Key/scope | Nội dung | Retention/đặc điểm |
|---|---|---|---|
| InstallationSettings | installation | Startup, chosen browser, monitors, mode selection, stop key | Local; không tự thành quyền backup import |
| SourceGrant | installation + app/site identity | read/control, generation, explicit consent | Chung mọi hồ sơ, không export/import |
| Profile | profileId | Name, size, selected/frozen, schema version | Một active; import thêm, không nút tạo mới |
| CharacterState | profileId | Needs, mood, sleep clock, activity state, timestamps | Persist bình thường, khác backup |
| RelationshipState | profileId | Closeness/trust/hurt, romance enabled, gradual recovery | Không user-facing numeric panel |
| Memory | memoryId + profileId | Content, topic, importance, pinned, provenance, reinforcement | Không secret; tài liệu chỉ topic/name |
| RelationshipContribution | contributionId, memoryId association | Delta/effect metadata cần để explicit deletion | Không bản sao raw content đã xóa; tránh double reversal |
| Lesson | lessonId + profileId | Scope, steps, parameter definitions, selection meaning, enabled, version | Reset profile xóa |
| FrameRecognition | profile/site/frame identity | Cách nhận khung đã được xác nhận | Revalidate, không quyền toàn source domain |
| MediaPreference | profileId + inferred topic/category | Evidence chọn/chuyển và duration eligible | Không full browser history, không audio record |
| PropState | propId + profileId | Type, position, held/inUse/left | Max5 left; inactive profile freeze |
| ActionHistory | eventId + installation/profile ref | Time, app/site identity sanitized, operation kind, outcome |30days; xóa sớm; không ảnh/chữ riêng |
| ActiveJob/Queue | session/profile | Pending/running/paused/yielded/failed | Ephemeral; exit/profile switch cancel |
| ExternalAICredential | machine secure store candidate | Key reference | Không DB plain text, không export |

Quan hệ sơ đồ ER tại [diagrams](../diagrams/README.md). Đây là ranh giới ý nghĩa, có thể gộp bảng vật lý khi có lý do; không bắt làm mỗi entity thành một database riêng.

## 2. Provenance và retention tags

Mọi observation/memory có nguồn và purpose để không nâng quyền đọc thành lưu lâu. Tag đề xuất: ScreenGeneral, DocumentTopicOnly, ClipboardEphemeral, SensitiveExcluded, UserInteraction, LearnedInstruction, MediaPreferenceEvidence. Tag không thể do model tự gỡ.

Clipboard plaintext chỉ phục vụ ngữ cảnh lúc bảng mở, không vào memory/contribution/log/backup. Khi đóng hoặc mất quyền, buffer pending không được tiếp tục dùng. Dữ liệu tài liệu trên màn hình: chỉ topic/name được xét ghi nhớ, không tóm tắt chi tiết trá hình. API keys và credentials bị loại khỏi pipeline.

## 3. Consistency operations

**Edit memory:** update content/provenance validation, giữ contribution ban đầu. Không model tự tính lại tình cảm khi đọc lại bản sửa.

**Explicit delete:** transaction xóa content + xử lý inverse contribution nếu có + đánh dấu thao tác đã xử lý để không trừ hai lần. Bulk delete by revoked source cũng dùng cùng nghiệp vụ. Dữ liệu không được sống lại từ cache/index; việc hoàn tác do bản backup cũ do người dùng nhập là workflow import riêng, không tự phục hồi ký ức vừa xóa.

**Natural fade:** quên chi tiết nhưng giữ relationship aggregate. Không áp inverse như explicit delete. Nếu cần metadata tối thiểu để giữ tổng hợp, không giữ nội dung “đã quên” trong một cột khác. Chính sách giới hạn ledger và pin cần chốt theo D-08 trước triển khai.

**Profile switch:** stop pending/control, cảnh báo và cancel jobs, commit trạng thái old profile; đóng băng old clock; load target profile theo cùng quyền installation. Switching thất bại không được để hai active profile; UX rollback chọn profile cần được kiểm thử.

**App close/reopen:** persist selected state và elapsed anchor; reconcile elapsed needs/cooling, không fabricate episode/task/relationship interaction. Inactive profiles không reconcile elapsed. Clock skew/rollback đồng hồ cần kỹ thuật chống elapsed âm/đột biến và test, không thêm penalty không có yêu cầu.

## 4. Export/import

Archive content đề xuất: formatVersion, profile payload, character/settings scope, schemaVersions, asset/model references phù hợp giấy phép, integrity metadata. Chưa chốt có đóng gói asset/model hay chỉ tham chiếu tải lại (D-09); không hứa backup tự đủ model offline.

**Cấm:** SourceGrant hiệu lực, AI credentials, raw clipboard/screenshots, action queue có thể tự chạy, bí mật khôi phục plaintext cùng ciphertext. Thiết lập nào export là per-profile hay installation phải whitelist rõ (D-09), không export toàn thư mục data.

Mỗi export bắt buộc password và có recovery code giữ riêng. Thiết kế dùng cơ chế mật mã đã được rà; không tự tạo thuật toán. Password/recovery mở cùng archive đúng kiểm tra toàn vẹn, sai credential không lộ chi tiết. Chưa có server reset password. Import validate format/schema/size/path trước ghi; không giải nén path traversal hoặc chạy executable trong archive.

Import thành profile riêng, không merge; grants hiện tại vẫn của máy. Collision profileId phải remap nội bộ an toàn; không thay nội dung/hồ sơ đang có. Chỉ một active; không tự cho profile nhập chạy queue.

## 5. Durability, updates, uninstall

Lưu trạng thái ứng dụng bình thường cần bền vững/transaction; user cấm automatic recovery backups, không phải cấm mọi journal nội bộ của storage engine. Lựa chọn journal/crash recovery cần giải thích và rà, không âm thầm tạo bản copy lịch sử người dùng.

Migration: version kiểm trước mở, cập nhật có kế hoạch lỗi/không tương thích. Không auto backup để migration “an toàn” khi user đã cấm. Nếu không bảo toàn được mà chưa có bản xuất thủ công hợp lệ, dừng update để người dùng quyết định, không xóa data.

Reset chỉ active profile và lesson/framelearned/memory/state liên quan; grants và profile khác giữ. Xóa app data khi gỡ không tự tìm/xóa file export ở Downloads hoặc ổ khác. Không có log/cloud upload mặc định.

## 6. Verification

Transaction tests, corruption fixtures, duplicate delete, naturalfade vs explicit-delete, inactive clocks, interrupted import/export/update, wrong password/code, foreign grants/keys exclusion và test no auto backup. Expected states mô tả trước khi viết migration/crypto code; dùng dữ liệu giả.
