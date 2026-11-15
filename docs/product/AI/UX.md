# UX specification — native app và nhân vật

Draft screen design. Nghiệp vụ lấy SRS/BUSINESS_RULES, không thêm chat/score/focusmode. [Human wireframes](../HUMAN/03-TRAI-NGHIEM.md) là phần giải thích. DESIGN.md vẫn là token source: #f5f6f8/#202b38/#155e52, systemfont16, spacing4/8; áp sang XAML/Godot UI phù hợp.

## 1. Information architecture

Routes đề xuất: FirstRun; Settings.Character; Settings.Modes; Settings.Permissions.Apps/Sites/Frames; Settings.Lessons; Settings.Queue; Settings.Memories; Settings.Relationship; Settings.Profiles; Settings.Backup; Settings.History; Settings.StartupUpdate; Settings.Help. Trayclick opens fullsettings; no hidden separate quickmenu replacing it. Avatarcontextmenu has Food/Cleanup only per agreed first scope.

| Route | Primary action | Secondary action | Dangerous/blocking state |
|---|---|---|---|
| FirstRun | Bắt đầu sinh hoạt | Xem mức hoạt động | Missingname rule TBD; no signupwall |
| Modes | Chọn cơ bản/nâng cao | Kiểm tra cấu hình/tải gói | Downloads showing actualsize, cancel, failedintegrity notready |
| Permissions | Bật/tắt đúng nguồn | Thêm website | Controlneedsread, unclear safe-region blocked |
| Lessons | Dạy thao tác / Thực hiện bài | Rename/enable/reteach/delete | Crossscope recording stops; no autosavebeforeconfirm |
| Queue | Tiếp tục hàng đợi | Hủy từng việc | Re-enable chưa resume; runningcancel explicit |
| Memories | Lưu sửa đổi / Ghim | Xóa từng ký ức | Explain relation impact on delete; edit no recalc |
| Relationship | Bật/tắt lãng mạn | Invite/leavegift whenhidden | Off asks keep/delete; no pressure text |
| Profiles | Chọn hồ sơ đã có | Import/reset | Switching warns unfinishedtasks; no create-new |
| Backup | Xuất bản sao / Nhập bản sao | Copy/cất riêng recoverycode | Requirepassword, wrongcredential clear, no keys/grants |
| History | Xem/lọc localhistory | Xóa history | No content payload; retention30days explicit |
| Update | Kiểm tra / Cài và khởi động lại | Để sau | No install without confirmation |

## 2. Five-state matrix

| Flow | Empty | Loading/cancel | Partial | Error | Success |
|---|---|---|---|---|---|
| Appscan/grants | No selectedsource, alloff | Scanning indicator | List partially unsupported | Identityunknown explanation | Grantstate visible, no capabilityoverpromise |
| Websafety | No allowedsite | Checking/stop | Safehold persists | Unsafe/private/unknown distinct | Only safe snapshot permitted |
| Lesson | Nolesons CTA teach | Recording with Stop | Draftreview unsaved | Targetmismatch needsreteach | Saved scopedversion |
| Job | Emptyqueue | Running step + cancel | Human-yield/paused-by-stop distinct | Failedatstep, nextjob eligibility | Verifiedpostcondition, not injectionack |
| AIpackage | Notinstalled | Size/progress/cancel | Downloadpresent but notvalidated | Corrupt/disk/network | Packagevalidated and chosentoggle |
| Backup | No archive selected | Export/import cancel safe | Credential/recovery step | Invalidarchive/wrongcredential | User sees file/profile created |
| Update | No knownupdate | Checking/downloading | Downloaded waiting user | Bad signature/schema | Restart completed + versioncheck |

Progress must reflect real work; no fake timed progress completing by itself. Long-lived work cannot cover all settings/stops with modalspinner. Exact cancel semantics of export/install need preimplementation design, don't claim all actions atomically reversible.

## 3. Avatar experience

Activity/mood reflected by art, not functional toasts every action. Attention invitations at most2+cooldown. Humanactive avatar still moves/lives but avoids cursor/typing zone; user may manually reposition subtitles/props. Modifier-drag is administrative reposition, no throw/relation penalty. Hotkey choice/thresholds remain D-05.

When relationalhidden, settings still invite/leaveexistingfood/plush; small locationmarker allowed by earlier choice, visibility and its interaction need designreview. It must not keep observing behind userback. No romantic pressure or toggle self-enable.

## 4. Accessibility/layout

Native controls with accessible names, visible focus and keyboard navigation; row labels read/control distinguish app vs site. Large font/longVietnamese labels wrap, lists virtualize if necessary, actionbar remains reachable at minimumsupported size/DPI. Selection must not accidentally toggle permission. Confirmation must name specific reset/delete effect.

Functional motion under250ms where applied, reducedmotion preference accommodated; avatar living animation timing is separate from UI microinteraction. Do not substitute CSS-only recipes for XAML; no WebView shell introduced.

## 5. UX review evidence

Screenstate matrix and native runtime keyboard/screenreader/resize/DPI tests before done. E02a keyboard/minimumresize still open, don't promote it as evidence of accessibilityproduction. Test with a new user who hasn't seen implementation terms: grants vs read, history vs memory, mood vs errors, hide vs stop.

<!-- CONFIRMED-2026-11-14 -->
## Quyết định hiện hành 2026-11-14 — ưu tiên hơn wording nháp cũ

