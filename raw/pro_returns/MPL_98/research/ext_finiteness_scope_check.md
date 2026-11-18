# Ext base change: an elementary finiteness counterexample

**Check ID:** MPL98-EXT-BC01. **Reviewer:** ChatGPT, GPT-6 Astra Pro; inherited effort setting not exposed; run MPL98, agent `norm_research`. **Date:** November 18, 2026. The example was proposed by the root agent and independently checked here. This note checks algebra only; it does not inspect or interpret any manuscript wording or margin.

## Statement and verdict

Set

\[
A=B=\mathbf Z,\qquad
M=\bigoplus_{n\ge1}\mathbf Z,\qquad
N=\mathbf Z,\qquad A'=\mathbf Q.
\]

Then *B*, *M*, *N*, *A'*, and every `Ext^i_B(M,N)` are flat over *A*. Nevertheless the natural degree-zero base-change map

\[
\operatorname{Hom}_{\mathbf Z}(M,N)\otimes_{\mathbf Z}\mathbf Q
\longrightarrow
\operatorname{Hom}_{\mathbf Q}(M\otimes\mathbf Q,N\otimes\mathbf Q)
\]

is not surjective. **The proposed example is correct.**

## Independent verification

The module *M* is free, hence projective. Therefore

\[
\operatorname{Ext}_{\mathbf Z}^{i}(M,\mathbf Z)=0\quad(i>0),
\qquad
\operatorname{Hom}_{\mathbf Z}(M,\mathbf Z)
=\prod_{n\ge1}\mathbf Z.
\]

The product is torsion-free, so it is flat over the principal ideal domain `Z`. One can check this directly with the flatness criterion for finitely generated ideals: every such ideal is `dZ`, and `dZ⊗P→P` identifies with multiplication by *d* on `P=∏Z`, which is injective. The higher Ext groups are zero and thus flat. The remaining named modules are free or a localization of `Z`, hence flat.

Tensor product commutes with direct sums, giving

\[
M\otimes\mathbf Q=\bigoplus_{n\ge1}\mathbf Q,
\qquad
\operatorname{Hom}_{\mathbf Q}\left(\bigoplus_{n\ge1}\mathbf Q,\mathbf Q\right)
=\prod_{n\ge1}\mathbf Q.
\]

Writing `S=Z\setminus{0}`, the source is

\[
S^{-1}\left(\prod_{n\ge1}\mathbf Z\right).
\]

Every element has one denominator: it is represented by `(a_n)_{n≥1}/d`, where `a_n∈Z` and `d∈S`. Therefore the image consists exactly of rational sequences having a common nonzero integer denominator. The map is injective: if every `a_n/d` is zero, every *aₙ* is zero.

The sequence

\[
q_n=\frac1{n!},\qquad n\ge1,
\]

is a legitimate element of `∏Q`, hence a legitimate linear functional on `⊕Q`. It is not in the image: a common denominator *d* would require `d/n!∈Z` for all *n*, equivalently `n!` divides the nonzero integer *d* for all *n*. Choosing `n!>|d|` is a contradiction.

## Consequence for a termwise Hom argument

For a finite-rank free module *F*, `Hom(F,N)` is a finite direct sum of copies of *N*, so tensor product has the expected termwise base-change identification. For the infinite-rank free module above, Hom produces an infinite product, and localization does not commute with that product. The failure occurs already in degree zero, even though the base change itself is flat and all Ext groups are flat.

Thus flatness hypotheses alone cannot justify dropping the finiteness condition in this general termwise Hom proof. The example does not say that finite rank is logically necessary for every individual module/base-change pair, nor that other suitably finite resolutions are unavailable; it disproves the unrestricted generalization in precisely the proposed scope.
