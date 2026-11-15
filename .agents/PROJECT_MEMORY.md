# PR2 review fixes — 2026-11-15

Được phép sửa/commit/push các lỗi review, không merge hoặc chạy sản phẩm. P1: bỏ output props xung đột SDK, dùng artifacts root theo task/dependency closure; P2: PowerShell env/call operator, cả ca âm có Player, exit/TRX. Validator LF/CRLF sẽ được sửa trong commit riêng, không đổi nghĩa yêu cầu. E02a T05 vẫn mở, UW01–30 NOT RUN.

# Bàn giao tài liệu Unity–Windows — 2026-11-15 (r4, nyua-8)

## Tóm tắt hoàn thành & Whitelist (`nyua-8`, docs-only trên `nyua-4`, HEAD `5e6e651`)
- **Phạm vi:** Chỉ cập nhật tài liệu & registry/generated trong `C:/Users/phamp/.ao/data/worktrees/nyua/nyua-4`; giữ nguyên mọi sửa đổi E02a/r1–r3 trước đó; không cài đặt, không tạo fixture/code, không chạy runtime/Unity, không sửa `labs/`, không commit/push/PR.
- **3 quyết định người dùng đã chốt (`r4`):**
  1. **Gói Unity & dự án cá nhân (`P00-04` / `D-13`):** Dự án cá nhân, không kinh phí → dùng gói miễn phí **Unity Personal** (chủ dự án vẫn xác minh điều kiện tài chính/non-Industry & lập inventory `P00-04` trước cài đặt).
  2. **Ngân sách công cụ giai đoạn thử (`SP06` / `D-13`):** Giai đoạn thử chỉ dùng **100% công cụ miễn phí (`$0`)** (không seat/dịch vụ/code-signing trả phí ở bản thử đầu).
  3. **Phạm vi `NV08` & phần cứng thiếu (`D-01` / `NV08`):** **Giữ nguyên yêu cầu `NV08`** (không hạ chuẩn); các ca kiểm chứng **nhiều màn hình (`UW11`, `UW12`)** và **toàn màn hình độc quyền (exclusive fullscreen)** đánh dấu **`NOT RUN` — chờ thiết bị thật** cho bản thử đầu.
- **Lựa chọn kỹ thuật đã chốt (mức đề xuất `UW-DOC-2026-11-15-r4`, `NOT_VERIFIED`):**
  1. **Unity candidate:** Unity `6.3 LTS` (`6000.3.28f1`, phát hành `2026-11-03`, trên sàn `CVE-2025-59489` `6000.3.0b4` phát hiện `2025-06-04`/advisory `2025-10-02` và đợt Oct 2026 Brotli `CVE-2026-111497` / eMudhra `CVE-2026-111943` `6000.3.27f2` kèm điều kiện cập nhật Windows OS root trust store; ghi nhận lỗi `UUM-142550`, `UUM-156125`, `UUM-158166`).
  2. **Compile/inclusion & ownership:** Đưa toàn bộ runtime scripts (`P02-02`, `P02-04`, `P20-02..05`) vào `unity/CompanionRenderer/Assets/Runtime/*.cs`; `P02-01` sở hữu `CompanionRenderer.Runtime.asmdef` + `Assets/Editor/ProbeBuild.cs` (cấu hình/assert `ApiCompatibilityLevel.NET_Standard_2_1`, `GraphicsDeviceType.Direct3D11`, URP từ `Packages/manifest.json` lúc build); `P02-02..05` dùng `.csproj`/`.Tests.csproj` tách biệt (`<EnableDefaultCompileItems>false</EnableDefaultCompileItems>`, cô lập chỉ bằng `--artifacts-path` dưới TEMP, đồng nhất theo dependency closure giữa `dotnet restore` và `dotnet build/test --no-restore`), tái build Player theo đúng output từng chặng (`p02-01`, `p02-02`, `p02-04`), phụ thuộc `B00-01`; các ca UI WPF (`UW07` dialog, `UW21-UI`/`UW22-UI`, `UW28`) giữ `NOT RUN — BLOCKED` chờ `src/Desktop.Wpf/` owner.
  3. **Render / Profile / IPC / Lifecycle:** `D3D11` + `URP 2D/Core`; Host `.NET 10 LTS` (`System.Text.Json` `MaxDepth=16`) vs Unity `.NET Standard 2.1` (strict UTF-8 JSON parser tự viết trong `HostChannel.cs`, không external DLL, kiểm roundtrip & negative vectors surrogate/duplicate/overflow/trailing token); separate-process Named Pipe `PipeOptions.CurrentUserOnly`, 32-bit LE length-prefix `<=64KiB`, `queue<=32`, `handshake<=10s`, `read<=2s`, `heartbeat 1s/3-miss`, `epoch` đơn điệu, giữ nguyên UX `PausedAfterFault` (`[Kết nối lại]` → `[Cho tiếp tục sau lỗi]` / `[Giữ tạm dừng]`, hoãn nút hủy hàng đợi tùy chọn).
  4. **Verification / Gates:** Toàn bộ `UW01–UW30` là `NOT RUN` (nhiều màn hình `UW11`/`UW12` & exclusive fullscreen đánh dấu `NOT RUN` chờ thiết bị thật cho bản thử đầu), timeout giám sát `120s`, giữ nguyên E02a `C3` (user acceptance) vs `T05` technical checklist open (`P01-01` chưa Done), các cổng `P20-01`/`P60-04`/`P60-05` `NOT_OBTAINED`, thực thi tương lai `NOT_AUTHORIZED`.
- **Exact file whitelist đã sửa (`r4`):** `.agents/PROJECT_MEMORY.md`, `docs/unity-windows/{SOURCES,SPEC,TEST_PLAN}.md`, `docs/product/AI/{backlog.json,BACKLOG.md,DECISIONS.md,INTERFACES.md,TASK_TRACEABILITY.csv}`, `docs/product/HUMAN/07-CONG-VIEC.md`, `tasks/phase-*.md`, `graphify-out/*`.
- **Kiểm tra & Snapshot (`r4`):** Chạy `sync_backlog.py`, `validate_tasks.py --negative-controls`, `validate_dossier.py`, `check_dossier_controls.py`, `context_nav.py build/test/measure/check` (Python 3.12), xuất snapshot + full diff tại `TEMP/nyua-unity-review-snapshot.json` & `TEMP/nyua-unity-review-full.diff`.

