# Reading workflow

Each page is assigned in the requested order to three newly spawned agents with no inherited conversation or earlier-page images. Each receives a page-specific directory containing only that page’s image paths, C and H extracts, prior C questions, supplied preamble, current brief and notation snapshot. Readers cannot consult each other. The main reader compares their complete returns, inspects the cited crops and makes a tight crop for remaining adjudication places without a reader crop. A page is written and its logs updated before the next page is assigned.

The original page and supplied halves are viewed once each by each reader. Crop metadata records source pixels, bounding box, scale and any rotation. The main reader retains returns and adjudication crops. No OCR or external research is used. Reader reports record any departures or remaining uncertainty.

## Reader runs and crop counts

| Page | Brief | R1 crops | R2 crops | R3 crops | Main-reader new crops | Total crops |
|---|---|---:|---:|---:|---:|---:|
| A57-02_57_scan022 | v01 | 9 | 7 | 7 | 4 | 27 |
| A57-02_57_scan023 | v02 | 1 | 1 | 1 | 1 | 4 |
| A57-02_57_scan073 | v03 | 3 | 5 | 3 | 6 | 17 |
| A57-02_57_scan074 | v04 | 10 | 11 | 10 | 10 | 41 |
| A57-02_57_scan075 | v05 | 5 | 4 | 4 | 3 | 16 |
| A57-02_57_scan076 | v05 | 5 | 5 | 6 | 2 | 18 |
| A57-02_57_scan077 | v06 | 19 | 20 | 16 | 2 | 57 |
| A57-02_57_scan078 | v07 | 11 | 11 | 12 | 5 | 39 |
| A57-02_57_scan079 | v08 | 7 | 6 | 7 | 4 | 24 |
| H63-01_63_scan003 | v09 | 5 | 5 | 5 | 0 | 15 |
| H63-01_63_scan004 | v09 | 0 | 0 | 0 | 0 | 0 |

## Brief changes and the observations behind them

### v02 — first used on A57-02_57_scan023

- All three scan-022 readers counted author-emphasis macro syntax as a difference; two counted an identity handwritten wrapper and one the archive reference marker. Explicit macro correspondences now exclude those rows.
- Scan-022 readers differed about live versus cancelled overtypes and about recoverable superposed ep/pe. The brief now separates character identity, layer recovery and cancellation state.
- The main reader needed coordinates for half-settled H differences. Coordinate boxes are now explicitly required.
- Three separate cohomology index positions were bundled by R1; they are now requested as individual collation places.
- Corrected doubled backslashes in the prose examples; PREAMBLE.tex always supplied the actual single-backslash commands.

### v03 — first used on A57-02_57_scan073

- Two scan-023 readers put firm prior spelling flags into the in-text C-doubt list. The brief now separates prior_flags from actual uncertainty macros.
- One scan-023 reader found superposed n/f in the context of the deletion crop. The brief explicitly permits using that existing context and requires deleted-before-live order in each alternative.

### v04 — first used on A57-02_57_scan074

- Two main-reader crop images on scan 073 were discarded by an output-size limit. Each scan-074 reader received the three-image batch limit in its initial task message, supplementing v03; the combined brief is preserved here as v04.

### v05 — first used on A57-02_57_scan075

- The three scan-074 complete readings preserved five spacing differences that their tables omitted; prose/math and punctuation spacing is now explicit.
- A scan-074 reader marked confident H editorial notes as doubts. h_marked now explicitly requires an uncertainty indication.
- Scan-074 readers differed on whether a heavy X settled a doubled alphabet; the distinction between visible double impression and alphabet identification is explicit.

### v06 — first used on A57-02_57_scan077

- A three-image result discarded R1's third scan-076 crop. The brief now recommends one image per output, at most two small images.
- R3 counted H cdot versus bullet on scan 076 despite both encoding the same visible raised filled point. This correspondence is now explicit.

### v07 — first used on A57-02_57_scan078

