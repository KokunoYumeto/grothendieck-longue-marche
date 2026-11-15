# Independent check: partitions and evaluation at one point

This check concerns the unrestricted reading of the evaluation claim in frozen cote 11, scan 038, and the abbreviated **Hua, findings register, 11-simplicial-bivariant-poincare-equivalence** entry in `notes/RESULTS_STATE.md` (status: conjecture, unsearched; statement card without a verdict). It uses the bivariant morphisms defined on scan 034 and the Poincaré pairing on scan 027. No source image or frozen fragment was changed.

## Construction and variance

For each nonempty finite set I, let P(I) be its finite set of partitions, equivalently equivalence relations, and put B(I)=Q^{P(I)}, with pointwise multiplication, all in degree zero and with d(B(I))=0. For α:I→J, define q_α:P(J)→P(I) by pulling an equivalence relation back along α; thus q_{β∘α}=q_α∘q_β. Give B(I) the trace κ_I(x)=∑_{p∈P(I)}x(p).

The bivariant morphism B(α):B(J)→B(I) has precisely the variance proposed by the root:

\[
B(\alpha)^*=q_\alpha^*:B(I)\longrightarrow B(J),
\qquad
B(\alpha)_*=q_{\alpha*}:B(J)\longrightarrow B(I),
\]

where pullback composes functions with q_α and

\[
(q_{\alpha*}x)(p)=\sum_{r\in P(J):\ q_\alpha(r)=p}x(r).
\]

Pullback is a unital algebra homomorphism, including for maps q_α that are not surjective. Empty fibers in the pushforward formula contribute zero.

## Verification of all required identities

For a map q:S→T between finite sets, x∈Q^S and y∈Q^T, evaluation at t∈T gives

\[
q_*(xq^*y)(t)
=\sum_{q(s)=t}x(s)y(q(s))
=y(t)\sum_{q(s)=t}x(s)
=(q_*x)(t)y(t).
\]

Pointwise commutativity gives the other projection formula q_*(q^*y·x)=y·q_*x by the same equality. Also,

\[
\kappa_T(q_*x)=\sum_{t\in T}\sum_{q(s)=t}x(s)=\sum_{s\in S}x(s)=\kappa_S(x),
\]

so the gauge identity is exact. Composition of function pullbacks and of fiber sums gives (rq)^*=q^*r^* and (rq)_*=r_*q_*; hence the displayed q_{β∘α} identity gives B(β∘α)=B(α)∘B(β), with identity maps respected. Thus B is a contravariant functor on all maps of nonempty finite sets, as required on scan 038.

The pairing κ_I(xy)=∑_p x(p)y(p) has identity matrix in the characteristic-function basis. It is perfect over Q; each B(I) is finite dimensional, concentrated in degree zero, and a Poincaré algebra with the stated trace. Both components of every bivariant map have the required degree zero. The definition transcribed on scan 027 has no connectedness requirement A^0=Q; the example uses that written definition, including for B(I)=Q².

## A specific morphism proving that unrestricted evaluation fails

Let C be the constant functor with value Q, its identity trace, and identity bivariant maps. Let t_I∈P(I) be the indiscrete partition; q_α(t_J)=t_I for every α. The maps

\[
\tau_I:C(I)=\mathbf Q\longrightarrow B(I),\qquad
\tau_I^*(x)=x(t_I),\qquad
\tau_{I*}(a)=a\,\mathbf 1_{\{t_I\}}
\]

are bivariant gauge-preserving morphisms by the preceding finite-set calculation. The identity q_α(t_J)=t_I proves B(α)τ_J=τ_I, so τ:C→B is a natural transformation, with both star components satisfying naturality.

At a singleton, P(I) has one element, B(I)=Q and τ_I is the identity. At a two-element set, P(I) has two elements, B(I)=Q² and τ_{I*} has rank one; an inverse bivariant morphism would give a two-sided linear inverse to this rank-one map, which is impossible. Therefore evaluation at a singleton sends this explicit noninvertible natural transformation to an identity morphism. An equivalence reflects isomorphisms: its quasi-inverse and the two natural isomorphisms transport an inverse of the image back to an inverse of the original morphism. This proves that the unrestricted evaluation functor is not an equivalence.

## The special condition and the scope of the example

For I and J singletons, the two pullbacks B(I)→B(I⊔J) and B(J)→B(I⊔J) send each scalar to a constant function on the two partitions. Their canonical tensor map is

\[
\mathbf Q\otimes\mathbf Q\longrightarrow\mathbf Q^2,
\qquad a\otimes b\longmapsto(ab,ab),
\]

which has rank one. Thus B fails the explicitly written special condition on scan 038, and this counterexample lies outside the category restricted by that condition. It establishes the necessity of retaining that restriction in the evaluation statement; it supplies no counterexample to the intended special statement.

One source-scope caution remains: scan 042's frozen degree interval is [1,d(A)] while the same scan explicitly includes k in degree zero. The present construction uses the coherent degree-zero Poincaré objects of scans 027, 034 and 038 and does not repair that frozen interval. Its force against the unrestricted scan-038/card reading is unaffected by that separate reading question.

Context search `simplicial|Poincar|partition|special|spécial` in the supplied transcription, notes and ledger finds no simplicial or partition occurrence in the context transcription, the Poincaré pairing in `MPL_16+47+54+44_transcription.tex`, cote 16, scan 025, and the direct simplicial claim in the Hua ledger entry. Relative to cote 16/025, the construction **adds** a functor with an explicit perfect pairing; relative to the unrestricted reading of the Hua claim, the explicit natural transformation **contradicts** equivalence, while its rank calculation shows exactly why the written special restriction excludes it. The Hua entry retains its supplied unsearched/conjecture status; this review proves only the displayed example and its stated obstruction.

**Verdict:** the construction, variance, functoriality, both projection formulas, trace identity, perfect pairing and rank obstruction all check. The added natural transformation τ makes the obstruction explicit at the morphism level, as well as at the object-dimension level. **Confidence: high**, because every identity reduces to a finite fiber sum or the displayed rank-one map. This is a concrete example, not a new conditional theorem or a claim of novelty.
