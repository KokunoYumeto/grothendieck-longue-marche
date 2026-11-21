"""One planned enlargement per unresolved locus; no text recognition or comparison."""
from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json
base=Path('/workspace/scratch/94548b74fbe0/out/readers/019/B')
source=Path('/workspace/scratch/94548b74fbe0/source/SP40_CW_81_scans/J81-03_81_scan019.jpg')
plans=[
('01_opening',(250,60,940,170),'Opening abbreviation, accent and punctuation'),
('02_top_edge',(1350,55,1692,168),'First-line endpoint at physical right edge; punctuation after 0,1'),
('03_avec',(250,265,790,355),'C row09: small word before card'),
('04_first_U',(550,505,1015,635),'C row10: first U entrance versus cancelled equals; nearby indices and sign'),
('05_lune',(935,735,1555,840),'C row11: l’une or l’un and endpoint'),
('06_on_a',(725,850,1285,950),'C row02: on a after récurrence'),
('07_first_union',(500,945,1205,1120),'C rows03–04: first large union and overwritten lower index'),
('08_brace_predecessor',(270,1160,975,1290),'C row12: overwritten Sigma and lower index; where-word'),
('09_on_a_donc',(270,1490,670,1585),'C row05 and H cancellation before On a donc'),
('10_second_union',(785,1580,1070,1745),'Independent later large join form and lower index'),
('11_display_endpoint',(1410,1570,1665,1745),'Detached right-side marks after displayed closing parenthesis'),
('12_deuxieme',(260,1755,1020,1888),'Au deuxième versus dernier, with cancelled Soit and following equals'),
('13_struck_somme',(1020,1755,1580,1870),'C row06: cancelled word after dans la'),
('14_borner_mark',(250,2015,1100,2110),'C row07 and H placeholder; à versus colon after borner'),
('15_last_formula',(600,2240,1510,2362),'Last display, all indices and endpoint at lower edge')
]
im=Image.open(source)
manifest=[]
for name,box,purpose in plans:
 crop=ImageOps.autocontrast(im.crop(box))
 width=2800
 crop=crop.resize((width,round(crop.height*width/crop.width)),Image.Resampling.LANCZOS)
 crop=crop.filter(ImageFilter.UnsharpMask(radius=1.1,percent=120,threshold=3))
 path=base/'crops'/(name+'.png')
 crop.save(path)
 manifest.append({'path':'crops/'+name+'.png','source':str(source),'bbox':list(box),'rotation':0,'width':width,'purpose':purpose,'viewed':False})
(base/'crops'/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print('Created',len(manifest),'planned crops; source size',im.size)
