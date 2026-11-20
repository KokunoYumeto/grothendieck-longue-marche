# SP50_CW_134-1+134-2 — Reading workflow

Each page was assigned in source order to three new independent sub-agents with fork_turns="none". No agent was given another reader’s return. Each received only this page’s witness extracts, images and earlier C questions, the controlling conventions, the current brief, and a frozen notation snapshot. The main reader retained their returns and inspected tight evidence crops for adjudication. The full individual reading, image-view log, evidence and reasoning are retained in readers/ and evidence/. Model names and exposed effort information are recorded in each report; effort is not invented where the runtime did not expose it.

No OCR, text recognition, PDF text layer, external archive, internet research or other reproduction was used. The supplied original images and witnesses are omitted from this return; cropped evidence is newly generated documentation, with source-pixel boxes and processing recorded alongside it. PREAMBLE.tex is included to specify the required macros.

## First reader brief

# Independent page-reader brief v01

First used: cote 134-1, scan 002. You are one of THREE independent readers of ONE page. Start only with the specified packet, the three images it names, this brief, conventions.md, PREAMBLE.tex and the supplied notation snapshot. Do not read other readers’ work, other pages’ text or images, main decisions, or external sources. Do not browse. Do not use OCR, text-recognition software, PDF layers or an external transcription. Do not spawn readers or delegate this page. You are done after returning this page.

## Required reading

a. View the whole image ONCE for layout: every block, display, drawing, diagram, margin, insertion, deletion and page number. Record image dimensions so crop boxes can be stated in source pixels.

b. View each supplied full-resolution half ONCE, sequentially, and read EVERY line against the complete C and H page texts. Agreement of C and H is not evidence: inspect every agreed word and sign too. Check spelling, absent accents, punctuation, word endings, all indices and exponents, direction and decoration of arrows, inequality signs, primes versus exclamation marks, deletion and insertion states, handwriting on type, underlines and marginal additions. Read the complete page; not just witness differences. The halves settle whatever is legible there; do not enlarge an entire half again.

c. List what the halves leave open, including every C doubt mark and every unresolved witness disagreement. Make ONE tight crop for EACH such place (word/formula plus a line of context), enlarge to about 2800 pixels across with LANCZOS, autocontrast and sharpen; rotate slanted writing upright. Use out/scripts/crop.py so coordinates and processing are logged. View the crop. Do not re-crop a decided place; do not crop a reading already settled by the halves. A long note can have separate crops only for genuinely separate unresolved places. Record remaining doubts honestly in place. Inspect dense mathematical symbols with particular care. Expected mathematics may prompt an inspection; only ink settles the transcription.

d. Write the FULL page in the required C macros, plus a structured report of every place differing from C OR H (including doubt resolutions and any uncovered text). Return evidence from a half or a named crop. Include inventory of ALL elements, short mathematical notes, notation observations, abbreviations and residual doubts. Record mathematical check events only for checking actually performed; ordinary reading is NOT a proof check. Your final message gives paths and a short overview; the full record is in your files.

## Conventions and witness interpretation

Read conventions.md and PREAMBLE.tex. Preserve language, spelling, accents or missing accents, abbreviations and punctuation. No modernization or silent mathematical repair. Use \deleted, \inserted, \margin, \uline, \uuline, \unsure, \illegible, \diagram and \figure as defined. Diagrams must be complete tikz-cd; drawings complete TikZ. No gaps or prose substitutes. Physically unreadable prose can use \illegible{n}; unreadable mathematical glyphs use a best \unsure reading. Mark all genuine uncertainty; do not retain a C doubt if ink settles it. Do not introduce doubt solely because H disagrees. Preserve whole-letter heading/closing line breaks; join prose line wraps and line-end hyphenation. Author page numbers use \mspage; archive pencil foliation is a TeX comment only. Plain guillemets in H may be its house syntax: inspect the actual quote shape.

In H, \uncertain is a doubt, \ill is unreadable, \struck is deletion, \add is insertion, \marginal is margin, \emph generally represents author emphasis. H’s \note, section titles, archive descriptions, editorial expansions and provenance are editorial metadata, not words to import into the transcription. Some H notes record actual ink missed from its body: inspect the page. Ignore pure macro-syntax differences when logging changes; log a difference in actual wording, glyph, decoration, state, placement or uncertainty. H has no text for scan 002: no H-difference rows there. Do not use H’s references to other copies as evidence; only supplied scan ink is authoritative.

