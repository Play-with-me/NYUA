# Mô tả Cấu trúc Thư mục, Công cụ Sử dụng & Ngôn ngữ Lập trình — Dự án NYUA

> **Trạng thái tài liệu:** Tổng hợp trung thực hiện trạng mã nguồn, công cụ và cấu trúc thư mục của repository `NYUA` tính đến **2026-11-16**.
> - **Nguyên tắc phân biệt rạch ròi:** Tài liệu tách rõ **(A) Thành phần ĐÃ CÓ THẬT trong repository** (mẫu `E02a`, bộ fixture bootstrap `B00-01`/`B00-02`, công cụ tài liệu/Graphify, trang chọn quyền lịch sử) với **(B) Cấu trúc và Công cụ DỰ KIẾN (PROPOSED)** cho ứng dụng sản phẩm đầy đủ (`src/`, `godot/CompanionRenderer/`, AI cục bộ, bộ cài).

---

## 1. Thống kê Ngôn ngữ Lập trình & Định dạng File Hiện có

Tổng số tệp được Git theo dõi trong repository (trước khi tạo `docsai/`): **168 tệp**.

| Ngôn ngữ / Định dạng | Đuôi file | Số lượng thực tế | Phạm vi & Vai trò sử dụng |
|---|---|---:|---|
| **Markdown** | `.md` | 94 | Đặc tả SRS, kiến trúc, nghiệp vụ, UX, Art, QA, 16 file phase tasks, bản đọc HUMAN, báo cáo kiểm chứng & bộ nhớ dự án |
| **Mermaid Diagram** | `.mmd` | 15 | 15 sơ đồ kiến trúc, ngữ cảnh, container, DAG module, read boundary, state machine, data ER, task DAG (`docs/product/diagrams/`) |
| **JSON** | `.json` | 12 | Registry chuẩn (`requirements.json`, `backlog.json`), schema, Graphify output (`graph.json`, `manifest.json`, `MEASUREMENTS.json`), config SDK/hooks |
| **C#** | `.cs` | 12 | **Ngôn ngữ chính tầng Core & Host (.NET 10 LTS):** 11 file trong `labs/policy-native/` (`PolicyLab.Core`, `Scenarios`, `App`, `Tests`) + 1 file trong `tests/bootstrap/companion/BootstrapTests.cs`. Dự kiến dùng cho toàn bộ `src/Host/*`, `src/Desktop.Wpf/*`, `src/BrowserBridge/*`, và script Godot C# (`godot/CompanionRenderer/scripts/*.cs`) |
| **Python 3.12** | `.py` | 11 | **Ngôn ngữ công cụ kiểm chứng & đồng bộ nội bộ:** 11 script đồng bộ `requirements/decisions/backlog`, kiểm tra dossier/task DAG, vẽ sơ đồ raster/SVG, và adapter Graphify (`docs/context/context_nav.py`, `check_checkout.py`) |
| **MSBuild / .NET Project** | `.csproj` | 5 | Khai báo build/dependency `.NET 10`: 4 project trong `labs/policy-native/` + 1 project trong `tests/bootstrap/companion/` |
| **PNG / SVG** | `.png`, `.svg` | 4 + 4 | 4 cặp sơ đồ xuất bản (`architecture`, `delivery`, `permissions`, `data`) do `build_diagrams.py` kết xuất |
| **CSV** | `.csv` | 2 | Ma trận truy vết `TRACEABILITY.csv` (yêu cầu ↔ AT ↔ task) & `TASK_TRACEABILITY.csv` |
| **XAML** | `.xaml` | 2 | **Giao diện Desktop Native (WPF):** `App.xaml` và `MainWindow.xaml` trong `labs/policy-native/PolicyLab.App/`; dự kiến dùng cho toàn bộ màn hình `src/Desktop.Wpf/*.xaml` |
| **GDScript** | `.gd` | 1 | **Script Godot Engine:** `BootstrapVerify.gd` cho phép thử headless `B00-02` và dự kiến `ProbeBuild.gd` ở `P02-01` |
| **Godot Project/Config/Scene** | `.godot`, `.cfg`, `.tscn` | 1 + 1 + 1 | Cấu hình dự án Godot 4.7 (`project.godot`), preset export (`export_presets.cfg`) và scene (`Bootstrap.tscn`) tại `tests/bootstrap/desktop-body/GodotFixture/` |
| **HTML5 + CSS3 + Vanilla JS** | `.html` | 1 | 1 tệp độc lập `permissions.html` (không thư viện ngoài, dùng cho bước phỏng vấn chọn 132 quyền lịch sử) |
| **Windows PowerShell 5.1** | `.ps1` | 1 | Supervisor kiểm thử có giới hạn thời gian 120s & diệt cây tiến trình (`tools/verify/companion.ps1`) |
| **Git config / ignore** | `.gitignore` | 1 | Quy tắc loại trừ `.tools/`, `bin/`, `obj/`, `artifacts/`, `TestResults/`, `.env`, `__pycache__/`, `.godot/` (cần bổ sung khi tạo `P02-01`) |

