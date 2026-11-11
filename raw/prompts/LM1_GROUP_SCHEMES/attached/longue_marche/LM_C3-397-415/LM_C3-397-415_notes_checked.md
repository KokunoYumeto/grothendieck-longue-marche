# LM_C3-397-415 — research notes, checked against the corrected transcription (scans 397–415)

Source: the first pass's research notes (answers/unzipped/LM_C3-397-415/LM_C3-397-415_notes.md, "Research notes —
English", 70 notes, numbered N1–N70 in their order), each checked against LM_C3-397-415_checked.tex. Verdicts: keep,
correct (text revised), drop. Notes marked **Claude (second pass)** are new. Kinds: conjecture (Grothendieck's
conjectures, questions, expectations), unproved claim, unpursued implication, own idea. "Unproved" means not proved
in the cited passage.

Conventions used in the checks (all from these pages): M_{ρ,σ} = τ_{ρ,σ}.SG with τ_{ρ,σ} = SG^*_{ρ,σ}(0) ⊂
T_0×T_ρ×N′_σ, group law componentwise; I = Ker Θ (rel. dim 2), J = Ker(M→PG) (rel. dim 3) (scan 398); modular case
ρ = (0 1; −1 1), σ = (0 1; −1 0), τ_∞ = diag(−1, 1) (scan 403); an element n ∈ N′_σ with ε(n) = −1 acts on
T_σ = units of O_S[σ] by a + bσ ↦ a − bσ, i.e. y ↦ ȳ, and ȳ = y⁻¹ when det y = 1.

## Notes of the first pass

### Scans 397–399

- **N1 — 397, after (4)–(7) — unproved claim — keep.** Θ is called epi because its image contains SG and its composite
  with det is the multiplier χ, itself epi. The reduction needs that a subgroup sheaf of G containing SG and mapping onto
  G/SG ≃ G_m is all of G, which is immediate fppf-locally; the page gives only the reduction.
- **N2 — 397, (8) — unpursued implication — keep.** M^+ := Ker χ is defined just before the hom of exact sequences (9).
  How M^+ sits over SG is the content of (9); see C1.
- **N3 — 398, after (9) — unproved claim — keep.** "nécessairement plat de dim relative 2" for I = Ker Θ needs Θ
  faithfully flat (a fibrewise surjective homomorphism of flat group schemes of finite presentation) and the dimension
  count 6 − 4 = 2; neither is argued.
- **N4 — 398, last paragraph — conjecture — keep.** "on prévoit qu'il est commutatif, (de dim relative 3) — et à
  composantes toriques si T°_ρ, T°_σ sont des tores": the insertion "à composantes" is confirmed. The expectation is
  conditional and is not proved here (for the neutral component it follows from (17) on scan 400).
- **N5 — 398, (10)–(11) — own idea (first pass) — keep.** Compare the filtration 1 ⊂ I ⊂ J ⊂ M (M/I ≃ G,
  M/J ≃ PG ≃ SG/μ_2, J/I ≃ G_m) with the coordinate descriptions (14) and (17)–(18). Medium confidence, as a
  consistency check.
- **N6 — 399, (12)–(13) — unproved claim — correct.** (13) is an equality in the ink (vertical "="): M_{ρ,σ} =
  {(x,y,f) | det f = det y = ε′ det x, ε′² = 1} ⊂ T_ρ×N′_σ×G. Its derivation from "par construction du produit ½ direct"
  (M = SG^*(0).SG, SG^*(0) ⊂ T_0×T_ρ×N′_σ, T_0.SG = G) is not written out. Revised: the first pass read "≃".
- **N7 — 399, (14) — unproved claim — correct.** The ink superposes I and J on the first label (now `\unsure{I|J}`) and
  has J on the second. By the definitions of scan 398 the λ-set {(x,y,λ) | det y = ε det x = λ², ε² = 1}
  (rel. dim 2+2+1−2 = 3, f = λ scalar so det f = λ²) is J, and the set {(x,y) | det y = 1, (det x)² = 1} (rel. dim 2,
  f = 1) is I. So either the overwriting ran J→I against the mathematics or the two labels are swapped; the mathematics
  does not depend on which.
