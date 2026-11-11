# LM_C3-606-624: research notes checked against the corrected transcription (scans 606–624)

**Source:** the first pass's research notes in `answers/unzipped/LM_C3-606-624/LM_C3-606-624_notes.md` (§5,
notes 1–39). Each note was checked against `LM_C3-606-624_checked.tex`.

**Verdicts:**
- keep: the note stands as written.
- correct: the note is revised; the reason is given.
- drop: the note is withdrawn.

**Kinds:**
- conjecture: Grothendieck's conjectures, questions and expectations.
- unproved claim: a claim without proof in the cited passage.
- unpursued implication.
- own idea.

Notes marked **Claude (second pass)** are new.

The pages are §49 V of the Circle table, upper numbers 607–615. Readings used below (see the changes file):
- ξ = c²+cd+d².
- ε₀ is the generator of L₀^𝒢 (not ξ₀).
- 𝒢₃ = 𝒢^{+∧}/Π (not 𝔖₃).
- (120) has α ∈ Π̂_{0τ}.
- (122) reads u ≡ ε₃[σ]a (Π̂).
- (7) reads N_σ^* ∩ 𝒢^{+∧} = L_σ.

## Notes of the first pass

### Scans 606–611

- **N1 — scan 606 — unproved claim — correct.** The margin "On aura néc.ᵗ μ ≡ −1 (3)" has a one-line proof:
  c²+cd+d² ≡ (c−d)² (mod 3), and a square that is a unit mod 3 is 1. So μ ≡ −1 (3), and there is no gap.
- **N2 — scan 606 — own idea (first pass) — keep.** For c even and d odd, c²+cd+d² ≡ cd+1 (mod 4), so (105) forces
  c ≡ 2 (mod 4). The live NB after (103) (changes row 7) is the same kind of check, made at the level of σa ≡ u (4).
- **N3 — scans 606–607 — unpursued implication — correct.** The computation settles the independence.
  - With c even and d odd, (cρ⁻¹+d)² ≡ 1 (mod 4), so aτ'(a)⁻¹ ≡ ξ⁻¹ ≡ ε₂(ξ) (mod 4). This depends on ξ = −μ only.
  - Under (105) the sign is −1. This is why the struck "le signe ε est égal à +1" was withdrawn.
  - The step from mod 4 to mod Π̂₀ is justified in C2.
- **N4 — scan 607 — own idea (first pass) — keep.**
  - ᵗu = (Tr u) − u is the adjugate of a 2×2 matrix. So ᵗa₀/det a₀ = a₀⁻¹, and ᵗu = u⁻¹ when det u = 1, as the margin says.
  - The margin is live text: "On pose pour u ∈ M₂(Ẑ)". "pose" is not struck (changes row 10).
- **N5 — scan 608 — unpursued implication — keep.** For abelian extensions the argument is sound: Ext¹_Z(−, μ) is
  additive, μ×μ = (1×μ) ⊕ diagonal, and the extension is trivial over both summands. It proves only that ℰ is not abelian,
  which is what the Corollaire states.
- **N6 — scans 608–609 — unproved claim — correct.** "les seuls élémts d'ordre 4 étant dans ℰ''" follows from the paragraph
  just before it. ℰ − ℰ'' lies over 1×μ and the diagonal, the extension is trivial over both, so these elements have order 2.
  The claim is proved on the page.
- **N7 — scan 609 — own idea (first pass) — correct (answered by C3).** The class of ℰ is the quadratic form
  x₁² + x₁x₂ = ε₃ ∪ (ε₃ε₂) on μ×μ, coordinates (ε₃, ε₂). It contains a square term, and as a whole it is one cup product of
  two distinct characters.
- **N8 — scan 610 — unpursued implication — keep.**
- **N9 — scan 610 — conjecture / question — keep.**
- **N10 — scan 610 — conjecture — keep, corrected.** If C3 holds, the extension induced on Γ_Q is split (c = 0). Its
  restriction to the subgroup Γ'_Q = Γ_Q ∩ Γ'^∼_Q is then split as well, against "et même l'extension qu'elle induit au
  sous-groupe Γ'_Q". The presumption about S₀^ΠΓ'' as a whole is not decided by this.
- **N11 — scan 610 — conjecture / question — keep.**
- **N12 — scan 611 — unproved claim — correct.** The ink has "ξ', ξ'' ∈ H²(Q, μ₂)" (changes row 22). Classes of
  quadratic fields lie in H¹(Q, μ₂) = Q*/Q*², and their cup product lies in H²(Q, μ₂) ⊂ Br(Q). So the H² is a slip for
  H¹, and it is kept in the text. Read this way, c = (−3) ∪ (3).
