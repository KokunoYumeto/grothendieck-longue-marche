from PIL import Image, ImageOps, ImageFilter
from pathlib import Path
import json
root=Path('/workspace/scratch/94548b74fbe0/out/readers/006/B')
im=Image.open('/workspace/scratch/94548b74fbe0/source/SP40_CW_81_scans/J81-01_81_scan006.jpg')
items=[
('01_second_derivative',(50,190,625,300),0,'overwritten sign before 2 and predecessor before P('),
('02_log_derivative',(864,461,1078,593),0,'overwritten first denominator'),
('03_product_rule',(36,566,422,663),0,'product superscript and three local derivative exponents'),
('04_general_quotient',(62,1002,451,1203),0,'overwritten numerator and denominator exponent'),
('05_expanded_quotient',(24,1201,983,1393),0,'local cancellations, sign and denominator exponent'),
('06_simplified_quotient',(20,1464,680,1607),0,'coefficient before P prime and lower extent'),
('07_final_minus',(542,1597,692,1662),0,'short horizontal before Q prime over Q'),
('08_determinant',(260,1528,1205,1658),180,'determinant overwritten cell, following sign and word'),
('09_first_delta',(204,1363,1098,1472),180,'first delta line and struck terminal writing'),
('10_aeta',(250,1267,1061,1366),180,'a eta delta line, coefficients and indices'),
('11_second_delta',(578,1100,1106,1239),180,'second delta line overwritten e and product punctuation'),
('12_ceta',(310,674,1088,812),180,'c eta line and nearby etc'),
('13_prose_first',(300,572,1027,663),180,'On en tire first products and overwritten f'),
('14_prose_list',(31,473,637,574),180,'continued product list and comme'),
('15_prose_abbreviations',(33,369,1069,475),180,'comb. lin, indices and coeff'),
('16_prose_last',(47,284,1089,369),180,'entiers fonctions and parameter list'),
('17_final_delta',(194,138,1107,218),180,'delta e1 xi line, overwritten delta and incomplete bound'),
('18_final_coefficients',(548,30,1110,146),180,'overwritten coefficient and final linear expression'),
]
records=[]
for name,bbox,rot,purpose in items:
 crop=im.crop(bbox)
 if rot: crop=crop.rotate(rot,expand=True,resample=Image.Resampling.BICUBIC,fillcolor='white')
 crop=ImageOps.autocontrast(crop)
 width=2600 if bbox[2]-bbox[0]>450 else 1800
 crop=crop.resize((width,round(crop.height*width/crop.width)),Image.Resampling.LANCZOS)
 crop=crop.filter(ImageFilter.UnsharpMask(radius=1.1,percent=120,threshold=3))
 path='crops/'+name+'.png'
 crop.save(root/path)
 records.append({'path':path,'bbox':list(bbox),'rotation':rot,'purpose':purpose})
(root/'crops.json').write_text(json.dumps(records,indent=2),encoding='utf-8')
print(json.dumps(records,indent=2))
