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
