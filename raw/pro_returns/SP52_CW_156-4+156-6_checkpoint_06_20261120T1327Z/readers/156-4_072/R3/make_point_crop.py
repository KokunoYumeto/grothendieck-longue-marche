from pathlib import Path
from PIL import Image,ImageOps,ImageFilter
import json
out=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_072/R3')
source='/workspace/scratch/6644f30583f9/source/SP52_CW_156-4+156-6_scans/J156-4-09_156-4_scan072.jpg'
bbox=[470,1635,735,1765]
im=ImageOps.autocontrast(Image.open(source).crop(bbox),cutoff=0.4)
scale=2400/im.width
im=im.resize((2400,round(im.height*scale)),Image.Resampling.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1.2,percent=115,threshold=3))
p=out/'crops'/'18_detached_point.jpg'
im.save(p,quality=94)
metadata=json.loads((out/'crop_metadata.json').read_text())
metadata.append(dict(path=str(p),source=source,bbox=bbox,scale=scale,rotation=0,reason='Still-open detached point or pair left of first C6 diagram, identified in the original lower-half reading.',transforms=['autocontrast cutoff 0.4%','no rotation','PIL LANCZOS resize to 2400 px across','UnsharpMask radius 1.2 percent 115 threshold 3','JPEG quality 94']))
(out/'crop_metadata.json').write_text(json.dumps(metadata,ensure_ascii=False,indent=2)+'\n')
print('Created only new crop 18')
