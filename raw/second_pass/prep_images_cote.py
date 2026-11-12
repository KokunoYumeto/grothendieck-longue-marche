"""Native-resolution images of the archive scans for the second pass, for any cote: the largest embedded image of each
PDF page as scanNNN.jpg plus two overlapping halves (top/bottom, or left/right for a landscape spread), scanNNN_a.jpg
and scanNNN_b.jpg. Cote 140-2 goes to second_pass/img (as prep_images.py), the others to second_pass/img_140-N.
Skips scans already done. usage: python -I prep_images_cote.py COTE FIRST LAST   (COTE: 140-1, 140-2, 140-3, 140-4)"""
import pathlib
import subprocess
import sys
import tempfile

from PIL import Image

BASE = pathlib.Path(r"C:\Users\user\Documents\interlanguage\Post_Stacks_Open_Source_Library\Reference_Only"
                    r"\Grothendieck_Late_Works\La_Longue_Marche\official_manuscript_witness")
PDF = {"140-1": "Montpellier_cote_140-1_La_Longue_Marche_brouillon.pdf",
       "140-2": "Montpellier_cote_140-2_La_Longue_Marche_pages_1-292.pdf",
       "140-3": "Montpellier_cote_140-3_La_Longue_Marche_pages_293-650.pdf",
       "140-4": "Montpellier_cote_140-4_La_Longue_Marche_pages_650bis-787.pdf"}
cote, first, last = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
OUT = pathlib.Path(__file__).parent / ("img" if cote == "140-2" else f"img_{cote}")
OUT.mkdir(exist_ok=True)
with tempfile.TemporaryDirectory() as tmp:
    for n in range(first, last + 1):
        if (OUT / f"scan{n:03d}_b.jpg").exists():
            continue
        d = pathlib.Path(tmp) / f"p{n}"
        d.mkdir()
        subprocess.run(["pdfimages", "-j", "-f", str(n), "-l", str(n), str(BASE / PDF[cote]), str(d / "i")], check=True)
        imgs = sorted(d.iterdir(), key=lambda p: Image.open(p).size[0] * Image.open(p).size[1], reverse=True)
        if not imgs:
            print(n, "no image");
            continue
        im = Image.open(imgs[0]).convert("RGB")
        im.save(OUT / f"scan{n:03d}.jpg", quality=92)
        w, h = im.size
        if w > h:
            a, b = im.crop((0, 0, w // 2 + 60, h)), im.crop((w // 2 - 60, 0, w, h))
        else:
            a, b = im.crop((0, 0, w, h // 2 + 80)), im.crop((0, h // 2 - 80, w, h))
        a.save(OUT / f"scan{n:03d}_a.jpg", quality=92)
        b.save(OUT / f"scan{n:03d}_b.jpg", quality=92)
    print(cote, first, last, "done ->", OUT)
