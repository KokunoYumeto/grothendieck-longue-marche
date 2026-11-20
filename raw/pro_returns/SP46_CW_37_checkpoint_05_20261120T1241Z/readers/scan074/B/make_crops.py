from PIL import Image, ImageOps, ImageFilter
from pathlib import Path
import json
out=Path('/workspace/scratch/006c0e32b2af/out/readers/scan074/B')
source=Path('/workspace/scratch/006c0e32b2af/source/SP46_CW_37_scans/B37-04_37_scan074.jpg')
im=Image.open(source).convert('RGB')
loci=[
 ('B074_01_clipped_diso.jpg',[1035,306,1208,383],'Clipped character after diso; retain visible fragment without supplied text.'),
 ('B074_02_preferable.jpg',[406,380,634,429],'Two overtyped positions within préférable; distinguish underlying and live letterforms.'),
 ('B074_03_lower_right_curve.jpg',[1088,1482,1196,1562],'Shape and material status of the isolated lower-right curved trace.')
]
records=[]
for name,bbox,reason in loci:
    crop=im.crop(bbox)
    crop=ImageOps.autocontrast(crop,cutoff=0.5)
    w,h=crop.size
    crop=crop.resize((2500,round(h*2500/w)),Image.Resampling.LANCZOS)
    crop=crop.filter(ImageFilter.UnsharpMask(radius=1.3,percent=110,threshold=3))
    crop.save(out/name,quality=95)
    records.append({'file':str(out/name),'bbox':bbox,'rotation':0,'reason':reason,'processing':'RGB autocontrast cutoff 0.5%; LANCZOS width 2500 px; UnsharpMask radius 1.3, percent 110, threshold 3.'})
(out/'crop_manifest.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(records,ensure_ascii=False,indent=2))
