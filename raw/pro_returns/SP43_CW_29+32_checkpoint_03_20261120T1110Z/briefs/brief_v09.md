# Independent reader brief v09

First use: cote 29, scan 115. You are one of three independent fresh readers of this ONE page. Do not inspect another reader's directory, messages, readings, or decisions. Do not read other pages. Source files are drafts; the scan alone decides. No OCR, PDF text extraction, recognition library, internet research, published text, or remembered completion. Follow the mathematics only to locate ink that needs inspection.

Read your page bundle's meta.json, C.tex, H.tex and C_prior_questions.md; read out/PREAMBLE.tex and the supplied notation snapshot. The main prompt supersedes older witness workflow instructions. Read only this brief and assigned files. No further agents: all three reader slots are already assigned.

## Required workflow

a. View the whole image ONCE for layout: all text, displays, drawings, diagrams, margins, insertions, deletions and page numbers.

b. View half_a and half_b ONCE EACH at original full resolution, then read every line, word, accent, ending, sign, formula, index, decoration and correction against BOTH witnesses. Each agreed reading must also be seen in the ink. Do not enlarge or reopen an entire half. Preserve the reading where settled there. C's notes and doubts are a list of questions to decide, not an answer key.

c. List places left open by the halves, including still-disputed witness readings, every unresolved C doubt, tiny mathematically decisive signs, slanted/struck/crowded notes. Make ONE tight crop for EACH open place (word/formula plus about one line around it); use Pillow LANCZOS to enlarge to roughly 2200–3200 pixels across, autocontrast, sharpen only if useful, rotate if slanted. View it with the image-viewing tool. Do not crop a place already settled by the halves or crop a decided place again. Record source image, pixel box, rotation, output path and what is visible. A candidate is not settled by grammar or expected mathematics. Retain explicit doubt if strokes do not decide. All crop files go only in YOUR assigned output directory's crops/.

d. Write your complete page reading and exhaustive differences from C and H. Include any differences in punctuation, accents, spelling, missing or extra text, deletion state, placement, underlining, alphabet and mathematics. Ignore macro syntax alone when it encodes the same ink. Account explicitly for EVERY C doubt, resolved or retained. Inventory every element and describe the mathematical content briefly. Record genuine mathematical checks separately from the act of reading; transcription is not proof verification. Return, then end this reader run. The next page has three fresh readers.

## Diplomatic conventions

Use only macros from PREAMBLE.tex plus standard LaTeX/amsmath/amssymb/mathrsfs, TikZ and tikz-cd. Preserve language, spelling, accents or absence, punctuation, numbering, abbreviations and surprises. No expansions, modernization or repairs. Join end-of-line hyphenated words, retain lexical hyphens; preserve paragraph boundaries, not ordinary line wrapping. Headings/closings/signatures of letters keep their lines.

Use \scanpage{N}, \mspage{n}; archive pencil numbers are comments `% archive sheet number: n`, stamps comments. Use \handwritten{} around handwritten parts of typed text; \deleted{}, \inserted{}, \margin{}, \uline{}, \uuline{}. Include readable cancelled letters, even inside words. An insertion's position follows the caret/arrow, never grammatical convenience. A physically empty interval is not a license to supply a missing arrow, Greek letter, intersection or relation.

Use the actual alphabet and decoration. Typescripts have no bold; distinguish two superposed copies of the same letter (\mathbb where the original conventions require it) from script capitals, unlike-letter overprinting and accidental heavy ink. Do not require an inference about the typist's intention. Inspect heading capitals independently. Distinguish i/j, l/1/ell, u/nu, prime/^!, bar/tilde/hat, upper/lower indices, stars and dots, arrow directions and inequalities. The actual letter shapes decide.

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

## Clarifications from scan 29/037 (v03)

- An insertion may include punctuation. Compare each comma or parenthesis with the base line and the raised insertion line before assigning its extent.
- Inspect the actual order of adjacent letters even in familiar repeated words: realization and relaization must be distinguished from the ink.
- List only alternatives with visible supporting contours; do not preserve an unsupported third candidate merely because C included it.
- Each unresolved item must include an explicit `reading` string (including alternatives), `place`, `confidence`, and `source`; do not supply alternatives only.
- Keep inventory rows in top-to-bottom page order, with the inserted/deleted parts following their containing text block. Distinguish the hand making an underline from the typed word where the hand is unassigned.
- A large multi-image tool response can overflow. View whole and halves in separate calls; view at most three small crops in one call. If display fails, record it and redisplay the same crop rather than making a new one.

## Clarifications from scan 29/038 (v04)

- Count distinct typewriter cells when overtyping obscures a familiar word. A proposed word must not introduce a cell absent from the ink. Separate uncertain cells can be encoded separately when that best records the visible contours.
- At a clipped scan edge, transcribe the visible fragment; do not supply wholly invisible letters even inside an uncertainty macro. Describe clipping in the doubt record. A partly visible terminal letter may still be read if its diagnostic contours survive.
- Compare visible punctuation gaps as well as glyphs. A full blank typewriter cell before a comma differs from adjacency; avoid treating an actual inserted/deleted gap as a mere macro difference. Do not count TeX source whitespace which renders identically.
- Detached marks around a letter need their own inventory entry when they are additions; do not omit them from the inventory merely because the letter is encoded with an accent command.
- Small image batches must also avoid a long accompanying text dump. Read report fields selectively; a display that overflowed was not inspected. Redisplay the same image file without recropping.

