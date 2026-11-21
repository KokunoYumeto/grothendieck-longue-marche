# Independent reading from images

This phase begins only after all 23 first readings are finalized. A reader must not receive a page they read in the first phase.

For the assigned scan, access only the original image, the neutral `second/149_scanNNN_boxes.tsv`, the crop-generation script, this method, and the transcription macro conventions already supplied. Do not open the witnesses, a proposed or finalized page, a review report, notes, `_first.tsv`, other readers' output, or notation decisions for the assigned page.

Run `python3 edition/scripts/crop_boxes.py NNN` once to make every listed box at large resolution from the original image. Personally inspect every resulting crop. If a note is slanted, rotate that same crop upright and record the angle in the manifest; do not replace a reading with OCR or text recognition. The neutral kind names identify layout only, not proposed words.

Transcribe the intended text or formula inside each box, preserving written abbreviations, punctuation, alphabets, primes, indices, insertions and deletion state. Where a complete formula is boxed, read every sign in it. When the rectangle necessarily contains text from a neighboring baseline, separate the target baseline according to the neutral kind and the visible layout; record any unavoidable scope uncertainty in an independent note. Do not invent content cut off by a boundary. A doubt is expressed with `\unsure{...}` or alternatives; mathematical plausibility alone cannot settle the ink.

Write `second/149_scanNNN_second.tsv`, exactly two columns `box` and `reading`, in the order of the supplied box list. Write this independent reading before any comparison is run. Do not revise it after learning the first reading; later adjudication belongs in a separate file. Optional source-grounded observations may be saved in `second/149_scanNNN_second_notes.md`.

Report the number of boxes inspected, the output path, and any physically clipped target. Do not run the comparison yourself or inspect its output. The main reader will compare the frozen readings token by token and adjudicate every difference on the saved crop.