## Files and report schema

Write ONLY your assigned reader directory and evidence subdirectory. Use UTF-8. Save reading.tex plus report.json. The report must be valid JSON with these keys:

- reader, page, started_utc, finished_utc; model = your actual exposed model; effort = exposed effort or "not exposed". Do not invent identifiers.
- view_log: ordered list of image paths actually viewed, each with purpose.
- changes: list of objects with `id`, `location`, `c`, `h`, `final`, `against_c` (boolean), `against_h` (boolean), `kind`, `marked_in_H` (yes/no/not applicable), `confidence` (high/medium/low), `evidence` (specific visible strokes), `crop` (relative file path or "half a"/"half b"), `math_consequential` (boolean). Retained C doubt gets a resolution entry with against_c=false, against_h as appropriate. If H has no text, against_h=false.
- doubts: location, reading, alternatives, confidence, reason, crop.
- inventory: list of objects with sheet_kind (text/reused_typed/typescript/letter/list/cancelled_draft/cover), hand, element, kind (text/display/diagram/drawing/margin note/insertion/deletion), position, first_words_or_objects, transcribed="yes". Every independent block and state change gets a row. Archive foliation is covered by a text row describing its comment representation.
- notes: concise English account of claims, questions, dates/pages, the author’s explicit doubt words, and mathematical points that prompted an ink inspection; separate author claims from your checks.
- checks: list of statement_id, type (one of the user’s six check-event types), outcome. Include reasoning for any actual targeted check; otherwise record a statement as carried as background without fault found only if it was actually used as background. Do not falsely label transcription as verification.
- notation: glyph, reading, location, evidence. abbreviations: abbreviation, proposed_expansion. slips: location, written, apparent_intention, reason (only if warranted).
- coverage: a paragraph documenting full line-by-line reading, displays, states, margins and whether either witness omitted ink.

`kind` for H differences is exactly one of: misread word; misread symbol or index; omission; text not on the page; deletion state (struck given live or live given struck); insertion or placement; abbreviation expanded or spelling modernised; readable ink left as \\ill{}; drawing or diagram; other.

Before returning, check that reading.tex is complete and that report changes agree with that reading. Do not substitute a patch or a summary for the full page.


## Last reader brief

# Independent page-reader brief v08

First used: cote 134-2, scan 153. You are one of THREE independent readers of ONE page. Start only with the specified packet, the three images it names, this brief, conventions.md, PREAMBLE.tex and the supplied notation snapshot. Do not read other readers’ work, other pages’ text or images, main decisions, or external sources. Do not browse. Do not use OCR, text-recognition software, PDF layers or an external transcription. Do not spawn readers or delegate this page. You are done after returning this page.

## Required reading

a. View the whole image ONCE for layout: every block, display, drawing, diagram, margin, insertion, deletion and page number. Record image dimensions so crop boxes can be stated in source pixels.

b. View each supplied full-resolution half ONCE, sequentially, and read EVERY line against the complete C and H page texts. Agreement of C and H is not evidence: inspect every agreed word and sign too. Check spelling, absent accents, punctuation, word endings, all indices and exponents, direction and decoration of arrows, inequality signs, primes versus exclamation marks, deletion and insertion states, handwriting on type, underlines and marginal additions. Read the complete page; not just witness differences. The halves settle whatever is legible there; do not enlarge an entire half again.

c. List what the halves leave open, including every C doubt mark and every unresolved witness disagreement. Make ONE tight crop for EACH such place (word/formula plus a line of context), enlarge to about 2800 pixels across with LANCZOS, autocontrast and sharpen; rotate slanted writing upright. Use out/scripts/crop.py so coordinates and processing are logged. View the crop. Do not re-crop a decided place; do not crop a reading already settled by the halves. A long note can have separate crops only for genuinely separate unresolved places. Record remaining doubts honestly in place. Inspect dense mathematical symbols with particular care. Expected mathematics may prompt an inspection; only ink settles the transcription.

