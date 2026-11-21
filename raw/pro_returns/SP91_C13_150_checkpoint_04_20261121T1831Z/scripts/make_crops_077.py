from PIL import Image,ImageOps
from pathlib import Path
import json,os
r=Path('/workspace/scratch/b12af914b284'); im=Image.open(r/'input/SP91_C13_150_scans/150_scan077.jpg').convert('RGB')
items=[
('p00_numbers',[40,20,344,133],'Author34 and underlined item15, punctuation',0),
('p01_title',[395,45,1215,145],'proespaces/provoisinages and title underline scope',0),
('p02_title_formula',[1211,21,1568,151],'Full heading formula, zero indices, final raised overwritten group M0649',0),
('p03_designation',[780,159,1290,283],'V_i exponent M0650, le state M0651, raised pro and attachment',0),
('p04_sens',[234,281,1002,380],'au sens des proespaces/provoisinages parenthesis',0),
('p05_x_definition',[1121,269,1545,403],'Full X star complement formula',0),
('p06_ainsi',[592,399,1064,481],'Ainsi cancelled on and live on a omitted by H',0),
('p07_formula51',[231,473,1030,617],'Whole map51, number, endpoint and exponent M0652',0),
('p08_homotopy',[1171,490,1678,657],'Wrapped equivalence caption, de/des and proespaces/provoisinages',0),
('p09_struck_si',[334,676,1040,833],'Cancelled Pour un drapeau and live Si i<j on pose',0),
('p10_formula52',[231,827,1113,980],'Whole formula52, number and overwritten X/V group',0),
('p11_left_margin',[24,799,454,1287],'Whole oblique Pourquoi note, formula and question M0653-55',-44),
('p12_right_nb',[1280,753,1669,1261],'Right NB full text/formulas, cancelled si and empty glyph',0),
('p13_right_insert',[1280,1091,1670,1489],'Inserted du moins parenthesis and entire attachment arrow',0),
('p14_diagram',[512,1088,1164,1509],'Whole diagram, all endpoints/labels, lower parenthesis/map M0656',0),
('p15_formula53',[232,1601,1374,1771],'Whole formula53, handwritten53 and overwritten sign M0657',0),
('p16_caption',[267,1753,1566,2017],'Recollement sentence, all V glyphs and underline',0),
('p17_formula54',[233,2102,1235,2279],'Whole formula54, number, indices0/n, continuation marks and last V retracing',0),
('p18_flag',[264,2258,1274,2359],'Last main line flag, zero/one indices and continuation strokes',0),
('p19_bottom_margin',[1270,2047,1678,2359],'Whole oblique bottom NB; M0658 M0659 and all lexical differences',-25),
('p20_folio',[19,2300,91,2350],'Pale other-hand folio76',0)
]
m={'scan':'077','size':list(im.size),'crops':[]}
for n,b,p,rot in items:
 c=ImageOps.autocontrast(im.crop(b))
 if rot:c=c.rotate(rot,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
 c=c.resize((2400,round(2400*c.height/c.width)),Image.Resampling.LANCZOS)
 f='crops/150_scan077_'+n+'.png';c.save(r/'edition'/f)
 m['crops'].append({'file':f,'box':b,'purpose':p,'rotation':rot})
p=r/'edition/scripts/150_scan077_crop_index.json';t=p.with_suffix('.json.tmp');t.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n');os.replace(t,p)
print(p);print('crops',len(items))
