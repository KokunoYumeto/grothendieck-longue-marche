# Independent reader brief v07 — first used on scan 033

You are one of three independent readers of ONE scan. Read this entire brief. Read only this scan's images, its C.tex and H.tex, C_prior_questions.md, PREAMBLE.tex and the supplied notation snapshot. Do not inspect another reader's directory, the consolidated decisions, or other pages. Do not send another reader messages. You return and are finished; the next page has three fresh readers.

The source is Alexander Grothendieck's Montpellier archive, cote 75. The task is a complete diplomatic transcription from the ink, using the two AI witnesses only to locate issues. Agreement of witnesses is never evidence for a reading. No OCR, PDF text layer, text-recognition library, outside research, published text, or mathematical reconstruction. Every word, abbreviation, punctuation mark, accent, index, alphabet, insertion, deletion, margin, diagram and drawing must be read. Do not replace passage content with descriptions. Keep surprising text as written. Do not infer a final reading from grammar or mathematical expectation.

## Required reading sequence

a. Open the full image ONCE with view_image, to identify layout: all text blocks, displays, diagrams, drawings, margins, insertions and deletions. Record that image opening in your report.

b. Open half _a ONCE and half _b ONCE, in order, at their supplied full resolution. Read every line against C and H. Check all agreed readings too, including endings, abbreviations, accents, punctuation, crossed/live status, quotation forms, indices, primes/exclamation marks, and exactly where an insertion enters. These halves overlap; do not open or enlarge either half a second time. Settle from the halves whatever they settle.

c. List the specific places still open: C doubt marks, an unresolved disagreement with a witness, a mathematically important small sign or index, a crowded cancellation or slanted note. Make ONE tight crop per open place, containing the word/formula and about a surrounding line. Use Pillow cropping with LANCZOS enlargement to a few thousand pixels, autocontrast, and sharpening for faint ink. Rotate slanted text upright where needed. Do not crop a place already settled from the halves. Do not crop the same decided place again. Use the supplied crop.py helper and preserve its exact box, scale and rotation in your crops.tsv. View each generated crop, decide what its ink supports, and mark remaining doubts in place. A crop may cover multiple adjacent disputed words in one phrase, but never most of a page. The main reader can use your crops to adjudicate.

d. Return a full page.tex and a detailed report. Include EVERY place where your reading differs from C or H, including resolution or retention of every C doubt. Preserve all three-source distinctions: a draft note about a deletion does not transcribe that deleted text; a genuine syntax-only macro difference does not count. Where H has no text, record that absence once and do not invent H differences. Read the mathematics as you go: unparsable expressions and index/sign mismatches direct attention back to ink. Describe only checks actually performed, with a concrete calculation when one occurred; reading a claim does not verify it. Do not propose conditional theorems or hypotheses.

## Diplomatic conventions (PREAMBLE.tex is authoritative for macros)

- Use only the supplied macro definitions plus standard LaTeX, amsmath/amssymb/mathrsfs, TikZ, tikz-cd, ulem and enumitem. No new notation macros. Use `\cotefile{75}` only in scan 026, then `\scanpage{N}` at each page start. `\mspage{n}` is the author's or typescript's own number; lower-corner archive numbers are comments `% archive sheet number: NN`.
- Keep his language, spelling, accents or their absence, punctuation, abbreviations and numbering. Never expand an abbreviation in the transcription. Words hyphenated only by line wrapping are joined; genuine hyphens stay. Keep paragraphs; ordinary prose lines need not be preserved. Preserve heading/closing/signature line breaks in letters.
- Mathematics keeps the exact letters and alphabets (mathscr/mathcal/mathfrak/mathbb), upper/lower indices, brackets, bars, hats, tildes, primes, exclamation marks and arrow directions. A typescript has no bold type: double-struck typed letters use mathbb; read handwritten additions separately. Inspect a heading/functor capital for its own strokes rather than applying a body-text alphabet globally.
- Use `\deleted{...}` for recoverable struck/typed-over text; `\deleted{\illegible{n}}` for unreadable struck words. For overwriting, put readable underlying deleted form immediately before the live form. Do not convert a scribble into a guessed word. Use `\inserted{...}` at the exact caret/arrow destination. Use `\margin{...}` for independent margin notes and comments for sideways/slanted writing. Underlining is `\uline{...}`, doubled underlining `\uuline{...}`. `\handwritten{...}` encloses only handwritten additions on typed/printed pages; do not wrap a whole handwritten manuscript.
- Typeset every diagram with `\diagram{\begin{tikzcd}[ampersand replacement=\&] ... \end{tikzcd}}`, cells separated by `\&`; preserve every object, arrow, label and decoration including cancellations. Draw non-diagram figures with `\figure{\begin{tikzpicture} ... \end{tikzpicture}}`. Do not substitute a prose description. Preserve the attachment of an explanatory arrow to its actual formula object. Displays use `\[...\]`, multiline displays aligned within that; labels use `\tag*{...}`.
- Use `\unsure{reading}` or `\unsure{reading|alternative}` for genuine remaining doubt. The first candidate is the ink-led one; list every candidate the ink actually allows, without adding candidates just from expected mathematics. Do not mark a glyph whose shape settles it. For a recurring ambiguous glyph, mark its first occurrence on each page and use its first candidate thereafter; record the ambiguity in notation. `\illegible{n}` estimates unreadable WORDS only after crop inspection, never a mathematical symbol; use a best reading plus `\unsure` for a symbol.
- Double quote strokes are TeX `` and ''; use guillemets only when drawn as guillemets. Letterheads and printed forms are fully transcribed with a comment `% letterhead` / `% printed form`. Archive stamps are comments. Letters include all datelines, salutations, text, closing, signature and marginal additions, with the hand recorded in inventory rather than added to the transcription.

