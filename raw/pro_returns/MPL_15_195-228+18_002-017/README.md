# MPL_15_195–228 + MPL_18_002–017

## Canonical deliverables

| File or directory | Contents |
| --- | --- |
| `MPL_15_195-228+18_002-017_transcription.tex` | Complete diplomatic LaTeX fragment, in the requested order; no preamble or document class. |
| `pages/` | The 49 individual page fragments, whose physical line numbers are used by the research notes and doubts table. |
| `MPL_15_195-228+18_002-017_doubts.md` | Shared notation table, 332 localized uncertainty entries, abbreviation expansions outside the transcription, and an account of legibility and limits. |
| `MPL_15_195-228+18_002-017_inventory.csv` | 705 element rows with the requested eight columns; every row is marked `transcribed=yes`. |
| `MPL_15_195-228+18_002-017_notes.md` | 119 research observations, the requested linear/non-linear table, historical and modern comparisons, two standing-question indexes, a scoped results-ledger assessment and 26 APA references. |
| `progress.log` | Actual UTC page-completion and audit records, freeze hashes, checkpoint events and final verification. |
| `records/` | Provenance, mechanical checks, research search records, expanded indexes and historical working scripts. |

The selection comprises **cote 15, scans 195–228 (34 pages)** and **cote 18, scans 2–7 and 9–17 (15 pages)**. The supplied blank scan 18/008 was omitted by the source package. No text or pagination has been reconstructed for it. The inventory identifies 24 text sheets, 20 reused typescripts, 4 covers and 1 cancelled draft; every reused or cancelled sheet is transcribed.

## Reading and freeze

One primary reader inspected all 147 supplied images, whole page first and then both halves, without OCR or delegated manuscript transcription. Each page was saved and inventoried before proceeding; all 49 pages received a second visual reading, followed by a package-wide notation audit. Research agents were used only after the freeze, for research, source checks and metadata review.

The transcription was frozen at **2026-11-15 13:53:15 UTC**. The context was first opened at **13:53:25 UTC**. The final verification confirms that all **50 frozen SHA-256 values**—49 individual pages and the combined fragment—remain unchanged. The combined transcription's SHA-256 is:

```text
4864c5a180ef69e8e49760c1977485eab5108242b09ab9d483971c860ec90e2d
```

Reading uncertainty remains explicit. The frozen transcription is not silently repaired by a later mathematical interpretation. Its page-state macros require definitions in a reader-supplied LaTeX wrapper; TikZ and `tikz-cd` source is included for drawings and diagrams. Braces and environments were mechanically checked, but **PDF compilation was not validated** because the available TeX installation lacked its format, class and required packages.

## How to use the indexes

A reference such as `15/203:L13–17` points to lines 13–17 of the individual file `pages/MPL_15_195-228+18_002-017_15_scan203.tex`, not to the combined transcription. CT and CN in the notes are defined there as the supplied context transcription and research notes. The supplied source archives, scans and context files are deliberately excluded from this ZIP.

Inventory rows follow page order and reviewed element position. Nested insertions, deletions and margins are placed beside their parent element; their identifiers remain stable labels and are not a second sequential reading order. The post-freeze inventory review changed metadata only. The upright reading orientation is used for the inverted reused sheet 18/016.

The observations distinguish conjectures, unproved assertions, implications, reading questions, author-marked checks, withdrawn proposals and the reader's own explicitly qualified ideas. Each has an independently executed context search and a status-qualified ledger connection. The notes do not treat the supplied first-pass returns as independently established results, or transfer a cancelled draft's status to a neighbouring live conjecture.

## Provenance and reproducibility limits

The files at the root and in `pages/` are authoritative. Material in `records/` preserves intermediate stages, including superseded first-pass wording, preliminary research reports and earlier inventory arrangements. Those records are retained so the work can be audited; they do not override the canonical deliverables.

In particular, historical `write_*`, finalization and integration scripts document past operations and **must not be rerun against the frozen transcription**. Read-only checks include `records/validate_structure.py`; the final reports are `records/final_structure_check.json` and `records/final_research_check.json`. Structural success does not certify the accuracy of every handwritten reading. The detailed method is in `records/READING_METHOD.md`.

The two hourly checkpoints were saved separately during work. This ZIP is the completed package, not a checkpoint or an extract.
