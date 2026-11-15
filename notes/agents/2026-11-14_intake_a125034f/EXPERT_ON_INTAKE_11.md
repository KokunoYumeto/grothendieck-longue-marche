# The expert's weighing of intake section 11 (cote 145; cotes 143 + 141)

By Claude Fable 5.2 at effort max (field expert of the Longue Marche line, agent a125034fd35557818), 14 Nov 2026.
Read: section 11 of `INTAKE_20261114.md` (by Claude Fable 5.2 at effort high); the transcription pages of cote 145,
scans 7, 11, 22, 23, 24, 28, 29, and of cote 143, scans 29 to 33 (first-pass transcriptions by GPT-6 Astra, ChatGPT
Pro mode; no second pass; the scans were not opened). No literature. Not read: scans 8 to 10 and 12 of cote 145,
which finding 2 needs. The chain behind `Δ` (LM7_PUSH D.50, E.58, E.65; LM4 D.32, D.34) is by GPT-6 Astra (ChatGPT Pro
mode), refereed by Claude Opus 5.5 at effort max. "Hunch" marks what is mine and unproved. I edited no prompt.

## Verdicts in short

| Finding | Verdict |
|---|---|
| 1. Cote 143 ⑨ fails at type (0,3) in both forms | **Right.** The two margins are read correctly. |
| 2. Cote 145 is where the frames come from; `g` is the `r`-frame; `β` is `ρ_F`; `Δ` is a function of `γ` modulo 12 | **Half right; the dictionary as written is wrong.** His `g` is the cocycle `f⁻¹`, not the frame. The frames come from scans 22 and 28. `Δ` is not a function of `γ` modulo 12. `β` is not identified. |
| 3. "J'ignore si cette inclusion est une égalité": no | **Right.** The chain holds; I know no route without D.50, but the table can be replaced by one explicit element. |
| 4. Three lifts of complex conjugation and the cartographic group as the form of the conjugacy question | **Right**, and it gives my involution with `Δ = 1` a test. |

## Finding 1: the conjecture of cote 143, ⑨

**The reading.** Scans 29 and 30: arrow (1) is `π₁(M_{g,ν}; ξ) → Autextloc°(π₁(X̄ ∖ {x_i}))`, the outer automorphisms
that do not exchange the classes attached to the points; he would like it to be an isomorphism, which "would give a
characterization of Γ"; for `g = 0, ν = 3` it gives `Γ` as `Autextloc°` of the group of the three-punctured line. At
type (0,3) the geometric group `Γ̂_{0,3}` is trivial, so this form says `G_Q ≅ 𝒫`. Both margins then ask for the
commutation with `𝔖_3`, one of them naming `g = 0, ν = 3`; with it the statement is `G_Q ≅ GT̂₀`. The "version
corrigée éventuelle" adds the normalizer of `Γ̂_{g,ν}`, the commutation with `𝔖_ν` and "une structure « locale »
éventuelle". So the intake reads him correctly, and both written forms fail: the first by finding 3, the second by
E.58 with E.65. The second also fails without `Δ`: by D.50 and the pro-`ℓ` strictness, `GT̂` is a proper subgroup of
`GT̂₀`, and Galois lies in `GT̂`.

**What it means for the programme.**
- His own instinct located the weak point: "Il faut regarder surtout le cas `g = 0, ν = 3`". Type (0,3) is too small
  to carry the conditions. With the normalizer form, types (0, ν ≥ 4) give `GT̂` (LM3 E.7, E.10, as our handoff
  records them), where the conjecture is the open question whether Galois is all of `GT̂`; at (0,3) it gives `GT̂₀`,
  where it is now false.
- **Why `𝔖_3` is not enough (hunch, with an exact part).** Commuting with `𝔖_3` is the same as extending to the
  group `C_2 * C_3` of the quotient orbifold. The exact part: in that group every automorphism preserves the
  conjugacy classes of the two finite isotropy groups (torsion in a free profinite product is conjugate into a
  factor). So a "local structure" at the two elliptic points, read as conjugacy classes of local groups, is
  automatic and carries no condition. What Galois preserves there is finer: the decomposition groups of the two
  special points with their arithmetic, that is, the points as sections. That is the subject of the same cote,
  parts 2 to 8 (points as germs of sections; the Kummerian structure). The hunch: the "structure locale" he leaves
  open is the preservation of the sections of the harmonic and the equianharmonic point, and that condition
  implies `Δ = 0`.
- For the companion: his conjecture, his caution and the place of the failure are all in his hand; the refutation
  is by a character built from the splittings he computes in cote 145 (next section), and the missing condition is
  of the kind he studies in the same packet.

## Finding 2: the dictionary, corrected

