"""One new evidentiary crop for a previously uncropped locus. No OCR."""
from PIL import Image,ImageOps,ImageFilter
from pathlib import Path
from datetime import datetime,timezone
import argparse,json
p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('destination');p.add_argument('box',nargs=4,type=int);p.add_argument('--rotation',type=float,default=0);p.add_argument('--width',type=int,default=2800)
a=p.parse_args();dest=Path(a.destination)
if dest.exists():raise SystemExit('Refusing to overwrite or recrop an existing evidence image.')
im=Image.open(a.source).crop(tuple(a.box))
if a.rotation:im=im.rotate(a.rotation,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
im=ImageOps.autocontrast(im).filter(ImageFilter.UnsharpMask(radius=1.2,percent=120,threshold=3))
im=im.resize((a.width,round(im.height*a.width/im.width)),Image.Resampling.LANCZOS)
dest.parent.mkdir(parents=True,exist_ok=True);im.save(dest,quality=95)
dest.with_suffix('.json').write_text(json.dumps({'source':str(Path(a.source).resolve()),'box':a.box,'rotation':a.rotation,'width':a.width,'transform':'crop; optional upright rotation; autocontrast; unsharp mask; LANCZOS','created_utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')},indent=2)+'\n')
print(str(dest))
