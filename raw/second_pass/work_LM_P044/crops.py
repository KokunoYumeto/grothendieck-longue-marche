import json, sys, os
from PIL import Image, ImageDraw, ImageOps, ImageEnhance

IMG = r"C:\Users\user\Documents\longue_marche_pro_pilot_20261104\second_pass\img"
OUT = r"C:\Users\user\Documents\longue_marche_pro_pilot_20261104\second_pass\work_LM_P044"

def crop_one(spec):
    scan, x0, y0, x1, y1 = spec["scan"], spec["box"][0], spec["box"][1], spec["box"][2], spec["box"][3]
    im = Image.open(os.path.join(IMG, "scan%d.jpg" % scan)).convert("L")
    c = im.crop((x0, y0, x1, y1))
    rot = spec.get("rot", 0)
    if rot:
        c = c.rotate(rot, expand=True, fillcolor=255)
    sc = spec.get("scale", 1.0)
    if sc != 1.0:
        c = c.resize((int(c.width * sc), int(c.height * sc)), Image.LANCZOS)
    if spec.get("contrast"):
        c = ImageEnhance.Contrast(c).enhance(spec["contrast"])
    return c

def montage(name, specs, maxw=1700):
    tiles = []
    for s in specs:
        c = crop_one(s)
        if c.width > maxw:
            r = maxw / c.width
            c = c.resize((maxw, int(c.height * r)), Image.LANCZOS)
        tiles.append((s.get("label", ""), c))
    W = max(t[1].width for t in tiles)
    H = sum(t[1].height + 24 for t in tiles)
    m = Image.new("L", (W, H), 255)
    d = ImageDraw.Draw(m)
    y = 0
    for lab, c in tiles:
        d.rectangle((0, y, W, y + 22), fill=200)
        d.text((4, y + 4), lab, fill=0)
        y += 24
        m.paste(c, (0, y))
        y += c.height
    p = os.path.join(OUT, name + ".png")
    m.save(p)
    print(p, m.size)

if __name__ == "__main__":
    groups = json.load(open(sys.argv[1], encoding="utf-8"))
    for name, specs in groups.items():
        montage(name, specs)
