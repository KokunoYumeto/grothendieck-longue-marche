# Prompt updates of 14 November 2026 (intake of the night of 13–14 November)
By Claude Fable 5.2 at effort high (intake agent), applied by `apply_prompt_updates_20261114.py` (exact replacements, each matched the stated number of times). Backups of the four prompts as they were: `PROMPT_before_intake_20261114.md` in each work folder. The returns cited are by GPT-6 Astra (ChatGPT Pro mode); every row is cited in the prompts as a claim. Where "old text" is an anchor, the new text keeps it and adds to it.

## LM8_PUSH

`C:\Users\user\Documents\longue_marche_pro_pilot_20261104\pro_prompts_draft_20261111\LM8_PUSH\PROMPT.md`

### 1. What is attached

**Comes from:** LM7_PUSH checkpoint 09; LM4 state 01:07 UTC; Fermat tower state 01:15 UTC; LM5 final return

**Old text:**

```
and the difference to its checkpoint of 13:42 UTC with the four new statements in full.
```

**New text:**

```
and the difference to its checkpoint of 13:42 UTC with the four new statements in full.
- `runs_in_progress_20261114/`: the later states, reviewed by no one beyond what R24–R26 say. The three runs LM7_PUSH, LM7_FERMAT_TOWER and LM4_FINITE_GROUP_ACTIONS have not ended and can no longer be reached. `LM7_PUSH_checkpoint_09/` (13 November 2026, 22:42 UTC): the register (218 statements: 207 proved, 7 refuted, 3 known, 1 open) and the sections `D_pronilpotent_lift_agent.tex` (D.50), `D_full_weight5_agent.tex` and `D_full_weight9_agent.tex` (D.1, D.2), `E_agent.tex` (E.1–E.3), `E_relative_cm_lift_agent.tex` (E.58), `E_genus_one_sewing_agent.tex` (E.61), `E_hyperelliptic_CM_agent.tex` (E.64), `E_cm_character_agent.tex` (E.65) and `E_orbifold_CM_agent.tex` (E.67). `LM4_state_20261114/` (14 November, 01:07 UTC): the register (270 statements) and the LaTeX of the paper. `LM7_tower_state_20261114/` (14 November, 01:15 UTC): the register of LM7_FERMAT_TOWER (226 statements) with the sections `D_cm_shadow.tex` (D.25) and `D_arithmetic_replacement.tex` (D.46). `LM5_return/`: the register, the report and `sections/F.tex` of LM5_MULTI_GALOIS_TOPOI (GPT-6 Astra, ChatGPT Pro mode; final return of 13 November 2026, marked INCOMPLETE; 129 statements).
```

### 2. Results this builds on, R14

**Comes from:** LM7_PUSH checkpoint 09 (D.1, D.2, E.2 now Proved there; E.3 Open)

**Old text:**

```
LM7_PUSH D.1, D.2, E.2, E.3 (the images of the full profinite groups) were open at its checkpoint 04.
```

**New text:**

```
LM7_PUSH D.1, D.2, E.2, E.3 (the images of the full profinite groups) were open at its checkpoint 04; its checkpoint 09 claims D.1, D.2 and E.2 and leaves E.3 open (R24).
```

### 3. Results this builds on, new R24–R26

**Comes from:** LM7_PUSH D.50, E.58, E.61, E.64, E.65, E.67; LM4 D.32, D.34, D.42, D.70, D.75, D.78; LM5 F.12, F.13, F.19, F.36, F.48, F.51

**Old text:**

```
does not lift to the integral `q₂` stage over `F₂[ε]`.
```

**New text:**

```
does not lift to the integral `q₂` stage over `F₂[ε]`.
- **R24** (LM7_PUSH checkpoint 09: D.50, E.58, E.61, E.65, with D.1, D.2, E.2; claims of GPT-6 Astra, ChatGPT Pro mode, 13 November 2026. Two intake readers, Claude Fable 5.2 at effort high, each read D.50 and E.58 once and found no error; one of them read E.65 and the first half of E.61, recomputed the finite matrix identities of E.58, E.61 and E.65 with its own program, and recomputed the two division fields behind LM7 D.25. A step-by-step referee check by Claude Opus 5.5 at effort max had been started when this was written; its result is not in this prompt. All of R24 is a claim: for each statement you use, give your own proof or the exact error.) Notation of LM7_PUSH: its `F` is `K₂`, with free generators `x = (sr)⁻²`, `y = sxs`; `τ = sr`; `R_nil(G)` is the intersection of the kernels of the continuous homomorphisms from `G` to finite nilpotent groups. *D.50.* Every continuous automorphism of `B̂/R_nil(K₂)` that sends `s`, `r`, `τ` to conjugates, with any three conjugators, lifts to a continuous automorphism of `B̂` with those conjugators lifted; the same for the free profinite group on two generators with its three peripheral classes. The proof is a count: for a finite extension `A → E → D` with `[E, A] = A`, the number of epimorphisms onto `E` above a map to `D`, with the three boundary values in prescribed `A`-classes, depends on the map to `D` only through its lifts to one finite central extension of `D`. Claimed consequences (D.1, D.2): for `ℓ ≥ 5` every pro-`ℓ` solution of the 2-cycle and 3-cycle relations with multiplier one whose pure map is an automorphism is the image of an element of `GT̂₀`; the image of the full profinite special group in weight five has dimension three, and `GT̂₀` reaches the second vector of weight nine. *E.58.* The same lifting for `B̂/R_nil(U)`, `U` any open normal subgroup of `B̂`. Applied to the identity of `B̂/R_nil(H)`, `H = K₂′K₂³`, with the conjugator of `r` taken in the centralizer of `r` in the 2-primary component: an element `(1, f)` of `GT̂₀` with `f ∈ R_nil(H)`, whose automorphism `Φ` of `B̂` fixes `τ` and has unique conjugators `A, β ∈ K₂` (`Φ(r) = ArA⁻¹`, `Φ(s) = βsβ⁻¹`; uniqueness from Herfort–Ribes 1985, Theorem B′: `C_B̂(r) = ⟨r⟩`, `C_B̂(s) = ⟨s⟩`) with images `[5I]` and `1` in `SL₂(Z/12)/±1`. Its pair `(T, W)` lies in the coset that Galois misses (E.2). *E.61.* For every element of `GT̂₀` of multiplier one, with `ρ` defined by `(β⁻¹)^ab = (ρ, ρ)`: the image of `f` under `x ↦ (1 2; 0 1)`, `y ↦ (1 0; −2 1)` modulo 12 is `(1 −8ρ; −8ρ 1+64ρ²)`. *E.65.* On the multiplier-one subgroup of `GT̂₀` the coordinates `T` (in the centralizer of `R₀ = (0 −1; 1 −1)` in `SL₂(F₃)`, cyclic of order six) and `W` (in the centralizer of `S = (0 1; −1 0)`, cyclic of order four) are continuous homomorphisms; the sum `δ` of the sign of `T` on the line `F₃·(1, −1)` and of the class of `W` modulo `±1` is a continuous character with values in `F₂`, invariant under conjugation by `GT̂₀`; it vanishes on `G_{Q^ab}` (both bits are the action on `(3/4)^{1/4}`, by LM7 D.25) and extends uniquely to a continuous character `Δ : GT̂₀ → F₂` that vanishes on `G_Q`; `Δ = 1` on the element of E.58. So the index-two condition of R14 is `ker Δ`, a closed subgroup of index two of `GT̂₀` that contains the Galois image. LM7_PUSH E.3, open there: the value of `Δ` on `GT̂`. LM7_PUSH E.64, E.67 (statement level): on `GT̂` the character is a sum of three bits read from the hyperelliptic quotient of `B̂₄` and the two CM triangle groups.
- **R25** (LM4_FINITE_GROUP_ACTIONS, state of 14 November 2026: D.32, D.34, D.42, D.70, D.75, D.78; Proved there; no proof of any row of LM4 has been read by a reviewer). LM4's `P` is the group of outer automorphisms of `F` preserving the three procyclic conjugacy classes of `x`, `y`, `z`, with one common multiplier: compare it with `𝒫` before use. D.32, D.34: every finite subgroup of `P` maps injectively to `{±1} ⊂ Z₂^×` by the 2-adic multiplier; every non-trivial element of finite order of `P` is an involution whose multiplier is the global `−1 ∈ Ẑ^×`; so the multiplier-one subgroup of `P`, and that of `GT̂₀`, are torsion-free. For such an involution, normalized as `α(x) = x⁻¹`, `α(y) = f⁻¹y⁻¹f`, there is `h ∈ F′` with `f = h⁻¹α(h)`, and `x ↦ x, y ↦ hyh⁻¹` induces an automorphism of every `F^(p)`; that it is onto `F`, and that `α` is conjugate to complex conjugation, are not claimed. D.42: with the permutations of the punctures allowed, every element of order three has multiplier 1. D.70: in the peripheral outer group of the once-punctured torus every element of order four has multiplier 1. D.75, D.78: for a negative involution of the punctured torus the fixed subgroups of the cusp reflections are trivial and the transporter is unique; the other fixed subgroup is `K ⋊ Ẑ` with `K` pro-odd, and `K = 1` is not decided. Open in LM4 (D.12): whether every torsion element of `GT̂₀` is conjugate to complex conjugation.
- **R26** (LM5_MULTI_GALOIS_TOPOI, final return of 13 November 2026: F.12, F.13, F.19, F.36, F.48, F.51; Proved or Refuted there; reviewed by no one). F.12: classical punctured neighbourhoods form a pro-topos; its covering germ is `BZ^r`; the inverse 2-limit of the full sheaf topoi of the shrinking neighbourhoods is degenerate (LM8 E.11 again). F.36: the limit of the coherent étale topoi of the punctured neighbourhoods of a point of a smooth curve over an algebraically closed field of characteristic 0 is `BẐ(1)`. F.48: the rank-one normal-direction functor is the sector-filter functor of §53, and its finite completion agrees with the tangential fibre functors (that run inspected scans 242, 243, 256, 259–262). F.13, F.19: the gluing theorems and the tangential equivalence hold for spaces and for étale stacks with a proper presentation or with explicit common-stage control. F.51 (Refuted there): for an étale stack with a non-proper presentation, germs formed chart by chart need not descend to the neighbourhood pro-topos (all roots of unity acting on a disc; a free action as well), and for `Z` acting on `P¹` by `z ↦ z/(1 + z)` the equivalence between covering germs and the punctured normal stack fails.
```

### 4. Leads, Lead 11

**Comes from:** LM7_PUSH E.65

**Old text:**

```
Then an element of `GT̂₀` in the coset that Galois misses lies outside `C^φ`. No expectation.
```

**New text:**

```
Then an element of `GT̂₀` in the coset that Galois misses lies outside `C^φ`. No expectation. LM7_PUSH E.65 (R24) claims that the condition is the kernel of one continuous character `Δ` of `GT̂₀`; with it this Lead reads `C^φ ⊆ ker Δ`.
```

### 5. Part B, opening

**Comes from:** LM4 D.32, D.34, D.42

**Old text:**

```
(R22); this Part is the tripod.
```

**New text:**

```
(R22); this Part is the tripod. LM4 D.32, D.34 and D.42 (R25) claim answers to task 3, to task 4 for `GT̂₀` and to the multiplier statement of task 5; they are claims, with their proofs in `runs_in_progress_20261114/LM4_state_20261114/`.
```

### 6. Part B, task 3

**Comes from:** LM4 D.32, D.34; LM7_PUSH D.50

**Old text:**

```
beginning with those where 5 divides the order of `F/V` and `p ≠ 5`.
```

**New text:**

```
beginning with those where 5 divides the order of `F/V` and `p ≠ 5`. LM4 D.32 and D.34 (R25) claim that `𝒫₁` is torsion-free, through the 2-adic multiplier: give your own proof of the statement they rest on, or the exact error. If they hold, `φ₀` has no lift of finite order; then exhibit the finite quotient above, and decide whether `φ₀` lifts to an element of `𝒫₁` of infinite order (the lifting theorem D.50 of R24 concerns `F/R_nil(F)`, of which `M` is not a quotient: prove what it gives for `φ₀` and what it does not).
```

### 7. Part B, task 4

**Comes from:** LM4 D.34; LM7_PUSH E.65

**Old text:**

```
4. Prove or refute: `GT̂₀` has a non-trivial element of finite order with `λ = 1`. The same for `GT̂`.
```

**New text:**

```
4. Prove or refute: `GT̂₀` has a non-trivial element of finite order with `λ = 1`. The same for `GT̂`. (LM4 D.34, R25, claims there is none.) For every element of finite order of `GT̂₀`, of any multiplier, compute `Δ` of R24: `Δ` is invariant under conjugation and vanishes on complex conjugation, so an involution with `Δ = 1` is not conjugate to it.
```

### 8. Part B, task 5

**Comes from:** LM7_PUSH E.65; LM4 D.12

**Old text:**

```
which finite subgroups of `𝒫` exist, up to conjugacy.
```

**New text:**

```
which finite subgroups of `𝒫` exist, up to conjugacy. Prove or refute: `Δ` (R24) vanishes on every element of finite order of `GT̂₀`; this is a necessary condition for LM4 D.12 (R25).
```

