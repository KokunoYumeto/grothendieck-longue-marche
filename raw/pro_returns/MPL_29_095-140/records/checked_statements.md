# Exact refined statements referenced by CHECK_EVENTS.tsv

Prepared 2026-11-18 by `/root/notes_inertia` from the current research notes, `CHECK_EVENTS.tsv`, and the written support proofs and reviews. These definitions specify the mathematical scope of the nine `.R1` identifiers already used in the register; they do not change the frozen transcription or add a literature/novelty claim. A proof reference below identifies the written argument, not a machine certificate.

**Status vocabulary:** **proved** means the stated qualified result has a complete argument in the cited record; **counterexample-only** means an unrestricted assertion is refuted without replacing it by a complete general theorem; **required missing condition** identifies an obligation for the attempted argument or reconstruction, supported by a counterexample to the weaker hypotheses, without claiming that a listed repair is sufficient.

| Refined ID | Status | Precisely scoped subject |
|---|---|---|
| N002.R1 | counterexample-only | Arithmetic inertia is not automatically central; retain its conjugation action |
| N025.R1 | proved | Uniqueness of geometrically injective kernels with finite étale quotients |
| N027.R1 | proved | Section and pointed-automorphism rigidity for the specified admissible torsors |
| N032.R1 | required missing condition | Equalizer flatness/closure is not implied by admissibility of source and target |
| N033.R1 | required missing condition | Reduced connectedness does not justify the claimed minimality–injectivity argument |
| N036.R1 | proved | Correct CRT equivalences and one-way intersection/product implication |
| N037.R1 | proved | Unique monic factors over a nonzero connected base |
| N041.R1 | required missing condition | Cartesian localization data alone do not give the claimed étale gluing |
| N056.R1 | proved | Qualified rigidity retains reducedness; its unrestricted removal is false |

## N002.R1 — Arithmetic inertia must retain its action

**Exact statement.** Unrestricted centrality of tame inertia over an arithmetic base is false, including for a regular formal disc with one boundary component. Explicitly, take

`K=F₂((t)), L=F₄((u)), u³=t`.

Then L/K is a tame Galois extension of degree 6, its inertia subgroup is `I≅C₃`, and a generator σ of its residue-field Galois quotient `C₂` conjugates a generator r of I by `σrσ⁻¹=r²≠r`. Therefore the inertia subgroup is not central.

The retained formulation is that an extension with an abelian inertia kernel must carry the induced conjugation action of its base quotient. In a tame description where that action is induced by the cyclotomic action on a Tate-module quotient, it must remain part of the data; choosing a basis at one geometric point does not eliminate it. Conditional on such an identification, centrality means that the induced action on the actual inertia quotient is trivial: for any exact group extension `1→I→E→B→1` with I abelian, conjugation descends to B and I is central in E exactly when that descended action is trivial.

**Status:** counterexample-only for the unrestricted formal-arithmetic centrality assertion. The elementary centrality/action criterion just stated is a group-theoretic formulation, not a newly proved general geometric identification of every inertia coefficient.

**Proof reference:** `records/notes_inertia_support.md`, check C1; `records/notes_root_support.md`, “Root review of ancillary checks”. The cubic is Eisenstein over F₄[[t]], and r(u)=ζu, σ(ζ)=ζ², σ(u)=u give the displayed relation directly.

**Explicit limits:** the target is the unrestricted adjective in **Hua, findings register, `29-formal-tame-pi1-self-intersection`**, and Hua’s “La suite exacte”. **Scan 096 does not itself assert centrality.** This check does not prove the complete formal-inertia classification, a general specialization sequence, or splitting of the extension; trivial conjugation and splitting are different conditions.

## N025.R1 — Uniqueness of the infinitesimal kernel without reducedness

**Hypotheses.** S is any scheme, G an S-group scheme, and for i=1,2 there are exact sequences of fppf sheaves represented by S-group schemes

`1→Uᵢ→G→Γᵢ→1`,

where Γᵢ is finite étale over S and Uᵢ→S is geometrically injective. In particular, each geometric fibre of Uᵢ has at most one geometric point, and its unit section supplies one.

**Conclusion.** U₁ and U₂ are equal as subgroup schemes of G. No reducedness or connectedness assumption on S is needed.

**Status:** proved.

