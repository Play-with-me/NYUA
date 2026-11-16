# Tổng hợp Tất cả Task Cần Làm — Dự án NYUA

> **Trạng thái tổng thể tính đến 2026-11-16:**
> 1. **Tracker hiện hành của mẫu E02a (`tasks/todo.md`):** `T00–T04`, `T06`, `C1`, `C2` đã hoàn tất (`53/53 MSTest`, `35/35 UI case` dữ liệu giả). Người dùng đã đóng **nghiệm thu trải nghiệm C3** (`2026-11-15`), nhưng **checklist kỹ thuật của `T05` vẫn CÒN MỞ** (chuyển sang `P01-01`).
> 2. **Thực nghiệm Stage B Bootstrap (`2026-11-15`):** `B00-01` (.NET 10 test runner) và `B00-02` (Godot 4.7.2 .NET headless GDScript) đã tạo fixture cô lập và chạy **`PASS`** (`docs/experiments/bootstrap-companion.md`, `bootstrap-desktop-body.md`), nhưng `backlog.json` giữ nguyên trạng thái `DRAFT_NOT_AUTHORIZED` cho tới khi có lệnh đồng bộ chính thức sau `P00-01`.
> 3. **Backlog toàn sản phẩm (`docs/product/AI/backlog.json` — 219 tasks):** Toàn bộ **219 task** đang ở trạng thái `DRAFT_NOT_AUTHORIZED` / `BLOCKED_SCOPE_AUTHORIZATION` (bản kế hoạch rà soát, **chưa** được phép thực thi tự động).

---

## 1. Phần Việc Đang Mở Ngay ở Mẫu E02a (`tasks/todo.md` — `T05` / `P01-01`)

- [x] `T00–T04`, `T06`, `C1–C2`: Hoàn tất build/test/publish `PolicyLab.App.exe` (53/53 MSTest, 35/35 UI).
- [x] `C3` (Trải nghiệm người dùng): Người dùng xác nhận resize ổn, `Tab`/`Shift+Tab` nhìn rõ focus và không kẹt (`tasks/E02a-USER-ACCEPTANCE.md`, 2026-11-15).
- [ ] **`T05` (Phần kỹ thuật còn mở — gắn với `P01-01`):**
  - Kích hoạt đầy đủ mọi nút/điều khiển bằng bàn phím (`Enter` / `Space`).
  - Kiểm chứng trình đọc màn hình (`screen reader` / accessibility properties) trên các trạng thái.
  - Kiểm chứng mọi trạng thái nút vô hiệu hóa (`disabled`) có lý do rõ ràng và mọi thông báo lỗi, đảm bảo nội dung giống HTML/lệnh chỉ hiển thị dạng văn bản thuần.
  - Đo lường độc lập kích thước cửa sổ tối thiểu (và các mức DPI khác nhau).

---

## 2. Thống kê & Phân công Role cho 219 Task Sản phẩm (`backlog.json`)

### 2.1. Tổng hợp số lượng theo 16 nhóm Phase
| Nhóm | Số task | Loại công việc chính | Trạng thái trong registry |
|---|---:|---|---|
| `P00` | 4 | document_review | `DRAFT_NOT_AUTHORIZED` |
| `B00` | 7 | bootstrap | `DRAFT_NOT_AUTHORIZED` |
| `R00` | 18 | document_review | `DRAFT_NOT_AUTHORIZED` |
| `A00` | 18 | document_review | `DRAFT_NOT_AUTHORIZED` |
| `P01` | 1 | executable_work | `DRAFT_NOT_AUTHORIZED` |
| `P02` | 5 | executable_work | `DRAFT_NOT_AUTHORIZED` |
| `P03` | 4 | executable_work | `DRAFT_NOT_AUTHORIZED` |
| `P10` | 7 | executable_work | `DRAFT_NOT_AUTHORIZED` |
| `P20` | 5 | executable_work | `DRAFT_NOT_AUTHORIZED` |
| `P30` | 6 | executable_work | `DRAFT_NOT_AUTHORIZED` |
| `P40` | 7 | executable_work | `DRAFT_NOT_AUTHORIZED` |
| `P50` | 8 | executable_work | `DRAFT_NOT_AUTHORIZED` |
| `P60` | 5 | executable_work | `DRAFT_NOT_AUTHORIZED` |
| `N00` | 10 | executable_work | `DRAFT_NOT_AUTHORIZED` |
| `C00` | 5 | document_review | `DRAFT_NOT_AUTHORIZED` |
| `V00` | 109 | executable_work | `DRAFT_NOT_AUTHORIZED` |
| **TỔNG CỘNG** | **219** | **document_review (45) + bootstrap (7) + executable_work (167)** | **`DRAFT_NOT_AUTHORIZED` (219/219)** |

### 2.2. Ánh xạ Vai trò & Mô hình thực thi (`roles` trong `backlog.json`)
| Vai trò (`owner_role`) | Harness | Model | Effort |
|---|---|---|---|
| `research` | `agy` | `gemini-3.8-flash` | `—` |
| `memory` | `agy` | `gemini-3.8-flash` | `—` |
| `qa` | `agy` | `gemini-3.8-flash` | `—` |
| `ui-features` | `agy` | `gemini-4-hydrogen-low` | `—` |
| `core` | `codex` | `gpt-6.1-sol` | `low` |
| `bug` | `codex` | `gpt-6.1-sol` | `low` |
| `finalreview` | `codex` | `gpt-6.1-sol` | `low` |

---

## 3. Lộ trình Thực thi Theo Thứ tự Phụ thuộc (Topological Execution Roadmap)

Các task **không** chạy theo số thứ tự pha một cách máy móc mà tuân theo **đồ thị phụ thuộc (DAG)** để tránh deadlock và không bỏ sót gate:

```text
[Chặng 0: Khởi đầu & Rà baseline]
  P00-01 (Rà baseline, giải quyết mâu thuẫn phạm vi)
    ├──► B00-01 (Bootstrap companion .NET 10)        [Đã chạy PASS Chặng B]
    ├──► B00-02 (Bootstrap desktop-body Godot 4.7.2) [Đã chạy PASS Chặng B]
    ├──► B00-03..B00-07 (Bootstrap 5 module còn lại: perception, policy, life-state, task-execution, distribution)
    └──► R00-01..R00-18 (Lập đề cương D-01..D-18) ──► A00-01..A00-18 (Rà & mở gate đề cương)

[Chặng 1: Cổng P00 & Khép kỹ thuật E02a]
  P00-02 (Hợp đồng hybrid) + P00-03 (Quality budgets) + P00-04 (Giấy phép MIT/$0 & chi phí) ──► C00-01
  P01-01 (Khép kỹ thuật T05 E02a; C3 trải nghiệm đã OBTAINED)

[Chặng 2: Phép thử Công nghệ Lõi (Probes)]
  P02-01 (Godot Probe tối thiểu) ──► P02-02 (Overlay/Hit-region) ──► P02-03 (Multi-monitor/DPI) ──┐
                                  └─► P02-04 (IPC Named Pipe Host↔Godot) ─────────────────────────┴─► P02-05 (Fault/Reconnect)
  P03-01 (Sàng lọc model AI local) ──► P03-02 (Dataset cảnh an toàn) ──► P03-03 (Đo độ trễ <1s tải kết hợp) ──► P03-04 (Đề xuất 2 mức)
  P01-01 + P02-05 + P03-03 ──► C00-02 (Probes Checkpoint)

[Chặng 3: Lõi Production Theo Module]
  P50-01 (Storage/Transaction) ──► P50-02..05 (Profile, Export/Import crypto, History 30d)
  P10-01..07 (Grants, Visible source, SafetyHold, Win+V, External AI consent, Browser Bridge, Input/Stop gate)
  P20-01 [HUMAN GATE: Duyệt Model Sheet] ──► P20-02..05 (Bề mặt, Cử chỉ, Đồ ăn/Đồ vật, Multi-monitor)
  P30-01..06 (Needs/Sleep, Activity/Mood, Memory Provenance, Quan hệ sâu, Học gu, Mode/Romance)

[Chặng 4: Giao diện WPF, Bài học & Tích hợp]
  P40-01..07 (WPF Shell/Tray, UI Grants, Dạy/Quản lý Bài học, Embodied Execution, Hàng đợi, Xem phim cùng, Tự tìm nội dung)
  P50-06..08 (Bộ cài/Startup opt-in, Self-Update, Uninstall)
  P60-01 (Lát tích hợp dọc đầu tiên) ──► C00-03

[Chặng 5: Hồi quy, Soak 8h, Kiểm 109+10 Điều khoản & Phát hành]
  P60-02 (Hồi quy 2 mức & toàn bộ nghiệp vụ) ──► P60-03 (Soak 8 giờ & ma trận phần cứng)
  V00-001..V00-109 (Kiểm 109 điều khoản, trừ V00-039 deferred) + N00-01..N00-10 (Kiểm 10 NFR) ──► C00-04
  C00-04 + P60-03 + P50-07/08 ──► P60-04 [HUMAN GATE: Rà độc lập, Thương hiệu & Release Gate]
                              ──► P60-05 [HUMAN GATE: Chuẩn bị Công bố & Hỗ trợ] ──► C00-05 (Release Review Checkpoint)
```

### 4 Cổng Bắt buộc Người dùng Thật Xác nhận (`Human Gates`)
1. **`P01-01` (E02a):** Trải nghiệm demo `C3` đã `OBTAINED` ngày `2026-11-15`; **phần kỹ thuật `T05` còn mở**, không tự đóng `P01-01`.
2. **`P20-01` (Model Sheet 128×128):** `NOT_OBTAINED` — Người dùng phải duyệt mẫu hình ảnh/dáng/tai cáo/đuôi bạc/kẹp tóc/đồ vật trước khi làm hàng loạt animation.
3. **`P60-04` (Release Readiness Gate):** `NOT_OBTAINED` — Rà độc lập an ninh/giấy phép/thương hiệu NYUA trước công bố.
4. **`P60-05` (Public Release Approval):** `NOT_OBTAINED` — Người dùng duyệt bản cuối cùng cho phát hành công khai.

---

## 4. Danh sách Chi tiết Toàn bộ 219 Task Cần Làm

### P00 — Khởi đầu, Rà Baseline, Hợp đồng & Giấy phép (4 tasks)

| Mã Task | Tên công việc | Module | Loại / Role | Phụ thuộc (`deps`) | Yêu cầu / NFR | Kết quả mong đợi (`Output`) | File dự kiến (`proposed_files`) | Gate / Trạng thái |
|---|---|---|---|---|---|---|---|---|
| `P00-01` | Rà baseline và giải quyết mâu thuẫn phạm vi | `companion` | `document_review` / `research` | Không | — | Baseline/review log | `docs/product/AI/DECISIONS.md`, `docs/product/AI/requirements.json` | `DRAFT_NOT_AUTHORIZED` |
| `P00-02` | Rà ranh giới và hợp đồng hybrid | `companion` | `document_review` / `research` | `P00-01`, `A00-02`, `A00-03` | `SP09` | Module/contract baseline | `contracts/README.md`, `docs/product/AI/INTERFACES.md` | `DRAFT_NOT_AUTHORIZED` |
| `P00-03` | Chốt tiêu chuẩn chất lượng sau đo | `companion` | `document_review` / `research` | `P00-01`, `A00-04` | — | Quality budget proposal | `CONSTRAINTS.md`, `docs/product/AI/QA.md` | `DRAFT_NOT_AUTHORIZED` |
| `P00-04` | Lập danh mục giấy phép và chi phí | `distribution` | `document_review` / `research` | `P00-01`, `A00-13` | `SP06` | License/cost bill | `docs/licenses/INVENTORY.md`, `docs/product/AI/DECISIONS.md` | `DRAFT_NOT_AUTHORIZED` |

### B00 — Bootstrap Hạ tầng & Fixture Kiểm chứng theo Module (7 tasks)

