"""Find a word on a page scan (Tesseract TSV, psm 6) and crop the lines around it, for checking by eye.
usage: python findcrop.py KEY REGEX OUT.png [nth] [lines_above lines_below]"""
import json, pathlib, re, subprocess, sys, tempfile
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from prep_images import scan_image
from PIL import ImageOps
TESS = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
BASE = pathlib.Path(__file__).resolve().parent.parent
P = {p["key"]: p for p in json.load(open(BASE / "PAGES.json", encoding="utf-8"))}
key, rx, out = sys.argv[1], sys.argv[2], sys.argv[3]
nth = int(sys.argv[4]) if len(sys.argv) > 4 else 0
up, down = (float(sys.argv[5]), float(sys.argv[6])) if len(sys.argv) > 6 else (1.3, 1.3)
im = ImageOps.autocontrast(scan_image(P[key]["cote"], P[key]["site"]), cutoff=0.5, preserve_tone=True)
cache = BASE / "work" / "tsv" / f"{key}.tsv"
cache.parent.mkdir(exist_ok=True)
if not cache.exists():
    with tempfile.TemporaryDirectory() as t:
        p = pathlib.Path(t) / "x.png"; im.convert("L").save(p)
        subprocess.run([TESS, str(p), str(pathlib.Path(t) / "x"), "-l", "eng", "--psm", "6", "tsv"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        cache.write_text((pathlib.Path(t) / "x.tsv").read_text(encoding="utf-8", errors="replace"), encoding="utf-8")
rows = [l.split("\t") for l in cache.read_text(encoding="utf-8").splitlines()[1:]]
hits = [r for r in rows if len(r) == 12 and re.search(rx, r[11], re.I)]
if not hits:
    sys.exit("not found")
r = hits[min(nth, len(hits) - 1)]
top, h = int(r[7]), int(r[9])
lh = 60
im.crop((0, max(0, int(top - up * lh)), im.width, min(im.height, int(top + h + down * lh)))).save(out)
print(len(hits), "hits; cropped at y", top)
