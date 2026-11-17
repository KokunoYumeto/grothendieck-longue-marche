# Exact mirror fold of the actual annular one-neck presentation

Status: complete algebraic comparison with the independently checked
actual comb-reflection input. This note makes no source-image
freeness, post-quotient vertex injection, or centralizer claim.

## 1. The actual mirror and the prequotient fold

Use B114's common neck basepoint at the selected gap. The actual mirror
`J(q,t)=(1/conj(q),1/conj(t))` fixes that basepoint and has square one.
It exchanges the two bad vertices and preserves the common disk group
K. Let `R=R_-`, let `mu:R -> R_+` be the reflected based isomorphism,
and let `eta=J_*|K`. Thus eta is an actual involutory automorphism of K,
not a generator-wise inversion convention. With both edge inclusions
written explicitly, one has

`mu i_-(k) = i_+(eta(k))`.

Here eta^-1=eta. The map j on `A=R_- *_K R_+` exchanges r with mu(r)
and applies mu^-1 on the other vertex. Its two formulas agree on the
common K precisely by the displayed relation. Hence j is a genuine
order-two automorphism of A.

Put `Q=K semidirect_eta <j>`. There is an exact isomorphism

\[
 \mathcal A\rtimes\langle j\rangle
 \cong R*_{K}Q
 =\langle R,j\mid j^2=1,\ j k j=\eta(k)\ (k\in K)\rangle.
 \tag{1}
\]

The forward map retains the first vertex and j. It is onto because
the other vertex is j R j. To write its inverse without suppressing
an edge map, send the first vertex identically to R and send
`s in R_+` to `j mu^-1(s) j`. On `i_+(k)` this gives
`j i_-(eta(k)) j=i_-(eta^2(k))=i_-(k)`, so the edge relation holds.
The resulting A-map extends over its actual mirror j. Both composites
fix all generators. This proves (1) directly; no tree realization or
unstated marking choice is involved.

The prequotient full-completion statement is proper. In the general
fully invariant paired-kernel lemma, the first ordinary vertex is
`H_-`, with its actual retraction to K, and the second ordinary vertex
is K itself inside `Q=K semidirect C2`, with the identity retraction.
Its cone/retraction endomorphism is eta. Thus compatible finite edge
kernels exist cofinally, and

\[
 \widehat{R*_{K}Q}
 \cong\widehat R\amalg_{\widehat K}\widehat Q
 \cong\widehat{\mathcal A}\rtimes\langle j\rangle.
 \tag{2}
\]

The last equality also follows from the full topology of every
finite-index subgroup, by taking finite-index cores. It is not an
assertion about completions of an arbitrary infinite-index kernel.

## 2. The actual quotient needs one folded relation

Let `c=c_-` be the actual common-neck cone, and `k=k_-` its actual
far/collar section loop. The reflected words are exactly
`c_+=j c j` and `k_+=j k j`, with the reflected orientation chosen
consistently. The two B114 relations are therefore

\[
 r=[j c j,k],\qquad j r j=[c,j k j].
\]

The normal closure of these two words in A is j-stable. Conversely,
the normal closure of r in `A semidirect <j>` is generated, as an
A-normal subgroup, by r and j r j, since A has index two. Hence

\[
 G_{\rm ann}\rtimes\langle j\rangle
 \cong (R*_{K}(K\rtimes_\eta C_2))
             /\langle\!\langle[j c j,k]\rangle\!\rangle.
 \tag{3}
\]

The full profinite version of (3) uses the closed normal closure of
the same single relation, by the universal property on all finite
targets. The mirror character sends R to zero and j to one; its
kernel is the original G_ann. This is distinct from the original
orientation character, which is the vertex orientation on R and
sends j to zero. The latter extends because J commutes with the
original involution. Both characters descend through the relation.

In the proper discrete amalgam before this quotient, r is a cyclically
reduced word of eight alternating syllables:

`j | c | j | k | j | c | j | k^-1`.

Indeed j is outside K by the mirror character, c is outside K by
original orientation, and k is outside K by geometric base winding.
This normal form establishes that the folded relation is genuine;
it does not establish a one-relator Freiheitssatz for its quotient.

The selected common cone is, after the corrected upper-collar
comparison, `c=a C a^-1`, not merely the adapted C. The section word
is `k=f^-1 h`. Both must be substituted together in (3). The initial
lower-corridor formula belongs to the opposite selected lift and
cannot be used as this c.

