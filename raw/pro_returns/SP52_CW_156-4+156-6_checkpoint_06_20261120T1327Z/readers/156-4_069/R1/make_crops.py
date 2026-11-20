from PIL import Image, ImageOps, ImageFilter
from pathlib import Path
import json
out=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_069/R1')
src=Path('/workspace/scratch/6644f30583f9/source/SP52_CW_156-4+156-6_scans/J156-4-09_156-4_scan069.jpg')
im=Image.open(src)
items=[
('01_presume_arm',[1250,40,1668,265],0,'Raised présume, cancelled dis, qu’on and connecting arm.'),
('02_ultra_quelc',[295,175,1640,458],0,'Raised ultra and opening quotation marks; Sup quelc. and closing punctuation; surrounding lines.'),
('03_supports',[315,360,1648,590],0,'Cancelled Il faudra y revenir; Donc; s’identifient; Parties and line surrounding.'),
('04_compact',[310,495,1668,795],0,'The crowded compact and separate cancelled groups, disconnexe, ultra punctuation and surrounding lines.'),
('05_margin_upper',[18,140,380,815],-46,'Opening slanted note through examples and cancelled word at donnés/au début, with adjoining slanted lines.'),
('06_margin_middle',[18,615,570,1230],-46,'Middle slanted passage: E, Σ, on trouve/trouvera, Stone, E_disc and following transition, with adjoining lines.'),
('07_margin_lower',[18,1080,390,1640],-46,'Lower slanted prose including je ne vois comment prouver, pour trois supports and P,Q,R.'),
('08_margin_formula',[145,920,580,1510],-53,'Whole marginal equality including extra opening mark and final punctuation, with surrounding line.'),
('09_construction',[300,1035,1668,1485],0,'Construction text, raised compatibility clause and long leader, toute/toutes insertion, marked Φ and surrounding lines.'),
('10_set_definition',[505,1575,1678,1825],0,'Set definition: one/two p operator, all capitals, primes, relation glyph, quantifier and delimiters with surrounding prose line.'),
('11_bottom_note',[115,1790,1210,2325],-21,'Foot note entirety, abbreviations/quotes and distinct long rule, with adjacent display margin.'),
]
meta=[]
for name,bbox,rot,reason in items:
 p=im.crop(tuple(bbox)).rotate(rot,expand=True,resample=Image.Resampling.BICUBIC,fillcolor='white')
 scale=2600/p.width
 p=p.resize((2600,round(p.height*scale)),Image.Resampling.LANCZOS)
 p=ImageOps.autocontrast(p).filter(ImageFilter.UnsharpMask(radius=1.1,percent=110,threshold=3))
 dest=out/'crops'/f'{name}.jpg'
 p.save(dest,quality=94)
 meta.append({'path':str(dest),'source':str(src),'bbox':bbox,'scale':scale,'rotation':rot,'reason':reason,'transform_order':['crop','rotate (PIL degrees; negative is clockwise), BICUBIC, expand, white fill','resize LANCZOS to width 2600','autocontrast','UnsharpMask radius 1.1 percent 110 threshold 3','JPEG quality 94']})
(out/'crop_metadata.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
(out/'inspection_log.md').write_text('# R1 inspection log — 156-4 scan 069\n\nStart: 2026-11-20T10:41:00Z (approximate; first tool clock at 10:41:36Z).\n\n1. Whole image: '+str(src)+' — viewed once for layout, without transformation.\n2. Supplied first half: '+str(src.with_name(src.stem+'_a.jpg'))+' — viewed once, no transformation.\n3. Supplied second half: '+str(src.with_name(src.stem+'_b.jpg'))+' — viewed once, no transformation.\n\nThe supplied whole is 1681 × 2358; each supplied half is 1681 × 1259. All own crop bboxes below refer to the whole image. Crops created by make_crops.py; transformations and exact scale are preserved in crop_metadata.json. A crop is logged as viewed only after the image tool returns it.\n')
print('Created',len(meta),'independent crops; all writes confined to R1 directory.')
