from PIL import Image
from pathlib import Path
import json
p=Path('work/crops119.json');rs=json.loads(p.read_text());src=rs[0]['source'];im=Image.open(Path('source')/src)
items=[('trucs-over',[1305,163,1352,212],22,0),('remarque-over',[344,1361,373,1405],26,0),('NB-unit',[1411,1904,1490,1958],18,-1),('NB-dash',[972,1944,1007,1971],24,0),('handcancel-upright',[470,1103,1001,1159],10,-2),('exists-guide',[390,566,1471,675],6,0)]
for ident,box,scale,rotation in items:
 rs.append(dict(id=ident,source=src,box=box,scale=scale,rotation=rotation));o=im.crop(box)
 if rotation:o=o.rotate(rotation,expand=True,fillcolor='white')
 o.resize((o.width*scale,o.height*scale)).save(f'work/crops/10-119-{ident}.png')
p.write_text(json.dumps(rs,indent=2));print(len(rs))
