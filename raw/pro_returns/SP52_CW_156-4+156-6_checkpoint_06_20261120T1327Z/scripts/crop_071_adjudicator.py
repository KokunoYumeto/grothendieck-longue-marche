from pathlib import Path
from PIL import Image,ImageOps,ImageEnhance
import json
O=Path(__file__).resolve().parents[1]
s=O.parent/'source/SP52_CW_156-4+156-6_scans/J156-4-09_156-4_scan071.jpg'
out=O/'crops/156-4_071';out.mkdir(parents=True,exist_ok=True)
items=[('a01_ce_qu_on_appelle.jpg',[260,875,1340,1020],'H two illegible placeholders: full ce qu’on appelle, whose upper/extreme lettering was clipped in existing reader crops'),('a02_cancelled_toute.jpg',[250,1070,1665,1260],'Deletion state of toute before partie, outside previous root-viewed crops')]
manifest=[]
for name,box,reason in items:
 p=out/name
 if p.exists():raise SystemExit('Crop already exists; do not recrop.')
 im=Image.open(s).crop(box);im=ImageOps.autocontrast(im);sc=2500/im.width;im=im.resize((2500,round(im.height*sc)),Image.Resampling.LANCZOS);im=ImageEnhance.Sharpness(im).enhance(1.2);im.save(p,quality=94)
 manifest.append(dict(path=str(p.relative_to(O)),source=str(s),bbox=box,rotation=0,scale=sc,transforms=['autocontrast','LANCZOS to 2500 pixels','sharpness 1.2'],reason=reason))
(out/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
