from PIL import Image, ImageOps, ImageEnhance
from pathlib import Path
src=Path('/workspace/scratch/17347c1714f0/source/SP36_CW_71_scans/J71-01_71_scan004_b.jpg')
out=Path('/workspace/scratch/17347c1714f0/out/readers/scan004/R2/signature.png')
im=ImageOps.autocontrast(Image.open(src).crop((900,735,1440,925)))
im=im.resize((2800,985),Image.Resampling.LANCZOS)
im=ImageEnhance.Sharpness(im).enhance(1.3)
im.save(out)
