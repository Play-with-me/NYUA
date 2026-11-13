# Sổ quyết định, câu hỏi mở và rủi ro

Baseline0.1 — 2026-11-13. **Định hướng đã đồng ý không biến mọi chi tiết kỹ thuật thành accepted.** Không hỏi lại các quyết định đã rõ, chỉ hỏi điểm ảnh hưởng bước chuẩn bị thực thi.

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
| D-01 | Unityversion/plugins, overlay, focus/hitzone, fullscreen/DPI | AI khảo sát/PoC, user duyệt chất lượng | Trước desktopbodyproduction |
| D-02 | Renderer/worker/extension disconnect, reconnect queue và UX | AI đề xuất safe default, user chốt tác động trải nghiệm | Trước IPC/taskintegration |
| D-03 | Transport, framing, schema, limits, heartbeat, peer/session auth | AI khảo sát officialdocs + abuse/compatibilitytests | Trước messageimplementation |
| D-04 | Model/runtime, package size, minimumconfigs, accuracy/resource/passpercentile budgets | AI đo/candidate licenses; user chấp nhận qualitytradeoff | Trước advancedacceptance/release |
| D-05 | Phím modifier; gesturethresholds; invitationinterval; mood/neglect mapping; “buổi” và selfhide threshold | User experience decisions từ ví dụ, AI measuredgestureoptions | Trước tương tác/relationshipalgorithms |
| D-06 | Searchsession boundary sau3 failures và retrycooldown | User chốt trải nghiệm, AI chỉ ra looprisk | Trước autonomousmedia |
| D-07 | Crypto/passwordKDF/recovery design, key storage | AI officiallibraries/securityreview; no customcrypto | Trước backup/secretstorage |
| D-08 | Memory/ledger limits, sourceprovenance và deletevsfade policy details | AI storage design, user quyết retentiontradeoff | Trước persist/memorypruning |
| D-09 | Exportsettings whitelist, asset/model references vs payload, versioncompatibility | AI + user khi ảnh hưởng file size/offline/privacy | Trước archiveformat |
| D-10 | Crash/incompletejob/datawrite/update behavior không controlledexit | AI failuremodel, user quyết recoveryUX | Trước durablequeue/migration |
| D-11 | Sleep time có cộng idlemediawait không; lock/playback edge | User quyết; unlock input rule đã chốt không hỏi lại | Trước timerruntime |
| D-12 | Quan sát lúc cô ấy ngủ có tiếp tục không | User quyết; sleeping != hidden chưa tự đồng nhất | Trước sleep/perceptionintegration |
| D-13 | Signing/distribution/updatehost, model/assetslicenses và tên NYUA | AI research, user duyệt phí/công bố; có thể cần chuyên môn ngoài | Trước publicrelease |
| D-14 | Fruit/juice/plush/toolvisuals, tray partialrefusal, ảnh mẫu/clipset | User duyệt mẫu; AI không tự chọn chính thức | Trước assetlibrary/mealUX |
| D-15 | Trustboundary prefilter: nhận diện sensitive data trước OCR/model và nghĩa “không đọc” | Security/design review + realfixtures; user chốt nếu cần thay phạm vi | Trước actualscreenpipeline |
| D-16 | Minimal backgroundmedia playbackmetadata cho nomedia gate khi chỉ visiblecontent được đọc | AI đề xuất metadataonlyscope, user xác nhận nếu thêm quyền | Trước nomedia detection |
| D-17 | Edit/delete/reteach lesson trong lúc có jobqueued/running | AI versionpolicy, user chốt continue/cancel UX | Trước lessoneditingruntime |
| D-18 | ExternalAI retry after failure, consent payload/source và category limits | User chốt sendbehavior; AI tránh duplicatecharge/leak | Trước externalproviderintegration |

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