- All three scan-077 readers gave 1 after Corollary, while the main crop exposed a detached lower point leaving 1/! open. Heading numerals and punctuation now receive explicit attention.
- Scan-077 readers supplied title/date metadata as a dictionary rather than the note-section list used in assembly. The list form is now explicit; the main record preserves all values.

### v08 — first used on A57-02_57_scan079

- Scan-078 readers varied between a closed marginal oval and an open arc; root also preserved the opening in the finite-morphism enclosure. Placement and visible gaps in drawing strokes are explicit.
- Readers disagreed on the extra character after or and on wheter/whether. The brief now emphasizes independent character/cancellation alternatives and visible typewriter positions.

### v09 — first used on H63-01_63_scan003

- Scan-079 readers differed on the interpretation and drawn representation of the noetherian correction. The complete path and paragraph continuity are now explicit.
- R3 exposed a new small-index uncertainty in the cancelled-word crop; the brief emphasizes reporting such context findings.
- The H extract included a section explicitly assigned to the following page. The boundary clarification sent to all three readers is retained as a general instruction.

## First reader brief

# Independent reader brief v01

First used: cote 57, scan 022. You read exactly the one page assigned in the task message. You are one of three independent readers. Do not consult another reader's files, messages, findings or images. Do not read earlier or later pages. Your only evidence is this page's three supplied images, its C and H extracts, its prior C doubts/notes/audit extract, the supplied macro definitions, and the current notation-table snapshot. No web research, OCR, PDF text recognition or text-recognition libraries. Use image viewing to read the ink.

## Reading workflow

1. Record your start UTC, model/run identity, and effort as exposed; do not invent an effort setting.
2. Read page.json, C.tex, H.tex and prior.md. H's status is explicit: where hua_has is desc, its note is background description only, with no H textual collation rows. Read the notation snapshot and PREAMBLE.tex. Your page must be complete even when H has no transcription.
3. View the whole image exactly once for layout. Identify every text block, display, diagram, drawing, margin, insertion, deletion, heading, signature and page number. Then view half_a exactly once and half_b exactly once, at their supplied resolution, line by line against C and H. Read every agreed word and glyph from the ink too; agreement between witnesses settles nothing. Keep an ordered line-by-line coverage record in observations.md. Images may be opened via tools.view_image, forwarding the image with image(). Do not reread a whole image or half.
4. List every place still open after the halves: an unresolved witness difference, each C doubt mark, crowded/slanted/struck text, or a mathematically consequential small sign/index that remains uncertain. Crop each such place once tightly, including its word or formula and a line of context. Use the supplied crop.py helper (Pillow only) to enlarge with LANCZOS to a few thousand pixels across, autocontrast, sharpen faint ink and rotate slanted text upright. View each crop once. Never crop a settled place merely to create activity; never make another crop of an already decided place. Record source, coordinates, scaling and rotation. The main reader will decide disagreements using these crops or one new crop where you supplied none.
5. Follow the mathematics as you read. A formula that fails to parse, inconsistent index, sign, inequality or arrow directs attention back to the ink; it never licenses a correction. Preserve the author's exact claim, even a visible slip. Record only the actual mathematical checking you performed, with its calculation or brief justification. Reading/transcribing a theorem is not a proof check. Do not research beyond this page or invent a conditional theorem. Attribute summaries to the page, and distinguish reading evidence from a mathematical check.
6. Write your complete proposed reading.tex, observations.md and report.json in your assigned output directory. Reading.tex may be built by editing C only after every line has been visually read. It must contain every word, symbol, deletion, insertion, note and drawn object in order. Return your file paths and a compact findings summary to the main reader, then finish. Do not await or inspect other readings.

## Diplomatic conventions

