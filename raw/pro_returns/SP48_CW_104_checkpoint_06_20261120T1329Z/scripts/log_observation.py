"""Append one main crop observation and mark exactly one planned view complete."""
from pathlib import Path
import json,sys
out=Path(__file__).resolve().parents[1]
n,k=map(int,sys.argv[1:3]);record=out/f'records/scan{n:03d}'
p=record/'main_crop_plan.json';plan=json.loads(p.read_text())
item=next(x for x in plan if x['number']==k)
if item['viewed']:raise RuntimeError('Observation already recorded; no repeat view')
s=sys.stdin.read().strip()
if not s:raise RuntimeError('Observation text required')
with (record/'main_observations.md').open('a') as f:f.write(f'\n{k}. {s}\n')
item['viewed']=True;p.write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n')
print(f'scan{n:03d} observation{k} recorded')
