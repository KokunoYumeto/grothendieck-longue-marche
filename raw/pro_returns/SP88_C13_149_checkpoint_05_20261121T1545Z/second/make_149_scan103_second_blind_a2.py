from pathlib import Path
import csv
from PIL import Image, ImageOps

root = Path('/workspace/scratch/0cab6a548abb')
source = root / 'source/SP88_C13_149_scans/149_scan103.jpg'
boxes = root / 'edition/second/149_scan103_boxes.tsv'
outdir = root / 'edition/crops'
outdir.mkdir(parents=True, exist_ok=True)
with boxes.open(encoding='utf-8', newline='') as handle:
    rows = list(csv.DictReader(handle, delimiter='\t'))
with Image.open(source) as page:
    for row in rows:
        dest = outdir / f"149_scan103_second_{row['box']}.png"
        if dest.exists():
            print(f"existing {row['box']} {dest}")
            continue
        bbox = tuple(int(row[k]) for k in ('x0', 'y0', 'x1', 'y1'))
        crop = ImageOps.autocontrast(page.crop(bbox).convert('RGB'))
        scale = 3
        crop = crop.resize((crop.width * scale, crop.height * scale), Image.Resampling.LANCZOS)
        crop.save(dest)
        print(f"created {row['box']} {dest}")

# Reading aid derived from the existing crop, without re-cropping the source.
rotated = outdir / '149_scan103_second_b06_rotminus45.png'
if not rotated.exists():
    with Image.open(outdir / '149_scan103_second_b06.png') as margin_crop:
        margin_crop.rotate(-45, resample=Image.Resampling.BICUBIC, expand=True, fillcolor='white').save(rotated)

rotated_second = outdir / '149_scan103_second_b06_rotminus35.png'
if not rotated_second.exists():
    with Image.open(outdir / '149_scan103_second_b06.png') as margin_crop:
        margin_crop.rotate(-35, resample=Image.Resampling.BICUBIC, expand=True, fillcolor='white').save(rotated_second)
