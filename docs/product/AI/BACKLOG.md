# Backlog toàn sản phẩm — task chi tiết để rà

Không thay tasks/todo.md đang dở của mẫu E02a. Toàn bộ task dưới đây DRAFT_NOT_AUTHORIZED; file paths là dự kiến chưa tồn tại. Mỗi task có tối đa3 file boundary đề xuất; nếu khi Plan thực tế vượt5file hoặc một phiên tập trung thì phải tách tiếp trước Ready. Không cam kết thời lượng/ngày phát hành.

## Milestones và task graph

P00 ràbaseline/contracts/licenses; P01 khép mẫu; P02 Unity/Windowsprobe; P03 localAIbenchmark; P10 nguồn/quyền; P20 avatar; P30 life; P40 trải nghiệm/tác vụ; P50 dữ liệu/phân phối; P60 integration/release. Không tạo task parser/file-reader bị hoãn.

## P00-01 — Rà baseline và giải quyết mâu thuẫn phạm vi

- Status: DRAFT_NOT_AUTHORIZED; owner: `companion`.
- Đầu ra: Baseline/review log.
- Requirements: Enabler cho SP09 và các task phụ thuộc; không phải tính năng mới.
- Phụ thuộc: Không task trước; vẫn phải được rà phạm vi.
- Blocker: Baseline/thiết kế của lát cần rà; không mặc định Ready.
- [ ] Đối chiếu toàn bộ sourceIDs/mode rows với SRS và xác nhận phần hoãn.
- [ ] Ghi user decision hoặc blocker cho mỗi mâu thuẫn; không tự dùng default.
- Kiểm chứng: Review SRS/registry/RTM và validate_dossier.py.
- File boundary dự kiến: `docs/product/AI/DECISIONS.md`; `docs/product/AI/requirements.json`

## P00-02 — Rà ranh giới và hợp đồng hybrid

- Status: DRAFT_NOT_AUTHORIZED; owner: `companion`.
- Đầu ra: Module/contract baseline.
- Requirements: SP09
- Phụ thuộc: P00-01
- Blocker: D-02, D-03
- [ ] Thống nhất host authority, renderer/model chỉ ý định và dữ liệu đã lọc.
- [ ] DTO/error/generation ownership rõ; không vòng dependency hoặc transport tự chốt.
- Kiểm chứng: Review INTERFACES/ARCHITECTURE và negative message examples.
- File boundary dự kiến: `contracts/README.md`; `docs/product/AI/INTERFACES.md`

## P00-03 — Chốt tiêu chuẩn chất lượng sau đo

- Status: DRAFT_NOT_AUTHORIZED; owner: `companion`.
- Đầu ra: Quality budget proposal.
- Requirements: Enabler cho SP09 và các task phụ thuộc; không phải tính năng mới.
- Phụ thuộc: P00-01
- Blocker: D-04
- [ ] Phân biệt target user đã chốt với ngưỡng còn phải đo.
- [ ] Mỗi gate có phép đo/command thực tế khi triển khai, không coverage/perf giả.
- Kiểm chứng: Rà CONSTRAINTS và positive/negative control kế hoạch.
- File boundary dự kiến: `CONSTRAINTS.md`; `docs/product/AI/QA.md`

## P00-04 — Lập danh mục giấy phép và chi phí

- Status: DRAFT_NOT_AUTHORIZED; owner: `distribution`.
- Đầu ra: License/cost bill.
- Requirements: SP06
- Phụ thuộc: P00-01
- Blocker: D-13
- [ ] Ghi source/terms/redistribution của Unity/plugin/model/art/runtime.
- [ ] Tên NYUA và signing/distribution còn mở được ghi riêng, khoản phí phải hỏi.
- Kiểm chứng: Đối chiếu primary terms và lưu evidence/version.
- File boundary dự kiến: `docs/licenses/INVENTORY.md`; `docs/product/AI/DECISIONS.md`

## P01-01 — Khép kiểm tra UI còn mở của E02a

- Status: DRAFT_NOT_AUTHORIZED; owner: `policy`.
- Đầu ra: Lab acceptance evidence.
- Requirements: Enabler cho SP09 và các task phụ thuộc; không phải tính năng mới.
- Phụ thuộc: P00-01
- Blocker: Baseline/thiết kế của lát cần rà; không mặc định Ready.
- [ ] Kiểm minimumresize/keyboard/focus trên mẫu hiện có bằng bằng chứng thật.
- [ ] Người dùng dùng thử; C3 chỉ đóng khi các tiêu chí bắt buộc đạt.
- Kiểm chứng: Theo tasks/todo.md và lab RESULTS; không rerun test không đổi chỉ để yên tâm.
- File boundary dự kiến: `labs/policy-native/RESULTS.md`; `tasks/todo.md`

## P02-01 — Chọn và dựng renderer thử tối thiểu

- Status: DRAFT_NOT_AUTHORIZED; owner: `desktop-body`.
- Đầu ra: Pinned Unity probe.
- Requirements: Enabler cho SP09 và các task phụ thuộc; không phải tính năng mới.
- Phụ thuộc: P00-02, P00-04
- Blocker: D-01
- [ ] Version/platform/renderpipeline và license được ghi; nhân vật chỉ placeholder.
- [ ] Build Windows chạy được, không input/capture/network authority.
- Kiểm chứng: Unity editor/build smoke và inventory dependency.
- File boundary dự kiến: `unity/CompanionRenderer/ProjectSettings/ProjectVersion.txt`; `unity/CompanionRenderer/Packages/manifest.json`; `unity/CompanionRenderer/Assets/Probe.unity`

