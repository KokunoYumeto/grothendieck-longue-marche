"""Create the prescribed blind-reading crops from a neutral box list only.

This does not read any witness, first reading, adjudication or notation file.
Run only once per page after all first readings have been committed.
"""
from pathlib import Path
import argparse, csv
from PIL import Image, ImageOps, ImageFilter

p=argparse.ArgumentParser()
p.add_argument('image',type=Path)
p.add_argument('boxes',type=Path)
p.add_argument('output',type=Path)
a=p.parse_args()
rows=list(csv.DictReader(a.boxes.open(),delimiter='\t'))
a.output.mkdir(parents=True,exist_ok=True)
with Image.open(a.image) as im:
    for r in rows:
        target=a.output/(r['box']+'.png')
        if target.exists():
            raise SystemExit(f'Refusing to replace an existing blind crop: {target}')
        box=tuple(int(r[k]) for k in ('x0','y0','x1','y1'))
        crop=im.crop(box)
        ratio=min(3000/crop.width,4000/crop.height)
        ratio=max(1,ratio)
        crop=crop.resize((round(crop.width*ratio),round(crop.height*ratio)),Image.Resampling.LANCZOS)
        crop=ImageOps.autocontrast(crop).filter(ImageFilter.UnsharpMask(radius=1.2,percent=110,threshold=3))
        crop.save(target)
        print(target)
