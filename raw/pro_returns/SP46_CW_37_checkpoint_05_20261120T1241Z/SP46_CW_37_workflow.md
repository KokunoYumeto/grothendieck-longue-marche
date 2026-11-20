# Reading workflow

Pages were processed in increasing scan order. Each page was assigned to three fresh agents with no inherited conversation. Their scope was one page, its two witness extracts, C’s earlier doubts/notes for that page, the conventions, and the notation table established so far. They could not read one another’s files. The main reader compared the returns and inspected disputed crops before committing each page.

## Reader briefs

### Version 1 — first used scan 52

Initial brief implementing the supplied second-pass method.

Full brief: `briefs/brief_v01.md`.

### Version 2 — first used scan 53

Scan 052 return B initially used diff_c=false for resolved C uncertainty and doubled the backslashes in report strings. These bookkeeping points were clarified to all current readers without sharing any reading; B corrected its report. The next brief makes uncertainty counting and report escaping explicit, and reminds readers to report H-only descriptions of drawings. Readers A and C also attempted compiles that stopped for missing pdflatex/lualatex formats; the next brief explicitly forbids engine/format attempts and retains the prescribed balance-only validation. Inventory kind labels also exceeded the specified enum; the next brief lists the exact allowed values.

Full brief: `briefs/brief_v02.md`.

### Version 3 — first used scan 54

Scan 053 readers treated C-context notation targets as explicit C doubts, differed on whether H archive wrappers were text changes, and differed on counting added uncertainty alternatives. The brief distinguishes these cases and distinguishes H’s italic-underlining convention from an omitted upper rule. The main reader selected a curved grouping path and retained uncertainty in the capital initial rather than treating size alone as decisive.

Full brief: `briefs/brief_v03.md`.

### Version 4 — first used scan 69

On scans 054–055 the readers retained literal uncertain colons for diagonally aligned detached points. The main crops supported uncertain graphic reproductions preserving orientation. The next brief explicitly separates visible shape from uncertain punctuation function, while excluding mere rendering-color differences from reading changes. An H packet boundary error on scan 055 was fixed in the packet and recovery script, without using the unrelated trailing note.

Full brief: `briefs/brief_v04.md`.

### Version 5 — first used scan 70

On scan 069 all three readers found the final d/e overtype and a/e correction, while A alone retained a possible third quotation stroke before implique; the main crop supported retaining that uncertainty. All three used bare inline TikZ because the prescribed figure macro is block-level. The next brief explains boxing it for inline placement. Returns also varied in duplicating unchanged C-context targets as decision rows (4/16/23 on scan 055; 15/20/19 on scan 069); confirmed targets may be grouped in mathematical-reading notes without reducing visual coverage.

Full brief: `briefs/brief_v05.md`.

### Version 6 — first used scan 71

Scan070 readers differed on the typed/handwritten state of repeated chi signs and citation components, and on the allocation of a low punctuation cluster beneath closing quotation marks. Clarify component-level material state, explicit state uncertainty and positional preservation.

Full brief: `briefs/brief_v06.md`.

### Version 7 — first used scan 72

Scan071 A/B made 45/35 crops versus C’s 7, largely because they left old-style numeral material state open. All ultimately agreed the references were typed. Reinforce settling legible fields from the halves without reducing character coverage; cap image-display batches after A’s delivery truncation, and request exact graphic snippets in reports.

Full brief: `briefs/brief_v07.md`.

### Version 8 — first used scan 77

On scan 076 all three readers performed conditional local composition diagnostics but supplied noncanonical check-event labels. Version 8 preserves those limited checks under the requested taxonomy and separates them from theorem proof claims.

Full brief: `briefs/brief_v08.md`.

### Version 9 — first used scan 87

On scan 086 B reproduced a vertical surface feature as an uncertain graphic, whereas A/C and the main crop identified a pale channel cutting an existing leader dot. Clarify recording established paper damage as an inspected exclusion, while preserving genuinely uncertain dark marks.

Full brief: `briefs/brief_v09.md`.


## First brief

# Independent reader brief — version 1 (first used scan 052)

