from PIL import Image, ImageOps, ImageFilter
from pathlib import Path
import json

OUT = Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_067/R1')
SRC = Path('/workspace/scratch/6644f30583f9/source/SP52_CW_156-4+156-6_scans')
specs = [
('01_top_first','a',[432,20,1666,222],2,0,'First operator, disjoint ending, index relation, raised inclusion and its connector.'),
('02_top_second','a',[432,195,1666,383],2,0,'Second definition and inserted equality: p strokes, disjoint ending, phi, extra closing mark and insertion connector.'),
('03_deleted_sentence','a',[292,400,1655,502],2,0,'Cancelled Donc sentence and the extent of its first formula.'),
('04_deleted_phi','a',[302,438,460,583],13,0,'Isolated cancelled phi below Donc, with part of the surrounding line.'),
('05_deleted_formulas','a',[473,477,1650,620],2,0,'Cancelled formula rows, operator spellings and overwritten/residual subscripts.'),
('06_left_note','a',[28,699,435,920],6,-15,'Slanted left note, including final word and connector near brace.'),
('07_brace','a',[441,677,1206,854],3,0,'Equivalence arrow, barred F and isolated low point in second brace row.'),
('08_right_note','a',[1219,615,1658,950],5,0,'NB margin text, Stable ending, underline and angular connecting marks.'),
('09_middle_definitions','a',[493,880,1565,1104],2.3,0,'Middle operator p strokes and accents on def labels.'),
('10_on_a','a',[286,1124,1648,1242],2,0,'Word following On a and the terminal Sup spelling and punctuation.'),
('11_passage','b',[291,137,1546,329],2,0,'Cancelled contient and passage phrase, including sous-figure ending.'),
('12_union','b',[1000,194,1576,330],4,0,'Cancelled first symbol before barred Phi, union bar and dotted indices.'),
('13_lower_operators','b',[296,349,1125,585],3,0,'Lower operator forms and overwritten second subscript.'),
('14_lower_builder','b',[705,429,1660,570],2.6,0,'Crossed loop before X, tt/forall, Y membership and closing brace.'),
('15_ramene','b',[313,550,1659,751],2,0,'ramene/revenu, terminal punctuation and section/question marker.'),
('16_saturee_heading','b',[302,700,1657,930],2,0,'Underlined heading, inserted F0, overwritten alphabet, cosupport and parenthetical abbreviation.'),
('17_saturee_sentence','b',[301,890,1652,1113],2,0,'Second saturee, raised M0, support/cosupport and correspondent wording.'),
('18_mutuellement_par','b',[299,1019,1066,1174],3,0,'Final mutuellement and heavy terminal par, with following display context.')
]
records=[]
for name,half,bbox,scale,rot,reason in specs:
    source=SRC/f'J156-4-09_156-4_scan067_{half}.jpg'
    im=Image.open(source).crop(bbox)
    im=ImageOps.autocontrast(im)
    im=im.resize((round(im.width*scale),round(im.height*scale)),Image.Resampling.LANCZOS)
    im=im.filter(ImageFilter.UnsharpMask(radius=1.2,percent=115,threshold=3))
    if rot:
        im=im.rotate(rot,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
    path=OUT/'crops'/f'{name}.jpg'
    im.save(path,quality=94)
    records.append(dict(path=str(path),source=str(source),bbox=bbox,scale=scale,rotation=rot,reason=reason,transformations='autocontrast; LANCZOS enlargement; UnsharpMask(radius=1.2, percent=115, threshold=3); rotation with BICUBIC only if nonzero'))
(OUT/'crop_manifest.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print(f'Created {len(records)} independent crops.')
