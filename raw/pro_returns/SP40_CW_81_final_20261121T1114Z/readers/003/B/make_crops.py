from PIL import Image, ImageOps, ImageFilter
from pathlib import Path
import json
root=Path('/workspace/scratch/94548b74fbe0')
out=root/'out/readers/003/B'
im=Image.open(root/'source/SP40_CW_81_scans/J81-01_81_scan003.jpg')
items=[
 ('01_title_insertion.png',(560,10,790,115),0,'Inserted orientée'),
 ('02_title_ending.png',(1290,75,1650,225),0,'isotopique or isotopiques'),
 ('03_morphism.png',(180,170,1030,280),0,'morphisme ending, arrow, field letters, spécial'),
 ('04_f0_overwrite.png',(1230,405,1415,527),0,'overwritten predecessor at f(0)=0'),
 ('05_cancelled_set.png',(515,555,930,660),0,'cancelled membership and set after on ait'),
 ('06_respt.png',(1035,910,1360,1020),0,'resp abbreviation and raised termination'),
 ('07_oblique_note.png',(20,935,435,1390),-40,'oblique normalization note and normalisés'),
 ('08_fraction_cancel.png',(185,1225,435,1355),0,'cancelled factor Q(z)'),
 ('09_NB_cancel.png',(345,1620,650,1720),0,'cancelled word after P(z)=Q(z)'),
 ('10_question.png',(205,1870,1260,2035),0,'parenthesis, inserted avec phrase and closing guide'),
 ('11_cancelled_start.png',(205,2038,665,2122),0,'cancelled line before Prenons'),
 ('12_QT_condns.png',(625,2080,1275,2170),0,'Q(T)=1 and cond abbreviation'),
 ('13_TP0.png',(1060,2160,1380,2255),0,'P(T)=TP0(T), overwritten symbols'),
 ('14_margin_line1.png',(19,1600,95,2445),-90,'sideways first line and supposons insertion'),
 ('15_margin_line2.png',(80,1495,170,2445),-90,'sideways second line: sera, zero set, cancelled unreadable word'),
 ('16_margin_line3.png',(152,1580,250,2445),-90,'sideways third line: evaluation, cancellations, ending'),
]
records=[]
for name,bbox,rot,purpose in items:
 crop=im.crop(bbox)
 if rot: crop=crop.rotate(rot,expand=True,resample=Image.Resampling.BICUBIC,fillcolor='white')
 crop=ImageOps.autocontrast(crop)
 w=3000 if name in ['03_morphism.png','10_question.png','14_margin_line1.png','15_margin_line2.png','16_margin_line3.png'] else 2600
 crop=crop.resize((w,round(crop.height*w/crop.width)),Image.Resampling.LANCZOS)
 crop=crop.filter(ImageFilter.UnsharpMask(radius=1.1,percent=120,threshold=3))
 crop.save(out/name)
 records.append({'path':name,'bbox':list(bbox),'rotation':rot,'purpose':purpose})
(out/'crop_manifest.json').write_text(json.dumps(records,indent=2))
print(json.dumps(records,indent=2))
