from PIL import Image,ImageOps
from pathlib import Path
b=Path('/workspace/scratch/825ce1dd1d03');p=b/'views/052_mark.png';assert not p.exists()
im=Image.open(b/'source/SP65_C13_16_scans/16_scan052.jpg');box=(835,598,904,660)
c=ImageOps.autocontrast(im.crop(box));c=c.resize((1800,round(c.height*1800/c.width)),Image.Resampling.LANCZOS);c.save(p)
print('scan 052',box)