<details>
<summary><b>Bảng chi tiết số lượng file theo từng phần mở rộng thực tế</b></summary>

| Phần mở rộng | Số lượng |
|---|---:|
| `.md` | 94 |
| `.mmd` | 15 |
| `.cs` | 12 |
| `.json` | 12 |
| `.py` | 11 |
| `.csproj` | 5 |
| `.png` | 4 |
| `.svg` | 4 |
| `.csv` | 2 |
| `.xaml` | 2 |
| `.cfg` | 1 |
| `.gd` | 1 |
| `.gitignore` | 1 |
| `.godot` | 1 |
| `.html` | 1 |
| `.ps1` | 1 |
| `.tscn` | 1 |

</details>

---

## 2. Stack Công nghệ & Công cụ: Đã Xác minh vs Đề xuất vs Chưa Chọn

### 2.1. Ngôn ngữ, Runtime & Công cụ ĐÃ CÓ BẰNG CHỨNG THỰC TẾ trên máy
| Thành phần | Phiên bản / Định danh thực tế | Giấy phép / Chi phí | Trạng thái & Nơi sử dụng |
|---|---|---|---|
| **`.NET SDK` & Runtime** | SDK **`10.0.404`**, Runtime **`10.0.15`** (`win-x64`, `net10.0` / `net10.0-windows`) | MIT (`$0`) | Cài cô lập (không sửa `PATH` hệ thống); chữ ký `dotnet.exe` Valid; ghim tại `labs/policy-native/global.json`. Đã build/test `E02a` (`53/53 PASS`) và `B00-01` (`PASS`). |
| **WPF (Windows Presentation Foundation)** | Thuộc `.NET 10 Desktop` (`UseWPF=true`, `net10.0-windows`) | MIT (`$0`) | Đã dùng chạy `labs/policy-native/PolicyLab.App/` (`35/35 UI cases`, đóng C3 trải nghiệm). Dùng cho màn hình cài đặt/tray Host. |
| **MSTest + Test SDK** | `Microsoft.NET.Test.Sdk 17.14.1`, `MSTest.TestAdapter 3.8.3`, `MSTest.TestFramework 3.8.3` | MIT (`$0`) | Restore offline từ cache NuGet; đã dùng ở `PolicyLab.Tests` & `Bootstrap.Tests`. Đã audit `--vulnerable --include-transitive`: 0 lỗ hổng tại thời điểm chạy. |
| **Godot Engine – .NET** | **`4.7.2-stable` Mono/.NET** (`4.7.2.stable.mono.official.ed1daf0bf`, Windows x64, `82/82` file khớp SHA-256) | MIT (`$0`, không trần doanh thu, không cần tài khoản) | Đã chạy kiểm chứng headless GDScript `B00-02` (`UW01` dương/âm & `UW02` hang kill-tree `PASS`). Cần truyền `DOTNET_ROOT` & `PATH` cục bộ trong tiến trình con. |
| **Python & Graphify AST** | **Python `3.12`** + **`graphifyy 0.9.97`** (`tree-sitter 0.25.2`, `tree-sitter-c-sharp 0.23.5`, `tree-sitter-python 0.25.0`) + **Pillow (PIL)** | Apache-2.0 + MIT (`$0`) | Chạy bộ công cụ kiểm tra dossier (`validate_dossier.py`, `validate_tasks.py`), sinh sơ đồ (`build_diagrams.py`), trích xuất AST cục bộ không LLM (`context_nav.py`). *Lưu ý:* `python` mặc định MSYS trên máy thiếu Pillow; chưa cài gói `jsonschema`. |
| **Windows PowerShell** | **`5.1.26100.9818`** | Tích hợp Windows | Chạy supervisor `tools/verify/companion.ps1` (`WaitForExit` tối đa `120s`, `taskkill /PID ... /T /F`, bọc `artifacts-path` cô lập vào `TEMP`). |
| **Trình duyệt / Web chuẩn** | HTML5 + CSS3 + ES6+ thuần (Zero dependencies) | Chuẩn mở (`$0`) | Dùng duy nhất cho file phỏng vấn lịch sử `permissions.html` (với `localStorage` key `anime-access-permissions-v2`, export JSON `schemaVersion: 4`). **Không** dùng làm giao diện sản phẩm chính (`SP09`). |
| **Git & AO Hooks** | Git (nhiều worktree) + `ao` hooks (`.agents/hooks.json`) | Miễn phí | Quản lý nhánh, worktree song song và kiểm tra checkout LF/CRLF (`check_checkout.py`). |