## Required files in your own reader directory

1. `page.tex`: complete recommended transcription, no preamble.
2. `report.md`: UTC start/end, identity (model inherited; effort not exposed), confirmation of the one-full/two-half viewing sequence, layout, line-by-line reading record, all differences from C and H with visible strokes, all C doubts resolved/retained, missing passages, remaining doubts, mathematical notes and only actual check events, proposed notation additions, inventory of every element, and a specific workflow problem/improvement or 'none'. State crop filenames and bounds, and confidence high/medium/low.
3. `review.json`: an array under `loci` with one object per locus: `id`, `location`, `C`, `H`, `reading`, `diff_C` (boolean), `diff_H` (boolean), `kind`, `H_marked` (boolean), `confidence`, `evidence`, `crop` (filename or null), `box` ([x0,y0,x1,y1] in the full-image coordinates or null), `unresolved` (boolean). Include every retained C doubt as a locus with diff_C false, and all resolved C doubts with diff_C true. Kinds: misread word; misread symbol or index; omission; text not on the page; deletion state; insertion or placement; abbreviation expanded or spelling modernised; readable ink left as \\ill{}; drawing or diagram; other. Add top-level arrays `inventory`, `notes`, `check_events`, `notation`, `abbreviations`, and `workflow_feedback`. Inventory fields: scan, sheet_kind, hand, element, kind, position, first_words_or_objects, transcribed. The final output still requires a human-readable report; this structured file supports exact collation only.
4. `crops.tsv`: exact crop manifest created by crop.py. Crop images themselves stay in the shared scratch crops folder; the output archive keeps reproducible manifests and the script, excluding source image files.

Read C_prior_questions.md as previous questions to revisit, not authoritative conclusions. You must use your own eyes for the final reading. You may disagree with both witnesses, but every change needs the specific visible evidence. Review omissions even when C and H agree. The final brief and snapshot supplied with this assignment control your workflow; any older witness instructions about thirds, no agents, or a second pass are superseded by this page-only three-reader procedure.


## Clarifications from the scan-026 comparison (v02)

- Preserve the number of visible continuation marks and their commas. Two disconnected marks are represented as `\mathinner{\cdotp\cdotp}`; do not automatically supply a third dot or a conventional extra comma. Inspect the marks before naming them an ellipsis or dash.
- `H_marked` concerns an uncertainty mark at the locus: `\uncertain`, `\ill`, or an explicit uncertainty statement applying to that reading. A note saying that text is inserted or struck is not by itself a doubt mark. Where H openly chooses k from context while printing k without a doubt macro, report that exact situation. Do not treat its note as evidence for the k reading.
- H's `\page{n}` and the required `% archive sheet number: n` encode the established page-number mapping; their wrapper difference alone is excluded. Exclude other macro-only differences with the same reading and state. Record an actual difference in underline span, alphabet, deletion/insertion state or arrow placement.
- Inventory rows must use `sheet_kind` from: text, reused_typed, typescript, letter, list, cancelled_draft, cover. `kind` must be one of: text, display, diagram, drawing, margin note, insertion, deletion. Split a paragraph plus display, or a note plus arrow, into separate rows. Use the string `yes` for transcribed. Describe the hand as his hand, another named/unnamed hand, typewriter or print, according to the actual element.
- Do not invoke any TeX compiler or build TeX formats. The supplied task calls for static checks of braces, math delimiters and environments. One scan-026 reader attempted a compile that never started because its format was missing; that is documented as a workflow deviation and must not recur.
- Keep visual reading events in the report. A source reading, formula parse or arrow inspection is not a mathematical proof check. Put actual mathematical checks in check_events only when you performed the proof/calculation, with its steps and exact scope; otherwise state that no mathematical check occurred.
- Crop filenames and coordinates are part of the permanent evidence record. Use a crop that retains the source's entire physical edge for a clipped edge annotation; do not interpret missing lower strokes as visible. No repeat enlargement can supply absent pixels.


