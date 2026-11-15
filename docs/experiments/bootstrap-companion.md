# Báo cáo Bootstrap `B00-01` — Companion (.NET 10 LTS Test Runner)

- **Trạng thái thực thi:** **`PASS` (Bootstrap `B00-01` / `UW01-companion` + `UW02` timeout supervisor)** — đã chạy thực tế theo ủy quyền **Chặng B** của người dùng; **CHƯA** chạy bất kỳ ca sản phẩm `UW03–UW30` nào.
- **Thời điểm thực thi:** `2026-11-15T23:52+07:00`
- **Ủy quyền phạm vi:** Người dùng đã duyệt **Chặng B** theo kế hoạch `b00-bootstrap-plan.md` rev5 (`SHA-256: c1f4dc7df184da96ff0d6c73c53c318ade8f6e1515147450f388ac3090e704d1`). Giữ nguyên 4 file whitelist của `B00-01`, không sửa `docs/product/AI/backlog.json`, `tasks/phase-*.md` hay `.gitignore` (toàn bộ 219 task trong `backlog.json` giữ `DRAFT_NOT_AUTHORIZED` / `BLOCKED_SCOPE_AUTHORIZATION` theo `tasks/validate_tasks.py` L29; `P00-01` chưa tự đóng).

## 1. Công cụ, Phiên bản & Giấy phép (`$0`)

- **Runtime / SDK:** `.NET SDK 10.0.404` tại `C:\Users\phamp\.ao\data\tools\nyua-dotnet\dotnet.exe` (runtimes `10.0.15`, `win-x64`, giấy phép MIT, `$0`, `PATH` hệ thống không bị thay đổi).
- **NuGet Packages (offline cache `C:\Users\phamp\.nuget\packages`, 0 mạng, `$0`):**
  - `Microsoft.NET.Test.Sdk` `17.14.1` (MIT)
  - `MSTest.TestAdapter` `3.8.3` (MIT)
  - `MSTest.TestFramework` `3.8.3` (MIT)
- **Dữ liệu thử & Bảo mật:** 100% giá trị tổng hợp (`syntheticSeed = 42`), không dữ liệu cá nhân, không mạng, không UI/input/capture thật.

## 2. Danh sách File Sở hữu (`B00-01` — 4/4 file)

1. `docs/experiments/bootstrap-companion.md` (báo cáo này)
2. `tests/bootstrap/companion/Bootstrap.Tests.csproj`
3. `tests/bootstrap/companion/BootstrapTests.cs`
4. `tools/verify/companion.ps1` (Windows PowerShell `5.1.26100.9818`, `System.Diagnostics.Process` + `WaitForExit` + `taskkill /PID ... /T /F`)

## 3. Kết quả Thực thi Thực tế (Chặng B, Cô lập `TEMP`)

- **Thư mục chạy cô lập:** `C:\Users\phamp\AppData\Local\Temp\nyua-b00-01-b31fcf3f` (đã dọn sạch sau khi thu TRX/kết quả; 0 `bin/`/`obj/`/`TestResults/` trong repo).

| Lượt kiểm tra | Lệnh thực tế đã chạy | Kỳ vọng | Kết quả thực tế | Đánh giá |
|---|---|---|---|---|
| `All` (`Restore` + `Positive` + `Negative`) | `powershell -NoProfile -File "tools/verify/companion.ps1" -RunDir "C:\Users\phamp\AppData\Local\Temp\nyua-b00-01-b31fcf3f" -TimeoutSeconds 120 -Mode All` | Supervisor exit `0` (`Restore` `0`, `Positive` `0`, `Negative` `!= 0`) | `Restore`: `TimedOut=False ExitCode=0`; `Positive`: `TimedOut=False ExitCode=0`; `Negative`: `TimedOut=False ExitCode=1`; `ALL_EXIT=0` | **PASS** |
| `NegativeControl` (chạy lẻ) | `powershell -NoProfile -File "tools/verify/companion.ps1" -RunDir "C:\Users\phamp\AppData\Local\Temp\nyua-b00-01-b31fcf3f" -TimeoutSeconds 120 -Mode Negative` | Supervisor truyền exit `!= 0`, TRX fail `> 0` | `TimedOut=False ExitCode=1`, `NEG_STANDALONE_EXIT=1` | **PASS** (expected negative fail) |
| `TimeoutHang` (`UW02`) | `powershell -NoProfile -File "tools/verify/companion.ps1" -RunDir "C:\Users\phamp\AppData\Local\Temp\nyua-b00-01-b31fcf3f" -TimeoutSeconds 5 -Mode Hang` | Timeout `<= 120s`, kill tree, exit `124` (`!= 0`) | `TimedOut=True ExitCode=124`, `HANG_EXIT=124` | **PASS** (supervisor kill-tree) |

### Bằng chứng TRX
- `b00-01-pos.trx`: `total=1 executed=1 passed=1 failed=0 outcome=Completed`
- `b00-01-neg.trx`: `total=1 executed=1 passed=0 failed=1 outcome=Failed`

## 4. Ranh giới Chấp nhận (Không đánh đồng phạm vi)
- Kết quả này chỉ chứng minh runner `.NET 10` cô lập của `B00-01`. Toàn bộ `UW03–UW30`, `NV08`, `E02a T05`, và các gate `P00-01`, `P00-04`, `P00-02`, `P02-*` vẫn **`NOT RUN`** / chưa đóng.
