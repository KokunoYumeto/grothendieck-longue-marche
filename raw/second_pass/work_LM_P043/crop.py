import sys
from PIL import Image, ImageOps

# usage: python -I crop.py scanNNN x0 y0 x1 y1 scale out_name [rotate_degrees]
# coordinates are fractions (0..1) of the full-page image scanNNN.jpg
base = r"C:\Users\user\Documents\longue_marche_pro_pilot_20261104\second_pass"
scan = sys.argv[1]
x0, y0, x1, y1 = [float(v) for v in sys.argv[2:6]]
scale = float(sys.argv[6])
out = sys.argv[7]
rot = float(sys.argv[8]) if len(sys.argv) > 8 else 0.0
im = Image.open(base + "\\img\\" + scan + ".jpg")
W, H = im.size
box = (int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H))
c = im.crop(box)
if rot:
    c = c.rotate(rot, expand=True, fillcolor=(255, 255, 255))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c = ImageOps.autocontrast(c.convert("L"), cutoff=1)
c.save(base + "\\work_LM_P043\\" + out + ".png")
print(W, H, box, c.size)
