# LM_C3-473-491 — research notes, checked against the corrected transcription (scans 473–491)

Source: the first pass's research notes (answers/unzipped/LM_C3-473-491/LM_C3-473-491_notes.md, notes 1–60), each
checked against LM_C3-473-491_checked.tex. Verdicts: keep, correct (text revised), drop. Notes marked **Claude (second
pass)** are new. Kinds: conjecture (Grothendieck's conjectures, questions, expectations, programme), unproved claim,
unpursued implication, own idea. "Unproved" means not proved in the cited passage.

Conventions used in the checks (from (8), scan 479): ρ = R = (0 1; −1 1), σ = J = (0 1; −1 0), acting on G = Gl(2) by
conjugation, so ρ(α) = RαR⁻¹, σ(b) = JbJ⁻¹; ρ³ = σ² = −1. Cross-references: p. 526' = scan 448, p. 535' = scan 466,
p. 536' = scan 468 (proposition (19)–(20), corollary (21)–(22)), p. 538' = scan 471 ((27)–(31), existence theorem).

## Notes of the first pass

### Scans 473–478 (§48.XI, 9°–10°)

- **N1 — scan 473, (34)–(36) — unproved claim — correct.** With (34) as definition, SM = M ×_{G_m} B′₀ is a fibre
  product of group schemes over homomorphisms, so the group law is automatic and the two projections give (35), (36)
  with kernels L₀ = Ker δ_{B′₀} and M⁺ = Ker χ. What remains to check is surjectivity: for (35) it is clear (det on
  B′₀ is split by T₀, scan 474); for (36) it needs χ: M → G_m to be fppf-surjective. Revised: the group law is not an
  issue, surjectivity of χ is.
- **N2 — scan 473, (37) — unpursued implication — keep.** (37) is the graph of Θ_G on M[0]; it meets L₀ trivially and
  maps isomorphically onto M[0] under (35); its image in B′₀ under (36) is Θ_G(M[0]). The cross-reference beside it is
  now read "(cf (14|19) p. 536')" (live, not struck).
- **N3 — scan 474, (38) — unproved claim — correct.** Checked: i_{T₀}(μ) = diag(μ,1) conjugates (1 λ; 0 1) to
  (1 μλ; 0 1), so through the embedding x ↦ (x, i_{T₀}(χ(x))) (scan 479, (7)) M acts on L₀ ≅ G_a by λ ↦ χ(x)λ, as the
  text says. Revised: verified.
- **N4 — scan 474, theorem (39) — unproved claim — correct.** The isomorphism is the existence-and-uniqueness statement
  of p. 538' (scan 471: (α,β,f) satisfying (27), (31) come from a unique (x,u) by (30)). The group law on SΣ* is the
  transported one, not the componentwise one: (x,u)(x′,u′) gives α″ = uu′a′⁻¹a⁻¹ ≠ αα′ in general (scan 472 speaks of a
  "groupe étrange … via relation de cocycles"). The ink cites "(17) et (31)"; see C2.
- **N5 — scan 475, (40)–(41) — unproved claim — correct.** Immediate: (1,ℓ)(x,u) = (x,ℓu) and a, b, U depend on x
  only, so α, β, f become ℓα, ℓβ, ℓf. Since the L₀-action on SM is free with quotient M, the quotient SΣ*/L₀ exists and
  is M through (22). Revised: verified.
- **N6 — scan 475, proposition (42)–(43) — unproved claim — correct.** The corollary is on scan 468: x ↦ (U,a,b) is a
  monomorphism with image δ_G(U) = δ_σ(b), [δ_ρ(a)/δ_σ(b)]² = 1. Adding det u = det U from the fibre product gives
  (43) at once, so "conséquence immédiate" holds. Revised: the missing corollary is located.
- **N7 — scan 475, (43) — own idea (first pass) — keep.** The condition det a/μ ∈ Γμ₂ is functorial and μ₂ is not
  étale at 2, so checks over rings where 2 is not invertible are warranted; C6 gives an instance where the 2-adic
  behaviour differs from the fibres over fields.
- **N8 — scan 476, (44) — unproved claim — correct.** Immediate from (22) of p. 536': for (a,b) ∈ 𝒯, (a,b,b) satisfies
  det b = det b and (det a/det b)² = 1, and (a,b) ↦ (a,b,b) is a homomorphism because M ⊂ T_ρ × N′_σ × G is a subgroup
  with the componentwise law and N′_σ ⊂ G. Revised: verified.
- **N9 — scan 476, (45)–(47) — unpursued implication — correct.** The asymmetry is located: (a,b,a) lies in M only if
  det a = det b, i.e. on 𝒯′ = Ker(ε₃) = T_ρ ×_{G_m} N′_σ, whereas (a,b,b) lies in M for all of 𝒯. (In (45) the ink
  writes "dans M", not "∈ M".)
- **N10 — scan 476, (46) — own idea (first pass) — correct.** On 𝒯′ the two sections agree exactly where a = b in G,
  i.e. on the diagonal copy of T_ρ ∩ N′_σ. Over a field this is the scalar G_m (cρ + d normalising ±σ forces c = 0), but
  over ℤ/4 the element 2ρ + 1 = (1 2; −2 3) lies in T_ρ and conjugates σ to −σ, so the intersection is larger at 2.
  Computation checked; confidence high for these facts, the subgroup-scheme description not worked out.
- **N11 — scan 477, Remq — unproved claim — correct.** The general situation is that of p. 526' ff (now read
  "avec 7°", doubtful): embeddings T_ρ, N′_σ ↪ G with δ_ρ, δ_σ induced by δ_G. Under these hypotheses N8 and N9 go
  through verbatim, the second only over 𝒯′. Revised: hypotheses identified.