d. Write the FULL page in the required C macros, plus a structured report of every place differing from C OR H (including doubt resolutions and any uncovered text). Return evidence from a half or a named crop. Include inventory of ALL elements, short mathematical notes, notation observations, abbreviations and residual doubts. Record mathematical check events only for checking actually performed; ordinary reading is NOT a proof check. Your final message gives paths and a short overview; the full record is in your files.

## Conventions and witness interpretation

Read conventions.md and PREAMBLE.tex. Preserve language, spelling, accents or missing accents, abbreviations and punctuation. No modernization or silent mathematical repair. Use \deleted, \inserted, \margin, \uline, \uuline, \unsure, \illegible, \diagram and \figure as defined. Diagrams must be complete tikz-cd; drawings complete TikZ. No gaps or prose substitutes. Physically unreadable prose can use \illegible{n}; unreadable mathematical glyphs use a best \unsure reading. Mark all genuine uncertainty; do not retain a C doubt if ink settles it. Do not introduce doubt solely because H disagrees. Preserve whole-letter heading/closing line breaks; join prose line wraps and line-end hyphenation. Author page numbers use \mspage; archive pencil foliation is a TeX comment only. Plain guillemets in H may be its house syntax: inspect the actual quote shape.

In H, \uncertain is a doubt, \ill is unreadable, \struck is deletion, \add is insertion, \marginal is margin, \emph generally represents author emphasis. H’s \note, section titles, archive descriptions, editorial expansions and provenance are editorial metadata, not words to import into the transcription. Some H notes record actual ink missed from its body: inspect the page. Ignore pure macro-syntax differences when logging changes; log a difference in actual wording, glyph, decoration, state, placement or uncertainty. H has no text for scan 002: no H-difference rows there. Do not use H’s references to other copies as evidence; only supplied scan ink is authoritative.

## Files and report schema

Write ONLY your assigned reader directory and evidence subdirectory. Use UTF-8. Save reading.tex plus report.json. The report must be valid JSON with these keys:

- reader, page, started_utc, finished_utc; model = your actual exposed model; effort = exposed effort or "not exposed". Do not invent identifiers.
- view_log: ordered list of image paths actually viewed, each with purpose.
- changes: list of objects with `id`, `location`, `c`, `h`, `final`, `against_c` (boolean), `against_h` (boolean), `kind`, `marked_in_H` (yes/no/not applicable), `confidence` (high/medium/low), `evidence` (specific visible strokes), `crop` (relative file path or "half a"/"half b"), `math_consequential` (boolean). Retained C doubt gets a resolution entry with against_c=false, against_h as appropriate. If H has no text, against_h=false.
- doubts: location, reading, alternatives, confidence, reason, crop.
- inventory: list of objects with sheet_kind (text/reused_typed/typescript/letter/list/cancelled_draft/cover), hand, element, kind (text/display/diagram/drawing/margin note/insertion/deletion), position, first_words_or_objects, transcribed="yes". Every independent block and state change gets a row. Archive foliation is covered by a text row describing its comment representation.
- notes: concise English account of claims, questions, dates/pages, the author’s explicit doubt words, and mathematical points that prompted an ink inspection; separate author claims from your checks.
- checks: list of statement_id, type (one of the user’s six check-event types), outcome. Include reasoning for any actual targeted check; otherwise record a statement as carried as background without fault found only if it was actually used as background. Do not falsely label transcription as verification.
- notation: glyph, reading, location, evidence. abbreviations: abbreviation, proposed_expansion. slips: location, written, apparent_intention, reason (only if warranted).
- coverage: a paragraph documenting full line-by-line reading, displays, states, margins and whether either witness omitted ink.

`kind` for H differences is exactly one of: misread word; misread symbol or index; omission; text not on the page; deletion state (struck given live or live given struck); insertion or placement; abbreviation expanded or spelling modernised; readable ink left as \ill{}; drawing or diagram; other.

Before returning, check that reading.tex is complete and that report changes agree with that reading. Do not substitute a patch or a summary for the full page.

## Additions after scan 004

For every changed or reviewed locus, include `source_bbox` in original whole-page pixels, especially where the half settled it and you made no crop. For a locus split across physical lines, give both boxes. The main reader needs these locations to crop witness disagreements without viewing the whole page again. Do not make redundant reader crops.

