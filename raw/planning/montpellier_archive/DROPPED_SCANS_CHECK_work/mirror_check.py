"""Show-through check: python -I mirror_check.py COTE SCAN NEIGHBOUR OUT
Places the enhanced, horizontally mirrored scan next to a neighbouring scan, to see whether faint marks are the neighbour's ink seen through the paper."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from render_dropped import render, enhance
from PIL import Image, ImageOps
cote, s, nb, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
a = ImageOps.mirror(enhance(render(cote, s, dpi=70)[0]))
b = render(cote, nb, dpi=70)[0]
W = Image.new("L", (a.width + b.width, max(a.height, b.height)), 255)
W.paste(a, (0, 0)); W.paste(b, (a.width, 0))
W.thumbnail((1100, 800)); W.save(out)
