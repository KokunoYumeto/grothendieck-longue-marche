"""How much of the manuscript is running text and how much is display (diagrams, displayed formulas), in the French
transcription and in the English, per cote and in total (read-only, 13 Nov 2026). Running text = everything outside
display environments, with LaTeX commands and inline math removed. usage: python -I -B text_vs_diagrams_20261113.py"""
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
BS = chr(92)
D = Path(__file__).resolve().parent.parent
DISP = re.compile(r"\\\[.*?\\\]|\\begin\{(tikzcd|equation\*?|align\*?|gather\*?|multline\*?|array|CD|tikzpicture|eqnarray\*?)\}.*?\\end\{\1\}|\$\$.*?\$\$", re.S)


def parts(t):
    t = re.sub(r"(?<!\\)%.*", "", t)
    disp = sum(len(m.group(0)) for m in DISP.finditer(t))
    body = DISP.sub(" ", t)
    body = re.sub(r"\$[^$]*\$", " ", body)
    body = re.sub(r"\\[A-Za-z]+\*?(\[[^\]]*\])?", " ", body)
    body = re.sub(r"[{}\\]", " ", body)
    words = len(re.findall(r"[A-Za-zÀ-ÿ]{2,}", body))
    return disp, words


tot = defaultdict(lambda: [0, 0, 0, 0])
for f in sorted((D / "source" / "units").glob("*.tex")):
    pk = f.stem.rsplit("_s", 1)[0]
    cote = pk.split("-")[0]
    dfr, wfr = parts(f.read_text(encoding="utf-8"))
    tot[cote][0] += dfr
    tot[cote][1] += wfr
for f in sorted((D / "translation" / "packages").glob("*_en.tex")):
    cote = f.stem[:-3].split("-")[0]
    den, wen = parts(f.read_text(encoding="utf-8"))
    tot[cote][2] += den
    tot[cote][3] += wen
print("cote | FR display chars | FR words of running text | EN display chars | EN words | EN/FR words")
for c, (a, b, x, y) in sorted(tot.items()):
    print(c, "|", a, "|", b, "|", x, "|", y, "|", round(y / b, 2) if b else "-")
A = [sum(v[i] for v in tot.values()) for i in range(4)]
print("ALL |", A[0], "|", A[1], "|", A[2], "|", A[3], "|", round(A[3] / A[1], 2))
