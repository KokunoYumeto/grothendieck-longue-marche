from PIL import Image,ImageOps,ImageEnhance
from pathlib import Path
import json
out=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_072/R1')
src=Path('/workspace/scratch/6644f30583f9/source/SP52_CW_156-4+156-6_scans/J156-4-09_156-4_scan072.jpg')
bbox=[1120,1110,1675,1315]
with Image.open(src) as im:
 c=ImageOps.autocontrast(im.crop(bbox),cutoff=0)
 scale=2500/c.width
 c=c.resize((2500,round(c.height*scale)),Image.Resampling.LANCZOS)
 c=ImageEnhance.Sharpness(c).enhance(1.15)
 p=out/'crops/17_envisagees_stop.jpg'
 c.save(p,quality=94,subsampling=0)
 rec=dict(path=str(p),source=str(src),bbox=bbox,scale=scale,rotation=0,reason='Previously open right-edge punctuation after envisagées, outside crop 09; includes preceding line.',autocontrast_cutoff=0,sharpen_factor=1.15,size=list(c.size))
rs=json.loads((out/'crop_metadata.json').read_text())
assert len(rs)==16
rs.append(rec)
(out/'crop_metadata.json').write_text(json.dumps(rs,ensure_ascii=False,indent=2)+'\n')
print('Created the one crop for previously unresolved right-edge punctuation; no earlier crop changed.')
