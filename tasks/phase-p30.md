# P30 task cards

Generated from docs/product/AI/backlog.json. Grouping is navigation only; dependencies below determine dispatch. No phase-level edges. All future work requires separate authorization.

## [P30-01] Needs/sleep/rest và elapsed reconciliation

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

life-state

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

core

**Mã yêu cầu:**

SH01, SH02, SH03, QD04

**Quyết định / rào cản:**

D-05, D-12

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Basic life clock

**Phụ thuộc:**

P00-02, P50-01, B00-05, A00-05, A00-12

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

src/Host/LifeState/NeedsClock.cs; src/Host/LifeState/ElapsedReconciler.cs; tests/Unit/NeedsClockTests.cs

**Các bước cụ thể:**

1. Đối chiếu SH01, SH02, SH03 với mục tiêu: Needs/sleep/rest và elapsed reconciliation. Đọc quyết định D-05, D-12; khóa lại phạm vi đầu ra Basic life clock.
2. Thực hiện lát có thể nghiệm thu riêng trong src/Host/LifeState/NeedsClock.cs; src/Host/LifeState/ElapsedReconciler.cs; tests/Unit/NeedsClockTests.cs sau khi được cho phép: Needs/sleep phản ứng clock/fatigue, reservefood/no heavyabsencepenalty. Nếu cần thêm file hoặc thay hợp đồng, chia lát và cập nhật whitelist trước Ready.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: Appclosed elapsed nofakeevents; inactiveprofilefreeze distinct. Không dùng kết quả mẫu giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap: SH01–03 unit logicalclock + restart fixtures. Lệnh chính xác do B00-05 xác minh; lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P30-01-01: Needs/sleep phản ứng clock/fatigue, reservefood/no heavyabsencepenalty.
- [ ] AT-P30-01-02: Appclosed elapsed nofakeevents; inactiveprofilefreeze distinct.
- [ ] AT-P30-01-03: AT-SH01 — D-12: Khi nhân vật ngủ dừng quan sát; thức dậy chỉ tiếp tục trong quyền hiện hành, không vượt SafetyHold/Thử đọc lại. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate.
- [ ] AT-P30-01-04: AT-QD04 — D-12: Nhân vật ngủ dừng quan sát; thức dậy không tự cấp quyền hoặc bỏ qua SafetyHold/Thử đọc lại. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-05", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "SH01–03 unit logicalclock + restart fixtures."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-05

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

SH01, SH02, SH03, QD04

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [P30-02] Lựa chọn hoạt động, mood và attention limits

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

life-state

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

core

**Mã yêu cầu:**

SP01, SP08, SH06, XP03, XP10

**Quyết định / rào cản:**

D-05

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Activity selection/state

**Phụ thuộc:**

P30-01, B00-05, A00-05

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

src/Host/LifeState/ActivitySelector.cs; src/Host/LifeState/AttentionClock.cs; tests/Unit/ActivitySelectorTests.cs

**Các bước cụ thể:**

1. Đối chiếu SP01, SP08, SH06, XP03, XP10 với mục tiêu: Lựa chọn hoạt động, mood và attention limits. Đọc quyết định D-05; khóa lại phạm vi đầu ra Activity selection/state.
2. Thực hiện lát có thể nghiệm thu riêng trong src/Host/LifeState/ActivitySelector.cs; src/Host/LifeState/AttentionClock.cs; tests/Unit/ActivitySelectorTests.cs sau khi được cho phép: Causalchoices from needs/mood/preferences/memory, canchangeintent; noOSpranks. Nếu cần thêm file hoặc thay hợp đồng, chia lát và cập nhật whitelist trước Ready.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: Invitation/tease share2attempts/>=30min, ignore→selfplay. Không dùng kết quả mẫu giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap: SP01/08 SH05/06 XP03/10 causal scenarios. Lệnh chính xác do B00-05 xác minh; lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P30-02-01: Causalchoices from needs/mood/preferences/memory, canchangeintent; noOSpranks.
- [ ] AT-P30-02-02: Invitation/tease share2attempts/>=30min, ignore→selfplay.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-05", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "SP01/08 SH05/06 XP03/10 causal scenarios."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-05

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