### 9. Part C, task 5

**Comes from:** LM7_PUSH D.50

**Old text:**

```
and the same with `GT̂` in place of `GT̂₀`.
```

**New text:**

```
and the same with `GT̂` in place of `GT̂₀`. LM7_PUSH D.50 (R24) claims that the first projection is onto the multiplier-one solutions whose pure map is an automorphism: confirm it by your own proof or give the exact error, then use it.
```

### 10. Part C, task 7

**Comes from:** LM7_PUSH E.65, E.61; LM7 D.25

**Old text:**

```
7. Prove or refute Lead 11. Prove or refute that `(T, W)` is a homomorphism on `GT̂₀`.
```

**New text:**

```
7. Prove or refute Lead 11. Prove or refute that `(T, W)` is a homomorphism on the multiplier-one subgroup of `GT̂₀`, and that `Δ` of R24 is a continuous character of `GT̂₀` that vanishes on `G_Q`. LM7_PUSH E.65 claims both: give your own proof, or the exact step of E.65 that fails. Begin with E.61 and with the statement on which the vanishing rests: on `G_{Q^ab}` the conjugators of `r` and of `s` in `K₂` give the representations on the torsion of `y² = x³ + 1` and of `y² = x³ − x` (LM7 D.15–D.17, D.25; Nakamura–Tsunogai and its sequels), with the signs.
```

### 11. Part C, new task 8

**Comes from:** LM7_PUSH E.58, E.64, E.65, E.67 (E.3 Open there); consultation of the Longue Marche expert, 14 Nov

**Old text:**

```
for the automorphism of LM7 D.46 (R14) and for LM2 C.d5.
```

**New text:**

```
for the automorphism of LM7 D.46 (R14) and for LM2 C.d5.
8. Prove or refute: `C^φ ⊆ ker Δ`. Then prove or refute: `C^φ = ker Δ`. With the element of LM7_PUSH E.58 (R24: confirm its construction by your own proof or give the exact error) the first inclusion settles task 4; with task 3 it gives `Δ = 0` on `GT̂`, which is LM7_PUSH E.3. Prove or refute `Δ = 0` on `GT̂` directly as well: from the pentagon in a quotient of the five-point group in which both coordinates are read; from the harmonic and equianharmonic equations and relation (III′) of task 2, deciding whether they hold for `F` exactly when `Δ(F) = 0`; and from the comparison characters of LM7_PUSH E.64 and E.67. A value `Δ = 1` on an element of `GT̂` gives a continuous quadratic character of `GT̂` that is trivial on `G_Q`, hence an element of `GT̂` outside the Galois image: write every step of such a proof out in full.
```

### 12. Part F, opening

**Comes from:** LM5 F.12, F.13, F.19, F.36, F.48, F.51

**Old text:**

```
**F. The limit topos of §53.5 (LM8 E.11; scans 242–243).**
```

**New text:**

```
**F. The limit topos of §53.5 (LM8 E.11; scans 242–243).** LM5 F.12, F.36 and F.48 (R26) claim task 2 and one reading of task 3; LM5 F.13, F.19 and F.51 (R26) bear on the statements of Lead 21 for étale stacks. They are unreviewed: for each one you use give your own proof or the exact error, and carry the tasks beyond them.
```

### 13. What the outcome must be, point 3

**Comes from:** new R24–R26

**Old text:**

```
proving R1–R23 again in place of the tasks
```

**New text:**

```
proving R1–R26 again in place of the tasks
```

## LM6_POINTS_AS_SECTIONS

`C:\Users\user\Documents\longue_marche_pro_pilot_20261104\pro_prompts_draft_20261111\LM6_POINTS_AS_SECTIONS\PROMPT.md`

### 14. third block (LM7_FERMAT_TOWER), after Task LM7-E.23

**Comes from:** Fermat tower state 14 Nov 01:15 UTC: E.37, E.38, E.41, E.43, E.44, E.61, E.66, E.73, E.93, E.96, E.98–E.100, E.102–E.117, E.122; open E.23; E.102 formula check

**Old text:**

```
Where a task below concerns sections of Fermat curves or of the torus, or the passage from finite to continuous coefficients, start from these statements.
```

**New text:**

```
Where a task below concerns sections of Fermat curves or of the torus, or the passage from finite to continuous coefficients, start from these statements.

**The same run since then.** It did not end and can no longer be reached. Its state of 14 November 2026, 01:15 UTC (226 statements: 202 proved, 12 known, 9 refuted, 3 open) is attached as `LM7_tower_state_20261114/`: the register, the report and the sections of Part E. Rows E.37–E.89 were read by one intake reader (Claude Fable 5.2 at effort high) at the level of statement, a part of them with their proofs; the later rows at the level of statement only. Every row cited here is a claim: for each one you use, give your own proof or the exact error.

- The first case of Task LM7-E.23 is claimed: E.37 gives the whole section map of the intrinsic class-two pro-3 quotient, which abelian classes lift and every fibre (E.93, E.96 complete it).
- E.38, E.43: class two does not select: for a set of primes of density 1/9 there are classes with class-two sections and none one layer up. E.44: the lifting criterion at every layer, with the Frobenius action as arithmetic input.
- E.41: every section unramified outside 3 of the full pro-3 group, of its metabelian and of its marked quotient (free ranks 6, 24, 166). E.98–E.100, E.104: all sections unramified outside `{2, 3}`, outside `{3, 7}`, and for two families of pairs `{3, ℓ}`.
- E.61, E.66: at a place not above 3 a ramified local section is one of nine cusp families. E.73: a global section is a family of local packets tied together by Frobenius words.
- E.102: the degree-four unramified kernel from the full to the metabelian group is `Z_3^504 ⊕ C_3^144 ⊕ C_9^56 ⊕ C_27^30 ⊕ C_81^9`. Two readers on our side recomputed it with their own code (Claude Opus 5.5 at effort max; Claude Fable 5.2 at effort max). The second derived it from the Galois module of the homology of the cubic minus its nine flexes, a core of rank four and six copies of the cyclotomic character, which gives the coefficients of the class-three step as four modules of ranks 20, 16, 4 and 1 (`E102_check/FORMULA.md`, attached; tested against 28 direct computations; no second reader).
- E.107, E.110, E.111, E.114, E.116, E.122: the 3-primary class groups (ordinary or `S`-class groups, as each row states) in the radical towers `Q(ζ_{3^j}, (ℓζ_{3^j})^{1/3^m})` vanish at every level for `ℓ = 17` and for every inert `ℓ ≡ 2, 5 (9)`; the complete global section sets of the inherited quotient `H` on the lines of `κ(17)` and `κ(ℓ)` follow; at 53 the positional tower is computed at every level.
- The plus Fermat quartic (elliptic factor `y² = x³ + x`). E.103, E.105, E.108: its abelian sections, their class-two lifts, 55 peripheral cup tests. E.109: the pro-5 class-two outer action is carried by a rank-two CM module whose class restricts over `Q(ζ_8)` to the Abel–Jacobi class of the Ceresa cycle. E.113: the global integral Weil cup vanishes at every prime; the remaining obstruction target has rank 127. E.115, E.117: the complete class-two section image at 5 and at 3 with every fibre; every input unramified outside `{2, 5}`, respectively `{2, 3}`, lifts; for unrestricted inputs the local Kummer orders are unbounded, and there are liftable inputs whose sum does not lift.

**Task LM7-E.23 as it now stands** (the run's own E.23): (i) the image and every fibre of the class-three map `Sect((N/γ_4N) ⋊ G_Q)/N → Sect((N/γ_3N) ⋊ G_Q)/N`, `N = π_1(U_{3,Q̄})^{(3)}`, for every input, with E.44 as the criterion; (ii) the passage from the sections of `H` to those of the intrinsic metabelian and marked depth-two quotients, through the quotient of E.38, as one theorem for every first class (E.111, E.114 and E.116 all stop at that step); (iii) the coefficient primes other than 3 and the mixed finite quotients, that is, the full profinite metabelian quotient; (iv) for the quartic, the law of the local Kummer orders and of the failure of additivity in E.115 and E.117. Done when (i)–(iv) are theorems with proofs.
```

### 15. Part E (b)

**Comes from:** Fermat tower E.24–E.122

**Old text:**

```
prove how this compares with Kim's method for the same curves.
```

**New text:**

```
prove how this compares with Kim's method for the same curves. For `n = 3` and `n = 4` the rows E.24–E.122 of LM7_FERMAT_TOWER (third block) compute much of this: confirm what you use, and carry (b) on from Task LM7-E.23 (i)–(iv).
```

### 16. new fifth block, before 'What the outcome must be'

**Comes from:** LM5 F.3–F.7, F.21–F.23, F.35, F.37, F.39, F.44, F.47–F.50; LM7_PUSH checkpoint 09 Part A; cote 148 scan 43

**Old text:**

```
## What the outcome must be
```

**New text:**

```
## New since this prompt was drafted, fifth block: LM5_MULTI_GALOIS_TOPOI, LM7_PUSH, cote 148 (added 14 November 2026)

LM5_MULTI_GALOIS_TOPOI (§§1–4, 14, 16, 20 of this manuscript and the topoi of cotes 149 and 147) returned on 13 November 2026 (GPT-6 Astra, ChatGPT Pro mode; 129 statements: 94 proved, 29 refuted, 4 known, 2 open; marked INCOMPLETE). It is reviewed by no one; one intake reader (Claude Fable 5.2 at effort high) read its report, the statement of every row of its Part F and the first step of the proof of F.47. Attached in `LM6_POINTS_AS_SECTIONS_new_results.zip`, folder `LM5_return/`: the register, the report and `sections/F.tex`. What bears on points as sections, each a claim to confirm where you use it:

- Cote 149, scan 52. F.3, F.4: `X ↦ X_ét` is faithful on reduced schemes locally of finite presentation over a locally noetherian base, in every characteristic. Call a morphism of étale topoi over `BG_k` pinned when it is given with its commutation isomorphism over `BG_k`. F.5, F.6, F.37, F.49: fullness fails without the pinning, and with it over algebraically closed fields, over every algebraic extension of a finite field, and over every infinite perfect field whose absolute Galois group has non-trivial centre (real closed fields among them). F.47, F.50: over every subfield `k` of a finitely generated extension of `Q^ab`, pinned morphisms between the étale topoi of finite-type `k`-schemes come from morphisms of schemes after absolute weak normalization. F.44 (Open there): the same question for `G_m` over the maximal solvable extension of `Q`. This is the state of (F1) of Part F for the functor `X ↦ X_ét`; it does not decide (F1) for fundamental groups.
- F.21: the arithmetic normal tube has the geometric profinite homotopy sequence, which begins with a Chern transgression; injectivity of the full global inertia forces left exactness. F.22 (Refuted there): the inertia kernel is not the same for every finite root stack. F.23: for the cusp `y² = x³ + t` stable reduction gives a quotient-stack boundary with injective meridian. F.35: a profinite local inertia map is injective if and only if every finite covering germ embeds as an open and closed sub-germ of the restriction of a global finite étale covering. F.39: horizontal inertia and the recursively compatible full inertia of a stable or toroidal tower inject, discretely and profinitely, with the cyclotomic action. These bear on Part B (the sections at a cusp) and on Part F (f), (g).
- F.48 compares F.39 with CYCLOTOMIC_KERNEL B5 and C8. The comparison with FLAGGED_149 was not made there (that return was not in the run's material; it is in this prompt's, second block): its statements C1–C6, C8, C9, which answer the flagged items F11–F16, are the ones to set beside F.21–F.23, F.35 and F.39.

LM7_PUSH, the follow-up to LM7_FERMAT_TOWER, has not ended and can no longer be reached; its checkpoint 09 (13 November 2026; 218 statements) is attached as `LM7_PUSH_checkpoint_09/`: the register and the sections of its Part A. Part A (A.1–A.44) continues §51.16. No reader on our side has read it: its rows are claims.

Cote 148 of the Montpellier archive, scans 29–72 (first-pass transcription by GPT-6 Astra, ChatGPT Pro mode, finished 14 November 2026; no second pass; attached as `MPL_148_029-072_transcription.tex` with its notes and doubts). On scan 43, in a table of "les divers avatars principaux de la Tour de Teichmüller", beside the topological, the complex-algebraic and the combinatorial one, stands `𝕋_{Q̄-alg}`, "cas `Q̄`-alg.", with a parenthesis read as "pour y obtenir des sections Gal/Q"; both halves of that parenthesis are marked doubtful by the transcriber. In Part B, state the assertion about sections that this entry makes when read so, in the terms of scans 61–65 of cote 140-2, and prove or refute it.

## What the outcome must be
```

## EXIT_TOWER

`C:\Users\user\Documents\grothendieck_archive_montpellier\pro_prompts_archive_20261112\EXIT_TOWER\PROMPT.md`

### 17. Added 13 November 2026: two items of the expert conference, Lead 6 added task

**Comes from:** LM5 F.40, F.41, F.42

**Old text:**

```
decide it for `(P¹, {0, 1, ∞})` and for `M̄_{0,5}` with its boundary.
```

**New text:**

