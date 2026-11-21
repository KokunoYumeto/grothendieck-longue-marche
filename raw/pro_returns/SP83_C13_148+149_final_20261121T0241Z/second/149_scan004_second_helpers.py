from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import csv
import json

ROOT = Path('/workspace/scratch/f28c4f52d3ec')
PAGE = '149_scan004'
im = Image.open(ROOT / 'source/SP83_C13_148+149_scans' / (PAGE + '.jpg')).convert('RGB')
with (ROOT / 'result/second' / (PAGE + '_boxes.tsv')).open(newline='') as f:
    parents = {r['box']: [int(r[k]) for k in ['x0', 'y0', 'x1', 'y1']] for r in csv.DictReader(f, delimiter='\t')}
specs = [
    ('B02_index', 'B02', [925, 390, 980, 450], 12),
    ('B03_number', 'B03', [275, 635, 345, 685], 10),
    ('B03_index', 'B03', [1035, 620, 1085, 675], 12),
    ('B04_oldword', 'B04', [1400, 735, 1640, 825], 6),
    ('B04_article', 'B04', [1130, 730, 1440, 850], 6),
    ('B04_abbrev', 'B04', [1175, 855, 1630, 960], 5),
    ('B04_closing', 'B04', [845, 975, 970, 1070], 8),
    ('B04_insertion', 'B04', [1310, 920, 1650, 1075], 5),
    ('B05_parenthesis', 'B05', [1295, 1085, 1620, 1175], 6),
    ('B05_replacement', 'B05', [875, 1160, 1110, 1295], 8),
    ('B05_index', 'B05', [545, 1180, 640, 1290], 8),
    ('B06_points', 'B06', [770, 1340, 945, 1430], 8),
    ('B06_lastline', 'B06', [280, 1545, 1630, 1665], 3),
    ('B07_number', 'B07', [290, 1800, 360, 1845], 12),
    ('B07_indices', 'B07', [1015, 1730, 1220, 1830], 8),
    ('B09_mark', 'B09', [290, 2200, 335, 2290], 10),
    ('B09_reference', 'B09', [820, 2170, 915, 2255], 8),
    ('B09_end', 'B09', [1240, 2240, 1678, 2345], 5),
]
manifest = []
for name, parent, bounds, scale in specs:
    p = parents[parent]
    assert p[0] <= bounds[0] < bounds[2] <= p[2] and p[1] <= bounds[1] < bounds[3] <= p[3]
    crop = ImageOps.autocontrast(im.crop(bounds))
    crop = crop.resize((crop.width * scale, crop.height * scale), Image.Resampling.LANCZOS)
    crop = crop.filter(ImageFilter.UnsharpMask(radius=1.2, percent=90, threshold=3))
    path = ROOT / 'result/crops' / (PAGE + '_second_' + name + '.png')
    crop.save(path)
    manifest.append({'helper': name, 'parent_box': parent, 'original_box': bounds,
                     'scale': scale, 'path': str(path), 'viewed': False,
                     'purpose': 'Same-box independent detail; no added source area outside prescribed rectangle.'})
(ROOT / 'result/second' / (PAGE + '_second_helper_manifest.json')).write_text(json.dumps(manifest, indent=2) + '\n')
print(json.dumps({'helper_count': len(manifest), 'names': [r['helper'] for r in manifest]}, indent=2))
