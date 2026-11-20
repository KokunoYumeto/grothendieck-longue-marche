from PIL import Image, ImageOps, ImageFilter
from pathlib import Path
import json
p=Path(__file__).parent
src=Path('/workspace/scratch/94548b74fbe0/source/SP40_CW_81_scans/J81-02_81_scan011.jpg')
manifest=[]
with Image.open(src) as original:
 for name,bbox,purpose in json.loads((p/'crop_plan.json').read_text()):
  im=ImageOps.autocontrast(original.crop(tuple(bbox)))
  width=2600
  im=im.resize((width,round(im.height*width/im.width)),Image.Resampling.LANCZOS)
  im=im.filter(ImageFilter.UnsharpMask(radius=1.1,percent=120,threshold=3))
  im.save(p/name)
  manifest.append(dict(path=name,bbox=bbox,rotation=0,purpose=purpose))
(p/'crop_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(len(manifest),'crops written')