- Use only PREAMBLE.tex macros plus standard LaTeX, amsmath/amssymb/mathrsfs, TikZ and tikz-cd. Preserve the page's language, spelling, accents or their absence, punctuation, abbreviations and numbering. Join words split solely at line ends, retain lexical hyphens. Preserve paragraphs; letter headings and closings may retain line breaks.
- Use \\scanpage{N}; visible author/typescript pagination is \\mspage{n}. The archive's corner pencil number is a comment `% archive sheet number: n`. Use \\cotefile{C} only when instructed for the beginning of a cote; main assembly handles it.
- Preserve mathematical alphabets, indices, exponents, bars, hats, tildes, primes, exclamation marks, inequality and arrow direction. A typed double impression is represented by \\mathbb rather than bold where the visible strokes establish it. Determine each glyph from its actual ink, including headings. A notation entry guides comparison but does not predetermine a new glyph.
- \\handwritten{...} marks handwritten additions on typed pages around the handwritten portion only. \\deleted{...} preserves legible struck/typed-over material; \\inserted{...} follows the actual caret/arrow attachment; \\margin{...} preserves independent marginal notes. Underlines are \\uline and \\uuline; mathematical underlines may use \\underline.
- \\unsure{reading} or \\unsure{reading|alternative} retains uncertainty in place. First reading follows the strokes, never the expected result. Use \\illegible{n} only for physically unreadable words after the tight crop, never a formula/diagram symbol. For a recurring ambiguous glyph, mark its first occurrence per page and list every supported candidate in the notation table. Decide every C doubt explicitly, including retained doubt.
- Render diagrams in \\diagram{\\begin{tikzcd}[ampersand replacement=\\&]...\\end{tikzcd}} with \\& separators; reproduce drawings in \\figure{\\begin{tikzpicture}...\\end{tikzpicture}}, including shapes, placement and all labels. Do not substitute a description. Include struck parts. Only a genuinely complex picture may carry `% crop-candidate: scan N` after its best drawn approximation.
- Displays use \\[...\\]; multiline displays use aligned; retain written labels with \\tag*. Preserve his double quotation marks as two backticks and two apostrophes, using guillemets only where drawn.
- Fully transcribe typed sheets, copied manuscripts, letters by others, lists and covers. Printed headings are text; stamps are comments. Put authorship in inventory, avoiding attribution stronger than the evidence supplies.

## Required report.json structure

An object with page, cote, our_scan, reader, start_utc, end_utc, model, effort, images_viewed (three paths), crops (list of file/source/bbox/rotation/purpose), coverage (all_lines_read, all_elements_included, concise block list), changes, c_doubts, remaining_doubts, inventory, notes, notation, abbreviations, check_events.

changes: one object per reading difference from either witness, excluding equivalent macro syntax. Fields: id, place, c (exact C reading), h (exact H reading or null for desc), reading (your exact proposed text), differs_c, differs_h, kind, h_marked (yes/no/not applicable), confidence (high/medium/low), scan_shows (actual strokes/letters/marks), evidence (half or crop path and coordinates), crop (path or null), mathematical_consequence (brief or null). Keep omissions, cancelled/live state, placement, punctuation and spelling differences distinct when they concern distinct places. H's editorial notes do not become page text. A missing drawn item needs its own row.

Allowed kind values: misread word; misread symbol or index; omission; text not on the page; deletion state; insertion or placement; abbreviation expanded or spelling modernised; readable ink left as \\ill{}; drawing or diagram; other.

c_doubts: every C uncertainty, including unchanged marks. Fields: place, c, reading, status (resolved/retained/revised), evidence, crop, confidence. Every changed doubt also appears in changes.

remaining_doubts: place, reading, alternatives, confidence, reason, crop.

inventory: every visible element top to bottom, including separate insertions/deletions/displays/diagrams/drawings/marginal notes. Fields: sheet_kind, hand, element, kind, position, first_words_or_objects, transcribed (yes). sheet_kind is text/reused_typed/typescript/letter/list/cancelled_draft/cover. kind is text/display/diagram/drawing/margin note/insertion/deletion. hand is his hand/another named or unnamed hand/typewriter/print as supported; specify name only with adequate supplied evidence.

