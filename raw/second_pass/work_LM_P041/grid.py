import sys
from PIL import Image, ImageDraw

# usage: python -I grid.py OUT COLS spec [spec ...]
# spec = SRC|x0,y0,x1,y1|scale   (pixel coordinates in SRC)
out = sys.argv[1]
cols = int(sys.argv[2])
tiles = []
for n, spec in enumerate(sys.argv[3:]):
    parts = spec.split('|')
    src = parts[0]
    scale = float(parts[2]) if len(parts) > 2 else 2.0
    im = Image.open(src).convert('L')
    if parts[1] == 'all':
        x0, y0, x1, y1 = 0, 0, im.width, im.height
    else:
        x0, y0, x1, y1 = [int(float(v)) for v in parts[1].split(',')]
    c = im.crop((x0, y0, x1, y1))
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
    label = '[%d] %s %s' % (n + 1, src.split('/')[-1].replace('.jpg', ''), parts[1])
    tiles.append((label, c))
rows = [tiles[i:i + cols] for i in range(0, len(tiles), cols)]
W = max(sum(t.width + 10 for _, t in r) for r in rows)
H = sum(max(t.height for _, t in r) + 26 for r in rows)
canvas = Image.new('L', (W, H), 255)
d = ImageDraw.Draw(canvas)
y = 0
for r in rows:
    x = 0
    h = max(t.height for _, t in r)
    for label, t in r:
        d.rectangle((x, y, x + t.width, y + 24), fill=200)
        d.text((x + 3, y + 6), label, fill=0)
        canvas.paste(t, (x, y + 26))
        x += t.width + 10
    y += h + 26
canvas.save(out, quality=90)
print(out, canvas.size)
