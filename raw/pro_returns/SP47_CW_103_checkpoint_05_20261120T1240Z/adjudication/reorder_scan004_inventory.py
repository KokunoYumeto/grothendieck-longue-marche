"""Order the completed inventory by its already-recorded source y coordinates.

This is a metadata-only change; no new image or textual reading is made.
"""
from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[1]
p=R/'decisions/scan004.json'
d=json.loads(p.read_text())
def y(row):
    found=re.search(r'y≈(\d+)',row['position'])
    if not found:raise ValueError(row['position'])
    return int(found[1])
d['inventory'].sort(key=y)
for i,row in enumerate(d['inventory'],1):
    row['element']=f'004.{i:03} '+re.sub(r'^004\.\d+ ','',row['element'])
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
