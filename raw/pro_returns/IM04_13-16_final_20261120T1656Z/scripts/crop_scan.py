#!/usr/bin/env python3
"""Create a reproducible visual crop; no OCR or text recognition is used."""
import argparse
import json
from pathlib import Path
from PIL import Image, ImageEnhance, ImageOps

p = argparse.ArgumentParser()
p.add_argument('source')
p.add_argument('output')
p.add_argument('box', nargs=4, type=int)
p.add_argument('--width', type=int, default=2800)
p.add_argument('--contrast', type=float, default=1.35)
a = p.parse_args()
im = Image.open(a.source).convert('RGB')
box = tuple(a.box)
assert 0 <= box[0] < box[2] <= im.width and 0 <= box[1] < box[3] <= im.height
cropped = im.crop(box)
cropped = ImageEnhance.Contrast(cropped).enhance(a.contrast)
cropped = cropped.resize((a.width, round(cropped.height*a.width/cropped.width)), Image.Resampling.LANCZOS)
out = Path(a.output)
out.parent.mkdir(parents=True, exist_ok=True)
cropped.save(out, quality=96, subsampling=0)
meta = {'source': Path(a.source).name, 'source_dimensions': list(im.size), 'box': list(box), 'width': a.width, 'contrast': a.contrast, 'resampling': 'Lanczos', 'output': out.name}
out.with_suffix('.crop.json').write_text(json.dumps(meta, indent=2)+'\n', encoding='utf-8')
print(json.dumps(meta))
