#!/usr/bin/env python3
"""Create a single evidence crop; no OCR or image synthesis is performed."""
import argparse, json
from pathlib import Path
from datetime import datetime, timezone
from PIL import Image
p=argparse.ArgumentParser()
p.add_argument('source');p.add_argument('output');p.add_argument('box',nargs=4,type=int)
p.add_argument('--scale',type=float,default=2.5);p.add_argument('--rotate',type=float,default=0)
p.add_argument('--place',required=True)
a=p.parse_args();out=Path(a.output);out.parent.mkdir(parents=True,exist_ok=True)
if out.exists():raise SystemExit('Refusing to overwrite an evidence crop')
im=Image.open(a.source);crop=im.crop(tuple(a.box))
if a.rotate:crop=crop.rotate(a.rotate,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
crop=crop.resize((round(crop.width*a.scale),round(crop.height*a.scale)),Image.Resampling.LANCZOS)
crop.save(out)
record={'source':Path(a.source).name,'box':a.box,'scale':a.scale,'rotation_degrees':a.rotate,'place':a.place,'output':out.name,'created_utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}
out.with_suffix('.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(record,ensure_ascii=False))
