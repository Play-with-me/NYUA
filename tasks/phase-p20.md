# P20 task cards

Generated from docs/product/AI/backlog.json. Grouping is navigation only; dependencies below determine dispatch. No phase-level edges. All future work requires separate authorization.

## [P20-01] Duyệt model sheet nhân vật gốc

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

desktop-body

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-4-hydrogen-low"}

**Vai trò:**

ui-features

**Mã yêu cầu:**

NV01, NV02, NV03, NV04

**Quyết định / rào cản:**

D-14

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Approved art reference

**Phụ thuộc:**

P00-04, B00-02, A00-14

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

art/character/model-sheet.png; art/character/manifest.json; docs/art/approval.md

**Các bước cụ thể:**

1. Đối chiếu NV01, NV02, NV03, NV04 với mục tiêu: Duyệt model sheet nhân vật gốc. Đọc quyết định D-14; khóa lại phạm vi đầu ra Approved art reference.
2. Thực hiện lát có thể nghiệm thu riêng trong art/character/model-sheet.png; art/character/manifest.json; docs/art/approval.md sau khi được cho phép: Đúng adultchibi/appearance/anatomicalclip và source128. Nếu cần thêm file hoặc thay hợp đồng, chia lát và cập nhật whitelist trước Ready.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: User duyệt sample; provenance/license recorded, no borrowedcharacter. Không dùng kết quả mẫu giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap: E01 review ở64/128/192/384. Lệnh chính xác do B00-02 xác minh; lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P20-01-01: Đúng adultchibi/appearance/anatomicalclip và source128.
- [ ] AT-P20-01-02: User duyệt sample; provenance/license recorded, no borrowedcharacter.
- [ ] AT-P20-01-03: AT-NV01 — D-14: Nhân vật chính chủ yếu hình người về mặt/dáng/đi đứng, không mõm cáo/bàn chân động vật. Chỉ đôi tai cáo trên đầu, không tai người; tai trắng bạc lòng hồng nhạt; một đuôi cáo trắng bạc. Giữ nữ trưởng thành chibi anime pixel 128x128, tóc trắng bạc ngang eo/mái thưa, mắt đỏ hồng, da sáng ấm, áo len rộng cổ tròn hồng nhạt, váy xếp ly xám đậm trên gối, chân trần, kẹp tim đỏ rượu bên phải nhân vật. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate.
- [ ] AT-P20-01-04: AT-NV02 — D-14: Giữ tóc/mắt/da đã chốt; tai trắng bạc lòng hồng nhạt và một đuôi trắng bạc đồng bộ tóc. Chỉ tai cáo, không tai người; không thay ngoại hình đã duyệt. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-02", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "E01 review ở64/128/192/384."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-02

**Gate nghiệm thu người dùng:**

{"required": true, "status": "NOT_OBTAINED", "evidence": null, "condition": "Actual user response on the exact reviewed artifact/revision is mandatory; automated or AI review cannot satisfy this gate."}

**Owner triển khai cho yêu cầu:**

NV01, NV02, NV03, NV04

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [P20-02] Di chuyển và bề mặt cửa sổ

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

desktop-body

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-4-hydrogen-low"}

**Vai trò:**

ui-features

**Mã yêu cầu:**

NV05, NV07, QD10

**Quyết định / rào cản:**

D-01

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Locomotion/surface model

**Phụ thuộc:**

P20-01, P02-03, P02-05, B00-02, A00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

godot/CompanionRenderer/scripts/SurfaceWorld.cs; godot/CompanionRenderer/scripts/BodyMotion.cs; tests/Integration/SurfaceWorldTests.cs

**Các bước cụ thể:**

1. Đối chiếu NV05, NV07, QD10 với mục tiêu: Di chuyển và bề mặt cửa sổ. Đọc quyết định D-01; khóa lại phạm vi đầu ra Locomotion/surface model.
2. Thực hiện lát có thể nghiệm thu riêng trong godot/CompanionRenderer/scripts/SurfaceWorld.cs; godot/CompanionRenderer/scripts/BodyMotion.cs; tests/Integration/SurfaceWorldTests.cs sau khi được cho phép: Followmovingwindow; closesupport→fall→land/stand đúng. Nếu cần thêm file hoặc thay hợp đồng, chia lát và cập nhật whitelist trước Ready.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: Geometryonly inputs và forbiddenwindowtitles không lọt renderer. Không dùng kết quả mẫu giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap: AT-NV05/07/QD10 + fixture window lifecycle. Lệnh chính xác do B00-02 xác minh; lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P20-02-01: Followmovingwindow; closesupport→fall→land/stand đúng.
- [ ] AT-P20-02-02: Geometryonly inputs và forbiddenwindowtitles không lọt renderer.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-02", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "AT-NV05/07/QD10 + fixture window lifecycle."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-02

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

