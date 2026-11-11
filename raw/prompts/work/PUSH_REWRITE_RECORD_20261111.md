# Push rewrite of LM4–LM8: record (11 November 2026)

Written by `push_rewrite_20261111.py` with `followups_block.py` (Claude, Fable 5.2). The "after" figures include the follow-ups L1–L6 of the Dérivateurs reviews, folded into the Parts. Standard: `PUSH_STANDARD_AND_AUDIT_20261111.md`. Before-copies: `<name>/PROMPT_before_push_20261111.md`.

Demanding verbs are counted with the pattern `\b(prove|proves|proved|refute|decide|construct|compute|classify|determine|derive|exhibit|enumerate|tabulate|attack|carry out|write a program|by program|find)\b` (case-insensitive); the audit's own count used a shorter list, so compare within this table only.

## Parts: words and demanding verbs

| Prompt | Parts words before | verbs before | Parts words after | verbs after |
|---|---|---|---|---|
| LM4_FINITE_GROUP_ACTIONS | 275 | 10 | 2302 | 86 |
| LM5_MULTI_GALOIS_TOPOI | 291 | 4 | 1920 | 75 |
| LM6_POINTS_AS_SECTIONS | 387 | 9 | 1867 | 62 |
| LM7_FERMAT_TOWER | 298 | 6 | 1380 | 58 |
| LM8_LIE_APPROXIMATIONS | 213 | 3 | 1663 | 59 |

For comparison, with the same pattern:

| Prompt | Parts words | verbs |
|---|---|---|
| LM1_GROUP_SCHEMES (sent) | 1351 | 65 |
| LM2_LOOP_EQUATIONS (sent) | 1237 | 45 |
| LM3_TEICHMULLER_TOWER (sent) | 362 | 4 |
| Dérivateurs 4_GALOIS (model) | 662 | 12 |
| Dérivateurs 7_BISITE | 755 | 12 |

## "What is to be settled": words and verbs; "After LM3"; whole prompt

| Prompt | Items words before | verbs before | Items words after | verbs after | After LM3 words | Prompt words before | after |
|---|---|---|---|---|---|---|---|
| LM4_FINITE_GROUP_ACTIONS | 429 | 0 | 767 | 23 | 827 | 3546 | 7494 |
| LM5_MULTI_GALOIS_TOPOI | 274 | 0 | 404 | 16 | 500 | 4981 | 7971 |
| LM6_POINTS_AS_SECTIONS | 411 | 1 | 566 | 15 | 658 | 2187 | 5177 |
| LM7_FERMAT_TOWER | 318 | 0 | 383 | 10 | 561 | 1982 | 4352 |
| LM8_LIE_APPROXIMATIONS | 303 | 0 | 411 | 14 | 678 | 1959 | 4858 |

## "What the outcome must be" (rule 0; added 11 November 2026, about 18:40 UTC)

Each of LM4–LM8 has the section before its Parts (text from `outcome_block.py`): deliverables with one row per statement and a table per item, lead and lettered task; the three outcomes that count as done; what is not acceptable; when the work is finished.

| Prompt | Outcome section words |
|---|---|
| LM4_FINITE_GROUP_ACTIONS | 357 |
| LM5_MULTI_GALOIS_TOPOI | 357 |
| LM6_POINTS_AS_SECTIONS | 357 |
| LM7_FERMAT_TOWER | 357 |
| LM8_LIE_APPROXIMATIONS | 357 |

## LM1 and LM2 (added 11 November 2026, about 14:40 UTC)

The user corrected the record: LM1_GROUP_SCHEMES and LM2_LOOP_EQUATIONS had not been sent. Both were rewritten by `lm12_push_20261111.py` in the same way (demands on the items; "After LM3"; "After BISITE and the seven Dérivateurs returns"; new Parts), their shared rules were replaced by today's `_COMMON_BLOCK.md` (rules 9–10), and both zips were rebuilt. Before-copies: `<name>/PROMPT_before_push_20261111.md`; previous zips and manifests: `<name>/<name>_background_v1.zip`, `MANIFEST_v1.tsv`.

| Prompt | Parts words before | verbs before | Parts words after | verbs after | Items words before → after | Items verbs before → after | After LM3 words | After BISITE words | Prompt words before → after |
|---|---|---|---|---|---|---|---|---|---|
| LM1_GROUP_SCHEMES | 271 | 5 | 1351 | 65 | 431 → 607 | 0 → 20 | 359 | 297 | 2023 → 4384 |
| LM2_LOOP_EQUATIONS | 300 | 8 | 1237 | 45 | 362 → 494 | 0 → 18 | 704 | 217 | 3126 → 5605 |

| Zip | files | bytes | previous kept as | files added | paths named in the prompt and absent |
|---|---|---|---|---|---|
| LM1_GROUP_SCHEMES_background.zip | 186 | 68788745 | v1 | 32 | B_4/, Z/, code/ |
| LM2_LOOP_EQUATIONS_background.zip | 191 | 39270444 | v1 | 35 | B_4/, code/, lean/ComparatorChallenges/, lean/docs/, return_2_later/ |

Both prompts have the section "What the outcome must be" (rule 0) before the Parts: LM1_GROUP_SCHEMES 357 words; LM2_LOOP_EQUATIONS 397 words. Rebuilt about 18:45 UTC.
