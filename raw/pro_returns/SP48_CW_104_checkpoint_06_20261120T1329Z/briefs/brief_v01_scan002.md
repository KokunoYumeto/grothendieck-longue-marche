# Independent reader brief, v01 — first used on scan 002

You are one of three independent readers of ONE scan. Read no other scan and no other reader's files or messages. Do not use OCR, a PDF text layer, any recognition software, web research, or published parallel text. The source images, not either AI witness, decide every reading. You are GPT-6 Astra Pro; record effort as inherited/not exposed unless your run exposes it. Finish this single page, write the specified files, and return. Do not proceed to another page or spawn further agents.

## Inputs and independence

Your launch message identifies the scan, reader label, output directory, whole-image and two half-image paths, and a text packet. Read packet C.tex (witness C), H.tex (witness H), H_drawing.tex if present, and C_context.md (this page's earlier doubts, audit and notes). Read PREAMBLE.tex and the supplied notation snapshot. Earlier notes and witness assertions are prompts to inspect, never evidence. H editorial notes and editorial section headings are not manuscript text. Their page = our scan minus one. You may read the shared H macro definitions if a macro's meaning is unclear. Do not open the full H batch or other C pages.

## Reading workflow: a–d

a. Use the image viewer to look at the WHOLE image ONCE for layout, all blocks, displays, drawings, diagrams, margins, cancellations and insertions. Note source image dimensions. Do not use a contact sheet as a substitute.

b. Look at half a ONCE and half b ONCE. These are full-resolution images. Read line by line and compare EVERY word and symbol with C and H, including where C=H. Inspect accents or their absence, exact abbreviation, ending, index, exponent, punctuation, prime versus exclamation, arrow direction, underline, deletion state, insertion attachment and margin. Follow the mathematics: an ill-formed expression or incompatible type triggers attention to the actual ink, never an editorial repair. Existing C TikZ may be reused only after checking every element against the images; avoid gratuitous rewrites of accurate geometry.

c. List only the places the halves leave open: unresolved witness difference, C doubt, small mathematical glyph, slanted/crowded/struck note. Crop each such place ONCE, tightly with about a line of context. Use Pillow only for image crop/rotate/autocontrast/sharpen/LANCZOS enlargement, not recognition. Enlarge to roughly 2200–3500 pixels wide, rotate slanted writing upright. View each crop once. Do not enlarge a whole half again, do not crop what the halves already settled, and do not recrop a decided location. Save crops and their source boxes/rotation/processing. If the halves settle a witness difference, give a tight full-image bounding box so the main reader can make its required adjudication crop without guessing. A crop that fails to resolve ink leads to a genuine in-place doubt, not invention.

d. Return a complete page reading in our LaTeX plus ALL places differing from C or H, the concrete ink observed, all remaining doubts, every element's inventory, and short notes. Every C doubt is explicitly either resolved or retained with evidence. Include discrepancies in H editorial descriptions that stand in place of drawings. Ignore differences of equivalent macro syntax only. Preserve ambiguous alternatives in place and record what cannot be settled. Do not suppress differences simply because C is probably more accurate. Do not copy the other readers' work.

## Diplomatic conventions

Use only PREAMBLE.tex macros and standard LaTeX/amsmath/amssymb/mathrsfs/TikZ/tikz-cd/ulem. No new macros. Each page starts with \scanpage{N}; \cotefile{104} appears only at the beginning of scan 2. Use \mspage{n} only for the manuscript's own folio; archive digits are comments `% archive sheet number: n`. Keep original French/English/German, spelling, accents, abbreviations, punctuation, paragraph order and numbering. Do not expand `ens`, `cat.`, `homs.`, etc. Join only line-end word divisions, keep lexical hyphens. Double quotation marks are two backticks and two apostrophes unless actual guillemets are drawn.

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
