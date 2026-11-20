from PIL import Image, ImageOps
from pathlib import Path
r=Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
im=ImageOps.autocontrast(Image.open(r/'packets/145_scan005/page.jpg').crop([48,22,776,123]))
im=im.resize((2400,round(im.height*2400/im.width)),Image.Resampling.LANCZOS)
im.save(r/'edition/crops/145_scan005_15_header.png')
