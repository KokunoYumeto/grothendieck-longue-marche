# LM_C3-321-339 — research notes, checked against the corrected transcription (scans 321–339)

Source: the first pass's research notes (answers/unzipped/LM_C3-321-339/LM_C3-321-339_notes.md, §5: 12 + 13 + 8 + 11
= 44 notes, numbered N1–N44 here in their order), each checked against LM_C3-321-339_checked.tex. Verdicts: keep,
correct (text revised), drop. Notes marked **Claude (second pass)** are new. Kinds: conjecture (Grothendieck's
conjectures, questions, expectations, programme), unproved claim, unpursued implication, own idea. "Unproved" means not
proved in the cited passage.

Conventions used in the checks: the normal form (5)/(45) ρ = (0 1; v w), σ = (0 −1; v' w'), v + v' = 0, w + w' = 1,
v invertible; the standard triple (57) ρ₀ = (0 1; −1 1), σ₀ = (0 −1; 1 0), ε₀ = (1 −1; 0 1); N = ρ + σ. Every identity
stated below was verified by hand on these matrices.

## Notes of the first pass

### Scans 321–326

- **N1 — scan 321, Remarque after (39) — unpursued implication — correct.** The page itself names what β alone loses:
  the "signe" ε, with μ = 1/U = ε/U₀ in (41)–(42). Scan 322 adds that U₀ invertible is necessary and depends only on
  β, and that then every ε ∈ Γμ₂ occurs, α being found locally up to α ↦ αb, b ∈ ΓT_ρ. What remains unpursued is a
  description of the β for which U₀ is invertible.
- **N2 — scan 322 — unproved claim — keep.** "ζ pourra bel et bien s'écrire loc.t sous la forme αρ(α)⁻¹" rests on the
  theory of (II) and on the lemma p. 455 (the solutions of det η = 1, Tr ησ = Tr σ form the ss-schéma A_σ); neither
  is proved again here.
- **N3 — scan 322 — own idea (first pass) — keep.** The infinitesimal part of μ₂ in characteristic 2 is not a
  formality on these pages: it is exactly what makes (60) fail (C3).
- **N4 — scan 323, (1)–(5) — unproved claim — correct.** "Il existe un épinglage unique*" is qualified by the author's
  own NB*, now read "L'unicité de v,w (i.e. de ρ₀,σ₀) n'est pas vraie sans quelques restrictions sur S, il suffit que
  tte section τ de O_S telle que 2τ=0, τ²=0 soit nulle". Existence is not proved on the page, and uniqueness does fail
  without the restriction (C2, C3).
- **N5 — scan 323, first NB — unproved claim — correct.** Corrected reading: "Si ε₀, ε₁ sont les relèvements
  canoniques de ε̃₀, ε̃₁ dans G, réguliers, avec σ̃(ε₀)=ρ̃(ε₀)=ε₁, on peut relever ρ̃,σ̃ de façon unique en ρ,σ" with
  −σ⁻¹ρ = ε₀ and (ρ+σ)² = ρ+σ. Once ε₀ is fixed the uniqueness is immediate (lifts λρ, μσ need λ = μ by the first
  relation and λ = 1 by idempotency); but a unipotent lift λε₀ of ε̃₀ needs only λ² = 1 and 2λ = 2, so the
  "canonical" lift is unique only where there is no τ ≠ 0 with 2τ = τ² = 0 (checked by Claude).
- **N6 — scan 323, NB* — unproved claim — correct.** The reading is "n'est pas vraie sans quelques restrictions sur
  S" (not "demande …", with "n'est pas vraie" struck), and the conditions 2τ = 0, τ² = 0 are now secure. The page
  gives neither a counterexample nor a proof that the condition suffices; C2 gives the counterexample and C3 shows
  that the same condition is exactly what (60) needs.
- **N7 — scan 323, NB* — own idea (first pass) — correct.** The proposed test has been carried out: the coefficients
  (v, w) are not unique over F₄[τ]/(τ²) (C2), and the épinglage is not unique over F₂[τ]/(τ²) (C3).
- **N8 — scan 324, (9)–(10) — unpursued implication — keep.**
- **N9 — scan 325, (13)–(15) — unproved claim — keep.** The equivalence of (12) with the épimorphisme N'_σ → μ₂ is
  stated without proof.
