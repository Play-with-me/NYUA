# life-state — đời sống, ký ức, quan hệ

Status: draft. Inputs: clock events, explicit interactions, sanitized context, mode/profile lifecycle. Outputs: internal state changes, memory candidates with provenance, activity intents; không click/gõ hoặc grant.

## Model

Tách needs/fatigue/sleep, momentary mood, relationship/closeness/trust/hurt, long-term personality, learned preferences và activity commitment. Các giá trị nội bộ có thể số hóa để test nhưng không tạo user dashboard. Chưa chốt thang điểm/hàm decay/weights/BehaviorTree/utility algorithm (D-05).

Basic: needs/mood/closeness và refusal-lift nhẹ; fixed core personality. Advanced: sâu hơn, romance opt-in, hurt/selfhide, long-term expression maturation. Downgrade suspend advanced expression/degradation nhưng preserve data. Advanced lãng mạn bật chưa tự thành partners.

## State transitions

Activity: Idle→Choose→ApproachOwnProp→Doing→Finish/ChangeMind; sleep có clock/fatigue transitions. Attention cooldown separate. Phản ứng cảnh tác động mood có smoothing, không lấy emotion label làm toàn bộ identity.

Interpersonal: Neutral/Close↔Upset→Withdrawn→SelfHidden→Reconnecting. Đây là nhãn logic đề xuất; transitions/threshold cần kịch bản người dùng rà. Firstthrow không lastinghurt; repeatedafterprotest unlock refusal, recovery readiness explicit gesture. Severe repair requires multiple genuine sessions, not apprestart spam.

## Clocks và persistence

Neglect clock chỉ active advanced visible human-input use; threshold48–72h based trust/hurt direction, formula open. Click/pet/feed break neglect streak, không erase sadness. Profile inactive freezes all; active appclosed elapsed reconcile needs/cooling only, không fabricated interactions. Appclose khác profile switch.

Memory lifecycle theo DATA: pin/fade/edit/delete semantics, topic-only document, no clipboard lasting. Long-term personality retains curiosity/playfulness/ownwill; maturing expression not consent to self-modifying source code.

## Verification

Deterministic logical clock/seed chosen test harness; seed không ép production luôn lặp giống nhau. Table scenarios firstthrow/repeat/refuse/pet/recover, absence vs neglect, basic downgrade, romanceoffkeep/delete, memorydelete vs naturalfade, multisession repair. AT-SH/KN/QH/SP07/SP08 và IT-07/08/12/13.

Blocked before detailed algorithm by D-05/08/12. Can prepare narrative/state scenarios without choosing fixed minute/day substitutes.
