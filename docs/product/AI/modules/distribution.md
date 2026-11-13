# distribution — hồ sơ, lưu trữ, backup và phát hành

Status: draft. Production storage/crypto/installer/signing not selected; no inferred free signing or automatic backup. DATA/RELEASE define related contracts.

## State ownership

Installation grants/settings shared, active profile selected; profile-scoped memory/relation/personality/lessons/props. Inactive profiles freeze all clocks. Import is sole additional-profile creation path; no createbutton. Reset current removes state/memory/relation/lessons and leaves others/global grants.

Local writes are normal persistence, not backup copies. Need transaction/durability and migration tests with explicit noautomaticbackup. Do not add database cloud sync/telemetry/report endpoint. External AI secret remains machine-owned and excluded from archive.

## Export/import

Manual export only, requiredpassword perexport, separately held recoverycode. Reviewed encryption/authentication primitive and bounded parsing; no invented crypto. Archive accepted only after schema/integrity/path/size validation; import newprofile, no merge, no grants/keys executable payload. Asset/model export scope is open D-09; archive cannot silently include all installedpackage caches.

Errors: wrongcredential/corruption/incompatibleversion insufficientdisk/incompletewrite; leave existing profiles intact. Destination selected explicitly; no delete unrelated exports on uninstall. No promise recovery without password or code.

## Installation/update

Install native app, optional renderer/dependencies/advancedpackage/extension components with license bill. Startup opt-in onboarding. Check/download ownupdates automatic; install/restart explicit userconfirm. Failed signature/integrity or unsupporteddata migration must not run installer. Update cannot update Chrome/Edge/other apps.

Uninstall asks retain/delete appdata and suggests manualexport, respects activejob warning. Existing manually exported archives outside appdata are not hunted. Rollback application binary not assumed safe with newer schema; migration compatibility and manualexport recovery workflow required before release.

## Acceptance

IT-12/14/15/16/17, AT-HS/SL/CD/BH13. Test duplicate importid, switch cancel, freeze time, recoverycode/passwordwrong, crashmidimport, archive traversal, migrationfailure, declineupdate, no auto backup and logs expire30days. Independent security review before public distribution remains unstaffed, not fake approved.
