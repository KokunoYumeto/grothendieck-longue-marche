"""Crop and enlarge regions of the second-pass scans for LM_P019, stacked into one montage.
usage: python -I LM_P019_crop.py OUTNAME SCAN:x0,y0,x1,y1[:scale[:rot]] ...
Coordinates are in full-page pixels of img/scanNNN.jpg. Output: work_LM_P019/OUTNAME.png
Each crop is autocontrasted, enlarged by `scale` (default 2), optionally rotated by `rot` degrees,
and the crops are stacked vertically, separated by a grey rule.
"""
import pathlib
import sys

from PIL import Image, ImageOps, ImageDraw

HERE = pathlib.Path(__file__).resolve().parent
IMG = HERE.parent / "img"

out = sys.argv[1]
tiles = []
for spec in sys.argv[2:]:
    parts = spec.split(":")
    scan, box = int(parts[0]), [int(v) for v in parts[1].split(",")]
    scale = float(parts[2]) if len(parts) > 2 else 2.0
    rot = int(parts[3]) if len(parts) > 3 else 0
    im = Image.open(IMG / f"scan{scan:03d}.jpg").convert("L")
    c = im.crop(tuple(box))
    c = ImageOps.autocontrast(c, cutoff=1)
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
    if rot:
        c = c.rotate(rot, expand=True, fillcolor=255)
    tiles.append(c)
W = max(t.width for t in tiles)
H = sum(t.height for t in tiles) + 6 * (len(tiles) - 1)
m = Image.new("L", (W, H), 255)
y = 0
d = ImageDraw.Draw(m)
for i, t in enumerate(tiles):
    m.paste(t, (0, y))
    y += t.height
    if i < len(tiles) - 1:
        d.rectangle([0, y + 1, W, y + 4], fill=128)
        y += 6
m.save(HERE / f"{out}.png")
print(out, m.size)
