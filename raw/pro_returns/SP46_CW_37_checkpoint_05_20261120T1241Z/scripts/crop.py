#!/usr/bin/env python3
"""Make a single reading crop (no recognition). Bbox uses original whole scan."""
from pathlib import Path
from PIL import Image,ImageOps,ImageEnhance,ImageFilter
import sys,json
O=Path(__file__).resolve().parents[1];R=O.parent
n=int(sys.argv[1]);key=sys.argv[2];box=list(map(int,sys.argv[3:7]));angle=float(sys.argv[7]) if len(sys.argv)>7 else 0
meta=json.loads((R/'packets'/f'scan{n:03}'/'meta.json').read_text());im=Image.open(meta['images'][0]).crop(box)
im=ImageOps.autocontrast(im)
if angle:im=im.rotate(angle,expand=True,fillcolor='white',resample=Image.Resampling.BICUBIC)
im=im.resize((2600,round(im.height*2600/im.width)),Image.Resampling.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1.2,percent=140,threshold=3))
d=O/'crops'/f'scan{n:03}';d.mkdir(parents=True,exist_ok=True);p=d/(key+'.jpg');assert not p.exists(),'One crop per place: reuse existing crop'
im.save(p,quality=90)
manifest=d/'manifest.json';rows=json.loads(manifest.read_text()) if manifest.exists() else [];rows.append({'file':str(p.relative_to(O)),'bbox':box,'rotation':angle,'processing':'autocontrast; Lanczos width 2600; unsharp mask 1.2/140/3','source':meta['images'][0]});manifest.write_text(json.dumps(rows,indent=2))
print(p)
