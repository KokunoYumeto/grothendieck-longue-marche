# Were the late hours of LM7 and LM4 worth as much as the first ones?

Claude Fable 5.2 (Anthropic), effort max, the Longue Marche expert; 13 Nov 2026. Basis: the statement heads in
`LATE_ROWS_LM7_LM4_20261113.md` (about 150 characters of each), the LM7 reviewer's register-level reading
(`pro_reviews_max_20261112/LM7/BUILD_ON_20261113.md`), my reading of LM7's first return and of LM4 D.29, D.30,
D.63-D.65. No proof of a late row was read; their correctness is the other intake's question. I have not read the
statements of LM4's open items C.12, D.12, F.7, so for LM4 kind (a) means "is a step on the route to one of them".

## Answer

No. Per hour the late work is worth clearly less than the first hours: by my count a fifth to a tenth. It was still
worth running, because a handful of late rows are among the best in each return and the hours cost nothing extra.

- **LM7.** In 2.8 h: 103 rows, which hold nearly everything the prompt asked: the whole of Parts A to C, the
  corrections to the manuscript's formulas, the three open items reduced to exact statements, and E.32, E.34, E.36.
  In the next 11.4 h: 75 rows, and the same three items open. Rate: 37 rows an hour, then 6.6; of the late ones
  about one an hour bears on an open item.
- **LM4.** 189 rows in 8.9 h (21 an hour), then 19 rows in 2.6 h (7 an hour), with C.12, D.12, F.7 unchanged.
- **What the late hours did give.** E.37 settles the class-two layer of E.23, the first thing the follow-up prompt
  asks. E.61 and E.66 (ramified local sections are the nine cusp families) and E.44 (the criterion at every layer)
  are results for the companion. D.27 corrects an early row (the twelve shadows of D.25 are not genuine), which
  changed our own prompt LM7_PUSH. D.46 is a new candidate for D.19. LM4 D.63-D.65 are new theorems and are
  already used in LM8_PUSH (R22, task B.5).
- **What they mostly were.** Six tenths of LM7's late rows are computations along one chosen route: the section
  fibres of one inherited quotient, the norms and class groups of one tower of fields, and survival tests of
  replacement shadows along families of quotients that are not cofinal, which decide nothing about D.19.
- **Against a fresh prompt.** LM7_PUSH, aimed at the same three items, reached 137 rows in about six hours with
  four of its six Parts complete and the leads proved or refuted. A push prompt gets more per hour than letting the
  first run go on. A run whose last two checkpoints add only rows of kinds (c) and (d) on one route can be stopped
  and its open items sent as a push prompt.

## LM7_FERMAT_TOWER: 75 late rows (D.27-D.49, E.37-E.89 without E.63)

| Kind | Count | Examples |
|---|---|---|
| (a) bears on a main question or an open item | 13 | E.37 (the whole section map of N/gamma_3 N: E.23 at class two); D.27 (the twelve shadows removed) and D.46 (the surviving candidate): D.19; E.61, E.66 (ramified local sections are cuspidal). Also D.32, D.45, E.38, E.40, E.41, E.43, E.44, E.73. |
| (b) new and usable, for the companion or a prompt | 16 | D.40-D.44 (over every base with non-abelian simple even part the image is the full fibre product, so an obstruction can only sit at solvable bases); D.34-D.36 (the rank-four kernel is the marked curve w^3 = z(z-1), with its CM unit lifts); E.39, E.50, E.74 (structure of the local and global pro-3 sources). Also E.54, E.55, E.58, E.75, E.77. |
| (c) side computation or incremental case | 38 | E.46-E.52, E.56 (the fibres of the inherited quotient H over particular first classes); E.48, E.65, E.72, E.79, E.86, E.88 (norms, units and class groups in the towers over Q(17^(1/3^d))); D.28-D.31, D.33, D.37-D.39 (survival of a replacement through one more quotient). |
| (d) repeats or reworks earlier rows | 8 | E.57, E.64, E.69 (norm steps restated in full by E.72 and E.88); E.76, E.81, E.84 (class groups at levels 1 and 2, then at every level in E.86); E.67 (inside E.71); E.83 (inside E.87, E.89). |

D.13 has no late row.

## LM4_FINITE_GROUP_ACTIONS: 19 late rows (C.54-C.63, D.59-D.65, F.10, F.11)

| Kind | Count | Examples |
|---|---|---|
| (a) step on an open item | 6 | C.62 (every equal-level prefix interval lies in a compact three-word image; the step behind C.12, by the report), C.63, C.59, C.60; F.10, F.11 (the residual centralizer of the icosahedral action). |
| (b) new and usable | 3 | D.63 (the characters of the centralizer of a negative torus involution), D.64, D.65 (both standard centralizers are C_2^2, multipliers +1 and -1 only; the square criterion). |
| (c) side computation or incremental case | 8 | C.54, C.55, C.57, C.58 (contractions, word bounds, centralizer cases for the plane loop); D.59-D.62 (the lemmas that D.63-D.65 need). |
| (d) repeats or reworks | 2 | C.56 (the word bound, generalized in C.58); C.61 (strengthened to C.62 within the hour). |

## What this sorting cannot say

Counts are from statement heads; a row filed under (c) may carry a lemma that a later proof needs, and the split
between (c) and (d) in the E rows is the least certain. The comparison of rates takes the early rows at their
reviewed value (LM7: 88 correct, 12 known, 3 open, none wrong); the late rows are unreviewed.
