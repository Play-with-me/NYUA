"""NYUA local Graphify adapter and bounded canonical-context navigation (no LLM)."""
from __future__ import annotations

import argparse
import contextlib
import hashlib
import importlib.metadata
import io
import json
import math
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'graphify-out'
AI = 'docs/product/AI/'
SCHEMA = 2
HASH_POLICY = 'utf8-text-bom-removed-universal-newlines-lf-v1'
VERSION = '0.9.97'
OFFICIAL_SHA256 = {
    'extract.py': '355f470579b44c0442ef38101e52bf2f075fdff4c6cfee8b1ef27d3508974fa5',
    'cli.py': 'a870f535868bc57927f4501c0edcac72194186e82033e2f0a74e25321eecb492',
}
MAX_PACK = 160_000
SCOPE = ('LOCAL-ONLY DOCS/TOOLING. No product implementation, runtime test, external AI/API, '
         'repository upload, push or PR update authorized by this integration. E02a user acceptance '
         'C3 experience acceptance was closed explicitly by user on 2026-11-15; unverified technical checks remain open. A proposed path is not an existing implementation or permission to write it. '
         'Source requirements/decisions win over this navigation cache; NOT RUN is never PASS. '
         'Do not read graph.json wholesale into the model. No hidden safety/acceptance truncation.')
REFERENCE = {
    'policy': ['PolicyLab.Core/PolicyEvaluator.cs', 'PolicyLab.Core/ReadCoordinator.cs'],
    'perception': ['PolicyLab.Core/PolicyEvaluator.cs'],
    'companion': ['PolicyLab.App/LabViewModel.cs'],
    'desktop-body': ['PolicyLab.App/MainWindow.xaml.cs'],
    'life-state': ['PolicyLab.Core/Contracts.cs'],
    'task-execution': ['PolicyLab.Core/ReadCoordinator.cs'],
    'distribution': ['PolicyLab.App/App.xaml.cs'],
}


class InvalidContext(ValueError):
    pass


def read(path):
    return (ROOT / path).read_text(encoding='utf-8-sig')


def load(path):
    return json.loads(read(path))


def encode(value):
    return json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + '\n'


def sha(path):
    # All freshness inputs/outputs are UTF-8 source or JSON/Markdown text.
    # Match Git LF blobs and CRLF working copies without ignoring real content edits.
    # Upstream distribution/binary checks below deliberately still hash raw bytes.
    return hashlib.sha256(read(path).encode('utf-8')).hexdigest()


def write(path, value):
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(value, encoding='utf-8', newline='\n')


def source_paths():
    """Explicit roots and suffixes: never scan binaries, secrets or generated phase copies."""
    paths = []
    for base, suffix in [('labs/policy-native', '.cs'), ('docs', '.py'), ('tasks', '.py')]:
        for p in (ROOT / base).rglob('*' + suffix):
            if not set(p.relative_to(ROOT).parts) & {'bin', 'obj', 'artifacts', 'TestResults', '__pycache__'}:
                if p.is_file() and not p.is_symlink():
                    paths.append(p.relative_to(ROOT).as_posix())
    return sorted(set(paths))


def inputs():
    core = ['CONSTRAINTS.md', 'DESIGN.md', 'CAPABILITY_MAP.md', '.agents/PROJECT_MEMORY.md',
            'docs/YEU_CAU_HIEN_HANH.md', 'tasks/todo.md', 'tasks/README.md', 'tasks/E02a-USER-ACCEPTANCE.md',
            'docs/context/README.md', AI + 'backlog.json', AI + 'requirements.json',
            AI + 'README.md', AI + 'SRS.md', AI + 'DECISIONS.md', AI + 'DECISION_SOURCE_2026-11-14.md',
            'docs/godot-windows/SPEC.md', 'docs/godot-windows/TEST_PLAN.md', 'docs/godot-windows/SOURCES.md']
    core += [p.relative_to(ROOT).as_posix() for p in (ROOT / (AI + 'modules')).glob('*.md')]
    return sorted(set(core + source_paths()))


