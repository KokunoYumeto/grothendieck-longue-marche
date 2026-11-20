#!/usr/bin/env python3
"""Create an explicitly located, enlarged facsimile crop; no OCR is used."""
import argparse, json
from pathlib import Path
from datetime import datetime, timezone
from PIL import Image, ImageEnhance

p = argparse.ArgumentParser()
p.add_argument('source')
p.add_argument('output')
p.add_argument('box', nargs=4, type=int)
p.add_argument('--width', type=int, default=2400)
p.add_argument('--contrast', type=float, default=1.25)
a = p.parse_args()
im = Image.open(a.source)
box = tuple(a.box)
assert 0 <= box[0] < box[2] <= im.width and 0 <= box[1] < box[3] <= im.height
crop = im.crop(box)
crop = ImageEnhance.Contrast(crop).enhance(a.contrast)
crop = crop.resize((a.width, round(crop.height * a.width / crop.width)), Image.Resampling.LANCZOS)
out = Path(a.output)
out.parent.mkdir(parents=True, exist_ok=True)
crop.save(out)
meta = {'source': Path(a.source).name, 'source_size': list(im.size), 'box_xyxy': list(box), 'output': out.name, 'output_size': list(crop.size), 'contrast_factor': a.contrast, 'resampling': 'LANCZOS', 'created_utc': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}
out.with_suffix('.json').write_text(json.dumps(meta, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(meta))
