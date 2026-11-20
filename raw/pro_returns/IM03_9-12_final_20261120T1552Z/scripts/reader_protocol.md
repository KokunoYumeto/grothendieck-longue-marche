# One-page reader protocol

You are one of exactly three readers. Work only on the one page assigned in your current task. Do not read other pages or rows, do not unpack the archive, and do not spawn agents. The main reader assigns the next page when you are free.

Read the assigned original .tex, its scan .jpg, its rows.tsv, and source/PREAMBLE.tex. Inspect the image directly with view_image. No OCR, PDF text layer, or text recognition. For every relevant place, make a tight crop at the original coordinates with scripts/crop_scan.py, enlarged to 2400–3200 pixels wide with raised contrast; then view it. Save crops as crops/<page>_<id>_<place>.jpg. Multiple separate places need separate tight crops. In notes describe actual visible strokes, not simply the proposed mathematical reading. Avoid seeing a watermark or paper speck as ink.

Decide every row:
- a = our misreading: edit to what is written, in the page's own macros.
- b = the ink is as our transcription but the correction is a mathematical amendment or his slip: leave text unchanged and explain written versus intended in notes.
- c = the original page already has the requested reading: leave unchanged.
- d = not on this page: leave unchanged and give location only if actually seen.

Always inspect all assigned row places in this run. Required especially for checked_on_scan=no; flag/open/not-sorted/second-model rows; disagreement between row and actual transcription. Apply Michel Hua's human facsimile checks unless the ink plainly contradicts them and document why. Where ink cannot settle a material reading, use \unsure{reading|alternative}, never choose by mathematical plausibility alone. Resolve the proposal as far as possible, explicitly flagging anything the main reader must decide.

Change no unrelated wording, accents, spelling, notation, spacing, line breaks, or formatting. Preserve his mathematical slips. Keep tikz-cd diagrams. Struck words use \deleted{…}; insertions \inserted{…}; margin notes \margin{…}; doubt \unsure{…}; illegible ink \illegible{n}.

Original TeX files use CRLF. Read using read_bytes().decode('utf-8') and write_bytes(...encode('utf-8')); preserve every unedited byte.

If a row proposes a mathematical amendment unsupported by ink, classify b and keep the original text including existing uncertainty macros. Record the visible reading and any mismatch between the row quotation and actual TeX in notes. A direct facsimile correction that explicitly resolves a doubt is different and should be applied when supported.

Output in reviews/<page>/:
1. proposal.json: object with page, reader, inspected_at_utc, rows. Each row has id, cote, scan, decision, find, replace, what_the_ink_shows, confidence (high/medium/low), notes, crops (array of paths relative to work root), unresolved (boolean). For a, find is the exact original string and must occur exactly once in original; replace is corrected same span. For b/c/d, find and replace are empty. For duplicate corrections at the same place, explain relationship; do not manufacture an additional unrelated change. Escapes/newlines must round-trip exactly.
2. proposed.tex: source page after only listed (a) edits. Keep original bytes elsewhere unchanged, including final newline. If multiple rows share an edit, apply it once.
3. Optional terse reasoning.md only if needed beyond row notes.

Use the supplied crop script so crop coordinates are preserved in crops/manifest.tsv. Do not edit global placements.tsv, notes.md, CHECK_EVENTS.tsv, progress.log, edited_pages/, or other readers' directories. Do not save to Library yourself. The main reader checks returns and writes final pages.

Return a concise summary of row decisions, exact proposed edits, what the ink shows, crop paths, and any uncertainty. Record your model as inherited GPT-6 Astra Pro and effort as not separately exposed, unless runtime explicitly supplies a different actual value. A transcription/image comparison is “used and rechecked in this run”; do not claim proof-checking or formal verification of the mathematics.
