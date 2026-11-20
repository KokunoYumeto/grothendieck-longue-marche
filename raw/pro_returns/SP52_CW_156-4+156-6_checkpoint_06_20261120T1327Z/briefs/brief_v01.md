# Independent reader brief v01 — first used 156-4 scan 065

You are one of three independent readers of ONE manuscript page. Do not inspect any other reader's files, other scans, prior conversation, or outside sources. Do not delegate. The attached second-pass task controls over historical instructions in C's files. Return only after your complete reading of this page.

Read metadata.json, C.tex, H.tex, CONVENTIONS.md, PREAMBLE.tex and C_context.md in the assigned packet, and the supplied notation snapshot. These are drafts: agreement of witnesses never establishes the reading. Nothing is to be inferred from expected mathematics or grammar. Do not run OCR, text recognition, or web research.

## Reading workflow

a. Use view_image on the whole page ONCE for layout. Identify every text block, display, diagram/drawing, margin, insertion and deletion.

b. Use view_image on each supplied full-resolution half ONCE, in order. Read every line, word, accent, punctuation and symbol against both C and H. Follow the mathematics to detect a suspicious sign/index, but the visible ink decides. Do not display an entire half a second time or enlarge a whole half. Do not rely on a witness as a substitute for seeing an agreed reading.

c. List all places the halves leave open: C doubts; remaining differences from either witness; crowded/slanted/cancelled writing; consequential small signs. Make ONE tight crop per open place, including one surrounding line; enlarge using PIL LANCZOS to about 2000–3000 px across; autocontrast, sharpen if helpful, rotate upright when necessary. View each crop. Never recrop a decided place. Record crop name, source and original pixel bbox, scale, rotation, and the visible evidence. For differences settled by a half, record the half and an original-image bbox so the adjudicator can make its one crop if needed. Crops must be your own, never another reader's.

d. Write the entire diplomatic page .tex using only the specified macros. You may use C as the editable base after checking every item against the ink. No omitted deletions, expanded abbreviations, or silently repaired mathematical slips. Preserve uncertainty the ink does not settle. Symbols inside mathematics must use a best reading with \\unsure, never \\illegible. Reproduce all diagrams/drawings with tikz-cd/TikZ. Complete the inventory, notes and witness differences before returning.

## Deliverables in your assigned output directory only

1. reading.tex, the full page fragment. Retain \\scanpage and \\mspage. Do not add a cote marker except if it already occurs in this C page.
2. report.json (UTF-8). Fields:
   - reader, cote, scan, brief_version, started_utc, finished_utc, image_views (the three paths actually viewed), reading_file.
   - differences: array of {id,location,c,h,reading,scan_shows,confidence,kind,marked_in_h,change_c,change_h,crop,bbox,math_consequential}. Include EVERY semantic, spelling, punctuation, alphabet, state, placement, or underline difference from C or H. Equivalent macro syntax alone is not a difference. Use actual LaTeX strings. Confidence high/medium/low. Kind one of: misread word; misread symbol or index; omission; text not on the page; deletion state (struck given live or live given struck); insertion or placement; abbreviation expanded or spelling modernised; readable ink left as \\ill{}; drawing or diagram; other. Marked_in_h yes/no. crop is an existing path or null, bbox is [left,top,right,bottom] on the named image. Clearly identify when the bbox refers to a half instead of the whole.
   - c_doubts: one item per C doubt {location,c,reading,status,scan_shows,crop,bbox}; status resolved/retained/revised. Do not leave out retained doubts.
   - inventory: {element,kind,position,first_words_or_objects,sheet_kind,hand,transcribed}. Include each text block, display, diagram, drawing, margin note, insertion, deletion separately. transcribed yes only after verifying inclusion. Use hand "his hand" for these manuscripts unless evidence says otherwise.
   - remaining_doubts: {location,reading,alternatives,confidence,reason}.
   - notation: {sign,latex,appearance,location,alternatives}; abbreviations: {form,expansion}.
   - notes: {summary,math_reading_decisions,author_checks,title_dates_pagination}. English, quotations in the page's language. Say which mathematical reasoning actually triggered an ink decision. No outside-page research.
   - check_events: {statement_id,date,who,type,outcome}. Record any mathematics actually checked/used/refuted, with the exact type: targeted proof check / independent re-proof / computation or formal certificate / used and rechecked in this run / carried as background without fault found / refuted, with refined statement id. Simply transcribing a statement is NOT proving it. An empty array is honest if no mathematical validation happened.
   - crops: {path,source,bbox,scale,rotation,reason}; workflow_feedback: concrete weaknesses in this brief, if any.
3. Keep crop images in your output directory's crops/ subdirectory. Include an inspection log naming each view in order and all transformations. Scripts belong in that same output directory. Do not change shared notation or any consolidated deliverable.

## Final return

Give paths to reading.tex and report.json, number of differences, remaining doubts, crop count, and the highest-priority readings requiring adjudication. Be candid if a mark cannot be read. Do not claim checks not actually done.
