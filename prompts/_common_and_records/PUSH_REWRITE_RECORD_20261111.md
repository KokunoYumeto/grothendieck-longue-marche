# Push rewrite of LM4–LM8: record (11 November 2026)

Written by `push_rewrite_20261111.py` with `followups_block.py` (Claude, Fable 5.2). The "after" figures include the follow-ups L1–L6 of the Dérivateurs reviews, folded into the Parts. Standard: `PUSH_STANDARD_AND_AUDIT_20261111.md`. Before-copies: `<name>/PROMPT_before_push_20261111.md`.

Demanding verbs are counted with the pattern `\b(prove|proves|proved|refute|decide|construct|compute|classify|determine|derive|exhibit|enumerate|tabulate|attack|carry out|write a program|by program|find)\b` (case-insensitive); the audit's own count used a shorter list, so compare within this table only.

## Parts: words and demanding verbs

| Prompt | Parts words before | verbs before | Parts words after | verbs after |
|---|---|---|---|---|
| LM4_FINITE_GROUP_ACTIONS | 275 | 10 | 2544 | 96 |
| LM5_MULTI_GALOIS_TOPOI | 291 | 4 | 2061 | 81 |
| LM6_POINTS_AS_SECTIONS | 387 | 9 | 2027 | 71 |
| LM7_FERMAT_TOWER | 298 | 6 | 1544 | 66 |
| LM8_LIE_APPROXIMATIONS | 213 | 3 | 1918 | 73 |

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
| LM4_FINITE_GROUP_ACTIONS | 429 | 0 | 767 | 23 | 827 | 3546 | 8566 |
| LM5_MULTI_GALOIS_TOPOI | 274 | 0 | 404 | 16 | 500 | 4981 | 8758 |
| LM6_POINTS_AS_SECTIONS | 411 | 1 | 566 | 15 | 658 | 2187 | 6131 |
| LM7_FERMAT_TOWER | 318 | 0 | 383 | 10 | 561 | 1982 | 5303 |
| LM8_LIE_APPROXIMATIONS | 303 | 0 | 411 | 14 | 678 | 1959 | 5987 |

## "What the outcome must be" (rule 0; added 11 November 2026, about 18:40 UTC)

Each of LM4–LM8 has the section before its Parts (text from `outcome_block.py`): deliverables with one row per statement and a table per item, lead and lettered task; the three outcomes that count as done; what is not acceptable; when the work is finished.

| Prompt | Outcome section words |
|---|---|
| LM4_FINITE_GROUP_ACTIONS | 510 |
| LM5_MULTI_GALOIS_TOPOI | 510 |
| LM6_POINTS_AS_SECTIONS | 510 |
| LM7_FERMAT_TOWER | 510 |
| LM8_LIE_APPROXIMATIONS | 510 |

## "After LM2" and rule 11 (added 12 November 2026)

After the LM2_LOOP_EQUATIONS return and its review (`..\pro_reviews_20261111\LM2_LOOP_EQUATIONS\REVIEW_author.md`): each of LM4–LM8 has a section "After LM2" and asks inside its Parts marked "after LM2" (`after_lm2_block.py`); LM8 Part B (d) no longer names the two linear symmetry equations as the graded form at `(0,3)`; the common block has rule 11 (a linearization is a statement to prove) and LM4–LM8 now take the current `_COMMON_BLOCK.md`. Per prompt: `<name>/CHANGES_20261112_LM2.md`. The figures of the first table above include these additions.

| Prompt | After LM2 section words | words of its asks in the Parts |
|---|---|---|
| LM4_FINITE_GROUP_ACTIONS | 594 | 242 |
| LM5_MULTI_GALOIS_TOPOI | 410 | 141 |
| LM6_POINTS_AS_SECTIONS | 558 | 160 |
| LM7_FERMAT_TOWER | 551 | 164 |
| LM8_LIE_APPROXIMATIONS | 638 | 240 |

## LM1 and LM2 (added 11 November 2026, about 18:45 UTC; restored 12 November)

This section is kept in `RECORD_LM12_SECTION.md` and appended by `push_rewrite_20261111.py`, because that script rewrites the record. On 12 November a rerun of the script dropped the section and anything that had been added to the record by hand after 18:45 UTC on 11 November; the figures below are restored from the run log of 11 November. Later hand additions by others, if there were any, are not restored.

The user corrected the record on 11 November: LM1_GROUP_SCHEMES and LM2_LOOP_EQUATIONS had not been sent. Both were rewritten by `lm12_push_20261111.py` in the same way as LM4–LM8 (demands on the items; "After LM3"; "After BISITE and the seven Dérivateurs returns"; "What the outcome must be"; new Parts), their shared rules were replaced by the common block of 11 November (rules 9–10), and both zips were rebuilt. Before-copies: `<name>/PROMPT_before_push_20261111.md`; previous zips and manifests: `<name>/<name>_background_v1.zip`, `MANIFEST_v1.tsv`. Do not rerun `lm12_push_20261111.py`: it writes into the upload folders, and LM2 has since been sent and answered.

| Prompt | Parts words before | verbs before | Parts words after | verbs after | Items words before → after | Items verbs before → after | After LM3 words | After BISITE words | Outcome section words |
|---|---|---|---|---|---|---|---|---|---|
| LM1_GROUP_SCHEMES | 271 | 5 | 1351 | 65 | 431 → 607 | 0 → 20 | 359 | 297 | 357 |
| LM2_LOOP_EQUATIONS | 300 | 8 | 1237 | 45 | 362 → 494 | 0 → 18 | 704 | 217 | 397 |

| Zip (as built 11 November) | files | bytes | previous kept as |
|---|---|---|---|
| LM1_GROUP_SCHEMES_background.zip | 186 | 68788745 | v1 |
| LM2_LOOP_EQUATIONS_background.zip | 191 | 39270444 | v1 |

LM2 was sent and has returned (79 statements). LM1 was not changed on 12 November: its prompt does not have rule 11 of the common block or an "After LM2" section.
