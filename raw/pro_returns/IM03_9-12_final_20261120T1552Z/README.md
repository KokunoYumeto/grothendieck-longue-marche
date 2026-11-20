# IM03_9-12: decided diplomatic corrections

This archive contains the decisions for the 75 supplied correction rows and all 58 resulting LaTeX pages. The original attachments are not included.

## Main deliverables

- `placements.tsv`: the eight requested columns, in the supplied correction-table order. Repeated IDs are distinguished by cote and scan. For decision **a**, `find` is an exact, unique span of the original page and `replace` is that same span with only the accepted reading corrections. For **b**, **c**, and **d**, both fields are empty.
- `edited_pages/`: every resulting page under its original filename, including pages that required no change. Original CRLF line endings and unedited bytes are preserved.
- `notes.md`: the written readings and proposed editorial sense for **b**, placement findings for **d**, and explicit doubt or mixed-row notes where applicable.
- `crops/`: enlarged, contrast-adjusted facsimile crops. `manifest.tsv` records the source coordinates, scale, contrast, and creation time. Separate places have separate crops.
- `CHECK_EVENTS.tsv`: an initial reader event and a main-reader event for each correction row, plus any focused rechecks. These events document actual visual and transcription comparisons, not mathematical proofs.
- `progress.log`: the initial UTC timestamp followed by the completion timestamp of every page.

The TSV uses standard quoted fields. Exact LaTeX spans may contain tabs or CRLF line breaks inside a quoted field. Read it with a TSV parser that supports quoting; a count of physical text lines is not a row count. No OCR, text recognition, or PDF text layer was used.

## Decisions and scope

**a** corrects the transcription to the ink. **b** preserves the written text and records the proposed mathematical amendment or other rejected conjectural rewriting in the notes. **c** means the supplied original already has the requested reading. **d** means the quoted target is absent from that assigned page; a different location is only identified when actually inspected.

The human facsimile checks are applied unless direct visual evidence plainly conflicts. Mathematical plausibility does not replace a reading of the strokes. Existing doubts outside an accepted correction are retained. A longer unique `find` span can encompass several targeted places without changing the intervening text. Two rows supporting the same local correction share that correction, which is applied only once.

## Review and reproducibility

`reviews/<page>/proposal.json` preserves the page reader's proposed decisions, exact spans, crop references, and observations. `accepted.json` contains the main reader's final decisions and review note. When the main reader changes a proposal, the initial proposal is retained separately. `proposed.tex` is the reviewed page before its identical copy is written to `edited_pages/`.

Exactly three concurrent page readers were used. Each received one page at a time in the supplied order, with the next page assigned to the first reader available. The main reader checked the returned evidence and accepted edits before marking each page done. The runtime identified the model as GPT-6 Astra Pro; a separate effort setting was not exposed and is not invented in the event log.

`scripts/crop_scan.py` creates documented crops. `scripts/finalize_page.py` checks unique original spans, reconstructs only the accepted edits, writes the final page, updates placements and notes, and records its events and completion. `scripts/validate_work.py` performs the final row, file, crop, event, and byte-preservation checks; its result is `validation.json`. These structural checks do not certify the mathematics.

To repeat the structural validation, place the supplied archive's contents under `source/` alongside these files, then run:

```sh
python3 scripts/validate_work.py --original-zip /absolute/path/to/the/original/IM03_9-12.zip
```

`scripts/package_work.py` packages deliverables and work documentation while excluding the original inputs, earlier ZIPs, and Python caches. Its checkpoint mode enforces the requested minimum 45-minute interval and unique sequential checkpoint filenames. A final package is created after all pages are complete.
