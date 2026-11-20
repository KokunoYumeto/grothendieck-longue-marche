from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json

root=Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
source=Image.open(root/'packets/145_scan024/page.jpg')
dest=root/'edition/crops'
items=[
 ('01_opening_s_and_insertion',[1180,155,1645,325],0,'Opening ornate S_3 and complete inserted parenthesis with doubtful words and final symbol'),
 ('02_first_pi_and_gamma',[275,430,610,530],0,'First hatted pi group sign and nearby doubled Gamma for local caps/legs comparison'),
 ('03_intersection_formulas',[585,525,1050,735],0,'Complete two-line intersection display, overwritten group sign, subscript and all C marks'),
 ('04_cancelled_nb',[1305,525,1435,635],0,'Separate cancelled underlined NB to the right of the intersection formulas'),
 ('05_complete_left_margin',[18,445,600,990],-25,'Complete diagonal NB: formula layout, inclusion sign, all doubtful ornate S signs and lexical disagreements'),
 ('06_des_elts',[640,895,1335,1000],0,'des elts de and complete following double-hatted E with exclamation'),
 ('07_lzero_and_pour_etre',[245,1000,1658,1385],0,'L_0 engendre par l_0; full kappa/k formula; u membership; pour etre insertion and its placement'),
 ('08_relation_twenty',[260,1555,1255,1725],0,'Complete relation20 with local pi form, all numeric indices and surrounding et des'),
 ('09_pour_relation_twentyone',[245,1725,970,1918],0,'pour state and complete relation21 including disputed dark exponent'),
 ('10_relation_twentytwo',[235,2015,1510,2170],0,'Complete relation22, all three dark exponent states, parentheses, middle dot and final punctuation'),
 ('11_final_lines',[245,2165,1640,2348],0,'Last two lines, underlining scope, final pi form, numbered reference and punctuation'),
 ('12_footer_twenty_three',[24,2265,115,2348],0,'Physical lower-left handwritten23 omitted by H'),
]
boxes={};meta=[]
for name,box,angle,target in items:
 key='145_scan024_'+name
 im=ImageOps.autocontrast(source.crop(box))
 if angle:im=im.rotate(angle,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
 im=im.resize((2800,round(im.height*2800/im.width)),Image.Resampling.LANCZOS)
 im=im.filter(ImageFilter.UnsharpMask(radius=1.2,percent=120,threshold=3))
 im.save(dest/(key+'.png'))
 boxes[key]=box
 meta.append({'file':'crops/'+key+'.png','box':box,'rotation_degrees':angle,'target':target})
(dest/'145_scan024_crop_boxes.json').write_text(json.dumps(boxes,ensure_ascii=False,indent=2)+'\n')
(dest/'145_scan024_crop_meta.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'crops':len(items),'manifest':str(dest/'145_scan024_crop_meta.json')},indent=2))