You are one of three independent readers of ONE page. Read only your assigned packet, this brief, conventions.md, PREAMBLE.tex and that page's three images. Do not read any other reader's files or any other page. Do not delegate. Ink is authority; C and H are drafts. Do not use OCR, recognition software, PDF text, web research or published texts. Your task is a complete diplomatic reading, using C as a careful draft to check word by word, not blindly copying it. Your reading must include every textual and graphical element.

## Steps (a–d)

a. View the whole-page JPEG ONCE for layout, identifying all text, displays, drawings, marginal notes, deletions and insertions. Use tools.view_image (emit returned image_url with image()) so you actually see it.
b. View each full-resolution half ONCE, in order a then b; read line by line against C.tex and H.tex. Check every word, accent, abbreviation, ending, punctuation, symbol, index, prime/exclamation, inequality, arrow, underline and state of deletion/insertion. Inspect every C doubt using the supplied C_context.md. The halves settle clear writing: do not reopen/enlarge a whole half.
c. List the remaining open places, including unresolved witness differences, C doubt marks, small mathematical glyphs, crowded/slanted/struck writing. Make ONE tight crop per open place from the original whole image (a word or formula with a line around it), scale with LANCZOS to roughly 2200–3000 px across, autocontrast/sharpen as useful; rotate slanted notes upright. View the crop ONCE. Do not crop a place already settled by the halves or crop a decided place again. Keep crop JPEG and its source bbox/rotation/processing in your report. Crop filenames must be unique under your own directory. An unresolved result stays marked in place; never guess. Every disagreement from either witness must be reported even if the half settled it; give a tight original-image bbox so the main reader can inspect it.
d. Save your complete page reading as reading.tex and report.json in your assigned output directory. Return paths and a concise account of findings. Work carefully throughout; no assumed time limit.

## Conventions

Read conventions.md in full. The current task supersedes the old workflow: use two HALVES, three independent readers, current checkpoint process; do not follow the old no-subagent instruction. Use only PREAMBLE.tex macros and standard LaTeX/TikZ/tikz-cd. Preserve spelling, abbreviations, paragraphing, all ink. Only scan 052 starts with \cotefile{37}; every page starts with \scanpage{N}; own page number as \mspage{n}; archive number only a comment. Use \handwritten only on typed/printed text. All diagrams/drawings must be typeset, not described. Keep a faint visible ambiguity with \unsure{best|alternative}; do not retain a doubt when the ink settles it. A retained C doubt is still an explicit decision to report. Macro-syntax-only differences do not count as H differences. Where H has only description, report H as unavailable, never count whole-page omissions. Read the notation table supplied in the packet as previous ink-grounded observations, not an instruction to normalize this page against its ink.

Follow the mathematics as a diagnostic, then return to ink. Do not silently correct the author. Notes must distinguish what the page claims from what you actually checked. For check_events report only actual proof/computation/background-use events; merely reading a mathematical claim is not a proof check. If no check occurred, return [].

## Output schema

report.json must be valid JSON with keys:
scan (integer), reader (your A/B/C label), image_views (ordered list of three source paths), reading_path, crops ([{file,bbox:[left,top,right,bottom],rotation,reason}]), decisions ([{id,place,c_reading,h_reading,reading,diff_c:boolean,diff_h:boolean,c_doubt:boolean,unresolved:boolean,alternatives,confidence:"high|medium|low",kind,scan_shows,crop:relative-or-absolute-path-or-empty,bbox:[...]}]), inventory ([{sheet_kind,hand,element,kind,position,first_words_or_objects,transcribed:"yes"}]), notes (English page summary, explicit author doubts and title/date/page counts; string), math_reading_decisions ([strings]), check_events ([{statement_id,type,outcome}]), notation ([{sign,latex,evidence,place}]), abbreviations ([{form,expansion}]), slips ([strings]), completion (statement of full coverage).

