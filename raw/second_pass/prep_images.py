"""Native-resolution images of the archive scans for the second pass: for scans FIRST..LAST of cote 140-2, the largest
embedded image of each PDF page as scanNNN.jpg, plus two overlapping halves (top/bottom, or left/right for a landscape
spread) scanNNN_a.jpg and scanNNN_b.jpg, so that every stroke is read at the archive's resolution.
usage: python -I prep_images.py FIRST LAST"""
import pathlib
import shutil
import subprocess
import sys
import tempfile

from PIL import Image

PDF = pathlib.Path(r"C:\Users\user\Documents\interlanguage\Post_Stacks_Open_Source_Library\Reference_Only"
                   r"\Grothendieck_Late_Works\La_Longue_Marche\official_manuscript_witness"
                   r"\Montpellier_cote_140-2_La_Longue_Marche_pages_1-292.pdf")
OUT = pathlib.Path(__file__).parent / "img"
OUT.mkdir(exist_ok=True)
first, last = int(sys.argv[1]), int(sys.argv[2])
with tempfile.TemporaryDirectory() as tmp:
    for n in range(first, last + 1):
        d = pathlib.Path(tmp) / f"p{n}"
        d.mkdir()
        subprocess.run(["pdfimages", "-j", "-f", str(n), "-l", str(n), str(PDF), str(d / "i")], check=True)
        imgs = sorted(d.iterdir(), key=lambda p: Image.open(p).size[0] * Image.open(p).size[1], reverse=True)
        if not imgs:
            continue
        src = imgs[0]
        im = Image.open(src).convert("RGB")
        im.save(OUT / f"scan{n:03d}.jpg", quality=92)
        w, h = im.size
        if w > h:  # landscape spread: left and right pages
            a, b = im.crop((0, 0, w // 2 + 60, h)), im.crop((w // 2 - 60, 0, w, h))
        else:
            a, b = im.crop((0, 0, w, h // 2 + 80)), im.crop((0, h // 2 - 80, w, h))
        a.save(OUT / f"scan{n:03d}_a.jpg", quality=92)
        b.save(OUT / f"scan{n:03d}_b.jpg", quality=92)
        print(n, w, h)