def blocked(*args, **kwargs):
    raise RuntimeError('Network and child processes are disabled during local extraction')


def extract_graph():
    version = importlib.metadata.version('graphifyy')
    if version != VERSION:
        raise InvalidContext(f'Expected Graphify {VERSION}, got {version}; review adapter before upgrade')
    package = Path(importlib.metadata.distribution('graphifyy').locate_file('graphify'))
    for name, expected in OFFICIAL_SHA256.items():
        if hashlib.sha256((package / name).read_bytes()).hexdigest() != expected:
            raise InvalidContext('Installed Graphify differs from verified official tag: ' + name)
    from graphify.extract import extract, RUN_ONLY_EXTRACTION_KEYS
    with tempfile.TemporaryDirectory(prefix='nyua-graphify-cache-') as cache:
        with patch.object(socket, 'socket', blocked), patch.object(socket, 'create_connection', blocked), \
                patch.object(subprocess, 'Popen', blocked), contextlib.redirect_stdout(io.StringIO()):
            result = extract([ROOT / p for p in source_paths()], root=ROOT,
                             cache_root=Path(cache), parallel=False, max_workers=1)
    if result.get('failed_sources') or result.get('skipped_sources'):
        raise InvalidContext('Graphify failed/skipped inputs; refusing a partial success map')
    if result.get('input_tokens', 0) or result.get('output_tokens', 0):
        raise InvalidContext('Unexpected LLM token usage')
    result = {k: v for k, v in result.items() if k not in RUN_ONLY_EXTRACTION_KEYS}
    result['nodes'].sort(key=lambda n: (n['id'], encode(n)))
    result['edges'].sort(key=lambda e: (e['source'], e['target'], e.get('relation', ''), encode(e)))
    result['graph'] = {'schema_version': SCHEMA, 'schema_owner': 'NYUA raw-extraction wrapper',
                       'graphify_version': version, 'mode': 'local deterministic AST + resolver',
                       'network_and_subprocess_guard': True, 'clustered': False}
    return result


def registry():
    return load(AI + 'backlog.json'), load(AI + 'requirements.json')['records']


def fingerprint(value):
    return hashlib.sha256(encode(value).encode('utf-8')).hexdigest()


def verify_metrics(manifest, metrics=None, certificate=None):
    measurement_digest = sha('graphify-out/MEASUREMENTS.json') if metrics is None else fingerprint(metrics)
    metrics = metrics if metrics is not None else load('graphify-out/MEASUREMENTS.json')
    certificate = certificate if certificate is not None else load('graphify-out/measurements-manifest.json')
    expected = {'schema_version': SCHEMA, 'hash_policy': HASH_POLICY, 'graphify_version': VERSION,
                'source_fingerprint': fingerprint(manifest['sources']),
                'map_fingerprint': fingerprint(manifest['outputs']),
                'measurement_sha256': measurement_digest}
    if certificate != expected:
        raise InvalidContext('STALE_MEASUREMENTS: source/map revision or measurement integrity changed; run build/measure')
    if any(metrics.get(k) != expected[k] for k in
           ['schema_version','hash_policy','graphify_version','source_fingerprint','map_fingerprint']):
        raise InvalidContext('STALE_MEASUREMENTS: snapshot revision fields differ')
    for p, digest in metrics['baseline_file_sha256'].items():
        if p not in manifest['sources'] or sha(p) != digest:
            raise InvalidContext('STALE_MEASUREMENTS baseline: ' + p)
    if metrics['pack_algorithm_sha256'] != sha('docs/context/context_nav.py'):
        raise InvalidContext('STALE_MEASUREMENTS: pack algorithm changed')


