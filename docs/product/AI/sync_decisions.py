"""Synchronize confirmed clauses into narrative specs from requirements registry."""
from pathlib import Path
import json
HERE=Path(__file__).resolve().parent
IDS={'SH01','QD04','CD01','BH06','BH02','XP07','XP08','AI02','AI01','XP05','NV11','QH05','SP09','SL01','NV01','NV02','SH04'}
def sync():
    records=json.loads((HERE/'requirements.json').read_text(encoding='utf-8'))['records']
    selections={HERE/'BUSINESS_RULES.md':IDS,HERE/'UX.md':IDS,HERE/'ART.md':{'NV01','NV02','NV11','SH04'},HERE.parent/'HUMAN/03-TRAI-NGHIEM.md':IDS}
    for p in (HERE/'modules').glob('*.md'):
        if p.stem=='README':continue
        selected={r['source_id'] for r in records if r['module']==p.stem and r['source_id'] in IDS}
        extra={'policy':{'SH01','AI02','XP05'},'perception':{'SH01','QD04','XP05'},'task-execution':{'SP09','CD01','XP07','XP08','XP05'},'desktop-body':{'SH04'},'distribution':{'CD01','SL01'},'life-state':{'QH05','SH01'},'companion':{'AI02','NV01','NV02'}}
        selections[p]=selected|extra.get(p.stem,set())
    marker='\n<!-- CONFIRMED-2026-11-14 -->'
    for p,ids in selections.items():
        text=p.read_text(encoding='utf-8').split(marker)[0]
        text+=marker+'\n## Quyết định hiện hành 2026-11-14 — ưu tiên hơn wording nháp cũ\n\nSinh từ registry; chỉ phần sau nhãn quyết định là bổ sung đã xác nhận. Chưa triển khai/chưa nghiệm thu; chi tiết kỹ thuật còn mở trong DECISIONS.\n\n'
        for r in records:
            if r['source_id'] in ids and ' Quyết định 2026-11-14 ' in r['source_text']:
                text+='- **'+r['source_id']+':** '+r['source_text'].split(' Quyết định 2026-11-14 ',1)[1]+'\n'
        p.write_text(text,encoding='utf-8')
    print('Synchronized confirmed clauses into module, HUMAN, UX, ART and business specs.')
if __name__=='__main__':sync()