- **N12 — scan 477, (50)–(52) — unpursued implication — correct.** ρ_G ∈ SG has ρ_G³ = −1, central, so int(ρ_G)³ = id,
  matching ρ̇³ = id; ρ̇ is the homography of the matrix ρ of (8), q ↦ (0·q + 1)/(−q + 1). So transporting M(0) and
  M(½) by int(ρ_G) is consistent on the two 3-cycles. Revised: settled.
- **N13 — scan 477, last paragraph — conjecture — keep.** "Je voudrait : définir M(−j)" (the ink has "voudrait"); the
  choice within the Sl(2,ℤ)^∧-conjugacy class is left open (see N15).
- **N14 — scan 477, (52) — own idea (first pass) — correct.** Verified: 0 ↦ 1 ↦ ∞ ↦ 0 and ½ ↦ 2 ↦ −1 ↦ ½; the fixed
  points of ρ̇ are the roots of q² − q + 1, i.e. −j and −j̄, which is why M(−j̄) = M(ρ) in (49) and M(−j) is a separate
  problem. Confidence high.
- **N15 — scan 478, (53) — conjecture — correct.** Scan 478 holds only the end of the sentence and (53), with σ_i
  clearly read; the rest of the page is blank and the next page starts §48.XII. The restricted choice among
  int(σ_i)(M(0)), i ∈ {0,1,∞}, is therefore left without criterion.

### Scans 479–482 (§48.XII, the group schemes)

- **N16 — scan 479, (1)–(4) — unproved claim — keep.** With the corrected readings: (1) M ⊂ T_ρ × N′_σ × G,
  (2) SM ⊂ B′₀ × T_ρ × N′_σ × G, (3) coordinates (a, b, U), (4) (u, a, b, U).
- **N17 — scan 479, (5)–(7) — unproved claim — correct.** The coordinate orders are now resolved from the ink (see C3):
  (3), (4) are revised to (a,b,U) and (u,a,b,U), but (5) "λ ↦ (1,1,1,λ)" and (7) "x = (U,a,b) ↦ (U,a,b,i_{T₀}(μ))" are
  in the older order, with U first and u last. In the revised order (5) is λ ↦ (λ,1,1,1); the semidirect product is N3.