### 2.2. Công nghệ ĐỀ XUẤT (`PROPOSED` / `NOT VERIFIED`) & Các Thành phần CHƯA CHỌN (`NOT SELECTED`)
| Thành phần | Định hướng đề xuất hiện tại | Trạng thái kiểm chứng |
|---|---|---|
| **Godot C# Renderer & Export** | `Godot.NET.Sdk` (`4.7.2`), `CompanionRenderer.csproj`, official `.NET` export templates (`Windows Desktop`), `GL Compatibility` vs `Forward+/Mobile` | **`NOT VERIFIED`:** Chưa cài export templates, chưa biên dịch C# trong Godot, chưa đo Windows 11 DWM transparency / `SetWindowRgn` clipping / click-through / DPI (`UW03–UW13`). |
| **Giao thức IPC Host ↔ Renderer** | `NamedPipeServerStream` (`PipeOptions.CurrentUserOnly`), `4-byte` LE length-prefix + UTF-8 JSON `<= 64 KiB`, `MaxDepth=16`, `System.Text.Json` strict allowlist | **`NOT IMPLEMENTED / NOT VERIFIED`:** Thuộc phạm vi `P02-04`, `P02-05` (`UW14–UW29`). |
| **Local AI / OCR tiếng Việt** | Chưa chọn model/runtime/quantization (`D-04`). Tách phản ứng nhanh C# và suy luận cảnh Local AI worker | **`NOT SELECTED`:** Phải sàng lọc giấy phép phân phối lại ở `P03-01` và đo benchmark dưới tải Godot ở `P03-02..P03-03`. |
| **Browser Bridge (Chrome/Edge)** | Extension tùy chọn (Manifest V3 + Native Messaging) chỉ khi bật tương tác website (`QD12`, `P10-06`) | **`NOT IMPLEMENTED`:** Mới khảo sát tài liệu Google/Microsoft (`docs/KHAO_SAT_SO_BO.md`). |
| **OS Capture / UI Automation / Input** | Windows Graphics Capture / UI Automation / `SendInput` có kiểm soát UIPI + `Win+V` Clipboard history (`GetHistoryItemsAsync`) | **`NOT IMPLEMENTED`:** Mới khảo sát tài liệu Microsoft (`K01–K04`). |
| **Storage Engine & Crypto Backup** | Chưa chọn DB vật lý (SQLite hoặc file transactional) và thư viện KDF/AEAD đã kiểm định (`D-07`, `K07`) | **`NOT SELECTED`:** Bắt buộc chốt thiết kế an toàn tại `P50-01`, `P50-03` (cấm tự viết thuật toán mã hóa). |
| **Installer / Code Signing / Auto-Update** | Chưa chọn công cụ đóng gói (MSIX/WiX/Inno), cơ chế update có chữ ký số (`D-13`, `K08`) | **`NOT SELECTED`:** Chưa có ngân sách ký số; mọi khoản phí cần user duyệt riêng. |

### 2.3. Cấu hình Phần cứng Máy Khảo sát Hiện tại (`docs/KHAO_SAT_MOI_TRUONG.md`)
*(Chỉ là máy dùng để thiết kế thử nghiệm — **không** phải cấu hình tối thiểu công bố cho người dùng)*
- **HĐH:** Windows 11 Pro, build `26300` (`x64`)
- **CPU:** AMD Ryzen 9 8945HX with Radeon Graphics
- **RAM:** ~`15.8 GiB`
- **GPU:** NVIDIA GeForce RTX 5070 Laptop GPU (`8151 MiB` VRAM, driver `592.01`)

---

## 3. Cấu trúc Thư mục Thực tế Hiện có trong Repository

