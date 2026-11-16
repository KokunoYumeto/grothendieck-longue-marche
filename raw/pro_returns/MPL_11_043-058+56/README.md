# MPL_11_043-058+56

## Files to read

| File | Contents |
|---|---|
| **MPL_11_043-058+56_transcription.tex** | The complete frozen LaTeX fragment, in the requested scan order, without a preamble. |
| **pages/** | One frozen `.tex` file for each of the 50 scans. |
| **MPL_11_043-058+56_doubts.md** | Recurring-notation table, all uncertain/illegible readings with locators and confidence, abbreviation list, and legibility assessment. |
| **MPL_11_043-058+56_inventory.csv** | 809 element records, all marked `yes`, with the requested eight columns and page classifications. |
| **MPL_11_043-058+56_notes.md** | 104 research notes; answers to the two planning questions; author-flag and title/count sections; context comparisons; results-register ledger; primary bibliography. |
| **progress.log** | Initial time, sequential page completions, second audits, notation review, hashes, freeze, context opening, checkpoints, and final verification. |
| **records/** | Reading/audit/notation logs, frozen-hash and package manifests, compilation reports and logs, per-note context searches, extended research calculations, and final preflight. |
| **scripts/** | Page-recording/audit/checkpoint/validation scripts, uncertainty-table generation, freeze verification, context-search reproduction, and final archive assembly. |

## Coverage and ordering

The selection contains **15 scans from cote 11** (043–058, with 050 omitted) followed by **35 scans from cote 56** (002–039, with 010,019,034 omitted). These omissions are the blanks specified in the supplied prompt. The page classes are **22 text**, **24 reused typed/printed**, **2 covers**, and **2 cancelled drafts**; reused, cancelled, and printed material is included in full.

The combined fragment is the ordered concatenation of the 50 page files, with one separating newline after each file. It retains scan order even where the internal pagination of a reused typescript reveals a different reading sequence. The notes identify those sequences and record all title/count evidence; the complete 50-row foliation table is in `records/context_concordance_review.md`, §4.3.

## Reading method and freeze

One principal transcriber read the pages in sequence, using each whole-page image and its two supplied halves. Each completed page was saved before moving to the next page. The second visual audit again covered all 50 whole pages and 100 halves, followed by a cross-page notation review. No OCR was used on the supplied scans. Auxiliary work and post-freeze research were delegated; the transcription itself remained a single stream.

The transcription was frozen at **2026-11-16 14:05:25 UTC**. Context contents were opened at **14:05:37 UTC**. An earlier archive-metadata listing exposed context member names and sizes, but no context member contents; this procedural detail was recorded at the start of `progress.log`. No page file or combined transcription was edited after the freeze.

The combined fragment's SHA-256 is:

```text
bfc09da4334c339e9bd540cf85c3dbb5993c387f68ca5a45cb7256237c8770e2
```

`records/transcription_sha256.txt` and `records/transcription_freeze.json` identify all 51 frozen files. From this directory, the following read-only check verifies them:

```sh
python3 scripts/verify_frozen_transcription.py
```

The final uncertainty table groups **251 rows** covering **374 `\unsure` occurrences and 7 `\illegible` occurrences**. These are occurrence counts, not estimated error rates. Crowded cancellations, faint pencil additions, coefficient letters, and some quadric indices remain the least secure readings; the doubts file records their actual locations and alternatives.

## LaTeX conventions and compilation evidence

The transcription uses the requested source-state macros: `\cotefile`, `\scanpage`, `\mspage`, `\deleted`, `\inserted`, `\margin`, `\uline`, `\uuline`, `\diagram`, `\figure`, `\unsure`, and `\illegible`, together with ordinary mathematical LaTeX, TikZ, and `tikz-cd`. A `\figure` here is the requested one-argument source macro, not a standard floating environment. The first alternative in `\unsure{reading|alternative}` is the ink reading, with no mathematical correction implied.

All 50 page fragments and the combined fragment passed the recorded syntax-compilation checks. The original diagnostic harnesses live under `records/`; they contain historical workspace paths and intentionally simple source-state styling. Their grey deletions and suppressed underlines are diagnostic choices, not a final diplomatic page design. The transcription's macros retain the states independently of any wrapper's appearance. A few wide source displays overflow the provisional A4 diagnostic layout; no fixed-layout PDF is part of this deliverable.

## Research scope

The main notes keep source assertions, source questions, reading questions, and explicit calculations separately labelled. They give exact maps for the correspondence/category comparison, the integral quadric checks, the Delzant filtration, and the Weyl-group example. The context files' first-pass status and every relevant results-register status are preserved. The source's unfinished steps are never completed by changing its transcription.

The extended Weyl calculation has a standard-library reproduction command:

```sh
python3 records/weyl_subquotient_permutation_check.py
```

To reproduce the context queries, extract the user-supplied context archive outside this package, obtain the supplied Oda PDF's native text layer, and run:

```sh
python3 scripts/search_note_context.py /absolute/path/to/context /absolute/path/to/oda_native_text.txt
```

The exact queries and results already used are preserved in `records/context_searches.md` and `.json`. The supplementary `context_search_hits.json` records the earlier targeted concordance search. Query hits document the search; the main notes state the inspected relationship and its limits.

## Archive contents

This archive includes the requested deliverables and the records, logs, and scripts documenting the work. It excludes the supplied ZIPs, scan images, context source files, native-text copies of supplied PDFs, image crops, generated QA PDFs, and temporary TeX binary/build products. Earlier hourly checkpoint ZIPs are preserved separately and are not nested inside the final archive.

`records/package_manifest.sha256` records every included file except the manifest itself. The final assembly script checks the archive's CRCs, each manifested member, and all 51 frozen transcription hashes after writing the ZIP; the structural and final freeze-check reports are preserved under `records/`.
