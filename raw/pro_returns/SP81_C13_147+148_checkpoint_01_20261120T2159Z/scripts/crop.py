from pathlib import Path
from PIL import Image,ImageOps,ImageEnhance,ImageFilter
import sys,json
ROOT=Path(__file__).resolve().parents[2]
page,name=sys.argv[1:3]
box=tuple(map(int,sys.argv[3:7]))
angle=float(sys.argv[7]) if len(sys.argv)>7 else 0
out=ROOT/'edition/crops'/f'{page}_{name}.png'
if out.exists():
    raise SystemExit(f'Crop already exists; view it instead: {out}')
im=Image.open(ROOT/'source/SP81_C13_147+148_scans'/f'{page}.jpg')
assert 0 <= box[0] < box[2] <= im.width and 0 <= box[1] < box[3] <= im.height
im=im.crop(box)
if angle: im=im.rotate(angle,expand=True,fillcolor='white')
im=ImageOps.autocontrast(im)
w=2600
im=im.resize((w,round(im.height*w/im.width)),Image.Resampling.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1.2,percent=110,threshold=3))
im.save(out)
with (ROOT/'edition/work'/f'{page}_crops.jsonl').open('a') as f:
 f.write(json.dumps({'file':out.name,'box':box,'rotation':angle,'width':im.width,'height':im.height})+'\n')
print(str(out))
