# Montpellier transcription package

**MPL_33_147-181+34_002-017**

## Deliverables

| File or folder | Contents |
|---|---|
| `MPL_33_147-181+34_002-017_transcription.tex` | Complete diplomatic LaTeX fragment, without a preamble, in the supplied scan order |
| `pages/` | One frozen LaTeX file for each of the 49 retained scan pages |
| `MPL_33_147-181+34_002-017_doubts.md` | 34-entry notation table, 406 doubt entries, 80 abbreviation entries, and an account of legibility and the least secure readings |
| `MPL_33_147-181+34_002-017_inventory.csv` | 951 inventoried elements; every row marked `transcribed=yes` |
| `MPL_33_147-181+34_002-017_notes.md` | 100 English research notes, context comparisons, authorial verification/deferment inventory, withdrawals and corrections, title/pagination catalogue, complete results-register disposition, and checked primary references |
| `progress.log` | Page completion and second-audit timestamps, frozen SHA-256 values, freeze/context boundary, hourly checkpoint records and final verification |
| `records/` | Reading, notation and audit records; historical save/audit scripts; actual context searches; working research memos; final research QA; compilation validation and final package validation |

## Coverage and evidence boundary

The package contains **34 pages of cote 33**, scans 147–181 excluding the supplied omission of blank scan 169, followed by **15 pages of cote 34**, scans 003–017; blank scan 002 was omitted from the input. The original scan and context archives, extracted scan images, reading crops, supplied context files and diagnostic PDFs are excluded from this ZIP. Their absence from the ZIP is intentional; the deliverables and work records are included.

The transcription was performed in one stream by the primary reader, using every whole-page image followed by its two supplied halves, without OCR or transcription delegation. A second visual reading of all 49 pages and the cross-page notation audit preceded the freeze at **2026-11-16 00:02:21 UTC**. The context archive was opened at **00:02:28 UTC**, after the freeze. Subsequent research used the frozen text; no post-context reading suggestion was incorporated into it. Research comparisons and independent research QA were delegated only after this boundary.

`records/frozen_sha256.txt` contains the SHA-256 values of the 49 page files and combined transcription. `records/final_validation.json` records the final comparison against all 50 values; `progress.log` also states the outcome. The notation table and doubts are integral to the transcription: an unmarked reading is not a guarantee of certainty, and the 406-entry doubt register includes nested and containing doubts. Mathematical incompleteness and apparent contradictions have been preserved as source features.

## Reading and compiling the LaTeX

The transcription is a fragment intended for a LaTeX document that defines the requested diplomatic macros and loads standard mathematical and TikZ/`tikz-cd` support. Page and archive boundaries are explicit in `\scanpage` and `\cotefile`; manuscript/source numbering, insertions, cancellations, marginalia and uncertain readings remain encoded separately. Per-page TeX line numbers are used in the doubts and research notes.

`records/compile_check.tex` is a **syntax-validation wrapper**. Its large diagnostic page size and neutral definitions of deletion, insertion and doubt macros were used to test compilation; it is not a typeset diplomatic reading edition. The retained validation log records a successful compilation. No diagnostic PDF is offered as a substitute for the source fragment.

## Research apparatus and reproducibility

The final research notes contain **D01–D40**, **M01–M28**, **R01–R28** and **I01–I04**. Each numbered item has one to four prose sentences, with source and context metadata separate. Own deductions carry their stated confidence and interpretation limits. Earlier supplied notes remain first-pass leads, and returned/intake/planning statuses are retained rather than upgraded. The dedicated register table accounts for all **44 returned-package leads** and **7 other substantive entries**.

Actual search queries, hits and no-hit results are retained in the records named by section 9 of the final notes. Earlier working memos are kept as provenance; the final notes supersede their draft wording and counts. The primary-source table states precisely which passages were checked and which broader collations remain open.

The save, audit and pre-freeze revision scripts are historical records, not instructions to rewrite the frozen files. `records/assemble_final_notes.py` reproduces the final research-note assembly from the retained research memos; `records/finalize_package.py` checks the deliverables and frozen hashes before preparing the ZIP. Neither script changes a frozen transcription file.
