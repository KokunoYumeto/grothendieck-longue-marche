"""LM_P017 crop helper: crop/enlarge regions of the scans into one montage.

Usage: python -I LM_P017_crop.py OUT.png SPEC [SPEC ...]
SPEC = scan:half:x0:y0:x1:y1:scale[:rot]
  half = a | b | f  (coordinates are those of scanNNN_a.jpg, scanNNN_b.jpg or scanNNN.jpg)
  rot  = degrees counter-clockwise (optional)
Each crop is enlarged, auto-contrasted, labelled and stacked vertically.
"""
import sys
from PIL import Image, ImageOps, ImageDraw

IMG = r"C:\Users\user\Documents\longue_marche_pro_pilot_20261104\second_pass\img"


def load(scan, half):
    full = Image.open(rf"{IMG}\scan{scan}.jpg").convert("L")
    if half == "f":
        return full, 0
    if half == "a":
        return full, 0
    hb = Image.open(rf"{IMG}\scan{scan}_b.jpg").size[1]
    return full, full.size[1] - hb


def main():
    out = sys.argv[1]
    tiles = []
    for spec in sys.argv[2:]:
        p = spec.split(":")
        scan, half = p[0], p[1]
        x0, y0, x1, y1 = map(int, p[2:6])
        sc = float(p[6])
        rot = float(p[7]) if len(p) > 7 else 0.0
        full, off = load(scan, half)
        im = full.crop((x0, y0 + off, x1, y1 + off))
        im = ImageOps.autocontrast(im, cutoff=1)
        im = im.resize((int(im.size[0] * sc), int(im.size[1] * sc)), Image.LANCZOS)
        if rot:
            im = im.rotate(rot, expand=True, fillcolor=255)
        lab = Image.new("L", (im.size[0], 22), 255)
        ImageDraw.Draw(lab).text((4, 4), spec, fill=0)
        tile = Image.new("L", (im.size[0], im.size[1] + 22), 255)
        tile.paste(lab, (0, 0))
        tile.paste(im, (0, 22))
        tiles.append(tile)
    w = max(t.size[0] for t in tiles)
    h = sum(t.size[1] for t in tiles) + 6 * len(tiles)
    mont = Image.new("L", (w, h), 200)
    y = 0
    for t in tiles:
        mont.paste(t, (0, y))
        y += t.size[1] + 6
    mont.save(out)
    print(out, mont.size)


if __name__ == "__main__":
    main()
