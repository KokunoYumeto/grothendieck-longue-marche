# Independent review of torsor checks A, C, D1 and D2

Reviewer: `/root/notes_inertia`, 2026-11-18. Reviewed the mathematical arguments in `records/notes_torsors_support.md`, the frozen text of scans137–140, and the corresponding supplied modern context. No source image was opened and no other record or deliverable was edited. This is a targeted proof review, distinct from contextual reading.

## Verdict

**No mathematical defect found in A, C, D1 or D2 under their explicitly stated hypotheses and the declared repaired definition of minimality.** In particular, D2 is a valid counterexample to the broad injectivity statement for **all admissible finite locally free S-group schemes and all S-group morphisms** over reduced connected S. The important limits are already present in the support file: finite étale quotients for A/C, proper finite flat subgroup reductions for minimality, and the distinction between variable S-group morphisms and morphisms obtained from fixed k-group schemes.

## A — uniqueness of the geometrically injective kernel

**Statement rechecked:** for arbitrary S, if `1→Uᵢ→G→Γᵢ→1` are exact sequences of fppf sheaves represented by S-group schemes, Γᵢ is finite étale, and Uᵢ→S is geometrically injective, then U₁=U₂. Neither reducedness nor connectedness of S is needed.

The proof works scheme-theoretically, including on a nonreduced S. The identity section of Γ₂ is open and closed; its inverse image in U₁ is therefore an open-and-closed subscheme. Every geometric fibre of U₁ has one point because it is geometrically injective and has a unit section, so every point of U₁ lies in that inverse image. An open subscheme with the whole underlying space is the entire scheme, with its original nilpotents, giving factorisation through the identity and hence U₁⊂U₂. Reversing the indices gives equality.

**Limit:** this verifies the explicit finite-étale-quotient statement. It does not by itself settle every possible historical meaning of “finite, flat, separable”, or remove reducedness from section rigidity.

## C — pointed-torsor rigidity

**Statement rechecked:** let S be reduced and connected, G finite locally free, and `1→U→G→Γ→1` exact with U geometrically injective and Γ finite étale. Two global sections of a G-torsor agreeing at a geometric point coincide; a G-equivariant automorphism of a pointed G-torsor fixing its geometric marking is the identity.

For sections, trivialising the torsor by the first section identifies the second with g∈G(S). Its image in Γ agrees with the identity on a nonempty clopen subset of connected S, so it lies in U. The equalizer of g and the identity is closed because U is separated, and contains every geometric point; its ideal is therefore contained in the nilradical of S and is zero. This is exactly where reducedness is used.

The passage to automorphisms is also valid. `Ad(P)` is the inner form representing G-equivariant automorphisms; inner conjugation preserves the kernel U, and the finite étale quotient and the stated properties descend under a faithfully flat torsor trivialisation. Equivalently, the uniqueness proved in A makes the kernel intrinsic under those identifications. One small implicit point can be made explicit if desired: **U is automatically finite locally free here**, because it is the pullback of the clopen identity section of Γ, hence an open-and-closed subscheme of the finite locally free G. The trivialising cover P need not be reduced, but this causes no problem: the descent properties and A hold without reducedness, and the final section-rigidity argument is applied over the original reduced S.

**Limits:** this does not apply to arbitrary reduced connected S-schemes P, nor to nonreduced S. It asserts no flatness of equalizers of group morphisms.

## D1 — nonflat equalizer over the regular base k[t]

**Statement rechecked:** for k of characteristic p>0, the equalizer of zero and `[t]:αₚ,S→αₚ,S` on S=Spec k[t] is `Spec k[t,T]/(Tᵖ,tT)`, and is nonflat even though both source and target groups are finite free and admissible.

The map `T↦tT` respects the additive Hopf structure over the base, so it is an S-group endomorphism. The displayed equalizer has generic fibre of length1 and fibre at t=0 of length p; equivalently, its nonzero element T is killed by the base nonzerodivisor t. Either argument proves nonflatness. This correctly detects failure of closure under equalizers for the class of all admissible finite flat relative group schemes.

**Limit:** by itself it supplies no minimal torsor and therefore is not yet a counterexample to the injectivity assertion. D2 supplies that additional datum.

## D2 — cusp minimality and equal pointed pushforwards

