from pathlib import Path
from PIL import Image, ImageOps, ImageFilter, ImageChops
import csv
import json

ROOT = Path('/workspace/scratch/f28c4f52d3ec')
PAGE = '149_scan004'
image = Image.open(ROOT / 'source/SP83_C13_148+149_scans' / (PAGE + '.jpg')).convert('RGB')
with (ROOT / 'result/second' / (PAGE + '_boxes.tsv')).open(newline='') as f:
    boxes = list(csv.DictReader(f, delimiter='\t'))
manifest = []
for row in boxes:
    bounds = [int(row[k]) for k in ['x0', 'y0', 'x1', 'y1']]
    assert 0 <= bounds[0] < bounds[2] <= image.width and 0 <= bounds[1] < bounds[3] <= image.height
    crop = ImageOps.autocontrast(image.crop(bounds))
    scale = min(8, max(2, 3000 / crop.width))
    crop = crop.resize((round(crop.width * scale), round(crop.height * scale)), Image.Resampling.LANCZOS)
    crop = crop.filter(ImageFilter.UnsharpMask(radius=1.2, percent=100, threshold=3))
    path = ROOT / 'result/crops' / (PAGE + '_second_' + row['box'] + '.png')
    crop.save(path)
    item = {'box': row['box'], 'kind': row['kind'], 'original_box': bounds, 'path': str(path),
            'scale': scale, 'bytes': path.stat().st_size, 'viewed': False}
    if path.stat().st_size > 6290000:
        transport = ROOT / 'result/crops/transport' / (PAGE + '_second_' + row['box'] + '.webp')
        transport.parent.mkdir(exist_ok=True)
        crop.save(transport, lossless=True, method=4)
        assert ImageChops.difference(crop, Image.open(transport).convert('RGB')).getbbox() is None
        item.update(transport_path=str(transport), transport_pixels_identical=True)
    manifest.append(item)
(ROOT / 'result/second' / (PAGE + '_second_crop_manifest.json')).write_text(json.dumps(manifest, indent=2) + '\n')
print(json.dumps({'source_size': image.size, 'crops': manifest}, indent=2))
