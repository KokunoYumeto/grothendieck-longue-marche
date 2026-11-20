# Static LaTeX and documentation review

Completed 2026-11-20 22:00:11 UTC after all 24 audits were committed. This report records source inspection and format-only repairs. **No TeX compilation was run.** No OCR, image inspection, blind-reading-table inspection, external research, or mathematical verification was performed in this review.

## Scope and supplied macro definitions

The authoritative sources are `work/pages/*.tex` and the combined `work/SP76_C13_145+147_transcription.tex`. Compatibility was checked against the supplied `source/SP76_C13_145+147_texts/PREAMBLE.tex`, including the actual definitions of `\deleted` and `\diagram`. No preamble was changed.

The two wrapper issues were source-compatibility defects, not optional typography changes. The supplied text-mode `\deleted` expands to `\sout`, so it cannot enclose the displayed environments as one text argument. The supplied `\diagram` captures its argument before TikZ reads a matrix; raw ampersands therefore have the wrong category code unless an explicit replacement token is used. Local installed package sources were consulted; no TeX engine was run.

## Exact format-only repairs

1. `work/pages/145_scan029.tex`: split the broad cancellation around two displayed formulas and their intervening prose into three cancellation spans. Each display now contains `\deleted{\displaystyle ...}`, and the intervening inserted parenthesis plus “avec les relations” remains inside a text `\deleted{...}`. The three original content segments were preserved verbatim. Existing local deletion, insertion and uncertainty scopes remain inside them. `\displaystyle` restores display style within the supplied deletion macro’s math box.
2. `work/pages/147_scan008.tex`: its one `tikzcd` environment now declares `[ampersand replacement=\&]`; its three matrix cell separators use `\&`.
3. `work/pages/147_scan009.tex`: both `tikzcd` environments now declare the same option; their three matrix cell separators in total use `\&`.

For 008 and 009, removing the added options and reversing those separator substitutions reproduced the original entire file exactly. The 029 repair asserted verbatim retention of each moved content segment. No symbol, word, mathematical relation, diagram label, arrow, reading alternative, or revision-state decision was changed.

## Exact wording repairs

- `work/reports/147_scan009.json`, `notes[1]`: “The complete systems remain in the future blind-reading boxes.” became “The complete systems were included in the independent-reading boxes and audited.”
- `work/reports/145_scan034.json`, `notes[0]`: “the draft retains both live terme” became “the final transcription retains both live terme”.
- `work/scripts/build_outputs.py`: the feedback sentence after the count of unchanged-C resolutions now reads: “These are excluded from corrections against C; independently flagged differences from H remain included in the H counts.” This clarifies the unchanged counting logic; no flags, classifications or arithmetic were changed.

The current notes and reporting supplements contain no remaining misleading present-tense claim that the completed independent reading is still future work. References to crops inspected during the first pass describe historical actions. The earlier doubts-register review remains a historical snapshot and is superseded for current coverage by `work/reports/final_doubts_coverage.md`.

## Metadata-only reconciliations

| Report | Field | Reconciliation |
| --- | --- | --- |
| 147_scan017.json | inventory[10].first_words_or_objects | Canceled adjective: unsure{standart\|stable}. |
| 147_scan019.json | inventory[10].first_words_or_objects | Canceled index: unsure{alpha\|nu}. |
| 147_scan019.json | inventory[12].first_words_or_objects | Canceled category word: unsure{catégorie\|catég.}. |
| 147_scan021.json | notes[0] | General note now includes le / les / la. |
| 147_scan022.json | doubts[2].place | Barred-m shorthand replaces the stale equals-shorthand label. |
| 147_scan022.json | changes[9].place | Barred-m shorthand replaces the stale verbal-equals label. |
| 147_scan022.json | inventory[2].first_words_or_objects | Existing NB excerpt expanded to show the audited barred m and the following des / de uncertainty. |

These changes copy current page/audit readings into descriptive metadata. They do not alter page readings, mark decisions, evidence prose, change flags, confidences, audit records, or frozen provenance. Each JSON edit was checked by reverting only its authorized fields in memory and comparing with the original object.

## Static checks and their limits

All 24 authoritative page files passed balanced-group, written math-delimiter, and environment-order checks. The three repaired `tikzcd` environments have no raw cell-separator ampersands. The command inventory contains no undefined nonstandard command relative to the supplied preamble and its packages. In particular, `\rotatebox` is available through PGF’s loading of graphicx; `\ldots` is valid in text as well as math. No additional malformed environment, active editorial prose, or incompatible wrapper was identified. No optional typesetting restyling was applied.

At the final check, the combined fragment exactly matched the authoritative page files in `work/page_order.txt` order with the expected cote separators. `build_outputs.py` passed an in-memory Python syntax check without execution. No rendered layout or compilation success is claimed. Line breaking and the appearance of long struck displays remain outside this static review.

## Independent count reconciliation after 023

The current 24 reports contain **466 change rows**: **118 against C**, **395 against H**, and **452 distinct substantive places** carrying at least one witness flag. Row confidence totals are **341 high, 68 medium, 57 low**. Against-C confidence totals are 60 high / 38 medium / 20 low; against-H totals are 289 high / 55 medium / 51 low. The generated changes total, all ten generated feedback classes, and all 395 collation rows agree with the current flags.

| Requested class | Against C | Against H | Distinct substantive places |
| --- | --- | --- | --- |
| Symbols and indices | 32 | 41 | 61 |
| Words | 20 | 87 | 103 |
| Omissions | 11 | 53 | 55 |
| Drawings and diagrams | 1 | 4 | 5 |
| Readable ink left as illegible | 3 | 31 | 32 |
| Insertions put in the wrong place | 6 | 34 | 38 |
| Struck text | 8 | 25 | 28 |
| Abbreviations expanded, spelling modernised | 16 | 48 | 49 |
| Text that is not on the page | 8 | 27 | 30 |
| Other | 13 | 45 | 51 |
| TOTAL | 118 | 395 | 452 |

There are 35 rows carrying `certainty_resolution_C`. Three also carry a substantive against-C flag, leaving **32 resolutions of an unchanged C reading**. Of those 32, 18 independently differ from H and are included in H’s 395 rows; the remaining 14 carry neither substantive witness flag. This explains 466 total rows versus 452 substantive places without altering any flags.

## Final doubts coverage and regeneration

All **147 active uncertainty occurrences** map to the **145 remaining-doubts entries**, including all seven occurrences on 147_scan023. The complete place-specific map is in `work/reports/final_doubts_coverage.md`. All 72 marked-decision readings and all 35 certainty-resolution final readings occur in their current page text; no resolved C mark remains listed by identifier as an unresolved doubt.

This agent did not rebuild combined outputs. The parent’s rebuild after committing 023 already includes the page wrapper repairs. Final regeneration of derived inventory, changes, notes and doubts from the subsequently reviewed report metadata is handled by the parent workflow before freeze and packaging. No immutable first readings, target-selection boxes, crop manifests, blind-reading files, comparisons, or image ledgers were altered.