## P02-02 — Thử transparent overlay và hit regions

- Status: DRAFT_NOT_AUTHORIZED; owner: `desktop-body`.
- Đầu ra: Overlay/hit test report.
- Requirements: Enabler cho SP09 và các task phụ thuộc; không phải tính năng mới.
- Phụ thuộc: P02-01
- Blocker: D-01
- [ ] Avatar/prop nhận chuột đúng vùng; vùng rỗng không chặn app phía dưới.
- [ ] Focus/topmost/fullscreen modes đo và ghi unsupported, không bypass.
- Kiểm chứng: E-INT native runtime trên Windows với fixtureapp.
- File boundary dự kiến: `unity/CompanionRenderer/Runtime/OverlayProbe.cs`; `tests/Fixtures/WindowSurface.cs`; `docs/experiments/overlay.md`

## P02-03 — Thử tọa độ qua monitor và DPI

- Status: DRAFT_NOT_AUTHORIZED; owner: `desktop-body`.
- Đầu ra: Coordinate contract/tests.
- Requirements: Enabler cho SP09 và các task phụ thuộc; không phải tính năng mới.
- Phụ thuộc: P02-02
- Blocker: D-01
- [ ] Phân biệt physical/DIP/Unity units và bind layoutgeneration.
- [ ] Move/scale/monitorchange làm vô hiệu target cũ.
- Kiểm chứng: IT-05 với mixedDPI/negativecoords/testrects.
- File boundary dự kiến: `src/Host/Geometry/CoordinateMap.cs`; `tests/Integration/CoordinateMapTests.cs`; `docs/experiments/coordinates.md`

## P02-04 — Thử kết nối typed host-renderer

- Status: DRAFT_NOT_AUTHORIZED; owner: `companion`.
- Đầu ra: IPC probe.
- Requirements: Enabler cho SP09 và các task phụ thuộc; không phải tính năng mới.
- Phụ thuộc: P02-01, P00-02
- Blocker: D-03
- [ ] Handshake role/version/session và boundedmessage validate.
- [ ] Duplicate/unknown/reordered messages không phát input hoặc đổi grants.
- Kiểm chứng: IT-04 contract/abuse tests, peercompatibility.
- File boundary dự kiến: `src/Host/Transport/RendererChannel.cs`; `unity/CompanionRenderer/Runtime/HostChannel.cs`; `tests/Integration/RendererChannelTests.cs`

## P02-05 — Thử mất kết nối và khôi phục an toàn

- Status: DRAFT_NOT_AUTHORIZED; owner: `companion`.
- Đầu ra: Failure state report.
- Requirements: Enabler cho SP09 và các task phụ thuộc; không phải tính năng mới.
- Phụ thuộc: P02-04, P02-03
- Blocker: D-02, D-10
- [ ] Mất renderer/latecallback không cho lệnh click vượt generation.
- [ ] Reconnect queue UX theo quyết định người dùng, không silent replay.
- Kiểm chứng: Kill/restart fakepeer, delayedack and reconnect IT-04.
- File boundary dự kiến: `src/Host/Transport/ConnectionLifecycle.cs`; `tests/Integration/ConnectionLifecycleTests.cs`; `docs/experiments/disconnect.md`

## P03-01 — Sàng lọc model/runtime local có quyền phân phối

- Status: DRAFT_NOT_AUTHORIZED; owner: `perception`.
- Đầu ra: Candidate/license matrix.
- Requirements: AI01
- Phụ thuộc: P00-04
- Blocker: D-04
- [ ] So Vietnamese/image/OCR/offline và redistribution terms thực tế.
- [ ] Không chọn model theo quảng cáo hoặc assumption free=redistributable.
- Kiểm chứng: Primary modelcards/licenses/runtime docs.
- File boundary dự kiến: `docs/experiments/model-candidates.md`; `docs/licenses/INVENTORY.md`

## P03-02 — Dựng benchmark dữ liệu cảnh an toàn

- Status: DRAFT_NOT_AUTHORIZED; owner: `perception`.
- Đầu ra: Dataset manifest/runner.
- Requirements: AI03
- Phụ thuộc: P03-01, P01-01
- Blocker: D-04
- [ ] Clip có quyền sử dụng, labels/onset/clear-hard cố định trước đo.
- [ ] Input đã biết an toàn, không capture desktop cá nhân hoặc gửi cloud.
- Kiểm chứng: E04 owned-fixture dryrun, confusion/uncertain outputs.
- File boundary dự kiến: `tests/Fixtures/Scenes/manifest.json`; `tools/bench/SceneBench.cs`; `docs/experiments/local-ai.md`

## P03-03 — Đo phản ứng toàn luồng dưới tải kết hợp

