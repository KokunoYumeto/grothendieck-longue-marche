# SP88_C13_149: work documentation

The attached prompt dated 2026-11-21 11:58:25 is the governing specification. The input ZIP was extracted once into `source/`; its scans and draft witnesses are excluded from this deliverable. No OCR, recognition library, PDF text layer, external research, or TeX compilation is used.

## First reading and adjudication

Three readers work concurrently, each on one assigned page, in the prescribed scan order. Each receives only the assigned full image, native overlapping halves, its C/H witnesses, filtered differences and marks, conventions/error sheet, and the current notation table. Native halves and packets are reproducible intermediates, excluded from the ZIP.

`review/149_scanNNN.tex` and `.json` hold each reader's return. `review/initial/` preserves the return before root changes. `review/accepted/` holds adjudicated metadata. The main reader visually inspects the full page and each returned disputed or unresolved crop. `root_reviewed` and the corresponding image list document this inspection. Accepted page files are written immediately; `assemble.py` rebuilds the common logs from those records.

All crop bounding boxes use original image coordinates. Enlargements and rotations do not change that coordinate system. Crops are made using Pillow and visually inspected. Short contextual crops may include fragments belonging to another line; such fragments are not independently completed.

## Independent second reading

Only after every first reading is accepted does `prepare_second.py` freeze the box lists and first readings. A reader who has not first-read that page receives only its image and box list, plus the transcription conventions. The reader writes `_second.tsv` without access to the first reading or either witness. `freeze_second.py` seals that completed reading and its inspection observations with SHA-256 before any comparison. `compare_second.py` verifies those seals, compares token streams and saves every difference. The main reader adjudicates each difference on the saved independent crop and records both frozen readings and the outcome. Changed places are additionally recorded in the changes log. `finish_second.py` checks completeness and records the audit counts and UTC completion time.

`FIRST_READINGS_SHA256.json` records the frozen first-reading files. The final transcription is frozen separately, after every audit and notation review, by logging SHA-256 hashes of all page fragments and the combined fragment. No PDF is compiled.

For audit counts, B is the number of boxes, D the number of boxes with at least one non-layout token difference, and K the number of boxes whose first reading changes after visual adjudication. Every differing token span is retained in the comparison JSON, including differences of uncertainty or editorial wrappers; these are not automatically counted as witness errors.

## Counts and mathematical notes

One logged place may differ from both witnesses. Macro-only differences and changes of certainty alone are excluded from witness-error counts. A change to the order of unchanged alternatives is also a certainty/preference update, not an error count. Baseline counts include main text, displays, readable deletions, margins, insertions, and standalone numbers; corrections on the same baseline do not add lines.

Mathematical notes distinguish the manuscript's claims from checks actually made. Merely transcribing a statement is not a check event. The runtime identifies the model as GPT-6 Astra Pro but does not expose a numeric/named reasoning-effort setting; the check log reports this limitation explicitly.

## Archives

`archive.py` packages every current deliverable and work document, including all crops, second readings, scripts and progress records, but excluding input scans/texts, native halves, prior ZIPs and Python caches. Its checkpoint mode enforces a minimum 45-minute interval and a new sequential filename. The archive includes a manifest with file hashes. Persistent-upload receipts are recorded without signed transfer URLs. The only final deliverable offered is `SP88_C13_149.zip`.
