# ADR-002 — Host là nơi cấp phép tác động

Date:2026-11-13. **PROPOSED**, không phải acceptedproductionarchitecture.

## Context/decision proposal

Page/model/renderer có thể đưa ý định cũ hoặc sai; một click nhầm có thể ảnh hưởng dữ liệu. Đề xuất host C# sở hữu quyền, generations và OSinput adapter. Godot chỉ report movement; AI chỉ report semantic observation; host kiểm lại quyền/target/userinput trước action.

## Alternatives/tradeoffs

Renderer trực tiếp SendInput giảm một lượt trao đổi nhưng thêm authoritypath và khó ngăn latecallback. Model generictoolaccess linh hoạt nhưng không phù hợp phạm vi denywrite/send/pay. Hostgate tăng protocol/statecode nhưng cho phép tập trung kiểm chứng rule và revoke.

Một hostgate không tự là securitysandbox; process cùnguser vẫn có thể gây tác động ngoài app. Cần IPCidentity/version/limits và reviewedadapter. Khi thay topology, giữ nguyên nghiệp vụ priority/permission; không chỉ mộtbool allow từUI.

## Acceptance/revisit

Contractreview + IT-02/03/04/06 và realadapter proof. Generationmismatch/stop/targetchange đều không input; peer callback không tự cấp quyền. Nếu host/UIsharedthread gây delay, có thể tách executionowner mà giữ authoritycontract, không bypassgate vì hiệu năng.
