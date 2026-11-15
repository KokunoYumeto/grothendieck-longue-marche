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
