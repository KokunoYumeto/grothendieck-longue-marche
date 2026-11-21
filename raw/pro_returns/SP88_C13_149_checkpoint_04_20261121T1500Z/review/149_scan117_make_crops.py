from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json
import sys

ROOT=Path('/workspace/scratch/0cab6a548abb')
PAGE='149_scan117'
BOXES={
 'p01': ([270,22,1650,355],0,3000),
 'p02': ([290,740,1505,1052],0,2600),
 'p03': ([290,985,1520,1235],0,2600),
 'p04': ([285,1230,1560,1555],0,3000),
 'p05': ([285,1550,1560,1730],0,3000),
 'p06': ([270,1725,1570,2010],0,3000),
 'p07': ([260,1995,1650,2335],0,3000),
 'p08': ([17,1175,1225,2315],-35,3600),
 'p09': ([130,2312,205,2356],0,1500),
 'p10': ([17,1390,735,2050],-35,3200),
 'p11': ([550,1175,1225,1650],-35,3200),
 'p12': ([17,1695,535,2315],-35,3000),
}
selected=set(sys.argv[1:]) if len(sys.argv)>1 else set(BOXES)
if selected-set(BOXES):
 raise ValueError(f'Unknown names: {selected-set(BOXES)}')
im=Image.open(ROOT/'packets'/PAGE/'full.jpg')
for key,(box,rotation,width) in BOXES.items():
 if key not in selected:
  continue
 out=ROOT/'edition'/'crops'/f'{PAGE}_{key}.png'
 if out.exists():
  raise RuntimeError(f'Refusing to overwrite {out}')
 c=ImageOps.autocontrast(im.crop(box).convert('RGB'))
 if rotation:
  c=c.rotate(rotation,Image.Resampling.BICUBIC,expand=True,fillcolor='white')
 c=c.resize((width,round(c.height*width/c.width)),Image.Resampling.LANCZOS)
 c=c.filter(ImageFilter.UnsharpMask(radius=1.2,percent=110,threshold=3))
 c.save(out)
(ROOT/'edition'/'review'/f'{PAGE}_crop_boxes.json').write_text(json.dumps(BOXES,indent=2)+'\n')
print(f'Saved {len(selected)} crops for {PAGE}.')
