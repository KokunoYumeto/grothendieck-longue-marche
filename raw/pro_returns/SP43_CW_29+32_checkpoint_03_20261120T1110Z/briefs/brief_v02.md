# Independent reader brief v02

First use: cote 29, scan 037. You are one of three independent fresh readers of this ONE page. Do not inspect another reader's directory, messages, readings, or decisions. Do not read other pages. Source files are drafts; the scan alone decides. No OCR, PDF text extraction, recognition library, internet research, published text, or remembered completion. Follow the mathematics only to locate ink that needs inspection.

Read your page bundle's meta.json, C.tex, H.tex and C_prior_questions.md; read out/PREAMBLE.tex and the supplied notation snapshot. The main prompt supersedes older witness workflow instructions. Read only this brief and assigned files. No further agents: all three reader slots are already assigned.

## Required workflow

a. View the whole image ONCE for layout: all text, displays, drawings, diagrams, margins, insertions, deletions and page numbers.

b. View half_a and half_b ONCE EACH at original full resolution, then read every line, word, accent, ending, sign, formula, index, decoration and correction against BOTH witnesses. Each agreed reading must also be seen in the ink. Do not enlarge or reopen an entire half. Preserve the reading where settled there. C's notes and doubts are a list of questions to decide, not an answer key.

c. List places left open by the halves, including still-disputed witness readings, every unresolved C doubt, tiny mathematically decisive signs, slanted/struck/crowded notes. Make ONE tight crop for EACH open place (word/formula plus about one line around it); use Pillow LANCZOS to enlarge to roughly 2200–3200 pixels across, autocontrast, sharpen only if useful, rotate if slanted. View it with the image-viewing tool. Do not crop a place already settled by the halves or crop a decided place again. Record source image, pixel box, rotation, output path and what is visible. A candidate is not settled by grammar or expected mathematics. Retain explicit doubt if strokes do not decide. All crop files go only in YOUR assigned output directory's crops/.

d. Write your complete page reading and exhaustive differences from C and H. Include any differences in punctuation, accents, spelling, missing or extra text, deletion state, placement, underlining, alphabet and mathematics. Ignore macro syntax alone when it encodes the same ink. Account explicitly for EVERY C doubt, resolved or retained. Inventory every element and describe the mathematical content briefly. Record genuine mathematical checks separately from the act of reading; transcription is not proof verification. Return, then end this reader run. The next page has three fresh readers.

## Diplomatic conventions

Use only macros from PREAMBLE.tex plus standard LaTeX/amsmath/amssymb/mathrsfs, TikZ and tikz-cd. Preserve language, spelling, accents or absence, punctuation, numbering, abbreviations and surprises. No expansions, modernization or repairs. Join end-of-line hyphenated words, retain lexical hyphens; preserve paragraph boundaries, not ordinary line wrapping. Headings/closings/signatures of letters keep their lines.

Use \scanpage{N}, \mspage{n}; archive pencil numbers are comments `% archive sheet number: n`, stamps comments. Use \handwritten{} around handwritten parts of typed text; \deleted{}, \inserted{}, \margin{}, \uline{}, \uuline{}. Include readable cancelled letters, even inside words. An insertion's position follows the caret/arrow, never grammatical convenience. A physically empty interval is not a license to supply a missing arrow, Greek letter, intersection or relation.

Use the actual alphabet and decoration. Typescripts have no bold; distinguish deliberate double striking (\mathbb) from script capitals and accidental heavy ink. Inspect heading capitals independently. Distinguish i/j, l/1/ell, u/nu, prime/^!, bar/tilde/hat, upper/lower indices, stars and dots, arrow directions and inequalities. The actual letter shapes decide.

Use \unsure{reading} or \unsure{reading|alternative}; first candidate is best ink, never merely expected mathematics. List all candidates supported by ink. A recurrent ambiguous glyph is marked at its first occurrence on each page, then uses that first candidate; document all candidates. \illegible{n} only for genuinely unreadable words after crop, never as a substitute for a symbol within formula/diagram. No omission as a doubt device. Double quotes are two backticks/two apostrophes unless literal guillemets are visible.

