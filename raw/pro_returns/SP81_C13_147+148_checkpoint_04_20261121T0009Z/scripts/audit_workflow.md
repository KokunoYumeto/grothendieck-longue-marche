# Independent box reading

Read only the assigned original scan, its neutral box list, and these transcription conventions. Do not read a page transcription, a first-reading TSV, either witness, notes, prior crop files, another reader's report, or a notation table containing page readings. You are independent of this page's first reader.

The box list has columns `box,kind,x0,y0,x1,y1` in original scan pixels. `kind` identifies the target spatially and distinguishes contextual crossing ink from that target. Inspect the whole image for orientation, then crop every listed box once with `scripts/crop.py PAGE second_BOX x0 y0 x1 y1 [rotation_degrees]`. Use a rotation determined by the original image when necessary. View every resulting enlarged PNG. Save crops under their generated names. Do not use OCR, outside material, a text layer, TeX compilation, or expected mathematics to supply letters.

Write `second/PAGE_second.tsv` using Python's `csv.DictWriter` with tab delimiter, columns `box,reading`. Include one row for every box, in box-list order. A reading is the complete targeted ink in that box, including its punctuation, corrections, underlining and formula labels. Use complete formulas and actual TikZ or tikz-cd diagrams. Do not use summaries or placeholders for readable mathematics. Write this TSV before any comparison; root performs the comparison. Do not open `PAGE_first.tsv` or `PAGE_comparison.json`.

Large PNGs can be omitted by the image-output budget. For each crop, `python scripts/display_crop.py CROP_FILENAME.png` returns the original path or a same-dimension JPEG display path while retaining the PNG evidence. Display the returned image individually, or only a small number of narrow crops together. An omitted or truncated tool image has not been inspected: display it again successfully. The conversion changes the encoding only; it does not recrop, rescale or replace the saved evidence.

## Transcription conventions

- Preserve the handwritten language, spelling, abbreviations, unexpected indices, punctuation, quotation marks, and paragraph order.
- Paper flecks, watermarks and mirrored show-through are excluded from the transcription. A box containing only such material can have an empty reading; explain the material judgment in your return message. Faint punctuation needs a place in the syntax and darkness comparable to nearby writing.
- `\unsure{reading}` retains an uncertain reading. `\unsure{a|b}` lists genuinely supported alternatives. Keep the source's form first; no regularization from expected meaning.
- `\illegible{n}` is for physically unreadable words only, never a mathematical symbol or a whole formula.
- `\deleted{...}` records the exact span crossed by a deletion. `\inserted{...}` records the addition at its actual attachment. A deleted insertion can nest these states.
- `\margin{...}` records marginal content. `\mspage{...}` records the author's own page number or a typed page number. An unattributed pencil number can be represented inside `\margin{...}`.
- `\uline{...}` and `\uuline{...}` record single and double underlining. Use two backticks and two apostrophes for drawn double quotation marks, guillemets only when drawn.
- Use standard LaTeX mathematics, `\diagram{...}` around a displayed diagram, `tikzcd` with `ampersand replacement=\&`, or `\figure{\begin{tikzpicture}...\end{tikzpicture}}` for drawings. Reproduce the written objects, connectors, arrow ends, labels and location relationships. Coordinates and spacing are editorial; glyphs and their relationships are readings.

After saving the TSV, return its path, the crop filenames, and a concise description of locations whose ink remains uncertain. For a graphical box, also report the point/shaft counts and uncertain endpoints that you actually observed; this supplementary report does not replace the complete TikZ reading in the TSV. Save a short observation per box as `work/PAGE_second_observations.json`, using only your own image reading. Do not start another page until assigned.
