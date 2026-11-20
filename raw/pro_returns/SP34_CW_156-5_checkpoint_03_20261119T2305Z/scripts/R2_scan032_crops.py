from pathlib import Path
from PIL import Image
import json
root=Path('/workspace/scratch/4770596940a0'); src='source/SP34_CW_156-5_scans/J156-5-04_156-5_scan032.jpg';im=Image.open(root/src)
p=root/'out/readers/R2/crops032.json'; rec=json.loads(p.read_text())
items=[('initial_F',[505,30,630,135],5,0),('reste',[275,100,965,205],4,0),('raised_G',[975,60,1305,210],5,0),('deleted_On_top',[1470,170,1615,255],5,0),('union',[270,265,685,420],5,0),('primes',[745,235,1650,370],3,0),('end_gagne',[855,535,1495,630],4,0),('cor_article',[505,655,1000,800],4,0),('chacune',[660,715,1070,850],4,0),('a_induit',[250,1010,710,1120],4,0),('a_insert_rot',[480,1040,950,1155],4,-8),('a_unknown',[1080,1115,1235,1260],5,0),('a_dans',[1150,1040,1510,1175],4,0),('b_can',[935,1310,1270,1430],4,0),('NB_abbrev',[1340,1410,1640,1515],4,0),('c_deletion',[475,1620,1550,1765],3,0),('dem_on',[165,1940,550,2085],5,0),('pex',[745,1980,920,2075],5,0),('bottom_dem',[275,2150,435,2255],5,0),('inclusion',[250,2200,780,2325],5,0),('can_arrow',[620,2175,965,2270],5,0),('long_margin_full_rot',[10,1240,1070,2135],2,-43)]
for name,box,scale,rot in items:
 if any(r['id']==name for r in rec):continue
 c=im.crop(box)
 if rot:c=c.rotate(rot,expand=True,fillcolor='white')
 c=c.resize((c.width*scale,c.height*scale));dest=f'crops/R2/scan032_{name}.png';c.save(root/dest)
 rec.append(dict(id=name,path=dest,source=src,bbox=box,rotation=rot,scale=scale))
p.write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n')
print('recipes',len(rec))
