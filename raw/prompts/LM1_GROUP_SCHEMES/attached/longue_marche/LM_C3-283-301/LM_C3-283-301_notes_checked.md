# LM_C3-283-301 — research notes, checked against the corrected transcription (scans 283–301)

Source: the first pass's research notes (answers/unzipped/LM_C3-283-301/LM_C3-283-301_notes.md, §5, 43 notes), each
checked against LM_C3-283-301_checked.tex. Verdicts: keep, correct (text revised), drop. Notes marked **Claude (second
pass)** are new. Kinds: conjecture (Grothendieck's conjectures, questions, expectations, programme), unproved claim,
unpursued implication, own idea. "Unproved" means not proved in the cited passage.

Conventions used in the checks (C0): ρ(x) = ρxρ⁻¹, so ζ = [α,ρ] = αρα⁻¹ρ⁻¹ and η = βσβ⁻¹σ⁻¹; matrices act on
columns, as in (31) on scan 300 (N₁e₀ = e₁, N₁e₁ = 0, N₁ = (0 0; 1 0)). In the numerical case of scan 288,
ρ = (0 1; −1 1), σ = (0 −1; 1 0), ε₁ = −ρσ⁻¹ = (1 0; 1 1), ε₀ = ρ⁻¹ε₁ρ = σ⁻¹ε₁σ = (1 −1; 0 1); so L₀ is the upper
unipotent group, B₀ the upper triangular Borel and B'₀ = {(x y; 0 1)}. With these, δD = c²+cd+d² and δ′U = t²+u² on
scan 288 come out as written, and (74), (79), (90) can be checked by hand.

## Notes of the first pass

### Scans 283–287

- **283-R1 — scan 283, margin NB — unproved claim — correct.** The numerals are 2°), 3°), not 29), 30): fibrewise
  independence of 1, ρ, σ (2°) follows from invertibility of Tr N₁ρ (3°). The margin calculation proves it once there is
  a local basis with N₁e₀ = e₁, N₁e₁ = 0 and ρe₀ ∈ D₁: then ρ = (0 u; a b), Tr N₁ρ = u, and after u = 1,
  σ = −ε₁⁻¹ρ = (0 −1; −a 1−b) and ρ+σ = diag(0,1), so 1, ρ, σ span the same module as 1, diag(0,1), ρ, free of rank 3
  on every fibre because the upper-right entry of ρ is 1. Such a basis exists exactly when D₀ = ρ⁻¹D₁ is a complement
  of D₁, which is the proposition of scans 297–298 ((i) ⟺ (iii), with c = Tr N₁ρ).
- **283-R2 — scan 283, exact sequence and character — unproved claim — correct.** The ink has B₀ without prime in all
  three places (checked enlarged), but both statements hold only for B'₀: for the Borel B₀ the kernel of det is the
  Borel subgroup of SG, of relative dimension 2, and u = diag(x, z) acts on N₀ by x/z, not by det u = xz. For
  B'₀ = {(x y; 0 1)} (C0) one has uN₀u⁻¹ = xN₀ = det(u)N₀ and ker det = L₀, as (74) on scan 281 states; so this is a
  slip of the pen for B'₀, not a gap.
- **283-R3 — scan 283, final morphism — own idea — keep.** The computation it proposes can be done in the numerical case
  of scan 288, where B'₀ = {(x y; 0 1)} is explicit (C0).