**Proof reference:** `records/notes_torsors_support.md`, proof A; independently reviewed in `records/review_torsor_checks.md`, section A. The inverse image of the clopen identity section of Γ₂ under `U₁→G→Γ₂` contains every geometric point of U₁ and is consequently all of U₁ as an open subscheme, giving U₁⊂U₂; reverse the indices.

**Explicit limits:** the quotient hypothesis here is **finite étale**. Applying it to the historical phrase “finite, flat, separable” requires that interpretation. This statement gives uniqueness of an existing kernel, not existence of a decomposition for every group, flatness of every subgroup/equalizer, or rigidity over nonreduced bases.

## N027.R1 — Rigidity with the torsor and admissibility hypotheses

**Hypotheses.** S is reduced and connected; `a:Spec Ω→S` is a geometric point; G is a finite locally free S-group scheme in an exact fppf sequence

`1→U→G→Γ→1`,

with U→S geometrically injective and Γ finite étale. Let P be a representable fppf G-torsor. The kernel U is automatically finite locally free, since it is the clopen inverse image of the identity section of Γ in G.

**Conclusions.** If two global sections s₁,s₂ of P/S have the same restriction to a, then s₁=s₂. If instead P is merely supplied with a geometric marking `ξ∈P(Ω)` over a, every G-equivariant S-automorphism of P fixing ξ is the identity; no global section of P is assumed for this second assertion.

**Status:** proved.

**Proof reference:** `records/notes_torsors_support.md`, proof C; `records/review_torsor_checks.md`, section C. A first global section trivialises P; the quotient in Γ of the second section equals the identity on a nonempty clopen subset and hence everywhere. The resulting section of U agrees geometrically with its identity, and the closed equalizer has zero ideal because S is reduced. For automorphisms, apply the same section argument to the inner form `Ad(P)`; the stated admissibility properties descend under a torsor trivialisation.

**Explicit limits:** this is not a theorem for arbitrary reduced connected S-schemes P. The omitted-torsor version is refuted by the sections 0,t of `A¹` over `Spec k[t]` in torsor proof B. Reducedness cannot be removed in this generality, as N056.R1 records. No closure or flatness assertion for equalizers of group morphisms follows. N019 uses this qualified rigidity result only; its broader functor-exactness and pro-representability assertions remain attributed source claims, not consequences independently established here.

## N032.R1 — Equalizer admissibility requires separate justification

**Exact negative statement.** Even when S is reduced, connected and regular, two admissible finite locally free S-group schemes can have a nonflat scheme-theoretic equalizer of two S-group morphisms. Hence the class of all such admissible relative groups is not automatically closed under equalizers.

For any field k of characteristic p>0, take `S=Spec k[t]`, `G=G′=αₚ,S`, and the morphisms zero and multiplication by t. Both groups are admissible with geometrically injective kernel equal to the group and trivial finite étale quotient, but

`H=Eq(0,[t])=Spec k[t,T]/(Tᵖ,tT)`

is not flat: its generic fibre is `Spec k(t)` of length 1, while its fibre at t=0 has length p. Precisely, localization at t gives `k[t,t⁻¹]`, and passage to the generic fibre gives k(t).

**Required missing condition.** An argument that needs H to be an admissible object must separately establish its flatness and the remaining admissibility requirements, or work in a specified category whose required equalizers are objects of that category. Admissibility of G and G′ and reduced connectedness of S do not provide this.

**Status:** required missing condition, justified by the explicit counterexample.

**Proof reference:** `records/notes_torsors_support.md`, proof D1; `records/review_torsor_checks.md`, section D1.

**Explicit limits:** no theorem that flatness alone suffices for the larger minimality or pro-representability argument is asserted. D1 alone does not specify a minimal torsor; the stronger failure involving one is N033.R1.

## N033.R1 — Reduced connectedness is insufficient for minimality–injectivity

**Exact negative statement.** The following data do **not** imply injectivity of `u↦u_*[P,ξ]`: a reduced connected scheme S; admissible finite locally free S-groups G,G′; a geometrically pointed G-torsor (P,ξ) minimal with respect to **proper admissible finite flat closed subgroup reductions**; and all morphisms `u∈Homₛ-gp(G,G′)`.