- **N8 — 399, last paragraph — unpursued implication — keep.** "Il me semble plus naturel" switches to dévissage through
  the neutral component; methodological, not a connectedness proof.

### Scans 400–401

- **N9 — 400, (15) — unproved claim — keep.** M/M° ≃ G^*(0)/G^*(0)° ≃ μ_2×μ_2 rests on "cf p. 489 (23)" (§48.VIII,
  which the Circle table starts at p. 485), outside this package.
- **N10 — 400, (16)–(18) — unproved claim — keep.** The passage from the determinant equations to the kernels J° and I°
  is asserted; the isomorphisms should be given as morphisms of group functors.
- **N11 — 400, (17) — own idea (first pass) — correct.** The forgetful map (x,y,λ) ↦ (x,y) from J° = {det x = det y =
  λ²} to T_ρ×_{G_m}T_σ has kernel {(1,1,±1)} ≃ μ_2 and is surjective only fppf-locally (det x needs a square root): it
  is an isogeny of degree 2, not the "≃" of (17). Whether some other isomorphism exists is not settled on the page;
  Grothendieck wrote "≃ T_ρ×_{G_m}T_σ" on the λ-line, struck it, and rewrote it on the next line. High confidence in
  the diagnostic; revised from "possible μ_2 kernel".
- **N12 — 401, theorem (19)–(20) — unproved claim — keep.** The theorem recapitulates (15); it depends on the
  definition "p. 487′ (20)" in §48.VIII, outside this package.
- **N13 — 401, (21) — unproved claim — correct.** As written ("central (dans M_{ρ,σ} tout entier)") the claim is false
  for the factor ST_σ: an element with ε = −1 acts on ST_σ by y ↦ ȳ = y⁻¹. Counterexample in the modular case on
  integral points: σ = (0 1; −1 0) gives (1,1,σ) ∈ ST_ρ×ST_σ ⊂ M(Z), τ_∞ = (τ_∞,1,τ_∞) ∈ M(Z) (36), and
  τ_∞στ_∞⁻¹ = σ⁻¹ ≠ σ (cf. scan 407, "τ_∞ opère … par symétrie sur le dernier"). ST_ρ×ST_σ is central in M°, and
  ST_ρ×μ_2 in M; the later computation (49) of scan 411 agrees. Revised from "requires the action of the quotient".
- **N14 — 401, NB between the boxes — unproved claim — correct.** "J° est encore central dans M_{ρ,σ}" fails for the
  whole M for the same reason: (1,σ,1) ∈ J° (det 1 = det σ = 1²) is conjugated to (1,σ⁻¹,1) by τ_∞. J° is central in
  M°; in fact J° = Centre(M°) (C6). The NB's unfinished "J° ∩ SG ≃" is {(1,1,λ) | λ² = 1} ≃ μ_2, the centre of SG.
- **N15 — 401, cancelled passage below (24) — unpursued implication — keep, with reason.** The inclusion G → M° is
  annotated "inexistant": a homomorphic section f ↦ (x,y,f) would need x ∈ T_ρ, y ∈ T_σ with det x = det y = det f
  chosen multiplicatively in f, which the page does not have; the page itself withdraws the stronger display.
- **N16 — 401, (25) — unpursued implication — correct.** Given (24) M^{°+} ≃ ST_ρ×ST_σ×SG (which holds: χ = det f = 1
  forces det x = det y = 1 in (16)) and the inclusions (26), the three μ_2 lie in distinct direct factors, so (25) is
  injective, as its hook arrow says. Revised: the first pass doubted injectivity.

### Scans 402–404

- **N17 — 402, (27) — unproved claim — keep.** Σ = (Z/2Z)³ → ΓM^{°+} "déjà envisagés par ailleurs"; scan 411 places
  Σ "déjà dans (IX)", §48.IX (p. 490 in the Circle table). The final superscript of (27) stays unsure (+ or *).
- **N18 — 402, (30)–(31) — unproved claim — correct.** The splitting section is named on scan 403 (32): M_{ρ,σ}(0) ↪
  M_{ρ,σ}, mapped isomorphically onto τ^!_{ρ,σ}; scan 415 (17), (22) defines M(0) = M[0] ∩ (T_0×T_ρ×N′_σ) and proves
  M(0) → τ an iso by the same pattern. What remains to check is that M(0) is a subgroup and that it acts on SG by
  conjugation through its T_0-component.
