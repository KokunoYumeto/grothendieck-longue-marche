from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json

source = Path('/workspace/scratch/94548b74fbe0/source/SP40_CW_81_scans/J81-01_81_scan005.jpg')
out = Path('/workspace/scratch/94548b74fbe0/out/readers/005/B')
specs = [
    ('crops/01_automorphisme.png', [560, 60, 1150, 180], 'Line 1: C doubt automorphisme'),
    ('crops/02_egalmt.png', [830, 245, 1198, 368], 'Line 3: contracted word after f sigma est; raised sigma in context'),
    ('crops/03_opere.png', [645, 354, 1165, 465], 'Line 4: presence or absence of accent in opere; Aut(C) in context'),
    ('crops/04_speciaux.png', [440, 460, 790, 578], 'Line 5: accent direction in special plural'),
    ('crops/05_barred_Q.png', [120, 675, 430, 797], 'Line 7: alphabet and bar on Q in Aut'),
    ('crops/06_coeff.png', [275, 770, 470, 916], 'Line 8: abbreviation punctuation and faint lower stroke at coeff.'),
    ('crops/07_sont.png', [745, 790, 940, 895], 'Line 8: crowded strokes in sont, possible cancellation'),
    ('crops/08_revient.png', [665, 895, 1205, 993], 'Line 9: C doubt revient, with au = de context'),
    ('crops/09_first_isolated_mark.png', [325, 1382, 480, 1460], 'First isolated lower mark: dark lower bar and faint upper bar'),
    ('crops/10_faint_detached_mark.png', [825, 1235, 905, 1300], 'Faint detached mark below diviseur: ink or surface/impression'),
]
im = Image.open(source)
records = []
for name, bbox, purpose in specs:
    crop = ImageOps.autocontrast(im.crop(tuple(bbox)))
    width = 2600 if bbox[2] - bbox[0] >= 250 else 2200
    crop = crop.resize((width, round(crop.height * width / crop.width)), Image.Resampling.LANCZOS)
    crop = crop.filter(ImageFilter.UnsharpMask(radius=1.1, percent=120, threshold=3))
    dest = out / name
    dest.parent.mkdir(parents=True, exist_ok=True)
    crop.save(dest)
    records.append({'path':name,'bbox':{'coordinate_system':'original full scan','xyxy':bbox},'rotation':0,'purpose':purpose})
(out / 'crop_manifest.json').write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(records, ensure_ascii=False, indent=2))