- **N18 — scan 479, (9)–(11) — unproved claim — correct.** The kernel of ε_σ is the centraliser of σ, the matrices
  (u t; −t u) = T_σ, and ε ↦ diag(1,ε) is a homomorphism μ₂ → N′_σ with diag(1,ε)σdiag(1,ε)⁻¹ = εσ over any ring. So
  (11) is split and surjective on points over every ring, not only fppf-locally. Verified.
- **N19 — scan 479, (9) — own idea (first pass) — keep.** t² + u² ≡ (t + u)² mod 2 and c² + cd + d² ≡ (c − d)² mod 3
  verified.
- **N20 — scan 480, (12)–(16) — unproved claim — correct.** The image of (13) is the locus (14) by the proposition of
  p. 536'. The last form of the sign condition in (14), "b ᵗb = ε", is wrong on Gl(2) (C1); the conditions themselves
  ("ε = ε_σ(b) i.e. b(σ) = εσ") are right.
- **N21 — scan 480, (17) — own idea (first pass) — keep.** The ink reads G_a (closed a, unlike the G_m of (13) on the
  same page). With G_a the equations of (17) do not force μ to be invertible, while (22) sends (u,a,b,U) to systems with
  μ = det u ∈ G_m and (31) of p. 538' has μ ∈ ΓG_m; either the relation forces invertibility or G_m is meant.
- **N22 — scan 481, (19) — unproved claim — correct.** If two systems share (α,β,f), then εε₁(μ − 1) = ε′ε₁(μ′ − 1),
  so ε₁(μ − μ′) is the scalar ε′/ε; a lower unipotent matrix is scalar only if it is 1, so μ = μ′ and ε = ε′ over any
  ring. Hence (19) is a monomorphism of functors. Verified.
- **N23 — scan 481, "librement" — unproved claim — correct.** ℓα = ℓ′α forces ℓ = ℓ′ (α invertible), so the action map
  L₀ × SΣ* → SΣ* × SΣ* is a monomorphism: the action is free scheme-theoretically. The quotient (21) exists through
  (22), being SM/L₀ = M.
- **N24 — scan 481, (22)–(23) — unproved claim — correct.** The inverse of (22) is the existence-and-uniqueness theorem
  of p. 538' (scan 471); compatibility of the actions is N5. The group structure is the transported one (N4).
- **N25 — scan 481, (24)–(25) — unproved claim — keep.**
- **N26 — scan 482, (26)–(27) — unpursued implication — correct.** Computed: Σ sits in M as the scalar triples via (30)
  and SG = {(1,1,U)}, so SG ∩ Σ = {(1,1,±1)} ≅ μ₂, central. Hence SG(Ẑ)/SG(Ẑ)∩Σ = Sl(2,Ẑ)/±1, consistent with reading
  the prime of Sl(2,Ẑ)′ as "mod ±1" (as in "le quotient Sl(2,Ẑ)′ de Sl(2,ℤ)^∧′", scan 487).
- **N27 — scan 482, (28)–(30) — unproved claim — correct.** Scalar triples (ε₁,ε₂,ε₃) with ε_i² = 1 satisfy (3) with
  ε′ = 1 and are central, so μ₂³ → M is a central monomorphism and Σ = μ₂³(ℤ) ≅ (ℤ/2ℤ)³. Verified.
- **N28 — scan 482, (31)–(32) — unpursued implication — correct.** M → 𝒯, (a,b,U) ↦ (a,b), has kernel SG; by (26) the
  image of G^{+∧}_{0,3} lies in SG(Ẑ)Σ/Σ, which dies in 𝒯(Ẑ)/Σ₀ with Σ₀ the image {±1}×{±1} of Σ. So (25) factors
  through M̃₀,₃/G^{+∧}_{0,3} = Γ̃₀,₃, giving (31).