## Clarifications from scan 29/039 (v05)

- Do not count H editorial section headings, batch-boundary headings or an omitted extraction page macro as ink discrepancies. Record their editorial status in notes. A wrong actual page number is a discrepancy; an equivalent archive number is not.
- For a small non-letter mark, reproduce the visible filled area and darker contours as well as the line skeleton and color when the scan distinguishes them. Do not label it handwriting, a signature or a particular material when its origin is unassigned. No whole-word interpretation is required for a nonverbal mark.
- Reports are final only when you have completed your run. Write the final return after all files are settled; do not make further changes after returning.


## Clarifications from scan 29/083 (v06)

- List each nonadjacent occurrence of a witness difference in its own difference row, with its own whole-image bbox. A repeated symbol can share the explanation by reference, but its six locations must not become one broad row. Adjacent parts of one local correction may remain one row. Make crops only for genuinely open places, not merely to populate a row.
- An explicit prose doubt note in H counts as a doubt mark when it identifies that glyph or recurrence. Preserve the note in `H_doubt_note` and set marked_in_H=yes. A cancellation alone still does not count as doubt.
- A familiar readable word can nevertheless contain unlike-letter overprinting. If different letter contours coexist, record those cells rather than resolving the spelling from its familiar appearance. Narrow uncertainty to the cells still open.
- Separate a crowded upper mark's shape from its maker. Do not automatically mark a blue overprint as handwritten merely because it is above a letter.
- Record the start time before the first image. If timing was not captured, report that limitation; never reconstruct an exact time from a later clock.
- The maximum of three crop images is per display response, not per page. Never combine a long text output with image output. If context/output capacity is low, display one saved crop at a time; a failed display is not an inspection and may be redisplayed without recropping.


## Clarifications from scan 29/102 (v07)

- The identity wrapper \handwritten{} preserves technique in the page file, but its absence from H around the same glyph is not by itself a collation difference. Inventory the handwritten addition without creating a macro-syntax discrepancy.
- Record every inherited ambiguous occurrence in C-doubt and unresolved lists. When a later occurrence uses the first candidate under the recurrence rule and that literal reading equals H, do not add a difference solely for the inherited doubt. An actual different glyph or explicit first uncertainty remains a difference.
- Nonverbal marks may contain a light stem plus several separate dark lobes. Preserve visible mass and tonal differences, but assign no hand, material or textual purpose without evidence.
- Small isolated points in a text line should be preserved with uncertainty if punctuation versus an incidental point is undecidable. Do not silently remove a visible mark merely because the sentence reads without it.
- Do not resolve an application letter from the defining formula. Distinct contours must decide between Greek letters; otherwise retain the ambiguity.
- Supplied prior questions must concern only this scan. If unrelated metadata appears, report it as an input limitation, ignore it, and continue without opening other-page material.


## Clarifications from scan 29/113 (v08)

- A cancelled formula may retain readable punctuation after its uncertain symbol, such as an opening parenthesis. Inspect the entire cancelled cell group and retain readable punctuation.
- Inspect mixed article and heading cells individually. A visible e bowl and raised apostrophe can coexist; do not choose from grammatical expectation. Separate readable cells from uncertain ones.
- An underline of an old cancelled heading may lie beneath a raised replacement heading. Determine which baseline and full word extent the independent stroke follows; do not duplicate it on both headings.
- Preserve left/right placement of written display labels using standard LaTeX. Avoid internal package commands. Placement alone is not a mathematical correction.
- A slanted lower stroke may distinguish leqslant from leq without changing the relation. Mark a change as mathematically consequential only when it changes mathematical content.
- Do not choose EGA/SGA or a Roman numeral by external reference chronology. Handwritten connected strokes are not fixed typewriter cells. Retain explicit alternatives where needed.
- A margin line can be brown-toned with dark reinforced ends. Preserve visible tone consistently, without inferring material or authorship.
- Prior-question extraction is now automatically restricted and validated for the current scan before assignment. If an out-of-page quotation nevertheless appears, ignore it, report exactly what was encountered, and do not open its source.


## Clarifications from scan 29/114 (v09)

- Count every occupied cell between secure word fragments. A tall extra t-like cell may stand beside, rather than inside, an m/n composite; familiar spelling must not suppress it. Narrow doubt to the genuinely mixed cell.
- Two detached points belonging spatially beside a formula must stay at their relative position in the inline TikZ representation, not move to a separate centered figure. Distinguish their tone, size and offsets without assigning purpose or maker.
- A second mark directly above pi may coexist with a separate upper-right exponent. Record both, with alternatives where contours remain mixed.
- Compare full blank cells before colons, semicolons, commas and periods explicitly. Include each nonadjacent difference. Equivalent bold/underline heading macros alone remain excluded.
- At a page boundary, retain the visible terminal fragment and its hyphen when its continuation is not on this page; do not supply a continuation. Ordinary within-page wrapping is still joined.
- Describe a theorem as beginning when only its hypotheses and definitions appear on this page; do not claim its absent conclusion has been read or verified.
- A prior question may contain a generic analogy to another page even after numbered references are filtered. Ignore that analogy; only this page is reading evidence.
