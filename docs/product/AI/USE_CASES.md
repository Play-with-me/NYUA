# Use case specification — v0.1 draft

Actors: user; hostpolicy/life/task engine; Unityrenderer; Windows/browseradapter; localAI; optionalexternalprovider; distributioncomponent. Systemcomponents không thay user consent. “Bước” dưới đây là nghiệp vụ, không command đã implement. Mỗi UC cần tách negativecases ở task tương ứng.

## UC-01 — Khởi tạo và bắt đầu dùng sản phẩm

- Trigger/preconditions: user cài/mở app lần đầu; chưa có activeprofile hoặc startupsettings.
- Main: hiển thị phạm vi local/noaccount → đặt tên → chọn startup → kiểm tra máy/giới thiệu2mode → tạo initialprofile → sinh hoạt với allgrants off.
- Alternatives: bỏ qua optionalAIoutside/webextension vẫn sống; advanced chưa tải báo unavailable; namevalidation chi tiết D-14 trước code.
- Postcondition/data: một activeprofile, settings userchọn, không sourcegrant tự bật. Productscope/free/Vietnamese/noaccount không chỉ là màn hình mà releasecontract.
- Trace: SP01–06, NV06, CD01; AT tương ứng, IT-11/16/20.

## UC-02 — Chọn mức và tải gói

- Preconditions: app hoạt động, hardwaremetadata được kiểm tra trong scope cần thiết.
- Main: recommend từ measuredcapability → user chọn → hiển thị actualdownload/diskneeds → user tảiadvanced → validate → enablefeatures tương ứng.
- Alternatives: user thử khi unsupported sau warning; overload hỏi reduce/continue; lostnet/corruptdownload giữ notready; không silentdowngrade.
- Postcondition: modechange preservesadvancedmemory/relation/personality; basic positiveinteractionmaintains relation, neglectdeep frozen.
- Trace: MC01–04, MODE01–09; IT-10/11/12.

## UC-03 — Di chuyển và tương tác avatar

- Preconditions: avatarvisible, chosenmonitor; no appcontrol needed for pet/lift.
- Main: click/pet/hold-drag → recognizegesture → moodreaction → release slowmove or fastthrow → collide/fall/stand; supportwindowmove follows, removalfalls.
- Alternatives: refusal-lift still pet/feed; modifier-drag administrativemove independent of mood; no actualcursordragprank; crossmonitor only permittedmonitors.
- Postcondition: updatedbodypose/interactionevent, no automatic OSinput. Velocity/hold/modifier open D-05.
- Trace: NV07–11, QH06; IT-05/07.

## UC-04 — Cho ăn và dọn đồ

- Preconditions: avatarcontextmenu available, existingfoods/props.
- Main: rightclick→Food→choosecategoryitems→dragindividual/tray→receive/refuseanimation; cleanupcommand causes animatedputaway.
- Alternatives: ownpreferences refuse; partialtrayhandling openD-14; cleanupdelay/refuse still usermove/hide; maximum5left forces animatedcleanupbeforemore.
- Postcondition: needs/props update, optionalmemory safeuserinteraction; no cost/economy. Không instantcleanup từ nút “nhanh”.
- Trace: SH02/04/07/08; IT-07/18.

## UC-05 — Tự sinh hoạt và ngủ

- Trigger: ownneeds/mood/context; currentprofileactive.
- Main: chooseeligibleactivity→perform→canchangeintent; sleep/rest fromfatigue/time, wakegesturevariable; advancedhobbies animationonly.
- Alternatives: absentuser no penalty; appclose elapsedreconcile no fabricatedevents; inactiveprofilefreeze; observationwhilesleep openD-12.
- Postcondition: state progression consistent withmode, no unwanted OSpranks.
- Trace: SP07/08, SH01–06, QH03; IT-08/18.

## UC-06 — Cấp và thu hồi quyền nguồn