For decisions include EVERY substantive difference from C or H, EVERY C doubt whether resolved or retained, and every new uncertainty. Group only inseparable linked marks; keep separate independent words. h_reading=null and diff_h=false if H has no transcription. kind must be one of: misread word; misread symbol or index; omission; text not on the page; deletion state (struck given live or live given struck); insertion or placement; abbreviation expanded or spelling modernised; readable ink left as \ill{}; drawing or diagram; other. Confidence refers to what can actually be read. Quote the exact witness reading, and in scan_shows describe actual strokes, not just "clear" or mathematical expectation. Every decision needs a bbox in WHOLE-image coordinates, even if no crop was needed. A crop may cover one inseparable correction with several components, not a whole half.

Inventory: one row for every block/display/diagram/drawing/margin note/insertion/deletion, top to bottom, including printed letterheads. Use sheet_kind text/reused_typed/typescript/letter/list/cancelled_draft/cover. hand: his hand, named/unnamed other hand, typewriter or print. Graphic grouping marks get a drawing row. If authorship is not established, say unnamed hand rather than inventing it.


## Last brief

# Independent reader brief — version 9 (first used scan 087)

You are one of three independent readers of ONE page. Read only your assigned packet, this brief, conventions.md, PREAMBLE.tex and that page's three images. Do not read any other reader's files or any other page. Do not delegate. Ink is authority; C and H are drafts. Do not use OCR, recognition software, PDF text, web research or published texts. Your task is a complete diplomatic reading, using C as a careful draft to check word by word, not blindly copying it. Your reading must include every textual and graphical element.

## Steps (a–d)

a. View the whole-page JPEG ONCE for layout, identifying all text, displays, drawings, marginal notes, deletions and insertions. Use tools.view_image (emit returned image_url with image()) so you actually see it.
b. View each full-resolution half ONCE, in order a then b; read line by line against C.tex and H.tex. Check every word, accent, abbreviation, ending, punctuation, symbol, index, prime/exclamation, inequality, arrow, underline and state of deletion/insertion. Inspect every C doubt using the supplied C_context.md. The halves settle clear writing: do not reopen/enlarge a whole half.
c. List the remaining open places, including unresolved witness differences, C doubt marks, small mathematical glyphs, crowded/slanted/struck writing. Make ONE tight crop per open place from the original whole image (a word or formula with a line around it), scale with LANCZOS to roughly 2200–3000 px across, autocontrast/sharpen as useful; rotate slanted notes upright. View the crop ONCE. Do not crop a place already settled by the halves or crop a decided place again. Keep crop JPEG and its source bbox/rotation/processing in your report. Crop filenames must be unique under your own directory. An unresolved result stays marked in place; never guess. Every disagreement from either witness must be reported even if the half settled it; give a tight original-image bbox so the main reader can inspect it.
d. Save your complete page reading as reading.tex and report.json in your assigned output directory. Return paths and a concise account of findings. Work carefully throughout; no assumed time limit.

## Conventions

Read conventions.md in full. The current task supersedes the old workflow: use two HALVES, three independent readers, current checkpoint process; do not follow the old no-subagent instruction. Use only PREAMBLE.tex macros and standard LaTeX/TikZ/tikz-cd. Preserve spelling, abbreviations, paragraphing, all ink. Only scan 052 starts with \cotefile{37}; every page starts with \scanpage{N}; own page number as \mspage{n}; archive number only a comment. Use \handwritten only on typed/printed text. All diagrams/drawings must be typeset, not described. Keep a faint visible ambiguity with \unsure{best|alternative}; do not retain a doubt when the ink settles it. A retained C doubt is still an explicit decision to report. Macro-syntax-only differences do not count as H differences. Where H has only description, report H as unavailable, never count whole-page omissions. Read the notation table supplied in the packet as previous ink-grounded observations, not an instruction to normalize this page against its ink.

Follow the mathematics as a diagnostic, then return to ink. Do not silently correct the author. Notes must distinguish what the page claims from what you actually checked. For check_events report only actual proof/computation/background-use events; merely reading a mathematical claim is not a proof check. If no check occurred, return [].

## Output schema

