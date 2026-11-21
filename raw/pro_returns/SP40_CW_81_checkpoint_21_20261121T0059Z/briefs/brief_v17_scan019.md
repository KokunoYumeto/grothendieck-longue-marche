# Independent reader brief v17 — first used on scan 019

You read ONE scan independently. Read only your assigned packet, the three images of this page, this brief, PREAMBLE.tex, and the notation snapshot. Do not inspect another reader's files or another page's images. Do not use OCR, text recognition, PDF text layers, external sources, or the internet. Do not delegate. The root will compare three independent returns and decide on ink.

## Required workflow

1. Record current UTC start time. Read C.tex, H.tex, metadata.json, C_doubts.txt and C_notes.txt for your assigned page. Notes containing other scans are context only: report only your page. Read PREAMBLE.tex and the notation snapshot supplied. H's page number is our scan minus one. H with status `nothing` or `desc` supplies no full text; do not invent H collation rows.
2. Open the whole scan ONCE with view_image for layout: text blocks, displays, margins, inserted and deleted writing, figures, and archive numbering. Then open half a ONCE and half b ONCE. Visually read every line, word, punctuation mark, accent, abbreviation, symbol, index, sign, bar, arrow and drawing against C and H. Agreement between witnesses supplies no visual evidence. Retain C wording only after seeing it.
3. List the places the halves leave open: each unsettled witness difference, every C doubt, small mathematical symbols, crowded/struck/slanted writing. Make ONE tight crop per unresolved place, with a line of context; use PIL LANCZOS enlargement to a few thousand pixels across, autocontrast, optional sharpening, rotation upright where needed. Use the supplied crop helper or your own equivalent. View each crop. Do not recrop a settled place or enlarge a whole half. A difference already settled on a half needs no crop: give a precise half-image location/bounding box so the root can adjudicate it. Include the crop filenames and coordinates in your record. If you still cannot settle it, keep explicit doubt.
4. Return a COMPLETE proposed page transcription and EVERY difference from either witness, including C doubts retained/resolved, deletion and insertion states, underlining, punctuation, omitted content, and drawing details. Macro-syntax differences conveying exactly the same reading do not count. Follow the mathematics enough to notice malformed expressions or contradictions; inspect their ink and keep the written form. No mathematical repair in the transcription.

## Conventions (authoritative current task)

Use only PREAMBLE.tex macros and standard LaTeX/amsmath/amssymb/mathrsfs/TikZ/tikz-cd/enumitem/ulem. `\cotefile{81}` belongs at the start of scan 002 only; `\scanpage{N}` at every scan. `\mspage{n}` records manuscript/typed page numbers. Archive pencilled numbers belong only in `% archive sheet number: N`.

Language, spelling, accent presence/direction, punctuation, abbreviations and numbering are diplomatic. Never expand abbreviations or modernize. His double quotes become two backticks and two apostrophes; guillemets only for drawn guillemets. Join line-end hyphenation, retain lexical hyphens. Paragraphs and text order follow the page. Every written mark matters, even cancelled, marginal or upside-down material.

`\deleted{...}` marks readable struck writing; physically unreadable struck prose may use `\deleted{\illegible{n}}`. A visible overwritten predecessor goes immediately before its live replacement. Whole-page cancellations must preserve every underlying element. `\inserted{...}` attaches at the ink's caret/arrow, `\margin{...}` holds independent marginal notes with `% slanted` or `% margin note written sideways` as appropriate. `\uline` and `\uuline` reproduce underlining. `\handwritten` is used only for handwriting on typed pages.

Letters/alphabets, indices, exponents, prime vs exclamation, directions, bars/hats/tildes, math punctuation: read their strokes. Do not choose an expected formula. Display math is `\[...\]`, multiline displays use aligned; written labels use `\tag*{...}`. `\diagram{\begin{tikzcd}[ampersand replacement=\&]...\end{tikzcd}}` reproduces diagrams. `\figure{\begin{tikzpicture}...\end{tikzpicture}}` reproduces drawings, including every label, line and cancellation. A genuine complex picture gets the best TikZ approximation plus `% crop-candidate: scan N`; no images or prose substitutes.

`\unsure{reading}` or `\unsure{reading|alternative}` marks genuine unresolved ink, the strongest visible reading first, every supported alternative retained. A recurring ambiguous symbol gets doubt at its first occurrence per page, then the first candidate unmarked. `\illegible{n}` is for physically unreadable words after zoom, never mathematical symbols: supply a marked candidate there. Keep a doubt when the strokes do not settle it; remove a doubt when they do. A doubt does not authorize omission.

