# P03 task cards

Generated from docs/product/AI/backlog.json. Grouping is navigation only; dependencies below determine dispatch. No phase-level edges. All future work requires separate authorization.

## [P03-01] Sàng lọc model/runtime local có quyền phân phối

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

perception

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-3.8-flash"}

**Vai trò:**

research

**Mã yêu cầu:**

AI01

**Quyết định / rào cản:**

D-04

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Candidate/license matrix

**Phụ thuộc:**

P00-04, B00-03, A00-04

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

docs/experiments/model-candidates.md; docs/licenses/INVENTORY.md

**Các bước cụ thể:**

1. Đối chiếu AI01 với mục tiêu: Sàng lọc model/runtime local có quyền phân phối. Đọc quyết định D-04; khóa lại phạm vi đầu ra Candidate/license matrix.
2. Thực hiện lát có thể nghiệm thu riêng trong docs/experiments/model-candidates.md; docs/licenses/INVENTORY.md sau khi được cho phép: So Vietnamese/image/OCR/offline và redistribution terms thực tế. Nếu cần thêm file hoặc thay hợp đồng, chia lát và cập nhật whitelist trước Ready.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: Không chọn model theo quảng cáo hoặc assumption free=redistributable. Không dùng kết quả mẫu giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap: Primary modelcards/licenses/runtime docs. Lệnh chính xác do B00-03 xác minh; lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P03-01-01: So Vietnamese/image/OCR/offline và redistribution terms thực tế.
- [ ] AT-P03-01-02: Không chọn model theo quảng cáo hoặc assumption free=redistributable.
- [ ] AT-P03-01-03: AT-AI01 — D-16: Chỉ kiểm tra trạng thái đang phát/không phát ở nền để tránh mở chồng; không tên bài/phim/hình/âm thanh/lịch sử hoặc suy gu; lỗi/không rõ không coi là không phát. Cách lấy/độ tin cậy cần kiểm chứng. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-03", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "Primary modelcards/licenses/runtime docs."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-03

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

AI01

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [P03-02] Dựng benchmark dữ liệu cảnh an toàn

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

perception

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

core

**Mã yêu cầu:**

AI03

**Quyết định / rào cản:**

D-04

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Dataset manifest/runner

**Phụ thuộc:**

P03-01, P01-01, B00-03, A00-04

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

tests/Fixtures/Scenes/manifest.json; tools/bench/SceneBench.cs; docs/experiments/local-ai.md

**Các bước cụ thể:**

1. Đối chiếu AI03 với mục tiêu: Dựng benchmark dữ liệu cảnh an toàn. Đọc quyết định D-04; khóa lại phạm vi đầu ra Dataset manifest/runner.
2. Thực hiện lát có thể nghiệm thu riêng trong tests/Fixtures/Scenes/manifest.json; tools/bench/SceneBench.cs; docs/experiments/local-ai.md sau khi được cho phép: Clip có quyền sử dụng, labels/onset/clear-hard cố định trước đo. Nếu cần thêm file hoặc thay hợp đồng, chia lát và cập nhật whitelist trước Ready.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: Input đã biết an toàn, không capture desktop cá nhân hoặc gửi cloud. Không dùng kết quả mẫu giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap: E04 owned-fixture dryrun, confusion/uncertain outputs. Lệnh chính xác do B00-03 xác minh; lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P03-02-01: Clip có quyền sử dụng, labels/onset/clear-hard cố định trước đo.
- [ ] AT-P03-02-02: Input đã biết an toàn, không capture desktop cá nhân hoặc gửi cloud.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-03", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "E04 owned-fixture dryrun, confusion/uncertain outputs."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-03

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

AI03

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [P03-03] Đo phản ứng toàn luồng dưới tải kết hợp

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

perception

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

core

**Mã yêu cầu:**

XP02

**Quyết định / rào cản:**

D-04

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Latency/quality report

**Phụ thuộc:**

P03-02, P02-04, B00-03, A00-04

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

tools/bench/CombinedBench.cs; contracts/SceneTiming.cs; docs/experiments/local-ai.md

**Các bước cụ thể:**

1. Đối chiếu XP02 với mục tiêu: Đo phản ứng toàn luồng dưới tải kết hợp. Đọc quyết định D-04; khóa lại phạm vi đầu ra Latency/quality report.
2. Thực hiện lát có thể nghiệm thu riêng trong tools/bench/CombinedBench.cs; contracts/SceneTiming.cs; docs/experiments/local-ai.md sau khi được cho phép: Đo scenevisible→filter/OCR/infer/decision→renderstart với Unity đang chạy. Nếu cần thêm file hoặc thay hợp đồng, chia lát và cập nhật whitelist trước Ready.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: Báo mọi mẫu sai/uncertain/unobserved, không đổi ngưỡng hoặc chọn lại clip. Không dùng kết quả mẫu giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap: IT-10 timing + RAM/VRAM/CPU/GPU observations. Lệnh chính xác do B00-03 xác minh; lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P03-03-01: Đo scenevisible→filter/OCR/infer/decision→renderstart với Unity đang chạy.
- [ ] AT-P03-03-02: Báo mọi mẫu sai/uncertain/unobserved, không đổi ngưỡng hoặc chọn lại clip.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-03", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "IT-10 timing + RAM/VRAM/CPU/GPU observations."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-03

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

XP02

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [P03-04] Đề xuất hai mức và luồng gói nâng cao

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

companion

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

core

**Mã yêu cầu:**

MC01, MC02, MC04

**Quyết định / rào cản:**

D-04

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Capability recommendation/pack states

**Phụ thuộc:**

P03-03, P00-03, B00-01, A00-04

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

src/Host/Capabilities/ModeAdvisor.cs; src/Desktop.Wpf/ModesView.xaml; tests/Unit/ModeAdvisorTests.cs

**Các bước cụ thể:**

1. Đối chiếu MC01, MC02, MC04 với mục tiêu: Đề xuất hai mức và luồng gói nâng cao. Đọc quyết định D-04; khóa lại phạm vi đầu ra Capability recommendation/pack states.
2. Thực hiện lát có thể nghiệm thu riêng trong src/Host/Capabilities/ModeAdvisor.cs; src/Desktop.Wpf/ModesView.xaml; tests/Unit/ModeAdvisorTests.cs sau khi được cho phép: Recommendation theo envelope đo, user override sau warning được. Nếu cần thêm file hoặc thay hợp đồng, chia lát và cập nhật whitelist trước Ready.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: Download/validate/cancel states rõ, no silent downgrade hoặc gói giảready. Không dùng kết quả mẫu giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap: MC01–04 fixtures cho unsupported/corrupt/offline. Lệnh chính xác do B00-01 xác minh; lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P03-04-01: Recommendation theo envelope đo, user override sau warning được.
- [ ] AT-P03-04-02: Download/validate/cancel states rõ, no silent downgrade hoặc gói giảready.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-01", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "MC01–04 fixtures cho unsupported/corrupt/offline."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-01

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

MC01, MC02, MC04

**Mã phi chức năng:**

See linked requirement / prerequisite scope.