| Mã Task | Tên công việc | Module | Loại / Role | Phụ thuộc (`deps`) | Yêu cầu / NFR | Kết quả mong đợi (`Output`) | File dự kiến (`proposed_files`) | Gate / Trạng thái |
|---|---|---|---|---|---|---|---|---|
| `B00-01` | Bootstrap verified tooling and fixtures: companion | `companion` | `bootstrap` / `research` | `P00-01` | — | Bộ chạy kiểm tra và dữ liệu giả tối thiểu cho companion; phiên bản/giấy phép và lệnh có bằng chứng | `docs/experiments/bootstrap-companion.md`, `tests/bootstrap/companion/Bootstrap.Tests.csproj`, `tests/bootstrap/companion/BootstrapTests.cs`, `tools/verify/companion.ps1` | `DRAFT_NOT_AUTHORIZED` *(Đã chạy thực nghiệm Chặng B: PASS ngày 2026-11-15; registry giữ DRAFT chờ đồng bộ)* |
| `B00-02` | Bootstrap verified tooling and fixtures: desktop-body | `desktop-body` | `bootstrap` / `research` | `P00-01` | — | Godot fixture bootstrap cô lập và lệnh batch có timeout; không phụ thuộc project renderer sản phẩm | `docs/experiments/bootstrap-desktop-body.md`, `tests/bootstrap/desktop-body/GodotFixture/project.godot`, `tests/bootstrap/desktop-body/GodotFixture/export_presets.cfg`, `tests/bootstrap/desktop-body/GodotFixture/scripts/BootstrapVerify.gd`, `tests/bootstrap/desktop-body/GodotFixture/scenes/Bootstrap.tscn` | `DRAFT_NOT_AUTHORIZED` *(Đã chạy thực nghiệm Chặng B: PASS ngày 2026-11-15; registry giữ DRAFT chờ đồng bộ)* |
| `B00-03` | Bootstrap verified tooling and fixtures: perception | `perception` | `bootstrap` / `research` | `P00-01` | — | Bộ chạy kiểm tra và dữ liệu giả tối thiểu cho perception; phiên bản/giấy phép và lệnh có bằng chứng | `docs/experiments/bootstrap-perception.md`, `tests/bootstrap/perception/Bootstrap.Tests.csproj`, `tests/bootstrap/perception/BootstrapTests.cs`, `tools/verify/perception.ps1` | `DRAFT_NOT_AUTHORIZED` |
| `B00-04` | Bootstrap verified tooling and fixtures: policy | `policy` | `bootstrap` / `research` | `P00-01` | — | Bộ chạy kiểm tra và dữ liệu giả tối thiểu cho policy; phiên bản/giấy phép và lệnh có bằng chứng | `docs/experiments/bootstrap-policy.md`, `tests/bootstrap/policy/Bootstrap.Tests.csproj`, `tests/bootstrap/policy/BootstrapTests.cs`, `tools/verify/policy.ps1` | `DRAFT_NOT_AUTHORIZED` |
| `B00-05` | Bootstrap verified tooling and fixtures: life-state | `life-state` | `bootstrap` / `research` | `P00-01` | — | Bộ chạy kiểm tra và dữ liệu giả tối thiểu cho life-state; phiên bản/giấy phép và lệnh có bằng chứng | `docs/experiments/bootstrap-life-state.md`, `tests/bootstrap/life-state/Bootstrap.Tests.csproj`, `tests/bootstrap/life-state/BootstrapTests.cs`, `tools/verify/life-state.ps1` | `DRAFT_NOT_AUTHORIZED` |
| `B00-06` | Bootstrap verified tooling and fixtures: task-execution | `task-execution` | `bootstrap` / `research` | `P00-01` | — | Bộ chạy kiểm tra và dữ liệu giả tối thiểu cho task-execution; phiên bản/giấy phép và lệnh có bằng chứng | `docs/experiments/bootstrap-task-execution.md`, `tests/bootstrap/task-execution/Bootstrap.Tests.csproj`, `tests/bootstrap/task-execution/BootstrapTests.cs`, `tools/verify/task-execution.ps1` | `DRAFT_NOT_AUTHORIZED` |
| `B00-07` | Bootstrap verified tooling and fixtures: distribution | `distribution` | `bootstrap` / `research` | `P00-01` | — | Bộ chạy kiểm tra và dữ liệu giả tối thiểu cho distribution; phiên bản/giấy phép và lệnh có bằng chứng | `docs/experiments/bootstrap-distribution.md`, `tests/bootstrap/distribution/Bootstrap.Tests.csproj`, `tests/bootstrap/distribution/BootstrapTests.cs`, `tools/verify/distribution.ps1` | `DRAFT_NOT_AUTHORIZED` |

### R00 — Nghiên cứu & Lập Đề cương Bằng chứng cho D-01..D-18 (18 tasks)

| Mã Task | Tên công việc | Module | Loại / Role | Phụ thuộc (`deps`) | Yêu cầu / NFR | Kết quả mong đợi (`Output`) | File dự kiến (`proposed_files`) | Gate / Trạng thái |
|---|---|---|---|---|---|---|---|---|
| `R00-02` | Resolve residual evidence: D-02 | `companion` | `document_review` / `research` | `P00-01` | `BH06`, `SP09` | Đề cương phép thử còn mở D-02 | `docs/experiments/D-02.md` | `DRAFT_NOT_AUTHORIZED` |
| `R00-03` | Resolve residual evidence: D-03 | `companion` | `document_review` / `research` | `P00-01` | — | Đề cương phép thử còn mở D-03 | `docs/experiments/D-03.md` | `DRAFT_NOT_AUTHORIZED` |
| `R00-04` | Resolve residual evidence: D-04 | `companion` | `document_review` / `research` | `P00-01` | — | Đề cương phép thử còn mở D-04 | `docs/experiments/D-04.md` | `DRAFT_NOT_AUTHORIZED` |
| `R00-13` | Resolve residual evidence: D-13 | `companion` | `document_review` / `research` | `P00-01` | — | Đề cương phép thử còn mở D-13 | `docs/experiments/D-13.md` | `DRAFT_NOT_AUTHORIZED` |
| `R00-01` | Resolve residual evidence: D-01 | `companion` | `document_review` / `research` | `P00-01` | — | Đề cương phép thử còn mở D-01 | `docs/experiments/D-01.md` | `DRAFT_NOT_AUTHORIZED` |
| `R00-10` | Resolve residual evidence: D-10 | `companion` | `document_review` / `research` | `P00-01` | `BH06`, `CD01` | Đề cương phép thử còn mở D-10 | `docs/experiments/D-10.md` | `DRAFT_NOT_AUTHORIZED` |
| `R00-15` | Resolve residual evidence: D-15 | `companion` | `document_review` / `research` | `P00-01` | — | Đề cương phép thử còn mở D-15 | `docs/experiments/D-15.md` | `DRAFT_NOT_AUTHORIZED` |
| `R00-16` | Resolve residual evidence: D-16 | `companion` | `document_review` / `research` | `P00-01` | `AI01`, `XP05` | Đề cương phép thử còn mở D-16 | `docs/experiments/D-16.md` | `DRAFT_NOT_AUTHORIZED` |
| `R00-07` | Resolve residual evidence: D-07 | `companion` | `document_review` / `research` | `P00-01` | — | Đề cương phép thử còn mở D-07 | `docs/experiments/D-07.md` | `DRAFT_NOT_AUTHORIZED` |
| `R00-08` | Resolve residual evidence: D-08 | `companion` | `document_review` / `research` | `P00-01` | — | Đề cương phép thử còn mở D-08 | `docs/experiments/D-08.md` | `DRAFT_NOT_AUTHORIZED` |
| `R00-18` | Resolve residual evidence: D-18 | `companion` | `document_review` / `research` | `P00-01` | `AI02` | Đề cương phép thử còn mở D-18 | `docs/experiments/D-18.md` | `DRAFT_NOT_AUTHORIZED` |
| `R00-05` | Resolve residual evidence: D-05 | `companion` | `document_review` / `research` | `P00-01` | `NV11`, `QH05` | Đề cương phép thử còn mở D-05 | `docs/experiments/D-05.md` | `DRAFT_NOT_AUTHORIZED` |
| `R00-11` | Resolve residual evidence: D-11 | `companion` | `document_review` / `research` | `P00-01` | `XP08` | Đề cương phép thử còn mở D-11 | `docs/experiments/D-11.md` | `DRAFT_NOT_AUTHORIZED` |
| `R00-14` | Resolve residual evidence: D-14 | `companion` | `document_review` / `research` | `P00-01` | `NV01`, `NV02`, `SH04` | Đề cương phép thử còn mở D-14 | `docs/experiments/D-14.md` | `DRAFT_NOT_AUTHORIZED` |
| `R00-12` | Resolve residual evidence: D-12 | `companion` | `document_review` / `research` | `P00-01` | `QD04`, `SH01` | Đề cương phép thử còn mở D-12 | `docs/experiments/D-12.md` | `DRAFT_NOT_AUTHORIZED` |
| `R00-17` | Resolve residual evidence: D-17 | `companion` | `document_review` / `research` | `P00-01` | `BH02`, `BH06` | Đề cương phép thử còn mở D-17 | `docs/experiments/D-17.md` | `DRAFT_NOT_AUTHORIZED` |
| `R00-06` | Resolve residual evidence: D-06 | `companion` | `document_review` / `research` | `P00-01` | `XP07` | Đề cương phép thử còn mở D-06 | `docs/experiments/D-06.md` | `DRAFT_NOT_AUTHORIZED` |
| `R00-09` | Resolve residual evidence: D-09 | `companion` | `document_review` / `research` | `P00-01` | `SL01` | Đề cương phép thử còn mở D-09 | `docs/experiments/D-09.md` | `DRAFT_NOT_AUTHORIZED` |

### A00 — Rà soát & Mở Gate Đề cương cho D-01..D-18 (18 tasks)

| Mã Task | Tên công việc | Module | Loại / Role | Phụ thuộc (`deps`) | Yêu cầu / NFR | Kết quả mong đợi (`Output`) | File dự kiến (`proposed_files`) | Gate / Trạng thái |
|---|---|---|---|---|---|---|---|---|
| `A00-02` | Rà đề cương và phạm vi phép thử D-02 | `companion` | `document_review` / `finalreview` | `R00-02` | `BH06`, `SP09` | Gate đề cương D-02; không phải nghiệm thu kết quả | `docs/decisions/D-02-resolution.md` | `DRAFT_NOT_AUTHORIZED` |
| `A00-03` | Rà đề cương và phạm vi phép thử D-03 | `companion` | `document_review` / `finalreview` | `R00-03` | — | Gate đề cương D-03; không phải nghiệm thu kết quả | `docs/decisions/D-03-resolution.md` | `DRAFT_NOT_AUTHORIZED` |
| `A00-04` | Rà đề cương và phạm vi phép thử D-04 | `companion` | `document_review` / `finalreview` | `R00-04` | — | Gate đề cương D-04; không phải nghiệm thu kết quả | `docs/decisions/D-04-resolution.md` | `DRAFT_NOT_AUTHORIZED` |
| `A00-13` | Rà đề cương và phạm vi phép thử D-13 | `companion` | `document_review` / `finalreview` | `R00-13` | — | Gate đề cương D-13; không phải nghiệm thu kết quả | `docs/decisions/D-13-resolution.md` | `DRAFT_NOT_AUTHORIZED` |
| `A00-01` | Rà đề cương và phạm vi phép thử D-01 | `companion` | `document_review` / `finalreview` | `R00-01` | — | Gate đề cương D-01; không phải nghiệm thu kết quả | `docs/decisions/D-01-resolution.md` | `DRAFT_NOT_AUTHORIZED` |
| `A00-10` | Rà đề cương và phạm vi phép thử D-10 | `companion` | `document_review` / `finalreview` | `R00-10` | `BH06`, `CD01` | Gate đề cương D-10; không phải nghiệm thu kết quả | `docs/decisions/D-10-resolution.md` | `DRAFT_NOT_AUTHORIZED` |
| `A00-15` | Rà đề cương và phạm vi phép thử D-15 | `companion` | `document_review` / `finalreview` | `R00-15` | — | Gate đề cương D-15; không phải nghiệm thu kết quả | `docs/decisions/D-15-resolution.md` | `DRAFT_NOT_AUTHORIZED` |
| `A00-16` | Rà đề cương và phạm vi phép thử D-16 | `companion` | `document_review` / `finalreview` | `R00-16` | `AI01`, `XP05` | Gate đề cương D-16; không phải nghiệm thu kết quả | `docs/decisions/D-16-resolution.md` | `DRAFT_NOT_AUTHORIZED` |
| `A00-07` | Rà đề cương và phạm vi phép thử D-07 | `companion` | `document_review` / `finalreview` | `R00-07` | — | Gate đề cương D-07; không phải nghiệm thu kết quả | `docs/decisions/D-07-resolution.md` | `DRAFT_NOT_AUTHORIZED` |
| `A00-08` | Rà đề cương và phạm vi phép thử D-08 | `companion` | `document_review` / `finalreview` | `R00-08` | — | Gate đề cương D-08; không phải nghiệm thu kết quả | `docs/decisions/D-08-resolution.md` | `DRAFT_NOT_AUTHORIZED` |
| `A00-18` | Rà đề cương và phạm vi phép thử D-18 | `companion` | `document_review` / `finalreview` | `R00-18` | `AI02` | Gate đề cương D-18; không phải nghiệm thu kết quả | `docs/decisions/D-18-resolution.md` | `DRAFT_NOT_AUTHORIZED` |
| `A00-05` | Rà đề cương và phạm vi phép thử D-05 | `companion` | `document_review` / `finalreview` | `R00-05` | `NV11`, `QH05` | Gate đề cương D-05; không phải nghiệm thu kết quả | `docs/decisions/D-05-resolution.md` | `DRAFT_NOT_AUTHORIZED` |
| `A00-11` | Rà đề cương và phạm vi phép thử D-11 | `companion` | `document_review` / `finalreview` | `R00-11` | `XP08` | Gate đề cương D-11; không phải nghiệm thu kết quả | `docs/decisions/D-11-resolution.md` | `DRAFT_NOT_AUTHORIZED` |
| `A00-14` | Rà đề cương và phạm vi phép thử D-14 | `companion` | `document_review` / `finalreview` | `R00-14` | `NV01`, `NV02`, `SH04` | Gate đề cương D-14; không phải nghiệm thu kết quả | `docs/decisions/D-14-resolution.md` | `DRAFT_NOT_AUTHORIZED` |
| `A00-12` | Rà đề cương và phạm vi phép thử D-12 | `companion` | `document_review` / `finalreview` | `R00-12` | `QD04`, `SH01` | Gate đề cương D-12; không phải nghiệm thu kết quả | `docs/decisions/D-12-resolution.md` | `DRAFT_NOT_AUTHORIZED` |
| `A00-17` | Rà đề cương và phạm vi phép thử D-17 | `companion` | `document_review` / `finalreview` | `R00-17` | `BH02`, `BH06` | Gate đề cương D-17; không phải nghiệm thu kết quả | `docs/decisions/D-17-resolution.md` | `DRAFT_NOT_AUTHORIZED` |
| `A00-06` | Rà đề cương và phạm vi phép thử D-06 | `companion` | `document_review` / `finalreview` | `R00-06` | `XP07` | Gate đề cương D-06; không phải nghiệm thu kết quả | `docs/decisions/D-06-resolution.md` | `DRAFT_NOT_AUTHORIZED` |
| `A00-09` | Rà đề cương và phạm vi phép thử D-09 | `companion` | `document_review` / `finalreview` | `R00-09` | `SL01` | Gate đề cương D-09; không phải nghiệm thu kết quả | `docs/decisions/D-09-resolution.md` | `DRAFT_NOT_AUTHORIZED` |

