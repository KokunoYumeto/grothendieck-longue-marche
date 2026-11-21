from pathlib import Path
import csv
from PIL import Image, ImageOps

ROOT = Path('/workspace/scratch/0cab6a548abb')
PAGE = '149_scan105'
source = ROOT / 'source' / 'SP88_C13_149_scans' / (PAGE + '.jpg')
boxes_path = ROOT / 'edition' / 'second' / (PAGE + '_boxes.tsv')
out_dir = ROOT / 'edition' / 'crops'
out_dir.mkdir(parents=True, exist_ok=True)

with Image.open(source) as original:
    with boxes_path.open(encoding='utf-8', newline='') as f:
        for row in csv.DictReader(f, delimiter='\t'):
            bbox = tuple(int(row[k]) for k in ('x0', 'y0', 'x1', 'y1'))
            crop = original.crop(bbox)
            crop = ImageOps.autocontrast(crop.convert('RGB'))
            crop = crop.resize((crop.width * 3, crop.height * 3), Image.Resampling.LANCZOS)
            dest = out_dir / f'{PAGE}_second_{row["box"]}.png'
            crop.save(dest)
            print(f'{row["box"]}\t{bbox}\t{dest}\trotation=0\tscale=3')
