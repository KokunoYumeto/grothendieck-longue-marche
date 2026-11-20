# Reader brief v14 — first used on scan 183

You are one of three independent fresh readers of ONE manuscript page. Read only the designated page packet, this brief, PREAMBLE.tex, the supplied current notation table, and that page’s three images. Do not open other reader returns, other page images/texts, external sources, or internet material. Never use OCR, text-recognition software or a PDF text layer. The scans are the sole authority; the two witnesses are drafts.

## Verification restriction

**Do not try to compile LaTeX. Do not invoke pdflatex, lualatex, xelatex, latexmk, tex, format builders, or TeX-engine probes.** This is an explicit rule of the inherited source PROMPT. Only structural text checks (braces, math delimiters, environments and required macros) are permitted. No PDF or render is requested.

## Required visual sequence

1. Read metadata.json, C.tex, H.tex and C_questions.md in the designated packet. H’s editorial `\note{...}` is not manuscript text; use it to identify its claims, not to import editorial words. Read PREAMBLE.tex.
2. View the whole image exactly once for layout. Then view each full-resolution half exactly once, top then bottom. Use the image-viewing tool, actually emit and inspect its image. Read every line, word, accent, abbreviation, ending, formula, sign, index, arrowhead, deletion, insertion, underline and marginal mark. Agreement of C and H supplies no evidence: see agreed readings in the ink too.
3. Resolve everything the halves settle. List remaining open places: unresolved witness disagreements, every unresolved C doubt, consequential small mathematical signs, crowded/struck/slanted writing. Crop EACH open place ONCE tightly (word or formula plus a line of context), enlarge with Pillow LANCZOS to about 2500–3500 px width, autocontrast, sharpen if faint, rotate if slanted. Save each crop and its original whole-image bounding box. View it once. Do not recrop a decided place or enlarge an entire half. A crop may settle a contiguous phrase, but do not use an expansive crop to avoid identifying distinct places.
4. Return a COMPLETE diplomatic LaTeX page and a complete difference report against BOTH witnesses, with ink evidence. Your reading must be independent of the other two. Identify C doubts resolved or retained. Include a coverage inventory; look for what both witnesses omit. Follow the mathematics while reading; if a formula does not parse or a sign/index/arrow contradicts the argument, inspect the ink. Preserve the ink even if mathematically surprising. Report actual mathematical checks separately from merely reading assertions.

## Conventions

Use only macros in PREAMBLE.tex plus standard LaTeX/amsmath/amssymb/mathrsfs/tikz/tikz-cd/ulem/enumitem. Keep C’s page filename. `\cotefile{134-2}` occurs only at the first page of the combined work (scan 170). Every page starts `\scanpage{N}\mspage{n}` with its observed author number. Archive pencil numbers are only `% archive sheet number: N` comments.

No translation, modernization, grammatical repair or abbreviation expansion. Preserve visible spelling, accents, punctuation, alphabets, indices, exponents and brackets. Double quotation marks are two backticks and two apostrophes unless actual guillemets occur. Join line-end word breaks; preserve paragraphs and letter heading/closing/signature lines.

Use `\deleted{...}` for readable cancelled ink (or `\deleted{\illegible{n}}` for physically unreadable words). For overwriting, readable underlying form precedes live corrected form. Use `\inserted{...}` at the exact caret/line destination; `\margin{...}` only for independent margin notes, with a sideways/slanted comment where applicable. Use `\uline` and `\uuline` for single and double underline. All-handwritten pages need no `\handwritten` wrappers; record the hand in inventory. In prose, a manuscript abbreviation stays an abbreviation even where its expansion is obvious.

Diagrams must be fully drawn in `\diagram{\begin{tikzcd}[ampersand replacement=\&]...\end{tikzcd}}`, including objects, arrow directions/decorations, labels and struck portions. Drawings must be reproduced in TikZ inside `\figure{...}`. Do not substitute verbal descriptions. Small separator strokes also belong to the inventory.

Use `\unsure{reading}` or `\unsure{reading|alternative}` only when ink remains doubtful, first candidate the strongest visual reading. Retain all supported alternatives. A recurring ambiguous alphabet/sign is marked at its first occurrence on EACH page and recorded in notation; later same-page occurrences use its first candidate. `\illegible{n}` is only for physically unreadable WORDS after crop, never for a mathematical symbol. No doubt mark is permission to omit ink. Distinguish prime from exclamation, i from j, stars from dots, arrows from plain lines, and underlining from descenders.

## Files to write

Your assigned private directory is `result/records/scanNNN/R/`, where R is your designated A, B or C. Write `reading.tex`, `report.json`, and optional readable `report.md` there. Save crops under `result/crops/scanNNN/R/`; use descriptive filenames. Do not modify shared notation, consolidated pages or any other reader’s files.