Assess small isolated dots as possible punctuation versus copying specks; report a meaningful possible mark omitted by both witnesses and keep its intentional status uncertain when necessary. Distinguish a dot above an exponent from a surface fleck; a hook alone does not establish its baseline or dot. Do not infer accents from spelling or dismiss them merely because copied edge marks are nearby. These are inspection prompts, not prescribed readings.

Each entry must identify one place. Adjacent words/states in one crop can have separate entries. Equivalent macro syntax is not a change. Actual quotation shape, underline, insertion, deletion, diagram placement, and index/exponent choices are changes. A note that explicitly gives the same author page number or foliation already supplies an H reading; do not call it omitted merely because it is in a note.

Save final reading.tex and report.json atomically when practical (temporary file, then rename) so timed checkpoints cannot capture a half-written JSON file.

## Additions after scan 005 (first used on scan 006)

Distinguish uncertainty about a word from uncertainty about whether it is deleted: if the letters are readable but the state is doubtful, place the deletion and live alternatives inside the outer unsure macro, with the ink-supported state first. For example, use `\unsure{\deleted{le}|le}` or `\unsure{le|\deleted{le}}`, rather than a definite deletion around an uncertain word. Do not mark the state certain while describing it as uncertain in your report.

A recurring glyph doubt is not a shortcut around inspecting later occurrences: compare their actual strokes separately, then note which instances share the same ambiguity. A comment about a copying artefact is not itself an omitted word or drawing in H.

## Additions after scan 006 (first used on scan 007)

For an alleged addition or deletion across a physical line break, record both end-of-line and next-line boxes. If the halves settle one side, do not crop it redundantly, but explain that the existing crop covers only the other side. A crop filename that mentions a locus does not establish coverage outside its actual box.

## Addition after scan 148 (first used on scan 149)

The exact six permitted check-event types are: `targeted proof check`; `independent re-proof`; `computation or formal certificate`; `used and rechecked in this run`; `carried as background without fault found`; `refuted, with the refined statement's id`. Use a type only for an event that actually occurred, and give the refined statement identifier when refuting. The earlier brief referred to these labels without supplying them; this addition makes the allowed input self-contained. A plain visual reading still is not proof checking, and an empty checks list is appropriate if no such event occurred.

For `marked_in_H`, use yes only when H actually marks the reading as uncertain (for example, its uncertainty macro or an explicit doubt). An editorial note merely acknowledging overwritten letters, an insertion, or a page number is not itself a doubt mark.

When a witness omits several separated words in one construction, log every omitted word or a clearly delimited entry covering the entire construction. A correct full reading is not enough if its difference list omits one of the restored words. Shared evidence may support several separate entries without making redundant crops.

## Addition after scan 150 (first used on scan 151)

A witness’s `--` or `-` may encode a single typeset dash or joining stroke; the number of TeX hyphen characters does not establish the number of handwritten strokes. Inspect the actual shape and position, and log only a substantive difference, not merely a typographic width encoding.

When a marginal note has a guide, bracket or arrow, include the graphic itself in TikZ, as the drawing rule requires. Determine its actual target from the page; do not silently invent a word-level anchor where the guide ends in blank space beside a line. Record the note and guide as separate inventory elements when they are distinct.

## Addition after scan 151 (first used on scan 152)

Equivalent LaTeX forms of the same mathematical relation, such as leq and leqslant for less-than-or-equal, are not by themselves different readings. Inspect every relation, but count a difference only when the actual symbol, its state, a meaningful decoration or its uncertainty differs. A typeface or standard glyph-style choice alone does not create an H error.

Keep reproduced insertion guides in their source vertical order near the relevant added text, with an explicit local attachment comment when needed. Do not move a guide below an entire paragraph merely for encoding convenience. If a possible point belongs spatially inside a guide or drawing, retain its position there instead of silently moving it into baseline prose. Equivalent numerical TikZ scaling is not a substantive reader disagreement.

## Addition after scan 152 (first used on scan 153)

At a crossing or close overlap, distinguish a letter’s ascender or descender from an independent guide. Do not extend or duplicate a guide along a nearby letter stroke merely because their endpoints approach one another. Explain an unresolved junction rather than inventing continuity.