Diagrams are \diagram{\begin{tikzcd}[ampersand replacement=\&] ... \end{tikzcd}}, including every arrow/label/decoration/struck part. Drawings are \figure{\begin{tikzpicture} ... \end{tikzpicture}}, with geometry and labels, never prose descriptions. Displays use \[ ... \], aligned when needed, tag* for written labels.

## Deliver your independent record

In your assigned directory, create:

- `reading.tex`: complete scan text in the required conventions.
- `report.json`: object with keys `reader`, `page`, `started_utc`, `finished_utc`, `views` (actual paths and observed role), `differences`, `c_doubts`, `inventory`, `notes`, `notation`, `checks`, `crops`, `unresolved`.
- `report.md`: readable concise account of the same findings; if report.json is complete this can be short.

Each `differences` item: `id`, `place` (approximate physical line), `C`, `H`, `reading`, `diff_C` boolean, `diff_H` boolean, `kind`, `marked_in_H` yes/no/absent, `evidence` (actual strokes/marks, not merely confidence), `source` (half name or crop relative path), `bbox` [left,top,right,bottom] on ORIGINAL WHOLE image for parent adjudication when possible, `confidence` high/medium/low, `mathematical` boolean. A difference may be one local cluster of adjacent changes, not a whole page or paragraph. `kind` is exactly one of: misread word; misread symbol or index; omission; text not on the page; deletion state; insertion or placement; abbreviation expanded or spelling modernised; readable ink left as \ill{}; drawing or diagram; other.

Every `c_doubts` item: `place`, `C`, `reading`, `status` resolved/retained/changed, `evidence`, `source`, `bbox`, `confidence`. Retaining the same explicit doubt is recorded here even if not a change. It may also be included in differences when H differs.

Every `inventory` item: `scan` as cote/NNN, `sheet_kind` (text, reused_typed, typescript, letter, list, cancelled_draft, cover), `hand` (his hand, another named/unnamed hand, typewriter, print), `element` id, `kind` (text, display, diagram, drawing, margin note, insertion, deletion), `position`, `first_words_or_objects`, `transcribed` yes. Each deletion/insertion has its own row, in addition to containing text block. Include page-number/title text elements.

`notes`: short English content description, written doubts/slips with exact words, dates/titles/counts, and each mathematical consideration that caused an ink decision. `notation`: provisional recurring signs with scan/line evidence and limits. `checks`: only actual events, each with statement_id, statement, type, outcome; allowed types: targeted proof check / independent re-proof / computation or formal certificate / used and rechecked in this run / carried as background without fault found / refuted, with refined statement id. Do not call mere transcription a mathematical check. Attribute document claims as claims, not verified theorems.

`crops`: list of every crop made, with `path`, `source_image`, `bbox`, `rotation`, `reason`. `unresolved`: all surviving doubts with alternatives and confidence. Record only work actually performed. Prefer an honest uncertainty to invented resolution. Do not make changes outside your assigned directory.

## Clarifications from scan 29/036 (v02)

- A cancellation marker alone is NOT a doubt mark. Set marked_in_H=yes only for an explicit uncertainty or illegibility mark, not merely \struck{}.
- H’s \page{n} records the archive page n. Do not count the same archive number in C’s comment as an H omission. Record any actual incorrect number, not formatting syntax.
- H’s \note{} and section headings may be editorial. Do not transcribe them as ink. Treat equivalent state/emphasis macros semantically.
- An overtyped cell can contain two recognizable letters without establishing which was earlier. Do not invent a deleted/inserted chronology. Mark competing readings when the ink does not establish the live form.
- Report placement uncertainty separately when the insertion is clear but its anchor is not. An absent caret alone does not require moving words away from their immediate spatial position.
- Keep the complete line-by-line reading, but avoid duplicating evidence paragraphs: a short sentence per difference is enough if it names the visible strokes. c_doubts and unresolved may cite a difference id for already stated evidence. notes should briefly cover page content, mathematical reading decisions, written reservations, and titles/dates/counts; a second prose copy of the entire reading is unnecessary.
- A standalone report.md may be a short pointer/summary; report.json and reading.tex carry the full record.
