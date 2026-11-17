# Independent audit of the actual symmetric source normalization

Date: 2026-11-16. Mathematical source/orientation audit and completed
independent projection verification: **PASS**.

Audited producers:

- `work_CE/code/extract_symmetric_source_lassos.py`;
- `work_CE/code/extract_symmetric_full_source.py`.

Only corrected chronological pullback/push arrays are used. The earlier
intrinsic Birman marking is a different Nielsen marking and is not silently
identified with these geometric cut coordinates.

## 1. The group extension and the sign of conjugation

The generic punctured fiber has actual based group (F_{21}\). In the
certified paired basis the selected geometric involution inverts the axis
and swaps ten pairs. With \(\tau_1=x_{\rm axis}\tau\), its extension is

\[
 F_{21}\rtimes\langle\tau\rangle
       \cong C_2*C_2*F_{10}.
\]

The code's free-product encoding is exactly
\(x_{\rm axis}=\tau_1\tau\), the ten right generators unchanged, and
their partners \(\tau a_j\tau\). Its Schreier decoding has both
orientations checked on every one of the twenty-one generators.

For a chronologically traversed base loop (g\), geometric push acts as

\[
 \alpha_g(x)=g^{-1}xg.
\]

Thus concatenation of base loops produces reverse composition of their
push automorphisms. The producer's `action` routine uses exactly this
order. If (g_s=g_{\rm far}h\), with (h\) a fiber word, then

\[
 \alpha_{g_s}=\operatorname{Inn}(h^{-1})\alpha_{g_{\rm far}}.
\]

This explains the sign and side of the displayed source correction; it
is not an arbitrary choice between a push and a pullback convention.

## 2. The unique correction is the actual source-path difference

For a loop returning the selected fixed branch, let

\[
 F\alpha F\alpha^{-1}=\operatorname{Inn}(k).
\]

The producer independently checks this equation on all twenty-one
generators and checks \(F(k)k=1\). It solves

\[
 \tau k=h\tau h^{-1},\qquad h\in F_{21},
\]

by free-product reduction. This is equivalent to
\(k=F(h)h^{-1}\). Consequently

\[
 \alpha_s=\operatorname{Inn}(h^{-1})\alpha,
 \qquad F\alpha_s=\alpha_sF.
\]

There is exactly one such (h\): the centralizer of the first involution
in (C_2*C_2*F_{10}\) is its own order-two factor, whose intersection
with the orientation kernel (F_{21}\) is trivial. Appending \(\tau\)
to an odd conjugator changes its orientation and leaves its conjugation
of \(\tau\) unchanged, giving the unique even representative used by
the code.

This uniqueness supplies the geometric identification. Over the regular
base the actual fixed source is a two-sheet cover. A returned source path
gives a literal source lift (g_s\); moving the basepoint on that fixed
source makes its pointed monodromy commute with (F\). Therefore its
actual difference (g_{\rm far}^{-1}g_s\) is a solution of the same
equation, and must be the computed (h\). No choice of an unrelated
conjugating path remains.

The old loop about (q=1\) exchanges the two fixed branches. Its
free-product core is the other involution factor; it is not incorrectly
treated as a returned source loop. Passing to the index-two source
cover is essential here.

## 3. Nodal filling and the positive source meridians

A far exterior section over a sufficiently small nodal disk extends
across the critical value while avoiding its finite puncture cluster.
Its base lasso therefore becomes trivial after that critical fiber is
included. Hence

\[
 g_s=g_{\rm far}h\quad\longmapsto\quad h
\]

in the actual filled total space. At a source node this is the positive
source peripheral. The independently checked physical abelianization
has coefficient (+1\) on the matching A and B meridians, agreeing with
the local model (z^2-t^2\) and its source (z=0\). After the B family
is filled, its word is a conjugate of the positive corresponding
A-meridian.

At a non-source node, the source section itself extends across the
disk, so the resulting source lasso becomes trivial. The word (h\)
need not be trivial in the free generic (F_{21}\), and the producer
correctly does not assert that. Its first-family (F_{13}\) image is
checked to be trivial.

## 4. Why the source has exactly the stated generators and operators

The regular q-base has free rank twenty-four: six old punctures and
eighteen new nodal values. Only the old loop (b\) about (q=1\) has
odd source-cover parity. The Schreier basis of its index-two kernel has
rank forty-seven. It consists of

\[
 g_i,\ bg_i b^{-1}\ (i\ne b),\ b^2
\]

for the eleven old generators, together with both sheet lifts of each
of the eighteen nodal loops. Of those thirty-six nodal lifts, eight
are actual source punctures and twenty-eight extend over regular source
points. Filling the latter basis members leaves the actual rank-nineteen
source group. Filling the remaining eight source punctures gives its
rank-eleven filled-source free-factor retraction.

The kernel is therefore generated as a subgroup by all orbits of the
eight source meridians under the eleven old source operators and their
inverses. Indeed, that subgroup contains the eight meridians, is
invariant under the complementary free factor, and is automatically
invariant under conjugation by its own generators. This is the usual
kernel of a free-factor retraction, transported through the actual
source map. It is not an ambient normal-closure replacement.

The code keeps the actual paired first-family (F_{13}\) and retained
filled (F_5\) maps. These are checked as quotient actions and inverse
actions on all retained generators, with every killed generator checked
to map to the kernel. The node words and their required global translates
remain geometrically specified; no finite orbit truncation is asserted.

## 5. Scope

This audit approves the exact extraction of the actual source words
and its complete eleven operator family, conditional only on the
already certified corrected geometric arrays read by the producer.
It does not establish source injectivity, source-image equality,
vanishing of the syzygy map \(\kappa\), a full-coefficient compact
comparison, or nonlinear fixed lifting.

## 6. Completed data and independent verification

The optimized CE run completed successfully in 7.034 seconds. Its
`extract_symmetric_full_source.py/.out/.err` and
`next_symmetric_nodes/symmetric_full_source_data.json` are saved. The
earlier redundant-expansion attempt remains separately preserved. The
optimization uses the proved discrepancy identity

\[
 k_{AB}=k_A A(k_B),\qquad k_{A^{-1}}=A^{-1}(k_A^{-1})
\]

for composition \(A\circ B\). Thus chronological base words satisfy
\(k_{uv}=k_v\alpha_v(k_u)\). Its source inverse is explicitly
\(\alpha_{\rm far}^{-1}\operatorname{Inn}(h)\); no enormous redundant
expansion of this identity is required.

The independent data-only checker is
`work_A/code/verify_symmetric_full_source_typing.py`, with genuine
`.out`, empty `.err`, and
`work_A/symmetric_full_source_typing_review.json`. It imports no producer
and hashes the final input files. It checks all eleven source actions
against (F\) on all twenty-one generators, both directions of both
actual filling diagrams, the (F_{13}\to F_5\) comparison, and direct
two-sided inverse identities on all five filled generators.

It also independently checks all thirty-six returned nodal words, the
twenty-eight trivial first-family images, and the eight positive source
peripherals. Their first-family positive cores are exactly

\[
 \{2,3,5,6,7,8,10,11\},
\]

the complete set of the eight deleted (F_{13}\) generators. On sheet
zero the four cores are (7,11,10,5\), with physical branch (w\);
on sheet one they are (2,6,8,3\), with physical branch (v\). The
respective critical indices are (0,8,12,16\) on each sheet. Every
word maps to zero in the retained (F_5\), and its physical
abelianization has positive coefficient one on exactly the matching
A and B components. These are literal projection and orientation
checks, not a claim that the eight displayed conjugates themselves
generate the entire ambient filling kernel.
