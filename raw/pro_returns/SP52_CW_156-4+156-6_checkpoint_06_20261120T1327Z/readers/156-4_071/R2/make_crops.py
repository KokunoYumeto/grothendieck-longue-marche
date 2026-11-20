from pathlib import Path
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
import json
base=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_071/R2')
src='/workspace/scratch/6644f30583f9/source/SP52_CW_156-4+156-6_scans/J156-4-09_156-4_scan071.jpg'
items=[
('01_folio70',(620,10,1020,190),0,'Overwritten running folio, with surrounding opening line.'),
('02_donnons',(270,190,1375,380),0,'Third-line wording and punctuation, with preceding line.'),
('03_condition',(260,375,1605,588),0,'Implication punctuation, parentheses, prime and disj. stops.'),
('04_margin_marks',(55,389,435,572),0,'Both detached marginal mark groups beside Une, preserving their height difference.'),
('05_corollary_correction',(615,535,1625,810),0,'Raised dans F, state of de, family letter, and surrounding corollary line.'),
('06_orders_abbreviation',(890,674,1595,875),0,'Non seult/seulemt and the two order relations.'),
('07_contree',(1180,780,1655,968),0,'Underlined sous, hyphen, accent and ending of first contrée, with preceding words.'),
('08_itou',(270,958,955,1112),0,'Worked word after Donc and beginning of pour, with surrounding line.'),
('09_quote_label',(270,1235,1160,1422),0,'Opening quotation, saturée ending, punctuation and absence/presence of closing quote.'),
('10_punctuation',(1260,1200,1688,1425),0,'Right-edge punctuation after terms de leq, with entire terminal group and clear page edge.'),
('11_final_live',(260,1360,1540,1555),0,'Cf page 67, automatically abbreviation, cancelled f-like group, une, final underived spelling and stop.'),
('12_folio55',(720,2140,1030,2340),180,'Inverted overwritten folio and neighbouring first-line letters.'),
('13_draft_opening',(75,2085,1450,2275),180,'Inverted opening un ensemble ... un ens de parties de M; line above condition.'),
('14_draft_capital',(715,2070,1030,2275),180,'Worked capital before un and its visible layering, with neighbouring line.'),
('15_draft_parenthesis',(75,2000,685,2180),180,'Parenthetical small word and dash after condition précédente.'),
('16_draft_alors',(25,1900,1445,2105),180,'Alors Phi, muni, relation inclusion punctuation; next C1 line.'),
('17_draft_application',(25,1740,1420,1960),180,'Ax, small x domain, application arrow terminal strokes and next line.'),
('18_draft_deletion',(775,1585,1430,1800),180,'Two locally cancelled groups after des, with preceding and following line context.'),
('19_draft_dem',(870,1465,1320,1650),180,'Opening final draft word and Ax, including accents and boundary stroke.'),
('20_draft_union',(55,1530,470,1740),180,'Final union, its index and Ai, with preceding line and surrounding strokes.'),
]
img=Image.open(src)
manifest=[]
for name,bbox,rot,reason in items:
 im=img.crop(bbox)
 if rot: im=im.rotate(rot,expand=True)
 scale=2400/im.width
 im=ImageOps.autocontrast(im,cutoff=.3).resize((2400,round(im.height*scale)),Image.Resampling.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1.2,percent=115,threshold=3))
 path=base/'crops'/(name+'.jpg')
 im.save(path,quality=94,subsampling=0)
 manifest.append(dict(path=str(path),source=src,bbox=list(bbox),scale=scale,rotation=rot,reason=reason,transform='PIL autocontrast cutoff 0.3%; LANCZOS resize to width 2400; UnsharpMask radius 1.2 percent 115 threshold 3; JPEG quality 94'))
(base/'crop_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
with (base/'inspection_log.txt').open('a') as f:
 f.write('Open-locus plan: twenty independent crops made once each, from original whole image; no re-crops. Each crop includes contextual neighbouring line material. All original bboxes, rotations and scales are in crop_manifest.json and report.json.\n')
 for i in manifest: f.write('Prepared '+i['path']+'; bbox='+str(i['bbox'])+'; scale='+str(i['scale'])+'; rotation='+str(i['rotation'])+'; '+i['transform']+'; '+i['reason']+'\n')
print('Created',len(manifest),'own crops.')
