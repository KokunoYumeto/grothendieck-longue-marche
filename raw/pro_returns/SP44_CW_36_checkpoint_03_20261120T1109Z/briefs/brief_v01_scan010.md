# Independent reader brief v01 — first used on scan 010

You are one of three independent readers of ONE page of the Montpellier Grothendieck archive, cote 36. Read only the assigned page. Do not inspect another reader's files or other pages. You have no inherited earlier images. Your role ends after returning this page. Do not delegate further. The main reader will decide disagreements. Work completely; no web, OCR, text recognition, published text, or inferred restoration.

## Inputs and authority

The page packet contains the paths to the whole image and two full-resolution overlapping halves, witness C, witness H, C's page-specific doubts and notes, and a frozen notation table from earlier decided pages. Both witnesses are fallible AI drafts. Agreement between them is not evidence. Read all ink, including agreed words and every exponent, accent, omission, deletion and insertion. The notation table is a set of earlier readings to compare with the present ink, never a rule overriding it.

## Required visual workflow (a–d)

a. Open the whole page image ONCE with view_image, for layout only. Identify all text blocks, displays, diagrams, drawings, margins, insertions, deletions, typed/handwritten matter, and page numbers.

b. Open the two supplied halves ONCE EACH, in order, and read every line against BOTH witnesses. Read ordinary prose letter by letter, especially accents, spelling and abbreviations. Read formulas symbol by symbol, including every prime, index, exponent, underline, hat, tilde, bar, relation and arrowhead. Determine struck/live state and attachment of insertions. Mark source typography without modernizing it. Full halves are already at source resolution: do not enlarge/reopen the entire half. A claim that you viewed images is permissible only if you actually called the viewer and saw them.

c. List the places those halves leave open: an unresolved witness disagreement, each C doubt, small consequential glyph, crowded/struck/slanted note, or glyph alphabet requiring a separate look. Crop each such place ONCE tightly, including the word/formula and about one surrounding line, enlarge with LANCZOS to 2000–3000 pixels wide, autocontrast, modest sharpening if helpful, and rotate slanted writing upright. Use the supplied crop helper (or a documented equivalent), then view_image to inspect the crop. Do not make multiple crops of the same locus or crop a place the halves settled. Record actual crop filename and bounding box. If uncertain after this, keep the uncertainty, not a guessed resolution.

d. Return the complete diplomatic LaTeX page, a full comparison report, and structured JSON. Record every semantic/ink difference from C or H, even when the final reading follows one witness; ordinary macro differences with the same reading do not count. Include C doubts that resolve or remain, even if unchanged. Include an inventory and notes of mathematical issues encountered while reading. Do not merely list amendments: the complete page is required.

## Diplomatic conventions

Use only the attached PREAMBLE macros and standard LaTeX/amsmath/amssymb/mathrsfs/TikZ/tikz-cd/enumitem/ulem. `\cotefile{36}` appears only at scan 010; each page begins `\scanpage{N}`. Use `\mspage{n}` for the text's number; archive pencil numbers only in `% archive sheet number: n` comments. Keep exact French/other language, spelling, accents, punctuation, abbreviations and numbering. Join line-end hyphenated words, but retain lexical hyphens. Preserve paragraphs and document order.

`\handwritten{...}` surrounds handwritten matter on this typescript, down to the handwritten part of a formula/word. `\deleted{...}` records readable cancelled matter (including machine x-outs), `\deleted{\illegible{n}}` physically unreadable cancelled words. `\inserted{...}` goes at the target indicated by a caret/line/arrow; `\margin{...}` is for an independent margin note. `\uline{...}`, `\uuline{...}` preserve single/double underlining. `\unsure{reading}` or `\unsure{reading|alternative}` marks unresolved reading, first candidate closest to ink. `\illegible{n}` only for physically unreadable words after zoom, never a formula/diagram symbol. A recurring ambiguous glyph is marked on its first occurrence on each page and entered in the notation table; subsequent instances use its first candidate. Preserve all candidates the ink actually permits. Do not invent candidates from mathematical expectation.

