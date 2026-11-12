"""LM_P032 helper: build labelled crop sheets from the scan halves.

Usage: python LM_P032_sheet.py SPEC.json OUTPREFIX
SPEC is a list of [label, scan, half, x0, y0, x1, y1, scale, rot]
(half = "a" or "b" or "" for the whole page; rot in degrees, counter-clockwise).
Crops are enhanced (autocontrast), enlarged and stacked into sheets of at most
MAXH pixels height and MAXW width.
"""
import json
import sys
from PIL import Image, ImageDraw, ImageOps

IMG = r"C:\Users\user\Documents\longue_marche_pro_pilot_20261104\second_pass\img"
MAXW, MAXH = 1600, 1700


def crop(scan, half, box, scale, rot):
    name = f"scan{scan}{'_' + half if half else ''}.jpg"
    im = Image.open(f"{IMG}\\{name}").convert("L")
    c = im.crop(tuple(box))
    if rot:
        c = c.rotate(rot, expand=True, fillcolor=255, resample=Image.BICUBIC)
    c = ImageOps.autocontrast(c, cutoff=1)
    w, h = c.size
    c = c.resize((max(1, int(w * scale)), max(1, int(h * scale))), Image.LANCZOS)
    if c.size[0] > MAXW:
        f = MAXW / c.size[0]
        c = c.resize((MAXW, int(c.size[1] * f)), Image.LANCZOS)
    return c


def main():
    spec = json.load(open(sys.argv[1], encoding="utf-8"))
    prefix = sys.argv[2]
    pieces = []
    for label, scan, half, x0, y0, x1, y1, scale, rot in spec:
        c = crop(scan, half, (x0, y0, x1, y1), scale, rot)
        lab = Image.new("L", (c.size[0], 22), 230)
        ImageDraw.Draw(lab).text((4, 4), f"{label}  [{scan}{half} {x0},{y0},{x1},{y1} x{scale} r{rot}]", fill=0)
        piece = Image.new("L", (c.size[0], c.size[1] + 22 + 6), 255)
        piece.paste(lab, (0, 0))
        piece.paste(c, (0, 22))
        pieces.append(piece)
    sheets, cur, curh = [], [], 0
    for p in pieces:
        if cur and curh + p.size[1] > MAXH:
            sheets.append(cur)
            cur, curh = [], 0
        cur.append(p)
        curh += p.size[1]
    if cur:
        sheets.append(cur)
    for i, s in enumerate(sheets, 1):
        W = max(p.size[0] for p in s)
        H = sum(p.size[1] for p in s)
        out = Image.new("L", (W, H), 255)
        y = 0
        for p in s:
            out.paste(p, (0, y))
            y += p.size[1]
        fn = f"{prefix}_{i}.png"
        out.save(fn)
        print(fn, out.size)


if __name__ == "__main__":
    main()
