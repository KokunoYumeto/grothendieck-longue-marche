# Assigned page only: first reading
Read only the assigned page's packet and images, reader_rules.md and this protocol; do not inspect any other page or report. No OCR, recognition library, outside research, or TeX compilation. Your task is a visual diplomatic transcription, not a rewrite of C. Parent performs its own crop review and finalizes. Do not delegate (all 3 slots are in use).

Read reader_rules.md fully (error sheet + conventions) and packet/PREAMBLE.tex. Whole image once for layout, supplied two native-resolution halves once each line by line against both witnesses. Read every agreed word too. Check each deletion's exact scope and each insertion attachment. Crop each materially differing C/H word and every C doubt you resolve; also unresolved small formulas, struck/crowded/slanted passages. Each place gets one crop: original box x0,y0,x1,y1; Pillow LANCZOS upscale to ~2000–3000 px width, autocontrast and modest sharpening where helpful. Save to work/crops/<page>_<place>.png; actually inspect using view_image. No repeat first-pass crop of decided place. Do not call paper noise text. Keep doubt where ink cannot settle it. Transcribe complete diagrams/drawings as TikZ or tikz-cd using available macros; never turn text into drawings. Record crop letter/stroke evidence, not vague 'scan confirms'.

Deliver to work/reports/<page>/draft.tex and report.json. Use the following JSON fields (all required; empty arrays are okay only genuinely empty). Paths in report are relative to work, e.g. crops/149_scan130_P01.png. Never edit final pages or shared logs.

{
 "page":"149_scan130", "reader":"reader_a", "line_count":0,
 "changes":[{"id":"P01","place":"L1 ...","c":"exact local C reading","h":"exact local H reading","final":"accepted reading in our macros","evidence":"what strokes/letters and state the crop shows","crop":"crops/...png","box":[0,0,1,1],"confidence":"high|medium|low","kind":"one of collation kinds below","against_c":true,"against_h":true,"marked_in_h":false,"consequential":false,"error_category":"one of 1..10 listed below"}],
 "decisions":[{"id":"Mxxxx","cote":"149","scan":"130","decision":"first|alternative|other|undecided","reading":"exact retained text in draft","evidence":"stroke evidence","crop":"crops/...png or page","box":[0,0,1,1],"confidence":"high|medium|low"}],
 "inventory":[{"scan":"149_scan130","sheet_kind":"text|reused_typed|typescript|letter|list|cancelled_draft|cover","hand":"his hand|...","element":"E01","kind":"text|display|diagram|drawing|margin note|insertion|deletion","position":"top... / original pixel box if useful","first_words_or_objects":"...","transcribed":"yes"}],
 "audit_boxes":[{"box":"B01","kind":"insertion|margin note|struck passage|doubtful formula|handwritten number|handwritten word on typescript|C/H different words|less than high confidence departure","xyxy":[0,0,1,1],"reading":"accepted exact content of box"}],
 "doubts":[{"place":"...","reading":"...","alternatives":"...","confidence":"low|medium","reason":"..."}],
 "notes":[{"id":"N01","text":"English: page contents, mathematical diagnostic and any author's question/slip (quote original words). Merely reporting source is not verifying a theorem."}],
 "check_events":[{"statement_id":"149_scan130.N01","type":"targeted proof check|independent re-proof|computation or formal certificate|used and rechecked in this run|carried as background without fault found|refuted, with refined id","outcome":"honest actual event only"}],
 "notation":[{"form":"...","meaning":"...","evidence":"..."}],
 "abbreviations":[{"form":"...","expansion":"..."}],
 "hand":[{"habit":"...","places":"...","consistency":"...","witness_errors":"..."}],
 "diff_coverage":[{"row":1,"disposition":"reading decision Pxx / macro-only / same reading ..."}],
 "deletion_insertion_review":[{"text":"...","scope_attachment":"...","evidence":"half or crop..."}]
}

Kinds for collation: misread word; misread symbol or index; omission; text not on the page; deletion state (struck given live or live given struck); insertion or placement; abbreviation expanded or spelling modernised; readable ink left as \\ill{}; drawing or diagram; other.
Error category: 1 Symbols and indices, 2 Words, 3 Omissions, 4 Drawings and diagrams, 5 Readable ink left as illegible, 6 Insertions put in wrong place, 7 Struck text, 8 Abbreviations expanded or spelling modernised, 9 Text not on page, 10 Other.
A changes row represents one actual place differing from either witness, including decisions resolving C doubts. Pure macro variants excluded; added uncertainty alone belongs in doubts. c/h/final strings must use exact local source forms with enough context. against_c/h reflect material source-text/state difference, not macro spelling. C uncertainty resolved may count against C as a certainty resolution, label it in evidence. All marks in packet/marks.tsv require decisions, in that order.

Audit box coverage is critical. Prepare one box for every insertion, margin note, struck passage, whole formula containing a C or your doubt, every number written by pen (including folio, formula numbering, inline digits, indices—nearby ones can share a formula box), every handwritten word on typescripts, every C/H different word, every below-high-confidence departure from C. Boxes may merge overlapping targets, but kind must state every covered category. Each box's first reading must cover exactly its targeted ink, so blind reader can transcribe same scope. Don't bake target readings into kind or box identifiers. Include surrounding readable context when needed; don't let huge page-area boxes defeat the audit. Parent will compare blind readings token by token.

When finished, report file paths, number of crops/changes/marks/audit boxes and the most consequential issues. Await next page assignment.
