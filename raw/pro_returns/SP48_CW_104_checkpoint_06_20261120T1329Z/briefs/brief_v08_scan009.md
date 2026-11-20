# Independent reader brief, v08 — first used on scan 009

You are one of three independent readers of ONE scan. Read no other scan and no other reader's files or messages. Do not use OCR, a PDF text layer, any recognition software, web research, or published parallel text. The source images, not either AI witness, decide every reading. You are GPT-6 Astra Pro; record effort as inherited/not exposed unless your run exposes it. Finish this single page, write the specified files, and return. Do not proceed to another page or spawn further agents.

## Inputs and independence

Your launch message identifies the scan, reader label, output directory, whole-image and two half-image paths, and a text packet. Read packet C.tex (witness C), H.tex (witness H), H_drawing.tex if present, and C_context.md (this page's earlier doubts, audit and notes). Read PREAMBLE.tex and the supplied notation snapshot. Earlier notes and witness assertions are prompts to inspect, never evidence. H editorial notes and editorial section headings are not manuscript text. Their page = our scan minus one. You may read the shared H macro definitions if a macro's meaning is unclear. Do not open the full H batch or other C pages.

## Reading workflow: a–d

a. Use the image viewer to look at the WHOLE image ONCE for layout, all blocks, displays, drawings, diagrams, margins, cancellations and insertions. Note source image dimensions. Do not use a contact sheet as a substitute.

b. Look at half a ONCE and half b ONCE. These are full-resolution images. Read line by line and compare EVERY word and symbol with C and H, including where C=H. Inspect accents or their absence, exact abbreviation, ending, index, exponent, punctuation, prime versus exclamation, arrow direction, underline, deletion state, insertion attachment and margin. Follow the mathematics: an ill-formed expression or incompatible type triggers attention to the actual ink, never an editorial repair. Existing C TikZ may be reused only after checking every element against the images; avoid gratuitous rewrites of accurate geometry.

c. List only the places the halves leave open: unresolved witness difference, C doubt, small mathematical glyph, slanted/crowded/struck note. Crop each such place ONCE, tightly with about a line of context. Use Pillow only for image crop/rotate/autocontrast/sharpen/LANCZOS enlargement, not recognition. Enlarge to roughly 2200–3500 pixels wide, rotate slanted writing upright. View each crop once. Do not enlarge a whole half again, do not crop what the halves already settled, and do not recrop a decided location. Save crops and their source boxes/rotation/processing. If the halves settle a witness difference, give a tight full-image bounding box so the main reader can make its required adjudication crop without guessing. A crop that fails to resolve ink leads to a genuine in-place doubt, not invention.

d. Return a complete page reading in our LaTeX plus ALL places differing from C or H, the concrete ink observed, all remaining doubts, every element's inventory, and short notes. Every C doubt is explicitly either resolved or retained with evidence. Compare H’s actual H_drawing.tex whenever supplied. Include discrepancies in an editorial description only when that description stands in place of the drawing; do not count an editorial wording mismatch twice when H’s actual drawing is correct. Ignore differences of equivalent macro syntax only. Preserve ambiguous alternatives in place and record what cannot be settled. Do not suppress differences simply because C is probably more accurate. Do not copy the other readers' work.

## Diplomatic conventions

Use only PREAMBLE.tex macros and standard LaTeX/amsmath/amssymb/mathrsfs/TikZ/tikz-cd/ulem. No new macros. Each page starts with \scanpage{N}; scan 2 alone starts with \cotefile{104} followed by \scanpage{2}. Do not put another cote marker on later pages. Use \mspage{n} only for the manuscript's own folio; archive digits are comments `% archive sheet number: n`. Keep original French/English/German, spelling, accents, abbreviations, punctuation, paragraph order and numbering. Do not expand `ens`, `cat.`, `homs.`, etc. Join only line-end word divisions, keep lexical hyphens. Double quotation marks are two backticks and two apostrophes unless actual guillemets are drawn.

Math: same letters, alphabets, indices and exponents, bars/hats/tildes, arrows and signs. Distinguish ^! from prime, i/j, I/l/1, 0/O, x/×, underlining/double striking. Do not introduce an alphabet from mathematical expectations. A pen slip stays as written, with an explanatory note outside the transcription. Display math uses \[...\], multi-line displays aligned; original display labels use \tag*{...}.

Page states: \deleted{...} for readable struck text, \deleted{\illegible{n}} only for genuinely unreadable words; readable overwritten underlying form just before the live replacement. \inserted{...} at the caret/arrow attachment. \margin{...} for a marginal note that is not an insertion; add `% slanted` or `% margin note written sideways` where appropriate. \uline and \uuline preserve underlining. Entirely handwritten pages do not get \handwritten; on typed material it encloses only actual handwriting. Transcribe typed reused sheets and labels completely, rotate their crops as needed; inventory identifies hand/typewriter/print.

Diagrams use \diagram{\begin{tikzcd}[ampersand replacement=\&]...\end{tikzcd}} with \& cells. Include every object, arrowhead, direction, label, decoration and crossed portion. Drawings use \figure{\begin{tikzpicture}...\end{tikzpicture}}, never a prose replacement. Reproduce geometry and labels; reserve `% crop-candidate: scan N` for a genuinely complex picture after best approximation, not ordinary diagrams. A visible nonlinguistic scribble can be traced as a drawing rather than called an unreadable word; explain the choice.

Doubt: \unsure{reading}, \unsure{reading|alternative} with all candidates the ink permits and the best ink reading first. Do not preserve a doubt that the strokes resolve. \illegible{n} is only for physically unreadable WORDS after close inspection, never for math or diagram symbols. For a recurring ambiguous glyph, mark its first occurrence per page and list alternatives in notation; use the first candidate thereafter on that page. The notation table is provisional and every occurrence is still checked.

## Output files in your reader directory

1. `reading.tex`: complete page, may start from C and amend only after direct examination.
2. `report.json`: valid UTF-8 JSON with these keys:
   - `scan`, `reader`, `model`, `effort`, `started_utc`, `finished_utc`.
   - `views`: ordered image paths, full, a, b, then crops actually seen.
   - `issues`: list of objects with `id` (short local id), `location`, `C`, `H`, `reading`, `evidence` (actual strokes/marks), `confidence` (high/medium/low), `diff_C`/`diff_H` booleans, `kind` (one of: misread word; misread symbol or index; omission; text not on the page; deletion state; insertion or placement; abbreviation expanded or spelling modernised; readable ink left as \ill{}; drawing or diagram; other), `marked_in_H` (yes/no/not applicable), `crop` (relative/absolute path or empty), `bbox` ([left,top,right,bottom] on FULL image), `unresolved` (boolean). Include C doubts even when unchanged, with diff_C=false.
   - `inventory`: one object per text block, display, drawing, diagram, margin, insertion, deletion, ordered top to bottom: `element`, `kind`, `position`, `first_words_or_objects`, `sheet_kind`, `hand`, `transcribed`=`yes`.
   - `notes`: short English per-page observations on what is stated/computed/asked, own slips and explicit author doubts verbatim, folio/date/title information. Distinguish observation from checked mathematics.
   - `notation`: recurring signs/abbreviations and exact ink evidence.
   - `checks`: actual mathematical check events, with statement id, type, outcome and argument; do not call reading a proof check. Allowed types: targeted proof check; independent re-proof; computation or formal certificate; used and rechecked in this run; carried as background without fault found; refuted, with refined statement id. Leave empty when no check was done. For any mathematical statement used as background, report that limited status honestly.
   - `crop_count`, `brief_feedback` (specific omission in these instructions or unnecessary work encountered).
3. `read_log.md`: brief line-by-line/element-by-element checked register, including agreement with both witnesses, crops performed, diagrams, manuscript text behind reuse if any, and unresolved issues. Not a stream of private reasoning: record observations and conclusions only.

Write reports before returning. Your final message gives output paths, number of issues/crops, and the concrete disputed readings the main reader must decide. Do not claim the entire task is complete. Keep independent work in your own directory and preserve source files.

## Clarifications from scan 002

- The whole image, its two halves and H_drawing.tex (if present) are expressly authorized page inputs. Landscape halves are left and right. You may inspect image metadata before viewing. Report all bounding boxes in whole-image coordinates.
- For graphics, check gaps at stroke endpoints, joints, little inward returns, and separate dots as well as cell counts and labels. Preserve visible stroke geometry without inferring mathematical significance. TikZ is an approximation, not a pixel facsimile; paper grain and pressure texture are not separate objects.
- Do not invent a word count for an unresolvable scribble. Trace its ink and place a comment recording uncertainty about whether it was lettering; never use an empty `\unsure{}` node. A real uncertain word or glyph gets the appropriate in-place textual uncertainty macro.
- A heavily retraced arrow need not establish a separately cancelled older sign. Distinguish the certain live shape from an uncertain writing history; put the secure visible reading first in any alternative.
- `marked_in_H` means an actual doubt/illegibility mark at that reading. An editorial explanation, or a general statement that a drawing is regularized or partial, is not itself a local doubt mark.
- Inventory vocabulary is exact: sheet_kind is text, reused_typed, typescript, letter, list, cancelled_draft or cover. Kind is text, display, diagram, drawing, margin note, insertion or deletion. For the author’s ordinary notes use sheet_kind=text and hand=his hand. Name other or unattributed hands explicitly. Keep positions as concise location text with whole-image bbox.
- View no more than two large decision crops in one tool response; excessive image batches can be truncated. If a view result is unavailable, record that delivery failure honestly and obtain the same crop once; do not re-crop a decided locus.
- Resolve and report every C doubt, including contextual doubts not marked inline. Keep quoted editorial metadata separate from manuscript claims. No mathematical check event is earned by reading alone.

## Clarifications from scan 003

- The supplied scans are already enhanced. Your decision crops must also record the requested autocontrast/LANCZOS and any sharpening actually used; do not claim processing that was not applied. Use the lowest enhancement that keeps faint strokes. Keep tall crops to a usable size; do not send more than two in one output.
- Distinguish an attached peg from a detached dot. For a dark endpoint, inspect whether it has a small enclosed white counter before declaring it uniformly filled or hollow. Literal graphic tracing can preserve a mostly black knot with a tiny off-centre counter.
- Readable type on reused sheets is transcribed fully. Pale background remnants or a witness note about show-through do not establish additional words; say what is not recoverable without reconstructing it. The inventory’s sheet_kind describes the sheet (reused_typed for its handwriting as well as its type); hand describes the individual element.
- Compare your final reading.tex against witness C once as text, to ensure every substantive change is reported: small extra hooks and omitted marks can otherwise escape the issue list. Do not reopen images merely to perform that text consistency check.
- Equivalent l/ell macros for the same observed letter are not lexical differences. Record a source-layout difference from H’s rendered math even when H’s explanatory note correctly describes the layout, with that qualification.
- A clipped or unmatched formula remains as seen. Do not supply an index, a relation bar or a parenthesis merely because it would make the expression familiar. Every detached prime-like or exclamation-like stroke must be checked locally.

## Clarifications from scan 004

- Compare closed ascending loops with nearby open C forms before naming an argument C. A product pattern does not decide C versus looped l/ell, or a small index. Report letter identity and index uncertainty separately when one is clearer.
- A doubled F requires visible separate returning stems/white space at that occurrence. A partial upper return may leave a local alphabet doubt; do not impose either a uniform doubled alphabet or a uniform plain one.
- Distinguish visible superposed letter contours from their chronological order. If both F and O are clear but which is older is not, preserve that uncertainty explicitly at its first occurrence. A hat-like mark and a dot-like mark on the same page need not be the same sign.
- A source can contain an unjoined arrowhead, a detached continuation stub, or a point beside a formula. Preserve a clear gap/mark without assigning a mathematical function. Do not turn paper grain or mere stroke-pressure variation into additional objects.
- Pale background traces plus an editorial assertion of a typed verso do not by themselves establish a reused_typed sheet or a count of unreadable words. Classify from the visible evidence and explain the limitation.

## Clarifications from scan 005

- Verify the explicit PDF/archive-page header in H_drawing.tex before collation. Drawing suffixes enumerate drawings and are not page numbers. If its header conflicts with the current page packet, flag the mismatch to the main reader, exclude that file as page evidence, and continue the authorized page images; do not open a different scan.
- A resolution of a C doubt is a reportable difference even when its previous first candidate is retained. Set diff_C=true for removed, refined or reordered uncertainty. Merely consolidating a repeated same-page doubt at its first occurrence does not create an independent resolution; explain the later use of that candidate.
- For a vertical membership sign, describe which way the arch actually opens as well as giving rotation code. Do not inherit a rotation sign from the witness. Check each occurrence separately.
- Preserve a single horizontal relation stroke, missing inner parenthesis, or unusual boundary index when that is the ink. The expected equation is only a prompt to examine, never a correction to enter. Keep a visible wave on an arrow shaft in its actual position.
- Doubled F decisions require the full stem in the decision crop. Include the complete symbol and index plus narrow context; avoid clipping a target F or a canceled ascender to make a crop artificially tight. A partial return may warrant a local doubt, not wholesale alphabet normalization.
- Distinguish a separate underline from a letter's own terminal stroke. A cancellation can also have a low return/rule; preserve the geometry without asserting an emphasis function.
- Record which words of a canceled phrase are struck individually. For example, a canceled de before live plus must not be described or transcribed as the whole phrase de plus canceled.


## Clarifications from scan 006

- Ignore a C-context table row whose primary scan label explicitly names another page; notify the main reader so the derived packet can be corrected. Historical cross-page statements in this page's audit are witness assertions, never verified evidence from another image.
- An entirely crossed connector may be one canceled symbol/cluster. Do not preserve a separate live path merely because C drew a path with a struck label. Distinguish surviving live ink from the cancellation itself.
- Preserve labels that float between two rows, labels crossed by an arc, gaps within a curve, and a detached arrowhead. A clean conventional diagram can change the observed attachment or geometry.
- Describe rotated-sign opening direction and verify that the code in reading.tex actually matches it. A generic word such as vertical does not settle rotation. Check separate returning stems across the complete F at every occurrence, including the last object of a chain.
- In-place uncertainty at the first recurrence does not make later ambiguous forms independently resolved. Preserve distinct local limits in the issue records. If two occurrences do not support the same complete alternative set, report that explicitly so the shared convention cannot hide the difference.
- Check stops after abbreviations, isolated points beside symbols, and upper/lower label alignment. Keep marks literal without assigning a mathematical role. Do not fill a real blank or replace an unusual relation because the other readers or either witness agree on an expected expression.


## Clarifications from scan 007

- A saved crop must include the complete disputed word or symbol, including its descender, accent, terminal point and deletion contour. Report the crop's actual bounding box as metadata, separately from an approximate issue box. If an intended locus falls outside an existing crop, say so rather than claiming it settled that locus.
- A label below an operator may attach to its last letter rather than the center of the whole operator. Preserve unequal row indentation, unequal arrow starts/lengths and a label between row levels; do not automatically align every arrow in one column.
- Check each end of a reference enclosure independently. A mixed opening parenthesis and closing bracket may be what the ink shows. A detached dot above a canceled ending may support a grammatically unusual reading; retain the ink-supported alternative first.
- Follow a small inserted prefix's leader to its exact landing gap; do not turn a displaced prefix into a formula subscript. Distinguish a long insertion leader from a local word underline.
- When filtering C contextual tables, the primary scan number may be followed by a comma or description. Other-page primary labels remain excluded. A delivery failure before an image was received permits redelivery of that exact existing file once; record it separately from actual views.


## Clarifications from scan 008

- Reconcile your issue report with your final reading: if the full reading retains five alternatives, do not report only four. Quote the witness itself for each comparison; do not manufacture punctuation or doubt marks from a paraphrase of it.
- Crop boundaries must include full descenders and the entire deletion contour. Describe which elements a tall bracket encloses, including any sign above a lower formula. A bracket around two rows must not become a bracket around only the bottom row.
- Check that diagram code implements your stated geometry. If a curve endpoint is detached, leave a real gap to the object; do not end it at the node corner. Retain unequal starts and lengths of parallel rows.
- Distinguish a physically present cluster from its uncertain cancellation status. Inventory the cluster once, without presenting one disputed deletion interpretation as a definite extra physical element. Preserve isolated points and their relative positions without assigning punctuation functions from context.
- Neither consensus nor mathematical syntax removes a locally unresolved glyph. A literal traced sign may be placed inside unsure, with possible interpretations in the record, when a clean standard symbol would lose its distinctive strokes.
