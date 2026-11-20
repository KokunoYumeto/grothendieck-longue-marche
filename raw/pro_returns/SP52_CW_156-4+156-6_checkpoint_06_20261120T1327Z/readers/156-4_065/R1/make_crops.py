from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json

out = Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_065/R1')
source = Path('/workspace/scratch/6644f30583f9/source/SP52_CW_156-4+156-6_scans/J156-4-08_156-4_scan065.jpg')
specs = [
    ('01_opening_deletion_parenthesis', [1225,115,1650,330], 2500, 'Opening canceled symbols and possible opening parenthesis, with next line context.'),
    ('02_question_final_F', [805,320,1155,520], 2300, 'Overwritten F and possible final subscript, with the preceding line.'),
    ('03_le_cas', [1080,505,1640,710], 2400, 'le/les before cas, with the next line.'),
    ('04_C4_symbols_and_des', [650,820,1605,1040], 2600, 'x/y/M alphabet and des/deux, with comp. connexes disjointes line.'),
    ('05_interlinear_note', [530,1095,1490,1255], 2700, 'néc abbreviation, canceled beginning and validity wording; C4 final line as context.'),
    ('06_Cor1_pres', [470,1350,1100,1570], 2500, 'Canceled start before que tout i, with preceding formula context.'),
    ('07_Cor2_heading_donc', [1090,1340,1650,1540], 2500, 'Inserted framed Cor. 2 label, deleted donc, and map; Cor. 1 line as context.'),
    ('08_Cor2_les_deux', [865,1490,1630,1690], 2500, 'les/le and deletion of deux in the Cor. 2 sentence, with preceding line.'),
    ('09_Cor2_suivants_fini', [280,1540,800,1735], 2500, 'Inserted I est and struck lower text, with preceding line.'),
    ('10_deleted_b_dash', [760,1730,1640,1900], 2500, 'The canceled b-case ending, dash or cancellation, with the next line.'),
    ('11_Cor3_figures_deletion', [1020,1800,1640,2010], 2500, 'Small canceled group after figures, with the previous and next lines.'),
    ('12_Cor3_parenthesis_Alors', [285,1850,1240,2070], 2700, 'Inserted resp. finies, canceled Alors il, and soient, with heading-line context.'),
    ('13_Cor3_same_deletion', [300,1950,1120,2140], 2500, 'Two-bar sign and following canceled group, with preceding line context.'),
    ('14_last_map', [270,2040,830,2290], 2500, 'Final family-to-product stroke, with adjacent lines.'),
    ('15_final_words', [1050,2110,1635,2315], 2500, 'l’ens punctuation and pres que spacing, with both final lines.'),
]
im = Image.open(source)
manifest=[]
for name,bbox,width,reason in specs:
    cropped=im.crop(bbox)
    cropped=ImageOps.autocontrast(cropped)
    scale=width/cropped.width
    cropped=cropped.resize((width,round(cropped.height*scale)),Image.Resampling.LANCZOS)
    cropped=cropped.filter(ImageFilter.UnsharpMask(radius=1.2,percent=110,threshold=3))
    path=out/'crops'/f'{name}.png'
    cropped.save(path)
    manifest.append(dict(path=str(path),source=str(source),bbox=bbox,scale=scale,rotation=0,reason=reason,transforms='PIL autocontrast; LANCZOS resize; UnsharpMask(radius=1.2, percent=110, threshold=3)'))
(out/'crops_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(f'Created {len(manifest)} independent crops.')
