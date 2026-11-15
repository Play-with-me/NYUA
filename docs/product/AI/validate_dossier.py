"""Consistency validator only. Passing does not certify semantics, safety, or readiness."""
from pathlib import Path
import csv
from source_hash import SOURCE_HASH_POLICY, canonical_source_text, source_sha256
import json
import re
import xml.etree.ElementTree as ET
from PIL import Image

ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
DOSSIER=HERE.parent
MODULES={'policy','life-state','desktop-body','perception','task-execution','companion','distribution'}

def validate():
    errors=[]
    def check(condition,message):
        if not condition: errors.append(message)
    source=canonical_source_text(ROOT/'docs/YEU_CAU_HIEN_HANH.md')
    data=json.loads((HERE/'requirements.json').read_text(encoding='utf-8'))
    requirements=data['records']
    tasks=json.loads((HERE/'backlog.json').read_text(encoding='utf-8'))['tasks']
    ids={r['source_id'] for r in requirements}
    taskids={t['id'] for t in tasks}
    check(len(ids)==len(requirements),'Duplicate source IDs')
    check(len(taskids)==len(tasks),'Duplicate task IDs')
    check(data.get('source_hash_policy')==SOURCE_HASH_POLICY,'Unknown canonical source hash policy')
    check(data['source_sha256']==source_sha256(ROOT/'docs/YEU_CAU_HIEN_HANH.md'),'Canonical source hash drift')
    original={}
    for line in source.splitlines():
        m=re.match(r'^\| ([A-Z]{2}\d{2})[^|]*\| (.+) \|$',line) or re.match(r'^- \*\*([A-Z]{2}\d{2}):\*\* (.+)$',line)
        if m:original[m.group(1)]=m.group(2)
    check({r['source_id'] for r in requirements if r['source_kind']=='explicit_id'}==set(original),'Missing/extra source IDs')
    srs=(HERE/'SRS.md').read_text(encoding='utf-8')
    human=(DOSSIER/'HUMAN/02-YEU-CAU.md').read_text(encoding='utf-8')
    ucs=set(re.findall(r'^## (UC-\d{2}) ',(HERE/'USE_CASES.md').read_text(encoding='utf-8'),re.M))
    decisions=set(re.findall(r'^\| (D-\d{2}) ',(HERE/'DECISIONS.md').read_text(encoding='utf-8'),re.M))
    for r in requirements:
        key=r['source_id']
        if key in original:check(original[key]==r['source_text'],f'Source text drift: {key}')
        check(f"### {r['id']}" in srs and r['source_text'] in srs,f'SRS omission: {key}')
        check(f'## {key}\n' in human and r['source_text'] in human,f'Human omission: {key}')
        check(r['human_acceptance'] in human,f'Human acceptance omission: {key}')
        check(r['module'] in MODULES,f'Unknown module: {key}')
        check(r['use_case'] in ucs,f'Unknown use case: {key}')
        check(r['task'] in taskids or (r['scope']=='deferred' and r['task']=='DEFERRED'),f'Unknown task: {key}')
        check(len(r['acceptance'].strip())>=40 and len(r['human_acceptance'].strip())>=40,f'Invalid acceptance length: {key}')
        check(r['acceptance_status']=='draft_for_review',f'Acceptance falsely approved: {key}')
    with (HERE/'TRACEABILITY.csv').open(encoding='utf-8-sig',newline='') as f:rtm=list(csv.DictReader(f))
    check(len(rtm)==len(requirements),'RTM count differs')
    for row,r in zip(rtm,requirements):
        check(all(row[k]==r[k] for k in row),f'RTM drift: {r["source_id"]}')
    graph={t['id']:t['dependencies'] for t in tasks}
    for t in tasks:
        check(t['module'] in MODULES,f'Unknown task module: {t["id"]}')
        check(t['status']=='DRAFT_NOT_AUTHORIZED',f'Task falsely started/authorized: {t["id"]}')
        check(0<len(t['proposed_files'])<=5,f'File scope invalid: {t["id"]}')
        check(bool(t['acceptance']) and all(len(a.strip())>=40 for a in t['acceptance']) and bool(t['verification']),f'Missing criteria: {t["id"]}')
        check(set(t['dependencies'])<=taskids,f'Missing dependency: {t["id"]}')
        check(set(t['source_ids'])<=ids,f'Unknown source on task: {t["id"]}')
        check(set(t['open_decisions'])<=decisions,f'Unknown decision: {t["id"]}')
        expected={r['source_id'] for r in requirements if r['task']==t['id']}
        check(expected==set(t['source_ids']),f'Task source mapping drift: {t["id"]}')
    active=set();seen=set()
    def visit(n):
        if n in active: raise ValueError(f'Task cycle: {n}')
        if n in seen:return
        active.add(n)
        for dep in graph.get(n,[]):visit(dep)
        active.remove(n);seen.add(n)
    try:
        for n in graph:visit(n)
    except ValueError as e:errors.append(str(e))
    for module in MODULES:check((HERE/f'modules/{module}.md').exists(),f'Missing module spec: {module}')
    for p in DOSSIER.rglob('*.md'):
        text=p.read_text(encoding='utf-8')
        check(text.count('```')%2==0,f'Code fence not closed: {p.name}')
        for link in re.findall(r'\]\(([^)]+)\)',text):
            if '://' in link or link.startswith('#'):continue
            check((p.parent/link.split('#')[0]).exists(),f'Missing local link: {p.relative_to(DOSSIER)} -> {link}')
    mmd=list((DOSSIER/'diagrams').glob('*.mmd'))
    check(len(mmd)==15,'Mermaid source inventory differs')
    for p in mmd:
        check(p.read_text(encoding='utf-8').splitlines()[0].split()[0] in {'flowchart','sequenceDiagram','stateDiagram-v2','erDiagram'},f'Unsupported diagram header: {p.name}')
    for name in ['architecture','delivery','permissions','data']:
        with Image.open(DOSSIER/f'diagrams/{name}.png') as im:check(im.width>=1400 and im.height>=1000,f'Image size: {name}')
        ET.parse(DOSSIER/f'diagrams/{name}.svg')
    import importlib.util
    spec=importlib.util.spec_from_file_location('taskchecks',ROOT/'tasks/validate_tasks.py')
    checks=importlib.util.module_from_spec(spec);spec.loader.exec_module(checks)
    errors.extend(checks.errors(json.loads((HERE/'backlog.json').read_text(encoding='utf-8')),requirements,True))
    print(f'Requirements={len(requirements)}; task proposals={len(tasks)}; module specs=7; use cases={len(ucs)}; Mermaid={len(mmd)}; PNG/SVG=4 pairs')
    if errors:
        print('\n'.join(errors));return 1
    print('PASS: source fidelity, two-edition coverage, references, RTM, task DAG, statuses, links and image containers.')
    print('Not checked: semantic approval, Mermaid rendering, production feasibility, security or native runtime.')
    return 0

if __name__=='__main__':raise SystemExit(validate())
