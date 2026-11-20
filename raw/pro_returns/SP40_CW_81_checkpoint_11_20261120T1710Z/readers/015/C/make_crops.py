from PIL import Image, ImageOps, ImageEnhance
from pathlib import Path
import json
root=Path('/workspace/scratch/94548b74fbe0/out/readers/015/C')
im=Image.open('/workspace/scratch/94548b74fbe0/source/SP40_CW_81_scans/J81-02_81_scan015.jpg')
items=[
 ('01_heading.png',(40,18,285,118),0,'Heading word and overwritten initial'),
 ('02_family.png',(1118,114,1355,224),0,'First family and predecessor under E'),
 ('03_fermes.png',(190,169,575,282),0,'Raised insertion fermés/fermées and insertion guide'),
 ('04_upper_margin.png',(14,382,442,1063),-38,'Entire slanted upper margin, its arrow, abbreviations and indexed symbols'),
 ('05_display_a.png',(359,352,1122,446),0,'Display (a), Card, pi index and predecessor under E'),
 ('06_right_NB.png',(1234,319,1676,472),0,'Upper right NB, second exponent and complement glyph'),
 ('07_b_Ej.png',(653,435,1185,533),0,'Display (b) first overwritten E and surrounding text'),
 ('08_b_Ei.png',(1397,515,1667,610),0,'Display (b) final overwritten E and punctuation'),
 ('09_automatiquement.png',(965,606,1682,720),0,'Faint verification wording and automatically'),
 ('10_case.png',(500,994,958,1100),0,'Case heading, crossed letters and relation, underline'),
 ('11_drawing.png',(19,1038,572,1374),0,'Oval, chords, braces, crossed upper label and right superscript'),
 ('12_equivaut.png',(1080,1277,1669,1478),0,'Ce qui, cancelled résulte de, equivaut à and endpoint'),
 ('13_car_si.png',(206,1437,438,1510),0,'Cancelled short wording under oval'),
 ('14_aussi.png',(223,1673,492,1755),0,'Aussi à and endpoint'),
 ('15_symetriquement.png',(211,1845,969,1947),0,'Faint et and symétriquement à endpoint'),
 ('16_vois.png',(409,2008,728,2144),0,'Cancelled vois. ouvert above inclusion'),
 ('17_lower_margin.png',(16,1943,466,2339),-38,'Complete lower slanted marginal note and curved guide'),
 ('18_louvert.png',(1274,2097,1660,2270),0,'Inserted l\u2019ouvert with curved placement guide'),
 ('19_un.png',(225,2231,811,2344),0,'Inserted un above fermé and bottom line'),
 ('20_donc.png',(807,2234,1139,2344),0,'Don c/puis and cancelled final group'),
]
report=[]
for name,bbox,angle,purpose in items:
 c=im.crop(bbox)
 c=ImageOps.autocontrast(c)
 if angle:
  c=c.rotate(angle,expand=True,fillcolor='white',resample=Image.Resampling.BICUBIC)
 c=c.resize((2400, round(2400*c.height/c.width)), Image.Resampling.LANCZOS)
 c.save(root/name)
 report.append({'path':name,'bbox':list(bbox),'rotation':angle,'purpose':purpose,'coordinate_system':'original full scan, origin upper left'})
(root/'crops.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
a=Image.open('/workspace/scratch/94548b74fbe0/source/SP40_CW_81_scans/J81-02_81_scan015_a.jpg')
b=Image.open('/workspace/scratch/94548b74fbe0/source/SP40_CW_81_scans/J81-02_81_scan015_b.jpg')
print('Full:', im.size, 'a:',a.size,'b:',b.size, 'dimension-derived lower-half offset:', im.height-b.height)
print('Crops written:',len(items))
