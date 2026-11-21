# Independent second reading: image alone

You are given exactly one page you did NOT read in the first pass, its source image, and second/<page>_boxes.tsv. Read only that image and box list. Do not read witnesses, page text, reports, draft, notes, notation table, _first.tsv, or other files that reveal its first reading. Do not consult the other readers. No OCR, image-to-text libraries, web, or published versions.

Use the established editorial conventions from the first-pass instructions (standard LaTeX, \deleted{}, \inserted{}, \margin{}, \unsure{reading|alternative}, \illegible{n}, \uline{}, \uuline{}, \diagram{tikzcd}, \figure{tikzpicture}); do not use the first-pass text of this page. Read what is visible, preserving cancelled and inserted words, alphabets, digits, punctuation and diagrams. If a clear glyph seems mathematically wrong, retain it. If the strokes do not decide, keep a doubt.

For each row in the box list, crop that box from the supplied original image once, autocontrast and enlarge with LANCZOS to roughly 2200–3200px wide, rotate when needed, save to WORK/crops/second_<page>_<box>.jpg, and inspect it visually. Read ALL ink intended in the box, including number, surrounding words that are fully within it, cancellations, insertions and relevant diagram parts. Do not import missing edge words. Use an editorial \unsure{} only for actual uncertainty in visible ink; do not silently restore context outside the box. A box that intentionally repeats part of another must still have its own independent reading.

Write second/<page>_second.tsv with columns box,reading (one row for each box, in the box list order). Write it before discussing your readings with the parent. Also write second/<page>_independent_notes.md with the box id and any uncertainty, and record the source image, crop paths, original boxes, rotations, your agent name, and UTC completion time. This is documentation of the blind reading. Do not include or inspect another page.

WORK=/workspace/scratch/27306e6fcc57/SP94_C13_151_work

Return a concise message naming the saved TSV, number of boxes, and any unresolved readings. The main reader will then compare both written readings by script and decide disagreements on the crops. Wait for the next assignment.
