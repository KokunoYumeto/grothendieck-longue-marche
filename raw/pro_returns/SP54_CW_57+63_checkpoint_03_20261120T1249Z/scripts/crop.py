#!/usr/bin/env python3
"""One documented crop of supplied scan pixels; no recognition or transcription."""
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
from pathlib import Path
from datetime import datetime, timezone
import argparse, json
p=argparse.ArgumentParser()
p.add_argument('source'); p.add_argument('output')
p.add_argument('bbox', nargs=4, type=int)
p.add_argument('--rotate', type=float, default=0)
p.add_argument('--width', type=int, default=3000)
p.add_argument('--purpose', default='unresolved reading')
a=p.parse_args()
dest=Path(a.output); dest.parent.mkdir(parents=True, exist_ok=True)
if dest.exists():raise SystemExit('Refusing to overwrite an existing crop; each place is cropped once.')
im=Image.open(a.source).crop(tuple(a.bbox))
if a.rotate:im=im.rotate(a.rotate, resample=Image.Resampling.BICUBIC, expand=True, fillcolor='white')
im=ImageOps.autocontrast(im)
im=im.resize((a.width, round(im.height*a.width/im.width)), Image.Resampling.LANCZOS)
im=im.filter(ImageFilter.UnsharpMask(radius=1.3, percent=125, threshold=3))
im.save(dest)
record={'source':str(Path(a.source).resolve()), 'file':str(dest.resolve()), 'bbox':a.bbox,'rotation':a.rotate,'output_size':list(im.size),'method':'Pillow crop, rotation if specified, autocontrast, LANCZOS, unsharp mask','purpose':a.purpose,'utc':datetime.now(timezone.utc).isoformat()}
dest.with_suffix('.json').write_text(json.dumps(record,ensure_ascii=False,indent=2))
print(json.dumps(record,ensure_ascii=False))