### Scans 483–486 (the four homomorphisms)

- **N29 — scan 483, (33)–(36) — unproved claim — keep.**
- **N30 — scan 483, (37)–(40) — unproved claim — keep.**
- **N31 — scan 483, last line — unproved claim — keep.**
- **N32 — scan 484, upper half — unproved claim — keep.**
- **N33 — scan 484, (41)–(42) — unpursued implication — correct.** det u = 1/D, and on S₀M̃ the multiplier is μ = det u
  (fibre product over G_m), so D = μ⁻¹ ∈ Ẑ*; by (42) this says c² + cd + d² ∈ Ẑ* for these α. Not stated on the page.
  (42) itself is verified in C7.
- **N34 — scan 484, after (42) — unproved claim — keep.**
- **N35 — scan 484, (43) — own idea (first pass) — correct.** No separate closure check is needed: M̃₀,₃(0) is the
  inverse image of T₀(Ẑ) under the homomorphism (33) restricted to M̃₀,₃[0], hence a subgroup once (33) is one.
- **N36 — scan 485, (44)–(45) — unproved claim — keep.**
- **N37 — scan 485, before (46) — unproved claim — keep.**
- **N38 — scan 485, (47) — unpursued implication — correct.** On M̃₀,₃[0], Θ^π_G = Θ^π_{B′₀} gives u (46), and u ∈ T₀
  ⇔ B = 0 ⇔ u = diag(1/D, 1) = i_{T₀}(μ); so (47) and (43) define the same subgroup (writing i′_{T₀} for i_{T₀}).
- **N39 — scan 486, 3°) — unproved claim — keep.** ("ici encore", corrected reading.)

### Scans 487–491 (programme)

- **N40 — scan 487, first line — unproved claim — keep.**
- **N41 — scan 487, central paragraph — conjecture — keep.** ("en ces tout derniers jours", corrected reading.)
- **N42 — scan 487, a) — conjecture — keep.**
- **N43 — scan 487, b) — conjecture — keep.**
- **N44 — scan 488, c) — conjecture — keep.**
- **N45 — scan 488, d) — conjecture — keep.**
- **N46 — scans 488–489, e) — unpursued implication — keep.**
- **N47 — scan 488, d) — own idea (first pass) — keep.**
- **N48 — scan 489, "procédé systématique" — conjecture — keep.**
- **N49 — scan 489, "(génériquement réductifs ??)" — conjecture — keep.**
- **N50 — scans 489–490, f) — unpursued implication — correct.** The direction "pourrait se poursuivre in vitro (or: en
  outre) dans le cadre des seuls gros groupes fondamentaux profinis": if "in vitro" is right, the point is that this
  study can be carried out within the profinite groups alone, without group schemes.
- **N51 — scan 490 — conjecture — keep.**
- **N52 — scan 490, critical points — conjecture — keep.** The list of points is explained in C5.
- **N53 — scan 490, Deligne — conjecture — keep.**
- **N54 — scan 490, compactification — conjecture — keep.** Qualifier and name still doubtful ("protilp." | "pro. tilp.";
  "pro-nilp." would fit but is not what the ink shows).
- **N55 — scan 490, "arithmétisation des points complexes" — conjecture — keep.**
- **N56 — scan 490 — own idea (first pass) — keep.**
- **N57 — scan 491, first paragraph — conjecture — keep.**
- **N58 — scan 491, "(moralement du moins, pour le moment !)" — unproved claim — keep.**
- **N59 — scan 491, (48)–(49) — unpursued implication — correct.** The restriction of ψ_ρ to 𝒯′ is forced by the
  definition (3) of M (N9); whether it reflects the arithmetic (the point −j̄ versus ½) is the open part.
- **N60 — scan 491, (48)–(49) — own idea (first pass) — correct.** Done: (a,b,a) ∈ M iff det a = det b, i.e.
  (a,b) ∈ 𝒯′ = T_ρ ×_{G_m} N′_σ, while (a,b,b) ∈ M for every (a,b) ∈ 𝒯 since det a/det b ∈ μ₂.

