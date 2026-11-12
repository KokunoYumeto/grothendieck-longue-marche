"""LM_P016 crop helper: cut regions from full-page scans, enlarge, optionally rotate,
and stack several crops into one labelled montage.

Usage:
  python LM_P016_crop.py OUTNAME SPEC [SPEC ...]
SPEC = scan:x0,y0,x1,y1:scale[:rot]
  coordinates in full-page pixels of second_pass/img/scanNNN.jpg;
  rot in degrees counter-clockwise (e.g. 90 or -90).
The montage is written to second_pass/work_LM_P016/OUTNAME.png.
"""
import os
import sys

from PIL import Image, ImageDraw, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(os.path.dirname(HERE), "img")
MAXW = 1800


def crop(spec):
    parts = spec.split(":")
    scan = int(parts[0])
    x0, y0, x1, y1 = (int(v) for v in parts[1].split(","))
    scale = float(parts[2])
    rot = float(parts[3]) if len(parts) > 3 else 0.0
    im = Image.open(os.path.join(IMG, "scan%03d.jpg" % scan)).convert("L")
    c = im.crop((x0, y0, x1, y1))
    c = ImageOps.autocontrast(c, cutoff=1)
    if rot:
        c = c.rotate(rot, expand=True, fillcolor=255)
    w, h = c.size
    c = c.resize((max(1, int(w * scale)), max(1, int(h * scale))), Image.LANCZOS)
    if c.size[0] > MAXW:
        r = MAXW / c.size[0]
        c = c.resize((MAXW, max(1, int(c.size[1] * r))), Image.LANCZOS)
    return spec, c


def main():
    out = sys.argv[1]
    crops = [crop(s) for s in sys.argv[2:]]
    W = max(c.size[0] for _, c in crops)
    H = sum(c.size[1] + 22 for _, c in crops)
    m = Image.new("L", (W, H), 255)
    d = ImageDraw.Draw(m)
    y = 0
    for spec, c in crops:
        d.text((4, y + 4), spec, fill=0)
        y += 20
        m.paste(c, (0, y))
        y += c.size[1] + 2
        d.line((0, y, W, y), fill=0)
    p = os.path.join(HERE, out + ".png")
    m.save(p)
    print(p, m.size)


if __name__ == "__main__":
    main()
