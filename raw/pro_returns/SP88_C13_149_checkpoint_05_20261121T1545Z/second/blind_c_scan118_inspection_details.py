from PIL import Image
from pathlib import Path
import json,sys
root=Path('/workspace/scratch/0cab6a548abb')
source,name,*coords=sys.argv[1:]
bbox=tuple(map(int,coords))
p=root/'edition/crops'/source
q=root/'edition/crops'/name
Image.open(p).crop(bbox).save(q)
log=root/'edition/second/blind_c_scan118_inspection_records.json'
r=json.loads(log.read_text())
r.append({'file':str(q),'derived_from':str(p),'derivative_pixel_bbox':list(bbox),'rotation_degrees':0,'layout':'detail of saved crop'})
log.write_text(json.dumps(r,indent=2),encoding='utf8')
print(q)