report.json must be valid JSON with keys:
scan (integer), reader (your A/B/C label), image_views (ordered list of three source paths), reading_path, crops ([{file,bbox:[left,top,right,bottom],rotation,reason}]), decisions ([{id,place,c_reading,h_reading,reading,diff_c:boolean,diff_h:boolean,c_doubt:boolean,unresolved:boolean,alternatives,confidence:"high|medium|low",kind,scan_shows,crop:relative-or-absolute-path-or-empty,bbox:[...]}]), inventory ([{sheet_kind,hand,element,kind,position,first_words_or_objects,transcribed:"yes"}]), notes (English page summary, explicit author doubts and title/date/page counts; string), math_reading_decisions ([strings]), check_events ([{statement_id,type,outcome}]), notation ([{sign,latex,evidence,place}]), abbreviations ([{form,expansion}]), slips ([strings]), completion (statement of full coverage).

For decisions include EVERY substantive difference from C or H, EVERY C doubt whether resolved or retained, and every new uncertainty. Group only inseparable linked marks; keep separate independent words. h_reading=null and diff_h=false if H has no transcription. kind must be one of: misread word; misread symbol or index; omission; text not on the page; deletion state (struck given live or live given struck); insertion or placement; abbreviation expanded or spelling modernised; readable ink left as \ill{}; drawing or diagram; other. Confidence refers to what can actually be read. Quote the exact witness reading, and in scan_shows describe actual strokes, not just "clear" or mathematical expectation. Every decision needs a bbox in WHOLE-image coordinates, even if no crop was needed. A crop may cover one inseparable correction with several components, not a whole half.

Inventory: one row for every block/display/diagram/drawing/margin note/insertion/deletion, top to bottom, including printed letterheads. Use sheet_kind text/reused_typed/typescript/letter/list/cancelled_draft/cover. hand: his hand, named/unnamed other hand, typewriter or print. Graphic grouping marks get a drawing row. If authorship is not established, say unnamed hand rather than inventing it.

## Clarifications after scan 052

- Removing a C doubt or adding a new doubt changes the transcription even if the preferred letters stay the same: diff_c=true. A wholly unchanged retained doubt is false. Keep a row for either decision.
- JSON LaTeX strings must decode to normal single-backslash commands, just as the .tex file does; JSON source escaping is not itself a second LaTeX backslash.
- Report all H differences in certainty or omission in addition to different words. A drawing described only by an H note must be listed as a drawing/diagram difference; exclude pure rendering syntax for the same semantic mark.
- Keep crop filenames unique and use whole-page bboxes. If a source half is left/right instead of top/bottom, infer its offset from its dimensions and the overlap.

- Do not run a TeX engine or attempt to build TeX formats. The source task explicitly requests balance checks instead of compilation; do those checks only after your reading is written.

- Inventory kind is exactly one of: text, display, diagram, drawing, margin note, insertion, deletion. Use text for a text block; an archive number may be inventoried as text recorded in a comment.

## Clarifications after scan 053

- c_doubt=true means an explicit unsure/illegible place in C’s transcription. C_context also contains notation inspection targets without doubt marks; review and report those targets, but do not label a confirmed unmarked reading as a retained C doubt.
- H page wrappers are archival metadata, not manuscript pagination. A wrapper versus our archive-number comment is not itself a collation difference.
- H italics explicitly stand for manuscript underlining in its notes. Do not count that macro convention alone; separately record an upper rule or other graphic stroke that H does not represent.
- A new alternative in an uncertainty record is a difference in recorded reading, not a macro-only change. State this explicitly if the preferred letters and uncertain status are otherwise shared.

## Clarification after scan 055

- Detached marginal points and strokes are not automatically punctuation. When their identity is uncertain, reproduce their observed shape and relative placement in TikZ, with an unsure marker as needed, and record possible punctuation or incidental-mark interpretations in the report. Distinguish a change of observed shape or placement from a mere macro/color presentation change. Do not infer that paper staining is authored ink.

## Clarifications after scan 069