- Status: DRAFT_NOT_AUTHORIZED; owner: `perception`.
- Đầu ra: Latency/quality report.
- Requirements: XP02
- Phụ thuộc: P03-02, P02-04
- Blocker: D-04
- [ ] Đo scenevisible→filter/OCR/infer/decision→renderstart với Unity đang chạy.
- [ ] Báo mọi mẫu sai/uncertain/unobserved, không đổi ngưỡng hoặc chọn lại clip.
- Kiểm chứng: IT-10 timing + RAM/VRAM/CPU/GPU observations.
- File boundary dự kiến: `tools/bench/CombinedBench.cs`; `contracts/SceneTiming.cs`; `docs/experiments/local-ai.md`

## P03-04 — Đề xuất hai mức và luồng gói nâng cao

- Status: DRAFT_NOT_AUTHORIZED; owner: `companion`.
- Đầu ra: Capability recommendation/pack states.
- Requirements: MC01, MC02, MC04
- Phụ thuộc: P03-03, P00-03
- Blocker: D-04
- [ ] Recommendation theo envelope đo, user override sau warning được.
- [ ] Download/validate/cancel states rõ, no silent downgrade hoặc gói giảready.
- Kiểm chứng: MC01–04 fixtures cho unsupported/corrupt/offline.
- File boundary dự kiến: `src/Host/Capabilities/ModeAdvisor.cs`; `src/Desktop.Wpf/ModesView.xaml`; `tests/Unit/ModeAdvisorTests.cs`

## P10-01 — Triển khai grants mặc định tắt và read/control

- Status: DRAFT_NOT_AUTHORIZED; owner: `policy`.
- Đầu ra: Production grant evaluator.
- Requirements: QD01
- Phụ thuộc: P00-02, P01-01
- Blocker: Baseline/thiết kế của lát cần rà; không mặc định Ready.
- [ ] App/site read-control riêng; browserANDsite; newsource defaultdeny.
- [ ] Revoke tăng generation và control không tự bật read.
- Kiểm chứng: AT-QD01/03, production unit/contract negative cases.
- File boundary dự kiến: `src/Host/Policy/GrantEvaluator.cs`; `src/Host/Policy/GrantState.cs`; `tests/Unit/GrantEvaluatorTests.cs`

## P10-02 — Nhận dạng nguồn và vùng đang hiển thị

- Status: DRAFT_NOT_AUTHORIZED; owner: `perception`.
- Đầu ra: Visible source adapter.
- Requirements: QD04, QD06
- Phụ thuộc: P10-01, P02-03
- Blocker: D-15, D-16
- [ ] Nguồn nền/thu nhỏ/bịche không được truyền nội dung; splitview đúng grants.
- [ ] Không mở mail gây mark-read; unsupportedsource chặn và giải thích.
- Kiểm chứng: IT-01/02 với owned app/browser fixture.
- File boundary dự kiến: `src/Host/Perception/VisibleSources.cs`; `src/BrowserBridge/SourceEvidence.cs`; `tests/Integration/VisibleSourceTests.cs`

## P10-03 — Lọc sensitive/private và retry hold trên nguồn thật

- Status: DRAFT_NOT_AUTHORIZED; owner: `policy`.
- Đầu ra: Safe snapshot boundary.
- Requirements: QD05, QD15
- Phụ thuộc: P10-02
- Blocker: D-15
- [ ] No forbidden sentinel in OCR/model/memory/log; unknownwholewindow hold.
- [ ] Explicit retry validates mới, revoke/change trongpipeline discard.
- Kiểm chứng: E02/IT-01/02 inspect actual consumers, not previewonly.
- File boundary dự kiến: `src/Host/Policy/SafetyHold.cs`; `src/Host/Perception/SafeSnapshotBuilder.cs`; `tests/Integration/SafeSnapshotTests.cs`

## P10-04 — Kiểm chứng clipboard history đúng Win+V scope

- Status: DRAFT_NOT_AUTHORIZED; owner: `perception`.
- Đầu ra: Clipboard adapter/proof.
- Requirements: QD08
- Phụ thuộc: P10-03
- Blocker: D-15
- [ ] Có evidence bảng open/close đúng trước đọc history; không tự bật setting.
- [ ] Đóng giữa chừng hủy buffer và no memory/log persistence.
- Kiểm chứng: K04 official API + owned clipboard fixtures IT-13.
- File boundary dự kiến: `src/Host/Perception/ClipboardScope.cs`; `tests/Integration/ClipboardScopeTests.cs`; `docs/experiments/clipboard.md`

## P10-05 — Luồng AI ngoài có preview và consent mỗi lần

- Status: DRAFT_NOT_AUTHORIZED; owner: `policy`.
- Đầu ra: Explicit text-only request.
- Requirements: AI02
- Phụ thuộc: P10-03, P50-01
- Blocker: D-07, D-18
- [ ] Exactsafe text+destination preview; payload/sourcechange invalidatesconsent.
- [ ] Reject/retry/offline no auto fallback or forbidden category send.
- Kiểm chứng: UC-13 mockprovider payload audit and errors.
- File boundary dự kiến: `src/Host/ExternalAI/ConsentRequest.cs`; `src/Desktop.Wpf/ExternalAIView.xaml`; `tests/Integration/ExternalAIConsentTests.cs`

## P10-06 — Bridge trình duyệt và ngoại lệ khung video

