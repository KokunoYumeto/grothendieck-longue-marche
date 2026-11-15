# Position paper, debate round 1: intake and register

By Claude Fable 5.2 at effort high (the agent of `INTAKE_ANABELIAN_149_FINAL_20261114.md` and
`INTAKE_LM6_FINAL_20261114.md`), 14 November 2026, 16:45–17:00 UTC (clock read at 16:45, 16:56 and 17:00). The returns are
by GPT-6 Astra (ChatGPT Pro mode); their statements are that model's claims. **(mine)** marks my own remarks; a
hunch is called a hunch. No code was run, no source opened.

Paths: `AP\` = `longue_marche_pro_pilot_20261104\answers\ANABELIAN_149_PUSH_final_20261114T1558Z_unzipped\
ANABELIAN_149_PUSH\sections\`; `LM6` = `...\answers\LM6_POINTS_AS_SECTIONS_final_20261114T1613Z_unzipped\
LM6_POINTS_AS_SECTIONS_paper.tex`.

## 0. Headline

1. Reading the proofs changed one thing of weight: **a new lever on A1 that the run stopped one step short of
   (mine).** A collision forces `p ∣ #J_D(L)/#J_C(L)` for every pointed cyclic étale cover `D` of odd prime degree,
   over every finite field `L` of definition. One cover whose Prym has no rational `p`-torsion proves A1 for that
   point. The run required `p`-rank zero and so needed a conductor of `2.4·10⁹` for two curves over `F_4`. The
   test reduces to point counts in cosets, and for `p > (2g − 2)²` it may give a general proof (section 4.1).
2. Everything I had left at statement level and have now read holds as far as I read: AP A.2, A.3, A.21, A.29l,
   F.43 (its valuation and detection steps), F.45 (all), F.47, D.32; LM6 B.14, B.15, F.29–F.31, B.38, B.41, A.10,
   A.46, A.61, A.62, B.12, B.28, B.34, C.5, F.8. Nothing wrong found.
3. For the tripod: residual irreducibility (mine), then two exact gaps; a hunch that the gap "finite ramification"
   is governed by the `lim¹` classes that the Fermat line keeps meeting (section 4.2).
4. The two successor drafts are written (section 6).

## 1. What I read in this round