- **284-R1 — scan 284, (79) and Corollaire — unproved claim — keep.** The proof strategy is on scan 282 ("il suffit …
  de montrer que c'est surjectif sur les pts à val. dans un corps alg clos … Je laisse tomber le détail des
  vérifications"), so the verifications are left out by the author. Both projections have source 𝒳_ρ in the ink
  (checked), where 𝒳_{ρ,σ} is meant.
- **284-R2 — scan 284, (80) and Scholie — unpursued implication — keep.** On 𝒳_{ρ,σ} the third coordinate is
  μ = 1/Tr ζ(ρ+σ) = 1/Tr η(ρ+σ), with ρ+σ = −N₁σ = N₁ρ = ρN₀ = −σN₀ (the insertion under the trace, now transcribed with
  its brace); the transported group law is made explicit on scan 285.
- **285-R1 — scan 285, (81) — unpursued implication — correct.** (81) is the cocycle identity and is immediate:
  [u′u, ρ] = u′(uρu⁻¹ρ⁻¹)u′⁻¹ · u′ρu′⁻¹ρ⁻¹ = u′(ζ)ζ′, and μ″ = det(u′u) = μμ′. The note's question, a law written in
  (ζ, η, μ) alone without u′, remains open and needs the inverse of (79).
- **285-R2 — scan 285, (83) épimorphisme — unproved claim — correct.** Given (79) and (87), (83) is the projection
  B'₀ × T_ρ × T_σ → B'₀ ≅ 𝒳_{ρ,σ}, because [ua⁻¹, ρ] = [u, ρ] for a commuting with ρ; so it is a split epimorphism,
  split by (84). What remains unproved here is (87) itself (and (79)).
- **286-R1 — scan 286, (84)–(85) — unproved claim — correct.** That (84) lands in 𝒢_{ρ,σ} is immediate from (79):
  ([u,ρ],[u,σ],det u) ∈ 𝒳_{ρ,σ} says [u,ρ] = [u,σ]ε₁(det u − 1), which is (82) for (u, u, det u). The description of all
  diagonal solutions, which the author postpones ("qu'on tâchera de déterminer aussi"), follows from (87)–(90): see O2.
- **286-R2 — scan 286, tuple and (86) — unpursued implication — keep.** The tuple has (ua, ub) and (86), (89) have
  (ua⁻¹, ub⁻¹) (both checked on the ink); T_ρ and T_σ are groups, so the two parametrisations differ by a ↦ a⁻¹, and
  (89) fixes the form used in the theorem.
- **287-R1 — scan 287, (87)–(90) — unproved claim — correct.** (90) gives the uniqueness of a, b in (88): if αa and αa′
  lie in B'₀ then a⁻¹a′ ∈ T_ρ ∩ B'₀ = {1}; the ink's "l'unicité de α, β" is a slip for a, b, as is "[β,ρ]" for [β,σ]
  in the line before (89). In the numerical case (90) holds as schemes: cρ + d = (d c; −c c+d) lies in B'₀ iff c = 0 and
  d = 1, and tσ + u = (u −t; t u) iff t = 0 and u = 1.
- **287-R2 — scan 287, product parametrisation — own idea — keep.** (87) is an isomorphism of schemes; which group law
  the product B'₀ × T_ρ × T_σ carries is not stated on these pages.

### Scans 288–292

- **B1 — scan 288, (94)–(95) — unproved claim — correct.** The denominators are units wherever α, β occur in a
  solution: αa ∈ B'₀ with a = c₀ρ + d₀ forces (c₀, d₀) = t(c, d) with t(c²+cd+d²) = 1, and likewise for β. Checking the
  formulas themselves shows (94) right and (95) wrong with the σ written on the page: see O1.
- **B2 — scan 288, margin "Il faudra revenir sur ces formules dans le cas général" — conjecture (programme) — keep.**
  (94)–(95) are tied to the numerical ρ, σ; in general only the shape a = c₀ρ + d₀, b = t₀σ + u₀ ((91)–(92)) is stated.
- **B3 — scans 288–289, the factor τ∞^α — conjecture (expectation) — correct.** The author resolves the apparent
  incompatibility on scan 289: loc. cit. wrote the equation of the loops ("des lacets", now read) with a sign,
  ζ = εηℓ₁^ν with ℓ₁^ν = ε₁(μ−1) in the present notation, and on p. 398' the factor τ∞^{α₂} carries that sign
  ((−1)^{α₂} = ε), whereas the present theory assumes ε = +1. What remains is a stated generalisation (B4).
- **B4 — scan 289, (95|96) — conjecture (programme) — keep.** The author will redo the theory for ζ = ε.ηε₁(μ−1) with ε a
  section of 𝒪_S, ε² = 1 by determinants, "sans doute" without assuming ε ∈ {±1}, after finishing the case ε = +1. The
  Circle table's §48.V (p. 454, "L'équation αρ(α⁻¹) = (βσβ⁻¹)ε₁(µ−1); le groupe G*_{ρ,σ}", symbols partly lost in
  extraction) is a lead for where this is done; not checked.
