# Root review of the henselization obstruction F.47

**Date:** 14 November 2026. **Verdict:** PASS for the complete candidate in
`audit/F_henselization_obstruction_candidate.md`, Sections 1--8. The intrinsic
converse classification F.9 remains unresolved. This review addresses the
closed-point-preserving relative-topos convention, not the already refuted
literal R27 formulation.

We read the full original candidate and its notation-clean revision. We also
reread the entire integrated proofs of F.32 and F.40 and the algebraic-closure,
trace, substitution and cardinality portions of F.42 on which the new proof
relies. We reran `code/F_Puiseux_checks.py`: all 27 exact rational identities
passed. Those truncated-series checks verify the finite algebraic formulas;
they do not replace the infinite field and topos proofs.

## 1. Ordinary henselization and the exact closure

Root independently opened and read The Stacks Project, Example 16.13.3,
Tag 0A1W, https://stacks.math.columbia.edu/tag/0A1W (`turn844view0`), together
with Definition 15.53.1, Lemma 15.53.2 and Proposition 15.53.3 in Tag 07QS,
https://stacks.math.columbia.edu/tag/07QS (`turn844view1`). The hypotheses
apply to the excellent local domain \(R=F[t]_{(t)}\). Its henselization is
exactly the algebraic-over-F(t) part of F[[t]]. Multiplication by a power of t
then identifies its fraction field with

\[
 A_0(F)=F((t))\cap F(t)^{\mathrm{alg}}.
\]

The closure used is the bounded-coefficient union of finite Puiseux levels,
not the full series field over an algebraic closure of F. Its algebraic-over-
F(t) part is algebraically closed by transitivity of algebraicity and hence
is an algebraic closure of A0(F).

The Fourier projection in (47.8) has the correct exponent and normalization:
the sum over roots of unity keeps precisely powers congruent to j modulo n,
and multiplication by u^(-j) makes their exponents multiples of n. Every
projected series remains algebraic over F(t). Applying a trace-dual basis to
its coefficient field gives finitely many series in F((t)) that remain
algebraic over F(t), so they belong to A0(F). Consequently

\[
 \Omega_0=\bigcup_{F'/F\,\mathrm{finite},\ n\ge1}A_0(F)F'(t^{1/n})
\]

is an equality of ordinary fields. No exchange of a field automorphism with
an unbounded infinite sum is needed in the later commutation proof.

Coefficientwise linear independence verifies the constant-extension degrees.
The inherited valuation has value group Z, and X^n-t is Eisenstein. After
adjoining roots of unity, the ramified pieces are cyclic of exact degree n.
Thus restriction and the coefficientwise splitting give the claimed
topological semidirect product Zhat(1) semidirect G_F, with cyclotomic action.

## 2. The substitution centralizes the entire absolute Galois group

Substitution by t+t^2 and by its inverse
\(r(t)=(-1+\sqrt{1+4t})/2\) preserve A0(F) in both directions, because
their images of t are algebraic over F(t). The compatible lift on each root
t^(1/n) uses the constant-term-one root of 1+t. These roots belong to A0(F)
itself, a fact that handles inertia as well as the coefficient Galois action.

For any g in G_A0, the maps g tau and tau g agree on A0, on the algebraic
constant field, and on every t^(1/n). The proved field-generation equality
makes them equal everywhere. This is stronger than checking the quotient
G_F alone. The induced field automorphism is nonidentity because it moves t.

## 3. Full-topos witness and algebraic-extension direction

F.40 supplies the structural isomorphism over BG_A0 from the trivial outer
Galois action. The underlying absolute scheme map is an isomorphism, so it
preserves closed points. Its rational-point function is sigma inverse, as
seen by pulling back the ideals (T-a). A relative algebraic map of Gm would
be cT^m; its values at 1 and 2 force c=1 and m=1, contradicted by the value
r(t) at t. Thus the witness concerns the full small etale topos, not merely
its fundamental group or its point set.

If an algebraic extension E/A0 reconstructed, F.32 would force A0 to
reconstruct. Its contrapositive therefore excludes every such E. The proof
correctly avoids claiming that sigma preserves an arbitrary E. Excluding
the smaller A0 directly strengthens F.42's earlier Puiseux-core example;
the direction could not be reversed just from the older negative result.

## 4. Intrinsic valuation corollary

Root independently opened the author PDF of Aschenbrenner, van den Dries,
and van der Hoeven, *Asymptotic differential algebra and model theory of
transseries*, https://www.math.ucla.edu/~matthias/pdf/mt.pdf. We read
Proposition 3.3.8 and Lemma 3.3.9, printed pp.117--118, including their full
proofs (`turn846view0`), and the henselization universal property preceding
Proposition 3.3.25, printed p.125 (`turn846view1`). The PDF has729 physical
pages; the stated numbers are the author's printed pages.

The candidate also proves the required coefficient-field statement directly.
A maximal subfield of the valuation ring maps injectively to the residue
field. A missing transcendental residue element gives a larger subfield by
lifting it; a missing algebraic residue element gives one by Hensel's lemma
and characteristic-zero separability. Thus the residue map is onto that
field. This argument holds for a henselian valuation of arbitrary rank.

For any nonzero t in the maximal ideal, the least nonzero exponent in a
polynomial over the coefficient field gives its unique least-valued term.
Hence t is transcendental and the restricted valuation ring on F(t) is
exactly F[t]_(t). If trdeg_Q K=d and trdeg_Q residue=d-1, then K/F(t) is
algebraic. Henselization universality embeds A0(F) into K over the chosen
F(t), and K is algebraic over its image. The preceding exclusion applies.
No discreteness assumption is needed. The precise residue-degree hypothesis
is indispensable to this argument and is retained in the theorem.

**Approved for integration after the independent review:** the ordinary
henselization counterexample, its algebraic-extension consequence, the exact
full tame Galois description, and the stated intrinsic henselian-valuation
obstruction. No sufficiency criterion or priority claim is inferred.


## Integrated proof readback

Root subsequently read all of `sections/F_henselization_obstruction_extension.tex`, including all13 equation tags, the full-field generator proof, actual relative-topos witness, algebraic-extension contrapositive and nondiscrete valuation corollary. The accepted proof is retained, and the inclusion A0(F) into the earlier Puiseux core is now explicit. Integrated F.47 passes.
