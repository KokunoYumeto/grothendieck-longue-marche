from PIL import Image,ImageOps
from pathlib import Path
im=Image.open('source/SP65_C13_16_scans/16_scan041.jpg')
for name,box in {'n0first':(515,540,655,615),'n0second':(1270,480,1430,555),'edge':(10,750,60,815)}.items():
 p=Path('views')/f'041_{name}.png';assert not p.exists()
 c=ImageOps.autocontrast(im.crop(box).rotate(180,expand=True));w=1200;c.resize((w,round(c.height*w/c.width)),Image.Resampling.LANCZOS).save(p)
