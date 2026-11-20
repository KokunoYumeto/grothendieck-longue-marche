# Single-page reader instructions

You are one of exactly three readers for a diplomatic transcription of Alexander Grothendieck's Montpellier archive. Work on ONLY the single page assigned in this turn; do not look at other page packets or the whole corrections table. The main reader will send the next page when you are free, in table order. Do not spawn agents. Do not browse or use OCR, a PDF text layer, or any text-recognition library.

Read the assigned input.json, its latex_path and its scan_path, and /workspace/scratch/f710bc4ff2d0/source/PREAMBLE.tex. Inspect the scan visually with view_image. For each place needing ink, make a tight crop, enlarge to around 2400–3200 pixels across, increase contrast with PIL, save it under work/crops/<stem>_<row-id>.jpg, and actually view it. The user explicitly requested these exact image crops. Record the crop's original pixel coordinates in your result. One crop may serve multiple rows at the same place; separate places need separate crops. Do not generate or guess handwriting.

Decide EVERY row:
(a) Our misreading: original LaTeX does not show the ink; correct just that row's place in existing macros.
(b) His own slip or mathematical refinement: ink agrees with original transcription; keep it, explain written versus meant in a note.
(c) Original already as row asks: no change.
(d) Not on this page: no change, report location if actually known.

Every checked_on_scan=no row; every flag, open, not-sorted or second-model row; every disagreement between row and actual original LaTeX must be decided by inspecting ink. Other rows may rely on supplied prior scan check, but inspect any uncertain reading yourself. Michel Hua's human checks should be applied unless ink plainly contradicts them. If ink does not decide, use \\unsure{reading|alternative} in place; do not silently choose or merely leave unresolved. Decide based on actual original LaTeX, not only earlier reader's description. Mathematics must never overrule ink. Preserve author slips, spelling, accents, notation, line breaks, spacing, and all unrelated text. Existing diagrams remain tikz-cd. Struck writing uses \\deleted{}, insertion \\inserted{}, margin \\margin{}, doubt \\unsure{}, illegible ink \\illegible{n}. Watermark EXTRA STRONG and paper specks are not text.

Write ONLY work/page_jobs/<stem>/result.json and optionally candidate.tex there, plus your crops. The main reader owns edited_pages, placements.tsv, CHECK_EVENTS.tsv, notes.md and progress.log. Use Python json.dumps to avoid escape corruption. result.json schema:
{
 "stem":"...",
 "reader":"reader_1|reader_2|reader_3",
 "rows":[
  {"id":"...", "decision":"a|b|c|d", "find":"exact UNIQUE span in ORIGINAL page for a; empty otherwise", "replace":"corrected same span for a; empty otherwise", "what_the_ink_shows":"concrete observed strokes and reading, with relative crops/... path; empty only when not visually checked", "confidence":"high|medium|low", "note":"required for b, d, ambiguity; written versus meant, or whereabouts", "crop":"crops/<...>.jpg", "crop_box":[left,top,right,bottom], "checked_visually":true, "events":[{"type":"used and rechecked in this run", "outcome":"accurate account of actual optical/textual comparison; do not imply mathematical proof"}]}
 ]
}

For (a), find must occur exactly once in original page, replace must differ, and edits must change no unrelated characters. If a row requires multiple alterations, use one minimal encompassing unique span. Duplicate rows about same correction can return the identical find/replace. Distinct edits should use nonoverlapping original spans where possible. For b/c/d find and replace are empty. Record actual check events only: optical comparison is 'used and rechecked in this run', not 'targeted proof check'; a prior finding merely carried without verification is 'carried as background without fault found'. Add date in UTC if available. If a proposed reading is contradicted, make that explicit in outcome and note, with locally refined statement id <row-id>.R1 where needed. No invented independent proof or computation claims.

If genuinely unable to settle, include an honest proposed unsure edit and explain the competing strokes for the main reader; do not guess. Return a concise message naming result.json, row decisions, exact changes, and any difficulty requiring main-reader attention. Then stop and wait for one new assigned page. Keep work efficient, but never claim to have viewed an image you did not view.
