"""Run only after the main reader has inspected every reported disagreement crop."""
from pathlib import Path
from datetime import datetime,timezone
import json,csv,sys,shutil,subprocess
r=Path(__file__).resolve().parents[1];page=sys.argv[1]
p=r/'work'/f'{page}_report.json';data=json.loads(p.read_text())
assert data['page']==page
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
data['root_approved']=True;data['approved_at']=stamp
shutil.copyfile(r/'work'/f'{page}.tex',r/'pages'/f'{page}.tex')
(r/'work'/f'{page}_final.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
with (r/'second'/f'{page}_boxes.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['box','kind','x0','y0','x1','y1'],delimiter='\t',extrasaction='ignore');w.writeheader();w.writerows(data['second_boxes'])
with (r/'second'/f'{page}_first.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['box','reading'],delimiter='\t',extrasaction='ignore');w.writeheader();w.writerows(data['second_boxes'])
subprocess.run([sys.executable,str(r/'scripts/build_deliverables.py')],check=True)
crops=list((r/'crops').glob(page+'_*.png'))
cote,scan=page.split('_scan')
with (r/'progress.log').open('a') as f:f.write(f'scan {scan} done {stamp} cote {cote}: {data["line_count"]} lines read, {len(crops)} places cropped, {len(data["changes"])} rows\n')
print(page,'approved')
