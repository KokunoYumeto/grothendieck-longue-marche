from PIL import Image, ImageOps, ImageEnhance
from pathlib import Path
import json, datetime
out=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_067/R2')
src='/workspace/scratch/6644f30583f9/source/SP52_CW_156-4+156-6_scans/J156-4-09_156-4_scan067.jpg'
im=Image.open(src)
items=[
('01_top_first_operator',(432,102,1155,238),0,'First family alphabet and single-p operator; adjoining set opening'),
('02_top_first_end',(1158,20,1662,270),0,'First disjoint ending, H_i relation, phi, and raised subset enclosure'),
('03_top_second_and_insert',(432,190,1662,395),0,'Second operator, disjoint ending, phi and closure; added third line with curved connector'),
('04_cancelled_prose',(290,397,1654,502),0,'Entire struck prose line including after Donc, last operator and missing argument'),
('05_cancelled_equations',(308,475,1643,620),0,'Cancelled phi, repeated equation and lower expressions, subscripts and cancellation strokes'),
('06_left_note',(33,690,435,916),-15,'Slanted left note and its arrow; mutuellement and determinent accents'),
('07_live_brace',(438,606,1190,845),0,'Live premise, double arrow, barred F, and low point before family'),
('08_right_note',(1223,612,1656,941),0,'Right marginal NB, final Stable ending, underline and enclosure connector'),
('09_double_prime_defs',(508,864,1570,1108),0,'Double primes, cosup/cosupp, def accents and supp p strokes'),
('10_on_a',(286,1117,1109,1237),0,'Word after On a and following inclusion'),
('11_sup_passage',(1060,1123,1647,1332),0,'Sup ending, punctuation, colon or a after passage and une'),
('12_contient_union',(295,1234,1622,1450),0,'Cancelled contient Phi, sous-figure ending, overwritten sign before barred Phi and union indices'),
('13_lower_cosup',(297,1445,1102,1693),0,'Lower operator spelling and overwritten subscript; initial correction before X'),
('14_tt_clause',(1014,1511,1665,1637),0,'Text disjoint de tt and Y membership in M with barred Phi'),
('15_ramene_section',(303,1655,1647,1865),0,'ramene or revenu, sentence punctuation and section mark'),
('16_saturee_heading',(296,1799,1645,2040),0,'Underlined heading, raised family zero, overwritten family, cosupport and p.r.a clause'),
('17_saturee_second',(292,2000,1660,2201),0,'Second saturee and raised M zero, cosupport versus support, sentence punctuation'),
('18_bottom_words_formula',(301,2159,1320,2358),0,'Mutuellement and par cancellation state; final formula bar and zeros')
]
(out/'crops').mkdir(exist_ok=True)
meta=[]
for name,bbox,rotation,reason in items:
    c=im.crop(bbox)
    scale=2400/c.width
    c=c.resize((2400,round(c.height*scale)), Image.Resampling.LANCZOS)
    c=ImageOps.autocontrast(c,cutoff=0.15)
    c=ImageEnhance.Sharpness(c).enhance(1.25)
    if rotation:c=c.rotate(rotation,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
    f=out/'crops'/(name+'.jpg')
    c.save(f,quality=94)
    meta.append(dict(path=str(f),source=src,bbox=list(bbox),scale=scale,rotation=rotation,reason=reason,transformations='PIL LANCZOS resize to 2400 px across before any rotation; autocontrast cutoff 0.15%; sharpness 1.25; JPEG quality 94'))
(out/'crops_manifest.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2))
(out/'inspection_log.md').write_text('# R2 inspection log — 156-4 scan 067\n\nAll bboxes below are original pixels on the explicitly named source. No OCR, external sources or LaTeX compiler used.\n\n1. Viewed whole `'+src+'` once, original 1681 × 2359, via view_image; no preprocessing. Identified page number, top two-line definition plus addition, struck block, two marginal notes, brace display, two definition lines, following paragraph with deletion and union, two lower formula lines, and saturated-part definition with final pair.\n2. Viewed supplied first half `'+src.replace('.jpg','_a.jpg')+'` once, original 1681 × 1259, via view_image; no preprocessing. Read every upper line against C and H.\n3. Viewed supplied second half `'+src.replace('.jpg','_b.jpg')+'` once, original 1681 × 1260, via view_image; no preprocessing. Read every lower line against C and H.\n\nOwn crop views follow in tool-emission order; the matching entries were added after each successful display.\n')
print(len(meta), 'crops created')