## Output and independence

Write only within your assigned reader directory. Keep `reading.tex`, `report.json`, `reading.md`, crop PNGs and scripts there. No reads of other reader directories or root's decisions. You may use witness C's TikZ paths after individually checking the drawing against the scan; do not generate new prose inside the transcription. Do not copy C blindly.

`report.json` should have these keys:

- scan, reader, start_utc, end_utc, full_image_viewed, halves_viewed, complete_visual_read (booleans must be honest).
- differences: list of objects with `id`, `location`, `C`, `H` (null when H has no text), `reading`, `evidence` (visible strokes), `confidence` (high/medium/low), `kind` (the requested H collation category), `diff_C`, `diff_H`, `C_doubt_status` (resolved/retained/null), `readers_crop` (relative filename or null), `bbox` (coordinates on original full scan or identify half coordinates), `mathematical_consequence` (only when present).
- doubts: location, reading, alternatives, confidence, reason, crop.
- inventory: one object per text/display/diagram/drawing/margin note/insertion/deletion; keys sheet_kind, hand, element, kind, position, first_words_or_objects, transcribed. Use his hand, another named/unnamed hand, typewriter or print for hand. Cover, text, reused_typed, typewriter/typescript, letter, list or cancelled_draft for sheet_kind. `transcribed=yes` only for material actually in reading.tex.
- notes: page content; author's own uncertainty with exact words; title/date/page counts; mathematics-led reading decisions. Do not claim proof checks merely from reading.
- notation: visually established signs/abbreviations with location and proposed LaTeX.
- check_events: actual mathematical checks only, each statement/location, type, result; no fabricated checks. Empty list is fine.
- crops: path, bbox, rotation, purpose.
- brief_feedback: concrete ambiguity or missing convention encountered.

In reading.md give a compact line-by-line reading audit, distinguishing readable ink from unresolved doubts. Your final chat return should name your files and summarize principal differences and unresolved places. You finish after this one scan; the next scan gets new readers.

## Revision v02 after scan 002

The three readers used differing record labels because v01 omitted the collation vocabulary. Use exactly these `kind` values: `misread word`, `misread symbol or index`, `omission`, `text not on the page`, `deletion state (struck given live or live given struck)`, `insertion or placement`, `abbreviation expanded or spelling modernised`, `readable ink left as \ill{}`, `drawing or diagram`, `other`. C doubt resolution/retention alone is `other`. H-absent pages have `H=null` and `diff_H=false`.

One reader preserved the cover title's physical wrap, another joined it. Apply the stated paragraph rule consistently: ordinary physical line wrapping does not require `\\`; preserve paragraph boundaries and the explicit special cases of letters, displays and tables. A physical line-wrap formatting choice is not a witness-reading difference.

Keep each crop tight enough to expose its target but with nearby ink to identify it. Closely adjoining doubt marks on one short line may share one crop; list each reading decision separately. Do not crop a place already settled by the supplied half. Do not crop again after an enlargement remains ambiguous: record the remaining doubt.


## Revision v03 after scan 003

Sideways crops on scan 003 sometimes clipped the tops or ends of their target wording. Include the entire ink height and continuation before rotating; a tight crop must retain every ascender, descender, cancellation and insertion guide needed for its locus. Do not mistake a clipped letter for illegible ink. Inspect the bounds before creating the one enlargement.

H's `\uncertain{...}` is an editorial doubt, not manuscript underlining. `\note{...}` supplies editorial apparatus: its explanations are not additional manuscript text to be removed in collation. Actual manuscript alternatives quoted within a note remain relevant witness readings. `\add` and `\struck` correspond to insertion and cancellation. A removal of H's doubt marker with exactly the same reading is not itself a collation row. Continue recording every C doubt's resolution or retention.

Make reading.tex and report.json agree, particularly on punctuation; the separate text and report comparison on scan 003 showed the need to verify their current versions together. Distinguish the concrete ink reading from its qualification in your reports. For a group of several word endings or multiple repeated symbols, give separate local decisions when the places can change independently.

Use only the requested inventory kinds: text, display, diagram, drawing, margin note, insertion, deletion. An underline can have its own text inventory item, explicitly described as underlining. Do not add a new inventory kind.

Every difference may cite a concise original C/H substring (optional C_anchor and H_anchor) so root can locate it reliably. Crop references must name existing files relative to your reader directory; when you use half coordinates, explicitly identify a or b and the coordinate origin.


