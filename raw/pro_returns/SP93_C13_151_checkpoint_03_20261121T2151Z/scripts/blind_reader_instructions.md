# Independent image-only second reading

You are a fresh reader. You have not read the assigned page before. Read only the specified original image and `second/<page>_boxes.tsv`. You may use `scripts/prepare_second_crops.py` to crop those boxes; it opens only the original image and box list. Never open witnesses, page transcriptions, reports, reviews, notation tables, first-reading TSVs, comparison TSVs, or another reader's files. Do not inspect other agents.

View the original image for orientation and layout. Make and actually view one enlarged crop of every listed box. The crop script uses Pillow only. Where orientation needs correction, use its `--rotate B001:180` style option based on the image. Do not use OCR, text recognition, external research, or TeX compilation. Output that was truncated before an image was displayed does not count as viewing that image; re-display the already saved crop.

Read all relevant ink in each box independently. Retain the source language, spelling, punctuation, abbreviations, accents as present, indices, arrow directions and ends, incomplete delimiters, cancellations and insertions. Do not supply a mathematically expected character absent from the ink. Preserve uncertainty locally. Separate faint foliation from dark author numbering and exclude paper specks/show-through.

Use diplomatic LaTeX: `\mspage`, `\margin`, `\deleted`, `\inserted`, `\uline`, `\uuline`, `\unsure{a}`, `\unsure{a|b}`, `\illegible{n}`, `\diagram{...}` with tikz-cd, and `\figure{...}` with TikZ, plus standard LaTeX. Transcribe words and letter glyphs as text, never as drawn paths. Reproduce genuine diagram/drawing geometry and labels in code rather than prose. An illegible mark in a mathematical formula still gets a locally doubtful symbol rather than an omitted object.

Write `second/<page>_second.tsv` with columns `box` and `reading`, one row per supplied box in exactly its order, using Python's CSV writer with tab delimiter so multiline LaTeX is quoted correctly. `reading` is the transcription only, without explanations or witness comparisons. If overlaps include partial adjacent content, transcribe the complete intended block and do not invent clipped continuations. A kind may identify another box that covers that adjacent material.

Write a short independent reading note in `second/<page>_reader_note.md` listing actually viewed crop files, remaining uncertainties, and any display failures that were corrected. Do not claim a proof check merely for reading a formula. Save your complete second TSV before sending your completion message. Do not compare it with any prior reading. Root performs comparison and adjudication only after this file exists.

Work on one assigned page at a time and await the next assignment. There is no permission or stopping question to ask.