- The supplied figure macro creates a centered paragraph block. To preserve a tiny graphic in line or under a particular symbol, put figure inside a suitably sized parbox and position that box with standard LaTeX makebox/raisebox, rather than omitting the prescribed figure wrapper. Keep the observed relation to surrounding text.
- Decision rows are required for every substantive witness difference, every explicit C doubt (resolved or retained), and every new uncertainty. Confirmed unmarked C-context notation targets may be reported together in math_reading_decisions instead of repeated as unchanged decision rows. This changes reporting only: every word and sign still receives the same independent ink check.
- For a faint apparent accent or odd stroke in a typescript, inspect both the upper and baseline traces for a recoverable overtyped letter before deciding its accent status. Preserve a legible underprint as deleted immediately before the live letter.

## Clarifications after scan 070

- On a typescript, classify the writing state of each component independently: handwritten digits can occupy spaces between typed reference points, and a Greek glyph need not share the writing state of a nearby Greek glyph. Do not place an entire number or formula in handwritten merely because some parts are penned.
- If the glyph is readable but its typed/handwritten construction is genuinely unresolved, record that state uncertainty explicitly, with the two material alternatives, and mark its first recurring occurrence on the page. Do not infer a deleted underlying letter merely from a composite typewriter shape.
- For punctuation crowded under quotation marks, preserve the observed vertical and horizontal relation. Report all visible low and high strokes as one inseparable cluster when assigning them separately would assume the punctuation being decided.

## Clarifications after scan 071

- Display enlarged crops in small batches of at most three images. If a tool delivery is truncated before an image reaches your context, retrieve the identical retained file for its first actual inspection; do not recrop it. Record requested deliveries separately from actual visual views.
- Complete the line-by-line half reading before listing open places. Curved or old-style typewriter numerals are not automatically handwritten. Use repeated impressions on the current page to distinguish design from pen construction; if the half settles a reference field, do not crop it merely because it contains digits. This does not relax the inspection of any character or any genuine material-state doubt.
- Confirmed unmarked targets may stay in math_reading_decisions. The main changes record needs the final exact LaTeX snippet for a graphic, not an English description in place of that snippet.

## Clarification after scan 076

- Use only the requested check-event types: targeted proof check; independent re-proof; computation or formal certificate; used and rechecked in this run; carried as background without fault found; refuted, with the refined statement’s id. A local source/target or internal-notation consistency check actually performed belongs under used and rechecked in this run, with its precise conditional scope. Preserve useful diagnostics, but do not invent event types or report a theorem proof when only a local diagnostic occurred. Merely reading an assertion still creates no mathematical check event.

## Clarification after scan 086

- Distinguish dark marks of unresolved origin from identifiable surface damage. If a crop establishes a paper-coloured channel that disrupts existing print, a crease, or a scratch rather than added ink, document the inspected exclusion in the report; do not insert it into the transcription merely as an uncertain drawing. If the material evidence remains open, preserve the actual dark shape with that uncertainty. This does not authorize dropping faint ink or making a second crop of a settled place.


## Crops and completion

Counts include retained reader crops and additional main-reader crops. Reuse of a reader crop for adjudication does not create another crop.

| Scan | A | B | C | Main additional | Total | Decided UTC |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| 52 | 23 | 16 | 21 | 12 | 72 | 2026-11-20 09:26:39 UTC |
| 53 | 10 | 7 | 8 | 8 | 33 | 2026-11-20 09:40:08 UTC |
| 54 | 11 | 10 | 10 | 2 | 33 | 2026-11-20 09:59:51 UTC |
| 55 | 6 | 5 | 5 | 0 | 16 | 2026-11-20 10:08:00 UTC |
| 69 | 6 | 5 | 5 | 1 | 17 | 2026-11-20 10:22:30 UTC |
| 70 | 8 | 6 | 9 | 1 | 24 | 2026-11-20 10:37:13 UTC |
| 71 | 45 | 35 | 7 | 0 | 87 | 2026-11-20 10:56:07 UTC |
| 72 | 3 | 4 | 4 | 0 | 11 | 2026-11-20 11:10:36 UTC |
| 74 | 4 | 3 | 3 | 0 | 10 | 2026-11-20 11:19:45 UTC |
| 75 | 5 | 7 | 8 | 0 | 20 | 2026-11-20 11:33:41 UTC |
| 76 | 9 | 9 | 9 | 0 | 27 | 2026-11-20 11:50:04 UTC |
| 77 | 13 | 11 | 12 | 6 | 42 | 2026-11-20 12:05:05 UTC |
| 85 | 5 | 5 | 5 | 1 | 16 | 2026-11-20 12:17:40 UTC |
| 86 | 7 | 7 | 5 | 1 | 20 | 2026-11-20 12:30:02 UTC |