- Status: DRAFT_NOT_AUTHORIZED; owner: `perception`.
- Đầu ra: Optional extension/frame binding.
- Requirements: QD12, QD13, QD14
- Phụ thuộc: P10-03, P00-04
- Blocker: D-03, D-15
- [ ] Chrome/Edge web requires extension only whenenabled; no broad grants.
- [ ] Crossoriginplayer identified/confirmed scopedparent; mismatch asksagain.
- Kiểm chứng: QD12–14 browser integration + ads/redirect negatives.
- File boundary dự kiến: `src/BrowserBridge/Extension/manifest.json`; `src/BrowserBridge/FrameBinding.cs`; `tests/Integration/FrameBindingTests.cs`

## P10-07 — Input arbitration và các nút dừng

- Status: DRAFT_NOT_AUTHORIZED; owner: `policy`.
- Đầu ra: Stop/input gate.
- Requirements: DK01, DK02, DK03, DK04, XP08
- Phụ thuộc: P10-01, P02-05
- Blocker: D-05, D-11
- [ ] Humaninput vs injected classified withoutkeycontent, idle60s/unlockexception đúng.
- [ ] Emergency/off/hide matrix + generation prevents lateraction; sleepedge resolved.
- Kiểm chứng: IT-06, input injection fakeadapter first then reviewed realtests.
- File boundary dự kiến: `src/Host/Policy/InputGate.cs`; `src/Host/Policy/StopController.cs`; `tests/Integration/InputGateTests.cs`

## P20-01 — Duyệt model sheet nhân vật gốc

- Status: DRAFT_NOT_AUTHORIZED; owner: `desktop-body`.
- Đầu ra: Approved art reference.
- Requirements: NV01, NV02, NV03, NV04
- Phụ thuộc: P00-04
- Blocker: D-14
- [ ] Đúng adultchibi/appearance/anatomicalclip và source128.
- [ ] User duyệt sample; provenance/license recorded, no borrowedcharacter.
- Kiểm chứng: E01 review ở64/128/192/384.
- File boundary dự kiến: `art/character/model-sheet.png`; `art/character/manifest.json`; `docs/art/approval.md`

## P20-02 — Di chuyển và bề mặt cửa sổ

- Status: DRAFT_NOT_AUTHORIZED; owner: `desktop-body`.
- Đầu ra: Locomotion/surface model.
- Requirements: NV05, NV07, QD10
- Phụ thuộc: P20-01, P02-03, P02-05
- Blocker: D-01
- [ ] Followmovingwindow; closesupport→fall→land/stand đúng.
- [ ] Geometryonly inputs và forbiddenwindowtitles không lọt renderer.
- Kiểm chứng: AT-NV05/07/QD10 + fixture window lifecycle.
- File boundary dự kiến: `unity/CompanionRenderer/Runtime/SurfaceWorld.cs`; `unity/CompanionRenderer/Runtime/BodyMotion.cs`; `tests/Integration/SurfaceWorldTests.cs`

## P20-03 — Pet/lift/throw và chuyển vị trí an toàn

- Status: DRAFT_NOT_AUTHORIZED; owner: `desktop-body`.
- Đầu ra: Gesture recognizer.
- Requirements: NV09, NV11, SH05
- Phụ thuộc: P20-02, P30-02
- Blocker: D-05
- [ ] Phân biệt các gestures bằng ngưỡng đã đo/chốt, no accidentalthrow từ slowmove.
- [ ] Refusallift giữ; modifierreposition neutral, readinessgesture có.
- Kiểm chứng: AT-NV09/11/SH05/QH06 + UX gestureplaytest.
- File boundary dự kiến: `unity/CompanionRenderer/Runtime/Gestures.cs`; `contracts/AvatarInteraction.cs`; `tests/Integration/GestureTests.cs`

## P20-04 — Foodtray, đồ vật và animatedcleanup

- Status: DRAFT_NOT_AUTHORIZED; owner: `desktop-body`.
- Đầu ra: Food/prop interaction.
- Requirements: SH04, SH07, SH08, XP09
- Phụ thuộc: P20-02, P30-01
- Blocker: D-14
- [ ] Đủ6foods; tray/lẻ/refusal behavior; max5left with inuse exemption.
- [ ] Sixthleft waits animatedputaway; usermove/hide always available.
- Kiểm chứng: AT-SH04/07/08/XP09 + interactionstate fixtures.
- File boundary dự kiến: `unity/CompanionRenderer/Runtime/PropWorld.cs`; `src/Host/LifeState/FoodInteraction.cs`; `tests/Integration/PropWorldTests.cs`

## P20-05 — Placement nhiều màn hình và fullscreen

- Status: DRAFT_NOT_AUTHORIZED; owner: `desktop-body`.
- Đầu ra: Placement/support matrix.
- Requirements: NV08
- Phụ thuộc: P20-02, P02-02
- Blocker: D-01
- [ ] Onlychosenmonitors, fullscreenedge withoutmidcenter obstruction.
- [ ] MixedDPI and unsupportedexclusive modes documented; not universalgame promise.
- Kiểm chứng: IT-05 native hardware matrix.
- File boundary dự kiến: `src/Host/Geometry/MonitorSelection.cs`; `unity/CompanionRenderer/Runtime/Placement.cs`; `tests/Integration/PlacementTests.cs`

