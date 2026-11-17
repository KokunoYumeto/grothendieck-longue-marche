# Pre-freeze validation

Completed 2026-11-17 23:06:48 UTC.

- 42 page files, exactly scans 046–078, 080–087 and 089.
- 42 per-page completion records and 42 separate visual audit records.
- 646 inventory rows; all marked `yes`; all required columns and allowed categories checked.
- One combined fragment, exactly the ordered concatenation of the page files, beginning with `\cotefile{138}` and `\scanpage{46}`.
- 26 TikZ-CD environments and 3 array tables within diagram macros.
- 349 explicit uncertainty macros and 3 physically unreadable word spans, estimated at 6 words in total.
- Successful pdfLaTeX compilation of the raw fragment using the disposable harness in `scripts/check_tex.py`; no syntax, missing-glyph, overfull or underfull warnings in the final log.
- Rendered checks inspected on 047, 053, 062, 064, 078 and 089. The drawing and its inner barycentric triangle on 078 share one TikZ figure and have separate inventory rows.
- The temporary harness uses colours for page-state macros and is not the diplomatic deliverable or a facsimile. Its 44 physical sheets do not assert manuscript pagination.
- SHA-256 hashes for all 42 page files and the combined fragment are recorded in `SHA256SUMS` and `progress.log` before any contextual source was opened.

No OCR or sub-agent transcription was used. Source images and the context archive are excluded from the deliverable archive.
