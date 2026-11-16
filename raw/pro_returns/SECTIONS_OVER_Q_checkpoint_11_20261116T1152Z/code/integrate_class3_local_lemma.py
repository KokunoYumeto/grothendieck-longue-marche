#!/usr/bin/env python3
"""Place the exact coefficient-prime lemma inside the proved A.59."""
from pathlib import Path

root = Path(__file__).resolve().parents[1] / "sections"
lemma = root / "class3_coefficient_prime_lemma.tex"
paper = root / "class3_ghost_construction.tex"
local = lemma.read_text()
local = local.replace("CP.", "A.59.C")
local = local.replace(r"\begin{proof}", r"\emph{Proof of the local image formula.}")
local = local.replace("\\end{proof}\n", "")
lemma.write_text(local)
text = paper.read_text().replace("CP.", "A.59.C")
line = "\\input{sections/class3_coefficient_prime_lemma.tex}\n"
text = text.replace(line, "")
text = text.replace(r"\emph{The all-place invariant.}", line + "\n" + r"\emph{The all-place invariant.}")
text = text.replace("There is an ordinary completed unit-equation pair in the",
                    "There is an infinite-support ordinary completed unit-equation pair in the")
paper.write_text(text)
print("Placed the supporting local calculation inside A.59 and renamed its tags A.59.C1--C11.")
