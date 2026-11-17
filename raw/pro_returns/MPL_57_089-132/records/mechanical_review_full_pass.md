# Mechanical review of page sources and metadata

2026-11-17 17:41:37 UTC

43 page files; 771 inventory rows; 43 page records, of which 43 contain reader audit metadata; 340 doubt macro instances; 129 TikZ arrow commands.

This review reads only transcription files and their metadata. It does not inspect scans or context, adjudicate readings, establish omissions, or replace the visual audit. The earlier partial combined transcription may intentionally be stale during auditing.

## Basic validation

No errors or warnings.

## Record schema

No issues detected.

## Control characters

No issues detected.

## Additional structural and TikZ heuristics

No issues detected.

## Inventory field/identifier checks

No issues detected.

## Macro-to-inventory counts

A discrepancy can reflect nested or grouped elements. The explanations below use only explicit source nesting and inventory labels. They do not certify visual completeness. Explanations apply only to the listed count pairs.

| Scan | Macro | Inventory kind | Macro count | Row count | Structural explanation |
|---|---|---|---:|---:|---|
| 092 | `margin` | margin note | 3 | 1 | Explained: two margin macros contain diagrams covered by diagram inventory rows 14–15; the remaining macro is margin-note row 18. |
| 094 | `margin` | margin note | 4 | 3 | Explained: one margin macro contains the cancelled diagram and associated cancelled condition, covered by diagram/deletion rows 7–8. |
| 094 | `deleted` | deletion | 10 | 4 | Explained: six deleted object/relation labels are inside the diagram covered by diagram row 7; four other deletion rows describe the remaining cancelled blocks. |
| 097 | `margin` | margin note | 4 | 6 | Explained: one margin macro is the cancelled note covered by deletion row 33; three table annotations are separately covered by margin-note rows 9, 13, and 14. |
| 097 | `deleted` | deletion | 10 | 9 | Explained: deletion row 24 explicitly groups the two separately marked deleted T tokens. |
| 102 | `margin` | margin note | 4 | 3 | Explained: one margin macro contains the diagram covered by diagram row 4. |
| 102 | `inserted` | insertion | 1 | 5 | Explained: four labels placed beneath relations are represented using underset, and covered by insertion rows 17 and 19–21. |
| 105 | `margin` | margin note | 3 | 2 | Explained: one margin macro wraps the cancelled note covered by deletion row 19. |
| 111 | `margin` | margin note | 5 | 2 | Explained: two margin macros contain diagrams and one contains the audit-added separating-stroke drawing; those elements are inventoried by their diagram/drawing kinds. |
| 112 | `deleted` | deletion | 8 | 6 | Explained: three paragraph-level deletion macros represent the cancelled whole manuscript body covered collectively by deletion row 1; the five inner cancellations have their own rows. |
| 117 | `margin` | margin note | 8 | 2 | Explained: seven margin macros wrap audit-added drawings; the two margin-note rows describe one margin macro and the top-center mspage number 20. |
| 119 | `margin` | margin note | 14 | 3 | Explained: twelve margin macros wrap audit-added drawings; the three margin-note rows describe two margin macros and the top-center mspage number 19. |
| 124 | `margin` | margin note | 2 | 1 | Explained: one margin macro wraps the audit-added emphasis-stroke drawing, inventoried as a drawing. |
| 126 | `margin` | margin note | 3 | 2 | Explained: one margin macro wraps the audit-added emphasis-stroke drawing, inventoried as a drawing. |
| 127 | `margin` | margin note | 5 | 4 | Explained: one margin macro wraps the audit-added pointer drawing, inventoried as a drawing. |
| 129 | `margin` | margin note | 2 | 1 | Explained: one margin macro wraps the audit-added corollary-stroke drawing, inventoried as a drawing. |
| 131 | `margin` | margin note | 3 | 2 | Explained: one margin macro wraps the audit-added lemma-stroke drawing, inventoried as a drawing. |

## Prime/exclamation candidates

These are literal source tokens identified in math-like regions. They are not classifications of manuscript ink. Apostrophes inside notation can have several roles.