SP01, SP08, SH06, XP03, XP10

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [P30-04] Memory provenance, pin/fade/edit/delete

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

life-state

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

core

**Mã yêu cầu:**

QD09, QD11, KN01, KN02

**Quyết định / rào cản:**

D-08

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Memory lifecycle

**Phụ thuộc:**

P50-01, P10-01, B00-05, A00-08

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

src/Host/LifeState/MemoryService.cs; src/Host/Storage/ContributionStore.cs; tests/Integration/MemoryTests.cs

**Các bước cụ thể:**

1. Đối chiếu QD09, QD11, KN01, KN02 với mục tiêu: Memory provenance, pin/fade/edit/delete. Đọc quyết định D-08; khóa lại phạm vi đầu ra Memory lifecycle.
2. Thực hiện lát có thể nghiệm thu riêng trong src/Host/LifeState/MemoryService.cs; src/Host/Storage/ContributionStore.cs; tests/Integration/MemoryTests.cs sau khi được cho phép: Documenttopiconly, no clipboard/secretlasting; pin/fade/provenance guards. Nếu cần thêm file hoặc thay hợp đồng, chia lát và cập nhật whitelist trước Ready.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: Editno relationrecalc; explicitdelete inverseonce vs naturalfade keepscloseness. Không dùng kết quả mẫu giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap: IT-13 with duplicatedelete/revoke/cache fixtures. Lệnh chính xác do B00-05 xác minh; lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P30-04-01: Documenttopiconly, no clipboard/secretlasting; pin/fade/provenance guards.
- [ ] AT-P30-04-02: Editno relationrecalc; explicitdelete inverseonce vs naturalfade keepscloseness.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-05", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "IT-13 with duplicatedelete/revoke/cache fixtures."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-05

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

QD09, QD11, KN01, KN02

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [P30-03] Quan hệ sâu, neglect và làm lành

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

life-state

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

core

**Mã yêu cầu:**

QH01, QH03, QH04, QH05, QH06, QH07

**Quyết định / rào cản:**

D-05

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Relationship state machine

**Phụ thuộc:**

P30-02, P30-04, B00-05, A00-05

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

src/Host/LifeState/RelationshipEngine.cs; src/Host/LifeState/NeglectClock.cs; tests/Unit/RelationshipTests.cs

**Các bước cụ thể:**

1. Đối chiếu QH01, QH03, QH04, QH05, QH06, QH07 với mục tiêu: Quan hệ sâu, neglect và làm lành. Đọc quyết định D-05; khóa lại phạm vi đầu ra Relationship state machine.
2. Thực hiện lát có thể nghiệm thu riêng trong src/Host/LifeState/RelationshipEngine.cs; src/Host/LifeState/NeglectClock.cs; tests/Unit/RelationshipTests.cs sau khi được cho phép: Eligibleactiveclock48–72h directionaltrust/hurt, no absence/basicpenalty. Nếu cần thêm file hoặc thay hợp đồng, chia lát và cập nhật whitelist trước Ready.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: Firstthrow/repeat/refusal/selfhide/invite/gifts gradual multisessionrepair đúng. Không dùng kết quả mẫu giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap: IT-07/08/12 with logicalclock and narrativeapproval. Lệnh chính xác do B00-05 xác minh; lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P30-03-01: Eligibleactiveclock48–72h directionaltrust/hurt, no absence/basicpenalty.
- [ ] AT-P30-03-02: Firstthrow/repeat/refusal/selfhide/invite/gifts gradual multisessionrepair đúng.
- [ ] AT-P30-03-03: AT-QH05 — D-05/H03: Buổi làm lành có thể cùng ngày nếu có khoảng nghỉ và tương tác thật; đóng/mở app hoặc quà liên tục không là buổi mới. Không tự đặt số phút/số buổi hoặc quà lập tức xóa tổn thương. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-05", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "IT-07/08/12 with logicalclock and narrativeapproval."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-05

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

