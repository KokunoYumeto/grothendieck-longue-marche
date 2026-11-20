from pathlib import Path
import json
from PIL import Image, ImageOps, ImageFilter

ROOT=Path('/workspace/scratch/94548b74fbe0')
DEST=ROOT/'out/readers/020/A'
box=(925,760,1310,875)
im=Image.open(ROOT/'source/SP40_CW_81_scans/J81-03_81_scan020.jpg').convert('RGB').crop(box)
im=im.resize((3200,round(im.height*3200/im.width)),Image.Resampling.LANCZOS)
im=ImageOps.autocontrast(im).filter(ImageFilter.UnsharpMask(radius=1.2,percent=120,threshold=3))
name='15_voisinage_detached_point.png'
im.save(DEST/name)
manifest=json.loads((DEST/'crop_manifest.json').read_text())
manifest.append({'path':name,'bbox':list(box),'coordinate_origin':'original full scan, upper left','rotation':0,'purpose':'New point noticed at lower-left boundary context of crop06; complete voisinage descender and following de to inspect attachment; the E-index decision is outside this crop.','processing':'PIL crop; LANCZOS to 3200 pixels wide; autocontrast; UnsharpMask(radius=1.2, percent=120, threshold=3)'})
(DEST/'crop_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print('Created one new complete attachment target; no prior image re-opened.')