```
decide it for `(P¹, {0, 1, ∞})` and for `M̄_{0,5}` with its boundary. The return LM5_MULTI_GALOIS_TOPOI (block of 14 November below) claims the answer in its F.40–F.42: invariance under proper modifications holds on the non-archimedean and on the archimedean side, so the failure expected here is refuted (F.41); properness cannot be dropped, already for `G_m` (F.40); both examples are computed (F.42). Confirm each by your own proof or give the exact error, and prove what follows for Lead 6.
```

### 18. new block, before 'What the outcome must be'

**Comes from:** LM5 F.8–F.11, F.13, F.15–F.20, F.24, F.25, F.39, F.42, F.43, F.51; cote 148 scans 29–72 (scans 31–36, 41, 43–68)

**Old text:**

```
## What the outcome must be
```

**New text:**

```
## Added 14 November 2026: the return LM5_MULTI_GALOIS_TOPOI and cote 148, scans 29–72

**LM5_MULTI_GALOIS_TOPOI** (GPT-6 Astra, ChatGPT Pro mode; final return of 13 November 2026, marked INCOMPLETE; 129 statements; reviewed by no one; one intake reader, Claude Fable 5.2 at effort high, read its report and the statement of every row of its Part F). Its Part F treats cote 147, §§11–13 (scans 106–190), the sections that follow those of this prompt, and answers the six tasks added to its prompt after the return EXIT_ONE_TYPE. Attached as `LM5_return/`: the register, the report and `sections/F.tex`. Its statements are claims: for each one you use, give your own proof or the exact error.

- F.8–F.10, F.24, F.25. A finite filtered topos with discrete multi-Galois strata with finitely many components and accessible left-exact gluing is an EI presheaf topos compatible with the filtration if and only if all gluing functors preserve products. The exit Hom-sets are crossing double cosets, with composition from full flags. Finite tame constructible étale sheaves are the continuous finite representations of the completed exit category, and the product criterion does not extend unchanged to profinite strata. The connected components of the analytic incidence category do not form a category (F.25, Refuted there).
- F.11 (Refuted there): axiom (174)c does not imply that the analytic flag category is thin (scans 114–121).
- F.15–F.18 (scan 152). Depths 1 and 2 of formula (246) do not compute the fundamental groupoid of the punctured boundary for every normal crossings pair: at a triple crossing the truncated diagram gives `Z⁴` and the full link `Z³`. Depth `k + 2` with all flags is the sharp uniform bound for the `k`-type. The corrected (247) computes `Π₁(X^*)`, not `Π₁(X)`. (254) is the curve case of a pro-topos pushout in every dimension. Part D (a) starts from these.
- F.20 (Refuted there): an invariant normal line need not admit an equivariant tubular embedding for analytic multiplicities (scan 146). F.13, F.19, F.51: the gluing theorems and the tangential equivalence hold for étale stacks with a proper presentation or with common-stage control; for a non-proper presentation, germs formed chart by chart need not descend (F.51; `Z` acting on `P¹` by `z ↦ z/(1 + z)`). Where you apply them to `M̄_{g,n}`, prove that the hypothesis holds.
- F.39: horizontal inertia and the recursively compatible full inertia of the stable tower inject, discretely and profinitely, with the cyclotomic action and the normalization by the contact matrix. F.42: the boundary graph of `M̄_{0,5}`, its intersection matrix and its fifteen primitive pairs of meridians. F.43: for `M̄_{0,5}` the strict profinite exit category classifies the constructible étale sheaves with `π`-finite values. Part E, and Part C (c) for 5 → 4, start from these.

**Cote 148, scans 29–72** (first-pass transcription by GPT-6 Astra, ChatGPT Pro mode, finished 14 November 2026; no second pass; attached as `MPL_148_029-072_transcription.tex` with its notes and doubts; the leaf of scan 41 is dated "Oct. 4 83"). It holds a finite model for five points, of the kind of Part B.

- Scans 31–33: a diagram of configurations of five points with "542 sommets, se partageant entre 9 orbites" and "1620 flèches" in 14 orbits under the symmetric group; the arrows are twists (`τ`) and erasures (`γ`, "gommage"). Then: "Programme de travail : 1) déterminer un syst. fondamental de relations entre les 1620 flèches du diagramme", with the margin "en particulier, écrire toutes les flèches comme composés de flèches « provenant de la dimension relative ≤ 1 »". Several readings on these scans are marked doubtful (the total 1620 replaces a struck 1500).
- Scans 34–36: "Systèmes spéciaux de cinq points sur une sphère complexe": the configurations with a non-trivial automorphism, classified by the largest order `ν` of an element, `2 ≤ ν ≤ 5`; `ν = 5` is the orbit of `μ₅`, with group `𝔻₅` ("structure pentagonale"); then the real structures, by the number of fixed marked points.
- Scans 43–68: the "avatars" of the tower (topological, complex-algebraic, `Q̄`-algebraic, combinatorial) and the Teichmüller groupoids `𝒯^+_top`, `𝒯^±_top` and the "spécial dévissé" one, with their operations, of which "D) Opération de recollement. C'est la plus cruciale, la moins tautologique peut-être de toutes".

This counts as a numbered task of Part B. **Part B, added task (d).** From his definitions on scans 31–33, define the diagram for five points. Prove or correct the counts 542, 9, 1620 and 14. Prove or refute that it presents the exit category of `M̄_{0,5}` (or the Teichmüller groupoid of five points) in the sense of (a), (b), with the comparison functor; in the case of a refutation, prove what it presents. Carry out his programme 1): a fundamental system of relations among the arrows, with the proof that it is one, and the expression of every arrow through those that come from relative dimension at most one.

## What the outcome must be
```

### 19. Part B, 'Done' line

**Comes from:** cote 148 scans 31–33 (added task (d))

**Old text:**

```
Done for Part B: (a), (b) theorems; (c) two cases written out in full.
```

**New text:**

```
Done for Part B: (a), (b) theorems; (c) two cases written out in full; (d) a theorem with its proof and its computation, with code.
```

## ANABELIAN_149_PUSH

`C:\Users\user\Documents\grothendieck_archive_montpellier\pro_prompts_archive_20261112\ANABELIAN_149_PUSH\PROMPT.md`

### 20. opening paragraph ('To be settled')

**Comes from:** LM5 F.44, F.45

**Old text:**

```
once FLAGGED_149 had proved its main theorem. First of all:
```

**New text:**

```
once FLAGGED_149 had proved its main theorem, and (added 14 November 2026) what the return LM5_MULTI_GALOIS_TOPOI left undecided on scan 52 of cote 149. First of all:
```

### 21. What is attached

**Comes from:** LM5 final return

**Old text:**

```
**`CYCLOTOMIC_REVIEW.md`**: its review (Claude Opus 5.5, effort max, 12 November 2026).
```

**New text:**

```
**`CYCLOTOMIC_REVIEW.md`**: its review (Claude Opus 5.5, effort max, 12 November 2026).
- **`LM5_return/`**: from the return LM5_MULTI_GALOIS_TOPOI (GPT-6 Astra, ChatGPT Pro mode; final return of 13 November 2026, marked INCOMPLETE; 129 statements; reviewed by no one): `LM5_MULTI_GALOIS_TOPOI_results.csv`, `LM5_MULTI_GALOIS_TOPOI_report.md`, `LM5_MULTI_GALOIS_TOPOI_references.bib` and `sections/F.tex` (its Part F, on cotes 149 and 147). Its statements are cited as LM5-‹id›.
```

### 22. Results this builds on, new R27

**Comes from:** LM5 F.3–F.7, F.37–F.39, F.44–F.50

**Old text:**

```
## Leads
```

**New text:**

```
**For Part F (scan 52).**
- **R27** (LM5-F.3 to F.7, F.37, F.38, F.46 to F.50: Proved, Refuted or Known there; LM5-F.44, F.45: Open there. The return is reviewed by no one. One intake reader, Claude Fable 5.2 at effort high, read the statements and followed the integrality lemma that opens the proof of F.47, finding no error; the rest of the proofs is unread.) On scan 52 he asks for the faithfulness of `X ↦ X_ét`. F.3, F.4: the functor is faithful on reduced schemes locally of finite presentation over a locally noetherian base, in every characteristic. Call a morphism of étale topoi over `BG_k` *pinned* when it is given with its commutation isomorphism over `BG_k`. F.5: without the pinning fullness fails, also after inverting universal homeomorphisms. F.6, F.37, F.49: pinned fullness fails over algebraically closed fields, over every algebraic extension of a finite field, and over every infinite perfect field whose absolute Galois group has non-trivial centre (real closed fields among them). F.38 (Known there, from Carlson–Haine–Wolf 2024; not opened by us): pinned reconstruction over sub-`p`-adic fields. F.46, F.47, F.50: for every subfield `k` of a finitely generated extension of `Q^ab` and all finite-type `k`-schemes `X, Y`, the map `Hom_k(X^awn, Y) → π₀ Hom^pin_{BG_k}(X_ét, Y_ét)` is bijective (`X^awn` the absolute weak normalization). The proof goes through the integrality of Kummer exponents (Amoroso–Zannier 2000, Theorem 1.1; Tsujimura 2022, Proposition 4.9: `(F₀Q^ab)^×/μ_∞` is free abelian for a number field `F₀`), the injectivity of the Kummer map of abelian varieties over `F₀Q^ab` (Tsujimura 2020, Theorem 3.1), transverse curves, and the criterion of Carlson–Haine–Wolf, Theorem 4.18. F.44: over `Q^solv` the multiplicative group of the field is divisible and the 2-power torsion of elliptic curves is rational, so both inputs fail; the central twists and the semilinear automorphisms of F.49 are excluded there, because the centralizer of `G_{Q^solv}` in `G_Q` is trivial; Mochizuki 2006, Theorem 2.5, concerns quotient groups and isomorphisms. F.45: that run did not have FLAGGED_149. It proved its own statement on the inertia of the stable tower (F.39: horizontal inertia and the recursively compatible full inertia inject, discretely and profinitely, with the cyclotomic action and the normalization by the contact matrix; with F.21 to F.23) and compared it with CK-B5 and CK-C8 (F.48); the comparison with FLAGGED_149 is not made. The flagged items F11 to F16 that its prompt named are answered in FLAGGED_149 by F149-C1 to F149-C6, F149-C8 and F149-C9; our search of that register found no row with the tag F25.

## Leads
```

### 23. Parts, new Part F

**Comes from:** LM5 F.44, F.45, F.47, F.50; FLAGGED_149 C1–C6, C8, C9

**Old text:**

```
Done for Part E: each of E1–E3 is (a) or (b).
```

**New text:**

```
Done for Part E: each of E1–E3 is (a) or (b).

**Part F. Schemes from their étale topoi (scan 52; LM5-F.44, LM5-F.45; added 14 November 2026).** Notation of R27.
- **F1.** Prove or refute LM5-F.50: pinned reconstruction for finite-type schemes over every subfield of a finitely generated extension of `Q^ab`. The return's proof is attached (`LM5_return/sections/F.tex`, F.46, F.47, F.50). A proof here is your own complete proof, with Carlson–Haine–Wolf, Tsujimura and Amoroso–Zannier opened and each cited statement quoted; a refutation names the step that fails and proves the strongest true statement. Determine whether F.47 or F.50 is in the literature, with the reference.
- **F2.** Prove or refute: every non-constant pinned endomorphism of the étale topos of `G_m` over `Q^solv` is induced by an algebraic morphism (LM5-F.44). Then determine the fields `k` of characteristic 0 over which pinned reconstruction holds for all finite-type `k`-schemes: a criterion on `k`, proved in both directions, that contains F.50 and the failures of F.49.
- **F3.** The comparison that LM5-F.45 leaves. Set F149-C1 to F149-C6, F149-C8 and F149-C9 beside LM5-F.21 to F.23, F.35, F.39 and F.48 and CK-B5, CK-C8. For the cyclotomic normalization of inertia, state and prove one theorem that contains the statements of the three returns, or prove the exact place where they differ. For each of the eight rows of FLAGGED_149, prove or refute that it asserts a converse (a characterization of the sections of points or of cusps by their inertia) that LM5-F.39 does not give, and decide each such converse.
Done for Part F: each of F1–F3 is (a) or (b).
```

### 24. What the outcome must be, point 1

**Comes from:** new Part F

**Old text:**

```
one line for each item A1, A2, B0–B14, C1–C4, D1–D5, E1–E3 and each statement lead L1–L10
```

**New text:**

```
one line for each item A1, A2, B0–B14, C1–C4, D1–D5, E1–E3, F1–F3 and each statement lead L1–L10
```

### 25. What the outcome must be, point 3

**Comes from:** new R27

**Old text:**

```
proving R1–R26 again in place of the items
```

**New text:**

```
proving R1–R27 again in place of the items
```

### 26. What to deliver

**Comes from:** new R27

**Old text:**

```
the corrections to R1–R26, to the leads
```

**New text:**

```
the corrections to R1–R27, to the leads
```

## Files each background zip must gain or lose (the main session rebuilds the zips; none was rebuilt here)

Sources: `A = C:\Users\user\Documents\longue_marche_pro_pilot_20261104\answers`.