- **N10 — scan 325, (17)–(18) — unproved claim — correct.** The connective now reads "donc si les car. rés. sont ≠ 2
  i.e. 2 inv": the page passes from "2 régulier" (sections of N_σ over S lie in N'_σ) to the equality of group schemes
  (18) when 2 is invertible. The doubt about the reading is settled; the point of keeping the two hypotheses apart
  stands (the first gives b = 0 from 2b = 0 in gσg⁻¹ = aσ + b, the second makes this hold after every base change).
- **N11 — scan 326, paragraph before 3° — conjecture (programme) — keep.** The wording is "On va se tourner vers des
  conditions qui doivent|vont servir à fixer v (ou encore v') de façon explicite".
- **N12 — scan 326, (20) — unproved claim — keep.** Immediate from (11) (det σ = det ρ = −v) and (6)
  (ε₀ = (1 1/v; 0 1)).

### Scans 327–332

- **N13 — scan 327, Dém. — unpursued implication — keep.**
- **N14 — scan 327, left margin — unproved claim (deferred) — keep.** The upper right margin, now read "cf cor. 2 plus
  bas", in addition refers the boxed ρ² − ρ + 1 = … to Corollaire 2 on scan 331 (C5).
- **N15 — scan 328, "sauf la dernière (27)", "Essayons de prouver" — conjecture (exploratory proof) — keep.**
- **N16 — scan 328, final matrix — own idea (first pass) — correct.** Done: ρ²σ = (−vw, w−(v+w²); −v(v+w²),
  −w(w²+2v)+v+w²), and ρ²σ = ε₀⁻¹ = (1 −1/v; 0 1) holds iff v = −w² and w³ = 1, which is (27bis) on scan 329. The
  ink's lower right entry "+v−w²" (kept as \unsure) cannot give the w³ that the author writes on the next page;
  "+v+w²" does.
- **N17 — scan 329, lemma (30)–(32) — unpursued implication — keep.**
- **N18 — scan 329, lemma — own idea (first pass) — keep.**
- **N19 — scan 330, struck "ρ+1 est inversible" — own idea (first pass) — keep.** det(ρ₀ + 1) = 3, so ρ₀ + 1 is not
  invertible at the fibre p = 3 of Spec Z although ρ₀ is nowhere scalar; this agrees with the marginal "faux".
- **N20 — scan 330, Corollaire 1 — unproved claim — keep.** Verified inside the normal form: det = Tr = 1 gives
  ρ²−ρ+1 = 0 and so ρ³ = −1; ρ³ = −1 with det ρ = 1 gives v = −1, w² = 1, w³ = 1, hence w = 1; ρ³ = −1 with
  Tr ρ = 1 gives v = −w² = −1. For arbitrary matrices it fails (ρ = −1).
- **N21 — scan 331, after (37) — unproved claim — keep.**
- **N22 — scan 331, (38)–(40) — own idea (first pass) — correct.** For ρ₀, ρ₀² + ρ₀ + 1 = 2ρ₀ ≠ 0, so (40) as written
  does not hold under the page's normalisation. The "+" of (40) is in darker ink, and so is a "+" written over a
  pencil "−" in the boxed (56) on scan 334; see C5.
- **N23 — scan 332, (41)–(44) — unproved claim — correct.** "De façon canonique" needs the NB* restriction: over a
  base with τ ≠ 0, 2τ = τ² = 0, (ρ₀, σ₀) and (ρ₀, (1+τ)σ₀) both satisfy (44) above the same σ̃₀, ρ̃₀ (C3).
- **N24 — scan 332, (45)–(47) — unproved claim — correct.** The "unique triplet (φ, ρ₀, σ₀)" fails over such bases
  (C2 for ρ₀, σ₀; C3 for φ).
- **N25 — scan 332, normal form from kernels and images — own idea (first pass) — keep.**

### Scans 333–335

- **N26 — scan 333, Théorème d'épinglage modulaire — unpursued implication — keep.** The cancelled heading on scan 332
  already reads "Théorème d'épinglage modulaire".
- **N27 — scan 333, (49)–(51) — own idea (first pass) — correct.** Over Spec Z the sheaf of projective modular triples
  is not the sheaf of trivializations: by C3 the map from Isom(GP(1), PG) is not injective on F₂[τ]/(τ²)-points. Over
  bases without τ ≠ 0, 2τ = τ² = 0 the question remains as stated.
- **N28 — scan 334, (56) — unproved claim — keep.** The boxed sign is a dark "+" over a pencil "−" (C5).
- **N29 — scan 334, (57) — unproved claim — correct.** Verified (Claude) over Z: −σ₀⁻¹ρ₀ = (1 −1; 0 1) = ε₀,
  ρ₀ + σ₀ = diag(0,1) is idempotent, N₀ = (0 −1; 0 0), N₁ = ρ₀N₀ρ₀⁻¹ = (0 0; 1 0), σ₀² = −1 and
  Tr ρ₀ = det ρ₀ = 1. So (52)–(56) hold, and N₀, N₁ are non-homothetic in every fibre.
- **N30 — scan 335, "Toutes les flèches de (58) sont bijections" — unproved claim — correct.** False without the NB*
  restriction: over F₂[τ]/(τ²) the lower horizontal arrow and the right vertical arrow of (58) are not injective (C3).
- **N31 — scan 335, (59) — unpursued implication — correct.** (59) holds over any base (Claude): a g commuting with
  ρ₀ and σ₀ commutes with N = diag(0,1), so it is diagonal, and commuting with σ₀ makes it scalar.
- **N32 — scan 335, (60) — unproved claim — correct.** False in general; it holds exactly when S has no section
  τ ≠ 0 with 2τ = τ² = 0, the condition of the NB* on scan 323 (C3).
- **N33 — scan 335, dual numbers — own idea (first pass) — correct.** Done: (60) fails on F₂[τ]/(τ²) and holds on
  F₃[τ]/(τ²), indeed wherever 2 is a non-zero-divisor (C3).

### Scans 336–339

- **N34 — scan 336, Rmq and (62)–(63) (R336.1) — conjecture — keep.** "Il est plausible" and "cela vaudrait bien la
  peine de tirer cette question au clair" make it a question; the inserted "seule" makes the claim "la seule relation
  (R)". See C7.
- **N35 — scan 336, margin of (61) (R336.2) — unproved claim — correct.** Verified: for N'_σ, det(εσ) = det σ gives
  ε² = 1; for N'_ρ, Tr(ερ) = Tr ρ = 1 even gives ε = 1 in the normalised situation (56).
- **N36 — scan 336 (R336.3) — own idea (first pass) — keep.**
- **N37 — scan 337, Rmq (R337.1) — conjecture — keep.** The doubt "l'ens.|l'une des trois conditions" remains in the
  transcription.
- **N38 — scan 337–338, N ≠ 0 and N ≠ 1 (R337.2) — unpursued implication — keep.**
- **N39 — scan 337 (R337.3) — own idea (first pass) — drop.** The page itself excludes N = 0 and N = 1 in every fibre
  (scans 337–338), which is the scalar case for the idempotent N; (64) has no solution with ρ, σ scalar over any
  non-zero ring.
- **N40 — scan 338, "(sauf erreur)" (R338.1) — unproved claim — keep.**
- **N41 — scan 338, (69) (R338.2) — conjecture (question) — correct.** "Il faudrait voir si oui ou non elle résulte
  des autres relations" is answered yes on scan 339 within the parametrisation (70) ((73) gives Tr ρσ = 2 in (74)), and
  in general by C4.
- **N42 — scan 338 (R338.3) — own idea (first pass) — correct.** Done in C4: no parametrisation is needed.
- **N43 — scan 339, (70bis)–(74) (R339.1) — unpursued implication — keep.** The parametrisation ρ = ρ₀,
  σ = uσ₀u⁻¹ with u ∈ ΓSl(2) needs local conjugacy and a square root of det u, i.e. it is fppf-local; C4 avoids it.
- **N44 — scan 339 (R339.2) — own idea (first pass) — correct.** Done in C4.

## Claude (second pass)

- **C1 — scan 321, (39) — own idea (editorial check).** (37) on scan 320 gives (−δv)D = −vd²+cd+c² = det(dρ+c), so
  1/D = −v(ad−bc)/(−vd²+cd+c²) and, with (38), B/D = (ac+bc−vbd)/(−vd²+cd+c²). The ink of (39) has d² for the last
  term of both denominators and a leading minus before ac in the second numerator; both are kept as written.
  Confidence: high for the computation, medium for the readings.
- **C2 — scan 323, NB* — own idea (counterexample).** Take R = F₄[τ]/(τ²), w ∈ F₄∖F₂ (so w² + w = 1) and v = 1. The
  normal forms for (v, w+τ) are carried by g = 1 + τ(1 1; 1 0) (det 1+τ) to (1+(w+1)τ)ρ and (1+wτ)σ, where ρ, σ are
  the normal forms for (v, w). So two épinglages give the same ρ̃, σ̃ with w ≠ w + τ: uniqueness of v, w fails on a
  base with τ ≠ 0, 2τ = τ² = 0, as the NB* says. Confidence: high (checked entry by entry).
- **C3 — scans 335 and 323, (60), (58), NB* — own idea (counterexample and criterion).** If τ ∈ Γ(S,O_S) satisfies
  2τ = τ² = 0, then g = 1 + τρ₀ = (1 τ; −τ 1+τ) commutes with ρ₀ and gσ₀g⁻¹ = (1+τ)σ₀, so g ∈ N'_ρ ∩ N'_σ and g is
  not scalar if τ ≠ 0. Conversely every g in N'_ρ ∩ N'_σ has ε = 1 (Tr ρ₀ = 1) and ε' = 1+τ with 2τ = τ² = 0
  (σ₀² = −1, and ρ₀ + ε'σ₀ = gNg⁻¹ is idempotent), and then g = a(1 + τρ₀); so (60) holds exactly when S has no such
  τ ≠ 0. On F₂[τ]/(τ²), int(g) is a non-trivial automorphism of GP(1) fixing (ρ̃₀, σ̃₀, ε̃₀), and (ρ₀, (1+τ)σ₀,
  (1+τ)ε₀) is a second modular triple over the same projective triple, so two arrows of (58) are not injective.
  Confidence: high.
- **C4 — scans 338–339, (64)–(69) — own idea (proof).** With N = ρ + σ, σ² = −1 and N² = N one has
  ρ² − ρ + 1 = (N−σ)² − (N−σ) + 1 = σ − Nσ − σN, so (64) amounts to σ = Nσ + σN. Multiplying on the left by N gives
  NσN = 0, hence Tr σN = Tr NσN = 0, i.e. Tr σρ = 2, which is (69), over any commutative ring. This answers "il
  faudrait voir si oui ou non elle résulte des autres relations" without the parametrisation (70)–(74). Confidence: high.
- **C5 — scans 327, 331, 334 — unpursued implication (editorial).** ρ² − ρ + 1 = 0 is written with "−" in (36), (38),
  (39), (64) and in the struck block of scan 330, while (40) has "ρ² + ρ + 1 = 0" with the "+" in darker ink and the
  boxed condition of (56) has a dark "+" over a pencil "−"; the corner margin of scan 327 refers "ρ² − ρ + 1 = …" to
  "cor. 2". Under the page's normalisation the "+" forms are false (ρ₀² + ρ₀ + 1 = 2ρ₀). Whether the dark signs belong
  to a later change of convention (ρ ↦ −ρ turns ρ³ = −1 into ρ³ = 1 and ρ² − ρ + 1 into ρ² + ρ + 1) is to be checked
  on the following pages. Confidence: medium.
- **C6 — scan 323 — own idea (editorial).** Two slips are kept as written: "inéquivalente à ε̃₀", where the sentence
  compares ε̃₀ with ε̃₁ (cf. (41) 2° and (51)), and "Algèbre d'Azumaya M de rang 1", where the glyph is his 1 but scan
  333 has "rg. 4", the rank of M₂. Confidence: medium.
- **C7 — scan 336, (62)–(63) — own idea.** On ℤ-points the subgroup generated by σ̃₀, ρ̃₀ and ε̃₀(ℤ) is
  PSL₂(ℤ) ≅ ℤ/2 * ℤ/3, of index 2 in PGL₂(ℤ), so "engendré" can only hold for the fppf sheaf. For instance diag(1, −1)
  becomes diag(i, −i), a product of elementary matrices in SL₂(ℤ[i]), after the fppf extension ℤ → ℤ[i]. The relations
  (62) and (63) do hold for the standard matrices: ρ₀⁻¹σ₀ε₀ = −1 = ρ₀³ = σ₀². The "seule relation" part remains
  untested. Confidence: medium.