def fresh(manifest=None, verify_measurements=True):
    m = manifest if manifest is not None else load('graphify-out/manifest.json')
    if m.get('schema_version') != SCHEMA or m.get('hash_policy') != HASH_POLICY or set(m['sources']) != set(inputs()):
        raise InvalidContext('STALE: schema or input inventory changed; run build')
    bad = [p for p, digest in m['sources'].items() if not (ROOT / p).is_file() or sha(p) != digest]
    for p, digest in m.get('outputs', {}).items():
        if not (ROOT / p).is_file() or sha(p) != digest:
            bad.append(p)
    if bad:
        raise InvalidContext('STALE: changed/missing source or map: ' + ', '.join(bad[:8]))
    if verify_measurements:
        verify_metrics(m)
    return m


def decision_text(ids):
    """Complete relevant confirmed sections and residual table rows, no semantic rewriting."""
    text = read(AI + 'DECISIONS.md')
    result = {}
    for did in sorted(set(ids)):
        row = next((line for line in text.splitlines() if line.startswith('| ' + did + ' |')), None)
        marker = '### ' + did + ': confirmed part'
        section = text.split(marker, 1)[1].split('\n### ', 1)[0].strip() if marker in text else None
        if row is None:
            raise InvalidContext('Unknown decision: ' + did)
        result[did] = {'residual_row_exact': row, 'confirmed_section_exact': section,
                       'source_anchor': AI + 'DECISIONS.md#' + did.lower()}
    return result


def neighbors(graph, files, limit=12):
    """One-hop only; optional AST evidence, bounded and explicitly accounts for omission."""
    nodes = {n['id']: n for n in graph['nodes']}
    seeds = {n['id'] for n in graph['nodes'] if n.get('source_file') in files
             and n.get('source_location') == 'L1'}
    candidates = [e for e in graph['edges'] if e['source'] in seeds or e['target'] in seeds]
    selected = candidates[:limit]
    used = seeds | {e[k] for e in selected for k in ['source', 'target']}
    return {'basis': 'One-hop file-root AST neighbors; reference code is NOT production implementation',
            'max_hops': 1, 'max_edges': limit, 'omitted_optional_edges': max(0, len(candidates)-limit),
            'nodes': [nodes[k] for k in sorted(used) if k in nodes], 'edges': selected,
            'confidence_rule': 'Original Graphify EXTRACTED/INFERRED tags retained; resolver is not runtime proof'}


def pack(tid, budget=MAX_PACK, check=True):
    if check:
        fresh()
    if not 1024 <= budget <= MAX_PACK:
        raise InvalidContext(f'Budget must be 1024..{MAX_PACK} UTF-8 bytes')
    data, requirements = registry()
    by = {t['id']: t for t in data['tasks']}
    if tid not in by:
        raise InvalidContext('UNKNOWN_TASK: ' + tid)
    t = by[tid]
    refs = set(t['source_ids'] + t['requirement_refs'] + t.get('implementation_requirements', []))
    # NFR objects retain exact threshold/open status; criteria in the task are always included in full.
    selected = [r for r in requirements if r['source_id'] in refs]
    decisions = list(t['open_decisions'])
    # Confirmed decisions must remain present even when not listed as an open blocker.
    import re
    for r in selected:
        decisions += re.findall(r'D-\d{2}', r['source_text'])
    if tid.startswith(('R00-', 'A00-')):
        decisions += ['D-' + tid.split('-')[1]]
    files = [p for p in t['proposed_files'] if p in source_paths()]
    reference_files = ['labs/policy-native/' + f for f in REFERENCE[t['module']]]
    graph = load('graphify-out/graph.json')
    payload = {
        'schema_version': SCHEMA, 'scope_and_safety': SCOPE,
        'source_hash_manifest': 'graphify-out/manifest.json',
        'task_exact': t, 'requirements_exact': selected,
        'decisions_exact': decision_text(decisions),
        'constraints_exact': read('CONSTRAINTS.md'),
        'nfr_exact': [n for n in data['nonfunctional_requirements'] if n['id'] in t.get('nfr_refs', [])],
        'prerequisites': [{k: by[d].get(k) for k in ['id','title','output','status','readiness',
                          'open_decisions','bootstrap_owner','human_gate']} for d in t['dependencies']],
        'existing_files': [p for p in t['proposed_files'] if (ROOT / p).is_file()],
        'missing_proposed_files': [p for p in t['proposed_files'] if not (ROOT / p).is_file()],
        'module_spec_anchor': AI + 'modules/' + t['module'] + '.md',
        'lab_reference_mapping': {'provenance': 'MANUAL_REFERENCE_NOT_IMPLEMENTATION',
                                  'files': reference_files},
        'real_code_neighbors': neighbors(graph, files or reference_files),
        'deeper_sources': {'task': AI + 'backlog.json /tasks[id=' + tid + ']',
                          'requirements': AI + 'requirements.json /records[source_id]',
                          'decisions': AI + 'DECISIONS.md', 'acceptance': 'tasks/todo.md#checkpoint-c3',
                          'freshness': 'graphify-out/manifest.json'},
    }
    text = encode(payload)
    size = len(text.encode('utf-8'))
    if size > budget:
        raise InvalidContext(f'OVERFLOW {tid}: required={size} bytes budget={budget}; '
                             'nothing emitted, no critical constraints truncated. Increase budget or read source anchors.')
    return text