## Revision v04 after scan 004

C_doubts.txt may include both the notation table and the actual uncertainty table. A notation or abbreviation table entry is not itself a C doubt. Set C_doubt_status only for an actual uncertainty marker/locus in C. Record settled recurring notation in notation, not as an invented resolved doubt.

An editorial description can convey an overall state already: H described the two large cancellation strokes on scan004 in its introductory note, so the overall cancellation was not an H difference. Local omitted cancellations remained separate differences. Clearly descriptive orientation captions such as Encadré or À droite and a repeated member needed to explain a horizontally rewritten vertical chain are apparatus, even outside a note macro. Document this classification; do not count those descriptive words as invented manuscript prose. Ink punctuation, parentheses, braces, inserted terms and physically distinct marks still require collation.

Compare uncertainty qualifications separately from readings. The same doubtful sign with an explicit blank alternative is not automatically a new C reading. Actual resolution/removal of a C doubt is logged. Report every newly noticed mark, including a detached dot, paired ticks, a second rule or an upper stroke, and mark uncertain intention explicitly. Keep your TeX and report consistent.

Give full-scan coordinates whenever possible. For supplied halves, derive the offset from the actual image dimensions, not a remembered page size. Include the full lower extent of inserted subscripts and tall symbols. Prose locations suffice in the inventory; pixel boxes are useful for cropping but are not a separate inventory gate.


## Revision v05 after scan 005

H's supplied preamble says its transcriptions use `\emph` for Grothendieck's own emphasis. H `\emph{words}` and our `\uline{words}` therefore carry the same emphasis reading when the exact marked span agrees. Macro conversion alone creates no collation row. Read the actual single/double underline and span from the ink. The root sent this clarification individually to all three scan005 readers; it is now part of the standing brief.

For consistent counts, resolving/removing an actual C doubt has `diff_C=true`, even when its first candidate is retained. Retaining the same uncertainty, including making its blank alternative explicit, has `diff_C=false`. Always set C_doubt_status correctly. For H, a different primary candidate is a qualified difference even when H's reading survives as an alternative; make that overlap explicit in evidence/qualification so it cannot be reported as a conclusively established H error. The same reading with only a different editorial uncertainty marker creates no H difference.

A tiny detached shape may have an unresolved role and hand. Preserve its supported visible candidate with `\unsure`, its position, and an explicit note about those unresolved matters. Standard overset/underset can preserve a small mark above/below prose; TikZ can preserve relative placement of several detached groups. A shape candidate carries no inferred semantic or mathematical connection. Use `undetermined hand` in the inventory when attribution is unsettled. Supply no character for an area that supports no character candidate; document the inspected area honestly. Preserve every supported mark without turning surrounding paper texture into a supplied word.

Record the current UTC start time before packet/image reading whenever possible, and describe the actual order honestly. Do not backdate a start time. Check the final reading.tex and report.json together, including any added faint marks and their alternative shapes.


## Revision v06 after scan 006

A long crossing stroke may pass through writing in the opposite direction. Record the visible glyph and the uncertainty about the cancellation target separately; do not infer a writing chronology. An exponent may have uncertain cancellation state while its base remains readable. Use explicit alternatives in `\unsure` for the supported states.

A repeated fraction rule, hooked return, extra line or other drawn detail must actually be reproduced in TikZ. A comment describing it alongside an ordinary fraction is incomplete. Preserve its visible shape without assigning an unestablished algebraic role. Closely adjacent local details can share one drawing and one crop, with separate decision rows where their readings can vary independently.

Scan006 prose crops clipped a predecessor ascender and a word endpoint; another crop stopped too tightly at a formula ending to settle H's punctuation. Plan the first crop to retain all ascenders, descenders, insertions and the adjoining endpoint space. Inspect source bounds before enlargement/rotation. Do not crop a decided place again; disclose any remaining boundary limit honestly.

H's commas, full stops, semicolons and parentheses attached to manuscript expressions require comparison with ink. The descriptive-caption exclusion does not automatically exempt endpoint punctuation. The final record counts one whole omitted passage or one ill placeholder once against H; local C doubts or changes within it remain separately reported with a cross-reference and diff_H=false. Preserve any source-level flags transparently. H's movement of a factor from a shared numerator to outside the fraction is a placement difference even when an explicit algebraic correspondence exists; simple quotient macro conversion alone is excluded.