`report.json` must contain:

- `scan`, `reader`, `complete` (true only after full visual reading), `viewed` (whole/a/b paths, each once), `reading_file`.
- `differences`: every reading/state/placement/punctuation difference from C or H, each with `place`, `C`, `H`, `final`, `differs_C`, `differs_H`, `evidence`, `confidence` (high/medium/low), `kind`, `marked_in_H`, `crop` (relative result path, or null if the half settles it), `bbox` (whole-image pixels, where useful). C’s doubt resolved or retained is explicitly recorded; syntax-only macro differences are not differences. H’s expanded abbreviations and omitted underlines/deletions are substantive.
- `unresolved`: place, reading, alternatives, confidence, reason; list every remaining `\unsure`/`\illegible`.
- `inventory`: one object per text block, display, diagram, drawing, margin note, insertion and deletion: `sheet_kind`, `hand`, `element`, `kind`, `position`, `first_words_or_objects`, `transcribed` (yes). Allowed sheet kinds: text, reused_typed, typescript, letter, list, cancelled_draft, cover. Allowed element kinds: text, display, diagram, drawing, margin note, insertion, deletion.
- `notation`: signs/alphabets/abbreviations to add or compare; include scan/place and visual grounds.
- `abbreviations`: written form and possible expansion (expansion is only in this list).
- `notes`: short English account of what this page states/computes/asks; its own explicit uncertainty with exact phrases; page/date/title evidence; math-triggered reading decisions. Do not claim to prove a statement merely by transcribing it.
- `check_events`: actual mathematical checks, with statement id, type, outcome and method. Allowed types: targeted proof check; independent re-proof; computation or formal certificate; used and rechecked in this run; carried as background without fault found; refuted, with the refined statement’s id. State if no proof was attempted.
- `crops`: path, bbox, rotation, scale/output size, and reason for each crop; `workflow_feedback`: what in this brief needs improvement.

Return a short message giving your report paths and the main disputed readings. Do not wait for the other readers. You are finished after this one page.

## Clarifications introduced after scan 170

- These sheets are continuations of a handwritten letter by Grothendieck (the final page includes its closing). Use sheet_kind `letter` and hand `his hand` for the main writing; separately identify archive pencil or uncertain additional hands.
- H’s preamble explicitly uses `\emph` for the author’s own emphasis. Treat H `\emph` and our `\uline` as equivalent when scope agrees. `\uncertain` is a doubt mark, not author underlining. H `\note` explaining an abbreviation does NOT itself mean H marked the reading doubtful.
- Report `line_coverage`: one short entry per actual manuscript line with its beginning/end or compact reading, confirming C and H were compared. Number main handwritten baselines from the top; number additions by the destination line. This is a coverage record, not a second transcription or a claim of mathematical proof.
- Your private filename is always `reading.tex`; record C’s original page filename as metadata. The main reader writes the final page under C’s original filename.
- Use the exact `kind` values required for H collation: misread word; misread symbol or index; omission; text not on the page; deletion state (struck given live or live given struck); insertion or placement; abbreviation expanded or spelling modernised; readable ink left as `\ill{}`; drawing or diagram; other. Use `other` for punctuation, paragraphing and uncertainty-only changes.
- A new sentence on a new line does not alone establish a paragraph. Examine indentation, unusual blank space, separators and how fully the preceding line is filled. Do not use a change of subject as an ink fact.
- Inspect comma tails versus points and dots after parentheses; compare their darkness and shape with copy grain. If you identify an isolated nontext mark, reproduce it without assigning an unsupported word or meaning, and give its physical position. Distinguish a continuous stroke from isolated reproduction specks.
- Do not crop a clear half-reading merely to document it. The main reader will make a crop if adjudication requires one. Do crop unresolved doubts and consequential small signs. Record all crops made.
- For check_events, reading an assertion is not proving or rechecking it. If there was no mathematical check, an empty array is correct. A local source/target consistency check may be recorded with its deliberately narrow scope.

## Clarifications introduced after scan 171

- A physically separate short stroke is distinct from an ordinary line-end hyphen. Locate each before adding it to the inventory. Reproduce a coherent nontext stroke without inventing its function. Do not promote faint copy grain to manuscript ink. A compact isolated point may remain of uncertain origin; if reproduced, distinguish that physical mark from an inferred sentence full stop, and record the uncertainty.
- A change from one TeX hyphen to two is not itself a collation difference when both represent the same single handwritten punctuation stroke. Report any actual difference in number, placement or reading of marks; keep mere typesetting choices out of counts.
- Crop views must actually be visible. If an image result is truncated or fails to display, document the failure and display the same saved crop successfully; do not make a replacement crop or claim the failed display was an inspection.

## Clarifications introduced after scan 172

