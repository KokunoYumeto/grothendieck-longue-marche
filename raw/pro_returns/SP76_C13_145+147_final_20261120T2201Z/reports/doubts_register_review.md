# Doubts register documentation review

> Historical coverage review of the state at 2026-11-20 20:43:53 UTC, before the later independent audits. Counts and recommendations below are retained as a dated snapshot. The recommended scan029 reason update was subsequently applied.

Checked: 2026-11-20 20:43:53 UTC.

## Findings

All **120 balanced uncertainty occurrences** in the current 24 page files are covered by the reports' **118 doubts entries**: 118 `\unsure` occurrences and 2 `\illegible` occurrences. There are **no missing occurrence-level entries and no stale resolved entries** in the current registers. Two entries legitimately cover more than one occurrence.

One existing doubt reason should be brought up to date with an additional unresolved possibility already recorded by the independent audit of 145_scan029. This is a report metadata recommendation; it does not call for a transcription change or a new ink judgment.

The check parsed complete balanced macro arguments, including nested braces, and matched complete macro contents or explicit preferred-reading/alternative pairs. Repeated short items were assigned by place. It did not accept a generic substring such as a single `s`, `0`, or `\tau` elsewhere on the page as coverage.

## Recommended report metadata update

**File:** `work/reports/145_scan029.json`  
**Target:** `doubts[5].reason` (zero-based JSON index; the sixth doubts entry)  
**Existing place:** `Struck product relation rho/exponent, not in MARKS.tsv`  
**Existing confidence:** `low`  
**Current page occurrence:** `work/pages/145_scan029.tex`, line 23, the obscured right end of the second relation  
**Existing independent-audit crop:** `crops/145_scan029_second_B22.png`  
**Audit box:** `B22`; actual bounds `[520, 1995, 1235, 2350]`, rotation `0` degrees.

The current row correctly covers the transcription's complete doubt: its preferred reading is the expression with a tentative canceled `-1` before the final `2`, and its explicit alternative is dotted rho to exponent `-2`. Audit B22 subsequently states that the second reader proposed a canceled `-2` before the final `2`, and that neither hidden numeral can be certified. That additional unresolved proposal currently appears in the audit evidence but is absent from this row's reason and alternatives, so it will not appear in the generated remaining-doubts table.

Recommended replacement for **the reason field only**, retaining the existing reading, alternatives, confidence, and place:

```json
"Final 2 legible, earlier exponent and prime/overdot position overlapped by dark revisions and block cancellation. Audit B22 additionally records that the second reading proposes a canceled -2 where the first proposed -1; neither hidden numeral can be certified."
```

This addition follows the committed B22 evidence. It records the unresolved proposal without choosing a prior numeral or asserting a revision sequence. The existing audit crop and its low confidence supply the provenance; no image was reinterpreted for this review.

## The rough diagnostic's two candidates are already covered

| Page occurrence | Existing doubts row | Why coverage is complete |
| --- | --- | --- |
| 145_scan029, line 16: `\unsure{\rho'\|\dot\rho'}` | `doubts[3]`, “Struck first generator, not in MARKS.tsv” | `reading` contains the complete preferred `\rho'`; the alternatives array separately contains `\dot\rho'`. The place and reason identify the locally canceled first generator. |
| 145_scan029, line 23: the whole rho/exponent uncertainty | `doubts[5]`, “Struck product relation rho/exponent, not in MARKS.tsv” | The complete first branch and the complete dotted-rho alternative are split between `reading` and `alternatives`. The coverage is valid; only the later B22 proposal described above needs to be carried into its reason. |

No new rows should be added for these candidates.

## Recent audit synchronization checks