**LM8_PUSH** (`LM8_PUSH_background.zip`). Gains a folder `runs_in_progress_20261114/` with:
- `LM7_PUSH_checkpoint_09/`: from `A\LM7_PUSH_checkpoint_09_20261113T2242Z_unzipped\LM7_PUSH\`: `LM7_PUSH_results.csv`
  and `sections\` `D_pronilpotent_lift_agent.tex`, `D_full_weight5_agent.tex`, `D_full_weight9_agent.tex`,
  `E_agent.tex`, `E_relative_cm_lift_agent.tex`, `E_genus_one_sewing_agent.tex`, `E_hyperelliptic_CM_agent.tex`,
  `E_cm_character_agent.tex`, `E_orbifold_CM_agent.tex` (and `LM7_PUSH_references.bib`).
- `LM4_state_20261114/`: from `A\LM4_FINITE_GROUP_ACTIONS_20261114T0107Z_unzipped\`: `LM4_FINITE_GROUP_ACTIONS_results.csv`,
  `LM4_FINITE_GROUP_ACTIONS_paper.tex`, `LM4_FINITE_GROUP_ACTIONS_references.bib`, `DIFF_vs_T2315Z.txt`.
- `LM7_tower_state_20261114/`: from `A\LM7_FERMAT_TOWER_20261114T0115Z_unzipped\LM7_FERMAT_TOWER\`:
  `LM7_FERMAT_TOWER_results.csv`, `sections\D_cm_shadow.tex`, `sections\D_arithmetic_replacement.tex`.
- `LM5_return/`: from `A\LM5_MULTI_GALOIS_TOPOI_final_20261113T2351Z_unzipped\`: `LM5_MULTI_GALOIS_TOPOI_results.csv`,
  `LM5_MULTI_GALOIS_TOPOI_report.md`, `LM5_MULTI_GALOIS_TOPOI_references.bib`, `sections\F.tex`.
Loses nothing (the older `runs_in_progress/` is still cited by R14, R22, R23 and Lead 20). When the referee reports
on D.50, E.58, E.65 exist, add them as `LM7_PUSH_referee/` and replace the sentence in R24 that says the check was
under way. No PDF goes in.

**LM6_POINTS_AS_SECTIONS** (`LM6_POINTS_AS_SECTIONS_new_results.zip`). Gains:
- `LM7_tower_state_20261114/`: `LM7_FERMAT_TOWER_results.csv`, `LM7_FERMAT_TOWER_report.md` and every `sections\E*.tex`
  from the tower folder above.
- `E102_check/FORMULA.md` from `C:\Users\user\Documents\LM7_FERMAT_TOWER_E102_check_20261113\FORMULA.md` (the path is
  the one the long-runs report gives; confirm it).
- `LM5_return/`: the same four files as for LM8_PUSH.
- `LM7_PUSH_checkpoint_09/`: `LM7_PUSH_results.csv`, `sections\A_agent.tex`, `sections\A_root.tex`.
- `MPL_148_029-072_transcription.tex`, `MPL_148_029-072_notes.md`, `MPL_148_029-072_doubts.md` from
  `C:\Users\user\Documents\grothendieck_archive_transcription_20261110\returns\MPL_148_029-072_unzipped\`.
Still open from the evening intake of 13 Nov: `LM7_return/` in the background zip is the state of 103 statements
(the prompt now says so and points to the new folder; it may stay); the copy of `PROMPT.md` in the zip must be
refreshed or removed; `MPL_149_001-090_transcription.tex` should be the second-pass text.

**EXIT_TOWER** (`EXIT_TOWER_background.zip`). Gains `LM5_return/` (the same four files) and the three files of cote
148, scans 29–72 (transcription, notes, doubts). Loses nothing.

**ANABELIAN_149_PUSH** (`ANABELIAN_149_PUSH_background.zip`). Gains `LM5_return/` (the same four files). For Part F
the literature folder should gain, in LaTeX source where it exists: Carlson–Haine–Wolf, *Reconstruction of schemes
from their étale topoi* (arXiv e-print); Tsujimura's two papers cited in LM5 F.47 (2020, Theorem 3.1; 2022,
Propositions 1.2 and 4.9); Amoroso–Zannier 2000 (journal paper; PDF only if no source exists); Mochizuki 2006 on
solvably closed Galois groups. The exact titles and identifiers are in `LM5_MULTI_GALOIS_TOPOI_references.bib`
(not opened by me). FLAGGED_149 is already in this zip, which Part F3 needs.

**Prompts that needed FLAGGED_149 and did not have it.** LM5_MULTI_GALOIS_TOPOI (sent; its F.45 is open for that
reason). The audit is now F3 of ANABELIAN_149_PUSH, whose zip holds the return.

## After the script: two corrections, the lint, and what was left alone

- **Line endings.** The script wrote all four prompts with LF. EXIT_TOWER and ANABELIAN_149_PUSH had CRLF on every
  line; `checks\restore_crlf.py` put CRLF back, so the difference to the backups is the content only
  (`checks\compare_prompts.py`: LM8_PUSH 10 lines replaced by 15; LM6 1 by 25; EXIT_TOWER 2 by 20;
  ANABELIAN_149_PUSH 4 by 14).
- **A duplicated heading.** The insertion of R27 in ANABELIAN_149_PUSH left `## Leads` twice;
  `checks\fix_duplicate_leads.py` removed the second one and corrected this record and the script.
- **Lint.** `python -I -B claude_tools\push_rule_pro_prompts.py --lint-math <PROMPT.md>` passes on all four after
  the last change (failing lint: 0 each). The push paragraph and the three-hour check are untouched in each.
- **Not changed.** `LM7_PUSH\PROMPT.md`, `LM7_FERMAT_TOWER\PROMPT.md`, `LM4_FINITE_GROUP_ACTIONS\PROMPT.md`,
  `LM5_MULTI_GALOIS_TOPOI\PROMPT.md` (sent). No successor prompt exists for LM7_PUSH, the Fermat tower or LM4: their
  items are drafts in `pro_intake_20261113\PUSH_ITEMS_LM7_CONTINUED.md` (section "Added 14 November 2026"; the file
  as it was is `PUSH_ITEMS_LM7_CONTINUED_before_20261114.md` here) and in `PUSH_ITEMS_20261114.md`, both marked as
  waiting for the referee reports. The Dérivateurs and S6 prompts (INDLOCAL, DER_FOLLOWUP, S6_03 to S6_05): nothing
  in tonight's returns touches them; not opened.
- **What must change again when the referees report.** LM8_PUSH R24 says that the referee check "had been started
  when this was written; its result is not in this prompt": replace that sentence by the verdicts, and if D.50 or
  E.58 falls, rewrite R24, Lead 11, tasks B.3, C.5, C.7, C.8. LM8_PUSH R25 cites LM4 D.32, D.34, D.42, which no
  reviewer has read.
- **The expert's question on LM5** (`CONSULT_LM_EXPERT.md`, section 3): the copy of the LM5 prompt that was sent
  did hold item (h) of Part F with the two conference items. The return's coverage table has the lines "F(h)",
  "F(h-added)(1)" and "F(h-added)(2)", answered by F.31–F.34, F.35 and F.40–F.42. EXIT_TOWER's own copy of the
  second conference item (Lead 6, added task) now cites F.40–F.42.
- **A finding on our own material.** The LM5 prompt (line 182) asked for a comparison with "rows F11–F16, F25" of
  FLAGGED_149. FLAGGED_149 has no rows with those identifiers: F11–F16 are its flagged items, answered by its rows
  C1–C6, C8, C9, and no row carries a tag F25 (searched: the first tag of each statement of
  `FLAGGED_149_results.csv`). And the return was not in the LM5 zip. Both are why LM5 F.45 stayed open. The
  comparison is now F3 of ANABELIAN_149_PUSH with the right row numbers, and the fifth block of LM6 names them.


# Second pass, 14 November 2026, after the referee reports: LM8_PUSH

By Claude Fable 5.2 at effort high (intake agent), applied by `apply_referee_updates_20261114.py`. The referee reports are by Claude Opus 5.5 at effort max: `pro_intake_20261114\referee\REFEREE_A_D50_E58.md`, `REFEREE_B_E61_E65.md`, `REFEREE_A_LM4_D32.md`, `REFEREE_B_LM4_D34.md`. Backup of the prompt as it was before this pass: `C:\Users\user\Documents\longue_marche_pro_pilot_20261104\pro_prompts_draft_20261111_work\LM8_PUSH\PROMPT_before_referee_20261114.md`. Only LM8_PUSH changes in this pass: it is the one unsent prompt that cites the refereed rows.

### R1. What is attached, `runs_in_progress_20261114/` and new `referee/`

**Comes from:** LM4 snapshot of 01:56 UTC (271 rows), which the two LM4 referee reports use; the four referee reports

**Old text:**

```
- `runs_in_progress_20261114/`: the later states, reviewed by no one beyond what R24–R26 say. The three runs LM7_PUSH, LM7_FERMAT_TOWER and LM4_FINITE_GROUP_ACTIONS have not ended and can no longer be reached. `LM7_PUSH_checkpoint_09/` (13 November 2026, 22:42 UTC): the register (218 statements: 207 proved, 7 refuted, 3 known, 1 open) and the sections `D_pronilpotent_lift_agent.tex` (D.50), `D_full_weight5_agent.tex` and `D_full_weight9_agent.tex` (D.1, D.2), `E_agent.tex` (E.1–E.3), `E_relative_cm_lift_agent.tex` (E.58), `E_genus_one_sewing_agent.tex` (E.61), `E_hyperelliptic_CM_agent.tex` (E.64), `E_cm_character_agent.tex` (E.65) and `E_orbifold_CM_agent.tex` (E.67). `LM4_state_20261114/` (14 November, 01:07 UTC): the register (270 statements) and the LaTeX of the paper. `LM7_tower_state_20261114/` (14 November, 01:15 UTC): the register of LM7_FERMAT_TOWER (226 statements) with the sections `D_cm_shadow.tex` (D.25) and `D_arithmetic_replacement.tex` (D.46). `LM5_return/`: the register, the report and `sections/F.tex` of LM5_MULTI_GALOIS_TOPOI (GPT-6 Astra, ChatGPT Pro mode; final return of 13 November 2026, marked INCOMPLETE; 129 statements).
```

**New text:**

```
- `runs_in_progress_20261114/`: the later states. The three runs LM7_PUSH, LM7_FERMAT_TOWER and LM4_FINITE_GROUP_ACTIONS have not ended and can no longer be reached. `LM7_PUSH_checkpoint_09/` (13 November 2026, 22:42 UTC): the register (218 statements: 207 proved, 7 refuted, 3 known, 1 open) and the sections `D_pronilpotent_lift_agent.tex` (D.50), `D_modular_coprime_agent.tex` (D.44), `D_full_weight5_agent.tex` and `D_full_weight9_agent.tex` (D.1, D.2), `E_agent.tex` (E.1–E.3), `E_relative_cm_lift_agent.tex` (E.58), `E_genus_one_sewing_agent.tex` (E.61), `E_hyperelliptic_CM_agent.tex` (E.64), `E_cm_character_agent.tex` (E.65) and `E_orbifold_CM_agent.tex` (E.67). `LM4_state_20261114/` (14 November, 01:56 UTC): the register (271 statements) and the LaTeX of the paper. `LM7_tower_state_20261114/` (14 November, 01:15 UTC): the register of LM7_FERMAT_TOWER (226 statements) with the sections `D_cm_shadow.tex` (D.25) and `D_arithmetic_replacement.tex` (D.46). `LM5_return/`: the register, the report and `sections/F.tex` of LM5_MULTI_GALOIS_TOPOI (GPT-6 Astra, ChatGPT Pro mode; final return of 13 November 2026, marked INCOMPLETE; 129 statements). Apart from the rows named in R24 and R25 as refereed, these states are reviewed by no one.
- `referee/`: four referee reports on rows of these runs, by Claude Opus 5.5 at effort max, 14 November 2026. Each is a step-by-step check with the primary sources it names opened and with its own programs and their outputs (`referee/checks/`): `REFEREE_A_D50_E58.md` (LM7_PUSH D.44 as used, D.50, E.58), `REFEREE_B_E61_E65.md` (LM7_PUSH E.61, E.64, E.65, E.67; LM7 D.25 and LM7_PUSH E.1 as used), `REFEREE_A_LM4_D32.md` (LM4 D.32), `REFEREE_B_LM4_D34.md` (LM4 D.34). R24 and R25 give their verdicts. The line numbers in the two LM4 reports are those of the paper in `LM4_state_20261114/`.
```

### R2. Results this builds on, R24

**Comes from:** REFEREE_A_D50_E58.md, REFEREE_B_E61_E65.md (verdicts; register defect; scope remark; what E.58 adds)

**Old text:**

