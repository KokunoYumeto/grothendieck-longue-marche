# Consolidated register of the debate of 14 November 2026

By Claude Fable 5.2 at effort high (the intake and register participant; single writer of this step), 14 November
2026, 17:36–17:50 UTC (clock read at 17:36). For the main session (Claude Opus 5.5 at effort max). The returns are
by GPT-6 Astra (ChatGPT Pro mode); "Proved" in a status column is that model's label. Readers: **I** = the intake
agent (Claude Fable 5.2 at effort high); **M** = manuscript participant, **F** = Fermat participant, **LM**, **P** =
the Longue Marche and Poincaré field experts (Claude Fable 5.2 at effort max); **X** = cross-run participant, **D** =
the dictionary's author (Claude Fable 5.2 at effort high); **W** = the war-game agent (Claude Fable 5.2 at effort
max). "followed" = the proof was read and no error found by that reader; "stmt" = statement level. No row here is
refereed (Claude Opus 5.5 at effort max) unless it says so. **(mine)** marks my own judgments.

**Read for this step:** the three other responses, the war-game note, the user's `Δ` hunch, `MATHS_PROMPTS_TALLY.md`,
the headings and the last section of `PUSH_ITEMS_ORDER5_FRAME.md`. **Not read:** `PUSH_ITEMS_20261114.md`,
`PUSH_ITEMS_LM7_CONTINUED.md`, `LM8_PUSH\PROMPT.md`, `EXIT_TOWER\PROMPT.md` (their states are taken from their
owners' responses), the Dérivateurs and S6 prompts.

Short names of prompts: **SQ** = `SECTIONS_OVER_Q_DRAFT\ITEMS_DRAFT.md`; **AS** =
`ANABELIAN_SUCCESSOR_DRAFT\ITEMS_DRAFT.md`; **FS** = the Fermat successor (`PUSH_ITEMS_20261114.md`, Part 1);
**L4S** = the LM4 successor (same file, Part 2); **DL** = the `Δ` prompt (`PUSH_ITEMS_LM7_CONTINUED.md` S.1–S.16
with `PUSH_ITEMS_ORDER5_FRAME.md` O.1–O.18); **L8** = `LM8_PUSH\PROMPT.md`; **ET** = `EXIT_TOWER\PROMPT.md`.

## 1. The register: the claims of the two final returns that matter

"Rests on": **T6** = OpenAI, *The p-adic section conjecture*, 6 October 2026 (unrefereed; LM6 D.6 reports a gap in
its Section 8); **BZ-A** = Boggi–Zalesskii 2024, Theorem A (one element of prime order); **BZ-19** = Boggi–Zalesskii
2019, Lemma 3.1; **CS** = Carlson–Stix 2026, Proposition 3.17; **CHW** = Carlson–Haine–Wolf 2024, Theorem 4.18 (5).

### 1.1 ANABELIAN_149_PUSH (AP), final of 14 November: 221 rows, 7 unresolved

| Rows | Claim | Status | Verdict, reader | Rests on | Implication | Astra item | Prompt |
|---|---|---|---|---|---|---|---|
| A.1–A.3 | A collision is his covering condition of scan 36; the lift with `p`-primary difference is unique and rational | Proved | followed (I) | — | A2 of the old prompt is A1 | AS A2 | AS |
| A.C2.7 | The class `T` has a free orbit under a deck group of odd order | Proved | followed (I, M) | — | the base of every lever | AS A2 | AS |
| A.C2.19, A.C2.20 | A cyclic odd cover with primitive part of `p`-rank zero excludes collisions | Proved | followed (I) | A.29l for odd `p` | superseded as a target by lever 1 | AS A6 | AS |
| (not in the return) | Lever 1 = criterion (R): a `P`-split cover of odd order with relative class number prime to `p` excludes collisions at `P` | — | derived independently by I and M; checked by no third reader | A.3, A.C2.7 | A1 becomes a count of points in cosets; **first item for Astra** | AS A2–A4 | AS |
| A.19 | No collision on hyperelliptic curves, `p` odd | Proved | unread | A.13–A.18 | genus two open only for `p = 2` | AS R4, check | AS |
| A.21, A.29l | Elliptic-image test; prime-to-`p` Galois covers of genus-one curves | Proved | followed (I) | BZ-19 | seeds of the closure principle | AS A5; BZ-19 also in L4S 2.4 (S6) | AS, L4S |
| A.C2.22–A.C2.26 | No collision on any genus-two curve over `F_4` | Proved | certificate, unreproduced | programs | to be re-derived from lever 1 | AS A4 | AS |
| A.C2.13–A.C2.18, A.C2.21, A.C2.23, A.C2.24, A.C2.14 | Families, method limits | Proved | stmt (I) | programs | context | — | AS (R7) |
| A.30, A.C2.6 | A1 in general; existence of theta torsion on all doubling orbits | Unresolved | — | — | main question | AS A1, A3, A6 | AS |
| B.1–B.24, C.1–C.8 | Scans 99–103 (good reduction a)–f)): the tables of implications; the multi-twist; the local fixed groups C.7h, C.7u | Proved / Known / Refuted | intakes of sections before 15 (not mine); C.7h stmt | T6 for C.7 | Parts B, C complete pending referee; C.7h is the local tool for LM8 G.20 | referee list | L8 A.7 |
| D.6, D.19 | Local sections are points or cusps | Proved | stmt | T6 | used by every D row | SQ R1, A2 | SQ |
| D.22 | Stoll's range, with open subcurves | Proved | stmt; same as LM6 D.4, B.29 | Stoll | two runs agree | — | SQ R3 |
| D.23, D.27–D.29 | Central lifts at punctures; reciprocity; its insufficiency | Proved | stmt | — | finite-level b) | SQ A9, A12 | SQ |
| D.25 | Local points integral at density one | Proved | stmt | T6 | — | SQ R5 | SQ |
| D.30, D.31 | Legendre representation: irreducible; finite ramification ⇔ integrality ⇒ elliptic curve; one cusp label suffices | Proved | followed (I) | T6, Pan 2022 (unopened) | D1 = finite ramification + labels | SQ A4, A7 | SQ |
| D.32 | Modular levels give no unit | Proved | followed in part (I) | — | labels live on non-congruence covers | SQ A7 | SQ |
| D.11–D.14 | Abstract semilinear actions: one with no fixed point | Proved / Refuted | stmt | — | refutes a statement he did not make (M) | SQ C2 | SQ |
| D.U1–D.U4 | Conjecture A, a), b) for the tripod and in general | Unresolved | — | — | main question of SQ | SQ A1, B1 | SQ |
| E.13, E.14 | Genus zero determines the outer actions; `G_Q` as the AA-subgroup containing `c` | Proved | selection step followed (I, section 14) | HMT 2025 (unopened) | cote 143 ⑨ | ET (e), L8 C.8, DL O.14 | ET, L8, DL |
| F.1, F.17 | Without the closed-point condition no field reconstructs | Refuted | stmt; M: refutes scan 52 as written | — | "pinned" = closed-point-preserving; R27 wording was ours | AS F1 | AS |
| F.7, F.37, F.43–F.46, F.49 | Reconstruction over classes of fields | Proved | F.45 followed, F.43 in part (I); rest stmt | CHW | sufficient classes | AS F5 | AS |
| F.41, F.42, F.47, F.48 | Failures; no criterion in Galois data | Proved | F.47 followed (I) | — | necessary conditions | AS F3, F4 | AS |
| F.15 | The comparison LM5 F.45 left (cyclotomic normalization of inertia across three returns) | Proved | stmt | — | LM5 needs no successor | referee | — |
| F.9 | Which fields reconstruct | Unresolved | — | — | ours, not his (M) | AS F3 | AS |
| G.1, G.2 | Covering-germ criterion for injectivity of local inertia | Proved | stmt | — | his scan 130 | SQ B3 | SQ |

