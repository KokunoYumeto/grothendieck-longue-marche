# SP31 — cote 156-3, scans 002–025

This package contains the diplomatic transcription of all 24 supplied scans, manuscript pages 1–24, with the two-witness collation, image-reading evidence, complete inventory, remaining doubts and post-freeze research notes.

## Main deliverables

| File or directory | Contents |
|---|---|
| `pages/` | One TeX fragment per scan, with the original witness-C filenames. |
| `SP31_CW_156-3_transcription.tex` | Exact byte concatenation of the 24 page files, in scan order, without a preamble. |
| `SP31_CW_156-3_changes.md` | Per-page C/H/final readings, crop evidence and confidence; counts; consequential corrections; all 517 source-C doubt dispositions and all eight S-row decisions. |
| `SP31_CW_156-3_collation.tsv` | The 259 localized differences from witness H, with the requested schema and categories. |
| `SP31_CW_156-3_doubts.md` | Notation table first, all remaining marked doubts, abbreviation interpretations and legibility assessment. |
| `SP31_CW_156-3_inventory.csv` | 563 entries covering text, formulas, drawings, margins, insertions and deletions; every entry marked transcribed. |
| `SP31_CW_156-3_notes.md` | 65 research items covering every page; context comparisons, checked proofs and counterexamples, the two standing questions, and the audit of all 50 original C-note items plus eight additions. |
| `CHECK_EVENTS.tsv` | Actual proof, documentary, background and refutation events, with their scope and authors. |
| `progress.log` | UTC start, page completion and audit records, freeze hashes, context-opening marker, scheduled checkpoints and final unchanged-hash confirmation. |
| `SP31_CW_156-3_manifest.tsv` | Byte lengths and SHA-256 hashes of all package files except this self-excluded manifest. |

## Evidence and reproducibility

`crops/` contains the derived image enlargements used in the reading; the full input scans, witnesses and context packets are not duplicated. `records/` holds the root's page-by-page decisions and notation records. `audit/` holds the source-C occurrence audit, mapping of all 107 mechanical non-doubt differences to decisions, structural and inventory evidence, and review reports. The two additional inventory TSVs expose display coverage and the top-to-bottom anchoring checks.

`research/` contains the supporting context memo, searches for every note, the detailed mathematical checks, the join proof and moderate-difference counterexample, and the documentary C-note audit. The main notes contain the complete user-facing apparatus; these supporting files supply fuller arguments and the check trail.

`scripts/` preserves the authoring, audit, validation and packaging code. They use the original workspace arrangement (`out/` beside `source/`) and the separately supplied input packets. The earlier page-authoring scripts document the work and must not be run over the frozen files. `PREAMBLE.tex` is the supplied macro reference; it is not inserted into the combined fragment. No OCR or TeX compilation was used.

## Freeze and scope

Root read every whole image and both halves in sequence, checked the crops, and performed a second sequential image audit. The 24 page files and their concatenation were frozen at **2026-11-19 21:46:48 UTC**, before research context was opened. Later mathematical corrections and interpretations are confined to the research notes. The final structural report is `validation.txt`, with machine-readable details in `validation.json`; historical reports retain their dates and earlier scope.

The two written dates are **(8 Juin 86)** on scan 002 and **(9 juin)** on scan 022. The latter does not itself state a year. The sheets carry consecutive manuscript numbers 1–24, but no authored statement of a total page count. Remaining ink uncertainty is preserved explicitly rather than settled by the mathematics or by witness agreement.

The immutable checkpoint archives are not nested in this final ZIP. Their current deliverable and documentation filenames are all retained here; the final packaging check verifies that coverage.
