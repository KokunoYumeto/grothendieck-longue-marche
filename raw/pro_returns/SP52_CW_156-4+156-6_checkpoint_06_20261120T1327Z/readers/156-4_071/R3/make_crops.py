from PIL import Image, ImageOps, ImageEnhance
from pathlib import Path
import json
out=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_071/R3')
src='/workspace/scratch/6644f30583f9/source/SP52_CW_156-4+156-6_scans/J156-4-09_156-4_scan071.jpg'
specs=[
('01_folio',[710,0,950,188],0,'Worked running folio, including the adjacent opening line.'),
('02_donnons',[265,185,1390,380],0,'Donnons nous and preceding line.'),
('03_margin_marks',[43,393,415,575],0,'Both detached left-margin columns with adjacent line starts.'),
('04_insertion',[620,530,1650,690],0,'Raised dans F, underlying de, object letter and surrounding corollary line.'),
('05_orders_abbreviation',[895,679,1615,880],0,'Contracted seulement and the two inequality forms with surrounding words.'),
('06_contree',[1180,780,1668,1050],0,'First sous-contrée spelling and following Phi subset F.'),
('07_itou',[270,895,820,1110],0,'Worked itou with surrounding words.'),
('08_live_final',[260,1198,1689,1545],0,'Quoted F-saturée, crowded parentheses/reference, abbreviation and cancelled mark before une.'),
('09_draft_folio',[820,2150,1015,2350],180,'Rotated draft folio with the adjacent first line.'),
('10_draft_opening_right',[720,2090,1440,2280],180,'Opening un ensemble et and overwritten capital with surrounding line.'),
('11_draft_opening_left',[45,2090,815,2270],180,'un ens de parties de M, condition précédente and parenthetical abbreviation.'),
('12_draft_alors',[22,1910,1435,2100],180,'Alors Phi muni through satisfait C1 and ses objets irréductibles.'),
('13_draft_application',[20,1740,600,1915],180,'Application arrow/ticks, endpoints, and neighbouring bijection line.'),
('14_draft_Ax_M',[590,1720,1435,1930],180,'Ax, x membership M and étant une bijection, with surrounding words.'),
('15_draft_final_left',[45,1485,620,1735],180,'Final union and tiny indices with preceding irréductibles de Phi.'),
('16_draft_deletion_dem',[615,1485,1415,1740],180,'Internal cancelled groups, Dém and beginning of last assertion.'),
]
im=Image.open(src)
meta=[]
for name,box,rotation,reason in specs:
 crop=im.crop(box)
 if rotation: crop=crop.rotate(rotation,expand=True)
 scale=2400/crop.width
 crop=crop.resize((2400,round(crop.height*scale)),Image.Resampling.LANCZOS)
 crop=ImageOps.autocontrast(crop)
 crop=ImageEnhance.Sharpness(crop).enhance(1.15)
 path=out/'crops'/(name+'.jpg')
 crop.save(path,quality=94)
 meta.append(dict(path=str(path),source=src,bbox=box,scale=scale,rotation=rotation,reason=reason,transforms=['crop','rotate '+str(rotation)+' degrees' if rotation else 'no rotation','LANCZOS resize to 2400 px across','autocontrast','sharpness 1.15','JPEG quality 94']))
(out/'crop_metadata.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
print(json.dumps([dict(name=Path(x['path']).name,bbox=x['bbox'],scale=x['scale'],rotation=x['rotation']) for x in meta],indent=2))