```text
NYUA/
├── .gitignore                        # Loại trừ .tools/, bin/, obj/, artifacts/, TestResults/, .env, __pycache__
├── CAPABILITY_MAP.md                 # Bản đồ 7 module khả năng & DAG phụ thuộc đã duyệt
├── CONSTRAINTS.md                    # Tiêu chuẩn chất lượng văn bản & các chiều cần đo
├── DESIGN.md                         # Quy ước giao diện (#f5f6f8, #202b38, #155e52, font 16, 4px/8px)
├── README.md                         # Điểm vào chính của dự án & liên kết hồ sơ
├── SPEC-policy.md                    # Đặc tả đã duyệt cho phép thử quyền E02a (dữ liệu giả)
├── permissions.html                  # Trang chọn 132 quyền (9 nhóm A-I) chạy offline bằng HTML/CSS/JS (lịch sử)
│
├── .agents/                          # Bộ nhớ liên tục & hooks cho AI Agents
│   ├── .gitignore
│   ├── PROJECT_MEMORY.md             # Nhật ký bộ nhớ dự án (đọc đầu phiên, cập nhật sau VERIFY)
│   └── hooks.json                    # Cấu hình hooks agent-orchestrator (ao)
│
├── docs/                             # Toàn bộ tài liệu nghiệp vụ, khảo sát, hồ sơ & công cụ
│   ├── YEU_CAU_HIEN_HANH.md          # Nguồn nghiệp vụ gốc duy nhất hợp nhất mọi quyết định hiện hành
│   ├── DIEM_CHUA_CHAC.md             # Phân loại điểm mở: H01-16 (Hỏi user), K01-09 (Khảo sát), T01-08 (Thử nghiệm)
│   ├── KE_HOACH_KIEM_CHUNG.md        # Đề cương 6 phép thử E01-E06
│   ├── PHEP_THU_DAU_TIEN.md          # Đề cương phép thử E02a (16 tình huống A01-A16 + B01-B06)
│   ├── E02a-CURRENT-MACHINE-RESULTS.md # Ghi nhận chạy demo E02a trên máy hiện tại (53/53 test, 35/35 UI)
│   ├── KHAO_SAT_MOI_TRUONG.md        # Thông số phần cứng máy khảo sát (11/2026)
│   ├── KHAO_SAT_SO_BO.md             # Khảo sát tài liệu Chrome/Edge extension, Win UI Automation, Win+V
│   ├── PHONG_VAN_DU_AN.md            # Lịch sử phỏng vấn đợt 1
│   ├── PHONG_VAN_BO_SUNG.md          # Lịch sử phỏng vấn bổ sung
│   ├── quyen-nhan-vat-da-chon.json   # Ảnh chụp JSON quyền cũ (69/132 — lịch sử, không dùng làm config)
│   ├── TEN_UNG_VIEN.md               # Nghiên cứu tên ứng viên & tra cứu sơ bộ WIPO/IPPlatform cho NYUA
│   ├── QUY_TRINH_TEAM_SAN_PHAM.md    # Quy trình làm việc chuẩn theo vai trò & gate
│   ├── QUY_TRINH_VIBE_CODE.md        # Tài liệu hướng dẫn học quy trình từng bước
│   ├── Y_TUONG_APP.md                # Mẫu bài tập khởi đầu (tài liệu học)
│   │
│   ├── context/                      # Hệ thống Graphify cục bộ & đóng gói ngữ cảnh có giới hạn (<=160KB)
│   │   ├── README.md                 # Hướng dẫn workflow đọc nhỏ & kiểm tra freshness
│   │   ├── VALIDATION.md             # Báo cáo đo baseline vs scoped context pack
│   │   ├── context_nav.py            # Adapter gọi graphifyy 0.9.97 (chặn socket/Popen, build/check/test/measure/task/module)
│   │   └── check_checkout.py         # Kiểm tra portable SHA256 LF/CRLF qua git archive trong TEMP
│   │
│   ├── experiments/                  # Báo cáo thực nghiệm các chặng bootstrap/probe đã chạy
│   │   ├── bootstrap-companion.md    # Báo cáo PASS bootstrap B00-01 (.NET 10 LTS + supervisor)
│   │   └── bootstrap-desktop-body.md # Báo cáo PASS bootstrap B00-02 (Godot 4.7.2 .NET headless)
│   │
│   ├── godot-windows/                # Tài liệu kỹ thuật HIỆN HÀNH cho phép thử Godot-Windows
│   │   ├── SPEC.md                   # Đặc tả đề xuất GW-DOC-2026-11-15-r1 (NOT_AUTHORIZED)
│   │   ├── TEST_PLAN.md              # Ma trận 30 ca kiểm UW01-UW30 (đều NOT RUN) & lệnh tương lai
│   │   └── SOURCES.md                # 12 nguồn chính thức Godot 4 & Microsoft Windows (S01-S12)
│   │
│   ├── unity-windows/                # [SUPERSEDED] Trang chuyển hướng từ Unity cũ sang Godot Engine
│   │   ├── SPEC.md
│   │   ├── TEST_PLAN.md
│   │   └── SOURCES.md
│   │
│   └── product/                      # Bộ hồ sơ sản phẩm toàn diện hai phiên bản (AI & HUMAN)
│       ├── README.md                 # Trang điều hướng bộ hồ sơ 0.1
│       ├── QUALITY_REPORT.md         # Kết quả chạy validator & các giới hạn chưa chứng minh
│       ├── RECOVERY_AUDIT.md         # Biên bản kiểm toán phục hồi tài liệu
│       ├── AI/                       # Bộ tài liệu kỹ thuật đầy đủ + Scripts đồng bộ & kiểm chứng
│       │   ├── README.md             # Điểm vào & protocol cho AI/kỹ thuật
│       │   ├── SRS.md                # Đặc tả 109 yêu cầu & 10 NFR (sinh đồng bộ từ requirements.json)
│       │   ├── ARCHITECTURE.md       # Kiến trúc tổng thể & luồng container
│       │   ├── INTERFACES.md         # Envelope, DTOs, Operations, Giao thức Named Pipe
│       │   ├── DATA.md               # 14 thực thể logic, Provenance, Export/Import & Consistency
│       │   ├── SECURITY.md           # 7 Trust boundaries & 12 biện pháp STRIDE (SEC-01..12)
│       │   ├── AI_LOCAL.md           # Thiết kế đánh giá AI cục bộ & đo độ trễ end-to-end
│       │   ├── BUSINESS_RULES.md     # Predicates, Precedence 7 tầng, Lifecycle matrix & Time semantics
│       │   ├── USE_CASES.md          # 18 Use Cases (UC-01..UC-18)
│       │   ├── UX.md                 # 13 Routes, Ma trận 5 trạng thái UX, Accessibility
│       │   ├── ART.md                # Model sheet 128x128, hoạt ảnh & đồ vật
│       │   ├── QA.md                 # Chiến lược test, IT-01..IT-20, kịch bản 8h & cổng chất lượng
│       │   ├── RELEASE.md            # Quy trình CI đề xuất, staged release, update & hỗ trợ không telemetry
│       │   ├── DECISIONS.md          # Sổ ADR tóm tắt, D-01..D-18, R-01..R-09
│       │   ├── DECISION_SOURCE_2026-11-14.md # Nguyên văn các quyết định chốt ngày 2026-11-14
│       │   ├── BACKLOG.md            # Điều hướng 16 file phase tasks
│       │   ├── TEAM.md               # Hợp đồng vận hành team, DoR/DoD & kiểm soát tài liệu
│       │   ├── requirements.json     # Registry chuẩn 109 yêu cầu + source SHA256
│       │   ├── requirements.schema.json # JSON Schema draft 2020-12 cho requirements.json
│       │   ├── backlog.json          # Registry chuẩn 219 task (667 KB)
│       │   ├── human_acceptance_notes.json # Diễn giải nghiệm thu dễ hiểu cho 109 yêu cầu
│       │   ├── human_task_notes.json # Diễn giải dễ hiểu cho task
│       │   ├── TRACEABILITY.csv      # Ma trận truy vết Yêu cầu <-> SRS <-> AT <-> Task <-> UC
│       │   ├── TASK_TRACEABILITY.csv # Ma trận truy vết Owner <-> AT <-> Verification <-> Final gate
│       │   ├── source_hash.py        # Chính sách hash `utf8-text-bom-removed-universal-newlines-lf-v1`
│       │   ├── sync_requirements.py  # Trình sinh SRS.md, HUMAN/02-YEU-CAU.md, TRACEABILITY.csv
│       │   ├── sync_decisions.py     # Trình đồng bộ phần CONFIRMED-2026-11-14 vào các tài liệu
│       │   ├── sync_backlog.py       # Trình sinh 16 file tasks/phase-*.md & BACKLOG.md
│       │   ├── validate_dossier.py   # Validator tổng hợp (hash, link, DAG, CSV, ảnh PNG/SVG)
│       │   ├── check_dossier_controls.py # Kiểm tra 5 negative controls & biến thể LF/CRLF/BOM trên TEMP
│       │   ├── adr/                  # ADR-001 (hybrid), ADR-002 (host authority), ADR-005 (local AI)
│       │   └── modules/              # Đặc tả chi tiết 7 module (policy, life-state, desktop-body, perception, task-execution, companion, distribution)
│       ├── HUMAN/                    # Bộ 7 tài liệu giải thích phi kỹ thuật cho Chủ sản phẩm (01..07)
│       └── diagrams/                 # 15 file .mmd + ATLAS.md + 4 cặp PNG/SVG + build_diagrams.py
│
├── graphify-out/                     # Cache tri thức cấu trúc AST & chỉ mục registry (cấm sửa tay)
│   ├── GRAPH_REPORT.md               # Điểm vào ngắn cho AI
│   ├── graph.json                    # 264 nodes, 660 edges AST từ C#/Python (617 EXTRACTED, 43 INFERRED)
│   ├── registry-index.json           # Quan hệ kế hoạch 219 task / 109 req / 7 module (REGISTRY_DECLARED_NOT_CODE)
│   ├── manifest.json                 # SHA256 tất cả nguồn & output
│   ├── MEASUREMENTS.json             # Số đo kích thước baseline vs context packs
│   └── measurements-manifest.json    # Chứng chỉ toàn vẹn số đo
│
├── labs/policy-native/               # MẪU E02a THỰC TẾ ĐÃ CHẠY (Dữ liệu giả, C# + WPF + MSTest)
│   ├── global.json                   # Ghim .NET SDK 10.0.404
│   ├── README.md                     # Hướng dẫn chạy & giới hạn mẫu
│   ├── RESULTS.md                    # Bằng chứng 53/53 MSTest, 35/35 UI, hash binary, audit NuGet
│   ├── PolicyLab.Core/               # Contracts.cs, PolicyEvaluator.cs, ReadCoordinator.cs (net10.0)
│   ├── PolicyLab.Scenarios/          # ScenarioCatalog.cs (35 cases A01-A16/B01-B06), ScenarioRunner.cs
│   ├── PolicyLab.App/                # WPF UI (App.xaml/.cs, MainWindow.xaml/.cs, LabViewModel.cs)
│   └── PolicyLab.Tests/              # PolicyEvaluatorTests.cs, ReadCoordinatorTests.cs, ScenarioTests.cs
│
├── tasks/                            # Theo dõi công việc & thẻ task
│   ├── plan.md                       # Kế hoạch đã duyệt của mẫu native E02a
│   ├── todo.md                       # Checklist thực thi E02a (T00-T06, C1-C3; T05 kỹ thuật còn mở)
│   ├── E02a-USER-ACCEPTANCE.md       # Ghi nhận user đóng nghiệm thu trải nghiệm C3 (2026-11-15)
│   ├── README.md                     # Hướng dẫn điều phối & mẫu prompt giao việc
│   ├── dispatch.py                   # In thứ tự topo 219 task từ backlog.json
│   ├── validate_tasks.py             # Validator 219 task + 9 negative controls (cycle, deadlock, gate...)
│   ├── decisions/D-12-sleep-observation.md # Ghi chú quyết định D-12
│   └── phase-*.md                    # 16 file thẻ task sinh tự động từ backlog.json (a00, b00, c00, n00, p00..p60, r00, v00)
│
├── tests/bootstrap/                  # Fixture bootstrap cô lập (Stage B — đã PASS 2026-11-15)
│   ├── companion/                    # B00-01: Bootstrap.Tests.csproj + BootstrapTests.cs (.NET 10 MSTest)
│   └── desktop-body/GodotFixture/    # B00-02: project.godot, export_presets.cfg, Bootstrap.tscn, BootstrapVerify.gd
│
└── tools/verify/                     # Công cụ xác minh tự động
    └── companion.ps1                 # Supervisor PowerShell 5.1 (timeout <=120s, taskkill /T /F, TEMP artifacts)
```

