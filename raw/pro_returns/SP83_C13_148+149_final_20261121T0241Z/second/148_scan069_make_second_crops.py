from pathlib import Path
from PIL import Image, ImageOps, ImageFilter, ImageChops
import csv, json

BASE = Path(__file__).resolve().parents[2]
PAGE = '148_scan069'
source = BASE / 'source' / 'SP83_C13_148+149_scans' / f'{PAGE}.jpg'
boxes_path = BASE / 'result' / 'second' / f'{PAGE}_boxes.tsv'
manifest_path = BASE / 'result' / 'second' / f'{PAGE}_second_crop_manifest.json'
if manifest_path.exists():
    raise SystemExit('Refusing to overwrite manifest')
with boxes_path.open(encoding='utf-8', newline='') as handle:
    boxes = list(csv.DictReader(handle, delimiter='\t'))
im = Image.open(source).convert('RGB')
manifest = {'page': PAGE, 'source': str(source), 'source_size': list(im.size),
            'mode': 'Independent blind second reading; no first-pass files consulted.', 'crops': []}
for row in boxes:
    coords = [int(row[k]) for k in ('x0', 'y0', 'x1', 'y1')]
    crop = ImageOps.autocontrast(im.crop(tuple(coords)))
    target = 3600 if row['box'] == 'B01' else 1000
    crop = crop.resize((target, round(crop.height * target / crop.width)), Image.Resampling.LANCZOS)
    crop = crop.filter(ImageFilter.UnsharpMask(radius=1.2, percent=100, threshold=3))
    path = BASE / 'result' / 'crops' / f'{PAGE}_second_{row["box"]}.png'
    if path.exists():
        raise SystemExit(f'Refusing to overwrite {path}')
    crop.save(path)
    entry = {'box': row['box'], 'kind': row['kind'], 'original_box': coords,
             'path': str(path), 'output_size': list(crop.size), 'rotation_degrees': 0,
             'transform': 'Exact original-coordinate crop; RGB autocontrast; LANCZOS enlargement; UnsharpMask radius1.2 percent100 threshold3.',
             'viewed': False, 'display_path': str(path)}
    if path.stat().st_size > 6000000:
        transport = BASE / 'transport' / f'{PAGE}_second_{row["box"]}.webp'
        transport.parent.mkdir(exist_ok=True)
        if transport.exists():
            raise SystemExit(f'Refusing to overwrite {transport}')
        crop.save(transport, format='WEBP', lossless=True, method=4)
        decoded = Image.open(transport).convert('RGB')
        assert decoded.size == crop.size and ImageChops.difference(crop, decoded).getbbox() is None
        entry['display_path'] = str(transport)
        entry['transport'] = 'Lossless WebP at identical dimensions; decoded pixels verified identical to canonical PNG. Display copy only.'
        entry['transport_bytes'] = transport.stat().st_size
    manifest['crops'].append(entry)
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'page': PAGE, 'source_size': list(im.size), 'crops': [{k:v for k,v in c.items() if k in ('box','path','display_path','output_size','transport_bytes')} for c in manifest['crops']]}))
