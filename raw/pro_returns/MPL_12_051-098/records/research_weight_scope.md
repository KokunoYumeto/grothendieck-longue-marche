# Research support: a concrete failure of the unrestricted coefficient bound

Research only, 17 November 2026. No scan image was opened, and no frozen transcription, doubts, or inventory file was changed. This supplements the parent draft's **N002**; it is an explicit modern calculation, not a proposed transcription correction.

## W01 — The manuscript and context question

**Kind:** unpursued implication, now tested by an own calculation. **Frozen sources:** `pages/MPL_12_051-098_12_scan051.tex`, cote 12/051, “plus gén.” and “si M pur de poids ρ”; `pages/MPL_12_051-098_12_scan073.tex`, cote 12/073, “M motif ct tordu de poids ρ”; `pages/MPL_12_051-098_12_scan074.tex`, cote 12/074, an abelian scheme and its relative first cohomology. **Context searches:** `constant tordu`, `lisse`, `poids`, `coefficients`; **RS:** `MPL_14_002-044 B04` is an unreviewed research-note lead and `WG2 §2.4 #3` is an unchecked planning item, neither a reviewed theorem establishing this coefficient bound. The issue is whether the proposed upper bound \(\rho+\min(2i,2n)\), and the resulting vanishing conditions on 073, can apply to arbitrary pure lisse geometric coefficients.

## W02 — The supplied modernized reading permits the counterexample

**Kind:** contextual comparison. Hua's supplied interpretation `context/hua_project/12.modern.tex`, subsection “Motifs constants tordus, et leurs anneaux (pages 35 à 40)”, lines 993–1025, characterizes the effective category by lisse ℓ-adic realization and makes Tate twisting preserve the property; this is not a finite-geometric-monodromy restriction. The same file's later subsection B on twisted coefficients, lines 2165–2195, distinguishes the looser bounds obtained from a smooth projective family from the sharper bounds asked for in marginal questions. These are **Hua's AI-assisted modernized readings of leaves outside the frozen packet**, credited as such, and their original manuscript pages were not independently inspected; current 12/074 does independently concern a general abelian scheme.

## W03 — A simpler unconditional example than the proposed symmetric square

**Kind:** own calculation based on published explicit computations. Put \(k=\mathbf F_5\), \(U=\mathbf P^1_k\setminus\{0,1,\infty\}\), and let \(f:E\to U\) be the smooth projective Legendre elliptic scheme whose affine equation is \(y^2=x(x-1)(x-\lambda)\); set \(V=R^1f_*\mathbf Q_\ell\), \(\ell\ne5\), a lisse rank-two sheaf pure of weight one. Stacks Project Tag **03VA** explicitly computes that \(H_c^0(\bar U,V)=H_c^2(\bar U,V)=0\) and that \(H_c^1(\bar U,V)\) has dimension two and geometric-Frobenius eigenvalues \(1,1\), since \(-1\) is a square in \(k\). This is a scheme with the explicit smooth compactification \(\mathbf P^1_k\); no modular-stack interpretation or level convention is needed.

## W04 — The weight is four, exceeding the proposed upper bound three

**Kind:** own calculation; **confidence: high**, because only the preceding explicit computation and Poincaré duality enter. Fibre cup product gives \(V\otimes V\to\mathbf Q_\ell(-1)\) perfectly, hence \(V^\vee\simeq V(1)\); curve Poincaré duality therefore gives the Frobenius-equivariant identities

\[
H^1(\bar U,V)
 \simeq H_c^1(\bar U,V^\vee)^\vee(-1)
 \simeq H_c^1(\bar U,V)^\vee(-2).
\]

Consequently the eigenvalues are \(25,25\), so \(H^1(\bar U,V)\) is pure of weight **4**, whereas \(\rho=1\), \(i=n=1\) would give the upper bound **3**. This uses the standard convention that geometric Frobenius acts by \(q\) on \(\mathbf Q_\ell(-1)\); no assumption of Frobenius semisimplicity is used, and only the semisimplification is asserted to be \(\mathbf Q_\ell(-2)^{\oplus2}\).

## W05 — The proposed arithmetic vanishing also fails in this scope