---

## 4. Kiến trúc Code Mẫu `labs/policy-native/` (Thành phần C#/WPF Hiện có)

Thể hiện rõ sự tách lớp chuẩn đã chứng minh trong mẫu `E02a`:
1. **`PolicyLab.Core` (`net10.0`, không phụ thuộc UI/mạng/file):**
   - `Contracts.cs`: Định nghĩa enum `SourceKind`, `Visibility`, `Privacy`, `RegionKind`, `Outcome`, `Reason` và các immutable record `Geometry`, `Access`, `RegionDescriptor`, `SourceDescriptor`, `PermissionState`, `Decision`, `SafeRegion`, `AnalysisInput`, `Diagnostic`.
   - `PolicyEvaluator.cs`: Hàm thuần `Evaluate(...)` và `CanEnableControl(Access)` kiểm tra hợp lệ đầu vào, trạng thái hiển thị nhân vật/quan sát, riêng tư, `App.Read`, `Site.Read`, `SafetyHold`/`isRetry`, lọc vùng `Safe`/`Unknown`.
   - `ReadCoordinator.cs`: Điều phối tuần tự trên 1 owner thread, quản lý `attemptId`, `Source.Revision`, `Permissions.Revision`, chốt `holds`, đồng bộ kiểm tra lại lần cuối trong `Complete(...)` trước khi giao `AnalysisInput` cho receiver.