def build():
    graph = extract_graph()
    write('graphify-out/graph.json', encode(graph))
    data, requirements = registry()
    relations = []
    for t in data['tasks']:
        for dep in t['dependencies']:
            relations.append({'source': t['id'], 'target': dep, 'relation': 'depends_on',
                              'provenance': AI + 'backlog.json', 'confidence': 'REGISTRY_DECLARED_NOT_CODE'})
        for rid in sorted(set(t['requirement_refs'] + t.get('implementation_requirements', []))):
            relations.append({'source': t['id'], 'target': rid, 'relation': 'planned_requirement_scope',
                              'provenance': AI + 'backlog.json', 'confidence': 'REGISTRY_DECLARED_NOT_CODE'})
    index = {'schema_version': SCHEMA, 'tasks': {t['id']: {'module':t['module'],
             'source_anchor': AI + 'backlog.json /tasks[id=' + t['id'] + ']'} for t in data['tasks']},
             'modules': {m: [t['id'] for t in data['tasks'] if t['module']==m] for m in sorted(REFERENCE)},
             'relations': relations, 'requirements': [r['source_id'] for r in requirements]}
    write('graphify-out/registry-index.json', encode(index))
    confidences = {c: sum(e.get('confidence')==c for e in graph['edges'])
                   for c in sorted({e.get('confidence','UNKNOWN') for e in graph['edges']})}
    report = f'''# NYUA — AI navigation entry (generated)

Read this file first; never load full graph.json into the prompt.

- Graphify {VERSION}, local deterministic AST/resolver; {len(source_paths())} C#/Python files,
  {len(graph['nodes'])} nodes, {len(graph['edges'])} edges: {confidences}.
- Registry: {len(data['tasks'])} tasks, {len(requirements)} requirements, {len(index['modules'])} modules.
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

Default/max pack budget {MAX_PACK} UTF-8 bytes; overflow emits no partial pack. Task, exact requirements,
acceptance, full CONSTRAINTS and relevant decisions are never truncated. Code neighborhood is optional,
one hop/max12 edges, with omitted count. Unknown task fails. E02a experience acceptance was closed by the user on2026-11-15; technical limits stay explicit.

Regenerate: `python docs/context/context_nav.py build` (Graphify pinned {VERSION}, 120-second supervisor).
Verify: `python docs/context/context_nav.py test`; measure: `python docs/context/context_nav.py measure`.
See docs/context/README.md for provenance, baseline and limits. No external LLM/API/upload.
'''
    write('graphify-out/GRAPH_REPORT.md', report)
    import graphify.extract
    manifest = {'schema_version': SCHEMA, 'hash_policy': HASH_POLICY, 'graphify_version': VERSION,
                'adapter': 'graphify.extract.extract explicit paths/root, parallel=False, TEMP cache',
                'official_repository': 'https://github.com/Graphify-Labs/graphify/tree/v0.9.97',
                'official_verified_file_hashes': OFFICIAL_SHA256,
                'parser_versions': {name: importlib.metadata.version(name) for name in
                                    ['tree-sitter','tree-sitter-c-sharp','tree-sitter-python']},
                'extraction_evidence': {'failed_sources': [], 'skipped_sources': [],
                                        'input_tokens': graph.get('input_tokens', 0),
                                        'output_tokens': graph.get('output_tokens', 0)},
                'installed_extractor_sha256': hashlib.sha256(Path(graphify.extract.__file__).read_bytes()).hexdigest(),
                'sources': {p: sha(p) for p in inputs()},
                'outputs': {p: sha(p) for p in ['graphify-out/graph.json', 'graphify-out/registry-index.json',
                                               'graphify-out/GRAPH_REPORT.md']}}
    write('graphify-out/manifest.json', encode(manifest))
    measure(emit=False)
    print(f'Built {len(source_paths())} files; {len(graph["nodes"])} nodes/{len(graph["edges"])} edges; '
          f'{len(data["tasks"])} tasks/7 modules. No network/LLM or application execution.')


