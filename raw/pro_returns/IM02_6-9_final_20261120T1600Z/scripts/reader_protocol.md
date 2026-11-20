# Assigned-page reader protocol
You are one of three page readers. Work ONLY on the one assigned page, its scan, its correction rows and the provided PREAMBLE. Do not inspect other pages or the full corrections table. No web research, OCR, PDF text extraction, or any text-recognition library. Inspect images yourself using view_image; crop with Pillow, enlarge a tight crop for each relevant place to about 2400–3200 pixels across with raised contrast, inspect that crop, and retain it under the designated crops path. You may inspect all row loci, including previously scan-checked ones.

For EACH supplied row choose a/b/c/d:
(a) Our misreading: change our text to the visible ink in its existing macros.
(b) His slip or a mathematical refinement: ink matches our text and correction says what he meant; retain text and explain in note what is written and what proposed refinement means. Do not claim to prove the mathematical refinement.
(c) Already as row asks: no change.
(d) Not on this page: no change; say location only if this page's evidence identifies it.
All checked_on_scan=no rows, flags, open or not-sorted rows, second-model rows, and row/current-TeX discrepancies MUST be decided by directly viewing the scan. Apply Michel Hua's human checks unless ink plainly contradicts them; explain any contradiction. Do not misclassify a plain transcription correction as mathematics. If the ink cannot settle the reading, put \unsure{reading|alternative} at that very place; never silently guess. An absent requested addition is not licensed merely by mathematics or another reader's assertion.

Preserve ALL unrelated bytes. No reformatting, normalizing, spelling, accent, abbreviation, punctuation or mathematical repairs outside row loci. Keep tikz-cd diagrams. \deleted{...} for cancellations, \inserted{...} for insertions, \margin{...} for margin notes, \unsure{...} for doubts, \illegible{n}. Paper watermark EXTRA STRONG and paper specks are not ink.

Your working input folder contains page.tex, scan.jpg, rows.json and PREAMBLE.tex. Return a report JSON under reviews/<pagekey>.json and a proposed file reviews/<pagekey>.proposed.tex. Do not write edited_pages, placements.tsv, CHECK_EVENTS.tsv or progress.log: the main reader owns final writing and review. You may write crop-generation scripts under deliverables/scripts/<pagekey>_crops.py and crops under deliverables/crops/<pagekey>_<rowid>_<locus>.jpg. Retain every image crop you use as evidence. Inspect each generated evidence crop yourself.

Report shape:
{
 "page": "6_scan032", "reader": "reader_1", "model": "GPT-6 Astra Pro", "effort": "inherited; not exposed", "completed_utc": "...",
 "rows": [
  {"id":"...","cote":"6","scan":"32","decision":"a|b|c|d",
   "find":"exact original unique span for a; empty otherwise",
   "replace":"same span with correction for a; empty otherwise",
   "what_the_ink_shows":"Concrete visual strokes/letters, and relative crops/... path(s); distinguish observation from inference.",
   "confidence":"high|medium|low",
   "note":"For b: written text + supplied intended refinement, no independent proof claimed. For d: absence/location. For unresolved ink: alternatives and reason.",
   "unsettled":false,
   "events":[{"date":"UTC timestamp", "who":"GPT-6 Astra Pro; effort inherited (not exposed); reader_N; run IM02_6-9_20261120", "type":"used and rechecked in this run", "outcome":"Actual scope of visual or textual check; do not label reading as proof."}]
  }
 ],
 "crops":["crops/...jpg"],
 "open_questions":[]
}

Each a find span must occur exactly ONCE in page.tex as originally supplied; use sufficient context. Minimal changes inside that span. All proposed edits should be non-overlapping relative to the original. If overlapping row loci prevent this, explain explicitly for main-reader resolution. Build proposed.tex only from those recorded a replacements. For b/c/d, find/replace empty. If uncertainty requires an added doubt mark, choose a and document it. For a previously existing doubt that remains unresolved with the same alternatives, do not change it; choose the closest honest category and explain.

Return concise results with report path, per-row decision and crop paths. If confident no further progress is possible, return the uncertainty for main-reader decision; do not wait for the user. After this page, stop until the main reader supplies the next single-page assignment. Do not delegate: the three readers are already active.