### 1.2 LM6_POINTS_AS_SECTIONS, final of 14 November: 225 rows, 13 open

| Rows | Claim | Status | Verdict, reader | Rests on | Implication | Astra item | Prompt |
|---|---|---|---|---|---|---|---|
| E.6 = B.14 | Finite support ⇒ point or cusp | Proved | followed (I, F) | Harari–Stix, Stoll | the engine | FS 1.13 | FS, SQ R2 |
| E.7–E.12 | Every Selmer section of the Fermat curve of odd exponent is cuspidal; every section, given T6 | Proved | followed (I, F) | Khare–Wintenberger, Stoll, Mazur; T6 for the last step | §51.16 answered in the limit; no nilpotent level sees it | FS 1.13, 1.14, 1.19 | FS |
| E.10 | `Y_1(7)(Q) ≠ ∅`, against Steklov | Refuted | checked by hand (F) | — | correction to a preprint | FS 1.13 | FS |
| E.13–E.39, E.21 | The nilpotent tower of the Fermat curves; E.21 open (Ross value, class-three image) | Proved / Open | stmt | programs | state of LM7 E.23 | FS 1.7–1.11, 1.17 | FS |
| E.16, E.31–E.34, E.38 | Non-cuspidal sections of pro-`ℓ` and metabelian quotients; a `lim¹` obstruction | Proved | stmt | Hoshi 2010 | ghosts exist at every such level | SQ A5; L8 D.5 | SQ, L8 |
| B.15, B.29 | `Y_1(N)`; open subcurves in Stoll's range | Proved | B.15 followed (I) | T6, Stoll | closes LM3 E.17 | — | SQ R3 |
| B.7, B.19 | Local classification, with stacks | Proved | stmt | T6 | — | SQ A2 | SQ |
| F.29–F.31, B.39 | Image of a homomorphism to a curve group: open, trivial, in one cusp | Proved | F.29–F.31 followed (I) | T6, CS | engine of B.38, B.41, A.61 | referee | SQ R10 |
| B.38–B.41 | `p`-adic function fields: unramified generic sections; isotrivial curves | Proved | B.38, B.41 followed (I) | T6 | new case of the section conjecture | SQ D3 | SQ |
| B.42 | A Tate-curve tower split at every closed point | Proved | stmt | — | blocks the closed-fibre argument | SQ D3 | SQ |
| B.27, F.15 | Tripod sections are points; birational lifting | Open | — | — | two statements (M's correction) | SQ A1 | SQ |
| D.1, D.4–D.7, D.8 | `Sec` = finite-descent set; D.6: a gap in T6 Section 8; D.8 finiteness open | Proved / Open | stmt | T6 | report to OpenAI after a check | SQ D1 | SQ |
| A.10, A.46, A.49, A.56–A.59, A.66 | Metabelian commutant larger than `S_3`; nothing lifts to `F/F‴`; A.46 against a conjecture of Yamaguchi | Proved / Refuted | A.10, A.46 followed (I) | Chen–Deligne | the Galois side of LM8 A.22 | L8 Part B; FS 1.5 | L8, FS |
| A.21, A.36, A.50–A.53, A.61–A.65; A.22 | LM8 G.20 reduced to splitting `1 → C → B → G_L → 1`; A.22 open | Proved / Open | A.61, A.62 followed (I) | T6, Faltings | — | L8 A.7 | L8 |
| A.12, A.32, A.40, A.45 | Side rows of Part A | Open | — | — | A.12 is now a computation in `H₂(M, Ẑ)` (X) | L8 Part B for A.12 | L8; rest: register |
| C.13–C.19; C.12 | Real structures in genus 3; C.12 open | Proved / Open | stmt | BZ-A (not the step under examination: X) | congruence kernel `K^τ` | ET | ET |
| F.45, F.46 | Tangential sections by two open homomorphisms; `±16` | Proved | stmt | Scherr–Zieve, Calegari–Dimitrov–Tang | his scan 85 | SQ L15 | SQ |
| F.41, F.47, F.9 | Abstract actions with one fixed point; B′ with continuity is B | Refuted / Proved | stmt | — | with AP D.12–D.14 | SQ C2 | SQ |
| B.34 | A printed statement of Mochizuki–Tsujimura's preprint (Theorem F (ii)) false as stated | Refuted | followed (I); source unopened | — | correction to a preprint | referee | — |
| B.12, B.28, C.5, F.8, F.20, F.22 | Claims of our LM6 prompt refuted | Refuted | followed (I) except F.20, F.22 | — | prompt-drafting slips | — | — |
| F.6, F.24, F.34 | Higher-dimensional targets; the tangential subtorsor by automorphisms only | Open | — | — | side rows | SQ D2 for F.6 | SQ; rest: register |

Correction rows (attributions; M): LM6 D.8 "scan 65" is cote 140-2 §8; "B′ refuted" holds for abstract actions
only; F.9 is our question; his margin "`S` de car. 0 ?" is about Frobenius. Readings: scan 36 "`Y′` de `X`" (his slip),
scan 126 `I_V`, scan 52 "`X_et`" for `S_et` and "structure à lacets", scan 35 "être à l'aise", "corps fini parfait".
Scans 99–103: which arrows of a)–f) hold is in AP Parts B, C (B.8, B.8u, B.20–B.24, C.3), read by earlier intakes.

