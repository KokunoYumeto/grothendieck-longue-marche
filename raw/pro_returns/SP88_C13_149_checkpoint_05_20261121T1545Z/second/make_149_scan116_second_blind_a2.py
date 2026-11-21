from pathlib import Path
import csv
from PIL import Image, ImageOps

root = Path('/workspace/scratch/0cab6a548abb')
source = root / 'source/SP88_C13_149_scans/149_scan116.jpg'
boxfile = root / 'edition/second/149_scan116_boxes.tsv'
outdir = root / 'edition/crops'
outdir.mkdir(parents=True, exist_ok=True)
with boxfile.open(encoding='utf-8', newline='') as handle:
    rows = list(csv.DictReader(handle, delimiter='\t'))
with Image.open(source) as page:
    for row in rows:
        dest = outdir / f"149_scan116_second_{row['box']}.png"
        if dest.exists():
            print(f"existing {row['box']}")
            continue
        bbox = tuple(int(row[k]) for k in ('x0', 'y0', 'x1', 'y1'))
        crop = ImageOps.autocontrast(page.crop(bbox).convert('RGB'))
        scale = 3 if row['box'] in ('b02', 'b07') else 2
        crop = crop.resize((crop.width * scale, crop.height * scale), Image.Resampling.LANCZOS)
        crop.save(dest)
        print(f"created {row['box']}")

rotated = outdir / '149_scan116_second_b02_rotminus50.png'
if not rotated.exists():
    with Image.open(outdir / '149_scan116_second_b02.png') as margin_crop:
        margin_crop.rotate(-50, resample=Image.Resampling.BICUBIC, expand=True, fillcolor='white').save(rotated)
