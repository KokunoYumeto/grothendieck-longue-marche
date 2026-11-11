# LM_C3-378-396 — research notes, checked against the corrected transcription (scans 378–396)

Source: the first pass's research notes (answers/unzipped/LM_C3-378-396/LM_C3-378-396_notes.md, "Research notes",
1–51), each checked against LM_C3-378-396_checked.tex. Verdicts: keep, correct (text revised), drop. Notes marked
**Claude (second pass)** are new. Kinds: conjecture (Grothendieck's conjectures, questions, expectations, programme),
unproved claim, unpursued implication, own idea. "Unproved" means not proved in the cited passage.

Conventions used in the checks (from the ink): G = Gl(2)_S; in the arithmetic case ρ = (0 1; −1 1) and
σ = (0 −1; 1 0) (scan 379), so Tr ρ = 1, Tr σ = 0, det ρ = det σ = 1, ρ³ = −1, σ² = −1. G*_{ρ,σ} ⊂ B′₀ × T_ρ × N′_σ
acts on G by inner automorphisms through the factor B′₀ (scans 391–392); u̲(x) means u̲xu̲⁻¹. Elements of the
semidirect products are written i_B(b)i_ρ(y)i_σ(z)i_G(g), with i_B(b)i_G(g)i_B(b)⁻¹ = i_G(bgb⁻¹).

## Notes of the first pass

### Scans 378–382

- **N1 — scan 378, Proposition and proof — unproved claim — correct.** The proof is complete modulo two facts it uses
  without proof: the centralisers of ρ and σ in G are T_ρ and T_σ with T_ρ ∩ T_σ = G_m (the centre), and
  G_m ∩ SG = μ₂. Then the first two formulas of (29) fix u̲ modulo G_m and det u̲ = μ fixes it modulo μ₂. The
  characteristic-2 restriction belongs to the following remark, not to the Proposition. Revised: the target of λ is μ₂
  in the statement but an Ɛ₂ (ε₂?) at the end of the proof (change 2).
- **N2 — scan 378, normalisation remark — unproved claim — correct.** The "sauf erreur" step works on the neutral
  component: if T_ρ, T_σ are tori, B′₀ × T_ρ × T_σ is connected, and a morphism from it to μ₂ (étale when 2 is
  invertible, hence "du moins en car. ≠ 2") with λ(1) = 1 is constant, hence trivial. The remaining freedom is a
  character of the component group, which the corrected sentence names: "la multiplication de u̲ par ε (correspondant
  à l'hom. can. (non trivial) de N′_σ/T_σ sur μ₂)" (change 3). That λ is a homomorphism on all of G*_{ρ,σ} still
  needs this component argument.
- **N3 — scan 378, diagonal margin — unpursued implication — keep.** On SG_{ρ,σ} instead of G*_{ρ,σ} the
  indeterminacy becomes multiplication by ε^iε′^j (i, j ∈ Z/2Z), now read without doubt (change 4): two independent
  sign characters instead of one. Comparing the component groups of the two schemes would explain the difference; not
  done on these pages.
- **N4 — scan 379, first paragraph — unproved claim — keep.** "nous pourrions faire leur construction aussi sans
  cette condition supplémentaire" (Tr σ = 0, i.e. working with G_{ρ,σ} instead of G*_{ρ,σ}) is asserted, not shown.
- **N5 — scan 379, normalisation Tr(ρ+σ) = 1 — unproved claim — correct.** The arithmetic pair of display (2) already
  satisfies both conditions: Tr σ = 0 and Tr(ρ+σ) = 1 + 0 = 1. The general "Nous pouvons au besoin supposer" (by which
  change of ρ, σ?) is not justified here; the conditions referred to are on p. 477′/478′ and in §48.V (pp. 455–457).
- **N6 — scan 379, display (2) — unpursued implication — correct.** Since ρ³ = −1 and σ² = −1, the images of ρ, σ in
  Gl(2,Ẑ)/{±1} have orders 3 and 2, matching the order-3 action ρ̇ on {0,1,∞} used on scan 381. The map (2) is only
  named "homomorphisme canonique"; its construction is not on these pages.
- **N7 — scan 380, opening — unproved claim — keep.** The promised compatibility of the new group law with "ledit
  morphisme" is a programme for the following pages (done for S₀M̃^!₀,₃ on scans 384–390).
- **N8 — scan 380, (3)–(4) — unproved claim — correct.** The corrected reading (change 7) is "déduite d'une extension
  de Ã₀,₃ = M̃₀,₃/Π̂₀,₃ ⊂ 𝒯̂₀,₃, et même d'une extension de 𝒯̂₀,₃ (via M̃₀,₃ → 𝒯̂₀,₃)": the extension is defined over
  𝒯̂₀,₃ and pulled back, and (3) indeed takes u ∈ 𝒯̂₀,₃. Still to prove: conjugators exist for every u (surjectivity)
  and the kernel is the product of the centralisers L_i ≅ Ẑ.
- **N9 — scan 380, (5) — unpursued implication — keep.** The product is stated only "en nous bornant (dégonflage!)"
  to u̇ = 1; for general u̇ the components would be permuted.
- **N10 — scan 381, (6)–(7) — unproved claim — correct.** For u = 1 (μ = 1), (4) reads ℓ_i = int(f_i⁻¹)(ℓ_i), so
  f_i centralises ℓ_i and the kernel is ∏ Z(ℓ_i). "f_i ∈ L_i" then uses that the centraliser of ℓ_i in Π̂₀,₃ is the
  procyclic L_i ≅ Ẑ, a known property of free profinite groups that is not proved here.
- **N11 — scan 381, (9)–(11) — unpursued implication — correct.** The identity under the brace follows by cubing (9):
  uρ³u⁻¹ = (gρ)³ = gρ(g)ρ²(g)ρ³, so gρ(g)ρ²(g) = 1 as soon as ρ³ = 1 as an automorphism of Π̂₀,₃ (ρ̇ of order 3);
  then f_i⁻¹ = ρ³(f_i⁻¹) closes the recurrence. In the ink the underline labelled 1 starts under ρ(g) (still
  unresolved), but the identity needs the first factor g.
- **N12 — scan 382, (11)–(12) — unproved claim — keep.** Closure of the quadruples satisfying (11) and the
  identification with the pairs (u, f₀) are asserted; (11) itself shows that f₀ determines f₁, f∞.
- **N13 — scan 382, (13)–(15) — unproved claim — keep.** The connectors of (14) are headless strokes (change 9);
  nothing mathematical changes.
- **N14 — scan 382, (15) — own idea (first pass) — keep.** Comparing the three-factor extension modulo the diagonal Ẑ
  with the finer one remains a reasonable check.

### Scans 383–387

- **N15 — scan 383, (16)–(18) — unproved claim — keep.** The parametrisation by (α, β, f) is imported from §46.V
  (p. 407 ff, which the Circle table confirms as "Récapitulation en termes de M̃!₀,₃[0]").
- **N16 — scan 383, after (17) — unproved claim — correct.** The text says μ is determined by α "et m̄ par la seule
  connaissance de ξ = α̲ρ(α̲)⁻¹". This cannot come from u̲(ρ) = ξ̲ρ alone, since u̲ is fixed only modulo T_ρ, whose
  determinants are arbitrary; it must come from (17), where the factor ε₁(μ−1) = ℓ₁^ν carries μ. Not proved here;
  scan 384 repeats it ("μ = μ(ξ) est déterminé par ξ").
- **N17 — scan 383, (18) — own idea (first pass) — keep.**
- **N18 — scan 384, (23)–(24) — unpursued implication — correct.** The stated sign-independence checks out: ρ and σ
  act by conjugation, so replacing α̲ by −α̲ (or β̲ by −β̲) leaves α̲ρ(α̲)⁻¹ (or β̲σ(β̲)⁻¹) unchanged, and (24) is
  well defined for lifts "déterminés au signe près". The relation is imposed in Sl(2,Ẑ), "pas dans Sl(2,Ẑ)′" (Gl/Sl
  as in the ink, change 13).
- **N19 — scan 384, (21)–(22) — own idea (first pass) — correct (settled).** The prose before (22) ("l'élément
  (u_{α,β,f}, f)") agrees with (21) and with scan 388, where the triple (1,1,f) corresponds to the pair
  (int(f⁻¹), f) = (u_{1,1,f}, f). So (22)'s (u_{α,β}, f) is a slip of the pen; the transcription keeps it.
- **N20 — scan 385, opening–(28) — unproved claim — keep.** The re-verification is completed on scan 386 for the α
  and β components; the μ, ε components follow from μ″ = μμ′ if ε₂ is a character, as "d'où ε₂″ = ε₂ε₂′" assumes.
- **N21 — scan 385, (27) — unproved claim — keep.** "(cf …)" is left blank in the ink.
- **N22 — scan 385, (25)–(28) — own idea (first pass) — keep.**
- **N23 — scan 386, before (29) — unproved claim — correct.** Corrected reading (change 17): "dans les conditions
  générales de V (ou même de III, si on s'intéresse à G_{ρ,σ}, au lieu de G*_{ρ,σ})", i.e. the verification is
  claimed even under the weaker hypotheses of III. Since (30) uses only the group structure of the decomposition (29),
  the claim reduces to the existence of that decomposition over the base, which is not shown here.
- **N24 — scan 386, after (30) — unproved claim — correct (checked).** The omitted computation is literally parallel:
  u̲′(β̲)β̲′ = u̲′u̲b̲⁻¹u̲′⁻¹·u̲′b̲′⁻¹ = (u̲′u̲)(b̲′b̲)⁻¹. So "et de m̄ pour la deuxième relation 30" holds; only
  associativity is used.
- **N25 — scan 386, (29)–(30) — own idea (first pass) — keep.**
- **N26 — scan 387, (31) and the bracket — unproved claim — keep.** The reading is now "par multiplication, [pour,
  struck] (α,β,μ,ε), de α et β chacun par une section de G_m" (change 20). The conditions α, β ∈ Γ{±1}→ΓG_m stay
  overwritten.
- **N27 — scan 387, Σ₀ — unpursued implication — keep.**
- **N28 — scan 387, own idea (first pass) — keep.**

### Scans 388–392

- **N29 — scan 388, (31) — unproved claim — keep.** The number (31) is used twice (scans 387 and 388), as in the ink.
- **N30 — scan 388, (32) — own idea (first pass) — correct (settled; consequential).** With the product (5) on pairs,
  (u′,f′)(u,f) = (u′u, f′u′(f)), one gets (int(f′), f′⁻¹)(int(f), f⁻¹) = (int(f′f), (f′f)⁻¹). So f ↦ (int(f), f⁻¹) is
  a homomorphism Π̂₀,₃ → S₀M̃^!₀,₃, and by (21) (int(f), f⁻¹) is the pair of the triple (1,1,f⁻¹), as (32) says. The
  written pair (int(f), f) is not in the subgroup {(int(h⁻¹), h)} unless f² = 1, so the missing −1 is Grothendieck's
  slip; the prose's f ↦ (int(f⁻¹), f) is an anti-homomorphism, which is why the inverse appears.
- **N31 — scan 388, (33) — unpursued implication — correct (checked).** For (u,f) = (1, ℓ₀ⁿ), (12) holds (ℓ₀ commutes
  with ℓ₀ⁿ, μ = 1), and (21) gives u_{α,β,f} = int(ℓ₀⁻ⁿ)int(ℓ₀ⁿ) = 1 with α = β = ℓ₀ⁿ, as written. The subgroup is the
  kernel of S₀M̃^!₀,₃ → M̃^!₀,₃ in (13), hence "invariant"; centrality is not claimed. The ambient group is now read
  Aut_lac (change 22).
- **N32 — scan 389, (34)–(36) — unpursued implication — correct (checked).** (34) agrees with (5) and (21):
  f″ = f′·u′(f) with u′ = int(f′⁻¹)u_{α′,β′} gives f″ = u_{α′,β′}(f)f′, and the display at the top of the page gives
  the same f″⁻¹ = f′⁻¹u_{α′,β′}(f⁻¹). The warning "Attention au passage de f à f⁻¹ !" concerns (36), where
  U·f ↦ (U, f⁻¹) turns this law into the semidirect product (35).
- **N33 — scan 389, own idea (first pass) — keep.**
- **N34 — scan 390, (37)–(38) — unpursued implication — correct.** Σ₀ is no longer called "impuissant" (the word is
  struck, change 25). Σ̃ = Σ₀ × {±1} is invariant as stated: Σ₀ acts trivially on G (its elements have u̲ = 1,
  scan 387), and −1 ∈ Sl(2,Ẑ) is central and fixed by inner automorphisms. Σ̃ is moreover central if Σ₀ is central in
  SG*_{ρ,σ}(Ẑ).
- **N35 — scan 390, (39)–(40) — unproved claim — correct (checked).** In the semidirect product,
  i_G(λ⁻¹)i_B(λ′) = i_B(λ′)i_G(λ′⁻¹λ⁻¹λ′), hence i(λ)i(λ′) = i_B(λλ′)i_G((λλ′)⁻¹) = i(λλ′) for any λ, λ′ ∈ B′₀;
  so (40) is a homomorphism, injective by its B′₀-component. Distinguishedness is checked on scans 391–392 (N37).
- **N36 — scan 390, own idea (first pass) — keep.**
- **N37 — scan 391, (40)–(42) — unproved claim — correct (checked).** The four verifications on scan 392 are right:
  i_B(x)i(λ)i_B(x)⁻¹ = i(xλx⁻¹) needs only that L₀ is normal in B′₀; i(λ) centralises i_G(G) because i_B(λ) acts on G
  as int(λ); i_ρ, i_σ commute with both factors (N39). So i(L₀) is distinguished in G*_{ρ,σ}·G.
- **N38 — scan 391, own idea (first pass) — keep.** The cancelled block (U = (u̲, a̲, b̲, ε f) = U₀·f, with a marginal
  "où U₀", change 28) begins the direct conjugation that N41 below makes general.
- **N39 — scan 392 — unproved claim — correct (settled).** "Pour les deux premiers, c'est trivial": G*_{ρ,σ} acts on G
  only through B′₀ ("via le facteur B′₀", top of the page) and B′₀ × T_ρ × N′_σ is a direct product, so i_ρ(x),
  i_σ(x) commute with i_B(λ) and with i_G(G), hence with i(λ).
- **N40 — scan 392 — unpursued implication — keep.**
- **N41 — scan 392, own idea (first pass) — correct (settled).** The general fact: if H acts on G through a
  homomorphism φ: H → G by inner automorphisms, then k(h) = i_H(h)i_G(φ(h)⁻¹) is a homomorphism H → H⋉G whose image
  centralises i_G(G), and (h,g) ↦ k(h)i_G(g) is an isomorphism H × G ≅ H⋉G. Here i(λ) = k(λ) for λ ∈ L₀ ⊂ B′₀, and
  k(L₀) is distinguished exactly when L₀ is normal in H.

### Scans 393–396

- **N42 — scan 393, dimensions — unproved claim — correct (checked).** The counts are coherent if B′₀ (dim 2) is
  T₀·L₀, with T₀ ≅ G_m by det (scan 396: "N′_σ →det G_m ←det,≃ T₀ ↪ G") and L₀ ≅ G_a. Then S̃M = G*·G has 6 + 4 = 10;
  SG*_{ρ,σ}, cut out of G* by the two conditions (20) of p. 487′, has dim 4, so SM has 4 + 3 = 7; the quotients by
  i(L₀) have 9 and 6. Flatness ("groupe plat") is asserted, not proved.
- **N43 — scan 393, (44) — unproved claim — correct (consequential).** With the struck S (change 29), the first line
  of (44) describes M_{ρ,σ} = SM_{ρ,σ}/i(L₀) ≃ SG*(0)·SG (dim 3 + 3 = 6), and the second M̃_{ρ,σ} ≃ G*(0)·G with
  G*(0) ≅ T₀ × T_ρ × N′_σ (dim 5 + 4 = 9), matching the dimensions above. "Le passage au quotient ne fait pas de
  difficultés" is the unproved step: it amounts to G* = G*(0)·i_B(L₀) with G*(0) ∩ i_B(L₀) = 1, so that G*(0)·G maps
  isomorphically onto the quotient.
- **N44 — scan 394, (45) — unpursued implication — keep.** The decomposition under (45) has T_σ(Ẑ) where (44) and (1)
  of scan 396 have N′_σ; the text does not explain the change.
- **N45 — scan 394, remark and (46) — unpursued implication — keep.**
- **N46 — scan 394, (47) — own idea (first pass) — correct (settled).** As written, (47) has M̃^!₀,₃ on both sides (no
  "(0)", confirmed on a crop) and ends with a separate mark read "!" or ":" (change 33). The intended decomposition is
  presumably that of (31) on scan 388, S₀M̃^!₀,₃ ≃ M̃^!₀,₃[0]·Π̂₀,₃. In M̃^!₀,₃ itself, M̃^!₀,₃ = M̃^!₀,₃(0)·int(Π̂₀,₃)
  holds (by (12) every u is int(f⁻¹) times a normaliser of L₀) but is not semidirect, since the intersection contains
  int(L₀).
- **N47 — scan 395, (48)–(49) — unproved claim — keep.**
- **N48 — scan 395, own idea (first pass) — keep.**
- **N49 — scan 396, (1)–(3) — unpursued implication — keep.** The section title in the ink is "Étude du groupe
  M_{ρ,σ} et de M_{ρ,σ} → Gl(2)"; the author's later table calls §48.X "Structure de Mρ,σ".
- **N50 — scan 396, last paragraph — unproved claim — correct (checked).** Θ is a homomorphism:
  (i_B(x)i_G(f))(i_B(x′)i_G(f′)) = i_B(xx′)i_G(x′⁻¹fx′f′) ↦ xx′x′⁻¹fx′f′ = (xf)(x′f′), the factors i_ρ, i_σ being
  ignored by Θ; and Θ(i(λ)) = λλ⁻¹ = 1. So Θ descends to M̃_{ρ,σ} once the quotient exists (N43).
- **N51 — scan 396, (2) — own idea (first pass) — correct (settled).** Θ(i_G(f)) = f, so i_G is a section of Θ, and
  by N41 the kernel {i_B(x)i_ρ(y)i_σ(z)i_G(x⁻¹)} ≅ T₀ × T_ρ × N′_σ centralises i_G(G): M̃_{ρ,σ} ≅ (T₀ × T_ρ × N′_σ) × G,
  with Θ the projection onto G. The same untwisting applies to (T_ρ × N′_σ)·G of scan 396, whose action is inner
  through N′_σ →det G_m ≅ T₀ ⊂ G; it does not apply to M_{ρ,σ} = SG*·SG itself, since T₀ acts on SG by automorphisms
  that are not inner in SG.

## New notes — Claude (second pass)

- **C1 — scan 379, margin — conjecture (programme) — Claude (second pass).** The note announces "Par la suite,
  l'« officialisation » … des schémas(?) en groupes S₀M_{ρ,σ}, cf p. 559 ff": a later, official definition of
  S₀M_{ρ,σ} as a group scheme, which the Circle table places in §49.II ("Les groupes Mρ,σ etc. « sans signes »",
  p. 553). On these pages S₀ appears only on the arithmetic side (S₀M̃^!₀,₃) and, struck or doubtful, in (39) and (45).
  Confidence: medium.
- **C2 — scan 381, (8) — own idea (editorial) — Claude (second pass).** (8) writes S₀M̃₀,₃ ⊂ M̃₀,₃ (no S on the right,
  confirmed on a crop), while the text builds S₀M̃^!₀,₃ as a subgroup of SM̃^!₀,₃ (scan 382) and (14) maps it to
  SM̃^!₀,₃. The inclusion as written is a slip for ⊂ SM̃₀,₃; the transcription keeps the ink. Confidence: medium.
- **C3 — scan 383, (17) — own idea — Claude (second pass).** The condition "si μ − 1 = 2ν" in the label is
  automatic: for μ ∈ Ẑ*, μ is a unit in Z₂ and 2 is invertible in Z_p for odd p, so μ − 1 ∈ 2Ẑ, and ν = (μ − 1)/2 is
  unique because Ẑ has no 2-torsion. So the label ε₁(μ−1) = ℓ₁^ν applies to every μ. Confidence: high.
- **C4 — scan 386, (29) — own idea (editorial) — Claude (second pass).** The membership conditions to the right of (29)
  read α̲, α̲′ ∈ T_ρ(Ẑ) and β̲, β̲′ ∈ N′_σ(Ẑ) (the Greek letters are clear on a 2.4× crop), but (30) uses the factors
  a̲, a̲′ ∈ T_ρ(Ẑ) and b̲, b̲′ ∈ N′_σ(Ẑ) of the decomposition G*_{ρ,σ} ⊂ B′₀ × T_ρ × N′_σ. The Greek letters are slips
  for a̲, b̲; the transcription keeps them. Confidence: high.
- **C5 — scan 390, (37)–(38) — unpursued implication — Claude (second pass).** Whether (37) lifts from
  SM_{ρ,σ}(Ẑ)/Σ̃ to SM_{ρ,σ}(Ẑ) is measured by pulling back 1 → Σ̃ → SM_{ρ,σ}(Ẑ) → SM_{ρ,σ}(Ẑ)/Σ̃ → 1 along (37): a
  class in H²(S₀M̃^!₀,₃, (Z/2Z)³) when Σ̃ is central (N34). The text passes to the quotient instead; the Circle table's
  §49.IV ("Où on se bat avec « les signes » … dans la relation des lacets", p. 568) returns to the signs.
  Confidence: medium.
