# LM_P04 (scans 31–40): research notes, checked against the corrected text

Each first-pass note (R1–R14 in `answers\unzipped\LM_P04\LM_P04_review_notes.md`) is checked against `LM_P04_checked.tex`. The verdict is keep, correct or drop, with a reason, followed by the note as it now stands. The notes added in this pass are labelled "(second pass)".

## First-pass notes

**R1 — Scans 31–34, morphisms of systems and their groupoid. Kind: claim without proof. Verdict: correct.**
The text defines a morphism as three functors with four commutation isomorphisms satisfying an unwritten compatibility with α, α′ ("que je n'écris pas"). It then asserts that these form a category, "en fait un groupoïde", whose morphisms are triples μ = (μ_U, μ_D, μ_{D*}); the first pass called them h. A proof must define the composition of the commutation isomorphisms and check both compatibilities: the prism equation u = v and the Kummer square. Reason for the correction: on scan 33 the corrected reading of the square has (f_{D*})^* in all three pullbacks, against (f_D)^* in the defining formula, and the 2-morphisms are μ.

**R2 — Scan 32, the bracketed reformulation. Kind: conjecture / expectation. Verdict: keep, with a correction.**
"Cette compatibilité pourrait s'exprimer" proposes reading a system Π as a category fibred over the square Q (named Π in the inserted letter), with the restriction to {e} imposed and with cartesian functors "entre catégories fibrées…". This sentence has no parenthesis. The work is to show that the explicit prism condition is the 2-cell condition for cartesian functors over Q that are the identity on the fibre at e. Reason: the reading is confirmed, apart from the spurious parentheses and the place of the Π.

