from pathlib import Path
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
import argparse, json

p=argparse.ArgumentParser()
p.add_argument('scan',type=int)
p.add_argument('place')
p.add_argument('box',nargs=4,type=int)
p.add_argument('--rotate',type=float,default=0)
p.add_argument('--width',type=int,default=2800)
p.add_argument('--sharpen',action='store_true')
a=p.parse_args()
root=Path(__file__).resolve().parents[2]
out=root/'SP72_C13_142_work'
dest=out/'crops'/f'scan{a.scan:03}_{a.place}.jpg'
if dest.exists():
    raise SystemExit('Crop already exists: reuse it; do not recrop a decided place.')
im=Image.open(root/'source/SP72_C13_142_scans'/f'142_scan{a.scan:03}.jpg')
im=ImageOps.autocontrast(im.crop(tuple(a.box)))
if a.rotate:
    im=im.rotate(a.rotate,expand=True,resample=Image.Resampling.BICUBIC,fillcolor='white')
im=im.resize((a.width,round(im.height*a.width/im.width)),Image.Resampling.LANCZOS)
if a.sharpen:
    im=im.filter(ImageFilter.UnsharpMask(radius=1.2,percent=120,threshold=3))
im.save(dest,quality=91,subsampling=0)
with (out/'crops/crop_manifest.jsonl').open('a') as f:
    f.write(json.dumps({'scan':a.scan,'place':a.place,'file':str(dest.relative_to(out)),'box':a.box,'rotation':a.rotate,'width':a.width,'sharpen':a.sharpen})+'\n')
print(dest)
