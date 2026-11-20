# Workflow record

Every scan is assigned in order to three new, independent readers. Each receives only that page’s scan images, C and H text (or H description), C’s page-specific questions and inventory, the conventions, and the current notation snapshot. Their complete readings, reports, and crops are retained under readers/. Main-reader decisions and all three readings are recorded under decisions/ and in the changes log. The main reader reviews crops for disagreements and writes the page and records before starting the next scan.

## Crop counts

| Scan | Brief | Reader 1 | Reader 2 | Reader 3 | Main new crops | Workflow observations |
| --- | --- | --- | --- | --- | --- | --- |
| 3 | v001 | 13 | 15 | 14 | 11 | All three agree on Manuscripts, sécrétaire and the cancelled Roman letters. They differ on underprint certainty, preferred order, surname confidence and frame geometry; main crop decisions retain nine unresolved loci. Half-settled differences needed source bboxes for main review. |
| 4 | v002 | 0 | 0 | 1 | 0 | All three readings agree with both witnesses. R3 used one crop to distinguish isolated lower-right specks from text. R2/r3 prepended an extra cote macro; r1 correctly follows the continuing fragment. This syntax scope difference does not concern ink. |
| 5 | v003 | 0 | 0 | 0 | 0 | The three readings are identical apart from trailing whitespace; no ink discrepancy and no crop. An extraction bug initially included SGA 5 rows from scan 003 among C prior notes; all readers identified or were notified of the mismatch, ignored those rows, and did not reopen images. Packet extraction now checks table headers and page-specific bullet ranges. |
| 7 | v003 | 1 | 1 | 1 | 1 | All three complete readings are identical. They independently cropped the same crowded ée word boundary and retained C/H. One H raised-ordinal placement difference was confirmed by the main crop; no brief change required. |
| 9 | v003 | 6 | 4 | 5 | 0 | Readers independently agreed on all prose and handwritten corrections except the epsilon glyph and signature punctuation. Main inspection selected r1 at those two loci. R2/r3 grouped the marginal bar correctly but needed an explicit left-margin setting; v004 clarifies that implementation detail. |
| 10 | v004 | 6 | 9 | 8 | 0 | All seven discrepancy loci inspected by main in existing crops. Foreground letters were separated from underprints and strike order. Different drawing implementations were compared by geometry; no new brief rule was needed. Mathematical checking is explicitly scoped apart from visual reading. |
| 11 | v004 | 8 | 9 | 11 | 0 | Readers agreed on most signs and state; main selected r2’s resolved du and r1’s narrower cancelled-reference scope. All six difference loci inspected on existing crops. Numbering was compared through completed records without reopening earlier images. Conditional mathematics is explicitly separated from glyph decisions. |
| 12 | v004 | 9 | 8 | 7 | 0 | All three complete readings compared. Nine existing r1 detail crops inspected by main in three small batches. An earlier attempted nine-image batch returned only a context-truncation notice; no image from that failed delivery is claimed as an inspection. No new crop or source whole/half view by main. Differences were ink judgments, not a brief gap; v004 retained. |
| 13 | v004 | 14 | 15 | 13 | 0 | All three complete readings compared. Main inspected 13 existing r1 crops and r2 crop 14, each once; no new crop. Explicit alternatives and visible overprint state were adjudicated. Different treatment of equivalent supplied/unsure clipped initials exposed a collation-brief gap; v005 clarifies it starting scan015. |
| 15 | v005 | 7 | 6 | 6 | 5 | The three full reading.tex files are identical. Main inspected six r3 crops plus r1’s line-end spots crop, and made/viewed five new crops for pourlla, quotation marks and three dash-classification disagreements. v006 clarifies typography-only dash/ellipsis collation from scan016 onward. |
| 16 | v006 | 7 | 8 | 8 | 1 | All three complete readings/reports compared. Main inspected seven existing crops and one new crop for the half-settled cancelled e. Disagreements concerned actual overprint contours and uncertainty, with no new briefing gap. v006 retained. |
| 18 | v006 | 24 | 23 | 23 | 11 | All three complete readings and reports compared. Main inspected 23 existing r2 crops, one r1 crop and 11 newly created crops, each once; no whole or half source reopened. Wider geometry/cancellation crops concern previously uninspected mark extents; incidental repeated text was not re-adjudicated. All 23 inline C marks receive explicit outcomes. v007 adds mechanically auditable C-mark coverage and clarifies underline versus italic state after the disagreement here. Record-only inventory audit after scan 025: six late-added cells (NB B, passage overprint, second sûr, and three raised ordinal-o forms) were moved into their already-recorded paragraph positions. Existing element IDs and transcription text are unchanged; no image was reopened. |
| 23 | v007 | 17 | 17 | 16 | 11 | All three complete readings and all report rows compared. Main inspected 17 existing reader crops and 11 new tight crops, no whole/half images. An earlier 3-image tool response was truncated before images were delivered and counted as no inspection; the same three paths were then successfully displayed once each. Geometry crop was used for enclosure/obliques, not to reopen settled text. The overlapping bis crop was used for exact, not to readjudicate est. |
| 24 | v008 | 13 | 11 | 12 | 8 | All three complete readings and every report section compared. Main inspected 13 existing reader crops and 8 new tight crops; no whole/half source view. One attempted three-image response was truncated before delivery and counted as no inspection; those existing paths were then displayed once successfully. The cancelled quasi-cpt crop and live-abbreviation crop were each used for their separate locus. Source graphics were checked independently of editorial meaning. |
| 25 | v009 | 20 | 23 | 25 | 11 | All three complete readings and all report sections compared. Main inspected 22 existing reader crops and 11 new crops, once each; no whole or half image was opened by main. Wider local crops were necessary for the cancellation geometry and the disputed order of sloping baselines; overlaps were incidental to distinct loci, not repeat adjudication. A report-output truncation was followed only by bounded text reads. The initially supplied conventions path was corrected to briefs/conventions.md; readers documented when they read it. r2 left-note crop was not rotated; main used the already upright r1 crop. Reader inventories grouped states out of physical order; main interleaved them top-to-bottom. Main found a visible final ét accent missed by all three readers. |
| 27 | v010 | 13 | 12 | 14 | 19 | Three fresh independent readers used v010 and the cumulative notation snapshot. All three complete readings and reports were compared. Main viewed 14 existing crops and five new crops, once each. The new body crop targets page-spanning cancellation geometry; other new crops target distinct prose glyph, comma, underline, and mathematically suspicious axis pairings. Rotated whole/half derivatives were moved outside the deliverable tree after an identical operational reminder, without reopening; v011 records that storage rule. No source view was repeated and no OCR or external research was used. |
| 30 | v011 | 6 | 6 | 7 | 16 | Three fresh independent readers used v011 and the cumulative notation snapshot. Main compared all three complete readings, reports and inventories, and inspected eight existing tight reader crops plus eight new tight main crops. Each delivered crop was viewed once. An attempted four-image tool result was truncated before any image was delivered; those unseen files were subsequently displayed in bounded pairs and counted only on that successful delivery. No whole or half source was reopened, no settled locus was recropped, and no OCR or external research was used. |

