"""Expose independent returns without choosing a reading."""
from pathlib import Path
import json,difflib,argparse
p=argparse.ArgumentParser();p.add_argument('scan',type=int);a=p.parse_args()
r=Path(__file__).resolve().parents[1];n=f'{a.scan:03d}';parts=[]
for role in ['A','B','C']:
    d=r/'readers'/n/role
    report=json.loads((d/'report.json').read_text())
    parts.append(f'## Reader {role}\n\n'+(d/'reading.tex').read_text()+'\n')
    parts.append(json.dumps({k:report.get(k) for k in ['differences','doubts','notes','notation','check_events','brief_feedback']},ensure_ascii=False,indent=2))
for x,y in [('A','B'),('A','C'),('B','C')]:
    xx=(r/'readers'/n/x/'reading.tex').read_text().splitlines()
    yy=(r/'readers'/n/y/'reading.tex').read_text().splitlines()
    parts.append('\n'.join(difflib.unified_diff(xx,yy,fromfile=x,tofile=y,lineterm='')))
out=r/'records'/f'comparison{n}.md';out.write_text('\n\n'.join(parts)+'\n')
print(out)
