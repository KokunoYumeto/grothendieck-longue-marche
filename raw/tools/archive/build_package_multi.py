"""Build one ChatGPT Pro transcription package from SEVERAL cotes of the Montpellier archive (11 Nov 2026; the plan's
"multi-cote option", PLAN_EVERYTHING.md: the small cotes of one rank share a package). Same images, same template and
same rules as build_package.py; the prompt is the template with the cote-specific places rewritten for several files:
images and page files carry the cote (`<PKG>_<cote>_scanNNN.jpg`), each file's pages open with `\\cotefile{C}`, and the
inventory gains a `cote` column.

usage: python -I build_package_multi.py SPEC [SPEC ...] [--context DIR] [--name NAME]
  SPEC = COTE (all scans) or COTE:FIRST-LAST (inclusive). Blank scans are dropped and listed, as in build_package.py.
  -> ...\\grothendieck_archive_transcription_20261110\\packages\\<NAME or MPL_<spec1>+<spec2>...>\\ PROMPT.md, _scans.zip
     (and _context.zip); the manifest goes to ../packages_work/<package>/MANIFEST.json
"""
import json
import pathlib
import re
import subprocess
import sys
import tempfile
import zipfile

from PIL import ImageFilter, ImageOps

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build_package import ARCH, OUTROOT, TEMPLATE, ink, page_image, row  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")


def npages(pdf):
    out = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout
    return int([l for l in out.splitlines() if l.startswith("Pages:")][0].split()[1])


def sub_once(t, old, new):
    if t.count(old) != 1:
        raise SystemExit(f"template changed: expected exactly one {old!r}, found {t.count(old)}")
    return t.replace(old, new)


