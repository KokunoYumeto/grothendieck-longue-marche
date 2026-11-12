"""Re-OCR (Tesseract, eng) the pages whose first OCR gave fewer than 60 words, after contrast enhancement
(first try: autocontrast and upscale, page segmentation 3, which helped 29 pages; second and kept: plain
greyscale with page segmentation mode 6, a single block of text, which reads the faint carbon copies). Writes work/ocr/<cote>/<site>.txt over the old file
(the old one is kept as <site>.orig.txt). Used only for aligning the drafts.
usage: python reocr.py COTE[,COTE...]
"""
import io
import pathlib
import re
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor

import fitz
from PIL import Image, ImageOps

TESS = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
BASE = pathlib.Path(__file__).resolve().parent.parent
ARCH = pathlib.Path(r"C:\Users\user\Documents\grothendieck_archive_montpellier")
PDFS = {"134-%d" % k: ARCH / "15_pursuing_stacks_a_la_poursuite_des_champs_first_ep" / f"134-{k}.pdf" for k in range(1, 9)}
PDFS["119"] = ARCH / "13_autour_desquisse_dun_programme" / "119.pdf"
PDFS["24"] = ARCH / "04_elements_de_geometrie_algebrique_ega" / "24.pdf"
PDFS["25"] = ARCH / "04_elements_de_geometrie_algebrique_ega" / "25.pdf"


def scan_image(cote, site):
    doc = fitz.open(PDFS[cote])
    pg = doc[site]
    imgs = pg.get_images(full=True)
    pix = fitz.Pixmap(doc, imgs[0][0])
    if pix.n - pix.alpha >= 4 or pix.alpha:
        pix = fitz.Pixmap(fitz.csRGB, pix)
    return Image.open(io.BytesIO(pix.tobytes("png"))).convert("RGB")


def nwords(t):
    return len(re.findall(r"[^\W\d_]{2,}", t))


def job(args):
    cote, site, tmp = args
    out = BASE / "work" / "ocr" / cote / f"{site}.txt"
    old = out.read_text(encoding="utf-8", errors="replace") if out.exists() else ""
    im = scan_image(cote, site).convert("L")
    png = pathlib.Path(tmp) / f"{cote}_{site}.png"
    im.save(png)
    base = str(png)[:-4]
    subprocess.run([TESS, str(png), base, "-l", "eng", "--psm", "6"], stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL)
    new = pathlib.Path(base + ".txt").read_text(encoding="utf-8", errors="replace")
    if nwords(new) > nwords(old):
        if old and not (out.parent / f"{site}.orig.txt").exists():
            (out.parent / f"{site}.orig.txt").write_text(old, encoding="utf-8")
        out.write_text(new, encoding="utf-8")
    return cote, site, nwords(old), nwords(new)


def main():
    todo = []
    with tempfile.TemporaryDirectory() as tmp:
        for cote in sys.argv[1].split(","):
            d = fitz.open(PDFS[cote])
            for s in range(len(d)):
                p = BASE / "work" / "ocr" / cote / f"{s}.txt"
                t = p.read_text(encoding="utf-8", errors="replace") if p.exists() else ""
                if nwords(t) < 60:
                    todo.append((cote, s, tmp))
        print(len(todo), "pages to re-OCR", flush=True)
        with ThreadPoolExecutor(8) as ex:
            for r in ex.map(job, todo):
                print(*r, flush=True)


if __name__ == "__main__":
    main()
