import sys
from PIL import Image, ImageDraw, ImageEnhance

# usage: python -I montage.py OUT spec [spec ...]
# spec = SRC:x0,y0,x1,y1:scale[:rot[:contrast]]   (pixel coordinates in SRC)
out = sys.argv[1]
tiles = []
for spec in sys.argv[2:]:
    parts = spec.split('|')
    src = parts[0]
    x0, y0, x1, y1 = [int(float(v)) for v in parts[1].split(',')]
    scale = float(parts[2]) if len(parts) > 2 else 2.0
    rot = float(parts[3]) if len(parts) > 3 else 0.0
    con = float(parts[4]) if len(parts) > 4 else 1.0
    im = Image.open(src).convert('L')
    c = im.crop((x0, y0, x1, y1))
    if con != 1.0:
        c = ImageEnhance.Contrast(c).enhance(con)
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
    if rot:
        c = c.rotate(rot, expand=True, fillcolor=255)
    tiles.append((spec, c))
W = max(t.width for _, t in tiles)
H = sum(t.height + 30 for _, t in tiles)
canvas = Image.new('L', (W, H), 255)
d = ImageDraw.Draw(canvas)
y = 0
for i, (spec, t) in enumerate(tiles):
    d.rectangle((0, y, W, y + 28), fill=200)
    d.text((5, y + 8), '[%d] %s' % (i + 1, spec.split('|')[1]), fill=0)
    y += 30
    canvas.paste(t, (0, y))
    y += t.height
canvas.save(out, quality=90)
print(out, canvas.size)
