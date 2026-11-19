# LM4_SUCCESSOR, final return (checkpoint 40): bounded intake

Intake by Claude Fable 5.2 at effort high, 17 Nov 2026 (step 2 of the field-expert workflow; no sub-agents).
The run: GPT-6 Astra (ChatGPT Pro mode), started 16 Nov 2026 00:49:30 UTC, stopped its mathematics at its
hour-40 review (its own record: 17 Nov 18:49:49 UTC; the folder name says 18:14Z), marked INCOMPLETE.

- Return: `<local>/Documents\longue_marche_pro_pilot_20261104\answers\LM4_SUCCESSOR_checkpoint_40_20261117T1814Z_unzipped\LM4_SUCCESSOR\`
- Prompt as sent: `<local>/Documents\github_backup_20261113\grothendieck-longue-marche\raw\pro_returns\LM4_SUCCESSOR_checkpoint_40_20261117T1814Z\PROMPT.md`
- Progress reviews: not at the top of `records\`; they are inside `historical_data.tar`
  (`LM4_SUCCESSOR/records/progress_review_03h.md` … `_37h.md`, `_39h.md`, `hour39_scheduled_review.json`,
  `hour40_scheduled_stop_review.json`, `final39_research_report.md`, `work_A/main_A_progress_assessment39.md`,
  `work_CE/main_B_surjectivity_bridge_assessment38.txt`). There is no review for hour 38 (a missed capture slot).

**What I checked myself, and what I report from the run.**
- Checked by me: the register counts (401 rows: 357 Proved, 19 Refuted, 19 Open, 6 Known; by Part: A 138, B 178,
  C 44, D 17, E 24); the 49 task rows of the report table (15 Proved, 3 Refuted, 1 Known, 30 Open); the status
  history of every row through all 37 registers kept in `historical_data.tar` (checkpoints 1–37) and the final;
  the finite counterexample of C.34 (my own program: `f = 1`, `λ ≡ 7 mod 24`, `x = (2 3 4)`, `y = (1 2 3 4)` in
  `S₄` fails the hexagon, `λ = ±1` pass); the arithmetic of E.38 (the fourteen family sizes sum to 1620 and give
  16 orbits if the family of 360 is three free orbits); the build log (0 overfull boxes, 762 pages; pages not
  rendered by me).
- Everything else is reported from the register, the report, the reviews and the two final assessments. I read no
  proof in the 762-page paper. Nobody outside the run has checked any of it.

## 1. Verdicts

### The final state

| Question | State | The exact remaining gate (reported from the run) |
|---|---|---|
| **Main A**: every involution of `𝒫`, `GT̂₀`, `GT̂` conjugate to `c` | **Open** (A.14) | For `α = (−1, f)` with its unique `u` (`u = f·α(u)`): `α ~ c` exactly when `x^d u⁻¹ y^d u ~ (xy)^d` for the one unit `d = d_α` read from the dihedral quotient (A.39, A.45). For `α ∈ GT̂`, `u` satisfies the pentagon (A.37) and the equation is equivalent to the hexagon for `(d_α, u)` (my reading of A.6, A.36, C.30 and the last clarification of A.138). In the run's last coordinates: `α(N) = N` for `N = (vδ^d)³`; proved is only `α(N) = vN⁻¹v`. |
| **Main B**: `𝒦 = 1` (the centralizer of the icosahedral `A₅` in `Γ̂_{0,[12]}` is finite) | **Open** (B.38, B.39, B.34) | Global: the uniform finite-cover condition (B.75.6) for the crossed map `δ(g) = s̄gs̄⁻¹g⁻¹ : G_V → B₄(S_{0,4})`, whose completed zero set is exactly `𝒦` (B.75). Local form reached at the end: `𝓘 = 𝒦_loc^δ`, that is `∂(𝓘) = ker(H¹(C₂, 𝒩) → H¹(C₂, 𝒦_a))` (B.164–B.166). No non-trivial element of `𝒦` was built. |
| **Coherent class / CM parity** (is `Δ = 0` on the involutions of `GT̂₀`, of `GT̂`) | **Open** (A.13) | `(−1)^{Δ(α)} = ε_A·ε_u` (A.105); for `α ∈ GT̂`, `ε_u = d mod 3`, so `Δ(α) = 0 ⟺ ε_A = d mod 3`. The class `ω_α ∈ H¹(C₂, T_e)` of A.111 has signed image `(−1)^{Δ(α)}`; neither is evaluated. |

The 49 task rows: **Proved 15** (Leads 1, 2, 5; A.2, A.7; B.1, B.2, B.8, B.3.P1–P3; C.4; D.1; E.2, E.3),
**Refuted 3** (A.3; B.3.P4; B.3.P7), **Known 1** (A.1), **Open 30** (Leads 3, 4, 6, 7, 8; A.4, A.5, A.6, A.8;
B.3, B.3.P5, B.3.P6, B.4 and all of B.4.a–h, B.5, B.6, B.7; C.1, C.2, C.3; D.2, D.3; E.1). Task labels and
statement ids overlap: task C.4 is Proved, while statement C.4 is the Open row that answers task C.1. Below, an id
is a statement of the register unless it is called a task.

### Results that are new and matter (reported; ids of the final register)

Involutions (Part A, with C.28–C.44):
- **A.2, A.3, A.34** (Leads 1, 2): `𝒫 = lim_U Out^♯(F/R_nil(U))`, conjugacy is detected level by level; lifting over
  any closed normal relative kernel is decided on the central quotient `F/[N, F]`.
- **A.6**: `C_𝒫(c) = N_𝒫(⟨c⟩) = {1, c}`; a conjugator from `c` to an involution of `GT̂₀` lies in `GT̂₀`.
  **A.36**: the same for `GT̂` (so for an involution of `GT̂` the three conjugacy questions are one).
- **A.7**: `H¹(C₂, ker λ)` has continuum many classes (`Ẑ^×/±1` embeds), all in one conjugacy class, `Δ = 0` on them.
- **A.11, A.39, A.45, A.37**: conjugacy to `c` ⟺ a reflection triangle ⟺ one third-cusp equation at `μ = ±d_α`;
  for `α ∈ GT̂` the word `u` satisfies the full pentagon. The equation is **not** detected by the maximal pro-`p`
  quotients (an `S₄` witness with a mixed-sign multiplier).
- **A.25, A.31**: one element `a ∈ GT̂₀` with `λ = −1`, `Δ = 1`, whose image is an involution at every relative
  principal-congruence level `12 | N`. The tower is not cofinal (its common kernel maps onto `A₇`); `a` itself is
  not proved to be an involution. This is Lead 3 at every congruence level, not Lead 3.
- **A.18, A.70, A.74, A.76, A.79, A.81**: R2 (LM7_PUSH D.50) has no order-preserving form. A.79: one finite
  action that passes every iterated source-central refinement with involutions, has an ordinary full lift, and has
  **no** full involutory lift for any choice of frames. A.81: the same at infinitely many fresh primes after the
  first refinement. These are ghosts in our sense: every tested level passes, no full object exists.
- **A.100, A.101, A.103**: for an involution of `GT̂` the pentagon forces the hexagon in the full Alexander ring
  and in every signed congruence image. **A.105, A.111**: the CM parity as a product of two frame signs.
- **C.28**: for every pure negative involution of a punctured sphere group, `n + 1` section classes, each
  self-centralizing, in the full profinite group. **C.30, C.31**: a unit pair with duality and hexagon is an
  automorphism; every endomorphism of the profinite parenthesized-braid operad has a unit multiplier (the `GT̂`
  monoid is a group). **C.34**: the literal prescribed-root form of Furusho's Question 14 is false (checked by me
  at the finite level). C.31 and C.34 need a literature check before anything is called new.

Icosahedral centralizer (Part B):
- **B.1–B.3**: the analysis of R5 stands (the last equality of both published proofs is the statement); the
  solvable case is repaired through the normalizer; the exact obstruction is a class in `H¹(H, U)` dying in
  `H¹(H, Û)`. **B.36**: no proved statement of our attached returns uses the nonsolvable equality.
- **B.4–B.7** (R6 proved): `K̂` characteristic; the peripheral centralizer of `A₅` is `{Φ ∈ GT̂₀ : λ ≡ ±1 mod 5}`;
  `C_{Γ_{0,[12]}}(A₅) = 1`, so the profinite centralizer is exactly `𝒦`, pure and torsion-free.
- **B.8–B.10** (P1–P3); **B.53** (the two quintic resolvents, the third target corrected); **B.55** (both are not
  the identity on `GT̂₀`); **B.25, B.37**: `𝒦_N = 1` for `N = 2, 3, 4, 6`.
- What a non-trivial `𝒦` would have to be: inside the closure of `[P, P]` (B.58, integral split injection
  `Z⁵⁴ → Z¹⁶⁸`); dead in `PSp₁₀(F₃)` (B.62); `𝒦 ∩ G_Q = 1` (B.10); abelian ⟹ trivial (B.33); every Sylow subgroup
  free pro-`p` of rank ≥ 2, centre trivial (B.50); a nonabelian pro-2 Sylow, no stable pro-odd part,
  `C_𝒦(c) = 1` (B.51). **B.72**: `H_T ∩ gH_5g⁻¹ = 1` for every `g` in the discrete group.
- What no linear test can decide: **B.23** (the congruence centralizer in the Deligne–Mostow lattice is an infinite
  compact torus), **B.64** (the whole 3-adic Eichler group is in the common image), **B.66** (a common prounipotent
  line at every prime). The solvable controls show the same picture and have `𝒦_N = 1`.

Parts C, D, E: independent proofs of LM4 D.42, D.70, D.74–D.78 (C.5–C.23), of LM4 C.88, C.90–C.92 (D.1–D.6), of
LM6 C.13–C.19 as audited (E.1–E.9), of LM4 D.28 for `𝒫` (E.50, E.51); the census of five points against cote 148
(E.30–E.40: 542 objects in 9 families; 1620 arrows in 14 families, which are 16 `S₅`-orbits).

### Refutations that matter outside this run

| Id | What falls | Where it matters |
|---|---|---|
| A.5 | The conjugator `ψ` of R1 does not preserve the class of `z` on `F/R_nil(F)` (quotient of order `7⁵`) | LM4 companion at D.32/D.34; the successor must not restate task A.3 |
| A.18 (with A.70, A.74, A.76, A.79, A.81) | No equivariant or order-preserving refinement of R2 | Every prompt and note that builds an element "by R2 with a further property": Lead 3, the `Δ = 1` constructions, `UNSTUCK_LM_EXPERT.md` on F.9 |
| B.42–B.45 | "The element of E.58" is a set of lifts; tripod and resolvent values vary over it; at most one lift can lie in `𝒦` | Every text that says "the element of E.58"; `UNSTUCK_LM_EXPERT.md` ("test every condition against the element of E.58") needs invariants constant on the lift set |
| B.54 | R2 cannot always be carried out inside the braid image | Task B.4(h) as posed |
| B.11/B.53, B.16, B.17/B.57 | P4's third quotient is `C₃ * C₃`; P7 false, graded (weight 4) and full | `POINCARE_AND_A5_20261114.md` (R7), any companion carrying P4, P7 |
| B.22 | Lead 7's three linear characters do not exist on the stated domain (semilinear; restrict to `λ ≡ 1 mod 6`) | `MOONSHINE_DICTIONARY_20261114.md` |
| B.47 (Known, Minasyan 2023), B.67, B.69, B.76, B.80, B.88 | One closed product does not give the intersection of closures; the rigid tests are not injective, discretely or completed | Routes B.4(a), B.4(c) as posed; Lead 5's hoped injectivity |
| A.21 | Real projectivity with an open `F̂₂` does not give recognition as a graph of finite groups | Any "virtually free, hence recognized" argument for Main A |
| C.2 | The structure in LM4 D.78 does not force `K′ = 1` | LM4 companion |
| C.34 | Furusho's Question 14, literal prescribed-root form | DELTA_ON_GT, GT_TOWER_CHECK texts that cite it |
| E.32, E.38, E.39 | Three statements read on cote 148, scans 31–36 (orders 6 and 10 occur; 16 orbits, the word after "14" struck out; the square pyramid has a real structure) | The edition notes of cote 148; DELTA_ON_GT task B.3 asked the same count. The run says it inspected the original scans, which were not attached: check against our scans first |
| A.1 (Known) | Collas's genus-one theorems are for the subgroup `IΓ`, not for all of `GT̂` | Any citation of Collas for `GT̂` in genus one |

## 2. The 19 open items

**They are the same 19 rows as at checkpoint 32, and as at checkpoint 3.** The only status change in the whole
run is B.17, Open → Refuted, at hour 3. The last refutation is from hour 19 (B.98, B.100); from checkpoint 20 on
all 132 added rows are Proved. Parts D and E have no row after hour 2 and hour 1; Part C none after hour 9.

| Row | What the run tried | Where it stalled | What I would try next |
|---|---|---|---|
| **A.14** (Main A) | A.36–A.46, C.35–C.42 (all `S₄`, `A₅`, dihedral, relative pro-2 tests pass); A.82–A.104 (augmentation modules, Fox and Alexander forms of the hexagon); A.106–A.118 (congruence and central towers, not cofinal); A.121–A.138 (Enriquez's elliptic section, elliptic cubic, annular images) | `α(N) = N`; "inverse-conjugacy does not imply fixedness … a genuinely different mathematical input is required" (its own assessment) | Q3 and Q4 of section 5. For `𝒫` and `GT̂₀`, aim at a refutation first (A.79, A.81 show how finite actions obstruct) |
| **A.12** (levels, Lead 3) | A.9, A.10 (odd primes: locally conjugate); A.16–A.35; the towers A.40–A.78 | The norm equation `u·t(u) = t⁻²` in the non-congruence kernel; no cofinal tower | Q3: one cohomological criterion for the whole kernel in place of layer-by-layer towers |
| **A.13** (CM parity) | A.24, A.25, A.31, A.32, A.105, A.109–A.113, A.117, A.119, A.120, A.124–A.127 | `ε_A = d mod 3` not evaluated; in `GT̂₀` no full involution with `Δ = 1` | Q6: if `Δ = 0` on `GT̂` stands (EXIT_TOWER E.49, checked in GT_TOWER_CHECK), the `GT̂` half is closed by A.105 |
| **B.38, B.39, B.34** (Main B; `𝒦_N`; Conjecture 2⁻; `𝒦` abelian) | B.56–B.75 (rigid tests, class two and three, symplectic images, the cocycle form); B.76–B.178 (about a hundred statements on explicit presentations of deletion kernels, necks, contacts and their completions) | The surjectivity `𝓘 = 𝒦_loc^δ` and the uniform condition B.75.6; the last words `w`, `w₂` lie in the image already known. `N = 7, 11` not started | Q1 (the free 62-point case), Q2 (virtual join), Q7 |
| **B.12** (P5 on all of `GT̂`) | B.53, B.55; Nakamura–Schneps and Hoshi–Mochizuki–Tsujimura read at the definitions | No proof that every element of `GT̂` satisfies the resolvent identity | Ask GT_TOWER_CHECK's result: an action of `GT̂` on the tower compatible with special loci would give it |
| **B.26** (lattice, Lead 6) | B.21, B.23–B.25 | The nonabelian `H¹(A₅, ker(Γ̂ → L_ℓ))` | Low priority: the 4- and 6-point controls have the same torus (B.25). Only useful as a side-by-side computation of the obstruction class at 6 and at 12 points |
| **B.27** (Jacobi sums, Lead 7) | B.21, B.22 | Not computed | Low priority until Main B moves |
| **B.40** (relative images at `U = K`, `K′K^p`) | B.20, B.54 | Not computed; bad primes untouched | Low priority |
| **B.41** (`Δ` on `𝒦`, further orbits) | B.10 only | Conditional on `𝒦 ≠ 1` | Becomes the centre of Q1 |
| **C.4** (`K′ = 1`, LM4 D.78) | C.1–C.3, C.12, C.25; A.130 (the kernel is trivial for the torus action built from a negative involution of `GT̂₀`) | No proof that `K` is finitely generated or abelian in general | Extend A.130's argument to every negative torus involution; C.25's free-factor route |
| **C.14** (torus conjugacy) | C.8, C.13, C.27, C.43, C.44, A.129 | The same full-profinite conjugacy as Main A | With Main A |
| **C.26** (scalar cubic) | C.16, C.24 | The linear obstruction is unavailable (C.24) | The Frobenius quotients of LM4 D.71, D.73 as joint constraints |
| **D.9–D.12** (noncompact level-zero comparison) | D.1–D.8, D.13–D.17; Yagasaki 2014, 2018 read | D.17 fills through maps with a uniform tail, not through homeomorphisms; no loop built from D.6 | A prompt of its own in geometric topology; nothing was done after hour 2 |
| **E.10** (genus-three real kernels) | E.1–E.9 | The congruence kernel of genus three (the congruence subgroup problem, open) | State it conditionally; no work after hour 1 |

**Do the 54 statements of checkpoints 33–40 move an open item?** (A.103–A.138, B.161–B.178.) By the run's own
final assessments, no: on A "an exact reformulation, not a new decision"; on B they "refine … the internal kernel
of an already known image". Three of them have value for us all the same: **A.105 with A.111** (the `GT̂` half of
A.13 is now one sign equation, which another run may already decide); **A.130** (a real partial case of C.4);
**B.164–B.166** (the clean cohomological statement of the local gate). The rest is detail on the two routes the run
had chosen: the elliptic route for A and the explicit presentations for B.

## 3. The three-hour check

**What happened.** 36 reviews (hours 3–37 and 39), every one CONTINUE; STOP at hour 40. The open rows did not
change after hour 3.

**The criterion it applied** was topical: is the work about the main questions, in the full profinite group,
and not a census. Its own words:
- hour 3: "The current work directly advances the two main questions … stop and deliver an honest INCOMPLETE final
  package if activity has become detail away from the main or requested open questions."
- hour 16: "These results change the remaining obstruction; the work has not become a finite census or detail away
  from the main question."
- hour 36: "These are direct structural steps toward the main decisions, so this is not a cycle spent only on
  remote side cases or another finite census."
- hour 39: "These are main-directed structural advances, not additional finite shadow tests."
- hour 40 (STOP): "Latest auxiliary results refine exact reformulations and the internal kernel of an already known
  image; no current argument moves either main decision."

**Why it kept deciding CONTINUE.**
1. The prompt's check has two cases, "moves the main question … forward" and "filling in detail away from the
   main question". Work that is about the main question and does not decide anything fits neither. The run filed it
   under the first: a sharper obstruction, a closed route, an equivalent form all counted as "moves".
2. Nothing in the check is measured. It never asks whether a row changed status, so 37 hours with no change passed it.
3. The push rule and rule 4 of the prompt pull the other way ("Do not deliver while an item is undecided and an
   untried approach remains"; "Keep working until then"), and the prompt lists dozens of routes, so an untried
   approach always remained.
4. The review was written by the process that had planned the hour, as a justification of that hour. The stop came
   when two of its sub-processes wrote assessments of their own branches and both said the branch had reached a
   reformulation.
5. The prompt's ban on finite, metabelian and census work gave it a ready test of what "detail" means; anything
   else passed.

**What the check should say instead (for the methodology and the template).** Make it a ledger, not a judgment
of relevance: *"After three hours, and every hour after that, write at the top of the report, before anything
else: (a) every Open row and every undecided task line, each with the hour at which its status last changed;
(b) for each main question, the gate: the one exact statement whose proof or refutation decides it, and whether it
is the same statement as at the previous check. Work has moved a question only if, since the previous check, an
Open row or a task line became Proved or Refuted, or the gate was replaced by a statement that you proved to be
strictly weaker and still sufficient. A statement that makes an obstruction exact, restates the gate in another
form, closes one route, or describes an auxiliary group has not moved it, however close to the main question it
is. If no main question has moved at two checks in a row, stop new mathematics, write the final package with each
gate, each route tried and the input you would need, and deliver it. This check takes precedence over the
sentence about untried approaches."* The two parts that do the work are the dated ledger and the sentence that
says reformulations do not count.

**A second finding for the template: the checkpoint paragraph.** "The final ZIP holds everything the checkpoints
held" and "never overwrite" were read as: every checkpoint carries every byte of every earlier one, page images
included (196,804 retained file identities; the unzipped final is about 1.9 GB, of which the paper PDF is 5 MB). From
about hour 25 the size of the package was a recurring task, and at hours 36–39 it went over a 512 MiB limit; the
run built three TAR containers and its own compression and verification code, rebuilt its workspace at hours 7
and 32, missed the hour-38 slot, failed the hour-39 size gate twice, and a large part of its late reviews is
packaging. The paragraph should say: a checkpoint holds the current
version of each deliverable and record; earlier versions stay in the earlier ZIPs, which we keep; do not copy
earlier checkpoints or rendered page images into later ones.

**A third: the breadth of the prompt.** 49 task lines with eight sub-routes under B.4. Parts C, D and E got their
rows in the first hours and nothing after hour 9, 2 and 1; eight of the nineteen open rows (C.4, C.14, C.26, D.9–D.12, E.10) got no further row in their own
Part (A.129, A.130 touch tasks C.1, C.2 at hour 37).

## 4. Implications and prompt updates (listed; no prompt edited)

**`04_ANABELIAN_A1_SUCCESSOR\PROMPT.md`** (unsent; read: its items are A1, G1, S1–S6, A12, B1, B2, N1–N4, B4, B5,
B6, B8). None of the 49 task lines of LM4_SUCCESSOR is an item there, and nothing in this final changes its Part A.
- **N2** (LM6 A.22, a procyclic subgroup with open arithmetic normalizer): add as tools, to be re-proved where
  used, **B.29** (such a subgroup is cuspidal or has no component at the primes whose Frobenius is a complex
  conjugation; it also corrects the citation in LM6 A.14) with **B.31–B.33, B.50, B.51**. Background files: the
  register rows and `work_CE/B_arithmetic.tex` of this return (LaTeX, no PDF).
- **N4** (Hoshi–Mochizuki 2011, Theorem C): as context, the source reading in **B.12** (Nakamura–Schneps 2000,
  Theorem 1.1, 1.2 are statements on the Galois image; Hoshi–Mochizuki–Tsujimura 2025, Definition 3.3 keeps its
  extra conditions).
- Its progress-check paragraph (line 56) and its checkpoint paragraph (line 72) are word for word the ones that
  failed here: apply section 3 to both before it is sent.

**`pro_prompts_draft_20261111\08_SECTION_GHOSTS\PROMPT.md`** (unsent; I read its head and searched it, not the
whole text). Add as background and as models to test against: **A.79, A.81** (compatibility through every
iterated central refinement plus an ordinary full lift, and still no full involution), **A.18, A.70, A.74, A.76**
(no equivariant R2), **A.31** with its caveat (a non-cofinal tower), **B.42–B.45** (E.58 is a lift set). The same
two paragraphs of section 3.

**Returns already in (DELTA_ON_GT, GT_TOWER_CHECK, EXIT_TOWER; not read by me): cross-checks for their intakes.**
- A.105/A.111 against EXIT_TOWER E.49 and GT_TOWER_CHECK's verdict on it (section 5, Q6).
- E.30–E.40 against DELTA_ON_GT task B.3 (the same lists on cote 148): two runs, one count to compare.
- B.42–B.45 against DELTA_ON_GT task B.5 ("the automorphism of LM7 D.46 … its lift is an element").
- A.121 uses Enriquez (2014), Proposition 2.20, for elements of `GT̂` in genus one; EXIT_TOWER claims an action of
  `GT̂` on the whole tower. Compare the inputs.

**A successor of this line** (to be designed by the field expert; my list of what it should carry):
- Main A alone, with C.1–C.3 (the same problem on the torus): gates A.39/A.45 and `α(N) = N`; tools A.2, A.3, A.34,
  A.6, A.36, A.37, C.28, C.30, C.31; the refuted routes A.5, A.18, A.21, A.79, A.81 named so they are not retried;
  the elliptic route (A.121–A.138) marked as tried, with where it stopped.
- Main B alone, with B.5 and B.6: gates B.75.6 and B.164–B.166; tools B.1–B.10, B.25, B.33, B.50, B.51, B.58, B.62,
  B.72; the routes that cannot decide it named (linear images: B.23, B.64, B.66; rigid-test injectivity: B.56,
  B.67, B.69; one closed product: B.47); the explicit-presentation route B.76–B.178 marked as tried.
- Part D and task E.1 leave this line (a topology prompt; a conditional statement). Leads 6, 7 and B.4(d), (e), (h)
  drop to background.
- Background files to attach: `LM4_SUCCESSOR_results.csv`, `LM4_SUCCESSOR_paper.tex` with `sections/`,
  `work_A/`, `work_CE/`, `work_DE/` TeX, `LM4_SUCCESSOR_references.bib`, `final39_research_report.md` and the two
  final assessments (from `historical_data.tar`); no PDF, no tar of images.

**Companions and records.**
- LM4 companion: R1 gains A.5, A.6, A.7, A.39, A.45; LM4 D.42, D.70, D.74–D.78, C.88, C.90–C.92, D.28 now have a
  second proof by the same model family (not an independent check); LM6 C.13–C.19 likewise.
- Cote 148 edition notes: E.32, E.38, E.39 after a look at our scans 31, 33, 35.
- Informing authors (Boggi, Zalesskii): B.1 agrees with the note of Claude Opus 5.5 at effort max; B.39 says the
  published statements are neither repaired nor refuted; B.36 says none of our proved rows depends on them.
- Before any publication: the proof-check record (nobody has checked a proof), and step 2 of the PDF check.

## 5. Hunches, as questions (all mine, unchecked)

**For GPT-6 Astra (ChatGPT Pro mode).**

- **Q1 (Main B and Conjecture 2⁻: the free case).** Puncture the sphere at all three singular orbits of `A₅`
  (12 + 20 + 30 = 62 points). The action is free and the quotient is the tripod, a triangle orbifold. B.39 says
  the free-action proof in Boggi's Section 3.1 does not use the unjustified step. *Check that proof for `A₅` on
  62 points. If it holds, the centralizer of `A₅` in `Γ̂_{0,[62]}` is finite: a nonsolvable triangle case where
  the closure equality holds, so Conjecture 2⁻ ("if and only if solvable") is false as stated, and Main B becomes
  one lifting question: is the `A₅`-equivariant forgetful map `C_{Γ̂_{0,[62]}}(A₅) → C_{Γ̂_{0,[12]}}(A₅)` onto?
  `𝒦` is then exactly the set of centralizing classes that do not lift along the orbits of 20 and 30 points
  (task B.7 turned round).* Why: the run treated only the 12-point instance; this one may be decided by a proof
  already in print, and it tells us where the user's hunch can still live (the cases where `A₅` has fixed points
  on the punctured surface). I have not opened Boggi's paper; this rests on B.39 and R5.
- **Q2 (Main B: the virtual join).** `𝒦 = closure(H_T) ∩ closure(H_5)` with `H_T ≅ F₁₃`, `H_5 ≅ F₆` the stabilizers
  of two Teichmüller discs that meet in one point, and `H_T ∩ gH_5g⁻¹ = 1` for all `g` (B.72). *Prove that
  finite-index subgroups `H_T′`, `H_5′` generate their free product `M` (ping-pong at the icosahedral point), then
  decide whether `M̂ → Γ̂_{0,12}` is injective on the set `Ĥ_T′·Ĥ_5′`; in the free profinite product the two factors
  meet trivially, and `𝒦` is torsion-free, so that gives `𝒦 = 1`. Tools: Minasyan's criterion (B.46),
  Minasyan–Mineh on virtual joins in relatively hyperbolic groups, the separability criterion of B.48 applied to
  `F₁₁ ⋊ M`.* Why: route B.4(c) was worked through deletion kernels for a hundred statements and never formed the
  join; this replaces "identify a presentation kernel" by one separability statement about one free group.
- **Q3 (Main A in `GT̂₀`, Lead 3: one criterion in place of towers).** Put `ε` = the sign of `λ` and
  `E_Δ = {g ∈ GT̂₀, λ(g) = ±1 : Δ(g) = ε(g)}`. An involution with `Δ = 1` exists exactly when `E_Δ` has torsion.
  *Decide whether `E_Δ` is torsion-free. Two handles: (i) if there is a continuous homomorphism from
  `{λ = ±1}` to the dihedral group of order 8 lifting the pair `(Δ, ε)`, that is `Δ ∪ ε = 0` in `H²`, then no
  involution has `Δ = 1`; the Kummer cocycle of 3 modulo 4 (the field `Q(3^{1/4}, i)` of Lead 3 has that group) is
  the candidate; (ii) by Serre's theorem a pro-2 group with an open subgroup of finite cohomological dimension has
  torsion exactly when `ε^n ≠ 0` for all `n`: compute `Δ ∪ ε^n` on a 2-Sylow subgroup. (Whether the multiplier-one
  group has finite 2-cohomological dimension is part of the question; the direction "an involution with `Δ = 1`
  gives `Δ ∪ ε^n ≠ 0` for all `n`" needs no hypothesis.)* Why: A.25, A.31 show no
  congruence level obstructs, and A.32 (by its title; proof not read) says the congruence refinements cannot supply a fourth-root obstruction, so
  the obstruction, if any, is a cohomology class of the non-congruence kernel; A.79, A.81 show such classes exist
  for finite actions.
- **Q4 (Main A in `GT̂`: Furusho's argument, profinitely).** For an involution of `GT̂` the gate is: a word `u`
  with the full pentagon and duality satisfies the hexagon with the one unit `d_α`. *Carry Furusho's derivation of
  the hexagon from the pentagon through in `Γ̂_{0,5}` for this `u`, and name the exact step that uses
  pro-unipotence. The sign of the root is already fixed across primes by the dihedral quotient (A.45), and the
  Alexander and congruence forms hold (A.100, A.101, A.103).* Why: the run went from the pentagon to elliptic
  braid groups; the direct derivation with the failing step named is either the proof or the precise new input
  its last assessment asks for.

**For the Longue Marche field expert (Claude Fable 5.2 at effort max).**

- **Q5.** Should the successor split Main A and Main B into two prompts? In this run they shared no argument after
  about hour 10, and the eight rows of C, D, E were starved. Against it stands the rule of one prompt per cluster.
- **Q6.** Does GT_TOWER_CHECK confirm EXIT_TOWER E.49 (`Δ = 0` on `GT̂`)? If yes, A.105 gives `ε_A = d mod 3` for
  every involution of `GT̂`, and the `GT̂` half of A.13 is closed. Does that sign also give `α(N) = N`, or only the
  signed image of `ω_α` (A.111)? Why: two runs reached the same bit from two sides; one check may close a row here.
- **Q7.** Is the mechanism behind the user's hunch on `A₅` the perfectness of the group? In the obstruction of B.3
  every abelian layer with trivial action contributes `Hom(A₅, ·) = 0`, while for a solvable group these layers
  carry the induction that proves the equality; the binary icosahedral group is perfect, which is the homology
  sphere. If so, the place to look for an element of `𝒦` is a tower in which every obstruction class dies, the
  dual of the ghosts of SECTIONS_OVER_Q. Does your knowledge of the ghost constructions give such a tower, or a
  reason it cannot exist? Why: every linear test (B.23, B.64, B.66) fails to tell `A₅` from `S₄`, so the
  difference must be in what linear tests do not see.
- **Q8.** C.31 (the profinite `GT̂` monoid is a group) and C.34 (Furusho's Question 14, literal form): known, or
  candidates for the list of checked new results after a referee?
