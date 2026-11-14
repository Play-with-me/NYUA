# D-12: Quan sát lúc nhân vật ngủ (Sleep Observation Policy)

- **ID:** D-12
- **Title:** Chính sách quan sát khi nhân vật ngủ
- **Date:** 2026-11-14
- **Status:** Confirmed
- **Source:** Direct user confirmation
- **Verbatim Confirmation:** "Khi nhân vật ngủ thì dừng quan sát, thức dậy mới tiếp tục trong phạm vi quyền đã cấp."

## Quyết định (Decision)

Khi nhân vật ngủ, hệ thống dừng hoàn toàn hoạt động quan sát. Khi nhân vật thức dậy, hoạt động quan sát mới được tiếp tục và phải tuân thủ nghiêm ngặt trong phạm vi quyền đã được cấp tại thời điểm đó.

## Tiêu chuẩn nghiệm thu (Acceptance Criteria)

- **Disable on Sleep:** Sleeping disables observation completely.
- **Resume on Wake:** Wake resumes observation only under currently granted permissions.
- **Safety Compliance:** No bypass of SafetyHold / retry rules.


Current full ledger: [DECISIONS](../../docs/product/AI/DECISIONS.md). Historical draft; no approval/test evidence added.
