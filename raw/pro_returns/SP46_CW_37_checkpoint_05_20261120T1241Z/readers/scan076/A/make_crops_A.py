from PIL import Image, ImageOps, ImageEnhance, ImageFilter
from pathlib import Path
import json
base=Path('/workspace/scratch/006c0e32b2af/out/readers/scan076/A')
source='/workspace/scratch/006c0e32b2af/source/SP46_CW_37_scans/H37-01_37_scan076.jpg'
plan=[
('A076_01_transition.jpg',[477,367,711,445],0,'First transition symbol: eta, Latin n or gamma; retain neighboring soit and un.'),
('A076_02_source_index.jpg',[932,365,1051,447],0,'Corrected or retraced source U-prime suffix, j versus i.'),
('A076_03_target_index.jpg',[1201,365,1312,440],0,'Corrected or retraced target U-prime suffix, i versus j.'),
('A076_04_tels.jpg',[930,449,1050,511],0,'Possible deleted d beneath initial t of tels.'),
('A076_05_donne.jpg',[1372,448,1485,510],0,'Final letters of donne/donnee, including accent.'),
('A076_06_remark_heading.jpg',[305,955,418,1023],0,'First underlined remark heading and final 1 or s.'),
('A076_07_itou.jpg',[417,954,512,1015],0,'First word of remark, C doubtful itou.'),
('A076_08_cancelled_heading.jpg',[302,1035,419,1100],0,'Full cancelled second remark heading and adjacent punctuation.'),
('A076_09_detached_marks.jpg',[1380,1357,1430,1408],0,'Detached diagonal dark marks below and right of signature; shape and status.'),
]
im=Image.open(source)
manifest=[]
for fn,bbox,rot,reason in plan:
 crop=im.crop(bbox)
 if rot: crop=crop.rotate(rot,Image.Resampling.BICUBIC,expand=True,fillcolor='white')
 crop=ImageOps.autocontrast(crop,cutoff=0.15)
 crop=crop.resize((2400,round(crop.height*2400/crop.width)),Image.Resampling.LANCZOS)
 crop=crop.filter(ImageFilter.UnsharpMask(radius=1.2,percent=115,threshold=3))
 crop.save(base/fn,quality=95)
 manifest.append({'file':str(base/fn),'bbox':bbox,'rotation':rot,'reason':reason,'source':source,'processing':'PIL autocontrast cutoff 0.15; LANCZOS width 2400; UnsharpMask radius 1.2, percent 115, threshold 3; JPEG quality 95','requested_deliveries':0,'actual_visual_views':0})
(base/'crop_manifest_A076.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('Created',len(manifest),'unique crops.')
