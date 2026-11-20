from pathlib import Path
import sys,json,csv,subprocess
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]
scan=int(sys.argv[1]);stem=f'147_scan{scan}'
report=ROOT/'review'/f'{stem}_reviewed.json'
if not report.exists():raise RuntimeError('Root-reviewed report required')
d=json.loads(report.read_text());d['reviewed_at']=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
report.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
page=ROOT/'pages'/f'{stem}.tex'
if not page.exists():page.write_text((ROOT/'reports'/f'{stem}_proposed.tex').read_text())
with (ROOT/'second'/f'{stem}_boxes.tsv').open('w') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['box','kind','x0','y0','x1','y1'])
    for b in d['second_boxes']:w.writerow([b['box'],b['kind'],*b['coords']])
with (ROOT/'second'/f'{stem}_first.tsv').open('w') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['box','reading'])
    for b in d['second_boxes']:w.writerow([b['box'],b['reading']])
subprocess.run([sys.executable,str(ROOT/'scripts/assemble.py')],check=True)
crops=list((ROOT/'crops').glob(f'{stem}_*.jpg'))
with (ROOT/'progress.log').open('a') as f:f.write(f'scan {scan:03d} done {d["reviewed_at"]} cote 147: {d["line_count"]} lines read, {len(crops)} places cropped, {len(d["rows"])} rows\n')
print('Committed',scan)
