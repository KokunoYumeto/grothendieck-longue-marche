"""One rotated narrow crop along a long mark, using supplied observed endpoints.
No recognition or image reading is performed by this script.
"""
from pathlib import Path
from PIL import Image,ImageOps
from datetime import datetime,timezone
import argparse,math,json
p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('dest');p.add_argument('endpoints',nargs=4,type=float);p.add_argument('--band',type=int,default=180);p.add_argument('--margin',type=int,default=20);p.add_argument('--width',type=int,default=3000);p.add_argument('--reason',required=True);a=p.parse_args()
dst=Path(a.dest)
if dst.exists():raise RuntimeError('Never overwrite/re-crop a decided place')
x1,y1,x2,y2=a.endpoints;length=math.hypot(x2-x1,y2-y1);tx=(x2-x1)/length;ty=(y2-y1)/length
w=math.ceil(length)+2*a.margin;h=a.band
affine=(tx,-ty,x1-a.margin*tx+a.band/2*ty,ty,tx,y1-a.margin*ty-a.band/2*tx)
im=Image.open(a.source).transform((w,h),Image.Transform.AFFINE,affine,Image.Resampling.BICUBIC)
im=ImageOps.autocontrast(im).resize((a.width,round(h*a.width/w)),Image.Resampling.LANCZOS)
dst.parent.mkdir(parents=True,exist_ok=True);im.save(dst)
record={'source_image':a.source,'path':str(dst),'endpoints':a.endpoints,'band':a.band,'margin':a.margin,'rotation_degrees':math.degrees(math.atan2(y2-y1,x2-x1)),'affine_output_to_source':affine,'width':a.width,'method':'one narrow affine crop along a single long mark; autocontrast and LANCZOS; no recrop','reason':a.reason,'UTC':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}
dst.with_suffix('.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record))