Displays use `\[...\]`, multiline displays `aligned`, labels `\tag*{...}`. Diagrams must be drawn in `\diagram{\begin{tikzcd}[ampersand replacement=\&] ... \end{tikzcd}}`; drawings in `\figure{\begin{tikzpicture}...\end{tikzpicture}}`, including every label and cancelled component. Never substitute a description. Use two backticks/two apostrophes for source double quotes; guillemets only when drawn. No new macros. No bold for heavy typewriter impressions: distinguish double strike (`\mathbb`), single glyph with a separate underline (`\underline`), and script handwriting (`\mathscr`/`\mathcal`) from actual strokes. Check capitals individually, especially in headings; no global alphabet normalization. Distinguish `^!` from prime, i from j, ell from 1, zero from o, and all signs/directions from ink. Leave the author's mathematical errors untouched.

## Mathematics and evidence

Follow the mathematics as a diagnostic: non-parsing formulas, wrong domain/codomain, indices, signs or implications flag a locus for reinspection; the ink decides. Briefly describe what the page states and any such decision, retaining the author's own words of doubt. Reading a claim is NOT proving it. Record an actual mathematical check separately with its assumptions and exact check type. Do not import literature or claims from other pages. No theorem needs to be proved merely because it appears.

## Output protocol

Your assigned directory is `readers/scanNNN/Rx/`. Create it if needed. Write:

1. `reading.tex`: full page in required macros.
2. `report.md`: UTC start/end, image-view record, line-by-line coverage (compact but explicit), all witness differences and C doubts with ink observations, mathematical reading notes, full inventory, notation additions, and any suggested clarification to this brief.
3. `result.json` with this schema:

```json
{
  "scan": 10, "reader": "R1", "started_utc": "...", "ended_utc": "...",
  "images_viewed": ["whole", "a", "b"],
  "differences": [{"id":"R1-010-01", "place":"line/display/margin", "C":"exact reading", "H":"exact reading", "reading":"your reading", "against_C":true, "against_H":true, "kind":"misread word", "marked_in_H":false, "confidence":"high", "ink":"specific strokes/marks", "evidence":"half a or crop relative path", "bbox":[0,0,100,100], "C_doubt":false, "math_consequence":"none or short explanation"}],
  "unresolved": [{"place":"...", "reading":"...", "alternatives":["..."], "confidence":"low", "reason":"..."}],
  "inventory": [{"sheet_kind":"typescript", "hand":"typewriter or his hand", "element":"010-01", "kind":"text", "position":"top", "first_words_or_objects":"...", "transcribed":"yes"}],
  "notation": [{"sign":"...", "appearance":"...", "latex":"...", "evidence":"...", "ambiguous":false}],
  "abbreviations": [{"form":"...", "expansion":"..."}],
  "notes": ["what it states", "own reservations quoted", "mathematical diagnostic and the ink decision"],
  "check_events": [{"statement_id":"36-010-...", "type":"targeted proof check", "outcome":"actual check, with limits"}],
  "crop_count": 0, "brief_feedback": "..."
}
```

Valid `kind` for a difference: misread word; misread symbol or index; omission; text not on the page; deletion state (struck given live or live given struck); insertion or placement; abbreviation expanded or spelling modernised; readable ink left as `\ill{}`; drawing or diagram; other. Each separate locus is a separate row. C-doubt confirmations may have both against flags false. Inventory kinds: text, display, diagram, drawing, margin note, insertion, deletion. Inventory covers EVERY text block and display and every individual intervention, including what both witnesses omit. Hand attribution must remain cautious where not established by the ink.

The final chat return to the main reader should give file paths, key decisions, crop paths, unresolved items, and count of rows, without pasting the entire page. Do not read any other reader's return. Do not alter shared deliverables, notation or progress.log.
