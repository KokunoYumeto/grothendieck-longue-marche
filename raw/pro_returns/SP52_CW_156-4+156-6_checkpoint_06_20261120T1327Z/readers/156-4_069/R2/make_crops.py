from PIL import Image, ImageOps, ImageFilter
from pathlib import Path
import json
out=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_069/R2')
src=Path('/workspace/scratch/6644f30583f9/source/SP52_CW_156-4+156-6_scans/J156-4-09_156-4_scan069.jpg')
im=Image.open(src)
specs=[
('01_presume',(1230,50,1655,265),0,'Inserted présume, struck dis, and curved connecting arm'),
('02_ultra',(295,195,760,385),0,'Raised ultra and quotation marks; shape of its insertion leader'),
('03_quelc',(1170,185,1635,390),0,'Sup quelc. and closing punctuation'),
('04_deleted_sentence',(310,345,1140,500),0,'Cancelled Il faudra y revenir and extent of cancellation'),
('05_supports',(330,375,1655,640),0,'Donc, s’identifient, Parties ending, and body continuation'),
('06_compact',(310,590,825,845),0,'Live compact abbreviation and surrounding cancelled groups'),
('07_disconnexe',(815,560,1655,795),0,'disconnexe, separation of ultra and stonien, final punctuation'),
('08_compatibility',(495,1080,1570,1305),0,'Raised compatibility clause, relation alphabet, full angular enclosure'),
('09_toute',(820,1195,1535,1360),0,'Lower insertion toute/toutes and complete local bracket'),
('10_phi',(620,1245,1100,1445),0,'Phi and displaced high mark with following M'),
('11_tuple',(280,1455,1410,1700),0,'Tuple alphabet and relation sign; M primes in surrounding text'),
('12_cosup',(535,1610,1030,1835),0,'Cosupport abbreviation, lowered M, M prime, and equality'),
('13_set',(960,1590,1670,1820),0,'Full set expression, x size, primes, calligraphic relation, quantifier, closing brace'),
('14_margin_open',(20,145,365,550),-36,'Opening slanted sentence and quotation extent'),
('15_margin_examples',(20,345,420,845),-38,'Examples types, donnés, deleted word, au début and terms'),
('16_margin_E',(20,610,440,1065),-40,'E (top. ou mesurable), alors Sigma, identification and parties de E'),
('17_margin_stone',(20,835,470,1270),-40,'Verb before compactifié, Stone, lowered disc. and sentence boundary'),
('18_margin_proof',(20,1005,535,1530),-40,'Dans le cas qui vient, je ne vois comment prouver, pour trois supports'),
('19_margin_formula',(25,960,585,1650),-46,'Complete P Q R and wedge/vee equality, extra hook and terminal mark'),
('20_bottom_note',(110,1790,1195,2320),-22,'Complete bottom example note, its lettering, quotes and long rule')]
meta=[]
for name,box,rot,reason in specs:
 c=im.crop(box)
 if rot: c=c.rotate(rot,Image.Resampling.BICUBIC,expand=True,fillcolor='white')
 scale=2500/c.width
 c=c.resize((2500,round(c.height*scale)),Image.Resampling.LANCZOS)
 c=ImageOps.autocontrast(c,cutoff=0.3)
 c=c.filter(ImageFilter.UnsharpMask(radius=1.2,percent=120,threshold=3))
 path=out/'crops'/f'{name}.jpg'
 c.save(path,quality=94)
 meta.append(dict(path=str(path),source=str(src),bbox=list(box),scale=scale,rotation=rot,reason=reason,transform='crop; rotate PIL BICUBIC expand white if nonzero; resize LANCZOS to 2500 px; autocontrast cutoff 0.3%; UnsharpMask radius 1.2 percent 120 threshold 3; JPEG quality 94',size=list(c.size)))
(out/'crop_metadata.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2))
(out/'inspection_log.md').write_text('# R2 inspection log: scan 069\n\nRecorded start: 2026-11-20 10:41:37 UTC (first clock reading).\n\n1. Viewed whole source J156-4-09_156-4_scan069.jpg once with view_image: layout, page 68, upper body, left diagonal note and formula, lower body, bottom oblique example and long rule.\n2. Viewed supplied half J156-4-09_156-4_scan069_a.jpg once with view_image: every visible body/marginal line; no redisplay.\n3. Viewed supplied half J156-4-09_156-4_scan069_b.jpg once with view_image: every visible body/marginal line, displays and bottom note; no redisplay.\n\nCrops prepared independently from whole source; see crop_metadata.json for exact source bboxes and transformations. The order of actual crop views is appended below. No OCR, external research or LaTeX compilation.\n')
print(json.dumps([{'name':Path(x['path']).name,'size':x['size']} for x in meta],ensure_ascii=False))