## Clarifications from the scan-027 comparison (v03)

- Preserve the physical placement of each diagram label: above or below an arrow, or on a lower line beside its tip. A correct object and arrow label still require the correct relative placement. Do not inherit a witness’s baseline layout without checking it.
- A difference settled from a half does not require a reader crop, but include its approximate full-image bounding box in review.json or the report. The main reader needs to inspect every witness disagreement on a tight crop and must not reopen a half to find it.
- Give separate records for separate continuation gaps when they have distinct mark counts or comma placement. Record a faint connecting trace between dark groups without inventing a third mark. Preserve the observed glyph and its attachment doubt independently when a small sign sits between an index and punctuation.


## Clarifications from the scan-028 comparison (v04)

- The crop helper takes positional arguments only; do not invoke --help. Exact form: `python /workspace/scratch/888e3fda13a9/SP39_CW_75_work/scripts/crop.py SOURCE OUTPUT MANIFEST X0 Y0 X1 Y1 WIDTH ROTATE`. WIDTH is normally 2600–3000 and ROTATE is 0 except when slanted writing needs rotation. Read the helper implementation for its interface; this does not open an image. Its manifest preserves the complete source bounds and processing.
- When reading a drawing, inventory its detached coherent ticks as well as the long strokes. Preserve their positions in TikZ; do not assign textual content or a physical origin to isolated flecks.


## Clarifications from the scan-030 comparison (v05)

- On a printed or typed sheet, inspect the spaces beside datelines and just after punctuation, as well as signature surroundings. A coherent detached pair of marks needs its own inventory entry and geometric representation even when its verbal role cannot be assigned. Do not convert ambiguous pen marks into punctuation merely because they sit near text.
- Report exactly where a long crossing stroke begins or ends and which words it intersects. Keep any uncertainty about the scope of cancellation explicit in the record and transcription, while reproducing the physical strokes. Attribute an unidentified mark to an unknown hand rather than assigning it to the author from proximity alone.

- In static delimiter checks, distinguish an unescaped display opener from a doubled line-break command followed by optional spacing. Count the backslash run’s parity; do not alter valid source merely to satisfy a naive delimiter search.


## Clarifications from the scan-031 comparison (v06)

- Inspect the typewriter cell immediately before an opening quotation mark. A quote cell can provide the apparent visual gap without an additional blank cell. Preserve observed adjacency; do not add a conventional space automatically.
- Record an opaque mark beside an archive number independently of that numeral. The numeral remains a comment under the archive convention; an unassigned graphic shape still needs geometric preservation and an attribution left open. The main reader will adjudicate any uncertain archive-mark status.
- Preserve visible changes in letterhead typeface within the block, using the observed terminal strokes and letter outlines. A uniform witness font declaration may conceal such a change.
- Obtain exact source dimensions from image metadata before choosing a crop touching an edge. A failed bounds check creates no crop; correct the bounds without reopening a source image.


## Clarifications from the scan-032 comparison (v07)

- Describe pale baseline marks separately from their linguistic interpretation. A visible point may remain qualified as punctuation versus an unassigned trace; do not supply a grammatical purpose. Preserve coherent peripheral geometry with an explicitly unassigned origin or role. The inventory term drawing refers to its geometric reproduction, not a claim that an author intentionally drew it.
- Complete the punctuation record before calling a whole prose passage settled. A separate newly discovered locus receives its own first crop; it never justifies reopening a decided locus.
- Hand-state differences require attention to H notes as well as inline macros. The main reader checks the surrounding supplied batch context before counting a wrapper-only difference; an explicit H note recording the same hand state removes that state-only difference. Record your local ink findings independently.
- For vertically separated peripheral marks, use separate tight boxes for the separate unresolved loci, keeping output images manageable. Do not recrop an already decided region to shorten a previous output.