| Scan | Source line | Token |
|---|---:|---|
| 094 | 14 | `X'` |
| 094 | 14 | `S'` |
| 094 | 14 | `X'` |
| 094 | 14 | `S'` |
| 094 | 17 | `X'` |
| 094 | 17 | `X''` |
| 094 | 18 | `S'` |
| 094 | 18 | `S''` |
| 094 | 22 | `X'` |
| 094 | 22 | `X''` |
| 101 | 20 | `X'` |
| 101 | 20 | `U'` |
| 101 | 20 | `X'` |
| 101 | 20 | `U'` |
| 101 | 20 | `X'` |
| 102 | 2 | `X'` |
| 102 | 2 | `U'` |
| 102 | 2 | `X'` |
| 102 | 2 | `i'` |
| 102 | 2 | `U'` |
| 102 | 2 | `X'` |
| 102 | 5 | `E'` |
| 102 | 6 | `X'` |
| 102 | 6 | `U'` |
| 102 | 6 | `k'` |
| 102 | 6 | `i'` |
| 102 | 7 | `k'` |
| 102 | 11 | `X'` |
| 102 | 11 | `U'` |
| 102 | 13 | `X'` |
| 102 | 14 | `U'` |
| 102 | 18 | `X'` |
| 102 | 19 | `U'` |
| 102 | 23 | `E'` |
| 102 | 25 | `X'` |
| 102 | 25 | `U'` |
| 102 | 27 | `U'` |
| 102 | 27 | `X'` |
| 102 | 29 | `E'` |
| 102 | 29 | `X'` |
| 102 | 29 | `i'` |
| 102 | 29 | `E'` |
| 102 | 31 | `i'` |
| 102 | 31 | `i'` |
| 102 | 31 | `E'` |
| 102 | 31 | `i'` |
| 102 | 31 | `i'` |
| 102 | 31 | `E'` |
| 102 | 31 | `i'` |
| 102 | 31 | `U'` |
| 102 | 31 | `X'` |
| 102 | 31 | `E'` |
| 102 | 35 | `E'` |
| 102 | 35 | `i'` |
| 102 | 35 | `i'` |
| 102 | 35 | `E'` |
| 103 | 2 | `U'` |
| 103 | 2 | `X'` |
| 106 | 6 | `S'` |
| 107 | 3 | `\prime` |
| 107 | 3 | `Z'` |
| 107 | 4 | `X'` |
| 107 | 5 | `S'` |
| 107 | 7 | `s'` |
| 107 | 7 | `a'` |
| 107 | 7 | `X'` |
| 107 | 7 | `S'` |
| 107 | 7 | `Z'` |
| 107 | 7 | `S'` |
| 107 | 13 | `Z'` |
| 107 | 13 | `S'` |
| 107 | 13 | `Z'` |
| 107 | 13 | `s'` |
| 107 | 13 | `Z'` |
| 107 | 13 | `a'` |
| 107 | 13 | `s'` |
| 107 | 15 | `L'` |
| 107 | 15 | `a'` |
| 107 | 15 | `a'` |
| 107 | 15 | `X'` |
| 107 | 15 | `S'` |
| 107 | 15 | `X'` |
| 107 | 15 | `a'` |
| 108 | 2 | `L'` |
| 108 | 2 | `X'` |
| 108 | 2 | `D'` |
| 108 | 3 | `L'` |
| 108 | 3 | `L'` |
| 108 | 5 | `D'` |
| 108 | 5 | `X'` |
| 108 | 5 | `X'` |
| 108 | 5 | `s'` |
| 108 | 7 | `D'` |
| 108 | 7 | `X'` |
| 108 | 7 | `s'` |
| 108 | 9 | `D'` |
| 108 | 9 | `X'` |
| 108 | 9 | `s'` |
| 108 | 9 | `X'` |
| 108 | 9 | `s'` |
| 108 | 9 | `D'` |
| 108 | 9 | `X'` |
| 108 | 9 | `s'` |
| 108 | 9 | `X'` |
| 108 | 9 | `s'` |
| 108 | 11 | `L'` |
| 108 | 13 | `L'` |
| 108 | 13 | `s'` |
| 108 | 13 | `D'` |
| 108 | 13 | `s'` |
| 108 | 15 | `D'` |
| 108 | 15 | `s'` |
| 108 | 15 | `D'` |
| 108 | 15 | `a'` |
| 108 | 15 | `s'` |
| 108 | 15 | `Z'` |
| 108 | 15 | `s'` |
| 109 | 2 | `Z'` |
| 109 | 2 | `a'` |
| 109 | 2 | `s'` |
| 109 | 2 | `Z'` |
| 109 | 2 | `s'` |
| 109 | 4 | `D'` |
| 109 | 4 | `L'` |
| 109 | 4 | `D'` |
| 110 | 2 | `D'` |
| 110 | 2 | `D'` |
| 110 | 2 | `D'` |
| 110 | 2 | `D'` |
| 110 | 4 | `S'` |
| 110 | 4 | `S'` |
| 110 | 4 | `X'` |
| 110 | 4 | `S'` |
| 111 | 15 | `D'` |
| 111 | 15 | `D'` |
| 112 | 2 | `D'` |
| 112 | 2 | `S'` |
| 112 | 4 | `D'` |
| 112 | 4 | `s'` |
| 112 | 4 | `D'` |
| 112 | 4 | `a'` |
| 112 | 4 | `s'` |
| 112 | 6 | `D'` |
| 112 | 6 | `a'` |
| 112 | 6 | `a'` |
| 112 | 6 | `s'` |
| 112 | 6 | `D'` |
| 112 | 6 | `s'` |
| 112 | 6 | `a'` |
| 112 | 6 | `s'` |
| 112 | 9 | `D'` |
| 113 | 8 | `R'` |
| 113 | 8 | `R'` |
| 114 | 2 | `R'` |
| 114 | 2 | `R'` |
| 114 | 2 | `D'` |
| 114 | 2 | `D'` |
| 114 | 2 | `D'` |
| 114 | 2 | `R'` |
| 117 | 3 | `X'` |
| 117 | 3 | `S'` |
| 117 | 3 | `X'` |
| 117 | 3 | `X'` |
| 117 | 3 | `S'` |
| 117 | 3 | `X'` |
| 117 | 3 | `S'` |
| 117 | 3 | `S'` |
| 117 | 3 | `X'` |
| 117 | 3 | `X'` |
| 117 | 3 | `X'` |
| 117 | 3 | `X'` |
| 117 | 3 | `S'` |
| 117 | 3 | `X'` |
| 117 | 3 | `S'` |
| 117 | 7 | `S'` |
| 117 | 9 | `U'` |
| 117 | 9 | `U'` |
| 117 | 9 | `S'` |
| 117 | 9 | `S'` |
| 117 | 9 | `S'` |
| 117 | 9 | `X'` |
| 117 | 9 | `S'` |
| 117 | 9 | `S'` |
| 117 | 13 | `S'` |
| 117 | 13 | `f'` |
| 117 | 13 | `X'` |
| 117 | 13 | `Y'` |
| 117 | 13 | `f'` |
| 117 | 13 | `f'` |
| 119 | 3 | `S'` |
| 119 | 3 | `S'` |
| 119 | 5 | `S'` |
| 119 | 7 | `X'` |
| 119 | 7 | `Y'` |
| 119 | 7 | `S'` |
| 119 | 7 | `X''` |
| 119 | 7 | `Y''` |
| 119 | 7 | `S''` |
| 119 | 7 | `S'` |
| 119 | 7 | `S'` |
| 119 | 9 | `S'` |
| 119 | 9 | `X'` |
| 119 | 9 | `Y'` |
| 119 | 9 | `S''` |
| 119 | 9 | `X''` |
| 119 | 9 | `Y''` |
| 119 | 11 | `S'` |
| 119 | 11 | `X'` |
| 119 | 11 | `Y'` |
| 119 | 11 | `X'` |
| 119 | 11 | `Y'` |
| 119 | 11 | `S''` |
| 119 | 11 | `S'` |
| 119 | 13 | `S'` |
| 119 | 13 | `S'` |
| 119 | 15 | `S'` |
| 119 | 15 | `X'` |
| 119 | 15 | `X'` |
| 119 | 15 | `S'` |
| 119 | 15 | `S'` |
| 119 | 15 | `k'` |
| 119 | 15 | `S'` |
| 119 | 15 | `S'` |
| 119 | 15 | `X'` |
| 119 | 15 | `S'` |
| 119 | 15 | `S'` |
| 119 | 15 | `X'` |
| 123 | 43 | `t'` |
| 123 | 43 | `t'` |
| 124 | 6 | `n''` |
| 124 | 15 | `Y'` |
| 124 | 15 | `Y'` |
| 124 | 15 | `Y'` |
| 126 | 2 | `X'` |
| 126 | 2 | `X''` |
| 126 | 2 | `X'` |
| 126 | 2 | `X'` |
| 126 | 2 | `X''` |
| 126 | 2 | `X'` |
| 126 | 2 | `X'` |
| 126 | 2 | `X'` |
| 126 | 2 | `f''` |
| 126 | 2 | `f''` |
| 126 | 5 | `f'` |
| 126 | 5 | `X'` |
| 126 | 5 | `f'` |
| 126 | 5 | `X'` |
| 126 | 5 | `f'` |
| 126 | 5 | `a'` |
| 126 | 5 | `f'` |
| 126 | 5 | `g'` |
| 126 | 5 | `X'` |
| 126 | 5 | `a'` |
| 126 | 5 | `Z'` |
| 126 | 5 | `Z''` |
| 126 | 5 | `X'` |
| 126 | 5 | `X''` |
| 126 | 5 | `Z'` |
| 126 | 5 | `a'` |
| 126 | 5 | `g'` |
| 126 | 5 | `a'` |
| 126 | 5 | `Z'` |
| 126 | 5 | `X''` |
| 126 | 5 | `X'` |
| 126 | 5 | `X'` |
| 126 | 5 | `X''` |
| 126 | 5 | `X'` |
| 126 | 5 | `X'` |
| 126 | 5 | `X'` |
| 126 | 7 | `X'` |
| 126 | 7 | `f'` |
| 126 | 7 | `a'` |
| 126 | 7 | `f'` |
| 126 | 7 | `f''` |
| 126 | 7 | `f''` |
| 126 | 7 | `a'` |
| 126 | 7 | `a''` |
| 126 | 7 | `Z'` |
| 126 | 7 | `f'` |
| 126 | 7 | `Z'` |
| 126 | 7 | `Z''` |
| 126 | 9 | `f'` |
| 126 | 9 | `X'` |
| 126 | 9 | `a'` |
| 126 | 11 | `Z'` |
| 126 | 13 | `X'` |
| 126 | 15 | `g'` |
| 126 | 15 | `g'` |
| 126 | 15 | `a'` |
| 126 | 15 | `X'` |
| 126 | 15 | `Z'` |
| 126 | 17 | `a'` |
| 126 | 17 | `X'` |
| 126 | 17 | `a'` |
| 126 | 20 | `X'` |
| 126 | 20 | `a'` |
| 126 | 20 | `X'` |
| 126 | 20 | `a'` |
| 127 | 2 | `X'` |
| 127 | 2 | `S'` |
| 127 | 2 | `L'` |
| 127 | 2 | `X'` |
| 127 | 2 | `g'` |
| 127 | 2 | `i'` |
| 127 | 2 | `L'` |
| 127 | 4 | `f'` |
| 127 | 4 | `a'` |
| 127 | 4 | `S'` |
| 127 | 5 | `X'` |
| 127 | 5 | `S'` |
| 127 | 5 | `g'` |
| 127 | 5 | `a'` |
| 127 | 5 | `X'` |
| 127 | 5 | `Z'` |
| 127 | 11 | `L'` |
| 127 | 11 | `L'` |
| 127 | 12 | `L'` |
| 127 | 12 | `L'` |
| 127 | 14 | `Z'` |
| 127 | 14 | `i'` |
| 127 | 14 | `L'` |
| 127 | 15 | `i'` |
| 127 | 15 | `L'` |
| 127 | 21 | `T''` |
| 127 | 23 | `g'` |
| 127 | 23 | `i'` |
| 127 | 27 | `X'` |
| 127 | 27 | `X''` |
| 127 | 27 | `X''` |
| 127 | 28 | `Z'` |
| 127 | 28 | `i'` |
| 127 | 28 | `Z''` |
| 127 | 28 | `i''` |
| 127 | 29 | `a'` |
| 127 | 29 | `g'` |
| 127 | 31 | `g'` |
| 128 | 2 | `L'` |
| 128 | 2 | `L'` |
| 128 | 2 | `i''` |
| 128 | 2 | `L'` |
| 128 | 2 | `i''` |
| 128 | 2 | `L'` |
| 128 | 2 | `Z''` |
| 128 | 2 | `Z'` |
| 128 | 2 | `i'` |
| 128 | 2 | `L'` |
| 128 | 2 | `i'` |
| 128 | 2 | `g'` |
| 128 | 2 | `L'` |
| 128 | 2 | `a'` |
| 128 | 4 | `f''` |
| 128 | 4 | `Z'` |
| 128 | 5 | `f''` |
| 128 | 5 | `Z''` |
| 128 | 5 | `a'` |
| 129 | 2 | `Z'` |
| 129 | 2 | `X''` |
| 129 | 2 | `1''` |
| 129 | 2 | `3''` |
| 129 | 2 | `Z''` |
| 129 | 2 | `i''` |
| 129 | 2 | `1''` |
| 129 | 2 | `X''` |
| 129 | 2 | `Z''` |
| 130 | 11 | `F'` |
| 130 | 11 | `F''` |
| 130 | 13 | `F'` |
| 130 | 13 | `F''` |
| 130 | 14 | `F'` |
| 130 | 14 | `F''` |
| 130 | 18 | `F'` |
| 130 | 18 | `F''` |
| 131 | 8 | `k'` |
| 131 | 8 | `k'` |
| 131 | 8 | `k'` |
| 131 | 8 | `X'` |
| 131 | 16 | `X'` |
| 131 | 16 | `X''` |