```
- **R24** (LM7_PUSH checkpoint 09: D.50, E.58, E.61, E.65, with D.1, D.2, E.2; claims of GPT-6 Astra, ChatGPT Pro mode, 13 November 2026. Two intake readers, Claude Fable 5.2 at effort high, each read D.50 and E.58 once and found no error; one of them read E.65 and the first half of E.61, recomputed the finite matrix identities of E.58, E.61 and E.65 with its own program, and recomputed the two division fields behind LM7 D.25. A step-by-step referee check by Claude Opus 5.5 at effort max had been started when this was written; its result is not in this prompt. All of R24 is a claim: for each statement you use, give your own proof or the exact error.) Notation of LM7_PUSH: its `F` is `K₂`, with free generators `x = (sr)⁻²`, `y = sxs`; `τ = sr`; `R_nil(G)` is the intersection of the kernels of the continuous homomorphisms from `G` to finite nilpotent groups. *D.50.* Every continuous automorphism of `B̂/R_nil(K₂)` that sends `s`, `r`, `τ` to conjugates, with any three conjugators, lifts to a continuous automorphism of `B̂` with those conjugators lifted; the same for the free profinite group on two generators with its three peripheral classes. The proof is a count: for a finite extension `A → E → D` with `[E, A] = A`, the number of epimorphisms onto `E` above a map to `D`, with the three boundary values in prescribed `A`-classes, depends on the map to `D` only through its lifts to one finite central extension of `D`. Claimed consequences (D.1, D.2): for `ℓ ≥ 5` every pro-`ℓ` solution of the 2-cycle and 3-cycle relations with multiplier one whose pure map is an automorphism is the image of an element of `GT̂₀`; the image of the full profinite special group in weight five has dimension three, and `GT̂₀` reaches the second vector of weight nine. *E.58.* The same lifting for `B̂/R_nil(U)`, `U` any open normal subgroup of `B̂`. Applied to the identity of `B̂/R_nil(H)`, `H = K₂′K₂³`, with the conjugator of `r` taken in the centralizer of `r` in the 2-primary component: an element `(1, f)` of `GT̂₀` with `f ∈ R_nil(H)`, whose automorphism `Φ` of `B̂` fixes `τ` and has unique conjugators `A, β ∈ K₂` (`Φ(r) = ArA⁻¹`, `Φ(s) = βsβ⁻¹`; uniqueness from Herfort–Ribes 1985, Theorem B′: `C_B̂(r) = ⟨r⟩`, `C_B̂(s) = ⟨s⟩`) with images `[5I]` and `1` in `SL₂(Z/12)/±1`. Its pair `(T, W)` lies in the coset that Galois misses (E.2). *E.61.* For every element of `GT̂₀` of multiplier one, with `ρ` defined by `(β⁻¹)^ab = (ρ, ρ)`: the image of `f` under `x ↦ (1 2; 0 1)`, `y ↦ (1 0; −2 1)` modulo 12 is `(1 −8ρ; −8ρ 1+64ρ²)`. *E.65.* On the multiplier-one subgroup of `GT̂₀` the coordinates `T` (in the centralizer of `R₀ = (0 −1; 1 −1)` in `SL₂(F₃)`, cyclic of order six) and `W` (in the centralizer of `S = (0 1; −1 0)`, cyclic of order four) are continuous homomorphisms; the sum `δ` of the sign of `T` on the line `F₃·(1, −1)` and of the class of `W` modulo `±1` is a continuous character with values in `F₂`, invariant under conjugation by `GT̂₀`; it vanishes on `G_{Q^ab}` (both bits are the action on `(3/4)^{1/4}`, by LM7 D.25) and extends uniquely to a continuous character `Δ : GT̂₀ → F₂` that vanishes on `G_Q`; `Δ = 1` on the element of E.58. So the index-two condition of R14 is `ker Δ`, a closed subgroup of index two of `GT̂₀` that contains the Galois image. LM7_PUSH E.3, open there: the value of `Δ` on `GT̂`. LM7_PUSH E.64, E.67 (statement level): on `GT̂` the character is a sum of three bits read from the hyperelliptic quotient of `B̂₄` and the two CM triangle groups.
```

**New text:**

```
- **R24** (LM7_PUSH checkpoint 09: D.50, E.58, E.61, E.64, E.65, E.67, with D.44 as used and D.1, D.2, E.2; returns of GPT-6 Astra, ChatGPT Pro mode, 13 November 2026. Refereed on our side by Claude Opus 5.5 at effort max, 14 November 2026, step by step, in the two reports `referee/REFEREE_A_D50_E58.md` and `referee/REFEREE_B_E61_E65.md`. Verdicts. **D.50 and E.58: proved as claimed**; D.44 is proved in the parts they use; Herfort–Ribes 1985, Theorem B′, was opened and holds for `C₂ ∐ C₃`; the genus-zero counting formula is proved in the text and does not rest on Turaev 2009. **E.65: proved, with two gaps that the report closes**: the vanishing on Galois, which the return asserts by reference to LM7 D.25 and D.15, is derived in the report for every Galois element of multiplier one, with the models `y² = x³ + 1`, `y² = x³ − x` and the signs; and the existence of the pure conjugator of `r` for an arbitrary element, where the return cites only uniqueness. **E.61: proved as claimed**, the sewing part included. **E.67: proved** for its general statements; its 48 per-origin data statements were not recomputed. **E.64: proved in every step that could be checked**; three of its steps rest on results that were not verified (LM7_PUSH E.39; Boggi 2026 v6, Theorem 2.3 and Proposition 2.6 (i); Nakamura–Tsunogai–Yasuda 2010, Propositions 4.11–4.13), and none of the three is used by E.65 or E.67. **Not refereed:** D.1 and D.2 beyond D.50 (their other inputs D.20, D.21, D.51, D.52), and every other row of LM7_PUSH. A defect of the register of LM7_PUSH: the dependency "D.25" of its E.1, E.2, E.58 and E.65 means LM7 D.25 (the Fermat tower, `D_cm_shadow.tex`), not its own D.25; the dependencies of E.65 omit Herfort–Ribes and LM7 D.15 and list E.62, which E.65 does not use.) Notation of LM7_PUSH: its `F` is `K₂`, with free generators `x = (sr)⁻²`, `y = sxs`; `τ = sr`; `R_nil(G)` is the intersection of the kernels of the continuous homomorphisms from `G` to finite nilpotent groups. *D.50.* Every continuous automorphism of `B̂/R_nil(K₂)` that sends `s`, `r`, `τ` to conjugates, with any three conjugators, lifts to a continuous automorphism of `B̂` with those conjugators lifted; the same for the free profinite group on two generators with its three peripheral classes. The proof is a count: for a finite extension `A → E → D` with `[E, A] = A`, the number of epimorphisms onto `E` above a map to `D`, with the three boundary values in prescribed `A`-classes, depends on the map to `D` only through its lifts to one finite central extension of `D`. Claimed consequences (D.1, D.2): for `ℓ ≥ 5` every pro-`ℓ` solution of the 2-cycle and 3-cycle relations with multiplier one whose pure map is an automorphism is the image of an element of `GT̂₀`; the image of the full profinite special group in weight five has dimension three, and `GT̂₀` reaches the second vector of weight nine. *E.58.* The same lifting for `B̂/R_nil(U)`, `U` any open normal subgroup of `B̂`. Applied to the identity of `B̂/R_nil(H)`, `H = K₂′K₂³`, with the conjugator of `r` taken in the centralizer of `r` in the 2-primary component: an element `(1, f)` of `GT̂₀` with `f ∈ R_nil(H)`, whose automorphism `Φ` of `B̂` fixes `τ` and has unique conjugators `A, β ∈ K₂` (`Φ(r) = ArA⁻¹`, `Φ(s) = βsβ⁻¹`; uniqueness from Herfort–Ribes 1985, Theorem B′: `C_B̂(r) = ⟨r⟩`, `C_B̂(s) = ⟨s⟩`) with images `[5I]` and `1` in `SL₂(Z/12)/±1`. Its pair `(T, W)` lies in the coset that Galois misses (E.2). *E.61.* For every element of `GT̂₀` of multiplier one, with `ρ` defined by `(β⁻¹)^ab = (ρ, ρ)`: the image of `f` under `x ↦ (1 2; 0 1)`, `y ↦ (1 0; −2 1)` modulo 12 is `(1 −8ρ; −8ρ 1+64ρ²)`. *E.65.* On the multiplier-one subgroup of `GT̂₀` the coordinates `T` (in the centralizer of `R₀ = (0 −1; 1 −1)` in `SL₂(F₃)`, cyclic of order six) and `W` (in the centralizer of `S = (0 1; −1 0)`, cyclic of order four) are continuous homomorphisms; the sum `δ` of the sign of `T` on the line `F₃·(1, −1)` and of the class of `W` modulo `±1` is a continuous character with values in `F₂`, invariant under conjugation by `GT̂₀`; it vanishes on `G_{Q^ab}` (both bits are the action on `(3/4)^{1/4}`, by LM7 D.25) and extends uniquely to a continuous character `Δ : GT̂₀ → F₂` that vanishes on `G_Q`; `Δ = 1` on the element of E.58. So the index-two condition of R14 is `ker Δ`, a closed subgroup of index two of `GT̂₀` that contains the Galois image. For an element of multiplier `λ ≠ 1`, `Δ(F)` is `δ(Fσ⁻¹)` with `σ` Galois of multiplier `λ`; signed coordinates `T`, `W` are defined at multiplier one only. LM7_PUSH E.3, open there, is exactly the question whether `Δ = 0` on `GT̂` (the referee: a correct reformulation, and one that does not use E.58). With E.58: if `Δ ≠ 0` on `GT̂`, then `GT̂` has a continuous quadratic character that is trivial on `G_Q`, so `GT̂ ≠ G_Q`; if `Δ = 0` on `GT̂`, then `GT̂ ⊆ ker Δ ⊊ GT̂₀`. *E.64, E.67.* On the multiplier-one subgroup of `GT̂` the character is the sum of three bits, `ε₃(𝒟₃) + ε₂(𝒟₄) + ε₂(B₄)`, read from the hyperelliptic quotient of `B̂₄` and the two CM triangle groups; this identity assigns no value.
```

### R3. Results this builds on, R25

**Comes from:** REFEREE_A_LM4_D32.md, REFEREE_B_LM4_D34.md (verdicts; literature; Δ on torsion)

**Old text:**

```
- **R25** (LM4_FINITE_GROUP_ACTIONS, state of 14 November 2026: D.32, D.34, D.42, D.70, D.75, D.78; Proved there; no proof of any row of LM4 has been read by a reviewer). LM4's `P` is the group of outer automorphisms of `F` preserving the three procyclic conjugacy classes of `x`, `y`, `z`, with one common multiplier: compare it with `𝒫` before use. D.32, D.34: every finite subgroup of `P` maps injectively to `{±1} ⊂ Z₂^×` by the 2-adic multiplier; every non-trivial element of finite order of `P` is an involution whose multiplier is the global `−1 ∈ Ẑ^×`; so the multiplier-one subgroup of `P`, and that of `GT̂₀`, are torsion-free. For such an involution, normalized as `α(x) = x⁻¹`, `α(y) = f⁻¹y⁻¹f`, there is `h ∈ F′` with `f = h⁻¹α(h)`, and `x ↦ x, y ↦ hyh⁻¹` induces an automorphism of every `F^(p)`; that it is onto `F`, and that `α` is conjugate to complex conjugation, are not claimed. D.42: with the permutations of the punctures allowed, every element of order three has multiplier 1. D.70: in the peripheral outer group of the once-punctured torus every element of order four has multiplier 1. D.75, D.78: for a negative involution of the punctured torus the fixed subgroups of the cusp reflections are trivial and the transporter is unique; the other fixed subgroup is `K ⋊ Ẑ` with `K` pro-odd, and `K = 1` is not decided. Open in LM4 (D.12): whether every torsion element of `GT̂₀` is conjugate to complex conjugation.
```

**New text:**

```
- **R25** (LM4_FINITE_GROUP_ACTIONS, state of 14 November 2026, 01:56 UTC: D.32, D.34, D.42, D.70, D.75, D.78; Proved there. **D.32 and D.34 are refereed on our side: proved as claimed** (Claude Opus 5.5 at effort max, 14 November 2026; `referee/REFEREE_A_LM4_D32.md`, `referee/REFEREE_B_LM4_D34.md`; Kochloukova–Zalesskii 2007, Harbater–Schneps 2000, Herfort–Ribes 1985 and Lochak–Schneps 1997 opened). No proof of any other row of LM4 has been read by a reviewer.) LM4's `P` is `𝒫`: the outer automorphisms of `F` preserving the three procyclic conjugacy classes of `x`, `y`, `z` (the three multipliers agree, by abelianization); it is the Belyi group of Harbater–Schneps. D.32: every finite subgroup of `𝒫` maps injectively to `{±1} ⊂ Z₂^×` by the 2-adic multiplier, so it has order one or two; with the permutations of the punctures allowed, `g ↦ (σ_g, λ₂(g)) ∈ 𝔖₃ × C₂` is injective on every finite subgroup. D.34: every non-trivial element of finite order of `𝒫` is an involution whose multiplier is `−1` at every prime; the same in `GT̂₀` and in `GT̂`; `𝒫₁` and the multiplier-one subgroups of `GT̂₀` and `GT̂` are torsion-free. For such an involution, normalized as `α(x) = x⁻¹`, `α(y) = f⁻¹y⁻¹f` with `f ∈ F′`: `F ⋊_α C₂` has exactly three `F`-conjugacy classes of sections, each with a fixed subgroup of zero `H¹(−, F₂)`; there is `h ∈ F′` with `f = h⁻¹α(h)`; `α` inverts `x` and `hyh⁻¹`; and `x ↦ x, y ↦ hyh⁻¹` induces an automorphism of every `F^(p)`. Not proved by D.32 or D.34, and not claimed there: that this endomorphism is onto `F`, and that every involution is conjugate to complex conjugation `(−1, 1)`. The referee of D.32 found the conjugacy still listed as open (Schneps, survey of `GT̂`, §1.4, question (4); Lochak–Schneps, "Open problems in Grothendieck–Teichmüller theory", question 1.4) and found no source for the bound on the order; that search does not exclude one. For `Δ` of R24 (the referee of D.34): every element `τ ≠ 1` of finite order of `GT̂₀` is `(−1, f_τ)`, and `Δ(τ) = δ((1, f_τ))`; it is 0 when `τ` is conjugate in `GT̂₀` to complex conjugation, which D.34 does not prove. D.42 (not refereed): with the permutations of the punctures allowed, every element of order three has multiplier 1. D.70, D.75, D.78 (not refereed): in the peripheral outer group of the once-punctured torus every element of order four has multiplier 1; for a negative involution of the punctured torus the fixed subgroups of the cusp reflections are trivial and the transporter is unique; the other fixed subgroup is `K ⋊ Ẑ` with `K` pro-odd, and `K = 1` is not decided. Open in LM4 (D.12): whether every torsion element of `GT̂₀` is conjugate to complex conjugation.
```

