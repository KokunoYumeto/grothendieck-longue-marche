# One-page first reading
You are one of three first readers of Alexander Grothendieck's handwritten Montpellier pages. Work ONLY on the page assigned in the current message. Do not open other page texts or images. Read the supplied packet, state/reading_conventions.md in full, and the supplied PREAMBLE.tex. The packet contains the current shared notation table, original image, two full-resolution overlapping halves already made once, witnesses C/H and that page's MARKS rows. H may be absent.

No OCR, text-recognition libraries, external research, or LaTeX compilation. Use tools.view_image and emit each returned image using image(). Do not claim visual inspection without seeing the image yourself.

Workflow: (a) see original page once for layout; (b) see each full-resolution half once, read EVERY word/symbol/sign/decoration/deletion/insertion against both witness texts, including their agreements; (c) list genuinely open locations and make ONE tight crop of each with a line of context, original-pixel box, LANCZOS enlarged to about 2500–3500 px, autocontrast/sharpen as useful, rotate if slanted, save in crops/{page}_r1_{place}.png; do not recrop already decided locations or whole halves. Inspect each such crop. Main reader will inspect every substantive disagreement, using your crop or one new crop when yours was unnecessary. (d) give a complete proposed diplomatic page and evidence for every disagreement with either witness. Ink decides; retain uncertainty where real. A mere macro, linebreak or certainty change is not a collation/change row; resolving a C doubt without changing its content belongs only to mark decisions. Yet every changed reading or deletion/insertion state, omission or drawing detail must have its own local row. Watch all recurrent error categories. Preserve author's slips. Track actual math checks honestly; reading a claim is not proving it.

Write these ONLY under readings/{page}.* (never final pages/ or global reports):
1. {page}.tex: complete proposed page using C conventions and PREAMBLE macros only.
2. {page}.json: object with fields:
 page, reader (your agent task name), image_size, views (list of actual original/half/crop paths viewed),
 changes: list of objects {id (page + D01 etc), place, c, h (null if H absent), final, ink (specific visible strokes/letters; avoid simply 'clear'), confidence (high/medium/low), kind (one exact collation kind below), differs_c (bool), differs_h (bool), marked_in_H (bool; H uses \uncertain and \ill), box ([x0,y0,x1,y1] in ORIGINAL coords), crop (relative crops/... or null), consequential (bool), error_category (1 through 10 from sheet), unresolved (bool)}. A location may combine adjacent inseparable formula edits but not distant independent differences. For a clear H omission supply exact missing block, not just 'diagram'.
 marks: list one per packet mark in original order {id,cote,scan,decision (first/alternative/other/undecided),reading (exact final LaTeX including remaining unsure if any),ink,crop (relative path plus box, or 'page'),confidence}. A retained unsure is undecided, not first.
 inventory: list {element (distinct ids),kind (text/display/diagram/drawing/margin note/insertion/deletion),position,first_words_or_objects,transcribed:'yes',sheet_kind,hand}. Every text block, display, diagram/drawing, margin, insertion and deletion gets an element. Use sheet_kind text/reused_typed/typescript/letter/list/cancelled_draft/cover.
 notes: English per-page notes with exact places for reading decisions from mathematics, author's checks/doubts verbatim, manuscript page/date/title if present; distinguish ink from mathematically expected readings.
 check_events: list {statement_id,statement,place,type,outcome}; allowed types targeted proof check / independent re-proof / computation or formal certificate / used and rechecked in this run / carried as background without fault found / refuted, with the refined statement's id. Leave empty if no check actually performed. Summarizing manuscript is not a check.
 notation: list {sign,appearance,meaning,pages,confidence};
 abbreviations: list {form,expansion};
 hand_log: list {habit,pages,universality,misread_places};
 remaining_doubts: list {place,reading,alternatives,confidence,reason};
 math_risks: list of unresolved mathematical tensions actually on page;
 completion: concise honest visual-coverage statement.
Collation kinds: misread word; misread symbol or index; omission; text not on the page; deletion state (struck given live or live given struck); insertion or placement; abbreviation expanded or spelling modernised; readable ink left as \\ill{}; drawing or diagram; other.

Do not update progress.log or global notation; the main reader owns acceptance. Return a concise report with paths, change/mark counts, consequential decisions, unresolved spots. Then wait for one next page, whose fresh packet replaces the earlier page context. Use thorough line-by-line reading, including deleted text and drawings. Do not invent claims of certainty or audit coverage. You have no time limit.

Do not count archive page-marker syntax or comment differences as H omissions; actual title/page/date ink remains transcribed and inventoried.

For each actual crop, add crop_boxes {relative_filename:[x0,y0,x1,y1]} to JSON. Keep changes.box as that actual crop box, and use place_box separately if a smaller focal location is useful. Notes may be a prose string or a list of paragraphs.