## Brief revision history

- **v001, scan 003:** Initial brief.
- **v002, first used scan 004:** Scan 003’s readers differed on underprint versus strike order, surname confidence, and whether the SGA 7 frame was continuous; these were genuine reading disagreements, adjudicated from crops. Clarified separation of visible glyph, possible underprint and order. Added contextual whole-source bboxes for all differences after half-settled leaders required main crops. Clarified reporting of accurately described but undrawn H graphic marks. Required actual start-time logging because r2 had only a first recorded timestamp. Standardized relative crop paths and compact report organization; no reading requirement was shortened.
- **v003, first used scan 005:** R2 and r3 added a cotefile macro to scan 004 while r1 retained the correctly scoped C fragment. Clarified that only the package’s first page carries that macro. No ink disagreement occurred.
- **Packet preparation correction during scan 005:** A table labelled SGA in C’s prior notes was initially parsed as a scan table, exposing irrelevant SGA 5 count rows. All three readers ignored them; r3 flagged the mismatch independently. The extraction script now admits scan-labelled tables and explicitly page-labelled bullets only. No page reading was changed and no image was reopened. This was a packet correction, not a new reader-brief version.

- v004, first scan 010: scan 009 readers all located note and bar in the left margin, but r2/r3 used the default right-margin macro without a side command. Clarified standard left-margin scoping and grouping marks.