- **B5 — scan 289, ε ∈ {±1} — own idea — keep.** A = F₂[t]/(t²), ε = 1 + t: ε² = 1 and ε ≠ ±1. The author's own caveat
  on scan 295, "en car. 2 λ₀ n'est déterminé que mod μ₂ !!!", is the same phenomenon, so μ₂ (non-reduced in
  characteristic 2) is the natural home both for ε and for the ambiguity of λ₀.
- **B6 — scan 290, forms and P¹-bundles — unproved claim — keep.**
- **B7 — scan 290, bijections induced by SG → G → PG — unproved claim — keep.**
- **B8 — scans 290–291, quotient by homotheties and the conic — own idea — keep.** See also O4 on the definition (1) of
  the conic.
- **B9 — scan 291, a ∈ Γ(S, 𝒪_S*) — unproved claim — correct.** Immediate: N and N′ = aN are non-zero on every fibre, so
  a(s) ≠ 0 at every point and a is a unit.
- **B10 — scan 291, the trace identities — own idea — correct.** The ink "2 Tr λ" (checked enlarged) makes the trace
  identities false as written: for a scalar λ, Tr(λ + N) = 2λ + Tr N, so either "Tr λ" is the trace of the scalar
  operator (= 2λ) and the 2 is redundant, or "Tr" is. The determinant identities are right, and their use (λ = 1:
  (3) ⟺ (1)) is unaffected.
- **B11 — scan 292, λ ∈ ΓG_m — unproved claim — correct.** Immediate as in B9: e′ = 1 + λN is ≠ 1 on every fibre, so
  λ(s)N(s) ≠ 0 and λ is a unit; the ink says "on aura néc.ᵗ λ ∈ ΓG_m".
- **B12 — scan 292, normalisers and Borels — unproved claim — keep.**
- **B13 — scan 292, the affine line E = 𝒫 ∖ {x∞} — unpursued implication — correct.** The package pursues it: the margin
  of scan 294 identifies L with the translation bundle of 𝒫 ∖ {x}; scan 296 takes F to be the extension of 𝒪_S by 𝒩 that
  gives this affine line and (20)–(21) identify 𝒩 = D°⊗D; (27) on scan 299 identifies U₁ = 𝒫 ∖ {x₁} with L₁ once x₀ is
  chosen.

### Scans 293–297

- **C1 — scan 293, vector-bundle structure on L — unproved claim — keep.**
- **C2 — scan 294 margin, L ≅ translations of 𝒫 ∖ {x} — unproved claim — correct.** It follows from (20)–(21): the lines
  D′ complementary to D are the images of the sections of F → F/D, a torsor under Hom(F/D, D) = D°⊗D = 𝒩, and 1 + u
  (u ∈ 𝒩) acts on them by translation by u.
- **C3 — scan 294, (10) — unproved claim — correct.** The first identification is false as written (C4); the other four
  are the standard ones (automorphisms of SG and of PG, Skolem–Noether for M, automorphisms of a P¹-bundle).
- **C4 — scan 294, (10) — own idea — correct (settled).** g ↦ det(g)⁻¹g is an automorphism of Gl(2)_S (a homomorphism
  because scalars are central, and its own inverse) that is not inner: it sends λ·1 to λ⁻¹·1, while inner automorphisms
  fix the centre. So PG → Aut_{S-gr}(G) is not an isomorphism for G = Gl(2)_S or its forms. What the argument uses, that
  ρ, σ act on G through their images in PG, is unaffected.