**Statement rechecked:** over `A=k[tᵖ,tᵖ⁺¹]`, with k algebraically closed of characteristic p>0, the pointed αₚ-torsor `P=Spec A[z]/(zᵖ−x)` at the cusp is minimal for proper admissible finite flat closed subgroup reductions, yet zero and `[x]` are distinct S-group endomorphisms with isomorphic pointed pushforwards.

### Torsor, nontriviality and minimality

Writing x=tᵖ and y=tᵖ⁺¹ gives `A≅k[x,y]/(yᵖ−xᵖ⁺¹)`, a domain with fraction field k(t). The algebra of P is free of rank p over A, and `T=z₂−z₁` gives the torsor identity `P×αₚ≅P×ₛP`. A global section would require b∈A with bᵖ=tᵖ; injectivity of Frobenius in k(t) forces b=t, which is not in the semigroup ring A. Thus P is nontrivial.

Every finite flat closed subgroup H⊂αₚ,S is finite locally free because A is noetherian; its rank is constant on connected S. Over k(t), an ideal defining a subgroup of `k(t)[T]/(Tᵖ)` is `(Tᵈ)`, and for 1<d<p the nonzero cross term `d·Tᵈ⁻¹⊗T` prevents it from being a Hopf ideal. Thus the generic rank is1 or p. Rank p makes the coordinate surjection between equal-rank locally free modules an isomorphism, so H=αₚ; rank1, together with the unit, makes H trivial. The only possible proper finite flat reduction would therefore trivialise P, which it cannot. This proves the stated minimality.

The torsor P itself is nonreduced: its coordinate ring can be written `k[z,δ]/(δᵖ)` with `δ=y−zᵖ⁺¹`. This is **not a defect**: the hypotheses require S reduced, not P reduced, and infinitesimal group torsors may have this form.

### Pushforward and the geometric marking

For an αₚ-torsor `zᵖ=f`, pushforward by `[c]` is `wᵖ=cᵖf`, with `[c]`-equivariant map w=cz. This formula is verified directly: the map from the contracted product sends `(z,h)` to `cz+h`; it is well-defined, αₚ-equivariant, and becomes an isomorphism after a torsor trivialisation.

For c=x, the target equation is `wᵖ=xᵖ⁺¹=yᵖ`, so w↦w−y identifies it with the trivial αₚ-torsor. At the cusp, x=y=z=0, and the induced point w=xz=0 goes to the identity under this translation. Thus this is a **pointed** trivialisation, just as for pushforward by zero. The maps zero and `[x]` remain distinct because xT is nonzero in the free A-module `A[T]/(Tᵖ)`.

### The proposed fibre product fails exactly at flatness

Under these pointed trivialisations, `P→Q=αₚ×αₚ` is `z↦(0,xz−y)`. Pulling back the diagonal gives

`R=Spec A[z]/(zᵖ−x,xz−y)=Spec k[z]`.

The equality of rings follows by substituting x=zᵖ and y=zᵖ⁺¹; the cusp relation then vanishes identically. This finite normalization has generic fibre length1 and cusp fibre `k[z]/(zᵖ)` of length p, hence is not flat. The equalizer subgroup `ker[x]=Spec A[T]/(Tᵖ,xT)` has the same rank jump and is not admissible. The distinguished point and topological surjectivity of R do not make it a finite flat reduction to which minimality applies.

### Essential scope distinction

The morphism `[x]` varies with S and **does not descend from a k-group morphism** `αₚ,k→αₚ,k`: such a fixed morphism has coefficients in k, whereas x is a nonconstant element of A. Thus D2 refutes the broad relative statement with `Homₛ-gp`, not the earlier statement restricted to objects and morphisms supplied by an exact base-change functor from finite k-group schemes. Nor does it refute a carefully chosen category closed under equalizers: the displayed kernel is nonflat and hence cannot be an object in such a finite-flat category. No general assertion about the correctness of the later contextual categorical proof is made by this review.

## Suggested review event

For the final IDs corresponding to A, C, D1 and D2, an appropriate CHECK_EVENTS type is **`used and rechecked in this run`** (or `targeted proof check` if root reserves the former for subsequent mathematical use). Outcome: **independently checked and sound under the explicit hypotheses; D2 refutes only the broad all-admissible-relative-group statement with variable S-group morphisms and the declared proper-subgroup definition of minimality**.

This review supplies no novelty claim, no bibliographic verification and no justification for modifying the frozen manuscript wording. The separate counterexample B was not a requested review target and is not included in this verdict.
