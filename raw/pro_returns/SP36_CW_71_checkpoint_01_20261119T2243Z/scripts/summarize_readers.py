"""Compact display of independent returns; no automatic adjudication."""
from pathlib import Path
import json,sys,difflib,re
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'out';scan=int(sys.argv[1])
c=(ROOT/'packets'/f'scan{scan:03d}'/'C.tex').read_text()
for name in ['R1','R2','R3']:
    p=OUT/'readers'/f'scan{scan:03d}'/name
    print('\nREADER',name)
    if not (p/'reading.tex').exists():print('No reading file yet.');continue
    t=(p/'reading.tex').read_text()
    diff=list(difflib.unified_diff(c.splitlines(True),t.splitlines(True),fromfile='C',tofile=name))
    print('TEXT DIFF')
    for line in diff:
        if line.startswith(('+','-')) and ('\\draw' in line or '.. controls' in line or '\\fill' in line):continue
        if line.startswith(('+','-','@@')):print(line.rstrip())
    if not (p/'report.json').exists():print('No report yet.');continue
    r=json.loads((p/'report.json').read_text())
    for i,f in enumerate(r.get('findings',[]),1):
        v={k:f.get(k) for k in ['place','c','h','reading','evidence','crop','diff_c','diff_h','c_doubt','confidence','unresolved']}
        for k in ['c','h','reading']:
            if isinstance(v[k],str) and len(v[k])>350:v[k]=v[k][:250]+' [full figure/long passage in report]'
        print(i,json.dumps(v,ensure_ascii=False))
    print('NOTES',json.dumps(r.get('notes',[]),ensure_ascii=False))
    print('CHECKS',json.dumps(r.get('checks',[]),ensure_ascii=False))
    print('FEEDBACK',json.dumps(r.get('brief_feedback',[]),ensure_ascii=False))
