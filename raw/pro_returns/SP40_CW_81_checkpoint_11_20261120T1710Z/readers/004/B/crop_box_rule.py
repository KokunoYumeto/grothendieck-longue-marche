from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json
base=Path('/workspace/scratch/94548b74fbe0/out/readers/004/B')
box=(105,860,1193,958)
im=Image.open('/workspace/scratch/94548b74fbe0/source/SP40_CW_81_scans/J81-01_81_scan004.jpg').crop(box)
im=ImageOps.autocontrast(im,cutoff=.3)
im=im.resize((3000,round(im.height*3000/im.width)),Image.Resampling.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1,percent=110,threshold=3))
im.save(base/'16_box_lower_rules.png')
p=base/'crop_manifest.json'
a=json.loads(p.read_text());a.append({'path':'16_box_lower_rules.png','bbox':list(box),'rotation':0,'purpose':'Two separately drawn lower rules beneath left boxed system'})
p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
