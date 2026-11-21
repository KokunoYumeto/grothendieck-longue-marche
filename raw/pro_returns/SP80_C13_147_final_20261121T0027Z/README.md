# SP80_C13_147 — consolidated diplomatic transcription

This package records a reading of the 23 supplied scans, numbered 108–117 and 119–131. Scan 118 was not supplied. The timestamped prompt `PROMPT(20261120-205306).md` governs the work; the other attached prompt versions were not combined into a new set of instructions.

## Files and conventions

`pages/` contains one LaTeX fragment per scan. `SP80_C13_147_transcription.tex` joins them in scan order, with a single `\cotefile{147}` header and no preamble. Use the supplied witness-C `PREAMBLE.tex` when incorporating these fragments elsewhere. The attached source scans, witnesses and preamble are deliberately excluded from this package.

The changes log records substantive locations against either witness. A location can count against both witnesses. Certainty-only changes are recorded in the doubt decisions, not counted as changes of text. Macro-only differences are not textual differences. H's editorial descriptions are distinguished from its attempted transcription of ink.

`decisions.tsv` preserves the order and identifiers of the supplied `MARKS.tsv`. Doubtful passages nested inside other macros that lacked a supplied identifier are still examined, transcribed and recorded in the doubts table; no fabricated mark identifiers are inserted in `decisions.tsv`.

The notation table is at the top of the doubts file. Suggested abbreviation expansions appear only in its editorial list. The notes distinguish assertions copied from the manuscript from checks actually performed. `CHECK_EVENTS.tsv` records the scope and type of each mathematical check or use.

## Reading and evidence

Each first reader received one page at a time, with that page's images, two witness texts, difference list, supplied marks, conventions, error sheet and the current shared notation table. The original was inspected once for layout, then its two native-resolution overlapping halves once each. Mandatory and unresolved passages were enlarged as saved crops. The main reader inspected each returned disputed or open place against its crop and committed the page before assigning the next page to the free reader.

The crops retain the original scan coordinate boxes in the change log and in `reports/*_crops.jsonl`. Enlargement and sharpening aid inspection; they do not add information. No OCR, text-recognition software, outside research, or TeX compilation is used.

After all 23 first passes were committed, three fresh image-only reader contexts were assigned the independent audit. The audit uses the fixed `second/*_boxes.tsv` and `second/*_first.tsv`. A different reader receives only the images, coordinates and generic transcription conventions, creates its own crops and writes `second/*_second.tsv` before comparison. `compare_second.py` compares literal non-whitespace tokens, including LaTeX commands and punctuation. Thus a differing box may reflect syntax, scope or uncertainty rather than a change of ink reading; the root's adjudication distinguishes these cases. Every differing box is inspected. A repaired first-pass difference-table parsing incident and the resulting additional blind-reader exclusions are documented in `review/difference_table_incident.md`. `D` in an audit progress line counts differing boxes; `K` counts boxes whose substantive transcription or expressed uncertainty changes.

`review/` and `reports/` preserve first-reader returns and the main reader's adjudication records. They are documentation, not a replacement for the consolidated files. The scripts reproduce assembly, cropping, comparison, static validation and ZIP packaging. The operational scripts resolve their paths relative to the package: restore this tree as `edition/` beside a `source/` directory containing the original attached scan/text folders and C/H difference list. The source attachments and native halves are not duplicated in the archive. Page-specific root review scripts are historical records; do not rerun them after a blind reading has been frozen.

## Completion record

`progress.log` records page completion, independent audits, checkpoint times, and final SHA-256 hashes. The transcription is final only after its freeze entry and the subsequent unchanged-hash verification. Checkpoints contain all deliverables and evidence written by their timestamp, never earlier checkpoint ZIPs or the original attachments.

The completed blind audit covers441 fixed boxes:352 token-different comparisons and80 changed box readings, including one correction where both readers agreed. All352 differences and that additional shared reading have individual root adjudications. These box counts include overlapping formulas and expressed uncertainty; they are not counts of independent witness errors. `review/final_accounting.md` reconciles the per-page totals and documents the extra110 context crop and two115 rotated viewing derivatives. `review/final_notation_check.md` records the final comparison of recurring forms across pages. `review/final_validation.json` contains the static final gate result; no TeX compilation was performed.
