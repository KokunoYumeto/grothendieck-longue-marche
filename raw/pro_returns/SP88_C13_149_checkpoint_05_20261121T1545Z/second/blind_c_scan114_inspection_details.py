from PIL import Image
from pathlib import Path
import json,sys
root=Path('/workspace/scratch/0cab6a548abb')
source,name,*coords=sys.argv[1:]
bbox=tuple(map(int,coords))
p=root/'edition/crops'/source
im=Image.open(p)
q=root/'edition/crops'/name
im.crop(bbox).save(q)
log=root/'edition/second/blind_c_scan114_inspection_records.json'
r=json.loads(log.read_text())
r.append({'file':str(q),'derived_from':str(p),'derivative_pixel_bbox':list(bbox),'rotation_degrees':-45 if 'rotate-45' in source else 0,'layout':'detail of saved inspection image'})
log.write_text(json.dumps(r,indent=2),encoding='utf8')
print(q)
