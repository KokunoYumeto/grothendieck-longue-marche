"""Enhanced crop of one scan: python -I crop.py COTE SCAN x0 y0 x1 y1 OUT [dpi] [gamma]
Coordinates are fractions of the page (0-1). Output goes to OUT."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from render_dropped import render
from PIL import Image
import numpy as np
cote, scan = sys.argv[1], int(sys.argv[2])
x0, y0, x1, y1 = map(float, sys.argv[3:7])
out = sys.argv[7]
dpi = int(sys.argv[8]) if len(sys.argv) > 8 else 250
g = float(sys.argv[9]) if len(sys.argv) > 9 else 3.0
img, _ = render(cote, scan, dpi=dpi)
W, H = img.size
c = img.crop((int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H)))
a = np.asarray(c).astype(np.float32)
lo, hi = np.percentile(a, 0.3), np.percentile(a, 50)
b = np.clip((a - lo) / max(hi - lo, 4), 0, 1) ** g
im = Image.fromarray((b * 255).astype(np.uint8))
im.thumbnail((1100, 1100))
im.save(out)
print(im.size)
