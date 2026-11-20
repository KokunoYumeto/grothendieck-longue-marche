#!/usr/bin/env python3
"""Called only after the main reader has visually adjudicated the page's crops."""
from pathlib import Path
from datetime import datetime,timezone
import json,sys,shutil,csv,subprocess
root=Path(__file__).resolve().parents[1]
scan=int(sys.argv[1]);page=f'147_scan{scan:03}'
source=root/'reader_returns'/page
reviewed=root/'reviewed'/f'{page}.json'
reviewed.parent.mkdir(exist_ok=True)
if not reviewed.exists():shutil.copyfile(source/'report.json',reviewed)
r=json.loads(reviewed.read_text())
assert r.get('root_review_complete'), 'Main-reader approval required in report'
for c in r.get('changes',[]):
    assert c.get('crop') and (root/'crops'/Path(c['crop']).name).is_file(),c
    assert len(c.get('box',[]))==4,c
if not (root/'pages'/f'{page}.tex').exists():shutil.copyfile(source/'proposed.tex',root/'pages'/f'{page}.tex')
boxes=r.get('second_boxes',[])
with (root/'second'/f'{page}_boxes.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['box','kind','x0','y0','x1','y1'],delimiter='\t',extrasaction='ignore');w.writeheader();w.writerows(boxes)
with (root/'second'/f'{page}_first.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['box','reading'],delimiter='\t',extrasaction='ignore');w.writeheader();w.writerows(boxes)
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
places=len(list((root/'crops').glob(f'{page}_place*')))+len(list((root/'crops').glob(f'{page}_root*')))
with (root/'progress.log').open('a') as f:f.write(f"scan {scan:03} done {now} cote 147: {r['physical_lines_read']} lines read, {places} places cropped, {len(r['changes'])} rows\n")
subprocess.run([sys.executable,str(root/'scripts/build_deliverables.py')],check=True)
