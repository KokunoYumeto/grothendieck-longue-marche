from PIL import Image,ImageOps
from pathlib import Path
r=Path(__file__).resolve().parents[2];im=Image.open(r/'source/SP65_C13_16_scans/16_scan049.jpg')
boxes={'prelim':(270,460,370,515),'delta1':(490,660,835,745),'delta2':(575,960,760,1025),'it':(635,1540,700,1600),'of':(475,1970,540,2025)}
for name,box in boxes.items():
 t=r/f'views/049_{name}.png';assert not t.exists();a=ImageOps.autocontrast(im.crop(box));a.resize((1800,round(a.height*1800/a.width)),Image.Resampling.LANCZOS).save(t)
print(boxes)
