# Independent reader brief v03 — first used on scan 004

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