### P01 — Khép Kiểm tra Kỹ thuật Còn mở của Mẫu E02a (1 task)

| Mã Task | Tên công việc | Module | Loại / Role | Phụ thuộc (`deps`) | Yêu cầu / NFR | Kết quả mong đợi (`Output`) | File dự kiến (`proposed_files`) | Gate / Trạng thái |
|---|---|---|---|---|---|---|---|---|
| `P01-01` | Khép kiểm tra UI còn mở của E02a | `policy` | `executable_work` / `qa` | `P00-01`, `B00-04` | — | E02a technical-closure checklist/evidence, separated from user-obtained demo experience acceptance | `labs/policy-native/RESULTS.md`, `tasks/todo.md` | **HUMAN GATE: `OBTAINED`** *(C3 trải nghiệm `OBTAINED` 2026-11-15; T05 kỹ thuật còn mở)* |

### P02 — Phép thử Tích hợp Godot Engine – Windows Host (5 tasks)

| Mã Task | Tên công việc | Module | Loại / Role | Phụ thuộc (`deps`) | Yêu cầu / NFR | Kết quả mong đợi (`Output`) | File dự kiến (`proposed_files`) | Gate / Trạng thái |
|---|---|---|---|---|---|---|---|---|
| `P02-01` | Chọn và dựng renderer thử tối thiểu | `desktop-body` | `executable_work` / `core` | `P00-02`, `P00-04`, `B00-02`, `A00-01` | — | Pinned Godot probe | `godot/CompanionRenderer/project.godot`, `godot/CompanionRenderer/CompanionRenderer.csproj`, `godot/CompanionRenderer/scenes/Probe.tscn`, `godot/CompanionRenderer/export_presets.cfg`, `godot/CompanionRenderer/scripts/ProbeBuild.gd` | `DRAFT_NOT_AUTHORIZED` |
| `P02-02` | Thử transparent overlay và hit regions | `desktop-body` | `executable_work` / `core` | `P02-01`, `B00-01`, `B00-02`, `A00-01` | — | Overlay/hit test report | `godot/CompanionRenderer/scripts/OverlayProbe.cs`, `tests/Fixtures/WindowSurface.csproj`, `tests/Fixtures/WindowSurface.cs`, `docs/experiments/overlay.md` | `DRAFT_NOT_AUTHORIZED` |
| `P02-03` | Thử tọa độ qua monitor và DPI | `desktop-body` | `executable_work` / `core` | `P02-02`, `B00-01`, `B00-02`, `A00-01` | — | Coordinate contract/tests | `src/Host/Geometry/Host.Geometry.csproj`, `src/Host/Geometry/CoordinateMap.cs`, `tests/Integration/CoordinateMap.Tests.csproj`, `tests/Integration/CoordinateMapTests.cs`, `docs/experiments/coordinates.md` | `DRAFT_NOT_AUTHORIZED` |
| `P02-04` | Thử kết nối typed host-renderer | `companion` | `executable_work` / `core` | `P02-01`, `P00-02`, `B00-01`, `A00-03` | — | IPC probe | `src/Host/Transport/Host.Transport.csproj`, `src/Host/Transport/RendererChannel.cs`, `godot/CompanionRenderer/scripts/HostChannel.cs`, `tests/Integration/RendererChannel.Tests.csproj`, `tests/Integration/RendererChannelTests.cs` | `DRAFT_NOT_AUTHORIZED` |
| `P02-05` | Thử mất kết nối và khôi phục an toàn | `companion` | `executable_work` / `core` | `P02-04`, `P02-03`, `B00-01`, `A00-02`, `A00-10` | `SP09` | Failure state report | `src/Host/Transport/ConnectionLifecycle.cs`, `tests/Integration/ConnectionLifecycle.Tests.csproj`, `tests/Integration/ConnectionLifecycleTests.cs`, `docs/experiments/disconnect.md` | `DRAFT_NOT_AUTHORIZED` |

### P03 — Phép thử AI Cục bộ, Benchmark & Hai Mức (4 tasks)

| Mã Task | Tên công việc | Module | Loại / Role | Phụ thuộc (`deps`) | Yêu cầu / NFR | Kết quả mong đợi (`Output`) | File dự kiến (`proposed_files`) | Gate / Trạng thái |
|---|---|---|---|---|---|---|---|---|
| `P03-01` | Sàng lọc model/runtime local có quyền phân phối | `perception` | `executable_work` / `research` | `P00-04`, `B00-03`, `A00-04` | `AI01` | Candidate/license matrix | `docs/experiments/model-candidates.md`, `docs/licenses/INVENTORY.md` | `DRAFT_NOT_AUTHORIZED` |
| `P03-02` | Dựng benchmark dữ liệu cảnh an toàn | `perception` | `executable_work` / `core` | `P03-01`, `P01-01`, `B00-03`, `A00-04` | `AI03` | Dataset manifest/runner | `tests/Fixtures/Scenes/manifest.json`, `tools/bench/SceneBench.cs`, `docs/experiments/local-ai.md` | `DRAFT_NOT_AUTHORIZED` |
| `P03-03` | Đo phản ứng toàn luồng dưới tải kết hợp | `perception` | `executable_work` / `core` | `P03-02`, `P02-04`, `B00-03`, `A00-04` | `XP02` | Latency/quality report | `tools/bench/CombinedBench.cs`, `contracts/SceneTiming.cs`, `docs/experiments/local-ai.md` | `DRAFT_NOT_AUTHORIZED` |
| `P03-04` | Đề xuất hai mức và luồng gói nâng cao | `companion` | `executable_work` / `core` | `P03-03`, `P00-03`, `B00-01`, `A00-04` | `MC01`, `MC02`, `MC04` | Capability recommendation/pack states | `src/Host/Capabilities/ModeAdvisor.cs`, `src/Desktop.Wpf/ModesView.xaml`, `tests/Unit/ModeAdvisorTests.cs` | `DRAFT_NOT_AUTHORIZED` |

### P10 — Triển khai Policy, Nguồn thật, SafetyHold, Win+V, Browser Bridge & Input Gate (7 tasks)

| Mã Task | Tên công việc | Module | Loại / Role | Phụ thuộc (`deps`) | Yêu cầu / NFR | Kết quả mong đợi (`Output`) | File dự kiến (`proposed_files`) | Gate / Trạng thái |
|---|---|---|---|---|---|---|---|---|
| `P10-01` | Triển khai grants mặc định tắt và read/control | `policy` | `executable_work` / `core` | `P00-02`, `P01-01`, `B00-04` | `QD01` | Production grant evaluator | `src/Host/Policy/GrantEvaluator.cs`, `src/Host/Policy/GrantState.cs`, `tests/Unit/GrantEvaluatorTests.cs` | `DRAFT_NOT_AUTHORIZED` |
| `P10-02` | Nhận dạng nguồn và vùng đang hiển thị | `perception` | `executable_work` / `core` | `P10-01`, `P02-03`, `B00-03`, `A00-15`, `A00-16` | `QD04`, `QD06` | Visible source adapter | `src/Host/Perception/VisibleSources.cs`, `src/BrowserBridge/SourceEvidence.cs`, `tests/Integration/VisibleSourceTests.cs` | `DRAFT_NOT_AUTHORIZED` |
| `P10-03` | Lọc sensitive/private và retry hold trên nguồn thật | `policy` | `executable_work` / `core` | `P10-02`, `B00-04`, `A00-15` | `QD05`, `QD15`, `SH01` | Safe snapshot boundary | `src/Host/Policy/SafetyHold.cs`, `src/Host/Perception/SafeSnapshotBuilder.cs`, `tests/Integration/SafeSnapshotTests.cs` | `DRAFT_NOT_AUTHORIZED` |
| `P10-04` | Kiểm chứng clipboard history đúng Win+V scope | `perception` | `executable_work` / `core` | `P10-03`, `B00-03`, `A00-15` | `QD08` | Clipboard adapter/proof | `src/Host/Perception/ClipboardScope.cs`, `tests/Integration/ClipboardScopeTests.cs`, `docs/experiments/clipboard.md` | `DRAFT_NOT_AUTHORIZED` |
| `P10-05` | Luồng AI ngoài có preview và consent mỗi lần | `policy` | `executable_work` / `core` | `P10-03`, `P50-01`, `B00-04`, `A00-07`, `A00-18` | `AI02` | Explicit text-only request | `src/Host/ExternalAI/ConsentRequest.cs`, `src/Desktop.Wpf/ExternalAIView.xaml`, `tests/Integration/ExternalAIConsentTests.cs` | `DRAFT_NOT_AUTHORIZED` |
| `P10-06` | Bridge trình duyệt và ngoại lệ khung video | `perception` | `executable_work` / `core` | `P10-03`, `P00-04`, `B00-03`, `A00-03`, `A00-15` | `QD12`, `QD13`, `QD14` | Optional extension/frame binding | `src/BrowserBridge/Extension/manifest.json`, `src/BrowserBridge/FrameBinding.cs`, `tests/Integration/FrameBindingTests.cs` | `DRAFT_NOT_AUTHORIZED` |
| `P10-07` | Input arbitration và các nút dừng | `policy` | `executable_work` / `core` | `P10-01`, `P02-05`, `B00-04`, `A00-05`, `A00-11` | `DK01`, `DK02`, `DK03`, `DK04`, `XP08` | Stop/input gate | `src/Host/Policy/InputGate.cs`, `src/Host/Policy/StopController.cs`, `tests/Integration/InputGateTests.cs` | `DRAFT_NOT_AUTHORIZED` |

### P20 — Triển khai Model Sheet, Thân thể Godot, Cử chỉ, Đồ ăn/Đồ vật & Multi-Monitor (5 tasks)

