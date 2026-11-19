from pathlib import Path
from PIL import Image
import json

ROOT = Path('/workspace/scratch/17347c1714f0/out/readers/scan003/R2')
SOURCE = Path('/workspace/scratch/17347c1714f0/source/SP36_CW_71_scans/J71-01_71_scan003_a.jpg')
SPECS = [
    ('01_top_overmarks.png', (205, 139, 540, 248), 0, 2800,
     'Three crowded overmarks in the second tier of the upper left table'),
    ('02_boundary_set.png', (308, 325, 518, 421), 0, 2800,
     'Small first letter in the two-point set'),
    ('03_first_identity.png', (705, 422, 1490, 510), 0, 3300,
     'First identity: initial and first primed subscripts, and terminal double-primed pair'),
    ('04_second_boundary.png', (1342, 497, 1488, 577), 0, 2800,
     'Second identity: detached mark above terminal boundary sign'),
    ('05_drawing_rotated.png', (142, 566, 438, 944), -90, 3000,
     'Quarter-turned drawing: labels, small loop marks, strokes, and endpoints'),
    ('06_beside_drawing.png', (442, 708, 684, 835), 0, 3000,
     'Expression beside drawing: cancelled superscript and crowded second double-primed subscript'),
    ('07_final_mark.png', (198, 1057, 311, 1153), 0, 2400,
     'Detached mark before the final U,C,V group'),
]

ROOT.mkdir(parents=True, exist_ok=True)
im = Image.open(SOURCE)
logs = []
for filename, box, rotation, width, place in SPECS:
    crop = im.crop(box)
    if rotation:
        crop = crop.rotate(rotation, expand=True, resample=Image.Resampling.BICUBIC)
    scale = width / crop.width
    crop = crop.resize((width, round(crop.height * scale)), Image.Resampling.LANCZOS)
    target = ROOT / filename
    crop.save(target)
    logs.append({'file': str(target), 'source': str(SOURCE), 'box': list(box),
                 'rotation': rotation, 'output_width': width, 'scale': scale,
                 'place': place})
(ROOT / 'crop_log.json').write_text(json.dumps(logs, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(logs, ensure_ascii=False, indent=2))