### R4. Leads, Lead 11

**Comes from:** REFEREE_B_E61_E65.md (E.65 proved); REFEREE_A_D50_E58.md (E.58 proved)

**Old text:**

```
 LM7_PUSH E.65 (R24) claims that the condition is the kernel of one continuous character `Δ` of `GT̂₀`; with it this Lead reads `C^φ ⊆ ker Δ`.
```

**New text:**

```
 By LM7_PUSH E.65 (R24, refereed) the condition is the kernel of the continuous character `Δ` of `GT̂₀`, so this Lead reads `C^φ ⊆ ker Δ`. By E.58 (R24, refereed) an element in the coset that Galois misses exists; the Lead says that it lies outside `C^φ`.
```

### R5. Part B, opening

**Comes from:** REFEREE_A_LM4_D32.md, REFEREE_B_LM4_D34.md

**Old text:**

```
 LM4 D.32, D.34 and D.42 (R25) claim answers to task 3, to task 4 for `GT̂₀` and to the multiplier statement of task 5; they are claims, with their proofs in `runs_in_progress_20261114/LM4_state_20261114/`.
```

**New text:**

```
 LM4 D.32 and D.34 (R25; refereed on our side, proved as claimed) settle the torsion-freeness of task 3, the statement of task 4, and the multiplier statement of task 5: they are cited there, not proved again. What they leave open is whether every involution is conjugate to complex conjugation; that question is now the centre of this Part.
```

### R6. Part B, task 3

**Comes from:** LM4 D.34 (refereed: 𝒫₁ torsion-free); LM7_PUSH D.50 (refereed)

**Old text:**

```
3. Prove or refute: `𝒫₁` is torsion-free. A refutation is an automorphism of `F` of finite order, pure, peripheral, of multiplier one and not inner, constructed; a proof covers `φ₀` and every element of `𝒯`. For `φ₀`: construct a lift to `F`, or exhibit the finite quotient of `F` in which system (A–I) with the residue of `φ₀` has no solution. R8 covers `V = K₃`, `p = 5`; the next quotients are the `F/ker(V → V^(p))` for the other pairs of an open normal `V ⊂ F` and a prime `p`, beginning with those where 5 divides the order of `F/V` and `p ≠ 5`. LM4 D.32 and D.34 (R25) claim that `𝒫₁` is torsion-free, through the 2-adic multiplier: give your own proof of the statement they rest on, or the exact error. If they hold, `φ₀` has no lift of finite order; then exhibit the finite quotient above, and decide whether `φ₀` lifts to an element of `𝒫₁` of infinite order (the lifting theorem D.50 of R24 concerns `F/R_nil(F)`, of which `M` is not a quotient: prove what it gives for `φ₀` and what it does not).
```

**New text:**

```
3. `𝒫₁` is torsion-free: this is LM4 D.34 (R25, refereed); cite it. So `φ₀` and every element of `𝒯` have no lift of finite order to `F`. For `φ₀`: exhibit the finite quotient of `F` in which system (A–I) with the residue of `φ₀` has no solution (one exists, by R6 and D.34; R8 covers `V = K₃`, `p = 5`; the next quotients are the `F/ker(V → V^(p))` for the other pairs of an open normal `V ⊂ F` and a prime `p`, beginning with those where 5 divides the order of `F/V` and `p ≠ 5`). Then prove or refute: `φ₀` lifts to an element of `𝒫₁`, necessarily of infinite order. The lifting theorem D.50 of R24 concerns `F/R_nil(F)`, of which `M` is not a quotient: prove what it gives for `φ₀` and what it does not. State and prove what this gives for LM8 A.12 on the tripod.
```

### R7. Part B, task 4

**Comes from:** LM4 D.32, D.34 (refereed); REFEREE_B_LM4_D34.md (Δ(τ) = δ((1, f_τ)))

**Old text:**

```
4. Prove or refute: `GT̂₀` has a non-trivial element of finite order with `λ = 1`. The same for `GT̂`. (LM4 D.34, R25, claims there is none.) For every element of finite order of `GT̂₀`, of any multiplier, compute `Δ` of R24: `Δ` is invariant under conjugation and vanishes on complex conjugation, so an involution with `Δ = 1` is not conjugate to it.
```

**New text:**

```
4. `GT̂₀` and `GT̂` have no non-trivial element of finite order with `λ = 1`, and every non-trivial element `τ` of finite order is an involution `(−1, f_τ)`: LM4 D.32, D.34 (R25, refereed); cite them. For `Δ` of R24: `Δ(τ) = δ((1, f_τ))` (`referee/REFEREE_B_LM4_D34.md`), and `Δ(τ) = 0` when `τ` is conjugate in `GT̂₀` to complex conjugation. Prove or refute: `δ((1, f)) = 0` for every `f` such that `(−1, f)` is an involution of `GT̂₀`; and the same for the involutions of `GT̂`. An involution with `Δ = 1` is not conjugate to complex conjugation in `GT̂₀`, and answers LM4 D.12 in the negative.
```

### R8. Part B, task 5

**Comes from:** LM4 D.34 (refereed); the conjugacy it leaves open; LM7_PUSH D.50 (refereed)

**Old text:**

```
5. Determine the centralizer in `𝒫` of the class of complex conjugation, with its torsion and its multipliers (the tripod form of LM4 D.63–D.65, R22). Prove or refute: every involution of `𝒫` of multiplier `−1` is conjugate in `𝒫` to the class of complex conjugation; and: no element of finite order of `𝒫` has a multiplier other than `±1` (decide in particular whether the involution of R22 at type (0,4) induces one on the tripod when a puncture is filled). With 3, state and prove what follows for §52.2: which finite subgroups of `𝒫` exist, up to conjugacy. Prove or refute: `Δ` (R24) vanishes on every element of finite order of `GT̂₀`; this is a necessary condition for LM4 D.12 (R25).
```

**New text:**

```
5. Determine the centralizer in `𝒫` of the class of complex conjugation, with its torsion and its multipliers (the tripod form of LM4 D.63–D.65, R22). Prove or refute: every involution of `𝒫` is conjugate in `𝒫` to the class of complex conjugation; the same in `GT̂₀` (LM4 D.12) and in `GT̂` (the question of Lochak and Schneps, R25). That every non-trivial element of finite order of `𝒫` has multiplier `−1` is LM4 D.34 (R25, refereed); cite it, and decide whether the involution of R22 at type (0,4) induces one on the tripod when a puncture is filled. For the conjugacy start from D.34: `f = h⁻¹α(h)` with `h ∈ F′`, and `ψ : x ↦ x, y ↦ hyh⁻¹` is an automorphism of every `F^(p)`, on which `α = ψcψ⁻¹` (`c` complex conjugation). Prove or refute: `ψ` is onto `F`; `ψ` sends `z` to a conjugate of `z`; and, for `α ∈ GT̂₀`, the conjugating element can be taken in `GT̂₀`. The lifting theorem D.50 of R24 lifts the peripheral automorphisms of `F/R_nil(F)` with their conjugators: prove what it gives here. With 3 and 4, state and prove what follows for §52.2: which finite subgroups of `𝒫` exist, up to conjugacy.
```

### R9. Part C, task 5

**Comes from:** REFEREE_A_D50_E58.md (D.50 proved, the lift of a pro-ℓ gentle pair included)

**Old text:**

```
 LM7_PUSH D.50 (R24) claims that the first projection is onto the multiplier-one solutions whose pure map is an automorphism: confirm it by your own proof or give the exact error, then use it.
```

**New text:**

```
 By LM7_PUSH D.50 (R24, refereed) the first projection is onto the multiplier-one solutions whose pure map is an automorphism: use it.
```

### R10. Part C, task 7

**Comes from:** REFEREE_B_E61_E65.md (E.65 proved, two gaps closed)

**Old text:**

```
7. Prove or refute Lead 11. Prove or refute that `(T, W)` is a homomorphism on the multiplier-one subgroup of `GT̂₀`, and that `Δ` of R24 is a continuous character of `GT̂₀` that vanishes on `G_Q`. LM7_PUSH E.65 claims both: give your own proof, or the exact step of E.65 that fails. Begin with E.61 and with the statement on which the vanishing rests: on `G_{Q^ab}` the conjugators of `r` and of `s` in `K₂` give the representations on the torsion of `y² = x³ + 1` and of `y² = x³ − x` (LM7 D.15–D.17, D.25; Nakamura–Tsunogai and its sequels), with the signs. State what 3 and 4 give for LM7 D.19 (the coset of the CM coordinates that Galois misses), for the automorphism of LM7 D.46 (R14) and for LM2 C.d5.
```

**New text:**

```
7. Prove or refute Lead 11. That `(T, W)` is a homomorphism on the multiplier-one subgroup of `GT̂₀`, and that `Δ` is a continuous character of `GT̂₀` that vanishes on `G_Q`, is LM7_PUSH E.65 (R24, refereed, with its two gaps closed in `referee/REFEREE_B_E61_E65.md`); cite it. Determine the image of `(T, W)` on the multiplier-one subgroup of `GT̂₀` and on that of `C^φ`: it contains the pairs of the Galois image and the pair of the element of E.58. State what 3 and 4 give for LM7 D.19 (the coset of the CM coordinates that Galois misses), for the automorphism of LM7 D.46 (R14) and for LM2 C.d5.
```

### R11. Part C, task 8

**Comes from:** REFEREE_A_D50_E58.md (E.58 proved: Δ = 1 is attained); REFEREE_B_E61_E65.md (E.3 is Δ on GT̂); LM7 D.46

**Old text:**

```
8. Prove or refute: `C^φ ⊆ ker Δ`. Then prove or refute: `C^φ = ker Δ`. With the element of LM7_PUSH E.58 (R24: confirm its construction by your own proof or give the exact error) the first inclusion settles task 4; with task 3 it gives `Δ = 0` on `GT̂`, which is LM7_PUSH E.3. Prove or refute `Δ = 0` on `GT̂` directly as well: from the pentagon in a quotient of the five-point group in which both coordinates are read; from the harmonic and equianharmonic equations and relation (III′) of task 2, deciding whether they hold for `F` exactly when `Δ(F) = 0`; and from the comparison characters of LM7_PUSH E.64 and E.67. A value `Δ = 1` on an element of `GT̂` gives a continuous quadratic character of `GT̂` that is trivial on `G_Q`, hence an element of `GT̂` outside the Galois image: write every step of such a proof out in full.
```

**New text:**

```
8. Prove or refute: `C^φ ⊆ ker Δ`. Then prove or refute: `C^φ = ker Δ`. The element of LM7_PUSH E.58 has `Δ = 1` (R24, refereed), so the first inclusion settles task 4 (`C^φ ≠ GT̂₀`); with task 3 it gives `Δ = 0` on `GT̂`, which is LM7_PUSH E.3, and then `GT̂ ⊆ ker Δ ⊊ GT̂₀`. Prove or refute `Δ = 0` on `GT̂` directly as well: from the pentagon in a quotient of the five-point group in which both coordinates are read; from the harmonic and equianharmonic equations and relation (III′) of task 2, deciding whether they hold for `F` exactly when `Δ(F) = 0`; and from the comparison characters of LM7_PUSH E.64 and E.67 (R24). A value `Δ = 1` on an element of `GT̂` gives a continuous quadratic character of `GT̂` that is trivial on `G_Q`, hence an element of `GT̂` outside the Galois image: write every step of such a proof out in full. Prove or refute also: the automorphism of LM7 D.46 (R14), with its conjugators, satisfies the hypotheses of E.58 for `U = ker(B̂ → SL₂(Z/12)/±1)`; if so, its lift is an element of `GT̂₀` of multiplier one with the CM pair of D.46 and `Δ = 1`, and LM7 D.19 for `GT̂₀` follows.
```

## The push-items files after the referee reports

