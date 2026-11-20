"""Make one evidence crop from a user-supplied scan; no text recognition."""
from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import argparse,json
p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('destination')
p.add_argument('box',nargs=4,type=int);p.add_argument('--width',type=int,default=2400)
p.add_argument('--rotate',type=float,default=0);p.add_argument('--sharpen',action='store_true')
p.add_argument('--grayscale',action='store_true',help='Use luminance for a faint graphite target when colour is not evidence')
a=p.parse_args();im=Image.open(a.source).crop(tuple(a.box))
if a.grayscale:im=im.convert('L')
im=ImageOps.autocontrast(im)
if a.rotate:im=im.rotate(a.rotate,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
im=im.resize((a.width,round(im.height*a.width/im.width)),Image.Resampling.LANCZOS)
if a.sharpen:im=im.filter(ImageFilter.UnsharpMask(radius=1.2,percent=120,threshold=3))
dest=Path(a.destination);dest.parent.mkdir(parents=True,exist_ok=True)
if dest.suffix.lower() in ['.jpg','.jpeg']:
 im.save(dest,quality=95,subsampling=0)
else:
 im.save(dest)
dest.with_suffix('.json').write_text(json.dumps(vars(a),indent=2)+'\n')
print(str(dest))
