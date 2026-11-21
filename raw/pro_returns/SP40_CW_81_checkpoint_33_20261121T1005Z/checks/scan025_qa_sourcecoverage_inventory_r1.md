# Scan025 independent source coverage inventory

Source-only inventory; no source file was changed. All identities use their original file plus JSON pointer. Own-reader readings, witness C/H fields and any later selected fields retain their separate roles.

| Reader | Differences | Doubts | Inventory | Groups | Text spans | Literal drawing commands |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| A | 21 | 14 | 29 | 21 | 19 | 143 |
| B | 28 | 15 | 32 | 18 | 6 | 149 |
| C | 28 | 18 | 31 | 21 | 4 | 151 |

The source packet has 8 actual C doubt rows, 8 separately scoped notation/slip rows, and 13 inventory rows.

Recorded 369 original row references, 60 complete group references, 29 text-span references, 443 literal drawing-command references, and 816 original qualification/hand/scope metadata fields.

Source checks: 477; failed checks: 0.

## Concrete findings

No source-reference or literal-offset defect remains after the bounded checker correction. B report source offsets use its declared UTF-8 convention. Inline and nested group markers are covered by their original source offsets; map array order is separately preserved. The initial QA snapshot and exact old/new checker changes are retained.

## Required preservation points

- Keep original C rows R01–R08 at their actual scope. A local_decisions and C local_parts remain attached to their original row identities.
- Keep A inventory scope_note, B inventory local_hand_scopes, and C inventory compound hand values. Complete group metadata and candidate-specific hand scopes remain at their original source pointers.
- Keep each complete graphical group, every node/word command, every drawing command, and adjoining text at the original source offset. Group and text-span boundaries are recorded literally.
- Preserve source-silent own-reader material from complete TeX. C’s live et candidate remains in reader C’s source role; B’s que-plus-point group remains in reader B’s source role.
- H marker catalog contains no uncertainty macro; supplied letters and the two note objects retain their local source spans. All later local marked_in_H choices belong to root review.
- S_scope records seven source rows and an empty direct_page_25_reading_rows array; its exact scope statement is bound as original source metadata.

Stage1 source-pool/projection replay remains pending source025 handoff.
