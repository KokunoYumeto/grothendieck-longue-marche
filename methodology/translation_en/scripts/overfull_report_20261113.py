"""Which overfull boxes of the English reader are diagrams or displays running off the page, and by how much
(read-only, 13 Nov 2026). usage: python -I -B overfull_report_20261113.py [THRESHOLD_PT]"""
import re
import sys
from collections import Counter
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
D = Path(__file__).resolve().parent.parent / "reader"
thr = float(sys.argv[1]) if len(sys.argv) > 1 else 10.0
log = (D / "LaLongueMarche_English.log").read_text(encoding="utf-8", errors="replace")
src = (D / "LaLongueMarche_English.tex").read_text(encoding="utf-8").split("\n")
kinds = Counter()
big = []
page = 0
for m in re.finditer(r"\[(\d+)(?=[\s\]])|Overfull \\hbox \(([\d.]+)pt too wide\) (in paragraph at lines (\d+)--(\d+)|detected at line (\d+)|in alignment at lines (\d+)--(\d+))", log):
    if m.group(1):
        page = int(m.group(1))
        continue
    w = float(m.group(2))
    a = int(m.group(4) or m.group(6) or m.group(7))
    b = int(m.group(5) or m.group(6) or m.group(8))
    # look back from the line for the enclosing display
    ctx = "\n".join(src[max(0, a - 40):b])
    last = max(ctx.rfind("\\begin{tikzcd}"), ctx.rfind("\\["), ctx.rfind("\\begin{align"), ctx.rfind("\\begin{gather"))
    kind = "tikzcd" if "\\begin{tikzcd}" in ctx[last:] or "tikzcd" in "\n".join(src[a - 1:b]) else (
        "display" if m.group(6) or m.group(7) else "text")
    kinds[(kind, w > thr)] += 1
    if w > thr:
        big.append((w, page + 1, a, kind))
print("overfull boxes by kind (kind, wider than %.0fpt): " % thr, dict(kinds))
big.sort(reverse=True)
print("widest (pt, page about, source line, kind):")
for x in big[:25]:
    print("  %.1f  p.%d  l.%d  %s" % x)
print("pages with a diagram/display more than %.0fpt too wide:" % thr, sorted({p for w, p, a, k in big if k != "text"})[:80])
