from PIL import Image,ImageOps
from pathlib import Path
im=Image.open('source/SP65_C13_16_scans/16_scan044.jpg')
boxes={'ell':(515,945,1095,1010),'propositions':(330,910,515,965),'so':(1225,1440,1320,1505),'degree':(1380,1505,1520,1575),'lower_insertions':(620,1780,1145,1870),'cancel_a':(1585,1945,1660,2010)}
for name,box in boxes.items():
 out=Path('views')/f'044_{name}.png';assert not out.exists()
 c=ImageOps.autocontrast(im.crop(box));w=2400 if c.width>500 else 1400;c.resize((w,round(c.height*w/c.width)),Image.Resampling.LANCZOS).save(out)
print(boxes)