## Bàn giao trước đó (nyua-4 / r1)
Đã viết docs/unity-windows/SPEC.md, TEST_PLAN.md, SOURCES.md: 30 ca tương lai đều NOT RUN; dependency/whitelist lấy canonical, thiếu build runner/script inclusion được chặn trước Ready. E02a C3 chỉ đóng trải nghiệm theo user; T05 kỹ thuật còn mở, không coi P01-01 Done. Kiểm tra thực chạy: task219/requirement109/NFR10 +10 negative controls; dossier +4 controls; context219packs/7modules +5 controls và FRESH. Không chạy sản phẩm/Unity, không cài hoặc tạo fixture, không commit/push. Rà nyua-5 đã đóng vấn đề P01; phát hiện inclusion được sửa rõ trong cả SPEC/TEST_PLAN, đang chờ closeout độc lập. Quyền build/install/run tương lai NOT_OBTAINED. Các số53/53 và35/35 là lịch sử, không chạy lại ở lượt này.

Scope đã được người dùng/điều phối cho phép: đồng bộ nghiệm thu trải nghiệm E02a đã đóng; chuẩn bị SPEC/TEST_PLAN/SOURCES tiếng Việt theo dependencies canonical, rồi independent read-only review. T05 kiểm kỹ thuật mở rộng còn mở. Không prototype/Unity fixture/run/install/product changes/commit/push/PR/deploy. Giữ nguyên local edits trước lượt này. Whitelist mới docs/unity-windows/{SPEC,TEST_PLAN,SOURCES}.md; maintenance chỉ memory/E02a records, tài liệu liên quan trạng thái hiện hành, canonical backlog/generator/validator/context khi thật sự cần đồng bộ. HEAD5e6e651 là ancestor của origin/main3329284; không checkout/reset/discard edits. Workflow: summary->fresh scoped task packs->official sources->docs->doc validators/context refresh->nyua-5 review->fix/re-review.

# E02a user acceptance — current 2026-11-15

User explicitly confirmed resize OK, Tab/Shift+Tab focus visible/no trap and said “Có nhìn rõ và không có chỗ nào bị kẹt, có thể đóng nghiệm thu E02a rồi”. E02a fake-demo EXPERIENCE acceptance C3 CLOSED by user, not AI. Record tasks/E02a-USER-ACCEPTANCE.md; todo updated. Full keyboard activation/screen-reader/all DPI and independently measured minimum dimensions remain unverified; T05 compound technical checklist remains open, no fabricated PASS. No product implementation/deploy/publishing authorized. Previous C3-open references below are historical.

# Hiện tại — Graphify / AI đọc ngắn

Bắt đầu `graphify-out/GRAPH_REPORT.md` → Python312 `docs/context/context_nav.py check` → `module <key>` hoặc `task <ID> --out <TEMP-file>` → đọc pack và source anchors. Không nạp toàn graph.json/SRS/backlog trước mỗi task. STALE/OVERFLOW phải dừng, không cắt safety/acceptance. Hướng dẫn: docs/context/README.md.

Phạm vi tích hợp hiện tại: chỉ local docs/tooling, không product changes/runtime tests/push/PR update. Điều này áp dụng cho đợt Graphify, KHÔNG phủ nhận demo E02a đã được người dùng cho build trước đó:53/53 tests và35/35 UI cases trên máy này; bản demo đã bàn giao. E02a experience acceptance C3 đã được user chấp nhận2026-11-15; T05/full activation/screenreader/số đo minimumresize vẫn chưa đủ evidence. PR1 đã merge vào main3329284 ngày2026-11-14; lượt docsUnity hiện tại chưa commit/push.

Graphify final targeted independent docs/measurement audit nyua-5 PASS: SRS/baseline hashes, raw measurement certificate, source/map fingerprint, algorithm revision and scoped entry workflow verified; no remaining material blocker. Owner controls covered219packs,5 context rejection controls plus real SRS/measurement edits in isolated TEMP. Đây là kết quả review đợt Graphify trước; PR1 đã merge sau đó. Đợt chuẩn bị Unity docs mới không được push.

Mốc dưới đây là lịch sử phục hồi tài liệu và các đợt trước, không thay trạng thái hiện tại ở đầu file.

---

# Documentation recovery — 2026-11-14 (current)

Local-only nyua-4: source drafts from nyua-2 and nyua-3 preserved at originals; exact orchestrator appended decisions saved in docs/product/AI/DECISION_SOURCE_2026-11-14.md and reconciled into canonical requirements, generated registry/HUMAN/SRS, module/UX/ART/DECISIONS. Task source now AI/backlog.json; 219 proposed tasks, 109 source requirements, 10 NFRs, 7 modules. tasks/README.md has prompts/dispatch, TASK_TRACEABILITY.csv links owners/AT/verification/final gates. All tasks DRAFT_NOT_AUTHORIZED and blocked on scope/evidence, not production approval.

Exact role mapping research/memory/QA agy gemini-3.8-flash; UI/features agy gemini-4-hydrogen-low; core/bug/finalreview codex gpt-6.1-sol effort low. Shift reposition, same-day genuine reconciliation sessions, sleep stops observation, explicit resume on restart/renderer recovery, lesson-edit dependent cancellation, next-absence retry after 3 failures, sleep-excluding wait, per-send AI consent, minimal playback metadata, AI-pack excluded from export, fox main avatar silver ears/pink inside/no human ears/one silver tail/all older appearance preserved, bunny plush/apple/orange juice synchronized with restrictions.

Documentation validation and negative controls actually run; no product tests, runtime, human acceptance, SDK/models or publish. E02a todo/plan unchanged and acceptance open. Python312 with Pillow needed for image checks; default MSYS Python lacks Pillow, jsonschema unavailable. See docs/product/QUALITY_REPORT.md for real evidence/limits. Four initial independent review findings repaired. Follow-up corrected document-only runtime-gate deadlock and Unity fixture ownership: document_review has no executable entry prerequisite; B00-02 owns five explicit isolated Unity fixture paths, independent of P02-01. Nine task negative controls and four dossier controls now required; final internal document re-review PASS by nyua-5 (2026-11-14 18:54:30 Asia/Saigon), with no remaining blocker from six findings; not product/user/publishing approval. Final artifact/commit details in session handoff, not a deployment-ready claim.

---

# Bộ nhớ dự án

## Trạng thái ưu tiên — sau yêu cầu “Proceed” ngày 2026-11-13

