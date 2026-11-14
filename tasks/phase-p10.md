# P10 task cards

Generated from docs/product/AI/backlog.json. Grouping is navigation only; dependencies below determine dispatch. No phase-level edges. All future work requires separate authorization.

## [P10-01] Triển khai grants mặc định tắt và read/control

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

policy

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

core

**Mã yêu cầu:**

QD01

**Quyết định / rào cản:**

Scope authorization and evidence prerequisites remain open.

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Production grant evaluator

**Phụ thuộc:**

P00-02, P01-01, B00-04

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

src/Host/Policy/GrantEvaluator.cs; src/Host/Policy/GrantState.cs; tests/Unit/GrantEvaluatorTests.cs

**Các bước cụ thể:**

1. Đối chiếu QD01 với mục tiêu: Triển khai grants mặc định tắt và read/control. Đọc quyết định liên quan trong DECISIONS; khóa lại phạm vi đầu ra Production grant evaluator.
2. Thực hiện lát có thể nghiệm thu riêng trong src/Host/Policy/GrantEvaluator.cs; src/Host/Policy/GrantState.cs; tests/Unit/GrantEvaluatorTests.cs sau khi được cho phép: App/site read-control riêng; browserANDsite; newsource defaultdeny. Nếu cần thêm file hoặc thay hợp đồng, chia lát và cập nhật whitelist trước Ready.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: Revoke tăng generation và control không tự bật read. Không dùng kết quả mẫu giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap: AT-QD01/03, production unit/contract negative cases. Lệnh chính xác do B00-04 xác minh; lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P10-01-01: App/site read-control riêng; browserANDsite; newsource defaultdeny.
- [ ] AT-P10-01-02: Revoke tăng generation và control không tự bật read.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-04", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "AT-QD01/03, production unit/contract negative cases."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-04

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

QD01

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [P10-02] Nhận dạng nguồn và vùng đang hiển thị

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

perception

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

core

**Mã yêu cầu:**

QD04, QD06

**Quyết định / rào cản:**

D-15, D-16

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Visible source adapter

**Phụ thuộc:**

P10-01, P02-03, B00-03, A00-15, A00-16

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

src/Host/Perception/VisibleSources.cs; src/BrowserBridge/SourceEvidence.cs; tests/Integration/VisibleSourceTests.cs

**Các bước cụ thể:**

1. Đối chiếu QD04, QD06 với mục tiêu: Nhận dạng nguồn và vùng đang hiển thị. Đọc quyết định D-15, D-16; khóa lại phạm vi đầu ra Visible source adapter.
2. Thực hiện lát có thể nghiệm thu riêng trong src/Host/Perception/VisibleSources.cs; src/BrowserBridge/SourceEvidence.cs; tests/Integration/VisibleSourceTests.cs sau khi được cho phép: Nguồn nền/thu nhỏ/bịche không được truyền nội dung; splitview đúng grants. Nếu cần thêm file hoặc thay hợp đồng, chia lát và cập nhật whitelist trước Ready.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: Không mở mail gây mark-read; unsupportedsource chặn và giải thích. Không dùng kết quả mẫu giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap: IT-01/02 với owned app/browser fixture. Lệnh chính xác do B00-03 xác minh; lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P10-02-01: Nguồn nền/thu nhỏ/bịche không được truyền nội dung; splitview đúng grants.
- [ ] AT-P10-02-02: Không mở mail gây mark-read; unsupportedsource chặn và giải thích.
- [ ] AT-P10-02-03: AT-QD04 — D-12: Nhân vật ngủ dừng quan sát; thức dậy không tự cấp quyền hoặc bỏ qua SafetyHold/Thử đọc lại. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-03", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "IT-01/02 với owned app/browser fixture."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-03

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

QD04, QD06

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [P10-03] Lọc sensitive/private và retry hold trên nguồn thật

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

policy

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

core

**Mã yêu cầu:**

QD05, QD15, SH01

**Quyết định / rào cản:**

D-15

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Safe snapshot boundary

**Phụ thuộc:**

P10-02, B00-04, A00-15

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

src/Host/Policy/SafetyHold.cs; src/Host/Perception/SafeSnapshotBuilder.cs; tests/Integration/SafeSnapshotTests.cs

**Các bước cụ thể:**

