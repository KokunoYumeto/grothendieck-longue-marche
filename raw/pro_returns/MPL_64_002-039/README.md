# MPL_64_002–039

Complete diplomatic transcription of cote64 PDF scans002–039, with research notes and an audit trail.

## Main deliverables

- MPL_64_002-039_transcription.tex: all38 pages, one LaTeX fragment without a preamble.
- pages/: one fragment per scan, in the same frozen reading.
- MPL_64_002-039_doubts.md: notation table,333 current unsure occurrences,four illegible spans,abbreviations and legibility assessment.
- MPL_64_002-039_inventory.csv:761 inventoried elements,all marked transcribed=yes.
- MPL_64_002-039_notes.md:63 research/apparatus items,with contextual comparisons,exact finite checks,self-flagged steps,title/pagination evidence and references.
- CHECK_EVENTS.tsv: event-level statement provenance and verification scope.
- progress.log: page completions,audits,freeze hashes and final integrity assertion.

## Evidence and supplementary research

records/ contains the visual-workflow records,freeze manifest,read-only validator,LaTeX syntax harness,research search logs,proof reports,finite computation scripts/results,and a checked30-node S4 subgroup-inclusion SVG with its generator key and CSV data. The supplied scans and contextual source archive are not redistributed.

The 38 page files and combined transcription were frozen before context access. Mathematical corrections and different contextual readings appear only in the notes. A successful syntax check is not a claim that every handwriting doubt has disappeared.

## Reproducible read-only structural check

From this directory:

    python3 records/validate_package.py --require-frozen --json

The finite mathematics can separately be reproduced with the three certificate scripts identified in the notes. They do not inspect images. Historical transcription-editing scripts are retained as process documentation; the delivered frozen files and hash manifest define the final transcription.