## New notes — Claude (second pass)

- **C1 — scan 480, (14) — own idea — Claude (second pass).** With σ acting by conjugation by J, σ(b) = JbJ⁻¹ =
  det(b)·ᵗb⁻¹, so on Gl(2) the condition σ(b) = εb reads b ᵗb = ε det b, not "b ᵗb = ε" (and the brace label "ᵗb⁻¹"
  holds only on SG). Counterexample: b = diag(1,−1) ∈ N′_σ(ℤ) has bσb⁻¹ = −σ, so ε = −1, but b ᵗb = 1. Confidence high.
- **C2 — scan 474, theorem (39) — own idea — Claude (second pass).** The ink cites "satisfaisant (17) et (31)", but (17)
  (p. 536, scan 467) defines SM as M[0]·SG; the conditions on (α,β,f) are (27) (det conditions) and (31) (loop
  relation) of p. 538', as scan 472 says "(27)(31)". Probably a slip for (27). Confidence medium.
- **C3 — scans 479–482, coordinate orders — unpursued implication — Claude (second pass).** On scan 479 the ambient
  (1) and the coordinates (3) were revised from (U,a,b) to (a,b,U), and (2), (4) to B′₀ × T_ρ × N′_σ × G and
  (u,a,b,U); (15), (22), (27), (29) use the revised order, while (5), (7), (13), (14) keep the older one (U first, u
  last). Formulas taken from these pages must be read in the order of their own display.
- **C4 — scans 479–480, (2) and (15) — unproved claim — Claude (second pass).** With the corrected fourth factor G
  ((2): B′₀ × T_ρ × N′_σ × G; (15): B′₀ × T_σ × N′_σ × G × G_m × μ₂ × μ₂), the embeddings are those of (42) on scan
  475; with B₀ they would be false, U = Θ_G(x) being any element of G with det U = μ. (15) also writes T_σ for T_ρ in
  second place (kept as written).
- **C5 — scan 490, the "points critiques" — own idea — Claude (second pass).** The eight points 0, 1, ∞, ½, 2, −1, −j̄,
  −j are the cusps and the points of P¹ − {0,1,∞} with non-trivial stabiliser in the anharmonic group S₃: ½, 2, −1 are
  fixed by the involutions q ↦ 1 − q, q ↦ q/(q − 1), q ↦ 1/q, and −j, −j̄ by the 3-cycles q ↦ 1/(1 − q),
  q ↦ 1 − 1/q. Confidence high.
- **C6 — scan 476, (46)–(47) — own idea — Claude (second pass).** 𝒯′ ⊂ 𝒯 is the kernel of ε₃ = det a/det b, and the
  two sections ψ_σ, ψ_ρ coincide on the diagonal of T_ρ ∩ N′_σ, which over fields is G_m but over ℤ/4 contains
  2ρ + 1 (N10). The comparison of the two scindages at 2 is therefore not determined by the fibres over fields.
  Confidence high for the example.
- **C7 — scan 484, (41)–(42) — own idea (verification) — Claude (second pass).** From ξ = αRα⁻¹R⁻¹ with α = (a b; c d),
  det α = ε′ = ±1: ξ = ε′(P + Q, −P; S + T, −S) with P = −(ac + bd + bc), Q = a² + ab + b², S = −(c² + cd + d²),
  T = ad + ac + bd. Hence ε′B = ac + bd + bc and ε′D = c² + cd + d², exactly (42) (the struck "/ε" was the same
  formula solved for D). Confidence high.
- **C8 — scan 486, "à partir du §46" — own idea — Claude (second pass).** The Circle table places §46 "Notations
  définitives (?)" at p. 390, with §46.V "Récapitulation en termes de M̃!₀,₃[0]" at p. 407: the work "dans M̃₀,₃[0]"
  began there, which supports the reading §46 (change 15). Confidence medium.
