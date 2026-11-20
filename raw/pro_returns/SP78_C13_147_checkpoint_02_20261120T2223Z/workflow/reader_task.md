# First reading: one page at a time

You are a diplomatic reader of a single Grothendieck manuscript page. Read only the page packet assigned, the common `reader_rules.md`, this instruction, and the current notation supplied. Do not inspect other pages or the parent's work. Work from the ink, without OCR, internet research or TeX compilation. Never silently normalize a spelling, abbreviation, mathematical slip or punctuation. A doubt must stay when ink does not decide.

1. Read `reader_rules.md` completely, your packet's C.tex, H.tex, differences.tsv, marks.tsv, PREAMBLE.tex, notation.md.
2. Use view_image to look at scan.jpg once for layout. Use view_image on top.png and bottom.png once each at native resolution, reading all physical lines and every letter, sign, index, insert, deletion, margin note and figure against both witnesses. Go explicitly through each deleted/inserted span from C to check its extent and placement. Treat H editorial page labels/synopses as editorial, not ink.
3. Crop each ambiguous place exactly once. Always crop differing WORD readings between C and H, every C doubt you resolve (including doubts inside strikes), unclear insertions and deletions, and doubtful formulas in full. Use Pillow, original pixel box, autocontrast, LANCZOS resize to 2000–3000 pixels wide, modest sharpening only as needed, rotation for slanted writing. Save PNGs in the shared work/crops/ directory with unique `147_scanNNN_placeXX.png` names. View every crop. A single crop can cover a tightly contiguous formula or word group but not a whole half. Do not crop a decided place a second time. Give precise ink evidence (letter shapes, ends of arrows, stroke coverage), not merely 'clear'. Retain uncertainty under cancellation unless every letter is plain.
4. Return a complete proposed diplomatic page, no preamble, using C's macro convention, to work/reader_returns/147_scanNNN/proposed.tex. Do not write the parent's final pages directory or global logs.
5. Write work/reader_returns/147_scanNNN/report.json with this schema. Use real strings (JSON properly escaped), original pixel boxes and crop basenames. Arrays can be empty where appropriate.

```
{
 "scan":54,"reader":"reader_a","physical_lines_read":0,
 "changes":[{"id":"054-01","place":"line ...","C":"...","H":"...","final":"...","evidence":"specific strokes/letters seen","crop":"147_scan054_place01.png","box":[0,0,1,1],"confidence":"high|medium|low","against_C":true,"against_H":true,"kind":"misread word|misread symbol or index|omission|text not on the page|deletion state|insertion or placement|abbreviation expanded or spelling modernised|readable ink left as \\ill{}|drawing or diagram|other","marked_in_H":false,"error_sheet_kind":"symbols and indices|words|omissions|drawings and diagrams|readable ink left as illegible|insertions put in wrong place|struck text|abbreviations expanded spelling modernised|text not on page|other","consequential":false}],
 "decisions":[{"id":"M...","cote":147,"scan":54,"decision":"first|alternative|other|undecided","reading":"...","ink":"...","crop":"filename and (x0,y0,x1,y1) or page if undecided","confidence":"high|medium|low"}],
 "inventory":[{"scan":54,"sheet_kind":"text","hand":"his hand","element":"01","kind":"text|display|diagram|drawing|margin note|insertion|deletion","position":"...","first_words_or_objects":"...","transcribed":"yes"}],
 "doubts":[{"place":"...","reading":"...","alternatives":"...","confidence":"medium|low","reason":"..."}],
 "notes":["English account of what page states, computes or asks; label claims as manuscript claims. Record author slips/doubts verbatim, and mathematics used for reading, without claiming a proof not done."],
 "check_events":[{"statement_id":"147-054-N1","date":"current UTC","who":"reader identity, actual model and effort if known","type":"targeted proof check|independent re-proof|computation or formal certificate|used and rechecked in this run|carried as background without fault found|refuted, with refined id","outcome":"exactly what was and was not checked"}],
 "notation":[{"sign":"...","reading":"...","evidence":"...","scope":"..."}],
 "hand_log":[{"habit":"...","pages":[54],"all_occurrences":"...","witness_misreadings":"..."}],
 "abbreviations":[{"written":"...","expansion":"..."}],
 "second_boxes":[{"box":"B01","kind":"insertion|margin note|struck passage|doubtful formula|handwritten number|word disagreement|non-high-confidence change","x0":0,"y0":0,"x1":1,"y1":1,"reading":"the proposed page's exact reading of everything in this box"}],
 "unresolved":["..."],
 "witness_comparison":"brief actual strengths/weaknesses on this page"
}
```

Every substantive final-vs-C OR final-vs-H difference must have one change row. Do not count macro syntax alone. Certainty-only ADDED doubts go to doubts, not changes; RESOLVED C doubts get decisions and evidence (a change row if substantive). Preserve substantive differences even when retaining C. Distinguish word omission from wrapper differences. Ensure H's normalized/expanded abbreviations and omitted struck text are recorded. Record exactly every MARKS.tsv row in order in decisions, and no extra decision IDs. Put doubtful struck text absent from MARKS.tsv in doubts, not decisions.

For `second_boxes`, cover every insertion, margin note, struck passage, formula with a C or proposed doubt, handwritten number (a full formula/line may encompass multiple numbers), word disagreement, and less-than-high-confidence departure from C. Boxes may cover closely adjacent items; give all ink in the box in its reading. Box labels and kinds must not reveal readings. For second-box readings, use exact TeX from the proposed page, including TikZ rather than prose for drawings. Keep separate pencil foliation in margin{}, not mspage{}. Use tight intelligible crops with enough context. The parent will save first readings separately for a different, blind reader.

Count physical manuscript lines read (explain treatment of displays/margins in a note), crop places, and changes. Before returning, check proposed.tex covers all inventory elements, all MARKS ids are present, and all crops cited exist. Do not claim your proposed page is final: the parent must review disputed crops.

Send the parent a short completion message with the two return paths, important issues and counts. Wait for the next assignment; do not start another page yourself.
