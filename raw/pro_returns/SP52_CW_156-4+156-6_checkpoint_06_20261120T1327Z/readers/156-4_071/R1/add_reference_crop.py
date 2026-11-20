from PIL import Image,ImageOps,ImageEnhance
from pathlib import Path
import json
out=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_071/R1')
src=Path('/workspace/scratch/6644f30583f9/source/SP52_CW_156-4+156-6_scans/J156-4-09_156-4_scan071.jpg')
bbox=(255,1340,825,1555)
im=ImageOps.autocontrast(Image.open(src).crop(bbox))
scale=2500/im.width
im=im.resize((2500,round(im.height*scale)),Image.Resampling.LANCZOS)
im=ImageEnhance.Sharpness(im).enhance(1.25)
p=out/'crops/13_page_reference.jpg'
im.save(p,quality=94)
records=json.loads((out/'crop_manifest.json').read_text())
records.append({'path':str(p),'source':str(src),'bbox':list(bbox),'scale':scale,'rotation':0,'reason':'C page versus H p. in the reference; the preceding crops did not include this target','transforms':['autocontrast','LANCZOS resize to 2500 px width','sharpness factor 1.25','JPEG quality 94']})
(out/'crop_manifest.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
