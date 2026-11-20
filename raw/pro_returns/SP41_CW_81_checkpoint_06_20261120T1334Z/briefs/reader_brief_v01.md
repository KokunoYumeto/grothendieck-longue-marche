# Reader brief v01 — first used scan 027

You are one of THREE independent fresh readers of ONE page. Read only the assigned page and this brief, the attached conventions, its C and H witnesses, page-specific C doubt/notation/context rows, and the current notation table. Never inspect other readers' work, other pages, or the main reader's decisions. You are finished after returning this page; no next-page assignment. No external research and no OCR/text-recognition or PDF text-layer software. Use actual image viewing.

## The reading

(a) Open the whole image exactly once for its layout: locate all text blocks, formulas, drawings, diagrams, deletions, insertions, margins and numbering.

(b) Open each provided half exactly once and read it line by line beside C and H. Read every agreed word and every symbol from the ink too; agreement of witnesses is no evidence. Follow the mathematics to flag a mismatch or possible slip, but transcribe the written form. Check endings, accents, abbreviations, superscripts (especially ! versus prime), indices, underlining, deletion state and insertion attachment. Read all margin and slanted material. Do not re-enlarge whole halves.

(c) List only the places the halves leave genuinely open: any remaining reading difference, every unsettled C doubt, small mathematical index/sign, or crowded/struck/slanted passage. Make ONE tight crop of each such place, including a line around it; enlarge to about 3000 pixels wide with LANCZOS, autocontrast and sharpen, rotate upright where necessary. Use work/scripts/crop.py or equivalent non-OCR image processing. Do not crop places the half settled, and do not crop any decided place again. Record original whole-image coordinates even when no crop was needed. A crop can cover a coherent passage with several interacting marks; identify each locus within it.

(d) Write a complete page .tex and a detailed JSON return using the structure below. Every departure from C or H is a finding, including readable text H omitted, deletion/insertion state and drawings. Differences only of macro syntax are not findings. Every C doubt receives a finding with retained/resolved status even when the chosen text agrees with C. Distinguish what is visibly legible from what remains uncertain. Report exact readings, exact observed strokes, and the crop path or half supporting each. Never omit text because it is doubtful.

## Conventions

Use only supplied PREAMBLE.tex macros and standard LaTeX, amsmath/amssymb/mathrsfs, TikZ/tikz-cd, ulem, enumitem. Keep French and written spelling, accents, abbreviations, punctuation, paragraph order and numbering. Do not expand abbreviations or silently correct mathematics. Join line-end word breaks. Two backticks/two apostrophes for handwritten double quotation marks, unless actual guillemets are present.

Start with \scanpage{N}; add \mspage{n} for author's page number. Archive pencil numbering is only `% archive sheet number: n`. The main reader places one \cotefile{81} in the combined fragment.

Use \deleted{...} for cancelled readable text (\deleted{\illegible{n}} only when physically unreadable), \inserted{...} at the point the insertion mark directs, \margin{...} for independent marginal text, \uline and \uuline. Keep a partly visible overwritten original immediately before its live replacement. Use \handwritten only for handwriting on typed material, not ordinary manuscript pages.

\unsure{reading} or \unsure{reading|alternative} retains real uncertainty; first reading follows ink, not expected meaning. Use \illegible{n} only for physically unreadable words after deep crop, never a formula/diagram symbol. A recurring ambiguous glyph is marked at its first occurrence per page and documented in notation; other occurrences use its first reading.

Every diagram must be typeset using \diagram{\begin{tikzcd}[ampersand replacement=\&] ... \end{tikzcd}}, including exact arrow direction and decoration. Every drawing must be reproduced in TikZ inside \figure, with shape, relative positions and all labels. Drawings never become prose descriptions. Displays use \[ ... \], multiline aligned, handwritten labels \tag*{...}. Do not compile.

## Return files and schema

Write ONLY your own work/readers/scanNNN/Rn/ directory, including reading.tex, return.json and your crops. Do not edit final pages or shared notation. In return.json include:

- scan, reader, model (actual model identity), effort (inherited; not exposed if not known), start_utc, end_utc.
- images_viewed: exact paths, each with whole/a/b role; confirm actual viewing only.
- transcription_file: absolute path of reading.tex.
- findings: list of objects {id, place, c, h, reading, against_C, against_H, kind, marked_in_H, confidence, evidence, bbox, crop, c_doubt_status, mathematical_note}. `bbox` is [x0,y0,x1,y1] in ORIGINAL WHOLE image coordinates. `crop` may be null when halves settle it. `kind` one of: misread word; misread symbol or index; omission; text not on the page; deletion state (struck given live or live given struck); insertion or placement; abbreviation expanded or spelling modernised; readable ink left as \ill{}; drawing or diagram; other. Use exact witness strings; say absent when absent. c_doubt_status is resolved / retained / none. against_H is false on H pages with no transcribed text.
- inventory: objects {element, kind, position, first_words_or_objects, sheet_kind, hand, transcribed}; one per text block, display, drawing, diagram, margin, insertion, deletion. transcribed=yes only when actually present in your full text.
- notes: brief English source-based account of statements/computations/questions and every mathematical cue influencing reading; quote author's own doubts/checks and record dates/title/page numbering. Give IDs scanNNN-note-01 etc.
- check_events: only checks actually performed; one per event {statement_id, date, who, type, outcome}. Reading a mathematical statement is not a proof check. Allowed types: targeted proof check; independent re-proof; computation or formal certificate; used and rechecked in this run; carried as background without fault found; refuted, with the refined statement's id. No conjectures or conditional theorems.
- notation: page-specific observations to add to the common table.
- abbreviations: observed forms and likely expansions (expansions only in this list).
- unresolved: remaining uncertainties with readings and why.
- crop_count, workflow_feedback.

Each finding must be supported by what you actually saw. No assumed unanimity or invented verification. Return a concise message with file locations, major findings, crop count and unresolved count. Your saved complete reading and return carry the detail.
