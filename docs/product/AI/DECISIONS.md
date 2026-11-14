# Sổ quyết định, câu hỏi mở và rủi ro

Baseline0.1 — reconciled 2026-11-14. **Định hướng đã đồng ý không biến mọi chi tiết kỹ thuật thành accepted.** Không hỏi lại các quyết định đã rõ, chỉ hỏi điểm ảnh hưởng bước chuẩn bị thực thi.

## 1. Decision ledger

| Record | Nội dung | Status / evidence |
|---|---|---|
| [ADR-001](adr/001-hybrid.md) | Unity rendering + C#/WPF host + localAI | Accepted direction theo cuộc trò chuyện/SP09; version/topology/transport chưa chọn |
| [ADR-002](adr/002-host-authority.md) | Host giữ authority, renderer/AI không phát input trực tiếp | Proposed architecture; phù hợp ranh giới quyền, cần review/integrationproof |
| ADR-003 | Thử separateprocess/IPC trước embedding Unity | Proposed; không cài plug-in hoặc chốt namedpipe chỉ từ gợi ý |
| ADR-004 | State normalpersistence khác manualbackup; không autobackup | Userdecided; storageengine/journal/migration plan proposed |
| [ADR-005](adr/005-local-ai.md) | AI local phân tích; host quyết mood/action, Unity render | Direction agreed; detailed models/algorithms pendingbenchmark |
| ADR-006 | Model/SDK/plugin/asset phải có nguồn/giấy phép | Required process; actual inventory production pending |
| ADR-007 | SRS và task toàn sản phẩm cùng được chuẩn bị theo yêu cầu user | Documentation scope authorized; chưa autoapprovespec/implementation |

Alternatives cho ADR-001: WPF-only giảm engineintegration nhưng tự làm animationtools; Unity-only thuận character pipeline nhưng vẫn cần Windowsauthority/settings; webproposal đã không được userchọn. Tradeoff hybrid: thêm IPC/packaging/sharedresources; kiểm chứng trước mở rộng.

## 2. Open decision register

| ID | Điều cần giải quyết | Ai quyết định / evidence | Chặn khi nào |
|---|---|---|---|
| D-01 | Unity version/license, overlay/hit regions/focus/fullscreen/DPI support proof. | Open research/design; no default approved | Before dependent task Ready |
| D-02 | Connection fault contract, ordering, bounded queues and reconnect protocol; recovery UX confirmed. | Confirmed behavior + residual probe; exact evidence below | Before dependent task Ready |
| D-03 | Transport, framing, message limits, peer/session authentication and abuse tests. | Open research/design; no default approved | Before dependent task Ready |
| D-04 | Measured models/runtime, package size, accuracy/resource/pass-rate budgets and supported hardware. | Open research/design; no default approved | Before dependent task Ready |
| D-05 | Gesture thresholds, mood/neglect/self-hide mapping and reconciliation spacing measured options; Shift and same-day sessions confirmed. | Confirmed behavior + residual probe; exact evidence below | Before dependent task Ready |
| D-06 | Probe event classification for return and next absence; no new product retry choice required. | Confirmed behavior + residual probe; exact evidence below | Before dependent task Ready |
| D-07 | Reviewed crypto/KDF/recovery/key storage and bounded archive design. | Open research/design; no default approved | Before dependent task Ready |
| D-08 | Memory/ledger limits and pruning/provenance implementation; do not change existing delete/fade rules. | Open research/design; no default approved | Before dependent task Ready |
| D-09 | Export settings/assets whitelist and version compatibility; advanced AI package excluded. | Confirmed behavior + residual probe; exact evidence below | Before dependent task Ready |
| D-10 | Crash/write atomicity and update interruption handling; paused explicit resume confirmed. | Confirmed behavior + residual probe; exact evidence below | Before dependent task Ready |
| D-11 | Probe suspend/resume/lock/input ordering; wait excludes sleep and preserves remainder. | Confirmed behavior + residual probe; exact evidence below | Before dependent task Ready |
| D-12 | Probe sleep/wake observation invalidation and SafetyHold; behavior confirmed, no product question. | Confirmed behavior + residual probe; exact evidence below | Before dependent task Ready |
| D-13 | Signing/update/distribution/name and license evidence; costs/public release need explicit user approval. | Open research/design; no default approved | Before dependent task Ready |
| D-14 | Visual samples/palette/prop detail/tool design and partial meal refusal; fox/bunny/apple/orange confirmed. | Confirmed behavior + residual probe; exact evidence below | Before dependent task Ready |
| D-15 | Pre-OCR/model privacy boundary feasibility and fail-closed fixtures. | Open research/design; no default approved | Before dependent task Ready |
| D-16 | Minimal playback status API and unknown handling proof; metadata scope confirmed. | Confirmed behavior + residual probe; exact evidence below | Before dependent task Ready |
| D-17 | Lesson dependency/version invalidation probe; cancellation behavior confirmed. | Confirmed behavior + residual probe; exact evidence below | Before dependent task Ready |
| D-18 | Provider error/uncertain response and per-attempt consent probe; no automatic retry. | Confirmed behavior + residual probe; exact evidence below | Before dependent task Ready |

