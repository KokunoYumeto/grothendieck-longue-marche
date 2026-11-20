# Page reader instructions

Read only your assigned page packet, its scan, and this instruction file. The packet contains that page's exact original LaTeX, its correction rows, the scan path, and PREAMBLE macros. Do not read other pages or the complete corrections table. Do not use OCR, text recognition, external sources, or any subagents. This is visual diplomatic transcription, not mathematical correction.

For EVERY assigned row locate the span in original LaTeX, inspect the actual scan visually with view_image, and make one tight crop for each relevant place, enlarged to about 2400–3200 pixels across with raised contrast. Use Pillow only for cropping/enlarging/contrast, not recognition. Save crops under `IM01_1-6_work/crops/` with page and row id in their names. Record original pixel coordinates and enhancement method in your proposal. Inspect the crop with view_image; merely creating it is not inspection. For classification/global rows inspect relevant title, passage, or page context, without attempting to prove mathematical claims that are not the task.

Decisions:
- a: original transcription misreads or omits visible ink: correct only that row's place in the page's own macros.
- b: manuscript reads as transcribed; suggested change is the author's slip, intended mathematics, or mathematical refinement. Leave the text untouched; provide a precise note about what is written and the proposed intended/refined reading, attributing mathematical assertions to the supplied correction unless actually checked.
- c: the original page already says what this row asks, including an existing explicit doubt when that is the row's request. No edit.
- d: the correction concerns text or catalogue metadata not on this page. No edit; say where the relevant place is if it is actually supplied/visible, and distinguish a pointer in the row from your observation.

Rows whose kind is flag, open, not sorted, a second-model pass, checked_on_scan=no, or whose account disagrees with original LaTeX MUST be decided on ink. We are visually checking all rows for a reliable record. Michel Hua's human checks should be applied unless ink plainly shows otherwise; explain any exception. Mathematical plausibility is not evidence of a letter or symbol. If ink cannot settle a reading, use an explicit `\unsure{reading|alternative}` at that row's place, with confidence medium or low, and explain the unresolved strokes; never invent a definite reading. Preserve genuine author slips.

Preserve every unrelated byte: no spelling/accents/abbreviations/notation normalization; no reformatting or new surrounding prose. `\deleted{…}` is struck ink, `\inserted{…}` is inserted ink, `\margin{…}` is a margin note, `\unsure{…}` is doubtful, `\illegible{n}` is illegible. Diagrams remain tikz-cd. Do not transcribe the paper watermark EXTRA STRONG or paper specks.

For each a row, give an exact `find` string that occurs ONCE in the ORIGINAL page and a `replace` string changing only the row's matter. For b/c/d, `find` and `replace` are empty. If two rows concern the same place, do not create duplicate overlapping edits: one a row can own the physical edit; for the other row judge the ORIGINAL page honestly, explain the relationship, and tell the main reader if an overlapping-row representation needs resolution. Mixed rows can be a for a real transcription change while preserving an author slip and documenting both.

Write a JSON proposal (UTF-8, ensure_ascii=False) to `IM01_1-6_work/reviews/<page>.json` with:
```
{
  "page": "1_scan004",
  "worker": "reader1",
  "rows": [{
    "id": "L...", "cote": "1", "scan": "4",
    "decision": "a|b|c|d", "find": "...", "replace": "...",
    "what_the_ink_shows": "Observed strokes and exact crop path(s), not merely a conclusion or a mathematical argument.",
    "confidence": "high|medium|low",
    "note": "Required for b, d, unresolved ink, mixed cases, or anything needing parent attention.",
    "checked_at": "actual current UTC timestamp",
    "event_type": "used and rechecked in this run",
    "event_outcome": "Describe only the visual/textual check actually done; do not claim a mathematical proof.",
    "crops": [{"path":"crops/<filename>.jpg", "box":[x0,y0,x1,y1], "scale_width":2800,"contrast":1.5}]
  }],
  "proposed_latex": "The complete original page with only the a edits applied.",
  "open_issues": []
}
```
Use `used and rechecked in this run` for an actual scan/text comparison. Use `carried as background without fault found` only for a separate mathematical assertion you did not check (tell parent if a second event is needed). Do not call visual inspection a proof check. Model/effort identity will be added centrally: GPT-6 Astra Pro, inherited effort not exposed, run name given by worker.

Do not write final edited_pages, placements.tsv, notes.md, CHECK_EVENTS.tsv or progress.log: the main reader reviews and writes those. Return a concise result listing each row's decision, exact edit, observed ink, crop paths, and any issues. Do not ask the user anything. Finish your assigned page then wait for a new assignment.
