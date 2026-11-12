"""Render the scans the packager dropped as blank, with strongly raised contrast.

Run with: python -I render_dropped.py
Writes <cote>_<scan>.png (full page, enhanced) next to this script.
"""
import sys, os
sys.path.append(os.path.expandvars(r"%APPDATA%\Python\Python313\site-packages"))
import fitz  # PyMuPDF
from PIL import Image, ImageOps
import numpy as np

ROOT = r"C:\Users\user\Documents\grothendieck_archive_montpellier"
OUT = os.path.dirname(os.path.abspath(__file__))
PDFS = {
    "1": r"01_mathematiques_recherche_travaux\1.pdf",
    "142": r"18_autour_de_la_longue_marche_a_travers_la_theorie_de\142.pdf",
    "146": r"18_autour_de_la_longue_marche_a_travers_la_theorie_de\146.pdf",
    "16": r"03_theorie_des_motifs\16.pdf",
    "5": r"02_cristaux\5.pdf",
    "6": r"02_cristaux\6.pdf",
    "7": r"02_cristaux\7.pdf",
    "8": r"02_cristaux\8.pdf",
    "100": r"11_geometrie_et_topologie_combinatoire\100.pdf",
}
DROPPED = {
    "1": [2, 37, 43, 47],
    "142": [23, 43, 65],
    "146": [26, 35, 42, 57, 70, 76, 79, 80, 88, 102, 105],
    "16": [2, 24],
    "5": [2],
    "6": [39, 58, 64],
    "7": [2, 20],
    "8": [24, 28, 33, 77],
    "100": [47],
}


def render(cote, scan, dpi=110):
    doc = fitz.open(os.path.join(ROOT, PDFS[cote]))
    page = doc[scan - 1]  # scan n = PDF page n
    pix = page.get_pixmap(dpi=dpi, colorspace=fitz.csGRAY)
    img = Image.frombytes("L", (pix.width, pix.height), pix.samples)
    return img, doc.page_count


def enhance(img):
    a = np.asarray(img).astype(np.float32)
    # histogram stretch: paper (high percentile) -> white, darkest 0.5% -> black
    lo = np.percentile(a, 0.5)
    hi = np.percentile(a, 60)  # paper level; pencil lies just below it
    if hi - lo < 4:
        hi = lo + 4
    b = np.clip((a - lo) / (hi - lo), 0, 1)
    b = b ** 2.2  # push faint marks darker
    return Image.fromarray((b * 255).astype(np.uint8))


if __name__ == "__main__":
    for cote, scans in DROPPED.items():
        for s in scans:
            img, n = render(cote, s)
            e = enhance(img)
            e.thumbnail((800, 1000))
            e.save(os.path.join(OUT, f"{cote}_{s}.png"))
            print(cote, s, "of", n, img.size)
