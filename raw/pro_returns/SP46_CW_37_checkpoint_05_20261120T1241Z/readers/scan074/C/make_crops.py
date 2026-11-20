from PIL import Image, ImageOps, ImageFilter
from pathlib import Path
import json
base=Path('/workspace/scratch/006c0e32b2af/out/readers/scan074/C')
source=Path('/workspace/scratch/006c0e32b2af/source/SP46_CW_37_scans/B37-04_37_scan074.jpg')
im=Image.open(source)
records=[]
for name,bbox,reason in [
 ('074C_01_clipped_disol.jpg',(1066,304,1200,351),'Remaining clipped glyph after diso at the right edge'),
 ('074C_02_preferable_overtypes.jpg',(408,382,625,430),'Two adjacent overlapping typewriter positions in préférable'),
 ('074C_03_bottom_curve.jpg',(1093,1489,1179,1559),'Material status and exact shape of the isolated lower-right curve')
]:
    c=im.crop(bbox)
    c=ImageOps.autocontrast(c,cutoff=0)
    c=c.resize((2600,round(c.height*2600/c.width)),Image.Resampling.LANCZOS)
    c=c.filter(ImageFilter.UnsharpMask(radius=1.3,percent=110,threshold=3))
    out=base/name
    c.save(out,quality=95)
    records.append({'file':str(out),'bbox':list(bbox),'rotation':0,'reason':reason,'processing':'RGB autocontrast with cutoff 0; LANCZOS resize to 2600 px wide; UnsharpMask radius 1.3, percent 110, threshold 3; JPEG quality 95'})
(base/'crop_manifest.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(records,ensure_ascii=False,indent=2))
