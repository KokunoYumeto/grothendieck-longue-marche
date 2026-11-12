import sys
from PIL import Image, ImageOps
# usage: crop.py scanNNN[_a|_b] x0 y0 x1 y1 scale out [rot] [nocontrast]
img, x0, y0, x1, y1, scale, out = sys.argv[1:8]
rot = int(sys.argv[8]) if len(sys.argv) > 8 else 0
base = r'C:/Users/user/Documents/longue_marche_pro_pilot_20261104/second_pass/'
im = Image.open(base + 'img/' + img + '.jpg')
c = im.crop((int(x0), int(y0), int(x1), int(y1)))
s = float(scale)
c = c.resize((int(c.width * s), int(c.height * s)), Image.LANCZOS)
if rot:
    c = c.rotate(rot, expand=True)
c = ImageOps.autocontrast(c.convert('L'), cutoff=1)
c.save(base + 'work_LM_P10/' + out + '.png')
print(out, im.size, c.size)
