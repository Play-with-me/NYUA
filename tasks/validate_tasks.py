"""Task consistency and readiness validation; no production or approval claims."""
from pathlib import Path
import copy,importlib.util,json,re,sys
ROOT=Path(__file__).resolve().parents[1]
HERE=ROOT/'docs/product/AI'
spec=importlib.util.spec_from_file_location('render',HERE/'sync_backlog.py');render=importlib.util.module_from_spec(spec);spec.loader.exec_module(render)
ROLES={'research':('agy','gemini-3.8-flash',None),'memory':('agy','gemini-3.8-flash',None),'qa':('agy','gemini-3.8-flash',None),'ui-features':('agy','gemini-4-hydrogen-low',None),'core':('codex','gpt-6.1-sol','low'),'bug':('codex','gpt-6.1-sol','low'),'finalreview':('codex','gpt-6.1-sol','low')}
def errors(data,req,generated=False):
    e=[]
    def check(ok,msg):
        if not ok:e.append(msg)
    ts=data['tasks'];by={t['id']:t for t in ts};ids=set(by);reqids={r['source_id'] for r in req};nf={n['id'] for n in data['nonfunctional_requirements']}
    check(len(ids)==len(ts),'duplicate task')
    graph={t['id']:set(t['dependencies']) for t in ts};anc={};active=set()
    def visit(k):
        if k in active:raise ValueError('cycle '+k)
        if k in anc:return anc[k]
        active.add(k);a=set()
        for dep in graph[k]:
            check(dep in ids,'missing dependency '+dep)
            if dep in ids:a|={dep}|visit(dep)
        active.remove(k);anc[k]=a;return a
    try:
        for k in ids:visit(k)
    except ValueError as ex:e.append(str(ex));return e
    for t in ts:
        k=t['id'];ex=t['execution'];role=t['owner_role']
        check(role in ROLES and (ex.get('harness'),ex.get('model'),ex.get('effort'))==ROLES.get(role),'invalid role '+k)
        check(t['status']=='DRAFT_NOT_AUTHORIZED' and t['readiness']=='BLOCKED_SCOPE_AUTHORIZATION','false readiness '+k)
        check(0<len(t['proposed_files'])<=5,'file boundary '+k)
        check(set(t['actual_allowed_files'])<={p for p in t['proposed_files'] if (ROOT/p).is_file()},'actual files invented '+k)
        check(set(t['requirement_refs'])<=reqids,'unknown requirement '+k)
        check(set(t.get('nfr_refs',[]))<=nf,'unknown NFR '+k)
        check(len(t['acceptance'])>=2 and len(t['acceptance'])==len(t['acceptance_ids']),'acceptance count '+k)
        for a in t['acceptance']:
            check(isinstance(a,str) and len(a.strip())>=40 and not re.fullmatch(r'(?i)(TBD|TODO|pass|done|test|ok)[.! ]*',a.strip()),'invalid acceptance '+k)
        check(len(t['steps'])>=3 and all(len(s)>40 for s in t['steps']),'unactionable steps '+k)
        fv=t['future_verification']
        if t.get('task_kind')=='document_review':
            check(fv['state']=='NOT_APPLICABLE_DOCUMENT_REVIEW' and fv['owner'] is None and t['bootstrap_owner'] is None and 'no executable bootstrap prerequisite' in fv['gate'],'document runner deadlock '+k)
        else:check(fv['state']=='GATED_NOT_RUN' and fv['command'] is None and len(fv['gate'])>=80,'future command gate '+k)
        b=t['bootstrap_owner']
        if b:check(b in anc[k] and fv['owner']==b,'bootstrap ordering '+k)
        for d in t['open_decisions']:check('A00-'+d.split('-')[1] in anc[k],'decision ordering '+k+' '+d)
    for r in req:
        mapped=[t for t in ts if r['source_id'] in t['requirement_refs'] and t['id'].startswith('V00-')]
        check(len(mapped)==1,'missing coverage '+r['source_id'])
        if mapped:
            check(r['acceptance']==mapped[0]['acceptance'][0],'acceptance drift '+r['source_id'])
            check(r['scope']=='deferred' or r['task'] in anc[mapped[0]['id']],'acceptance before output '+r['source_id'])
    for r in req:
        owners=[t for t in ts if r['source_id'] in t.get('implementation_requirements',[])]
        check(bool(owners) if r['scope']!='deferred' else not owners,'missing implementation ownership '+r['source_id'])
        verification=next((t for t in ts if t['id'].startswith('V00-') and t['requirement_refs']==[r['source_id']]),None)
        for owner in owners:
            check(owner['id'].startswith('P'),'verification-only owner '+r['source_id'])
            check(verification is not None and owner['id'] in anc[verification['id']],'owner evidence ordering '+r['source_id'])
            if ' Quyết định 2026-11-14 ' in r['source_text']:
                clause=r['source_text'].split(' Quyết định 2026-11-14 ',1)[1]
                check(any(clause in a for a in owner['acceptance']),'owner missing confirmed acceptance '+r['source_id'])
    for tid in ['P01-01','P20-01','P60-04','P60-05']:
        gate=by[tid].get('human_gate',{})
        if tid=='P01-01':
            evidence=ROOT/'tasks/E02a-USER-ACCEPTANCE.md'
            statement='Có nhìn rõ và không có chỗ nào bị kẹt, có thể đóng nghiệm thu E02a rồi'
            check(gate.get('required') and gate.get('status')=='OBTAINED'
                  and gate.get('evidence')=='tasks/E02a-USER-ACCEPTANCE.md'
                  and gate.get('date')=='2026-11-15' and gate.get('user_statement')==statement
                  and evidence.exists() and statement in evidence.read_text(encoding='utf-8-sig')
                  and 'remaining technical checklist not automatically passed' in gate.get('scope',''),
                  'false human approval '+tid)
        else:
            check(gate.get('required') and gate.get('status')=='NOT_OBTAINED' and gate.get('evidence') is None,'false human approval '+tid)
    for n in data['nonfunctional_requirements']:
        check(n['task'] in ids and n['id'] in by[n['task']].get('nfr_refs',[]),'missing NFR coverage '+n['id'])
    for checkpoint in data['checkpoints']:
        check(checkpoint in ids and bool(graph.get(checkpoint)),'checkpoint ordering '+checkpoint)
    check(set(data['checkpoints'])-{'C00-05'}<=anc.get('C00-05',set()),'final checkpoint omits prior checkpoint')
    for tid in ['P60-04','P60-05']:
        required={t['id'] for t in ts if t['id'].startswith(('V00-','N00-')) and not t.get('deferred')}
        check(required<=anc[tid],'release bypass '+tid)
    for t in ts:
        if t['id'].startswith('B00-'):
            if t['id']=='B00-02':
                expected={'docs/experiments/bootstrap-desktop-body.md','tests/bootstrap/desktop-body/GodotFixture/project.godot','tests/bootstrap/desktop-body/GodotFixture/export_presets.cfg','tests/bootstrap/desktop-body/GodotFixture/scenes/Bootstrap.tscn','tests/bootstrap/desktop-body/GodotFixture/scripts/BootstrapVerify.gd'}
                check(set(t['proposed_files'])==expected,'Godot fixture ownership '+t['id'])
                check('P02-01' not in anc[t['id']],'Godot fixture ownership circularity')
            else:check(any(p.startswith('tests/bootstrap/') for p in t['proposed_files']) and any(p.startswith('tools/verify/') for p in t['proposed_files']),'bootstrap fixture scope '+t['id'])
            check('does not require a pre-existing' in t['future_verification']['gate'],'bootstrap self-deadlock '+t['id'])
    for source,forbidden in [('NV11','buổi làm lành'),('QH05','Shift'),('SH04','tai cáo')]:
        row=next(r for r in req if r['source_id']==source)
        check(forbidden not in row['source_text'],'cross-requirement contamination '+source)
    writers={}
    for t in ts:
        for p in t['proposed_files']:writers.setdefault(p,[]).append(t['id'])
    for p,ks in writers.items():
        for i,a in enumerate(ks):
            for b in ks[i+1:]:check(a in anc[b] or b in anc[a],'unordered file conflict '+p+' '+a+' '+b)
    check({t['module'] for t in ts}=={'policy','life-state','desktop-body','perception','task-execution','companion','distribution'},'module coverage')
    if generated:
        for p,expected in render.outputs(data).items():check(p.exists() and p.read_text(encoding='utf-8-sig')==expected,'generated card drift '+str(p.relative_to(ROOT)))
        for p in (ROOT/'tasks').glob('phase-*.md'):check(p in render.outputs(data),'obsolete divergent phase '+p.name)
    return e