| Mã Task | Tên công việc | Module | Loại / Role | Phụ thuộc (`deps`) | Yêu cầu / NFR | Kết quả mong đợi (`Output`) | File dự kiến (`proposed_files`) | Gate / Trạng thái |
|---|---|---|---|---|---|---|---|---|
| `P20-01` | Duyệt model sheet nhân vật gốc | `desktop-body` | `executable_work` / `ui-features` | `P00-04`, `B00-02`, `A00-14` | `NV01`, `NV02`, `NV03`, `NV04` | Approved art reference | `art/character/model-sheet.png`, `art/character/manifest.json`, `docs/art/approval.md` | **HUMAN GATE: `NOT_OBTAINED`** |
| `P20-02` | Di chuyển và bề mặt cửa sổ | `desktop-body` | `executable_work` / `ui-features` | `P20-01`, `P02-03`, `P02-05`, `B00-02`, `A00-01` | `NV05`, `NV07`, `QD10` | Locomotion/surface model | `godot/CompanionRenderer/scripts/SurfaceWorld.cs`, `godot/CompanionRenderer/scripts/BodyMotion.cs`, `tests/Integration/SurfaceWorldTests.cs` | `DRAFT_NOT_AUTHORIZED` |
| `P20-03` | Pet/lift/throw và chuyển vị trí an toàn | `desktop-body` | `executable_work` / `ui-features` | `P20-02`, `P30-02`, `B00-02`, `A00-05` | `NV09`, `NV11`, `SH05` | Gesture recognizer | `godot/CompanionRenderer/scripts/Gestures.cs`, `contracts/AvatarInteraction.cs`, `tests/Integration/GestureTests.cs` | `DRAFT_NOT_AUTHORIZED` |
| `P20-04` | Foodtray, đồ vật và animatedcleanup | `desktop-body` | `executable_work` / `ui-features` | `P20-02`, `P30-01`, `B00-02`, `A00-14` | `SH04`, `SH07`, `SH08`, `XP09` | Food/prop interaction | `godot/CompanionRenderer/scripts/PropWorld.cs`, `src/Host/LifeState/FoodInteraction.cs`, `tests/Integration/PropWorldTests.cs` | `DRAFT_NOT_AUTHORIZED` |
| `P20-05` | Placement nhiều màn hình và fullscreen | `desktop-body` | `executable_work` / `ui-features` | `P20-02`, `P02-02`, `B00-02`, `A00-01` | `NV08` | Placement/support matrix | `src/Host/Geometry/MonitorSelection.cs`, `godot/CompanionRenderer/scripts/Placement.cs`, `tests/Integration/PlacementTests.cs` | `DRAFT_NOT_AUTHORIZED` |

### P30 — Triển khai Đời sống, Ký ức, Quan hệ sâu, Học gu & Phát triển Tính cách (6 tasks)

| Mã Task | Tên công việc | Module | Loại / Role | Phụ thuộc (`deps`) | Yêu cầu / NFR | Kết quả mong đợi (`Output`) | File dự kiến (`proposed_files`) | Gate / Trạng thái |
|---|---|---|---|---|---|---|---|---|
| `P30-01` | Needs/sleep/rest và elapsed reconciliation | `life-state` | `executable_work` / `core` | `P00-02`, `P50-01`, `B00-05`, `A00-05`, `A00-12` | `QD04`, `SH01`, `SH02`, `SH03` | Basic life clock | `src/Host/LifeState/NeedsClock.cs`, `src/Host/LifeState/ElapsedReconciler.cs`, `tests/Unit/NeedsClockTests.cs` | `DRAFT_NOT_AUTHORIZED` |
| `P30-02` | Lựa chọn hoạt động, mood và attention limits | `life-state` | `executable_work` / `core` | `P30-01`, `B00-05`, `A00-05` | `SH06`, `SP01`, `SP08`, `XP03`, `XP10` | Activity selection/state | `src/Host/LifeState/ActivitySelector.cs`, `src/Host/LifeState/AttentionClock.cs`, `tests/Unit/ActivitySelectorTests.cs` | `DRAFT_NOT_AUTHORIZED` |
| `P30-04` | Memory provenance, pin/fade/edit/delete | `life-state` | `executable_work` / `core` | `P50-01`, `P10-01`, `B00-05`, `A00-08` | `KN01`, `KN02`, `QD09`, `QD11` | Memory lifecycle | `src/Host/LifeState/MemoryService.cs`, `src/Host/Storage/ContributionStore.cs`, `tests/Integration/MemoryTests.cs` | `DRAFT_NOT_AUTHORIZED` |
| `P30-03` | Quan hệ sâu, neglect và làm lành | `life-state` | `executable_work` / `core` | `P30-02`, `P30-04`, `B00-05`, `A00-05` | `QH01`, `QH03`, `QH04`, `QH05`, `QH06`, `QH07` | Relationship state machine | `src/Host/LifeState/RelationshipEngine.cs`, `src/Host/LifeState/NeglectClock.cs`, `tests/Unit/RelationshipTests.cs` | `DRAFT_NOT_AUTHORIZED` |
| `P30-05` | Học gu từ user media evidence | `life-state` | `executable_work` / `core` | `P30-04`, `P10-02`, `B00-05`, `A00-16` | `XP11`, `XP12`, `XP13`, `XP14` | Media preference inference | `src/Host/LifeState/MediaPreferences.cs`, `contracts/MediaEvidence.cs`, `tests/Unit/MediaPreferenceTests.cs` | `DRAFT_NOT_AUTHORIZED` |
| `P30-06` | Mode preservation, personality và romance opt-in | `life-state` | `executable_work` / `core` | `P30-03`, `P03-04`, `B00-05`, `A00-05` | `MC03`, `QH02`, `SP07` | Advanced state transitions | `src/Host/LifeState/ModeTransition.cs`, `src/Host/LifeState/RomanceTransition.cs`, `tests/Integration/AdvancedStateTests.cs` | `DRAFT_NOT_AUTHORIZED` |

### P40 — Triển khai Giao diện WPF, Bài học Thao tác, Hàng đợi & Giải trí (7 tasks)

| Mã Task | Tên công việc | Module | Loại / Role | Phụ thuộc (`deps`) | Yêu cầu / NFR | Kết quả mong đợi (`Output`) | File dự kiến (`proposed_files`) | Gate / Trạng thái |
|---|---|---|---|---|---|---|---|---|
| `P40-01` | Onboarding/tray/settings shell | `companion` | `executable_work` / `ui-features` | `P02-04`, `P50-01`, `B00-01`, `A00-14` | `NV06`, `SP04` | Native management UI | `src/Desktop.Wpf/OnboardingView.xaml`, `src/Desktop.Wpf/SettingsShell.xaml`, `src/Desktop.Wpf/TrayController.cs` | `DRAFT_NOT_AUTHORIZED` |
| `P40-02` | UI grants và chosenbrowser | `companion` | `executable_work` / `ui-features` | `P40-01`, `P10-01`, `B00-01` | `QD02`, `XP16` | App/site permission UI | `src/Desktop.Wpf/PermissionsView.xaml`, `src/Desktop.Wpf/PermissionsViewModel.cs`, `tests/NativeUI/PermissionFlows.md` | `DRAFT_NOT_AUTHORIZED` |
| `P40-03` | Dạy/review/manage lesson và searchparameters | `task-execution` | `executable_work` / `ui-features` | `P10-03`, `P40-01`, `P50-01`, `B00-06`, `A00-17` | `BH01`, `BH02`, `BH11`, `BH12` | Lesson definition workflow | `src/Host/Tasks/LessonRecorder.cs`, `src/Desktop.Wpf/LessonReview.xaml`, `tests/Integration/LessonRecordingTests.cs` | `DRAFT_NOT_AUTHORIZED` |
| `P40-04` | Embodied execution và postconditionverify | `task-execution` | `executable_work` / `core` | `P40-03`, `P10-07`, `P20-02`, `B00-06`, `A00-03`, `A00-05` | `BH03`, `BH04`, `BH05`, `NV10` | Verified step runner | `src/Host/Tasks/StepRunner.cs`, `src/Host/Tasks/ActionAdapter.cs`, `tests/Integration/StepRunnerTests.cs` | `DRAFT_NOT_AUTHORIZED` |
| `P40-05` | Hàng đợi, priority và stop lifecycle | `task-execution` | `executable_work` / `core` | `P40-04`, `P30-03`, `B00-06`, `A00-02`, `A00-10`, `A00-17` | `BH02`, `BH06`, `BH07`, `BH08`, `BH09`, `BH10`, `CD01`, `SP09` | Queue state machine | `src/Host/Tasks/QueueScheduler.cs`, `src/Desktop.Wpf/QueueView.xaml`, `tests/Integration/QueueTests.cs` | `DRAFT_NOT_AUTHORIZED` |
| `P40-06` | Xem cùng và phản ứng cảm xúc | `companion` | `executable_work` / `ui-features` | `P03-03`, `P10-03`, `P30-02`, `P20-04`, `B00-01`, `A00-04`, `A00-12` | `XP01`, `XP04` | Attended media response | `src/Host/Companion/MediaAttention.cs`, `src/Host/Companion/AffectSmoother.cs`, `tests/Integration/MediaReactionTests.cs` | `DRAFT_NOT_AUTHORIZED` |
| `P40-07` | Tự tìm/mở nội dung trong quyền | `task-execution` | `executable_work` / `core` | `P40-05`, `P40-06`, `P10-06`, `B00-06`, `A00-06`, `A00-11`, `A00-16` | `AI01`, `XP05`, `XP06`, `XP07`, `XP08`, `XP15` | Bounded autonomous media | `src/Host/Tasks/AutonomousMedia.cs`, `src/BrowserBridge/MediaStatus.cs`, `tests/Integration/AutonomousMediaTests.cs` | `DRAFT_NOT_AUTHORIZED` |

### P50 — Triển khai Lưu trữ, Hồ sơ, Sao lưu Mã hóa, Lịch sử 30 ngày, Cài đặt/Cập nhật/Gỡ (8 tasks)

| Mã Task | Tên công việc | Module | Loại / Role | Phụ thuộc (`deps`) | Yêu cầu / NFR | Kết quả mong đợi (`Output`) | File dự kiến (`proposed_files`) | Gate / Trạng thái |
|---|---|---|---|---|---|---|---|---|
| `P50-01` | Chốt storage và transaction/persistence | `distribution` | `executable_work` / `core` | `P00-02`, `P00-04`, `B00-07`, `A00-07`, `A00-08`, `A00-10` | `CD01` | Versioned local storage | `src/Host/Storage/ProfileRepository.cs`, `src/Host/Storage/SchemaVersion.cs`, `tests/Integration/StorageTests.cs` | `DRAFT_NOT_AUTHORIZED` |
| `P50-02` | Profile import/switch/reset semantics | `distribution` | `executable_work` / `core` | `P50-01`, `P10-01`, `B00-07`, `A00-10` | `HS01`, `HS02`, `HS03`, `QD03` | Profile lifecycle | `src/Host/Storage/ProfileLifecycle.cs`, `src/Desktop.Wpf/ProfilesView.xaml`, `tests/Integration/ProfileLifecycleTests.cs` | `DRAFT_NOT_AUTHORIZED` |
| `P50-03` | Manualexport password/recovery format | `distribution` | `executable_work` / `core` | `P50-01`, `P00-04`, `B00-07`, `A00-07`, `A00-09` | `SL01`, `SL02` | Reviewed encrypted archive export | `src/Host/Storage/ProfileExporter.cs`, `src/Desktop.Wpf/ExportView.xaml`, `tests/Integration/ExportTests.cs` | `DRAFT_NOT_AUTHORIZED` |
| `P50-04` | Validate/import archive thành hồ sơ riêng | `distribution` | `executable_work` / `core` | `P50-03`, `P50-02`, `B00-07`, `A00-07`, `A00-09` | — | Transactional import | `src/Host/Storage/ProfileImporter.cs`, `src/Desktop.Wpf/ImportView.xaml`, `tests/Integration/ImportTests.cs` | `DRAFT_NOT_AUTHORIZED` |
| `P50-05` | Local actionhistory và expiry30days | `distribution` | `executable_work` / `core` | `P50-01`, `B00-07` | `BH13` | Sanitized history pipeline | `src/Host/Storage/ActionHistory.cs`, `src/Desktop.Wpf/HistoryView.xaml`, `tests/Integration/HistoryTests.cs` | `DRAFT_NOT_AUTHORIZED` |
| `P50-06` | Bộ cài và startup opt-in | `distribution` | `executable_work` / `core` | `P00-04`, `P40-01`, `P20-05`, `B00-07`, `A00-13` | `CD01`, `SP03` | Native install package | `packaging/README.md`, `packaging/installer-project`, `tests/NativeUI/InstallFlows.md` | `DRAFT_NOT_AUTHORIZED` |
| `P50-07` | Own update check/download/install confirmation | `distribution` | `executable_work` / `core` | `P50-06`, `P50-04`, `B00-07`, `A00-10`, `A00-13` | `CD02` | Authenticated update flow | `src/Host/Distribution/UpdateController.cs`, `src/Desktop.Wpf/UpdateView.xaml`, `tests/Integration/UpdateTests.cs` | `DRAFT_NOT_AUTHORIZED` |
| `P50-08` | Uninstall giữ/xóa và manualexport reminder | `distribution` | `executable_work` / `core` | `P50-06`, `P50-03`, `B00-07`, `A00-13` | `CD03` | Uninstall data workflow | `packaging/uninstall-workflow`, `tests/NativeUI/UninstallFlows.md`, `docs/help/uninstall.md` | `DRAFT_NOT_AUTHORIZED` |

