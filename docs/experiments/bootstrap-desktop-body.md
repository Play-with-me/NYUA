# Báo cáo Bootstrap `B00-02` — Desktop Body (Godot 4.7.2 .NET Headless Fixture)

- **Trạng thái thực thi:** **`PASS` (Bootstrap `B00-02` / `UW01` + `UW02` timeout supervisor)** — đã chạy thực tế theo ủy quyền **Chặng B** của người dùng; **CHƯA** chạy `P02-*` hay `UW03–UW30`.
- **Thời điểm thực thi:** `2026-11-15T23:57+07:00`
- **Ủy quyền phạm vi:** Người dùng đã duyệt **Chặng B** theo kế hoạch `b00-bootstrap-plan.md` rev5 (`SHA-256: c1f4dc7df184da96ff0d6c73c53c318ade8f6e1515147450f388ac3090e704d1`). Giữ nguyên 5 file whitelist của `B00-02`, không sửa `docs/product/AI/backlog.json`, `tasks/phase-*.md` hay `.gitignore` (các task trong `backlog.json` giữ `DRAFT_NOT_AUTHORIZED` / `BLOCKED_SCOPE_AUTHORIZATION` theo `tasks/validate_tasks.py` L29; `P00-01` chưa tự đóng).

## 1. Công cụ, Phiên bản, Giấy phép & Phát hiện Môi trường (`$0`)

- **Engine đã xác minh:** Godot `4.7.2-stable` (`.NET`, `MIT`, `$0`, `4.7.2.stable.mono.official.ed1daf0bf`) tại `C:\Pet\.tools\godot\Godot_v4.7.2-stable_mono_win64\Godot_v4.7.2-stable_mono_win64_console.exe` (`82/82` file khớp SHA-256 gói chính thức).
- **Phát hiện thực tế về `.NET` cô lập:** Lần gọi đầu tiên không có `DOTNET_ROOT`/`PATH` trỏ tới `C:\Users\phamp\.ao\data\tools\nyua-dotnet` làm `Godot_v4.7.2-stable_mono_win64_console.exe` báo `ERROR: Could not create child process: dotnet --list-sdks` / `find_hostfxr` và bị supervisor `WaitForExit` + `taskkill /T /F` ngắt đúng hạn (`ExitCode=124`). Khi truyền **`DOTNET_ROOT=C:\Users\phamp\.ao\data\tools\nyua-dotnet`** và **`PATH` cục bộ chỉ trong tiến trình con** (không sửa `PATH` hệ thống hay registry), cả 3 lượt `UW01` dương, `UW01` âm, và `UW02` hang chạy đúng kỳ vọng.
- **Export Templates:** **Chưa cài đặt** (`%APPDATA%\Godot\export_templates` không tồn tại) và **chưa cần** cho `B00-02`; hoãn tới `P02-01` sau `P00-04`/`P00-02`/`A00-01`.
- **Ranh giới trung thực (KHÔNG chứng minh quá phạm vi):**
  - `B00-02` chỉ chạy **GDScript `--headless`** (`extends SceneTree`) để nạp `res://scenes/Bootstrap.tscn`.
  - Kết quả của `B00-02` **KHÔNG** chứng minh biên dịch C# (`Godot.NET.Sdk`), export `.exe` Windows, DWM `per_pixel_transparency`, `window_set_mouse_passthrough`, `Shift+drag`, IPC Named Pipe, `NV08`, hay `E02a T05`.

## 2. Danh sách File Sở hữu (`B00-02` — 5/5 file)

1. `docs/experiments/bootstrap-desktop-body.md` (báo cáo này)
2. `tests/bootstrap/desktop-body/GodotFixture/project.godot`
3. `tests/bootstrap/desktop-body/GodotFixture/export_presets.cfg`
4. `tests/bootstrap/desktop-body/GodotFixture/scenes/Bootstrap.tscn`
5. `tests/bootstrap/desktop-body/GodotFixture/scripts/BootstrapVerify.gd`

## 3. Kết quả Thực thi Thực tế (Chặng B, Cô lập `TEMP` + Process-Scoped `DOTNET_ROOT`/`PATH`)

- **Thư mục chạy cô lập:** `C:\Users\phamp\AppData\Local\Temp\nyua-b00-02-bf15060b` (đã xóa sau khi thu log/hash; `GODOT_PROCS_LEFT=0`; `tests/bootstrap/desktop-body/GodotFixture/.godot/` không tồn tại trong repo).

| Ca kiểm tra | Lệnh thực tế (Windows PowerShell 5.1 `Invoke-GodotBounded`, `DOTNET_ROOT` + `PATH` cục bộ) | Kỳ vọng | Kết quả thực tế & SHA-256 log | Đánh giá |
|---|---|---|---|---|
| `UW01` Dương | `--headless --path tests/bootstrap/desktop-body/GodotFixture --script scripts/BootstrapVerify.gd --quit --log-file "<TEMP>\UW01-pos.log"` (`120000` ms) | `TimedOut=False`, `ExitCode=0` | `TimedOut=False`, `ExitCode=0`, log `[NYUA-B00-02] Bootstrap.tscn instantiated OK (positive headless smoke).` (`SHA-256: 81cf5b7392043c29596f2acfc43725b17d0a1b80c9505cf62b8e8478258d478e`) | **PASS** |
| `UW01` Âm | `--headless --path tests/bootstrap/desktop-body/GodotFixture --script scripts/BootstrapVerify.gd --quit --log-file "<TEMP>\UW01-neg.log" -- --probe-neg` (`120000` ms) | `TimedOut=False`, `ExitCode!=0` | `TimedOut=False`, `ExitCode=1`, log `[NYUA-B00-02] Deliberate negative control (--probe-neg) -> exit 1.` (`SHA-256: d2e3eb49f95fc872ba5f8b0b95fb682fe8312c4262376e7b1f3e29d2adcc5f2f`) | **PASS** (expected negative fail) |
| `UW02` Hang | `--headless --path tests/bootstrap/desktop-body/GodotFixture --script scripts/BootstrapVerify.gd --log-file "<TEMP>\UW02-hang.log" -- --probe-hang` (`5000` ms <= `120s`) | `TimedOut=True`, `taskkill /T /F`, `ExitCode=124` | `TimedOut=True`, `ExitCode=124`, log `[NYUA-B00-02] Entering deliberate hang (--probe-hang) for UW02 supervisor kill-tree check...` (`SHA-256: 879bb1311912ccd0ec1ed04d9f00d788988537ce7597c9189e088c6ff9419849`), `GODOT_PROCS_LEFT=0` | **PASS** (supervisor kill-tree) |
