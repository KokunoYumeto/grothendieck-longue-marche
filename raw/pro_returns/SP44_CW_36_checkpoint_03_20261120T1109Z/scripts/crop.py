from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
from datetime import datetime, timezone
import argparse, json

p=argparse.ArgumentParser()
p.add_argument('--scan',type=int,required=True)
p.add_argument('--reader',required=True)
p.add_argument('--label',required=True)
p.add_argument('--box',type=int,nargs=4,required=True)
p.add_argument('--rotate',type=float,default=0)
p.add_argument('--width',type=int,default=2400)
a=p.parse_args()
root=Path(__file__).resolve().parents[2]
out=root/'SP44_CW_36_work'
src=next((root/'source/SP44_CW_36_scans').glob(f'*scan{a.scan:03d}.jpg'))
dest=out/'crops'/f'scan{a.scan:03d}'/a.reader
dest.mkdir(parents=True,exist_ok=True)
fn=dest/f'{a.label}.jpg'
if fn.exists(): raise SystemExit('Crop already exists: do not re-crop a decided locus')
with Image.open(src) as im:
    x0,y0,x1,y1=a.box
    if not (0<=x0<x1<=im.width and 0<=y0<y1<=im.height): raise ValueError('Out-of-bounds crop')
    c=ImageOps.autocontrast(im.crop(tuple(a.box)).convert('RGB'))
    if a.rotate: c=c.rotate(a.rotate,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
    c=c.resize((a.width,round(c.height*a.width/c.width)),Image.Resampling.LANCZOS)
    c=c.filter(ImageFilter.UnsharpMask(radius=1.0,percent=110,threshold=3))
    c.save(fn,quality=90,optimize=True)
meta={'scan':a.scan,'reader':a.reader,'source':src.name,'crop':str(fn.relative_to(out)),'box':a.box,'rotation':a.rotate,'width':a.width,'operations':'autocontrast; LANCZOS; UnsharpMask(1,110,3); JPEG90','utc':datetime.now(timezone.utc).isoformat()}
(dest/f'{a.label}.json').write_text(json.dumps(meta,indent=2))
print(fn)