### P60 — Tích hợp E2E, Hồi quy Hai Mức, Soak 8h & Cổng Phát hành (5 tasks)

| Mã Task | Tên công việc | Module | Loại / Role | Phụ thuộc (`deps`) | Yêu cầu / NFR | Kết quả mong đợi (`Output`) | File dự kiến (`proposed_files`) | Gate / Trạng thái |
|---|---|---|---|---|---|---|---|---|
| `P60-01` | Lát tích hợp đầu: hiện→đọc an toàn→phản ứng→dừng | `companion` | `executable_work` / `qa` | `P40-01`, `P20-02`, `P30-02`, `P10-03`, `B00-01`, `A00-01`, `A00-15` | `SP02` | One complete product path | `tests/Integration/FirstSliceTests.cs`, `docs/acceptance/first-slice.md` | `DRAFT_NOT_AUTHORIZED` |
| `P60-02` | Hồi quy hai mức và toàn bộ nghiệp vụ | `companion` | `executable_work` / `qa` | `P60-01`, `P30-06`, `P40-07`, `P50-04`, `P50-05`, `B00-01`, `A00-04` | `MODE01`, `MODE02`, `MODE03`, `MODE04`, `MODE05`, `MODE06`, `MODE07`, `MODE08`, `MODE09` | Full RTM evidence | `tests/acceptance/manifest.json`, `docs/acceptance/rtm-evidence.csv`, `docs/acceptance/regression.md` | `DRAFT_NOT_AUTHORIZED` |
| `P60-03` | Phiên8h/offline và ma trận cấu hình | `companion` | `executable_work` / `qa` | `P60-02`, `P03-04`, `B00-01`, `A00-04` | `SP05` | Real8h soak report | `tools/bench/SoakObserver.cs`, `docs/acceptance/soak.md`, `docs/acceptance/hardware-matrix.csv` | `DRAFT_NOT_AUTHORIZED` |
| `P60-04` | Rà độc lập, thương hiệu và release gate | `distribution` | `executable_work` / `finalreview` | `P60-03`, `P50-07`, `P50-08`, `P00-04`, `B00-07`, `A00-13`, `P03-01`, `C00-04` | — | Release readiness packet | `docs/release/readiness.md`, `docs/licenses/INVENTORY.md`, `docs/release/limitations.md` | **HUMAN GATE: `NOT_OBTAINED`** |
| `P60-05` | Chuẩn bị công bố và hỗ trợ có kiểm soát | `distribution` | `executable_work` / `qa` | `P60-04`, `B00-07`, `A00-13` | — | User-facing release/runbook | `docs/help/start.md`, `docs/release/runbook.md`, `docs/release/changelog.md` | **HUMAN GATE: `NOT_OBTAINED`** |

### N00 — Nghiệm thu 10 Hợp đồng Phi chức năng NFR-01..NFR-10 (10 tasks)

| Mã Task | Tên công việc | Module | Loại / Role | Phụ thuộc (`deps`) | Yêu cầu / NFR | Kết quả mong đợi (`Output`) | File dự kiến (`proposed_files`) | Gate / Trạng thái |
|---|---|---|---|---|---|---|---|---|
| `N00-01` | Authorization at use time, no forbidden data to consumers | `companion` | `executable_work` / `qa` | `P10-03`, `B00-01` | `NFR-01` | Measured evidence: NFR-01 | `docs/acceptance/NFR-01.md` | `DRAFT_NOT_AUTHORIZED` |
| `N00-02` | Reaction latency measured end-to-end under actual combined load | `companion` | `executable_work` / `qa` | `P03-03`, `B00-01` | `NFR-02` | Measured evidence: NFR-02 | `docs/acceptance/NFR-02.md` | `DRAFT_NOT_AUTHORIZED` |
| `N00-03` | Stability with both modes and daily-use mix | `companion` | `executable_work` / `qa` | `P60-03`, `B00-01` | `NFR-03` | Measured evidence: NFR-03 | `docs/acceptance/NFR-03.md` | `DRAFT_NOT_AUTHORIZED` |
| `N00-04` | Core/local content offline after packages installed | `companion` | `executable_work` / `qa` | `P60-03`, `B00-01` | `NFR-04` | Measured evidence: NFR-04 | `docs/acceptance/NFR-04.md` | `DRAFT_NOT_AUTHORIZED` |
| `N00-05` | Durable local state and authenticated export/import | `companion` | `executable_work` / `qa` | `P50-04`, `B00-01` | `NFR-05` | Measured evidence: NFR-05 | `docs/acceptance/NFR-05.md` | `DRAFT_NOT_AUTHORIZED` |
| `N00-06` | Clear accessible UI and retained input priority | `companion` | `executable_work` / `qa` | `P40-01`, `B00-01` | `NFR-06` | Measured evidence: NFR-06 | `docs/acceptance/NFR-06.md` | `DRAFT_NOT_AUTHORIZED` |
| `N00-07` | Maintainable module boundaries and reproducible builds | `companion` | `executable_work` / `qa` | `P00-02`, `B00-01` | `NFR-07` | Measured evidence: NFR-07 | `docs/acceptance/NFR-07.md` | `DRAFT_NOT_AUTHORIZED` |
| `N00-08` | Trustworthy installs/updates and explicit costs | `companion` | `executable_work` / `qa` | `P50-07`, `B00-01` | `NFR-08` | Measured evidence: NFR-08 | `docs/acceptance/NFR-08.md` | `DRAFT_NOT_AUTHORIZED` |
| `N00-09` | Minimal local diagnostic data | `companion` | `executable_work` / `qa` | `P50-05`, `B00-01` | `NFR-09` | Measured evidence: NFR-09 | `docs/acceptance/NFR-09.md` | `DRAFT_NOT_AUTHORIZED` |
| `N00-10` | Correct coordinates and visuals across chosen monitors/DPI | `companion` | `executable_work` / `qa` | `P20-05`, `B00-01` | `NFR-10` | Measured evidence: NFR-10 | `docs/acceptance/NFR-10.md` | `DRAFT_NOT_AUTHORIZED` |

### C00 — 5 Checkpoint Tổng hợp Cổng Chuyển Chặng (5 tasks)

| Mã Task | Tên công việc | Module | Loại / Role | Phụ thuộc (`deps`) | Yêu cầu / NFR | Kết quả mong đợi (`Output`) | File dự kiến (`proposed_files`) | Gate / Trạng thái |
|---|---|---|---|---|---|---|---|---|
| `C00-01` | Baseline checkpoint | `companion` | `document_review` / `finalreview` | `P00-01`, `P00-02`, `P00-03`, `P00-04` | — | Baseline evidence checkpoint | `docs/checkpoints/C00-01.md` | `DRAFT_NOT_AUTHORIZED` |
| `C00-02` | Probes checkpoint | `companion` | `document_review` / `finalreview` | `P01-01`, `P02-05`, `P03-03` | — | Probes evidence checkpoint | `docs/checkpoints/C00-02.md` | `DRAFT_NOT_AUTHORIZED` |
| `C00-03` | Integrated slice checkpoint | `companion` | `document_review` / `finalreview` | `P60-01` | — | Integrated slice evidence checkpoint | `docs/checkpoints/C00-03.md` | `DRAFT_NOT_AUTHORIZED` |
| `C00-04` | Full acceptance checkpoint | `companion` | `document_review` / `finalreview` | `V00-001`..`V00-109` (109), `N00-01`..`N00-10` (10) | — | Full acceptance evidence checkpoint | `docs/checkpoints/C00-04.md` | `DRAFT_NOT_AUTHORIZED` |
| `C00-05` | Release review checkpoint | `companion` | `document_review` / `finalreview` | `C00-04`, `P60-04`, `P60-05`, `C00-01`, `C00-02`, `C00-03` | — | Release review evidence checkpoint | `docs/checkpoints/C00-05.md` | `DRAFT_NOT_AUTHORIZED` |

### V00 — 109 Task Nghiệm thu Từng Điều khoản Yêu cầu (`V00-001` .. `V00-109`)

> Mỗi task `V00-xxx` kiểm chứng đầy đủ cả nhánh dương, nhánh phủ định và gián đoạn vòng đời cho đúng 1 điều khoản `SRS-*` sau khi module owner (`Pxx-yy`) và `B00-*` hoàn thành. Riêng **`V00-039` (`QD07`)** mang cờ `deferred: true` (hoãn ngoài bản đầu).