- Preconditions: settings accessible independently of avatar mood; grants initiallyfalse.
- Main: appscan→user selectsread→optionalcontrol; webpaste→normalizeidentity→choose read/control→enforcebrowserANDsite. Revoke stops new use immediately then offerkeep/delete sourcememory.
- Alternatives: controlbeforeread blocked; newapp/site noinherit; private/unknown identity deny; scanunsupportedapp doesn't promise automation support.
- Postcondition: installationgrants/generation updated, pendingdata stale; memorycleanup decision separate.
- Trace: QD01–06/09/12, HS02; IT-01/02.

## UC-07 — Quan sát an toàn và thử lại

- Preconditions: sourcevisible/allowed, notprivate, safeclassification possible.
- Main: filterregions→safe snapshot→analysis→generationcheck→semanticcontext. Unknownsensitiveboundary latcheswindow and explainswhy.
- Alternatives: userfixescontent but no autoderead; explicitRetry checksnewsource, unsafe stillblocked. Win+V history ephemeral whileopen, filedirect excluded, documenttopicretention only.
- Postcondition: no forbiddenpayload at any downstreamconsumer, no late use after revoke. Metadata-only exception separate.
- Trace: QD04/05/08/10/11/13–15; IT-01/02/13.

## UC-08 — Dạy, quản lý và gọi bài học

- Preconditions: explicitDemo enabled, supportedallowedapp/site.
- Main: recordone-scopesteps→reviewsummary/selectionmeaning→confirm→saveenabledlesson→choose+searchparameter→requestjob→approach/recheck/action/verify.
- Alternatives: crossscope stop; rejectunsafestep; usercanceldraft no save; mooddelayonce; usersecondrequest promotes not duplicate; targetchanged failstep/reteach. Editsduringjob D-17.
- Postcondition: verifiedsuccess or explicitjobstate, never unobservedreplay. Lessononlyrequested inbothmodes.
- Trace: BH01–05/10–12, NV10, DK02; IT-03/14.

## UC-09 — Nhường, dừng và hàng đợi

- Preconditions: jobs queued/running or autonomousexploration eligible.
- Main: humaninput yield, after60s revalidate; useremergency/off/hide cancelrunning/pausepending; enable/show requiresResumeQueue; exit/switch warncancelall.
- Alternatives: joberror onlystopsit, laterjobs independentlyeligible; selfhide samequeuepolicy; disconnected/crash behavior D-02/10 before implementation.
- Postcondition: cancelled terminal, no automatic resurrection; stops reachable even avatarrefuses.
- Trace: DK01–04, BH06–10, QH07; IT-06/14.

## UC-10 — Xem phim cùng người dùng

- Preconditions: permittedvisiblefilm, attentionselected; contentrights for testing.
- Main: attend/Vietsubtitle+scene inference→hoststate→silentaffect/sofa/popcorn; endedepisode+knownnexttarget allowsapproach/finalcheck/click.
- Alternatives: unobserved/hardscene uncertain; wrongemotion adjustsnextscene, nofeedbackUI; cannotcapture choosewatchorotheractivity; user manuallyrepositions subtitlescover.
- Postcondition: playbacknotinterrupted; emotiontargetlatency measured notpromised.
- Trace: XP01–04/09/10, AI03; IT-09/10.

## UC-11 — Tự mở nội dung giải trí

- Preconditions: advanced, idledefault5m, unlocked, nomedia, chosenbrowser+sitegrants.
- Main: ownsearch eligibleYouTube/explicitallowedmoviesite→own tab→freecontent→watch/play; returnuser yieldsinput but keepsplayback.
- Alternatives: login/pay/verify skipmax3; uncertainadtab notclose, returnfilm; embeddedplayer uncertainuserpointsconfirms; searchsessionboundary D-06.
- Postcondition: preserveusertabs, no payment/write/downloadgrant, nointerrupt existingmedia.
- Trace: XP05–08/15/16, QD13/14; IT-09/11.

## UC-12 — Học gu phim/nhạc

- Preconditions: allowedobservedcontent, userselection/transition evidence.
- Main: gathereligiblewatchduration/userchoice→movie>=20min or repeated/similarmusic evidence→updatepreference inference, notabsolute like.
- Alternatives: agent/autoplay doesn't prove userpresence; self-open onlycountswithusercontinueduse evidence; nohistory/backgroundcontent/audioanalysis.
- Postcondition: preferenceprovenance minimal, avoid learning own selections as proof withoutuserevidence.
- Trace: XP11–14; IT-09/13.