- v005, first used scan 015, after scan 013: r1 excluded equivalent cautious clipped-initial readings from H counts, while r2/r3 counted supplied/unsure wrapper differences. Main crop review confirmed identical tentative letters. Brief now distinguishes equivalent marked partial-letter readings from genuinely unverified restored words/suffixes, punctuation, alternatives and correction states. No earlier decided textual page used this supplied/unsure boundary case.

- v006, first used scan 016, after scan 015: all three complete texts agreed, but r1 counted three single prose dashes encoded by H as -- while r2/r3 excluded them. Main checked all three source crops and retained the short source stroke without counting typography-only encoding differences. Brief explicitly clarifies dash/ellipsis equivalence, distinguishing truly different visible punctuation.

- v007, first used scan 023, after scan 018: the packet's earlier C question list contained only three rows while C.tex contained 23 inline doubt marks. All three readers received the same coverage reminder without sharing readings, and all supplied 23 outcomes. Added a mechanical C_marked_loci list and explicit C-mark IDs so this mandatory coverage is auditable. Scan 018 also exposed a policy disagreement: r3 treated italic emph as equivalent to an underline. Main inspected the source underline and supplied H style (normalem), and now explicitly distinguishes real underline state from generic emphasis. Added explicit acknowledgement of H's declared omission of typewriter superpositions. These changes refine reporting; they do not relax source inspection.

## v008 — first used on scan 024
After scan 023: clarified that ordinary H notes/add/struck are not doubt flags (same reporting reminder sent to all scan023 readers). r1 described the cancelled block frame/obliques in a comment, r3 omitted their geometry, while r2 drew them; v008 explicitly requires those source graphics in TikZ and distinguishes ordinary insertion calls from standalone drawings. No reading was shared among readers.

## v009 — first used on scan 025
Scan 024 r1 marked two H differences as doubtful because an adjacent cancellation carried ill, although the differing reference and live q.c. did not. Clarified exact scope, including physical correspondence when H relocates a doubtful oval label. Readers r1/r3 also retried already-unavailable TeX formats; clarified structural validation and centrally recorded compile limitation. No source-reading expectation was added.

## v010 — first used on scan 027
Scan 025 inventories grouped deletions and additions rather than interleaving them in physical order; all three oval settings displaced its vertical level. Clarified physical inventory order and placement within a common graphic coordinate system. One slanted marginal crop was not rotated, so the brief emphasizes planning upright rotation before the one view. Main found a final ét acute missed by all three readers, prompting a reminder that each occurrence is independently read. Clarified exact valid LaTeX in report fields and full-reading/report coverage after one missed subscript row.

## v011 — first used scan 030

Scan 027 required an identical operational reminder to move rotated whole/half derivatives outside the deliverable tree; all readers did so without reopening. The new brief states this before viewing. Main also found the handwritten state of the comma after E, while two readers treated it as ordinary punctuation and one omitted it. v011 calls for explicit inspection of added punctuation hand.

## First brief

# Reader brief v001 — first used on scan 003

You are one of THREE independent readers of ONE page in a diplomatic second pass. Do not read another reader's files or ask another reader; do not open other pages' images, witnesses, reports, or source notes. Your task ends with this page. The main reader will adjudicate all differences. Read slowly and completely, from the INK, with both draft witnesses beside it. No OCR, text recognition, external research, published text, or mathematical reconstruction.

Inputs: the assigned packet's metadata.json, C.tex, H.tex, C_prior_questions.md, C_inventory.json; this brief, conventions.md, PREAMBLE.tex; and the supplied notation snapshot. Only metadata.json gives this page's image paths. H may be description only: then it is not a textual witness; do not generate H collation rows for that page.