H01–H16/K01–K09/T01–T08 gốc tại [điểm chưa chắc](../../DIEM_CHUA_CHAC.md). D-xx gom thêm câu hỏi phát hiện lúc thiết kế; không sửa chúng thành yêu cầu đã chốt. Không hỏi đồng loạt18câu khi chưa tới task liên quan.

## 3. Risk register

| Risk | Impact | Current evidence | Mitigation/gate |
|---|---|---|---|
| R-01 Masking không đủ an toàn cho nguồn thật | Lộ privatecontent trước inference | Chỉ E02a fakeproof | E02/D-15 failclosed, đo falseblock |
| R-02 Subsecondemotion với localAI+Unity không đạt | Coreexperience trễ/giật | Chưa benchmark | E04 combinedload, userdecides tradeoff |
| R-03 Overlay focus/input/DPI unstable | Cản công việc hoặc click nhầm | Chưa Unityproof | E-INT trước animationlibrary |
| R-04 Queue/IPC replay after stop | Tác động máy ngoài ý muốn | E02a1thread only | Generations/dedup/faulttests, D-02/03 |
| R-05 Relation rules thành gánh nặng hoặc dễ exploit | Trải nghiệm sai ý user | Qualitative interviews only | Narrative/state playtests, D-05 |
| R-06 Archive/migration corruption | Mất dữ liệu không auto backup | Chưa storage/crypto | Authenticated boundedimport, faulttests/manualexport policy |
| R-07 Engine/model/plugin license mismatch | Không phân phối hợp lệ, phát sinh phí | Chưa productioninventory | Licensebill + review trước chọn/mua |
| R-08 “Mọi app” được hiểu là mọi app hỗ trợ | Overpromise và hành động sai | Onlyscan intent, no compatibilitymatrix | Declare testedapp/surfaces, blockunsupported |
| R-09 Quá nhiều tài liệu nhưng code lệch | Nghiệm thu không nhất quán | Dossier generators+validation | RTM/sourcehash/review + executabletests later |

Không gán xác suất phần trăm giả hoặc ngày giải quyết chưa được đo. Mỗi risk phải có task/evidenceowner trước Ready; blocker không tự hết vì qua một sprint.

## Confirmed decisions — exact source and current interpretation

[Exact append sequence](DECISION_SOURCE_2026-11-14.md). Later clarifications supersede earlier uncertainty; no behavior below is implemented or tested by this documentation session.

### D-12: confirmed part

Khi nhân vật ngủ thì dừng quan sát; thức dậy mới tiếp tục trong phạm vi quyền hiện hành, không vượt SafetyHold/Thử đọc lại.

Residual: Probe sleep/wake observation invalidation and SafetyHold; behavior confirmed, no product question.

### D-10: confirmed part

Mở lại app giữ việc đang dở tạm dừng, hỏi trước tiếp tục; không tự chạy lại; kiểm tra quyền/an toàn hiện hành. Crash khi ghi dữ liệu/cập nhật còn phải khảo sát.

Residual: Crash/write atomicity and update interruption handling; paused explicit resume confirmed.

### D-17: confirmed part

Sửa/xóa bài học dừng việc đang dùng và hủy lượt chờ dùng bài học đó; người dùng phải giao lại. Không hủy việc không liên quan, không hoàn tác thao tác đã xong, không chuyển lượt cũ sang phiên bản mới.