NV05, NV07, QD10

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [P20-03] Pet/lift/throw và chuyển vị trí an toàn

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

desktop-body

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-4-hydrogen-low"}

**Vai trò:**

ui-features

**Mã yêu cầu:**

NV09, NV11, SH05

**Quyết định / rào cản:**

D-05

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Gesture recognizer

**Phụ thuộc:**

P20-02, P30-02, B00-02, A00-05

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

godot/CompanionRenderer/scripts/Gestures.cs; contracts/AvatarInteraction.cs; tests/Integration/GestureTests.cs

**Các bước cụ thể:**

1. Đối chiếu NV09, NV11, SH05 với mục tiêu: Pet/lift/throw và chuyển vị trí an toàn. Đọc quyết định D-05; khóa lại phạm vi đầu ra Gesture recognizer.
2. Thực hiện lát có thể nghiệm thu riêng trong godot/CompanionRenderer/scripts/Gestures.cs; contracts/AvatarInteraction.cs; tests/Integration/GestureTests.cs sau khi được cho phép: Phân biệt các gestures bằng ngưỡng đã đo/chốt, no accidentalthrow từ slowmove. Nếu cần thêm file hoặc thay hợp đồng, chia lát và cập nhật whitelist trước Ready.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: Refusallift giữ; modifierreposition neutral, readinessgesture có. Không dùng kết quả mẫu giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap: AT-NV09/11/SH05/QH06 + UX gestureplaytest. Lệnh chính xác do B00-02 xác minh; lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P20-03-01: Phân biệt các gestures bằng ngưỡng đã đo/chốt, no accidentalthrow từ slowmove.
- [ ] AT-P20-03-02: Refusallift giữ; modifierreposition neutral, readinessgesture có.
- [ ] AT-P20-03-03: AT-NV11 — D-05: Giữ Shift rồi kéo chuyển vị trí kể cả khi từ chối nhấc; không chơi/quăng hay ảnh hưởng quan hệ, không thêm tùy chọn phím; ngưỡng cử chỉ còn phải đo. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-02", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "AT-NV09/11/SH05/QH06 + UX gestureplaytest."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-02

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

NV09, NV11, SH05

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [P20-04] Foodtray, đồ vật và animatedcleanup

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

desktop-body

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-4-hydrogen-low"}

**Vai trò:**

ui-features

**Mã yêu cầu:**

SH04, SH07, SH08, XP09

**Quyết định / rào cản:**

D-14

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Food/prop interaction

**Phụ thuộc:**

P20-02, P30-01, B00-02, A00-14

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

godot/CompanionRenderer/scripts/PropWorld.cs; src/Host/LifeState/FoodInteraction.cs; tests/Integration/PropWorldTests.cs

**Các bước cụ thể:**

1. Đối chiếu SH04, SH07, SH08, XP09 với mục tiêu: Foodtray, đồ vật và animatedcleanup. Đọc quyết định D-14; khóa lại phạm vi đầu ra Food/prop interaction.
2. Thực hiện lát có thể nghiệm thu riêng trong godot/CompanionRenderer/scripts/PropWorld.cs; src/Host/LifeState/FoodInteraction.cs; tests/Integration/PropWorldTests.cs sau khi được cho phép: Đủ6foods; tray/lẻ/refusal behavior; max5left with inuse exemption. Nếu cần thêm file hoặc thay hợp đồng, chia lát và cập nhật whitelist trước Ready.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: Sixthleft waits animatedputaway; usermove/hide always available. Không dùng kết quả mẫu giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap: AT-SH04/07/08/XP09 + interactionstate fixtures. Lệnh chính xác do B00-02 xác minh; lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P20-04-01: Đủ6foods; tray/lẻ/refusal behavior; max5left with inuse exemption.
- [ ] AT-P20-04-02: Sixthleft waits animatedputaway; usermove/hide always available.
- [ ] AT-P20-04-03: AT-SH04 — D-14/H08: Trong sáu món đã chốt, trái cây là táo, nước trái cây là nước cam; không thêm món thứ bảy. Thú bông thỏ là đồ vật/quà riêng, không nhân vật chính. Màu/chi tiết thú bông, dụng cụ/hình mẫu còn chờ duyệt. Kiểm case cho phép, từ chối và gián đoạn ở đầu ra của task này; ghi expected/actual hoặc NOT RUN, không tự đóng human gate.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-02", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "AT-SH04/07/08/XP09 + interactionstate fixtures."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-02

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

