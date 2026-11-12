import sys
from PIL import Image, ImageDraw, ImageOps

IMG = r"C:\Users\user\Documents\longue_marche_pro_pilot_20261104\second_pass\img"
OUT = r"C:\Users\user\Documents\longue_marche_pro_pilot_20261104\second_pass\work_LM_P042"

# usage: python -I crop.py outname "scan:x0,y0,x1,y1:scale:rot:contrast;..."
# coordinates are in full-page pixels of scanNNN.jpg
outname = sys.argv[1]
specs = [s for s in sys.argv[2].split(";") if s.strip()]
maxw = int(sys.argv[3]) if len(sys.argv) > 3 else 1800
tiles = []
for sp in specs:
    parts = sp.split(":")
    scan = parts[0]
    x0, y0, x1, y1 = [int(v) for v in parts[1].split(",")]
    scale = float(parts[2]) if len(parts) > 2 and parts[2] else 2.0
    rot = float(parts[3]) if len(parts) > 3 and parts[3] else 0.0
    con = parts[4] if len(parts) > 4 else ""
    im = Image.open(f"{IMG}\\scan{scan}.jpg").convert("L")
    c = im.crop((x0, y0, x1, y1))
    if con:
        c = ImageOps.autocontrast(c, cutoff=1)
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
    if rot:
        c = c.rotate(rot, expand=True, fillcolor=255)
    if c.width > maxw:
        r = maxw / c.width
        c = c.resize((maxw, int(c.height * r)), Image.LANCZOS)
    lab = Image.new("L", (c.width, 22), 230)
    ImageDraw.Draw(lab).text((4, 4), sp, fill=0)
    tiles.append(lab)
    tiles.append(c)
W = max(t.width for t in tiles)
H = sum(t.height for t in tiles) + 4 * len(tiles)
m = Image.new("L", (W, H), 255)
y = 0
for t in tiles:
    m.paste(t, (0, y))
    y += t.height + 4
m.save(f"{OUT}\\{outname}.png")
print(m.size)
