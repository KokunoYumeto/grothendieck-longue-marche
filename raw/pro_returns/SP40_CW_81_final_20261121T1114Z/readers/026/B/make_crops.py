from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json
root=Path(__file__).resolve().parent
source=root.parents[3]/'source/SP40_CW_81_scans/J81-03_81_scan026.jpg'
# Coordinates refer to original 1694 x 2370 scan, origin upper left; boxes are half-open.
plan=[
('01_family',(550,270,820,355),0,'C026-R01, first Sigma alpha placements and family-index glyph'),
('02_interest',(590,690,1575,820),0,'H disputed on s’intéresse au cas où les'),
('03_hemispheres',(265,770,1610,945),0,'hémisphères cancellation state; first body Sigma; inserted de and its guide'),
('04_interlinear',(640,855,1415,1015),0,'C026-R02a–c, R03, R15; full inserted equation, after-connexes cancellation, et où; insertion guide'),
('05_si_condition',(560,975,1650,1110),0,'C026-R02d and R12; si les Sigma connexes et E relation emptyset, X est'),
('06_connexe_correction',(535,1055,1655,1210),0,'deleted les Sigma connexes, raised X connexe et, C026-R04 aussitôt and connected guide'),
('07_margin_diagram',(38,950,265,1375),-52,'complete slanted diagramme, two endpoints, segment, struck sign, lower label C026-R05–R06'),
('08_barred_formulas',(445,1150,1660,1340),0,'all four closure/intersection/right-difference Sigma groups, commas and head runs'),
('09_parenthesis_end',(270,1285,1600,1550),0,'H disputed complete ending; C026-R07 superscript and following comma; two Sigma forms'),
('10_pairs_correction',(85,1605,775,1775),0,'C026-R08 and R13; both pairs, crossed distinctes, raised de X and full guide'),
('11_adjective',(1100,1595,1650,1725),0,'C026-R09 whole underlined non adjective and full p descender'),
('12_distinctes_insertion',(260,1690,1005,1885),0,'full elles sont distinctes et si insertion, base si/on and long bent guide'),
('13_first_display',(620,1875,1650,2035),0,'two positive Sigmas, d’où and E1 E2, signs, endpoint parenthesis'),
('14_first_bottom_row',(290,2040,1515,2175),0,'on a alors; C026-R10 and R14; first inclusion, cancellation, i.e., equality'),
('15_second_bottom_row',(625,2150,1515,2265),0,'C026-R11 label points; second inclusion and equality complete glyphs'),
('16_final_row',(515,2240,1470,2348),0,'final definition label def/déf and complete three Sigma terms with endpoint signs')
]
img=Image.open(source).convert('RGB')
records=[]
for name,box,rot,purpose in plan:
 im=img.crop(box)
 cropped=im.size
 if rot: im=im.rotate(rot, resample=Image.Resampling.BICUBIC, expand=True, fillcolor='white')
 rotated=im.size
 width=3000
 height=round(im.height*width/im.width)
 im=im.resize((width,height),Image.Resampling.LANCZOS)
 im=ImageOps.autocontrast(im)
 im=im.filter(ImageFilter.UnsharpMask(radius=1.2,percent=120,threshold=3))
 dest=root/'crops'/f'{name}.png'; dest.parent.mkdir(exist_ok=True)
 im.save(dest)
 records.append({'path':str(dest.relative_to(root)),'bbox':list(box),'rotation':rot,'rotation_convention':'PIL degrees counterclockwise with expand=True; BICUBIC rotation, white fill','crop_size':list(cropped),'rotated_size':list(rotated),'display_size':[width,height],'resize':'PIL LANCZOS','autocontrast':True,'sharpen':{'method':'UnsharpMask','radius':1.2,'percent':120,'threshold':3},'purpose':purpose,'status_before_view':'unresolved after prescribed half views'})
(root/'crop_plan.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print(json.dumps([{'path':r['path'],'bbox':r['bbox'],'size':r['display_size']} for r in records],indent=2))
