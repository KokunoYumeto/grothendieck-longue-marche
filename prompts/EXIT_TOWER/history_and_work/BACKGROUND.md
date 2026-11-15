# EXIT_TOWER: background

Written by Claude Fable 5.2 (effort max), 12 November 2026, as reader R-GLUE of the Montpellier archive programme. A draft, not authority: the arguments are sketches by one reader, checked by no one.

## 1. Sources and their status

- Cote 147, §9 (scans 76–89), §10 (scans 90–104), the struck section (scan 105), §§11–12 (scans 106–180): first-pass transcriptions by GPT-6 Astra (ChatGPT Pro mode); no second pass. §9 was read in a condensed form (diagrams and prose, without the struck passages in full); scans 60 and 86–89 by search only.
- Cote 146: **only scan 100 was read.** The definitions of `S_0𝒯`, `_0𝒯`, `R_0𝒯`, of `Â`, of the action of `(Z^Â, μ_2^Â)` and of "genre virtuel" are before and after it; the prompt tells the model to read them in the attached transcription. Cote 142 (which round 2 of our planning connects with hole filling, scans 18–21) was not read for this prompt.
- STRATA F, RESIDUE H, BISITE F.15–F.17: claims of GPT-6 Astra (ChatGPT Pro mode); no review at full effort. Read in their registers of results, not in their proofs.
- LM3, LM3b: read through the reviews by Claude Opus 5.5 (effort max, 12 November 2026); the statements cited carry the review's verdict. The returns themselves were not opened for this prompt.
- The 2026 preprint of Boggi named in Lead 5 was read by an earlier reader in its introduction only.

## 2. His §§9–10 in present terms

| His object (scan) | What it is |
|---|---|
| MD-graph `G` | stable graph: vertices with genera, edges (nodes), legs (marked points) |
| `M_G` (76) | curves with an identification of their graph with `G`: a product of the `M_{g_α, Î_α}` over the vertices, `Î_α` the legs and half-edges at `α`; the stratum itself is the quotient by `Γ_G = Aut G` |
| `(ΠM_G, Γ_G)` (77) | orbifold fundamental groupoid of the stratum; for a multicurve `σ` with graph `G`, its group is `Stab(σ)/Δ_σ` |
| `G′ = G/C`, generization (78) | contracting the edges in `C`: smoothing those nodes; `τ = σ ∖ C` |
| `M^*_{G,G′}`, `ΠM^*_{G,G′}` (79–80) | punctured germ of the stratum of `G` in the closure of that of `G′`: the link; its groupoid is that of crossing arrows |
| `φ_{G,G′}`, `γ_{G,G′}` (103) | source and target of crossing arrows; `φ` is an extension by `Z^C` |
| (105) | composition of crossing arrows, as a 2-fibre product over the middle stratum |
| `S_AΠM_G` (113) | the link of the stratum in the open stratum: group `Stab(σ)` |
| normalization morphisms (95) | cutting edges (strict), forgetting legs, passing to a union of components |
| (144), (148) | a stratum is a product of open moduli; what remains is forgetting marked points on the open moduli |

## 3. Sketches behind the leads

**Lead 1.** In the exit category of the returns, `Hom(σ, τ) = {g : gσ ⊇ τ}/Δ_σ`. The groupoid of crossing arrows from the orbit of `σ` to that of `τ` is the action groupoid of `Aut(σ) × Aut(τ)` on this set. At the class of the identity (`σ ⊇ τ`) its isotropy is the set of pairs `(xΔ_σ, x′Δ_τ)` with `x′ ∈ xΔ_σ`, `x ∈ Stab(σ)`, `x′ ∈ Stab(τ)`; such a pair is determined by `x′ ∈ Stab(σ) ∩ Stab(τ)` modulo `Δ_τ`. So the isotropy is `Stab(σ, τ)/Δ_τ`, which maps onto `Stab(σ, τ)/Δ_σ` with kernel `Δ_σ/Δ_τ ≅ Z^C`. This is his "extension par `Z^C`", the group `Γ^!_{G,G′}` accounting for the difference between `Stab(σ, τ)` and the pure stabilizer. His (105): for `σ ⊇ τ ⊇ ρ` the composite of crossing arrows has isotropy `Stab(σ, τ, ρ)/Δ_ρ`, of finite index in `Stab(σ, ρ)/Δ_ρ`, an extension of the stratum group of `σ` by `Z^{C ⊔ C′}`.

**Lead 2.** A vertex of genus 0 with three special points becomes unstable when one of them is the forgotten mark. If the other two are half-edges (a bridge), the two edges merge into one, and both Dehn twists become the twist along the merged curve: the map of lattices is the sum `Z² → Z`. If one is a half-edge and one a leg (a tail), the edge disappears and its twist becomes trivial; but that twist is already in `Δ_σ`, which is divided out in the exit category, so no automorphism is lost there. RESIDUE H.3 says that the lifting category is `BZ` exactly in the bridge case when the arrow downstairs smooths the merged node.

**Lead 3.** RESIDUE H.5: the forgetful functor is smooth only over `(0, 3)`. The first failure of exactness found by LM3b B.5 is for `(0, 4) → (0, 3)`. Unless the comparison between the two settings (automorphisms of completed categories against lifting categories) is not the one we suppose, the `BZ` cannot be the cause there.

**Lead 4.** As in the background of EXIT_ONE_TYPE, §3: the homotopy fibre of a thickening of the strata of dimension `≤ k` over `M_{g,n}` is the realization of a rank-selected subposet of the curve complex. In genus ≥ 1 the curve complex is not of the dimension of its simplices' maximal chains in homotopy (Harer: a wedge of spheres of dimension `2g − 3 + n` for `n > 0`, `2g − 2` for `n = 0`), so Cohen–Macaulayness in the dimension `d − 1` fails and the guess is only a guess.

## 4. What the returns say of themselves

STRATA F.17 gives the genus-zero Teichmüller groupoid as the open subgroupoid with a presentation by elementary moves, and states: no profinite completion of the moduli category, no arithmetic Galois action, no comparison with the Grothendieck–Teichmüller group. LM3 F.18 (open) and LM3b H.9 (open) leave the comparison of all finite homotopy types open from `n = 5` on; LM3b H.8 claims `n = 4` (reviewed: correct).

## 5. Literature named in the prompt (from memory; to be opened and verified)

Jansen (2023), the stratified homotopy type of the Deligne–Mumford compactification (Construction 3.18, Corollary 6.6, Theorem 6.7, as quoted by the returns). Charney–Lee (1984), moduli space of stable curves from a homotopy viewpoint. Harvey (1981), boundary structure of the modular group. Harer (1986). Hatcher–Thurston (1980); Hatcher–Lochak–Schneps (2000), on the Teichmüller tower of mapping class groups. Nakamura–Schneps (2000). Boggi (2020, and a 2026 preprint). Hoshi–Minamide–Mochizuki (2022); Hoshi–Mochizuki (2011). Harbater–Schneps (2000). Barwick–Glasman–Haine, *Exodromy*. Chan–Galatius–Payne (2021).
