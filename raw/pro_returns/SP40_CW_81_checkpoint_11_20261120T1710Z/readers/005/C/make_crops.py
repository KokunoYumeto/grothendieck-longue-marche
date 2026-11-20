from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json
out=Path(__file__).parent
source=Path('/workspace/scratch/94548b74fbe0/source/SP40_CW_81_scans/J81-01_81_scan005.jpg')
im=Image.open(source)
for r in json.loads((out/'crop_manifest.json').read_text()):
    crop=ImageOps.autocontrast(im.crop(tuple(r['bbox'])))
    crop=crop.resize((2600,round(crop.height*2600/crop.width)),Image.Resampling.LANCZOS)
    crop=crop.filter(ImageFilter.UnsharpMask(radius=1.1,percent=120,threshold=3))
    crop.save(out/r['path'])
