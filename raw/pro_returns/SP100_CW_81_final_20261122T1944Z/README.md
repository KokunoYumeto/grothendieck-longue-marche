# SP100_CW_81 — consolidated diplomatic transcription

## Scope and evidence

This return concerns Montpellier cote 81, archive PDF scans 43–55. The page numbering of witness H is one lower than the archive PDF scan number. The supplied current `PROMPT(20261122-171353).md` governs the work; the other three prompt versions are historical materials. Only the present thirteen scans are transcribed.

The images are the primary source. C (the supplied Codex transcription), H (the Commutator project transcription, commit `aef7db2`), and the relevant S correction (`SA01-K81-03`) are witnesses to be checked. A witness agreement is not independent evidence for a reading. This return does not assert human verification.

## Completion

All thirteen pages completed the first reading, root adjudication, blind second reading, and root crop audit. The final transcription was frozen at **2026-11-22 19:39:13 UTC**; the individual page and combined-file SHA-256 values are recorded in `progress.log` and `records/transcription_frozen_sha256.json`.

| Measure | Final count |
| --- | ---: |
| Scan pages | 13 |
| Blind-reading boxes | 225 |
| Boxes with unequal input token sequences | 186 |
| Boxes changed by final adjudication | 44 |
| Distinct logged correction places | 469 |
| Places changed against C | 143 |
| Places changed against H | 437 |
| Correction places: high / medium / low confidence | 328 / 66 / 75 |
| Inventory elements | 287 |
| Remaining doubt entries | 168 |
| Recorded mathematical check events | 27 |

The 168 doubt entries comprise 165 in-text doubt marks and three graphical or attribution qualifications on scan 55. No passage is left under an illegibility macro. The counts against C and H overlap and must not be added as distinct places. Blind boxes can also overlap; their disagreement and change counts are audit units, not manuscript error-rate estimates.

`validation.json` reports no remaining structural errors. Its initial findings and the metadata/validator corrections are preserved separately in `records/`: twenty scan 51 crop paths needed an archive-relative prefix correction, and a row-break spacing option was initially mistaken for a display opener. These corrections changed no transcription reading.

## Contents

- `pages/` contains root-adjudicated page fragments; `SP100_CW_81_transcription.tex` concatenates them in scan order, with one opening cote marker.
- The changes log records decisions against either witness, including crop coordinates and visible strokes. The TSV collation selects differences against H; scan 55 has no H collation rows because H provides only a description.
- The doubts file starts with the checked notation table, followed by unresolved readings and abbreviations. The inventory enumerates page elements. Notes distinguish what the manuscript says from any mathematical checks actually performed.
- `crops/` contains generated visual evidence crops. Coordinates always refer to the supplied full-page JPEG, before enhancement or rotation.
- `second/` contains box lists, first readings fixed before blind rereading, independent second readings, token comparisons, and adjudication records.
- `records/` retains generated reader and root decision records and the generated `READER_PROTOCOL.md`. `scripts/` contains assembly and verification utilities; they perform no text recognition.
- `progress.log` records actual UTC work events, completion and audit counts, and the frozen transcription hashes. `CHECK_EVENTS.tsv` identifies the precise scope of mathematical checks.

Audit counts use boxes as their unit: B is boxes read; D is boxes with unequal comparison token sequences, including markup or included-context differences; K is boxes whose final reading changed, including changes of uncertainty. Boxes may overlap. D and K are separate from token-edit blocks and from the distinct C/H correction places counted in the changes log.

No OCR, outside research, or TeX compilation is used. Structural validation is limited to delimiters, environments, file coverage, apparatus consistency, and hashes. The LaTeX fragments use the preamble supplied with the source materials; that unchanged source preamble is not duplicated here.

## Lossless packaging and crop hashes

The final ZIP preserves every generated deliverable and evidence crop. To fit the upload size limit, the PNGs are losslessly recompressed: only their compressed IDAT encoding changes. Their dimensions, color modes, pixel bytes, filtered image data, and all other PNG chunks remain identical. No crop is resized or regenerated.

Historical reader records retain the SHA-256 of each original PNG encoding. `PACKAGING_LOSSLESS_MANIFEST.json` maps `original_sha256` to `packaged_sha256` for every archive member and records the common decoded-pixel and filtered-data hashes for the crops. `PACKAGING_LOSSLESS_RECEIPT.json` explains and records the transformation. All original non-PNG files, including frozen readings and transcription files, are packaged byte for byte. The implementation and its documentation are in `scripts/package_lossless.py` and `scripts/LOSSLESS_PACKAGING.md`.

Checkpoint 03 required the same lossless compression after its initial size rejection. Its original archive was retained unchanged; the retry preserves its complete 844-member snapshot. The initial failure, successful save, member mapping, and compression experiments are documented in `records/` and `scripts/packaging_history/`. No earlier checkpoint ZIP is included in this return.

## Source references

Grothendieck, A. (n.d.). *Immersions du disque et de la circonférence: Notes manuscrites* [Archive catalogue title; cote 81, scans 43–55]. Fonds Grothendieck, Université de Montpellier. https://grothendieck.umontpellier.fr/81.pdf

Commutator project. (n.d.). *Grothendieck project: Cote 81 transcription* [AI transcription; supplied snapshot at commit aef7db2]. https://github.com/Commutator-IO/grothendieck-project

The catalogue title above is supplied metadata. The present leaves concern segments and partitions of a bicircular set and the attachment of maps along edges. Source URLs are recorded as supplied; no external source was retrieved in this run. Source integrity identifiers are in `SOURCE_MANIFEST.tsv`.
