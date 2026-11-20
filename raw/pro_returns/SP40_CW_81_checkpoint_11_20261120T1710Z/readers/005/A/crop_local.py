from pathlib import Path
from PIL import Image,ImageOps,ImageEnhance
import json
root=Path('/workspace/scratch/94548b74fbe0/out/readers/005/A')
source=Image.open('/workspace/scratch/94548b74fbe0/source/SP40_CW_81_scans/J81-01_81_scan005.jpg')
specs=[
 ('01_automorphisme',(560,52,1150,180),'C doubt in first-line automorphisme; include un and complete ascenders'),
 ('02_egalmt',(925,252,1203,370),'C doubt in contracted word after est on line 3'),
 ('03_autc_opere',(645,360,1045,466),'Bar/doubling of C and C accent doubt in first opere'),
 ('04_speciaux',(475,462,768,578),'C accent doubt at plural spèciaux; include preceding f'),
 ('05_autq',(132,678,430,795),'C doubt in ordinary/double-stroked barred Q; whole Aut and parentheses'),
 ('06_revient',(675,903,1200,1020),'C doubt revient and adjoining au = de'),
 ('07_lower_left_mark',(145,1237,473,1455),'C doubt dash/equals below unfinished line, with preceding de f est'),
 ('08_coeff',(285,762,448,915),'Small detached stroke at lower end of coeff. and final abbreviation point'),
 ('09_special_quotient',(970,683,1176,802),'Compressed spécial after f=P/Q, accent and comma')
]
records=[]
for name,bbox,purpose in specs:
 im=ImageOps.autocontrast(source.crop(bbox))
 factor=2400/im.width
 im=im.resize((2400,round(im.height*factor)),Image.Resampling.LANCZOS)
 p=root/'crops'/f'{name}.png'
 im.save(p)
 records.append({'path':str(p.relative_to(root)),'bbox':{'coordinate_system':'original full scan','xyxy':list(bbox)},'rotation':0,'purpose':purpose})
(root/'crop_manifest.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(records,ensure_ascii=False))