## P30-01 — Needs/sleep/rest và elapsed reconciliation

- Status: DRAFT_NOT_AUTHORIZED; owner: `life-state`.
- Đầu ra: Basic life clock.
- Requirements: SH01, SH02
- Phụ thuộc: P00-02, P50-01
- Blocker: D-05, D-12
- [ ] Needs/sleep phản ứng clock/fatigue, reservefood/no heavyabsencepenalty.
- [ ] Appclosed elapsed nofakeevents; inactiveprofilefreeze distinct.
- Kiểm chứng: SH01–03 unit logicalclock + restart fixtures.
- File boundary dự kiến: `src/Host/LifeState/NeedsClock.cs`; `src/Host/LifeState/ElapsedReconciler.cs`; `tests/Unit/NeedsClockTests.cs`

## P30-02 — Lựa chọn hoạt động, mood và attention limits

- Status: DRAFT_NOT_AUTHORIZED; owner: `life-state`.
- Đầu ra: Activity selection/state.
- Requirements: SP08, SH06, XP03, XP10
- Phụ thuộc: P30-01
- Blocker: D-05
- [ ] Causalchoices from needs/mood/preferences/memory, canchangeintent; noOSpranks.
- [ ] Invitation/tease share2attempts/>=30min, ignore→selfplay.
- Kiểm chứng: SP01/08 SH05/06 XP03/10 causal scenarios.
- File boundary dự kiến: `src/Host/LifeState/ActivitySelector.cs`; `src/Host/LifeState/AttentionClock.cs`; `tests/Unit/ActivitySelectorTests.cs`

## P30-03 — Quan hệ sâu, neglect và làm lành

- Status: DRAFT_NOT_AUTHORIZED; owner: `life-state`.
- Đầu ra: Relationship state machine.
- Requirements: QH01, QH03, QH04, QH05, QH06, QH07
- Phụ thuộc: P30-02, P30-04
- Blocker: D-05
- [ ] Eligibleactiveclock48–72h directionaltrust/hurt, no absence/basicpenalty.
- [ ] Firstthrow/repeat/refusal/selfhide/invite/gifts gradual multisessionrepair đúng.
- Kiểm chứng: IT-07/08/12 with logicalclock and narrativeapproval.
- File boundary dự kiến: `src/Host/LifeState/RelationshipEngine.cs`; `src/Host/LifeState/NeglectClock.cs`; `tests/Unit/RelationshipTests.cs`

## P30-04 — Memory provenance, pin/fade/edit/delete

- Status: DRAFT_NOT_AUTHORIZED; owner: `life-state`.
- Đầu ra: Memory lifecycle.
- Requirements: QD09, QD11, KN01, KN02
- Phụ thuộc: P50-01, P10-01
- Blocker: D-08
- [ ] Documenttopiconly, no clipboard/secretlasting; pin/fade/provenance guards.
- [ ] Editno relationrecalc; explicitdelete inverseonce vs naturalfade keepscloseness.
- Kiểm chứng: IT-13 with duplicatedelete/revoke/cache fixtures.
- File boundary dự kiến: `src/Host/LifeState/MemoryService.cs`; `src/Host/Storage/ContributionStore.cs`; `tests/Integration/MemoryTests.cs`

## P30-05 — Học gu từ user media evidence

- Status: DRAFT_NOT_AUTHORIZED; owner: `life-state`.
- Đầu ra: Media preference inference.
- Requirements: XP11, XP12, XP13, XP14
- Phụ thuộc: P30-04, P10-02
- Blocker: D-16
- [ ] Movie20min/musicrepeat + usertransitions, selfopen does not prove presence.
- [ ] No browserhistory/backgroundcontent/audioanalysis, preference notcertaintylike.
- Kiểm chứng: AT-XP11–14 controllednavigation/duration fixtures.
- File boundary dự kiến: `src/Host/LifeState/MediaPreferences.cs`; `contracts/MediaEvidence.cs`; `tests/Unit/MediaPreferenceTests.cs`

## P30-06 — Mode preservation, personality và romance opt-in

- Status: DRAFT_NOT_AUTHORIZED; owner: `life-state`.
- Đầu ra: Advanced state transitions.
- Requirements: SP07, MC03, QH02
- Phụ thuộc: P30-03, P03-04
- Blocker: D-05
- [ ] Downgrade preservesstate and suspendsdeeppenalty/expression, reenablecontinues.
- [ ] Romanceoff keep/delete respectschoice; personalitymatures withoutlosingcorenets.
- Kiểm chứng: IT-12 + user narrative review and deletecases.
- File boundary dự kiến: `src/Host/LifeState/ModeTransition.cs`; `src/Host/LifeState/RomanceTransition.cs`; `tests/Integration/AdvancedStateTests.cs`

## P40-01 — Onboarding/tray/settings shell

- Status: DRAFT_NOT_AUTHORIZED; owner: `companion`.
- Đầu ra: Native management UI.
- Requirements: NV06
- Phụ thuộc: P02-04, P50-01
- Blocker: D-14
- [ ] Firstprofile/name/startupchoice, tray opensfullsettings, no signupgate.
- [ ] Namesize/modes/monitors and stop routes accessible independentofmood.
- Kiểm chứng: UC-01/02 and IT-20 native UI states.
- File boundary dự kiến: `src/Desktop.Wpf/OnboardingView.xaml`; `src/Desktop.Wpf/SettingsShell.xaml`; `src/Desktop.Wpf/TrayController.cs`

