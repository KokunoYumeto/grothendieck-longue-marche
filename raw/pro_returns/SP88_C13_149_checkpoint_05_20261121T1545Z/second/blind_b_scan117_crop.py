from pathlib import Path
import csv
from PIL import Image, ImageOps

ROOT = Path('/workspace/scratch/0cab6a548abb')
PAGE = '149_scan117'
out_dir = ROOT / 'edition' / 'crops'
out_dir.mkdir(parents=True, exist_ok=True)
with Image.open(ROOT / 'source' / 'SP88_C13_149_scans' / f'{PAGE}.jpg') as original:
    with (ROOT / 'edition' / 'second' / f'{PAGE}_boxes.tsv').open(encoding='utf-8', newline='') as f:
        for row in csv.DictReader(f, delimiter='\t'):
            bbox = tuple(int(row[k]) for k in ('x0', 'y0', 'x1', 'y1'))
            crop = ImageOps.autocontrast(original.crop(bbox).convert('RGB'))
            crop = crop.resize((crop.width * 3, crop.height * 3), Image.Resampling.LANCZOS)
            dest = out_dir / f'{PAGE}_second_{row["box"]}.png'
            crop.save(dest)
            print(f'{row["box"]}\t{bbox}\t{dest}\trotation=0\tscale=3')
