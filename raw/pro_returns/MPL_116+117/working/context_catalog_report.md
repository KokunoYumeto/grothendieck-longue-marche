# Mechanical context coverage catalogue

Created 2026-11-17 18:36:34 UTC.

## Source coverage

- DSS: **255** rows; STRATA 10, PATHS 76, BISITE 113, RESIDUE 56.
- NEW_RESULTS: **15** items: numbered rows 1–12 and three unnumbered “Known after all” coda entries (Isbell–Mitchell; Nielsen realization; localiseur spécial/accessibility).
- DSS IDs are unique. No missing numerical IDs have been invented or repaired; the source selects particular sections.
- All 255 DSS rows have exactly four table columns; all 12 numbered NEW_RESULTS rows have exactly six. The internal mathematical bar in BISITE A.28 is preserved.
- No pre-existing partial catalog files were found before this catalog was written.

## Status and locator boundaries

- DSS statuses are copied literally, including `claim (return: ...)`; no status is upgraded.
- NEW_RESULTS has no formal status column. The exact `Checked by` and `Proved by` cells are retained separately; the three coda items retain their shared “Known after all” status.
- DSS has 16 blank manuscript-locator cells: RESIDUE B.2; RESIDUE B.4; RESIDUE B.9; RESIDUE B.10; RESIDUE C.1; RESIDUE C.4; RESIDUE C.5; RESIDUE C.8; RESIDUE D.7; RESIDUE D.9; RESIDUE F.5; RESIDUE F.6; RESIDUE F.7; RESIDUE I.7; RESIDUE J.2; RESIDUE J.3.
- DSS statement cells containing an ellipsis character: none. No explicit source truncation marker was found in the DSS statement cells; this does not certify source correctness or completeness of the original research returns.
- Many RESULTS_STATE excerpts are visibly truncated with an ellipsis. The exact excerpts, status text, line numbers and original register-source filenames are preserved in the JSON; no missing statement text is reconstructed.
- The three coda entries are short bibliographic notices; only the Isbell–Mitchell notice points back to numbered item 11, and none supplies its own manuscript page range.

## Exact same-ID RESULTS_STATE entries

15 of the 255 DSS IDs have their own structured status entry in RESULTS_STATE:

- PATHS D.22: state line 438 [Open (the return's claim)]
- BISITE A.19: state line 455 [Proved (the return's claim)]
- BISITE B.21: state line 428 [Open (the return's claim)]
- BISITE B.22: state line 456 [Proved (the return's claim)]
- BISITE C.1: state line 447 [Proved (the return's claim)]
- BISITE C.3: state line 457 [Refuted (the return's claim)]
- BISITE C.10: state line 441 [Open (the return's claim)]
- BISITE F.18: state line 429 [Open (the return's claim)]
- BISITE G.10: state line 459 [Proved (the return's claim)]
- RESIDUE D.9: state line 439 [Open (the return's claim)]
- RESIDUE F.3: state line 473 [Proved (the return's claim)]
- RESIDUE F.5: state line 421 [Open (the return's claim)]
- RESIDUE F.6: state line 422 [Open (the return's claim)]
- RESIDUE F.7: state line 425 [Open (the return's claim)]
- RESIDUE I.7: state line 426 [Open (the return's claim)]

The JSON also records mentions of each DSS ID elsewhere in RESULTS_STATE and exact named cross-references found in its statement/locator; these are references only, not substantive manuscript judgments.

## Files

- `working/context_catalog.json`: exact source statements and metadata, including the structured state-entry index.
- `working/context_catalog.csv`: flat status/locator/ID reference index.
- `scripts/catalog_context.py`: reproducible extraction and coverage assertions.
