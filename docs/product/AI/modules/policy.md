# policy — quyền và ranh giới tác động

Status: production draft. Inputs authoritative: user grants/mode commands, source identity evidence, human input events. Screen text, model output, Unity callback và imported archive không được tạo grants.

## Scope và contracts

Sở hữu QD01–QD15, DK01–DK04, HS02, BH08/BH09 invariants; phối hợp chứ không sở hữu memory content. Cung cấp EvaluateRead/EvaluateAction, stop-generation và grant-revocation events theo INTERFACES. Consumer nhận safe-plan/deny hoặc one-use permit; không nhận “admin access” chung.

Installation grants theo app identity/site canonical identity; read/control riêng, browser+site AND. Chuẩn domain/subdomain phải xét origin/registrable-domain semantics được rà, không contains string. Embedded frame grant bind parent site và frame recognition, không whole thirdparty host. Incognito luôn deny; private-state unknown phải chặn cho đến khi xác định.

## State và transitions

Orthogonal flags: observationEnabled, controlEnabled, characterVisible, humanIdle, machineLock; generation tăng mọi thay đổi ảnh hưởng authority. SafetyHold per-window giữ khi không chắc sensitive-region; RetryWindow chỉ khởi động validation mới. Revocation tức thì ở host adapter/consumer path, không chỉ checkbox UI.

Human input yield khác emergency latch. Direct user job bypass initial60s, nhưng input sau đó yield. Hidden state không được tiếp tục capture/control ngầm. Metadata-only geometry path không được chứa title hoặc routing tới OCR.

## Failure cases

Malformed identity/unknown target/private region → deny. Changed source/grant/layout/input generation → discard old permit/result. Unsupported UIPI/secure desktop → deny, không escalate. Adapter không xác nhận command đã đi chưa → unknown outcome, không tự replay.

## Acceptance and prerequisites

AT-QD*, AT-DK*, IT-01/02/03/06. Phải test trên đường dữ liệu thật trước nói production đạt. E02a hiện chứng minh fixture filtering/revision/retry ở một owner thread, chưa chứng minh OS capture/IPC.

Ready blockers: D-02/03 (IPC identity/order), D-01 (overlay/input), K02/K03/K04 real adapters. Không cần chờ model để test quyền trên sentinel sources; phải có quyền/fixtures hợp pháp và kế hoạch không dùng dữ liệu cá nhân.

<!-- CONFIRMED-2026-11-14 -->
## Quyết định hiện hành 2026-11-14 — ưu tiên hơn wording nháp cũ

Sinh từ registry; chỉ phần sau nhãn quyết định là bổ sung đã xác nhận. Chưa triển khai/chưa nghiệm thu; chi tiết kỹ thuật còn mở trong DECISIONS.

- **SH01:** D-12: Khi nhân vật ngủ dừng quan sát; thức dậy chỉ tiếp tục trong quyền hiện hành, không vượt SafetyHold/Thử đọc lại.
- **QD04:** D-12: Nhân vật ngủ dừng quan sát; thức dậy không tự cấp quyền hoặc bỏ qua SafetyHold/Thử đọc lại.
- **XP05:** D-16: Được kiểm trạng thái đang phát/không phát ở nền tối thiểu để tránh mở chồng; không đọc tên/nội dung hoặc suy gu. Lỗi/không xác định không coi là không phát; API/độ tin cậy cần kiểm chứng.
- **AI02:** D-18: Gửi chữ lỗi/chưa rõ thành công thì báo lỗi và chờ bấm thử lại; xem/duyệt chữ trước mỗi lần gửi mới kể cả chữ không đổi. Không tự gửi lại, không coi timeout là chưa nhận, không mở rộng loại dữ liệu/quyền.
