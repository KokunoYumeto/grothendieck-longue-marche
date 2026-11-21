# First reading: one assigned manuscript page only

Use only the assigned reading_packets/<page>/ directory, these instructions, and your own assigned output files. Do not inspect another page, other readers' reports, the whole source tree, or earlier conversation. No web research; no OCR or text recognition. The images must be visually read with view_image. You are one of exactly three first readers. Await a new one-page assignment after completing this one.

Read reading_rules.md in full before starting, plus PREAMBLE.tex and notation.md. Read C.tex, H.tex, differences.tsv and marks.tsv. Look at page.jpg once for layout, then each supplied full-resolution half once, reading every line and comparing every word and symbol against BOTH witnesses. Agreed text still needs visual confirmation. Check every deletion and insertion: exact strike scope and exact attachment. Track the mathematics as a diagnostic, never as authority over clear ink.

For each unresolved place, every different WORD between C and H, every C doubt mark you resolve, each disputed formula and each final disagreement with either witness, make one tight crop in WORK/crops/<page>_<place>.jpg with Pillow, save its original pixel box, autocontrast and enlarge by LANCZOS to about 2200–3200 pixels across, sharpen if needed. Inspect the actual crop via view_image. No redundant recropping of decided places in the first reading. For a whole formula with a doubt, include the whole formula. State the actual strokes/letters you see, including what remains unclear. Do not replace uncertainty with mathematical expectations. Do not draw running text.

WORK = /workspace/scratch/27306e6fcc57/SP94_C13_151_work

Write your proposed page to WORK/drafts/<page>.tex, and a detailed report to WORK/reports/<page>.json. Do NOT write WORK/pages, aggregate logs, progress.log, notation.md, or another reader's files. Parent will independently view every disputed crop and commit the page. Keep each report self-contained. Use JSON structure below; fields may contain standard LaTeX. This report is working documentation, not a substitute for the final deliverables.

{
  "page": "151_scan036", "scan":36, "reader":"reader_a", "lines_read":20,
  "changes":[{
    "id":"r01", "place":"line 2", "c":"witness C reading", "h":"witness H reading", "final":"proposed final reading",
    "evidence":"Exact visible letters/strokes; explain surviving ambiguity.",
    "confidence":"high|medium|low", "kind":"one collation kind below", "error_category":1,
    "diff_c":true, "diff_h":false, "marked_h":false,
    "crop":"crops/151_scan036_r01.jpg", "box":[0,0,100,100],
    "consequential":"brief mathematical consequence, or empty string"
  }],
  "decisions":[{"id":"M0943","decision":"first|alternative|other|undecided","reading":"as in page","evidence":"what ink shows","crop":"crops/...jpg or page","box":[0,0,100,100],"confidence":"high|medium|low"}],
  "inventory":[{"element":"e01","kind":"text|display|diagram|drawing|margin note|insertion|deletion","position":"top ...","first_words_or_objects":"...","sheet_kind":"text","hand":"his hand","transcribed":"yes"}],
  "doubts":[{"place":"...","reading":"...","alternatives":"...","confidence":"medium|low","reason":"..."}],
  "notes":["English page summary; actual checks and author doubts/slips, numbered as scanNNN.N1 etc."],
  "checks":[{"statement_id":"scan036.N1","type":"carried as background without fault found","outcome":"Only carried as background while transcribing; not proved."}],
  "hand":[{"habit":"...","evidence":"...","every_occurrence":"yes/no/not established","misread_places":"..."}],
  "notation":[{"form":"...","meaning":"...","evidence":"..."}],
  "abbreviations":[{"form":"...","expansion":"..."}],
  "audit_boxes":[{"box":"b01","kind":"page number / insertion / margin note / struck text / doubtful formula / differing words / low-confidence departure","coords":[0,0,100,100],"reading":"ENTIRE transcription of the proposed box, in our conventions; no ellipses","reason":"..."}],
  "deletion_insertion_checks":[{"text":"C macro or new addition","state":"exact scope and insertion attachment confirmed/uncertain","evidence":"..."}],
  "difference_coverage":[{"rows":[1,2],"classification":"macro syntax / textual difference / same reading / editorial marker","change_id":"r01 or empty","explanation":"..."}]
}

Allowed kind values: misread word; misread symbol or index; omission; text not on the page; deletion state; insertion or placement; abbreviation expanded or spelling modernised; readable ink left as \\ill{}; drawing or diagram; other. Error categories: 1 symbols/indices, 2 words, 3 omissions, 4 drawings/diagrams, 5 readable ink left illegible, 6 insertion placement, 7 struck text, 8 abbreviations/spelling, 9 invented text, 10 other. Do not count pure macro or certainty differences as substantive textual corrections; unresolved certainty belongs in doubts. Mark resolution still goes in decisions with its crop and may be described in changes when useful, clearly identified.

Include audit boxes for EVERY insertion, margin note, struck passage, whole formula containing C or proposed doubt, handwritten number (including folio/formula numbers and inline digits), differing C/H word, and non-high-confidence departure from C. Closely adjacent features may share a box only if every required feature is fully visible and its reading is complete. Audit box names must be neutral, e.g. b01, not reading-revealing. These will go to another reader without either witness. Make the boxes generous enough for all relevant ink but no unnecessarily unrelated text. Distinguish bracket/underline/leader from cancellation. Ensure figures and diagrams are actually encoded in TikZ/tikz-cd using the provided conventions.

Every mark in marks.tsv must have exactly one decision, in order. Every literal word difference in differences.tsv must be accounted for and cropped. Macro syntax and editorial page-marker-only differences need neither a crop nor a change row. Use high confidence only where strokes settle it. You may leave genuine uncertainty; do not guess. Preserve misspellings, abbreviations, incomplete parentheses, author's mathematical slips, marginal numbers, underlines and page order. Do not compile TeX.

End with a concise message stating the two files written, number of reading changes/crops, and especially any open decisions the parent must inspect. Do not assert the whole task is complete.
