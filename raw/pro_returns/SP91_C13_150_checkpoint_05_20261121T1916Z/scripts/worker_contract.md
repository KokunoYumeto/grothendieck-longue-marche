# Page reader contract

Read only your assigned page, its C and H files, packet differences and marks, the current notation snapshot, PREAMBLE.tex, and reading_instructions.md. Never OCR or search the internet. Use image viewing, Pillow for crops, and text/file scripts only. Do not inspect other page records or images. Do not delegate: all three available reader slots are in use.

The page is assigned individually. Inspect the whole scan once; inspect the pre-made two full-resolution halves once each, reading every token against both witnesses. Review each insertion and deletion individually. Create and visually read one tight enlarged crop for every lexical C/H difference, every C doubt you resolve, and every other unresolved place. A single crop may encompass a single phrase/formula that contains several adjacent disagreements; list the individual readings separately. No second crop of a decided place before the blind audit. Reuse existing crop files for reinspection. Crop files must live in edition/crops and have unique names beginning 150_scanNNN_. Record original pixel boxes. Do not claim any image inspection that did not actually occur.

Use scripts/crop.py SOURCE NAME X0 Y0 X1 Y1 [ROTATION_DEGREES] to make a crop. The helper saves a lossless PNG at 2400 pixels wide using LANCZOS and autocontrast. You can instead use Pillow directly. View every crop with tools.view_image. A picture returned without explicitly emitting it through image(result.image_url) has not been inspected.

Write proposed full transcription to edition/reader_returns/150_scanNNN.tex. Write edition/reader_returns/150_scanNNN.json with this structure (all substantive observations must be grounded in inspected images):

{
 "scan": "052", "reader": "reader_a", "line_count": 25,
 "changes": [
   {"id":"052-01", "place":"line 1", "C":"literal C reading", "H":"literal H reading", "final":"chosen reading in our macros", "against_C":true, "against_H":false, "kind":"misread word", "error_category":"Words", "marked_in_H":true, "confidence":"high", "evidence":"Exact visible letters or strokes; describe uncertainty precisely.", "crop":"crops/150_scan052_p01.png", "box":[10,20,500,100], "mathematical_consequence":"Only when it changes mathematical content; otherwise empty string"}
 ],
 "decisions": [
   {"id":"M0557","decision":"first|alternative|other|undecided","reading":"exact reading as proposed","evidence":"what the ink shows","crop":"crops/name.png or page","box":[0,0,1,1],"confidence":"high|medium|low"}
 ],
 "inventory": [
   {"element":"E01","kind":"text|display|diagram|drawing|margin note|insertion|deletion","position":"top, lines 1–2","first_words_or_objects":"...","sheet_kind":"text","hand":"his hand","transcribed":"yes"}
 ],
 "doubts": [{"place":"line...","reading":"...","alternatives":"...","confidence":"low","reason":"..."}],
 "notes": [{"id":"150-052-N01","text":"English account of the page's claims; attribute claims to the author. Do not invent or prove conditional theorems. Include manuscript number, author doubts, slips, and mathematics used in readings."}],
 "check_events": [{"statement_id":"150-052-N01","type":"carried as background without fault found","outcome":"Only record genuinely used/checked mathematical statements. Reading alone is not proof checking."}],
 "notation": [{"form":"...","meaning":"...","evidence":"visible use on this page","places":"..."}],
 "abbreviations": [{"written":"ens","expansion":"ensemble","places":"..."}],
 "hand_log": [{"habit":"...","places":"...","scope":"all observed occurrences or specified limitations","witness_errors":"C/H places"}],
 "audit_boxes": [{"box":"B01","kind":"insertion|margin note|struck passage|doubtful formula|handwritten number|lexical disagreement|medium-confidence departure","x0":0,"y0":0,"x1":100,"y1":100,"reading":"exact transcription of only the ink inside the box"}],
 "crops": [{"file":"crops/name.png","box":[0,0,100,100],"purpose":"..."}],
 "unresolved": ["..."],
 "coverage": {"whole_image_viewed":true,"halves_viewed":["top","bottom"],"all_tokens_read":true,"all_C_insertions_deletions_checked":true,"differences_considered":36,"macro_only_differences_ignored":"specify types"}
}

Use booleans for against_C/H based on substantive words, symbols, omission, placement, strike state or figure differences, ignoring equivalent TeX syntax and certainty-only differences. Every actual reading difference from either witness must be represented. Adding doubt without changing text belongs in doubts only. Resolving a C mark belongs in decisions with its required crop even when the letters stand unchanged. Change-log rows may document a doubt resolution as a reading decision but distinguish certainty-only rows from counted textual changes. C/H quotations should be exact locally, while final is the corresponding local reading, not a long unrelated excerpt.

Allowed kind values: misread word; misread symbol or index; omission; text not on the page; deletion state; insertion or placement; abbreviation expanded or spelling modernised; readable ink left as \\ill{}; drawing or diagram; other.
Error categories: Symbols and indices; Words; Omissions; Drawings and diagrams; Readable ink left as illegible; Insertions put in the wrong place; Struck text; Abbreviations expanded, spelling modernised; Text that is not on the page; Other. State-only doubts are separate.

For audit_boxes include every insertion, marginal note, struck passage, whole formula containing any C or proposed doubt, every handwritten number (including foliation and numerals inside formulas), all lexical C/H differences and every less-than-high-confidence departure from C. Combine touching boxes into a phrase or full formula when needed; ensure the reading field reproduces all foreground ink in the chosen box, and make box boundaries tight. Every number on these manuscript pages must be covered by a box. This list will be finalized by the main reader after review. Do not create second-pass crops yourself during the first reading.

Return a concise report to the main reader with paths, principal decisions, remaining uncertainty, and a list of crop files. The main reader will inspect crops and decide. Do not write edition/pages or global logs; do not claim the page is finalized. Preserve disagreements and doubtful ink honestly.