notes: summary (what this page states, computes or asks), reading_decisions (only decisions prompted by mathematics, with exact place/readings/reason), author_checks (his own uncertainty/check words quoted exactly), titles_dates_pagination (as present). Summaries describe the page, without claiming proof verification.

notation: sign, latex, place, visible_shape, alternatives; list additions or page evidence for current notation. abbreviations: abbreviation, proposed_expansion, place (expansions never enter the transcription).

check_events: one row per mathematical statement actually checked, used or refuted, with statement_id, date, who, type, outcome, evidence. Allowed types: targeted proof check; independent re-proof; computation or formal certificate; used and rechecked in this run; carried as background without fault found; refuted, with refined statement id. An empty list is proper when no mathematical check occurred. Do not claim a proof check for transcription, inventory or witness comparison. When you use a fact for a reading decision, record the precise check or its background status.

## Last reader brief used

# Independent reader brief v09

First used: cote 63, scan 003. You read exactly the one page assigned in the task message. You are one of three independent readers. Do not consult another reader's files, messages, findings or images. Do not read earlier or later pages. Your only evidence is this page's three supplied images, its C and H extracts, its prior C doubts/notes/audit extract, the supplied macro definitions, and the current notation-table snapshot. No web research, OCR, PDF text recognition or text-recognition libraries. Use image viewing to read the ink.

## Reading workflow

1. Record your start UTC, model/run identity, and effort as exposed; do not invent an effort setting.
2. Read page.json, C.tex, H.tex and prior.md. H's status is explicit: where hua_has is desc, its note is background description only, with no H textual collation rows. Read the notation snapshot and PREAMBLE.tex. Your page must be complete even when H has no transcription.
3. View the whole image exactly once for layout. Identify every text block, display, diagram, drawing, margin, insertion, deletion, heading, signature and page number. Then view half_a exactly once and half_b exactly once, at their supplied resolution, line by line against C and H. Read every agreed word and glyph from the ink too; agreement between witnesses settles nothing. Keep an ordered line-by-line coverage record in observations.md. Images may be opened via tools.view_image, forwarding the image with image(). Do not reread a whole image or half.
4. List every place still open after the halves: an unresolved witness difference, each C doubt mark, crowded/slanted/struck text, or a mathematically consequential small sign/index that remains uncertain. Crop each such place once tightly, including its word or formula and a line of context. Use the supplied crop.py helper (Pillow only) to enlarge with LANCZOS to a few thousand pixels across, autocontrast, sharpen faint ink and rotate slanted text upright. View each crop once. Never crop a settled place merely to create activity; never make another crop of an already decided place. Record source, coordinates, scaling and rotation. The main reader will decide disagreements using these crops or one new crop where you supplied none.
5. Follow the mathematics as you read. A formula that fails to parse, inconsistent index, sign, inequality or arrow directs attention back to the ink; it never licenses a correction. Preserve the author's exact claim, even a visible slip. Record only the actual mathematical checking you performed, with its calculation or brief justification. Reading/transcribing a theorem is not a proof check. Do not research beyond this page or invent a conditional theorem. Attribute summaries to the page, and distinguish reading evidence from a mathematical check.
6. Write your complete proposed reading.tex, observations.md and report.json in your assigned output directory. Reading.tex may be built by editing C only after every line has been visually read. It must contain every word, symbol, deletion, insertion, note and drawn object in order. Return your file paths and a compact findings summary to the main reader, then finish. Do not await or inspect other readings.

## Diplomatic conventions