def test():
    m = fresh()
    data, requirements = registry()
    index = load('graphify-out/registry-index.json')
    graph = load('graphify-out/graph.json')
    assert set(index['tasks']) == {t['id'] for t in data['tasks']}
    assert set(index['modules']) == set(REFERENCE)
    maximum = 0
    for t in data['tasks']:
        text = pack(t['id'], check=False)
        p = json.loads(text)
        assert p['task_exact'] == t
        assert p['constraints_exact'] == read('CONSTRAINTS.md')
        assert {x['source_id'] for x in p['requirements_exact']} == set(t['source_ids'] + t['requirement_refs'] + t.get('implementation_requirements', []))
        assert [x['id'] for x in p['prerequisites']] == t['dependencies']
        assert p['task_exact']['acceptance'] == t['acceptance']
        assert len(p['real_code_neighbors']['edges']) <= 12
        assert p['real_code_neighbors']['max_hops'] == 1
        assert set(t['open_decisions']) <= set(p['decisions_exact'])
        # Confirmed decisions linked by requirements must survive even when not open blockers.
        import re
        referenced = {d for r in p['requirements_exact'] for d in re.findall(r'D-\d{2}',r['source_text'])}
        assert referenced <= set(p['decisions_exact'])
        assert p['task_exact']['proposed_files'] == t['proposed_files']
        assert p['task_exact'].get('human_gate') == t.get('human_gate')
        for edge in p['real_code_neighbors']['edges']:
            assert edge in graph['edges']
        maximum = max(maximum, len(text.encode('utf-8')))
    bad = json.loads(encode(m)); bad['sources']['CONSTRAINTS.md']='0'*64
    bad_srs = json.loads(encode(m)); bad_srs['sources'][AI+'SRS.md']='0'*64
    bad_metrics = load('graphify-out/MEASUREMENTS.json')
    bad_metrics['baseline']['utf8_bytes'] += 1
    for label, operation in [('unknown ID', lambda: pack('UNKNOWN',check=False)),
                             ('stale source hash', lambda: fresh(bad)),
                             ('stale SRS baseline', lambda: fresh(bad_srs)),
                             ('modified measurement', lambda: verify_metrics(m, metrics=bad_metrics)),
                             ('budget overflow', lambda: pack('P10-03',budget=1024,check=False))]:
        try:
            operation()
        except InvalidContext:
            print('REJECTED negative control: ' + label)
        else:
            raise AssertionError(label + ' unexpectedly accepted')
    graph = load('graphify-out/graph.json')
    assert all(e.get('confidence') in {'EXTRACTED','INFERRED'} for e in graph['edges'])
    assert all(e['confidence']=='REGISTRY_DECLARED_NOT_CODE' for e in index['relations'])
    for edge in graph['edges']:
        if edge.get('source_file'):
            assert edge['source_file'] in source_paths(), edge['source_file']
    print(f'PASS: all {len(data["tasks"])} packs, 7 modules, exact criteria/deps/decisions/constraints, '
          f'bounded neighbors. Largest pack {maximum} bytes. Original inputs unmodified.')


