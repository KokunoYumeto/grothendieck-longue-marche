from pathlib import Path
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
source=Path('/workspace/scratch/17347c1714f0/source/SP36_CW_71_scans/J71-01_71_scan004_b.jpg')
box=(900, 735, 1440, 925)
im=Image.open(source).crop(box)
im=ImageOps.autocontrast(im)
im=im.resize((2800,round(im.height*2800/im.width)), Image.Resampling.LANCZOS)
im.save('/workspace/scratch/17347c1714f0/out/readers/scan004/R1/autograph.png')
print('source',source,'box',box,'rotation',0,'width',2800,'scale',2800/540)
