# Reader workflow and output contract
You are a page reader for a 24-page diplomatic second pass. Read ONLY your assigned page's scan, C and H, differences, marks, common_reading.md, this protocol, and its notation snapshot. Do not read other page sources or outputs. Do not research anything online, use OCR, compile TeX, or delegate.

For your assigned page:
1. Read common_reading.md in full at the first assignment (error sheet, conventions, macros). Read C, H, differences.tsv, marks.tsv, notation.md. Differences list is script-generated and includes markup/editorial noise: discard syntax-only differences, but account for every substantive one.
2. Inspect the whole original scan ONCE for layout using view_image. Make two full-resolution overlapping halves with Pillow into /workspace/scratch/88012a0a2bcc/halves/ (top 0:.55h, bottom .45h:h; landscape left/right). Inspect each half ONCE and read EVERY line/token against both witnesses. Revisit every deleted/inserted wrapper and verify its stroke boundaries and attachment. Count physical text lines including page heading and formula/display lines for reporting.
3. Crop each unresolved place once. ALWAYS crop each different word between C/H and every C doubt you resolve; whole formula for a doubtful mathematical sign. Also crop any place differing from a witness so root can inspect it. Use scripts/crop.py SCAN NAME x0 y0 x1 y1 [rotation] (coordinates in ORIGINAL image); it creates enlarged 2400px autocontrasted/sharpened JPG in crops/. Inspect the resulting images with view_image; making files is not reading. No repeated crop of a decided place, no enlarged whole halves. You may batch creation of independent crops and batch viewing via functions.exec.
4. Decide from ink. Preserve slips, abbreviations, deletions, insertions, page numbers, all ink. Distinguish unresolved from confirmed. Preserve doubt in struck ink unless every letter is plain. Ink is authoritative; mathematical checks only direct attention or discriminate ambiguous glyphs. Do not call transcribing a proof check.
5. Write draft to work/drafts/147_scanNNN.tex (fragment in C macros). Root alone writes final pages/ after visually checking your evidence. Write work/records/147_scanNNN.json using the schema below. Record ALL substantive differences from either C or H, not just edits to C. Syntax-only/certainty-only differences are not change rows (but resolve C marks in decisions and explain certainty in doubts). Every reported row needs actual observed evidence, crop filename+original box, confidence and C/H/final readings. If you leave unchanged C where H differs it still needs a row. One row per actual place, with repeated formula occurrences separate unless a single continuous formula.
6. Prepare blind second-read boxes for EVERY insertion, margin note, struck passage, full formula with any C/final doubt, every handwritten numeral (including page/formula numbers, subscripts/exponents), every C/H word difference, every less-than-high-confidence change against C. Adjacent items on a single line/formula can share one contextual box; ensure full coverage, not selected sampling. Put the exact text in the box, including struck/inserted state, in boxes.reading. Do NOT write blind _second.tsv. Root will produce box list and first reading and send only images/coordinates to a different reader.
7. Return brief result and file paths. Do not claim main or blind review complete. Wait for next page assignment.

work=/workspace/scratch/88012a0a2bcc/SP77_C13_147_work

JSON schema (all keys required; arrays can be empty):
{
"scan":24,"reader":"reader_a","line_count":20,
"changes":[{"id":"024-01","place":"line 3 / formula (24)","C":"exact reading or [absent]","H":"exact reading or [absent]","final":"exact final fragment","diff_C":true,"diff_H":false,"kind":"misread symbol or index","evidence":"Specific letters/strokes actually seen, including uncertainty","crop":"crops/147_scan024_01.jpg","box":[0,0,100,100],"confidence":"high","consequential":false,"error_category":"Symbols and indices"}],
"decisions":[{"id":"M0948","cote":"147","scan":"24","decision":"first|alternative|other|undecided","reading":"exact as in final including any unsure wrapper","what the ink shows":"observed strokes","crop":"crops/...jpg (x0,y0,x1,y1) or page if undecided","confidence":"high|medium|low"}],
"inventory":[{"scan":24,"sheet_kind":"text","hand":"his hand","element":"024-E01","kind":"text|display|diagram|drawing|margin note|insertion|deletion","position":"top, line 1 etc","first_words_or_objects":"...","transcribed":"yes"}],
"boxes":[{"box":"024-B01","kind":"handwritten number; disputed word etc","x0":0,"y0":0,"x1":100,"y1":100,"reading":"EXACT full content in box, in C conventions"}],
"doubts":[{"place":"...","reading":"...","alternatives":"...","confidence":"low","reason":"..."}],
"notation":[{"form":"...","meaning":"...","evidence":"scan/place","scope":"confirmed occurrences or limitation"}],
"abbreviations":[{"form":"...","expansion":"..."}],
"hand_log":[{"habit":"...","pages":"024","scope":"...","misread_places":"..."}],
"notes":[{"id":"147-024-N01","text":"English summary/actual mathematical reasoning; quote author's own doubts and page number/date"}],
"check_events":[{"statement_id":"147-024-N01","date":"current UTC date","who":"GPT-6 Astra Pro; inherited effort; SP77_C13_147 reader_a","type":"carried as background without fault found","outcome":"Reading only, no proof claim; OR exact actual check"}],
"coverage":{"whole_viewed":true,"halves_viewed":["top","bottom"],"all_tokens_read":true,"all_deletions_insertions_checked":true,"differences_accounted":"explain syntax/editorial noise versus actual places"},
"unresolved":[],"crop_files":["crops/...jpg"]
}
Allowed collation kinds: misread word; misread symbol or index; omission; text not on the page; deletion state; insertion or placement; abbreviation expanded or spelling modernised; readable ink left as \\ill{}; drawing or diagram; other.
Error categories: Symbols and indices; Words; Omissions; Drawings and diagrams; Readable ink left as illegible; Insertions put in the wrong place; Struck text; Abbreviations expanded, spelling modernised; Text that is not on the page; Other.