- **N19 — 402, left margin — unpursued implication — correct.** New reading: the sign "!" "est tombé du ciel" (came
  from nowhere), "même dans la section suivant le X", and Γ_{ρ,σ} (not τ_{ρ,σ} "sans l'exposant") would be the right
  name. Scan 415's margin makes the same proposal (Γ_{ρ,σ}, after Γ_{g,ν}, Γ_{0,3}); the dark ink suggests both notes
  were added after XI was written.
- **N20 — 403, Rmq — conjecture rejected — correct.** The reason is now legible: "vu que G̃^+_{ρ,σ} ≃ Sl(2)_S est
  [struck word] relt connexe sur S". A group scheme with connected fibres has no non-trivial finite étale quotient, so
  no π with G̃^+/π ≃ G̃_3 exists among schemes; that is the stated obstruction. Revised: the first pass called the
  reason faint.
- **N21 — 403, (33)–(34) — unproved claim — keep.** The canonical section τ̇ = τ̇_∞ with representative τ_∞ =
  diag(−1, +1) in ΓM^!_{ρ,σ}(0): membership is checked on scan 405 ((36)), canonicity is asserted.
- **N22 — 403, last line → 404 — conjecture — keep.** "Il serait intéressant de voir si, en dehors du cas modulaire, on
  peut introduire des anti-involutions …"; the question continues on 404.
- **N23 — 404, (35) — conjecture — keep.** "je suis convaincu que oui": r_0, r_1, r_∞ are involutions of det −1 (r_1² =
  1 checked); the reference "p. 335′, §42, IV" is §42.IV "Relations avec SL(2,Z)" (p. 335). A general construction
  would need the base hypotheses that replace the modular coordinates.
- **N24 — 404, middle correction — unpursued implication — keep.** "je me mélange là les pinceaux": the −1 sections of
  the three μ_2 lie in M°, the reflections have multiplier −1 and lie over (−1,−1) ∈ M/M°. The struck qualifier of
  "les sections" reads "modulaires".
- **N25 — 404, struck centre sentence and inserted Z — unproved claim — keep.** Z_{ρ,σ} := (Centr M°_{ρ,σ}) replaces a
  struck claim about the centre of M; the centre of M° is computed in C6.
- **N26 — 404, struck calculation after (36) — own idea (first pass) — keep.** j_ρ, j_σ: G_m → T_ρ, T_σ composed with
  det give λ ↦ λ²; this is where the squares in (17) and (49) come from. Medium confidence as a check.

### Scans 405–406

- **N27 — 405, invariants of τ_∞ — unproved claim — keep.** "les calculs déjà faits donnent" α, ζ, β, η, μ, ε, ε′ from
  earlier pages; ζ = αρ(α)⁻¹ = −ℓ_1⁻¹ = −(1 0; −2 1) agrees with ℓ_1 = (1 0; 2 1). See C3 for the matrix entry B/D.
- **N28 — 405, NB → 406 — question — keep.** For u̲ = (μ λ; 0 1) the invariants are computed on 406: α = u̲, a̲ = 1,
  ε = ε′ = μ = (−1)^k, β = uτ_∞^k, b̲ = τ_∞^k.
- **N29 — 405, tuples (36) and NB — own idea (first pass) — correct.** The ring is settled on 406: the tuple of (37)
  lies in M_{ρ,σ}[0](Ẑ). The NB's "B′_0(Ẑ) ⊂ Gl(2,Z)" has no hat on the second Z (a slip for Ẑ, or for B′_0(Z)); the
  check of the coordinates over the stated ring stays useful.
- **N30 — 406, after (37) — unproved claim — keep.** "il n'est pas dans ΓG^*(0), sauf si λ = 0" explains why the group
  name SG^*(0)(Ẑ) of (37) is replaced by M[0](Ẑ).
- **N31 — 406, left margin NB — unproved claim — keep, verified.** r_1 = (−1 1; 0 1) = τ_∞·(1 −1; 0 1) with
  (1 −1; 0 1) ∈ L_0, so r_1 ≡ τ_∞ mod L_0 and both give (−1, 1, τ_∞) in τ_{ρ,σ} = M[0]/L_0.
