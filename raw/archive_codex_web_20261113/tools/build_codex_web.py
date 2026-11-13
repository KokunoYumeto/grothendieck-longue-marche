"""Build the Codex-web drag folders of 13 Nov 2026 (Claude Opus 5.5, effort high): easy-to-read scans of the Montpellier
archive (typescripts with his corrections, typed and handwritten letters), for a ChatGPT work session with GPT-6 Astra
at reasoning effort high, one folder of about an hour each. Form of the Deligne drag folders
(deligne_codex_packets_20261112/drag/): flat folder with PROMPT.md, PREAMBLE.tex and <ID>_scans.zip (whole page plus
three overlapping thirds per scan, MANIFEST.tsv with SHA-256). Images as in the archive's Pro packages
(grothendieck_archive_tools_20261110/build_package*.py: largest image of the PDF page, autocontrast cutoff 1, unsharp
mask r2 p120 t3, JPEG q88), here in grayscale. Reads the archive PDFs only; writes only under codex_web_20261113/.

usage: python -I -B build_codex_web.py            (builds every folder in FOLDERS that does not exist yet)
"""
import hashlib
import io
import json
import pathlib
import re
import subprocess
import sys
import tempfile
import zipfile

from PIL import Image, ImageFilter, ImageOps

sys.stdout.reconfigure(encoding="utf-8")
ARCH = pathlib.Path.home() / "Documents" / "grothendieck_archive_montpellier"
HERE = pathlib.Path(__file__).resolve().parent
BASE = HERE.parent
TEMPLATE = HERE / "PROMPT_TEMPLATE_CODEX_WEB.md"
PREAMBLE = HERE / "PREAMBLE.tex"

# id, cote, scans (in order), material sentence(s) for the prompt
FOLDERS = [
    ("A57-01", "57", list(range(3, 14)),
     "They are a typescript in English, typed throughout, with handwritten corrections, insertions and symbols "
     "filled in by hand; the pages follow on from one another."),
    ("A57-02", "57", [20, 21, 22, 23, 73, 74, 75, 76, 77, 78, 79],
     "They are typed letters in English (scans 20-23, then scans 73-79), with handwritten corrections, insertions "
     "and signatures."),
    ("A29-01", "29",[3, 4, 5, 6, 8, 9, 10, 11, 12, 79, 80, 81],
     "They are letters in English: typed letters with handwritten corrections and signatures, a letter written by "
     "hand (scans 5-6), and typed comments (scans 80-81). Scan 7, a blank sheet, is left out."),
    ("A36-01", "36", list(range(10, 19)),
     "They are a typescript in French, typed with many handwritten corrections, insertions, margin notes and "
     "formulas filled in by hand; the pages follow on from one another, and the typescript goes on in scans 19-27 "
     "(another task)."),
    ("A36-02", "36", list(range(19, 28)),
     "They are a typescript in French, typed with many handwritten corrections, insertions, margin notes and "
     "formulas filled in by hand; the pages follow on from one another, and continue the typescript of scans 10-18 "
     "(another task)."),
]


# More folders (13 Nov 2026, user: every easy-to-read run for Codex web at GPT-6 Astra max): FOLDERS_EXTRA.json
_EXTRA = HERE / "FOLDERS_EXTRA.json"
if _EXTRA.exists():
    FOLDERS += [tuple(x) for x in json.loads(_EXTRA.read_text(encoding="utf-8"))]

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


def ink(im):  # as in build_package.py
    g = im.convert("L")
    w, h = g.size
    g = g.crop((int(w * .08), int(h * .03), int(w * .92), int(h * .94)))
    hist = g.histogram()
    tot = sum(hist)
    acc, med = 0, 0
    for v, c in enumerate(hist):
        acc += c
        if acc >= tot / 2:
            med = v
            break
    return sum(hist[:max(0, med - 40)]) / tot


def jpg(im):
    b = io.BytesIO()
    im.save(b, "JPEG", quality=88)
    return b.getvalue()


