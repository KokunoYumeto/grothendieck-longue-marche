# LM_C3-264-282 — research notes checked against the corrected transcription

Scans 264–282 (ms. pp. 433–442, §48 I end and §48 II). Notes 1–43 are the first pass's notes (section 5 of
`answers\unzipped\LM_C3-264-282\LM_C3-264-282_notes.md`), each with a decision: keep, correct or drop. Notes S1–S9 are
new, written in the second pass. References to scans and equation numbers follow `LM_C3-264-282_checked.tex`.

## First-pass notes

1. **Scan 264 — claim.** *Correct.* "D est inversible ssi N(cρ+d) l'est" follows at once from (23) when ad−bc is a unit, and N_{A_ρ/A}(cρ+d) = det(cρ+d) = c²+cd+d² because Tr ρ = det ρ = 1. The claim is proved on the page; no further hypotheses are needed.
2. **Scan 264 — question ("est-ce que D peut être égal à 0 mod 3 ?").** *Keep.* G's own computation (ξ = (A 1; −1 0), ξρ = (−1 A+1; 0 −1), regular iff A ≠ −1) shows D ≡ 0 mod 3 does occur with ξρ regular, so he leaves the case open. The single excluded point A = −1 is ξ = −ρ⁻¹, the singular point of S5.
3. **Scan 264 — claim without proof, Pic(A_σ) = 0 "(sauf erreur)".** *Correct.* "(sauf erreur)" is now read without doubt; the value is written 0 over 1 (or 1 over 0). The claim is true: σ² = −1, so A_σ = Z[σ] ≅ Z[i], a principal ideal domain (S4).
4. **Scan 265 — claim.** *Correct.* (27) reads η = βσ(β)⁻¹ = [β,σ] with σ(β) = σβσ⁻¹ (S1). Passing from (28)–(29) and Pic = 0 to a solution β ∈ Gl(2,Z) is the Latimer–MacDuffee correspondence: ησ is regular with characteristic polynomial x²+1, Z² is an invertible Z[σ]-module, free since Pic = 0, so ησ is conjugate to σ; the page gives no proof.
5. **Scans 265–266 — implication, (31) and "le reste de U mod 4".** *Correct.* The ink of (31) is "(rt − su)U = t²+u²", but the computation (S2) gives (ru − st)U = t²+u², with ru − st = det β as in (23): the written factor is a slip. The mod-4 description of the obstruction is right for Z and Z₂ (S4).
6. **Scans 266–267 — claim, the Proposition.** *Keep.* The margin "(base quelc.)" is joined by a line to the "ssi" of scan 266, l. 1: the equivalence "U inv. ssi tσ+u inv." is asserted over any base, the residue statements only for Z, Z_ℓ, Ẑ.
7. **Scan 267 — implication, item 3 "automatique".** *Correct (answered).* For ℓ ≠ 3, 3 is a unit of Z_ℓ and Z_ℓ[ρ] is étale over Z_ℓ, so norms of units are onto and nothing is obstructed; likewise ℓ ≠ 2 for σ. Over Ẑ = ∏ Z_ℓ the obstruction sits at ℓ = 3 (resp. 2) only (S4).
8. **Scans 267–268 — expectation that μ is a section of G_m.** *Correct (proved later).* Scan 270 proves it under (42): (43) P(ξ)μ = c with c invertible forces P(ξ) and μ invertible, μ = c/P(ξ) (44), over any base, nilpotents included.
9. **Scan 268 — implication (reduced system vs. lifting α, β).** *Keep.*
10. **Scan 264 — first-pass own idea (enumerate modulo 3ⁿ).** *Keep*, low priority: S5 already locates the decisive point modulo 3.
11. **Scans 267–268 — first-pass own idea (treat the equations as functors).** *Keep* as a methodological remark; it adds nothing specific.
12. **Scan 269, NB — claim λ₀² = 1.** *Correct.* It is proved by one determinant: det(ε₁σ) = det(−λ₀ρ) gives 1 = λ₀² when det ρ = det σ = 1 (ε₁ unipotent). Over an integral A this gives λ₀ = ±1; in general λ₀ ∈ μ₂(A) (note 13).
13. **Scan 269 — first-pass own idea (μ₂ in characteristic 2).** *Keep.*
14. **Scan 270 — implication (c not a unit).** *Keep.*
15. **Scan 271, NB — claim of equivalence with (40 bis).** *Correct.* The sign is now settled: the ink reads "Q′(η) = c^te = λ′₀ Trσ − Trρ". Taking the constant term as for ξ (Tr(ηε₁(μ−1)ρ) − Trρ = P′(η)μ − Q′(η) at μ = 0) gives Q′(η) = Trρ − Tr ηε₁⁻¹ρ = Trρ + λ′₀Trσ = λ′₀c, once ε₁⁻¹ρ = −λ′₀σ, which (40 bis) gives with λ′₀ = 1/λ₀. So the written definition (sign, subscript 0 for 1) and the written value carry slips, while "c′ = λ′₀c" (scan 272) and "c inv. ⟺ c′ inv." are right.
16. **Scan 272 — first-pass own idea (symmetric treatment).** *Keep.*
17. **Scan 272, (47)–(49) — implication.** *Correct.* "N₁² = 1" is confirmed in the ink (a plain stroke) and is a slip for N₁² = 0: the same line says "de carré nul" and (48)–(50) use N₁² = 0. The "λ" before (1−μ) is overwritten by the parenthesis and has no role, since ε₁(1−μ) = 1 + (1−μ)N₁.
18. **Scan 273, Corollary — claim.** *Correct.* "de dim 1" is confirmed in the ink and is a slip for 2 (a trace level set in SG(𝓜), of relative dimension 3). "définit toujours un sous-schéma lisse" is too strong: the level set is singular where ξρ is scalar (S5); the open condition "P(ξ) inversible" removes those points, so the Corollary itself stands.
19. **Scan 273 — first-pass own idea (critical points have P(ξ) = 0).** *Keep*; confirmed by the example in S5.
20. **Scan 273 — implication (P(ξ) = D, P′(η) = U).** *Keep*; scan 274 carries it out: the solution scheme is that of the (D, B) with D invertible.
21. **Scan 274, (55) — claim.** *Keep.* The matrices (μ M; 0 1) = (1/D B/D; 0 1) normalise ε₀(λ) = (1 −λ; 0 1): they form the group B′₀ of scan 280, so (55) already shows the final answer of the section.
22. **Scan 274 — "T − S = 1" and "avec S inv."** *Correct.* Both are firm in the ink. From η = ξε₁(1−μ): S = B, U = D, T = C + (1−μ)D; with μD = 1 and C + D − B = 1 this gives T − S = 0 (cf. (29)) and U = D invertible. So both are slips (for "T − S = 0" and "U inv."), and the rewritten first letter of the second row of (54) must be C.
23. **Scan 275 — implication (the two characters χ, χ′).** *Keep.*
24. **Scan 275 — exact sequence and marginal warning.** *Correct (answered).* In the split model B̃₀* = {(p ℓ; 0 q) : q² = 1} and the kernel of det is {p = q = ±1} = μ₂·L₀, not L₀; the sequence 1 → L₀ → B̃₀* → G_m → 1 is therefore false, as the margin "C'est faux, cf plus bas" says. G reaches this on scan 279 (μ₂) and scan 280 ((71), q² = 1).
25. **Scan 275 — first-pass own idea (p/q = pq).** *Keep*; G carries it out on scan 280, (71).
26. **Scan 276 — expectation (64).** *Keep*; proved for u ∈ L₀ on scan 276 and reduced to the definition of B̃₁* on scans 277–278.
27. **Scan 276 — sign audit.** *Correct (done).* With ε₀(λ) = 1 + λN₀ (58), ε₀(−λ) = 1 − λN₀, so the annotation "1 + N₀λ" and "1 + (σN₀σ⁻¹)λ" carry a sign slip. The conclusion (65) σε₀(λ)σ⁻¹ = ε₁(λ) is still right, because σN₀σ⁻¹ = N₁, and [u,σ] = ε₀(λ)ε₁(−λ) follows.
28. **Scan 277 — implication.** *Keep.*
29. **Scan 278 — question "est-ce un isomorphisme ?"** *Keep*; answered on scans 279–281: the kernel of (66) is μ₂ (69), B̃₀/μ₂ ↪ X_{ρ,σ} (70), and B′₀ ↪ X_{ρ,σ} (76) is asserted to be an isomorphism.
30. **Scan 278 — first-pass own idea (T_ρ ∩ B̃₀ on scalar sections).** *Correct.* G himself finds T_ρ ∩ B̃₀* = μ₂ on scan 279; what remains of the note is that μ₂ is to be taken as a group scheme (non-reduced in characteristic 2).
31. **Scan 279, (68) — claim.** *Keep*, with a proof route: over a field, if 1, ρ, σ are linearly independent, the subalgebra they generate in M₂ has dimension ≥ 3 and its commutant is the scalars. Over S, the commutant is the kernel of x ↦ ([x,ρ],[x,σ]) on 𝓜; O_S·1 is a direct summand, and the induced map 𝓜/O_S → 𝓜² is injective on every fibre, hence locally split injective (Nakayama), so the commutant is O_S and T_σ ∩ T_ρ = G_m over any base.
32. **Scan 279, (69) — implication.** *Keep.*
33. **Scan 280, (70)–(71) — implication.** *Keep.*
34. **Scan 280 — "par un calcul immédiat".** *Correct (verified).* For u = (p ℓ; 0 q) and N₀ = (0 −1; 0 0), uN₀u⁻¹ = (p/q)N₀, so χ′(u) = p/q and χ(u) = pq, which gives (71).
35. **Scan 280, (72)–(74) — claim ("se décompose intrinsèquement").** *Keep*, with a route: locally, where 𝓜 = End(E), Im N₀ = Ker N₀ is a B₀-stable line L, and p(u), q(u) are the characters of u on L and on E/L; a global version should use the one-sided ideal N₀𝓜 or 𝓜N₀ instead of E.
36. **Scan 281 — claim (lisse even in characteristic 2; exact sequence).** *Correct (verified in the split model).* B′₀ = {(p ℓ; 0 1)} ≅ G_a ⋊ G_m is smooth of relative dimension 2 in every characteristic; det = p, and its kernel is the upper unipotent group L₀, so 1 → L₀ → B′₀ → G_m → 1 is exact (the star on L₀ stays doubtful in the ink). "Canonique" needs the intrinsic q of note 35.
37. **Scan 281 — claim ("en vertu des principes généraux … surjectif sur les pts à val. dans un corps alg clos").** *Keep*; S8 gives the principle presumably meant and the hypotheses it needs.
38. **Scan 281 — implication (the remark that starts from ε₁ and ρ).** *Keep.*
39. **Scan 282 — claim (scalar multiples).** *Correct.* The upper-left margin now reads "Je prends la constante qui intervient dans le cas qui nous intéresse le plus, où −σ⁻¹ = σ, de sorte que (40 bis) devient ε₁ = ρσ": the dropped constant is λ₀ = 1. F_ρ and F_σ are unchanged by scalars, but c = Tr N₁ρ scales with ρ, which is what note 42 uses.
40. **Scan 282 — claim (equivalent independence conditions).** *Keep.* Right multiplication by ρ⁻¹ (resp. σ⁻¹) is an automorphism of the module 𝓜 taking 1, ρ, N₁ρ to ρ⁻¹, 1, N₁; with ρ + σ = N₁ρ = −N₁σ this gives all the stated equivalences.
41. **Scan 282, (78 bis) — implication.** *Keep.* The identities follow from N₀ = ρ⁻¹N₁ρ (57) and σN₀σ⁻¹ = N₁ (scan 276): N₁ρ = ρN₀ and N₁σ = σN₀.
42. **Scan 282, lower-left margin — claim (normalisation).** *Correct.* γ₀ (or δ₀) = N₁ρ and Tr N₁ρ = c (main text), so the normalisation is c = 1. Replacing ρ by tρ with ε₁ fixed forces σ ↦ tσ (σ = −ε₁⁻¹ρ) and c ↦ tc, so when c is a unit exactly one t gives c = 1: this is the "normalise entièrement".
43. **Scan 282 — implication (the final Proposition, unfinished at "— on").** *Keep.*

