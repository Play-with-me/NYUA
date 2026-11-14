# task-execution — demonstration, execution and queue

Status: draft. Owns BH01–13 workflows; policy owns permissions. Learned lessons never autonomous triggers. Advanced exploration is a separate source of bounded intents, not replay of enabled lessons.

## Demo and review

States: Idle→RecordingExplicit→DraftReview→Saved or Discarded. Record only authorized scope, no raw keylogging. Crossing app/site ends/stops recording rather than saving unapproved multiscoped lesson. Summary includes steps, scope, search parameter slots and target selection first-result/exact-item. User confirmation required; cannot infer selection semantic from coordinates.

Lesson management view/rename/enable/delete/reteach perprofile, versions explicit. Request snapshot version+parameter validation; editing lesson while queued/running needs D-17 decision before execution coding. No typing outside search/navigation, even if demonstrated.

## Run lifecycle

Requested→DelayedOnce/Queued→Checking→Approaching→Rechecking→Acting→Verifying→Succeeded. Orthogonal branches YieldedHuman, PausedByStop, FailedNeedsTeaching, Cancelled. Only final postcondition establishes success; SendInput accepted events not enough.

Direct request starts without initial60s unless mooddelayonce. Repeat request can promote existing delayed intent, not duplicate a new job (dedupe request semantic), must still satisfy policy. Without repeat, job remains pending after own activity ends. Job precedence over autonomous exploration; own-play cleanup request semantics remain separate.

Human input yields immediately then60s eligibility; may refocus old allowed app/site. Before resume reidentify target; mismatched UI stops at failingstep, asks reteach. Later queue entries need independent eligibility; no claiming previousfailed job success.

Emergency/observationoff/manualhide/selfhide cancel running and pause unstarted. Show/re-enable doesn't resume until ResumeQueue. Exit/profile switch warns+cancels all unfinished, no persistent queue auto-replay. Disconnect/crash semantics outside these explicit cases need D-02/10.

## Side effects and controls

Action allowlist navigate/search/allowedclick; deny writes/deletes/messages/forms/payment/mark-read. Do not “test click” to discover if unsafe. Inspect element/surface purpose; if unknown block. Adclose only clearly identified origin, uncertain tab kept while return film; freecontent max3.

## Acceptance

E03/IT-03/06/14. Changedtarget after approach; revoked grants between checks; duplicate callback; interrupted verify; failure with unknown sideeffect; scopeswitch demo; first-result with changed search query; explicitsecondrequest dedupe. Logs sanitized30days via distribution, no raw typed text.

<!-- CONFIRMED-2026-11-14 -->
## Quyết định hiện hành 2026-11-14 — ưu tiên hơn wording nháp cũ

Sinh từ registry; chỉ phần sau nhãn quyết định là bổ sung đã xác nhận. Chưa triển khai/chưa nghiệm thu; chi tiết kỹ thuật còn mở trong DECISIONS.

- **SP09:** D-02: Hình ảnh lỗi thì tạm dừng thao tác lên app khác; phục hồi vẫn tạm dừng và hỏi trước tiếp tục, kiểm quyền/an toàn mới. Không phát lại mù quáng; hợp đồng kết nối/mất kết nối còn mở.
- **BH02:** D-17: Sửa/xóa bài học dừng việc đang dùng và hủy lượt chờ dùng bài học đó; người dùng giao lại, không chuyển lượt cũ sang phiên bản mới, không hủy việc không liên quan hoặc hoàn tác thao tác đã xong.
- **BH06:** D-02/D-10/D-17: Renderer lỗi thì tạm dừng thao tác app khác; hình ảnh phục hồi hoặc mở lại app giữ việc tạm dừng và hỏi trước tiếp tục, kiểm quyền/an toàn mới, không phát lại mù quáng. Sửa/xóa bài học dừng việc đang dùng và hủy lượt chờ dùng bài học đó, phải giao lại; không hủy việc không liên quan hoặc hoàn tác việc đã xong.
- **XP05:** D-16: Được kiểm trạng thái đang phát/không phát ở nền tối thiểu để tránh mở chồng; không đọc tên/nội dung hoặc suy gu. Lỗi/không xác định không coi là không phát; API/độ tin cậy cần kiểm chứng.
- **XP07:** D-06: Sau 3 nội dung không mở được về sinh hoạt; chờ người dùng thao tác trở lại rồi chỉ tìm trong đợt vắng mặt tiếp theo. Không tìm lặp cùng đợt hoặc chỉ dùng bộ đếm để mở lại tìm kiếm; quyền/chờ/không gián đoạn vẫn áp dụng.
- **XP08:** D-11: Máy ngủ không cộng thời gian chờ mở phim/nhạc; máy thức tiếp tục phần còn lại, không reset chỉ vì thức. Giữ quyền/khóa/input/phát đã chốt, máy ngủ khác nhân vật ngủ.
- **CD01:** D-10: Mở lại app giữ việc đang dở tạm dừng, hỏi trước tiếp tục; không tự chạy lại, vẫn kiểm quyền/an toàn hiện hành. Crash ghi dữ liệu/cập nhật còn cần khảo sát.
