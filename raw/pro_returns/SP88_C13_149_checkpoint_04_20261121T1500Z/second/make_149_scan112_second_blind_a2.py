from pathlib import Path
import csv
from PIL import Image, ImageOps

root = Path('/workspace/scratch/0cab6a548abb')
source = root / 'source/SP88_C13_149_scans/149_scan112.jpg'
boxfile = root / 'edition/second/149_scan112_boxes.tsv'
outdir = root / 'edition/crops'
outdir.mkdir(parents=True, exist_ok=True)
with boxfile.open(encoding='utf-8', newline='') as handle:
    rows = list(csv.DictReader(handle, delimiter='\t'))
with Image.open(source) as page:
    for row in rows:
        dest = outdir / f"149_scan112_second_{row['box']}.png"
        if dest.exists():
            print(f"existing {row['box']}")
            continue
        bbox = tuple(int(row[k]) for k in ('x0', 'y0', 'x1', 'y1'))
        crop = ImageOps.autocontrast(page.crop(bbox).convert('RGB'))
        scale = 3 if row['box'] == 'b15' else 2
        crop = crop.resize((crop.width * scale, crop.height * scale), Image.Resampling.LANCZOS)
        crop.save(dest)
        print(f"created {row['box']}")