- Use only PREAMBLE.tex macros plus standard LaTeX, amsmath/amssymb/mathrsfs, TikZ and tikz-cd. Preserve the page's language, spelling, accents or their absence, punctuation, abbreviations and numbering. Join words split solely at line ends, retain lexical hyphens. Preserve paragraphs; letter headings and closings may retain line breaks.
- Use \scanpage{N}; visible author/typescript pagination is \mspage{n}. The archive's corner pencil number is a comment `% archive sheet number: n`. Use \cotefile{C} only when instructed for the beginning of a cote; main assembly handles it.
- Preserve mathematical alphabets, indices, exponents, bars, hats, tildes, primes, exclamation marks, inequality and arrow direction. A typed double impression is represented by \mathbb rather than bold where the visible strokes establish it. Determine each glyph from its actual ink, including headings. A notation entry guides comparison but does not predetermine a new glyph.
- \handwritten{...} marks handwritten additions on typed pages around the handwritten portion only. \deleted{...} preserves legible struck/typed-over material; \inserted{...} follows the actual caret/arrow attachment; \margin{...} preserves independent marginal notes. Underlines are \uline and \uuline; mathematical underlines may use \underline.
- \unsure{reading} or \unsure{reading|alternative} retains uncertainty in place. First reading follows the strokes, never the expected result. Use \illegible{n} only for physically unreadable words after the tight crop, never a formula/diagram symbol. For a recurring ambiguous glyph, mark its first occurrence per page and list every supported candidate in the notation table. Decide every C doubt explicitly, including retained doubt.
- Render diagrams in \diagram{\begin{tikzcd}[ampersand replacement=\&]...\end{tikzcd}} with \& separators; reproduce drawings in \figure{\begin{tikzpicture}...\end{tikzpicture}}, including shapes, placement and all labels. Do not substitute a description. Include struck parts. Only a genuinely complex picture may carry `% crop-candidate: scan N` after its best drawn approximation.
- Displays use \[...\]; multiline displays use aligned; retain written labels with \tag*. Preserve his double quotation marks as two backticks and two apostrophes, using guillemets only where drawn.
- Fully transcribe typed sheets, copied manuscripts, letters by others, lists and covers. Printed headings are text; stamps are comments. Put authorship in inventory, avoiding attribution stronger than the evidence supplies.

## Required report.json structure

An object with page, cote, our_scan, reader, start_utc, end_utc, model, effort, images_viewed (three paths), crops (list of file/source/bbox/rotation/purpose), coverage (all_lines_read, all_elements_included, concise block list), changes, c_doubts, remaining_doubts, inventory, notes, notation, abbreviations, check_events.

changes: one object per reading difference from either witness, excluding equivalent macro syntax. Fields: id, place, c (exact C reading), h (exact H reading or null for desc), reading (your exact proposed text), differs_c, differs_h, kind, h_marked (yes/no/not applicable), confidence (high/medium/low), scan_shows (actual strokes/letters/marks), evidence (half or crop path and coordinates), crop (path or null), mathematical_consequence (brief or null). Keep omissions, cancelled/live state, placement, punctuation and spelling differences distinct when they concern distinct places. H's editorial notes do not become page text. A missing drawn item needs its own row.

Allowed kind values: misread word; misread symbol or index; omission; text not on the page; deletion state; insertion or placement; abbreviation expanded or spelling modernised; readable ink left as \ill{}; drawing or diagram; other.

c_doubts: every C uncertainty, including unchanged marks. Fields: place, c, reading, status (resolved/retained/revised), evidence, crop, confidence. Every changed doubt also appears in changes.

remaining_doubts: place, reading, alternatives, confidence, reason, crop.

inventory: every visible element top to bottom, including separate insertions/deletions/displays/diagrams/drawings/marginal notes. Fields: sheet_kind, hand, element, kind, position, first_words_or_objects, transcribed (yes). sheet_kind is text/reused_typed/typescript/letter/list/cancelled_draft/cover. kind is text/display/diagram/drawing/margin note/insertion/deletion. hand is his hand/another named or unnamed hand/typewriter/print as supported; specify name only with adequate supplied evidence.

notes: summary (what this page states, computes or asks), reading_decisions (only decisions prompted by mathematics, with exact place/readings/reason), author_checks (his own uncertainty/check words quoted exactly), titles_dates_pagination (as present). Summaries describe the page, without claiming proof verification.

notation: sign, latex, place, visible_shape, alternatives; list additions or page evidence for current notation. abbreviations: abbreviation, proposed_expansion, place (expansions never enter the transcription).

