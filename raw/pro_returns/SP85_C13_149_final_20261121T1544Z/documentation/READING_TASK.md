# Page-reader task

You are one of three readers for a diplomatic transcription of Grothendieck's cote 149. Read only the single page assigned by the main reader, its C/H witnesses and difference/mark rows, the common instructions, preamble, and the supplied current notation table. Do not inspect another page or another reader's output. This is intermediate analysis; the main reader owns final files and saving.

Read `common.md` in this directory in full before the first page, and `PREAMBLE.tex`. Your page packet contains C.tex, H.tex, marks.json, differences.json, and native-resolution top.png / bottom.png. The original image is in `/workspace/scratch/6313bc9439de/source/SP85_C13_149_scans/`. Do not use OCR, image text extraction, web research, or TeX compilation.

1. View the original full image once for layout. View each provided half once, reading line by line against both witnesses, including their agreements. Explicitly check every deletion's scope, insertion's attachment, missing text, abbreviations, accents, small mathematical signs, and manuscript numbering.
2. Make ONE tight crop per unresolved place, plus every different-word C/H disagreement and every C doubt you resolve. Include enough surrounding line/formula to interpret it. Use Pillow, LANCZOS to around 2400 pixels wide (at least 2x), autocontrast; rotate slanted ink if necessary. Do not re-crop decided places. Save to the shared output `SP85_C13_149_work/crops/` with names `149_scanNNN_p01.jpg`, etc. Record ORIGINAL-image pixel coordinates. View every crop you use. No claim of visual verification without actually viewing.
3. Read every word from the ink. Mathematics can flag a problem or distinguish ambiguous glyphs, never supply missing ink. Retain genuine slips. A doubtful cancellation remains doubtful unless ALL letters are plain.
4. Write a complete proposed LaTeX fragment and a structured review JSON under `SP85_C13_149_work/reader_returns/149_scanNNN.tex` and `.json`. Use only supplied macros plus standard LaTeX/TikZ. Do not write final `pages/` files or edit global logs.

## Review JSON schema

Use this schema with enough detail for the main reader to inspect and decide EVERY departure:

```
{
 "page":"149_scanNNN", "scan":NNN, "lines_read":number,
 "rows":[{
   "place":"line/block/position", "C":"exact relevant reading", "H":"exact relevant reading", "final":"proposed reading",
   "against_C":true, "against_H":true,
   "kind":"misread word|misread symbol or index|omission|text not on the page|deletion state|insertion or placement|abbreviation expanded or spelling modernised|readable ink left as \\ill{}|drawing or diagram|other",
   "error_category":"Symbols and indices|Words|Omissions|Drawings and diagrams|Readable ink left as illegible|Insertions put in the wrong place|Struck text|Abbreviations expanded, spelling modernised|Text that is not on the page|Other",
   "scan_shows":"specific visible letters/strokes and attachment; distinguish what is secure from doubtful",
   "crop":"crops/149_scanNNN_p01.jpg", "box":[x0,y0,x1,y1],
   "confidence":"high|medium|low", "marked_in_H":false,
   "consequential":false
 }],
 "decisions":[{"id":"Mnnnn","decision":"first|alternative|other|undecided","reading":"as proposed in the page","ink":"visible strokes","crop":"crops/... or page","box":[0,0,0,0],"confidence":"high|medium|low"}],
 "inventory":[{"element":"E01","kind":"text|display|diagram|drawing|margin note|insertion|deletion","position":"...","first_words_or_objects":"...","sheet_kind":"text|reused_typed|typescript|letter|list|cancelled_draft|cover","hand":"his hand|...","transcribed":"yes"}],
 "doubts":[{"place":"...","reading":"...","alternatives":"...","confidence":"medium|low","reason":"..."}],
 "audit_boxes":[{"box":"B01","kind":"insertion|margin note|struck passage|doubtful formula|handwritten number|handwritten word on typescript|C/H different words|departure below high confidence","coords":[x0,y0,x1,y1],"reading":"exact corresponding proposed transcription"}],
 "notes":"English page summary; claims/questions; his slips/doubts with words; mathematical reading decisions; numbering",
 "hand_log":[{"habit":"...","places":"...","scope":"...","witness_errors":"..."}],
 "notation":[{"form":"...","meaning":"...","evidence":"..."}],
 "abbreviations":[{"form":"...","expansion":"..."}],
 "check_events":[{"statement_id":"...","type":"actual event type","outcome":"..."}],
 "crops":[{"file":"crops/...","box":[x0,y0,x1,y1],"reason":"..."}],
 "open_questions":["..."]
}
```

Set against_C/H truthfully for MATERIAL reading differences; identical text in different macros is not a row. A new doubt over an unchanged reading belongs only in doubts, while a resolved C mark belongs in decisions with its crop. Do not invent a row for folio metadata or H's editorial notes. Match H page number = scan minus one. Keep uncertainty wherever the ink is not decisive. Cover every entry of marks.json in decisions, even one in deleted text. Different words always get a crop with letter-level evidence.

Audit boxes will be sent later to a reader who has NOT read this page. Include every insertion, marginal note, struck passage, entire formula containing any C or proposed doubt, every number written by pen (including folio, formula indices/numerals as necessary), all different-word disputes, and every departure from C below high confidence. Overlapping categories can share a box if it contains the whole relevant passage. Box kind must not disclose a reading. Keep number of boxes reasonable by grouping a contiguous phrase/formula but never omit an eligible occurrence.

The main reader checks each proposed departure on its saved crop; supply the crops for this check, including clear mathematical departures if needed. If the half settles a same-reading editorial state, document it precisely. Return concise status with paths, counts, principal findings, and any open questions. Then wait for the next single-page assignment.