## Workflow, exactly once per source view
1. Read the textual inputs. Look at the WHOLE image ONCE with view_image for layout (text blocks, displays, margins, additions, cancellations, drawings). This view counts as actual image inspection only if emitted and seen.
2. Look at half _a ONCE and half _b ONCE, line by line against C AND H. Read EVERY word, abbreviation, accent, punctuation mark, symbol, index, exponent, arrow, deletion, insertion and marginal note. Agreement between witnesses supplies no evidence. Settle everything the halves settle; do not reopen/re-enlarge a whole half.
3. List unresolved loci. Crop each unresolved locus ONCE from the source using PIL: tight word/formula and surrounding line; upscale using LANCZOS to about 2000–3500 pixels across; autocontrast/sharpen if needed; rotate upright if slanted. View the crop. Each crop must have a unique name and documented original coordinates, source, transforms, and locus. No repeat crop of a decided place. A C doubt always gets an explicit resolution or retention; no need to crop if the half settles it. Follow the mathematics as a detector of suspicious indices/signs/arrows, but never repair the page to make the mathematics true.
4. Write the COMPLETE page reading in our LaTeX macros as reading.tex in your assigned output directory. Copy C as a base if helpful only AFTER checking every element against the ink; your output is a full, independently verified reading, not just proposed edits. Write report.json (schema below). Summarize your principal findings and counts, then finish. Do not edit shared deliverables or other readers' directories.

## Fidelity priorities
Keep every typed error, strange accent, abbreviation, singular/plural, underlining, deletion state, insertion placement and source question mark. Every letter in a heading/functor is checked separately for single/double strike. Distinguish actual overtyping correction from mere heavier or doubled same-letter type. His double quotes are ``...'' (not guillemets unless drawn). Join line-end hyphenations; keep real word hyphens. Typescript capitals are not bold. In doubt, give visible candidates with unsure, not a contextual restoration. No illegible for mathematical symbols; no omission. Diagrams in tikz-cd and drawings in TikZ, never just descriptions. H's editorial descriptions are not source text. Same reading in different macro syntax is not a collation difference; real state (strike/insertion/underline), spelling, omission or placement IS a difference. Do not declare an abbreviation wrong merely because H includes normal nonbreaking spaces or different line wrapping.

## Report schema (valid UTF-8 JSON)
{
 "scan": 3, "reader": "r1", "model": "GPT-6 Astra Pro", "effort": "inherited; not independently exposed", "started_utc": "...", "ended_utc": "...",
 "views": [{"path":"...", "role":"whole|a|b", "viewed_once":true}],
 "coverage": "Specific concise account of all blocks actually read, including margins and deletions; say if any part remains unviewed.",
 "changes": [{"locus":"specific source line/block", "c":"exact C reading", "h":"exact H reading or [description only]", "reading":"your final reading", "diff_c":true, "diff_h":false, "kind":"one allowed H kind below", "marked_in_H":false, "confidence":"high|medium|low", "evidence":"actual letters/strokes/marks observed, half or crop", "crop":"relative crop path if any", "bbox":[x0,y0,x1,y1], "mathematical_consequence":"if any"}],
 "c_doubts": [{"locus":"...", "c":"...", "decision":"resolved|retained", "reading":"...", "evidence":"...", "crop":"..."}],
 "unresolved": [{"locus":"...", "reading":"...", "alternatives":["..."], "confidence":"...", "reason":"..."}],
 "inventory": [{"sheet_kind":"text|reused_typed|typescript|letter|list|cancelled_draft|cover", "hand":"his hand|another named or unnamed hand|typewriter|print", "element":"unique short id", "kind":"text|display|diagram|drawing|margin note|insertion|deletion", "position":"...", "first_words_or_objects":"...", "transcribed":"yes"}],
 "notes": [{"id":"s003-note01", "text":"English description of what the page states/calculates/asks or dates/counts, source words for doubts, and any math-triggered reading decision.", "basis":"specific page locus; distinguish observation, inference, proof check"}],
 "notation": [{"sign":"...", "latex":"...", "locus":"...", "evidence":"...", "alternatives":"..."}],
 "abbreviations": [{"form":"...", "expansion":"tentative expansion, here only"}],
 "check_events": [{"statement_id":"...", "date":"UTC date/time", "who":"model, effort, this reader run", "type":"actual permitted check event type", "outcome":"exactly what was checked; transcription alone is NOT proof checking"}],
 "crops": [{"path":"relative to work root", "source":"...", "bbox":[...], "transforms":"...", "locus":"..."}],
 "brief_feedback": "any ambiguity/omission in brief that affected the reading, else none"
}