## P40-02 — UI grants và chosenbrowser

- Status: DRAFT_NOT_AUTHORIZED; owner: `companion`.
- Đầu ra: App/site permission UI.
- Requirements: QD02, XP16
- Phụ thuộc: P40-01, P10-01
- Blocker: Baseline/thiết kế của lát cần rà; không mặc định Ready.
- [ ] Scannedapps+pastedwebsites separategrants with explanatorylabels, alloff.
- [ ] Chrome/Edge selectedbrowser doesnot grantpermissions; revoke routescorrectly.
- Kiểm chứng: AT-QD02/XP16 native UI+policyintegration.
- File boundary dự kiến: `src/Desktop.Wpf/PermissionsView.xaml`; `src/Desktop.Wpf/PermissionsViewModel.cs`; `tests/NativeUI/PermissionFlows.md`

## P40-03 — Dạy/review/manage lesson và searchparameters

- Status: DRAFT_NOT_AUTHORIZED; owner: `task-execution`.
- Đầu ra: Lesson definition workflow.
- Requirements: BH01, BH02, BH11, BH12
- Phụ thuộc: P10-03, P40-01, P50-01
- Blocker: D-17
- [ ] Explicitrecording sameapp/site, reviewconfirm then saveversion.
- [ ] Manage/reteach, searchparameters and firstresult/exactmeaning clear; illegaltyping denied.
- Kiểm chứng: UC-08 draft/cancel/crossscope/editcases.
- File boundary dự kiến: `src/Host/Tasks/LessonRecorder.cs`; `src/Desktop.Wpf/LessonReview.xaml`; `tests/Integration/LessonRecordingTests.cs`

## P40-04 — Embodied execution và postconditionverify

- Status: DRAFT_NOT_AUTHORIZED; owner: `task-execution`.
- Đầu ra: Verified step runner.
- Requirements: NV10, BH03, BH04, BH05
- Phụ thuộc: P40-03, P10-07, P20-02
- Blocker: D-03, D-05
- [ ] Approach→reobserve→finalpermit→singleaction→postcondition, targetchange stops.
- [ ] Human yield60s/resume/reteach, no forbiddenwrites/forms/payments; directrequestdelayonce.
- Kiểm chứng: E03/IT-03/14 with fakeinput then ownedsurfaces.
- File boundary dự kiến: `src/Host/Tasks/StepRunner.cs`; `src/Host/Tasks/ActionAdapter.cs`; `tests/Integration/StepRunnerTests.cs`

## P40-05 — Hàng đợi, priority và stop lifecycle

- Status: DRAFT_NOT_AUTHORIZED; owner: `task-execution`.
- Đầu ra: Queue state machine.
- Requirements: BH06, BH07, BH08, BH09, BH10
- Phụ thuộc: P40-04, P30-03
- Blocker: D-02, D-10, D-17
- [ ] Runningcancel/pendingpause/resumeexplicit/exitcancel matches matrix.
- [ ] Jobfailed stopsalone, nextindependent runs; directrequest preemptsdiscovery, no doublejob.
- Kiểm chứng: IT-06/14 with stale/duplicate/switch/selfhidecases.
- File boundary dự kiến: `src/Host/Tasks/QueueScheduler.cs`; `src/Desktop.Wpf/QueueView.xaml`; `tests/Integration/QueueTests.cs`

## P40-06 — Xem cùng và phản ứng cảm xúc

- Status: DRAFT_NOT_AUTHORIZED; owner: `companion`.
- Đầu ra: Attended media response.
- Requirements: XP01, XP04
- Phụ thuộc: P03-03, P10-03, P30-02, P20-04
- Blocker: D-04, D-12
- [ ] Safeobservations drive smoothaffect, silentreactions; hard/uncaptured nofakeunderstanding.
- [ ] Usermovie not interrupted, nextended target rechecked; no subtitleautoavoid requirement.
- Kiểm chứng: IT-09/10 with bothcontenttypes Vietsubs.
- File boundary dự kiến: `src/Host/Companion/MediaAttention.cs`; `src/Host/Companion/AffectSmoother.cs`; `tests/Integration/MediaReactionTests.cs`

## P40-07 — Tự tìm/mở nội dung trong quyền

- Status: DRAFT_NOT_AUTHORIZED; owner: `task-execution`.
- Đầu ra: Bounded autonomous media.
- Requirements: XP15, XP05, XP06, XP07
- Phụ thuộc: P40-05, P40-06, P10-06
- Blocker: D-06, D-11, D-16
- [ ] Advancedidle5m+unlocked+nomedia, owntab/chosenbrowser, preserveusertabs/playback.
- [ ] Skiplogin/pay/verify max3; uncertainadkeep; allowedframe scoped.
- Kiểm chứng: UC-11 IT-09 with redirects/autoplay/returninput.
- File boundary dự kiến: `src/Host/Tasks/AutonomousMedia.cs`; `src/BrowserBridge/MediaStatus.cs`; `tests/Integration/AutonomousMediaTests.cs`

