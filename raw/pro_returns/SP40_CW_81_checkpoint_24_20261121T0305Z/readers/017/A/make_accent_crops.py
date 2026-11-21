from pathlib import Path
from PIL import Image, ImageOps
import json
root=Path('/workspace/scratch/94548b74fbe0')
out=root/'out/readers/017/A'
specs=[
 ('17_considerons',(310,1135,742,1245),'Previously uncropped Considérons: local acute-accent strokes'),
 ('18_definies',(530,1500,1010,1627),'Previously uncropped plural définies: local acute and ending'),
 ('19_last_definie',(1090,1743,1460,1843),'Previously uncropped final définie: local acute and word ending')
]
manifest=json.loads((out/'crop_manifest.json').read_text())
with Image.open(root/'source/SP40_CW_81_scans/J81-02_81_scan017.jpg') as src:
 for name,box,purpose in specs:
  im=ImageOps.autocontrast(src.crop(box).convert('RGB'))
  pre=im.size
  target=(2600,round(im.height*2600/im.width))
  im=im.resize(target,Image.Resampling.LANCZOS)
  path=name+'.png'; im.save(out/path)
  manifest.append({'path':path,'bbox':list(box),'rotation':0,'purpose':purpose,'source':'full scan, upper-left origin','pre_enlargement_size':list(pre),'output_size':list(target),'processing':'RGB autocontrast; width 2600 with proportional rounded height; LANCZOS enlargement; no sharpening'})
(out/'crop_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print('Created three previously uncropped accent loci; no decided locus reopened or recropped.')