## Second-pass notes (own)

S1. **Scans 265–266 — own note (notation).** The commutator is written [β,σ] = βσ(β)⁻¹ with σ(β) = σβσ⁻¹, the convention of the author's later table for §48 I ("α → αρ(α⁻¹) = [α,ρ]") and §48 III ("αρ(α⁻¹) = βσ(β)⁻¹ε₁(μ−1)"). With this reading the system of the Proposition is the pair of commutator equations; the first pass's alternative (βσ)⁻¹ would make it trivial. Confidence high.

S2. **Scan 265 — own idea (verification).** For β = (r s; t u) and δ = ru − st one finds η = βσβ⁻¹σ⁻¹ = δ⁻¹(r²+s², rt+su; rt+su, t²+u²). So η is symmetric ((29)) and of determinant 1 automatically, and δU = t²+u² = N(tσ+u): this corrects the factor "(rt − su)" written in (31). Confidence high.

S3. **Scan 266 — own note (claim check).** (16) is written "B + D − C = 1", but item 1) of the same Proposition displays ξρ = (−B A+B; −D C+D), whose trace is C + D − B; with Tr ρ = 1 the trace condition is C + D − B = 1, the form used in (54) on scan 274. (16) comes from an earlier page outside this package, so it is either a slip or another convention. Confidence medium.

