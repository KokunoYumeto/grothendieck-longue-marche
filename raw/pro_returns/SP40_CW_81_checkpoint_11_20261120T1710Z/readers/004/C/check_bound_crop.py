from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json
p=Path('/workspace/scratch/94548b74fbe0/out/readers/004/C')
box=(327,465,609,548)
im=Image.open('/workspace/scratch/94548b74fbe0/source/SP40_CW_81_scans/J81-01_81_scan004.jpg').crop(box)
im=ImageOps.autocontrast(im)
im=im.resize((2800,round(im.height*2800/im.width)),Image.Resampling.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1,percent=110,threshold=3))
im.save(p/'14_left_bound.png')
a=json.loads((p/'crops_manifest.json').read_text())
a.append({'path':'14_left_bound.png','bbox':list(box),'rotation':0,'purpose':'Both comparison signs in the parenthesized left bound'})
(p/'crops_manifest.json').write_text(json.dumps(a,indent=2,ensure_ascii=False)+'\n')
print('Created one tight crop of the left bound.')