The same handwritten lowercase l may be encoded as l or ell. As with equivalent inequality styles, that typographic choice alone is not a different mathematical letter; inspect the ink for an actual alphabet or symbol difference before counting it.

At a physically clipped page edge, distinguish surviving but incomplete letters from punctuation outside the recoverable image. Keep the clipped word uncertain when necessary, but do not restore a point or comma merely because the word would conventionally take one. Note the edge loss and avoid claiming that the uncut manuscript lacked unseen punctuation.


## Changes to the brief

- after 134-1_scan004, v02 (first used 134-1_scan005): Source boxes were needed for half-resolved changes. Reader disagreements exposed an isolated dot missed by both witnesses, dotted/hooked exponent uncertainty, and differing accent certainty. Added location and small-mark reporting guidance without prescribing readings; added atomic save guidance for timed checkpoints.
- after 134-1_scan005, v03 (first used 134-1_scan006): Readers differed about le cancellation but two encoded certainty of deletion while describing uncertain state. Clarified outer unsure for state alternatives, independent inspection of repeated endings, and exclusion of purely editorial artefact comments from counts; corrected literal collation-kind macro spelling.
- after 134-1_scan006, v04 (first used 134-1_scan007): The disputed extra deletion between d’autres and termes straddled a line break; crop coverage covered only the next-line start, so main adjudication needed a separate end-of-line crop. Require both boxes and explicit coverage. Correct the inherited stale version heading and first-used line.
- after 134-2_scan148, v05 (first used 134-2_scan149): Reader r1 requested exact check-event labels missing from v04; the identical clarification was delivered to all three and is retained as an addendum. Adjudication also corrected an H doubt flag inferred from an editorial overwriting note and added the separated omitted que absent from two difference lists. The new brief enumerates the six event labels, distinguishes physical-state acknowledgment from uncertainty, and requires complete coverage of multiword omissions.
- after 134-2_scan150, v06 (first used 134-2_scan151): Two readers counted H’s -- as two manuscript strokes, although it represents one typographic dash. All three commented on the marginal guide without reproducing it; the main reader drew it and found no exact word anchor. Clarified that TeX dash width alone is not a difference and reiterated graphic reproduction and target evidence.
- after 134-2_scan151, v07 (first used 134-2_scan152): R1 counted two leq/leqslant encoding differences as H symbol errors; these were excluded. All readers drew the guides, but r1/r3 moved the second guide below the whole paragraph, and r3 moved an internal uncertain point into prose. Clarified mathematical style equivalence and source placement of guides and internal marks without changing the crop workflow.
- after 134-2_scan152, v08 (first used 134-2_scan153): R1/r3 extended an insertion guide along the nearby f stem; r2 separated the strokes. R2 counted l/ell as a letter error although it is the same handwritten lowercase letter. Readers differed over conjectural terminal punctuation at the clipped lower edge. Added guidance on junctions, typographic letter equivalence and recoverable edge evidence.

## Crops and completion by page

Counts are actual tight-crop files made in this run, not source halves. A main-reader inspection of an existing reader crop does not add a new crop.

| Cote / scan | Reader 1 | Reader 2 | Reader 3 | Main | Total | Status |
| --- | --- | --- | --- | --- | --- | --- |
| 134-1 / 2 | 1 | 1 | 1 | 0 | 3 | decided |
| 134-1 / 4 | 13 | 13 | 13 | 8 | 47 | decided |
| 134-1 / 5 | 14 | 12 | 11 | 9 | 46 | decided |
| 134-1 / 6 | 12 | 14 | 12 | 4 | 42 | decided |
| 134-1 / 7 | 16 | 13 | 14 | 7 | 50 | decided |
| 134-2 / 146 | 9 | 11 | 9 | 3 | 32 | decided |
| 134-2 / 147 | 7 | 7 | 6 | 8 | 28 | decided |
| 134-2 / 148 | 8 | 6 | 9 | 6 | 29 | decided |
| 134-2 / 149 | 10 | 11 | 11 | 7 | 39 | decided |
| 134-2 / 150 | 16 | 15 | 16 | 4 | 51 | decided |
| 134-2 / 151 | 12 | 12 | 13 | 5 | 42 | decided |
| 134-2 / 152 | 10 | 8 | 9 | 3 | 30 | decided |
| 134-2 / 153 | 10 | 14 | 7 | 0 | 31 | in progress |

