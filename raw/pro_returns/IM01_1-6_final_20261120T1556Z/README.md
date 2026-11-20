# IM01_1-6 diplomatic transcription audit

The authoritative row decisions are in `placements.tsv`, in the order of the supplied corrections table. The final page texts are in `edited_pages/`. The original attachments remain the source for scans, unedited pages, the correction table and `PREAMBLE.tex`; those inputs are intentionally omitted from this package.

## Contents and conventions

| Path | Purpose |
| --- | --- |
| `placements.tsv` | One decision per supplied row, with exact original and replacement spans for decision (a), visible-ink accounts, crop references and confidence. |
| `edited_pages/` | Complete pages, including pages whose decisions require no change. |
| `notes.md` | Author slips, mathematical refinements, off-page or catalogue matters, and explicit doubts. Precise table proposals are retained with attribution. |
| `crops/` | Visually inspected crops from the supplied scans, enlarged and contrast-enhanced; no OCR was used. |
| `CHECK_EVENTS.tsv` | Actual visual checks, main-reader reviews and explicitly attributed background uses. These are not mathematical proof certificates. |
| `progress.log` | UTC start time followed by page completion records. A page is logged only after its text and placements are written. |
| `reviews/` | Per-page proposals supplied by the three readers, with crop coordinates and enhancement settings; any main-reader amendment is documented in the final row account. |
| `accepted/` | Main-reader decisions, complete proposed page text, timestamps and original/edited SHA-256 hashes. |
| `scripts/` | Reader conventions, exact-span application and audit, and crop reproduction. |

Decisions: **(a)** correct the transcription to the ink, including an explicit doubt where necessary; **(b)** retain the written author text and note the proposed intended reading or mathematical refinement; **(c)** already as requested; **(d)** the requested change is not on the assigned page. A mixed row may have one local transcription correction and an author-slip note. Repeated statement IDs are distinguished by cote and scan.

Original line endings and unrelated page bytes are preserved. Every nonempty `find` span must occur exactly once in the supplied original page. The audit reconstructs the whole edited page from those spans and requires exact equality with the delivered file. It also checks for overlapping edits, complete row coverage and complete page coverage. TSV fields containing tabs or newlines use standard quoted TSV, readable with Python's `csv` module or a spreadsheet importer.

## Reproducing the audit

Place the once-unpacked original attachment in a sibling directory named `source`, so that it contains `source/IM01_1-6_pages`, `source/IM01_1-6_scans`, and `source/IM01_1-6_corrections.tsv`. Keep this package's directories together. From this package directory, run:

```sh
python scripts/coordinator.py audit --final
```

The audit uses Python's standard library. Crop reproduction additionally uses Pillow. Each crop record specifies its source-page rectangle as `[left, top, right, bottom]`, output width, contrast factor and any rotation. Example:

```sh
python scripts/make_crop.py ../source/IM01_1-6_scans/1_scan144.jpg reproduced.jpg 262 60 930 153 --width 2800 --contrast 1.5
```

The crop is evidence for a reading, not a replacement for the original scan. Enlarging a low-resolution mark does not resolve genuinely ambiguous ink; the corresponding LaTeX retains or adds the archive's `\unsure{...}` macro.

For a rotated crop, add `--rotate 180` (or the recorded angle). When its record states that contrast was applied after resizing, also add `--contrast-after-resize`.

## Scope of the checks

Readers inspected assigned pages and cropped loci, with the main reader checking every return. Mathematical and bibliographical assertions supplied by earlier readers are identified as background unless independently verified. The audit does not silently repair the author's mathematics, infer authorship from a typescript, or execute external catalogue changes. An absent locus is recorded as (d), with a destination only when supported by the supplied material.

Check-event timestamps are UTC. The runtime exposed the model identity but did not expose a numerical reasoning-effort setting, so the event log records that limitation explicitly.
