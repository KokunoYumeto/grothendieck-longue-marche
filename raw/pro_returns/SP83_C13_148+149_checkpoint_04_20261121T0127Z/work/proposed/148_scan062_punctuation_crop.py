from PIL import Image, ImageOps, ImageFilter
from pathlib import Path
import json
root=Path('/workspace/scratch/f28c4f52d3ec'); page='148_scan062'
im=Image.open(root/'source/SP83_C13_148+149_scans/148_scan062.jpg').convert('RGB')
box=[1090,1707,1340,1815]
region=ImageOps.autocontrast(im.crop(box)); region=region.resize((2000,864),Image.Resampling.LANCZOS).filter(ImageFilter.UnsharpMask(1.2,105,3))
p=root/'result/crops'/f'{page}_tels_que.png'; region.save(p)
f=root/'proposed'/f'{page}_crop_boxes.json'; data=json.loads(f.read_text())
for rec in data: rec['viewed']=True
# This is a new, previously uncropped punctuation question from the half reading.
data.append({'name':'tels_que','path':str(p),'crop':f'crops/{p.name}','box':box,'rotation':0,'viewed':False})
f.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
print(str(p))