QH01, QH03, QH04, QH05, QH06, QH07

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [P30-05] Học gu từ user media evidence

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

life-state

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

core

**Mã yêu cầu:**

XP11, XP12, XP13, XP14

**Quyết định / rào cản:**

D-16

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Media preference inference

**Phụ thuộc:**

P30-04, P10-02, B00-05, A00-16

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

src/Host/LifeState/MediaPreferences.cs; contracts/MediaEvidence.cs; tests/Unit/MediaPreferenceTests.cs

**Các bước cụ thể:**

1. Đối chiếu XP11, XP12, XP13, XP14 với mục tiêu: Học gu từ user media evidence. Đọc quyết định D-16; khóa lại phạm vi đầu ra Media preference inference.
2. Thực hiện lát có thể nghiệm thu riêng trong src/Host/LifeState/MediaPreferences.cs; contracts/MediaEvidence.cs; tests/Unit/MediaPreferenceTests.cs sau khi được cho phép: Movie20min/musicrepeat + usertransitions, selfopen does not prove presence. Nếu cần thêm file hoặc thay hợp đồng, chia lát và cập nhật whitelist trước Ready.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: No browserhistory/backgroundcontent/audioanalysis, preference notcertaintylike. Không dùng kết quả mẫu giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap: AT-XP11–14 controllednavigation/duration fixtures. Lệnh chính xác do B00-05 xác minh; lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P30-05-01: Movie20min/musicrepeat + usertransitions, selfopen does not prove presence.
- [ ] AT-P30-05-02: No browserhistory/backgroundcontent/audioanalysis, preference notcertaintylike.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-05", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "AT-XP11–14 controllednavigation/duration fixtures."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-05

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

XP11, XP12, XP13, XP14

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [P30-06] Mode preservation, personality và romance opt-in

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

life-state

**Môi trường và mô hình chính xác:**

{"harness": "codex", "model": "gpt-6.1-sol", "effort": "low"}

**Vai trò:**

core

**Mã yêu cầu:**

SP07, MC03, QH02

**Quyết định / rào cản:**

D-05

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Advanced state transitions

**Phụ thuộc:**

P30-03, P03-04, B00-05, A00-05

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

src/Host/LifeState/ModeTransition.cs; src/Host/LifeState/RomanceTransition.cs; tests/Integration/AdvancedStateTests.cs

**Các bước cụ thể:**

1. Đối chiếu SP07, MC03, QH02 với mục tiêu: Mode preservation, personality và romance opt-in. Đọc quyết định D-05; khóa lại phạm vi đầu ra Advanced state transitions.
2. Thực hiện lát có thể nghiệm thu riêng trong src/Host/LifeState/ModeTransition.cs; src/Host/LifeState/RomanceTransition.cs; tests/Integration/AdvancedStateTests.cs sau khi được cho phép: Downgrade preservesstate and suspendsdeeppenalty/expression, reenablecontinues. Nếu cần thêm file hoặc thay hợp đồng, chia lát và cập nhật whitelist trước Ready.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: Romanceoff keep/delete respectschoice; personalitymatures withoutlosingcorenets. Không dùng kết quả mẫu giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap: IT-12 + user narrative review and deletecases. Lệnh chính xác do B00-05 xác minh; lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P30-06-01: Downgrade preservesstate and suspendsdeeppenalty/expression, reenablecontinues.
- [ ] AT-P30-06-02: Romanceoff keep/delete respectschoice; personalitymatures withoutlosingcorenets.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-05", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "IT-12 + user narrative review and deletecases."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-05

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

SP07, MC03, QH02

**Mã phi chức năng:**

See linked requirement / prerequisite scope.
