from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json

ROOT = Path('/workspace/scratch/17347c1714f0/out/readers/scan003/R1')
SOURCE = Path('/workspace/scratch/17347c1714f0/source/SP36_CW_71_scans/J71-01_71_scan003_a.jpg')
SPECS = [
    ('01_borde.png', (650, 45, 1070, 142), 0, 'top middle, first verbal row; unresolved ending of borde'),
    ('02_overmarks.png', (208, 136, 540, 222), 0, 'top left, three cancelled marks over double-primed Gamma'),
    ('03_endpoint_set.png', (306, 326, 522, 414), 0, 'endpoint set, first letter'),
    ('04_first_identity.png', (708, 423, 1479, 506), 0, 'first union identity, left subscript and primed/double-primed subscripts'),
    ('05_row2_terminal.png', (1340, 497, 1481, 575), 0, 'second union identity, possible dot above terminal boundary sign'),
    ('06_drawing.png', (141, 569, 427, 941), -90, 'quarter-turned drawing, outer subscript and two marks inside endpoint loop'),
    ('07_side_identity.png', (441, 720, 678, 831), 0, 'identity beside drawing, cancelled superscript and second double-primed subscript'),
]

im = Image.open(SOURCE)
log = []
for name, box, angle, place in SPECS:
    crop = im.crop(box)
    if angle:
        crop = crop.rotate(angle, expand=True, resample=Image.Resampling.BICUBIC)
    w, h = crop.size
    width = 2800
    scale = width / w
    crop = crop.resize((width, round(h * scale)), Image.Resampling.LANCZOS)
    crop = ImageOps.autocontrast(crop, cutoff=0.1)
    crop = crop.filter(ImageFilter.UnsharpMask(radius=1.2, percent=125, threshold=3))
    output = ROOT / name
    crop.save(output)
    log.append(dict(file=str(output), source=str(SOURCE), box=list(box), rotation=angle,
                    output_width=width, scale=scale, place=place))
(ROOT / 'crop_log.json').write_text(json.dumps(log, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(log, ensure_ascii=False, indent=2))
