# First-reader return format

Work on only your assigned scan. Read `reader_rules.md` in full before the first page. No OCR, text recognition, web research, or TeX compilation. You may use Pillow to crop. The packet supplies this page only: page.jpg, top.jpg, bottom.jpg, C.tex, H.tex, differences.tsv, marks.tsv, PREAMBLE.tex, notation.md. View whole page once, both halves once, then crop all C/H word disagreements and all C doubts you propose to resolve, plus every unresolved small sign, strike, insertion or crowded passage. Independently compare all unmarked text too. Inspect each deleted/inserted span separately for boundaries. Never claim you saw a crop without viewing it.

Create crops with `python /workspace/scratch/12caffedf246/edition/scripts/crop.py SCAN PLACE X0 Y0 X1 Y1 [ANGLE]`; coordinates are in the original page. Use `tools.view_image` and emit its image result. Only one first-pass crop of each place. Each crop gets a few thousand pixels width. If several marks occupy the same whole formula or passage, one crop can establish them all, but identify the span of each.

Write your proposed full page to `edition/reports/147_scanNNN_proposed.tex`. Write `edition/reports/147_scanNNN_report.json` with:

```
{
 "scan": 108,
 "reader": "reader_a",
 "line_count": 20,
 "rows": [
  {"place":"line 2", "C":"literal C span", "H":"literal H span", "final":"final span", "scan_shows":"Precise visual evidence: which letters/strokes are plain, which are not.", "crop":"crops/147_scan108_place.jpg", "box":[0,0,100,100], "confidence":"high|medium|low", "kind":"one of requested H-collation kinds", "against_C":true, "against_H":true, "marked_in_H":false, "math_consequential":false, "error_category":"Symbols and indices|Words|Omissions|Drawings and diagrams|Readable ink left as illegible|Insertions put in the wrong place|Struck text|Abbreviations expanded, spelling modernised|Text that is not on the page|Other"}
 ],
 "decisions":[{"id":"M1167","decision":"first|alternative|other|undecided","reading":"literal final reading including unsure wrapper when retained","ink":"specific visual evidence","crop":"crops/filename.jpg","box":[0,0,100,100],"confidence":"high|medium|low"}],
 "inventory":[{"element":"E01","kind":"text|display|diagram|drawing|margin note|insertion|deletion","position":"precise page location","first_words_or_objects":"verbatim start","sheet_kind":"text","hand":"his hand","transcribed":"yes"}],
 "doubts":[{"place":"line 2","reading":"...","alternatives":"...","confidence":"medium"}],
 "notes":["English note explaining what page claims, with scan/place, and any mathematical reading test; do not claim proof verification merely from transcription."],
 "check_events":[{"statement_id":"S108-01","type":"targeted proof check|independent re-proof|computation or formal certificate|used and rechecked in this run|carried as background without fault found|refuted, with refined statement id","outcome":"what was actually done"}],
 "hand_log":[{"habit":"visual habit","places":"specific locations","scope":"observed extent; do not claim universality without evidence","misreadings":"C/H readings affected"}],
 "notation":[{"notation":"...","meaning_or_form":"...","places":"..."}],
 "abbreviations":[{"form":"...","expansion":"..."}],
 "second_boxes":[{"box":"B01","kind":"number|insertion|margin note|struck passage|doubtful formula|different words|low confidence departure","coords":[0,0,100,100],"reading":"your full reading of the text inside this tightly selected box"}],
 "unresolved":["..."],
 "deletion_insertion_checks":[{"span":"exact C span","finding":"boundaries/attachment seen in image"}]
}
```

Rows: one per substantive location where final differs from C or H. Do not create rows for syntax-only changes or adding uncertainty alone. A resolved C doubt does need its decision and crop; a certainty-only resolution can be kept in decisions rather than inflating textual changes. H editorial summaries/page explanations are not ink and are not omissions. Do not use the raw scripted diff rows as the log without judging them.

Allowed `kind` values are: `misread word`; `misread symbol or index`; `omission`; `text not on the page`; `deletion state (struck given live or live given struck)`; `insertion or placement`; `abbreviation expanded or spelling modernised`; `readable ink left as \\ill{}`; `drawing or diagram`; `other`.

Inspect all C doubt macros, including in struck text, even when MARKS.tsv does not give them IDs. Only supplied IDs go in `decisions`, but every retained doubtful passage belongs in `doubts` and, where applicable, `second_boxes`.

Second-box list MUST cover every insertion, margin note, struck passage, doubtful whole formula (C or proposed text), every handwritten number (including manuscript page numbers, formula labels, small integers in formulas), every C/H different word, every departure from C below high confidence. Combine only genuinely contiguous marks; a box must be tight enough that its reading is unambiguous. Covering adjoining symbols with one formula box is appropriate. Provide reading of the WHOLE box, not just a selected word inside it, to make the blind comparison meaningful. Avoid whole-page boxes. All boxes coordinates must fit page dimensions.

Send a concise return to root with paths, change/mark/crop counts, difficult decisions, and page completion. Do not save to Library or edit root deliverable files yourself. Do not spawn subagents: all three available slots are assigned to page readers. Await the next one-page assignment.
