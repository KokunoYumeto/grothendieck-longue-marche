#!/usr/bin/env python3
from pathlib import Path
import argparse,json,difflib
p=argparse.ArgumentParser();p.add_argument('page');a=p.parse_args()
out=Path(__file__).resolve().parent.parent
for reader in ['R1','R2','R3']:
    d=out/'readers'/a.page/reader
    p=d/'report.json'
    if not p.exists():print(json.dumps({'reader':reader,'pending':True}));continue
    r=json.loads(p.read_text())
    print(json.dumps({'reader':reader,'changes':r.get('changes'),'c_doubts':r.get('c_doubts'),'remaining_doubts':r.get('remaining_doubts'),'notes':r.get('notes'),'check_events':r.get('check_events'),'crops':r.get('crops')},ensure_ascii=False))
print('READING DIFFS:')
first=out/'readers'/a.page/'R1/reading.tex'
if first.exists():
    for other in ['R2','R3']:
        p=out/'readers'/a.page/other/'reading.tex'
        if p.exists():print(''.join(difflib.unified_diff(first.read_text().splitlines(True),p.read_text().splitlines(True),fromfile='R1',tofile=other)))