## Quote-token counts outside TikZ syntax

Math-region tokens are excluded, except in explicit text groups, so double primes are not counted as closing quotation marks. Literal double quotes inside TikZ environments are excluded because arrow-label syntax uses them. Paired backticks/apostrophes are counted as tokens, not globally paired across unrelated passages. The scan 117 source shares one closing quote between a deleted opening and its inserted replacement; scan 127 uses three standalone opening-quote tokens in inserted labels. These structural facts explain their count imbalances without changing readings.

| Scan | Token | Count |
|---|---|---:|
| 095 | two apostrophes | 1 |
| 095 | two backticks | 1 |
| 096 | two apostrophes | 1 |
| 096 | two backticks | 1 |
| 100 | two apostrophes | 2 |
| 100 | two backticks | 2 |
| 116 | two apostrophes | 1 |
| 116 | two backticks | 1 |
| 117 | two apostrophes | 6 |
| 117 | two backticks | 7 |
| 119 | two apostrophes | 1 |
| 119 | two backticks | 1 |
| 120 | two apostrophes | 1 |
| 120 | two backticks | 1 |
| 122 | two apostrophes | 1 |
| 122 | two backticks | 1 |
| 123 | two apostrophes | 1 |
| 123 | two backticks | 1 |
| 127 | two backticks | 3 |