- **ANABELIAN** (`AP\`): `A.tex` lines 108–279 (A.2, A.3), 1580–1691 (A.21), 4885–5127 (A.29l);
  `F_algebraic_constants_extension.tex` lines 330–482 (rest of F.45); `F_henselization_obstruction_extension.tex`
  (all, F.47); `F_solvable_closure_extension.tex` lines 95–331 (F.43: divisibility, detection, integrality);
  `D_modular_unit_obstruction.tex` lines 1–215 (D.32). Not read: D.29; F.44, F.46, F.48, F.49 (they repeat the
  template of F.43 and F.45, by their paragraph headings); the rest of F.43; A.19.
- **LM6**: lines 6009–6066 (B.14, B.15); 18021–18349 (F.29, F.30, F.31); 7628–7759 (B.38); 8122–8261 (B.41);
  4225–4474 (A.61, A.62 to (A46)); 599–725 (A.10); 2568–2627 (A.46); 5899–5930 (B.12); 6627–6672 (B.28);
  7068–7150 (B.34); 8605–8636 (C.5); 16961–16992 (F.8). Not read: B.29, B.39, B.40, A.56, F.45–F.47, F.20–F.22.
- **Cote 149, second pass**: the checked files of scans 35, 36, 52, 126, 127
  (`grothendieck_archive_transcription_20261110\second_pass\out\`).

## 2. The new mathematics, after reading

### 2.1 Finite fields (ANABELIAN Part A; scans 35–36)

- **A.2, A.3.** A collision is equivalent to his covering condition; the lift `Q′` with `p`-primary difference is
  unique (Hilbert 90 on a function with divisor `n(σR − R)`: the invariant divisor has degree divisible by the
  order of `σ`). Holds as far as I read.
- **A.21.** For a map `D → E` to a genus-one curve with a fibre of ramification indices divisible by `m`, colliding
  points have equal images: pull back by `[ℓ]`, take an `e`-th root, land on a hyperelliptic curve where A1 is
  known (A.19 for odd `p`; a direct Cartier computation for `p = 2`). Holds as far as I read; A.19 unread.
- **A.29l.** A displacement `g` between colliding points with the same image centralizes `s_P` in the orbifold
  group; the centralizer is finite (Frobenius weights), so it lies in one inertia group, and `P` is then a
  ramification point fixed by `g`. Holds as far as I read. It rests on a lemma of Boggi–Zalesskii (2019, Lemma
  3.1) on finite subgroups of pro-`𝒮` completions of orbifold groups: **an Astra and referee item**, given the
  other Boggi–Zalesskii step under examination.
- **A.C2.7, A.C2.19, A.C2.20** (read in the intake): hold.

### 2.2 Sections over `Q` (ANABELIAN Part D, LM6 Parts B, E, F)

- **LM6 F.31** (with F.29, F.30). Embed the finitely generated field in a `p`-adic field; the local theorem makes
  every map to a proper cover point-theoretic; covers of unbounded genus force constancy; so the geometric image is
  open, trivial or in one cusp. Holds as far as I read, on the local theorem and Carlson–Stix, Proposition 3.17.
  It is the engine of B.38, B.41, A.61.
- **LM6 B.38, B.41.** A generic section of a proper family over a `p`-adic base kills each inertia group, because
  `G_{k((t))} ≅ π_1(G_m)` receives the tripod and the image in a proper curve group is procyclic, hence trivial.
  Constant families then reduce to Mochizuki's Hom theorem. Holds as far as I read.
- **LM6 B.14, B.15** (and E.6–E.12, read before): hold. **AP D.30, D.31** (read before), **D.32**: hold.
- **LM6 A.61.** A section of the normalizer of a procyclic `A` and a Faltings retraction `T_ℓJ → A_ℓ` give a
  homomorphism from the group of a Jacobian with procyclic image; F.31 puts it in a cusp. Holds as far as I read.
- **LM6 A.10, A.46.** The involutions `1 − 2e_p` of the metabelian tripod group commute with `G_K` because the
  Galois action on the Alexander ring is by scalars and fixes `e_p`. Holds as far as I read, on Chen–Deligne's
  description of `Out(M)`. Whether it contradicts Yamaguchi's conjecture as printed needs the source.
- **LM6 B.34.** A tangential section at the cusp 2 of `P¹ ∖ {0, 1, ∞, 2}` maps to the point section of 2. The
  mathematics is trivial and right; that the preprint's Theorem F (ii) says otherwise needs the source.
- **LM6 B.12, B.28, C.5, F.8** (refutations of our prompt): all right. Each is a slip of the prompt's drafting.

### 2.3 Topoi (ANABELIAN Part F; scan 52)

- **F.45, complete.** The Kummer class of a point function is a unit up to a constant in `Q̄^×` at each point;
  comparing `φ`, `φ − 1`, `φ − b` at points of large degree removes the constants. Holds as far as I read.
- **F.43.** The trick that makes divisible constants harmless: an element `σz/z` lies in a fixed finitely generated
  field, where nothing is divisible. Detection of arithmetic quotients through `A_n ⊂ H^∞`. Holds as far as I read.
- **F.47.** `t ↦ t + t²` centralizes `G` of the henselization because `(1 + t)^{1/n}` lies in the field. Holds.
- F.44, F.46, F.48, F.49: unread; same template. **Astra item**: one line-by-line pass over F.24–F.49.

### 2.4 Second-pass readings of cote 149 that the rows touch

Scan 35: "pour être à l'aise [l'air]" (first pass: "pour Artin"); "th. 3 ou [en] de son cor."; margin "corps fini
parfait" (first pass: "profini"). Scan 52: "qui respecte la structure à lacets" (first pass: "Qcts|Dcts"): his
experiment is about automorphisms preserving the loop structure. Scan 126: `I_V` or `N_V`; "ce" struck. None
changes a verdict; the successor drafts quote the second-pass text.

## 3. What it means

- **For Grothendieck's sentence of scan 36.** He has `Q′ − P′` of `p`-torsion on every cover and hopes for `P = Q`.
  The return adds that this class has a free orbit under the deck group. With 4.1 the conclusion is within reach
  of counting: the Prym of every pointed cyclic cover would have to have rational `p`-torsion.
- **For Conjecture A (scan 56).** Proved, given the local theorem: for the affine Fermat curves, for `Y_1(N)`, for
  open subcurves in Stoll's range, for isotrivial curves over `p`-adic function fields. Open for the tripod; the
  two runs together reduce it to finite ramification and congruence rigidity (4.2).
- **For the other runs.** LM8_PUSH Part A is now the splitting of `1 → C → B → G_L → 1` (LM6 A.62). LM8_PUSH Part B
  and the E.65 chain: the metabelian involutions commute with Galois and do not lift to the third derived level
  (LM6 A.10, A.56); so the multiplier-one torsion of the metabelian level is not seen by `G_Q`-commutants above
  it. The Fermat line: LM6 E.12 settles the full profinite question for odd exponents (on the local theorem), and
  E.16, E.31–E.34, E.38 say no pro-`ℓ` nilpotent level does; the remaining content of §51.16 is the tower.
- **The big picture (mine).** Three times the same shape appears: a local theorem at every place plus a
  finiteness statement gives the global one (E.6 with Stoll; D.31 with units; F.31 through one `p`-adic place).
  What is missing each time is the finiteness input, and in the tripod case it is "finite ramification". The
  `lim¹` classes (LM7 E.32, LM8 F.21, LM6 E.38) are the one object in our registers that sees infinite
  ramification while vanishing at every finite level.

## 4. Where we are stuck, and how to get unstuck

### 4.1 A1: use rational torsion, not `p`-rank (mine; derivation checked by me only)

*Claim.* Let `P ≠ Q` collide on `C/k`. Let `L/k` be finite, `ℓ ≠ p` an odd prime, `χ : J_C(L) → Z/ℓ` non-trivial,
`D_χ → C_L` the pull-back of the Lang cover by the Abel map based at `P`. Then `p ∣ #J_{D_χ}(L)/#J_C(L)`.

*Why.* `D_χ` has the rational point `(P, 0)` and rational deck group. By A.3 there is `Q′ ∈ D_χ(L)` with
`T = [Q′ − (P, 0)]` of `p`-primary order, and `T` is `L`-rational. By A.C2.7, `σT ≠ T` (else `D_χ` is
hyperelliptic). So `(1 − σ)T` is a non-zero rational `p`-primary point of the Prym `im(1 − σ)`, which has
`#J_{D_χ}(L)/#J_C(L) = ∏_i L_P(χⁱ, 1)` rational points.

*What it buys.* The run asked for covers whose primitive part has `p`-rank zero (no geometric `p`-torsion) and
wrote that the rational version "would require a new controlled-field endgame" (report, "Universal
primitive-cover existence", §5). For prime degree there is no endgame. Modulo a prime over `p`,
`L_P(χ, 1) ≡ det(1 − Φ ∣ H¹(C, L_χ))`; in genus two the test fails only when `Σ_{x ∈ C(L)} χ([x − P]) ≡ −1`. A
random character fails with probability about `1/p^f`. If `p` is a primitive root modulo `ℓ`, a collision forces
the counts `N_b` of points of `C(L) − P` in the cosets `b` of `ℓJ(L)` to satisfy `N_b ≡ N_0 + 1 (mod p)` for all
`b ≠ 0`; with more cosets than points every non-zero coset holds a multiple of `p` points, and the Weil bound on
pairs gives a contradiction when `p > (2g − 2)²`. For composite degree the endgame of A.C2.20 gives the same test
unless `C` is a double cover of a genus-one curve.

*Hunch about the truth.* A1 is true, and provable along this line in most characteristics; the hard residue is
small `p` relative to the genus, with `p = 2`, `g = 2` the worst case, where the count must be done by hand or by
a finer estimate.

*Risk.* I may have missed why the run set this aside. The two steps (rationality of `T` over the field of the
cover; `(1 − σ)T ≠ 0`) are both in proofs I followed. Astra should check it first.

### 4.2 The tripod over `Q`

- *Residual irreducibility (mine).* LM6's proof of E.9 uses the Fermat curve only to get an invariant line. So a
  section of the tripod with `ρ̄_{s,ℓ}` reducible for one `ℓ ≥ 5` lifts to `Z_ℓ → X_0(4ℓ)` and is geometric by
  E.6; rational points do not have such isogenies. Hence `ρ̄_{s,ℓ}` is irreducible for every non-cuspidal section
  and every `ℓ ≥ 5`, modular of some level `N_ℓ` by Khare–Wintenberger, and D.30's finite ramification is the
  statement that the `N_ℓ` have bounded support.
- *What is really going on (hunch).* The abelian data `(A_s, B_s)` of a section are a solution of a "completed unit
  equation": `± ∏ q^{a_q}` with integer exponents tending to 0 in `Ẑ`, summing to 1 in every `Q_p`. I expect
  infinitely supported solutions to exist (Dirichlet and Weil, step by step); if so, no argument at the abelian
  level proves finite ramification, which explains why AP D.27–D.29 found only negative results. The first place
  where an infinitely supported solution can fail is the cup product `A ∪ B` in `H²_cts(G_Q, Ẑ(2))`: zero at every
  place and every finite level, a `lim¹` class. My hunch: it is not zero for infinitely supported solutions, or
  the weight-three class is not, and that is the proof of finite ramification.
- *After finite ramification (mine).* D.30 gives an elliptic curve; with Faltings it is `𝓔_{λ₀}` for a rational
  `λ₀`, and `s` agrees with `s_{λ₀}` modulo the congruence kernel of the level-two group. The rest of D1 is
  congruence rigidity of point sections, and the cusp-label problem of D.31 is its local face (a cuspidal section
  with parameter `λ₀^u` has the Legendre representation of the point). D.32 says modular covers cannot separate
  them; the Fermat covers, which are not congruence covers, can: `A_s` must equal `κ(λ₀)`.

### 4.3 F.9

Hunch: the criterion is F.39–F.40 (no automorphism of `k̄` centralizes `G_E`, for every finite `E/k`). Every
proved failure is produced by such an automorphism (F.41, F.42, F.47, F.48), and every proved success has none.
The test case is a henselian valuation with transcendence defect.

### 4.4 LM8 G.20 (through LM6 A.61–A.62)

The remaining extension `1 → C → B → G_L → 1` has `C` prime to `ℓ` and centralizing the line `P`. Hunch: it never
splits for non-cuspidal `A`, and such `A` do not exist; a proof must use that `B` sits in a curve group, since
A.63 gives an abstract non-split example. I have no route beyond what the run tried.

## 5. What Astra should grind next (whole tasks)

1. **The rational-torsion test** (4.1): prove or refute the claim, its composite-degree form, and the existence of
   a witness for every `(C, P)`; compute the test for all genus-two curves over `F_4`, `F_8`, `F_16` and all plane
   quartics over `F_3`, `F_5`. Items A2–A4 of `ANABELIAN_SUCCESSOR_DRAFT`. Background: `AP\A*.tex`, the report.
2. **The completed unit equation and its phantom class** (4.2): items A3, A4 of `SECTIONS_OVER_Q_DRAFT`, with LM7
   E.32, LM8 F.21, LM6 E.38.
3. **Residual irreducibility and congruence rigidity**: items A2, A5 of `SECTIONS_OVER_Q_DRAFT`.
4. **Line-by-line checks** (referee work for Astra): AP A.19 with A.13–A.18; Boggi–Zalesskii 2019 Lemma 3.1 as
   used in A.29l; AP F.24–F.49 as one chain; LM6 B.39, B.40, A.56; the certificates of AP A.C2.25–A.C2.26
   (superseded if item 1 succeeds); the source statements behind LM6 A.46, B.34, D.6 and AP D.30 (Pan).
5. **F.9**: items F1–F3 of `ANABELIAN_SUCCESSOR_DRAFT`.

## 6. Prompt changes

**Made (new files, mathematics only; the main session adds the frame):**
- `longue_marche_pro_pilot_20261104\pro_prompts_draft_20261111\SECTIONS_OVER_Q_DRAFT\ITEMS_DRAFT.md`: what is to
  be settled; his text; conventions; R1–R14 (rows of both returns with what was read); Leads L1–L6 (mine); Part A
  (A1–A6, the tripod), Part B (B1–B3, birational lifting), Part C (C1–C4, finiteness, fields, `x⁴ + y⁴ = z⁴`);
  background list.
- `grothendieck_archive_montpellier\pro_prompts_archive_20261112\ANABELIAN_SUCCESSOR_DRAFT\ITEMS_DRAFT.md`: the
  same structure; R1–R9; Leads L1–L6 (the rational-torsion test and its count); Part A (A1–A6), Part F (F1–F4,
  with his experiment of scan 52 in its second-pass reading); background list.
No existing prompt was edited, so there is no backup file.

**Proposed for prompts I do not own:**
- **LM8_PUSH** (cross-run owner). Part A: restate from LM6 A.21, A.36, A.50–A.53, A.61, A.62, A.65: the item is
  the splitting of `1 → C → B → G_L → 1` inside the curve group; add A.63 as the abstract counterexample. Part B:
  add LM6 A.10, A.11, A.49, A.54–A.59, A.66, A.67 and the open row A.12; add AP C.7h to Part A as in section 14.3.
- **EXIT_TOWER** (cross-run owner): LM6 C.12–C.19, flagged as resting on Boggi–Zalesskii 2024 Theorem A.
- **Fermat successor** (`PUSH_ITEMS_20261114.md` Part 1; Fermat owner): LM6 E.12 as settled for full profinite
  sections of odd exponent (on the local theorem), so that the successor asks for the tower only; LM6 E.13–E.39 as
  its state and E.21 as the open row; E.38 beside LM7 E.32; and my 4.2: the same `lim¹` classes on the tripod.
- **Any reuse of the R27 wording**: "pinned" is closed-point-preserving (AP report lines 1613–1621; LM6 report
  line 905).
- **Report to OpenAI**, after a check: LM6 D.6 (a gap in a density step of Section 8 of the local-theorem paper).
- **Manuscript participant**: the second-pass readings of 2.4, for the companion notes on scans 35–36 and 52.

## 7. Corrections to my own intakes

- `INTAKE_ANABELIAN_149_FINAL`, 3.3 (3) and 5 (a): the "cheaper target" I proposed (a theta point of prime order)
  is superseded by 4.1, which needs no theta point.
- `INTAKE_LM6_FINAL`, section 6: the D-item of the ANABELIAN successor is now in `SECTIONS_OVER_Q_DRAFT`, as
  proposed there; both drafts exist.
- Verdicts raised from statement level to "holds as far as I read": the rows listed in 0.2.
