"""Neighbour sheet: python -I neighbours.py COTE SCAN OUT
Enhanced scan (plain and mirrored) beside raw scans n-1 and n+1, page area only, to decide show-through vs writing."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from render_dropped import render, enhance
from PIL import Image, ImageOps
cote, s, out = sys.argv[1], int(sys.argv[2]), sys.argv[3]
def pg(n, enh=False):
    im = render(cote, n, dpi=60)[0]
    if enh: im = enhance(im)
    return im.crop((int(.08 * im.width), int(.06 * im.height), int(.92 * im.width), int(.89 * im.height)))
e = pg(s, True)
ims = [e, ImageOps.mirror(e), pg(s - 1), pg(s + 1)]
w, h = ims[0].size
W = Image.new("L", (4 * w, h), 255)
for k, i in enumerate(ims): W.paste(i, (k * w, 0))
W.thumbnail((1400, 600)); W.save(out)