def main():
    a = sys.argv[1:]
    ctx = name = None
    if "--context" in a:
        i = a.index("--context"); ctx = pathlib.Path(a[i + 1]); del a[i:i + 2]
    if "--name" in a:
        i = a.index("--name"); name = a[i + 1]; del a[i:i + 2]
    specs = []
    for s in a:
        cote, _, rng = s.partition(":")
        r = row(cote)
        pdf = ARCH / r["folder"] / r["file"]
        n = npages(pdf)
        first, last = (int(x) for x in rng.split("-")) if rng else (1, n)
        specs.append(dict(cote=cote, row=r, pdf=pdf, first=first, last=min(last, n), whole=not rng or (first == 1 and last >= n)))
    pkg = name or "MPL_" + "+".join(s["cote"] if s["whole"] else f'{s["cote"]}_{s["first"]:03d}-{s["last"]:03d}' for s in specs)
    out = OUTROOT / "packages" / pkg
    if out.exists():
        raise SystemExit(f"exists: {out}")
    kept_all = []
    with tempfile.TemporaryDirectory() as tmp:
        work = pathlib.Path(tmp) / "img"
        work.mkdir()
        for s in specs:
            s["kept"], s["skipped"] = [], []
            ctmp = pathlib.Path(tmp) / f'c_{s["cote"]}'  # page_image makes p<N> per scan: one folder per cote
            ctmp.mkdir()
            for n in range(s["first"], s["last"] + 1):
                im = page_image(s["pdf"], n, ctmp)
                if im is None or ink(im) < 0.0003:
                    s["skipped"].append(n)
                    continue
                s["kept"].append((n, round(ink(im), 4)))
                im = ImageOps.autocontrast(im, cutoff=1).filter(ImageFilter.UnsharpMask(radius=2, percent=120, threshold=3))
                w, h = im.size
                if w > h:
                    p1, p2 = im.crop((0, 0, w // 2 + 60, h)), im.crop((w // 2 - 60, 0, w, h))
                else:
                    p1, p2 = im.crop((0, 0, w, h // 2 + 80)), im.crop((0, h // 2 - 80, w, h))
                stem = f'{pkg}_{s["cote"]}_scan{n:03d}'
                im.save(work / f"{stem}.jpg", quality=88)
                p1.save(work / f"{stem}_a.jpg", quality=88)
                p2.save(work / f"{stem}_b.jpg", quality=88)
            kept_all += [(s["cote"], k[0]) for k in s["kept"]]
        out.mkdir(parents=True, exist_ok=False)
        with zipfile.ZipFile(out / f"{pkg}_scans.zip", "w", zipfile.ZIP_STORED) as z:
            for f in sorted(work.iterdir()):
                z.write(f, f.name)
    count = len(kept_all)
    cotes = [s["cote"] for s in specs]
    cote_list = ", ".join(cotes[:-1]) + " and " + cotes[-1] if len(cotes) > 1 else cotes[0]
    files = "\n".join(f'- `{s["cote"]}.pdf`: "{s["row"]["title"]}" ({s["row"]["date"]}), scans {s["first"]}-{s["last"]}, '
                      f'{len(s["kept"])} pages kept' for s in specs)
    skipped = "; ".join(f'`{s["cote"]}.pdf` scans ' + ", ".join(map(str, s["skipped"])) for s in specs if s["skipped"]) or "none"
    t = TEMPLATE.read_text(encoding="utf-8")
    t = sub_once(t, "the Montpellier archive, cote {COTE}", "the Montpellier archive, cotes " + cote_list)
    t = sub_once(t, """**{COUNT} scan pages** of the Montpellier archive file `{COTE}.pdf`: "{TITLE}" ({DATE}). For every scan page N there
are three images: `{PKG}_scanNNN.jpg` (the whole page) and `{PKG}_scanNNN_a.jpg`, `{PKG}_scanNNN_b.jpg` (its top and""",
                 """**{COUNT} scan pages** from """ + str(len(specs)) + """ files of the Montpellier archive, separate folders of notes, in this
order:
""" + files + """

Transcribe the files in this order. For every scan page N of file C there are three images: `{PKG}_C_scanNNN.jpg` (the
whole page) and `{PKG}_C_scanNNN_a.jpg`, `{PKG}_C_scanNNN_b.jpg` (its top and""")
    t = sub_once(t, "N is the page\nnumber in the archive's PDF.", "N is the page\nnumber in that file's PDF.")
    t = sub_once(t, "   - `\\scanpage{N}` at the top of each scan page (N as above);",
                 "   - `\\cotefile{C}` before the first page of each archive file C (for example `\\cotefile{" + cotes[0] + "}`);\n"
                 "   - `\\scanpage{N}` at the top of each scan page (N as above, the page number within its file);")
    t = sub_once(t, "write it to its own file `pages/{PKG}_scanNNN.tex`", "write it to its own file `pages/{PKG}_C_scanNNN.tex`")
    t = sub_once(t, "append a line `scan NNN done <current UTC time>`", "append a line `C scan NNN done <current UTC time>`")
    t = sub_once(t, "starting with\n   `\\scanpage{N}` of the first page,", "starting with\n   `\\cotefile{C}` and `\\scanpage{N}` of the first page,")
    t = sub_once(t, "a table of doubts (scan page, line", "a table of doubts (file, scan page, line")
    t = sub_once(t, "(columns `scan,element,kind,", "(columns `cote,scan,element,kind,")
    t = sub_once(t, "One note per item: scan page (and line", "One note per item: file and scan page (and line")
    summary = ""
    if ctx:
        with zipfile.ZipFile(out / f"{pkg}_context.zip", "w", zipfile.ZIP_DEFLATED) as z:
            for f in sorted(ctx.rglob("*")):
                if f.is_file() and f.name != "SUMMARY.txt":
                    z.write(f, f.relative_to(ctx).as_posix())
        sfile = ctx / "SUMMARY.txt"
        summary = sfile.read_text(encoding="utf-8").strip().splitlines()[0] if sfile.exists() else "see its README.md"
        t = re.sub(r"<!-- /?CONTEXT -->\n?", "", t)
    else:
        t = re.sub(r"<!-- CONTEXT -->.*?<!-- /CONTEXT -->\n?", "", t, flags=re.S)
    for k, v in {"{PKG}": pkg, "{COUNT}": str(count), "{SKIPPED}": skipped, "{CONTEXT_SUMMARY}": summary}.items():
        t = t.replace(k, v)
    left = re.findall(r"\{(?:COTE|TITLE|DATE|PKG|COUNT|SKIPPED|CONTEXT_SUMMARY)\}", t)
    if left:
        raise SystemExit(f"placeholders left in the prompt: {left}")
    (out / "PROMPT.md").write_text(t, encoding="utf-8")
    wd = out.parent.parent / "packages_work" / out.name
    wd.mkdir(parents=True, exist_ok=True)
    (wd / "MANIFEST.json").write_text(json.dumps(dict(
        package=pkg, files=[dict(cote=s["cote"], source_pdf=str(s["pdf"]), url=s["row"]["url"], title=s["row"]["title"],
                                 date=s["row"]["date"], scans=[k[0] for k in s["kept"]], ink=[k[1] for k in s["kept"]],
                                 skipped_blank=s["skipped"]) for s in specs],
        context=str(ctx) if ctx else None, images_per_scan=3,
        enhancement="autocontrast cutoff 1; unsharp mask r2 p120 t3; JPEG q88; halves overlap 80 px (60 for spreads)"),
        ensure_ascii=False, indent=1), encoding="utf-8")
    zsize = (out / f"{pkg}_scans.zip").stat().st_size
    print(pkg, "| files", " ".join(f'{s["cote"]}:{s["first"]}-{s["last"]} kept {len(s["kept"])} skipped {s["skipped"]}' for s in specs),
          "| total", count, "| zip MB", round(zsize / 1e6, 1), "->", out)


if __name__ == "__main__":
    main()
