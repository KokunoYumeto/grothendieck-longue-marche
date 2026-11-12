"""crop a scan: python -I img.py PKG SCAN OUT x0 y0 x1 y1 [width]  (fractions of the page; output width in px)"""
import sys, pathlib
from PIL import Image, ImageOps
L = pathlib.Path(__file__).resolve().parents[2]
pkg, scan, out = sys.argv[1], sys.argv[2], sys.argv[3]
x0, y0, x1, y1 = (float(v) for v in sys.argv[4:8])
w = int(sys.argv[8]) if len(sys.argv) > 8 else 1000
im = Image.open(L / pkg / f"{pkg}_scan{scan}.jpg").convert("L")
W, H = im.size
c = im.crop((int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H)))
c = ImageOps.autocontrast(c, cutoff=1)
s = w / c.size[0]
c = c.resize((w, max(1, int(c.size[1] * s))), Image.LANCZOS)
c.save(pathlib.Path(__file__).parent / "img" / out)
print(out, c.size)
