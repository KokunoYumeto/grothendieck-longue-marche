# MPL_136_002–046

## Canonical deliverables

| File | Contents |
|---|---|
| `MPL_136_002-046_transcription.tex` | One LaTeX fragment, without a preamble, containing the exact ordered bytes of all 44 individual page files. |
| `pages/` | One diplomatic fragment for each supplied scan 002–046, excluding the omitted blank 019. |
| `MPL_136_002-046_doubts.md` | Common notation table, chronological doubt register and audit additions, abbreviation expansions, and legibility limits. Later audit/reconciliation rows supersede earlier readings where explicitly stated. |
| `MPL_136_002-046_inventory.csv` | 902 inventory elements across all 44 pages; every row is marked `yes`. This records coverage checked by the reader, not an automated guarantee of reading accuracy. |
| `MPL_136_002-046_notes.md` | Complete English research report, including the planning answers, itemized notes, self-flagged steps, titles and pagination, and results-state reconciliation. |
| `progress.log` | UTC page-completion and audit records, notation reconciliation, freeze time, 45 SHA-256 values, context-opening time, checkpoints, and final unchanged-hash verification. |

The transcription was frozen at **2026-11-17 15:04:33 UTC** and the supplied context opened at **15:04:34 UTC**. The one reader personally viewed all whole pages and supplied halves, transcribed them in sequence, and gave every page a second visual audit; no OCR or parallel image reading was used. Context research was undertaken only after the freeze, and it did not change the page files or combined transcription.

## Supporting work records

`research/` contains the itemized source drafts used to assemble the canonical notes, the supplied-context search ledgers and their generators, an explicit mathematical appendix for the negative-Hom diagnostics, and an independent check of that appendix. These are supporting records; the complete organized report is the top-level `MPL_136_002-046_notes.md`.

`scripts/` contains the saving, auditing, concatenation/freezing, checkpoint, transfer and validation helpers used in the work. The attached scans, original context and prompt, and previous ZIP archives are not embedded in this return. The two hourly checkpoint receipts are retained as work records.

## Reading and verification limits

The fragments use the requested editorial macros plus standard mathematical LaTeX and TikZ/TikZ-cd. The reader's compilation environment must provide the editorial macro definitions and the corresponding ordinary math/TikZ packages; no preamble has been inserted into the requested combined fragment. A local compilation attempt could not start because the installed engines lacked LaTeX format files, so this return does not claim a successful compilation.

Structural validation checks page names and markers, balanced braces and environments, inventory coverage, literal concatenation, and the frozen hashes. It does not certify the handwriting or prove the mathematics. In particular, the 273 explicit doubt macros and the one physically illegible-word marker are part of the transcription, not placeholders to be silently filled from the context.

The report cites the earlier same-cote notes as first-pass leads and credits Michel Hua's project whenever its modernised interpretation or findings register is used. Research deductions, counterexamples, and repairs are labelled separately from the original manuscript; the explicit mathematical appendix is a work product of this return and is not represented as a formally machine-checked proof.
