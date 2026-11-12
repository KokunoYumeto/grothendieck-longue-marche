"""LM_P013_crop.py -- crop and enlarge regions of scan images into one montage.

Usage:
  python LM_P013_crop.py OUT.png SPEC [SPEC ...]
SPEC = imgname:x0,y0,x1,y1[:scale[:rot]]
  imgname relative to second_pass/img (e.g. scan121_a.jpg); coordinates in that image's pixels;
  scale default 2.0; rot = degrees counter-clockwise (optional).
Crops are stacked vertically, each preceded by a thin label bar.
"""
import sys
import os
from PIL import Image, ImageDraw, ImageOps

IMG_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "img")


def main():
    out = sys.argv[1]
    specs = sys.argv[2:]
    tiles = []
    for spec in specs:
        parts = spec.split(":")
        name = parts[0]
        box = tuple(int(v) for v in parts[1].split(","))
        scale = float(parts[2]) if len(parts) > 2 and parts[2] else 2.0
        rot = float(parts[3]) if len(parts) > 3 else 0.0
        im = Image.open(os.path.join(IMG_DIR, name)).convert("L")
        c = im.crop(box)
        if rot:
            c = c.rotate(rot, expand=True, fillcolor=255)
        c = c.resize((max(1, int(c.width * scale)), max(1, int(c.height * scale))), Image.LANCZOS)
        c = ImageOps.autocontrast(c, cutoff=1)
        bar = Image.new("L", (c.width, 22), 200)
        ImageDraw.Draw(bar).text((4, 4), spec, fill=0)
        t = Image.new("L", (c.width, c.height + 22), 255)
        t.paste(bar, (0, 0))
        t.paste(c, (0, 22))
        tiles.append(t)
    w = max(t.width for t in tiles)
    h = sum(t.height for t in tiles) + 6 * (len(tiles) - 1)
    m = Image.new("L", (w, h), 255)
    y = 0
    for t in tiles:
        m.paste(t, (0, y))
        y += t.height + 6
    m.save(out)
    print(out, m.size)


if __name__ == "__main__":
    main()
