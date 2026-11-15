# MPL_154_127-176

Diplomatic transcription and separate research notes for Alexander Grothendieck's manuscript notes, Montpellier archive, cote 154, **scans 127–176 inclusive: 50 selected scans**.

## Deliverables

| File or folder | Contents |
|---|---|
| `MPL_154_127-176_transcription.tex` | All fifty page fragments in scan order, with no preamble or document class. |
| `pages/` | One authoritative frozen TeX fragment per scan. |
| `MPL_154_127-176_doubts.md` | Notation table, proposed abbreviation expansions, legibility assessment, and every uncertainty occurrence with location and confidence. |
| `MPL_154_127-176_inventory.csv` | 636 recorded elements across all fifty scans; every row marked `yes`. |
| `MPL_154_127-176_notes.md` | 75 English research notes, contextual comparisons, standing sections on unverified steps and documentary evidence, conditional calculations, and APA references. |
| `progress.log` | Actual UTC completion and audit events, checkpoint records, freeze hashes, and final integrity verification. |
| `records/` | Reading and audit records, exact-hash compilation coverage, search ledgers, research working memos, and review reports. |
| `scripts/` | Work and validation scripts retained for provenance and recovery. |

The source scans and supplied context archive are not included. The work records refer to those original inputs by their supplied names. Historical candidate memos are retained as records; the selected and reviewed research deliverable is `MPL_154_127-176_notes.md`.

## Freeze and separation of evidence

The root reader personally read every whole page and both halves in scan order, completed each page and inventory before moving on, and conducted a second visual audit of all fifty pages. No OCR was used on the manuscript images. Research collaborators worked only from the frozen text and the subsequently opened context; they did not read manuscript images or alter the transcription.

The transcription was frozen at **2026-11-15 01:44:43 UTC**. The context was opened at **2026-11-15 01:44:50 UTC**. `records/frozen_hashes.sha256` records the fifty page files and the combined fragment, and the same hashes are recorded in `progress.log`. The final validation and progress-log entry report the comparison with those frozen values.

Contextual expectations, conditional mathematical calculations and later literature have not been used to rewrite the frozen readings. The notes distinguish explicit manuscript questions, declarative claims, cancelled trials, editorial reading questions and our proposed comparisons. Earlier research-return statuses remain claims at the review level recorded in the supplied context.

## Locators and uncertainty

Scan numbers always refer to the supplied PDF page numbering. The recorded marginal numbers are 126–175, one less than the corresponding scan number; their presence does not establish who added the pagination or the complete work's extent. Approximate line locators in the doubts and notes refer to the corresponding TeX source file, including drawing-code lines where relevant.

The doubts register has **687 uncertainty occurrences: 657 `\unsure` and 30 `\illegible`**. These are occurrences, not distinct words: repetitions are retained, and an illegible-word count is an estimate. Confidence labels are 427 medium and 260 low; no explicitly uncertain occurrence is rated high. The legibility section identifies the weakest prose, printing and overdrawn labels, and explains the limits of the manually estimated TikZ geometry.

## TeX use and verification

The transcription is deliberately a fragment. Typeset it within a host document that loads the necessary mathematics, TikZ and TikZ-CD packages and defines the requested diplomatic macros; `\figure{...}` is the editorial drawing macro, not the ordinary LaTeX float environment. Deletions, insertions, marginalia, underlining and uncertainty must be represented by the host's chosen editorial styles.

All fifty final page hashes have successful **pdfLaTeX and XeLaTeX syntax-processing checks**, recorded in `records/post_audit_compile_coverage.csv`. The harness in `scripts/compile_fragments.py` compiles copies in temporary storage with shell escape disabled; its simplified macro definitions serve syntax testing and do not constitute a visually verified reading edition. These tests do not certify image fidelity, drawing topology, page layout or correctness of a reading.

For structural and frozen-hash verification, from the extracted package directory run:

```bash
python3 scripts/validate_package.py --root . --complete
```

The combined fragment is assembled by joining the authoritative page-file bytes in numerical order with one additional newline between fragments. No images are embedded or substituted for textual or graphical transcription.

## Historical scripts

The page generators, commit scripts, audit corrections and freeze script document the work that produced the frozen edition. **Do not rerun them against this finished package:** some contain earlier readings and some append completion or inventory records. The page files and their freeze manifest are authoritative. `scripts/assemble_research_notes.py` handles only research-note selection and presentation; it does not read or write the frozen transcription.

Some older reports record intermediate failures or pending checks. Their timestamps and hashes identify the state they examined; the complete visual-audit record, final exact-hash coverage and final validation supersede those intermediate states without deleting the history.
