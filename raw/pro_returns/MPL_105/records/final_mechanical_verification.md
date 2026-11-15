# Final mechanical verification

Verified: 2026-11-15 21:07:02 UTC.

**Result: PASS.** The existing package validator and comparison-coverage checker returned success with no reported errors or warnings. The checks did not modify the transcription, page fragments, notes, doubts, inventory or progress log.

## Package structure and frozen text

- **48 of 48** expected page files are present, covering scans 002–053 except 009, 024, 029 and 042.
- Page markers, completion entries and audit entries satisfy the existing validator.
- The combined transcription equals the exact ordered concatenation of the page fragments and has the required initial cote/scan markers.
- All **49 SHA-256 values**—48 page fragments and the combined transcription—match the frozen manifest.
- The required transcription, doubts, notes, inventory and progress deliverables are present; the required nonempty-file checks pass.

## Inventory

The CSV contains **1,180 rows**, covers **48 scans**, and has **1,180 unique element identifiers**. Every row has `transcribed=yes`. All column names, sheet-kind values and element-kind values satisfy the validator.

| Sheet kind | Rows |
|---|---:|
| `reused_typed` | 797 |
| `cancelled_draft` | 56 |
| `cover` | 3 |
| `text` | 324 |

| Element kind | Rows |
|---|---:|
| `text` | 525 |
| `margin note` | 78 |
| `diagram` | 112 |
| `deletion` | 225 |
| `display` | 116 |
| `insertion` | 119 |
| `drawing` | 5 |

## Comparison headings

All **267 expected comparison IDs** occur in exactly one correctly formed heading: **255 dossier IDs** and **12 NEW_RESULTS IDs**. Missing IDs: **0**; repeated expected IDs: **0**; unexpected comparison IDs: **0**; malformed comparison headings: **0**. Detection is restricted to the STRATA, PATHS, BISITE, RESIDUE and NEW_RESULTS prefixes. The complete structural results are in `comparison_coverage.json` and `comparison_coverage.md`.

## Intended ZIP membership

The read-only member selection, using `make_zip.excluded` and the ZIP script's symlink rule, selects **101 files**, including this report. **4 files** are excluded. Source-image, source-directory and archive candidates in the selected member set: **0**. No final ZIP was created by this verification.

## Limits

These checks establish file structure, identifier coverage, inventory value validity and preservation of the frozen bytes. They do not establish transcription accuracy, completeness of manuscript interpretation, correctness of the research comparisons, or visual agreement of diagrams with the scans. No manuscript image or context source was opened for this verification. Full TeX compilation was unavailable because the installed TeX engine lacks `pdflatex.fmt`; compilation was not repeated here.
