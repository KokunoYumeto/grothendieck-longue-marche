"""Make one documented inspection crop; no OCR or recognition is used."""
from pathlib import Path
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
from datetime import datetime, timezone
import argparse,json
p=argparse.ArgumentParser()
p.add_argument('source');p.add_argument('dest');p.add_argument('box',nargs=4,type=int)
p.add_argument('--width',type=int,default=2600);p.add_argument('--rotate',type=float,default=0)
p.add_argument('--sharpen',action='store_true');p.add_argument('--reason',default='Adjudication of reader/witness disagreement')
a=p.parse_args();src=Path(a.source);dst=Path(a.dest)
if dst.exists():raise RuntimeError('Do not overwrite/re-crop a decided place')
im=Image.open(src).crop(a.box)
if a.rotate:im=im.rotate(a.rotate,Image.Resampling.BICUBIC,expand=True,fillcolor='white')
im=ImageOps.autocontrast(im)
im=im.resize((a.width,round(im.height*a.width/im.width)),Image.Resampling.LANCZOS)
if a.sharpen:im=im.filter(ImageFilter.UnsharpMask(radius=1.2,percent=120,threshold=3))
dst.parent.mkdir(parents=True,exist_ok=True);im.save(dst)
record={'path':str(dst),'source_image':str(src),'bbox':a.box,'rotation':a.rotate,'width':a.width,'sharpen':a.sharpen,'reason':a.reason,'UTC':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}
dst.with_suffix('.json').write_text(json.dumps(record,ensure_ascii=False,indent=2))
print(json.dumps(record))
