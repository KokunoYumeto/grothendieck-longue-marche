# Blind second reading

You receive exactly one page image and its `_boxes.tsv`, with no witnesses,
first reading, transcription, notes or notation table. Do not access any such
files. Work from the image alone. Do not perform OCR or external research.

For each box, use Pillow to crop the listed original-pixel coordinates once,
enlarge with LANCZOS, optionally autocontrast/sharpen/rotate, save under
`crops/<page>_second_<box>.png`, and inspect it visually. Read every word,
symbol, index, accent, punctuation mark, strike and insertion in its target
passage. Include complete adjacent context inside the box. Do not complete
letters clipped by the rectangle or borrow words from another source. Record
clipped neighbouring material as such in a separate observation, if it matters.

Use ordinary LaTeX plus `\deleted{...}`, `\inserted{...}`, `\margin{...}`,
`\uline{...}`, `\uuline{...}`, `\unsure{a|b}`, `\unsure{a}`, and
`\illegible{n}` (only physically unreadable text, never substitute it for an
uncertain mathematical symbol). Preserve the actual spelling and short forms.
Use two backticks and two apostrophes for double quotes. Do not invent balanced
parentheses or punctuation. Read an overwritten underletter only when its
strokes are distinguishable; mark uncertainty where necessary.

Write `second/<page>_second.tsv`, columns exactly `box`, `reading`, in the box
list's order. Write a separate `<page>_second_observations.json` containing your
reader name, inspection list, crop bboxes/rotation and any clipped context or
genuine ambiguity. These files must be completed and frozen before comparison.
Do not inspect `_first.tsv` or any comparison output at any time. Notify the
main reader when complete. Your task is reading the ink; do not harmonize with
another page or expected mathematics.