**R3 — Scan 33, margin beside the Kummer square. Kind: claim without proof (author's self-correction). Verdict: correct.**
The note now reads: "non, ça ne marche que pour les cas de morphismes étales, sinon il faut faire intervenir la multiplication par des 'degrés de ramification' d_{i′} (i′ ∈ π₀(Π′_{D*}))". So the square commutes only for étale morphisms. In general the map π₁(σ′) → (f)^*π₁(σ) must be compared with T through multiplication by the ramification index at each boundary component i′. Reason: the first pass had only fragments ("commute", "degrés des morphismes").

**R4 — Scan 34, rigidity. Kind: conjecture / expectation. Verdict: keep, with a correction.**
"J'ai l'impression que ce groupoïde Hom((f′,α′),(f,α)) est tjrs rigide, i.e. Aut(f,α) est toujours réduit au groupe unité — j'ai la flemme de vérifier". This is an expectation stated for all systems ("tjrs" = toujours), not proved. Reason: the first pass read "trop/très rigide", which hides the universal claim.

**R5 — Scan 34, centralisers. Kind: own idea (first pass). Verdict: keep.**
In the one-object case a natural automorphism of a homomorphism f: G → H is an element of the centraliser of f(G) in H. The four face conditions then cut down the triple of centraliser elements. The calculation is correct and remains the right test of R4.

**R6 — Scan 34, passage to π₀. Kind: implication not pursued. Verdict: keep, with a correction.**
"Quoi qu'il en soit, on posera Hom = π₀ Hom" (the first pass had "on pose"). Composition on isomorphism classes is well defined whether or not rigidity holds, so the category of systems does not depend on R4. Reason: the reasoning is correct; only the verb needed correcting.

**R7 — Scan 35, Conjecture bordélique 7.1. Kind: conjecture. Verdict: correct.**
For pairs (X,S) with X projective and smooth of dimension ≤ 1 and anabelian, the functor to the category ℬ is fully faithful. The source category consists of X locally of finite type over K and S a closed subscheme (written over a struck "partie discrète") étale over K, with X smooth of relative dimension 1 at the points of S. Its morphisms are the f: X′ → X with f^{-1}(S)_réd = S′. Reason: the number now reads 7.1, consistent with § 7 in the CSG table of contents, so the conjecture can be cited by that number. The source category is also stated more precisely than in the first pass.

**R8 — Scan 35, "La fidélité est facile…". Kind: claim without proof. Verdict: keep, with a correction.**
The margin note ends with three dots, not "!". Faithfulness (two geometric morphisms inducing the same class of morphisms of systems are equal) is asserted and not proved; fullness is the content of 7.1.

**R9 — Scans 35–36, reduction to group data. Kind: claim without proof. Verdict: correct.**
The text says that the data (σ, ψ, k) "est exprimée" by the system (𝓔_i), the exact sequences 1 → T(K̄) →^{k_i} 𝓔_i →^{p_i} Γ with open images Σ_i = Im p_i, and the compatibility of k_i with the operations of Σ_i ≃ Coker k_i. This is weaker wording than the first pass's "est équivalente", and the images are named Σ_i, not Γ_i. The direction change in R9 still stands: k_i: Ker σ_i ≃ T(K̄) becomes k_i: T(K̄) → 𝓔_i in the box. An inverse construction (from group data to a groupoid system) is still owed.

**R10 — Scans 37–38, changing μ_i. Kind: own idea (first pass). Verdict: keep.**
If ρ_i is replaced by int(h_i)∘ρ_i, then φ∘int(h_i)∘ρ_i = int(φ(h_i)γ_i)∘p_i, so γ_i becomes φ(h_i)γ_i. The calculation is correct, and the corrected reading γ_i (not σ_i) is the letter it uses.

**R11 — Scan 38, Ker p_i into Ker p. Kind: claim without proof. Verdict: keep.**
"ce qui implique d'ailleurs que ρ_i applique Ker p_i dans Ker p" follows at once from φ∘ρ_i = int(γ_i)∘p_i. CSG and IUT read the relation as "… ∘ ρ_i" and the kernels as "ker ρ_i, ker ρ", which would make the implication meaningless. The ink has p_i in the relation.

**R12 — Scan 38, injectivity of Γ_i → Γ_0. Kind: implication not pursued. Verdict: correct.**
The sentence (unrevised ink) still says "Γ_i → Γ_0 injectif". The diagram above it was revised in bold to Σ_i and Σ_0, and the text then continues "et ceci posé" (not "à ceci près"). Injectivity is automatic: the induced map is the restriction of the automorphism int(γ_i) of Γ to Σ_i. The note should say so rather than leave it as a check.

**R13 — Scan 39, struck NB on I = ∅. Kind: own idea (first pass) prompted by a struck claim. Verdict: keep.**
The abstract-data example (𝓔 = H × Γ_0, kernel H ≠ 1, I empty) is correct and shows that the struck statement "π = {1}" is not a consequence of the group data. See N3 below for why the author may have struck it.

**R14 — Scans 39–40, morphisms in group terms. Kind: unfinished construction. Verdict: correct.**
The reading is now: the data f_{D*}, f_D, α_{D*,D}, α_{D,e} "équivaut alors" to elements α_i (i ∈ I) of Γ, re-boxed as α_{i′} ∈ Γ (i′ ∈ I′), such that g_{i′}(γ′) = int(α_{i′})(γ′) for γ′ ∈ Γ′_{i′}. The f_U-part gives f_𝓔 with φ f_𝓔 = int(α) φ and then f_{Γ₀}(γ′) = int(α)γ′ for γ′ ∈ Γ′₀. Two slips remain in the ink and should be noted, not repaired: "celle de α_{D,e}" where α_{U,e} is needed, and the unprimed φ on the right, where φ′ is needed. The excerpt stops at "le", before the datum α_{D*,U}.

## Notes added in the second pass

**N1 (second pass) — Scan 33 margin. Kind: implication not pursued.**
Grothendieck's own correction means that the category ℬ as defined captures only "étale" morphisms on the boundary. For ramified ones, the identification k must be twisted by multiplication by d_{i′} on T(K̄). On tame inertia this is the Kummer fact that a cover ramified with index e acts on Ẑ(1) by multiplication by e. The morphisms of ℬ (and later of the group-theoretic systems) therefore need the indices d_{i′} as part of the data, or a weakened Kummer square. Nothing on scans 31–40 carries this out.

**N2 (second pass) — Scan 36 margins. Kind: claim without proof.**
The NB asserts that the geometric extensions 1 → T(K̄) → 𝓔_i → Σ_i → 1 split. A uniformiser at s_i defines a splitting, and so does a basis of the tangent space at s ("et même … le choix d'une base de l'espace tangent"). The Re N.B. adds that different bases give different splittings. This is the tangential-base-point description of sections of a decomposition group. Two tangent vectors differing by c ∈ K(s)^* give splittings differing by the Kummer class of c, which is non-zero unless c is an n-th power for all n.

**N3 (second pass) — Scans 35 and 39, dimension ≤ 1 and the struck NB. Kind: model's own idea.**
Conjecture 7.1 allows dim X ≤ 1. On a 0-dimensional component X = Spec L we have S = ∅ (I empty), π = {1}, and 𝓔 = Gal(K̄/L) is an open subgroup of Γ. This is exactly what the struck NB on scan 39 says ("π = {1} et 𝓔 se réduit à un ss-groupe"). For an anabelian complete curve, S = ∅ gives π ≠ 1. That conflict is a likely reason for the deletion.

**N4 (second pass) — Scan 37 margin. Kind: claim without proof.**
"Dans les situations géom." the extension 1 → π → 𝓔 → Σ → 1 splits over an open subgroup: there is an open Σ₀ with a lift Σ₀ → 𝓔. Geometrically, a rational point, or a tangential base point at a cusp, over a finite extension L/K gives a section over Gal(K̄/L). The note thus records that geometric systems satisfy a section condition that abstract systems need not satisfy; the conjecture leaves this unexploited here.

**N5 (second pass) — Scans 36–38, the Σ revision layer. Kind: model's own idea (editorial consequence).**
A later, heavier-ink pass renames the images: Σ_i = Im p_i (scan 36), Σ = Im φ and Σ_{(0)} in the boxed sequence (scan 37), and Σ_i, Σ_0 in the diagram of scan 38. The unrevised sentences keep Γ_i, Γ_0, as do the diagrams of scan 40. A reader must identify Σ_i with ψ_i(Γ_i) ⊂ Γ and Σ with Im φ. Any normalised edition should state this identification instead of silently unifying the letters.

**N6 (second pass) — Scan 33 diagram. Kind: implication not pursued.**
The defining formula pulls back by f_D, but the revised diagram writes (f_{D*})^* three times. With local systems on Π′_D, only (f_D)^* is meaningful. (f_{D*})^* would make sense only after pulling everything back to Π′_{D*} along σ′, using α_{D*D}. This may be what the revision intends, since the comparison map is "défini à l'aide de f_{D*}, f_D, α_{D*D}". Which of the two is meant changes where the square lives.

**N7 (second pass) — Scan 34, rigidity. Kind: model's own idea.**
Building on R5: rigidity holds whenever the images of the f's have trivial centralisers in the target groups. For anabelian data this is the known fact that open subgroups of geometric fundamental groups of hyperbolic curves, and of Gal(K̄/K) for number fields, have trivial centraliser. "Toujours" is too strong for general systems, for example when 𝓔 is abelian. So the expectation is plausible exactly on the anabelian locus where Conjecture 7.1 is stated.
