# SP73_C13_142+143 — consolidated diplomatic transcription

This archive contains the completed collation of all 24 requested scans: 18 from cote 142 and six from cote 143. Each page received a full first reading by one of the three readers, main-reader image adjudication, and a full independent second reading by a different reader after all first readings were completed. The manuscript ink controls the readings. Source slips, unfinished expressions and unresolved physical details are retained.

## Final files

| File or directory | Contents |
| --- | --- |
| `pages/` | The 24 final LaTeX page fragments, named as in witness C. |
| `SP73_C13_142+143_transcription.tex` | The complete fragment in page order, with cote and scan boundaries and no preamble. |
| `SP73_C13_142+143_changes.md` | Counts, consequential differences, every substantive comparison entry and the remaining doubts per page. |
| `SP73_C13_142+143_collation.tsv` | The comparisons against the supplied witness H text, with its page mapping and local evidence. |
| `decisions.tsv` | All 175 original source-mark decisions, in MARKS.tsv order. |
| `SP73_C13_142+143_doubts.md` | The reconciled notation table, remaining doubts, abbreviation expansions and legibility assessment. |
| `SP73_C13_142+143_inventory.csv` | The complete page inventories in physical reading order. |
| `SP73_C13_142+143_notes.md` | Brief English reading notes for every page, including literal slips, dates and sheet metadata, mathematical diagnostics and their limits. |
| `CHECK_EVENTS.tsv` | Mathematical work actually performed, with statement IDs, actors, dates, event types, outcomes and places. |
| `SP73_C13_142+143_sheet_feedback.md` | Error-sheet category counts, their locations and recurring additional failure modes. |
| `SP73_C13_142+143_hand_log.md` | Local handwriting and notation habits, their scope and witness misreadings. |
| `progress.log` | Page completion/audit history, checkpoint records, the transcription freeze and SHA-256 verification. |
| `crops/` | All retained evidence crops; their boxes refer to original scan coordinates. |

## Reading and comparison limits

There are **876 distinct substantive comparison locations**: **423 against C** and **651 against H**, with **198 shared** between those totals. Confidence is high at 623 locations, medium at 197 and low at 56. Certainty-only changes and differences of macro syntax alone are excluded from these counts. The inventories contain 753 elements, and 188 local uncertainties remain explicitly documented.

H has no supplied text for 142_scan109, so that page has no H-collation rows. H’s separate drawing files were not supplied. Figure comparisons therefore use its supplied local code, explicit local claims and individually named labels; generic descriptive silence is not evidence that a detail was absent from an unavailable drawing.

The 45 check events concern 43 distinct statement IDs. Two IDs have separately performed reader and main-reader events. Reading a statement is not reported as proving it, and conditional checks do not repair the manuscript. No external research, OCR or TeX compilation was used.

## Work documentation and verification

The `readings/`, `audits/`, `state/` and `scripts/` directories retain the work records, individual returns, assignments, adjudications, report-building code and validation tools. Earlier packets and original returns can contain proposals or comparison flags later superseded by main adjudication. Use the final page files and top-level reports for the consolidated result; `state/*_accepted.json` holds the integrated decisions. The final cross-page reconciliation is also recorded in `state/notation_reconciliation.md`.

`state/transcription_sha256.json` records SHA-256 values for exactly the 24 page files and the combined transcription. Their freeze and final unchanged verification are logged in `progress.log`. The archive is checked for CRC integrity and for exact agreement with those 25 hashes.

Original attachments, full scans, native halves and earlier checkpoint ZIPs are excluded from this archive. The evidence crops and work documentation are included. The supplied original PREAMBLE.tex remains the macro reference for the fragments.
