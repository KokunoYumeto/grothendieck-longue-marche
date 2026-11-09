# LM_P067 (scans 81–90) — research notes checked against the corrected transcription

Part A takes the first pass's research notes (`answers/unzipped/LM_P067/LM_P067_notes.md`, §5) one by one: the
decision (keep, correct, drop) with its reason, then the note as it now stands, read against `LM_P067_checked.tex`.
Part B gives the second pass's own notes, labelled as such. "Unproved here" means that these pages give no proof.
Notation follows the corrected text: the group is 𝔖_{0,3} (not 𝒢), the cocycle is ξ, the exponent γ, the hatted map φ̂.

## A. First-pass notes

### Scans 81–83

1. **Scan 81, diagonal NB — question.** Correct: the reading changed. The NB reads "Il faudrait s'assurer par contre
   que la connaissance de g₀ ne détermine pas γ i.e. p, i.e. que le γ tel que ξ = ℓ₀^γ h₀⁻¹ satisfasse (A) ne soit
   pas unique. À éclaircir!" Grothendieck asks to verify that g₀ does not determine γ (equivalently p), i.e. that
   several γ make ℓ₀^γh₀⁻¹ a solution of (A), and leaves the point open.

2. **Scan 81, "Ici, la seule équation délicate" — claim without proof / stated difficulty.** Correct: the equations
   are not missing, they are on scan 80 (package P066): (A) ξρ(ξ)ρ²(ξ) = 1; (B) ξ = λρ(λ)⁻¹ or ξ = λℓ₀⁻¹ρ(λ)⁻¹;
   C σ∞(ξ) = ℓ₁^γ ξ⁻¹ ℓ₀^γ. Only C is delicate: the existence (not the uniqueness, "en bon cas") of γ ∈ Ẑ, plus
   2γ+1 ∈ Ẑ*, which makes it a condition on λ ∈ Π̂_{0,3}, of two types according to the branch of (B). Unproved here.

3. **Scans 81–82, "Je prévois" — conjecture.** Keep. The branch of (B) should be fixed by p ≡ 1 or −1 mod 3
   (γ ≡ 0 or −1 mod 3; γ ≡ 1 is excluded because 3 would divide p), "c'est en tous cas ce qui sera le cas si
   u ∈ Γ_{Q₀}". Unproved here.

