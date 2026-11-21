import csv
import json
from pathlib import Path
from PIL import Image, ImageOps, ImageFilter

BASE = Path('/workspace/scratch/f28c4f52d3ec')
PAGE = '148_scan062'
source = BASE / f'source/SP83_C13_148+149_scans/{PAGE}.jpg'
with (BASE / f'result/second/{PAGE}_boxes.tsv').open(newline='') as stream:
    boxes = list(csv.DictReader(stream, delimiter='\t'))
image = Image.open(source).convert('RGB')
manifest = {'page': PAGE, 'source': str(source), 'source_size': list(image.size), 'mode': 'Independent blind second reading; no first-pass files consulted.', 'crops': []}
rotations = {'B08': -25, 'B11': -32}
for row in boxes:
    box = tuple(int(row[k]) for k in ('x0', 'y0', 'x1', 'y1'))
    crop = ImageOps.autocontrast(image.crop(box))
    width = crop.width
    if row['box'] in rotations:
        out_width = 2600
    elif width < 120:
        out_width = 1200
    elif width < 350:
        out_width = 2400
    elif width < 700:
        out_width = 3300
    else:
        out_width = 4200
    enlarged = crop.resize((out_width, round(crop.height * out_width / crop.width)), Image.Resampling.LANCZOS)
    enlarged = enlarged.filter(ImageFilter.UnsharpMask(radius=1.2, percent=110, threshold=3))
    rotation = rotations.get(row['box'], 0)
    if rotation:
        enlarged = enlarged.rotate(rotation, Image.Resampling.BICUBIC, expand=True, fillcolor=(255,255,255))
    output = BASE / f'result/crops/{PAGE}_second_{row["box"]}.png'
    if output.exists():
        raise FileExistsError(output)
    enlarged.save(output, optimize=True)
    manifest['crops'].append({'box': row['box'], 'kind': row['kind'], 'original_box': list(box), 'path': str(output), 'output_size': list(enlarged.size), 'rotation_degrees': rotation, 'transform': 'Exact original-coordinate crop; RGB autocontrast; LANCZOS enlargement; UnsharpMask radius1.2 percent110 threshold3; stated rotations use bicubic interpolation and expanded white canvas.', 'viewed': False})
output = BASE / f'result/second/{PAGE}_second_crop_manifest.json'
with output.open('x') as stream:
    json.dump(manifest, stream, ensure_ascii=False, indent=2)
    stream.write('\n')
print(json.dumps({'page': PAGE, 'count': len(boxes), 'source_size': list(image.size), 'largest_png_bytes': max(Path(c['path']).stat().st_size for c in manifest['crops']), 'manifest': str(output)}))