2. **`PolicyLab.Scenarios` (`net10.0`, tham chiếu `Core`):**
   - `ScenarioCatalog.cs`: Khai báo `35` kịch bản/biến thể giả (`A01–A16`, `B01–B06`).
   - `ScenarioRunner.cs`: `ScenarioSession` dùng chung cho cả Unit Test lẫn WPF App.
3. **`PolicyLab.App` (`net10.0-windows`, `UseWPF=true`, tham chiếu `Core` & `Scenarios`):**
   - `LabViewModel.cs` + `MainWindow.xaml/.cs`: Giao diện thử nghiệm tuân thủ `DESIGN.md`, phân biệt 5 trạng thái, tách geometry khỏi nội dung, tắt quan sát xóa payload cũ.
4. **`PolicyLab.Tests` (`net10.0`, MSTest 3.8.3):**
   - 3 bộ kiểm thử (`PolicyEvaluatorTests.cs`, `ReadCoordinatorTests.cs`, `ScenarioTests.cs`) đạt **53/53 PASS** ở cấu hình Release.

---

## 5. Cấu trúc Thư mục Dự kiến Cho Giai đoạn Sản phẩm (`PROPOSED — Chưa tạo`)

Khi các gate `P00`, `B00`, `R00/A00` và `P02` được cấp phép thực thi tuần tự, cây thư mục sản phẩm dự kiến mở rộng như sau *(chưa được phép tạo ở hiện tại)*:

```text
NYUA/ (Dự kiến tương lai — NOT_AUTHORIZED)
├── contracts/                        # Hợp đồng DTO & Timing dùng chung (vd: SceneTiming.cs, AvatarInteraction.cs, MediaEvidence.cs)
├── src/
│   ├── Host/
│   │   ├── Geometry/                 # P02-03: Host.Geometry.csproj, CoordinateMap.cs, MonitorSelection.cs
│   │   ├── Transport/                # P02-04..05: Host.Transport.csproj, RendererChannel.cs, ConnectionLifecycle.cs
│   │   ├── Policy/                   # P10-01/03/07: GrantEvaluator.cs, GrantState.cs, SafetyHold.cs, InputGate.cs, StopController.cs
│   │   ├── Perception/               # P10-02/03/04: VisibleSources.cs, SafeSnapshotBuilder.cs, ClipboardScope.cs
│   │   ├── ExternalAI/               # P10-05: ConsentRequest.cs (xem & duyệt chữ mỗi lần)
│   │   ├── Capabilities/             # P03-04: ModeAdvisor.cs (đề xuất Cơ bản/Nâng cao)
│   │   ├── LifeState/                # P20-04, P30-01..06: NeedsClock.cs, ElapsedReconciler.cs, ActivitySelector.cs, MemoryService.cs, RelationshipEngine.cs, NeglectClock.cs, MediaPreferences.cs, ModeTransition.cs, RomanceTransition.cs
│   │   ├── Tasks/                    # P40-03/04/05/07: LessonRecorder.cs, StepRunner.cs, ActionAdapter.cs, QueueScheduler.cs, AutonomousMedia.cs
│   │   ├── Companion/                # P40-06: MediaAttention.cs, AffectSmoother.cs
│   │   ├── Storage/                  # P30-04, P50-01..05: ProfileRepository.cs, SchemaVersion.cs, ContributionStore.cs, ProfileLifecycle.cs, ProfileExporter.cs, ProfileImporter.cs, ActionHistory.cs
│   │   └── Distribution/             # P50-07: UpdateController.cs
│   ├── Desktop.Wpf/                  # P40-01..05, P50-02..07, P10-05: Views XAML & ViewModels (Onboarding, SettingsShell, TrayController, Permissions, Modes, Lessons, Queue, Profiles, Export, Import, History, Update, ExternalAI)
│   ├── BrowserBridge/                # P10-02/06, P40-07: SourceEvidence.cs, FrameBinding.cs, MediaStatus.cs, Extension/manifest.json
│   └── LocalAI.Worker/               # Tiến trình / worker AI cục bộ tách biệt (đề xuất)
├── godot/
│   └── CompanionRenderer/            # P02-01..04, P20-02..05: project.godot, CompanionRenderer.csproj (Godot.NET.Sdk), export_presets.cfg, scenes/Probe.tscn, scripts/{ProbeBuild.gd, OverlayProbe.cs, HostChannel.cs, SurfaceWorld.cs, BodyMotion.cs, Gestures.cs, PropWorld.cs, Placement.cs}
├── art/character/                    # P20-01: model-sheet.png, manifest.json (128x128 đã duyệt)
├── packaging/                        # P50-06/08: Bộ cài Windows & quy trình gỡ cài đặt
├── tools/
│   ├── verify/                       # B00-03..07: policy.ps1, perception.ps1, life-state.ps1, task-execution.ps1, distribution.ps1
│   └── bench/                        # P03-02/03, P60-03: SceneBench.cs, CombinedBench.cs, SoakObserver.cs
├── tests/
│   ├── bootstrap/{policy,perception,life-state,task-execution,distribution}/ # B00-03..07
│   ├── Unit/                         # Unit tests từng service Host
│   ├── Integration/                  # Integration tests & P02/P10..P60 probes
│   ├── NativeUI/                     # Kịch bản kiểm thử native WPF/keyboard/DPI/install
│   ├── Fixtures/                     # WindowSurface.csproj (cửa sổ nền thử click-through), Scenes/manifest.json
│   └── acceptance/                   # P60-02: manifest.json
└── docs/                             # Bổ sung báo cáo khi chạy các pha: acceptance/, art/, checkpoints/, decisions/, experiments/, help/, licenses/INVENTORY.md, release/
```