Allowed kind: misread word; misread symbol or index; omission; text not on the page; deletion state (struck given live or live given struck); insertion or placement; abbreviation expanded or spelling modernised; readable ink left as \\ill{}; drawing or diagram; other.
Allowed check event type: targeted proof check; independent re-proof; computation or formal certificate; used and rechecked in this run; carried as background without fault found; refuted, with the refined statement's id. Never label mere transcription as a mathematical check. If no mathematical checking occurs, state that and leave check_events empty; main reader will record the epistemic status of consolidated notes. Inventory must include every meaningful text block/display/correction/marginal drawing, not only differences. All actual differences from C or H must be in changes, including resolved doubt marks; C doubt retentions are also recorded in c_doubts.

## Last brief used

# Reader brief v011 — first used on scan 030

You are one of THREE independent readers of ONE page in a diplomatic second pass. Do not read another reader's files or ask another reader; do not open other pages' images, witnesses, reports, or source notes. Your task ends with this page. The main reader will adjudicate all differences. Read slowly and completely, from the INK, with both draft witnesses beside it. No OCR, text recognition, external research, published text, or mathematical reconstruction.

Inputs: the assigned packet's metadata.json, C.tex, H.tex, C_prior_questions.md, C_marked_loci.md, C_inventory.json; this brief, conventions.md, PREAMBLE.tex; and the supplied notation snapshot. Only metadata.json gives this page's image paths. H may be description only: then it is not a textual witness; do not generate H collation rows for that page.

## Workflow, exactly once per source view
1. Read the textual inputs. Look at the WHOLE image ONCE with view_image for layout (text blocks, displays, margins, additions, cancellations, drawings). This view counts as actual image inspection only if emitted and seen.
2. Look at half _a ONCE and half _b ONCE, line by line against C AND H. Read EVERY word, abbreviation, accent, punctuation mark, symbol, index, exponent, arrow, deletion, insertion and marginal note. Agreement between witnesses supplies no evidence. Settle everything the halves settle; do not reopen/re-enlarge a whole half.
3. List unresolved loci. Crop each unresolved locus ONCE from the source using PIL: tight word/formula and surrounding line; upscale using LANCZOS to about 2000–3500 pixels across; autocontrast/sharpen if needed; rotate upright if slanted. View the crop. Each crop must have a unique name and documented original coordinates, source, transforms, and locus. No repeat crop of a decided place. A C doubt always gets an explicit resolution or retention; no need to crop if the half settles it. Follow the mathematics as a detector of suspicious indices/signs/arrows, but never repair the page to make the mathematics true.
4. Write the COMPLETE page reading in our LaTeX macros as reading.tex in your assigned output directory. Copy C as a base if helpful only AFTER checking every element against the ink; your output is a full, independently verified reading, not just proposed edits. Write report.json (schema below). Summarize your principal findings and counts, then finish. Do not edit shared deliverables or other readers' directories.

## Fidelity priorities
Keep every typed error, strange accent, abbreviation, singular/plural, underlining, deletion state, insertion placement and source question mark. Every letter in a heading/functor is checked separately for single/double strike. Distinguish actual overtyping correction from mere heavier or doubled same-letter type. His double quotes are ``...'' (not guillemets unless drawn). Join line-end hyphenations; keep real word hyphens. Typescript capitals are not bold. In doubt, give visible candidates with unsure, not a contextual restoration. No illegible for mathematical symbols; no omission. Diagrams in tikz-cd and drawings in TikZ, never just descriptions. H's editorial descriptions are not source text. Same reading in different macro syntax is not a collation difference; real state (strike/insertion/underline), spelling, omission or placement IS a difference. Do not declare an abbreviation wrong merely because H includes normal nonbreaking spaces or different line wrapping.