- **N32 — 406, 3° — expectation — keep, verified.** r_1r_∞ = (1 1; 0 1) and r_∞r_0 = (0 −1; 1 0) generate SL(2,Z), and
  det r_∞ = −1, so r_0, r_1, r_∞ generate GL(2,Z), as "ça vaut mieux" requires.
- **N33 — 406, last paragraph → 407 — unpursued implication — keep.** τ′_∞ = τ_∞σ_∞ gives σ_∞ = (0 −1; 1 0) ∈ SG(Z);
  the common image (−1, 1, τ_∞) of the three reflections is stated on 407 (39).
- **N34 — 405–406, comparison of (36)–(38) — own idea (first pass) — keep.** Comparing the three images in M and in
  M/SG is useful; N31 and N33 now settle it for the quotient.

### Scans 407–408

- **N35 — 407, (40) — unproved claim — keep.** The numeral in "groupe dihédral d'ordre 4" is a 4 at enlargement;
  |{1,τ_∞}.Z/4Z| = 8, so "4" is the index n of D_n or a slip.
- **N36 — 407, (41) — unproved claim — correct.** τ_∞ lies in the third factor of a direct product, so its action on
  the first two factors is trivial without computation; on T_σ(Z) = ⟨σ⟩: τ_∞στ_∞⁻¹ = σ⁻¹, so "par symétrie" is
  inversion and (Z/2Z.Z/4Z) = D_4. Revised: verification added.
- **N37 — 407, margin NB at (42) — unpursued implication — keep.** "automatique, car G_m(Z) = {±1}" holds for
  integral points only.
- **N38 — 408, (43)–(44) — unproved claim — correct.** The ink has Z/4Z in (43) and twice in (44), while the first line
  of 408 and (42) have Z/6Z and (45) overwrites 4 by 6: (43)–(44) keep an uncorrected slip for Z/6Z×D_4. The
  semi-direct product uses the section M(0)(Z) ≃ τ(Z), acting on Sl(2,Z) through D_4 → {1,τ_∞} by conjugation.
- **N39 — 408, (45) — unpursued implication — keep.** The sign map is trivial on Z/6Z×D_4^+ and (−1,−1) on τ_∞, so its
  image on integral points is the diagonal {(1,1),(−1,−1)}: "pas surjectif" (409).

### Scans 409–410

- **N40 — 409, "pas surjectif" — unproved claim — keep.** The failure is on integral points; the scheme map
  M → μ_2×μ_2 is epi (15).
- **N41 — 409, first paragraph and margin "faux" — unproved claim — keep.** The margin's objection (g.f central
  without g acting trivially) is exactly what N13/C6 exhibit.
- **N42 — 409, (46) — unproved claim — correct.** The argument needs B′_0 to act faithfully on SG; the ink says "opère
  trivialt" (kept as written), which contradicts its use. The kernel of conjugation G → Aut(SG) is the centre G_m of
  G, and B′_0 ∩ G_m = {1}, which gives the faithfulness and implies (46).
- **N43 — 409, "Reste" and lower margin — unpursued implication — keep.** Reduction to the invariants of μ_2×μ_2 on τ°;
  the margin limits it to the intersection of the centre with τ°.
- **N44 — 409, own idea (first pass) — keep.** Centrality of (n,a) in N⋊A: a acts on N as conjugation by n⁻¹ and n is
  fixed by A. High confidence as a strategy.
- **N45 — 410, (48) — unproved claim — keep.** The action of μ_2×μ_2 on τ° factors through the first projection
  ε(b̲).
- **N46 — 410, invariants — unproved claim — keep, with caveat.** The invariants of σ ↦ −σ on T_σ are the scalars
  G_m only where 2 is invertible.
- **N47 — 410, last paragraph — unproved claim — correct.** The corrected sentence is "la trace du centre de τ_{ρ,σ}
  sur le sous-groupe τ′_{ρ,σ} … est aussi la trace, sur ce sous-groupe, de T_0×T_ρ×G_m": Centre(τ) ∩ τ′ =
  (T_0×T_ρ×G_m) ∩ τ′. With faithfulness on τ′ (τ′ → T_σ epi) Centre(τ) ⊂ τ′, hence Centre(τ) =
  (T_0×T_ρ×G_m) ∩ τ, the second line of (49). Revised: the first pass read "portion" (deleted).