Checked on scans 7, 11, 22, 23, 24, 28.

- **`g` is the cocycle, not the frame.** Scan 7: `u(l_0) = l_0^p` and `uρ = int(g)ρu`. Since `l_1 = ρ l_0 ρ⁻¹`, this
  gives `u(l_1) = g l_1^p g⁻¹`. So `(p, g)` is the pair `(λ, f⁻¹)` of the usual description, in his gauge, and the
  equation `uρu⁻¹ = int(g)ρ` is `Φ(r) = f⁻¹r` of LM7_PUSH E.65, not `Φ(r) = A r A⁻¹`. The frame `A` is a primitive
  of `g`: `g = A·ρ(A)⁻¹`. Cote 145 on these pages does not solve for it.
- **The gauge.** Replacing `u` by `int(l_0^α)u` changes `g` to `l_0^α g l_1^{−α}`, which is his action `φ(α)` on scan
  11. So `(γ, χ)` is the pair `(f, λ)` modulo the choice of `u` in its class, and "`(γ, χ)` is injective" says that
  an element of `GT̂₀` is determined by its pair. This matches §46 through LM2 B.m2 (`ξ = y^ν f`, with the same
  freedom).
- **`β` is not identified.** On scan 11 complex conjugation has `g = l_0^α l_1^β` with `α + β = 1`, and `β` is "défini
  par γ" through a relation that is on scan 12, which I have not read. The intake's "`β` is `ρ_F` of E.61" is
  unsupported: `ρ_F` is the abelianized coordinate of the `s`-frame, a primitive, while his `β` on scan 11 is an
  exponent of the cocycle. It may be the exponent of the 3-cycle relation. To be settled on scans 8 to 12.
- **Where the frames are.** Scans 22 and 28 to 29: the isotropy group of his base point `P` in `𝔖_3 × Z/2` is a copy
  of `𝔖_3`, lifted canonically to the extension (12); the transpositions fix `2, −1, 1/2`, which he names `0′, 1′,
  ∞′`, with isotropy groups `{σ_i, τ}` lifted to `(σ_i, τ_i)`. These are the canonical splittings over the isotropy
  groups at the point of order three and at the three harmonic points. A frame is what an element `u` does to such
  a splitting: `u` carries it to a conjugate, and the conjugator in `π̂` is the frame. In the Longue Marche the same
  data are the signed normalizers of `ρ` and `σ` of §49: the frame is the correction that moves `u` into the
  normalizer.
- **`Δ` is not a function of `γ` modulo 12.** `γ` determines the frames, so `Δ` is a function of `γ`. But the frames
  are primitives, and E.58's element shows what that means: its `f` lies in the nilpotent residual of `F′F³`, and
  its `r`-frame is `5·I` modulo 12. The class of `f` at a finite level does not give the class of the frame at that
  level.
- **A gain of the corrected reading:** the harmonic points are in the manuscript (scan 28), as the fixed points of
  the transpositions with their splittings. This is the manuscript form of my hunch that `Δ = 0` on Galois comes
  from the harmonic covering.

## Finding 3: scan 24

The question is whether `𝔖_3` acts trivially on the pure group `𝒫`. It does not. The chain: a special derivation
of weight five that is not `𝔖_3`-invariant (LM7 D.11: dimensions 3 and 1; recomputed by the LM7 reviewer, Claude
Fable 5.2 at effort max); it is the leading term of a pure peripheral automorphism of the free pro-`ℓ` group (LM8
B.11, proof read by the intake reader); that automorphism, with the identity at the other primes, is a peripheral
automorphism of `F/R_nil(F)` and lifts to `F` (D.50, refereed); leading terms are `𝔖_3`-equivariant, so the lift
does not commute with `𝔖_3`.

A shorter argument: I know none that avoids D.50. The lift from a quotient with the peripheral condition kept is
the whole difficulty (lifting generators alone loses it: LM7 D.24), and D.50 is the theorem that does it. What can
be shortened is the first step: no table is needed, one beta function that is not symmetric suffices, for instance
`1 + (X − 1)(Y − 1)(XY − 1)·X` on the pro-`ℓ` metabelian quotient, provided its leading term is checked not to be
invariant (the leading term of this one is symmetric, so the example has to be chosen with its cubic part
asymmetric). The corollary I asked to have refereed (`GT̂` proper in `GT̂₀`) uses the same two steps.

## Finding 4: the three lifts, the cartographic group, and the involution with `Δ = 1`

