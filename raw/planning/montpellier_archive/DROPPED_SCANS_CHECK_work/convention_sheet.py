"""Side-by-side: package scan022 / scan024 (MPL_142_001-093) against PDF pages 22 and 24, for the scan-numbering check."""
import sys, os, io, zipfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from render_dropped import render
from PIL import Image
Z = r"C:\Users\user\Documents\grothendieck_archive_transcription_20261110\packages_done\09_MPL_142_001-093\MPL_142_001-093_scans.zip"
z = zipfile.ZipFile(Z)
tiles = []
for s in (22, 24):
    a = Image.open(io.BytesIO(z.read(f"MPL_142_001-093_scan{s:03d}.jpg"))).convert("L")
    print(s, a.size)
    b = render("142", s, dpi=40)[0]
    for im in (a, b):
        im = im.copy(); im.thumbnail((250, 350)); tiles.append(im)
W = Image.new("L", (1000, 350), 255)
for i, t in enumerate(tiles):
    W.paste(t, (i * 250, 0))
W.save(os.path.join(os.environ.get("TMP_OUT", "."), "convention_sheet.png"))
