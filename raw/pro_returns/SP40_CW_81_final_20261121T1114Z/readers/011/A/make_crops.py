from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json
root=Path(__file__).parent
source=Path('/workspace/scratch/94548b74fbe0/source/SP40_CW_81_scans/J81-02_81_scan011.jpg')
with Image.open(source) as original:
    for c in json.loads((root/'crop_manifest.json').read_text()):
        im=original.crop(tuple(c['bbox']))
        im=ImageOps.autocontrast(im)
        width=2600
        im=im.resize((width,round(im.height*width/im.width)),Image.Resampling.LANCZOS)
        im=im.filter(ImageFilter.UnsharpMask(radius=1.1,percent=120,threshold=3))
        im.save(root/c['path'])
        print(c['path'],c['bbox'],im.size)
