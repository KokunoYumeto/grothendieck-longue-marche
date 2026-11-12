"""Crop a region of a page scan for checking by eye: python crop.py KEY Y0 Y1 [X0 X1] OUT.png  (fractions of the page)."""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from prep_images import scan_image
from PIL import ImageOps
BASE = pathlib.Path(__file__).resolve().parent.parent
P = {p["key"]: p for p in json.load(open(BASE / "PAGES.json", encoding="utf-8"))}
key, y0, y1 = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])
x0, x1 = (float(sys.argv[4]), float(sys.argv[5])) if len(sys.argv) > 6 else (0.0, 1.0)
out = sys.argv[-1]
im = ImageOps.autocontrast(scan_image(P[key]["cote"], P[key]["site"]), cutoff=0.5, preserve_tone=True)
w, h = im.size
im.crop((int(x0 * w), int(y0 * h), int(x1 * w), int(y1 * h))).save(out)
