#!/usr/bin/env python3
"""Resolve historical ledger paths after later revisions; verify every old hash."""
from pathlib import Path
import csv,hashlib,json,zipfile

root=Path(__file__).resolve().parents[1]
ledger=root/'checkpoint_history.csv'
rows=list(csv.DictReader(ledger.open(newline='')))
cache={}
def digest(p):
    if p not in cache:
        cache[p]=hashlib.file_digest(p.open('rb'),'sha256').hexdigest()
    return cache[p]
index={}
for p in sorted((root/'history').rglob('*')):
    if p.is_file():
        index.setdefault(digest(p),[]).append(p)
changed=[]
missing=[]
for row in rows:
    p=root/row['retained_path']
    if p.is_file() and digest(p)==row['sha256']:
        continue
    choices=index.get(row['sha256'],[])
    if not choices:
        archive=root.parent/('EXIT_TOWER_checkpoint_'+row['checkpoint']+'.zip')
        with zipfile.ZipFile(archive) as z:
            data=z.read(row['original_path'])
        assert hashlib.sha256(data).hexdigest()==row['sha256']
        restored=root/'history'/('checkpoint_'+row['checkpoint'])/row['original_path']
        if restored.exists():
            assert restored.read_bytes()==data
        else:
            restored.parent.mkdir(parents=True,exist_ok=True)
            restored.write_bytes(data)
        choices=[restored]
        index[row['sha256']]=choices
    preferred=root/'history'/('checkpoint_'+row['checkpoint'])/row['original_path']
    chosen=preferred if preferred in choices else choices[0]
    old=row['retained_path']
    row['retained_path']=chosen.relative_to(root).as_posix()
    row['treatment']='prior bytes retained; ledger location resolved after a later revision'
    changed.append({'checkpoint':row['checkpoint'],'original_path':row['original_path'],
                    'old_retained_path':old,'retained_path':row['retained_path']})
assert not missing,json.dumps(missing,indent=2)
qa=root/'qa'/'checkpoint_06'
before=qa/'history_ledger_before_resolution.csv'
if not before.exists():before.write_bytes(ledger.read_bytes())
original={(r['checkpoint'],r['original_path']):r for r in csv.DictReader(before.open(newline=''))}
changed=[{'checkpoint':r['checkpoint'],'original_path':r['original_path'],
          'old_retained_path':original[(r['checkpoint'],r['original_path'])]['retained_path'],
          'retained_path':r['retained_path']}
         for r in rows if original[(r['checkpoint'],r['original_path'])]['retained_path']!=r['retained_path']]
with ledger.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
for row in rows:
    assert digest(root/row['retained_path'])==row['sha256']
result={'historical_members_verified':len(rows),'resolved_paths':len(changed),
        'checkpoint_05_members':sum(r['checkpoint']=='05' for r in rows),
        'missing_members':0,'changes':changed}
(qa/'history_audit.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='changes'},indent=2))
