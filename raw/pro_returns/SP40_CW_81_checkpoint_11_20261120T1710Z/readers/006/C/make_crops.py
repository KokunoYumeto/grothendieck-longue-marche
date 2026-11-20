from PIL import Image, ImageOps, ImageFilter
from pathlib import Path
import json
base = Path('/workspace/scratch/94548b74fbe0/out/readers/006/C')
source = Path('/workspace/scratch/94548b74fbe0/source/SP40_CW_81_scans/J81-01_81_scan006.jpg')
items = [
 ('u02_corrections',[230,190,615,310],0,2600,'Second quotient derivative sign and predecessor before P'),
 ('u03_denominator',[865,465,1070,585],0,2200,'Middle right quotient overwritten denominator'),
 ('u04_product',[35,550,420,665],0,3000,'Product exponent and derivative ticks'),
 ('u05_general_quotient',[55,995,210,1170],0,1600,'General quotient numerator predecessor'),
 ('u06_numerator_sign',[125,1205,500,1300],0,2800,'Cancelled cross terms and sign before Q double-prime P'),
 ('u06_first_factor',[495,1205,585,1300],0,1400,'First Q factor and its raised exponent cancellation'),
 ('u06_second_factor',[780,1205,930,1300],0,1800,'Second Q factor cancellation'),
 ('u06_denominator',[430,1320,545,1400],0,1600,'Denominator exponent crossed by opposite-layer diagonal'),
 ('u07_coefficient',[275,1460,680,1555],0,3000,'Coefficient before P prime and repeated fraction rule'),
 ('u08_fragment',[425,1575,695,1665],0,2500,'Lowercase or uppercase first squared letter and initial minus'),
 ('r01_determinant',[330,1490,1205,1670],180,3600,'Determinant row, local predecessor, separator, and terminal word'),
 ('r02_first_row',[195,1360,1110,1490],180,3600,'First delta row and cancelled ending'),
 ('r03_eta_row',[255,1250,1085,1378],180,3400,'First eta row and vertical equality'),
 ('r04_second_pair',[555,945,1115,1250],180,3000,'Second pair, local overwritten f, coefficients, and vertical equality'),
 ('r05_third_row',[30,810,1120,955],180,3600,'Third delta row and indices'),
 ('r06_ceta_row',[300,660,1080,815],180,3400,'Third eta row and etc'),
 ('r07_prose_one',[30,555,1060,667],180,3800,'Prose opening and first two products with overwritten predecessor'),
 ('r08_prose_two',[25,455,635,570],180,3000,'Continuation of product list and comme'),
 ('r09_prose_three',[30,355,1060,475],180,3800,'Abbreviations, basis indices, and coeff'),
 ('r10_prose_four',[35,280,1065,370],180,3800,'Entiers fonctions and parameter list'),
 ('r11_final_system',[395,25,1120,225],180,3600,'Final delta system, cancelled delta and coefficient predecessor')
]
manifest=[]
im=Image.open(source)
for name,bbox,rotation,width,purpose in items:
 c=im.crop(bbox)
 if rotation:
  c=c.rotate(rotation,expand=True,resample=Image.Resampling.BICUBIC,fillcolor='white')
 c=ImageOps.autocontrast(c)
 c=c.resize((width,round(c.height*width/c.width)),Image.Resampling.LANCZOS)
 c=c.filter(ImageFilter.UnsharpMask(radius=1.1,percent=120,threshold=3))
 rel=f'crops/{name}.png'
 c.save(base/rel)
 manifest.append({'path':rel,'bbox':bbox,'rotation':rotation,'purpose':purpose})
(base/'crop_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'created':len(manifest),'directory':str(base/'crops')}))
