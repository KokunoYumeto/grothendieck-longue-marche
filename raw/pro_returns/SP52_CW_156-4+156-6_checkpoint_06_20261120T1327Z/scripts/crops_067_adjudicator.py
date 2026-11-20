from pathlib import Path
from PIL import Image, ImageOps
import json
O=Path(__file__).resolve().parents[1];D=O/'crops/156-4_067';D.mkdir(parents=True,exist_ok=True)
src=O.parent/'source/SP52_CW_156-4+156-6_scans/J156-4-09_156-4_scan067.jpg'
items=[
 ('a01_upper_def',[1050,805,1290,965],'Top def label extends above every reader definition crop; accent not yet adjudicated.'),
 ('a02_final_stop',[1120,2240,1530,2358],'Right margin after final brace is outside the available reader crop; terminal punctuation not yet adjudicated.'),
 ('a03_live_premise',[285,580,1120,710],'Live Donc pour family letter is cut by the top edge of available reader crop; inspect complete letter and line.')
]
manifest=[]
for name,bbox,reason in items:
 dest=D/(name+'.jpg')
 if dest.exists():raise SystemExit('Do not recreate an existing crop: '+str(dest))
 im=ImageOps.autocontrast(Image.open(src).crop(bbox));scale=2400/im.width
 im=im.resize((2400,round(im.height*scale)),Image.Resampling.LANCZOS);im.save(dest,quality=94)
 manifest.append(dict(path=str(dest),source=str(src),bbox=bbox,scale=scale,rotation=0,reason=reason,transformations='autocontrast; LANCZOS to 2400 px across; JPEG 94'))
(D/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(len(manifest))
