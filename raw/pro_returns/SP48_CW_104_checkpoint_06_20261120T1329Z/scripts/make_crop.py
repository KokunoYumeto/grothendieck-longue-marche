"""Make one adjudication crop, without recognition or repeated whole-image viewing."""
from pathlib import Path
from PIL import Image,ImageOps,ImageEnhance,ImageFilter
from datetime import datetime,timezone
import argparse,json,csv
p=argparse.ArgumentParser()
p.add_argument('scan',type=int);p.add_argument('name')
p.add_argument('box',nargs=4,type=int);p.add_argument('--rotate',type=float,default=0)
p.add_argument('--width',type=int,default=2600)
a=p.parse_args()
out=Path(__file__).resolve().parents[1]
folder='H104-01' if a.scan<10 else 'H104-02'
src=out.parent/f'source/SP48_CW_104_scans/{folder}_104_scan{a.scan:03d}.jpg'
dest=out/f'crops/scan{a.scan:03d}_{a.name}.png'
if dest.exists():raise RuntimeError('Refusing to recrop an existing place')
im=Image.open(src).crop(tuple(a.box))
if a.rotate: im=im.rotate(a.rotate,expand=True,resample=Image.Resampling.BICUBIC,fillcolor='white')
im=ImageOps.autocontrast(im)
im=im.resize((a.width,round(im.height*a.width/im.width)),Image.Resampling.LANCZOS)
im=im.filter(ImageFilter.UnsharpMask(radius=1.3,percent=120,threshold=3))
im.save(dest)
manifest=out/'crops/main_crop_manifest.jsonl'
with manifest.open('a') as f:f.write(json.dumps({'scan':a.scan,'name':a.name,'source':str(src),'box':a.box,'rotate':a.rotate,'width':a.width,'processing':'autocontrast, LANCZOS, unsharp mask','output':str(dest.relative_to(out)),'created_utc':datetime.now(timezone.utc).isoformat()})+'\n')
print(dest)
