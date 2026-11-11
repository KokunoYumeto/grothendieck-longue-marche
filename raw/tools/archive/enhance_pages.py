"""Contrast-enhanced page images of the Montpellier archive PDFs (user, 10 Nov 2026: "Up contrast").

Each page of the archive's PDFs is one colour JPEG scan (250 ppi). This script extracts the scans without re-encoding
(pdfimages -j), keeps the largest image of each page, stretches its levels on the luminance (the same curve on all
three channels, so coloured inks keep their colour), darkens the middle tones a little, and writes
<topic folder>/<cote>_pages/pNNNN.jpg. The PDFs stay untouched as the originals.

usage:
  python -I enhance_pages.py sample COTE PAGE OUTDIR       before/after crops of one page, for choosing the settings
  python -I enhance_pages.py cote COTE [--force]           all pages of one cote
  python -I enhance_pages.py all                           every downloaded cote that has no _pages folder yet
settings: --cutoff LOW,HIGH (percent clipped at the dark and light ends; default 0.5,1.0)  --gamma G (default 1.3)"""
import json
import pathlib
import shutil
import subprocess
import sys

from PIL import Image, ImageOps

sys.stdout.reconfigure(encoding="utf-8")
ROOT = pathlib.Path(r"C:\Users\user\Documents\grothendieck_archive_montpellier")


def opt(name, default):
    return sys.argv[sys.argv.index(name) + 1] if name in sys.argv else default


CUT = tuple(float(x) for x in opt("--cutoff", "0.5,1.0").split(","))
GAMMA = float(opt("--gamma", "1.3"))
LUT = [round(255 * (v / 255) ** GAMMA) for v in range(256)]


def enhance(im):
    im = im.convert("RGB")
    im = ImageOps.autocontrast(im, cutoff=CUT, preserve_tone=True)
    return im.point(LUT * 3)


def row(cote):
    for r in json.loads((ROOT / "MANIFEST.json").read_text(encoding="utf-8")):
        if r["cote"] == cote:
            return r
    raise SystemExit("unknown cote " + cote)


def extract(pdf, tmp, first=None, last=None):
    tmp.mkdir(parents=True, exist_ok=True)
    cmd = ["pdfimages", "-j", "-png", "-p"]
    if first:
        cmd += ["-f", str(first), "-l", str(last or first)]
    subprocess.run(cmd + [str(pdf), str(tmp / "im")], check=True, capture_output=True)
    best = {}
    for f in tmp.iterdir():
        parts = f.stem.split("-")  # im-PPP-NNN
        if len(parts) < 3:
            continue
        pg = int(parts[1])
        if pg not in best or f.stat().st_size > best[pg].stat().st_size:
            best[pg] = f
    return best


def do_cote(cote, force=False):
    r = row(cote)
    pdf = ROOT / r["folder"] / r["file"]
    if not pdf.exists():
        print(cote, "not downloaded yet")
        return
    out = ROOT / r["folder"] / f"{cote}_pages"
    if out.exists() and not force:
        print(cote, "already done")
        return
    tmp = ROOT / r["folder"] / f"{cote}_tmp_extract"
    best = extract(pdf, tmp)
    out.mkdir(exist_ok=True)
    for pg, f in sorted(best.items()):
        with Image.open(f) as im:
            enhance(im).save(out / f"p{pg:04d}.jpg", quality=90, subsampling=0, optimize=True)
    shutil.rmtree(tmp)
    print(cote, len(best), "pages ->", out.relative_to(ROOT), flush=True)


def sample(cote, page, outdir):
    r = row(cote)
    pdf = ROOT / r["folder"] / r["file"]
    if not pdf.exists():
        pdf = ROOT / "cote_134_modelizing_story" / r["file"]
    outdir = pathlib.Path(outdir)
    best = extract(pdf, outdir / "tmp", page, page)
    with Image.open(best[page]) as im:
        im = im.convert("RGB")
        en = enhance(im)
        w, h = im.size
        box = (0, int(h * 0.15), w, int(h * 0.45))  # a band of text near the top
        pair = Image.new("RGB", (w, 2 * (box[3] - box[1]) + 20), "white")
        pair.paste(im.crop(box), (0, 0))
        pair.paste(en.crop(box), (0, box[3] - box[1] + 20))
        pair.thumbnail((1800, 1800))
        p = outdir / f"compare_{cote}_p{page}_g{GAMMA}.jpg"
        pair.save(p, quality=88)
    shutil.rmtree(outdir / "tmp")
    print(p)


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "sample":
        sample(sys.argv[2], int(sys.argv[3]), sys.argv[4])
    elif cmd == "cote":
        do_cote(sys.argv[2], "--force" in sys.argv)
    elif cmd == "all":
        for r in json.loads((ROOT / "MANIFEST.json").read_text(encoding="utf-8")):
            if r["file"] and (ROOT / r["folder"] / r["file"]).exists():
                do_cote(r["cote"])
