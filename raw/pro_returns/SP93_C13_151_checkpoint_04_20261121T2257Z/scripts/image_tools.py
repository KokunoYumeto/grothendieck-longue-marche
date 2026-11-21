"""Deterministic image preparation only; no OCR or text recognition."""
from pathlib import Path
import argparse
import json
from PIL import Image, ImageOps, ImageFilter

ROOT = Path('/workspace/scratch/d12e26a9cd50')

def original(scan):
    return ROOT / 'source/SP93_C13_151_scans' / f'151_scan{int(scan):03d}.jpg'

def halves(scan):
    name = f'151_scan{int(scan):03d}'
    im = Image.open(original(scan))
    w, h = im.size
    if w > h:
        boxes = [(0, 0, round(w * .55), h), (round(w * .45), 0, w, h)]
        labels = ['left', 'right']
    else:
        boxes = [(0, 0, w, round(h * .55)), (0, round(h * .45), w, h)]
        labels = ['top', 'bottom']
    for box, label in zip(boxes, labels):
        p = ROOT / 'reading_work/halves' / f'{name}_{label}.png'
        if not p.exists():
            im.crop(box).save(p)
        print(json.dumps({'file': str(p), 'box': box, 'size': im.crop(box).size}))

def crop(scan, identifier, box, rotate=0, width=2400, second=False):
    im = Image.open(original(scan))
    if not (0 <= box[0] < box[2] <= im.width and 0 <= box[1] < box[3] <= im.height):
        raise ValueError(f'Invalid box {box} for {im.size}')
    target = ROOT / 'SP93_C13_151_work/crops' / f'151_scan{int(scan):03d}_{identifier}.png'
    if target.exists():
        raise FileExistsError(f'Reuse the already saved crop: {target}')
    clipped = im.crop(box)
    if rotate:
        clipped = clipped.rotate(rotate, resample=Image.Resampling.BICUBIC, expand=True, fillcolor='white')
    clipped = ImageOps.autocontrast(clipped)
    clipped = clipped.resize((width, max(1, round(clipped.height * width / clipped.width))), Image.Resampling.LANCZOS)
    clipped = clipped.filter(ImageFilter.UnsharpMask(radius=1.2, percent=110, threshold=3))
    clipped.save(target)
    print(json.dumps({'file': str(target), 'box': box, 'rotation': rotate, 'size': clipped.size}))

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest='mode', required=True)
    h = sub.add_parser('halves'); h.add_argument('scan')
    c = sub.add_parser('crop'); c.add_argument('scan'); c.add_argument('identifier')
    c.add_argument('box', type=int, nargs=4); c.add_argument('--rotate', type=float, default=0)
    c.add_argument('--width', type=int, default=2400)
    a = p.parse_args()
    if a.mode == 'halves': halves(a.scan)
    else: crop(a.scan, a.identifier, a.box, a.rotate, a.width)
