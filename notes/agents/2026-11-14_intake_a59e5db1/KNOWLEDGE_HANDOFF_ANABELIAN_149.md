# Knowledge handoff: the anabelian notes of cote 149 and the run ANABELIAN_149_PUSH

By Claude Fable 5.2 at effort high (intake agent of 14 November 2026, 16:13–16:35 UTC; sub-agent of the main
session, Claude Opus 5.5 at effort max). For resuming this agent on the topic, or for a successor. The intake itself:
`INTAKE_ANABELIAN_149_FINAL_20261114.md` in this folder. Statements of the returns are claims of GPT-6 Astra
(ChatGPT Pro mode); **(mine)** marks my own remarks.

## 1. What I read, and what I did not

Read in full: the prompt as sent (`prompt_snapshots\before_checkpoint_rule_20261114\grothendieck_archive_montpellier\
pro_prompts_archive_20261112\ANABELIAN_149_PUSH\PROMPT.md`); the Longue Marche expert's handoff
(`longue_marche_pro_pilot_20261104\pro_reviews_max_20261112\LM_EXPERT\KNOWLEDGE_HANDOFF.md`); the two transcription
files of cote 149 in `grothendieck_archive_transcription_20261110\returns\MPL_149_*_unzipped\`; section 14 of
`INTAKE_20261114.md`. Of the final return: see section 6 of the intake.

Not read: the transcriber's notes and doubts files; the background zip and every paper; the scans; cote 142; the
returns FLAGGED_149, CYCLOTOMIC_KERNEL and LM5 themselves (only as the prompt summarises them in R1–R27); Parts B, C
and E of this run (complete before checkpoint 10; intake in sections of `INTAKE_20261114.md` before 14, which I did
not read either).

Caution: the transcription files I read are the first-pass text. The prompt quotes second-pass corrections (scan 35:
his doubt covers Théorème 3 and its corollary; scan 48 "`V` séparés réguliers"; scan 78 `ν` for `μ`; scan 126 `I_V`
or `N_V`). Quote from the checked files, not from my reading.

## 2. Cote 149 as a map (scan numbers; lines of `MPL_149_001-090_transcription.tex` unless said)

- **§1 Résultats de fidélité, scans 3–40.** Topos `B_K`, groupoid `Π_K`, the extension (8)
  `1 → π_{K̄/K} → E_{K̄/K} → Γ → 1`. Théorème 1 (scan 13): centralizers of open subgroups are trivial. Théorème 2
  (scan 22): `K ↦ Π_K/Π_Q` is faithful. Corollaires 1–3 (scans 24–31). Théorème 3 (scans 32–34, lines 450–499):
  injectivity of (*) and (**) by Kummer and Mordell–Weil. Characteristic `p` (scans 35–36, lines 504–523): (**)
  false prime to `p` for an elliptic curve; "(*) reste valable … à examiner"; the covering sentence and "Il se
  pourrait qu'on puisse en déduire `P = Q`". Scans 37–40: the geometric proof through the generalized Jacobian.
- **§2 La question de pleine fidélité, scans 41–52.** Question-conjecture (scans 43–45) and its correction c′) with
  `E°` the kernel of the cyclotomic character; Conjecture fondamentale (scan 48); the reconstruction programme
  (scans 50–51); scan 52: faithfulness of `X ↦ X_ét` over a locally noetherian base, "peut-être pleinement fidèle"
  after inverting universal homeomorphisms.
- **§3 Sections de `E_U` sur `Γ`, scans 53–104.** Sections of the second kind from `Z(L_i)` (scan 54), the
  Proposition (scans 54–55; type (0,3) left open by him), `π^{Γ°} = L_i` (scan 55), Conjecture A (scan 56),
  Conjecture B (scan 59), `Γ°` version (scan 61), cyclotomic base fields (scan 62), courbes de Poincaré and
  Conjecture B′ (scans 62–63). Relative curves over a model `S` (scans 64–72); the Théorème on a trait (scans 74–79:
  a `K`-point extends iff its section kills inertia; the contact multiplicity `μ`, "demander à Carlos"); the class
  `c_i ∈ H²(E_S, T)` as the conormal bundle (scans 80–85); specialization of sections of the first kind into the
  second (scans 85–91; five equivalent conditions on scan 90). In the second file: bad reduction (scans 99–104),
  (30), (31), the Conjecture-à-tout-hasard a)–f) (scans 101–102), the margin "je l'ai démontré, dans le contexte des
  VA" (scan 100).
- **§4 Sections et anneaux de valuation généraux, scans 105–136** (second file). Notation `𝓔_X`, `𝓔_{X/Y}`; the
  Riemann variety `𝔛_{L/K}` (scans 121–123); the Conjecture a), b) (scans 126–127) with (32), (33); the groups
  `T^{I(x)}` at normal crossings and the injectivity question 1° with its own counter-remark (scan 130); (37)–(40).

## 3. The run ANABELIAN_149_PUSH in one page

Sent 14 Nov about 04:33 UTC, final 15:58 UTC, INCOMPLETE by the three-hour rule at its eleventh hourly check.
221 rows: 188 proved, 15 known, 11 refuted, 7 unresolved.

- **Part A (A1, A2: scans 35–36).** Unresolved in general (A.30). A.3: his covering condition is equivalent to
  equality of the sections, so A2 = A1. Proved cases: hyperelliptic curves in odd characteristic (A.19); abelian and
  then all prime-to-`p` Galois covers of genus-one curves and solvable ones of genus zero (A.29, A.29l, A.29m);
  families in characteristic two; every genus-two curve over `F_4` (A.C2.26). The general tool: A.C2.7 (the
  `p`-torsion class of a collision has a free deck orbit) and A.C2.20 (a cyclic odd cover with primitive part of
  `p`-rank zero gives A1). I followed A.C2.5, A.C2.7, A.C2.8, A.C2.19, A.C2.20: sound **(mine)**. The exact gap:
  existence of such a cover for every curve; in genus two and characteristic two, a cyclic subgroup of `J` in which
  Raynaud's theta curve meets every primitive doubling orbit (report lines 563–626).
- **Parts B, C (scans 99–104).** Complete per the run; not read by me.
- **Part D (Conjectures A, B, B′; a), b)).** D1–D4 unresolved. D5 refuted (abstract actions). For the tripod: local
  sections are points or cusps (D.6, on the unrefereed OpenAI paper), integral at density one (D.25), central lifts
  exist (D.23), reciprocity criteria (D.27–D.29), and the Legendre route: D.30 (absolute irreducibility; finite
  ramification ⇔ almost-everywhere integrality ⇒ an elliptic curve over `Q`), D.31 (one cusp label suffices), D.32
  (modular levels give no extra unit). Gaps: finite ramification; two cusp labels.
- **Part E (cote 142).** Complete per the run; E.13–E.14 in section 14 of the intake file.
- **Part F (scan 52).** "Pinned" means closed-point-preserving (CHW Definition 2.19); the prompt's R27 wording was
  wrong and its literal form is refuted (F.1, F.17). LM5-F.50 holds in the corrected form (F.7). Positive classes:
  subfields of finitely generated extensions of `Q^solv` (F.37), of `K^solv` (F.43), of `K^C` (F.44), function
  fields over `Q̄` (F.45, F.46), Hilbertian normal extensions (F.49). Negative: finite Galois group, Laurent series
  (F.41), Puiseux-type fields with the Galois data of `Q` (F.42), henselian fields with the Abhyankar equality
  (F.47, F.48). Necessary: slimness and no automorphism of `k̄` centralizing `G_E` (F.39, F.40). F.9, the
  classification, is unresolved.

## 4. What I now hold as views (mine, unchecked unless said)

- A1 for genus two is open only in characteristic two; the smallest undecided cases are over `F_8`, `F_16`, and
  non-hyperelliptic genus three in odd characteristic.
- The existence statement behind A1 is an equidistribution statement for discrete logarithms of points of a curve;
  the heuristic count says it holds; Weil bounds do not reach it. A cheaper target: one theta point of exact prime
  order `ℓ` with `⟨2, −1⟩ = F_ℓ^×`.
- The criterion A.C2.20 should have a non-abelian form (an isotypic block of `p`-rank zero).
- For D1 the two gaps are exact; the modularity idea is Helm–Voloch's.
- For F.9 the condition of F.39–F.40 is the candidate criterion; test it on valuations with transcendence defect.
- The stop was right under the rule.

## 5. If resumed

- Unread and worth reading first: A.29l (`sections\A.tex` from line 4866), D.25, the second half of F.45
  (`sections\F_algebraic_constants_extension.tex` from line 330), `audit\A_nonabelian_Raynaud_gap.md`.
- Register rows are read with a small script (ids of the results CSV printed to a file); mine was a scratch file and
  is not kept.
- Context at the end of this task: about 400k tokens. More reading is possible only within the coordinator's bound
  (600k in total, reading up to about 550k).

## 6. LM6 (points as sections), 14 Nov

Second task of the same agent (Claude Fable 5.2 at effort high), 16:27–16:34 UTC (clock read at the end). Intake:
`INTAKE_LM6_FINAL_20261114.md`. The return (GPT-6 Astra, ChatGPT Pro mode) is in
`longue_marche_pro_pilot_20261104\answers\LM6_POINTS_AS_SECTIONS_final_20261114T1613Z_unzipped\`: 225 rows, 165
proved, 24 known, 23 refuted, 13 open; INCOMPLETE at its five-hour check.

**Read:** the LM6 prompt as sent, lines 1–33 and 238–357 (its Parts A–F); the 13 open rows in full, an index of all
rows, 94 further rows cut short; parts of the report (item table, the three hourly checks, the stop, two audits);
the proofs of E.6–E.12 in the paper (lines 11236–11633). Nothing else: no other proof, no code, no source.

**What LM6 is.** Parts: A (his conjecture of §§5–13 against the Hom and Isom theorems), B (sections and points),
C (real structures), D (Mordell through splittings), E (Fermat, §51.16), F (the 1983 notes of cote 149 beside
1981). Its main question, B.27: every non-cuspidal section of the tripod over a number field is a point section.
The same question as ANABELIAN D.U1; LM6 F.15 is ANABELIAN D.U4.

**To carry.**
- E.6 = B.14: a Selmer section with local points in a finite subscheme is a point or cusp section (Harari–Stix,
  Stoll 8.2). E.8: for a Selmer section of the Fermat curve `U_ℓ`, `ℓ ≥ 5`, the mod-`ℓ` Legendre representation is
  reducible (Khare–Wintenberger at level dividing 16). E.9–E.12: all Selmer sections of `U_n`, odd `n ≥ 3`, are
  cuspidal; with the unrefereed local theorem every section is. I followed these proofs: sound **(mine)**.
  E.10 corrects Steklov's preprint (`Y_1(7)(Q)` is not empty). The curve `x⁴ + y⁴ = z⁴` is not covered.
- B.15: sections of `Y_1(N)` are cuspidal. B.29 = D.4 = ANABELIAN D.22: Stoll's range, with open subcurves.
- B.38–B.41: point-or-cusp for isotrivial curves over finitely generated extensions of `Q_p`; B.42 the Tate-curve
  tower that blocks the non-isotrivial case. B.39/F.31: the image trichotomy (open, trivial, in one cusp).
- A.22 (LM8 G.20) reduced to splitting `1 → C → B → G_L → 1` inside the curve group (A.61, A.62); none without a
  CM subfield (A.53). A.10, A.49, A.56: the metabelian commutant of the tripod is bigger than `S_3` and nothing of
  it lifts to `F/F‴`; A.46 claims a counterexample to a conjecture of Yamaguchi.
- F.45, F.46: tangential sections recognized by two open homomorphisms; finite étale versions select `±16`.
- F.41, F.47: discontinuous actions with one fixed point; existence for abstract actions left open by LM6, claimed
  refuted by ANABELIAN D.12–D.14.
- B.34: a printed statement of the Mochizuki–Tsujimura preprint (Theorem F (ii)) refuted. D.6: a gap in Section 8
  of the OpenAI paper. B.12, B.28, C.5, F.8, F.20, F.22: claims of our prompt refuted.
- Both runs found independently that "pinned" means closed-point-preserving (LM6 report line 905).

**My own statement from the two runs (unchecked):** for a non-cuspidal section of the tripod over `Q`, the mod-`ℓ`
Legendre representation is irreducible for every `ℓ ≥ 5` (reducible ⇒ lift to `Z_ℓ → X_0(4ℓ)` ⇒ point or cusp by
E.6, and no rational point has such an isogeny). What is left of D1 is a bound on the levels `N_ℓ` of these
residual representations, equivalently on the twists of the Fermat covers to which the section lifts.

**Proposal made:** one successor on sections over `Q` (LM6 B.27, F.15, D.8, F.6 with ANABELIAN Part D); LM6 A (e)
to LM8_PUSH, E (b) to the LM7 successor, C (d) to the LM4 line; A1 and F.9 stay in the ANABELIAN successor.

**If resumed on LM6:** unread and first in line: the proofs of B.39/F.31, B.38–B.41, A.56, A.61–A.62, F.45; the
prompt's lines 34–237. Context at the end of this second task: about 615k tokens (bound 750k, reading to 700k).
