import sys
from PIL import Image, ImageOps

# usage: python -I cropx.py IMGNAME x0 y0 x1 y1 scale out_name [rotate_degrees]
# IMGNAME is e.g. scan422_b (a file in second_pass\img); coordinates are pixels of that image.
# Several crops can be chained: separate groups of 7/8 arguments with a single "+".
base = r"C:\Users\user\Documents\longue_marche_pro_pilot_20261104\second_pass"
args = sys.argv[1:]
groups = []
cur = []
for a in args:
    if a == "+":
        groups.append(cur)
        cur = []
    else:
        cur.append(a)
if cur:
    groups.append(cur)
for g in groups:
    name = g[0]
    x0, y0, x1, y1 = [int(float(v)) for v in g[1:5]]
    scale = float(g[5])
    out = g[6]
    rot = float(g[7]) if len(g) > 7 else 0.0
    im = Image.open(base + "\\img\\" + name + ".jpg")
    c = im.crop((x0, y0, x1, y1))
    if rot:
        c = c.rotate(rot, expand=True, fillcolor=(255, 255, 255))
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
    c = ImageOps.autocontrast(c.convert("L"), cutoff=1)
    c.save(base + "\\work_LM_P043\\" + out + ".png")
    print(name, im.size, (x0, y0, x1, y1), c.size, out)
