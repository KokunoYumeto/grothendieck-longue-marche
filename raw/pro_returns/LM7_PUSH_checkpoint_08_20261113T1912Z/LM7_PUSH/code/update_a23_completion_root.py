#!/usr/bin/env python3
"""Preserve the superseded A.23 gap and install its proved synthesis."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
path = ROOT / "sections/A_root.tex"
source = path.read_text()
start = source.index(r"\begin{statement}{A.23}{Open}")
end = source.index(r"\subsection{Explicit nine-torsion covers", start)
retained = ROOT / "research/A23_superseded_checkpoint04.tex"
assert not retained.exists(), "Do not overwrite the preserved former gap"
retained.write_text(source[start:end])
replacement = r"""\begin{statement}{A.23}{Proved}{The complete higher images and fibers in Task A.6}
For each of $G=N/N''$ and $G=N/\gamma_3(I_{\rm mark})$,
let $X_n(s,G)$, $G_n$, $A_n$ and $J_n$ be the explicitly
constructed finite arithmetic data of A.43 for an exact
class-two target $s$. Then the image consists exactly of
the classes satisfying
\[
             X_n(s,G)\ne\varnothing\quad\text{for every }n,
\]
and its entire fiber is
\[
                  \varprojlim_n X_n(s,G)/J_n^c.
\]
Every finite test terminates and uses the actual based
arithmetic action and finite target table. The inherited
ramification constraints give its transition maps, including
for infinitely ramified targets. The lower-central quotients
of A.21 are cofinal for the same section problem. Their
metabelian coefficient lattices and derived limits are A.22;
their marked coefficient lattices and derived limits are A.44.
The exact maps to the inherited quotients, with both kernels,
are (A.44.2).
\end{statement}
\begin{proof}
The two geometric kernels are closed and arithmetic-stable.
The quotient maps in (A.43.2) are their actual finite images,
and (A.43.8) identifies their inverse limits with the specified
groups. Normalization at complex conjugation is possible
inside each pro-three lifting kernel. A.43 proves the
uniform ramification bound from the abelian target and
enumerates every possible finite graph field within its
explicit degree and discriminant bounds. The resulting
finite sets therefore give both directions of the image
criterion, with continuous compatible cocycles.

For the fiber, A.43 proves that the image of the actual
geometric kernel is $J_n$, and that its $c$-fixed subgroup
surjects onto $J_n^c$. The global class-two centralizer is
trivial. Its compact conjugator comparison consequently
gives precisely the displayed inverse limit of orbits.
No extra finite-level centralizer is divided out.

A.21 proves both the group and section-class comparisons
with the stated finite-rank lower-central towers. A.22 and
A.44 identify the actual coefficient lattices and actions;
their residue formulas use the image on restricted integral
families and retain its nonzero first derived limit at every
positive higher layer. Thus convergence has not been
replaced by independent local solvability. Formula (A.44.2)
comes from the same based Fermat covering and gives the
requested inherited comparisons. These statements together
settle every image, fiber, cofinality and coefficient-layer
requirement of Task A.6. The finite arithmetic stages form
an infinite criterion; no total stopping algorithm is used.
\end{proof}

"""
path.write_text(source[:start] + replacement + source[end:])
print("Preserved former A.23 in research/A23_superseded_checkpoint04.tex")
print("Installed proved A.23 synthesis from A.21--A.22 and A.43--A.44")