- In report crop paths use `crops/scanNNN/R/name.png`, relative to result/, not `result/crops/...`. Keep each noncontiguous quoted expression as its own place rather than grouping several line numbers into one change row.
- If H marks the same preferred reading uncertain, our explicit spelling-out of an alternative alone is not a substantive H difference. Record that retained doubt in the doubt review, without an H collation row. Resolving the uncertainty, changing the preferred reading, or changing a word/mark remains a difference.
- Distinguish uncertainty about a point’s visible shape/presence from uncertainty about its intended role. A clearly distinct inline point can be transcribed literally without claiming a sentence boundary. A nontext point beside a formula must not become a multiplication sign or index. Reproduce such a mark in TikZ using the prescribed figure macro inside a small zero-width inline parbox/raisebox at its anchor, with coordinates and uncertain origin recorded. Do not create a new macro or promote ordinary copy grain to ink.
- One complete insertion can be a content entry, with its attachment as a separate placement entry. Do not also count each resolved sub-doubt as a duplicate content change unless it is a genuinely separate place; still review every C doubt explicitly.

## Clarifications introduced after scan 173

- Distinguish physical position from inferred writing chronology. A smaller cancelled phrase below a normal baseline does not by itself make the live words above it insertions. Use a caret, attachment stroke, replacement alignment or other visible evidence; otherwise preserve the normal live baseline and anchor the cancellation at the phrase above its physical location, adding a brief position comment. Do not move a subline cancellation to a more grammatical point.
- Report `viewed` consistently as an object with keys `whole`, `a`, `b`, each containing `path` and `count: 1`. This is a record of actual successful inspections, not a default to fill before viewing.

## Clarifications introduced after scan 174

- A physical word-continuation hyphen at the page foot is recorded in a comment. End the visible fragment without that hyphen and with a percent sign suppressing whitespace (for example para%). Do not complete it from another page. The main reader handles the joined page seam; every page marker line also ends with a percent sign. This does not apply to lexical compound hyphens.
- H’s editorial note is a doubt mark only if it actually expresses uncertainty about the reading. A note merely describing marginal placement does not count as marked_in_H=yes.
- A low loop within cancellation may belong to a live descender above it. Where those possibilities remain inseparable, retain a supported letter only as doubtful and state the geometric alternative in the report; do not turn an editorial explanation into manuscript text.
- Use abbreviation objects with keys written and expansion. Report all forms encountered, with expansions only in that list.

## Clarifications introduced after scan 175

- Count prose/main text baselines as L1, L2, etc. Number diagram object rows and label rows separately as D1, D2, etc.; do not let a diagram change the count of later prose baselines. Give additions the destination line plus a suffix. Record every diagram label even when it occupies its own row.
- For isolated nontext marks, a structurally reviewed zero-width pattern is a raisebox with explicit zero height and depth containing a zero-width parbox, the required figure macro, and an overlay TikZ picture. It may sit within one uninterrupted math span where needed. Record the physical coordinates and approximate anchor; do not split or change the mathematical formula to assign the mark a meaning. The main reader will normalize the wrapper. Do not run TeX to test it.
- Record an underline’s physical endpoint in the evidence when it falls within a symbol’s horizontal extent; do not silently decide its scope by grammar. Distinguish the observed ruled span from an interpretation of emphasis.

## Clarifications introduced after scan 176

- In the L1, L2 sequence count displayed formula baselines as main baselines too; keep diagram object/label rows in the separate D sequence. A two-line display contributes two main baselines.
- Supply an explicit `C_doubt_review` array with every supplied question, its decision (resolved/retained/confirmed), final reading and ink evidence. Duplicate questions about one physical place share a single crop and one substantive change row.
- A recurring alphabet doubt may extend across prose, operators and diagram labels, but decide each new form from its own visible strokes before treating it as the same form. Do not propagate case merely because the mathematical function is the same. When the forms agree, mark the first occurrence on the page and use its preferred candidate thereafter; record every witness difference.
- Keep H editorial claims in a separate notes field. An incorrect explanatory page-location note is not an additional manuscript collation row when H already puts the same diagram at the same transcription location. Actual omitted or misplaced manuscript content remains a collation difference.
- Letter headings, closing lines and signatures preserve their manuscript line endings with `\\`, as required by the inherited conventions. Ordinary running prose follows normal paragraph flow.
- The required large crop of a tiny mark may add no source detail. Record that limit honestly, inspect the saved crop once, and do not recrop merely to obtain a more attractive display.

## Clarifications introduced after scan 177