Residual: Lesson dependency/version invalidation probe; cancellation behavior confirmed.

### D-06: confirmed part

Sau 3 nội dung không mở được, về sinh hoạt; chờ người dùng thao tác trở lại rồi chỉ tìm trong đợt vắng mặt tiếp theo. Không lặp cùng đợt hoặc dùng bộ đếm chờ đơn thuần để tìm lại; vẫn áp dụng quyền/chờ/không gián đoạn.

Residual: Probe event classification for return and next absence; no new product retry choice required.

### D-11: confirmed part

Không tính thời gian máy ngủ vào thời gian chờ tự mở phim/nhạc; máy thức tiếp tục thời gian còn lại, không reset chỉ vì thức. Máy ngủ khác nhân vật ngủ; quyền/khóa/phát/input vẫn áp dụng.

Residual: Probe suspend/resume/lock/input ordering; wait excludes sleep and preserves remainder.

### D-18: confirmed part

Gửi chữ lỗi hoặc chưa rõ thành công: báo lỗi, chờ bấm thử lại và xem/duyệt chữ trước mỗi lần gửi mới, kể cả chữ không đổi. Không tự gửi lại hoặc coi timeout là chưa nhận; không mở rộng loại dữ liệu/quyền.

Residual: Provider error/uncertain response and per-attempt consent probe; no automatic retry.

### D-16: confirmed part

Cho kiểm tra riêng trạng thái phát/không phát ở nền chỉ để tránh mở chồng. Không đọc tên phim/bài, hình/âm thanh, lịch sử hoặc suy gu. Lỗi/không xác định không được coi là không phát; cách lấy/độ tin cậy cần kiểm chứng.

Residual: Minimal playback status API and unknown handling proof; metadata scope confirmed.

### D-05: confirmed part

Giữ Shift rồi kéo để chuyển vị trí kể cả khi từ chối nhấc; không tính chơi/quăng hay ảnh hưởng quan hệ; không thêm tùy chọn phím. Buổi làm lành có thể cùng ngày nếu có khoảng nghỉ và tương tác thật; đóng/mở app hoặc quà liên tục không thành buổi mới. Chưa chốt phút nghỉ, số buổi/ngưỡng cử chỉ, không quà lập tức xóa tổn thương.

Residual: Gesture thresholds, mood/neglect/self-hide mapping and reconciliation spacing measured options; Shift and same-day sessions confirmed.

### D-02: confirmed part

Hình ảnh nhân vật lỗi: tạm dừng thao tác app khác; phục hồi giữ việc tạm dừng và hỏi trước tiếp tục, không tự chạy lại. Cho tiếp tục vẫn kiểm tra quyền/an toàn mới, không phát lại mù quáng; hợp đồng kết nối/mất kết nối còn mở.

Residual: Connection fault contract, ordering, bounded queues and reconnect protocol; recovery UX confirmed.

### D-09: confirmed part

Không kèm gói AI nâng cao trong sao lưu; máy mới tải lại khi cần. Vẫn giữ dữ liệu nhân vật/ký ức/thiết lập thuộc phạm vi; không tùy chọn kèm gói mỗi lần xuất; quyền máy/khóa AI ngoài không mang sang. Whitelist/tài nguyên khác/tương thích còn phải đặc tả.

Residual: Export settings/assets whitelist and version compatibility; advanced AI package excluded.

### D-14: confirmed part

Nhân vật chính chủ yếu hình người về mặt/dáng/đi đứng, không mõm cáo/bàn chân động vật; chỉ đôi tai cáo trên đầu, không tai người; tai trắng bạc lòng hồng nhạt, một đuôi cáo trắng bạc. Giữ nữ trưởng thành chibi anime pixel 128x128, tóc trắng bạc ngang eo/mái thưa, mắt đỏ hồng, da sáng ấm, áo len rộng cổ tròn hồng nhạt, váy xếp ly xám đậm trên gối, chân trần, kẹp tim đỏ rượu bên phải nhân vật. Thú bông thỏ là đồ vật riêng; trái cây là táo, nước trái cây là nước cam trong sáu món SH04, không thêm món. Màu/chi tiết thú bông, dụng cụ và hình mẫu còn chờ duyệt.

Residual: Visual samples/palette/prop detail/tool design and partial meal refusal; fox/bunny/apple/orange confirmed.
