from PIL import Image, ImageOps, ImageFilter
from pathlib import Path
import json
root=Path('/workspace/scratch/f28c4f52d3ec'); page='148_scan064'
im=Image.open(root/'source/SP83_C13_148+149_scans/148_scan064.jpg').convert('RGB')
items=[
 ('bouchage',[1060,75,1345,184],0),
 ('cela',[1170,183,1435,274],0),
 ('operation5',[988,468,1395,608],0),
 ('liaison',[1118,817,1576,932],0),
 ('avec_ca',[310,975,630,1073],0),
 ('celle_des',[895,1061,1516,1152],0),
 ('pi_tuple',[978,1113,1570,1249],0),
 ('nonempty_base',[596,1201,1475,1355],0),
 ('donnee_comme',[855,1455,1457,1553],0),
 ('nouvelle',[307,1596,936,1707],0),
 ('representation',[959,1542,1624,1664],0),
 ('du_groupoide',[318,1701,1307,1810],0),
 ('covering_insert',[1286,1623,1660,1751],0),
 ('revetement',[307,1781,1019,1922],0),
 ('du_groupoide_final',[304,1915,1245,2039],0),
 ('margin',[20,1303,543,1953],-19),
 ('bottomfolio',[52,2268,137,2340],0),
]
records=[]
for name,box,angle in items:
 p=root/'result/crops'/f'{page}_{name}.png'
 region=ImageOps.autocontrast(im.crop(box))
 if angle: region=region.rotate(angle,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
 scale=max(3,min(8,3000/region.width)); region=region.resize((round(region.width*scale),round(region.height*scale)),Image.Resampling.LANCZOS)
 region=region.filter(ImageFilter.UnsharpMask(1.2,105,3)); region.save(p)
 records.append(dict(name=name,path=str(p),crop=f'crops/{p.name}',box=box,rotation=angle,viewed=False))
(root/'proposed'/f'{page}_crop_boxes.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print(f'Created {len(records)} first-reading evidence crops.')
