# Packaging preflight

Checked 2026-11-20 21:59:28 UTC. **PASS: no packaging omissions or missing evidence files found at this snapshot.** This was a read-only structural preflight apart from creating this report; no images were opened, no transcription or generated output was edited, no progress entry was changed, and no TeX compilation or metadata/doubts reassessment was performed.

## Required contents

| Check | Actual result |
| --- | --- |
| Page files and order | 24 nonempty page files; exact supplied witness-C filename set; `page_order.txt` has all 24 once in source-filename order. |
| Combined transcription | Byte-for-byte text equality with the 24 page fragments in `page_order.txt` order, with the two expected cote wrappers and the documented separator convention. |
| Named root outputs | All 11 required root files exist and are nonempty. |
| Mark decisions | 72 rows; IDs match all 72 source `MARKS.tsv` rows in their original order. |
| Independent-reading evidence | 24 each of box lists, first readings, second readings, comparisons, adjudication tables, crop manifests, and image-only notes. |
| Audit row coverage | 332 boxes; first/second/comparison/manifest IDs match box IDs in order; adjudication IDs match the nonidentical-token comparison boxes. No duplicate IDs. |
| Crop references | All 555 distinct concrete crop filenames found in text records resolve; all 332 expected second crops exist. All 642 saved crop PNGs are included by the package rule. |

The 11 required root files are:

- `SP76_C13_145+147_transcription.tex`
- `SP76_C13_145+147_changes.md`
- `SP76_C13_145+147_collation.tsv`
- `decisions.tsv`
- `SP76_C13_145+147_doubts.md`
- `SP76_C13_145+147_inventory.csv`
- `SP76_C13_145+147_notes.md`
- `CHECK_EVENTS.tsv`
- `progress.log`
- `SP76_C13_145+147_sheet_feedback.md`
- `SP76_C13_145+147_hand_log.md`

## Exclusions

The raster-file sweep found only 642 PNGs, all directly under `crops/`; there are no JPEG original scans, image files outside `crops/`, named half images, or ZIPs in `work/`. No source-witness directory, `hua_` file, `PREAMBLE.tex`, `MARKS.tsv`, or attached differences table is included. Exact-content SHA-256 comparison of packaged TeX files against the source TeX files found no copied source witness or preamble. No symlinks or empty files were found. A generic `crops/...png` example in the protocol is a placeholder, not a broken evidence reference.

## Checkpoint preservation

The proposed member set uses the current `scripts/package.py` rule: every work file except ZIPs, `.pyc`, and `__pycache__` content. It contains 952 files including this report at the checked snapshot. The ZIP central directories were read without extracting or opening their images.

| Existing checkpoint | File members | Members absent from proposed package |
| --- | ---: | ---: |
| `SP76_C13_145+147_checkpoint_01.zip` | 227 | 0 |
| `SP76_C13_145+147_checkpoint_02.zip` | 405 | 0 |
| `SP76_C13_145+147_checkpoint_03.zip` | 641 | 0 |
| `SP76_C13_145+147_checkpoint_04.zip` | 807 | 0 |

**Documents that would be omitted: none.** Every member of every existing checkpoint is present in the proposed current package. This checks member preservation, not unchanged contents of evolving logs or historical archives. The final ZIP has not been built by this preflight; root can package after completing freeze and final verification.