- **C5 — scan 295, (14)–(16) — unproved claim — keep.** L₁ → PG is a closed immersion (1 + λN₁ scalar forces λ = 0,
  since N₁ is regular and so has locally a unit off-diagonal entry), so ε̃₁ has a unique lift ε₁ in L₁; how (16) then determines λ₀ is C6.
- **C6 — scan 295, NB — unproved claim — correct.** The caveat is now read: "(Mais en car. 2 λ₀ n'est déterminé que mod
  μ₂ !!!)". Proof of the whole NB: ε₁ = −λ₀ρσ⁻¹ unipotent means det = 1 and Tr = 2, i.e. λ₀² det(ρσ⁻¹) = 1 and
  −λ₀Tr(ρσ⁻¹) = 2; two solutions differ by θ with θ² = 1 and 2(θ − 1) = 0, so θ = 1 when 2 is regular, and in
  characteristic 2 only θ ∈ μ₂ is left.
- **C7 — scan 295, rescaling by 1 + δ in characteristic 2 — own idea — correct.** This is the author's "mod μ₂": over
  k[δ]/(δ²), char 2, θ = 1 + δ gives θε₁ with det 1 and trace 2, but θε₁ = 1 + δ + (1+δ)N₁ ∉ L₁. So in characteristic 2
  the normalisation (16) does not fix ε₁; its definition (15) as the lift in L₁ of ε̃₁ does.
- **C8 — scan 296, F as an extension — unproved claim — keep.**
- **C9 — scan 296, (20)–(21) — own idea — correct.** Reading 𝒫 = P(F) as the bundle of lines D ⊂ F (as the text does),
  the tangent line at x_D is Hom(D, F/D), and 𝒩 = D°⊗D = Hom(F/D, D) is its dual, the cotangent line at x_D; by C2 it
  is also the translation bundle of 𝒫 ∖ {x_D}. The V/V̌ convention in (9) was not checked against the author's.
- **C10 — scan 297, reduction to an algebraically closed field — unproved claim — correct.** (22) needs no reduction:
  ρ̃σ̃⁻¹ ∈ ΓL̃₁ normalises L̃₁, so ρ̃⁻¹(L₁) = σ̃⁻¹(L₁) as subgroup schemes. The reduction serves (i) ⟺ (iii), whose
  conditions are fibrewise (c a unit; ε₁ ≠ 1 and ρ̃⁻¹(x₁) ≠ x₁ on every fibre), so passing to geometric points is
  legitimate; scan 282 appeals to the same "principes généraux".
- **C11 — scan 297, (iii) as a principal open — unpursued implication — keep.** See O3: (iii) does not depend on the
  choice of λ₀.

### Scans 298–301

- **D1 — scan 298, matrix calculation — own idea — correct (settled).** With the conventions of (31) (C0),
  σ = (a b; c d) gives σe₁ = be₀ + de₁; the ink's "σe₁ = ae₀ + be₁" (checked; b and the last index are retraced) is a
  slip. The conclusion is right: Tr N₁σ = b and D + σD = D + 𝒪_S·be₀, which is F iff b is a unit.
- **D2 — scan 298, (23)–(25), "tore (maximal)" — unproved claim — keep.**
- **D3 — scan 299, opposite Borels ↔ maximal tori of B₁ — unproved claim — correct.** Over a base both sides are
  L₁-torsors: L₁ acts simply transitively by conjugation on the maximal tori of B₁ = T.L₁, and by translation on the
  sections x₀ of U₁ = 𝒫 ∖ {x₁} ((27)); B₀ ↦ B₀ ∩ B₁ is L₁-equivariant, hence bijective.