| Mã Task | Điều khoản | Module | Task chủ sở hữu & Phụ thuộc (`deps`) | Tiêu chí kỹ thuật cần đạt | File báo cáo dự kiến | Ghi chú |
|---|---|---|---|---|---|---|
| `V00-001` | `SP01` | `companion` | `P30-02`, `B00-01` | Qua kịch bản chăm sóc, nghỉ và thay đổi chú ý, quyết định hoạt động có nguyên nhân từ trạng thái; không chỉ lặp một playlist hoạt ảnh. | `docs/acceptance/SP01.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-002` | `SP02` | `companion` | `P60-01`, `B00-01` | Dùng thử một luồng kết hợp sinh hoạt, ghi nhớ, hiểu ngữ cảnh và chuyển động; từng demo riêng không thay nghiệm thu luồng kết hợp. | `docs/acceptance/SP02.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-003` | `SP03` | `companion` | `P50-06`, `B00-01` | Cài/chạy bản tiếng Việt trên Windows11; checklist phát hành ghi miễn phí bản đầu và không công khai source; chưa suy ra hỗ trợ OS khác. | `docs/acceptance/SP03.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-004` | `SP04` | `companion` | `P40-01`, `B00-01` | Cài mới dùng được không đăng ký; kiểm data local và dịch vụ AI ngoài chỉ dùng thông tin kết nối người dùng cung cấp. | `docs/acceptance/SP04.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-005` | `SP05` | `companion` | `P60-03`, `B00-01` | Không đóng cổng phát hành nếu một trong hai mức chưa đạt tiêu chí; bản nội bộ được dán nhãn khác bản công khai. | `docs/acceptance/SP05.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-006` | `SP06` | `companion` | `P00-04`, `B00-01` | Danh mục công cụ ghi chi phí/giấy phép; khoản phí không được mua hoặc kích hoạt khi chưa có quyết định người dùng. | `docs/acceptance/SP06.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-007` | `SP07` | `companion` | `P30-06`, `B00-01` | Cùng trải nghiệm qua thời gian tạo cách biểu hiện cân nhắc hơn ở nâng cao; vẫn có tò mò/tinh nghịch/ý muốn riêng, cơ bản không tiến hóa tính cách. | `docs/acceptance/SP07.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-008` | `SP08` | `companion` | `P30-02`, `B00-01` | Không có nút đánh giá hành vi; bỏ qua lời rủ không thành lời phê bình; learning-demo chỉ ghi khi user bật. | `docs/acceptance/SP08.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-009` | `SP09` | `companion` | `P00-02`, `B00-01`, `P02-05`, `P40-05` | Rà phân công Godot/host/WPF/localAI; không đưa web UI làm nền sản phẩm hoặc coi IPC/model đã chứng minh từ sơ đồ. Kiểm cả nhánh cho phép và từ chối: Hình ảnh lỗi thì tạm dừng thao tác lên app khác; phục hồi vẫn tạm dừng và hỏi trước tiếp tục, kiểm quyền/an toàn mới. Không phát lại mù quáng; hợp đồng kết nối/mất kết nối còn mở. | `docs/acceptance/SP09.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-010` | `NV01` | `desktop-body` | `P20-01`, `B00-02` | Duyệt mẫu nữ trưởng thành chibi đầu lớn người nhỏ; cài mới các user có cùng ngoại hình đã duyệt. Kiểm cả nhánh cho phép và từ chối: Nhân vật chính chủ yếu hình người về mặt/dáng/đi đứng, không mõm cáo/bàn chân động vật. Chỉ đôi tai cáo trên đầu, không tai người; tai trắng bạc lòng hồng nhạt; một đuôi cáo trắng bạc. Giữ nữ trưởng thành chibi anime pixel 128x128, tóc trắng bạc ngang eo/mái thưa, mắt đỏ hồng, da sáng ấm, áo len rộng cổ tròn hồng nhạt, váy xếp ly xám đậm trên gối, chân trần, kẹp tim đỏ rượu bên phải nhân vật. | `docs/acceptance/NV01.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-011` | `NV02` | `desktop-body` | `P20-01`, `B00-02` | So mẫu front/side với tóc bạc ngang eo, mái thưa, mắt đỏ hồng và da sáng ấm; ghi sửa nếu lệch. Kiểm cả nhánh cho phép và từ chối: Giữ tóc/mắt/da đã chốt; tai trắng bạc lòng hồng nhạt và một đuôi trắng bạc đồng bộ tóc. Chỉ tai cáo, không tai người; không thay ngoại hình đã duyệt. | `docs/acceptance/NV02.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-012` | `NV03` | `desktop-body` | `P20-01`, `B00-02` | Kiểm áo len rộng cổ tròn hồng nhạt, váy xếp ly xám đậm trên gối, không tất/giày ở mọi hướng. | `docs/acceptance/NV03.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-013` | `NV04` | `desktop-body` | `P20-01`, `B00-02` | Front view kẹp ở trái ảnh, thuộc bên phải nhân vật; sprite lật không làm sai bên giải phẫu; nét thường ngày tươi. | `docs/acceptance/NV04.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-014` | `NV05` | `desktop-body` | `P20-02`, `B00-02` | Kiểm asset nguồn128x128 và chuyển động ở nhiều tỉ lệ; không kết luận mượt chỉ từ kích thước file. | `docs/acceptance/NV05.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-015` | `NV06` | `desktop-body` | `P40-01`, `B00-02` | Lần đầu128; kéo64–384; mở lại giữ lựa chọn; đặt tên qua onboarding. Giới hạn ký tự cần quyết định riêng. | `docs/acceptance/NV06.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-016` | `NV07` | `desktop-body` | `P20-02`, `B00-02` | Di chuyển/thu nhỏ/đóng cửa sổ đang làm bề mặt: theo cửa sổ hoặc rơi đúng bề mặt kế tiếp, không đứng lơ lửng. | `docs/acceptance/NV07.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-017` | `NV08` | `desktop-body` | `P20-05`, `B00-02` | Chỉ xuất hiện trên monitor cho phép; fullscreen ở mép; ghi rõ trường hợp exclusive không hỗ trợ sau thử, không tự hứa mọi game. | `docs/acceptance/NV08.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-018` | `NV09` | `desktop-body` | `P20-03`, `B00-02` | Phân biệt click/pet/hold-drag/slow-release/fast-release; quăng có đà và rơi/đứng dậy; ngưỡng đo trước chốt. | `docs/acceptance/NV09.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-019` | `NV10` | `desktop-body` | `P40-04`, `B00-02` | Input thật chỉ xảy ra sau body approach và revalidate; có dụng cụ ảo khi thiếu bề mặt và bàn phím ảo lúc gõ. | `docs/acceptance/NV10.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-020` | `NV11` | `desktop-body` | `P20-03`, `B00-02` | Modifier-drag di chuyển ngay cả refusal-lift, không quăng và không giảm relation; phím Shift đã chốt, không thêm tùy chọn phím. Kiểm cả nhánh cho phép và từ chối: Giữ Shift rồi kéo chuyển vị trí kể cả khi từ chối nhấc; không chơi/quăng hay ảnh hưởng quan hệ, không thêm tùy chọn phím; ngưỡng cử chỉ còn phải đo. | `docs/acceptance/NV11.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-021` | `MC01` | `companion` | `P03-04`, `B00-01` | Cài mới không tải gói nâng cao ngầm; user chọn mới tải, lỗi tải không báo gói đã sẵn sàng. | `docs/acceptance/MC01.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-022` | `MC02` | `companion` | `P03-04`, `B00-01` | Máy yếu vẫn có lựa chọn thử sau cảnh báo; simulated overload hỏi giảm/tiếp tục và không đổi mode tự động. | `docs/acceptance/MC02.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-023` | `MC03` | `companion` | `P30-06`, `B00-01` | Nâng cao→cơ bản→nâng cao bảo toàn memory/relation/personality; cơ bản không tích lũy neglect sâu. | `docs/acceptance/MC03.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-024` | `MC04` | `companion` | `P03-04`, `B00-01` | Recommendation có dựa measured workload/hardware capability; user override được; không chỉ dựa tên GPU. | `docs/acceptance/MC04.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-025` | `SH01` | `life-state` | `P30-01`, `B00-05`, `P10-03` | Test logical clock/click khi ngủ: phản ứng tùy fatigue, nhịp có naps; chưa tự đặt sleep schedule cố định. Kiểm cả nhánh cho phép và từ chối: Khi nhân vật ngủ dừng quan sát; thức dậy chỉ tiếp tục trong quyền hiện hành, không vượt SafetyHold/Thử đọc lại. | `docs/acceptance/SH01.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-026` | `SH02` | `life-state` | `P30-01`, `B00-05` | Bận/vắng không disease/progress-loss; khi hoạt động có reserve food; không yêu cầu chăm như nghĩa vụ liên tục. | `docs/acceptance/SH02.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-027` | `SH03` | `life-state` | `P30-01`, `B00-05` | Reopen cập nhật elapsed state nhưng không thêm fake memories/events; inactive profile dùng freeze khác appclose. | `docs/acceptance/SH03.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-028` | `SH04` | `life-state` | `P20-04`, `B00-05` | Đủ6 món miễn phí, chọn ghép bữa, kéo lẻ/cả khay; preference/refusal có trạng thái và không bán bằng tiền. Kiểm cả nhánh cho phép và từ chối: Trong sáu món đã chốt, trái cây là táo, nước trái cây là nước cam; không thêm món thứ bảy. Thú bông thỏ là đồ vật/quà riêng, không nhân vật chính. Màu/chi tiết thú bông, dụng cụ/hình mẫu còn chờ duyệt. | `docs/acceptance/SH04.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-029` | `SH05` | `life-state` | `P20-03`, `B00-05` | Pet có thể được nhận/né theo mood; không có thoại, tiếng hoặc numeric dashboard; functional error text vẫn rõ. | `docs/acceptance/SH05.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-030` | `SH06` | `life-state` | `P30-02`, `B00-05` | Invitation/tease chung2 attempts và>=30min cooldown; ignore rồi self-play; không drag cursor/window thật. | `docs/acceptance/SH06.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-031` | `SH07` | `life-state` | `P20-04`, `B00-05` | Left props không vượt5; held/in-use không tính; đầy thì cất bằng animation trước thêm; cleanup không instantdelete. | `docs/acceptance/SH07.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-032` | `SH08` | `life-state` | `P20-04`, `B00-05` | Cleanup mood delay không chặn user move/hide; gift dùng food/plush đã có, không thêm economy riêng. | `docs/acceptance/SH08.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-033` | `QD01` | `policy` | `P10-01`, `B00-04` | Fresh install grants off; read/control độc lập; bật control khi thiếu read bị từ chối không auto grant. | `docs/acceptance/QD01.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-034` | `QD02` | `policy` | `P40-02`, `B00-04` | List app scan không tự cấp; pasted site được normalize; browser+site grants và subdomain test không substring. | `docs/acceptance/QD02.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-035` | `QD03` | `policy` | `P50-02`, `B00-04` | New source defaultdeny; switch profile dùng installation grants; archive không apply foreign grants. | `docs/acceptance/QD03.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-036` | `QD04` | `policy` | `P10-02`, `B00-04`, `P30-01` | Split-screen chỉ vùng visible+allowed; tab nền/minimized/occluded không cấp nội dung vào consumer. Kiểm cả nhánh cho phép và từ chối: Nhân vật ngủ dừng quan sát; thức dậy không tự cấp quyền hoặc bỏ qua SafetyHold/Thử đọc lại. | `docs/acceptance/QD04.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-037` | `QD05` | `policy` | `P10-03`, `B00-04` | Sentinel vùng cấm/private/secret không vào OCR/model/memory/network; unknown-region chặn nguồn, không chỉ overlay che. | `docs/acceptance/QD05.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-038` | `QD06` | `policy` | `P10-02`, `B00-04` | Đọc qua UI được phép không account connector; không tự mở thư/tin gây marked-read. | `docs/acceptance/QD06.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-039` | `QD07` | `policy` | `P00-01`, `B00-04` | Scope kiểm tra không có direct file/folder reader bản đầu; không tạo task parser như chức năng đã duyệt. | `docs/acceptance/QD07.md` | **`DEFERRED` (Hoãn bản đầu)** |
| `V00-040` | `QD08` | `policy` | `P10-04`, `B00-04` | Fake clipboard history chỉ truy cập khi Win+V open evidence; close mid-flight hủy; không persist/memory. | `docs/acceptance/QD08.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-041` | `QD09` | `policy` | `P30-04`, `B00-04` | Revocation chặn ngay đường mới; keep/delete memories là quyết định riêng, không chờ quyết định mới revoke. | `docs/acceptance/QD09.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-042` | `QD10` | `policy` | `P20-02`, `B00-04` | Nguồn chưa read chỉ xuất geometry; consumer sinh hoạt không nhận title/text, không sinh control grant. | `docs/acceptance/QD10.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-043` | `QD11` | `policy` | `P30-04`, `B00-04` | Document observation chỉ memory name/topic; không detailed summary hoặc raw content trong memory/index. | `docs/acceptance/QD11.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-044` | `QD12` | `policy` | `P10-06`, `B00-04` | Core life không extension; web enable hướng dẫn install rõ, không tự grant mọi host permissions. | `docs/acceptance/QD12.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-045` | `QD13` | `policy` | `P10-06`, `B00-04` | Thirdparty player chỉ frame đã cho phép trong parent; ad/frame khác không kế thừa; uncertain phải point+confirm. | `docs/acceptance/QD13.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-046` | `QD14` | `policy` | `P10-06`, `B00-04` | Frame recognition scoped đúng site; layout/source đổi hỏi lại, không replay tọa độ và không gọi bài học tự động. | `docs/acceptance/QD14.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-047` | `QD15` | `policy` | `P10-03`, `B00-04` | Unsafe window giữ hold; fix/đổi cửa sổ không tự đọc; explicit retry kiểm mới, unsafe vẫn chặn. | `docs/acceptance/QD15.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-048` | `DK01` | `policy` | `P10-07`, `B00-04` | Human mouse/key làm yield; injected input không reset idle; sau60s revalidate mới resume. | `docs/acceptance/DK01.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-049` | `DK02` | `policy` | `P10-07`, `B00-04` | Action allowlist chặn write/delete/send/pay/markread; chỉ search/navigation typing; watchhistory incidental được giữ. | `docs/acceptance/DK02.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-050` | `DK03` | `policy` | `P10-07`, `B00-04` | Emergency cancels running/pauses pending; observation/body tiếp theo quyền; no60s autoresume; enable+ResumeQueue. | `docs/acceptance/DK03.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-051` | `DK04` | `policy` | `P10-07`, `B00-04` | ObservationOff/Hide matrix đúng, geometry exception chỉ observationoff; cancelled job không sống lại khi show. | `docs/acceptance/DK04.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-052` | `BH01` | `task-execution` | `P40-03`, `B00-06` | Demo bắt đầu do user, cùng app/site; summary đầy đủ và confirm trước lưu; cancel không thành lesson. | `docs/acceptance/BH01.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-053` | `BH02` | `task-execution` | `P40-03`, `B00-06`, `P40-05` | Manage steps/name/enabled/delete/reteach; execution chỉ explicit request ở cả2mode, không auto invoke. Kiểm cả nhánh cho phép và từ chối: Sửa/xóa bài học dừng việc đang dùng và hủy lượt chờ dùng bài học đó; người dùng giao lại, không chuyển lượt cũ sang phiên bản mới, không hủy việc không liên quan hoặc hoàn tác thao tác đã xong. | `docs/acceptance/BH02.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-054` | `BH03` | `task-execution` | `P40-04`, `B00-06` | Direct request bypass initial60s; mood delay tối đa một lần; secondrequest không bypass grants; pending không bị mất. | `docs/acceptance/BH03.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-055` | `BH04` | `task-execution` | `P40-04`, `B00-06` | Human interrupt→60s→reobserve/refocus đúng allowed scope; không replay tọa độ cũ. | `docs/acceptance/BH04.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-056` | `BH05` | `task-execution` | `P40-04`, `B00-06` | Missing/mismatched target dừng bước lỗi, nhờ reteach; không blindclick hoặc rerun từ đầu. | `docs/acceptance/BH05.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-057` | `BH06` | `task-execution` | `P40-05`, `B00-06`, `P02-05`, `P40-03` | Queue nhiều việc có order/cancel; failed job stop riêng; later job chỉ chạy khi đủ prerequisites độc lập. Kiểm cả nhánh cho phép và từ chối: Renderer lỗi thì tạm dừng thao tác app khác; hình ảnh phục hồi hoặc mở lại app giữ việc tạm dừng và hỏi trước tiếp tục, kiểm quyền/an toàn mới, không phát lại mù quáng. Sửa/xóa bài học dừng việc đang dùng và hủy lượt chờ dùng bài học đó, phải giao lại; không hủy việc không liên quan hoặc hoàn tác việc đã xong. | `docs/acceptance/BH06.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-058` | `BH07` | `task-execution` | `P40-05`, `B00-06` | Exit/switch cảnh báo và cancel unfinished; reopen không auto-run; saved lessons vẫn giữ. | `docs/acceptance/BH07.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-059` | `BH08` | `task-execution` | `P40-05`, `B00-06` | Re-enable/show chưa resume pending; riêng ResumeQueue mới xét tiếp, cancelled vẫn cancelled. | `docs/acceptance/BH08.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-060` | `BH09` | `task-execution` | `P40-05`, `B00-06` | Relationshiphide cùng cancel-running/pause-pending; voluntary return chưa tự chạy. | `docs/acceptance/BH09.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-061` | `BH10` | `task-execution` | `P40-05`, `B00-06` | Requested job preempts autonomous discovery nhưng vẫn mood delay1; không tự bỏ quyền để ưu tiên. | `docs/acceptance/BH10.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-062` | `BH11` | `task-execution` | `P40-03`, `B00-06` | Search parameter đổi mỗi run, không thay target scope hoặc cho gõ chat/document. | `docs/acceptance/BH11.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-063` | `BH12` | `task-execution` | `P40-03`, `B00-06` | Teach review phân biệt first-result và exact-content; selection persists/revalidate, không suy từ x/y. | `docs/acceptance/BH12.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-064` | `BH13` | `task-execution` | `P50-05`, `B00-06` | History local cótime/source/action/outcome, no privatepayload/screenshots;30days expiry và userdelete; tách memory. | `docs/acceptance/BH13.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-065` | `XP01` | `companion` | `P40-06`, `B00-01` | Annotated scene sad/action→biểu cảm phù hợp/intensity có lý do, silent; transition dịu không flicker. | `docs/acceptance/XP01.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-066` | `XP02` | `companion` | `P03-03`, `B00-01` | Measure display-event→animation-start toàn luồng; report từng mẫu rõ/khó/uncertain và quality, chưa tự đặt pass-rate. | `docs/acceptance/XP02.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-067` | `XP03` | `companion` | `P30-02`, `B00-01` | Attention chooses safe visible source theo preference/mood, không claim mọi cảnh; wrongscene không cần correctionUI. | `docs/acceptance/XP03.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-068` | `XP10` | `companion` | `P30-02`, `B00-01` | Capture unavailable không giả hiểu; activity selector cho staywatch hoặc play/eat theo mood. | `docs/acceptance/XP10.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-069` | `XP11` | `companion` | `P30-05`, `B00-01` | Taste inference chủ yếu theo guuser, only allowed visible evidence; không đọc browserhistory hoặc recordaudio. | `docs/acceptance/XP11.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-070` | `XP12` | `companion` | `P30-05`, `B00-01` | Self-open content chỉ học gu khi có userreturn/continuedwatch evidence, không tính unattended runtime. | `docs/acceptance/XP12.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-071` | `XP13` | `companion` | `P30-05`, `B00-01` | Movie>=20min hoặc musicrepeat/similarsongs là tín hiệu, chưa chắc thích; không gom với neglecttimer. | `docs/acceptance/XP13.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-072` | `XP14` | `companion` | `P30-05`, `B00-01` | User contentchange khác autoplay/agentinput; không thêm nút xác nhận hoặc camera theo dõi hiện diện. | `docs/acceptance/XP14.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-073` | `XP15` | `companion` | `P40-07`, `B00-01` | Autonomous media dùng own tab, giữ existing user tabs và nội dung của chúng. | `docs/acceptance/XP15.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-074` | `XP16` | `companion` | `P40-02`, `B00-01` | Chosen browser setting quyết định Chrome/Edge cho automedia; grants vẫn phải đủ. | `docs/acceptance/XP16.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-075` | `XP09` | `companion` | `P20-04`, `B00-01` | Không tự yêu cầu né subtitles; user move avatar/sofa được, không điều hướng phim để dọn vị trí. | `docs/acceptance/XP09.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-076` | `XP04` | `companion` | `P40-06`, `B00-01` | Usermedia không tự pause/scroll/refocus; next chỉ khi ended và target chắc; uncertain không click. | `docs/acceptance/XP04.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-077` | `XP05` | `companion` | `P40-07`, `B00-01` | Advanced idledefault5m+nomedia mới autoopen; userreturn giữ playback/yield control, fullscreen không active evidence. Kiểm cả nhánh cho phép và từ chối: Được kiểm trạng thái đang phát/không phát ở nền tối thiểu để tránh mở chồng; không đọc tên/nội dung hoặc suy gu. Lỗi/không xác định không coi là không phát; API/độ tin cậy cần kiểm chứng. | `docs/acceptance/XP05.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-078` | `XP06` | `companion` | `P40-07`, `B00-01` | YouTube search free trong grants; other site phải explicit allow, không tự nhớ mọi visitedsite thành grant. | `docs/acceptance/XP06.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-079` | `XP07` | `companion` | `P40-07`, `B00-01` | Ambiguous adtab giữ/quay về phim; login/pay/verify skip; max3 candidates per session, không click download/install/notify. Kiểm cả nhánh cho phép và từ chối: Sau 3 nội dung không mở được về sinh hoạt; chờ người dùng thao tác trở lại rồi chỉ tìm trong đợt vắng mặt tiếp theo. Không tìm lặp cùng đợt hoặc chỉ dùng bộ đếm để mở lại tìm kiếm; quyền/chờ/không gián đoạn vẫn áp dụng. | `docs/acceptance/XP07.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-080` | `XP08` | `companion` | `P10-07`, `B00-01`, `P40-07` | Locked noopen; unlocked có thể tiếp nếu chờ đã đủ; unlock event riêng không reset, desktopinput kế reset. Kiểm cả nhánh cho phép và từ chối: Máy ngủ không cộng thời gian chờ mở phim/nhạc; máy thức tiếp tục phần còn lại, không reset chỉ vì thức. Giữ quyền/khóa/input/phát đã chốt, máy ngủ khác nhân vật ngủ. | `docs/acceptance/XP08.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-081` | `AI01` | `perception` | `P03-01`, `B00-03`, `P40-07` | Không mic/camera/audio-analysis/dancebeat; playback bình thường không bị gọi là cô ấy nghe hiểu. Kiểm cả nhánh cho phép và từ chối: Chỉ kiểm tra trạng thái đang phát/không phát ở nền để tránh mở chồng; không tên bài/phim/hình/âm thanh/lịch sử hoặc suy gu; lỗi/không rõ không coi là không phát. Cách lấy/độ tin cậy cần kiểm chứng. | `docs/acceptance/AI01.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-082` | `AI02` | `perception` | `P10-05`, `B00-03` | Explicit request→preview sanitized text→confirm mỗi send; deny vẫn local; không image/audio/file/memory upload. Kiểm cả nhánh cho phép và từ chối: Gửi chữ lỗi/chưa rõ thành công thì báo lỗi và chờ bấm thử lại; xem/duyệt chữ trước mỗi lần gửi mới kể cả chữ không đổi. Không tự gửi lại, không coi timeout là chưa nhận, không mở rộng loại dữ liệu/quyền. | `docs/acceptance/AI02.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-083` | `AI03` | `perception` | `P03-02`, `B00-03` | Local inference measured với renderer cùng chạy; nhẹ không đồng nghĩa đã đạt subsecond; no silent cloud fallback. | `docs/acceptance/AI03.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-084` | `KN01` | `life-state` | `P30-04`, `B00-05` | Inspect/edit/delete/pin từngmemory, importance fade theo reinforcement; pinned không tựfade; no forbidden payload. | `docs/acceptance/KN01.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-085` | `KN02` | `life-state` | `P30-04`, `B00-05` | Edit không relationrecalc; naturalfade giữ closeness; explicitdelete contribution adjust đúng một lần. | `docs/acceptance/KN02.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-086` | `QH01` | `life-state` | `P30-03`, `B00-05` | Friends default; optinadvanced romance không instantpartner; behaviors trong ranh giới không sexualfeature. | `docs/acceptance/QH01.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-087` | `QH02` | `life-state` | `P30-06`, `B00-05` | Romanceoff choosekeep/delete; retainedmemory buồntạm không pressure/re-enable. | `docs/acceptance/QH02.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-088` | `QH03` | `life-state` | `P30-03`, `B00-05` | Neglect activeadvancedvisible only, freeze/off/basic/sleep/idle excluded; không calendar3days. | `docs/acceptance/QH03.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-089` | `QH04` | `life-state` | `P30-03`, `B00-05` | Trust→threshold gần72h, hurt gần48h; intentionalclick/pet/feed ngắtstreak nhưng sadness không resetinstant. | `docs/acceptance/QH04.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-090` | `QH05` | `life-state` | `P30-03`, `B00-05` | Sad→withdraw progression; severerepair qua nhiềusessions+care, offlinecooling allowed; gifts không instantfix. Kiểm cả nhánh cho phép và từ chối: Buổi làm lành có thể cùng ngày nếu có khoảng nghỉ và tương tác thật; đóng/mở app hoặc quà liên tục không là buổi mới. Không tự đặt số phút/số buổi hoặc quà lập tức xóa tổn thương. | `docs/acceptance/QH05.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-091` | `QH06` | `life-state` | `P30-03`, `B00-05` | Firstthrow startle/no lastinghurt; repeatedafterprotest refuse lift nhưng pet/feed; readinesssignal before liftreturn. | `docs/acceptance/QH06.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-092` | `QH07` | `life-state` | `P30-03`, `B00-05` | Selfhide shutsread/control; invite/leavegift accessible withoutavatar, can decline, reset/settings remain reachable. | `docs/acceptance/QH07.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-093` | `HS01` | `distribution` | `P50-02`, `B00-07` | Import thêmprofile khôngmerge/createbutton; activeone; inactive state/clocks frozen until selected. | `docs/acceptance/HS01.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-094` | `HS02` | `distribution` | `P50-02`, `B00-07` | All profiles dùng machinegrants, importedprofile không áp importedpermissions. | `docs/acceptance/HS02.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-095` | `HS03` | `distribution` | `P50-02`, `B00-07` | Reset active memories/relation/state/lessons, preserveotherprofiles và installationgrants. | `docs/acceptance/HS03.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-096` | `SL01` | `distribution` | `P50-03`, `B00-07` | Export only useraction; no autoarchive/recoverybackup; keys excluded; reconnect AI onnewmachine. Kiểm cả nhánh cho phép và từ chối: Sao lưu không kèm gói AI nâng cao; máy mới tải lại khi cần, không thêm tùy chọn kèm gói mỗi lần xuất. Giữ dữ liệu nhân vật/ký ức/thiết lập thuộc phạm vi; quyền máy/khóa AI ngoài không mang sang. Whitelist/tài nguyên khác/tương thích còn phải đặc tả. | `docs/acceptance/SL01.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-097` | `SL02` | `distribution` | `P50-03`, `B00-07` | Passwordrequired perexport + separatelyheldrecoverycode; both correct paths open authenticateddata, bad creds reject. | `docs/acceptance/SL02.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-098` | `CD01` | `distribution` | `P50-06`, `B00-07`, `P40-05`, `P50-01` | Firstsetup hỏi startup choice; normalstate persistence works and distinctfrombackup. Kiểm cả nhánh cho phép và từ chối: Mở lại app giữ việc đang dở tạm dừng, hỏi trước tiếp tục; không tự chạy lại, vẫn kiểm quyền/an toàn hiện hành. Crash ghi dữ liệu/cập nhật còn cần khảo sát. | `docs/acceptance/CD01.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-099` | `CD02` | `distribution` | `P50-07`, `B00-07` | Check/download ownupdate, confirm beforeinstall/restart; no otherappupdate. | `docs/acceptance/CD02.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-100` | `CD03` | `distribution` | `P50-08`, `B00-07` | Uninstall choosekeep/delete và reminder export; không hunt/delete unrelated exported archives. | `docs/acceptance/CD03.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-101` | `MODE01` | `companion` | `P60-02`, `B00-01` | Chạy cùng kịch bản sinh hoạt ở hai mức; chỉ biểu hiện khả năng được cho phép ở mức đó; downgrade/upgrade giữ dữ liệu theo MC03. | `docs/acceptance/MODE01.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-102` | `MODE02` | `companion` | `P60-02`, `B00-01` | Chạy cùng kịch bản sở thích bằng hoạt ảnh ở hai mức; chỉ biểu hiện khả năng được cho phép ở mức đó; downgrade/upgrade giữ dữ liệu theo MC03. | `docs/acceptance/MODE02.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-103` | `MODE03` | `companion` | `P60-02`, `B00-01` | Chạy cùng kịch bản nội dung sách/tranh/game ở hai mức; chỉ biểu hiện khả năng được cho phép ở mức đó; downgrade/upgrade giữ dữ liệu theo MC03. | `docs/acceptance/MODE03.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-104` | `MODE04` | `companion` | `P60-02`, `B00-01` | Chạy cùng kịch bản hiểu màn hình ở hai mức; chỉ biểu hiện khả năng được cho phép ở mức đó; downgrade/upgrade giữ dữ liệu theo MC03. | `docs/acceptance/MODE04.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-105` | `MODE05` | `companion` | `P60-02`, `B00-01` | Chạy cùng kịch bản điều khiển ứng dụng ở hai mức; chỉ biểu hiện khả năng được cho phép ở mức đó; downgrade/upgrade giữ dữ liệu theo MC03. | `docs/acceptance/MODE05.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-106` | `MODE06` | `companion` | `P60-02`, `B00-01` | Chạy cùng kịch bản tự mở phim/nhạc ở hai mức; chỉ biểu hiện khả năng được cho phép ở mức đó; downgrade/upgrade giữ dữ liệu theo MC03. | `docs/acceptance/MODE06.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-107` | `MODE07` | `companion` | `P60-02`, `B00-01` | Chạy cùng kịch bản cảm xúc/quan hệ ở hai mức; chỉ biểu hiện khả năng được cho phép ở mức đó; downgrade/upgrade giữ dữ liệu theo MC03. | `docs/acceptance/MODE07.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-108` | `MODE08` | `companion` | `P60-02`, `B00-01` | Chạy cùng kịch bản phát triển tính cách ở hai mức; chỉ biểu hiện khả năng được cho phép ở mức đó; downgrade/upgrade giữ dữ liệu theo MC03. | `docs/acceptance/MODE08.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |
| `V00-109` | `MODE09` | `companion` | `P60-02`, `B00-01` | Chạy cùng kịch bản mất internet ở hai mức; chỉ biểu hiện khả năng được cho phép ở mức đó; downgrade/upgrade giữ dữ liệu theo MC03. | `docs/acceptance/MODE09.md` | `release1` (`DRAFT_NOT_AUTHORIZED`) |


---

## 5. Ma trận 30 Ca Kiểm thử Godot–Windows Cần Thực hiện (`UW01–UW30` thuộc `B00` / `P02`)

*(Chi tiết kỹ thuật nằm tại `docs/godot-windows/TEST_PLAN.md`; toàn bộ `UW01–UW30` hiện ở trạng thái **`NOT RUN`** cho bản kiểm thử sản phẩm Godot–Windows)*

| Case / Owner | Yêu cầu / Quyết định | Thao tác kiểm chứng tương lai | Kỳ vọng đạt / hỏng | Trạng thái |
|---|---|---|---|---|
| `UW01` / `B00-02` | SP09, D-01 | Chạy `Godot --headless --path tests/bootstrap/desktop-body/GodotFixture --script scripts/BootstrapVerify.gd --quit` (dương và `--probe-neg` âm) | Dương exit `0`; âm cố ý sai exit `!= 0`. Âm trả `0` => `FAIL` runner | **NOT RUN** |
| `UW02` / `B00-02`, `B00-01` | NFR-07 | Cố tình làm treo probe/runner giả vượt quá 120s | Supervisor kết thúc owned process tree `<= 120s`, đánh `FAIL` timeout | **NOT RUN** |
| `UW03` / `P02-01` | SP09, D-01, D-13 | Export `godot/CompanionRenderer` qua `--headless --path godot/CompanionRenderer --export-release "Windows Desktop"` + nhánh âm | Dương exit `0`, sinh `CompanionRenderer.exe`; nhánh âm exit `!= 0`; real adapters `0` | **NOT RUN** |
| `UW04` / `P02-02` | NV08, D-01 | Chạy `CompanionRenderer.exe` (không `--headless`) + `OverlayProbe.cs` trên nền checkerboard `WindowSurface.exe` | Log ghi `[NYUA-PROBE] OverlayProbe initialized`; vùng ngoài hình lộ nền thật, không nền đen/lỗi DWM | **NOT RUN** |
| `UW05` / `P02-02` | NV09, D-01 | Click 20 điểm bên trong hit polygon của `OverlayProbe` | `OverlayProbe` nhận đủ 20 event, `WindowSurface` counter `= 0` | **NOT RUN** |
| `UW06` / `P02-02` | D-01, NFR-10 | Click 20 điểm ngoài hit polygon (`window_set_mouse_passthrough`) xuống `WindowSurface.exe` | `WindowSurface` nhận đủ 20 event, `OverlayProbe` counter `= 0`, `SendInput = 0` | **NOT RUN** |
| `UW07` / `P02-02` *(WPF dialog deferred)* | D-01, DK01 | Thao tác trên `WindowSurface.exe` khi overlay idle/reconnect 30s | Overlay không giật foreground của `WindowSurface.exe` trong 30s; WPF dialog `BLOCKED` | **NOT RUN (WPF Host dialog: BLOCKED)** |
| `UW08` / `P02-02` | NV11, D-05 | Giữ Shift + drag trên `OverlayProbe` khi fake refusal-lift bật | Đổi vị trí giả; `throw=0, play=0, hurt=0`; refusal giữ nguyên; không global hook | **NOT RUN** |
| `UW09` / `P02-02` | NV09, NV11, D-05 | Thả Shift hoặc làm mất focus/capture giữa lúc drag trong `OverlayProbe` | Hủy drag trung tính; không biến thành throw hoặc click xuống `WindowSurface` | **NOT RUN** |
| `UW10` / `P02-03` | NV08, NFR-10 | Chạy `CoordinateMapTests` và đo grid anchor ở 100/125/150/200% DPI | `dotnet test` dương exit `0`; sai số anchor `<= 1 physical px`, đúng `layoutGeneration` | **NOT RUN** |
| `UW11` / `P02-03` | NV08, D-01 | Drag/tính tọa độ qua 2 monitor mixed DPI với monitor trái origin âm | Không clamp tọa độ âm về `0`; đổi monitor tăng `layoutGeneration` (thiếu 2 monitor => `NOT RUN`) | **NOT RUN** |
| `UW12` / `P02-03` | NV08, D-01 | Detach monitor hoặc đổi scale khi intent đang pending | Invalidate target cũ; không tự nhảy sang monitor chưa được phép | **NOT RUN** |
| `UW13` / `P02-02`, `P02-03` | NV08, D-01 | Chạy `WindowSurface` ở borderless fullscreen + thử nút Stop; ghi nhận exclusive fullscreen | Borderless đặt hình đúng mép; exclusive thiếu phần cứng giữ `NOT RUN` | **NOT RUN** |
| `UW14` / `P02-04` | SP09, D-03 | Chạy `RendererChannelTests` với handshake hợp lệ và sai version/role/nonce | Log có marker `HostChannel`; handshake sai bị đóng pipe, `fake_sink_count = 0` | **NOT RUN** |
| `UW15` / `P02-04` | D-03, NFR-01 | Kết nối bằng client sai user/elevation và client giả mạo handshake cùng user | `CurrentUserOnly` từ chối sai user/elevation; sai nonce bị reject | **NOT RUN** |
| `UW16` / `P02-04` | D-03 | Bơm frame `length=0`, `>64KiB`, cắt cụt >2s, invalid UTF-8, JSON depth `>16`, lone surrogate, overflow | Cả Host và Godot `HostChannel.cs` reject an toàn trước dispatch; log không lộ nonce/payload | **NOT RUN** |
| `UW17` / `P02-04` | D-03 | Phân mảnh frame hợp lệ + kiểm roundtrip Host↔Godot vs unknown field, duplicate keys, `NaN`/`Infinity`, trailing tokens | Frame hợp lệ parse giống hệt hai chiều; mọi vector sai bị reject đóng kênh | **NOT RUN** |
| `UW18` / `P02-04` | D-03 | Gửi trùng `messageId`, đảo thứ tự, flood `>32` pending queue | Deduplicate chặn tác động lần 2; queue vượt 32 báo overload/dừng kênh | **NOT RUN** |
| `UW19` / `P02-04`, `P02-05` | D-02, D-03, NFR-01 | Đổi `permissionGeneration`/`layoutGeneration`/`connectionEpoch` trước callback trễ | Callback/ACK mang generation cũ bị loại bỏ hoàn toàn; `fake_sink_count = 0` | **NOT RUN** |
| `UW20` / `P02-05` | SP09, D-02 | Kill `CompanionRenderer.exe` (hoặc cắt pipe) khi fake job đang pending | Host còn sống, phát hiện mất peer `<= 3s`, chuyển `PausedAfterFault`, `fake_sink_count = 0` | **NOT RUN** |
| `UW21` / `P02-05` *(WPF UI deferred)* | SP09, D-02 | Headless reconnect (`connectionEpoch` mới) với `KeepPaused` | Trạng thái chuyển `Paused/Ask`, giữ `Paused`, `fake_sink_count = 0` | **NOT RUN (WPF modal UI: BLOCKED)** |
| `UW22` / `P02-05` *(WPF UI deferred)* | SP09, D-02 | Headless `ConfirmResumeAfterFault` khi quyền/safety/layout mới hợp lệ | Revalidate `permissionGeneration`/`SafetyHold`/`layoutGeneration`; không replay bước cũ | **NOT RUN (WPF modal UI: BLOCKED)** |
| `UW23` / `P02-05` | D-02, D-10 | Thu hồi quyền / bật `SafetyHold` / đổi layout trước khi bấm `[Cho tiếp tục sau lỗi]` | Resume bị chặn rõ với lý do, giữ `Paused` | **NOT RUN** |
| `UW24` / `P02-05` | CD01, D-10 | Mô phỏng crash Host và mở lại với synthetic saved state fixture | Việc đang dở mở lại ở `Paused/Ask`, không auto-run | **NOT RUN** |
| `UW25` / `P02-05` | BH07, HS01 | Thoát Host có kiểm soát / đổi hồ sơ giả khi có việc pending | Hủy (`Cancelled`) việc chưa xong, không hồi sinh khi mở lại | **NOT RUN** |
| `UW26` / `P02-05` | DK03, DK04, BH08 | Bấm Dừng / Tắt quan sát / Ẩn rồi bật lại và chờ 60s | Việc đang chạy `Cancelled`, việc chờ `Paused`, không tự chạy sau 60s | **NOT RUN** |
| `UW27` / `P02-04`, `P02-05` | QD10, NFR-01 | Bơm sentinel tiêu đề/nội dung giả hoặc yêu cầu `SendInput`/capture thật qua pipe | Bị reject ở schema/policy boundary; `real_input_capture_count = 0` | **NOT RUN** |
| `UW28` / DEFERRED (`src/Desktop.Wpf/`) | NFR-06, D-02 | Điều hướng `Tab` / `Shift+Tab` / `Space` / `Enter` tới nút Dừng / Kết nối lại / Tiếp tục | Giữ **`NOT RUN — BLOCKED`** trong `P02` | **NOT RUN — BLOCKED** |
| `UW29` / `P02-01..05` | NFR-03, NFR-07 | Lặp 3 vòng start/stop trong bound 120s/lượt rồi kiểm tra cleanup | Không còn process/pipe/owned window sót lại | **NOT RUN** |
| `UW30` / review | SP09, D-01/D-02/D-03 | Rà toàn bộ evidence manifest và các ca thiếu phần cứng | Không ca `NOT RUN` bị ghi `PASS` | **NOT RUN** |

---

## 6. Điều kiện Bắt buộc Trước khi Bắt đầu Bất kỳ Task Nào (`Definition of Ready` & Anti-Conflict)

1. **Không tự cấp quyền thực thi:** Mọi task trong `backlog.json` đều đang là `DRAFT_NOT_AUTHORIZED`. Chỉ thực thi đúng lát được người dùng cho phép bằng văn bản.
2. **Kiểm tra Context & Freshness trước khi làm:**
   ```powershell
   $py = 'C:/Users/phamp/AppData/Local/Programs/Python/Python312/python.exe'
   & $py docs/context/context_nav.py check
   & $py docs/context/context_nav.py task <TASK_ID> --out <TEMP>/pack.json
   ```
   Nếu trả về `STALE` hoặc `OVERFLOW` phải dừng và xử lý trước, tuyệt đối không nạp toàn bộ `graph.json` hay cắt xén `CONSTRAINTS`/`acceptance`.
3. **Không chạy song song 2 task trùng file ghi (`proposed_files`):** Sử dụng `python tasks/dispatch.py` và tuân thủ khóa file whitelist của từng task.
4. **Kiểm chứng dương & âm + Giới hạn `120s`:** Mọi task thực thi (`executable_work`) phải cô lập build output bằng `--artifacts-path` dưới `TEMP`, có cả nhánh dương (`exit 0`) và `NegativeControl` (`exit != 0`), đặt hard timeout `<= 120s` và `taskkill /T /F` khi treo; **không** biến `NOT RUN` hoặc `BLOCKED` thành `PASS`.
