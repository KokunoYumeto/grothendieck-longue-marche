from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import csv
import json

BASE = Path(__file__).resolve().parents[2]
PAGE = '148_scan064'
source = BASE / 'source' / 'SP83_C13_148+149_scans' / f'{PAGE}.jpg'
box_path = BASE / 'result' / 'second' / f'{PAGE}_boxes.tsv'
manifest_path = BASE / 'result' / 'second' / f'{PAGE}_second_crop_manifest.json'
if manifest_path.exists():
    raise SystemExit('Refusing to overwrite current crop manifest')
with box_path.open(encoding='utf-8', newline='') as handle:
    boxes = list(csv.DictReader(handle, delimiter='\t'))
im = Image.open(source).convert('RGB')
manifest = {'page': PAGE, 'source': str(source), 'source_size': list(im.size),
            'mode': 'Independent blind second reading; no first-pass files consulted.', 'crops': []}
for row in boxes:
    coords = [int(row[key]) for key in ('x0', 'y0', 'x1', 'y1')]
    crop = ImageOps.autocontrast(im.crop(tuple(coords)))
    width = coords[2] - coords[0]
    rotation = -20 if row['box'] == 'B18' else 0
    target = 2200 if rotation else (1200 if width < 120 else (2400 if width < 350 else (3300 if width < 700 else 4200)))
    scale = target / crop.width
    crop = crop.resize((target, round(crop.height * scale)), Image.Resampling.LANCZOS)
    crop = crop.filter(ImageFilter.UnsharpMask(radius=1.2, percent=110, threshold=3))
    if rotation:
        crop = crop.rotate(rotation, Image.Resampling.BICUBIC, expand=True, fillcolor='white')
    path = BASE / 'result' / 'crops' / f'{PAGE}_second_{row["box"]}.png'
    if path.exists():
        raise SystemExit(f'Refusing to overwrite {path}')
    crop.save(path)
    manifest['crops'].append({'box': row['box'], 'kind': row['kind'], 'original_box': coords,
        'path': str(path), 'output_size': list(crop.size), 'rotation_degrees': rotation,
        'transform': 'Exact original-coordinate crop; RGB autocontrast; LANCZOS enlargement; UnsharpMask radius1.2 percent110 threshold3; stated rotation uses bicubic interpolation and expanded white canvas.',
        'viewed': False})
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'page': PAGE, 'crop_count': len(manifest['crops']), 'source_size': list(im.size)}))
