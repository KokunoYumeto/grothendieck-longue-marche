# Independent reader brief v05 — first used 156-4 scan 069

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
   - inventory: {element,kind,position,first_words_or_objects,sheet_kind,hand,transcribed}. Use kind EXACTLY one of: text, display, diagram, drawing, margin note, insertion, deletion. Use sheet_kind EXACTLY one of: text, reused_typed, typescript, letter, list, cancelled_draft, cover. Ordinary handwritten subject notes are text. Page numbers and headings are text; underlines remain part of their text element. Include each block, display, diagram, drawing, margin note, insertion and deletion separately. transcribed yes only after verifying inclusion. Use hand "his hand" for these manuscripts unless evidence says otherwise.
   - remaining_doubts: {location,reading,alternatives,confidence,reason}.
   - notation: {sign,latex,appearance,location,alternatives}; abbreviations: {form,expansion}.
   - notes: {summary,math_reading_decisions,author_checks,title_dates_pagination}. English, quotations in the page's language. Say which mathematical reasoning actually triggered an ink decision. No outside-page research.
   - check_events: {statement_id,date,who,type,outcome}. Record any mathematics actually checked/used/refuted, with the exact type: targeted proof check / independent re-proof / computation or formal certificate / used and rechecked in this run / carried as background without fault found / refuted, with refined statement id. Simply transcribing a statement is NOT proving it. An empty array is honest if no mathematical validation happened.
   - crops: {path,source,bbox,scale,rotation,reason}; workflow_feedback: concrete weaknesses in this brief, if any.
3. Keep crop images in your output directory's crops/ subdirectory. Include an inspection log naming each view in order and all transformations. Scripts belong in that same output directory. Do not change shared notation or any consolidated deliverable.

## Clarifications from the first page

- Separate lettering from the state of its ink: one overwritten word must not become an invented deleted word plus a second complete live word. In a crowded correction, first establish how many word-sized groups exist. A tall stem at the end of a cancelled word may belong to that word; do not create an extra isolated letter without a distinct position.
- Establish the full extent of an insertion: if an entire phrase is on the raised line, mark the whole phrase inserted. When cancellation state is unclear, express the alternatives in place (for example, one word with a possibly cancelled last letter), rather than assert two separate words.
- Reproduce angular insertion enclosures, connecting arms, brackets and other drawn marks in TikZ when they are distinct graphic elements. A comment describing the mark is not its transcription. Ordinary deletion/underline/insertion macros still represent their ordinary strokes.
- Check actual point/accent strokes rather than conventional punctuation. A terminal hook attached to a letter is not automatically a full stop; a tiny separate mark may require an accent doubt. Report the visible stroke and its ambiguity, not just a grammatical preference.
- Report differences in certainty as well as wording: if H marks a word uncertain and the ink settles it, include that locus. Do not count equivalent macros as different readings. Mark math_consequential only when the decision changes a mathematical statement or object; alphabet style and renamed bound variables alone do not automatically do so.
- Preserve crop coordinates in report.json with bbox_image/source. Prefer high-quality JPEG (quality 94) for new crops, 2000–3000 pixels across, to limit checkpoint size. Batch independent file reads or crop creation where useful, but emit at most three crop images per tool result so no image is lost through output truncation. If a display is truncated, do not claim the image was seen.
- Keep notes brief and specific to the page. Do no optional mathematical research. A checked reading is not a proved theorem; check_events may be empty when all assertions are only transcribed.

## Clarifications from scan 066

- Do not invoke a LaTeX compiler, including LuaLaTeX. The deliverable is a fragment in the supplied conventions; perform structural checks only. One previous reader tried compilation, which failed before producing a render. This was an unnecessary deviation and must not recur.
- Keep every component of a composite small mark. A d-like loop over a separate point is not faithfully represented by a lone d. Preserve vertical placement of cancelled superscripts above surviving signs.
- Connected interlinear glosses may be rendered once as labels in the same TikZ group as the formula and its pointers. Do not also duplicate their words in margin macros. Preserve relative positions with node anchors when possible.
- Distinguish uncertainty at separate occurrences of the same alphabet: an uncertain initial C does not make a later clearly curled C uncertain. Scope report entries to the actual occurrence.
- Include dispositions for the explicit notation checks in C_context as well as every unsure macro in C.tex. Ignore any context row that concerns another scan. Report the actual source of each decision without inheriting an earlier reader's assertion as evidence.
- If tool output truncates an image, display the same existing crop in a smaller batch; this is not a new crop and must not be falsely logged as a successful first view.

## Clarifications from scan 067

- Before saving a crop, include the entire target, especially an upper accent/exponent, a letter head, the final closing mark, and a little clear space beyond terminal punctuation. Include the surrounding line as instructed. A crop that clips the target cannot establish absence of an accent or punctuation. Report such a framing failure honestly; do not count it as a settled reading.
- Distinct insertion leaders may be long oblique strokes attached to a raised symbol. An inserted macro records the addition but does not reproduce a separate graphical arm: include that arm in the local TikZ group, with adjoining words once.
- A short pointer may merge with a word's final stroke. Preserve uncertainty about whether it is a distinct arrow; do not add a confident arrowhead merely because the note points toward a formula.
- Absence of a securely visible accent can remain a spelling doubt. Do not restore a French accent from grammar. Distinguish a short dash-like stop from an assumed period.
- Scope difference snippets consistently. If a row concerns an omitted drawing, include the drawing or its exact final figure reference rather than identical text labels with a change flag. Preserve primes and doubt marks when quoting witnesses. Context dispositions covering multiple occurrences must state local differences, such as one-p versus two-p operators.

## Clarifications from scan 068

- Compare witness quotations directly before labelling a difference. Keep a row's C, H and final snippets at the same scope; count punctuation separately from an already recorded alphabet change. An editorial suggestion in an H comment is not its literal manuscript transcription: report it separately, and do not count its rejection as omitted text.
- A single densely worked word does not establish an extra complete unreadable older word. Retain uncertainty in the lettering and deletion state without adding a separate illegible word-sized layer unless its separate position is actually visible.
- Preserve detached small marks at their actual position, including points below a word. Draw them when needed without inferring a punctuation, linguistic or mathematical function. A clear word can coexist with unexplained marks.
- Make every remaining-doubt entry agree with reading.tex. Different occurrences of P, F or another letter can have different certainty; report their exact scopes. Do not turn a clipped crop boundary into evidence of absence.

## Final return

Give paths to reading.tex and report.json, number of differences, remaining doubts, crop count, and the highest-priority readings requiring adjudication. Be candid if a mark cannot be read. Do not claim checks not actually done.
