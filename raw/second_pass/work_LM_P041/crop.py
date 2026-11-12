import sys
from PIL import Image, ImageOps, ImageEnhance

# usage: python -I crop.py SRC OUT x0 y0 x1 y1 [scale] [rotate] [contrast]
# coordinates are fractions (0..1) of the source image size when all <= 1, else pixels
src, out = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = [float(v) for v in sys.argv[3:7]]
scale = float(sys.argv[7]) if len(sys.argv) > 7 else 2.0
rot = float(sys.argv[8]) if len(sys.argv) > 8 else 0.0
con = float(sys.argv[9]) if len(sys.argv) > 9 else 1.0
im = Image.open(src)
W, H = im.size
if max(x0, y0, x1, y1) <= 1.0:
    box = (int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H))
else:
    box = (int(x0), int(y0), int(x1), int(y1))
c = im.crop(box)
c = c.convert('L')
if con != 1.0:
    c = ImageEnhance.Contrast(c).enhance(con)
if scale != 1.0:
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
if rot:
    c = c.rotate(rot, expand=True, fillcolor=255)
c.save(out, quality=92)
print(src, (W, H), box, '->', out, c.size)