## Report schema (valid UTF-8 JSON)
{
 "scan": 3, "reader": "r1", "model": "GPT-6 Astra Pro", "effort": "inherited; not independently exposed", "started_utc": "...", "ended_utc": "...",
 "views": [{"path":"...", "role":"whole|a|b", "viewed_once":true}],
 "coverage": "Specific concise account of all blocks actually read, including margins and deletions; say if any part remains unviewed.",
 "changes": [{"locus":"specific source line/block", "c":"exact C reading", "h":"exact H reading or [description only]", "reading":"your final reading", "diff_c":true, "diff_h":false, "kind":"one allowed H kind below", "marked_in_H":false, "confidence":"high|medium|low", "evidence":"actual letters/strokes/marks observed, half or crop", "crop":"relative crop path if any", "bbox":[x0,y0,x1,y1], "mathematical_consequence":"if any"}],
 "c_doubts": [{"locus":"...", "c":"...", "decision":"resolved|retained", "reading":"...", "evidence":"...", "crop":"...", "c_mark_ids":["C001"]}],
 "unresolved": [{"locus":"...", "reading":"...", "alternatives":["..."], "confidence":"...", "reason":"..."}],
 "inventory": [{"sheet_kind":"text|reused_typed|typescript|letter|list|cancelled_draft|cover", "hand":"his hand|another named or unnamed hand|typewriter|print", "element":"unique short id", "kind":"text|display|diagram|drawing|margin note|insertion|deletion", "position":"...", "first_words_or_objects":"...", "transcribed":"yes"}],
 "notes": [{"id":"s003-note01", "text":"English description of what the page states/calculates/asks or dates/counts, source words for doubts, and any math-triggered reading decision.", "basis":"specific page locus; distinguish observation, inference, proof check"}],
 "notation": [{"sign":"...", "latex":"...", "locus":"...", "evidence":"...", "alternatives":"..."}],
 "abbreviations": [{"form":"...", "expansion":"tentative expansion, here only"}],
 "check_events": [{"statement_id":"...", "date":"UTC date/time", "who":"model, effort, this reader run", "type":"actual permitted check event type", "outcome":"exactly what was checked; transcription alone is NOT proof checking"}],
 "crops": [{"path":"relative to work root", "source":"...", "bbox":[...], "transforms":"...", "locus":"..."}],
 "brief_feedback": "any ambiguity/omission in brief that affected the reading, else none"
}

Allowed kind: misread word; misread symbol or index; omission; text not on the page; deletion state (struck given live or live given struck); insertion or placement; abbreviation expanded or spelling modernised; readable ink left as \\ill{}; drawing or diagram; other.
Allowed check event type: targeted proof check; independent re-proof; computation or formal certificate; used and rechecked in this run; carried as background without fault found; refuted, with the refined statement's id. Never label mere transcription as a mathematical check. If no mathematical checking occurs, state that and leave check_events empty; main reader will record the epistemic status of consolidated notes. Inventory must include every meaningful text block/display/correction/marginal drawing, not only differences. All actual differences from C or H must be in changes, including resolved doubt marks; C doubt retentions are also recorded in c_doubts.

## Clarifications after scan 003 (v002)
- Log the real UTC start time before the first source view; do not reconstruct an exact start time later.
- For EVERY reported discrepancy, provide a tight whole-source bbox even when the halves settle it and you do not crop it. Include the identifying word/row label along with a pointer or grouping mark, so the main reader can locate its attachment from one crop.
- Crop paths in report.json are relative to SP45_CW_37_work, not relative to your reader directory. JPEG at quality 95–96 is suitable; do not keep duplicate format copies. Do not spend further image views on a settled place.
- Distinguish a visible character from an uncertain underprint and from uncertain strike order. Heavy/doubled type alone is not evidence of a different earlier character. Use only alternatives the actual strokes support; do not invent chronological certainty.
- H may correctly describe a drawing in an editorial note without drawing it. Record that as drawing or diagram when our transcription actually reproduces it, while acknowledging that the verbal description may be accurate. Differences in doubt state are recorded as such, not automatically called errors.
- Keep the report precise and compact: full source reading in reading.tex, all loci and evidence in report.json, without repeating the entire page in narrative. Complete coverage remains mandatory. All source margins and numbers must still be inspected even on a short letter.

## Scope clarification after scan 004 (v003)
- Only scan 003, the first page of the complete package, starts with \cotefile{37}. Every later reading.tex starts with its \scanpage{N}; do not add another cotefile merely because you are a fresh reader. This is a fragment-scope rule, not a reading decision.

## Margin placement clarification after scan 009 (v004)
- The supplied margin macro uses the document default (right-hand margin). If the source has a LEFT marginal note or drawing, use standard LaTeX \reversemarginpar before it and \normalmarginpar afterward. Keep a grouping bar/pointer with its words when the source places them together; a separate centred figure changes the source placement. Record actual relative geometry, not merely the words.

