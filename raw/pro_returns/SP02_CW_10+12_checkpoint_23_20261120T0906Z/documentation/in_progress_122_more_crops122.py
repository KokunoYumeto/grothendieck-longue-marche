from PIL import Image
from pathlib import Path
import json
p=Path('work/crops122.json');rs=json.loads(p.read_text());src=rs[0]['source'];im=Image.open(Path('source')/src)
items=[('change-en',[1415,435,1469,483],26,0),('change-phi',[1462,419,1547,488],24,0),('ax-close',[1401,787,1435,832],30,0),('savoir-sa',[250,857,303,908],30,0),('savoir-sample',[386,856,509,908],20,0),('cinsertion-full',[610,941,919,1060],13,0),('koko-close',[1252,1065,1309,1121],30,0),('dimension-close',[786,1291,845,1340],30,0),('margin-detail',[17,1270,310,1600],12,-30),('margin-bottom',[17,1532,282,1671],16,-30),('cancel-colon',[593,1417,729,1480],24,0),('compatible-le',[632,1485,697,1545],30,0),('C-over',[1518,1485,1574,1546],30,0),('final-cancel-top',[1051,1971,1137,2025],28,0),('final-cancel-bottom',[1051,2002,1226,2050],24,0),('final-cancel-wide',[1009,1962,1251,2058],15,0),('tri-close',[252,505,323,555],28,0),('G2punct-close',[1613,336,1665,404],28,0)]
for ident,box,scale,rot in items:
 rs.append(dict(id=ident,source=src,box=box,rotation=rot,scale=scale));o=im.crop(box)
 if rot:o=o.rotate(rot,expand=True,fillcolor='white')
 o.resize((o.width*scale,o.height*scale)).save(f'work/crops/10-122-{ident}.png')
p.write_text(json.dumps(rs,indent=2));print(len(rs))