## What worked and what did not

Observations through scan 052 (to be extended as the work proceeds):

Independent readers usefully exposed disagreements hidden by agreement with a draft: the verb after the second entry’s colon, the coefficient exponent and alphabet, and the possible upper mark on the final arrow. The main reader adjudicated every reported change and every reader disagreement on retained reader crops or additional tight crops. Differences in certainty were not decided by majority vote. Unresolved handwriting was retained with explicit alternatives.

The first page required 23, 16 and 21 reader crops, plus nine additional main-reader crops. Several clear witness differences were settled by readers on a half, so the main reader made tight crops for its own adjudication. One attempted tool output containing nine large main crops was truncated before usable visual output; the same existing files were displayed in three smaller groups. No second crop was created for that technical re-display.

Reporting needed clarification after scan 052: resolved/new doubt marks change C even where the preferred letters are unchanged; JSON escaping must decode to ordinary LaTeX; graphic rules and enclosures described only in H notes still need collation; inventory kind values must use the requested enumeration. Readers A and C attempted TeX engines, which stopped for missing formats before document processing. These were unsuccessful attempts, not compilation validation. The next brief explicitly prohibits compilation and keeps the original balance-only requirement. No OCR, web research or external mathematical source was used.

Crop paths and complete independent returns are retained. The changes log contains both changed places and explicit decisions to retain C doubts. H-description-only pages will have no H collation rows. Documentary source checks in CHECK_EVENTS.tsv are identified as documentary and never presented as proof checks.

After scan 053, comparison of the Roman-heading convention identified four upper-rule omissions in H not separately logged on scan 052. Four collation rows were added, using one existing crop and three new graphic-locus crops. The scan 052 transcription did not change. Its main additional crop total is therefore twelve, including the later notation comparison.

Scan 054: disagreements chiefly involved stroke confidence (Jouanolou, the stop after 40, and the retraced middle of throughout), small marginal marks and graphic geometry. These did not reveal a new missing convention, so brief v03 continues for scan 055. The main reader viewed ten of reader A’s existing crops (all except the unchanged resp. target) and made two new crops for frame and grouping geometry. The top note is anchored before the lower-starting printed letterhead; isolated marks are reproduced without invented semantic values. All eight explicit C doubts were decided. Structural validation passed.

During scan 055, the extracted H description was found to carry a following SGA 6 cover note because that unnumbered H section has no intervening page wrapper. That following section was removed from the active packet, and all three readers were told to exclude it. It supplies no text or collation for scan 055. Future packets will be checked at launch for trailing unnumbered material.

Scan 055: three independent full readings agreed on all prose and mathematical content and retained the four C doubts. Main inspected four existing A crops, with no additional crop. The only main refinement is the observed orientation/shape of the uncertain marginal dot pair. The diagram arrows agree semantically; B’s gray rendering is cosmetic. C’s inventory separates all three long arrows and was retained. Brief v04 clarifies uncertain marginal graphics before scan 069.

Scan 069: the complete independent page texts were compared while the readers finished reports; main crop decisions were committed only after all three full reports were available. Main viewed C’s five retained crops and A’s extra implique crop, then made one new pagination crop. Two overtypes and an underlined coefficient were independently resolved. A’s extra quotation-stroke uncertainty was retained from the main crop. Tiny shapes are boxed so the supplied paragraph-level figure macro can retain their inline placement. H’s descriptive claim of no handwriting did not override the visible additions. Brief v05 records these lessons and avoids duplicating unchanged inspection targets in decision tables.

Scan070: independent readers identified the same numeral rules but disagreed over letter/number index identity, material state, and allocation of a crowded punctuation cluster. Main reused nine retained reader crops and made only the missing pagination crop. State uncertainty was kept distinct from mathematical character identity; handwritten digits were separated from typed reference points.