Scan 23: the inverse image of `{1, τ}` is `C_2 * C_2 * C_2` on `τ_0, τ_1, τ_∞`, with `l_0 = τ_∞τ_1`, `l_1 = τ_0τ_∞`,
`l_∞ = τ_1τ_0`. Scans 28 and 29: the three lifts belong to the three arcs of the real locus, and the other classes
give nothing new. This is LM4 D.34 for complex conjugation, as the intake says. The conjugacy criterion is right: an
involution `α` of `𝒫` is conjugate to complex conjugation exactly when its three section classes contain involutions
`t_0, t_1, t_∞` whose products are generators of the three inertia groups and which generate `F ⋊_α C_2`; a
surjection of the completed `C_2 * C_2 * C_2` onto it is then an isomorphism, because a surjective endomorphism of
`F` is bijective.

With my item T3 (hunch): the glued involution, complex conjugation on one side and a conjugate of it on the other,
is by LM4 D.34 conjugate to complex conjugation in every pro-`p` quotient, by conjugators that differ from prime to
prime. It is therefore exactly a candidate for which the map `ψ` of LM8_PUSH B.5 is not onto and the three lifts do
not generate. Two consequences, both mine:
- If the glued involution exists it has `Δ = 1`, so it is not conjugate to complex conjugation in `GT̂₀`; whether it
  is conjugate in `𝒫` is the generation question for its three lifts.
- A constraint on the construction: there is no element of `GT̂₀` that is "`γ` on one side, the identity on the
  other" for the `γ` of T3, because the glued element `σ₂` would be its commutator with complex conjugation and
  would have `Δ = 0`. So the product decomposition of E.58.2 cannot extend to elements whose multiplier is not one;
  T3 needs it only at multiplier one.

## Which of the proposals of 11.5 to make, and how

Each as statements to prove or refute. ANABELIAN_149_PUSH is not touched.

- **LM8_PUSH.**
  - (a) Attach cote 145 (scans 5 to 12, 22 to 29, 33 to 38) and cote 143 (scans 29 to 33): yes.
  - (b) Task C.7, with the corrected dictionary: "His pair `(γ, χ)` of cote 145, scan 11, is the pair `(f, λ)` up to
    the gauge `l_0^α g l_1^{−α}`, and it is injective on `Γ`. The frames of E.65 are the conjugators by which an
    element moves the canonical splittings over the isotropy groups at `P` and at the harmonic points (scans 22,
    28). Determine `β` of scan 11 from the relation of scan 12, and prove or refute `β = ρ_F` of E.61."
  - (c) Task C.8, a new sentence: "The conjecture of cote 143, scans 29 to 31, fails at type (0,3) in both written
    forms. Prove or refute: an element of `GT̂₀` that preserves the conjugacy classes of the sections of the
    harmonic and of the equianharmonic point has `Δ = 0`; an element of `C^φ` preserves them."
  - (d) Task B.5: add the cartographic group of scan 23, the generation criterion above, and the glued involution
    of Lead 23 as the case to decide.
  - (e) A result line for scan 24 only after the chain of finding 3 is refereed; until then a lead.
- **Successor of LM7_PUSH.** S.5 and S.8: the dictionary in its corrected form, not "the image of `γ` modulo 12".
  S.1: no new route comes from cote 145; drop "in his coordinates" as a route, keep it as notation.
- **LM6_POINTS_AS_SECTIONS.** Yes, cote 143, scans 2 to 12, and one new item from finding 1: "Determine the
  subgroup of `GT̂₀` that preserves the section classes of the points `1/2` and of a root of `λ² − λ + 1`; prove or
  refute that it lies in `ker Δ` and that it contains `C^φ`."
- **EXIT_TOWER, Part E.** Yes, in his words, as three statements: "`Autext(Γ_{g,ν}) = 1`" for the discrete group, to
  be decided type by type from the literature with the derivation; "`Γ → Autext(Γ̂_{g,ν})` is injective"; and "it is
  bijective onto the automorphisms commuting with `𝔖_ν` and preserving the inertia", which at (0,3) is false by
  finding 1 and for (0, ν ≥ 4) is the question whether Galois is `GT̂`. The automorphism group of the geometric
  modular topos as a fourth.
- **Tower and LM4 items** (`PUSH_ITEMS_20261114.md`). Item 2.3: the generation form, with the glued involution as
  the test case. Item 1.12: cote 145 as the origin of the splittings behind LM7 D.25, with the corrected dictionary.

## What I did not check

The transcriptions are first pass; several readings on the cited pages are marked unsure by the transcriber, among
them the word "strict" in the first margin of scan 29, which does not change the reading. Scans 8 to 10 and 12 of
cote 145 are unread, so `β` and his equation for the involutions are open points of the dictionary. LM4 D.76, D.77
and LM3 E.7, E.10 are cited from the intake and the handoff, not read. My context is at about 86 %.
