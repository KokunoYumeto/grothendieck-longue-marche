from PIL import Image, ImageOps, ImageFilter
from pathlib import Path
import json
root=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_073/R2')
source='/workspace/scratch/6644f30583f9/source/SP52_CW_156-4+156-6_scans/J156-4-09_156-4_scan073.jpg'
im=Image.open(source)
items=[
 ('01_top_cancelled_capital',[695,20,980,180],0,'First cancelled primed capital; includes folio and adjacent de/la.'),
 ('02_top_overwritten_g',[1170,135,1580,290],0,'Overwritten capital in the upper continuation; preceding figure and following de F.'),
 ('03_margin_note',[22,25,315,465],-55,'Entire oblique annotation, including detached low de and all high-right continuations.'),
 ('04_c7_ending',[1175,415,1680,655],0,'Induise/induit and final open primed capital, with preceding line and right-edge stop.'),
 ('05_roles_and_mark',[730,635,1310,855],0,'Role ending and worked mark before straight order; includes symétrique descender.'),
 ('06_after_faux',[400,765,820,975],0,'Curled crossed mark after faux and following colon; preceding line included.'),
 ('07_donnes',[270,850,970,1070],0,'Adjective after F-prime bowed-order F, with surrounding line.'),
 ('08_soit',[275,970,935,1150],0,'Compressed verb before induite, with line above.'),
 ('09_parenthesis_last_capital',[1350,950,1675,1155],0,'Overwritten last capital, de and closing punctuation, with line above.'),
 ('10_renforcera',[445,1135,1540,1270],0,'Peut, final verb ending and full par la suite phrase.'),
 ('11_before_c7',[275,1230,750,1370],0,'Small mark before unindexed C7, with immediate phrase.'),
 ('12_crossed_heading',[280,1465,780,1655],0,'Complete scribbled title and final numeral, including underline and next raised line.'),
 ('13_lower_overwritten_g',[1060,1465,1405,1610],0,'Capital under G in Soient F, G, including comma and deux.'),
 ('14_insertion_and_adjective',[275,1575,1070,1735],0,'Full insertion enclosure and struck adjective after Conditions.'),
 ('15_conclusion',[965,2025,1678,2175],0,'Complete parenthetic conclusion, middle word, comma and final punctuation.'),
 ('16_square',[1250,2085,1550,2305],0,'Complete four-node drawing, extra upper stroke, left cup, bottom dots and right endpoint.'),
 ('17_final_arrow',[340,2150,1155,2330],0,'Both final implications, local horizontal cancellation, final heavy arrow and C7 subscript.')
]
out=[]
for name,bbox,rotation,reason in items:
 c=ImageOps.autocontrast(im.crop(bbox))
 if rotation: c=c.rotate(rotation,Image.Resampling.BICUBIC,expand=True,fillcolor='white')
 scale=2500/c.width
 c=c.resize((2500,round(c.height*scale)),Image.Resampling.LANCZOS)
 c=ImageEnhanceSharpness(c) if False else c.filter(ImageFilter.UnsharpMask(radius=1.1,percent=110,threshold=3))
 path=root/'crops'/f'{name}.jpg'
 c.save(path,quality=94)
 out.append({'path':str(path),'source':source,'bbox':bbox,'scale':scale,'rotation':rotation,'reason':reason,'transforms':'PIL autocontrast, optional expanded rotation, LANCZOS resize to 2500 px wide, UnsharpMask radius 1.1 percent 110 threshold 3, JPEG quality 94'})
(root/'crop_manifest.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps([{'name':Path(x['path']).name,'bbox':x['bbox'],'scale':x['scale'],'rotation':x['rotation']} for x in out],indent=2))
