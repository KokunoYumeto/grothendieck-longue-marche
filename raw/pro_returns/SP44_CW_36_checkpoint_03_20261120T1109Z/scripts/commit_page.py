"""Commit a decided page, update all records, then append its UTC completion."""
from pathlib import Path
from datetime import datetime,timezone
import sys,json,subprocess,re

out=Path(__file__).resolve().parents[1];n=int(sys.argv[1])
p=out/'decisions'/f'scan{n:03d}.json';d=json.loads(p.read_text())
done=[int(m) for m in re.findall(r'^scan (\d+) done ',(out/'progress.log').read_text(),re.M)]
if done!=list(range(10,n)):raise SystemExit(f'Commit order violation: {done}, next {n}')
for r in ('R1','R2','R3'):
    for f in ('result.json','reading.tex','report.md'):
        if not (out/'readers'/f'scan{n:03d}'/r/f).exists():raise SystemExit(f'Missing {r}/{f}')
if not (out/'pages'/d['filename']).exists():raise SystemExit('Missing final page')
d['decided_utc']=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
subprocess.run([sys.executable,str(out/'scripts/build_records.py')],check=True)
counts=[len(list((out/'crops'/f'scan{n:03d}'/r).glob('*.jpg'))) for r in ('R1','R2','R3','MAIN')]
workflow=out/'SP44_CW_36_workflow.md';s=workflow.read_text()
line=f"| {n:03d} | "+' | '.join(map(str,counts))+f" | {d.get('brief','v01')} | "+d.get('workflow_observation','').replace('|',' / ')+' |\n'
marker='\n## Preservation and reproducibility'
s=s.replace(marker,line+marker)
workflow.write_text(s)
with (out/'progress.log').open('a') as f:f.write(f"scan {n:03d} done {d['decided_utc']}\n")
print(f"Committed scan {n:03d}; crops {counts}")
