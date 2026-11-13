"""Contact sheets for the visual check of a reader (13 Nov 2026): the pages on which the typesetting pass changed
something (the LMFIT lines of the log), the pages that hold the places of an earlier build's overfull boxes wider than
10pt (found again through the [scan n] marks), and N pages spread over the book; 20 pages to a sheet (5 x 4), each
page with its number, rendered with mutool and joined with ImageMagick.
usage: python -I -B contact_sheets_20261113.py READER.tex OUT_DIR [--before OLD.tex OLD.log] [--spread N] [--max M]"""
import pathlib
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
tex = pathlib.Path(sys.argv[1])
out = pathlib.Path(sys.argv[2])
out.mkdir(parents=True, exist_ok=True)
a = sys.argv[3:]
pdf, log = tex.with_suffix(".pdf"), tex.with_suffix(".log").read_text(encoding="utf-8", errors="replace")
src = tex.read_text(encoding="utf-8").split("\n")
BS = chr(92)


def marks(lines):
    """[(line, ordinal of the scan mark)] of a reader source"""
    return [(i + 1, k) for k, i in enumerate(j for j, l in enumerate(lines) if l.startswith(BS + "scanpage{"))]


txt = subprocess.run(["mutool", "draw", "-F", "txt", "-o", "-", str(pdf)], capture_output=True).stdout.decode(
    "utf-8", errors="replace").split("\f")
page_of = []  # page of the k-th [scan n] mark
for p, t in enumerate(txt, 1):
    page_of += [p] * len(re.findall(r"\[scan \d+\]", t))
npages = len([t for t in txt if t.strip()]) or len(txt)
M = marks(src)


def page_at(line, mk):
    """the page of a source line, by its place between two scan marks"""
    prev = [(l, k) for l, k in mk if l <= line]
    if not prev:
        return 1
    l1, k = prev[-1]
    if k >= len(page_of):
        return page_of[-1]
    p1 = page_of[k]
    if k + 1 < len(mk) and k + 1 < len(page_of):
        l2, p2 = mk[k + 1][0], page_of[k + 1]
        return p1 + int((line - l1) / max(1, l2 - l1) * (p2 - p1) + 0.5) if p2 > p1 else p1
    return p1


chosen = {}
for m in re.finditer(r"^LMFIT (\w+) scale ([\d.]+) at input line (\d+)", log, re.M):
    chosen.setdefault(page_at(int(m.group(3)), M), []).append("%s %.2f" % (m.group(1), float(m.group(2))))
n_pass = len(chosen)
if "--before" in a:
    otex = pathlib.Path(a[a.index("--before") + 1]).read_text(encoding="utf-8").split("\n")
    olog = pathlib.Path(a[a.index("--before") + 2]).read_text(encoding="utf-8", errors="replace")
    OM = marks(otex)
    for m in re.finditer(r"Overfull " + BS * 2 + r"hbox \(([\d.]+)pt too wide\) (?:in paragraph at lines (\d+)--\d+|detected at line (\d+))", olog):
        if float(m.group(1)) > 10:
            line = int(m.group(2) or m.group(3))
            prev = [(l, k) for l, k in OM if l <= line]
            if prev and prev[-1][1] < len(M):
                l1, k = prev[-1]
                l2 = OM[k + 1][0] if k + 1 < len(OM) else l1 + 1
                n1 = M[k][0]
                n2 = M[k + 1][0] if k + 1 < len(M) else n1 + 1
                chosen.setdefault(page_at(n1 + int((line - l1) / max(1, l2 - l1) * (n2 - n1)), M), []).append(
                    "was %.0fpt" % float(m.group(1)))
n_before = len(chosen) - n_pass
spread = int(a[a.index("--spread") + 1]) if "--spread" in a else 20
for i in range(spread):
    chosen.setdefault(1 + int((i + 0.5) * npages / spread), []).append("spread")
pages = sorted(chosen)
if "--max" in a:
    pages = pages[:int(a[a.index("--max") + 1])]
print("pages chosen:", len(pages), "| with a change of the pass:", n_pass, "| more with an earlier overflow > 10pt:",
      n_before, "| of", npages)
(out / "PAGES.txt").write_text("\n".join("%d\t%s" % (p, "; ".join(chosen[p])) for p in pages), encoding="utf-8")
subprocess.run(["mutool", "draw", "-r", "38", "-o", str(out / "p%04d.png"), str(pdf), ",".join(map(str, pages))],
               capture_output=True)
pngs = sorted(out.glob("p*.png"))
for f, p in zip(pngs, pages):
    f.rename(out / ("n%04d.png" % p))
names = [str(out / ("n%04d.png" % p)) for p in pages]
for s in range(0, len(names), 20):
    args = ["magick", "montage"]
    for nme in names[s:s + 20]:
        args += ["-label", str(int(pathlib.Path(nme).stem[1:])), nme]
    subprocess.run(args + ["-tile", "5x4", "-geometry", "+2+1", "-background", "#888", "-pointsize", "11",
                           str(out / ("sheet_%02d.png" % (s // 20 + 1)))], capture_output=True)
for nme in names:
    pathlib.Path(nme).unlink()
print("sheets:", len(list(out.glob("sheet_*.png"))))
