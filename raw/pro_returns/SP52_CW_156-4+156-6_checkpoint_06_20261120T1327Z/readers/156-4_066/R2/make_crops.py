from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json
p=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_066/R2')
src='/workspace/scratch/6644f30583f9/source/SP52_CW_156-4+156-6_scans/J156-4-09_156-4_scan066.jpg'
a=Image.open(src)
items=[
('01_lemma_resp', [1220,120,1640,370], 0, 'Raised parenthesis fini/finie and Il/il below'),
('02_lemma_nb_sont', [965,275,1635,495], 0, 'Compressed nb and sont/soient'),
('03_after_piG', [565,530,930,745], 0, 'Cancelled mark after pi-zero(G)'),
('04_first_exponent', [505,735,850,945], 0, 'Deleted superscript and live exclamation mark'),
('05_attention_second_exponent', [925,700,1555,935], 0, 'Attention and d/! exponent'),
('06_quotation', [680,850,1325,1055], 0, 'du/des and Sup, quotation/parenthesis punctuation'),
('07_tuple_C_gloss', [205,1040,570,1295], -4, 'Alphabet of C and Contrée gloss with its pointer'),
('08_tuple_relation_gloss', [540,1060,840,1305], 0, 'Overwritten third relation and three-line note'),
('09_C4_cancelled', [1375,1395,1640,1620], 0, 'Cancelled group after product'),
('10_C4_overwrite_F', [1140,1415,1410,1650], 0, 'Underlying glyph at final Fi'),
('11_C4_final_relation', [1400,1495,1660,1675], 0, 'Relation between i and I'),
('12_heading', [330,1710,950,1980], 0, 'Contrée/Contrie and résiduelle/réssiduelle'),
('13_bottom_family', [285,1890,940,2095], 0, 'Cancelled parenthesized family and inserted Hi/connector'),
('14_bottom_Cosupp', [365,2000,740,2220], 0, 'Cancelled Cosupp. and Phi'),
('15_bottom_disjointe', [1060,1975,1550,2250], 0, 'Disjointe/disjoint ending'),
('16_last_cancelled', [925,2215,1495,2348], 0, 'Cancelled Posons/Poser and live Posons'),
]
records=[]
for name,bbox,rot,reason in items:
 c=a.crop(bbox)
 c=ImageOps.autocontrast(c)
 scale=2400/c.width
 c=c.resize((2400, round(c.height*scale)),Image.Resampling.LANCZOS)
 if rot: c=c.rotate(rot,Image.Resampling.BICUBIC,expand=True,fillcolor='white')
 c=c.filter(ImageFilter.UnsharpMask(radius=1.1,percent=120,threshold=3))
 target=p/'crops'/f'{name}.jpg'
 c.save(target,quality=94)
 records.append(dict(path=str(target),source=src,bbox=bbox,scale=scale,rotation=rot,reason=reason,transforms='autocontrast; LANCZOS resize to 2400 px before rotation; UnsharpMask radius 1.1 percent 120 threshold 3; JPEG quality 94'))
(p/'crops_manifest.json').write_text(json.dumps(records,indent=2,ensure_ascii=False))
(p/'inspection_log.md').write_text('# R2 inspection log — 156-4 scan 066\n\n1. Whole page viewed once: '+src+'; native view; layout inventory.\n2. Upper half viewed once: '+src.replace('.jpg','_a.jpg')+'; native view; every line collated against C and H.\n3. Lower half viewed once: '+src.replace('.jpg','_b.jpg')+'; native view; every line collated against C and H.\n\n## Open places after the halves\n\n'+ '\n'.join(f'- {r["reason"]}: {r["path"]}' for r in records)+'\n\n## Crop views (in order)\n\n')
print('Created',len(records),'own crops; none viewed yet.')
