# Independent reader brief — v05, first used on scan 014

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

## Clarifications after scan 010 (v02)

- The exact preamble is `/workspace/scratch/a62c50f64437/SP44_CW_36_work/PREAMBLE.tex`; read it. It defines the diplomatic macros; do not invent new ones. The preceding page's notation remains a provisional comparison, not a mandate for the present ink.
- Distinguish a mechanically repeated chi-shaped substitute from a pen ell, and a genuinely displaced double impression from merely heavy type. Record what is seen; retain a literal alphabet uncertainty where needed, rather than silently selecting the intended mathematical parameter.
- A typed letter can survive within a correction: preserve the surviving typed part and mark only the added/cancelled parts. Likewise, separately account for live new and cancelled old closing parentheses. Do not restore a complete old word when only some of it was cancelled.
- Do not collate a mere missing handwriting wrapper around an otherwise identical filled-in glyph as an H reading error. Record that provenance in the inventory/report. Explicitly wrong typed/handwritten claims, changed deletion/insertion state, missing old letters, missing words, and actual glyph/underline differences still require rows. Treat an H note that records a particular old letter as part of H, even if not inline. Macro equivalents (e.g. arrow commands of the same meaning/shape, source add versus inserted) alone are not rows.
- Keep the complete difference list and inventory in result.json. report.md may refer to those lists instead of duplicating them in full; it must still give compact line-by-line coverage, visual sequence, mathematical diagnostics, actual check reasoning, unresolved readings, and brief feedback. This removes repetition without reducing the examination.
- Check-event types must be exactly one of the user's categories: targeted proof check; independent re-proof; computation or formal certificate; used and rechecked in this run; carried as background without fault found; refuted, with the refined statement's id. Classify a small conditional degree calculation as computation, explicitly saying no formal certificate. A local conditional argument is a targeted proof check, not a proof of every theorem on the page. No mathematical check is required merely because a statement was transcribed.
- Nonalphabetic marks may be reproduced faithfully as TikZ with an in-place doubt indicator for uncertain interpretation. Do not invent authorial letters/drawings from incidental pale scan-edge traces. A remaining interpretive doubt must be documented.

## Clarifications after scan 011 (v03)

- Look carefully for a smaller old letter under an otherwise normal live word: a round bowl under t, an ascender under v, or an extra x-out cell can be a real correction, not merely heavy type. Separate the old glyph from the live one only where strokes support it; do not invent a whole earlier word. Distinguish repeated damage to a typewriter key from a local overprint.
- Do not infer handwriting simply because a numeral lacks serifs. Compare the same numeral in other formulas on THIS page. If source-layer uncertainty remains, mark it in place, e.g. a preferred ordinary numeral with its handwritten alternative. Do not use other pages’ images.
- A pen underline below typed letters is represented by the established \uline{word}; record the pen provenance of the rule in inventory. Do not wrap an unexecuted command alone as \handwritten{\uline}{word}, and do not label the word itself as handwriting.
- For every difference settled directly on a half, give an approximate bounding box in WHOLE-image coordinates. This lets the main reader make a local adjudication crop without reopening the whole page. Do not make an extra reader crop merely to supply a bounding box.
- Preserve observable paragraph cues (indent, blank line, enlarged spacing). A source line break alone is not a paragraph. Record uncertain paragraph intention separately without supplying unobserved spacing.
- A literal o-shaped typewriter index and its numerical-zero interpretation can remain uncertain. Compare size/strokes locally; the mathematical role alone does not settle the alphabet.
- Structural checks only: balanced braces/math/environments, allowed macros, complete JSON/inventory. Do not compile the LaTeX.


## Clarifications after scan 012 (v04)

- H's supplied opening note explicitly says the machine ell is chi-shaped and that constant sheaves are underlined. Credit this global note throughout: H ell versus a literal chi/ell transcription alone is not an H error. A source-layer change against C can still be recorded. Do not change a present glyph merely to match prior notation.
- H's supplied preamble says emph marks authorial emphasis. Equivalent emph/uline markup alone is not an H difference. Compare actual extent of underlining, which can differ. Bold Z/Q versus ordinary underlined Z/Q alone is house typography unless the ink establishes a different alphabet.
- Clearly marked H explanatory/editorial commentary is not authorial text. Do not classify its absence from the scan as spurious source text. H notes asserting an old letter, a pen/type source layer or a particular correction ARE witness readings and must be checked.
- Distinguish the visible x-out characters from recoverable underlying cancelled letters. If xx records two visible cancellation cells rather than an old lexical xx, say so explicitly in the report. Do not pretend to recover old letters from the count of cancellation strokes.
- Overlapping letter components need not prove a temporal old/live order. If that order is uncertain, retain an in-place structural alternative rather than making an unqualified deletion. Conversely, the old and live final vowels can each remain uncertain; certainty about one must not be inferred from grammatical expectation.
- A curved hook adjacent to an insertion may be the end of a placement guide. Follow its visible continuation before adding punctuation, and preserve the actual insertion target.
- Prefer one or two images per viewer output so that image delivery is not truncated. If a viewer output is truncated before inspection, record it and resend the SAME saved image; do not create another crop of the locus.


## Clarifications after scan 013 (v05)

- An underline can begin inside a word. If the endpoint is visually clear, encode the actual partial-word span with ordinary uline, rather than forcing a whole-word alternative. Semantic emphasis is not inferred from the endpoint. Retain doubt only where the stroke itself remains uncertain.
- Inspect accents on handwritten insertions as strokes; a familiar word must not dictate acute versus grave. Distinguish the source form from its expected spelling.
- A typed interlinear insertion can have a pen placement guide. Assign the source layer separately to the letters/rule and to the guide; do not infer that the letters are pen merely because the guide is pen.
- In the JSON counts, resolving a C doubt is against_C=true, even if its first candidate is retained. An unchanged doubt is false. Different ordering of secondary alternatives alone need not be counted. For H, uncertainty markup alone with the same preferred reading is not automatically a reading error; an actual alphabet, correction-state, source-layer or scope difference still is.
- Record each literal typewriter x product locus when its baseline character differs from H's rendered multiplication cross. A dark impression alone does not prove a pen intervention. Supply whole-image boxes for half-settled loci; do not crop them again merely to add coordinates.
- Preserve observable paragraph/display placement. A final equation printed as an ordinary continuation at the text margin is retained there; a witness's added centered display is a placement difference. Equivalent tag/itemize commands alone are not reading differences.