## What worked and what did not

- Scan 002: all three full readings agreed. The sole crop per reader isolated the doubtful terminal point; magnification exposed the point but could not establish intention. Retaining doubt was necessary. No defect in the brief caused a disagreement, so v01 remains in force.
- Packet preparation: the first prior-question extraction also selected a few notation rows for other scans because they mentioned the current scan as a comparison. The filter was corrected to the leading scan number during scan 004, and all active readers were told to ignore those cross-reference rows. No extra images were supplied or viewed.
- Scan 004: all three readings were compared at every difference; their certainty/alternatives differed at maître, faute, pens, deux, peut-être and the H exponents. Main inspection retained uncertainty where strokes were lost; pens and the first exponent resolved. The isolated point after pour was seen by r2 and added with doubt after main inspection. Each reader made 13 crops and the main reader made 8 more. Source boxes became required in v02. A naive brace checker produced false alarms at an escaped literal brace and a line break before a closing brace; escape-parity handling fixed the checker, with no transcription change.
- Scan 005: the three independent returns had different confidence in the degree sign, colon, nécessairement, champ(s) endings and classes/données, and different encodings of the article’s deletion state. The main reader inspected fourteen existing r1 crops, two existing r2 crops and nine new crops. The colon resolved; the other uncertain ink was retained with the state uncertainty expressed explicitly. The first attempted delivery of four crop images was truncated by the tool/context boundary before they could be inspected; those existing images were then delivered successfully, without creating replacement crops. The lower-left copied impressions were documented but not counted as a lexical H omission.

## Scan 006

All three independent returns were compared. Main adjudication reused thirteen reader crops and made four missing-locus crops (top strokes, end of d’autres, ensembliste quotes and foliation). The beginning of termes and end of d’autres required separate evidence across a line break; the reader crop alone covered only one side. A tool output containing four crops was truncated before image delivery; those existing files were then viewed in smaller calls, without recropping. One transient execution-server failure was retried successfully. The ornate H was standardized from its inspected loops, while the final object and argument-end marks remained doubtful.

## Scan 007

All three independent readings were compared before main adjudication. The main reader used seventeen existing reader crops and seven new missing-locus crops, including both sides of the missing parenthesis and name punctuation at line breaks. A truncated tool output did not deliver two requested crops; the same files were then displayed individually, without recropping. The literal abbreviation and final verb were resolved; clipped or fused strokes remained doubtful. Isolated raised points were retained as physical observations without inventing textual function. The brief already covered the relevant disagreements, so v04 remains suitable for the next page.

## Scan 146

All three independent full returns were compared. Main adjudication inspected eleven existing crops and made three missing-locus crops (par, nager and the line-start tu). The month crop also covered the distinct year line and the newly reported terminal point. Reader differences concerned certainty of crowded word interiors, accent direction, literal word endings and recovery under cancellation. Both proposed deleted readings are kept explicitly tentative. H’s note already records the est correction and page numbers, avoiding false omission counts. The existing brief addressed these issues, so no revision was needed.

## 134-2_scan147

Three independent returns were compared in full. Main adjudication reused nine reader crops and made eight crops for witness differences already settled by the readers’ halves. The differences among readers concerned qu’une/que une and two possible punctuation loci. Final live words were separated from uncertain underlying layers; H’s editorial correction notes were considered. A tool output containing two main crops was truncated before delivery; those same existing files were retried singly, without recropping or a duplicate actual image view. The existing v04 brief covered all observed issues, so it remains unchanged for the next page.

## 134-2_scan148

All three independent returns were compared. Main adjudication inspected ten existing reader crops and made six missing-locus crops; the first Dold-Puppe joining stroke was already covered by the connector crop. Reader differences concerned word-ending certainty, the function of a short connector stroke and isolated points. The final transcription retains eight doubts rather than choosing by grammatical expectation. H’s note about overwritten letters was not treated as a doubt mark, and its typographic double-hyphen encodings were excluded from change counts. R1 requested the exact check-event labels missing from the brief; the same clarification was delivered to all three readers without sharing readings, and is retained in the page addendum. Version v05 will enumerate those labels and clarify H doubt flags for the next page.

