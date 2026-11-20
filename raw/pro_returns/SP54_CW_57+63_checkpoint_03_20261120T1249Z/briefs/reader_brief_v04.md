# Independent reader brief v04

First used: cote 57, scan 074 (v03 plus the pre-reading task-message addendum below). You read exactly the one page assigned in the task message. You are one of three independent readers. Do not consult another reader's files, messages, findings or images. Do not read earlier or later pages. Your only evidence is this page's three supplied images, its C and H extracts, its prior C doubts/notes/audit extract, the supplied macro definitions, and the current notation-table snapshot. No web research, OCR, PDF text recognition or text-recognition libraries. Use image viewing to read the ink.

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

Emit no more than three crop images in one tool result to avoid output truncation. If an image is explicitly discarded by the tool output limit, record that delivery failure and resend the existing image; do not remake the crop or count an unseen discarded output as visual inspection.
