# Verification and validation plan

Status: toàn sản phẩm draft. 53 MSTest/35 fakecases ở [mẫu](../../../labs/policy-native/RESULTS.md) là evidence hẹp, không fulfilled production requirements. AT trong registry là proposedacceptance, không test đã chạy.

## 1. Levels and evidence

Unit: authorization/state/clocks/contribution/queue. Contract: typed IPC/source/mode/profile generations. Integration: realadapter→filter→consumer→reaction/action. NativeUI: fullflows/keyboard/resize/DPI. Acceptance: userexperience. Security/performance: independent tools/review khi có thật. SameAI selfreview không independentreview.

Every report: testId/requirementIds, fixture/data rights, build/toolversions, environment, preconditions, procedure, expected, actual, logs with no privatecontent, result Pass/Fail/Blocked/NotRun, limitation. Blocked/NotRun not counted Pass. For intentionalfailure testcase, expected error handling can pass assertion, but actionoutcome remains error.

## 2. Integration cases

| ID | Scenario | Required result / edge |
|---|---|---|
| IT-01 | Mixed allowed/disallowed/private/sensitive visible sources | Forbidden sentinel not in OCR/model/memory/log/network; unknownsafe blocks |
| IT-02 | Revoke/changesource during capture/inference/result/approach | Pendingresult/action stale, no late disclosure/click |
| IT-03 | Useraction→bodyapproach→targetmoves→input | Finalcheck prevents oldtargetclick; uncertainty no replay |
| IT-04 | Godot connectionlost/duplicate/reorder/foreignsession | No unauthorizedinput; reset epoch; queue UX per approved D-02 |
| IT-05 | Chosenmonitors, mixedDPI, moved/minimizedsupport/fullscreen | Correct coordinate/surface/hitzone, declaredunsupported no bypass |
| IT-06 | Humaninput and emergency/off/hide/selfhide/exit/switch | BUSINESS_RULES matrix and ResumeQueue exact; injectedinput nothuman |
| IT-07 | Pet/lift/throw/protest/modifiermove/recovery | Firstthrow no lastinghurt, refusal maintained, adminmove neutral |
| IT-08 | Neglect/absence/basic/inactive/sleep/clockjump | Correct48–72h eligibleclock, no falsepenalty/fabricatedevents |
| IT-09 | Videoended/uncertaintarget/externalframe/ad/tab | No interruption, scopedframe, uncertainadkeep, own tab |
| IT-10 | Frozen Vietsubtitle scene dataset under combinedload | Accuracy+latencyallstages, uncertainty/unattended split |
| IT-11 | Offline after packageinstall, externalAI absent | Localfeatures work; web/update clear errors; no cloudfallback |
| IT-12 | Downgrade/upgrade/profilefreeze/romanceoff | Preserveadvancedstate, selectionrespected, no auto enable |
| IT-13 | Memoryedit/delete/fade/pin/provenance | Correct contribution semantics, no documentdetail/clipboardpersistence |
| IT-14 | Multisteplesson dynamicsearch + humaninterrupt + failure | Explicitreview, searchmeaning, stopfailingstep, queueindependence |
| IT-15 | Export/importwrongcreds/recovery/corrupt/foreigngrants | Authenticatedboundedparsing, preserveexisting, no keys/grantsimport |
| IT-16 | Install/startupchoice/updateconfirm/signature/migration/uninstall | No silentinstall/data loss/otherappupdate; no auto backup |
| IT-17 | Localhistory retention30days, deletion, errorsupport | No raw/privatepayload, no uploads, actualexpiry |
| IT-18 | Attention invitations/teasing + ownactivities + requestedjob |2attempts/>=30min, no OSpranks, requestedpriority/delayonce |
| IT-19 |8h bothmodes dailywork/rest/media/offline | No leaks/permissionregressions/data loss; budget D-04 measured |
| IT-20 | Allsettings native keyboard/screenreader/resize/DPI/language | Namedcontrols/reachableactions/clearstate; not color-only |

Add atomic subcases at each implementation task; IT-xx group doesn't mean one happy-path assertion covers it all. Fixtures test malicious strings that resemble system instructions, wrongsource IDs, stalegenerations, duplicatecallbacks and outofboundscoordinates.

## 3. Existing experiments and order

E02a current fakebaseline needs UI/userclosure. E-INT is new proposed hybridprobe: transparentbody, emptyarea clickthrough, hitboxes, monitor/DPI, disconnect and measuredload. E01 art and E04 AI are independent riskprobes. E02 realprivacy must precede realcapture consumers; E03 action only after policy/sourceproof; E06 state/data; E05 integrationlast.

## 4. Proposed 8-hour script (not executed)

| Segment | Length | Workload |
|---|---|---|
| Start/settings/firstinteraction |1h | Bothmodes setup, selectedsources, keyboard/resize |
| Normalwork |2h | Humaninput priority, ignore invitations, memory/props |
| Rest/idle |1h | Noactiveinput clocks, autonomouseligiblemedia, return |
| Movies/localcontent |2h | Subtitles/reactions, nextend, nointerrupt, offlinepart |
| Statechanges |1h | Modes/profiles/lock/sleep/recovery without privatecontent |
| Failure/restart/data |1h | Controlledfailures, queuecancel, exports and persistedstate |

Total8h. Segment design and environments must be approved/frozen before run; not run this benchmark in unattendedbackground just because schedule exists. No simulatedclock used to claim an actual8h soak; logicalclock only for long stateunitcases.

## 5. Exit gates and defect severity

Leak/forbiddenaction/unstoppableinput/corruptdata block affected integration/release. UIcosmetic tracked separately. No loosening thresholds/tests to pass. Current resource/accuracy/passpercentile thresholds unresolved; after measurement, user decides then update CONSTRAINTS and executablechecks with positive/negative controls.

Ready for publicrelease requires bothmodes stable, definedhardwarematrix, offline, supporteddomains/apps documented, assets/modellicenses, installer/updateauth, datarecoverytests and useracceptance. No productionauth/server/CWVchecklist blindly copied to a localdesktopapp.