## Collation equivalence clarification after scan 013 (v005)
- When H explicitly marks a clipped initial as supplied and our tentative reading gives the SAME letters with unsure, do not count a change solely for that equivalent cautious presentation. Record the clipping in C doubt outcomes. Distinguish this from H supplying an entire absent word/suffix that our reading leaves unreadable, adding unsupported punctuation, omitting a correction, or giving different letter alternatives; those are substantive differences. State which case applies.

## Prose punctuation encoding clarification after scan 015 (v006)
- A single prose dash encoded as - versus --, or the same three dots encoded literally versus \ldots, is not by itself a new reading. Preserve the actual source form in our text, but do not count H typography/code alone as a collation difference. Count genuinely different visible punctuation marks (for example guillemets versus paired upright quote strokes), extra/absent marks, or an ink-supported difference in symbol identity. Explain any borderline classification.

## Explicit C-mark coverage after scan 018 (v007)
- Also read your packet’s C_marked_loci.md. This is a mechanical list of every unsure/illegible macro in C.tex, supplementing the earlier C questions, which can be incomplete. It supplies no reading. Every numbered C mark needs an explicit resolution or retention.
- In each c_doubts entry add `"c_mark_ids": ["C001", "C002"]` for the mark(s) that the outcome covers. One physical locus may cover several IDs or a duplicate prior question. Together the entries must cover every ID in C_marked_loci.md. Unmarked C questions still receive outcomes, with an empty ID list. No extra crop is needed merely to populate these IDs.

## Visible state versus emphasis after scan 018 (v007)
- A visible underline is a source state, not merely generic emphasis. H's emph is not equivalent to uline unless the supplied H style actually makes it an underline. The supplied H style uses ulem with normalem, so ordinary emph is italic. Record that state difference when the source is visibly underlined; do not extend prose-dash equivalence to it. Likewise retain the literal capital in Lim even if H uses a conventional lower-case limit operator.
- If H explicitly declares that a type of mark (such as typewriter superpositions) is outside its scope, record the actual difference but acknowledge that declaration. Do not describe a declared scope omission as a hidden or unmarked uncertainty.

## H uncertainty flags after scan 023 (v008)
- marked_in_H is true only when H explicitly marks doubt, illegibility, or supplied doubtful text at that locus (including an editorial note expressly saying illisible). An ordinary note describing a correction, insertion, superposition or drawing is not a doubt mark. The add/struck state macros alone are not doubt marks. This flag is independent of whether H accurately acknowledges the mark.

## Graphic cancellation after scan 023 (v008)
- A cancelled block’s enclosing border and long oblique strokes are source graphics. Reproduce their actual geometry in TikZ around the complete text; a deleted macro or a comment describing the frame does not reproduce those marks. Short ordinary insertion calls may be encoded by the insertion’s correct attachment; nested call lines whose geometry distinguishes punctuation must be drawn. Inventory should classify an ordinary insertion leader as an insertion, not claim an undrawn standalone drawing.

## Precise uncertainty scope and validation after scan 024 (v009)
- Apply marked_in_H to the exact differing words or marks. An illegibility mark on a neighbouring cancellation does not mark doubt on a separately written reference accent or an added live abbreviation. If H explicitly locates its doubtful reading in a physical oval, retain that physical-locus correspondence when reporting relocation.
- The installed TeX engines have no LaTeX formats or package tree, and this limitation is already documented centrally. Do not repeat optional compile attempts. Validate fragment scope, balanced groups/environments, report fields and paths without reopening source images; main handles aggregate validation.


## Physical order and local ink checks after scan 025 (v010)
- Interleave inventory entries in physical top-to-bottom reading order. Do not group all deletions before all insertions. When a margin oval is alongside the middle of a tall graphic, preserve that vertical relationship, preferably within the same TikZ coordinate system; anchoring it before or after the whole graphic moves it.
- Rotate slanted marginal text upright in its one crop. Plan that transformation before viewing; do not make a second crop merely to rotate a settled locus.
- Check every repeated subscript and accent locally. On scan 025 all three readers missed a visible acute on the final et, although other occurrences genuinely lacked it. A notation-table pattern never settles the next occurrence.
- In report reading fields use the exact valid LaTeX of reading.tex. A prime is an apostrophe or superscript, not a bare mathematical prime command after the baseline letter. Confirm that every difference in the full reading has a change row; one reader on scan 025 omitted one otherwise correctly read subscript discrepancy.