## UC-13 — Dùng AI bên ngoài theo yêu cầu

- Preconditions: userexplicitrequest, providerconfig/userpaidkey, safe eligibletext.
- Main: construct exactpayload→preview and destination→userconfirms→onesend→validateoutput→usecontextwithout authoritychange.
- Alternatives: reject/nomoney/networkfailure remainslocal; payload/sourcechange invalidatesconsent; retrypolicy D-18, not auto uploadmore.
- Postcondition: no images/audio/files/memorykeys transmitted; credentialstored via reviewedmechanism.
- Trace: AI02, SP04; IT-01/17.

## UC-14 — Quản lý ký ức

- Preconditions: settings accessible, currentprofilememory.
- Main: inspect→editcontent or pin/unpin or explicitdelete→confirmappropriateeffect→updateatomically.
- Alternatives: editno relationrecalc; naturalfade keepscloseness; delete reversescontribution ifany once; source-revoke offerssamekeep/deletepolicy.
- Postcondition: deletedcontentnotinindexes/caches/backupautocopies; clipboardneverlasting, documenttopiconly.
- Trace: KN01/02, QD09/11; IT-13.

## UC-15 — Quan hệ sâu, làm lành và lãng mạn

- Preconditions: advanced fordeep/romance; friendsdefault.
- Main: experiences→gradualrelationship; optinromance; neglecteligible48–72h→sad/withdraw; repeatedboundaryviolations→refusal/selfhide; invite/gifts+goodtreatment overseveralsessions→repair.
- Alternatives: absence/appoff/basic no deeppenalty; giftsnoninstant; romanceoff choosekeep/delete, respectchoice; hiddenread/controloff.
- Postcondition: currentrelationshipprivate, no forcedaffection or sexualfeature; useralwayssettings/reset.
- Trace: QH01–07, SP07, MC03; IT-07/08/12.

## UC-16 — Đổi/reset hồ sơ

- Preconditions: oneactive, otherprofilesonlyfromimports.
- Main: chooseexisting→warnunfinishedjobs→cancel→freezeold/loadtarget withcommonmachinegrants. Resetcurrentwarn→clearstate/memory/relation/lessons, preserveothers/grants.
- Alternatives: switchloadfailure safe recoveryUX D-10; importedprofileidcollision handled withoutmerge; no createnewbutton.
- Postcondition: exactlyoneactive; inactiveclocks unchanged.
- Trace: HS01–03, BH07; IT-12/15.

## UC-17 — Xuất/nhập sao lưu

- Preconditions: userpressesexport/import, chosenfile destination/source.
- Mainexport: collectwhitelistedprofiledata→requirepassword→createauthenticatedarchive→provide recoverycodeseparately→reportfilecreated. Mainimport: validate→credential→decode/schema→newseparateprofile.
- Alternatives: wrongcreds/corrupt/full disk/cancel leaveexisting intact; no keys/grants/queue restore; backupasset/modelscope D-09.
- Postcondition: no autobackup, no accountrecoverypromise; password or code paths tested.
- Trace: SL01/02, HS01/02; IT-15.

## UC-18 — Cập nhật, gỡ, chẩn đoán và phát hành

- Preconditions: versionedinstalledapp, trustedupdatesource chosen before release.
- Main: check/downloadownupdate→userconfirminstall/restart→safejobshutdown→verifiedinstall/migration→statecheck. Uninstalloffersretain/delete + manualexportreminder. Historyinspect/delete/30daysexpiry independentmemory.
- Alternatives: declineupdate keepscurrent; signature/migrationfailure stops safely; no otherappupdate or deletionofexportselsewhere; no telemetry/supportuploadwithoutnewconsent.
- Postcondition: version/data consistent, no fakepublicreadiness frominternaldemo.
- Trace: CD01–03, BH13, SP03/05/06; IT-16/17/19/20.