Do not propose reconstructed or conditional theorems in the notes. A concrete mathematical computation must state its exact objects, generator assignments or other map, and actual outcome; it never repairs the ink. Every check or explicitly used/rechecked mathematical correspondence receives an honest check-event entry. Merely transcribing a statement is not a check. Empty check_events remains appropriate when no such work was performed.


## Revision v07 after scan 007

Count duplicate C-doubt-table entries for one physical locus once, and explicitly map both source entries. A solid cancellation can preserve one compact unreadable item without revealing its original word count; state that limitation honestly.

Distinct paired cancellation strokes may be reproduced graphically while retaining the deleted wording. Do not introduce or redefine macros, or change PREAMBLE.tex. For explicit inline TikZ cancellation paths, standard boxing can preserve the supplied deletion annotation without a generic extra visible stroke: the node content `\rlap{words}\phantom{\deleted{words}}` draws the words once and takes their dimensions from the invisible deleted copy; draw the actual cancellation paths over that node. Keep the surrounding prose in its original order. Explain such a geometric addition separately from an unchanged cancellation state.

Include archive numerals in the inventory even when the transcription records them only in a comment. Confidence concerns the recovered reading: an unreadable original item remains low confidence even when the presence of its cancellation is clear. Report all further unresolved formula/candidate loci that prompted crops, including their resolutions without a witness change, in the audit or notation rather than inventing a C difference.


## Revision v08 after scan 008

The extracted C_doubts and C_notes now preserve their source section headings and table headings. Count actual rows in the source's doubtful-readings section, including a row whose C.tex has no unsure macro. Keep notation and retained-spelling rows in their original categories. Duplicate mentions of the same physical locus remain one doubt.

An apparent extra punctuation mark can belong to the neighbouring line. Preserve enough neighbouring context in the planned crop to establish that placement, and map the source coordinates before proposing a second copy. On scan008, the lower curved mark beside the pale formula was the apostrophe of C'est below; the complete note crop showed its attachment. Preserve visible detached marks with their uncertainties; gray residual shapes can be drawn without inventing a character or role.

Connected rules and frames require one drawing that preserves the connection. Standalone versions can hide a shared boundary even with all text present. Mark any crop boundary that clips part of a connected feature honestly; do not repeat a settled crop.

Use structural source checks only. Do not invoke pdfLaTeX, LuaLaTeX, XeLaTeX, latexmk, TeX format builders, or any compiler, and do not install packages. The three scan008 compiler attempts failed before page processing because format files were unavailable. No successful compilation or render validation is claimed. Check braces, environments, delimiters, macro names, reading/report consistency and file references directly.


## Revision v09 after scan 010

A single C doubtful-readings row can name several separated physical regions. Preserve its source-row identity and report each local sublocus explicitly. Count the source row once; do not silently attach a neighbouring doubt through a shared crop. Keep every source doubt, local candidate and crop mapping traceable.

For a drawing with uncertain cancellation state, mark that uncertainty on the local graphic itself. Draw the observed cancellation strokes and preserve the supplied deleted annotation by standard invisible boxing where needed; do not add a generic horizontal rule absent from the ink. A mere wrapper change carries no independent change count; altered visible geometry must be identified.

Decide filled/open vertex candidates from each local rim, light centre and hook. A neighbouring graph or an expected classification supplies no fill reading. A supported shape with an unsettled hand, role or surface origin stays graphical. Give the visible path confidence separately from its unresolved interpretation, and retain pale interruptions and detached pieces.

Compare inventory descriptions with the actual TeX paths. An inventory saying three strokes while four are already reproduced requires an inventory correction, explicitly mapped to the four paths; it creates no additional transcription change. A new detached mark discovered in that crop still requires its own path and record. Include all target endpoints in the first planned crop; disclose a faint continuation reaching a boundary without recropping a settled place.


## Revision v10 after scan 011

Use genuine tikz-cd for a diagram, with standard local TikZ nodes or end-picture overlays for overwritten letters, detached strokes and retraced arrows. Free TikZ belongs inside the figure macro for drawings. Keep the diagram's observed detached pieces detached; preserve their entire supported endpoints without inferred connections.

A readable glyph and its cancellation target can have separate confidence. Record both, including explicit cancelled/live alternatives where the strokes leave the target open. The correction count for a shared physical glyph/state cluster is one per witness; cross-reference the additional local qualification and retain it in the changes log. The original C source-row map remains separate from this physical-locus count.

Tiny detached strokes newly observed in a crop require their own graphical representation and inventory item. A supported path can have high shape confidence while its role, hand or surface origin remains unknown. Inspect thin continuations, gaps and lower ends within the planned crop. Give every report difference and every remaining doubt an explicit local entry with its exact location, evidence and source-row identity. Keep reading.tex and report.json synchronized before returning.