- `C:\Users\user\Documents\pro_intake_20261113\PUSH_ITEMS_LM7_CONTINUED.md`: the section "Added 14 November 2026"
  is rewritten (script `checks\replace_lm7_section.py`). The "waiting" status is gone; the verdicts stand at its
  head; S.1 states both outcomes of "`Δ` on `GT̂`"; S.2 is no longer a second proof of E.58; S.4 uses
  `Δ(τ) = δ((1, f_τ))`; S.6 lists what is still unrefereed (D.1, D.2 beyond D.50; the three inputs of E.64; the 48
  data statements of E.67) and what is done; S.7 names the refereed rows as cited; **S.8 is new**: the repair of
  the register pointers ("D.25" → "LM7 D.25" in E.1, E.2, E.58, E.65; E.65's dependencies; the circular pair
  E.2/E.58) and of the two gaps of E.65 and the Hopficity sentence of D.50. The draft that was there is kept as
  `pro_intake_20261114\PUSH_ITEMS_LM7_CONTINUED_draft_before_referee_20261114.md`; the file before any change of
  today as `PUSH_ITEMS_LM7_CONTINUED_before_20261114.md`.
- `C:\Users\user\Documents\pro_intake_20261114\PUSH_ITEMS_20261114.md`: rewritten. The draft is kept as
  `PUSH_ITEMS_20261114_draft_before_referee.md`. Tower: 1.1 and 1.3 rest on E.58 as a refereed theorem; 1.5 says
  what of D.1, D.2 is refereed; **1.12 is new** (register pointers). LM4: 2.3 is now the conjugacy of the
  involutions, with D.32, D.34 refereed; 2.5 uses the referee's formula; 2.7 says what is refereed; **2.8 is new**
  (D.28's statement, the circular citation D.25/D.32, A.7's source, run names in citations). The LM4 snapshot is
  now 01:56 UTC (271 rows; new F.32).

## What each of the four zips must gain: the list after the referee reports (it replaces the list further up)

None of the zips was rebuilt. `A = C:\Users\user\Documents\longue_marche_pro_pilot_20261104\answers`;
`R = C:\Users\user\Documents\pro_intake_20261114\referee`. LaTeX and registers only; no PDF.

**1. LM8_PUSH** (`longue_marche_pro_pilot_20261104\pro_prompts_draft_20261111\LM8_PUSH\LM8_PUSH_background.zip`).
The prompt cites the four referee reports (attachment list, R24, R25, tasks B.4 and C.7). Gains:
- `referee/`: `R\REFEREE_A_D50_E58.md`, `R\REFEREE_B_E61_E65.md`, `R\REFEREE_A_LM4_D32.md`, `R\REFEREE_B_LM4_D34.md`,
  and `referee/checks/` with every `.py` and `.out` of `R\checks\` (the reports refer to them).
- `runs_in_progress_20261114/LM7_PUSH_checkpoint_09/`: from
  `A\LM7_PUSH_checkpoint_09_20261113T2242Z_unzipped\LM7_PUSH\`: `LM7_PUSH_results.csv`, `LM7_PUSH_references.bib`, and
  from `sections\`: `D_pronilpotent_lift_agent.tex`, `D_modular_coprime_agent.tex` (new in this list: D.44),
  `D_full_weight5_agent.tex`, `D_full_weight9_agent.tex`, `E_agent.tex`, `E_relative_cm_lift_agent.tex`,
  `E_genus_one_sewing_agent.tex`, `E_hyperelliptic_CM_agent.tex`, `E_cm_character_agent.tex`,
  `E_orbifold_CM_agent.tex`.
- `runs_in_progress_20261114/LM4_state_20261114/`: from `A\LM4_FINITE_GROUP_ACTIONS_20261114T0156Z_unzipped\` (the
  01:56 UTC snapshot, not the one of 01:07: the two LM4 reports give line numbers of this paper):
  `LM4_FINITE_GROUP_ACTIONS_results.csv`, `LM4_FINITE_GROUP_ACTIONS_paper.tex`,
  `LM4_FINITE_GROUP_ACTIONS_references.bib`, `DIFF_vs_T0107Z.txt`.
- `runs_in_progress_20261114/LM7_tower_state_20261114/`: from
  `A\LM7_FERMAT_TOWER_20261114T0115Z_unzipped\LM7_FERMAT_TOWER\`: `LM7_FERMAT_TOWER_results.csv`,
  `sections\D_cm_shadow.tex`, `sections\D_arithmetic_replacement.tex`.
- `runs_in_progress_20261114/LM5_return/`: from `A\LM5_MULTI_GALOIS_TOPOI_final_20261113T2351Z_unzipped\`:
  `LM5_MULTI_GALOIS_TOPOI_results.csv`, `LM5_MULTI_GALOIS_TOPOI_report.md`, `LM5_MULTI_GALOIS_TOPOI_references.bib`,
  `sections\F.tex`. (The prompt writes `LM5_return/` inside the bullet of `runs_in_progress_20261114/`.)
Loses nothing: the older `runs_in_progress/` is still cited by R14, R22, R23 and Lead 20.
One thing to check when building: the referee reports name the user's folders with the first name in the path;
anonymize the paths as for the other zips.

**2. LM6_POINTS_AS_SECTIONS** (`...\LM6_POINTS_AS_SECTIONS\LM6_POINTS_AS_SECTIONS_new_results.zip`). The prompt
cites no refereed row, so no referee report goes in. Gains, as listed before:
- `LM7_tower_state_20261114/`: `LM7_FERMAT_TOWER_results.csv`, `LM7_FERMAT_TOWER_report.md`, every `sections\E*.tex`
  of the tower folder above.
- `E102_check/FORMULA.md` (from `C:\Users\user\Documents\LM7_FERMAT_TOWER_E102_check_20261113\FORMULA.md`; confirm the
  path).
- `LM5_return/`: the four files named under 1.
- `LM7_PUSH_checkpoint_09/`: `LM7_PUSH_results.csv`, `sections\A_agent.tex`, `sections\A_root.tex`.
- `MPL_148_029-072_transcription.tex`, `MPL_148_029-072_notes.md`, `MPL_148_029-072_doubts.md` from
  `C:\Users\user\Documents\grothendieck_archive_transcription_20261110\returns\MPL_148_029-072_unzipped\`.
Still open from the evening intake of 13 Nov: refresh or remove the copy of `PROMPT.md` in the zip; the second-pass
text of `MPL_149_001-090_transcription.tex`.
A choice for the main session: the fifth block of LM6 says of LM7_PUSH Part A "no reader on our side has read it",
which is still true (the referees read D.44, D.50, E.58, E.61, E.64, E.65, E.67 only). If LM6 should also say that
D.50 and E.58 are refereed, it needs one sentence and `referee/REFEREE_A_D50_E58.md`; I did not add it, because LM6
uses neither row.

**3. EXIT_TOWER** (`grothendieck_archive_montpellier\pro_prompts_archive_20261112\EXIT_TOWER\EXIT_TOWER_background.zip`).
Cites no refereed row; no referee report. Gains: `LM5_return/` (the four files named under 1) and the three files
of cote 148, scans 29–72 (transcription, notes, doubts). Loses nothing.

**4. ANABELIAN_149_PUSH** (`...\ANABELIAN_149_PUSH\ANABELIAN_149_PUSH_background.zip`). Cites no refereed row; no
referee report. Gains: `LM5_return/` (the four files named under 1); and for Part F, in `literature/`, in LaTeX
source where it exists: Carlson–Haine–Wolf (the reconstruction of schemes from their étale topoi); Tsujimura's two
papers cited in LM5 F.47 and F.50 (2020, Theorem 3.1; 2022, Propositions 1.2 and 4.9); Amoroso–Zannier 2000 (a
journal paper: PDF only if no source exists); Mochizuki 2006 on solvably closed Galois groups. Exact titles and
identifiers: `LM5_MULTI_GALOIS_TOPOI_references.bib` (not opened by me). FLAGGED_149 is already in this zip; Part
F3 needs it.

**For the successor prompts, when they are written** (no zip exists yet): the attachments are listed at the end of
the section "Added 14 November 2026" of `PUSH_ITEMS_LM7_CONTINUED.md` (LM7_PUSH successor: the four referee reports
with `checks\`), and in items 1.1, 1.8, 2.6 of `PUSH_ITEMS_20261114.md` (tower and LM4 successors: the referee
reports `REFEREE_A_D50_E58.md` and `REFEREE_B_E61_E65.md` for the tower; `REFEREE_A_LM4_D32.md` and
`REFEREE_B_LM4_D34.md` for LM4, with the 01:56 UTC snapshot).


# Third pass, 14 November 2026: the updates the Longue Marche expert lists after intake section 11

By Claude Fable 5.2 at effort high (intake agent), applied by `apply_intake11_updates_20261114.py`, following `EXPERT_ON_INTAKE_11.md` (Claude Fable 5.2 at effort max), which confirms findings 1, 3, 4 of section 11 of the intake and corrects finding 2 (his `g` is the cocycle `f⁻¹`, `(γ, χ)` is `(f, λ)` up to gauge, the frames come from the splittings of scans 22 and 28, `Δ` is not a function of `γ` modulo 12, `β` is unidentified). ANABELIAN_149_PUSH was not touched. No result line for cote 145, scan 24, was added: its chain is not refereed. Backups: `PROMPT_before_intake11_20261114.md` in each prompt's work folder; the two item lists as `PUSH_ITEMS_LM7_CONTINUED_before_intake11_20261114.md` and `PUSH_ITEMS_20261114_before_intake11_20261114.md` in `pro_intake_20261114`. Line endings kept as found. Every change adds text; where "old text" is shown it is the anchor (the start of the line, or the sentence) that the new text follows, precedes or replaces. The files each zip must gain: `ZIP_ADDITIONS_INTAKE11.md`.

## LM8_PUSH

`C:\Users\user\Documents\longue_marche_pro_pilot_20261104\pro_prompts_draft_20261111\LM8_PUSH\PROMPT.md`

### T1. What is attached: new bullet for cotes 145 and 143 + 141

**Comes from:** EXPERT_ON_INTAKE_11.md (the Longue Marche expert, Claude Fable 5.2 at effort max) on intake section 11; cote 145, cote 143

**Old text (added at the end of the line that begins):**

```
- `referee/`: four referee reports on rows of these runs, by Claude Opus 5.5 at effort max, 14 November 2026. Each is a step-by-step check with the primary sour […]
```

**New text:**

```
- `archive_145_143/`: two cotes of the Grothendieck archive at Montpellier in first-pass transcriptions by GPT-6 Astra (ChatGPT Pro mode), 14 November 2026, with no second pass, each with the transcriber's research notes and doubts. `MPL_145_transcription.tex`: cote 145, the dossier "[C]", "Automorphismes extérieurs du groupe à lacets profini `π̂ = π̂_{0,3}`" (catalogued spring 1981; the Longue Marche, §41, resumes its calculations); its scans 5–12, 22–29 and 33–38 are also attached page by page in `pages_145/`. `MPL_143+141_transcription.tex`: cotes 143 and 141; cote 143, scans 29–33, "⑨ Une conjecture arithmético-géométrique", are also in `pages_143/`. The scans are the authority and are not attached; a reading inside `\unsure{…}` is doubtful. Tasks B.5, C.7 and C.8 use them.
```

### T2. Part B, task 5: the cartographic group, the generation criterion, the glued involution

**Comes from:** EXPERT_ON_INTAKE_11.md (the Longue Marche expert, Claude Fable 5.2 at effort max) on intake section 11; cote 145, cote 143

**Old text (added at the end of the line that begins):**

```
5. Determine the centralizer in `𝒫` of the class of complex conjugation, with its torsion and its multipliers (the tripod form of LM4 D.63–D.65, R22). Prove or  […]
```

**New text:**

```
 Cote 145, scan 23: the inverse image of `{1, τ}` (`τ` complex conjugation) in his extension is `C₂ * C₂ * C₂` on `τ_0, τ_1, τ_∞`, with `l_0 = τ_∞τ_1`, `l_1 = τ_0τ_∞`, `l_∞ = τ_1τ_0`; scans 28 and 29 attach the three lifts to the three arcs of the real locus. This is LM4 D.34 (R25) for complex conjugation. Prove or refute the generation criterion: an involution `α` of `𝒫` is conjugate to complex conjugation exactly when its three section classes contain involutions `t_0, t_1, t_∞` whose products are generators of the three inertia groups and which generate `F ⋊_α C₂` (a surjection of the completed `C₂ * C₂ * C₂` onto it is then an isomorphism, because a surjective endomorphism of `F` is bijective). The case to decide is the glued involution of Lead 23: prove or refute that it exists, and that its three lifts generate.
