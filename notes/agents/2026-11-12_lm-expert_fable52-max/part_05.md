- (2:sc351–363, pp. 177–183) (3) 2g'−2+card I' = n(2g−2+card I): −EP_! ≥ 1 is the anabelian condition, stable under
  coverings. Every discretization of π induces one of π' ⊂ π (oriented ones too, via the trace isomorphism T' ≃ T).
  **C (2:sc352)** for π' normal in π, G = π/π': Discrét(π) → Discrét(π') is injective, with image the π'_0 such that
  G → 𝒯̂̂(π̂'_0) factors through 𝒯(π'_0) (even 𝒯(π'_0)^+). Necessity clear; sufficiency reduces to: the extension π_0
  of G by π'_0 is a loop group with the right d_i — "comme si on savait déjà que toute extension sans torsion d'un
  groupe fini par un groupe à lacets est (de la façon canonique) un groupe à lacets" (N: this is the
  torsion-free-virtually-surface-group statement, a theorem via Nielsen realization/Eckmann–Müller–Linnell and the
  convergence group theorem; exact form for READING_BASE). **Cor** injectivity "en tous cas". **NB** not always
  bijective: conjugate G ⊂ 𝒯(π'_0) by γ ∈ 𝒯̂̂ so that it no longer stabilizes a discretization ("Un tel γ existe
  toujours").
- **C/expectations (4)–(6)**: Prédiscr^+(π) → Prédiscr^+(π') bijective, Préarith(π) → Préarith(π') bijective, and
  Γ_Σ ≃ Γ_{Σ'} canonically. Reduction to π' characteristic; conditions on the inclusions (7)
  𝔖̂^+(π_0) ⊂ M(π_0) ⊂ 𝔖̂̂(π_0) into the same for π'_0: (a) injectivity of P(π) → P(π') ("assez plausible"), (b)
  surjectivity ("beaucoup plus problématique, voire douteuse": 𝒯̂̂(π_0)~ = Norm_{𝒯̂̂(π'_0)}(G) may be much smaller than
  𝒯̂̂(π'_0)), (c) M(π_0) → M(π'_0) (needed to define A(π) → A(π') and Γ_Σ → Γ_{Σ'}; "pas anodine du tout"), (d), (e).
  Test cases he names: π' of index 2; the kernel of π → (π_ab)_2 for π = Π̂_{0,3}: "situation de la courbe de Fermat
  x^2+y^2+z^2 = 0 (revêtement octaédral de P^1∖{0,1,∞})".
- **D (2:sc364–366)** *correspondences* between loop groups π, π': (π'', p: π'' → π, q: π'' → π') with p, q composites
  of hole-pluggings and isomorphisms onto finite-index subgroups; *arithmetic correspondences* (with Σ'' = p^*Σ =
  q^*Σ'); they induce *arithmetically exterior isomorphisms* (P_Σ, Γ_Σ) ≃ (P_{Σ'}, Γ_{Σ'}); the connected groupoid of
  "courbes arithmétiques extérieures", with automorphism group Γ_0 of the reference object; equivalent to the
  category of Γ_0-torsors.

### §29 Critique of the preceding approach (2:sc367–378, pp. 186–191)

- "L'approche des § précédents semble franchement très brutale." Doubts on the hole-plugging conjecture: the
  canonical (1) 𝒯̂̂(π)_i → 𝔖̂̂(π') (stabilizer of i) "il est problématique si c'est un isomorphisme — et même si c'est
  injectif, ou si c'est surjectif". What holds: for a discretization π_0, 𝒯(π_0)_i ≃ 𝔖(π'_0), 𝒯̂(π_0)_i ≃ 𝔖̂(π'_0), so
  (4) 1 → π̂'_0 → 𝒯̂(π_0)_i → 𝒯̂(π'_0) → 1 and an injection (5) i_{π_0}: π' → 𝒯̂̂(π)_i depending on π_0:
  i_{u(π_0)} = int(u)∘i_{π_0}∘u_{π'}^{-1}; independence ⇔ its image is normal in 𝒯̂̂(π)_i. **D** H_{π_0,i} := elements
  of 𝒯̂̂(π)_i normalizing i_{π_0}(π') and acting on it through (1); H_{π_0} := elements of 𝒯̂̂(π) permuting the i_{π_0,i};
  H ⊃ 𝒯̂(π_0). **Key remark (2:sc369)**: the image of π_1(M_{g,ν}) in 𝒯̂̂ must not only normalize 𝒯̂^+ but lie in H.
  "Il est possible que 𝒯̂̂(π_0) soit un groupe à tel point démesuré et pathologique, qu'il ne pourra jamais être
  question d'en dire des choses raisonnables"; one should work with smaller subgroups "qui restent proches du
  discret". In 𝒯̂(π_0) (ν ≠ 0) there is a "structure simpliciale d'extensions successives" respected by Galois: part
  of the "structure à l'infini" of π_1 of the modular multiplicities M_{g,ν} (N: the first appearance of the
  Teichmüller-tower/stratification-at-infinity idea of the Esquisse).
- **New definitions (2:sc371–377)** (replacing the normalizer definitions): from the transcendental construction,
  π_1(𝒰_{g,ν,Q}) with its three-step filtration (π̂_{g,ν}; 𝒯̂^+; Γ_Q) maps ("on présume injectivement") to 𝔖̂̂_{g,ν};
  **M_{g,ν} := its image**, 𝔖̂_{g,ν} ⊂ M_{g,ν} ⊂ 𝔖̂̂_{g,ν}; **N_{g,ν} := M_{g,ν}/π̂**, 𝒯̂_{g,ν} ⊂ N_{g,ν} ⊂ 𝒯̂̂_{g,ν}, with 𝒯̂^+
  normal in N; **Γ_{g,ν} := N_{g,ν}/𝒯̂^+_{g,ν}** (12), with canonical element τ_{g,ν} of order 2; Γ_Q ↠ Γ_{g,ν} (13)
  "dont on présume qu'il est bijectif". For (π, α) (α a prediscretization): M_α, N_α, Γ_α, τ_α by transport.
  **D** *arithmetization* of π: an element of A(π) := Isom_lac(π̂_{g,ν},π)/M_{g,ν} = Isomext_lac/N_{g,ν} (20);
  P(π) := oriented prediscretizations (21); A(π) = P(π)/Γ_{g,ν} (22): P_a is a Γ_{g,ν}-torsor; M_a, N_a, 𝒯̂^+_a
  (independent of α ∈ P_a), Γ_a := N_a/𝒯̂^+_a = Γ_{g,ν} twisted by P_a.
  Three connected groupoids with origin (π̂_{g,ν}, a_{g,ν}): exterior arithmetized loop groups (automorphism group
  N_{g,ν} ≃ π_1(M_{g,ν,Q}) if Γ_Q → Γ_{g,ν} is injective; objects = universal coverings of M_{g,ν,Q}); arithmetized
  loop groups (M_{g,ν} ≃ π_1(𝒰_{g,ν,Q}); objects = universal coverings of 𝒰_{g,ν,Q}); arithmetized loop groups with
  arithmetically exterior isomorphisms (Γ_{g,ν}; conjecturally = algebraic closures of Q).
  **P/C (29),(30)** P_a → {elements of order 2 of Γ_a}, α ↦ τ_α, τ_α = τ_{−α}; if Γ_Q ≃ Γ_{g,ν}: a bijection
  P_a/±1 ≃ {elements of order 2 of Γ_a} (uses: the only elements of order 2 of Γ_Q are the conjugates of τ, and
  Centr(τ) = {1,τ}); an unoriented prediscretization over a = an archimedean valuation of Q̄.

### §30 Properties of the N_{g,ν}, Γ_{g,ν}: (a) properties tied to finite subgroups (2:sc379–391, pp. 192–198)

- Aim: properties, suggested by geometry, formulated purely algebraically, "assez fortes peut-être pour finir par
  caractériser les N_{g,ν}". A curve of type (g,ν) over Q̄ ⇔ a germ of lifting of N_a → Γ_a (kernel 𝒯̂^+_a), over a
  finite K' a lifting on an open Γ'; only *admissible* liftings (special properties, some "du genre Weil").
  For a closed Γ ⊂ M_a with (a) Γ → Γ_a injective with open image: wanted (b) π^{Γ'} = 1 for open Γ' ⊂ Γ (rigidity
  of the category of points); (c) Z := (𝒯̂^+_a)^{Γ^♮} = Centr_{N_a}(Γ̃^♮) ∩ 𝒯̂^+_a is finite (= Aut of the curve over Q̄),
  and conjugate in M_a to a subgroup of some 𝒯(π_0)^+.
- For a finite G ⊂ 𝒯̂^+_a contained in some 𝒯^+(π_0) and realizable: there is an admissible germ Γ_a → N_a
  centralizing G; Centr_{N_a}(G) → Γ_a has kernel 𝒯̂_a^{+G}, not finite in general (the fixed locus of G in
  Teichmüller space has positive dimension unless U/G has genus 0 ...). **(d)** for every finite G ⊂ 𝒯̂^+_a (at least
  G ⊂ 𝒯^+): N_a ∩ Z(G) → Γ_a has open image (Z(G) the centralizer in 𝒯̂̂). Consequence: Γ_{g,ν} ∩ Z'_{g,ν} is open in
  Γ_{g,ν}, Z'_{g,ν} the intersection of the images of the centralizers of the finitely many classes of finite
  subgroups of 𝒯(π_{g,ν}). For finite (cyclic) G ⊂ 𝔖(π_0) (action with a fixed point): π^G = 1 (known discretely,
  admitted profinitely), 𝔖̂̂^G → 𝒯̂̂^G injective. He corrects himself: 𝔖(π_0)^G → 𝒯(π_0)^G is not surjective
  (automorphisms commuting with G only permute the fixed points); only the stabilizer of the point lifts.

### §31 Liftings of an exterior action of a finite group on a profinite loop group (2:sc391–394, pp. 198–199)

- G = G^+ ⊂ 𝒯̂̂(π) finite, with an invariant discretization π_0 (G ⊂ 𝒯(π_0)). Discrete case understood: the finite
  groupoid [U^!] with strict G-action whose points are the π_0-classes of maximal partial sections; u̇ ∈ 𝒯(π_0)^G
  lifts to 𝔖(π_0)^G iff u̇(P) = P. **Q/C (2:sc393)**: (a) is {π_0-classes of splittings of 1 → π_0 → E → G → 1} →
  {π̂_0-classes of splittings of 1 → π̂_0 → Ê → G → 1} bijective? (b) is π^G = 1 for G ≠ 1? "J'ai envie de conjecturer
  sans vergogne qu'il en est ainsi". (N: this is a torsion/conjugacy-separability ("goodness"-type) question for
  virtually surface groups: finite subgroups of the profinite completion of a Fuchsian group are conjugate to
  finite subgroups of the discrete group; to cite exactly — it is known for good/virtually free and Fuchsian
  groups; LM4.)

### §32 Arithmetic aspects of hole plugging: Γ_{g,ν} versus Γ_{g,ν−1}; curves as "potential curves" (2:sc395–436, pp. 200–220)

- (1)–(4) N_{g,ν} = N^!_{g,ν}·𝒯̂^+_{g,ν}, N^!/𝒯̂^{!+} ≃ Γ_{g,ν}. For each i (with (g,ν−1) anabelian, 2g+ν ≥ 4): the
  injective (5) φ_i: π'_i → 𝒯̂^{+!} ⊂ N^! ⊂ 𝒯̂̂_i. **(e)** ("il est vrai que") N^!_{g,ν} normalizes the images of the
  π'_i ↪ 𝒯̂^{!+}_{g,ν} (0 ≤ i ≤ ν−1). **(f)** ψ_i: 𝒯̂̂^!_{g,ν} → 𝔖̂̂^!_{g,ν−1} induces an *isomorphism* (6)
  N^!_{g,ν} ≃ M^!_{g,ν−1}: the map exists and is surjective by the arithmetic-geometric definition, since (8)
  Θ_{g,ν}: Γ_Q ↠ Γ_{g,ν} and Θ_{g,ν−1} are compatible; bijectivity ⇔ Θ_{g,ν} and Θ_{g,ν−1} have the same kernel.
  "Il ne serait pas impossible que (f) soit faux, i.e. que les Θ_{g,ν} soient infidèles, mais de moins en moins
  quand on fait augmenter ν", with (perhaps) only the limit Θ_{g,∞} faithful. He works with (f): the *fundamental
  exact sequences* (9) 1 → π̂_{g,ν−1} → N^!_{g,ν} → N^!_{g,ν−1} → 1 [M/N as in his text], extending (10)
  1 → π̂_{g,ν−1} → 𝒯̂^!_{g,ν} → 𝒯̂^!_{g,ν−1} → 1, "et tient lieu de la suite exacte peut-être défaillante"
  1 → π̂_{g,ν−1} → 𝒯̂̂^!_{g,ν} → 𝒯̂̂^!_{g,ν−1} → 1 (marked ??). For (π,a): arithmetizations a'_i on the π'_i, (11)
  1 → π'_i → (N_a)_i → N_{a'_i} → 1, Γ_a ≃ Γ_{a'_i} (13), P_a ≃ P_{a'_i} (14). No claim on a bijection of the sets of
  arithmetizations. **P** hole plugging = an equivalence {exterior arithmetized profinite loop groups of type (g,ν)}
  ≃ {arithmetized (non-exterior) loop groups of type (g,ν−1)}.
  (N: with the arithmetic definition, (f) is exactly: the kernel of the outer Galois action on π̂_1 of M_{g,ν}-type
  objects is independent of ν; this is known: the kernels of Γ_Q → Out(π̂_1(M_{g,n})) are all trivial by Belyi for
  genus 0 and by Matsumoto/Hoshi–Mochizuki in general; injectivity statements to cite.)
- **Q (15)** describe Γ_{g,ν} inside Γ'_{g,ν} := Norm_{𝒯̂̂}(𝒯̂^+)/𝒯̂^+ via its exterior action on 𝒯̂^+_{g,ν} or 𝒯̂^{+!}_{g,ν}:
  conditions of type (e) (normalizing the π'_i), stable under descent in ν; empty in the limit cases (g,0),
  (1,1), (0,3); "il est possible qu'il faille faire intervenir des propriétés des π_1 des M_{g,ν,Q̄} liées à la
  compactification". Only for (0,3) no such condition is to be expected.
- **D** *potential algebraic curve*: (π, a) with an admissible germ of lifting (16) Γ_a^♮ → N_a; relative to a
  Γ_{g,ν}-torsor P (an algebraic closure of Q). *Points* of π: π-conjugacy classes of admissible liftings (19)
  Γ^♮ → M_a, i.e. germs of true actions with (20) π^{Γ^♮} = 1. **Question liminaire / (g)** ("facultatif"): does
  (π, Σ_a, Γ') determine the arithmetization? ⇔ for every open N' ⊂ N_{g,ν}, the elements of 𝒯̂̂_{g,ν} normalizing
  𝒯̂_{g,ν} and carrying N' into N_{g,ν} lie in N_{g,ν}.
- Plugging I' ⊂ I stable under Γ: Γ ↪ N_{a'} (23); for i' ∈ I' fixed by Γ a canonical Γ → π'(i') lifting the
  exterior action, hence (25) I' → Pts(π',a',Γ). **P ("Je dis que", 2:sc410)** this map is injective — evident
  geometrically; internal reason wanted.
- **Axiomatics (2:sc411–421)**: given, for fixed g, closed subgroups N_{g,ν} ⊂ 𝒯̂̂_{g,ν} normalizing 𝒯̂_{g,ν} with
  M_{g,ν} ≃ ... ≃ M_{g,ν−1} via the ψ_i [(g): (𝔖̂̂_{g,ν})_i → 𝔖̂̂_{g,ν−1} sends (M_{g,ν})_i into M_{g,ν−1}], and a notion
  of *admissible* exterior action of profinite groups Γ on arithmetized π, he asks: (1) stability under open
  subgroups; (2) stability under plugging a Γ-stable I'; a true action is admissible iff the exterior action
  obtained by drilling is; (3) admissible true action ⇒ π^Γ = 1 (rigidity of the Γ-points of B_{π,Γ}); (4) an
  admissible exterior action lifts to an admissible true action on an open subgroup (Pt_ad ≠ ∅); (5) for i fixed by
  Γ, (27) Pt_ad(B_{π,Γ}) → Pt_ad(B_{π'_i,Γ}) is a bijection onto the complement of the canonical point P [a), b),
  c)]; (6) extension of an action from an open Γ' to Γ: existence and uniqueness (uniqueness from L^{Γ'} = 1).
  Consequence: the equivalence (30) {(π,a,I',Γ,θ): Γ fixing each point of I'} ≃ {(π',a',Γ,θ', I' ⊂ Pt_ad(B_{π',Γ})^Γ)}:
  "forage de trous en I'".
- General frame (2:sc422–429): a set X of "points" with groupoids Π_{U_I} for finite I ⊂ X, functorial with strict
  transitivity, loop structures, hole-plugging compatibility, a group Γ acting strictly with all stabilizers Γ_P ≠ 1
  of finite index; wanted: reconstruct X and the Π_{U_I} from the "soft" exterior action of Γ on π = π(∅):
  2°) U_I → Pt(B_{π(I),Γ^♮}) (germs of splittings of the extension E(I) of Γ by π(I)) injective, and with a notion of
  admissible lifting U_I ≃ Pt_ad(B_{π(I)},Γ^♮).
- **"Conjecture provisoire profinie" (2:sc431–433; margin: "Canulé, cf plus bas")**: an exterior action of a
  profinite Γ on an arithmetized anabelian (π,a) is *admissible* if (a) Γ → Γ_a has open image; (b) the effective
  actions deduced by hole plugging normalize no loop subgroup; (c) there are infinitely many π-classes of germs of
  splittings normalizing no loop subgroup (margin: (c) excludes Γ = N_{g,ν} for (g,ν) ≠ (0,3): 𝒰_{g,ν} → M_{g,ν}
  has presumably no étale multisections). An effective action is admissible if the exterior one is and it normalizes
  no loop subgroup. Then: (a) π^Γ = 1 (perhaps even π^{Γ^+} = 1, Γ^+ = Ker χ); (b), (c) no loop subgroup normalized
  after plugging; (d) Pt_ad(B_{π,Γ^♮}) → Pt_ad(B_{π',Γ^♮}) injective with image the complement of {P}.
  **He retracts the surjectivity part (2:sc433–435)**: for Γ = π_1(S), S a parameter scheme of finite type over Q,
  an admissible action = a family of curves over S; two distinct sections need not be disjoint, so surjectivity
  fails. One needs "sections strictement distinctes": proceed by induction on the dimension of S ("se tirer par les
  lacets de souliers"), starting in dimension 0 with *arithmetically faithful* actions (Γ → Γ_a injective), where
  the conjecture "semble raisonnable". "Le test décisif ... serait la possibilité d'obtenir les courbes ainsi
  définies comme des revêtements de P^1∖{0,1,∞}".
  (N: the points-as-sections statements here are the section conjecture for hyperbolic curves over number fields
  with the cuspidal sections removed ("normalize no loop subgroup"), plus its relative version over a base S; the
  remark on non-disjoint sections is the correct obstruction. This is LM6 territory. The claim (5)(c) is the
  section conjecture for the affine curve in terms of the one for the plugged curve.)

### §33 Topological digression: anti-involutions of compact oriented surfaces (2:sc437–, pp. 221–)

- *Algebroid surface*: U = X∖S, X compact orientable, S finite; X = Û the "pure compactification". (U,σ) with σ an
  anti-involution ⇔ (Y,T), Y = Û/σ a compact surface with boundary, T finite; inverse: the oriented double.
  Case ν = 0: χ(Y) = 1 − (γ+μ) for Y non-orientable of genus γ with μ boundary circles; χ(X) = 2χ(Y): g = γ+μ.
  **Proposition/Corollaire as first stated** ((X,σ) of genus g ↔ non-orientable (γ,μ) with γ+μ = g; exactly g+1
  classes, by μ = card π_0(X^σ)) **are corrected in the margins**: this covers only the (X,σ) with X/σ
  non-orientable; there are also the doubles of orientable Y of type (γ,μ), μ ≥ 1, with g = 2γ+μ−1.
  (N: the correct count of conjugacy classes of orientation-reversing involutions of a closed genus g surface is
  ⌊(3g+4)/2⌋ (Weichold/Klein: species (μ, separating or not)); to check in LM4.)
  **Admitted Lemma (2:sc440)**: every anti-involution of the disc (or of C) is conjugate to z ↦ z̄; so its fixed set
  is ≃ R, connected. **Théorème (begins 2:sc440)**: U oriented surface not S^2, σ an anti-involution, E the extension
  of Z/2 by π ...
