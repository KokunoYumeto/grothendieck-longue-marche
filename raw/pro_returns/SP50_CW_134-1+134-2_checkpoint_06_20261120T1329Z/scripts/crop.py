"""Make one documented enlarged crop. No OCR or recognition is used."""
import argparse,json
from pathlib import Path
from datetime import datetime,timezone
from PIL import Image,ImageOps,ImageEnhance,ImageFilter
p=argparse.ArgumentParser()
p.add_argument('source');p.add_argument('output');p.add_argument('box',nargs=4,type=int)
p.add_argument('--width',type=int,default=2800)
p.add_argument('--rotate',type=float,default=0)
p.add_argument('--contrast',type=float,default=1.12)
p.add_argument('--label',default='')
a=p.parse_args()
src=Path(a.source);dst=Path(a.output);dst.parent.mkdir(parents=True,exist_ok=True)
im=Image.open(src).convert('RGB')
box=tuple(a.box)
assert 0<=box[0]<box[2]<=im.width and 0<=box[1]<box[3]<=im.height,(box,im.size)
im=im.crop(box)
if a.rotate: im=im.rotate(a.rotate,expand=True,resample=Image.Resampling.BICUBIC,fillcolor='white')
im=ImageOps.autocontrast(im)
im=ImageEnhance.Contrast(im).enhance(a.contrast)
im=im.resize((a.width,round(im.height*a.width/im.width)),Image.Resampling.LANCZOS)
im=im.filter(ImageFilter.UnsharpMask(radius=1.2,percent=125,threshold=3))
im.save(dst,quality=93,optimize=True)
record={'source':src.name,'output':dst.name,'box':list(box),'width':a.width,'rotate':a.rotate,'contrast':a.contrast,'label':a.label,'utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}
with (dst.parent/'crops.jsonl').open('a') as f:f.write(json.dumps(record,ensure_ascii=False)+'\n')
print(json.dumps(record,ensure_ascii=False))
