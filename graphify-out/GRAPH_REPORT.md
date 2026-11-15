# NYUA — AI navigation entry (generated)

Read this file first; never load full graph.json into the prompt.

- Graphify 0.9.97, local deterministic AST/resolver; 21 C#/Python files,
  259 nodes, 646 edges: {'EXTRACTED': 603, 'INFERRED': 43}.
- Registry: 219 tasks, 109 requirements, 7 modules.
- No community clustering/Leiden/God-Node claim: raw source extraction only. No semantic/doc LLM pass.
- Registry/proposed relations live separately in registry-index.json, never labelled AST EXTRACTED.
- Existing lab source is a reference only; proposed production file paths remain unimplemented.
- Freshness: every query verifies source inventory/SHA256/schema/output hashes; stale -> error, rebuild.
  Schema2 hashes UTF-8 text after BOM removal and LF normalization, portable across Git LF/CRLF checkouts.

## Small-first workflow

1. `python docs/context/context_nav.py check`
2. `python docs/context/context_nav.py module policy` (one of seven module keys)
3. `python docs/context/context_nav.py task P10-03 --out <TEMP-file>`; read that pack.
4. Read only cited source anchors for deeper evidence. No pack grants product/publishing authorization.

Default/max pack budget 160000 UTF-8 bytes; overflow emits no partial pack. Task, exact requirements,
acceptance, full CONSTRAINTS and relevant decisions are never truncated. Code neighborhood is optional,
one hop/max12 edges, with omitted count. Unknown task fails. E02a experience acceptance was closed by the user on2026-11-15; technical limits stay explicit.

Regenerate: `python docs/context/context_nav.py build` (Graphify pinned 0.9.97, 120-second supervisor).
Verify: `python docs/context/context_nav.py test`; measure: `python docs/context/context_nav.py measure`.
See docs/context/README.md for provenance, baseline and limits. No external LLM/API/upload.
