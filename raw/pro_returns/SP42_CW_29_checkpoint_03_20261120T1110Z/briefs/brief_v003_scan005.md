# Reader brief v003 — first used on scan 005

You are one of three independent readers of exactly ONE archive page. Your run ends after that page. Do not look at another reader's files, returns, crops, or messages; do not look at other page images or texts. Your task message gives a reader label, page packet, image base, and an output directory. Only inspect those source files, the packet PREAMBLE.tex, this brief, the notation snapshot in the packet, and your own files. No internet or outside sources; no OCR, text-recognition library, PDF text layer, or automated image-to-text pipeline. Use the image-viewing tool yourself.

## Authority and order

The INK is the authority. C and H are independent, unchecked AI drafts. Their agreement never validates a reading. Verify every agreed word and sign against the page, as well as every difference. Retain genuine typos, incomplete notation, blanks reserved by a typist, and surprising mathematics. Do not silently normalize them. Prior C doubts and notes are questions to inspect, not established results. S, if present, is another witness to confirm or overturn from the image; editorial mathematical proposals never enter the diplomatic text.

## The reading workflow (a–d)

a. View the whole image ONCE, for layout: all text blocks, displays, diagrams, drawings, marginal writing, insertions and deletions. Record positions and handwriting/type distinctions.

b. View the two supplied full-resolution halves, `_a.jpg` and `_b.jpg`, ONCE EACH, in order. Read line by line against `C.tex` and `H.tex`. Read every word, accent, abbreviation, punctuation mark, symbol, alphabet, subscript, superscript, prime or exclamation mark, arrow direction, inequality, parenthesis, underline, deletion and insertion. Read margins and tilted writing in full. Do not enlarge a whole half again. The halves overlap; record the whole-image coordinates of each disputed place. Whole-image coordinates, not coordinates within a half, are required in your report. You may get image dimensions and compare overlap with Python; do not use text recognition.

c. List places that remain open after the halves: a still unresolved witness difference; a C doubt not settled by the halves; a small mathematically decisive sign; slanted, struck or crowded writing. Crop each such place ONCE, tightly, including about one surrounding line. Enlarge it with LANCZOS to about 2,000–3,000 pixels across, use autocontrast and sharpening if faint, rotate tilted writing upright. Use `scripts/crop.py` or equivalent PIL operations; these are explicitly requested evidence operations, not creative image editing. View each crop. Do not crop a place the halves already settle; do not recrop or repeatedly view a settled place. Save crops as JPEG quality 95 (subsampling 0) with coordinate/transform metadata under your own output directory. Include all of the target glyph: do not clip a descender, prime or subscript at the crop edge. Where the halves settle a difference, provide a tight bounding box so the main reader can inspect it independently.

d. Return the complete page reading in our LaTeX conventions and EVERY substantive place where it differs from either witness, with the actual letters, strokes or marks observed, confidence, and the half/crop used. Also return every C doubt, whether resolved or retained, and every S row, whether confirmed or overturned. Follow the mathematics while reading: an expression that fails to parse, an inconsistent index or arrow, or a contradiction is a reason to look again; the ink still decides. Record mathematical checks only if actually performed, distinguishing them from simply reading a claim. Do not claim independent proof if you only checked notation or quoted the page.

## Transcription conventions

Use exactly the attached PREAMBLE macros plus standard LaTeX, amsmath, amssymb, mathrsfs, TikZ, tikz-cd, ulem and enumitem. No custom notation macros. Keep the language and spelling, accents or their absence, numbering, punctuation, abbreviations and paragraphs. Never expand abbreviations in the transcription. Join words hyphenated solely at a line break. Keep heading, address and signature line breaks with `\\`.

`\scanpage{N}` begins each page. Preserve `\cotefile{29}` only on scan 003. Visible author/typed page numbers use `\mspage{n}`; archive numbers go only in `% archive sheet number: n` comments. Preserve them in the inventory, but do not count H’s omission of archival comments as a substantive manuscript-reading difference. A typed/authorial page number omitted by H DOES count. Letterheads are fully transcribed with `% letterhead`; archive/library stamps are comments.

Use `\handwritten{...}` for the handwritten part of a typescript, `\deleted{...}` for readable cancellations/overtyping, `\inserted{...}` at the actual insertion point, `\margin{...}` for a non-insertion marginal note, `\uline{...}` and `\uuline{...}` for underlines. A visible but uncertain deletion still needs its state. A correctly positioned hand completion already encoded by \handwritten (for example a final e occupying a typed blank) need not acquire an additional \inserted wrapper. Such equivalent state wrappers and closing-line layout differences alone do not count as substantive differences. Do not collapse alternative correction orders into one confident order unless the ink establishes it. Typescripts have no bold; a double-struck letter is `\mathbb`, not `\mathbf`. Inspect candidate doubled letters individually, especially headings and functor names.

Use the exact letter/alphabet, indices, exponents, bars, hats, tildes and arrows written. `^!` and a prime are different. Keep missing arrow or bracket slots as visible spacing, never supply the mathematically expected symbol. His double quotation marks are two backticks and two apostrophes; guillemets only when drawn. Diagrams must be typeset using `\diagram{\begin{tikzcd}[ampersand replacement=\&] ... \end{tikzcd}}`, with every object, arrow, label and deletion. Inline correction strokes remain inline TikZ; do not wrap an inline transposition mark in the block-producing \figure macro. Free-standing drawings must be reproduced with `\figure{\begin{tikzpicture}...\end{tikzpicture}}`; no replacement by prose or an image. Use `% crop-candidate: scan N` only after a best TikZ approximation of a genuinely too-complex drawing.

Restrict doubt to the letters genuinely unresolved; do not keep a whole signature uncertain if the initials are clear.

