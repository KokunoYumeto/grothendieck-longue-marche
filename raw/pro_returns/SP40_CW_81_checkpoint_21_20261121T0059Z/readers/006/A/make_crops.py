from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json
base=Path('/workspace/scratch/94548b74fbe0')
out=base/'out/readers/006/A'
source=base/'source/SP40_CW_81_scans/J81-01_81_scan006.jpg'
specs=[
('u02_second_derivative.png',[53,188,625,303],0,'Second derivative: equality, crowded sign, cancelled coefficient and open parenthesis.'),
('u03_log_quotients.png',[850,460,1074,592],0,'Both logarithmic quotients and the overwritten first denominator.'),
('u04_product.png',[42,559,373,651],0,'Product superscript and each derivative exponent across the overlap.'),
('u05_general_quotient.png',[60,1000,467,1218],0,'General quotient: overwritten numerator, equality, and denominator exponent.'),
('u06_expanded_numerator.png',[22,1194,978,1381],0,'Expanded fraction, local cancellation strokes, numerator sign and denominator exponent.'),
('u07_simplified_fraction.png',[25,1460,675,1604],0,'Following fraction: coefficient of P-prime, exact symbols and denominator.'),
('u08_lowest_fragment.png',[424,1580,687,1659],0,'Lowest fragment: p/P, leading minus before Q-prime quotient and open continuation.'),
('r01_determinant.png',[345,1502,1207,1656],180,'Half-turned determinant, cancelled extra first-cell letter, relation, and inversible.'),
('r02_first_pair.png',[206,1268,1102,1476],180,'Half-turned first pair: vertical equality, eta and cancelled terminal fragment.'),
('r03_second_pair.png',[574,946,1106,1233],180,'Half-turned second pair and overwritten predecessor before e1.'),
('r04_third_pair.png',[50,661,1104,948],180,'Half-turned third pair including first eta-like sign, vertical equality and etc.'),
('r05_prose.png',[30,278,1075,664],180,'Half-turned three-line prose, crossed coefficient list and abbreviations.'),
('r06_final_pair.png',[195,29,1108,224],180,'Half-turned last pair: s overwrite, deleted sign before x, and unfinished bound.')
]
records=[]
for name,bbox,rotation,purpose in specs:
    im=Image.open(source).crop(bbox)
    if rotation: im=im.rotate(rotation,expand=True,resample=Image.Resampling.BICUBIC,fillcolor='white')
    im=ImageOps.autocontrast(im)
    width=2800
    im=im.resize((width,round(im.height*width/im.width)),Image.Resampling.LANCZOS)
    im=im.filter(ImageFilter.UnsharpMask(radius=1.1,percent=120,threshold=3))
    im.save(out/name)
    records.append(dict(path=name,bbox=bbox,rotation=rotation,purpose=purpose))
(out/'crop_log.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(records,ensure_ascii=False,indent=2))