## P50-01 — Chốt storage và transaction/persistence

- Status: DRAFT_NOT_AUTHORIZED; owner: `distribution`.
- Đầu ra: Versioned local storage.
- Requirements: SH03
- Phụ thuộc: P00-02, P00-04
- Blocker: D-07, D-08, D-10
- [ ] Logicalentity/provenance ownership và state commit transactional, no hiddenbackup.
- [ ] Corrupt/interruptedwrite handling preservesexisting or reportsfailure; no fake recovery.
- Kiểm chứng: DATA review + durabilityfixtures, licensecheck of engine.
- File boundary dự kiến: `src/Host/Storage/ProfileRepository.cs`; `src/Host/Storage/SchemaVersion.cs`; `tests/Integration/StorageTests.cs`

## P50-02 — Profile import/switch/reset semantics

- Status: DRAFT_NOT_AUTHORIZED; owner: `distribution`.
- Đầu ra: Profile lifecycle.
- Requirements: QD03, HS01, HS02, HS03
- Phụ thuộc: P50-01, P10-01
- Blocker: D-10
- [ ] Onlyimportadds, exactlyoneactive, inactiveallfreeze and sharedmachinegrants.
- [ ] Resetcurrent clearsstate/memory/relation/lessons, preserveothers; switch cancelsunfinished.
- Kiểm chứng: UC-16 IT-12/15 collision/loadfailure cases.
- File boundary dự kiến: `src/Host/Storage/ProfileLifecycle.cs`; `src/Desktop.Wpf/ProfilesView.xaml`; `tests/Integration/ProfileLifecycleTests.cs`

## P50-03 — Manualexport password/recovery format

- Status: DRAFT_NOT_AUTHORIZED; owner: `distribution`.
- Đầu ra: Reviewed encrypted archive export.
- Requirements: SL01, SL02
- Phụ thuộc: P50-01, P00-04
- Blocker: D-07, D-09
- [ ] Requiredpassword/recovery separate, auditedprimitive and boundedformat.
- [ ] Whitelist excludesgrants/keys/rawsources/queue; no autoarchives.
- Kiểm chứng: SL01/02 IT-15 ciphertext/credential/exportscope tests.
- File boundary dự kiến: `src/Host/Storage/ProfileExporter.cs`; `src/Desktop.Wpf/ExportView.xaml`; `tests/Integration/ExportTests.cs`

## P50-04 — Validate/import archive thành hồ sơ riêng

- Status: DRAFT_NOT_AUTHORIZED; owner: `distribution`.
- Đầu ra: Transactional import.
- Requirements: Enabler cho SP09 và các task phụ thuộc; không phải tính năng mới.
- Phụ thuộc: P50-03, P50-02
- Blocker: D-07, D-09
- [ ] Wrongpassword/code/corrupt/pathtraversal/unknownschema boundedreject.
- [ ] Successnewprofile no merge/foreigngrants, existingdata preserved onfailure.
- Kiểm chứng: IT-15 maliciousarchive/partialwrite/collision cases.
- File boundary dự kiến: `src/Host/Storage/ProfileImporter.cs`; `src/Desktop.Wpf/ImportView.xaml`; `tests/Integration/ImportTests.cs`

## P50-05 — Local actionhistory và expiry30days

- Status: DRAFT_NOT_AUTHORIZED; owner: `distribution`.
- Đầu ra: Sanitized history pipeline.
- Requirements: BH13
- Phụ thuộc: P50-01
- Blocker: Baseline/thiết kế của lát cần rà; không mặc định Ready.
- [ ] Time/source/action/outcome only, no raw/privatepayload/screenshots; no telemetry.
- [ ] Userdelete and30days expiry actual, history separatememory.
- Kiểm chứng: IT-17 errorpaths/clockedge/retentionfixtures.
- File boundary dự kiến: `src/Host/Storage/ActionHistory.cs`; `src/Desktop.Wpf/HistoryView.xaml`; `tests/Integration/HistoryTests.cs`

## P50-06 — Bộ cài và startup opt-in

- Status: DRAFT_NOT_AUTHORIZED; owner: `distribution`.
- Đầu ra: Native install package.
- Requirements: CD01
- Phụ thuộc: P00-04, P40-01, P20-05
- Blocker: D-13
- [ ] Actualcompatible host/renderer/runtime components pinned and installtested.
- [ ] Startup userchoice, basic works without optionalAIpack/extension/account.
- Kiểm chứng: IT-16 cleanWindowsinstall/startup flows.
- File boundary dự kiến: `packaging/README.md`; `packaging/installer-project`; `tests/NativeUI/InstallFlows.md`

## P50-07 — Own update check/download/install confirmation

- Status: DRAFT_NOT_AUTHORIZED; owner: `distribution`.
- Đầu ra: Authenticated update flow.
- Requirements: CD02
- Phụ thuộc: P50-06, P50-04
- Blocker: D-10, D-13
- [ ] Ownupdatesource/download verified, userconfirm before install/restart.
- [ ] Invalidsignature/migration stops, no otherappupdate or auto backup; rollback compatibility explicit.
- Kiểm chứng: IT-16 declining/corrupt/migrationfailure scenarios.
- File boundary dự kiến: `src/Host/Distribution/UpdateController.cs`; `src/Desktop.Wpf/UpdateView.xaml`; `tests/Integration/UpdateTests.cs`

