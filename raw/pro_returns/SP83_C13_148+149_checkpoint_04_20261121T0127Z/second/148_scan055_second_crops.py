"""Generate exact independent audit crops; no first-reading input is used."""
import csv
import json
from pathlib import Path
from PIL import Image, ImageOps, ImageFilter

BASE = Path('/workspace/scratch/f28c4f52d3ec')
PAGE = '148_scan055'
source = BASE / 'source/SP83_C13_148+149_scans' / f'{PAGE}.jpg'
boxes = BASE / 'result/second' / f'{PAGE}_boxes.tsv'
with boxes.open(newline='') as f:
    rows = list(csv.DictReader(f, delimiter='\t'))
im = Image.open(source).convert('RGB')
manifest = []
for row in rows:
    bounds = tuple(int(row[k]) for k in ('x0','y0','x1','y1'))
    crop = ImageOps.autocontrast(im.crop(bounds))
    scale = min(8, max(2, 3000 / crop.width))
    crop = crop.resize((round(crop.width*scale),round(crop.height*scale)),Image.Resampling.LANCZOS)
    crop = crop.filter(ImageFilter.UnsharpMask(radius=1.2,percent=100,threshold=3))
    dst = BASE / 'result/crops' / f"{PAGE}_second_{row['box']}.png"
    crop.save(dst)
    manifest.append({'box': row['box'], 'kind': row['kind'], 'original_box': list(bounds),
                     'path': str(dst), 'relative_path': f'crops/{dst.name}', 'scale': scale,
                     'bytes': dst.stat().st_size, 'viewed': False,
                     'needs_transport': dst.stat().st_size > 6290000})
(BASE/'result/second'/f'{PAGE}_second_crop_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'source_size': im.size, 'crop_count': len(manifest), 'crops': manifest},indent=2))