def thirds(im):
    w, h = im.size
    if w > h:
        s, o = w // 3, 60
        return [im.crop((0, 0, s + o, h)), im.crop((s - o, 0, 2 * s + o, h)), im.crop((2 * s - o, 0, w, h))]
    s, o = h // 3, 60
    return [im.crop((0, 0, w, s + o)), im.crop((0, s - o, w, 2 * s + o)), im.crop((0, 2 * s - o, w, h))]


def ranges(scans):
    out, a = [], scans[0]
    for p, q in zip(scans, scans[1:] + [None]):
        if q != p + 1:
            out.append(f"{a}" if a == p else f"{a}-{p}")
            a = q
    return ", ".join(out[:-1]) + " and " + out[-1] if len(out) > 1 else out[0]


def build(fid, cote, scans, material):
    out = BASE / "drag" / fid
    if (BASE / "done" / fid).exists():  # returned folders live in done/ (13 Nov 2026)
        print("done, skipped:", fid)
        return None
    if out.exists():
        print("exists, skipped:", out)
        return None
    r = row(cote)
    pdf = ARCH / r["folder"] / r["file"]
    files, man, inks = [], [], {}
    with tempfile.TemporaryDirectory() as tmp:
        for n in scans:
            im = page_image(pdf, n, tmp)
            if im is None or ink(im) < 0.0003:
                raise SystemExit(f"{fid}: cote {cote} scan {n} is blank or has no image")
            inks[n] = round(ink(im), 4)
            im = ImageOps.autocontrast(im.convert("L"), cutoff=1).filter(ImageFilter.UnsharpMask(radius=2, percent=120, threshold=3))
            stem = f"{fid}_{cote}_scan{n:03d}"
            for part, sub in [("whole", im)] + [(f"s{i}", t) for i, t in enumerate(thirds(im), 1)]:
                name = stem + ("" if part == "whole" else "_" + part) + ".jpg"
                data = jpg(sub)
                files.append((name, data))
                man.append((name, len(data), hashlib.sha256(data).hexdigest(), cote, n, part, sub.size[0], sub.size[1]))
    out.mkdir(parents=True)
    mtsv = "file\tbytes\tsha256\tcote\tscan\tpart\twidth\theight\n" + "".join("\t".join(map(str, m)) + "\n" for m in man)
    with zipfile.ZipFile(out / f"{fid}_scans.zip", "w", zipfile.ZIP_STORED) as z:
        z.writestr("MANIFEST.tsv", mtsv)
        for name, data in files:
            z.writestr(name, data)
    t = TEMPLATE.read_text(encoding="utf-8")
    for k, v in {"{ID}": fid, "{COTE}": cote, "{TITLE}": r["title"], "{DATE}": r["date"], "{COUNT}": str(len(scans)),
                 "{SCANS}": ranges(scans), "{MATERIAL}": material}.items():
        t = t.replace(k, v)
    left = re.findall(r"\{(?:ID|COTE|TITLE|DATE|COUNT|SCANS|MATERIAL)\}", t)
    if left:
        raise SystemExit(f"placeholders left: {left}")
    (out / "PROMPT.md").write_text(t, encoding="utf-8")
    (out / "PREAMBLE.tex").write_bytes(PREAMBLE.read_bytes())
    z = out / f"{fid}_scans.zip"
    with zipfile.ZipFile(z) as zz:
        assert zz.testzip() is None and len(zz.namelist()) == 1 + 4 * len(scans)
    rec = dict(id=fid, cote=cote, scans=scans, ink=inks, pdf=str(pdf).replace(pathlib.Path.home().name, "user"), url=r["url"], title=r["title"], date=r["date"],
               zip_mb=round(z.stat().st_size / 1e6, 1), zip_sha256=hashlib.sha256(z.read_bytes()).hexdigest())
    print(json.dumps(rec, ensure_ascii=False))
    return rec


if __name__ == "__main__":
    recs = []
    for f in FOLDERS:
        try:
            x = build(*f)
        except SystemExit as e:
            print("FOLDER FAILED:", f[0], e)
            continue
        if x:
            recs.append(x)
    log = HERE / "BUILD_LOG.jsonl"
    with open(log, "a", encoding="utf-8") as f:
        for x in recs:
            f.write(json.dumps(x, ensure_ascii=False) + "\n")