## P50-08 — Uninstall giữ/xóa và manualexport reminder

- Status: DRAFT_NOT_AUTHORIZED; owner: `distribution`.
- Đầu ra: Uninstall data workflow.
- Requirements: CD03
- Phụ thuộc: P50-06, P50-03
- Blocker: D-13
- [ ] Explicitretain/deleteappdata, remindmanualexport, jobswarncancel.
- [ ] No search/delete manuallyexported archives outsideowneddata.
- Kiểm chứng: IT-16 retain/reinstall/delete scenarios withfakedata.
- File boundary dự kiến: `packaging/uninstall-workflow`; `tests/NativeUI/UninstallFlows.md`; `docs/help/uninstall.md`

## P60-01 — Lát tích hợp đầu: hiện→đọc an toàn→phản ứng→dừng

- Status: DRAFT_NOT_AUTHORIZED; owner: `companion`.
- Đầu ra: One complete product path.
- Requirements: SP01, SP02, SP04
- Phụ thuộc: P40-01, P20-02, P30-02, P10-03
- Blocker: D-01, D-15
- [ ] Không dùng cannedlabel thay realperception; life/render/grants cùng chạy.
- [ ] Stop/revoke actualconsumers, E02afakeproof không được promote.
- Kiểm chứng: SP02 walkthrough + end-to-end sentinelcapture.
- File boundary dự kiến: `tests/Integration/FirstSliceTests.cs`; `docs/acceptance/first-slice.md`

## P60-02 — Hồi quy hai mức và toàn bộ nghiệp vụ

- Status: DRAFT_NOT_AUTHORIZED; owner: `companion`.
- Đầu ra: Full RTM evidence.
- Requirements: MODE01, MODE02, MODE03, MODE04, MODE05, MODE06, MODE07, MODE08, MODE09
- Phụ thuộc: P60-01, P30-06, P40-07, P50-04, P50-05
- Blocker: D-04
- [ ] Allscope requirements mapped to test/results, deferredseparate; modefeatures correct.
- [ ] Negativepaths/keyboard/DPI/privacy/state tested, no skippedcriteria.
- Kiểm chứng: QA IT-01..20 and AT registry; native runtime.
- File boundary dự kiến: `tests/acceptance/manifest.json`; `docs/acceptance/rtm-evidence.csv`; `docs/acceptance/regression.md`

## P60-03 — Phiên8h/offline và ma trận cấu hình

- Status: DRAFT_NOT_AUTHORIZED; owner: `companion`.
- Đầu ra: Real8h soak report.
- Requirements: SP05
- Phụ thuộc: P60-02, P03-04
- Blocker: D-04
- [ ] Frozen8h schedule, measuredresource/faults on definedmachines.
- [ ] Offlineworks afterinstall, no unapprovedautodowngrade/cloud; actual8h notsimclock.
- Kiểm chứng: E05/IT-11/19 logs/profiles/rendering observations.
- File boundary dự kiến: `tools/bench/SoakObserver.cs`; `docs/acceptance/soak.md`; `docs/acceptance/hardware-matrix.csv`

## P60-04 — Rà độc lập, thương hiệu và release gate

- Status: DRAFT_NOT_AUTHORIZED; owner: `distribution`.
- Đầu ra: Release readiness packet.
- Requirements: SP03
- Phụ thuộc: P60-03, P50-07, P50-08, P00-04
- Blocker: D-13
- [ ] Bothmodesstable, security/data/license/name issues resolved or explicitapprovedscope.
- [ ] Actualreviewer/owner recorded; no pretendingAIselfreview independent.
- Kiểm chứng: RELEASE checklist, independentreview findings and closure.
- File boundary dự kiến: `docs/release/readiness.md`; `docs/licenses/INVENTORY.md`; `docs/release/limitations.md`

## P60-05 — Chuẩn bị công bố và hỗ trợ có kiểm soát

- Status: DRAFT_NOT_AUTHORIZED; owner: `distribution`.
- Đầu ra: User-facing release/runbook.
- Requirements: Enabler cho SP09 và các task phụ thuộc; không phải tính năng mới.
- Phụ thuộc: P60-04
- Blocker: D-13
- [ ] User approves actualpublicartifact/costs/communication, notjustplan.
- [ ] Vietnamesehelp/privacy/AIcosts/localhistory/support/redactedbugtemplate ready.
- Kiểm chứng: Install smoke onexactartifact and rollbackrunbookdryrun.
- File boundary dự kiến: `docs/help/start.md`; `docs/release/runbook.md`; `docs/release/changelog.md`

## Checkpoints

C-BASE: baseline/contracts/qualityreview trước productioncode. C-PROBE: E02a/E-INT/E04 có bằng chứng hoặc userchấp nhận giới hạn rõ trước reuse. C-SLICE: P60-01 chứng minh luồng kết hợp, không demoriêng. C-REGRESSION: SRS/AT/RTM actualevidence cả2mode. C-RELEASE: useracceptance/8h/privacy/data/license/cost/publicartifactreview; không auto publish.
