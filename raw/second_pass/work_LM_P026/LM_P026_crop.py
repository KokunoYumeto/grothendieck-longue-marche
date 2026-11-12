"""LM_P026 crop helper: crop regions of a scan, enlarge, optionally rotate and stack.

Usage: python LM_P026_crop.py OUTNAME SCAN x0 y0 x1 y1 [scale] [rot] [; SCAN x0 y0 x1 y1 [scale] [rot] ...]
Coordinates refer to the full scan image scanNNN.jpg. Several crops separated by ';' are stacked vertically.
"""
import sys
from PIL import Image, ImageOps

IMG = r"C:\Users\user\Documents\longue_marche_pro_pilot_20261104\second_pass\img"
OUT = r"C:\Users\user\Documents\longue_marche_pro_pilot_20261104\second_pass\work_LM_P026"

def one(spec):
    p = spec.split()
    scan = p[0]
    x0, y0, x1, y1 = map(int, p[1:5])
    scale = float(p[5]) if len(p) > 5 else 2.0
    rot = float(p[6]) if len(p) > 6 else 0.0
    im = Image.open(f"{IMG}\\scan{scan}.jpg").convert("L")
    c = im.crop((x0, y0, x1, y1))
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
    if rot:
        c = c.rotate(rot, expand=True, fillcolor=255)
    c = ImageOps.autocontrast(c, cutoff=1)
    return c

def main():
    name = sys.argv[1]
    specs = " ".join(sys.argv[2:]).split(";")
    ims = [one(s.strip()) for s in specs if s.strip()]
    w = max(i.width for i in ims)
    h = sum(i.height for i in ims) + 6 * (len(ims) - 1)
    out = Image.new("L", (w, h), 255)
    y = 0
    for i in ims:
        out.paste(i, (0, y))
        y += i.height + 6
    # keep the result within a readable size
    if out.width > 1900:
        f = 1900 / out.width
        out = out.resize((int(out.width * f), int(out.height * f)), Image.LANCZOS)
    out.save(f"{OUT}\\{name}.png")
    print(name, out.size)

if __name__ == "__main__":
    main()
