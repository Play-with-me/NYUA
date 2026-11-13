# perception — đường dữ liệu quan sát và AI

Status: draft. Content is untrusted; metadata authority must come from OS/browser adapter evidence, not page text/model. No account API connectors. No hidden/minimized/private reads. Direct file reader deferred.

## Pipeline

1. Discover candidate visible source without ingesting forbidden content into AI.
2. Resolve identity and applicable app/site/frame grants.
3. Determine safe regions before OCR/vision; unknown or incomplete sensitive masking blocks window and latches SafetyHold.
4. Build ephemeral safe snapshot with source/policy generations, provenance and purpose.
5. OCR/context/simple classifier or local advanced model, then output bounded semantic observations.
6. Before consumer use, recheck generation; discard stale data/results, do not add memory or react using revoked in-flight content.

Sensitive detector itself must operate within a reviewed trusted filtering boundary; “AI needs raw screenshot to find secrets” does not authorize giving raw image to general reasoning model. Must define what prefilter reads vs what “exclude from read” means and get safety review D-15 before actual capture implementation.

## Special sources

Split view can read both allowed visible regions; own attention selects one/main topic. Geometry path separate. Documents only topic/name retained; clipboard full history only while Win+V evidence, no long memory. APIs and open/close detection not established by E02a. Background media metadata exception for no-media check is not permission to read tab content; exact minimal metadata access D-16.

Video embedded cross-origin exception: frame identity/user-confirmed mapping+parent context; no generic grant to source origin. User guidance confirmation retained/revalidated, mismatch asks again. Protected capture can fail; no bypass, still watch or selfplay based mood.

## LocalAI and uncertainty

AI_LOCAL.md defines model candidate validation, confidence/uncertain and benchmark. No model-selected action can directly execute. ExternalAI is explicit separate consented text-only route; never hidden fallback. Hearing/audio/mic/camera excluded.

## Acceptance

Real source sentinel capture path including logs/worker/network, private status, occlusion and mid-capture switch; model no prohibited sentinel. AT-QD04–15, AT-AI*, AT-XP01–03/10, IT-01/02/09/10. Report falsepositive blocks as usability limitation, not silently disable filtering.
