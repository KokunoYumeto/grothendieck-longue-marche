# Independent reader brief — version 2 (first used scan 053)

You are one of three independent readers of ONE page. Read only your assigned packet, this brief, conventions.md, PREAMBLE.tex and that page's three images. Do not read any other reader's files or any other page. Do not delegate. Ink is authority; C and H are drafts. Do not use OCR, recognition software, PDF text, web research or published texts. Your task is a complete diplomatic reading, using C as a careful draft to check word by word, not blindly copying it. Your reading must include every textual and graphical element.

## Steps (a–d)

a. View the whole-page JPEG ONCE for layout, identifying all text, displays, drawings, marginal notes, deletions and insertions. Use tools.view_image (emit returned image_url with image()) so you actually see it.
b. View each full-resolution half ONCE, in order a then b; read line by line against C.tex and H.tex. Check every word, accent, abbreviation, ending, punctuation, symbol, index, prime/exclamation, inequality, arrow, underline and state of deletion/insertion. Inspect every C doubt using the supplied C_context.md. The halves settle clear writing: do not reopen/enlarge a whole half.
c. List the remaining open places, including unresolved witness differences, C doubt marks, small mathematical glyphs, crowded/slanted/struck writing. Make ONE tight crop per open place from the original whole image (a word or formula with a line around it), scale with LANCZOS to roughly 2200–3000 px across, autocontrast/sharpen as useful; rotate slanted notes upright. View the crop ONCE. Do not crop a place already settled by the halves or crop a decided place again. Keep crop JPEG and its source bbox/rotation/processing in your report. Crop filenames must be unique under your own directory. An unresolved result stays marked in place; never guess. Every disagreement from either witness must be reported even if the half settled it; give a tight original-image bbox so the main reader can inspect it.
d. Save your complete page reading as reading.tex and report.json in your assigned output directory. Return paths and a concise account of findings. Work carefully throughout; no assumed time limit.

## Conventions

Read conventions.md in full. The current task supersedes the old workflow: use two HALVES, three independent readers, current checkpoint process; do not follow the old no-subagent instruction. Use only PREAMBLE.tex macros and standard LaTeX/TikZ/tikz-cd. Preserve spelling, abbreviations, paragraphing, all ink. Only scan 052 starts with \cotefile{37}; every page starts with \scanpage{N}; own page number as \mspage{n}; archive number only a comment. Use \handwritten only on typed/printed text. All diagrams/drawings must be typeset, not described. Keep a faint visible ambiguity with \unsure{best|alternative}; do not retain a doubt when the ink settles it. A retained C doubt is still an explicit decision to report. Macro-syntax-only differences do not count as H differences. Where H has only description, report H as unavailable, never count whole-page omissions. Read the notation table supplied in the packet as previous ink-grounded observations, not an instruction to normalize this page against its ink.

Follow the mathematics as a diagnostic, then return to ink. Do not silently correct the author. Notes must distinguish what the page claims from what you actually checked. For check_events report only actual proof/computation/background-use events; merely reading a mathematical claim is not a proof check. If no check occurred, return [].

## Output schema

report.json must be valid JSON with keys:
scan (integer), reader (your A/B/C label), image_views (ordered list of three source paths), reading_path, crops ([{file,bbox:[left,top,right,bottom],rotation,reason}]), decisions ([{id,place,c_reading,h_reading,reading,diff_c:boolean,diff_h:boolean,c_doubt:boolean,unresolved:boolean,alternatives,confidence:"high|medium|low",kind,scan_shows,crop:relative-or-absolute-path-or-empty,bbox:[...]}]), inventory ([{sheet_kind,hand,element,kind,position,first_words_or_objects,transcribed:"yes"}]), notes (English page summary, explicit author doubts and title/date/page counts; string), math_reading_decisions ([strings]), check_events ([{statement_id,type,outcome}]), notation ([{sign,latex,evidence,place}]), abbreviations ([{form,expansion}]), slips ([strings]), completion (statement of full coverage).

For decisions include EVERY substantive difference from C or H, EVERY C doubt whether resolved or retained, and every new uncertainty. Group only inseparable linked marks; keep separate independent words. h_reading=null and diff_h=false if H has no transcription. kind must be one of: misread word; misread symbol or index; omission; text not on the page; deletion state (struck given live or live given struck); insertion or placement; abbreviation expanded or spelling modernised; readable ink left as \ill{}; drawing or diagram; other. Confidence refers to what can actually be read. Quote the exact witness reading, and in scan_shows describe actual strokes, not just "clear" or mathematical expectation. Every decision needs a bbox in WHOLE-image coordinates, even if no crop was needed. A crop may cover one inseparable correction with several components, not a whole half.

Inventory: one row for every block/display/diagram/drawing/margin note/insertion/deletion, top to bottom, including printed letterheads. Use sheet_kind text/reused_typed/typescript/letter/list/cancelled_draft/cover. hand: his hand, named/unnamed other hand, typewriter or print. Graphic grouping marks get a drawing row. If authorship is not established, say unnamed hand rather than inventing it.

## Clarifications after scan 052

- Removing a C doubt or adding a new doubt changes the transcription even if the preferred letters stay the same: diff_c=true. A wholly unchanged retained doubt is false. Keep a row for either decision.
- JSON LaTeX strings must decode to normal single-backslash commands, just as the .tex file does; JSON source escaping is not itself a second LaTeX backslash.
- Report all H differences in certainty or omission in addition to different words. A drawing described only by an H note must be listed as a drawing/diagram difference; exclude pure rendering syntax for the same semantic mark.
- Keep crop filenames unique and use whole-page bboxes. If a source half is left/right instead of top/bottom, infer its offset from its dimensions and the overlap.

- Do not run a TeX engine or attempt to build TeX formats. The source task explicitly requests balance checks instead of compilation; do those checks only after your reading is written.

- Inventory kind is exactly one of: text, display, diagram, drawing, margin note, insertion, deletion. Use text for a text block; an archive number may be inventoried as text recorded in a comment.