- **N48 — 410, own idea (first pass) — keep.** Test the fixed-point equations over rings with 2 = 0 (see N46).

### Scans 411–412

- **N49 — 411, (49)–(50) — unproved claim — keep.** (50) is written as an equality ST′_ρ = {a̲ | (det a̲]² = 1}; the
  restriction u = 1 for trivial action on SG relies on (47)/(46), see N42.
- **N50 — 411, (51) and "faux le centre est plus grand" — unproved claim — keep.** (52) is a computation for the
  displayed subgroup, not for the centre.
- **N51 — 411, (52) NB — unpursued implication — keep.** "Ce groupe est en fait contenu dans M°(Z)".
- **N52 — 411, after (52) — unproved claim — keep, verified.** ρ³ = −1, so −ρ has order 3; det ρ = 1, so ST′_ρ(Z) =
  T_ρ(Z) ≃ Z/6Z and the group is Z/6Z × μ_2(Z) × μ_2(Z) as in (52); Σ is referred to "(IX)".
- **N53 — 411, last line — expectation — keep.** "Plus intéressant serait sans doute le centre de M°", continued on 412.
- **N54 — 411, own idea (first pass) — keep.** Solving centrality against SG and the complement together is what C6
  does.
- **N55 — 412, margin "faux ! Centre est de dim 3" — unproved claim — keep.** Confirmed by C6.
- **N56 — 412, (54) and "deux fois plus gros" — unpursued implication — keep.** Cancelled comparison on integral
  points; the label is written "(14)" for (54).
- **N57 — 412, struck Rmq — unproved claim (cancelled) — keep.** "La composante neutre du centre de M° est bien sûr
  ST_ρ×ST_σ" is withdrawn by the dimension-3 margin (C6).
- **N58 — 412, own idea (first pass) — keep.** Superseded in substance by C6, which gives the centre.

### Scans 413–415

- **N59 — 413, (1)–(3) — unproved claim — keep.** Existence, uniqueness and base change of the canonical lifts are not
  argued; (3) fixes the sign of σ (C4).
- **N60 — 413, (5)–(8) — unproved claim — keep, verified.** From (3) and (7): ε_1 = −ρσ⁻¹ = (1 0; 1 1) (6), ε_0 =
  −σ⁻¹ρ = (1 1/v; 0 1) (8), det ρ = det σ = −v, Tr ρ = 1, Tr σ = 0. The épinglage is fixed by (6); its global
  existence over S is not shown.
- **N61 — 413, own idea (first pass), signs and characteristic 2 — keep.** The generator is now read ε (ε_0, ε_1).
- **N62 — 413, (7) — unpursued implication — keep.** The single parameter v ∈ ΓG_m.
- **N63 — 414, λ versus λ/v — own idea (first pass) — keep.** L_0 = {(1 λ; 0 1)} as a set and ε_0(λ) = (1 λ/v; 0 1)
  as a parametrisation agree because v is invertible.
- **N64 — 414, (12) — own idea (first pass) — keep, verified.** Discriminants 1 + 4v and 4v; in the modular case
  v = −1 they are −3 and −4, the units Z[ζ_6]^* ≃ Z/6Z and Z[i]^* ≃ Z/4Z of (40).
- **N65 — 414, (13)–(14) — unproved claim — keep.** Exactness of 1 → T_σ → N′_σ → μ_2 → 1 as sheaves, including
  characteristic 2.
- **N66 — 414, (10) — unpursued implication — keep.** T_0 acts on L_0 by μ·ε_0(λ)·μ⁻¹ = ε_0(μλ).
- **N67 — 415, (17)–(19) — unproved claim — keep.** M[0] ≃ M(0).L_0 (½-direct) is asserted.
- **N68 — 415, (17) — own idea (first pass) — keep.** Ink re-checked: "défini par u̲ = 1" is clear. The "i.e." that
  follows (intersection with T_0×T_ρ×N′_σ) means that the upper-right entry λ of u̲ vanishes, not u̲ = 1; the two
  conditions conflict, and (22) uses the intersection.
