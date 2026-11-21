from pathlib import Path
from PIL import Image
import json
root=Path(__file__).resolve().parents[1]
im=Image.open(root.parent/'source/SP88_C13_149_scans/149_scan118.jpg')
rows=[]
for box,bbox,reason in [('b01',[307,375,1310,549],'Canonical audit crop touches the top of the disputed L/I stem; restore its full upper context.'),('b02',[22,490,405,925],'Canonical audit crop clips the right end of the first marginal baseline; restore the complete le after joue.')]:
 p=root/'crops'/f'149_scan118_audit_{box}_context.png'
 if p.exists():raise FileExistsError(p)
 c=im.crop(bbox);c.resize((c.width*3,c.height*3)).save(p)
 rows.append({'box':box,'crop':p.relative_to(root).as_posix(),'bbox':bbox,'reason':reason})
(root/'second/149_scan118_context_repairs.json').write_text(json.dumps(rows,indent=2)+'\n')
