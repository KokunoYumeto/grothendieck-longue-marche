from PIL import Image
from pathlib import Path
import json
p=Path('work/crops119.json');rs=json.loads(p.read_text());src=rs[0]['source'];im=Image.open(Path('source')/src)
for ident,box,scale,rotation in [('NB-unit-correct',[1460,1898,1610,1985],16,-1),('NB-dash-correct',[970,1900,1060,1985],12,-1)]:
 rs.append(dict(id=ident,source=src,box=box,scale=scale,rotation=rotation));o=im.crop(box).rotate(rotation,expand=True,fillcolor='white');o.resize((o.width*scale,o.height*scale)).save(f'work/crops/10-119-{ident}.png')
p.write_text(json.dumps(rs,indent=2));print(len(rs))