Scan071: A/B/C retained 45/35/7 crops. Many A/B crops confirmed the curved reference numerals as typewriter impressions; C settled those fields from the halves. All agreed on their final material state. The brief now more explicitly separates a typeface design difference from an unresolved pen/type question. A’s batch for crops31–38 was truncated before image delivery; the same files were subsequently displayed in pairs for their first actual views, with no recropping. Main inspected nine existing crops and needed no additional crop.

Scan 072: all readers returned four mandatory loci (A and C additionally logged the confirmed hyphen contrast). A made 3 crops, B 4 and C 4; main reused B’s four and made none. One main-reader two-image response was truncated before images were delivered; the same retained files were successfully delivered individually for first actual viewing. No settled locus was recropped. The small satellite in the detached cluster was present in B’s drawing and confirmed by main; A and C omitted it.

Scan 074: A/B/C returned five mandatory loci and made 4/3/3 crops. Main viewed A’s four crops, with one crop serving the two adjacent overprints, and made none. The new m alternative at the clipped edge was retained because its first x-height stem cannot be separated from the other partial forms. H’s supplied-letter markers are distinguished from explicit doubt markers in the collation. The material doubt mentioned only in C’s context for the curve is now marked in the text. No brief change was required.

Scan 075: A/B/C made 5/7/8 crops. Main viewed five B crops and C’s marginal-cluster crop, with no additional crop. The page texts agreed on every diagram object and arrow. Main retained the new capital-J alternative, rejected a proposed 1/i ambiguity from the point’s offset, and recorded the low detached grey shapes without asserting authorship. The marginal graphic combines the independently observed main lobes and faint companions. Reader A adjusted its margin-anchor position after the initial text was written; the completed return and report agree. No brief change was needed.

Scan 076: all three readers made nine crops. Main inspected ten existing crops, with no new crop; the insertion pointer had been settled by A/C from the half and cropped by B. Source/target image requests lost to truncation were recovered from the identical files for first actual viewing. Main restricted eta/n/gamma to eta/n, retained the added k target alternative and material-state uncertainty in tels, and chose the more faithful B graphical contours. The d_2 eta expression was already settled by all three halves and was not recropped. Readers reported useful conditional composition diagnostics but used nonstandard event labels; version 8 clarifies classification without inflating them into theorem proofs.

Scan 077: A/B/C made 13/11/12 crops. Main viewed 13 retained reader crops and made six additional single-locus crops for the letterhead, enclosing loop, three clear ruled Roman groups and lower brace, because the readers had settled those H differences from the half. The combined numeral/upper-brace crop settled both adjoining retraced components. Main merged the printed text and its rule into one letterhead collation locus to avoid duplicate counting, chose the doubled lower brace contour, resolved the endpoint 1.22, preferred colon over à, and retained the accent and word-ending doubts. All ten C doubt occurrences have separate decisions. No brief change was needed; remaining differences concerned the ink.

Scan 085: A/B/C each made five crops. Main viewed five retained crops and made one additional pagination crop because all readers had settled its missing dashes from the half. Seven recorded loci include the two explicit C doubts and an unchanged C-context punctuation target. The linked overprints and newly noticed terminal impression were adjudicated from the same retained word crop, with no recrop. Main retained the first underprint doubt against C-reader’s resolution and ordered all three terminal-s alternatives from observed spacing. The graphic differences were reconciled without imposing punctuation. No brief change was required; differences concerned local ink and material interpretation.

Scan 086: A/B/C made 7/7/5 crops. Main viewed seven retained reader crops and made one missing pagination crop. The vertical-feature dispute was settled as surface disruption because a pale channel cuts an existing printed leader dot. The detached pair was retained from A/B against its absence in C-reader. The 6.10 underletter and low trace were kept as one linked correction locus: main added A’s j alternative while retaining B’s observed contour with uncertain assignment. All five explicit C doubts remain recorded. Version 9 clarifies that established surface damage is documented as an exclusion, rather than reproduced as an uncertain authored graphic.

