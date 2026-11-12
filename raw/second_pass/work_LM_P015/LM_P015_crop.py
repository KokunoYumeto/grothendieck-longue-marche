"""Stack several enlarged crops of the LM_P015 scans (141-150) into one labelled image.
usage: python -I LM_P015_crop.py OUT.png SPEC [SPEC ...]
SPEC = scan:x0,y0,x1,y1[:scale[:rot]]   (full-page pixel coordinates)
       prefix the box with 'b' (e.g. 141:b100,200,500,300) to give coordinates relative to the bottom half
       (half 'b' starts at y = h//2 - 80).
"""
import pathlib
import sys

from PIL import Image, ImageDraw, ImageOps

IMG = pathlib.Path(__file__).resolve().parent.parent / "img"
out = pathlib.Path(sys.argv[1])
tiles = []
for spec in sys.argv[2:]:
    parts = spec.split(":")
    n = int(parts[0])
    box = parts[1]
    im = Image.open(IMG / f"scan{n:03d}.jpg").convert("L")
    off = 0
    if box.startswith("b"):
        off = im.size[1] // 2 - 80
        box = box[1:]
    x0, y0, x1, y1 = (int(v) for v in box.split(","))
    scale = float(parts[2]) if len(parts) > 2 else 2.0
    rot = int(parts[3]) if len(parts) > 3 else 0
    c = im.crop((x0, y0 + off, x1, y1 + off))
    c = ImageOps.autocontrast(c, cutoff=1)
    c = c.resize((int(c.size[0] * scale), int(c.size[1] * scale)), Image.LANCZOS)
    if rot:
        c = c.rotate(rot, expand=True, fillcolor=255)
    lab = Image.new("L", (c.size[0], 22), 255)
    ImageDraw.Draw(lab).text((4, 4), spec, fill=0)
    t = Image.new("L", (c.size[0], c.size[1] + 22), 255)
    t.paste(lab, (0, 0))
    t.paste(c, (0, 22))
    tiles.append(t)
W = max(t.size[0] for t in tiles)
H = sum(t.size[1] + 6 for t in tiles)
canvas = Image.new("L", (W, H), 160)
y = 0
for t in tiles:
    canvas.paste(t, (0, y))
    y += t.size[1] + 6
canvas.save(out)
print(out, canvas.size)