- Where a smaller interlinear parenthesis has no caret or guide fixing its attachment, preserve its physical upper-before-lower order in the text, document its position in a comment and inventory, and explicitly retain attachment uncertainty. Do not move it solely to obtain smoother prose. Normal baseline words are not insertions merely because an interlinear qualification occurs nearby.
- Supplied C questions and H notes may quote or mention an English version or other pages. These are earlier editorial comments only, not evidence. Do not consult any external text or other-page image, and do not use translated wording to choose the French ink.
- For every saved crop, report the actual rectangle used as bbox; if additionally giving the smaller feature rectangle or point coordinates, label them separately. The main reader must be able to reuse the existing file without recropping.

## Clarifications introduced after scan 178

- The lack of an alternative word does not settle faint letters. Retain a one-reading uncertainty where parts of the preferred word remain physically insecure; identify the faint strokes. Conversely, resolve readable portions of a cancellation word by word rather than giving the whole phrase one blanket certainty.
- Distinguish visible point count from punctuation function. Two clear stops after an abbreviation may be preserved literally without assigning a second sentence stop; a detached point outside the line may be drawn without an interpretation. Give coordinates so that points noticed by only one reader can be compared.
- Tracing shafts and heads to read a diagram is visual transcription, not by itself a mathematical proof check or a used-and-rechecked event. Put it in ink evidence. Only an actual mathematical deduction or verification receives a narrowly scoped mathematical check event; record source assertions as carried background.

## Clarifications introduced after scan 179

- Author page numbers and archive pencil numbers belong in the inventory, not in the L baseline sequence. Main prose/formula baselines use L; additions use the destination line plus a suffix; diagrams use D.
- For superposed articles, distinguish the visible letter shapes from their chronological assignment. Give a preferred old/live order only with stroke evidence, retain supported alternatives for each layer, and explicitly state any uncertain chronology. A single inventory entry can document the complete overwritten site; do not add a separate insertion wrapper solely because it is a correction.
- A raised replacement may descend toward the following baseline. Describe the actual alignment and any guide/caret before deciding its scope. If placement itself remains ambiguous, record that doubt separately from uncertainty in the letters; do not use grammar to settle either.
- Keep the line-coverage ledger consistent with the final reading: a mentioned comma or letter must actually appear there or be documented as rejected after the crop. A reporting slip is not manuscript ink.
- Combine content and attachment decisions for one contiguous replacement in one substantive difference row, with sub-doubts in C_doubt_review. Separate physical signs such as opening and closing delimiters may remain separate places.


## Clarifications introduced after scan 180

- A supplied C question may itself assert a reading. Treat its wording as the earlier reader’s proposal, never as a confirmed answer. Inspect the letters independently and retain a third supported reading when the strokes require it; neither witness’s candidate list is exhaustive.
- In a cancellation, assess the letter body and any accent separately. If an a-like loop survives but an accent cannot be separated from crossing ink, do not silently impose à from syntax. State supported accented and unaccented alternatives and their preferred order.
- Distinguish a point at the inline writing level from an off-line nontext mark. A literal point does not assert a sentence boundary; a TikZ drawing does not establish authorship. Give whole-image coordinates, the nearest text anchor and its above/below/left/right relation. Uncertain origin alone need not create a doubtful word when the physical shape is clear.
- Tiny features still follow the requested few-thousand-pixel crop workflow; no lower-resolution exception is introduced. Record when enlargement adds no new source information. Incidental adjacent context can overlap a crop of a different target, but do not make a second crop of the same physical target.


## Clarifications introduced after scan 181

- If an underline starts inside the second or later letter of a word, record its literal covered-letter span and both physical endpoints. Do not silently extend it to the whole word. Keep uncertain intended semantic emphasis separate from clear physical stroke extent.
- Choose the one tight crop rectangle from the half view so that the target word’s ascender tips and diacritics are included. If the saved crop nevertheless clips part of the target, record the limitation and retain warranted doubt; do not recrop or claim the missing strokes were resolved.
- For several compact spots above a letter, record the actual count and positions. A possible diacritic may be a supported alternative, but do not infer its deliberate use or replace what is visible with the count asserted by an earlier question.


## Clarifications introduced after scan 182

- Distinguish the presence of an accent from its shape. A secure raised mark may still leave acute, grave or circumflex uncertain; describe its strokes rather than resolving the whole word solely because some accent is present.
- A compact mark newly noticed inside an already required crop may be recorded from that saved inspection without another crop. Give its coordinates and distinguish physical presence from origin, hand, or possible association with overwritten ink. Colour alone does not settle that origin.
- A tiny point between exponent letters can have uncertain attachment as well as uncertain shape. If supported by the actual positions, retain a letter-dot/no-operator alternative alongside operator readings. Adding an alternative to an already uncertain unchanged preferred reading does not alone create another substantive witness-change count.
- When H omits an older overwritten layer from its main text but describes the overwrite in a note, record the omitted layer as omission. The note is a doubt mark only if it expresses a reading uncertainty; describing a superposed sign does not by itself do so.
