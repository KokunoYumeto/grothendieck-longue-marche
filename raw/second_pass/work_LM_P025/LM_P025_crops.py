"""LM_P025 second pass: build labelled composite crops from the scan halves.

Usage: python LM_P025_crops.py SPEC.json
SPEC: {"out_prefix": "c", "items": [[label, scan, half, x0, y0, x1, y1, scale, rotate], ...]}
half is "" (whole page), "_a" or "_b"; coordinates are in that image's pixels.
Composites are split so that each page stays within MAXW x MAXH.
"""
import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageOps

IMG = Path(r"C:\Users\user\Documents\longue_marche_pro_pilot_20261104\second_pass\img")
OUT = Path(r"C:\Users\user\Documents\longue_marche_pro_pilot_20261104\second_pass\work_LM_P025")
MAXW, MAXH = 1600, 1550


def piece(label, scan, half, x0, y0, x1, y1, scale, rotate):
    im = Image.open(IMG / f"scan{scan}{half}.jpg").convert("L")
    im = im.crop((x0, y0, x1, y1))
    if rotate:
        im = im.rotate(rotate, resample=Image.BICUBIC, expand=True, fillcolor=255)
    im = ImageOps.autocontrast(im, cutoff=1)
    w, h = im.size
    s = scale
    if w * s > MAXW:
        s = MAXW / w
    im = im.resize((max(1, int(w * s)), max(1, int(h * s))), Image.LANCZOS)
    band = Image.new("L", (im.width, 22), 230)
    ImageDraw.Draw(band).text((4, 4), f"{label}  [scan{scan}{half} {x0},{y0}-{x1},{y1} x{s:.2f} r{rotate}]", fill=0)
    out = Image.new("L", (im.width, im.height + 22 + 6), 255)
    out.paste(band, (0, 0))
    out.paste(im, (0, 22))
    return out


def main():
    specs = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    if isinstance(specs, dict):
        specs = [specs]
    for spec in specs:
        build(spec)


def build(spec):
    prefix = spec["out_prefix"]
    pages, cur, curh = [], [], 0
    for it in spec["items"]:
        p = piece(*it)
        if cur and curh + p.height > MAXH:
            pages.append(cur)
            cur, curh = [], 0
        cur.append(p)
        curh += p.height
    if cur:
        pages.append(cur)
    for i, pg in enumerate(pages, 1):
        w = max(p.width for p in pg)
        h = sum(p.height for p in pg)
        canvas = Image.new("L", (w, h), 255)
        y = 0
        for p in pg:
            canvas.paste(p, (0, y))
            y += p.height
        name = OUT / f"{prefix}_{i}.png"
        canvas.save(name)
        print(name, canvas.size)


if __name__ == "__main__":
    main()