S4. **Scans 264–267 — own idea (verification of the arithmetic).** A_ρ = Z[ρ] ≅ Z[ζ₆] (ρ² − ρ + 1 = 0) and A_σ ≅ Z[i] are principal, so Pic = 0. Norms of units satisfy c² + cd + d² ≡ (c − d)² ≡ 1 (mod 3) in the ramified Z₃[ρ] and t² + u² ≡ 1 (mod 4) in the ramified Z₂[σ], while for other ℓ the extension is unramified and the norm on units is onto. Hence Z_ℓ*/N(A*) = ±1 exactly at ℓ = 3 (resp. 2), detected by D mod 3 (resp. U mod 4), as items 2)–3) of the Proposition state. Confidence high.

S5. **Scans 264 and 273 — own idea (test case for "toujours lisse").** Over F₃, ξ = −ρ⁻¹ = (−1 1; −1 0) has det ξ = 1 and Tr(ξρ) = −2 = 1 = Tr ρ, while ρξ = −1 is scalar, so the differential of ξ ↦ Tr(ξρ) on SL₂ vanishes there and the level set is singular at that point. There D = P(ξ) = 0, so the open set "P(ξ) inversible" of the Corollary removes it; it is also exactly the point A = −1 where ξρ fails to be regular in G's mod-3 computation on scan 264. Confidence high.