- Mới nhất: người dùng yêu cầu toàn bộ tài liệu tiền triển khai (đặc tả/SRS/task/sơ đồ/giải thích), rồi yêu cầu riêng bản người đọc và AI. Đã tạo docs/product/README.md làm entry, HUMAN và AI dùng chung registry; đây là baseline0.1 để rà, không tự phê duyệt toàn backlog.
- Nội dung:109 mục (100 sourceIDs gồm SP09 ghi hướnghybrid đã thống nhất +9moderows), SRS/PRD/danh mục dễ đọc,7specmodule,18UC, nghiệp vụ/UX/art/architecture/interface/data/security/localAI/QA/release/team,52taskproposal códeps/criteria/files/blockers,RTM.csv,18điểm mở D-01..18,ADR001/002/005 với status thật.
- Hình vẽ:15Mermaid sources+Atlas,4cặp PNG/SVG đã nhìn trực tiếp, sourcegenerator local. Task DAG đầy đủ sinh từ backlog. Không có Graphify production hoặc Mermaid engine renderproof; không giả graph đã extracted.
- Đồng bộ: AI/sync_requirements.py, sync_backlog.py, diagrams/build_diagrams.py; validate_dossier.py kiểmsourcehash/text/coverage/reference/taskDAG/status/links/images. Đạt cleancontrol,3negativecontrols(hash/cycle/link) bị từchối. JSONSchema chưa validatebằngtoolđộclập. QUALITY_REPORT ghi giới hạn.
- Canonical docs/YEU_CAU_HIEN_HANH.md đã cập nhật thực trạng E02a và SP09; các phần chưa chốt luôn proposed/TBD cóowner+gate. tasks/todo.md E02a không đổi, appcode không sửa, không cài/thử Unity/model hoặc phần production mới.
- Bước tiếp: người dùng đọc HUMAN theo thứ tự, rà nhóm quyết định ảnh hưởng lát kế; không phỏng vấn lại toàn bộ hoặc tự bắt đầu52task. Tiếp tục khép UI/useracceptance E02a khi quay lại thực thi, rồi lập spec/plan scoped của hybridprobe theo bằng chứng.

- Gói bàn giao tài liệu: C:\Pet\.tools\deliverables\Ho-so-san-pham-0.1.zip,87file tài liệu/hình/nguồn kèm manifestSHA256 và CRC kiểm tốt. Không .exe/.dll/model/SDK/key/Gitmetadata; notes giải thích liên kết workspace không có trong gói. Bộ docs/product có39Markdown,15mmd,4PNG+4SVG và dữ liệu/script đồng bộ. Bản HUMAN có human_acceptance_notes và human_task_notes riêng bằng lời thường, cùng registry/backlog với bản AI.

- Mới nhất: người dùng đã duyệt kế hoạch và yêu cầu bắt đầu xây. Mẫu native E02a đã triển khai tại labs/policy-native: Core C#, Scenarios, WPF App, MSTest. Không Unity/AI/capture thật. Bản self-contained win-x64 mở tại labs/policy-native/artifacts/app/PolicyLab.App.exe, đã để mở cho người dùng thử.
- SDK 10.0.404/runtime10.0.15 cài riêng C:\Pet\.tools\dotnet bằng script Microsoft, không đổi PATH/registry; dotnet.exe chữ ký Valid. Git cục bộ đã khởi tạo và có các mốc tài liệu/core/coordinator/catalog/WPF; không push/remote. .tools/bin/obj/TestResults/artifacts được ignore.
- Kết quả thật: 53/53 MSTest Release đạt (35 trường hợp A/B + các kiểm tra core/coordinator/inventory); build0 warnings/errors, publish self-contained thành công. Audit NuGet Tests không thấy vulnerable packages theo nguồn hiện có; snapshot runtime TCP0/UDP0. Rà cùng AI, không độc lập.
- Runtime đã quan sát A01 chặn, A05 chỉ SAFE-A, tắt quan sát xóa đầu vào cũ nhưng giữ geometry, A09 thử lại/sửa vùng/thử lại, A10-revoke hủy đúng. Bộ chạy UI35/35 trước sửa cuối chỉ về label tổng kết; bản cuối mở được, chưa chạy lại UI35 vì phát hiện người dùng thao tác, đã nhường. Không tự thao tác tiếp trên cửa sổ khi người dùng đang dùng.
- Chưa đủ bằng chứng resize tối thiểu/full keyboard hoặc user acceptance. tasks/todo.md còn các ô này và C3 mở; không báo E02a nghiệm thu toàn bộ. README/RESULTS ghi hướng dẫn, kết quả từng case từ TRX, hạn chế. JSON gốc Downloads và docs cùng hash. Chưa cài Unity/model, không đọc dữ liệu thật.
- Bước sau: người dùng thử mẫu và phản hồi; kiểm tra tiếp các mục UI còn mở trước đóng C3. Sau đó đặc tả phép thử Unity–C# riêng và đường nguồn thật riêng, không tự mở rộng app.

- Sau “Tiếp tục theo quy trình chuẩn”: đã tạo tasks/plan.md và tasks/todo.md cho E02a native C# + WPF, .NET 10 LTS/MSTest đề xuất, 7 task T00–T06 và checkpoint C1–C3. Kế hoạch chờ rà trước triển khai, toàn bộ task chưa chạy. Không cài SDK/Unity/model, không tạo project hoặc Git trong lượt này.
- E02a giữ dữ liệu giả, không Unity/AI/quan sát máy thật. Tích hợp Unity–Windows phải đặc tả/phép thử riêng; hướng sản phẩm hybrid đã được người dùng tiếp tục thảo luận/chấp nhận, chưa chứng minh transparency/click-through/IPC/hiệu năng.
- Nguồn đã đọc: Microsoft WPF overview, .NET support policy (.NET10 LTS còn hỗ trợ), MSTest tutorial. dotnet không PATH/hai vị trí chuẩn, Git có nhưng .git chưa tồn tại. Phiên bản SDK/package phải xác minh lúc cài; không dùng số ví dụ từ docs.

- Mới nhất MC04/AI03: người dùng muốn AI local nhẹ xử lý cảm xúc nhanh, kiểm tra cấu hình để đề xuất hai mức phù hợp. Chưa chọn model/runtime hoặc benchmark; không tự hứa dưới 1 giây. Giữ MC02: người dùng tự chọn/bật thử, không tự đổi mức.
- Người dùng đã duyệt SPEC-policy.md và cho lập kế hoạch xây mẫu. Chưa tạo tasks/plan.md/todo.md vì đang so sánh nền tảng. Đề xuất web/Node chưa được duyệt, người dùng yêu cầu native. Người dùng đề xuất Unity hiển thị nhân vật, C# + WPF phần app; hướng này cần phép thử tích hợp, chưa coi transparency/click-through/IPC/hiệu năng đã đạt, chưa cài .NET/Unity.

