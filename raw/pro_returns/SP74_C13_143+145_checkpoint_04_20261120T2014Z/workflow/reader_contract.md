# Reader contract

You are one of three readers for a diplomatic transcription. Work ONLY on the assigned page. Do not read other page packets or images. Read reading_guidelines.md, the assigned JSON packet (contains C, H, PREAMBLE, marks, raw differences and image paths), and the current notation.md supplied by the main reader. No web research, OCR, text-recognition software or TeX compilation.

Read the full image ONCE for layout, then both existing full-resolution halves ONCE each, line by line against both witnesses. Start with C/H differences but inspect EVERY word/sign/index/underline/deletion/insertion/margin, including where C and H agree. Use tools.view_image and emit the returned image; calling without actually viewing its output is not inspection. Do not upscale whole halves. For unresolved places create ONE tight crop per place with Pillow from the original, use LANCZOS scaling to about 2400–3200 pixels width, autocontrast, sharpen faint ink, rotate if necessary. Save to work/crops/KEY_descriptive-name.png with original pixel box recorded. Do not crop settled places again. The main reader will inspect the crops or create one where necessary.

Work output root: /workspace/scratch/8f839dff4bf0/SP74_C13_143+145_work
Write your candidate only to reviews/KEY_readerX.tex and reviews/KEY_readerX.json. Do not edit final pages, shared notation, or aggregate logs. Reader identity X will be A, B or C, as assigned. Create scripts under scripts/ if useful, with page and reader in the name. Crops are shared and must have unique names.

JSON report schema (all fields required; [] when empty):
{
  "key":"143_scan008", "reader":"A", "stage":"first", "image_views":["original","half1","half2"],
  "changes":[{"place":"line or block", "C":"exact witness excerpt", "H":"exact witness excerpt or [no witness]", "final":"exact final excerpt", "against_C":true, "against_H":false, "kind":"allowed collation kind", "ink":"specific visible strokes/letters/deletion or insertion attachment, not merely 'clear'", "confidence":"high|medium|low", "crop":"crops/KEY_name.png", "box":[0,0,1,1], "marked_in_H":false, "consequential":false}],
  "decisions":[{"id":"M...", "decision":"first|alternative|other|undecided", "reading":"exact final reading including unsure if retained", "ink":"observed evidence", "crop":"page or crops/name.png", "box":null, "confidence":"high|medium|low"}],
  "inventory":[{"sheet_kind":"text", "hand":"his hand", "element":"E01", "kind":"text|display|diagram|drawing|margin note|insertion|deletion", "position":"top to bottom and optional box", "first_words_or_objects":"...", "transcribed":"yes"}],
  "remaining_doubts":[{"place":"...", "reading":"...", "alternatives":"...", "confidence":"low|medium", "reason":"..."}],
  "certainty_resolutions":[{"place":"...", "C":"...", "final":"...", "ink":"..."}],
  "notation":[{"form":"...", "meaning":"...", "evidence":"..."}],
  "abbreviations":[{"form":"...", "expansion":"..."}],
  "hand_log":[{"habit":"...", "places":"...", "scope":"all occurrences inspected or qualified", "misreadings":"..."}],
  "notes":[{"id":"KEY-N1", "text":"English account of what page states/asks, source scope only, author doubts/slips quoted exactly, mathematical reading decisions"}],
  "check_events":[{"statement_id":"...", "type":"targeted proof check|independent re-proof|computation or formal certificate|used and rechecked in this run|carried as background without fault found|refuted, with REFINED-ID", "outcome":"actual check performed; transcription alone is not proof"}],
  "unresolved_for_main":[], "raw_difference_disposition":"Explain that all packet differences were inspected; markup-only differences excluded."
}

Use allowed collation kind values: misread word; misread symbol or index; omission; text not on the page; deletion state; insertion or placement; abbreviation expanded or spelling modernised; readable ink left as \\ill{}; drawing or diagram; other.

Every material difference from either witness must have a changes row, even if final=C. Pure macro syntax is excluded. Certainty changes alone belong to certainty_resolutions and decisions, not changes. Keep each distinct locus separate, although one mathematical expression at one locus can be a row. If a change is settled by halves use crop="page" and box=null; the main reader creates a crop if needed. If a locus remains uncertain, retain \\unsure in candidate and describe alternatives honestly. Inventory every text block/display/diagram/drawing/marginal item/insertion/deletion. Marks must all have decisions, in packet order. List notes as source accounts, not assertions of mathematical proof. If you used or checked a mathematical assertion for a reading, log the actual check type; background claims can be logged as carried as background without fault found, expressly not proved.

At completion send main reader: exact candidate/report paths, concise material findings, all unresolved places and crop filenames. Do not announce that the final page is done; main reader adjudicates and writes it. Wait for next one-page assignment.
