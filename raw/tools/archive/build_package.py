"""Build one ChatGPT Pro transcription package from a cote of the Montpellier archive (user, 10 Nov 2026: one zip of
about 45 scans, sized so that a run works 60-80 minutes in the sandbox; the first package is checked, then the size is
tuned). Images as in the Longue Marche packages: the largest image of each PDF page, autocontrast (cutoff 1), unsharp
mask; plus two overlapping halves at full resolution. Blank pages (no ink against the paper) are left out and listed.

usage: python -I build_package.py COTE FIRST_SCAN COUNT [CONTEXT_DIR]
       -> C:\\Users\\user\\Documents\\grothendieck_archive_transcription_20261110\\packages\\MPL_<cote>_<first>-<last>\\
          PROMPT.md, MPL_..._scans.zip (and MPL_..._context.zip with CONTEXT_DIR): the upload set, nothing else (no subfolders); the manifest goes to ../packages_work/<package>/MANIFEST.json
          (user, 11 Nov 2026: the top level of a package folder holds only what is uploaded)
CONTEXT_DIR (11 Nov 2026, user: the notes should have "more bearing on our new knowledge"): a folder of our earlier work
on the neighbouring material (e.g. from build_lm_context.py), zipped as the second attachment; the prompt has the model
open it only after the transcription is written. Its first line of SUMMARY.txt, if present, names the contents in the
prompt. Without CONTEXT_DIR the template's <!-- CONTEXT --> blocks are dropped."""
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile

from PIL import Image, ImageFilter, ImageOps

sys.stdout.reconfigure(encoding="utf-8")
ARCH = pathlib.Path(r"C:\Users\user\Documents\grothendieck_archive_montpellier")
OUTROOT = pathlib.Path(r"C:\Users\user\Documents\grothendieck_archive_transcription_20261110")
TEMPLATE = OUTROOT / "ARCHIVE_PROMPT_TEMPLATE.md"


def row(cote):
    for r in json.loads((ARCH / "MANIFEST.json").read_text(encoding="utf-8")):
        if r["cote"] == cote:
            return r
    raise SystemExit("unknown cote " + cote)


def page_image(pdf, n, tmp):
    d = pathlib.Path(tmp) / f"p{n}"
    d.mkdir()
    subprocess.run(["pdfimages", "-j", "-png", "-f", str(n), "-l", str(n), str(pdf), str(d / "i")], check=True)
    imgs = sorted(d.iterdir(), key=lambda p: Image.open(p).size[0] * Image.open(p).size[1], reverse=True)
    return Image.open(imgs[0]).convert("RGB") if imgs else None


def ink(im):
    """Fraction of pixels clearly darker than the paper, in the central part of the page."""
    g = im.convert("L")
    w, h = g.size
    g = g.crop((int(w * .08), int(h * .03), int(w * .92), int(h * .94)))  # leaves out the archive's sheet number
    hist = g.histogram()
    tot = sum(hist)
    acc, med = 0, 0
    for v, c in enumerate(hist):
        acc += c
        if acc >= tot / 2:
            med = v
            break
    # 10 Nov: blank sheets measure about 0.00001 here, a sheet with three faint lines at the top 0.006 (cote 1, scan 41)
    return sum(hist[:max(0, med - 40)]) / tot


def main():
    cote, first, count = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    ctx = pathlib.Path(sys.argv[4]) if len(sys.argv) > 4 else None
    r = row(cote)
    pdf = ARCH / r["folder"] / r["file"]
    npages = int([l for l in subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout.splitlines()
                  if l.startswith("Pages:")][0].split()[1])
    kept, skipped, n = [], [], first
    with tempfile.TemporaryDirectory() as tmp:
        work = pathlib.Path(tmp) / "img"
        work.mkdir()
        while len(kept) < count and n <= npages:
            im = page_image(pdf, n, tmp)
            if im is None or ink(im) < 0.0003:
                skipped.append(n)
                n += 1
                continue
            kept.append((n, round(ink(im), 4)))
            im = ImageOps.autocontrast(im, cutoff=1).filter(ImageFilter.UnsharpMask(radius=2, percent=120, threshold=3))
            w, h = im.size
            if w > h:
                a, b = im.crop((0, 0, w // 2 + 60, h)), im.crop((w // 2 - 60, 0, w, h))
            else:
                a, b = im.crop((0, 0, w, h // 2 + 80)), im.crop((0, h // 2 - 80, w, h))
            n += 1
            kept[-1] = kept[-1] + ((w, h),)
            pk = f"S{kept[-1][0]:03d}"
            im.save(work / f"{pk}.jpg", quality=88)
            a.save(work / f"{pk}_a.jpg", quality=88)
            b.save(work / f"{pk}_b.jpg", quality=88)
        last = kept[-1][0]
        pkg = f"MPL_{cote}_{first:03d}-{last:03d}"
        out = OUTROOT / "packages" / pkg
        out.mkdir(parents=True, exist_ok=False)
        with zipfile.ZipFile(out / f"{pkg}_scans.zip", "w", zipfile.ZIP_STORED) as z:
            for f in sorted(work.iterdir()):
                num, rest = f.stem[1:4], f.stem[4:]
                z.write(f, f"{pkg}_scan{num}{rest}.jpg")
    skip_txt = ("scans " + ", ".join(map(str, skipped))) if skipped else "none"
    t = TEMPLATE.read_text(encoding="utf-8")
    summary = ""
    if ctx:
        with zipfile.ZipFile(out / f"{pkg}_context.zip", "w", zipfile.ZIP_DEFLATED) as z:
            for f in sorted(ctx.rglob("*")):
                if f.is_file() and f.name != "SUMMARY.txt":
                    z.write(f, f.relative_to(ctx).as_posix())
        s = ctx / "SUMMARY.txt"
        summary = s.read_text(encoding="utf-8").strip().splitlines()[0] if s.exists() else "see its README.md"
        t = re.sub(r"<!-- /?CONTEXT -->\n?", "", t)
    else:
        t = re.sub(r"<!-- CONTEXT -->.*?<!-- /CONTEXT -->\n?", "", t, flags=re.S)
    for k, v in {"{PKG}": pkg, "{COTE}": cote, "{COUNT}": str(len(kept)), "{TITLE}": r["title"], "{DATE}": r["date"],
                 "{SKIPPED}": skip_txt, "{CONTEXT_SUMMARY}": summary}.items():
        t = t.replace(k, v)
    (out / "PROMPT.md").write_text(t, encoding="utf-8")
    (out.parent.parent / "packages_work" / out.name).mkdir(parents=True, exist_ok=True)
    (out.parent.parent / "packages_work" / out.name / "MANIFEST.json").write_text(json.dumps(dict(package=pkg, cote=cote, source_pdf=str(pdf), url=r["url"],
                                                       title=r["title"], date=r["date"], scans=[k[0] for k in kept],
                                                       ink=[k[1] for k in kept], skipped_blank=skipped,
                                                       images_per_scan=3, enhancement="autocontrast cutoff 1; unsharp "
                                                       "mask r2 p120 t3; JPEG q88; halves overlap 80 px (60 for spreads)"),
                                                  ensure_ascii=False, indent=1), encoding="utf-8")
    zsize = (out / f"{pkg}_scans.zip").stat().st_size
    print(pkg, "| scans", kept[0][0], "-", last, "| kept", len(kept), "| skipped blank", skipped,
          "| zip MB", round(zsize / 1e6, 1), "->", out)


if __name__ == "__main__":
    main()
