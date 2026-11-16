# Intrinsic anti-chains and an equivariant common refinement

Date: 2026-11-16. Proposed research lemma following B91–B92.
The statements below are discrete and integral. They make no compact
coefficient comparison and assert no vanishing of the full obstruction.

## 1. Work intrinsically in the actual image module

Retain B92's equivariant node map

\[
 d_0:P_0\longrightarrow\bar L\subset P,
 \qquad Z_0=\ker d_0,
\]

where (P=I_{\mathbb Z[R]}\otimes I_{\mathbb Z[R]}\), F acts by
negative swap, and

\[
 \operatorname{im}\{H^1(C_2,P_0)\to H^1(C_2,P)\}=J_I.
\]

Let (v\in\bar L\) have an explicit finite expression in actual
common-whisker node columns and actual old-base/deck/E translates.
If the entire integral chain satisfies

\[
                         Fv=-v,
\]

then its Tate diagonal is intrinsically in

\[
 U=\operatorname{im}\{H^1(C_2,\bar L)\to H^1(C_2,P)\}.
\]

Consequently its class modulo (J_I\) belongs to the actual image of
\(\kappa\). This assertion uses the actual image module and does
not identify the common-whisker relation kernel with (Z_0\).

For a finite two-chain in the common Cayley-edge basis, the diagonal is

\[
 \operatorname{diagTate}(v)=
 \sum_{u,i} [v_{(u,i),(u,i)}],u(x_i-1)
        \quad\text{in }I_{\mathbb F_2[R]}.
\]

The whole integral anti-invariance equation must hold. A solution of its
mod-two reduction alone does not establish a cohomology class here.

## 2. An honest refined H2 representative

Let (C\) be the free (\mathbb Z[E]\)-module on the finitely many
common columns used in the proposed expression. Let

\[
 J(C)=\operatorname{Ind}_{E}^{E\rtimes C_2} C
\]

be the module consisting of C and a formal F-copy, with the appropriate
semilinear E-action. Map its two copies to the actual columns and their
F-images. This gives an equivariant map (d_C:J(C)\to\bar L\).
Set

\[
 P_+=P_0\oplus J(C),\qquad
 d_+(p,c)=d_0(p)+d_C(c),\qquad Z_+=\ker d_+.
\]

The underlying C2 module (J(C)\) is induced from the trivial
subgroup, so its positive-degree cohomology vanishes. This can also be
checked directly: fixed vectors in the two summands are norms, and
anti-invariant vectors are differences; neither assertion divides by
two. Since (d_0\) surjects onto (\bar L\), projection to the added
summand gives an exact sequence

\[
 0\longrightarrow Z_0\longrightarrow Z_+
       \longrightarrow J(C)\longrightarrow0.
\]

It follows that

\[
 H^2(C_2,Z_0)\xrightarrow{\ \sim\ }H^2(C_2,Z_+).
\]

Also (H^1(C_2,P_+)\) has the same image (J_I\) in
\(H^1(C_2,P)\). Thus the refined presentation has the same obstruction
map, under this canonical cohomological identification.

If (p\) in the common summand satisfies (d_Cp=v\), then

\[
 z=(1+F)p\in Z_+,
\]

because (v+Fv=0\). It is invariant, and its refined H2 class maps
to \(\operatorname{diagTate}(v)\bmod J_I\). The isomorphism above
gives a corresponding class for B92's original presentation. No literal
identification (\ker d_{\rm common}=Z_0\) is needed or claimed.

If (v=u-Fu\) with (u\in\bar L\), this is a coboundary in
\(H^1(C_2,\bar L)\); its diagonal class is zero. In particular,
symmetrizing an arbitrary common column does not manufacture a new
obstruction.

## 3. The bounded sixty-four-column test

Let (c_1,\ldots,c_{64}\) be the corrected actual finite seed columns.
The initial test solves

\[
 (1+F)\sum_{j=1}^{64}n_jc_j=0,
                    \qquad n_j\in\mathbb Z.
\]

This retains every full E vertex and every Cayley-edge label. It is
not the augmented incidence matrix and is not the full old-base/deck/E
orbit module.

The same test captures the Tate image of the C2-stable **integer
span** of these seeds and their F-images. Indeed, if

\[
 v=\sum_j a_jc_j+b_jFc_j
\]