- Mới nhất: người dùng chấp nhận bản đồ bảy phần và yêu cầu tiếp tục đặc tả phép thử. CAPABILITY_MAP.md đã ghi duyệt ranh giới; không phải duyệt stack/phát hành.
- Đã tạo SPEC-policy.md cho E02a: hai lớp người dùng/kỹ thuật, hợp đồng metadata/đầu vào đã lọc/bộ nhận, revision chống dữ liệu cũ, SafetyHold và thử lại, trạng thái UI, truy vết A01–A16 kèm biến thể và B01–B06. Chỉ dữ liệu giả, không đọc màn hình/clipboard/điều khiển thật; chưa code/test/kết quả.
- Điểm dừng hiện tại theo spec-driven-development: đặc tả chờ người dùng duyệt trước bước Plan. Chưa tạo tasks/plan.md hoặc tasks/todo.md; chưa chọn stack/runner/lệnh chạy. README đã liên kết đặc tả. Các dòng cũ nói bản đồ chờ duyệt đã được thay bởi quyết định mới này.

- Người dùng yêu cầu áp dụng skill để tổ chức như team sản phẩm chuyên nghiệp. Đã tạo docs/QUY_TRINH_TEAM_SAN_PHAM.md (vai trò, bước/đầu ra/gate, tiêu chí bắt đầu/hoàn thành, thay đổi/lỗi/phát hành, truy vết và cách làm mỗi buổi), CAPABILITY_MAP.md (7 mã giữ từ đề cương, đề xuất chờ rà), CONSTRAINTS.md (chỉ quy tắc viết, chưa kiểm tra tự động). README đã nối.
- Ranh giới hiện tại: cần rà bản đồ khả năng trước đặc tả từng phần theo spec-driven-development Phase 0; chưa viết đặc tả module/backlog triển khai, chưa chạy E02a hay chọn stack/cài công cụ. Không đồng nhất vai trò AI với nhiều người rà độc lập. Không tự thêm telemetry hoặc backup tự động.
- Quy trình đề xuất giữ E02a là phép thử cổng quyền đầu, E01/E04 cần bằng chứng riêng. Chỉ chia việc thực thi chi tiết khi đặc tả phạm vi tương ứng đã được rà. Mọi lượt code đọc CONSTRAINTS.md; chưa thiết lập Git/test runner/CI.

- Người dùng đã đồng ý rà yêu cầu rồi chuẩn bị phép thử nhỏ và nhắn Proceed. Đã rà tài liệu, đồng bộ XP13 với XP14 và sửa mô tả điểm chưa chắc; không phỏng vấn lại các lựa chọn mới BH09–BH13/XP10–XP16.
- Bước chuẩn bị hoàn tất: docs/PHEP_THU_DAU_TIEN.md chọn E02a, 16 tình huống nguồn giả/cổng quyền/bộ nhận đầu vào. Không có code thử hoặc kết quả chạy; không chứng minh capture thật/lọc bí mật tổng quát. E01/E04 vẫn phải thực hiện riêng. README và đề cương E02 đã liên kết tài liệu này.
- Tiếp theo: dựng mẫu thử E02a theo tài liệu và quy trình UI trước khi nối nguồn thật; chưa triển khai app đầy đủ, chưa cài tiện ích/model hoặc dùng dịch vụ tốn phí. Không nhầm việc chuẩn bị đã xong với phép thử đã đạt.

- BH13 thời hạn đã chốt: lịch sử thao tác giữ 30 ngày rồi tự xóa, vẫn cho xóa sớm.

- BH13: lịch sử thao tác cục bộ trong cài đặt, xem/xóa được; thời điểm, app/website, thao tác, kết quả; không ảnh màn hình/nội dung riêng tư, tách ký ức. Chưa chốt thời hạn giữ.

- BH12: lưu bài học cho chọn rõ bấm kết quả đầu tiên hay đúng nội dung đã chỉ; không tự đoán từ cú bấm mẫu. Vẫn kiểm tra quyền/an toàn.

- BH11: cho đổi nội dung tìm kiếm trước mỗi lần chạy bài học, giữ nguyên các bước đã dạy; không mở rộng quyền gõ sang tài liệu/chat/biểu mẫu.

- XP16: người dùng chọn Chrome hoặc Edge trong cài đặt để tự mở phim/nhạc; không tự chọn theo trình duyệt mặc định hoặc tự cấp quyền.

- XP15: tự mở phim/nhạc dùng tab riêng, giữ nguyên các tab người dùng; không thay nội dung tab của người dùng.

- XP14: dựa thao tác người dùng chuyển tập/kênh/video/nhạc để nhận biết xem/nghe và học gu; không thêm nút xác nhận. Tự phát tiếp hoặc nhân vật thao tác không phải bằng chứng người dùng hiện diện. XP12/13 đọc cùng XP14.

- XP13: học gu phim từ ít nhất 20 phút xem; nhạc nghe lặp lại hoặc nhiều bài cùng kiểu. Chỉ là tín hiệu sở thích. Chưa chốt hiện diện khi xem/nghe thụ động; không tự dùng mốc 60 giây của quan hệ.

- XP12: nội dung nhân vật tự mở vẫn có thể học gu nếu người dùng quay lại và tiếp tục xem/nghe đủ lâu. Chưa chốt dấu hiệu hiện diện khi không thao tác/ngưỡng thời gian; không dùng thời gian phát lúc vắng mặt để kết luận thích.

- XP11 cập nhật: học gu từ nội dung người dùng chủ động mở và xem/nghe lâu, chỉ trong phạm vi quan sát đã cấp; không tự đọc lịch sử trình duyệt hoặc phân tích âm thanh. Mở thử không đủ để coi là thích.

- XP11: tự chọn phim/nhạc chủ yếu học và theo gu người dùng. Chưa chốt tín hiệu học gu; không đồng nghĩa cho phép đọc lịch sử trình duyệt hoặc nội dung nền.

- BH10: việc người dùng giao ưu tiên hơn tự tìm phim/khám phá ứng dụng; dừng khám phá để nhận việc, vẫn được trì hoãn một lần theo tâm trạng.

