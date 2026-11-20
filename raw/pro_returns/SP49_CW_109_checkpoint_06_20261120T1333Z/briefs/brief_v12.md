# Independent page reader brief — version 12, first used scan 027

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


## Version 02 clarifications (from scan 009)

- Exact allowed `kind` values: misread word; misread symbol or index; omission; text not on the page; deletion state (struck given live or live given struck); insertion or placement; abbreviation expanded or spelling modernised; readable ink left as \ill{}; drawing or diagram; other.
- Count a resolved or narrowed C doubt as a C change even if its first candidate stays the same; also list its doubt decision. A retained identical doubt is a decision but not a change. H macro spelling alone is not a difference.
- `marked_in_H` means an actual doubt mark (such as ill or uncertain) at that locus. A descriptive note or deletion macro by itself is not a doubt mark.
- If proposing to remove a witness’s isolated period as a paper/ink speck, use a tight crop with surrounding context when the half leaves its position unclear. Do not decide absence merely because unrelated specks occur elsewhere.
- A smaller or raised line can be a separate entry. Insertion markup requires visible placement evidence (caret, connector, interlinear continuation), not an assumed sequence of writing. Describe the evidence and retain distinct entries/references.
- Keep all reading fields literal. Do not replace a drawing/diagram reading by a description or ellipsis; put its actual TeX in reading.tex and quote the relevant code in the report, or state the exact file span in a separate code-reference field. Short English content notes are enough; put workflow observations in brief_feedback, not the content notes.
- These reader files are intermediate work for the parent’s single ZIP. The parent handles persistence; do not upload separate files or contact the user. Do not inspect source pages beyond your assigned page or any other reader output. Model provenance is GPT-6 Astra Pro (inherited); reasoning effort is not exposed, so record that honestly.


## Version 03 clarifications (from scan 010)

- Inventory sheet_kind must be exactly one of text, reused_typed, typescript, letter, list, cancelled_draft, cover. Put finer descriptions in layout/position, not a new enum value. Kind must be text, display, diagram, drawing, margin note, insertion or deletion; underline spans may be nested text rows.
- Read H together with its page note. If the note explicitly preserves an interlineation or other state that its running-text macros flatten, treat the combined encoding as equivalent; do not count an omitted insertion merely because a macro is absent. Still report wrong scope, extra punctuation or missing underlines. Editorially supplied letters absent from the ink are differences, but describe them as transparent editorial additions.
- Record all explicit C doubt marks and the page-specific doubts/context alternatives, even when confirmed unchanged. Distinguish confidence in deletion extent from confidence in a cancelled letter. A majority reading does not by itself settle buried ink.
- Use smaller image-output groups if displaying many crops risks tool-output truncation. A generated crop not actually displayed has not been visually inspected.


## Version 04 clarifications (from scan 011)

- H’s literal guillemets versus manuscript paired quote strokes are shape differences, not macro-syntax equivalence; list each affected quoted span. The same distinction applies to visibly different mathematical alphabets.
- H explanatory notes can govern more than one page. Parent will supply any relevant inherited note as H_context.md where applicable. Consult it if present; do not seek other pages. A mark explicitly preserved there must not be called omitted. A documented interlineation can still be attached to the wrong position in H’s running text.
- A whole-word cancellation can have certain extent but uncertain interior letters. Read the old word from its surviving strokes, not from an adjacent live replacement.
- Do not count normal TeX wrapping as layout differences. Report actual paragraph/order differences where visible spacing, indentation, connectors or block structure support them.


## Version 05 clarification (from scan 013)

A removed or revised C uncertainty macro counts as a literal C change. A C_context alternative rejected while the literal C text remains identical is a confirmed context/doubt decision only, not a changes row. Put all such confirmations in c_doubts/notation as appropriate. Keep actual mathematical checks separate from ink confirmation; record any proof, scope check or counterexample actually performed, with its limits, without inserting qualifications absent from the page.


## Version 06 clarifications (from scan 018)

- Mark uncertainty at every occurrence whose ink remains uncertain. A doubt on an earlier occurrence, or a shared note saying both occurrences are doubtful, does not make a later unmarked occurrence certain. Recheck the actual strokes independently; do not propagate uncertainty or certainty solely from repetition.
- Before reporting a witness difference, compare the exact literal C/H text at that location. A preliminary visual impression is not yet a collation row. Check the final full-text diff against the reported change list so existing punctuation is not falsely called omitted.


## Version 07 clarification (from scan 021)

Do not attempt LaTeX compilation, format building or installation. The supplied first-pass PROMPT.md explicitly says not to try compiling in this sandbox; this instruction was outside the excerpted Absolute rules. Use static brace, delimiter, environment, macro and literal-diff checks only. If a page input includes C_context_addendum.md, read it with C_context.md; the parent supplies any missing source context equally to all readers.


## Version 08 clarification (from scan 022)

Preserve the physical side of marginal notes. The supplied margin macro alone normally places a note on the right; for a visibly left-hand note, use standard LaTeX margin-side controls or an anchored TikZ placement, without moving it to the opposite side. A single physical punctuation group between two entries must be represented once even when its attachment is uncertain; record that uncertainty and the observed position instead of reproducing a witness's double assignment.


## Version 09 clarification (from scan 023)

Check quotation strokes at each edge of a cancelled phrase separately. Do not automatically include the opening and closing marks in a whole-phrase deletion merely because the words are cancelled in C. Distinguish a quote visibly outside the cancellation path from a quote within its terminal crossing; preserve the different states when the ink supports them. Record visible isolated points without inventing their function, and distinguish an uncertain punctuation identity from a geometrically certain mark.


## Version 10 clarification (from scan 024)

When long rules or other drawings run beside or through text, preserve their relationship to that text using anchored TikZ or a faithful local layout. Do not relocate them to a disconnected geometry panel before the writing. At an isolated upper stroke near an i, distinguish its visible geometry from a proposed function; if reproducing it separately, do not inadvertently add the same physical dot twice. Do not infer any missing letter from this guidance.


## Version 11 clarification (from scan 025)

Distinguish a mark outside the extent of a cancellation from a mark whose separated parts happen to straddle its path. A line passing between an exclamation stem and dot, and continuing beyond them, does not alone prove that the sign is live. Keep deletion state uncertain when the path does not decide it. Raised text/marks and visible carets belong at their observed height; an insertion macro alone does not encode that physical position. Check every small index independently, including adjacent indices in the same formula.


## Version 12 clarification (from scan 026)

An overwritten multi-character reference may reuse an unchanged leading character. Preserve each physical glyph once and place the old/new portions over one another where the ink overlaps; do not automatically print complete old and new numbers consecutively. For faint rules or traces, describe their observed endpoints as well as a readable middle segment; a local crop confirming the middle does not establish extension to the foot of the sheet.