Doubt goes at the place: `\unsure{reading}` or `\unsure{reading|alternative}` (all stroke-compatible candidates, ink-favoured first). For a recurring ambiguous sign, mark the first occurrence on each page and use that first candidate thereafter, with alternatives in notation/doubts. `\illegible{n}` is only physically unreadable words after highest zoom, never a mathematical symbol: use a candidate plus `\unsure` there. Do not leave gaps or silently guess.

Before returning, check that every inventory assertion is actually represented in reading.tex. In particular, encode hand-added accents and dots that complete typed punctuation, using standard LaTeX overlays where needed; distinguish genuinely blue marks from black typed punctuation. Count repeated letters by their separate printed cells, stems and bowls, not by expectation.

H uses `\struck` for deleted, `\marginal` for margin, `\uncertain` for its uncertainty, and `\ill` for illegible. Its `\note` is editorial commentary, not manuscript text. `marked_in_H` means an uncertainty flag such as \uncertain or \ill, not the mere presence of a marginal annotation or an editorial note. Editorial quotation italics and equivalent emphasis encodings alone are not substantive collation differences. Editorial section titles before the page are not ink. Macro syntax, line wrapping and semantically equivalent mathematical spacing alone do NOT create a difference row. Underlining/placement/deletion changes DO count when the underlying reading/state differs. Lack of a `\handwritten` wrapper alone is a reporting-convention difference, unless a hand correction, added sign or insertion has actually been lost or misplaced. Do not list H's prose inventory in an editorial note as extra manuscript text.

## Required files in YOUR output directory

1. `reading.tex`: the complete page, including all visible elements. You may start from C but must verify all of it visually; a copied uninspected passage is not a reading.
2. `report.json`: valid UTF-8 JSON with this structure (all fields explicit). If no start clock was captured, use a truthful “not captured” value and give the earliest actual recorded time; do not estimate or delay the reading to reconstruct timing:

```
{
  "scan": 3, "reader": "R1", "started_utc": "...", "finished_utc": "...",
  "views": ["whole", "half_a", "half_b", "crop filenames actually viewed"],
  "differences": [{"id":"R1-003-01", "place":"paragraph/line anchor", "c":"exact C reading", "h":"exact H reading or omission", "reading":"your final reading", "against_c":true, "against_h":true, "kind":"one allowed kind below", "marked_in_H":false, "confidence":"high", "evidence":"specific visible strokes and state; no merely contextual justification", "bbox":[0,0,100,100], "crop":"relative crop path or null", "math_note":"if applicable or empty"}],
  "c_doubts":[{"place":"...", "c":"...", "reading":"...", "resolved":false, "evidence":"...", "bbox":[...], "crop":null}],
  "s_rows":[{"where":"exact row identifier", "decision":"confirm/overturn/editorial only", "reading":"...", "evidence":"...", "bbox":[...], "crop":null}],
  "remaining_doubts":[{"place":"...", "reading":"...", "alternatives":["..."], "confidence":"medium", "reason":"..."}],
  "inventory":[{"sheet_kind":"letter", "hand":"typewriter / his hand / named or unnamed other hand / print", "element":"E01", "kind":"text", "position":"top", "first_words_or_objects":"...", "transcribed":"yes"}],
  "notation":[{"place":"...", "visible":"...", "latex":"...", "uncertainty":"..."}],
  "abbreviations":[{"form":"...", "expansion":"tentative expansion; only in this list"}],
  "notes":{"content":"brief English account with source places", "author_checks":["verbatim doubts/checks, or none"], "titles_dates_pages":["..."], "math_reading_decisions":["..."]},
  "check_events":[{"statement_id":"003-R1-M01", "date":"UTC", "who":"actual model/effort if known; otherwise not exposed; run id", "type":"actual type from list below", "outcome":"what was checked and its limits"}],
  "brief_feedback":["specific ambiguity or failure in this brief, if any"]
}
```

Allowed difference kinds: `misread word`, `misread symbol or index`, `omission`, `text not on the page`, `deletion state (struck given live or live given struck)`, `insertion or placement`, `abbreviation expanded or spelling modernised`, `readable ink left as \\ill{}`, `drawing or diagram`, `other`.

Allowed inventory kinds: text, display, diagram, drawing, margin note, insertion, deletion. Split actual insertions and deletions into their own inventory rows; include every block and display. Allowed sheet kinds: text, reused_typed, typescript, letter, list, cancelled_draft, cover.

Allowed check-event types: `targeted proof check`, `independent re-proof`, `computation or formal certificate`, `used and rechecked in this run`, `carried as background without fault found`, `refuted, with the refined statement's id`. Pure visual verification is not a mathematical proof check; describe an unproved mathematical claim carried into the notes as background, explicitly unverified. Empty check_events is legitimate if no mathematical statement is checked or used.

3. `report.md`: a human-readable account of your complete reading, discrepancies, retained doubts, inventory and notes; it may point to the full `reading.tex` and structured report. Include actual source-view and crop counts.

Finish by returning a concise message with the paths, number of differences, unresolved doubts, and any material point requiring main-reader adjudication. Do not send another reader your results, do not adjudicate other readers, do not continue to another page, and do not alter shared deliverables.

## Revision record

Version 002 follows scan 003: supplies the omitted PREAMBLE; clarifies H uncertainty flags, emphasis-only differences and inline TikZ; requires complete glyph bounds and inventory/reading agreement; specifies compact evidence JPEGs. These changes respond to actual independent-reader disagreements and main adjudication, recorded in scan 003 workflow.

Version 003 follows scan 004: excludes archival comments and line-layout-only changes from H counts; distinguishes an already encoded hand completion from a new physical insertion; focuses doubt on unresolved letterforms; and allows uncaptured start timing to be stated honestly. These issues arose in the three scan 004 returns.