## Revision v11 after scan 012

A packet can end with a heading or note that explicitly names another sheet. Record the boundary from the supplied text and exclude that contextual tail from this scan's transcription and collation. H's own rereading correction is read together with its initial description: compare the integrated witness reading to the ink.

Map all proposed graphical additions to exact physical components. Two slightly different bounding boxes can identify one feathered small patch; preserve both source reports and count the physical mark once. For a multi-component graphical cluster, keep each local component and its confidence explicit while giving the shared physical cluster one witness-change count. Preserve source-doubt-row identity separately.

For source drawings made of filled contour blocks, keep a local path map and confirm every original component and text label against the half images. A proposed new point can already be a short excursion inside a larger source path; inspect the literal source coordinates before adding a duplicate. Every newly retained path requires an inventory entry or an explicit component entry for its local cluster. A short thin-line candidate and a filled wedge candidate must be identified by their actual source commands, not by an assumed shared shape name.

Display crops one at a time when tool output limits threaten image delivery. An image dropped before it is shown has not been viewed; retry the same existing image file and disclose the failed unseen attempt. Do not make a new crop for that retry. Do not reopen a successfully inspected and decided image.


## Revision v12 after scan 013

Read a cancelled predecessor from its own surviving strokes. A later live form and a witness-table explanation based on that live form do not supply the predecessor's missing stroke. Record the actual C source doubt separately from a newly discovered state uncertainty: a glyph can be resolved while its cancelled/live status remains open. Preserve the original source-row identity, including separately named local parts of one compound row.

For a ruled table, reproduce each visible run, interruption, curvature and endpoint. Do not force regular spacing or a complete grid where a faint division remains uncertain. A whole-rule source path supplies surrounding context; a local filled wedge requires its own exact component identification. Distinguish path-command counts from disconnected visible components: one command can contain several disconnected runs.

When combining local TikZ fragments, state the actual coordinate and dimension maps and use fixed origins. Confirm the selected body once, including ordinary text labels and archive-number comments. Preserve the fuller selected qualified glyph without drawing its separately reported component strokes a second time. In the inventory, use the final reading and state wording, retain original reader descriptions in provenance, and order items by their supported page positions.


## Revision v13 after scan 014

A supported detached shape can remain graphical while its character, role, hand and surface origin stay unresolved. Put the selected shape under a local unsure qualification and give its exact source component; a prose observation alone does not draw it. Do not supply letters for diffuse shading that yields no discrete candidate. Keep observed locus boxes distinct from the actual bounds of approximate Bézier paths: both remain documented, and fixed local rectangles preserve the selected origin.

An insertion macro preserves the added wording and its attachment. A separately visible long bent or hooked guide also requires its observed path. Record that geometry as a local addition while retaining the unchanged insertion state and wording. Fixed placement or typography alone supplies no lexical correction count. Archive-number inventory attribution remains explicit; retain undetermined hand when the local evidence does not identify a writer.

## Revision v14 after scan015

Compare the complete proposed TeX with the report, including physical order and every explicit cancellation or guide path. On scan015 one report described a crossed inclusion to the left of equivalence wording while its TeX left the old order; two added crossing paths appeared in TeX without dedicated report differences. Give those source choices explicit local records. A compound source row with one resolved part and one retained part keeps both statuses and its single original identity.

Before making the one enlargement, plan the target's complete continuation and long descender endpoints from the full-resolution half. On scan015 two lower-note crops stopped within the right-hand ending; equivalence and symmetry crops cut descender endpoints. Preserve the deciding word, all its ascenders/descenders and any endpoint punctuation in the initial crop. Disclose clipping honestly without reopening a decided place.

A nested unsure graphic changes the node's dimensions. A centre anchor alone does not establish the inner path's full-scan origin. Use a declared local origin, baseline and base-west anchor, zero inner/outer separation, consistent x/y units, and explicit scope translations for selected literal path bodies. Keep the observed locus box separate from the drawing rectangle and the font extents. Source-coordinate declarations do not require optional curve-extrema computations. Preserve each physical stroke once when one fuller selected component incorporates an overlapping report component.

Keep each confirmation of an S bar distinct from a current-witness correction. A current C/H expression may already contain the confirmed bar. H's one drawing-description replacement and one whole ill placeholder each receive one physical parent count, with all independently variable local details logged under it. Give uncertain glyphs, graphical shapes and unestablished roles their own local confidence.



