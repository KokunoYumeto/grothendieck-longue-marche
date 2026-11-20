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

After all first passes are committed, the independent audit uses the fixed `second/*_boxes.tsv` and `second/*_first.tsv`. A different reader receives only the images, coordinates and generic transcription conventions, creates its own crops and writes `second/*_second.tsv` before comparison. `compare_second.py` compares literal non-whitespace tokens, including LaTeX commands and punctuation. Thus a differing box may reflect syntax, scope or uncertainty rather than a change of ink reading; the root's adjudication distinguishes these cases. Every differing box is inspected. `D` in an audit progress line counts differing boxes; `K` counts boxes whose substantive transcription or expressed uncertainty changes.

`review/` and `reports/` preserve first-reader returns and the main reader's adjudication records. They are documentation, not a replacement for the consolidated files. The scripts reproduce assembly, cropping, comparison, static validation and ZIP packaging. Several scripts refer to the working directory and input-source folder used for this run; restoring a checkpoint elsewhere requires adapting those paths and supplying the original attachments.

## Completion record

`progress.log` records page completion, independent audits, checkpoint times, and final SHA-256 hashes. The transcription is final only after its freeze entry and the subsequent unchanged-hash verification. Checkpoints contain all deliverables and evidence written by their timestamp, never earlier checkpoint ZIPs or the original attachments.