## 3. The actual six-cone rewriting of the mirror vertex

The complete actual comb computation is now saved and independently
read in `work_DE/next_marginal_source/annular_neck_reflection_proof23.md`.
Its two genuine producers/certificates are `check_annular_neck_bridge23`
and `check_annular_neck_reflection23` in the same directory. The bridge
has exactly the one positive sigma2 crossing and sends the entire old
ordinary basis O=(x1,x3,x4,x5,x6) literally to the endpoint ordinary cuts.
The actual upper-gap Cayley basis is exactly those cuts. Both ordinary
and reflected polygons are also independently read by
`work_CE/code/compile_annular_neck_presentation23.py`, which verifies
the reflection words without assuming their formula.

Thus, for P_i=O1...Oi, the actual involution satisfies
`eta(O_i)=P_(i-1) O_i^-1 P_(i-1)^-1` and `eta(P_i)=P_i^-1`.
The prefixes are a free basis, with inverse Nielsen substitutions
`O1=P1`, `Oi=P_(i-1)^-1 P_i`. Put `r_0=j` and `r_i=j P_i`.
Their squares are one, and

\[
 Q\cong C_2(r_0)*C_2(r_1)*\cdots*C_2(r_5).
 \tag{4}
\]

This follows by substituting `P_i=r_0 r_i` in the full presentation
`<P_i,j | j^2, j P_i j=P_i^-1>`; no relation remains except the six
squares. This choice gives the particularly simple literal edge map
`O_i=r_(i-1) r_i`, 1<=i<=5. The alternative factors P_i j are the
simultaneous j-conjugates of these factors. Arbitrarily chosen
representatives of six involution classes would not have sufficed;
the one actual prefix system is essential.

The short bridge remains in Re(Q)>=0, Im(Q)>=3, where
Im(A_j)>1 and the selected h_j are in the first quadrant. The lower
bound for the least Im(A_j) is equivalent to 39>17 sqrt(5).
This keeps all selected y-punctures in the upper half-plane. The
exact endpoint q=(4+3i)/5 is connected to the original q*=exp(i pi/5)
in the same marked region. The exact polynomial separation and
actual-root displacement bounds are retained in DE's companion
deformation JSON. No arbitrary first-arc or endpoint-only isotopy
has been substituted.

In these six reflection generators the five adapted common letters
are literally

\[
\begin{aligned}
 a&=r_1r_2,& B=\bar b&=r_2r_1r_0r_2,& d&=r_3r_4,\\
 e&=r_5r_3r_2r_5,& f&=r_3r_5r_4r_3.
\end{aligned}
\]

Together with C=C_- and k=k_-, this is an eight-generator folded
presentation: seven involution squares (the six r_i and C), the
six generic regional relations, ten simultaneous node relations,
and the one cross relation. There are 24 free-group relators.
The region retains h=fk and b=C B C. The outer C and k are j C j
and j k j, and the selected inner cone is a C a^-1. No individual
node relation or all-height closure is omitted by this substitution.

The exact finite-word certificate is `work_A/annular_mirror_fold23.json`,
produced by `work_A/code/compile_annular_mirror_fold23.py` with genuine
`.out/.err` alongside. It independently checks inverse maps on all 8
folded and 10 extended original generators, all 16 outer regional
relators as literal j-conjugates, and the second cross relation as the
j-conjugate of the first. The six actual source words are transferred
from CE's based direct package, with lengths 10,38,26,26,11,1 in this
free-product marking. Both original-orientation and mirror parity are
checked. No word equality is inferred from an unproved quotient solver.

## 4. Exact remaining normal-form issue

The fold removes the duplicate full bad vertex but retains all actual
edge words and the genuine folded relation. The original source has
abstract group F6, but its image may have relations after (3); no free
image is assumed. In particular, the known commutations of k with
selected common ordinary letters can interact with the new relation
`[j c j,k]`. Such an interaction requires exact marked source words,
not ranks or an unmarked identification of cone classes.

The normal-form tools available before the quotient cannot simply be
reused after it. A successful further rewriting must preserve the
actual embedding of K, the selected cone a C a^-1, the far loop
f^-1 h, and the entire eta action. This is the remaining algebraic
input; no whole-region or whole-surface conclusion is made here.
