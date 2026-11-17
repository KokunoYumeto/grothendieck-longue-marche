# MPL_31_002-051

Diplomatic transcription and research dossier for the 46 retained scans of Montpellier archive file 31.pdf, scans 002–051. The supplied omissions are 034, 040, 041 and 046.

## Contents

| Path | Contents |
|---|---|
| MPL_31_002-051_transcription.tex | Combined LaTeX fragment, in scan order, with the requested documentary-state and doubt macros. |
| pages/ | One frozen LaTeX fragment for each of the 46 retained scans. |
| MPL_31_002-051_doubts.md | Notation table first, then 449 occurrence-specific doubt entries, abbreviation interpretations, and the legibility account. |
| MPL_31_002-051_inventory.csv | 1,177 page-element records in the requested eight-column format; every row is marked yes. |
| MPL_31_002-051_notes.md | 94 substantive research items and seven title/count items; the author's verification flags; title and pagination inventories; context comparisons; primary references; and the disposition of all 26 selected register entries. |
| progress.log | Sequential completion records, second-reading records, freeze hashes, context-opening time, hourly checkpoints, and final integrity checks. |
| records/ | Reading and notation audits, the 47 frozen SHA-256 digests, per-item search evidence, structured research data, source records, and mechanical validation reports. |
| scripts/ | The working and validation scripts, with their roles described in scripts/README.md. |

## Reading the dossier

The primary reader examined every whole-page image and both supplied halves in one sequence, then completed a second visual audit of all 46 scans. No manuscript OCR was used. The transcription was frozen at **2026-11-16 23:40:30 UTC**; the context archive was opened at **23:40:37 UTC**. The final verification compares every page and the combined fragment with those 47 recorded hashes.

Approximate line locators in the doubts and research notes refer to the individual LaTeX fragments. The doubt register records proposed visual readings and their confidence. Its concluding legibility account identifies the least secure passages; unmarked text remains the reader's best direct reading.

Every numbered research item has an executed context search. The available context consists of README.md and notes/RESULTS_STATE.md, including truncated excerpts of earlier work. The research notes preserve those limits and attribute each recorded status to its source. The own-idea items supply confidence and reasons alongside their questions and concrete calculations.

## LaTeX and verification

The transcription files are fragments with no preamble. A host document must supply the requested documentary-state macros and the standard mathematics, TikZ and tikz-cd facilities used in the fragments. The temporary wrapper in scripts/check_fragments.py records a successful syntax compilation of all 46 page files; its pass-through macro definitions are for that check.

records/final_validation.json contains the final package checks. records/package_manifest.json gives the byte length and SHA-256 of every packaged file except the manifest itself. Mechanical checks address file structure, recorded coverage and integrity; the reading judgments and limitations are documented in the visual audit and doubts files.

Historical first-pass records and writing scripts are retained as work records. The final fragments and second-audit records carry the completed readings. Supplied source archives, scan images and original context files are omitted from this ZIP as requested.
