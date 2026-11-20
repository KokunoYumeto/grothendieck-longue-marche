"""Make one enhanced reading crop. No OCR; coordinates must come from visual inspection."""
from PIL import Image, ImageOps, ImageFilter
from pathlib import Path
from datetime import datetime, timezone
import argparse,json
p=argparse.ArgumentParser()
p.add_argument('source');p.add_argument('output');p.add_argument('box',nargs=4,type=int)
p.add_argument('--rotate',type=float,default=0);p.add_argument('--width',type=int,default=2400)
p.add_argument('--reason',required=True)
a=p.parse_args()
im=Image.open(a.source).crop(tuple(a.box))
if a.rotate:im=im.rotate(a.rotate,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
im=ImageOps.autocontrast(im)
im=im.resize((a.width,max(1,round(im.height*a.width/im.width))),Image.Resampling.LANCZOS)
im=im.filter(ImageFilter.UnsharpMask(radius=1.2,percent=120,threshold=3))
out=Path(a.output);out.parent.mkdir(parents=True,exist_ok=True)
im.save(out,quality=93,subsampling=0)
with (out.parent/'crops.jsonl').open('a') as f:
    f.write(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'source':a.source,'output':str(out),'box':a.box,'rotate':a.rotate,'width':a.width,'reason':a.reason})+'\n')
print(str(out))
