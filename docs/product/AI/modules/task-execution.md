# task-execution — demonstration, execution and queue

Status: draft. Owns BH01–13 workflows; policy owns permissions. Learned lessons never autonomous triggers. Advanced exploration is a separate source of bounded intents, not replay of enabled lessons.

## Demo and review

States: Idle→RecordingExplicit→DraftReview→Saved or Discarded. Record only authorized scope, no raw keylogging. Crossing app/site ends/stops recording rather than saving unapproved multiscoped lesson. Summary includes steps, scope, search parameter slots and target selection first-result/exact-item. User confirmation required; cannot infer selection semantic from coordinates.

Lesson management view/rename/enable/delete/reteach perprofile, versions explicit. Request snapshot version+parameter validation; editing lesson while queued/running needs D-17 decision before execution coding. No typing outside search/navigation, even if demonstrated.

## Run lifecycle

Requested→DelayedOnce/Queued→Checking→Approaching→Rechecking→Acting→Verifying→Succeeded. Orthogonal branches YieldedHuman, PausedByStop, FailedNeedsTeaching, Cancelled. Only final postcondition establishes success; SendInput accepted events not enough.

Direct request starts without initial60s unless mooddelayonce. Repeat request can promote existing delayed intent, not duplicate a new job (dedupe request semantic), must still satisfy policy. Without repeat, job remains pending after own activity ends. Job precedence over autonomous exploration; own-play cleanup request semantics remain separate.

Human input yields immediately then60s eligibility; may refocus old allowed app/site. Before resume reidentify target; mismatched UI stops at failingstep, asks reteach. Later queue entries need independent eligibility; no claiming previousfailed job success.

Emergency/observationoff/manualhide/selfhide cancel running and pause unstarted. Show/re-enable doesn't resume until ResumeQueue. Exit/profile switch warns+cancels all unfinished, no persistent queue auto-replay. Disconnect/crash semantics outside these explicit cases need D-02/10.

## Side effects and controls

Action allowlist navigate/search/allowedclick; deny writes/deletes/messages/forms/payment/mark-read. Do not “test click” to discover if unsafe. Inspect element/surface purpose; if unknown block. Adclose only clearly identified origin, uncertain tab kept while return film; freecontent max3.

## Acceptance

E03/IT-03/06/14. Changedtarget after approach; revoked grants between checks; duplicate callback; interrupted verify; failure with unknown sideeffect; scopeswitch demo; first-result with changed search query; explicitsecondrequest dedupe. Logs sanitized30days via distribution, no raw typed text.
