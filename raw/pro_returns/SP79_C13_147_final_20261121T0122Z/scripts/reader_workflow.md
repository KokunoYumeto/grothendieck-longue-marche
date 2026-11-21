# Page reader instructions

You receive one page at a time. Read only the assigned packet, the shared reading_rules.md, and this workflow. No OCR, recognition software, external sources, or other pages. The scan is the authority; C and H are fallible drafts. Use view_image for visual reading.

1. Read reading_rules.md in full before the first page, plus this page's C.tex, H.tex, PREAMBLE.tex, marks.tsv, differences.tsv and notation.md. The diff list is mechanically noisy: macro syntax and editorial page markers are not textual differences.
2. View page.jpg once for layout, then top.jpg and bottom.jpg once each at their native resolution. These halves were made once already with Pillow. Read every line against both witnesses. Review every C deletion and insertion separately, checking exact scope and attachment. Count physical written lines for progress (state your counting convention).
3. Crop once each unresolved place, every C/H difference in actual words, and every C doubt mark you resolve. Crop full formulas surrounding doubtful symbols. Use Pillow, original image coordinates, LANCZOS enlargement to about 2200–3000 pixels wide, autocontrast; mild sharpening if needed. Rotate slanted passages upright if useful. Save only these crops to the shared crops/ as 147_scanNNN_<specific-place>.png. One crop can cover a closely related local phrase/formula but must not replace a whole-half reading. Never re-crop a decided place during this first pass. Look at every created crop using view_image. Keep original box coordinates and any rotation in the report.
4. Produce a complete diplomatic page in reviews/147_scanNNN.tex. Keep all readable cancelled content. Transcribe drawings using TikZ and diagrams using tikz-cd. Preserve ink that seems mathematically wrong, and explain separately. Uncertainty must be honest and local, without invented text. Follow only supplied PREAMBLE macros plus standard LaTeX/TikZ. Do not compile TeX.
5. Produce reviews/147_scanNNN.json using the schema below. The main reader will inspect your crops and finalize. Do not write final pages/ or progress.log. Do not save to Library. Stop after this page and return a compact summary and exact file paths; wait for a new page.

## JSON schema

Top-level keys:
- scan: integer; reader: your agent task name; line_count: integer; line_count_note: string; ms_page: string; sheet_kind: permitted inventory kind.
- changes: array, one substantive place per object: {id, place, C, H, final, ink, crop, box, confidence, kind, against_C, against_H, consequential, category}. `C`, `H`, `final` are exact LaTeX snippets or explicit absence. `ink` describes actual letters/strokes distinguishing readings, not mathematical plausibility. `crop` is relative crops/ path or empty if genuinely settled on a half (a differing word always has crop). `box` is [x0,y0,x1,y1] or null. confidence high/medium/low. against_C and against_H are booleans based on reading, not mere macro syntax. consequential true if mathematics changes. category is one of the ten numbered error-sheet categories (symbols and indices, words, omissions, drawings and diagrams, readable ink left as illegible, insertion placement, struck text, abbreviations and spelling, text not on the page, other). `kind` is one of the user's H-collation kinds. Include `marked_in_H` boolean.
- decisions: every assigned MARKS.tsv row in order: {id, decision, reading, ink, crop, box, confidence}. decision is first/alternative/other/undecided. Every resolved mark requires an inspected crop. Unresolved mark can cite page. Preserve uncertainty inside struck text unless every letter is plain.
- inventory: every text block, display, diagram, drawing, margin note, insertion and deletion top-to-bottom as objects {element,kind,position,first_words_or_objects,hand,transcribed}. hand usually 'his hand'; transcribed 'yes'. Page number gets an element too.
- doubts: remaining uncertainty objects {place,reading,alternatives,confidence,reason}.
- notes: English text explaining page claims, mathematics used for reading, apparent slips and author's own uncertainty with exact words, page numbers/dates. Do not silently assert checked theorems.
- check_events: array {statement_id,type,outcome}. Only record what actually was checked/used; mere reading is not proof checking. Permitted types in governing prompt. 'carried as background without fault found' is appropriate only if actually used as background.
- hand_log: objects {habit,holds,misread_locations}; report whether all observed occurrences support it, avoid overgeneralization.
- notation: objects {notation,meaning_or_form,evidence}; proposed updates for shared table.
- abbreviations: objects {form,expansion}.
- deletion_checks: array of strings, one per C deletion; insertion_checks likewise.
- second_boxes: every mandatory hard place for blind second reading: {box,kind,x0,y0,x1,y1,reading}. Box must include every insertion, margin note, struck passage, formula containing a C or final doubt, handwritten number (including manuscript page number and numerical formula tokens), different C/H words, and any departure from C below high confidence. Combine overlapping local regions when sensible, with all required kinds named. `reading` is exact final transcription of everything inside that box using our macros; choose boundaries cleanly to avoid clipping words. Main reader freezes _first.tsv before blind read. It is fine to include an additional difficult place.
- unresolved: concise list of places requiring main reader decision.

Make a crop for every reported disagreement that main reader must decide, even if a half already seems persuasive; reuse existing local crop when it contains the disputed strokes. Be complete and rigorous rather than fast. No invented checks, no guessed letters, and no claim of a visual read without actually viewing the image.

## Controlled vocabularies

sheet_kind: text, reused_typed, typescript, letter, list, cancelled_draft, cover.
H-collation kind: misread word; misread symbol or index; omission; text not on the page; deletion state; insertion or placement; abbreviation expanded or spelling modernised; readable ink left as \\ill{}; drawing or diagram; other.
check-event type: targeted proof check; independent re-proof; computation or formal certificate; used and rechecked in this run; carried as background without fault found; refuted, with the refined statement's id.
