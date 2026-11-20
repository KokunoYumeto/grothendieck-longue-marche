from PIL import Image,ImageOps,ImageFilter
from pathlib import Path
import json
root=Path('/workspace/scratch/94548b74fbe0/out/readers/003/A')
im=Image.open('/workspace/scratch/94548b74fbe0/source/SP40_CW_81_scans/J81-01_81_scan003.jpg')
specs=[
('01_title_insertion',(540,15,790,128),0,2400,'Inserted parenthetic adjective'),
('02_title_ending',(1020,72,1655,197),0,3000,'cat. and terminal of isotopique(s)'),
('03_morphism',(175,170,1150,280),0,3500,'Morphism word, arrow, target C, quoted adjective'),
('04_f0_overwrite',(1210,420,1545,525),0,2700,'Overwritten value f(0)'),
('05_cancelled_set',(510,565,940,655),0,3000,'Cancelled relation and set after on ait'),
('06_ramification',(1275,580,1785,705),0,3000,'en z or en un z'),
('07_polynomials',(515,736,1110,825),0,3000,'Opening curve and C(z) delimiters'),
('08_resp',(1010,915,1360,1005),0,2600,'Raised abbreviation ending'),
('09_slanted_note',(20,930,445,1355),-45,3000,'Slanted normalization note'),
('10_fraction_cancellation',(190,1228,600,1345),0,2700,'Cancelled Q(z) beside numerator'),
('11_deleted_word',(215,1635,635,1717),0,2800,'Deleted au/ou after equality'),
('12_question_parenthesis',(212,1934,980,2020),0,3300,'d’où/donc and parenthesis'),
('13_question_insertion',(810,1830,1238,2020),0,3000,'Insertion word, formula, and attachment at question'),
('14_struck_start',(205,2020,810,2160),0,3200,'Struck preliminary sentence and Q(T)=1'),
('15_cond_abbreviation',(790,2075,1120,2153),0,2500,'conditions abbreviation'),
('16_TP0',(1040,2160,1370,2265),0,2600,'P(T)=TP0(T) and possible earlier cancellation'),
('17_sideways_note',(20,1490,250,2440),-90,4300,'Sideways continuation with cancelled prose and final stroke')
]
records=[]
for name,bbox,rot,width,purpose in specs:
 c=im.crop(bbox)
 if rot:c=c.rotate(rot,expand=True,resample=Image.Resampling.BICUBIC,fillcolor='white')
 c=ImageOps.autocontrast(c)
 c=c.resize((width,round(c.height*width/c.width)),Image.Resampling.LANCZOS)
 c=c.filter(ImageFilter.UnsharpMask(radius=1.1,percent=120,threshold=3))
 c.save(root/(name+'.png'))
 records.append(dict(path=name+'.png',bbox=bbox,rotation=rot,purpose=purpose))
(root/'crop_records.json').write_text(json.dumps(records,ensure_ascii=False,indent=2))
print(json.dumps(records))