## 134-2_scan149

Three independent returns were compared in full. Main adjudication inspected eleven existing reader crops and made seven missing-locus crops. A failed image-output attempt before context rollover delivered no image; the identical existing inverse-relation crop was retried successfully, not recropped. The disagreements concerned certainty of the inverse relation, an isolated low mark, the raised placement of paired points, and the alternatives for a cancelled oval. All are recorded with the three readings. The inherited inventory description of the inline inverse expression was corrected from display to text. H’s misplaced underline-wave note is counted once, at the second occurrence; identical emphasis macros alone are not a change. No brief revision was required before page 150: v05 already covers these uncertainty and physical-state distinctions.

## 134-2_scan150

All three complete readings were compared before main adjudication. Fourteen existing reader crops were inspected, and four new crops supplied int punctuation, quotation endpoints, and the omitted body-target region beside the marginal guide. The target crop was necessary because all existing rotated note crops stopped inside the margin. The arrow was reproduced in TikZ, retaining its down-right shaft and unequal head strokes without inventing a syntactic insertion anchor. Reader disagreements on invariant, retomber, sur state, two accents, affines punctuation, the final word, and margin placement are recorded explicitly. The sur word/state entries were merged into one delimited locus to avoid double-counting the same crowded cluster. H’s double-hyphen joining dash was reviewed but excluded as typographic encoding; v06 will make that distinction explicit for later readers. A conditional targeted check of the two group-action axioms and a counterexample to a stronger antecedent interpretation were recorded separately from the image readings.

## 134-2_scan151

All three complete readings were compared, including all TeX content differences. The main reader inspected 13 existing reader crops and made five new tight crops for half-settled witness disagreements; all 18 were viewed once, with no failed image delivery. Existing crops covered the first two chain hooks, the closing quotation and multiple adjacent accent questions, so no duplicate crops were needed.

The readers agreed on the hook geometry and the clear word ouvrent, but differed in uncertainty, small accents, possible cancellation, the interlinear opening and the placement of guides/isolated marks. The main decision kept those distinctions explicit. The two leq/leqslant flags from r1 were encoding-only and excluded. The guide shapes were correctly reproduced by all three under v06; r1/r3 placed the second guide after the paragraph in reading order, whereas the source places it above. This motivates a brief reminder about graphic order and maintaining a point’s position inside a graphic. No proof checking is attributed to the readers. The root’s actual degree-shift check is separately recorded.

## 134-2_scan152

All three complete readings, their indexed loci, and their notes/inventories were compared. The main reader inspected eleven existing reader crops and three newly made tight crops, fourteen successful image views in total. An attempted two-image delivery was truncated at a context boundary and neither image was considered viewed; the same existing files were then successfully delivered one at a time, without recropping. The retry is recorded in the main-review journal.

Disagreements concerned uncertainty, accents, the surname, four detached marks, bottom-edge losses and the left insertion guide’s endpoint. R1/r3 extended that guide along the nearby f stem; r2 correctly separated the independent line and letter. The l/ell choice is encoding-only and excluded from counts. R2’s uncertain semicolon glyph was resolved, while its logical attachment remains open. A narrower surname crop preserved genuine graphic questions that the broader r2 crop did not settle. No mathematical proof check was performed on this programmatic page. The next brief adds general guidance on separating letter strokes from guides, l/ell equivalence, and not inventing punctuation beyond a clipped edge.

## Record organization and checkpoint policy

Each decided page is written to pages/ before the next page is assigned. decisions/ records the main reader’s choice at every logged place, including all three readings when they differed; build_records.py renders the cumulative tables. CHECK_EVENTS.tsv distinguishes actual targeted mathematical checking from background carried without a detected fault. Reading alone is never labelled a proof check. Checkpoints are new cumulative ZIPs created at 45-minute intervals only. Earlier checkpoint ZIPs and original source attachments are not nested in any archive. Final SHA-256 hashes are recorded only when all page readings and the combined fragment are frozen, then verified unchanged at the end.