---

## 6. Lệnh Kiểm chứng Tài liệu & Công cụ Đang Hoạt động

Chạy từ thư mục gốc repository (dùng Python 3.12 có `Pillow` và `graphifyy==0.9.97`):

```powershell
$py = 'C:/Users/phamp/AppData/Local/Programs/Python/Python312/python.exe'

# 1. Kiểm tra đồng bộ toàn bộ hồ sơ, liên kết, DAG, hình ảnh & negative controls
& $py docs/product/AI/validate_dossier.py
& $py tasks/validate_tasks.py --negative-controls
& $py docs/product/AI/check_dossier_controls.py

# 2. Kiểm tra độ mới của bản đồ Graphify & context packs (219 packs, <=160KB)
& $py docs/context/context_nav.py check
& $py docs/context/context_nav.py test
& $py docs/context/check_checkout.py HEAD

# 3. Sinh lại khi nguồn yêu cầu/backlog/bộ nhớ thay đổi
& $py docs/product/AI/sync_requirements.py
& $py docs/product/AI/sync_decisions.py
& $py docs/product/AI/sync_backlog.py
& $py docs/context/context_nav.py build
```

Kiểm thử cho mẫu `E02a` (`labs/policy-native/`) & Bootstrap (`B00-01` / `B00-02`):
- **E02a MSTest (`labs/policy-native/`):** `dotnet test ./PolicyLab.Tests/PolicyLab.Tests.csproj --configuration Release --artifacts-path <TEMP>/e02a-build`
- **Bootstrap `B00-01` (.NET 10):** `powershell -NoProfile -File "tools/verify/companion.ps1" -RunDir "<TEMP>/b00-01" -TimeoutSeconds 120 -Mode All`
- **Bootstrap `B00-02` (Godot 4.7.2 .NET headless):** Truyền `DOTNET_ROOT` & `PATH` tới `.NET 10` cục bộ rồi gọi `Godot_v4.7.2-stable_mono_win64_console.exe --headless --path tests/bootstrap/desktop-body/GodotFixture --script scripts/BootstrapVerify.gd --quit` (timeout `<= 120s`).
