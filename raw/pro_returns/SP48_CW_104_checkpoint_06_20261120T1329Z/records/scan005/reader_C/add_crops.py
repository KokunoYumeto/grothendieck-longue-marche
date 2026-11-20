from PIL import Image, ImageOps
from pathlib import Path
import json
root=Path('/workspace/scratch/7178efd1cfac/SP48_CW_104/records/scan005/reader_C')
src=Path('/workspace/scratch/7178efd1cfac/source/SP48_CW_104_scans/H104-01_104_scan005.jpg')
im=Image.open(src)
manifest=json.loads((root/'crop_manifest.json').read_text())
items=[('19_background',[195,180,350,510],90,2600),('20_cp_opening',[250,1465,885,1625],0,3000)]
for name,box,rot,width in items:
 c=ImageOps.autocontrast(im.crop(box),cutoff=0)
 if rot: c=c.rotate(rot,expand=True)
 c=c.resize((width,round(c.height*width/c.width)),Image.Resampling.LANCZOS)
 out=root/'crops'/f'{name}.png'
 c.save(out)
 manifest.append({'path':str(out),'source':str(src),'bbox':box,'rotation_degrees':rot,'autocontrast':'Pillow ImageOps.autocontrast cutoff=0','resize':'LANCZOS','output_dimensions':list(c.size),'sharpening':'none','viewed':False})
(root/'crop_manifest.json').write_text(json.dumps(manifest,indent=2))