| Page | Current register result |
| --- | --- |
| 145_scan028 | The former single canceled `_P` reading has been replaced in the register by the full two-zone covering expression. Its one grouped row covers both current uncertainty macros. The resolved dotted-tau uncertainty from B12 has no remaining doubts row. The canceled `conj.`, Gamma/F, and en/ou uncertainties remain registered. |
| 145_scan029 | All seven current uncertainties have distinct matching entries, including the two different tau issues: deletion state after rho, and the separately canceled symbol before the first decorated sigma. The B22 reason addition above is the sole recommended update. |
| 145_scan030 | All 14 occurrences are registered. The new first-commutation subscript, lower-left elements word, and short word before ss-groupe are present. The canceled starter now has Or/On/Ceci in both the page and the register; no stale Ceci-only row remains. |
| 145_scan031 | The i.e. row now records uncertain cancellation state rather than only uncertain letters. The new colon/semicolon row between the two en words is present. The resolved multiplication point from B09 has no remaining doubts row. |
| 145_scan033 | All nine occurrences are registered, including the new lac/loc Aut-subscript uncertainty. The two infinity/zero occurrences in formula (2) are separate rows, and the underlying canceled zero has its own row. The clipped tuple closing parenthesis and final comma remain registered. |

The named manuscript-mark decisions were also cross-checked against doubts rows that cite their IDs: no such row points to a resolved, unqualified reading in the current mark decisions. Lower confidence on a narrow doubtful feature was not automatically replaced by a whole-box audit confidence.

## Complete occurrence-to-register map

For each page, the last column lists the **one-based doubts row number** for each uncertainty macro in **TeX occurrence order**. This records place-specific assignments, including repeated identical macro text. A JSON array index is one less than the row number shown here.

| Page | Uncertainty occurrences | Doubts rows | Assigned doubts rows, in occurrence order |
| --- | ---: | ---: | --- |
| 145_scan028 | 5 | 4 | 1, 1, 2, 3, 4 |
| 145_scan029 | 7 | 7 | 1, 2, 3, 4, 7, 5, 6 |
| 145_scan030 | 14 | 14 | 1, 2, 3, 4, 12, 13, 5, 6, 7, 14, 8, 9, 10, 11 |
| 145_scan031 | 4 | 4 | 1, 2, 4, 3 |
| 145_scan033 | 9 | 9 | 1, 2, 3, 4, 5, 9, 6, 7, 8 |
| 145_scan034 | 6 | 6 | 1, 2, 3, 4, 5, 6 |
| 145_scan035 | 8 | 8 | 1, 2, 3, 4, 5, 6, 7, 8 |
| 145_scan036 | 10 | 9 | 1, 2, 3, 4, 5, 5, 6, 7, 8, 9 |
| 145_scan037 | 1 | 1 | 1 |
| 145_scan038 | 4 | 4 | 1, 2, 3, 4 |
| 147_scan003 | 3 | 3 | 1, 2, 3 |
| 147_scan004 | 2 | 2 | 1, 2 |
| 147_scan007 | 4 | 4 | 1, 2, 3, 4 |
| 147_scan008 | 5 | 5 | 1, 2, 3, 4, 5 |
| 147_scan009 | 0 | 0 | — |
| 147_scan010 | 2 | 2 | 1, 2 |
| 147_scan014 | 0 | 0 | — |
| 147_scan016 | 6 | 6 | 1, 2, 3, 4, 5, 6 |
| 147_scan017 | 6 | 6 | 1, 2, 3, 4, 5, 6 |
| 147_scan018 | 5 | 5 | 1, 2, 3, 4, 5 |
| 147_scan019 | 6 | 6 | 1, 2, 3, 4, 5, 6 |
| 147_scan021 | 3 | 3 | 1, 2, 3 |
| 147_scan022 | 3 | 3 | 1, 2, 3 |
| 147_scan023 | 7 | 7 | 1, 2, 3, 4, 5, 6, 7 |
| **Total** | **120** | **118** | Every occurrence and every register row accounted for |

The deliberate grouped mappings are 145_scan028 row 1, which contains both canceled covering zones, and 145_scan036 row 5, whose place explicitly names M0908 and M0909 and covers both S-alphabet occurrences in the same chain. Conversely, the two MD-prefix hyphens on 147_scan017 and the two clipped right-edge fragments on 147_scan023 are mapped to separate place-specific entries.

## Scope and limits

This review compares documentation and existing adjudications. It does not establish any new reading or ink evidence. No page TeX, report JSON, reading table, comparison, crop manifest, image ledger, or generated output was changed. No images were opened, and no OCR, external research, or TeX compilation was performed. Only this review file was written. Later changes to a page or its report will require a corresponding register check.
