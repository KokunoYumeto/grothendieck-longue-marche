import sys
from PIL import Image, ImageEnhance

# usage: python -I rotcrop.py SRC OUT x0,y0,x1,y1 scale angle cx0,cy0,cx1,cy1 [contrast]
src, out = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = [int(v) for v in sys.argv[3].split(',')]
scale = float(sys.argv[4])
ang = float(sys.argv[5])
cx0, cy0, cx1, cy1 = [int(v) for v in sys.argv[6].split(',')]
con = float(sys.argv[7]) if len(sys.argv) > 7 else 1.0
im = Image.open(src).convert('L').crop((x0, y0, x1, y1))
im = im.resize((int(im.width * scale), int(im.height * scale)), Image.LANCZOS)
im = im.rotate(ang, expand=True, fillcolor=255)
im = im.crop((cx0, cy0, cx1, cy1))
if con != 1.0:
    im = ImageEnhance.Contrast(im).enhance(con)
im.save(out, quality=92)
print(out, im.size)
