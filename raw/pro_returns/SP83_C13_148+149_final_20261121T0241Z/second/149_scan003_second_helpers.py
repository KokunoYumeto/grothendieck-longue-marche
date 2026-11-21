from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json

ROOT = Path('/workspace/scratch/f28c4f52d3ec')
PAGE = '149_scan003'
image = Image.open(ROOT / 'source/SP83_C13_148+149_scans' / (PAGE + '.jpg')).convert('RGB')
specs = [
    ('B01_mark', 'B01', [1150, 35, 1210, 85], 12),
    ('B03_deleted', 'B03', [1100, 870, 1280, 990], 8),
    ('B03_formula', 'B03', [1000, 750, 1640, 890], 4),
    ('B04_ending', 'B04', [280, 1420, 1665, 1560], 3),
    ('B05_word', 'B05', [1080, 1520, 1640, 1655], 5),
    ('B06_formula', 'B06', [410, 2110, 720, 2202], 6),
    ('B04_deleted', 'B04', [570, 1190, 840, 1320], 6),
    ('B06_word', 'B06', [445, 2000, 775, 2100], 6),
]
parents = {
    'B01': [260, 22, 1225, 155], 'B03': [280, 650, 1665, 1025],
    'B04': [280, 970, 1665, 1560], 'B05': [280, 1495, 1640, 1785],
    'B06': [280, 1990, 1660, 2202],
}
manifest = []
for name, parent, bounds, scale in specs:
    p = parents[parent]
    assert p[0] <= bounds[0] < bounds[2] <= p[2] and p[1] <= bounds[1] < bounds[3] <= p[3]
    crop = ImageOps.autocontrast(image.crop(bounds))
    crop = crop.resize((crop.width * scale, crop.height * scale), Image.Resampling.LANCZOS)
    crop = crop.filter(ImageFilter.UnsharpMask(radius=1.2, percent=90, threshold=3))
    path = ROOT / 'result/crops' / (PAGE + '_second_' + name + '.png')
    crop.save(path)
    manifest.append({'helper': name, 'parent_box': parent, 'original_box': bounds,
                     'scale': scale, 'path': str(path), 'viewed': False,
                     'purpose': 'Independent same-box detail; no extension outside prescribed audit rectangle.'})
(ROOT / 'result/second' / (PAGE + '_second_helper_manifest.json')).write_text(json.dumps(manifest, indent=2) + '\n')
print('\n'.join(m['path'] for m in manifest))
