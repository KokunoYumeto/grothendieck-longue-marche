"""Re-encode an existing image for display; never resample or crop pixels.

Canonical evidence remains in crops/. These temporary display encodings stay
outside the deliverable tree. Pixel equality is asserted after encoding.
"""
from pathlib import Path
from PIL import Image, ImageChops
from concurrent.futures import ThreadPoolExecutor
import sys, json

ROOT = Path(__file__).resolve().parents[2]
DEST = ROOT / 'transport'
DEST.mkdir(exist_ok=True)

def encode(name):
    p = Path(name)
    if not p.is_absolute():
        p = ROOT / p
    im = Image.open(p).convert('RGB')
    out = DEST / (p.stem + '.webp')
    if not out.exists():
        tmp = out.with_suffix('.working.webp')
        im.save(tmp, 'WEBP', lossless=True, quality=100, method=4)
        assert ImageChops.difference(im, Image.open(tmp).convert('RGB')).getbbox() is None
        tmp.rename(out)
    else:
        assert ImageChops.difference(im, Image.open(out).convert('RGB')).getbbox() is None
    result = {'source': str(p.relative_to(ROOT)), 'display': str(out.relative_to(ROOT)),
              'size': im.size, 'bytes': out.stat().st_size, 'pixel_identical': True}
    print(json.dumps(result), flush=True)
    return result

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=3) as pool:
        list(pool.map(encode, sys.argv[1:]))
