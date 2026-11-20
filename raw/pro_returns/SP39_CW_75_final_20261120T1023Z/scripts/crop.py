#!/usr/bin/env python3
"""Create a reproducible inspection crop. Does not recognize text.

Usage: crop.py SOURCE OUTPUT MANIFEST X0 Y0 X1 Y1 [WIDTH=2800] [ROTATE=0]
Bounds refer to the supplied whole-page image, measured from upper left.
"""
from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
from datetime import datetime, timezone
import csv, sys

source, output, manifest = map(Path, sys.argv[1:4])
box = tuple(map(int, sys.argv[4:8]))
width = int(sys.argv[8]) if len(sys.argv) > 8 else 2800
rotation = float(sys.argv[9]) if len(sys.argv) > 9 else 0.0
im = Image.open(source)
assert 0 <= box[0] < box[2] <= im.width and 0 <= box[1] < box[3] <= im.height
crop = im.crop(box)
if rotation:
    crop = crop.rotate(rotation, Image.Resampling.BICUBIC, expand=True, fillcolor='white')
crop = ImageOps.autocontrast(crop)
crop = crop.resize((width, round(crop.height * width / crop.width)), Image.Resampling.LANCZOS)
crop = crop.filter(ImageFilter.UnsharpMask(radius=1.0, percent=130, threshold=3))
output.parent.mkdir(parents=True, exist_ok=True)
assert not output.exists(), f'Crop already exists: {output}; reuse it rather than recropping.'
crop.save(output)
manifest.parent.mkdir(parents=True, exist_ok=True)
new = not manifest.exists()
with manifest.open('a', newline='') as f:
    w = csv.writer(f, delimiter='\t')
    if new:
        w.writerow(['crop', 'source', 'x0', 'y0', 'x1', 'y1', 'output_width', 'rotation_degrees', 'processing', 'utc'])
    w.writerow([output.name, source.name, *box, width, rotation, 'autocontrast; LANCZOS; UnsharpMask(1.0,130,3)', datetime.now(timezone.utc).isoformat(timespec='seconds')])
print(str(output))