def measure(emit=True):
    manifest = fresh(verify_measurements=False)
    # Explicit reproducible baseline: canonical source, SRS, decision/constraint/module specs,
    # complete canonical backlog and requirement registry, excluding duplicated generated phase cards.
    baseline = ['docs/YEU_CAU_HIEN_HANH.md','CONSTRAINTS.md', AI+'SRS.md',AI+'DECISIONS.md',
                AI+'backlog.json',AI+'requirements.json']
    baseline += sorted(p.relative_to(ROOT).as_posix() for p in (ROOT/(AI+'modules')).glob('*.md'))
    text = ''.join(read(p) for p in baseline)
    def counts(s):
        return {'unicode_characters':len(s),'utf8_bytes':len(s.encode('utf-8')),
                'token_estimate_ceil_chars_div4_NOT_TOKENIZER':math.ceil(len(s)/4)}
    result = {'schema_version':SCHEMA,'hash_policy':HASH_POLICY,'graphify_version':VERSION,
              'source_fingerprint':fingerprint(manifest['sources']),
              'map_fingerprint':fingerprint(manifest['outputs']),
              'pack_algorithm_sha256':sha('docs/context/context_nav.py'),
              'baseline_files':baseline,'baseline_file_sha256':{p:sha(p) for p in baseline},
              'baseline':counts(text),
              'method':'Exact Unicode characters and UTF-8 bytes of decoded prompt input (UTF-8 BOM removed, newlines normalized to LF); not raw on-disk file byte totals. chars/4 ceiling is heuristic, not model tokenizer or billing.',
              'tasks':{tid:counts(pack(tid,check=False)) for tid in ['P01-01','P10-03','P40-05']},
              'pack_sha256':{tid:hashlib.sha256(pack(tid,check=False).encode('utf-8')).hexdigest()
                             for tid in ['P01-01','P10-03','P40-05']}}
    write('graphify-out/MEASUREMENTS.json',encode(result))
    certificate={'schema_version':SCHEMA,'hash_policy':HASH_POLICY,'graphify_version':VERSION,
                 'source_fingerprint':fingerprint(manifest['sources']),
                 'map_fingerprint':fingerprint(manifest['outputs']),
                 'measurement_sha256':fingerprint(result)}
    write('graphify-out/measurements-manifest.json',encode(certificate))
    if emit:
        print(encode(result))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command',choices=['build','_build','check','task','module','test','measure'])
    parser.add_argument('id',nargs='?');parser.add_argument('--out');parser.add_argument('--budget',type=int,default=MAX_PACK)
    args=parser.parse_args()
    try:
        if args.command=='build':
            subprocess.run([sys.executable,str(Path(__file__).resolve()),'_build'],check=True,timeout=120)
        elif args.command=='_build':build()
        elif args.command=='check':fresh();print('FRESH: schema, inventory, source and map hashes match')
        elif args.command=='test':test()
        elif args.command=='measure':measure()
        elif args.command=='task':
            text=pack(args.id,args.budget)
            if args.out:
                # Context packs are working material; explicit location, never generated into git by default.
                Path(args.out).write_text(text,encoding='utf-8');print(f'Wrote {len(text.encode("utf-8"))} bytes to {args.out}')
            else:print(text,end='')
        elif args.command=='module':
            fresh();index=load('graphify-out/registry-index.json')
            if args.id not in index['modules']:raise InvalidContext('UNKNOWN_MODULE: '+str(args.id))
            print(encode({'module':args.id,'task_ids':index['modules'][args.id],
                          'source_anchor':AI+'modules/'+args.id+'.md','scope':SCOPE}))
    except (InvalidContext,subprocess.TimeoutExpired,subprocess.CalledProcessError) as error:
        print(str(error),file=sys.stderr);return 2
    return 0


if __name__=='__main__':
    raise SystemExit(main())
