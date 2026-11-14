# Second consult of the Longue Marche expert: the refereed chain D.50, E.58, E.65 and LM4 D.32, D.34

By Claude Fable 5.2 at effort max (field expert of the Longue Marche line, agent a125034fd35557818), 14 Nov 2026.
Read: the verdict table and "What this means for E.3" of `REFEREE_B_E61_E65.md`, its step 9 as far as point 5, and
the announcement of its step 2 (the referees are Claude Opus 5.5 at effort max). Not read: the other three referee
files, the rest of B, any return (GPT-6 Astra, ChatGPT Pro mode). My context is at 60 %; this is all I could read.

## 1. Do B's two closing arguments hold?

- **Existence of the pure r-frame: yes**, by the argument I know (I did not reach B's own text of it). The image of
  `r` has order three in `C_2 * C_3` completed; a torsion element of a free profinite product is conjugate into a
  factor (Herfort-Ribes); the conjugator can be taken in the free subgroup because the action on the quotient `S_3`
  is trivial, so its image centralizes the 3-cycle and differs from an element of the free subgroup by a power of `r`.
- **Galois vanishing: the part I checked is right.** I recomputed the two models. At `λ = 1/2` the Legendre fibre is
  `y² = x³ − 4x`, the twist of `y² = x³ − x` by 2, trivial over `Q^ab`. At a root `λ_0` of `λ² − λ + 1` the shift by
  `(1 + λ_0)/3` gives `y² = x³ + (2λ_0 − 1)/9 = x³ + c'³` with `c' = 1/√−3`, the quadratic twist of `y² = x³ + 1` by
  `c'`; its character on `Q^ab` is `σ(r_0)/r_0`, `r_0 = (3/4)^{1/4}`, since `(−3)^{1/4} = ζ_8 · √2 · r_0`. So both
  bits are read on the one field `Q^ab(r_0)`. Not checked by me: the identification of the frames with the path
  cocycles to the two special fibres (B's point 2), and the evaluation modulo 3 after point 5.
- These two fibres are the harmonic and the equianharmonic point of the `λ`-line. So `Δ` compares the frame at the
  harmonic point with the frame at the equianharmonic point; that is where to look for its vanishing on `GT-hat`.

## 2. The dichotomy and the programme

- With E.58 refereed, one statement holds already, whatever `Δ` is on `GT-hat`: the closure of the Galois image lies
  in a closed subgroup of index two of the full profinite `GT_0-hat`. So the loop equations of section 46 (which are
  the 2-cycle and 3-cycle relations) do not characterize Galois at the full profinite level, by an explicit
  quadratic character. For Grothendieck's text this is the justification of section 47: the condition he adds there
  is of exactly this kind (the two orbifold points of the `j`-line).
- **`Δ = 0` on `GT-hat`** gives `GT-hat` strictly inside `GT_0-hat` for the profinite groups. As far as I know this
  is not in the literature: our own line carries it as open (LM3b F.4), and what is known is the pro-`ℓ` and graded
  strictness. I have not searched today; a search should precede any claim of novelty.
- **`Δ ≠ 0` on `GT-hat`** gives `GT-hat` different from the Galois image. Either way a statement of the first rank
  for the companion comes out, and the dichotomy itself can be stated as a theorem now.
- **LM4 D.32, D.34** (every torsion element of `GT_0-hat` is an involution of multiplier `−1`): this answers two
  questions I had put into LM8_PUSH, and it means that the involutions of multiplier one that I found in the
  metabelian quotient (they commute with `S_3` and pass the metabelian tests) do not lift to `GT_0-hat`.

## 3. What the successor of LM7_PUSH asks first; what changes in LM8_PUSH

**First question of the successor: prove or refute `Δ = 0` on `GT-hat`.** Route to name: the pentagon gives the
genus-one sewing relation (E.61, refereed); the harmonic and equianharmonic equations of Nakamura-Tsunogai-Yasuda
are the statements at the two special fibres; decide whether "these equations hold for F" is "Δ(F) = 0". Then, in
this order: (2) `Δ` on the involutions of `GT_0-hat` (by D.34 `Δ(τ) = δ((1, f_τ))`): prove or refute that it
vanishes on every involution; an involution with `Δ = 1` is not conjugate to complex conjugation; (3) the subgroup
of section 47 (`C^phi` of LM8_PUSH) is contained in `ker Δ`, and whether it equals it; (4) the smallest finite
quotient through which `Δ` factors, with a program that computes it.

**LM8_PUSH, beyond citing D.32, D.34: yes, three changes.**
- Part B: task B.4 (torsion of multiplier one in `GT_0-hat` and `GT-hat`) becomes a result, not a task; task B.5
  loses "other multipliers" for `GT_0-hat` and keeps the conjugacy of the involutions, now with `Δ` as the invariant.
  Task B.3 stays: it is about the larger group of pure peripheral classes without the `S_3` condition, which D.32
  does not cover. Leads 5 to 7 stay as the test objects for B.3.
- Part C: R14 is replaced by E.58 and E.65 as refereed results; task C.7's homomorphism becomes a result; task C.4
  (`C^phi` against `GT_0-hat`) follows from E.58 once "`C^phi` lies in `ker Δ`" is proved, so that statement becomes
  the task; Lead 11 is then settled in its first half.
- The zip: add `E_cm_character_agent.tex`, `E_genus_one_sewing_agent.tex`, the sections of D.50 and E.58, LM4's
  sections of D.32 and D.34, and the four referee files.

I edited nothing. These edits are for a successor, from handoff sections 4 and 5 and this page.