**Kind:** own calculation; **confidence: high**, with the same normalization. For \(M=V(2)\), the coefficient weight is \(\rho=-3\), while the geometric-Frobenius eigenvalues on \(H^1(\bar U,M)\) are \(1,1\), so this group has a nonzero invariant vector even without a splitting assertion. The Hochschild–Serre exact sequence over the finite field surjects \(H^1(U,M)\) onto these invariants, proving \(H^1(U,M)\ne0\), although at \(i=1\) neither displayed condition on 12/073 holds: the first requires \(-3\le0\le-3\), and the second \(-2\le0\le-1\). Thus, under the general pure-lisse interpretation, this is a counterexample to both the asserted upper bound and its stated vanishing consequence, rather than merely a missing justification.

## W06 — The originally proposed symmetric-square example is consistent

**Kind:** own calculation from primary local-monodromy statements; **confidence: high**. Katz, *Convolution and Equidistribution*, author draft `mellin357.pdf`, chapter 15, pp. 77–78, explicitly gives purity of weight two, geometric monodromy \(\mathrm{SO}_3\), and a single tame unipotent block at each puncture for \(F=\operatorname{Sym}^2 V\); his *Twisted L-Functions and Monodromy*, author draft, printed p. 175 / PDF page 181, describes the split multiplicative fibre at \(\lambda=1\) with \(V^I=\mathbf Q_\ell\), \(V/V^I=\mathbf Q_\ell(-1)\). For \(j:U\hookrightarrow\mathbf P^1_k\), this gives \((R^1j_*F)_1=H^1(I,F)=\mathbf Q_\ell(-3)\), and absence of global geometric invariants implies \(H^2(\mathbf P^1_{\bar k},j_*F)=0\), so Leray makes this weight-six space a quotient of \(H^1(\bar U,F)\), exceeding \(\rho+2i=4\). The rank-two example above is preferable in the main notes because the exact compact-support computation is already printed explicitly.

## W07 — Appropriate scope of the conclusion

**Kind:** interpretation boundary. These calculations disprove the bound for **general pure lisse sheaves of geometric origin**, including relative first cohomology of a nonconstant abelian scheme, and explain why the distinction raised in N002 matters. They do not disprove the constant-coefficient bound or its extension when a coefficient becomes a constant pure Frobenius module after a finite étale cover, where descent and tensoring recover the usual upper bound. The archival conclusion should remain conditional on the intended definition of “constant tordu” until its original defining leaves are inspected; the modern mathematical counterexample itself is unconditional.

## Checked primary/author sources and tool references

1. **Stacks Project, §64.24, Tag 03VA, “The Legendre family”.** <https://stacks.math.columbia.edu/tag/03VA>. Exact family, lissity, vanishing, and characteristic polynomial \((1-T)^2\). Opened refs `turn196551735view0`, `turn610018403view2`, `turn108172923view1` (the last explicitly displays the eigenvalue passage).
2. **N. M. Katz, *Convolution and Equidistribution: Sato-Tate Theorems for Finite-Field Mellin Transforms*, author draft**, chapter 15, pp. 77–78. <https://web.math.princeton.edu/~nmk/mellin357.pdf>. Purity, geometric monodromy, and local monodromy for Legendre and its symmetric square. Opened refs `turn196551735view1`, `turn926997006view0`; the latter's find result includes both paragraphs in full. Pagination differs from other author versions.
3. **N. M. Katz, *Twisted L-Functions and Monodromy*, author draft dated 5 November 2001**, printed p. 175 / PDF page 181, proof of Theorem 8.9.2. <https://web.math.princeton.edu/~nmk/twistedLfctnov052001.pdf>. Explicit local decomposition-group representation at the Legendre split multiplicative fibre. Opened refs `turn196551735view2`, `turn926997006view1`, `turn946768447view0` (the last confirms printed pagination).
4. **J. S. Milne, *Lectures on Étale Cohomology*, v2.21 (2013)**, Theorem 14.7, printed p. 93, and Theorem 24.1, printed p. 144. <https://www.jmilne.org/math/CourseNotes/LEC.pdf>. Poincaré duality, first with finite coefficients; pass to ℓ-adic coefficients. Opened refs `turn610018403view0`, `turn778198416view3`, `turn778198416view4`; the surrounding §14 also supplies Hochschild–Serre over finite fields.
5. **K. S. Kedlaya, *Weil Cohomology in Practice*, “Étale fundamental groups”, Proposition 16.1.9** in the retrieved version. <https://kskedlaya.org/weil-cohom/Weil-cohom-18.html>. Explicit Galois-equivariant ℓ-adic duality pairing into \(\overline{\mathbf Q}_\ell(-n)\). Opened refs `turn610018403view1`, `turn778198416view5`.

Parent must open any source it wishes to cite in the user-facing response; these references are a handoff record, not evidence of parent inspection.