- **D4 — scan 299, (27) — unpursued implication — keep.**
- **D5 — scan 300, (28), "épinglage complet" — unproved claim — correct.** In the normal form (31)–(32) the three
  sections are x₁ = [e₁], x₀ = [e₀] and ε₁x₀ = [e₀ + e₁], the points ∞, 0, 1 of P¹_S up to the labelling; the claim is
  that (ρ, σ) with the regularity conditions give this pinning canonically.
- **D6 — scan 300, (29)–(31) — own idea — keep.** After D₁ ≃ 𝒪_S, e₁ is fixed up to a unit and e₀ is then fixed by
  N₁e₀ = e₁ (30); the model is canonical only up to that unit.
- **D7 — scan 301, (33) — unproved claim — keep.** The residual freedom is a common scalar, (ρ, σ) ↦ (λρ, λσ), which
  preserves ρσ⁻¹ = −ε₁; (34) fixes it by the upper-right entry, a unit since det ρ = −uv is.
- **D8 — scan 301, (*) and (34) — own idea — correct.** Done: (33) gives σ = −ε₁⁻¹ρ = (0 −1; −v 1−w) and
  ρ + σ = diag(0, 1), the margin normal form of scan 283 with (a, b) = (v, w) and (37) at the top of scan 302; v = −1,
  w = 1 is the numerical case of scan 288. Nothing changes in characteristic 2.

Verdicts: 43 notes; keep 20, correct 23, drop 0.

## New notes — Claude (second pass)

- **O1 — scan 288, (95) — own idea — Claude (second pass).** With the σ on the page, σ = (0 −1; 1 0), formula (95) fails:
  β(tσ + u) has lower-left entry 2tu, and β = σ (t = 1, u = 0) gives b = σ, βb = σ² = −1 ∉ B'₀. The formula that works
  is b = (u − tσ)/(t² + u²), i.e. (tσ∞ + u)/(t² + u²) with σ∞ = σ⁻¹ = (0 1; −1 0), the matrix of p. 398'; (94) is right,
  since α(cρ + d) = (δ, ac+bc+bd; 0, c²+cd+d²). Confidence high (explicit 2×2 computation with C0); it bears out the
  author's "sauf erreur".
- **O2 — scan 286, (85) — unpursued implication — Claude (second pass).** The diagonal solutions follow from (87)–(90):
  α = β in (89) forces a = b ∈ T_ρ ∩ T_σ, the common centraliser of ρ and σ, which is G_m when 1, ρ, σ are independent
  on every fibre (2°). So the solutions of (85) are the pairs (u, μ) with u ∈ Γ(B₀), B₀ = B'₀·G_m, and μ the character
  by which u acts on N₀ (u(N₀) = μN₀). Confidence medium: in the numerical case T_ρ ∩ T_σ = G_m holds as schemes
  (cρ + d commutes with σ iff c = 0); the general case needs the same check.
- **O3 — scans 297–298, condition (iii) — own idea — Claude (second pass).** (iii) does not depend on the choice of λ₀
  left open in characteristic 2: two admissible values differ by θ with θ² = 1 and 2(θ − 1) = 0, so
  (θ − 1)² = −2(θ − 1) = 0, and c changes by the square-zero element (θ − 1)λ₀Tr ρ. So "c = λ₀Tr ρ + Tr σ inversible"
  is well posed over every base. Confidence high.
- **O4 — scan 290, (1) — unpursued implication — Claude (second pass).** The ink replaces a struck "N² = 0" by (1), "det N
  = 0, Tr N = 0, d'où N² = 0". For sections non-zero on every fibre the two agree: Cayley–Hamilton gives
  Tr(N)·N = det(N)·1, and locally N has a unit off-diagonal entry, which forces Tr N = 0 and then det N = 0. Without
  regularity they differ (N = δ·1, δ² = 0, 2 ≠ 0: N² = 0 but Tr N = 2δ), so (1) is the sound definition of the conic.
