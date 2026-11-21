# Page reader output contract

Read only your assigned packet and its images. Do not inspect any other page, global report, or source file. Do not use OCR or any image-to-text software. Do not compile TeX. The page image and two native halves already exist; view each once. Use tight crops for every material C/H word disagreement, every C doubt you resolve, and all other unresolved ink. Make each first-pass crop once (Pillow, LANCZOS enlargement to 2500–3200 pixels wide, autocontrast, mild sharpening); record original image coordinates. The bottom half begins at round(height*0.45); all boxes use whole-image coordinates.

Deliver a proposed complete page in `work/SP86_C13_149/readings/PAGE.tex`, and a JSON report in `work/SP86_C13_149/readings/PAGE.json`. Root will inspect the ink and write final `pages/` files. Report with this schema (all arrays required, empty where appropriate):

```
{
 "page":"149_scanNNN", "scan":N, "reader":"reader_a/b/c", "line_count":30,
 "changes":[{"id":"P01","place":"line 2","C":"literal source reading","H":"literal source reading","final":"proposed LaTeX","evidence":"exact letters/strokes seen; any still unclear","crop":"crops/149_scanNNN_P01.png","box":[x0,y0,x1,y1],"confidence":"high|medium|low","against_C":true,"against_H":true,"kind":"allowed collation kind","error_category":"Symbols and indices|Words|Omissions|Drawings and diagrams|Readable ink left as illegible|Insertions put in the wrong place|Struck text|Abbreviations expanded, spelling modernised|Text that is not on the page|Other","marked_in_H":false,"consequential":false}],
 "decisions":[{"id":"M....","cote":"149","scan":"N","decision":"first|alternative|other|undecided","reading":"exact final LaTeX","evidence":"ink evidence","crop":"crops/149_scanNNN_P01.png (x0,y0,x1,y1)","confidence":"high|medium|low"}],
 "inventory":[{"element":"E01","kind":"text|display|diagram|drawing|margin note|insertion|deletion","position":"top/right etc; original pixels or lines","first_words_or_objects":"literal opening or math","sheet_kind":"text|reused_typed|typescript|letter|list|cancelled_draft|cover","hand":"his hand|another hand|typewriter|print","transcribed":"yes"}],
 "doubts":[{"place":"...","reading":"...","alternatives":"...","confidence":"medium|low","reason":"..."}],
 "notes":["English description of the page's content with statement/source labels; preserve any author's own question or doubt verbatim; report actual performed mathematical checks separately."],
 "check_events":[{"statement_id":"...","type":"actual check type or carried as background without fault found","outcome":"precise performed action; reading alone is not a proof check"}],
 "hand":[{"form":"...","observation":"...","places":"...","scope":"all observed occurrences or local limitation","witness_errors":"..."}],
 "notation":[{"form":"...","meaning":"as established by this page only","places":"..."}],
 "abbreviations":[{"written":"...","expansion":"...","places":"..."}],
 "audit_boxes":[{"box":"B01","kind":"insertion|margin note|struck passage|formula with doubt|handwritten number|C/H word disagreement|lower confidence departure","coords":[x0,y0,x1,y1],"reading":"all target text in this box in exact proposed conventions"}],
 "diff_coverage":[{"row":1,"status":"material; P01|macro syntax only|editorial page marker|certainty only|equivalent typography","reason":"concrete reason"}],
 "deletion_insertion_review":["Each C deletion/insertion checked for exact scope and attachment"],
 "open_issues":["places root must decide; do not hide uncertainty"],
 "viewed":["page", "top half", "bottom half", "crop filenames"]
}
```

Allowed collation kinds: misread word; misread symbol or index; omission; text not on the page; deletion state; insertion or placement; abbreviation expanded or spelling modernised; readable ink left as `\\ill{}`; drawing or diagram; other.

Count material differences only. Same visible reading in different macro systems or editorial markers needs no change row/crop. A certainty-only addition belongs in doubts; every resolved C mark still needs its decision and crop. Every material departure from either witness must have an evidence row and a saved crop available to root. Retain marks within struck text unless every letter is visible. All source words, including agreements, require direct visual inspection. A narrow uncertainty must not swallow a readable phrase.

Build audit boxes now for every insertion, margin note, struck passage, whole formula containing any C/proposed doubt, every handwritten number (nearby numbers can share a whole-formula box), every C/H different word, and every departure from C below high confidence. Include source manuscript page number. Keep boxes local, avoid needless large overlapping regions. Exact reading of each box must be available for later blind comparison; the independent reader will receive only image and box coordinates, not these readings.

Do not write a proof or external research. Describe source claims in notes. Perform only mathematical checks that directly aid a reading, and record exactly what was checked. No speculation or conditional theorems. Nothing beyond these pages is researched. Return a brief completion message listing output paths and number of changes/crops/open issues; do not dump the whole report in chat.