- BH09: tự ẩn vì buồn/tổn thương hủy việc đang làm, giữ các việc chưa chạy tạm dừng. Trở lại vẫn phải bấm Tiếp tục hàng đợi, không tự chạy hoặc phục hồi việc đã hủy.

- XP10: không nhìn được phim thì tự chọn ở lại xem hoặc chuyển sang chơi/ăn/sinh hoạt khác tùy tâm trạng, không bắt buộc xem tiếp. Không suy diễn đã hiểu hình ảnh không quan sát được.

- QD15/H16: không xác định chắc vùng an toàn thì ngừng đọc cửa sổ và báo lý do, người dùng xử lý sau; vẫn sinh hoạt. Điều khiển cửa sổ cũng bị chặn vì cần đọc an toàn trước. Chưa chốt cách cho đọc lại.
- QD15/H16 mới hơn: chỉ bấm Thử đọc lại mới kiểm tra an toàn để tiếp tục; không bỏ bộ lọc hoặc tự đọc lại khi đổi cửa sổ. Hành vi đã chốt, còn E02 kiểm chứng.

- Cập nhật ưu tiên mới nhất: NYUA được chọn làm ứng viên tên, chưa chốt nhãn hiệu. Đã tra WIPO qua UI: Embedded NYUA không kết quả; Fuzzy + VN + nhóm 9 có 32 gợi ý chưa rà hết; mở NYNA thấy hàng bảo hộ và trạng thái Từ chối. IPPlatform hiện vào được form nhưng gửi NYUA trả lỗi máy chủ. Không tuyên bố tên an toàn; xem docs/TEN_UNG_VIEN.md.
- Đã đọc cấu hình không benchmark: Windows 11 Pro build 26300, Ryzen 9 8945HX, RAM 15.8 GiB, RTX 5070 Laptop 8151 MiB, driver 592.01. Xem docs/KHAO_SAT_MOI_TRUONG.md; không phải cấu hình tối thiểu hoặc bằng chứng đạt AI.

