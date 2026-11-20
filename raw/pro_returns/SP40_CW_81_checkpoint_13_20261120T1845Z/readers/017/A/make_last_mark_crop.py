from pathlib import Path
from PIL import Image,ImageOps
import json
out=Path('/workspace/scratch/94548b74fbe0/out/readers/017/A')
box=(1340,1688,1625,1840)
with Image.open('/workspace/scratch/94548b74fbe0/source/SP40_CW_81_scans/J81-02_81_scan017.jpg') as src:
 im=ImageOps.autocontrast(src.crop(box).convert('RGB'))
 pre=im.size;size=(2600,round(im.height*2600/im.width))
 im.resize(size,Image.Resampling.LANCZOS).save(out/'20_right_detached_marks.png')
manifest=json.loads((out/'crop_manifest.json').read_text())
manifest.append({'path':'20_right_detached_marks.png','bbox':list(box),'rotation':0,'purpose':'Previously uncropped separated dark marks far right between partition display and final prose; adjacent par is context only','source':'full scan, upper-left origin','pre_enlargement_size':list(pre),'output_size':list(size),'processing':'RGB autocontrast; width 2600 with proportional rounded height; LANCZOS enlargement; no sharpening'})
(out/'crop_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print('Created one final previously uncropped detached-mark locus.')