- **N69 — 415, (20)–(23) — unproved claim — keep.** χ, ε_2, ε_3 are trivial on L_0 (det u̲, b̲ unchanged), so they
  factor through τ = M[0]/L_0; ε_3 = det a̲/det b̲ = ε′ by (16).
- **N70 — 415, lower margin — unpursued implication — keep.** "Cette notation n'est pas du tout adéquate (inspirée à
  tort du τ_{g,ν}) … la notation Γ_{ρ,σ} conviendrait": the same proposal as the note on 402 (N19).

## New notes (Claude, second pass)

- **C1 — 398, (9) — own idea (Claude, second pass).** The right vertical arrow G_m → G_m (its label "det" struck) must be
  the identity, since det∘Θ = χ (397). The snake lemma then gives M^+ → SG epi with kernel I_{ρ,σ} (I ⊂ M^+ because
  χ = det∘Θ is trivial on Ker Θ). Confidence high.
- **C2 — 401, (24) — own idea (Claude, second pass).** M^{°+} = Ker(χ|M°) = {(x,y,f) | det x = det y = det f = 1} =
  ST_ρ×ST_σ×SG inside T_ρ×T_σ×G by (16): (24) holds, with relative dimension 1+1+3 = 5 = 6 − 1. Confidence high.
- **C3 — 405, matrix u — own idea (Claude, second pass).** The ink writes the upper-right entry as "B/D = μD"; with
  1/D = μ it is μB. Here B = 0, so u = diag(−1, 1) = τ_∞ either way; the slip does not affect (36). Confidence high
  for the algebra, the ink reading kept.
- **C4 — 413, (3) and (7) — unpursued implication (Claude, second pass).** In the modular case v = −1, (7) gives
  σ = (0 −1; 1 0), which is −1 times the σ of scan 403 and equals σ_∞ of scan 406. The sign is forced by (3): with
  σ = (0 1; −1 0), −σ⁻¹ρ = (−1 1; 0 −1) is not unipotent. So the canonical lift of σ̃ in XI is not the σ of the
  "cas modulaire" of 403; formulas carried over from 403–412 should be checked for this sign. Confidence high.
- **C5 — 401, (21) and NB — unproved claim (Claude, second pass).** The statements "ST_ρ×ST_σ … central (dans M tout
  entier)" and "J° est encore central dans M" are false as stated for the whole group; the counterexample is in N13
  and N14 (τ_∞ inverts σ ∈ ST_σ(Z)). Both are true for M°. The later pages (409–412) compute the centre with T_σ-part
  G_m and so contradict (21) without saying so. Confidence high.
- **C6 — 412, centre of M° — own idea (Claude, second pass).** Centre(M°) = J°: Θ: M° → G is epi, so a central element
  maps into the centre G_m of G, whence Centre(M°) ⊂ Ker(M° → PG) = J°; conversely J° ⊂ T_ρ×T_σ×G_m is central in
  M° ⊂ T_ρ×T_σ×G. So the centre is {(x,y,λ) | det x = det y = λ²}, of relative dimension 3, as the margin "faux !
  Centre est de dim 3" says against the struck (53), and its neutral component is not ST_ρ×ST_σ (dimension 2).
  Confidence high.
- **C7 — 409, (46)–(47) — unpursued implication (Claude, second pass).** With N42 (faithful action of B′_0), the
  subgroup of τ acting trivially on SG is τ ∩ (1×T_ρ×N′_σ) = {(1,a̲,b̲) | det b̲ = 1, (det a̲)² = 1}, which is (47) as
  written; the left-margin "faux" concerns the next step (centre of a semi-direct product), not (47). Confidence
  medium.
- **C8 — 403, reference — unpursued implication (Claude, second pass).** "(§46, V)": the Circle table's §46.V,
  "Récapitulation en termes de M̃^!_{0,3}[0]; les sous-groupes M̃^!_{0,3}(q), q ∈ {0,1,∞}" (p. 407), is the source of
  M^{!~}_{0,3}(0) ⊂ M̃_{0,3} with which M_{ρ,σ}(0) is compared; reading the two together would show whether the
  analogy extends to the three subgroups q ∈ {0,1,∞} (here: r_0, r_1, r_∞). Confidence medium.