S6. **Scan 269 — own note (supports an uncertain reading).** By (33), η = ξε₁(1−μ), so Tr ησ = Tr σ becomes Tr((ξε₁(1−μ) − 1)σ) = 0. This is exactly what the first pass reads, with doubt, in the overwritten third condition of (36) (σ moved out of the parenthesis, −1 inserted), and the second condition Tr(ξ − 1)ρ = 0 is likewise Tr ξρ = Tr ρ; the reworked formulas are therefore coherent. Confidence medium.

S7. **Scan 267 — own note (cross-reference).** The author's table titles §48 II (p. 434) "L'équation ξ = ηε₁(μ − 1) et le groupe B′₀ ⊂ B_{ρ,σ}" and starts III at p. 443, just after this package. The title names the outcome of scans 280–281, the "bon" group B′₀ (q = 1), not the first candidate B̃₀. Confidence high.

S8. **Scan 281 — own idea (the "principes généraux").** One route: a monomorphism locally of finite presentation between smooth S-schemes of the same relative dimension (here 2: B′₀ ≅ G_a ⋊ G_m, and X_{ρ,σ} by the Corollary of scan 273) is unramified, hence étale on fibres (an injective tangent map between spaces of equal dimension), hence flat by the fibrewise criterion (EGA IV 11.3.10) and étale; an étale monomorphism is an open immersion (EGA IV 17.9.1), so surjectivity on geometric points makes it an isomorphism. This uses the smoothness of X_{ρ,σ}, i.e. the open condition P(ξ) inversible (S5). Confidence medium.

S9. **Scan 274 — own note (link to the final group).** In the explicit case the identification (55) sends a solution to (1/D B/D; 0 1), and μ = 1/D is its determinant, which is the character det of B′₀; so the isomorphism B′₀ ≅ X_{ρ,σ} asserted on scan 281 can be checked directly here, with (66) u ↦ ([u,ρ], [u,σ], det u) restricted to q = 1. Confidence medium.
