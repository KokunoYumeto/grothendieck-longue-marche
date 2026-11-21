from PIL import Image, ImageOps, ImageFilter
from pathlib import Path
import json
base=Path('/workspace/scratch/94548b74fbe0/out/readers/015/A')
source=Path('/workspace/scratch/94548b74fbe0/source/SP40_CW_81_scans/J81-02_81_scan015.jpg')
items=[
('01_heading',(43,19,283,120),0,'Heading letters, overwritten predecessor and underline'),
('02_family',(1110,119,1675,225),0,'First indexed family overwritten glyph, ens. punctuation'),
('03_fermes',(190,177,555,296),0,'Opening insertion fermés/fermées and curved attachment guide'),
('04_upper_margin',(17,380,431,1068),-43,'Entire slanted upper-left note, local source doubts and arrow'),
('05_right_nb',(1238,324,1675,468),0,'Upper-right NB, exponent and complement glyph'),
('06_b_final_e',(1432,512,1665,607),0,'Final overwritten E in (b) and endpoint punctuation'),
('07_automatiquement',(976,603,1683,719),0,'Pale automatiquement and line ending'),
('08_case',(501,996,944,1113),0,'Case heading overwritten letters/sign and underline'),
('09_drawing_cancel',(132,1037,247,1134),0,'Crossed upper-left drawing label and its strokes'),
('10_drawing_exponent',(474,1180,570,1259),0,'Right drawing label overwritten exponent'),
('11_equivaut',(685,1371,1414,1466),0,'First cancelled inclusion, équivaut à and punctuation'),
('12_car_si',(202,1435,433,1518),0,'Cancelled phrase beneath drawing'),
('13_symetrique',(210,1845,981,1949),0,'Faint et before symétriquement and ending à'),
('14_vois_deleted',(408,1993,643,2078),0,'Cancelled vois. ouvert above bottom inclusion'),
('15_lower_margin',(17,1962,432,2345),-40,'Entire lower slanted note and curved guide'),
('16_bottom_words',(225,2238,1105,2346),0,'Inserted un, donc, and final cancelled group'),
('17_louvert',(1273,2093,1644,2252),0,'Inserted l\'ouvert, attachment guide and surrounding parenthesis'),
('18_car_formula',(691,2123,1228,2259),0,'Car, closure bar and underline geometry'),
('19_detached_top',(157,108,322,177),0,'Detached mark left of opening text'),
('20_detached_lower',(1533,1720,1661,1826),0,'Two detached spots beside display (2)'),
('21_bottom_insertion',(734,1984,1668,2138),0,'Inserted i.e. clause, cancellation, and on a ending'),
('22_aussi',(224,1673,497,1752),0,'Pale continuation aussi à'),
]
with Image.open(source) as original:
 for name,bbox,rotation,purpose in items:
  im=original.crop(bbox).convert('RGB')
  if rotation: im=im.rotate(rotation,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
  im=ImageOps.autocontrast(im)
  scale=2600/im.width
  im=im.resize((2600,round(im.height*scale)),Image.Resampling.LANCZOS)
  im=im.filter(ImageFilter.UnsharpMask(radius=1,percent=80,threshold=3))
  im.save(base/(name+'.png'))
records=[dict(path=name+'.png',bbox={'coordinate_system':'full scan; origin upper left','xyxy':list(bbox)},rotation=rotation,purpose=purpose) for name,bbox,rotation,purpose in items]
(base/'crops.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print('Created',len(items),'single local enlargements from the full scan.')
