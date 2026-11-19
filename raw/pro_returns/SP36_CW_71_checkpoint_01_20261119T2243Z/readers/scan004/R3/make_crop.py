from PIL import Image, ImageOps, ImageFilter
from pathlib import Path
root=Path(__file__).resolve().parent
source=Path("/workspace/scratch/17347c1714f0/source/SP36_CW_71_scans/J71-01_71_scan004_b.jpg")
image=Image.open(source).crop((900,740,1440,925))
image=ImageOps.autocontrast(image)
image=image.resize((2800,round(image.height*2800/image.width)),Image.Resampling.LANCZOS)
image=image.filter(ImageFilter.UnsharpMask(radius=1.0,percent=120,threshold=3))
image.save(root/"signature_crop.png")
