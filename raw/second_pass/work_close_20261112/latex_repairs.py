"""LaTeX-only repairs (the reading is unchanged) of current texts that do not compile even after the reader build's
mechanical repairs. Each edit is an exact, unique replacement, written to second_pass/PKG_checked_fixed.tex (created
from PKG_checked.tex if needed). usage: python -I latex_repairs.py"""
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
SP = pathlib.Path(__file__).resolve().parent.parent
B = "\\"
E = [
    # a math letter in text mode inside a deletion
    ("LM_P065", "car " + B + "deleted{" + B + "unsure{" + B + "mathfrak S}} le centre",
     "car " + B + "deleted{" + B + "unsure{$" + B + "mathfrak S$}} le centre"),
    # \capB read as one control sequence: T_alpha cap B'_0
    ("LM_C3-302-320", "T_" + B + "alpha" + B + "capB'_0", "T_" + B + "alpha" + B + "cap B'_0"),
]
for pkg, old, new in E:
    out = SP / f"{pkg}_checked_fixed.tex"
    src = out if out.exists() else SP / f"{pkg}_checked.tex"
    t = src.read_text(encoding="utf-8")
    if new in t and old not in t:
        print(pkg, "already repaired")
        continue
    n = t.count(old)
    if n != 1:
        print(pkg, "NOT repaired: found", n, repr(old))
        continue
    out.write_text(t.replace(old, new), encoding="utf-8")
    print(pkg, "repaired ->", out.name)