is anti-invariant, then \(\sum_j(a_j+b_j)c_j\) is anti-invariant,
and their difference \(\sum_jb_j(Fc_j-c_j)\) is a coboundary.
Thus adjoining the F-images alone introduces no additional diagonal
classes beyond the integral kernel just displayed.

An integer basis spanning the rational kernel can initially have an
even lattice index. It must therefore be 2-saturated before its
diagonal image modulo two is used as an exact result for this finite
span. The following finite operation does so. If the columns of a
kernel basis K have a nonzero binary dependence a, replace one basis
column with \(Ka/2\), choosing its coefficient in a to be one.
This is integral, preserves the kernel, and enlarges its lattice by
index two. Repetition terminates because the initial kernel lattice
has finite index in the saturated integer kernel. At termination the
remaining index is odd, so the diagonal images modulo two coincide.
Every replacement and the final integral anti-invariance equations
are retained as exact certificates.

## 4. Finite certificates for zero in the full source ideal

The actual source certificate supplies eight source kernel seeds and
eleven source operators. A word in those seeds and their operator
orbits is an actual element of I. Consequently a finite identity

\[
 \psi=\sum_\ell g_\ell(i_\ell-1),\qquad i_\ell\in I,
\]

with every (i_\ell\) accompanied by its actual source expression,
certifies \(\psi\in J_I\) for the **full** source ideal.

Equivalently, pair the finite support words of (\psi\) into pairs
\(g,h\) for which an explicit source expression for (g^{-1}h\)
is given; then (g+h=g(1+g^{-1}h)\) in characteristic two. A finite
source subgroup and a certified free-group rewriting procedure can
produce such witnesses. Failure to rewrite in that finite subgroup
does not prove nonmembership in the full I and will be reported only
as an unresolved certificate attempt.

## 5. Scope of any finite result

Even an exact zero diagonal image for the sixty-four-column span
does not establish \(\kappa=0\). Conversely, an odd diagonal is
only a candidate until its source-ideal class is determined. The
complete old-base/deck/E translates, nonlinear fixed-lifting problem,
and actual compact comparison remain outside this bounded test.

## 6. Completed exact sixty-four-column result

The bounded calculation is complete. Its producer is
`work_A/code/check_intrinsic_64_anti_chains.py`, with genuine `.out`,
empty `.err`, and complete data
`work_A/intrinsic_64_anti_chain_certificate.json`.

There are 1,951 nonzero full off-diagonal equations, reducing by exact
integer row normalization and duplicate removal to 84 distinct
equations in 64 coefficients. The matrix has rank 59. The certificate
retains a 59-by-59 minor of determinant **−1**, together with five
independent null vectors; these prove the rank over the rationals
without relying on a modular rank inference.

The entire integral anti-invariant coefficient kernel has basis

\[
 \begin{split}
 &c_{7,7}-c_{7,6},\
 &c_{10,3}-c_{10,1},\
 &c_{12,1},\
 &c_{14,3}-c_{14,1},\
 &c_{16,1}.
 \end{split}
\]

The pairs are the stored `(loop_index, local_node_index)` labels. All
five vectors have literal integral anti-invariant full chains. Their
coefficient basis is already 2-saturated; no saturation replacement
was required.

The first, second, and fourth chains have zero Tate diagonal. The
third and fifth have diagonals, respectively,

\[
 r_3-1,\qquad r_4-1,
\]

where (r_3,r_4\) are exactly the third and fourth actual source
seeds in `symmetric_source_node_alignment.json`. They are the
positive first-sheet source meridians at critical indices 12 and16
(physical w-branches with coefficient indices3 and4). The free R
words are, in the unchanged common basis,

\[
 \begin{split}
 r_3={}&x_{33}x_{34}x_{35}x_{36}x_{38}x_{39}
             x_{38}^{-1}x_{36}^{-1}x_{35}^{-1}x_{34}^{-1}x_{33}^{-1},\
 r_4={}&x_{20}.
 \end{split}
\]

Thus the diagonal image has binary dimension two, and **all five
kappa values vanish modulo the actual full source ideal**. For the
two nonzero diagonals the zero certificate is simply the corresponding
single source seed, not a finite-orbit membership heuristic. The full
certificate verifies those identities by substitution into the saved
actual source words.

This exactly handles the integer span of these 64 columns and its
F-closure. It leaves all additional E, retained-deck, and old-base
translates in the full module unexamined. No global kappa vanishing
or source-image equality follows.