Sinh từ registry; chỉ phần sau nhãn quyết định là bổ sung đã xác nhận. Chưa triển khai/chưa nghiệm thu; chi tiết kỹ thuật còn mở trong DECISIONS.

- **SP09:** D-02: Hình ảnh lỗi thì tạm dừng thao tác lên app khác; phục hồi vẫn tạm dừng và hỏi trước tiếp tục, kiểm quyền/an toàn mới. Không phát lại mù quáng; hợp đồng kết nối/mất kết nối còn mở.
- **NV01:** D-14: Nhân vật chính chủ yếu hình người về mặt/dáng/đi đứng, không mõm cáo/bàn chân động vật. Chỉ đôi tai cáo trên đầu, không tai người; tai trắng bạc lòng hồng nhạt; một đuôi cáo trắng bạc. Giữ nữ trưởng thành chibi anime pixel 128x128, tóc trắng bạc ngang eo/mái thưa, mắt đỏ hồng, da sáng ấm, áo len rộng cổ tròn hồng nhạt, váy xếp ly xám đậm trên gối, chân trần, kẹp tim đỏ rượu bên phải nhân vật.
- **NV02:** D-14: Giữ tóc/mắt/da đã chốt; tai trắng bạc lòng hồng nhạt và một đuôi trắng bạc đồng bộ tóc. Chỉ tai cáo, không tai người; không thay ngoại hình đã duyệt.
- **NV11:** D-05: Giữ Shift rồi kéo chuyển vị trí kể cả khi từ chối nhấc; không chơi/quăng hay ảnh hưởng quan hệ, không thêm tùy chọn phím; ngưỡng cử chỉ còn phải đo.
- **SH01:** D-12: Khi nhân vật ngủ dừng quan sát; thức dậy chỉ tiếp tục trong quyền hiện hành, không vượt SafetyHold/Thử đọc lại.
- **SH04:** D-14/H08: Trong sáu món đã chốt, trái cây là táo, nước trái cây là nước cam; không thêm món thứ bảy. Thú bông thỏ là đồ vật/quà riêng, không nhân vật chính. Màu/chi tiết thú bông, dụng cụ/hình mẫu còn chờ duyệt.
- **QD04:** D-12: Nhân vật ngủ dừng quan sát; thức dậy không tự cấp quyền hoặc bỏ qua SafetyHold/Thử đọc lại.
- **BH02:** D-17: Sửa/xóa bài học dừng việc đang dùng và hủy lượt chờ dùng bài học đó; người dùng giao lại, không chuyển lượt cũ sang phiên bản mới, không hủy việc không liên quan hoặc hoàn tác thao tác đã xong.
- **BH06:** D-02/D-10/D-17: Renderer lỗi thì tạm dừng thao tác app khác; hình ảnh phục hồi hoặc mở lại app giữ việc tạm dừng và hỏi trước tiếp tục, kiểm quyền/an toàn mới, không phát lại mù quáng. Sửa/xóa bài học dừng việc đang dùng và hủy lượt chờ dùng bài học đó, phải giao lại; không hủy việc không liên quan hoặc hoàn tác việc đã xong.
- **XP05:** D-16: Được kiểm trạng thái đang phát/không phát ở nền tối thiểu để tránh mở chồng; không đọc tên/nội dung hoặc suy gu. Lỗi/không xác định không coi là không phát; API/độ tin cậy cần kiểm chứng.
- **XP07:** D-06: Sau 3 nội dung không mở được về sinh hoạt; chờ người dùng thao tác trở lại rồi chỉ tìm trong đợt vắng mặt tiếp theo. Không tìm lặp cùng đợt hoặc chỉ dùng bộ đếm để mở lại tìm kiếm; quyền/chờ/không gián đoạn vẫn áp dụng.
- **XP08:** D-11: Máy ngủ không cộng thời gian chờ mở phim/nhạc; máy thức tiếp tục phần còn lại, không reset chỉ vì thức. Giữ quyền/khóa/input/phát đã chốt, máy ngủ khác nhân vật ngủ.
- **AI01:** D-16: Chỉ kiểm tra trạng thái đang phát/không phát ở nền để tránh mở chồng; không tên bài/phim/hình/âm thanh/lịch sử hoặc suy gu; lỗi/không rõ không coi là không phát. Cách lấy/độ tin cậy cần kiểm chứng.
- **AI02:** D-18: Gửi chữ lỗi/chưa rõ thành công thì báo lỗi và chờ bấm thử lại; xem/duyệt chữ trước mỗi lần gửi mới kể cả chữ không đổi. Không tự gửi lại, không coi timeout là chưa nhận, không mở rộng loại dữ liệu/quyền.
- **QH05:** D-05/H03: Buổi làm lành có thể cùng ngày nếu có khoảng nghỉ và tương tác thật; đóng/mở app hoặc quà liên tục không là buổi mới. Không tự đặt số phút/số buổi hoặc quà lập tức xóa tổn thương.
- **SL01:** D-09: Sao lưu không kèm gói AI nâng cao; máy mới tải lại khi cần, không thêm tùy chọn kèm gói mỗi lần xuất. Giữ dữ liệu nhân vật/ký ức/thiết lập thuộc phạm vi; quyền máy/khóa AI ngoài không mang sang. Whitelist/tài nguyên khác/tương thích còn phải đặc tả.
- **CD01:** D-10: Mở lại app giữ việc đang dở tạm dừng, hỏi trước tiếp tục; không tự chạy lại, vẫn kiểm quyền/an toàn hiện hành. Crash ghi dữ liệu/cập nhật còn cần khảo sát.