- H04 đã được trả lời: Tắt quan sát vẫn cho biết vị trí/kích thước cửa sổ để sinh hoạt trên cạnh; không đọc nội dung hoặc điều khiển app. Đã cập nhật DK04 và bảng điểm chưa chắc.
- H01: giữ một phím + kéo để chuyển vị trí dù nhân vật từ chối nhấc; không phải chơi/quăng, không ảnh hưởng xấu quan hệ. Chưa chọn phím cụ thể; đã ghi NV11.
- H05: thao tác mở khóa không reset thời gian chờ; input tiếp theo trong desktop mới reset mốc 60 giây/5 phút. Đã cập nhật XP08.
- H06: sửa nội dung ký ức không đổi mức thân thiết; xóa vẫn có thể ảnh hưởng theo đóng góp. Đã cập nhật KN02.
- H07: nội dung tập tin/thư mục cho đọc chỉ dùng tức thời, không tạo ký ức lâu dài. Đã cập nhật QD07.
- H09 bổ sung: trì hoãn bài học vẫn giữ yêu cầu; xong hoạt động hiện tại tự thực hiện khi đủ quyền/giao diện/điều kiện. Chưa chốt hàng đợi/hủy.
- H09/BH06 mới hơn: hàng đợi nhiều việc, xem thứ tự/hủy từng việc riêng. Chưa chốt cách xử lý phần còn lại nếu một việc lỗi.
- BH06 bổ sung: việc lỗi dừng riêng, các việc sau tiếp tục nếu từng việc đủ quyền/điều kiện. Không tự chạy lại việc lỗi hoặc ghi là thành công.
- BH07: thoát app báo rõ và hủy các việc chưa hoàn thành; không tự chạy hàng đợi khi mở lại. Giữ bài học đã lưu.
- BH07/H09 mới nhất: đổi hồ sơ cũng báo rõ/hủy việc chưa xong, không chuyển việc sang hồ sơ khác. Nhóm hàng đợi đã chốt hành vi chính.
- H10/SH07: tối đa 5 đồ ảo để lại, không tính đồ đang cầm/dùng; cách xử lý khi đầy chưa chốt.
- H10/SH07 mới hơn: đủ 5 thì tự cất bớt bằng hoạt ảnh trước khi để thêm đồ mới.
- QD10: được biết riêng vị trí/kích thước cửa sổ chưa cấp Đọc để đi lại, không đọc tiêu đề/nội dung, không tự cấp Điều khiển.
- H02/QH06: giận nhẹ không thời gian từ chối nhấc cố định; tùy tâm trạng và cách được dỗ, không tự đặt vài phút.
- XP09/H10: nhân vật/sofa che phụ đề thì người dùng tự kéo ra chỗ khác, không yêu cầu tự né phụ đề.
- QD11: tài liệu mở trong app như Word chỉ được nhớ tên/chủ đề đang đọc, không chi tiết nội dung; đọc file trực tiếp vẫn tức thời theo QD07. Không dùng quyền nhớ màn hình để vượt giới hạn này.
- HS03: Đặt lại nhân vật chỉ reset ký ức/quan hệ/trạng thái hồ sơ đang chọn, giữ hồ sơ khác và quyền chung; bài học khi reset chưa chốt.
- HS03 mới hơn: đặt lại xóa cả mọi bài học của hồ sơ đó; không ảnh hưởng hồ sơ khác/quyền chung.
- Đã bắt đầu khảo sát đọc-only nguồn chính thức Chrome content scripts/permissions, Edge native messaging, Windows UI Automation. Ghi docs/KHAO_SAT_SO_BO.md; chưa chọn stack hoặc cài gì. Câu kế tiếp: người dùng có chấp nhận cài tiện ích hỗ trợ khi bật tương tác website hay không.
- QD12 mới nhất: người dùng chấp nhận tiện ích Chrome/Edge tùy chọn khi bật tương tác web; cơ bản không cần, không tự cấp mọi website. Chưa cài/chọn phương án.
- SP07/H15: tính cách có thể thay đổi lâu dài theo trải nghiệm/cách đối xử, không chỉ tâm trạng/sở thích. Cần hỏi ví dụ/giới hạn; không phải tự sửa code.
- SP07/H15 ví dụ được xác nhận: ban đầu tinh nghịch/làm trước nghĩ sau, qua trải nghiệm/hướng dẫn dần cân nhắc hơn nhưng vẫn có ý muốn riêng. Chưa chốt áp dụng mức nào.
- SP07/H15 mới hơn: phát triển tính cách chỉ ở nâng cao; cơ bản giữ tính cách ban đầu, vẫn thay đổi tâm trạng. Đã cập nhật bảng hai mức.
- MC03 mới hơn: giữ tính cách đã phát triển khi hạ cơ bản; nâng cao bật lại tiếp nối, không reset.
- SP07/H15: luôn giữ tò mò/tinh nghịch/ý muốn riêng; chỉ thay đổi cách thể hiện và biết cân nhắc hơn, không biến thành tính cách khác hoàn toàn.
- SP08/H15: chỉ học cách hành xử từ tương tác/trải nghiệm, không nút đánh giá hành vi; không tự coi bỏ qua lời rủ khi bận là phê bình.
- QD13/H11: người dùng chọn phương án 2 sau giải thích: cho dùng riêng khung video khác nguồn nhúng trong trang phim được phép, không cho mở/khám phá toàn website nguồn; không áp sang quảng cáo hoặc khung khác. Cần kiểm chứng nhận diện đúng.
- QD13 bổ sung: chưa chắc khung video thì nhờ người dùng chỉ và xác nhận trước khi dùng, không tự mở rộng quyền.
- QD14: được nhớ nhận diện ô video trên đúng trang, lần sau kiểm tra lại/không khớp thì hỏi; không dùng tọa độ cũ hoặc tự gọi bài học.
- DK03: Dừng khẩn cấp hủy việc đang chạy; giữ việc chưa chạy tạm dừng. Không tự chạy lại sau 60 giây.
- DK04 mới hơn: Tắt quan sát/Ẩn cũng hủy việc đang chạy, giữ việc chưa chạy tạm dừng. Các ngoại lệ metadata vị trí/kích thước khi tắt quan sát vẫn giữ.
- BH08: bật lại chức năng/hiện nhân vật không tự chạy việc cũ; phải bấm Tiếp tục hàng đợi riêng, không phục hồi việc đã hủy. E03 đã thêm kiểm chứng vòng đời này.
- K04 khảo sát tài liệu Microsoft: GetHistoryItemsAsync, các trạng thái Success/AccessDenied/ClipboardHistoryDisabled và IsHistoryEnabled. Chưa gọi API hoặc đọc clipboard thật, chưa chứng minh detect Win+V; ghi KHAO_SAT_SO_BO.md.
- H13: TCYP (Take Care Your Pet) chỉ là tên người dùng đề xuất, chưa chốt. Muốn tên ngắn gọn/sang trọng, có thể khác hoàn toàn TCYP. Chưa đổi tên tài liệu/dự án.
- H13 mới hơn: người dùng muốn tránh xung đột “bản quyền” tên. Chưa chốt TCYP/Ylune/Sylmi/Aelvi; chưa có tra cứu nhãn hiệu đủ để xác nhận an toàn. Đã đọc hướng dẫn WIPO về nhãn hiệu/tra cứu cả cơ sở quốc gia; cần hỏi thị trường phát hành, không hứa rủi ro bằng không.
- SP03/H13 mới nhất: phát hành Việt Nam trước, quốc tế để sau; phạm vi tra cứu tên ban đầu là Việt Nam. Chưa chốt tên chính thức.
- H13 mới nhất: bỏ TCYP, tìm tên mới ngắn/sang trọng. Không dùng các tên gợi ý trước như đã được xác nhận an toàn; chưa chốt thương hiệu.
- Đợt sàng lọc tên mới: đề xuất hai hướng Ylavi (i-la-vi) và Ylavyn (i-la-vin), chưa được chọn/chưa clearance nhãn hiệu. Chi tiết docs/TEN_UNG_VIEN.md. Chỉ tìm web sơ bộ; không tuyên bố đã tra cứu đầy đủ cơ sở Việt Nam/WIPO. Tài khoản cá nhân Ylavi xuất hiện trên web không được tự coi là quyền nhãn hiệu.
- H13 mới nhất: đã loại Ylavi/Ylavyn vì không hợp gu. Người dùng thích tên AIRI từng thấy GitHub; chỉ tham chiếu phong cách, chưa chọn tên chính thức hoặc đồng ý dùng tên gần giống. Cần hỏi thích điểm nào thay vì tiếp tục đoán tên kỳ ảo.
- H13 gu đã xác nhận: mềm như tên nhân vật + hình thức gọn, hiện đại; thích kết hợp hai điểm này ở AIRI. Không phải chọn AIRI hoặc tên gần giống, vẫn cần sàng lọc nhãn hiệu VN.
- Đang đề xuất tên theo gu mới: UYRI (uy-ri), NYUA (nyu-a); chỉ ứng viên, chưa được người dùng chọn và chưa clearance nhãn hiệu. Đã tìm web sơ bộ; không coi ít kết quả là bằng chứng an toàn.
- Quyết định mới nhất QD07/H07/K06: đọc tập tin/thư mục chọn riêng để cập nhật sau. Không hỏi tiếp định dạng, không khảo sát parser hoặc triển khai chức năng đó trong bản đầu. Không đồng nhất với quan sát màn hình hoặc xuất/nhập sao lưu vẫn còn trong phạm vi.

- Đã được cho tiến hành: hợp nhất yêu cầu, phân loại điểm chưa chắc và lập đề cương phép thử nhỏ. Chưa cho xây ứng dụng đầy đủ; lượt này chỉ sửa tài liệu.
- Đọc docs/YEU_CAU_HIEN_HANH.md làm nguồn yêu cầu hiện tại; docs/DIEM_CHUA_CHAC.md và docs/KE_HOACH_KIEM_CHUNG.md cho câu hỏi/khảo sát/phép thử còn mở. Các phần bên dưới và hai file phỏng vấn là lịch sử.
- Đã hợp nhất cả các câu trả lời sau lần lưu PHONG_VAN_BO_SUNG: Windows + V đọc toàn lịch sử khi mở, không nhớ lâu; danh bạ/email/lịch qua giao diện; thư mục gồm thư mục con; thu hồi quyền cho chọn xóa ký ức.
- Sao lưu chỉ xuất thủ công, bắt buộc mật khẩu + mã khôi phục, không khóa AI. Nhập thêm hồ sơ, chỉ một hoạt động; hồ sơ không chọn đóng băng mọi trạng thái; quyền chung trên máy, không tự nhập quyền từ file.
- Mốc thiếu quan tâm là tổng 48–72 giờ thao tác người dùng đủ điều kiện, dừng sau 60 giây không thao tác; không còn 3 ngày lịch. Tin tưởng gần 72, tổn thương gần 48; buồn trước rồi mới tự ẩn nếu kéo dài. Dỗ qua vài buổi, không một lần là hết.
- Quà là đồ ăn/thú bông; mời ra/tặng từ cửa sổ khay hệ thống hoặc biểu tượng nhỏ chỗ ẩn. Đọc chỉ cửa sổ/tab đang thực sự hiện, cả hai khi chia màn hình có quyền; tự chọn chú ý theo sở thích, không phải luôn theo mọi cảnh.
- Gỡ app hỏi giữ/xóa dữ liệu và nhắc xuất. Chưa công khai mã nguồn. Chuyển động pixel mượt mềm mại.
- Sáu phép thử mới chỉ là đề cương, chưa triển khai/chạy. Không công bố đạt dưới 1 giây, che bí mật hoàn hảo, hỗ trợ mọi app, cấu hình tối thiểu hoặc model đã chọn.
- Bước tiếp: rà điểm sản phẩm ảnh hưởng phép thử đầu và hỏi từng câu; khảo sát nguồn chính thức để đề xuất phương án thử. Không quay lại hỏi các điểm đã được chốt.
- Không có app native, Graphify hay Git trong workspace được thiết lập ở lượt này. Không đổi permissions.html/JSON quyền gốc hoặc DESIGN.md.

