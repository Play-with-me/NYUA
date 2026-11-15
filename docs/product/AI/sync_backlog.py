"""Render task presentations from backlog.json, the sole editable task registry."""
from pathlib import Path
import json
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
TASKDIR=ROOT/'tasks'
def load(): return json.loads((HERE/'backlog.json').read_text(encoding='utf-8'))
def card(t):
    fields=[('Trạng thái / điều kiện bắt đầu',t['status']+' / '+t['readiness']),('Phân hệ',t['module']),('Môi trường và mô hình chính xác',json.dumps(t['execution'],ensure_ascii=False)),('Vai trò',t['owner_role']),('Mã yêu cầu',', '.join(t['requirement_refs']) or 'Enabler; linked predecessors define bounded output.'),('Quyết định / rào cản',', '.join(t['open_decisions']) or 'Scope authorization and evidence prerequisites remain open.'),('Đầu vào','; '.join(t['inputs'])),('Đầu ra',t['output']),('Phụ thuộc',', '.join(t['dependencies']) or 'None'),('File thực có trong phạm vi dự kiến','; '.join(t['actual_allowed_files']) or 'None; all below are proposed.'),('Whitelist đề xuất — chưa cho phép sửa sản phẩm','; '.join(t['proposed_files'])),('Các bước cụ thể','\n'.join(f'{i}. {s}' for i,s in enumerate(t['steps'],1))),('Tiêu chí nghiệm thu','\n'.join(f'- [ ] {aid}: {a}' for aid,a in zip(t['acceptance_ids'],t['acceptance']))),('Lệnh thực có — chỉ kiểm hồ sơ',t['verification']),('Kiểm chứng tương lai — CHƯA CHẠY',json.dumps(t['future_verification'],ensure_ascii=False)),('Chủ nhiệm chuẩn bị công cụ',t['bootstrap_owner'] or 'This is a planning/research/checkpoint task; any executable probe still requires scoped authorization and an established bounded command.'),('Gate nghiệm thu người dùng',json.dumps(t.get('human_gate',{'required':False,'note':'No user approval inferred; linked checkpoint may require it.'}),ensure_ascii=False)),('Owner triển khai cho yêu cầu',', '.join(t.get('implementation_requirements',[])) or 'Không phải task triển khai; xem predecessor.'),('Mã phi chức năng',', '.join(t.get('nfr_refs',[])) or 'See linked requirement / prerequisite scope.')]
    return '\n'.join([f"## [{t['id']}] {t['title']}\n"]+[f'**{k}:**\n\n{v}\n' for k,v in fields])
def outputs(data):
    tasks=data['tasks']; groups={}
    for t in tasks:groups.setdefault(t['id'].split('-')[0],[]).append(t)
    out={}
    for group,ts in groups.items():out[TASKDIR/f'phase-{group.lower()}.md']=f'# {group} task cards\n\nGenerated from docs/product/AI/backlog.json. Grouping is navigation only; dependencies below determine dispatch. No phase-level edges. All future work requires separate authorization.\n\n'+'\n'.join(card(t) for t in ts)
    out[HERE/'BACKLOG.md']='# Canonical backlog navigation\n\nEditable source: [backlog.json](backlog.json). Run `python docs/product/AI/sync_backlog.py` to regenerate all task cards. No task is authorized by this dossier. Active E02a tracker is unchanged.\n\n'+f"Tasks: {len(tasks)}; nonfunctional contracts: {len(data['nonfunctional_requirements'])}.\n\n"+'\n'.join(f"- [{g}: {len(ts)} tasks](../../../tasks/phase-{g.lower()}.md)" for g,ts in groups.items())+'\n'
    human=['# Công việc và điều kiện bắt đầu\n\nDanh sách dự kiến; chưa được phép xây sản phẩm. Không thay tracker và bằng chứng nghiệm thu E02a. Thứ tự thực hiện theo phụ thuộc từng việc, không theo thứ tự nhóm.\n']
    for t in tasks: human.append(f"## {t['id']} — {t['title']}\n\nKết quả cần có: {t['output']}.\n\nLàm sau: {', '.join(t['dependencies']) or 'Không việc trước; vẫn cần duyệt phạm vi.'}.\n\nKiểm tra: "+' '.join(t['acceptance'])+f"\n\n[Thẻ đầy đủ](../../../tasks/phase-{t['id'].split('-')[0].lower()}.md). Chưa chạy/chưa nghiệm thu.\n")
    out[HERE.parent/'HUMAN/07-CONG-VIEC.md']='\n'.join(human)
    return out
def sync():
    data=load()
    for p,text in outputs(data).items():p.write_text(text,encoding='utf-8')
    import csv
    req=json.loads((HERE/'requirements.json').read_text(encoding='utf-8'))['records']
    rows=[]
    for r in req:
        owners=[t for t in data['tasks'] if r['source_id'] in t.get('implementation_requirements',[])]
        verification=next(t['id'] for t in data['tasks'] if t['id'].startswith('V00') and t['requirement_refs']==[r['source_id']])
        for owner in owners or [{'id':'DEFERRED'}]:rows.append({'requirement':r['source_id'],'implementation_owner':owner['id'],'acceptance_id':r['acceptance_id'],'verification_task':verification,'scope':r['scope'],'final_gate':'C00-04 -> P60-04 -> P60-05 -> C00-05' if owners else 'Deferred exclusion review'})
    with (HERE/'TASK_TRACEABILITY.csv').open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    print(f"Generated exact task cards for {len(data['tasks'])} tasks; registry unchanged.")
if __name__=='__main__':sync()
