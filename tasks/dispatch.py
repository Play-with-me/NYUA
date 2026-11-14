"""Print dependency order only; never execute or authorize tasks."""
from pathlib import Path
import json
d=json.loads((Path(__file__).resolve().parents[1]/'docs/product/AI/backlog.json').read_text(encoding='utf-8'))
by={t['id']:t for t in d['tasks']};seen=set();active=set();order=[]
def visit(k):
    if k in active:raise ValueError('cycle '+k)
    if k in seen:return
    active.add(k)
    for v in by[k]['dependencies']:visit(v)
    active.remove(k);seen.add(k);order.append(k)
for k in by:visit(k)
for k in order:print(k+' | '+by[k]['title']+' | BLOCKED: separate scope authorization + dependencies/evidence')
