# companion — điều phối trải nghiệm và ứng dụng quản lý

Status: draft. Combines states without taking ownership of policy bypass, raw capture or storage format. SP*, MC*, XP* trải nghiệm tích hợp và UX routes.

## Coordination

One owner/scheduler serializes current intent and policy generation updates; UI command, human input, context/model and Godot events are typed events, not arbitrary method calls. Host output decides render intent, job request or no-action. Model may suggest affect, not execute.

Life-state supplies possible own activities; policy filters real-app actions; taskengine executes eligible jobs; body renders. “Mood ownwill” cannot refuse to expose settings/reset/stops, and cannot mutate grants. Prefer simple typed calls until asynchronous topology is justified; no generic agent tool executor with unrestricted desktop tools.

## UX ownership

First run name/startup/mode recommendation, tray opens full settings; contextmenu food/cleanup. Settings source/model/profile/queue/memory controls must show state and precise errors. No numeric mood/dashboard, no correction-emotion feedback, no chat. Menu grouping is draft in UX and human03.

Mode change preserves advanced state and suspends expression; not a data reset. Hardware recommendation from measured combined workload; user chooses unsupported trial after warning. Per-monitor placement and resize do not change source grants.

## Media orchestration

User playback preservation takes precedence. Advanced idle5m default and nomedia+unlocked+grants → own tab chosen browser. Return userinput yields but playback remains. Capture unavailable still lets life-state choose stay/play/eat. Taste from allowed evidence and user transitions; not a guarantee user watches every elapsed second.

No interruption of user media except allowed next after end. Basic lesson on same source permitted only direct request. Respect direct-request priority and yield rules without resetting media attempt counter or attention cooldown.

## Resilience and acceptance

Separate productstate from UI loading/error; renderer unhealthy state must not hide host settings. IPC failure safeaction blocking needs D-02. AT-SP02, MC*, XP*, IT-04/06/09/10/11/18. Complete verticalslice with real dependencies is required; individual demos don't meet SP02.

<!-- CONFIRMED-2026-11-14 -->
## Quyết định hiện hành 2026-11-14 — ưu tiên hơn wording nháp cũ

Sinh từ registry; chỉ phần sau nhãn quyết định là bổ sung đã xác nhận. Chưa triển khai/chưa nghiệm thu; chi tiết kỹ thuật còn mở trong DECISIONS.

- **SP09:** D-02: Hình ảnh lỗi thì tạm dừng thao tác lên app khác; phục hồi vẫn tạm dừng và hỏi trước tiếp tục, kiểm quyền/an toàn mới. Không phát lại mù quáng; hợp đồng kết nối/mất kết nối còn mở.
- **NV01:** D-14: Nhân vật chính chủ yếu hình người về mặt/dáng/đi đứng, không mõm cáo/bàn chân động vật. Chỉ đôi tai cáo trên đầu, không tai người; tai trắng bạc lòng hồng nhạt; một đuôi cáo trắng bạc. Giữ nữ trưởng thành chibi anime pixel 128x128, tóc trắng bạc ngang eo/mái thưa, mắt đỏ hồng, da sáng ấm, áo len rộng cổ tròn hồng nhạt, váy xếp ly xám đậm trên gối, chân trần, kẹp tim đỏ rượu bên phải nhân vật.
- **NV02:** D-14: Giữ tóc/mắt/da đã chốt; tai trắng bạc lòng hồng nhạt và một đuôi trắng bạc đồng bộ tóc. Chỉ tai cáo, không tai người; không thay ngoại hình đã duyệt.
- **XP05:** D-16: Được kiểm trạng thái đang phát/không phát ở nền tối thiểu để tránh mở chồng; không đọc tên/nội dung hoặc suy gu. Lỗi/không xác định không coi là không phát; API/độ tin cậy cần kiểm chứng.
- **XP07:** D-06: Sau 3 nội dung không mở được về sinh hoạt; chờ người dùng thao tác trở lại rồi chỉ tìm trong đợt vắng mặt tiếp theo. Không tìm lặp cùng đợt hoặc chỉ dùng bộ đếm để mở lại tìm kiếm; quyền/chờ/không gián đoạn vẫn áp dụng.
- **XP08:** D-11: Máy ngủ không cộng thời gian chờ mở phim/nhạc; máy thức tiếp tục phần còn lại, không reset chỉ vì thức. Giữ quyền/khóa/input/phát đã chốt, máy ngủ khác nhân vật ngủ.
- **AI02:** D-18: Gửi chữ lỗi/chưa rõ thành công thì báo lỗi và chờ bấm thử lại; xem/duyệt chữ trước mỗi lần gửi mới kể cả chữ không đổi. Không tự gửi lại, không coi timeout là chưa nhận, không mở rộng loại dữ liệu/quyền.