Here “minimal” has the declared repaired mathematical meaning: there is no proper admissible finite flat closed subgroup `G₀⊊G` and pointed G₀-torsor `(P₀,ξ₀)` with `(P,ξ)≅(P₀,ξ₀)×^{G₀}G`. This definition is a mathematical interpretation and does not amend the frozen contracted-product formula.

**Explicit witness.** Let k be algebraically closed of characteristic p>0,

`A=k[tᵖ,tᵖ⁺¹]=k[x,y]/(yᵖ−xᵖ⁺¹)`, `S=Spec A`, `G=G′=αₚ,S`,

and let a be the cusp x=y=0. The torsor `P=Spec A[z]/(zᵖ−x)`, pointed by z=0 over a, is nontrivial and minimal in the stated sense. The distinct S-group morphisms zero and `[x]` nevertheless have pointed-trivial pushforwards: the second has equation `wᵖ=xᵖ⁺¹=yᵖ`, and w↦w−y trivialises it while preserving the cusp marking.

In the attempted reduction diagram, the equalizer and fibre product are

`H=Spec A[T]/(Tᵖ,xT)`,

`R=Spec A[z]/(zᵖ−x,xz−y)=Spec k[z]`.

Both have generic fibre length 1 and cusp fibre length p; neither is flat. Thus the proposed R is not an admissible finite flat subgroup reduction to which the defined minimality applies.

**Required missing condition for that argument.** Before invoking minimality on the exhibited fibre product, one must establish that H is an admissible subgroup and R is a pointed H-torsor giving a structural-group reduction of P. Those properties do not follow from the displayed Cartesian diagram, a geometric marking, or reduced connectedness of S. **This refinement is negative: it makes no claim that any proposed additional condition is sufficient for a general injectivity theorem.**

**Status:** required missing condition, with a complete counterexample to the broad injectivity assertion.

**Proof reference:** `records/notes_torsors_support.md`, proof D2; `records/review_torsor_checks.md`, section D2; root’s independent cusp check in `records/notes_root_support.md`.

**Explicit limits:** `[x]` is an S-dependent morphism and does not descend from a morphism of fixed k-group schemes. The example therefore does not refute the earlier restricted exact-functor setting with only such field-group morphisms, and does not verify or refute the later context-only proof in a suitably equalizer-closed category. It proves no claim of historical or published novelty.

## N036.R1 — The correct CRT chain

**Hypotheses.** A is any commutative unital ring and I,J are ideals of A. Define the canonical map

`α:A/IJ→A/I×A/J`.

**Conclusions.** The following are equivalent: α is surjective; α is bijective; and I+J=A. Under these conditions I∩J=IJ. In general `ker α=(I∩J)/IJ`, so I∩J=IJ is equivalent to injectivity alone and does not imply the three preceding conditions.

**Status:** proved.

**Proof reference:** `records/notes_local_support.md`, proof P1; `records/review_local_checks.md`, section P1. A preimage of `(1,0)` proves comaximality; if u+v=1 with u∈I and v∈J, then xv+yu lifts any pair of residues. The same decomposition proves I∩J=IJ. The ideals `(x),(y)` in k[x,y] refute the added converse from intersection/product equality to comaximality.

**Explicit limits:** no finite-generation, noetherian or completeness hypothesis is needed. The refuted equivalence is Hua’s strengthened formulation; the frozen source’s one-way implication is not refuted.

## N037.R1 — Unique monic ideal factors with constant ranks

**Hypotheses.** A≠0 is a commutative unital ring with connected spectrum, P∈A[T] is monic, and ideals J,J′⊂A[T] satisfy

`J+J′=A[T]`, `JJ′=(P)`.

**Conclusion.** There are unique monic polynomials Q,Q′∈A[T] such that

`J=(Q)`, `J′=(Q′)`, `P=QQ′`.

No locality, noetherianity, reducedness or completeness assumption on A is needed. The degree-zero case is included, with monic constant polynomial 1.

**Status:** proved.

**Proof reference:** `records/notes_local_support.md`, proof P3; `records/review_local_checks.md`, P2–P3. CRT decomposes `A[T]/(P)` into two finite projective quotient summands. Connectedness makes their ranks constant; characteristic polynomials of multiplication by T, Cayley–Hamilton and equal-rank surjections give the two monic generators. Characteristic-polynomial multiplicativity gives P=QQ′, and monic divisibility gives uniqueness.