1. Đối chiếu QD05, QD15 với mục tiêu: Lọc sensitive/private và retry hold trên nguồn thật. Đọc quyết định D-15; khóa lại phạm vi đầu ra Safe snapshot boundary.
2. Thực hiện lát có thể nghiệm thu riêng trong src/Host/Policy/SafetyHold.cs; src/Host/Perception/SafeSnapshotBuilder.cs; tests/Integration/SafeSnapshotTests.cs sau khi được cho phép: No forbidden sentinel in OCR/model/memory/log; unknownwholewindow hold. Nếu cần thêm file hoặc thay hợp đồng, chia lát và cập nhật whitelist trước Ready.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: Explicit retry validates mới, revoke/change trongpipeline discard. Không dùng kết quả mẫu giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap: E02/IT-01/02 inspect actual consumers, not previewonly. Lệnh chính xác do B00-04 xác minh; lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P10-03-01: No forbidden sentinel in OCR/model/memory/log; unknownwholewindow hold.
- [ ] AT-P10-03-02: Explicit retry validates mới, revoke/change trongpipeline discard.
- [ ] AT-P10-03-03: AT-SH01 — D-12: Khi nhân vật ngủ dừng quan sát; thức dậy chỉ tiếp tục trong quyền hiện hành, không vượt SafetyHold/Thử đọc lại. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-04", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "E02/IT-01/02 inspect actual consumers, not previewonly."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-04

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

SH01, QD05, QD15

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [P10-04] Kiểm chứng clipboard history đúng Win+V scope

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

perception

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

core

**Mã yêu cầu:**

QD08

**Quyết định / rào cản:**

D-15

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Clipboard adapter/proof

**Phụ thuộc:**

P10-03, B00-03, A00-15

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

src/Host/Perception/ClipboardScope.cs; tests/Integration/ClipboardScopeTests.cs; docs/experiments/clipboard.md

**Các bước cụ thể:**

1. Đối chiếu QD08 với mục tiêu: Kiểm chứng clipboard history đúng Win+V scope. Đọc quyết định D-15; khóa lại phạm vi đầu ra Clipboard adapter/proof.
2. Thực hiện lát có thể nghiệm thu riêng trong src/Host/Perception/ClipboardScope.cs; tests/Integration/ClipboardScopeTests.cs; docs/experiments/clipboard.md sau khi được cho phép: Có evidence bảng open/close đúng trước đọc history; không tự bật setting. Nếu cần thêm file hoặc thay hợp đồng, chia lát và cập nhật whitelist trước Ready.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: Đóng giữa chừng hủy buffer và no memory/log persistence. Không dùng kết quả mẫu giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap: K04 official API + owned clipboard fixtures IT-13. Lệnh chính xác do B00-03 xác minh; lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P10-04-01: Có evidence bảng open/close đúng trước đọc history; không tự bật setting.
- [ ] AT-P10-04-02: Đóng giữa chừng hủy buffer và no memory/log persistence.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-03", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "K04 official API + owned clipboard fixtures IT-13."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-03

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

QD08

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [P10-05] Luồng AI ngoài có preview và consent mỗi lần

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

policy

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

core

**Mã yêu cầu:**

AI02

**Quyết định / rào cản:**

D-07, D-18

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Explicit text-only request

**Phụ thuộc:**

P10-03, P50-01, B00-04, A00-07, A00-18

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

src/Host/ExternalAI/ConsentRequest.cs; src/Desktop.Wpf/ExternalAIView.xaml; tests/Integration/ExternalAIConsentTests.cs

**Các bước cụ thể:**

1. Đối chiếu AI02 với mục tiêu: Luồng AI ngoài có preview và consent mỗi lần. Đọc quyết định D-07, D-18; khóa lại phạm vi đầu ra Explicit text-only request.
2. Thực hiện lát có thể nghiệm thu riêng trong src/Host/ExternalAI/ConsentRequest.cs; src/Desktop.Wpf/ExternalAIView.xaml; tests/Integration/ExternalAIConsentTests.cs sau khi được cho phép: Exactsafe text+destination preview; payload/sourcechange invalidatesconsent. Nếu cần thêm file hoặc thay hợp đồng, chia lát và cập nhật whitelist trước Ready.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: Reject/retry/offline no auto fallback or forbidden category send. Không dùng kết quả mẫu giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap: UC-13 mockprovider payload audit and errors. Lệnh chính xác do B00-04 xác minh; lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P10-05-01: Exactsafe text+destination preview; payload/sourcechange invalidatesconsent.
- [ ] AT-P10-05-02: Reject/retry/offline no auto fallback or forbidden category send.
- [ ] AT-P10-05-03: AT-AI02 — D-18: Gửi chữ lỗi/chưa rõ thành công thì báo lỗi và chờ bấm thử lại; xem/duyệt chữ trước mỗi lần gửi mới kể cả chữ không đổi. Không tự gửi lại, không coi timeout là chưa nhận, không mở rộng loại dữ liệu/quyền. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-04", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "UC-13 mockprovider payload audit and errors."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-04

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

