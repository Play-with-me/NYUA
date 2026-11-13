# UX specification — native app và nhân vật

Draft screen design. Nghiệp vụ lấy SRS/BUSINESS_RULES, không thêm chat/score/focusmode. [Human wireframes](../HUMAN/03-TRAI-NGHIEM.md) là phần giải thích. DESIGN.md vẫn là token source: #f5f6f8/#202b38/#155e52, systemfont16, spacing4/8; áp sang XAML/Unity UI phù hợp.

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
