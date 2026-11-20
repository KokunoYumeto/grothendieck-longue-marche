from PIL import Image, ImageOps, ImageEnhance
from pathlib import Path
import json
out=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_071/R1')
src=Path('/workspace/scratch/6644f30583f9/source/SP52_CW_156-4+156-6_scans/J156-4-09_156-4_scan071.jpg')
im=Image.open(src)
specs=[
 ('01_top_folio',(620,0,1120,190),0,'Overwritten upper page number with the adjoining first line'),
 ('02_donnons',(260,190,1380,385),0,'Opening second line and the compact Donnons nous group'),
 ('03_margin_left',(35,385,335,570),0,'Both columns of detached marginal ink and adjacent line start'),
 ('04_formula_insertion',(780,385,1645,695),0,'Formula punctuation, inserted dans F and underlying de'),
 ('05_non_seult',(620,600,1600,815),0,'Contraction after non and first inequality, with preceding line'),
 ('06_second_order_sous',(950,770,1655,1035),0,'Second relation and first sous-contree, including accents and punctuation'),
 ('07_itou',(270,925,1020,1120),0,'Worked itou and preceding ce qu on appelle'),
 ('08_quotation_end',(275,1205,1690,1425),0,'Quoted F-saturee, both right punctuation groups and adjacent line'),
 ('09_automatic_deleted',(530,1320,1510,1565),0,'Abbreviated automatiquement and the cancelled mark before une'),
 ('10_rotated_open',(35,2075,1460,2350),180,'Inverted folio, overwritten capital, un ens de parties, first two lines and parenthesis'),
 ('11_rotated_middle',(35,1800,1430,2110),180,'Inverted Alors Phi muni, C1, indices and complete application line'),
 ('12_rotated_end',(35,1490,1460,1845),180,'Inverted bijection ending, internal cancelled words, final Dém and union formula'),
]
records=[]
for name,bbox,rot,reason in specs:
 crop=im.crop(bbox)
 if rot: crop=crop.rotate(rot,expand=True)
 crop=ImageOps.autocontrast(crop)
 scale=2500/crop.width
 crop=crop.resize((2500,round(crop.height*scale)),Image.Resampling.LANCZOS)
 crop=ImageEnhance.Sharpness(crop).enhance(1.25)
 path=out/'crops'/f'{name}.jpg'
 crop.save(path,quality=94)
 records.append({'path':str(path),'source':str(src),'bbox':list(bbox),'scale':scale,'rotation':rot,'reason':reason,'transforms':['autocontrast','LANCZOS resize to 2500 px width','sharpness factor 1.25','JPEG quality 94']})
(out/'crop_manifest.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print(len(records),'crops created')
