# Engineering delivery, CI và phát hành — draft

Không tạo pipeline/remote/installer trong đợt hồ sơ. Desktoplocalapp không cần backendaccount/service monitoring để hợp một checklist web.

## 1. Build/reproducibility

Pin .NET SDK, Godot editor/export templates/plugins, modelweights/runtime và testtools sau technicalselection; record OS/architecture, filehash, licenses and notices. Build host/renderer/optionalworker/extension separately, package manifests tie compatible versions. No secrets in repo/buildlogs. Actual commands only after productionprojects exist; existing labcommands at [native README](../../../labs/policy-native/README.md).

## 2. Proposed CI gates

| Stage | Checks | Before calling enforced |
|---|---|---|
| Fast change | Compile/types/style, relatedunit, nosecret/suppression review | Real runner/command + knownbad and clean controls |
| Integration | Policy/IPC/state/source adapter with fake fixtures | Deterministic results, no privatecontent, negativecases |
| NativeUI | WPF flows + Godot overlay/hitzone on supportedWindowsrunner | Actualdesktop session; not headlesspass substituted |
| Performance | Definedbenchdataset + load + signedhardwarematrix | Recordedbaseline and approved budgets |
| Security/licensing | Native packageaudit, asset/modelinventory, archive/updateabuse | Currentadvisorysources and reviewer findings |
| Package | Reproducibleversion, integrity/signature, install/update/uninstallsmoke | Testedartifact equals reviewedbuild |

CIservice/machines costs need approval; no cloudtest uploading personal data. Expensive8h soak runs deliberately with duration, not eachsmallchange or backgroundforever. No coveragepercent invented from template. No skip/error suppression to obtain green.

## 3. Staged release

Internal prototypes separately labeled → completeintegrated internalbuild → useracceptance of bothmodes → limited testers only after stability gate and explicit distributiondecision → public. User requires stablebasic+advanced before publicrelease; don't ship halfproduct as publicbeta to bypass that gate.

Release checklist: openblockers resolved; policy/data/input safetytests; offline; bothbrowsers; definedmonitor/DPI/fullscreenlimits;8h; manualexport/recovery; startupoptin; versioncompatibility; notices; Vietnamesehelp/privacy/costs; selectedname reviewed; knownlimitations. No automatictelemetry to verify adoption.

## 4. Update lifecycle

Check→metadata authenticated→download→integrityverify→DownloadedAwaitingUser→userconfirm install/restart→quiesce/canceljobs with warning→install/migration→reopenstateverify. Invalidsignature/wrongcomponentversion/schemaunsupported/diskfull must stop before state loss. Exact update mechanism/source/signing open D-13.

Old binaries reinstall không mặc nhiên downgrade được DB. Rollbackrunbook must specify schema compatibility and data preservation. No autoexport/backup to make migration convenient. If safer migration requires usermanualexport, make requirement explicit before proceeding.

## 5. Operations/support without telemetry

Localhistory only BH13. Bugreport form/template can ask appversion, OSversion, steps, expected/actual and redacted evidence chosen by user. No auto upload, crashdump/key/screenshot collection. Incident: stop affected control/observation via existing product controls, preserve minimaldiagnostics, reproduce with fakefixtures, issue reviewed fix and release notes. No remote kill-switch claim without architecture/userconsent.

## 6. Ownership

User decides release/costs/publiccommunication. AI prepares/reviews/tests, but selfreview not independent. Before launch assign security/data/license review explicitly or keep gate blocked. Uninstall asks keep/delete and manualexport reminder, does not remove arbitrary archives elsewhere.
