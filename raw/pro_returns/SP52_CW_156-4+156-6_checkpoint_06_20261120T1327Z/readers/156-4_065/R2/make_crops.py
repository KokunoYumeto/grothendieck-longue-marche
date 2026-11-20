from pathlib import Path
from PIL import Image, ImageOps, ImageEnhance
import json
out=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_065/R2')
src=Path('/workspace/scratch/6644f30583f9/source/SP52_CW_156-4+156-6_scans/J156-4-08_156-4_scan065.jpg')
# Each crop is independently selected after the one whole and two half views.
items=[
 ('01_opening_correction',[1260,115,1640,330],0,'Deleted F_i and membership; possible opening parenthesis and quantifier.'),
 ('02_terminal_F',[820,330,1160,525],0,'Overwritten terminal F and possible subscript in the opening question.'),
 ('03_le_cas',[1120,500,1615,725],0,'Article before cas, with the following line as context.'),
 ('04_c4_des',[950,825,1585,1035],0,'C4 word after appartiennent à, with following line context.'),
 ('05_c4_comp',[275,955,1180,1145],0,'Possible dot after comp and spelling disjointes; following line context.'),
 ('06_interlinear_note',[510,1035,1470,1240],0,'Abbreviation néc and overwritten/cancelled beginning of validité; one preceding context line.'),
 ('07_cor1_heading',[290,1248,1120,1450],0,'Exact punctuation and underline extent at Corollaire 1, with following line.'),
 ('08_cor1_pres',[285,1360,1095,1570],0,'Cancelled pres before que tout i, with preceding line.'),
 ('09_cor2_revisions',[285,1410,1640,1730],0,'Connected Cor 2 insertion and cancellation complex, including donc, les/le, I est, suivants, and abandoned f.'),
 ('10_cancelled_cases',[320,1690,1635,1870],0,'Cancelled a and b cases; possible independent dash before alors.'),
 ('11_cor3_first_de',[1220,1765,1640,2015],0,'Cancelled word after figures, with following line.'),
 ('12_cor3_parenthesis',[765,1825,1240,2050],0,'Inserted parenthesis and cancelled Alors il, with adjacent statement line.'),
 ('13_cor3_repeat',[290,1950,895,2130],0,'Repetition/equality-like sign and cancelled word before pour, with preceding line.'),
 ('14_final_map',[270,2135,835,2320],0,'Final family-to-product separator, with following line.'),
 ('15_final_words',[1110,2098,1640,2325],0,'Punctuation after ens, spacing pres que, and final i punctuation.')
]
im=Image.open(src)
rows=[]
for name,bbox,rot,reason in items:
 c=im.crop(tuple(bbox))
 c=ImageOps.autocontrast(c,cutoff=0)
 scale=2400/c.width
 c=c.resize((2400,round(c.height*scale)),Image.Resampling.LANCZOS)
 c=ImageEnhance.Sharpness(c).enhance(1.25)
 if rot:
  c=c.rotate(rot,expand=True,fillcolor='white',resample=Image.Resampling.BICUBIC)
 p=out/'crops'/f'{name}.png'
 c.save(p)
 rows.append({'path':str(p),'source':str(src),'bbox':bbox,'scale':scale,'rotation':rot,'reason':reason})
(out/'crop_manifest.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
print(f'Created {len(rows)} independently selected crops; all source coordinates refer to whole image.')
