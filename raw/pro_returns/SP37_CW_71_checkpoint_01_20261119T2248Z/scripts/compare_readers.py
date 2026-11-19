#!/usr/bin/env python3
from pathlib import Path
import difflib,json,sys
r=Path(__file__).resolve().parents[1];n=int(sys.argv[1]);d=r/f'readers/scan{n:03d}'
for who in ['R1','R2','R3']:
    p=d/who/'report.json'
    if not p.exists():print(who,'NOT READY');continue
    j=json.loads(p.read_text());print('\nREADER',who,'CROPS',j.get('crop_count'))
    for x in j.get('issues',[]):
        print(json.dumps(x,ensure_ascii=False))
for who in ['R2','R3']:
    a=d/'R1/reading.tex';b=d/who/'reading.tex'
    if a.exists() and b.exists():
        print('\nDIFF R1',who)
        print(''.join(difflib.unified_diff(a.read_text().splitlines(True),b.read_text().splitlines(True),fromfile='R1',tofile=who)))
