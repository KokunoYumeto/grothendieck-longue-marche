from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json
root=Path('/workspace/scratch/94548b74fbe0')
out=root/'out/readers/008/C'
source=root/'source/SP40_CW_81_scans/J81-01_81_scan008.jpg'
items=[
 ('01_top_cancelled_neq0.png',[1114,198,1389,280],0,'Crowded deleted sign and zero after q-i-1, before >0'),
 ('02_struck_donc_si.png',[94,375,483,455],0,'Entire isolated cancelled line; final p condition'),
 ('03_zeta_forms.png',[548,879,1167,981],0,'First zeta/delta doubt and its raised recurrence on the same line'),
 ('04_cancelled_subscript.png',[449,1044,723,1139],0,'Small cancelled lower-right character under a prime'),
 ('05_lower_alors_and_pale.png',[545,1378,1005,1467],0,'Cancelled alors and adjoining pale p=q, a-prime/gamma addition'),
 ('06_cancelled_p_power.png',[98,1446,551,1540],0,'Cancelled p-like item before q squared and surviving first implication'),
 ('07_lower_cancellations.png',[452,1452,837,1589],0,'Two cancelled ou p=1 endings, pale absurde car q nondivides a, and smudged interline area'),
 ('08_final_cancelled_q.png',[518,1576,733,1699],0,'Final cancelled q and raised q alpha minus one, with adjacent gamma equality'),
 ('09_first_hypothese.png',[226,1324,613,1403],0,'Accent and full word in ruled hypothesis'),
 ('10_final_hypothese.png',[1019,1585,1345,1686],0,'Accent and word in final parenthesis, with closing punctuation')
]
im=Image.open(source)
records=[]
for name,bbox,rotation,purpose in items:
 crop=im.crop(tuple(bbox))
 if rotation:
  crop=crop.rotate(rotation,expand=True,resample=Image.Resampling.BICUBIC,fillcolor='white')
 crop=ImageOps.autocontrast(crop)
 width=2800
 crop=crop.resize((width,round(crop.height*width/crop.width)),Image.Resampling.LANCZOS)
 crop=crop.filter(ImageFilter.UnsharpMask(radius=1.1,percent=120,threshold=3))
 crop.save(out/name)
 records.append(dict(path=name,bbox=bbox,rotation=rotation,purpose=purpose,size=list(crop.size)))
(out/'crop_manifest.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(records,ensure_ascii=False,indent=2))
