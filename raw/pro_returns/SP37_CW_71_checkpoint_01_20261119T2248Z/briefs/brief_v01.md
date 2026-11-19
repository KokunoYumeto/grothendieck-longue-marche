# Reader brief v01 — first used scan 036

You are one of three independent readers of ONE manuscript scan. Read only the assigned page's images and input excerpts, this brief, the supplied conventions and current notation table. Do not consult other readers, their files, preceding or following pages, the web, OCR, text-recognition software, or a PDF text layer. Your task is visual collation, not reconstruction from mathematics. You are done after returning this page.

## Required sequence

a. Display the whole JPEG ONCE for layout, locating all text, displays, drawings, margins, insertions, deletions, page numbers and hands. Record its path and time in your report.

b. Display the two supplied halves (_a and _b) ONCE EACH, in order. Read every line against C.tex and H.tex, word by word and symbol by symbol. Check even agreement between witnesses. Do not redisplay or enlarge an entire half. The halves are full resolution. Identify what both witnesses missed. Do not silently normalize spelling, accents, grammar, abbreviations, mathematical signs, struck text, or insertion placement. Read the relevant C_doubts_notes.md as a guide to places needing attention, not authority.

c. Make a list of places still open after the halves: a difference from a witness, any C doubt, consequential small sign or index, crowded/struck/slanted writing. If a half settles a place, explicitly report that evidence and do not crop it. For each genuinely open place, make ONE tight crop (word/formula with one neighboring line) from the original whole image, upscaled with LANCZOS to around 2400–3600 pixels across, autocontrast and light sharpening, rotated upright where needed. The script scripts/crop.py is available. View the resulting crop once. Never crop an already decided place again. Retain the crop and its coordinates/rotation in your output directory. A crop may show its immediate neighbor as context, but do not make broad page-section crops as substitutes for reading the halves.

d. Return your COMPLETE proposed page transcription in reading.tex, and report.json with every difference from C or H, all C doubts (resolved or retained), your remaining doubts, inventory, mathematical notes, and actual check events. Reading a claim is not proving it. Use only these pages; no outside research. You may use elementary reasoning to identify a problematic reading, but the strokes decide. Keep author slips in the transcription. If the image cannot be viewed, report that immediately and do not invent a reading.

## Exact transcription conventions

Use the supplied PREAMBLE.tex macros only, plus standard LaTeX, amsmath, amssymb, mathrsfs, TikZ, tikz-cd, ulem and enumitem. No new macros. Preserve C's formatting where it represents the same ink; avoid stylistic rewrites that obscure a substantive comparison.

* One `\\cotefile{71}` at the start of scan 036 only; `\\scanpage{N}` each page; `\\mspage{...}` for manuscript pagination. Archive pencil numbering is a `% archive sheet number: NN` comment only.
* `\\deleted{...}`, `\\inserted{...}`, `\\margin{...}`, `\\uline{...}`, `\\uuline{...}` preserve cancellation, additions, placement and underlining. A corrected glyph over an earlier glyph is represented by its final visible form; recoverable earlier form can be `\\deleted{...}` immediately before it. Mark uncertainty where earlier text cannot be identified.
* `\\unsure{reading}` or `\\unsure{reading|alternative}`: first candidate must follow the ink. Retain every plausible visible candidate; do not retain a doubt once strokes settle it. `\\illegible{n}` is for physically unreadable words, never formula/diagram symbols.
* A recurring ambiguous glyph is described in the notation table and marked at its first occurrence on each page; later identical occurrences use the first candidate. Do not make a convention override different strokes on a new page.
* `\\diagram{\\begin{tikzcd}[ampersand replacement=\\&] ... \\end{tikzcd}}`, cells separated by `\\&`. Every arrow, object, label and struck part is represented. `\\figure{...TikZ...}` for drawings, preserving shapes, locations and every label. Never replace a drawing with prose. Best approximation plus `% crop-candidate: scan N` only if genuinely too complex.
* Preserve original language, spellings, accents and absent accents, punctuation, abbreviations, numbering, letters and alphabets, subscripts/superscripts, primes versus !, directions, dots/hats/bars. Do not fix a mathematical error. His double quotes are two backticks/two apostrophes, unless actual guillemets appear.
* Preserve paragraphs and text order. Join line-end word hyphenations; retain semantic hyphens. Do not retain ordinary line wrapping in prose.
* Inventory distinguishes fair-copy main ink from pencil annotations; do not confidently assign a named author from handwriting alone. Use `another unnamed hand (main ink)` and `another unnamed hand (pencil)` where uncertain. Do not infer author identity from the catalog.

## Witness H handling

H uses `\\page` = our scan minus one. Its `\\note` often summarizes the main text; that is not a diplomatic transcription. Its `\\marginal` gives readings of annotations. For H pages with `hua_has=text`, report substantive differences in its transcribed annotations, and main-text omissions by coherent paragraph/display block. Do not compare a summary's editorial paraphrase as if it claimed to be literal ink. For `desc` or `nothing`, give no H collation rows. Mere macro differences are not readings. State H's absence explicitly.

## Files to return (write only in your assigned reader directory)

1. `reading.tex`: full proposed page.
2. `report.json`: object with `scan`, `reader`, `views` (path/time for whole and halves), `crop_count`, `issues`, `inventory`, `doubts`, `notation`, `abbreviations`, `notes`, `check_events`, `summary`.

Each issue has `id`, `place`, `C`, `H`, `reading`, `evidence` (specific visible strokes/marks), `image` (half filename or crop path), `bbox` if cropped, `confidence` (high/medium/low), `against_C` and `against_H` booleans, `kind`, `H_marked` (yes/no/not applicable), `C_doubt` boolean. Include retained C doubts even if against_C=false. Kinds for H: misread word; misread symbol or index; omission; text not on the page; deletion state; insertion or placement; abbreviation expanded or spelling modernised; readable ink left as \\ill{}; drawing or diagram; other. Reports should give actual text, not just 'changed' or 'see file'. All C uncertainties must be accounted for. If an entire block is absent in H, the reading may give exact opening and closing words plus identify the complete block in reading.tex.

Each inventory element has `sheet_kind`, `hand`, `element`, `kind`, `position`, `first_words_or_objects`, `transcribed`='yes'. One row per text block, display, diagram/drawing, marginal note, insertion and deletion. Kind is one of text, display, diagram, drawing, margin note, insertion, deletion. Page number/archival mark may be noted separately in notes.

Each doubt: `place`, `reading`, `alternatives`, `confidence`, `reason`. Notes: what this page states/computes/asks; every mathematical trigger for a reading decision with location and readings; its own checks/doubts verbatim; titles, dates, page counts. Check events: `statement_id`, `date`, `who`, `type`, `outcome`; only classify what actually happened (targeted proof check / independent re-proof / computation or formal certificate / used and rechecked in this run / carried as background without fault found / refuted, with refined statement id). Identify yourself as GPT-6 Astra Pro, inherited effort (not exposed), reader/run ID; do not invent an effort setting.

Finish with a concise message to the main reader naming your files, main differences, unresolved issues and crop count. Do not send another reader your conclusions.