**Explicit limits:** connectedness is a sufficient way to guarantee the globally constant quotient ranks used by this argument, not a logically necessary condition in every example. The same written argument works if the two quotient ranks are separately assumed globally constant. Without such rank control the assertion is false over k×k, as proof P2 shows. This independent proof does not recover the missing words or completion-based reasoning of scan 110.

## N041.R1 — Cartesian localization data alone do not glue

**Exact negative statement.** Even over a reduced connected regular noetherian scheme S, a quasi-finite separated étale scheme `X(s)→Spec O_{S,s}` of finite presentation for every point s, together with cocycle-compatible Cartesian transition identifications along all generalizations, need not be the system of localizations of any étale scheme X→S.

**Explicit witness.** Take `S=Spec Q[t]`, generic point η, `K=Q(t)`, and let E be the set of closed points `(t−n)` for n∈Z. Set

- `X(η)=Spec K`;
- `X(s)=Spec O_{S,s}` for closed s∈E;
- `X(s)=Spec K` for closed s∉E, using its natural map to `Spec O_{S,s}`.

At a closed point `(q(t))`, inverting q in the DVR `O_{S,s}` gives K, so the last local morphism is a principal open immersion and has all the stated local geometric properties. The maps from η and the identities give Cartesian transition squares and satisfy the cocycle conditions. A global étale realization would have image exactly `{η}∪E`, whose complement contains infinitely many points `(t−1/m)`, m≥2. This image is not open, contradicting openness of an étale morphism.

**Required missing condition.** A gluing argument must control more than these localizations and their specialization maps. The appropriate geometric finite-presentation models over open neighborhoods, and compatible maps from their localizations to the other prescribed objects, matter; merely allowing arbitrary scheme models does not express that control. In the natural quasi-finite étale model category, the necessary open-image compatibility fails in this example. **No assertion is made that the uncertain insertion on scan 135, or any proposed formulation of it, is sufficient for a gluing theorem.**

**Status:** required missing condition, supported by a counterexample to gluing from Cartesian local data alone.

**Proof reference:** `records/notes_local_support.md`, proof P4; `records/review_local_checks.md`, section P4, including the distinction between finite-presentation geometric models and arbitrary global localization models.

**Explicit limits:** this refutes the weaker contextual formulation and does not refute or prove the full source statement with its inserted neighborhood hypothesis. It resolves no uncertain source word and proves no complete representability criterion. The finite-presentation assertion concerns each local `Spec K→Spec O_{S,s}`; the global `Spec K→Spec Q[t]` is not of finite presentation and cannot be substituted for an appropriate neighborhood model.

## N056.R1 — Retain reducedness in the qualified rigidity statement

**Retained proved statement.** Let S be reduced and connected, G finite locally free in an exact fppf sequence `1→U→G→Γ→1` with U geometrically injective and Γ finite étale, and let P be a representable fppf G-torsor. Two global sections of P agreeing over one geometric point coincide, and every G-equivariant automorphism of a geometrically pointed P fixing that marking is the identity. These are exactly the hypotheses and conclusions of N027.R1, retained here as the refinement of the attempted removal of reducedness.

**Sharp negative test of that removal.** Let k be a field of characteristic p>0, `S=Spec k[ε]/(ε²)`, `G=αₚ,S`, and P=G the trivial torsor. S is connected but nonreduced; G is admissible with infinitesimal kernel G and trivial finite étale quotient. The distinct sections T=0 and T=ε both satisfy Tᵖ=0 and agree after passage to a geometric point over the unique point of S. Translation by ε is a nonidentity G-equivariant automorphism fixing the geometric marking. Thus the retained rigidity statement is false if reducedness is simply dropped while the remaining hypotheses are kept.

**Status:** proved for the retained qualified statement, with an explicit counterexample to its unrestricted extension to nonreduced bases.

**Proof reference:** N027.R1 and `records/notes_torsors_support.md`, proof C, for the positive statement; `records/notes_root_support.md`, proof R7, for the dual-number counterexample.

**Explicit limits:** reducedness is not claimed necessary for every individual group or torsor, or for every possible fundamental-group construction. Kernel uniqueness N025.R1 remains valid without reducedness and is a different assertion. The source’s qualified Proposition 3 is not refuted, and neither LM1 E.2 nor LM1 E.11 is settled by this example.
