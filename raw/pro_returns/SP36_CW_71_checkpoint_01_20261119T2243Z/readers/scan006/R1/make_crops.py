from pathlib import Path
from PIL import Image, ImageOps
import json
BASE = Path('/workspace/scratch/17347c1714f0')
OUT = BASE / 'out/readers/scan006/R1'
SRC = BASE / 'source/SP36_CW_71_scans'
specs = [
 ('01_script_x','a',[255,75,363,153],0,2400,'opening recurrent script X'),
 ('02_de_endings','a',[264,162,922,307],0,2800,'both de endings, first doubtful cancelled s'),
 ('03_sur','a',[969,176,1091,265],0,2400,'opening parenthesis word'),
 ('04_naturelle','a',[1217,335,1474,427],0,2600,'cancelled naturelle'),
 ('05_deleted_de','a',[825,463,933,527],0,2400,'cancelled mark preceding map'),
 ('06_operator','a',[1172,526,1426,643],0,2700,'overwritten operator before barred U'),
 ('07_index_w','a',[980,703,1230,822],0,2700,'parenthesized coproduct suffix'),
 ('08_side_display','a',[1355,678,1657,911],0,3000,'right-hand subscript, parallel strokes, Im and arrowed gloss'),
 ('09_drawing_ticks','a',[193,493,527,753],0,3000,'drawing branch strokes, ticks and labels'),
 ('10_cest_une','a',[1099,1005,1414,1075],0,2700,'sentence connective before immersion abbreviation'),
 ('11_imm','a',[437,1125,618,1192],0,2400,'abbreviation before fermée'),
 ('12_inserted_stars','b',[930,326,1255,433],0,2800,'interlinear U prime formula, tiny superscripts and insertion leader'),
 ('13_slanted_note','b',[24,394,262,712],-45,2800,'slanted verification note'),
 ('14_replacement_condition','b',[290,492,843,669],0,3000,'cancelled and inserted K condition'),
 ('15_deleted_parenthesis','b',[862,513,1143,621],0,2700,'cancelled parenthesis and raised final mark'),
 ('16_sufficiency_suffix','b',[1194,649,1598,750],0,3000,'cancelled K group, following word and K prime'),
 ('17_own_number','b',[97,1018,183,1125],0,2400,'larger freehand page numeral')
]
manifest=[]
for stem, part, box, rot, width, place in specs:
    src=SRC/f'J71-01_71_scan006_{part}.jpg'
    im=Image.open(src).convert('L').crop(box)
    im=ImageOps.autocontrast(im)
    if rot:
        im=im.rotate(rot,resample=Image.Resampling.BICUBIC,expand=True,fillcolor=255)
    pre=im.size
    height=round(im.height*width/im.width)
    im=im.resize((width,height),Image.Resampling.LANCZOS)
    target=OUT/f'{stem}.jpg'
    im.save(target,'JPEG',quality=97,optimize=True)
    manifest.append({'file':str(target),'source':str(src),'box':box,'rotation':rot,'output_width':width,'output_height':height,'scale':width/pre[0],'processing':'grayscale, autocontrast; rotation with BICUBIC only where noted; LANCZOS resize; JPEG quality 97; no sharpening','place':place,'observed':None})
(OUT/'crop_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(f'Saved {len(manifest)} crops and manifest.')