## Đọc trước: trạng thái hiện hành

- Cập nhật mới nhất sau nhiều vòng hỏi: đọc docs/PHONG_VAN_BO_SUNG.md trước; tài liệu này bổ sung/thay thế quyết định cũ ở các điểm mâu thuẫn. Phỏng vấn vẫn đang tiếp tục, người dùng chưa cho chuyển bước.
- Điểm dừng mới nhất: bài học yêu cầu trực tiếp có thể trì hoãn một lần theo tâm trạng, yêu cầu lần hai thì thực hiện nếu đủ quyền/điều kiện; dọn đồ có thể từ chối theo tâm trạng. Chưa gửi câu tiếp theo sau mốc này.

- Người dùng yêu cầu lưu tiến độ phỏng vấn ngày 2026-11-13. Xem docs/PHONG_VAN_DU_AN.md để biết các quyết định mới nhất; các mục bên dưới là lịch sử và có thể đã bị thay thế.
- Dự án: cô gái anime trưởng thành chibi pixel 128×128 sống tự do trên desktop/cạnh cửa sổ. Tóc trắng bạc dài ngang eo, mái thưa; mắt đỏ hồng; áo len rộng hồng nhạt, chân váy xám đậm; chân trần.
- Đã chốt quyền theo app và theo website: đọc/điều khiển riêng, mặc định tắt; che vùng không được đọc; nhường chuột/phím, chờ 60 giây người dùng không thao tác để trở lại.
- Âm thanh tạm gác. Gửi chữ tới AI phải xem và hỏi mỗi lần. Tự cập nhật riêng app nhân vật. Không tác vụ sửa dữ liệu/gửi tin/mua hàng; cần làm rõ ngoại lệ dữ liệu riêng.
- Bản sao file quyền gốc: docs/quyen-nhan-vat-da-chon.json; quyết định phỏng vấn sau đó ưu tiên hơn file.
- Tiếp tục interview-me qua ô câu hỏi từng câu; người dùng muốn chọn từng chi tiết trước tạo mẫu. Điểm dừng: tóc dài ngang eo; tiếp theo hỏi màu da. Chưa tạo mẫu hoặc code nhân vật; chưa có xác nhận ý định cuối.

## Mục tiêu và cách phối hợp

- Người dùng mới học vibe code, muốn vừa làm vừa học cùng AI.
- Giải thích bằng tiếng Việt dễ hiểu; hỏi từng câu về nhu cầu thực tế.
- Làm từng phần nhỏ: mô tả → triển khai → AI kiểm tra → người dùng dùng thử → lưu mốc.
- Không tự biến ví dụ app công việc thành yêu cầu sản phẩm.

## Trạng thái ngày 2026-11-13

- Thư mục ban đầu trống; đã tạo bộ hướng dẫn Markdown, mẫu mô tả ý tưởng và bộ nhớ này.
- Chưa chọn ý tưởng, nền tảng, công nghệ hay dịch vụ; chưa có code ứng dụng.
- Chưa thiết lập Git, lệnh chạy hoặc triển khai. Không tuyên bố có mốc khôi phục khi chưa thiết lập.
- Chưa có Graphify hoặc DESIGN.md; chỉ tạo khi có dự án và nhu cầu tương ứng.

## Tài liệu

- README.md: điểm bắt đầu.
- docs/QUY_TRINH_VIBE_CODE.md: quy trình, câu nhắn mẫu và cách kiểm tra.
- docs/Y_TUONG_APP.md: mẫu để người dùng điền trước khi xây dựng.

## Kiểm chứng

- Tài liệu được đọc lại và kiểm tra liên kết tương đối, cấu trúc khối mã sau khi tạo.
- Chưa có app để chạy hoặc kiểm thử; người dùng chưa dùng thử tài liệu.

## Bước tiếp theo

Người dùng điền mô tả app hoặc kể ý tưởng bằng lời. AI làm rõ từng câu, chốt phạm vi và luồng sử dụng trước khi chọn công nghệ hay viết code.

## Cập nhật: phỏng vấn và trang chọn quyền

- Ý tưởng đã được kể: nhân vật anime pixel 128×128 sống trên máy, hoạt bát, tò mò và tinh nghịch; chào khi mở máy, tự ngủ/thức, không bắt buộc trò chuyện.
- Muốn nhìn nội dung màn hình, cùng xem phim trên sofa ảo, ăn bắp ngô, nhảy theo nhạc; leo giao diện và bấm chuyển tập thật.
- Đây chưa phải bản yêu cầu đã xác nhận đầy đủ. Tiếp tục interview-me, từng câu bằng ô câu hỏi; không tự đoán các phần còn thiếu.
- Người dùng yêu cầu danh sách quyền chi tiết và trang HTML/CSS để tick. Đã tạo permissions.html với 160 quyền A01–L12, 12 nhóm; điều kiện riêng, hỏi mỗi lần hoặc tự làm trong giới hạn, tìm kiếm, lọc, lưu localStorage có báo lỗi và xuất JSON.
- Quyền nhóm L và các thao tác tập tin nhạy cảm giữ chế độ hỏi mỗi lần. Mọi quyền ban đầu chưa chọn; không có quyền hệ thống thực nào được cấp.
- Trang chạy trực tiếp trong trình duyệt, không mạng hay thư viện. DESIGN.md ghi quy ước giao diện. README.md thêm hướng dẫn mở.
- Kiểm tra thực tế: Node biên dịch JavaScript thành công; kiểm đếm dữ liệu được 160 quyền / 12 nhóm. Chưa kiểm tra trong trình duyệt thật; chưa xác minh thao tác tick, tải file và hiển thị. Chưa có trình tự động kiểm tra trình duyệt được cài trong dự án.
- Thư mục chưa phải kho Git; không có commit hoặc mốc khôi phục Git.
- Bước tiếp theo: người dùng mở permissions.html, chọn quyền và tải JSON; dùng lựa chọn đó để tiếp tục phỏng vấn về giới hạn và hành vi nhân vật.