check_events: one row per mathematical statement actually checked, used or refuted, with statement_id, date, who, type, outcome, evidence. Allowed types: targeted proof check; independent re-proof; computation or formal certificate; used and rechecked in this run; carried as background without fault found; refuted, with refined statement id. An empty list is proper when no mathematical check occurred. Do not claim a proof check for transcription, inventory or witness comparison. When you use a fact for a reading decision, record the precise check or its background status.


## Clarifications introduced in v02

- Exclude equivalent witness-encoding wrappers from reading counts. The correspondence is explicit: H's `\emph{word}` denotes the author's emphasis, represented by C's `\uline{word}` when the ink is a single underline; C's `\handwritten{symbol}` has the same symbol argument as unwrapped H text and adds provenance only; H's `\page{n}` maps to our scan n+1 by page_map.tsv. The visible underline, hand and archive number must still be checked and inventoried. H's `\supplied{...}` is editorial supply and must be compared with the actual ink, not accepted as source text.
- Preserve overtyped source layers wherever their characters are recoverable. State separately the character reading and its live/cancelled state; when the cancellation state itself remains uncertain, include both states explicitly in `\unsure` rather than dropping the underlying character. Darkness alone does not establish cancellation: identify actual crossing strokes, displaced impressions or superposed letter bodies.
- When the halves settle a difference and no crop is needed by you, provide a tight source-coordinate box in evidence so the main reader can make the required adjudication crop without reopening a half.
- If distinct indices in one expression differ from H, list each position separately; one crop may document the whole short expression.
- Use the brief's required report field names exactly. observations.md should be a concise line/block coverage record, without duplicating the full report.


## Clarifications introduced in v03

- `c_doubts` lists actual in-text C uncertainty macros. Prior prose tables also contain firm readings flagged as spelling slips or mathematical questions. Record those separately in an optional `prior_flags` list; confirming such a flag does not remove a doubt mark and is not a C change.
- Keep separate the clearly recoverable layers of an overtype and the order in which they were applied. Within each alternative, place the deleted layer before the live layer. A crop made for one unresolved place can expose a new issue in its immediate context; record that issue from the existing crop, without recropping it.


## Clarification introduced in v04

Emit one or at most two crop images in one tool result to avoid output truncation. If an image is explicitly discarded by the tool output limit, record that delivery failure and resend the existing image; do not remake the crop or count an unseen discarded output as visual inspection.


## Clarifications introduced in v05

- Compare visible spacing at prose/math boundaries as well as punctuation: attached f-label/is or f-label/via, spaces before punctuation, and crowded inserted letters all belong in the difference record when a witness changes them. A spacing row must not double-count a symbol change already recorded at the same place.
- `h_marked` means an actual uncertainty indication (such as a doubt, question or unreadable marker). A confident editorial note describing a correction or a marginal line is not itself a doubt mark; explain its content separately.
- A heavy typed impression may leave an intended doubled alphabet and an overstruck plain letter unresolved. Record the visible doubled strokes and retain both readings when their separation is unclear; weight alone does not settle the alphabet.


## Clarifications introduced in v06

- A three-image result still discarded a crop on scan 076. Prefer one image per tool result, with two only when small; the resend-without-recropping rule applies to any explicitly unseen output.
- H `f^{\cdot}` and C `f^{\bullet}` map to the same visible filled raised point when the ink establishes that shape. Do not count the macro names as a reading difference. An actual open ring or prime remains a separately judged glyph.


## Clarifications introduced in v07

- Inspect manuscript marks in headings as carefully as formula exponents. A numeral-like upper flag combined with a detached lower point can leave numeral/punctuation alternatives unresolved; expected numbering cannot settle that shape. On scan 077 the main crop retained 1/! although the three readers gave 1.
- Return titles_dates_pagination as a list of strings or of objects with place, text and form, so the visible headings, dates and page counts are retained completely in the assembled notes.


## Clarifications introduced in v08