- **N13 — scan 611 — own idea (first pass) — keep, confirmed.** (−3, 3) = 0 in Br(Q): 3 = −(−3), and (a, −a) = 0 because
  −a = N(√a). So "c ainsi explicité est ≠ 0" is false for c = ξ'ξ''. C3 shows that ξ'ξ'' is indeed the inflation of the class
  of ℰ, so the slip is not in the choice of the two fields.

### Scans 612–618

- **N14 — scan 612 — unproved claim — keep, corrected.** The short symbols that the note left open are now read:
  - (120): α ∈ Π̂_{0τ}.
  - (121): ε₂(σ).
  - (122): u ≡ ε₃[σ]a (Π̂).

  C4 derives both congruences of (122) from (120). The "théorème récapitulatif" asked for in the margin is in effect
  9°), scans 621–624.
- **N15 — scan 613 — unpursued implication — keep.** The sentence now reads "Z = Z_{ρ,σ} ⊄ M̃_{0,3}". The index-2 relation
  is L₀^Π = ℓ₀^Ẑ = ε₀^{2Ẑ} ⊂ L₀^𝒢 = ε₀^Ẑ (C5).
- **N16 — scan 614 — unproved claim — correct.** The value b = −1 is proved by what the page has.
  - Existence: −ℓ₀ is one of the generators of Π₀ (scan 605), so −1 ≡ ℓ₀ (Π₀), and −1 ∈ N_σ^*.
  - Uniqueness: N_σ^* ∩ Π₀ = {1}, scan 622 (7).
- **N17 — scan 615 — own idea (first pass) — keep.**
- **N18 — scan 615 — unproved claim — keep.**
- **N19 — scan 615 — unpursued implication — keep.**
- **N20 — scan 616 — unproved claim — keep, corrected.** The two lines "Im(… → N_ρ^*)" of (134) are slips for N_σ^*. The
  defined group, the set {β⁻¹u | u(σ) = ε₂(u) int(β)(σ)} and the last line all concern σ. The ink is kept.
- **N21 — scan 617 — unproved claim — keep.**
- **N22 — scan 617 — unpursued implication — keep.** M^! = Ker(M → 𝒢₃) is normal in M, and M₀^! is a direct factor of
  M^! ≃ M₀^! × μ, so it is normal in M^!. Non-normality in M is asserted and deferred ("cf plus bas").
- **N23 — scans 617–618 — unproved claim — keep.** The ink puts v = α⁻¹u in N_ρ^{!*} (changes row 39), the group of (141).
  The Proposition on 618 is the conclusion of this argument.
- **N24 — scan 618 — unpursued implication — keep.**
- **N25 — scan 618 — own idea (first pass), low — keep.**

### Scans 619–624