def main():
    data=render.load();req=json.loads((HERE/'requirements.json').read_text(encoding='utf-8'))['records']
    e=errors(data,req,True)
    if e:print('\n'.join(e));return 1
    print(f"PASS: {len(data['tasks'])} task cards exactly match canonical fields; {len(req)} requirement acceptance mappings; {len(data['nonfunctional_requirements'])} NFRs; DAG/references/roles/bootstrap/decision/checkpoint/file-conflict/readiness checks.")
    if '--negative-controls' in sys.argv:
        cases={}
        x=copy.deepcopy(data);x['tasks'][0]['dependencies'].append(x['tasks'][0]['id']);cases['cycle']=x
        x=copy.deepcopy(data);next(t for t in x['tasks'] if t['id'].startswith('V00-'))['requirement_refs']=[];cases['missing coverage']=x
        x=copy.deepcopy(data);x['tasks'][0]['acceptance'][0]='OK';cases['invalid acceptance']=x
        x=copy.deepcopy(data);x['tasks'][0]['dependencies'].append('MISSING');cases['missing dependency']=x
        x=copy.deepcopy(data);x['tasks'][0]['execution']['model']='pro';cases['invalid role']=x
        x=copy.deepcopy(data);next(t for t in x['tasks'] if t['bootstrap_owner'])['bootstrap_owner']='MISSING';cases['bootstrap ordering']=x
        x=copy.deepcopy(data);next(t for t in x['tasks'] if t['id']=='P60-04')['dependencies']=[v for v in next(t for t in x['tasks'] if t['id']=='P60-04')['dependencies'] if v!='C00-04'];cases['release bypass']=x
        x=copy.deepcopy(data);next(t for t in x['tasks'] if t['id']=='P00-01')['future_verification']['state']='GATED_NOT_RUN';cases['document runner deadlock']=x
        x=copy.deepcopy(data);next(t for t in x['tasks'] if t['id']=='B00-02')['proposed_files'].pop();cases['Godot fixture ownership']=x
        x=copy.deepcopy(data);next(t for t in x['tasks'] if t['id']=='P01-01')['human_gate']['evidence']='missing.md';cases['false human approval']=x
        for name,x in cases.items():
            result=errors(x,req)
            if not any(name in s for s in result):print('NEGATIVE CONTROL FAILED: '+name);return 1
            print('REJECTED negative control: '+name)
        print('Negative controls used deep copies in memory; real inputs untouched.')
    return 0
if __name__=='__main__':raise SystemExit(main())
