# Prompt impact of TOTAL_EXACT_2 (T) and LM8 (L) on the READY prompts

Claude Fable 5.2, effort high, 13 Nov 2026. Rows of `MATHS_PROMPTS_TALLY.md` in state READY: 13. Changed by
script: 3 (INDLOCAL, LM5, LM6). Block written for the expert: 1 (DER_FOLLOWUP). No change: 9.

How the "no change" verdicts were reached: each PROMPT.md was scanned for the terms the two returns touch
(total / exact / quasi-filtered / `Ty^op` / `K*` / TOTAL_EXACT / LM8 / `q_7` / `GT_0` / CK E3 / LM3b D.4 / `ε_4` /
lim¹ / Mittag-Leffler / limiting topos / `M_{1,1}` / E.32 / `ST_{1,1}` / `B_3` / `y² = x³ − x` / `s(Δ)`), and the
hits were read in context. The Parts of those nine prompts were not read in full. A prompt whose items meet the
returns under other words would be missed by this scan.

Script: `pro_intake_20261113\apply_prompt_changes_20261113.py` (dry run, then `--apply`); inserted blocks:
`pro_intake_20261113\blocks\`. Backups: in each prompt's work folder, `backup_intake_20261113\` (the PROMPT.md and
every zip before the change). None of the three work folders holds a live `PROMPT.md` (they hold dated
before-copies only), so the upload copy is the one edited. Lint (`push_rule_pro_prompts.py --lint-math`) after the
change, each: `files: 1 failing lint: 0`.

## Changed

| Prompt | What the returns do to it | Change | Zip | Lint |
|---|---|---|---|---|
| INDLOCAL | T C.40 proves R8 (`Ty^op` fails span completion, no affine equalizer, `H_1 = Z`), with one correction: "no affine equalizer" needs a non-zero ring | R8: status "read by nobody else" → proved independently as T C.40, attached; "over any non-zero ring" added | `INDLOCAL_new_results.zip`: + `TOTAL_EXACT_2/finite_tests.tex`, `TOTAL_EXACT_2/TOTEX2_results.csv`, README extended (156 → 158 entries) | passes |
| LM5_MULTI_GALOIS_TOPOI | L E.11 corrects a premise of Part F (d), (g): the topos of a punctured germ is not the limit of the sheaf topoi (degenerate); L E.10 gives its covering germ (`BZ`; `Z^r` at normal crossings) | new block "the return LM8_LIE_APPROXIMATIONS" before "What the outcome must be" (E.10, E.11 stated exactly; check the proofs first; what changes in F (d), F (g); the coherent-topos lead to prove or refute); one clause in Part F (d) where the premise is used | background zip: root `PROMPT.md` refreshed, + `LM8_return/sections/E.tex`, `00_conventions.tex`, results register, 3 MANIFEST rows (678 → 681 entries) | passes |
| LM6_POINTS_AS_SECTIONS | L G.10, G.13 settle CK E3 and LM3b D.4 for the CM curve in every pro-ℓ quotient; L G.11 does the eigenline lifting that line 28 asked for (lifts through `N_4`, stops at `N_5`); L G.6 refutes the lead on three degree-4 components; L G.19–G.20 leave the full profinite case; L F.4, F.14, F.15, F.21, F.24 are the lemmas LM8 was asked to pass to this prompt | (1) the task sentence of "After LM3 and LM3b" (lift the eigenline, decide D.4) rewritten to: check G.11–G.13, then decide D.4 for the full profinite group and for general curves; (2) "stay open" in the CYCLOTOMIC block corrected; (3) fourth New-since block (statements exact; G.20 asked here; F.15/F.21 to be named wherever a task passes to a limit) | `LM6_POINTS_AS_SECTIONS_new_results.zip`: + `LM8_return/` (12 files: sections A, C, E, F, F_advanced, G, two G inputs, conventions, main file, register, report), README extended (67 → 79 entries); background zip: root `PROMPT.md` refreshed | passes |

## Block for the expert (not applied)

| Prompt | What the returns do to it | Where |
|---|---|---|
| DER_FOLLOWUP | T C.40 settles Part B.1 (R12); T C.28, C.37, D.1 settle the premise of Part A.2 (R14) for every admissible construction; T A.1 (total ⊋ exact) changes the status line "still running", makes the case "total, not exact" of Part D.1 non-empty and gives a new R-item | `BLOCK_FOR_DER_FOLLOWUP.md` |

## No change

| Prompt | Reason |
|---|---|
| REVERSIBLE_LOCALIZERS | no item on exactness of colimits, on towers or on the LM8 material. L B.6, B.9 give new fundamental localizers `W_𝔞 ⊃ W_1` with their intrinsic coverings; they are examples for its questions, not a settlement of any. Recorded for the expert (IMPLICATIONS I3, HANDOFF_ADDENDUM_DERIVATEURS); adding them is the expert's decision, since the Parts were not read here. |
| FINMON | no hit in context (its "E3" is its own item on homotopy types). |
| S2COUNT | no hit. |
| S6_03_CDP, S6_04_MAPS_MANIFOLDS, S6_05_ARITHMETIC, S6_02_PUSH | no hit in context (the words "exact" and "total" occur in other senses). The S6 expert has not been asked. |
| ANABELIAN_149_PUSH | its only contact is R9 (`y² = x³ − t²x` over `Q((t))`, a quadratic twist of the CM curve): a statement about bad reduction that L Part G does not touch. Its items E1–E3 are its own (isotopy relation). |
| EXIT_TOWER | no hit. L E.10–E.11 (covering germs, the degenerate limit) concern punctured neighbourhoods; if EXIT_TOWER defines a topos of a tubular germ as a limit of sheaf topoi, the correction made in LM5 applies there too. Not verified: its text was scanned for "limiting topos", "limit of … topoi" only. |

## Not touched, as instructed

- LM4_FINITE_GROUP_ACTIONS and LM7_PUSH (RUNNING). When they end: LM7_PUSH Part F ("the lim¹ check as a theorem")
  meets L F.15 and F.21 directly (F.21 is its R2 = E.32 at the prime 5, with an actual pair); LM4 Part D meets
  L A.11–A.26 (LM8 could not use LM4: "LM4 not supplied").

## Tally changes to make (the tally script was not changed)

- INDLOCAL: "TOTEX2 C.40 folded into R8 (13 Nov); new_results zip 158 entries".
- LM5_MULTI_GALOIS_TOPOI: "LM8 block (E.10, E.11) added 13 Nov; zip 681 entries".
- LM6_POINTS_AS_SECTIONS: "LM8 folded in as its fourth New-since block (13 Nov); new_results zip 79 entries; root PROMPT
  of the background zip refreshed".
- TOTAL_EXACT_2: "intake 13 Nov (Fable high): 89 consistent, 0 doubt, 0 wrong; 47 proofs read or recomputed, among
  them the whole chain of the main theorem".
- LM8_LIE_APPROXIMATIONS: "intake 13 Nov (Fable high): 161 consistent, 6 open, 0 doubt, 0 wrong; 32 proofs read,
  re-derived or recomputed; no PDF in checkpoint 16 (build and PDF check still to do)".
- DER_FOLLOWUP: "BLOCK_FOR_DER_FOLLOWUP.md written 13 Nov; the hold on A.2 and B.1 ends when the expert has applied it".