## Pic macro variants

The table reports lexical variants only. An underlined occurrence and a bare occurrence may both accurately represent the page.

| Variant | Scan: count |
|---|---|
| `bare \mathrm{Pic}` | 097: 20, 099: 2 |
| `bare \operatorname{Pic}` | 101: 2, 102: 4, 103: 4 |
| `underline + \mathrm{Pic}` | 089: 1, 091: 13, 092: 1, 100: 5 |
| `underline + \operatorname{Pic}` | 101: 3, 105: 2, 106: 1, 109: 1, 110: 2, 111: 1, 112: 1, 126: 8, 127: 4, 129: 6, 131: 7 |

## Greek command variants

All distinctions are preserved; their presence is not a reason to normalize any reading.

| Command | Scan: count |
|---|---|
| `\alpha` | 099: 3, 100: 1, 117: 9, 119: 8, 120: 2, 122: 7, 130: 34, 132: 1 |
| `\beta` | 122: 2, 130: 6 |
| `\Gamma` | 090: 9, 095: 13, 120: 1, 121: 2, 130: 14 |
| `\Delta` | 110: 4 |
| `\varepsilon` | 118: 2, 123: 9, 124: 8 |
| `\eta` | 105: 5, 107: 5, 108: 4, 109: 7, 110: 5, 111: 3, 112: 6 |
| `\theta` | 090: 6, 095: 4 |
| `\Theta` | 112: 7 |
| `\lambda` | 090: 6, 095: 4 |
| `\mu` | 099: 3, 100: 1 |
| `\xi` | 089: 2, 094: 1, 095: 7, 120: 1 |
| `\pi` | 097: 3, 099: 2, 108: 2 |
| `\rho` | 097: 6 |
| `\sigma` | 095: 9, 105: 1, 109: 3, 122: 2 |
| `\Sigma` | 126: 25, 127: 6, 128: 2 |
| `\tau` | 097: 5, 100: 4, 101: 1 |
| `\varphi` | 108: 6, 109: 1, 127: 5, 130: 8 |
| `\psi` | 127: 6 |
| `\omega` | 089: 3, 091: 11, 092: 4 |
| `\Omega` | 089: 2, 091: 1, 092: 2, 100: 4 |