- Reproduce a visible opening in an oval rather than automatically closing the curve. On scan 078, the marginal oval and the finite-morphism enclosure have small openings. Preserve the side of marginal notes with standard LaTeX placement controls when needed.
- A possible cancellation of one extra character must not force a cancellation of the adjacent live word. Keep character identity and cancellation-state alternatives explicit when the overprint does not separate them.
- In comparing full readings, inspect compact typewriter spellings by their visible character positions; do not let a familiar spelling supply a missing letter.


## Clarifications introduced in v09

- A correction stroke can touch a baseline word while forming part of an insertion bracket. Record the complete path and any uncertain cancellation state; where its shape is material, reproduce the source fragment in TikZ without duplicating its words. Keep a prose paragraph continuous with an inline carrier when possible.
- Report a newly exposed index or glyph uncertainty in a crop's immediate context even when it was not the crop's original target. Read that occurrence from its own strokes, without imposing nearby indices.
- A witness extract may include a following section whose editorial note explicitly names a later page. Respect the assigned page_map boundary; following-page headings are not omissions on the assigned page, and no following image is to be opened.

## What worked; what needed correction

The independent readings exposed disagreements both with the witnesses and between readers. Retaining exact proposed page files makes those disagreements reviewable. Tight crops preserve the visible basis of the main decision. The initial brief needed explicit correspondence rules for equivalent macro wrappers and for archive page references; those rows were removed from the final counts, while the original reader reports were retained.

Heavy typewriter overprinting can establish several underlying letter strokes without establishing the temporal order of the impressions. The final reading retains that uncertainty, including uncertain live/cancelled state. A vote does not determine the reading: the main crop decision can retain uncertainty even when one reader proposed a confident text.

The record-assembly scripts do not infer or recognize source text. They assemble manually adjudicated readings and keep page order, inventory and difference counts aligned. Static delimiter checks do not verify manuscript readings or mathematical truth.

Checkpoint ZIPs include the complete current deliverables and reading documentation, excluding input scans/witnesses and earlier checkpoint archives. They are created only at the requested 45-minute interval.

## Recorded delivery and comparison details

Cote 57 scan 073: two crop image outputs (s_morphism, continuation) were discarded by the tool output limit in a six-image batch. The existing crops were resent and first visually inspected in the next call; no new crop was made and no decision was made before the images were visible. Subsequent main-reader image batches are limited to three images.

Scan 075: R1 preserved typed page 3 in its complete reading but omitted the corresponding H-omission row. The main union added that row from R2/R3 and checked the pagination crop. The existing brief already requires page numbers; no new brief version was needed.

Scan 076, R1: a three-image result discarded its third crop (overtyped_to.png). R1 resent the unchanged file alone and inspected it once. The reader reported the event explicitly; no crop was regenerated. The three-image ceiling did not prevent this output-size discard.

Scan 076, main reader: the first attempted delivery of deleted_continuation.png and 06_handwritten_m.png was wholly truncated at a context limit; neither image reached the reader. The two existing files were then resent individually and first inspected. The same discarded-result call had successfully created proofsbeing.png and is_space.png; those existing crops were each first viewed individually. No crop was regenerated.

Scan 077: all crop outputs reached the main reader individually. R1/R3 preserved the space after the Pic formula; R2 did not. The full-text comparison exposed that difference. R1 alone recorded a possible point after u; the main crop retained it as uncertain. The main heading crop introduced 1/! uncertainty after Corollary despite three numeral-1 readings. No already settled place was recropped.

Assembler robustness: note sections supplied as dictionaries now retain their key/value contents, including nested lists, instead of rendering only the keys. Completed page-077 title/date metadata was explicitly normalized to the list format before assembly. Earlier completed records used lists or a string in these sections and were unaffected.

- Scan 63/003: the first root delivery of R1/01_entry3.png was explicitly discarded for context/output limits. The same existing crop was resent successfully; no second crop was made and only the successful delivery counts as a root view. All four adjudication crops were then viewed one per result.
