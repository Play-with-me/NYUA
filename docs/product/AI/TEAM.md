# Team operating contract — dossier edition

Nguồn quy trình đầy đủ: [QUY_TRINH_TEAM_SAN_PHAM](../../QUY_TRINH_TEAM_SAN_PHAM.md). Bản này là checklist ngắn cho AI/team khi dùng bộ hồ sơ. Không thay AGENTS/CONSTRAINTS hoặc quyết định người dùng.

## Roles/accountability

Productowner=user owns scope/experience/cost/releaseapproval. BA/UX/Windows/Godot/AI/QA/security/release là các trách nhiệm, AI có thể đảm nhận nối tiếp. Không coi đổi vai hoặc đọc lại code là independentreview. Không tự gửi message/email cho tester/team khi chưa có lệnh.

## Definition of Ready

Requirement/AT đã rõ; module boundaries/contracts reviewed; no relevant unresolvedblocker; test data rights known; sourceofficial research đủ; exact file whitelist and dependencies recorded; revert/codecheckpoint plan; test commands actual hoặc có task chuẩn bị rõ ràng. Task Draft/Blocked cannot be marked Ready because AI wants to start.

## Definition of Done

Acceptance met with negativecases; propertests/build/runtime evidence; no unrelatedscope/grantincrease; review correct/readable/architecture/security/performance; docs/RTM/state updated; checkpoint Git saved; userexperience approval when needed. Automatedpass not equivalent to useracceptance or broadcompatibility. No productionrelease without bothmodes gate.

## Change control

Record userchange → assess SRS/spec/data/UX/test/backlog impact → ask only remaining productdecision → amend canonical source → sync two editions → validator → reviewdiff → update scopedwork. Prior decision preserved with supersededstatus; don't erase evidence to change conclusion. CurrentE02a tasks remain active until closed, no overwrite.

## Review cadence

At taskstart readmemory+spec+CONSTRAINTS; before meaningfulchange explainwhat/howverified; duringwork report newfacts/unknowns; at end evidence+limitations+nextsmallstep. No mandatory dailymeeting dates for a oneperson+AIproject. Keep writtenhandoff per session. Ask one productquestion at a time only when needed.

## Documentation controls

Run `python docs/product/AI/sync_requirements.py` after canonical requirementchange, then `python docs/product/AI/sync_backlog.py` and `python docs/product/AI/validate_dossier.py`. Sourcehash drift, missingtask/reference, stale requirementcounts or cyclicdependency are errors. Validator only checks documentconsistency, not semanticapproval/security/runtimecorrectness.

Do not manually edit generatedSRS/human02/registry/RTM/backlogoutput without updating generator/input. Narrative docs still need semanticreview by reader; sourcehash does not prove prose fidelity. Date and artifactversion required at baselinechanges; no fake ISOcertification.
