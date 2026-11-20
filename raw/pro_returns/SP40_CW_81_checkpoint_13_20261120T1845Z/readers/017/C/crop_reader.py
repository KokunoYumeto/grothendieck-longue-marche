from pathlib import Path
import json
from PIL import Image, ImageOps

ROOT = Path('/workspace/scratch/94548b74fbe0')
DEST = ROOT / 'out/readers/017/C'
SOURCE = ROOT / 'source/SP40_CW_81_scans/J81-02_81_scan017.jpg'
PLAN = [
    ('crop01_opening.png', (1020, 175, 1675, 345), 0, 'Cancelled first clause and parenthetical opening; source doubt row 1.'),
    ('crop02_cancelled_sentence.png', (260, 275, 980, 440), 0, 'Cancelled sentence; source doubt row 2, including complete que descender.'),
    ('crop03_equalities.png', (535, 400, 1215, 610), 0, 'Upper equality punctuation and detached right-side small mark.'),
    ('crop04_join.png', (525, 730, 1240, 855), 0, 'Overdrawn first join in third equality; source doubt row 3.'),
    ('crop05_margin.png', (20, 925, 325, 1325), -45, 'Complete angled marginal note, its partition letter and cancelled predecessor; source doubt row 4.'),
    ('crop06_old_sigma.png', (1240, 1255, 1600, 1410), 0, 'Earlier overwritten E_j/Sigma glyph and adjacent condition; source doubt row 7a.'),
    ('crop07_intersection.png', (305, 1390, 850, 1510), 0, 'Cancelled opening and live intersection strokes; source doubt row 6.'),
    ('crop08_late_cancel.png', (1030, 1485, 1450, 1620), 0, 'Later cancelled isolated sign after E_j; source doubt row 7b.'),
    ('crop09_display_marks.png', (1090, 1600, 1620, 1770), 0, 'Detached right-side small marks with neighbouring display context.'),
    ('crop10_pi_union.png', (735, 1935, 1320, 2100), 0, 'First raised partition ring and possibly barred union; source doubt rows 8a and 11.'),
    ('crop11_binary.png', (1055, 2045, 1575, 2210), 0, 'Binary partition ring/indices and inserted condition guide; source doubt row 8b.'),
    ('crop12_U.png', (305, 2120, 815, 2350), 0, 'Inserted U subscript correction and guide, with full lower endpoints; source doubt row 12.'),
    ('crop13_end.png', (1100, 2195, 1669, 2350), 0, 'Last quantified letter, closing punctuation and final word; source doubt rows 9 and 10.'),
]

DEST.mkdir(parents=True, exist_ok=True)
log = []
with Image.open(SOURCE) as source:
    for name, box, rotation, purpose in PLAN:
        cropped = source.crop(box).convert('RGB')
        cropped = ImageOps.autocontrast(cropped)
        if rotation:
            cropped = cropped.rotate(rotation, resample=Image.Resampling.BICUBIC, expand=True, fillcolor='white')
        before = cropped.size
        enlarged = cropped.resize((before[0] * 4, before[1] * 4), Image.Resampling.LANCZOS)
        enlarged.save(DEST / name)
        log.append({'path': name, 'source': str(SOURCE), 'bbox': list(box), 'coordinate_origin': 'full scan, top-left; right/bottom exclusive', 'rotation': rotation, 'rotation_resampling': 'BICUBIC' if rotation else None, 'autocontrast': True, 'sharpening': False, 'scale': 4, 'pre_resize_size': list(before), 'output_size': list(enlarged.size), 'purpose': purpose})
(DEST / 'crop_log.json').write_text(json.dumps(log, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(log, ensure_ascii=False))
