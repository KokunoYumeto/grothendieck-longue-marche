from PIL import Image,ImageOps,ImageFilter
from pathlib import Path
p=Path('source/SP60_CW_71_scans/J71-06_71_scan045.jpg')
im=Image.open(p)
boxes={'supset':(792,336,875,395),'secteur':(645,594,795,667),'et':(179,1053,239,1122),'notinclusion':(1200,1124,1263,1185),'deleted_after_int':(1384,1104,1472,1177),'ext_over':(1031,1223,1099,1287),'cap_minus':(856,1327,935,1411),'relie':(1348,1761,1470,1830),'exponent':(520,1990,594,2064),'existe_insert':(225,2068,362,2127),'existe_foot':(199,2260,321,2327),'puisque':(1280,88,1445,158)}
for n,b in boxes.items():
 c=im.crop(b);c=c.resize((2200,round(c.height*2200/c.width)),Image.Resampling.LANCZOS);c=ImageOps.autocontrast(c).filter(ImageFilter.UnsharpMask(radius=1.1,percent=120,threshold=3));c.save(Path('work_crops')/f'045_{n}.png')
print(im.size,boxes)
