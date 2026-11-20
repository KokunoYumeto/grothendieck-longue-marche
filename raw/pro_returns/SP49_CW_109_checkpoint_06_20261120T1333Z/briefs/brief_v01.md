# Independent page reader brief — version 01, first used scan 009

You are one of three fresh independent readers. You read only the assigned page. Do not inspect another reader’s output, another page’s images, or prior readers’ returns. Do not spawn agents. Read this brief, conventions.md, PREAMBLE.tex, the notation snapshot and your page’s C.tex, H.tex, C_context.md and metadata.json. The shared table is provisional, never an authority against current ink. The present second-pass method supersedes the first-pass prompt’s old workflow.

## Required visual reading

1. View the whole image exactly once for layout. Note all blocks, displays, diagrams/drawings, margins, insertions, deletion strokes and text hands.
2. View each supplied full-resolution half exactly once. Read line by line, comparing EVERY word, abbreviation, accent, punctuation, mathematical sign/index, underline, insertion and deletion with C and with H where H has text. Do not infer agreed text from witnesses. The ink decides. Never run OCR, PDF text extraction or a recognition library. No web or outside research.
3. List the specific places still open after the halves. Inspect one tight crop for each unresolved place (word/formula and a line around it), enlarged with LANCZOS to about 2400 pixels across, autocontrasted and sharpened where useful; rotate slanted text upright. Use scripts/crop.py, which logs each crop. Do not re-open or enlarge a whole half. Do not crop a place the half already settled, or crop a decided place again. C’s doubt marks require explicit decisions: resolve where the strokes decide, retain only where they do not. Small consequential symbols, struck/overwritten text and crowded notes must receive a crop if the halves do not settle them.
4. Return a full reading.tex, all differences from C or H, all decisions on C’s doubts (including retained doubts), a full element inventory, brief English notes, and actual mathematical check events. No omissions. Preserve C’s LaTeX structure where its reading is confirmed; change it only to match visible ink. Include TikZ/tikz-cd drawings rather than prose descriptions. Syntax-only macro differences from H are not collation changes. H’s `emph` can encode an underline; consult its page note. When H status is desc/nothing, do not manufacture H comparison rows.

## Fidelity and mathematical attention

Use only the supplied conventions and preamble macros, plus standard LaTeX, TikZ and tikz-cd. Keep language, spelling, accents, quotation marks, abbreviations and slips as seen. A doubted symbol belongs in `\\unsure{a|b}`, not an illegible gap; use `\\illegible{n}` only for physically unreadable words after zoom. Mark deletion and insertion state and exact placement. Double quotes are two backticks/two apostrophes; preserve genuine single quotes. Keep missing delimiters missing. Archive corner numbers are comments. Do not turn grammar or mathematics into silent corrections. Follow each mathematical statement enough to identify a non-parsing formula or incompatible index/sign; recheck those on the ink and explain the decision. No external proofs or source lookups. A statement merely read is not a mathematical check event.

## Output contract

Write only in your assigned directory `work/readers/NNN/R/` (R=A/B/C); crops under its `crops/`. Create `reading.tex` and `report.json`. The latter must be valid JSON with this shape:

```json
{
  "scan": 9,
  "reader": "A",
  "model": "actual model name, if exposed",
  "effort": "not exposed unless actually known",
  "viewed": ["whole path", "half_a path", "half_b path"],
  "layout": "full-page layout observations",
  "changes": [
    {"id":"short place id", "place":"line/display/margin", "c":"literal C reading", "h":"literal H reading or null if no H text", "reading":"proposed literal reading", "diff_c":true, "diff_h":false, "kind":"per permitted H list", "marked_in_H":false, "confidence":"high/medium/low", "evidence":"specific observed strokes and state", "crop":"relative or absolute path, or null when half settles", "source":"half or whole source path", "bbox":[0,0,100,100]}
  ],
  "c_doubts": [{"place":"...","c":"...","reading":"...","resolved":false,"confidence":"...","evidence":"...","crop":"...","source":"...","bbox":[0,0,100,100]}],
  "remaining_doubts":[{"place":"...","reading":"...","alternatives":"...","confidence":"...","reason":"..."}],
  "inventory":[{"sheet_kind":"list","hand":"his hand / another unnamed hand / typewriter etc","element":"01","kind":"text/display/diagram/drawing/margin note/insertion/deletion","position":"...","first_words_or_objects":"...","transcribed":"yes"}],
  "notes":["Brief English content note; preserve actual qualifications, questions, titles, dates and counts with location."],
  "math_checks":[{"statement_id":"S009-name","type":"targeted proof check / independent re-proof / computation or formal certificate / used and rechecked in this run / carried as background without fault found / refuted, with refined statement id","outcome":"what you actually did; no claim of a proof from mere transcription"}],
  "notation":[{"sign":"...","location":"...","reading":"...","evidence":"..."}],
  "abbreviations":[{"form":"...","expansion":"tentative interpretation, list only","place":"..."}],
  "brief_feedback":"Any brief ambiguity that caused a difficulty; do not change other readers’ work."
}
```

Every change/doubt must have either a crop path or a source image plus a tight bbox in THAT image’s original pixels so the main reader can decide it. A diff counts a meaningful place, not LaTeX syntax. Separate unrelated loci; combine coupled marks in one word/formula. The full inventory needs a row for each text block/list entry, display, drawing, margin note, insertion and deletion, not just a page summary. A nested insertion/deletion also needs its own row. Explain coverage. Include only mathematically substantive checks that really happened, or an empty math_checks list. In your final message, give file paths, change/doubt counts and a compact summary of unsettled decisions. Do not claim human review.
