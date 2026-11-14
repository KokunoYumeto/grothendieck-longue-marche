# Reviews of 14 November 2026: the refereed chain behind Δ, and the field expert's reading of it

What this folder holds, and who wrote each file. The mathematics refereed here is GPT-6 Astra's (OpenAI, ChatGPT Pro
mode), in the runs LM7_PUSH (checkpoint 09) and LM4_FINITE_GROUP_ACTIONS, whose raw returns are in `raw/pro_returns/`.

| File | Written by | What |
|---|---|---|
| `referee/REFEREE_A_D50_E58.md` | referee A, Claude Opus 5.5 (Anthropic, effort max) | LM7_PUSH D.44 (the parts used), D.50 and E.58, checked line by line: proved as claimed |
| `referee/REFEREE_A_LM4_D32.md` | referee A | LM4 D.32 (finite subgroups of the three-cusp group have order at most two): proved as claimed |
| `referee/REFEREE_B_E61_E65.md` | referee B, Claude Opus 5.5 (Anthropic, effort max) | LM7_PUSH E.61-E.67: E.65 proved, with two gaps closed by the referee; E.61 proved; E.64 proved where checkable; E.67's general statements proved |
| `referee/REFEREE_B_LM4_D34.md` | referee B | LM4 D.34 (every involution has multiplier -1): proved as claimed |
| `referee/checks/*.py`, `*.out` | the referees | the finite computations the reports cite, with their outputs |
| `CONSULT_LM_EXPERT.md`, `CONSULT_LM_EXPERT_2.md` | the Longue Marche field expert, Claude Fable 5.2 (Anthropic, effort max) | the expert's reading of the referee verdicts |
| `EXPERT_IMPLICATIONS_E65_LM.md` | the same expert | what follows from the character Δ: GT0-hat → F_2 (vanishing on Galois, non-zero on E.58's element): the dichotomy for E.3, torsion, section 47, hunches, and eight items for GPT-6 Astra |

The referees' finite computations prove finite statements only; the general statements rest on the proofs in the
reports.
