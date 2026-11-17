# MPL_12_099–149

This archive contains the completed diplomatic transcription and separate research apparatus for the **36 retained scans** of cote 12 in the supplied selection.

## Main deliverables

| File | Contents |
|---|---|
| `MPL_12_099-149_transcription.tex` | One LaTeX fragment, with no preamble, concatenating the 36 page files in the required order. |
| `pages/` | One diplomatic LaTeX fragment for each retained scan. |
| `MPL_12_099-149_doubts.md` | Recurring-notation table first; English reading doubts, abbreviation expansions, and a legibility assessment. |
| `MPL_12_099-149_inventory.csv` | 911 element records, all marked `yes`, including sheet-kind classifications. |
| `MPL_12_099-149_notes.md` | 99 individually identified research notes; the four-pair comparison table; evidence-qualified answers to the context questions; manuscript-explicit reservations; title-sheet/count section; APA references. |
| `progress.log` | Page completion, second audits, the pre-context freeze and 37 SHA-256 digests, context-opening time, checkpoint records, and final hash verification. |

## Reading and evidence boundaries

The primary reader worked in one ordered transcription stream, using the supplied whole-page images and their halves; OCR was not used on the manuscript. Every retained page received a second visual audit before the transcription was frozen, and the recurring notation was compared before context was opened. Research helpers were used only after the freeze; their source comparisons and mathematical checks did not alter the frozen reading.

The selected order is:

`99, 101, 104, 105, 106, 107, 108, 109, 111, 112, 113, 114, 115, 116, 118, 119, 120, 122, 125, 127, 129, 131, 133, 135, 137, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149`.

The inclusive numerical range has 51 scans; three omitted blank scans and twelve previously assigned scans leave these 36 retained faces. The inventory classifies 30 as `text`, three as `cover`, and three as `reused_typed`; printed and legible typed material on retained faces is included. The only retained handwritten page marker is `1` on scan 099; archive foliation is confined to TeX comments, and no retained cover states a total extent.

## Research records

`records/` preserves the working research reports, the complete register of explicit doubts and revised proof steps, independent checks of the local/global elliptic examples and the double blowup, source-verification records, and assembly manifests. `records/research_searches/` contains a separate query and complete match-locator list for every main research-note ID; substantive matches and negative findings are distinguished in the notes and manifests. The earlier research returns and Hua's modernization remain contextual leads, and internal “Proved” statuses are never promoted merely by citation.

The supplied scans, context files, and source PDFs are not included, since they remain the task inputs. The scripts and records document the work; temporary extracted text, image crops, caches, and attached archives are also excluded.

## Technical validation

The structural validator checks page markers, inventory schema, exact concatenation, brace and doubt-argument balance, event ordering, and agreement with the frozen SHA-256 values. The final builder additionally checks the archived bytes and ZIP CRCs, and places its report at `records/final_structure_check.json` inside the archive. These checks do not replace the visual reading or prove mathematical claims.

No successful TeX-to-PDF compilation is claimed: the available TeX executables lack the required document class and AMS/TikZ packages, as documented in `scripts/TEX_SYNTAX_CHECK.md`. The transcription is intentionally a fragment using the editorial macros specified by the user; a consuming document must define those macros and load its typesetting dependencies.

## Reproduction and preservation

Research notes can be assembled by `scripts/assemble_notes.py`; it writes only research outputs. `scripts/search_context.py` expects the supplied context at the workspace-relative location recorded in that script. **Do not rerun** the page-writing, reading-finalization, or freeze scripts on this completed package: the transcription has already been frozen, and any later proposed reading belongs in a new research note.

Two numbered hourly checkpoints were created without overwriting their predecessors; their persistence receipts are recorded in the work record. The final ZIP is the sole requested delivery. A local file listing or a link alone is not taken as evidence of persistence; successful upload receipts are recorded separately.