- **N26 — scans 619–620 — conjecture — keep, corrected.** The nontriviality of M(0)^∼ ("dont on s'est convaincu plus ou
  moins") is not proved here. If C3 holds, the extension splits over Γ_Q ⊂ M(0). Any nontriviality must then come from
  M(0) beyond Γ_Q.
- **N27 — scan 619 — unproved claim — keep.**
- **N28 — scan 620 — unproved claim — keep.** The case split uses α ∈ Π̂_τ = {1,τ}.Π̂. The inserted condition reads
  ε₃ \unsure{=|≠} −1, and only "= −1" fits the case split. A struck "α = α₀" stands before "α = α₀τ" (changes row 43).
- **N29 — scans 619–620 — own idea (first pass), medium — keep.**
- **N30 — scan 621 — unproved claim — keep.**
- **N31 — scan 621 — unpursued implication — keep.**
- **N32 — scan 622 — unproved claim (recapitulated) — keep.**
- **N33 — scan 622 — own idea (first pass) — correct.**
  - The labels of (5) now read ε'_γ = ε^ρ_γ and ε''_γ = ε_γ^{ρ|σ}.
  - In the second label the raised letter is partly hidden by the arrow. σ is expected, and (5 bis) identifies the two maps
    with ε₃ and ε₂.
  - The suggested audit stands.
- **N34 — scan 622 — unproved claim (recapitulated) — correct.**
  - The second line of (7) is an equality: N_σ^* ∩ 𝒢^{+∧} = L_σ. The only ≃ is in "(≃ Z/4Z)" (changes row 48).
  - There is no isomorphism symbol to retain, so that remark of the first pass is withdrawn.
  - The four intersections are restated without proof, as the note says.
- **N35 — scan 623 — unproved claim (recapitulated) — keep.** The iso (10) was first stated as (138) on scan 617.
- **N36 — scans 622–623 — own idea (first pass) — keep.**
- **N37 — scan 624 — unproved claim (recapitulated) — keep.** The first Cent subscript stays doubtful (M(0)|M).
- **N38 — scans 623–624 — own idea (first pass) — keep.**
- **N39 — scan 624 — unpursued implication — keep.**

## Claude (second pass)

- **C1 — scan 606 — unpursued implication.** The live NB explains why (102)–(103) are mod 2. By scan 605, (100),
  σa = (−d −c; −c c+d). If σa ≡ u = diag(μ,1) (mod 4), then −d ≡ μ and d ≡ 1, so μ ≡ −1 (4), against (95). The moduli 2
  written over 4 and the struck "(102) est trop fort … (102 bis)" are the trace of this correction.
- **C2 — scans 607–608 — own idea; confidence high.** "a fortiori on a la congruence mod Π̂₀" is valid.
  - In Γ(2) = Π, squares and commutators lie in Γ(4), and both subgroups have index 8. So Γ(4) is the Frattini subgroup of
    Γ(2).
  - Every index-2 subgroup of Γ(2) therefore contains Γ(4). This includes Π₀, of index 2 because Π = Π₀ × {±1} (scan 605),
    and it holds for the closures.
  - So a congruence mod 4 to the scalar ε₂(ξ) gives the congruence mod Π̂₀.
- **C3 — scans 609–611 — own idea; confidence medium-high.** The class of ℰ in H²(μ×μ, μ) is the squaring form
  q(g) = (lift of g)².
  - q = 1 on the image (−1, 1) of ℰ'' (u² = −1). q = 0 on 1×μ and on the diagonal: the restrictions are trivial (scan 608),
    and τ_ℰ² = 1.
  - In the coordinates (ε₃, ε₂) this gives q = ε₃² + ε₃ε₂ = ε₃ ∪ (ε₃ε₂). Since q takes the value 1 once, ℰ ≃ D₄ as in (111).
  - Inflated along Γ_Q → (Z/12)^* ≃ μ×μ, ε₃ goes to (−3) and ε₃ε₂ to 3 in Q*/Q*². This is exactly Grothendieck's ξ'ξ''
    for Q(√−3) and Q(√3), and it is 0 in Br(Q) (N13).
  - So if the extension on Γ_Q is the pull-back of ℰ, it splits, and "c ≠ 0" is false. The pull-back reading is suggested
    by τ_ℰ = τ_{S₀Γ} mod S₀^ΠΓ⁰, i.e. ℰ = S₀^ΠΓ^!/S₀^ΠΓ⁰.
- **C4 — scan 612 — own idea; confidence high.** (122) follows from (120).
  - With τ = diag(−1,1) and τ' = (0 1; 1 0) as on scan 605, ττ' = σ. From (120), u = α ε₃[τ'] a.
  - If ε₃(u) = 1: α ∈ Π̂₀ and u ≡ a (Π̂).
  - If ε₃(u) = −1: α = α₀τ and u = α₀ττ'a = α₀σa ≡ σa (Π̂).
  - This is u ≡ ε₃[σ]a (Π̂), with ε[x] = x^{(1−ε)/2}. It needs α ∈ {1,τ}.Π̂₀, the subscript reading Π̂_{0τ}, not the
    coset Π̂₀τ.
  - The other congruence, u ≡ b (Π̂₀), comes from b = β⁻¹u.
  - The ink's ε₂(σ) in (121) is most likely a slip for ε₂(u), compare (119) and (134).
- **C5 — scans 613–614 — unpursued implication.**
  - Take ε₀ = (1 −1; 0 1) and ℓ₀ = ε₀² = (1 −2; 0 1), as in the first passes of 568–586 and 587–605.
  - Then (127) reads L₀^Π = ℓ₀^Ẑ = ε₀^{2Ẑ} ⊂ L₀^𝒢 = ε₀^Ẑ, of index 2, and (129) gives L₀^Π/L₀^{Π₀} ≃ μ.
  - The first pass's ξ₀ named no element of the manuscript.
- **C6 — scans 616, 617, 623 — unpursued implication.**
  - 𝒢₃ = 𝒢^{+∧}/Π^∧ ≃ SL(2, Z/2) ≃ 𝔖₃. Since 𝔖₃ has trivial centre and only inner automorphisms, the map
    𝒢^{+∧}/Π^∧ → Aut(𝒢^{+∧}/Π^∧) in the NB of 616 is an isomorphism.
  - M^! is the kernel of the action of M on 𝒢₃, as (8) on scan 623 restates.
  - The letter is 𝒢 on all three pages (changes rows 35, 38).
- **C7 — scan 609 — unproved claim (reading).** In "x.u serait d'ordre 4|8" only 4 makes the argument valid: x.u would be
  an element of order 4 outside ℰ'', against scan 608. The ink's figure is ambiguous, so the reading stays open.
- **C8 — scan 622 — unpursued implication.** If the raised letter of the second label of (5) is ρ, as the ink suggests,
  both labels read ε^ρ_γ. That would be a slip, since (5 bis) sends the lower map to ε₂, the character attached to σ.