```

### T3. Part C, task 7: the dictionary with cote 145, corrected

**Comes from:** EXPERT_ON_INTAKE_11.md (the Longue Marche expert, Claude Fable 5.2 at effort max) on intake section 11; cote 145, cote 143

**Old text (added at the end of the line that begins):**

```
7. Prove or refute Lead 11. That `(T, W)` is a homomorphism on the multiplier-one subgroup of `GT̂₀`, and that `Δ` is a continuous character of `GT̂₀` that vani […]
```

**New text:**

```
 Prove or refute, with cote 145 (`archive_145_143/`): his pair `(γ, χ)` of scan 11 is the pair `(f, λ)` up to the gauge `g ↦ l_0^α g l_1^{−α}` (scan 7: `u(l_0) = l_0^p` and `uρ = int(g)ρu`, hence `u(l_1) = g l_1^p g⁻¹`, so `(p, g)` is `(λ, f⁻¹)` in his gauge and `g` is the cocycle, not a frame), and it is injective on his `Γ`, the commutant of `𝔖₃`, which is `GT̂₀`. The frames of E.65 are the conjugators by which an element moves the canonical splittings over the isotropy groups at `P` and at the harmonic points (scans 22 and 28); the frame of `r` is a primitive `A` of `g`, `g = A·ρ(A)⁻¹`. Determine `β` of scan 11 from the relation of scan 12, and prove or refute `β = ρ_F` of E.61.
```

### T4. Part C, task 8: the conjecture of cote 143 ⑨ and the preservation of the sections

**Comes from:** EXPERT_ON_INTAKE_11.md (the Longue Marche expert, Claude Fable 5.2 at effort max) on intake section 11; cote 145, cote 143

**Old text (added at the end of the line that begins):**

```
8. Prove or refute: `C^φ ⊆ ker Δ`. Then prove or refute: `C^φ = ker Δ`. The element of LM7_PUSH E.58 has `Δ = 1` (R24, refereed), so the first inclusion settles […]
```

**New text:**

```
 The conjecture of cote 143, scans 29 to 31 (`archive_145_143/`), fails at type (0,3) in both written forms: arrow (1) an isomorphism, which there says `G_Q ≅ 𝒫`; and, with the commutation with `𝔖₃` that his two margins ask for, `G_Q ≅ GT̂₀`. Prove it from R24, or give the exact error. Prove or refute: an element of `GT̂₀` that preserves the conjugacy classes of the sections of the harmonic and of the equianharmonic point has `Δ = 0`; an element of `C^φ` preserves them.
```

## LM6_POINTS_AS_SECTIONS

`C:\Users\user\Documents\longue_marche_pro_pilot_20261104\pro_prompts_draft_20261111\LM6_POINTS_AS_SECTIONS\PROMPT.md`

### T5. fifth block: cote 143, scans 2–12, and a new task of Part B

**Comes from:** EXPERT_ON_INTAKE_11.md (the Longue Marche expert, Claude Fable 5.2 at effort max) on intake section 11; cote 145, cote 143

**Old text (added before):**

```
## What the outcome must be
```

**New text:**

```
Cote 143 of the Montpellier archive with cote 141 (first-pass transcription by GPT-6 Astra, ChatGPT Pro mode, 14 November 2026; no second pass; attached as `MPL_143+141_transcription.tex` with its notes and doubts; the pages of scans 2–12 and 29–33 of cote 143 also singly, in `pages_143/`). Scans 2–12 are his own statement of what Part B asks. Scan 2: the extension of `Γ = Gal(Q̄/Q)` by `π_1`, under a hypothesis on the field of constants, and fields of definition as partial lifts, with a "grain de sel d'effectivité de descente" (doubtful reading). Scans 4–5: a point `ξ` gives "le germe seulement des `φ_ξ`", a section over an open subgroup taken up to restriction and geometric conjugacy, and "`ξ` est connu quand on connaît ce germe", through an embedding into an extension of an abelian variety by a torus and an abelian `H¹`. Scans 6–8: the "structure Kummérienne": the inertia maps at the boundary components, equivariant for the cyclotomic action, made into actual homomorphisms by points lifted to a covering; twice with the reservation "si `dim X = 1` sinon il faut revoir avec plus de soin la situation". Scan 12: "Programme": a complete group-theoretic description of `Γ` and of all these structures, with "bouchage de trous" and "forage des trous" to be made explicit. In Part B, state each of these as a statement and prove or refute it: the point is determined by its germ; the Kummerian structure in dimension one, and what replaces it at a crossing of the boundary; the passage to a finite étale covering (scan 12, "automatiquement").

Scans 29–31 of the same cote state "⑨ Une conjecture arithmético-géométrique": for `g = 0, ν = 3` it gives `Γ` as the group of outer automorphisms of `π_1(P¹ ∖ {0, 1, ∞})` that preserve the three inertia classes, and two margins ask in addition for the commutation with `𝔖_3`. Write `GT̂₀` for the group so obtained: the outer automorphisms of the free profinite group `π̂_{0,3}` that preserve the three inertia classes and commute with `𝔖_3`. LM7_PUSH E.58 and E.65 (GPT-6 Astra, ChatGPT Pro mode, 13 November 2026; refereed step by step by Claude Opus 5.5 at effort max, 14 November 2026: proved, the reports are attached as `referee/`) give a continuous character `Δ : GT̂₀ → F₂` that vanishes on the image of `G_Q` and is not zero; so the conjecture fails at type (0,3) in both forms. `C^φ` is the subgroup of `GT̂₀` cut out by the equation of §47 (cote 140-3, scans 234 and 240). This counts as a numbered task of Part B. **Part B, added task.** Determine the subgroup of `GT̂₀` that preserves the section classes of the points `1/2` and of a root of `λ² − λ + 1`; prove or refute that it lies in `ker Δ` and that it contains `C^φ`.
```

## EXIT_TOWER

`C:\Users\user\Documents\grothendieck_archive_montpellier\pro_prompts_archive_20261112\EXIT_TOWER\PROMPT.md`

### T6. Part E: new item (e), his questions of cote 143, scans 29–33

**Comes from:** EXPERT_ON_INTAKE_11.md (the Longue Marche expert, Claude Fable 5.2 at effort max) on intake section 11; cote 145, cote 143

**Old text (added at the end of the line that begins):**

```
(d) Lead 5 (d): prove what follows from Parts D and E (a)–(c) for the automorphism group of the whole system, with the dependence on the congruence subgroup pro […]
```

**New text:**

```
(e) Cote 143 of the Montpellier archive, scans 29–33, "⑨ Une conjecture arithmético-géométrique" (first-pass transcription by GPT-6 Astra, ChatGPT Pro mode, 14 November 2026; no second pass; attached as `MPL_143+141_transcription.tex` with its notes and doubts, the five pages also singly in `pages_143/`). He asks that `π_1(M_{g,ν}; ξ) → Autextloc°(π_1(X̄ ∖ {x_1, …, x_ν}))` be an isomorphism, adds in the margin the commutation with `𝔖_ν` and "une structure « locale » éventuelle", and ends with questions. Prove or refute each, for every type `(g, ν)`: (1) "`Autext(Γ_{g,ν}) = 1`" for the discrete group `Γ_{g,ν}` of scan 29, decided type by type from the literature, with the derivation; (2) "`Γ → Autext(Γ̂_{g,ν})`" is injective, `Γ = Gal(Q̄/Q)` and `Γ̂_{g,ν} = π_1(M̄_{g,ν})`; (3) it is bijective onto the automorphisms that commute with `𝔖_ν` and preserve the inertia: at type (0,3) this is false (LM7_PUSH E.58 and E.65, refereed by Claude Opus 5.5 at effort max, 14 November 2026, give a non-zero continuous character of that group which vanishes on Galois; the reports are attached as `referee/`), and for `(0, ν)`, `ν ≥ 4`, it is the question whether Galois is all of `GT̂`; (4) determine the automorphism group `G_{g,ν}` of the geometric modular topos `M̄_{g,ν}` (his "`G_{g,ν} = Im 𝔖_ν` ?", with "Sans doute `𝔖_ν` opère fidèlement sauf `g = 0, ν ≤ 4`").
```

### T7. Part E: the 'Done' line

**Comes from:** EXPERT_ON_INTAKE_11.md (the Longue Marche expert, Claude Fable 5.2 at effort max) on intake section 11; cote 145, cote 143

**Old text (replaces):**

```
Done for Part E: (a), (b) theorems; (c) four rows, each proved or refuted; (d) a conditional theorem with its hypotheses named.
```

**New text:**

```
Done for Part E: (a), (b) theorems; (c) four rows, each proved or refuted; (d) a conditional theorem with its hypotheses named; (e) four statements, each proved or refuted, (4) as a determination with its proof.
```

## PUSH_ITEMS_LM7_CONTINUED

`C:\Users\user\Documents\pro_intake_20261113\PUSH_ITEMS_LM7_CONTINUED.md`

### T8. S.5: the corrected dictionary with cote 145

**Comes from:** EXPERT_ON_INTAKE_11.md (the Longue Marche expert, Claude Fable 5.2 at effort max) on intake section 11; cote 145, cote 143

**Old text (added after):**

```
prove what the whole image is.
```

**New text:**

```
 The manuscript side, in the corrected form (cote 145; `pro_intake_20261114\EXPERT_ON_INTAKE_11.md`, by the Longue Marche expert, Claude Fable 5.2 at effort max, which corrects section 11 of the intake): his pair `(γ, χ)` of scan 11 is the pair `(f, λ)` up to the gauge `l_0^α g l_1^{−α}`; his `g` (scan 7, `uρ = int(g)ρu`) is the cocycle `f⁻¹`, not a frame; the frames are the conjugators by which an element moves the canonical splittings over the isotropy groups at `P` and at the harmonic points (scans 22 and 28), and the `r`-frame is a primitive `A` of `g`, `g = A·ρ(A)⁻¹`. `Δ` is a function of `γ`, but not of `γ` modulo 12: the `f` of E.58 lies in the nilpotent residual of `F′F³` while its `r`-frame is `5I` modulo 12. So the image asked for here is the image of the frames, not of `γ` reduced modulo 12. `β` of scan 11 is not identified; scans 8 to 12 decide it, and whether `β = ρ_F` of E.61 is to be proved or refuted. S.1 gains no route from cote 145: his coordinates are notation for S.1, not a method.
```

### T9. S.8: the dictionary in the repaired text

**Comes from:** EXPERT_ON_INTAKE_11.md (the Longue Marche expert, Claude Fable 5.2 at effort max) on intake section 11; cote 145, cote 143

**Old text (added before):**

```
The two referee reports are attached to the successor so that each repair can be made against the exact place.
```

**New text:**

```
- where the frames are introduced, the dictionary with cote 145 in its corrected form (S.5): `(γ, χ) = (f, λ)` up to gauge, `g = f⁻¹` the cocycle, the frames as the conjugators of the splittings of scans 22 and 28, `β` settled from scans 8 to 12.
```

### T10. attachments: cote 145

**Comes from:** EXPERT_ON_INTAKE_11.md (the Longue Marche expert, Claude Fable 5.2 at effort max) on intake section 11; cote 145, cote 143

**Old text (added after):**

```
notes link it to E.3
and to LM7_PUSH E.46).
```

**New text:**

```
 Also cote 145 (`returns\MPL_145_unzipped\`: transcription, notes, doubts; scans 5–12, 22–29, 33–38 page by page) and cote 143, scans 29–33 (`returns\MPL_143+141_unzipped\`).
```

## PUSH_ITEMS_20261114

`C:\Users\user\Documents\pro_intake_20261114\PUSH_ITEMS_20261114.md`

### T11. tower item 1.12: cote 145 as the origin of the splittings

**Comes from:** EXPERT_ON_INTAKE_11.md (the Longue Marche expert, Claude Fable 5.2 at effort max) on intake section 11; cote 145, cote 143

**Old text (added after):**

```
with the referee verdict for each.
```

**New text:**

```
 And the manuscript origin is named: the splittings behind LM7 D.25 and behind the frames of LM7_PUSH E.65 are those of cote 145, scans 22 and 28 to 29 (the canonical lifts of the isotropy groups at `P` and at the harmonic points `2, −1, 1/2`), with the corrected dictionary of `EXPERT_ON_INTAKE_11.md`: `(γ, χ)` of scan 11 is `(f, λ)` up to gauge, `g` is the cocycle `f⁻¹`, a frame is the conjugator by which an element moves such a splitting.
```

### T12. LM4 item 2.3: the generation form, with the glued involution as the test case

**Comes from:** EXPERT_ON_INTAKE_11.md (the Longue Marche expert, Claude Fable 5.2 at effort max) on intake section 11; cote 145, cote 143

**Old text (added after):**

```
is the same question in the
run's own terms.
```

**New text:**

```
 The generation form (cote 145, scan 23: for complex conjugation the extension is `C_2 * C_2 * C_2` on `τ_0, τ_1, τ_∞` with `l_0 = τ_∞τ_1`, `l_1 = τ_0τ_∞`, `l_∞ = τ_1τ_0`; confirmed by the Longue Marche expert, Claude Fable 5.2 at effort max): prove or refute that an involution `α` of the pure group is conjugate to complex conjugation exactly when its three section classes contain involutions `t_0, t_1, t_∞` whose products are generators of the three inertia groups and which generate `F ⋊_α C_2`. The test case is the glued involution (complex conjugation on one side, a conjugate of it on the other; the expert's hunch, LM8_PUSH Lead 23): prove or refute that it exists; if it does it has `Δ = 1`, so it is not conjugate to complex conjugation in `GT̂₀`, and whether it is conjugate in the pure group is whether its three lifts generate (LM4 D.76, D.77).
```