SH04, SH07, SH08, XP09

**Mã phi chức năng:**

See linked requirement / prerequisite scope.

## [P20-05] Placement nhiều màn hình và fullscreen

**Trạng thái / điều kiện bắt đầu:**

DRAFT_NOT_AUTHORIZED / BLOCKED_SCOPE_AUTHORIZATION

**Phân hệ:**

desktop-body

**Môi trường và mô hình chính xác:**

{"harness": "agy", "model": "gemini-4-hydrogen-low"}

**Vai trò:**

ui-features

**Mã yêu cầu:**

NV08

**Quyết định / rào cản:**

D-01

**Đầu vào:**

docs/YEU_CAU_HIEN_HANH.md; docs/product/AI/SRS.md; docs/product/AI/DECISIONS.md

**Đầu ra:**

Placement/support matrix

**Phụ thuộc:**

P20-02, P02-02, B00-02, A00-01

**File thực có trong phạm vi dự kiến:**

None; all below are proposed.

**Whitelist đề xuất — chưa cho phép sửa sản phẩm:**

src/Host/Geometry/MonitorSelection.cs; godot/CompanionRenderer/scripts/Placement.cs; tests/Integration/PlacementTests.cs

**Các bước cụ thể:**

1. Đối chiếu NV08 với mục tiêu: Placement nhiều màn hình và fullscreen. Đọc quyết định D-01; khóa lại phạm vi đầu ra Placement/support matrix.
2. Thực hiện lát có thể nghiệm thu riêng trong src/Host/Geometry/MonitorSelection.cs; godot/CompanionRenderer/scripts/Placement.cs; tests/Integration/PlacementTests.cs sau khi được cho phép: Onlychosenmonitors, fullscreenedge withoutmidcenter obstruction. Nếu cần thêm file hoặc thay hợp đồng, chia lát và cập nhật whitelist trước Ready.
3. Kiểm nhánh lỗi/gián đoạn và bất biến riêng của lát: MixedDPI and unsupportedexclusive modes documented; not universalgame promise. Không dùng kết quả mẫu giả thay nguồn thật.
4. Chuẩn bị và chạy sau bootstrap: IT-05 native hardware matrix. Lệnh chính xác do B00-02 xác minh; lưu expected/actual từng case, exit code và revision, không đánh dấu nghiệm thu khi chưa chạy.

**Tiêu chí nghiệm thu:**

- [ ] AT-P20-05-01: Onlychosenmonitors, fullscreenedge withoutmidcenter obstruction.
- [ ] AT-P20-05-02: MixedDPI and unsupportedexclusive modes documented; not universalgame promise.

**Lệnh thực có — chỉ kiểm hồ sơ:**

python tasks/validate_tasks.py (documentation consistency only; never product evidence)

**Kiểm chứng tương lai — CHƯA CHẠY:**

{"state": "GATED_NOT_RUN", "owner": "B00-02", "command": null, "gate": "Bootstrap owner must establish and successfully execute an exact bounded runner/build command on owned fixtures, record version/toolchain/results and approved whitelist before this task can become Ready.", "cases": "IT-05 native hardware matrix."}

**Chủ nhiệm chuẩn bị công cụ:**

B00-02

**Gate nghiệm thu người dùng:**

{"required": false, "note": "No user approval inferred; linked checkpoint may require it."}

**Owner triển khai cho yêu cầu:**

NV08

**Mã phi chức năng:**

See linked requirement / prerequisite scope.
