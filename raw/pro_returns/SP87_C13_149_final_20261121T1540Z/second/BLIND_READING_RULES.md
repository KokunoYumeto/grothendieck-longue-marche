# Blind image reading

You are assigned one page that you did not read during the first pass. Read only its source image, anonymous box list, and the crops made from those boxes. Do not read its witness texts, input.json, draft, approved page, report, notes, changes, or `_first.tsv`. Do not search the workspace for candidate readings. Your earlier work on other leaves is not a source for missing ink.

Inspect the source image and anonymous box list for layout and attachment context. Choose rotation angles for boxes whose principal writing is slanted. Run `scripts/prepare_second.py NNN` once for the assigned page, optionally passing a JSON map of box IDs to rotation angles as its second argument (for example, `'{"B003":-35}'`). It loads only the image and box list and saves a crop for each box in `crops/second_149_scanNNN_Bxxx.png`. Read the resulting crop manifest and inspect every crop. The tool applies LANCZOS enlargement, autocontrast, light sharpening, and any supplied rotation. If crops already exist, inspect them without rerunning or replacing them.

Transcribe all legible source content in each box, preserving the French, abbreviations, punctuation, labels, signs, numbers, deletions, insertions, and orientations. A box may include surrounding lines: distinguish its main complete passage from clipped context and explain any scope ambiguity. Do not supply ink that ought to be present. Use a doubt mark where the image does not decide. An uncertain formula is read as a whole.

Save `second/149_scanNNN_second.tsv`, columns `box`, `reading`, with exactly one row per box, in box order. Use Python csv.DictWriter with delimiter tab, so multiline TeX is properly quoted. Save this independent reading before receiving or comparing any first reading. You may also save `second/149_scanNNN_reader_notes.json` with box-specific stroke evidence and remaining doubts. Tell the main reader when both files are complete; do not run the comparison script yourself.

## Macro conventions only

Use standard LaTeX, TikZ/tikz-cd, and these transcription wrappers:

- `\deleted{...}`: cancelled ink; retain the recoverable underlying letters.
- `\inserted{...}`: added writing, at its observed attachment point.
- `\margin{...}`: a marginal note or foliation.
- `\mspage{...}`: author's own page number.
- `\uline{...}` and `\uuline{...}`: one and two underlines.
- `\unsure{reading}` or `\unsure{reading|alternative}`: unresolved reading, the ink-preferred reading first.
- `\illegible{n}`: physically unreadable letters only, not a fallback for a mathematical sign.
- `\diagram{\begin{tikzcd}...\end{tikzcd}}`: actual diagram. The wrapper stands at text level, outside display math.
- `\figure{\begin{tikzpicture}...\end{tikzpicture}}`: actual drawing only. Running text is always transcribed as text.

Preserve vertical equalities and other relations vertically. Do not turn an unheaded shaft into a map from mathematical expectation. Quote marks use two backticks and two apostrophes unless actual guillemets appear. Do not compile TeX. No OCR, recognition tools, outside texts, or external research.