## Điều chỉnh phạm vi danh sách quyền

- Người dùng chỉ muốn chọn quyền truy cập/tác động lên máy, không hỏi hành vi sinh hoạt; hành vi nhân vật sẽ bàn sau.
- Đã thay danh sách bằng 132 quyền trong 9 nhóm: màn hình, đầu vào, âm thanh/camera, trình duyệt, tập tin, hệ điều hành, dữ liệu cá nhân/tài khoản, lưu trữ và mạng/AI.
- Đổi nhãn thành “Xin phép khi dùng quyền”; giữ giới hạn riêng. Mặc định tất cả chưa chọn.
- Dùng khóa lưu anime-access-permissions-v2 và schemaVersion 2; không áp lựa chọn cũ vào mã quyền đã đổi. Dữ liệu v1 không bị xóa.
- Kiểm tra Node thành công: cú pháp, 132 ID duy nhất, 9 nhóm và khóa lưu riêng. Trình duyệt công cụ chặn truy cập file:// nên chưa xác minh trực quan bản sửa.

## Lựa chọn toàn quyền

- Theo yêu cầu người dùng, mỗi mục có thêm mode full: “Toàn quyền đối với quyền này”, không hỏi lại/không giới hạn bổ sung cho riêng mục. Không cấp các quyền khác, không bỏ giới hạn bắt buộc hay điều kiện trong tên quyền.
- Full vô hiệu hóa ô giới hạn và xuất note rỗng; giữ nội dung cũ trên trình duyệt để người dùng đổi lại chế độ. Mode limited thiếu giới hạn sẽ chặn xuất và đưa focus tới ô cần điền.
- Bỏ cơ chế ép chế độ ask ở một số mục trên bản yêu cầu; mọi mục đều có ba lựa chọn. Không có thực thi hoặc thay đổi quyền hệ thống.
- Giữ khóa lưu v2 để bảo toàn lựa chọn hiện tại, nâng schema JSON lên 3. Đã kiểm tra cú pháp và cấu trúc mã bằng Node; chưa xác minh tương tác trong trình duyệt.

## Mô tả từng quyền

- Đã bổ sung 132 mô tả riêng ngay dưới 132 quyền trong permissions.html, gồm ý nghĩa, ví dụ và ranh giới với quyền khác khi phù hợp.
- Mô tả luôn nhìn thấy trước khi tick, gắn aria-describedby vào checkbox; tìm kiếm bao gồm mô tả, JSON xuất kèm explanation, schemaVersion 4.
- Giữ nguyên ID và khóa lưu v2 nên không chủ động xóa lựa chọn đã lưu của người dùng.
- Node kiểm tra cú pháp, đủ 132 mô tả đúng ID, liên kết mô tả trợ năng và tích hợp xuất JSON thành công; chưa kiểm chứng hiển thị trong trình duyệt.


## E02a guided user acceptance — historical blocker locating binary

User reports no E02a window/executable and requests locating existing build only, no rebuild/product changes/publishing. Accessible C: filename search found no PolicyLab EXE/DLL; documentation ZIP has no binaries. No PolicyLab.App process found. User-feedback record: tasks/E02a-USER-ACCEPTANCE.md. All UI/acceptance checks remain untested/open; do not mark any checkbox passed. Await existing binary/backup location from user; do not build without later explicit authorization.


## Demo E02a trên máy hiện tại

Explicit user authorized rebuilding E02a demo locally after confirming old binary was on another machine. Existing source unchanged, isolated SDK10.0.404, tests53/53 and UI RunAll35/35. Artifact E02a-demo.zip, report docs/E02a-CURRENT-MACHINE-RESULTS.md. No full-product/Unity/AI or publishing; resize/full keyboard/human acceptance remain open.


## Graphify local navigation — current integration

Explicit new task authorizes only local docs/tooling, no product changes/runtime tests/push/PR update. Installed graphifyy0.9.97 verified against official tag; extract.py/cli.py SHA match. docs/context/context_nav.py uses real deterministic extract API with explicit C#/Python allowlist, socket/subprocess deny guard and120s build supervisor. No semantic/API/upload or global skill/hook installation. graphify-out/GRAPH_REPORT.md is short entry; graph.json raw AST/resolver tags preserved, registry-index separate REGISTRY_DECLARED_NOT_CODE. Manual module→lab reference is NOT production implementation. XAML/runtime not scanned/proven. Task context pack retains complete task/requirements/acceptance/relevant confirmed+residual decisions/full CONSTRAINTS/prereqs/whitelist/anchors; max160000UTF8bytes, fail on overflow without partial safety data. Optional code neighbors1hop/12edges with omitted count. All219tasks/7modules checked, stale/unknown/overflow negative controls. Freshness hashes source inventory/schema/output; change -> rebuild, never trust stale map. AI workflow summary -> check -> task pack -> exact anchors; never load full graph.json into prompt. Measurements exact bytes/chars, token estimate chars/4 only. E02a human acceptance C3 remains open. Documentation ZIP updated in place; source code not bundled, checkout required for freshness/rebuild. No new Graphify work pushed.


## PR1 merge review — portable hash fix

Full exact-head review found schema1 raw source/output fingerprints tied to Windows CRLF and stale after Git LF checkout. Schema2 now explicitly normalizes UTF8 text BOM/newlines only for source/map/measurement freshness; whitespace/content edits remain significant, upstream package/binary/ZIP checks remain raw. Clean git archive LF + CRLF roundtrip and edited-source controls required before merge; no product functionality or acceptance change. Authenticated GitHub access works; native SCM review cannot attach, independent fallback exact-head review required. No deployment.
