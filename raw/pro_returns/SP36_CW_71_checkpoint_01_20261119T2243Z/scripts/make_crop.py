"""PIL crop/enhancement only. No text recognition. Log every produced crop."""
from PIL import Image,ImageOps,ImageFilter
from pathlib import Path
import argparse,json,datetime
p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('destination');p.add_argument('--box',nargs=4,type=int,required=True);p.add_argument('--rotate',type=float,default=0);p.add_argument('--width',type=int,default=2800);p.add_argument('--place',required=True);a=p.parse_args()
im=Image.open(a.source).crop(a.box)
if a.rotate:im=im.rotate(a.rotate,expand=True,resample=Image.Resampling.BICUBIC)
im=ImageOps.autocontrast(im)
im=im.resize((a.width,round(im.height*a.width/im.width)),Image.Resampling.LANCZOS)
im=im.filter(ImageFilter.UnsharpMask(radius=1.5,percent=130,threshold=3))
dest=Path(a.destination);dest.parent.mkdir(parents=True,exist_ok=True);im.save(dest)
entry={**vars(a),'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
with (dest.parent/'crop_log.jsonl').open('a') as f:f.write(json.dumps(entry)+'\n')
print(str(dest))
