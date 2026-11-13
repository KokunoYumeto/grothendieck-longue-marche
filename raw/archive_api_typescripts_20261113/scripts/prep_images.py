"""Render the page images sent over the API (12 Nov 2026).

Each page's scan is the single JPEG embedded in its PDF page (site s = PyMuPDF page index s = PDF page s+1), used at
its native resolution (about 1690 x 2360 px). Tone is stretched with PIL's autocontrast (cut-off 0.5 %, the same
curve on all three channels, so ink colours keep their hue), which makes the faint carbon copies legible. The page is
cut into an upper part (0-53 % of the height) and a lower part (47-100 %), each about 1690 x 1250 px, so that the
API does not downscale them; saved as colour JPEG, quality 85, in work/img/<key>_a.jpg and _b.jpg.
usage: python prep_images.py [KEY_PREFIX ...]   (default: every page of PAGES.json)
"""
import hashlib
import io
import json
import pathlib
import sys
from concurrent.futures import ThreadPoolExecutor

import fitz
from PIL import Image, ImageOps

BASE = pathlib.Path(__file__).resolve().parent.parent
ARCH = pathlib.Path(r"C:\Users\user\Documents\grothendieck_archive_montpellier")
PDFS = {"134-%d" % k: ARCH / "15_pursuing_stacks_a_la_poursuite_des_champs_first_ep" / f"134-{k}.pdf" for k in range(1, 9)}
PDFS["119"] = ARCH / "13_autour_desquisse_dun_programme" / "119.pdf"
PDFS["24"] = ARCH / "04_elements_de_geometrie_algebrique_ega" / "24.pdf"
PDFS["25"] = ARCH / "04_elements_de_geometrie_algebrique_ega" / "25.pdf"
PDFS["129"] = ARCH / "14_descentes" / "129.pdf"  # 13 Nov 2026: next texts (scripts/next_texts_20261113.py)
PDFS["162-5"] = ARCH / "22_dossiers_rassembles_par_grothendieck_sur_different" / "162-5.pdf"
IMG = BASE / "work" / "img"
IMG.mkdir(parents=True, exist_ok=True)


def scan_image(cote, site):
    doc = fitz.open(PDFS[cote])
    imgs = doc[site].get_images(full=True)
    assert len(imgs) == 1, (cote, site, len(imgs))
    pix = fitz.Pixmap(doc, imgs[0][0])
    if pix.n - pix.alpha >= 4 or pix.alpha:
        pix = fitz.Pixmap(fitz.csRGB, pix)
    return Image.open(io.BytesIO(pix.tobytes("png"))).convert("RGB")


def job(p):
    a, b = IMG / f"{p['key']}_a.jpg", IMG / f"{p['key']}_b.jpg"
    if a.exists() and b.exists():
        return p["key"], None
    im = ImageOps.autocontrast(scan_image(p["cote"], p["site"]), cutoff=0.5, preserve_tone=True)
    w, h = im.size
    im.crop((0, 0, w, int(0.53 * h))).save(a, quality=85)
    im.crop((0, int(0.47 * h), w, h)).save(b, quality=85)
    return p["key"], (w, h)


def main():
    pages = json.load(open(BASE / "PAGES.json", encoding="utf-8"))
    if len(sys.argv) > 1:
        pages = [p for p in pages if any(p["key"].startswith(x) or p["key"] == x for x in sys.argv[1:])]
    with ThreadPoolExecutor(6) as ex:
        for k, size in ex.map(job, pages):
            if size:
                print(k, size, flush=True)
    meta = {}
    for f in sorted(IMG.glob("*.jpg")):
        meta[f.name] = {"bytes": f.stat().st_size, "sha256": hashlib.sha256(f.read_bytes()).hexdigest()}
    json.dump(meta, open(BASE / "work" / "img_manifest.json", "w"), indent=0)


if __name__ == "__main__":
    main()
