"""Manual reading crops only. Does no OCR or recognition. Coordinates in original whole scan."""
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
from pathlib import Path
import argparse,json,datetime
p=argparse.ArgumentParser()
p.add_argument('source');p.add_argument('target');p.add_argument('box',nargs=4,type=int)
p.add_argument('--rotate',type=float,default=0);p.add_argument('--width',type=int,default=3000)
a=p.parse_args()
im=Image.open(a.source).crop(tuple(a.box))
if a.rotate: im=im.rotate(a.rotate,expand=True,resample=Image.Resampling.BICUBIC,fillcolor='white')
im=ImageOps.autocontrast(im)
im=im.resize((a.width,round(im.height*a.width/im.width)),Image.Resampling.LANCZOS)
im=im.filter(ImageFilter.UnsharpMask(radius=1.0,percent=120,threshold=3))
t=Path(a.target);t.parent.mkdir(parents=True,exist_ok=True);im.save(t)
record={'source':a.source,'target':a.target,'bbox':a.box,'rotation_degrees':a.rotate,'width':a.width,'UTC':datetime.datetime.now(datetime.timezone.utc).isoformat()}
with (t.parent/'crop_manifest.jsonl').open('a') as f:f.write(json.dumps(record)+'\n')
print(json.dumps(record))