4. **Scans 82–83, the test by reduction — deferred work.** Correct: notation, and the relation used. 𝔖̂⁺_{0,3} is
   reduced modulo the single relation ℓ₀³ = 1, i.e. (σ∞ρ)⁶ = 1 (a display with three cubic relations is struck),
   which gives an extension of 𝔖₃ by ⟨ℓ₀, ℓ₁, ℓ∞ | ℓᵢ³ = ℓ∞ℓ₁ℓ₀ = 1⟩; "ou mieux", 𝔖̂⁺_{0,3} ≃ Sl(2,Z)′^ is reduced
   to Sl(2,Z/6Z)′ ≃ Sl(2,Z/2Z) × Sl(2,Z/3Z)′. The matrices of σ∞ and ρ in Sl(2,Ẑ) are postponed ("explicitation
   que nous ferons tantôt").

5. **Scan 83, (61)–(63) — claim without proof (conjectured parametrization).** Correct: the map and the unknowns.
   "On pense donc que u correspond à (ξ, g₀, γ, β)" subject to (62), where g₀ = φ̂(ξ)ε₀^{γ−β} comes from (24 bis)
   and φ̂ is the homomorphism Π̂_{0,3} → 𝔖̂⁺_{0,3}. Eliminating g₀ gives (63) in the unknowns (ξ, r, s), r = γ−β,
   s = γ+β (r and s are written over γ and β), with r+s+1 = p ∈ Ẑ*. The correspondence itself is conjectured.

6. **Scan 83, last paragraph — implication not pursued.** Keep (with ξ). λ is determined up to λ ↦ ℓ₀^α λ, which
   turns ξ into ℓ₀^α ξ ℓ₁^{−α}; scan 80 adds g₀ ↦ g₀ℓ₀^{−α}. Which data of (63) are invariant is not examined.

7. **Scan 82 — model's own idea (finite check modulo 6).** Keep. Once σ∞ and ρ have explicit matrices, compute in
   Sl(2,Z/6Z)′ and test the two classes of p mod 3 separately. A positive finite check would not prove the
   profinite statement.

8. **Scan 83 — model's own idea (formal elimination).** Correct: carried out. The forward elimination (62) ⇒ (63)
   holds (note B3). The converse, rebuilding g₀ and u from a solution of (63), still needs the facts of the
   earlier pages (Π̂_{0,3}^{σ∞} = {1}, the lifting of u).

### Scans 84–86

9. **Scan 84, heading — claims without proof.** Correct: the group's name. Under "Récapitulation sur le groupe",
   𝔖_{0,3} is identified with Π₁(U^{an}_{0,3}, 𝔖₃; −j̄), with Π̃′_{0,3} ≃ Π₁((ℙ^{1an}, 0{0}+2{1}+3{∞}), {1,τ}; −j̄),
   with Gl(2,Z)′ = Gl(2,Z)/{±1} ≃ GP(1,Z) and with 𝒯′_{1,1} = 𝒯_{1,1}/{±1}. None is proved on this page.

10. **Scan 84, (1) — claim without proof.** Keep (with 𝔖). 𝔖_{0,3} is an extension of 𝒯_{0,3} ≃ 𝔖₃ × Z/2Z by
    Π_{0,3} = Π₁(U^{an}_{0,3}; −j̄); §37 states the same ("S0,3 est une extension de T0,3 = S3 × Z/2Z par π0,3",
    CSG/IUT), so the construction is earlier in the manuscript.

11. **Scan 84, (2)–(4) — formulas to be checked.** Keep, with a precision. (3) holds for composition read from
    right to left (σ̇₀σ̇₁(z) = σ̇₀(1/z) = 1/(1−z) = ρ̇(z)). The insertion over σ̇₀ is a separate doubt (B5).

12. **Scan 85, margin NB — claim without proof.** Keep: the empty fixed sets of ρ̇τ and ρ̇⁻¹τ are verified in B6.

13. **Scan 85, "L'image la plus suggestive" — geometric picture, not a conjecture.** Keep. τ, τ̇′₀, τ̇′₁, τ̇′∞ are
    the reflections in the equator and in three meridians through the poles −j̄, −j, which cut the equator at
    0, ½, 1, 2, ∞, −1; the figure also names the reflections ṙ₀, ṙ₁, ṙ∞ (τ̇′₀ = ṙ₁, τ̇′∞ = ṙ₀).

14. **Scan 85, (7)–(9) — model's own idea (ledger of fixed loci).** Keep; carried out in B6 for (8), (9) and the NB.

15. **Scan 86, the 12 triangles — claim without proof.** Keep. The four great circles cut the sphere into 12
    spherical triangles, fundamental domains permuted simply transitively by 𝒯_{0,3} ≃ 𝔖₃ × Z/2 of order 12; the
    insertion identifies them with the barycentric subdivision of the two hemispheres of ℙ¹_ℝ with vertices 0, 1, ∞.

16. **Scan 86, (11)–(12) — model's own idea (reflection-group presentation).** Keep, with B7. The reflections
    τ, τ̇′∞, τ̇′₀ in the sides of the triangle (−j̄, 0, ½) give a (2,2,3) Coxeter presentation of 𝒯_{0,3}; B7 shows
    that (12) agrees with (3) only if its middle generator is τ̇′₀τ̇′∞ = ρ̇⁻¹.

17. **Scan 86, (13) — claim without proof.** Keep. Π_{0,3} is generated by ℓ₀, ℓ₁, ℓ∞ with the single relation
    ℓ∞ℓ₁ℓ₀ = 1; the order of the product depends on the basepoint −j̄ and on loop conventions not drawn here.

18. **Scan 86, the stabilizer of −j̄ — claim without proof.** Keep (with 𝔖′₃ and sg). The index-2 subgroup
    𝔖′₃ = (𝒯_{0,3})_{−j̄} = {(g, τ^ε) : sg(g) = (−1)^ε} = {1, τ̇₀, τ̇₁, τ̇∞, ρ̇, ρ̇⁻¹} acts on Π_{0,3}, its actions
    being named 1, τ′₀, τ′₁, τ′∞, ρ, ρ⁻¹; B8 checks one element against the basepoint.

19. **Scan 86, the two families of involutions — model's own idea.** Keep, sharpened. On the sphere the τ̇ᵢ = τσ̇ᵢ of
    (6) and the τ̇′ᵢ of (7) are the same maps (τσ̇₀(z) = z̄/(z̄−1)); the two names only separate for the lifts to
    𝔖_{0,3}, where τᵢ = σᵢτ′ᵢ (scan 87).

### Scans 87–88

20. **Scan 87, (17)–(18) — claims without proof.** Correct: the doubt is now located. (17) and the first two chains
    of (18) agree with (14) and (16); the third chain ends with ℓ₀ρ⁻¹ in the ink, whereas (14) gives ρℓ∞ = ℓ₀ρ.
    The transcription keeps the ink (B10).

21. **Scan 87, the characterization of τᵢ — claim without proof.** Keep. τᵢ = σᵢτ′ᵢ = τ′ᵢσᵢ "est caractérisé" by lying
    over τ, having square 1 (insertion) and commuting with σᵢ (or with τ′ᵢ); the margin "rappeler pourquoi on a cette
    caractérisation" defers the proof of uniqueness.

22. **Scan 87, last lines — deferred work.** Correct: the reference. It is "[C]", with square brackets, and the same
    [C] occurs on scan 86 ("τ′₀, τ′₁, τ′∞ étaient notés précédemment (dans [C]) σ̄₀, σ̄₁, σ̄∞"): [C] is an earlier
    text of the author in which these operators were described under other names. The adjective of "la
    description … (faite dans [C])" is still uncertain.

23. **Scan 88, εᵢ² = ℓᵢ — claim without proof.** Keep. εᵢ (ε₀ = σ∞ρ = ρσ₁, ε₁ = σ₀ρ = ρσ∞, ε∞ = σ₁ρ = ρσ₀) lies in
    𝔖⁺_{0,3} over σ̇ᵢ and is "caractérisé" by εᵢ² = ℓᵢ; uniqueness of this square root over σ̇ᵢ is not proved here.

24. **Scan 88, the exception for ρ̇τ, ρ̇⁻¹τ — claim without proof.** Keep. The two elements of order 6 cannot be
    lifted with the same order, "en effet ℙ¹^{ρ̇τ} = ℙ¹^{ρ̇⁻¹τ} = ∅"; the empty fixed sets are checked in B6, the step
    from fixed points to lifts is the general theory invoked in the next sentence.

25. **Scan 88, "On sait que" — claim without proof.** Keep. Lifts of the same order, up to Π_{0,3}-conjugation,
    correspond to the connected components of the fixed points in U = U^{an}_{0,3} of the corresponding
    topological automorphisms; this underlies all the counts that follow.

26. **Scan 88, the counts — claim without proof.** Keep. One class each over σ̇ᵢ and τ̇′ᵢ; three over τ (τ₀, τ₁, τ∞);
    two over ρ̇, ρ̇⁻¹ (poles −j̄, −j; −j̄ is chosen); the lifts at −j are obtained by conjugating with a τᵢ.

27. **Scans 87–88 — model's own idea (audit on free-group words).** Keep; partly done in B8–B10, which find two
    entries that disagree with the rest of the tables ((14) last entry, (18) last chain).

28. **Scan 88 — model's own idea (cocycle formulation).** Keep. Lifts of order n of an element of order n of
    𝔖_{0,3}/Π_{0,3}, up to Π_{0,3}-conjugation, are nonabelian 1-cocycles of Z/n in Π_{0,3}; comparing this with the
    fixed-component description is a route for checking the counts, not a result.

### Scans 89–90

29. **Scan 89, (23) — claim without proof.** Keep; the inserted identities are verified in B11. That ρ₀, ρ₁, ρ∞ are
    not Π_{0,3}-conjugate to ρ is asserted, not proved; it is what the fixed-point correspondence predicts (two
    poles, two classes).

30. **Scan 89, (24) — claim without proof.** Keep. Π_{0,3}^{σᵢ} = Π_{0,3}^{ρ} = Π_{0,3}^{τᵢ} = Π_{0,3}^{τ′ᵢ} = {1} is
    drawn from "la théorie générale" and from the 1-connectedness of the components of the fixed-point sets.

31. **Scan 89, the stabilizers — claim without proof.** Keep. The two exceptional orbits (2, −1, ½) and (−j̄, −j)
    have stabilizers of order 4 (at 2: D₂ ≃ Z/2Z × Z/2Z, generated by σ̇₀, τ̇₀) and 6 (at −j̄: 𝔖′₃ ≃ D₃), both lifted
    to 𝔖_{0,3}.

32. **Scans 89–90, the classes of these lifts — claim without proof.** Keep. D₂^{(0)} has one fixed point (2),
    𝔖′₃ = D₃ two (−j̄, −j); the class for −j is obtained by conjugating with any τᵢ, consistent with (23), where
    the three conjugates are Π_{0,3}-conjugate to each other.

33. **Scan 90, (25)–(27) — implication not pursued.** Keep; verified in B12. The unoriented triangulated
    cartographic group Π̃′_{0,3} has involutive generators σ₀, σ₁, σ₂ (retraced marks read as primes) with
    relations (25); its index-2 subgroup Π′_{0,3} is the quotient of Π_{0,3} by ℓ₁², ℓ∞³, via (27).

34. **Scan 90, last line — deferred continuation.** Keep. "Cet homomorphisme se prolonge en" continues on scan 91,
    outside this package.

35. **Scan 89, (23)–(24) — model's own idea (universal cover).** Keep. Realize the lifts as lifts of the conformal
    maps to the universal cover of U based over −j̄ and compare the classes of ρ and ρ₀ through their fixed points.

36. **Scan 90 — model's own idea (presentation of the index-2 subgroup).** Correct: done. The even-length subgroup
    of (25) is generated by ρ_f, ρ_s, σ with the relations (26) (B12).

## B. Second-pass notes (mine)

B1. **Scan 81, NB — question, read precisely (second pass).** Since h₀ = σ∞(g₀)⁻¹g₀ is fixed with g₀, the NB asks
    whether {γ ∈ Ẑ : ℓ₀^γ h₀⁻¹ satisfies (A)} has more than one element. This is not the uniqueness stated on scan 80
    (there ξ is fixed and C has at most one solution γ); here h₀ is fixed and ξ moves with γ. The first word of
    "ne détermine pas" could also be "n'en".

B2. **Scan 82 — implication not pursued (second pass).** The prime in Sl(2,Z/6Z)′ and Sl(2,Z/3Z)′ is presumably the
    quotient by {±1}, as Gl(2,Z)′ = Gl(2,Z)/{±1} on scan 84; then the displayed isomorphism is the Chinese-remainder
    splitting, −1 being 1 modulo 2. The relation ℓ₀³ = 1 ⇔ (σ∞ρ)⁶ = 1 matches ε₀ = σ∞ρ, ε₀² = ℓ₀ of (22).

B3. **Scan 83 — check of the elimination (62) ⇒ (63) (second pass).** With σ∞(x) = σ∞xσ∞⁻¹ (scan 87: g(x) = gxg⁻¹),
    σ∞² = 1 (by (16) σ∞² fixes ℓ₀, ℓ₁) and (22), σ∞(ε₀) = ρσ∞ = ε₁. Putting g₀ = φ̂(ξ)ε₀^r into
    ξσ∞(g₀)⁻¹g₀ = ℓ₀^γ = ε₀^{2γ} gives σ∞(φ̂(ξ))⁻¹φ̂(ξ) = ε₁^r ξ⁻¹ ε₀^{2γ−r} = ε₁^r ξ⁻¹ ε₀^s, the second line of (63),
    and 2γ+1 = r+s+1: (63) follows from (62) as written.

B4. **Scan 84, margin — claim without proof (second pass).** Grothendieck counts five descriptions ("visions") of
    𝔖_{0,3} in the recapitulation and says there are in fact about ten, "cf. (V) ci-dessous"; the author's table of
    contents has §42 V "Les avatars de S0,3" (ms p. 336). The five are presumably Aut_lac(Π_{0,3}), the
    equivariant π₁ with 𝔖₃, the orbifold group Π̃′_{0,3}, Gl(2,Z)/{±1} ≃ GP(1,Z) and 𝒯′_{1,1}.

B5. **Scan 84, (2) — check (second pass).** z/(z−1) = 1 + 1/(z−1). The insertion over σ̇₀ is correct only with the
    denominator z−1, while the dark retraced strokes look like 1−z; the transcription keeps both readings.

B6. **Scan 85, (8), (9) and the NB — check (second pass).** σ̇₀, σ̇₁, σ̇∞, ρ̇ fix {0,2}, {1,−1}, {∞,½}, {−j̄,−j}
    (for ρ̇: z² − z + 1 = 0), as displayed. Fix(τ̇′₀) = {z + z̄ = zz̄} = {|z−1| = 1} = 1 + 𝕌, so the stacked insertion,
    if it reads "= ½ − 𝕌", is wrong. ρ̇τ(z) = 1/(1−z̄) = z forces z − |z|² = 1, so z real with z² − z + 1 = 0,
    impossible, and ∞ ↦ 0; ρ̇⁻¹τ likewise: the NB is right.

B7. **Scans 84 and 86, (3) against (12) — inconsistency in the ink (second pass).** From (3) (σ̇∞σ̇₀ = ρ̇, involutions)
    σ̇₀ρ̇σ̇∞ = (σ̇₀σ̇∞)² = ρ̇⁻² = ρ̇ ≠ 1. What holds is σ̇₀·(τ̇′₀τ̇′∞)·σ̇∞ = (ττ̇′∞)² = 1 with τ̇′₀τ̇′∞ = ρ̇⁻¹ by (10); so
    (12) is right only if its ρ̇ stands for the generator τ̇′₀τ̇′∞, which supports the exponent −1 in the generator
    list above (12). The unsubscripted σ̇² in (12) is a further slip or abbreviation.

B8. **Scans 86–87 — checks of the stabilizer, (16) and (14) (second pass).** τ̇′₀(−j̄) = −j/(−j−1) = −j̄, so τ̇′₀
    fixes the basepoint, as stated. Applying σᵢ to ℓ∞ℓ₁ℓ₀ = 1 gives each third entry of (16) from the first two
    (e.g. σ∞(ℓ∞) = (ℓ₀ℓ₁)⁻¹), which supports the overwritten ℓ₁, ℓ₀ of the σ∞ row. In (14), τ′∞ = τ′₁ρ (from (15))
    gives τ′∞(ℓ∞) = ℓ∞⁻¹ and τ′∞(ℓ₀) = ℓ₁⁻¹ as written, and τ′∞(ℓ₁) = ℓ₀⁻¹, not the ℓ₁⁻¹ of the last written entry.

B9. **Scan 87 — implication (second pass).** The identification Aut_lac(Π_{0,3}) ≃ 𝔖_{0,3} makes each σ both an
    element and the automorphism x ↦ σxσ⁻¹; this convention is the one behind σ∞(g₀) in (62)–(63) and has to be
    kept when (17)–(22) are checked.

B10. **Scan 87, (18) — inconsistency in the ink (second pass).** σ∞σ₀ = ρℓ∞ = ℓ₀ρ follows from ρℓ∞ρ⁻¹ = ℓ₀ in
     (14); the ink writes ℓ₀ρ⁻¹ (the exponent is clearly visible and is kept). The other chains, ρℓ₀ = ℓ₁ρ and
     ρℓ₁ = ℓ∞ρ, follow the same rule.

B11. **Scan 89, (23) — check (second pass).** From (17) ρτ₀ = τ₁ρ, (20) τ₀² = 1 and (21) τ₁τ₀ = ℓ∞:
     ρ₀ = τ₀ρτ₀ = τ₀τ₁ρ = ℓ∞⁻¹ρ, and ℓ∞⁻¹ρ = ρℓ₁⁻¹ because ρ⁻¹ℓ∞ρ = ℓ₁ by (14). Likewise ρ₁ = ℓ₀⁻¹ρ = ρℓ∞⁻¹ and
     ρ∞ = ℓ₁⁻¹ρ = ρℓ₀⁻¹: these are exactly the inserted formulas, so each ρᵢ differs from ρ by a peripheral loop.

B12. **Scan 90, (25)–(27) — check, and a link with scan 85 (second pass).** With ρ_f = σ′₁σ′₀, ρ_s = σ′₂σ′₁,
     σ = σ′₀σ′₂, (25) gives ρ_fσρ_s = σ′₁σ′₀σ′₀σ′₂σ′₂σ′₁ = 1, σ² = 1 and ρ_f³ = 1, i.e. (26), and (27) sends
     ℓ∞ℓ₁ℓ₀ = 1 to ρ_fσρ_s = 1, so Π′_{0,3} = Π_{0,3}/⟨⟨ℓ₁², ℓ∞³⟩⟩; this supports σ′₀σ′₂ as the third generator. The
     margin's wish to name the generators "carrément r₀, r₁, r∞" matches the labels ṙ₀, ṙ₁, ṙ∞ of the reflections
     in the sides of the fundamental triangle in the sphere figure of scan 85.

B13. **Scan 90 — plan of §42 (second pass).** Heading III announces both the cartographic group Π̃′_{0,3} and "et
     avec Sl(2,Z)"; the author's later table of contents splits this into III (p. 334) and IV "Relations avec
     SL(2, Z)" (p. 335), and writes π0,3 for Π̃′_{0,3}. The target of "Cet homomorphisme se prolonge en" is on scan 91.
