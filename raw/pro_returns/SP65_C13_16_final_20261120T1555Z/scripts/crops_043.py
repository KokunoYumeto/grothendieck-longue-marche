from PIL import Image,ImageOps
from pathlib import Path
im=Image.open('source/SP65_C13_16_scans/16_scan043.jpg')
boxes={'above':(1155,165,1445,235),'cancel_son':(345,240,460,300),'cancel_donc':(620,245,735,300),'old_morphism':(975,230,1495,320),'ref':(690,1020,920,1090),'omega':(485,1085,995,1165),'margin':(25,1115,245,1540),'suite':(220,1370,420,1470),'et_un':(975,1405,1375,1465),'a_u':(900,1590,1140,1675),'injectif':(290,1750,610,1820),'typo':(1030,1750,1240,1810),'immersion':(1040,1820,1520,1890)}
for name,box in boxes.items():
 p=Path('views')/f'043_{name}.png';assert not p.exists()
 c=ImageOps.autocontrast(im.crop(box));c=c.rotate(-40,expand=True) if name=='margin' else c
 w=2400 if c.width>500 else 1400;c.resize((w,round(c.height*w/c.width)),Image.Resampling.LANCZOS).save(p)
print(boxes)