AI02

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [P10-06] Bridge trình duyệt và ngoại lệ khung video

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

perception

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

core

**Mã yêu cầu:**

QD12, QD13, QD14

**Quyết định / rào cản:**

D-03, D-15

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Optional extension/frame binding

**Phụ thuộc:**

P10-03, P00-04, B00-03, A00-03, A00-15

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

src/BrowserBridge/Extension/manifest.json; src/BrowserBridge/FrameBinding.cs; tests/Integration/FrameBindingTests.cs

**Các bước cụ thể:**

1. Đối chiếu QD12, QD13, QD14 với mục tiêu: Bridge trình duyệt và ngoại lệ khung video. Đọc quyết định D-03, D-15; khóa lại phạm vi đầu ra Optional extension/frame binding.
2. Thực hiện lát có thể nghiệm thu riêng trong src/BrowserBridge/Extension/manifest.json; src/BrowserBridge/FrameBinding.cs; tests/Integration/FrameBindingTests.cs sau khi được cho phép: Chrome/Edge web requires extension only whenenabled; no broad grants. Nếu cần thêm file hoặc thay hợp đồng, chia lát và cập nhật whitelist trước Ready.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: Crossoriginplayer identified/confirmed scopedparent; mismatch asksagain. Không dùng kết quả mẫu giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap: QD12–14 browser integration + ads/redirect negatives. Lệnh chính xác do B00-03 xác minh; lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P10-06-01: Chrome/Edge web requires extension only whenenabled; no broad grants.
- [ ] AT-P10-06-02: Crossoriginplayer identified/confirmed scopedparent; mismatch asksagain.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-03", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "QD12–14 browser integration + ads/redirect negatives."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-03

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

QD12, QD13, QD14

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [P10-07] Input arbitration và các nút dừng

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

policy

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

core

**Mã yêu cầu:**

DK01, DK02, DK03, DK04, XP08

**Quyết định / rào cản:**

D-05, D-11

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Stop/input gate

**Phụ thuộc:**

P10-01, P02-05, B00-04, A00-05, A00-11

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

src/Host/Policy/InputGate.cs; src/Host/Policy/StopController.cs; tests/Integration/InputGateTests.cs

**Các bước cụ thể:**

1. Đối chiếu DK01, DK02, DK03, DK04, XP08 với mục tiêu: Input arbitration và các nút dừng. Đọc quyết định D-05, D-11; khóa lại phạm vi đầu ra Stop/input gate.
2. Thực hiện lát có thể nghiệm thu riêng trong src/Host/Policy/InputGate.cs; src/Host/Policy/StopController.cs; tests/Integration/InputGateTests.cs sau khi được cho phép: Humaninput vs injected classified withoutkeycontent, idle60s/unlockexception đúng. Nếu cần thêm file hoặc thay hợp đồng, chia lát và cập nhật whitelist trước Ready.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: Emergency/off/hide matrix + generation prevents lateraction; sleepedge resolved. Không dùng kết quả mẫu giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap: IT-06, input injection fakeadapter first then reviewed realtests. Lệnh chính xác do B00-04 xác minh; lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P10-07-01: Humaninput vs injected classified withoutkeycontent, idle60s/unlockexception đúng.
- [ ] AT-P10-07-02: Emergency/off/hide matrix + generation prevents lateraction; sleepedge resolved.
- [ ] AT-P10-07-03: AT-XP08 — D-11: Máy ngủ không cộng thời gian chờ mở phim/nhạc; máy thức tiếp tục phần còn lại, không reset chỉ vì thức. Giữ quyền/khóa/input/phát đã chốt, máy ngủ khác nhân vật ngủ. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-04", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "IT-06, input injection fakeadapter first then reviewed realtests."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-04

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

DK01, DK02, DK03, DK04, XP08

**Mã phi chức năng:**

See linked requirement / prerequisite scope.