## Orientation derivatives and punctuation after scan 027 (v011)
- If a source is upside-down, rotate each whole/half before its single view. Put these full-view derivatives outside SP45_CW_37_work, in the workspace oriented_views/scanNNN/reader directory; they are supplied-source derivatives and must not enter deliverable ZIPs. Record the transformation and original-source bbox mapping. Keep only the tight evidence crops in your reader output.
- Inspect whether an added punctuation mark is handwritten. On scan 027, the main comma crop showed a long curved handwritten comma that two readers included as ordinary typed punctuation and one omitted. Encode its hand state as well as its presence.

## Assessment

Assessment through scan 030; the final review must include all 30 pages.

Three fresh readers per page kept their source views independent. Comparing
complete LaTeX readings, rather than only their proposed changes, was essential:
reports occasionally grouped several differences together or omitted a
discrepancy already present in the reading. Main adjudication therefore checked
the union of all three reports and the full-file differences. Each page was
committed and the cumulative records rebuilt before the next page was assigned.

Tight existing reader crops usually sufficed for main decisions. Additional
main crops were necessary for differences settled in the halves without a
reader crop, and for the full extent of graphic marks or disputed order on
sloping baselines. Wider local graphic crops were used for geometry, with
separate small crops for still-open letters. Incidental overlap was not treated
as permission to re-adjudicate a settled locus. Rotated crops were especially
useful for the left oval on scan 025; one reader had left it at its source
slant, so main used another reader's already upright crop.

The brief needed substantive reporting clarifications: source bboxes for
half-settled differences; visible underprint versus uncertain strike order;
left-margin placement; equivalence of cautious clipped-letter readings and
routine dash encoding; physical underline versus italic emphasis; exact H
uncertainty scope; complete cancelled-block graphics; and inventory order.
These revisions did not reduce the required inspection. The cumulative
notation table remained a record of particular glyphs, never a normalization
rule. The acute missed by all three readers on scan 025 illustrates why each
occurrence still needs its own inspection.

Operational problems were recorded rather than hidden. A packet-extraction
bug on scan 005 exposed irrelevant earlier C rows and was corrected without
source rereading. An initial conventions path on scan 025 was corrected and
the readers recorded when they read the proper file. Some large tool outputs
were truncated before images were delivered; those failed deliveries were not
counted as inspections, and bounded subsequent calls displayed the intended
crops once. The available TeX engines lacked the necessary formats/packages,
and the attempted alternative could not obtain its bundle. Structural checks
were completed, but no successful full TeX compilation or rendered-page QA is
claimed; compilation_status.md records the limitation.

Notes and CHECK_EVENTS distinguish documentary comparisons from actual
mathematical work. Limited proof checks are accompanied by their assumptions
and exclusions; none supplies a letter, reference, index or missing word.
Checkpoint ZIPs follow the requested elapsed 45-minute schedule rather than
page boundaries. They contain the entire current deliverable and working
record, excluding the supplied originals and earlier ZIPs.

The later inventory-order review also found six scan 018 entries appended
after the original inventory. They were moved into the positions already
recorded in their entries and confirmed by the consolidated text; no source
image was reopened and no transcription changed. The script and progress log
preserve this record-only correction.

On scan 027, whole and half views had to be rotated through 180 degrees.
All readers moved the resulting full-view derivatives outside the deliverable
tree after an identical reminder, without reopening them. v011 makes that
location explicit before reading. Original-source crop coordinates remain
authoritative. Main added five crops and reused fourteen reader crops.
The mathematical axis mismatch was confirmed in the ink and preserved;
the notes separately record a concrete conditional counterexample, a refined
statement, a domain check and a limited unit-equality proof.

On scan 030, the comparison of all three complete readings recovered a short
extra marginal word reported by only one reader and distinguished three
underline spans from one continuous span. Main viewed eight existing crops
and eight new crops; an initially truncated image output delivered none and
was not counted until the files were actually displayed. The faint comma
after th. remains uncertain rather than being promoted to certain punctuation.
The main decision records the broken lower stroke and retains the incomplete
typed insertion. No additional brief revision was needed for scan 031.
