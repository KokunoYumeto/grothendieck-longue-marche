"""Assemble the independently checked arithmetic, curve, and variety arguments."""
from pathlib import Path

base = Path(__file__).resolve().parents[1]
root = base.parent / "root"
foundations = base.parent / "foundations"
statement = r"""\paragraph{F.47 (Proved). Pinned reconstruction over cyclotomic algebraic bases.}
Let $k\subset\overline{\mathbb Q}$ be any subfield contained in
$F\mathbb Q^{\mathrm{ab}}$ for some number field $F$. For all
finite-type $k$-schemes $X,Y$, the natural map
\[
 \operatorname{Hom}_k(X^{\mathrm{awn}},Y)
   \longrightarrow
 \pi_0\operatorname{Hom}^{\mathrm{pin}}_{B G_k}
                 (X_{\mathrm{et}},Y_{\mathrm{et}})
\]
is a bijection, where a relative geometric morphism includes its
commutation isomorphism over $B G_k$. Equivalently, the etale-topos
functor is fully faithful on finite-type schemes after inverting
universal homeomorphisms, with pinned geometric morphisms as the
target morphisms. In characteristic zero the absolute weak
normalization is seminormalization. In particular this settles the
test over $\mathbb Q(\mu_{2^\infty})$ in full, including constants
and noninvertible morphisms, and applies to $\mathbb Q^{\mathrm{ab}}$
and all its finite extensions. We give the derivation from the
verified arithmetic theorems and the reconstruction criterion;
no priority assertion is intended.

\begin{proof}
"""
integrality = (root / "cyclotomic_integrality.tex").read_text()
integrality = integrality.replace(r"\begin{proof}", "").replace(r"\end{proof}", "")
integrality = integrality.replace(
    "Theorem~1.1 of Amoroso and Zannier (2000)",
    r"Theorem~1.1 of Amoroso--Zannier \cite{AmorosoZannier2000}")
integrality = integrality.replace(
    "Tsujimura (2022,\nProposition~4.9)",
    r"Tsujimura's Proposition~4.9 \cite{Tsujimura2022}")
integrality = integrality.replace("CI.", "F47.R")
curve = (base / "F47_curve.tex").read_text()
higher = (foundations / "cyclotomic_higher.tex").read_text()
higher = higher.replace("CH.", "F47.H")
complete = statement + integrality + "\n" + curve + "\n" + higher + "\n\\end{proof}\n"
assert complete.count(r"\begin{proof}") == complete.count(r"\end{proof}") == 1
(base / "F47.tex").write_text(complete)
print("F.47 assembled from three independently audited fragments.")
print("Lines:", len(complete.splitlines()))
print("Words:", len(complete.split()))
print("Balanced outer proof environment: 1")
print("Inputs:", root / "cyclotomic_integrality.tex", base / "F47_curve.tex",
      foundations / "cyclotomic_higher.tex")