## Revision v15 after scan016

A compound doubt-table entry can qualify a second repeated occurrence even when C.tex prints that occurrence without an unsure macro. Preserve the table's actual local scope. On scan016 the original row12 covers both final joins and their old/live components. A recognizable square-form glyph and an uncertain cancellation/replacement sequence require explicit complete-state alternatives; do not let a resolved component silently remove the state doubt.

Report literal brace paths and other graphical additions that appear in your TeX, including their endpoint spans and disconnected components. A comma represented graphically remains the same physical punctuation locus; retain the selected representation once. Compare H's transcribed body and its drawing apparatus together. A repeated formula inside an apparatus note identifies an existing physical locus and creates no second manuscript occurrence.

Give the exact source-coordinate convention without optional image-comparison calculations. Any computation actually performed, including a finite pixel-difference calculation, must be disclosed with its fixed inputs, mapping, recorded result, and actual scope; an empty mathematical-check array must not conceal it. No alignment or identity result follows from a label in a script. The root will record the actual event without rerunning it.

Before cropping a correction beside a live continuation, include the full target chosen from the half. A formula or bracket at the physical page boundary may preserve only partial strokes. Draw those surviving parts and retain the interpretation locally qualified; do not supply an unseen connection. Preserve any unresolved word ending or accent locally, including an explicit blank candidate for an absent ending when that is the selected primary reading.

Keep empty physical lines outside display-math delimiters and math environments: an empty line introduces a paragraph token. When inserting a selected TikZ fragment into a display, preserve its content without adding such an empty line, and update exact source offsets after any source repair.

## Revision v16 after scan017

A detached point near an indexed letter can also be that letter's displaced dot. Compare the full local group before adding a second printed mark. Preserve the point's visible position and unresolved attachment once; a selected dotless-letter node plus one explicit point must stay together as its complete source group. A literal shape does not establish a prime, an operation, punctuation, or a particular hand.

Plan a marginal crop to include any neighbouring letter that may continue a small edge fragment. On scan017 a narrow reported wedge was resolved by the root's first complete-context crop as part of the main word Soit. Preserve the glyph through its actual word, and map a proposed separate path to that same component without duplicating it.

Audit every proposed TeX spelling, mark and state against the report, including an unreported unchanged witness spelling that differs from another reader. Scan017 required separate source anchors for three live accented words, a plain exponent, an absent baseline point, and the dotless-index group. Keep independent physical words separate even when their spelling is the same.

Retaining the same primary reading with a different editorial uncertainty marker alone creates no H collation count. A changed primary with H's reading as an alternative remains a qualified difference. Original C doubt resolutions and retentions keep their explicit status and source identity. Apply the recurring-glyph rule exactly: mark its first occurrence on each page, then print the same primary unmarked, while recording every independently inspected local occurrence and any source-table doubt at that occurrence.

Read complete adjoining words when selecting a guide group: one source may include de, another de X, and another neither. Every live word and inserted label must occur once in the consolidated source. Retain manual geometric approximations honestly and do not claim rendered or metric validation from source declarations.


## Revision v17 after scan018

An original C doubt can concern a visible mark's attachment, role or cancellation state as well as its presence. Clear presence alone does not resolve an original attachment or state question. Preserve the exact source-table scope, including expressly named parts, later contextual recurrences and each independently inspected local occurrence. Keep a later recurrence's local alternative in the report even when the first-occurrence rule prints that later glyph without another unsure wrapper.

Public reader readings must expose what the complete source actually selects, including report-silent words, accents, punctuation and absent graphical components. A source that prints a recurring circle while retaining zero in its doubt list has both facts recorded. A source that draws a hook as a definite guide return must say so alongside a source that retains punctuation/guide uncertainty. State local hand uncertainty separately from an adjoining word's established hand.

Select and report complete graphical groups with their adjoining words, insertion/cancellation state, qualifiers, origin and baseline. A selected group can already contain classe, de, ne, a formula, a comma or a period. Identify those exact boundaries so the consolidated source preserves every word and mark once. Preserve exact source excerpts and state an absent separate component only within its inspected complete source span.

Record UTC before reading the packet. Bound text output to prevent truncation; display one image per tool call. After an interruption, resume the same reader context at the first unviewed target. Keep honest logs of failed unseen image deliveries, and never reopen an image already delivered successfully. Use literal single-backslash LaTeX commands in actual files; JSON escaping belongs only to the serialized representation.