## 2. The hunch map

| # | Hunch or path | From | Went into |
|---|---|---|---|
| 1 | Lever 1: relative class number prime to `p`, `P` split | I, M | AS L1, L2; items A2–A4 |
| 2 | The group-ring form; the singleton lemma; least field; (E) | M (T1) | AS, "Changes of the consolidation"; items A2, A3 |
| 3 | The count in cosets; `p > (2g − 2)²` | I | AS L3; A3 |
| 4 | Lever 2: correspondences to a curve with no rational `p`-torsion; Bogomolov–Tschinkel; the `L`-zero test | P (rational form: I, M) | AS L5; A5 |
| 5 | The closure principle | M, P | AS L6; A5 |
| 6 | Lever 3: Frobenius at closed points | LM | AS L7 (as lever 1 on covers; Path 1 as stated rejected by I, M) |
| 7 | Lever 4: not ordinary in the eigenspace of `T` | LM | AS L8; A6 |
| 8 | A1 as "the exceptional set of Saïdi–Tamagawa is empty" | P | AS L9; A8 |
| 9 | Conway–McKay–Trojan coverings as test objects | D (4.6) | AS L10; A7 |
| 10 | His margin: Théorème 2 in characteristic `p` | M | AS A9 |
| 11 | F.9: no automorphism centralizes `G_E` | I | AS F3 (a) |
| 12 | F.9: equivalence with the Isom form for genus-0 curves | P | AS F3 (b), lead item |
| 13 | F.9: the pro-form of scans 6–8; scan 52 as written; unpinned morphisms are his conjecture a) | M (T3) | AS F1, F3 (c) |
| 14 | F.9 false as stated; add "sections of points preserved" | LM | not taken (that condition is the closed-point condition); its test rule is in AS "The pattern" |
| 15 | His experiment with the loop structure | M | AS F2 |
| 16 | The pro-pro-group of `(C, C)` (scan 8) | M | AS F6 |
| 17 | The LM5 F.45 audit | X | not added: done in AP F.15 (register 1.1) |
| 18 | Ghosts and rigid targets (the one pattern) | P, LM, X, F | AS and SQ (conventions, leads); L8, ET (X) |
| 19 | b) and Stix 2015 | M (corrected in round 2) | SQ L1, A2 |
| 20 | Statement (G): a ghost at every puncture | M (T2) | SQ L19; A12, A13 |
| 21 | b) at finite level; the extension `Π_s` | M | SQ L17; A9 |
| 22 | Residual irreducibility; levels `N_ℓ`; twists | I | SQ L4, L5; A3, A4 |
| 23 | Residual against `ℓ`-adic finite ramification | P, F | SQ L3, L21 |
| 24 | Stacky heights on `P¹(n, n, n)` | P | SQ L7; A4 |
| 25 | Where ghosts die: metabelian, `X(3)`, `X(4)`, `X(5)`, `X(7)` | P | SQ L8; A5. Fermat-curve half: FS 1.18 |
| 26 | The completed unit equation has ghost solutions | I (LM asks the opposite) | SQ L9; A5, A12 |
| 27 | The phantom (`lim¹`) cup product; cyclotomic descent | I, LM, F | SQ L10; A5. Also FS 1.20, L8 Lead 16 |
| 28 | Local cuspidal families; independence of `ℓ` | LM | SQ L11; A6. Also FS 1.19 |
| 29 | Self-covers of the tripod throw a non-point into a cusp | LM | SQ L11 (iv); A14 |
| 30 | Lattès semigroup on sections (M5 (c)) | D, via X | SQ L20; A14 |
| 31 | Congruence rigidity; labels live on non-congruence covers | I, P | SQ L12; A7 |
| 32 | Serre–Tate parameter fixes the local point (disputed) | P; caution I | SQ L13; A7 |
| 33 | The unit `1 − 1728/j`; five added points (M4 (a)) | D | SQ L14; A8 |
| 34 | Two maps from one neighbourhood | I | SQ L15; A7 |
| 35 | Rank-zero twists (cubic, quartic, sextic) | F | FS 1.16 (table); SQ L6, A10 (statement) |
| 36 | The quartic through its CM quotients (M4 (b)) | D, F | FS 1.14; SQ D4 (pointer) |
| 37 | Cyclotomic base (scans 61–62) | M | SQ C1 |
| 38 | B′ with continuity | M (T4) | SQ R16, C2 (already proved: LM6 F.9) |
| 39 | Scans 120, 128, 130; scan 50 | M | SQ B3, D5 |
| 40 | The two towers (Fermat and congruence) are one object | F | FS (framing; item 1.15); companion §51 |
| 41 | The prosolvable quotient over `SL_2(F_ℓ)` carries the theorem | F | FS 1.15; L8 D.5 |
| 42 | The Ross value through the Hodge realization | F | FS 1.17 |
| 43 | LM8 G.20's extension never splits; specialize first | I, LM | L8 A.7 |
| 44 | Sub-configuration lever; cross-ratio form; M2 | P, D | L4S 2.4 (S1)–(S4) |
| 45 | M3 resolvent maps; M5 (a), (b) Lattès maps and `T`, `W` | D, P | L8 Lead 27, C.10, C.11 |
| 46 | M1 (a)–(d): the frame in `{1, 5, 7, 11}`, Weil representation, braided categories, other levels | D | ORDER5 O.9–O.12 and LM7 successor S.13–S.16 (stated twice: see 4.1) |
| 47 | `Δ = 0` on `GT̂` through Lead 24; Lead 25 (one bit only) | X | L8 C.8; LM7 successor S.1 |
| 48 | Test every condition on the element of E.58 | LM | ET (e); ORDER5; L8 C.8 |
| 49 | `Δ` is a sign cancellation; a sign, not a number; the obstruction as an operator, `Δ` as what cancels it | the user | ORDER5 O.15–O.18 |
| 50 | Dictionary S8 (Mathieu groups, additive polynomials; LM8 B.24d) | D | **unplaced**: register of open rows (X); see 4.3 |
| 51 | War game H3, S5 (rank selection in the curve complex; cote 142's category with admissible covers) | W | ET, **still to fold in** (W; owner X) |
| 52 | War game H5 (trace triples), LM2 B.f5: `GT̂₀` against Galois on regular maps with group `PSL₂(F_q)` | W | **unplaced**: see 4.3 |
| 53 | War game H6; Dérivateurs H2, H9 | W | tally row 20, to write (not Longue Marche) |
| 54 | Cotes 145, 143, 148, 64, 79, 83 move up in the reading order | W | not a prompt: main session |

## 3. Every unsent mathematics prompt

| Prompt | State | What the new results changed | Updated by | Left to do |
|---|---|---|---|---|
| **SQ** (new) | items draft, three states kept | whole prompt new: R1–R18, L1–L21, Parts A–D | I | frame, zip, lint (main session); remove D4 and thin A10 if 4.4 is accepted |
| **AS** (new) | items draft, three states kept | whole prompt new: A1 cluster, Part F | I | frame, zip, lint; Astra to check lever 1 first |
| **DL**: LM7 successor S.1–S.16 | item list | M1 as S.13–S.16; Lead 25; joint level 12 | F | merge with ORDER5 (4.1); the Longue Marche expert's two preconditions (W 3.2) |
| **DL**: ORDER5_FRAME O.1–O.18 | item list | O.9–O.14 (X); O.15–O.18, the user's hunch (I) | X, I | merge (4.1); checkpoint paragraph |
| **FS** | item list | 1.13–1.20 lead it; additions to 1.2, 1.5, 1.14, 1.15 | F | frame; overlaps with SQ (4.4); (X4) and Lead 25 to be copied in |
| **L4S** | item list 2.1–2.9 | 2.4 gained (S1)–(S6) | X | frame; decision on 2.4 (4.2) |
| **L8** (LM8_PUSH) | READY, lint passes | Part A restated from LM6 A.61–A.62; Lead 27, C.10, C.11; C.7, C.9; A.7; D.5 | X | zip to rebuild (attachments named, not added) |
| **ET** (EXIT_TOWER) | READY, lint passes | (e) with the E.58 test; attachments; the caution on the two proofs | X | zip to rebuild; war-game H3, S5 not yet folded in |
| POLYHEDRA_SHADOWS | not written | — | — | decision 4.3 |
| LM5_MULTI_GALOIS_TOPOI | tally says READY; it returned (final of 13 Nov) | no successor needed (X, W, I) | — | **tally row stale** |
| LM6, ANABELIAN_149_PUSH, LM4, LM7_PUSH | tally says READY or RUNNING; all returned | — | — | **tally rows stale** (main session) |
| INDLOCAL, REVERSIBLE_LOCALIZERS, FINMON, S2COUNT, DER_FOLLOWUP | READY | none found; not examined by any participant | — | to the main session: no owner in this debate |
| Dérivateurs hunches H2, H9 (with war-game H6) | TO WRITE | — | — | to the main session |
| S6_03_CDP, S6_04_MAPS_MANIFOLDS, S6_05_ARITHMETIC, S6_02_PUSH | READY | not examined; S6_05 (periods at special points) may meet FS 1.17 (a regulator through the Hodge realization) **(mine, unchecked)** | — | to the main session: ask the S6 expert about S6_05 |

Rows of the two finals that no prompt takes: LM6 A.32, A.40, A.45, F.24, F.34; AP D.24-type route closures. They
stay in the list of open rows for version 2 of the companion.

## 4. Decisions left open, with my recommendation

### 4.1 `Δ`: one prompt or two

The cross-run participant proposes one prompt "`Δ` on `GT̂`" (S.1–S.16 with O.1–O.18); the war game counts two. M1 is
now stated twice (O.9–O.12 and S.13–S.16). Both lists have the same main question, LM7_PUSH E.3, and the
three-hour rule gives a run's hours to one main question. **Recommendation: one prompt.** Main question: E.3 in
the user's form (O.18). Routes in this order: O.18 with O.15–O.17; the braided-category route (O.11 = S.15);
frames at five points (O.1–O.7); Lead 24 and Lead 25. A second Part for what is not a route to E.3: O.8 (six and
seven points), O.12 (other levels), O.13 (his list of cote 148), the rows D.1, D.2 of LM7_PUSH. M1 is kept once.

### 4.2 Item 2.4 (the icosahedral centralizer): inside the LM4 successor or its own prompt

L4S has D.12 (the involutions) as main question; 2.4 is a second main question with its own levers (S1)–(S6), and
the Poincaré expert calls it the cheapest decisive item. **Recommendation: its own prompt**, so that both get
hours. Its home in the war game's map is Book IV (maps and polyhedra).

### 4.3 POLYHEDRA_SHADOWS

M3 and M5 (a), (b) are in L8. What is left of it: war-game H5 (trace triples), LM2 B.f5, the levels 7 and 11 of
(S5), dictionary S8. **Recommendation: not a prompt of its own now.** Put that residue as the second Part of the
icosahedral prompt of 4.2, which is the Book IV prompt in any case. If 4.2 is decided the other way, the residue
waits in the register for version 2.

### 4.4 Overlaps between the Fermat successor and SECTIONS_OVER_Q

| Topic | FS | SQ | Recommendation |
|---|---|---|---|
| Line-by-line check of LM6 E.6–E.12 | 1.13 | R2, R4 (used) | FS keeps it; SQ uses it and checks only the steps it needs |
| `x⁴ + y⁴ = z⁴`, even exponents | 1.14 | D4 | FS keeps it; SQ D4 becomes a pointer |
| Rank-zero twists | 1.16 (table) | A10 | FS computes the table; SQ A10 asks only the statement for the tripod and the positive-rank question |
| Where ghosts die | 1.18 (twists of the cubic) | A5 (the tripod) | both, each on its own curve; they run in parallel and cannot use each other's output |
| Local cuspidality, independence of `ℓ` | 1.19 (to cut E.12's dependence on T6) | A6 | both: different purposes |
| Phantom classes on the tripod | 1.20 | A5, L10 | SQ keeps it (it is a route to SQ's main question); FS 1.20 becomes a pointer |

FS then has two blocks, as its owner says: the check and extension of the headline (1.13, 1.14, 1.16, 1.19) and
the tower (1.15, 1.17, 1.7–1.11). If one run is too small for both, the first block is the clean unit to send first.

## 5. The Longue Marche prompts left before version 1 of the companion

**With my recommendations: seven.**
1. **`Δ` on `GT̂`** (LM7 successor merged with ORDER5_FRAME): is `Δ = 0` on `GT̂`.
2. **SECTIONS_OVER_Q**: every non-cuspidal section of the tripod over `Q` is a point; birational lifting.
3. **The Fermat successor**: the check and extension of Fermat for sections; then the nilpotent tower (E.21).
4. **The LM4 successor**: D.12, the involutions of `GT̂₀` (with C.12, 2.5, 2.6, 2.9).
5. **The icosahedral centralizer** (item 2.4 as its own prompt, with the residue of POLYHEDRA_SHADOWS).
6. **LM8_PUSH**: LM8 G.20 as one extension inside the curve group; the metabelian family.
7. **EXIT_TOWER**: the tower with its structure at infinity.

**Outside the count** (the war game's reason: its questions are asked in cote 149 only): the **ANABELIAN
successor** (A1; scan 52). I recommend sending it early all the same: lever 1 is cheap to check and may settle A1.

If the decisions go the other way (two `Δ` prompts, 2.4 inside L4S, POLYHEDRA_SHADOWS written) the count is the
war game's eight. No successor of LM5 in either count. Before the `Δ` prompt goes out: the Longue Marche expert's
two preconditions (the literature search on `GT̂` against `GT̂₀`; the corollary of D.50 written and refereed).

The register should gain, when it becomes the list of blocks of the companion (war game 2.3): a stable id per row
and the "rests on" column filled for every row; here it is filled for T6, BZ-A, BZ-19, CS and CHW only.
