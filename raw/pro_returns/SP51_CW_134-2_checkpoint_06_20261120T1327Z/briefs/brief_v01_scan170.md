# Reader brief v01 — first used on scan 170

You are one of three independent fresh readers of ONE manuscript page. Read only the designated page packet, this brief, PREAMBLE.tex, the supplied current notation table, and that page’s three images. Do not open other reader returns, other page images/texts, external sources, or internet material. Never use OCR, text-recognition software or a PDF text layer. The scans are the sole authority; the two witnesses are drafts.

## Required visual sequence

1. Read metadata.json, C.tex, H.tex and C_questions.md in the designated packet. H’s editorial `\note{...}` is not manuscript text; use it to identify its claims, not to import editorial words. Read PREAMBLE.tex.
2. View the whole image exactly once for layout. Then view each full-resolution half exactly once, top then bottom. Use the image-viewing tool, actually emit and inspect its image. Read every line, word, accent, abbreviation, ending, formula, sign, index, arrowhead, deletion, insertion, underline and marginal mark. Agreement of C and H supplies no evidence: see agreed readings in the ink too.
3. Resolve everything the halves settle. List remaining open places: unresolved witness disagreements, every unresolved C doubt, consequential small mathematical signs, crowded/struck/slanted writing. Crop EACH open place ONCE tightly (word or formula plus a line of context), enlarge with Pillow LANCZOS to about 2500–3500 px width, autocontrast, sharpen if faint, rotate if slanted. Save each crop and its original whole-image bounding box. View it once. Do not recrop a decided place or enlarge an entire half. A crop may settle a contiguous phrase, but do not use an expansive crop to avoid identifying distinct places.
4. Return a COMPLETE diplomatic LaTeX page and a complete difference report against BOTH witnesses, with ink evidence. Your reading must be independent of the other two. Identify C doubts resolved or retained. Include a coverage inventory; look for what both witnesses omit. Follow the mathematics while reading; if a formula does not parse or a sign/index/arrow contradicts the argument, inspect the ink. Preserve the ink even if mathematically surprising. Report actual mathematical checks separately from merely reading assertions.

## Conventions

Use only macros in PREAMBLE.tex plus standard LaTeX/amsmath/amssymb/mathrsfs/tikz/tikz-cd/ulem/enumitem. Keep C’s page filename. `\cotefile{134-2}` occurs only at the first page of the combined work (scan 170). Every page starts `\scanpage{N}\mspage{n}` with its observed author number. Archive pencil numbers are only `% archive sheet number: N` comments.

No translation, modernization, grammatical repair or abbreviation expansion. Preserve visible spelling, accents, punctuation, alphabets, indices, exponents and brackets. Double quotation marks are two backticks and two apostrophes unless actual guillemets occur. Join line-end word breaks; preserve paragraphs and letter heading/closing/signature lines.

Use `\deleted{...}` for readable cancelled ink (or `\deleted{\illegible{n}}` for physically unreadable words). For overwriting, readable underlying form precedes live corrected form. Use `\inserted{...}` at the exact caret/line destination; `\margin{...}` only for independent margin notes, with a sideways/slanted comment where applicable. Use `\uline` and `\uuline` for single and double underline. All-handwritten pages need no `\handwritten` wrappers; record the hand in inventory. In prose, a manuscript abbreviation stays an abbreviation even where its expansion is obvious.

Diagrams must be fully drawn in `\diagram{\begin{tikzcd}[ampersand replacement=\&]...\end{tikzcd}}`, including objects, arrow directions/decorations, labels and struck portions. Drawings must be reproduced in TikZ inside `\figure{...}`. Do not substitute verbal descriptions. Small separator strokes also belong to the inventory.

Use `\unsure{reading}` or `\unsure{reading|alternative}` only when ink remains doubtful, first candidate the strongest visual reading. Retain all supported alternatives. A recurring ambiguous alphabet/sign is marked at its first occurrence on EACH page and recorded in notation; later same-page occurrences use its first candidate. `\illegible{n}` is only for physically unreadable WORDS after crop, never for a mathematical symbol. No doubt mark is permission to omit ink. Distinguish prime from exclamation, i from j, stars from dots, arrows from plain lines, and underlining from descenders.

## Files to write

Your assigned private directory is `result/records/scanNNN/R/`, where R is your designated A, B or C. Write `reading.tex`, `report.json`, and optional readable `report.md` there. Save crops under `result/crops/scanNNN/R/`; use descriptive filenames. Do not modify shared notation, consolidated pages or any other reader’s files.

`report.json` must contain:

- `scan`, `reader`, `complete` (true only after full visual reading), `viewed` (whole/a/b paths, each once), `reading_file`.
- `differences`: every reading/state/placement/punctuation difference from C or H, each with `place`, `C`, `H`, `final`, `differs_C`, `differs_H`, `evidence`, `confidence` (high/medium/low), `kind`, `marked_in_H`, `crop` (relative result path, or null if the half settles it), `bbox` (whole-image pixels, where useful). C’s doubt resolved or retained is explicitly recorded; syntax-only macro differences are not differences. H’s expanded abbreviations and omitted underlines/deletions are substantive.
- `unresolved`: place, reading, alternatives, confidence, reason; list every remaining `\unsure`/`\illegible`.
- `inventory`: one object per text block, display, diagram, drawing, margin note, insertion and deletion: `sheet_kind`, `hand`, `element`, `kind`, `position`, `first_words_or_objects`, `transcribed` (yes). Allowed sheet kinds: text, reused_typed, typescript, letter, list, cancelled_draft, cover. Allowed element kinds: text, display, diagram, drawing, margin note, insertion, deletion.
- `notation`: signs/alphabets/abbreviations to add or compare; include scan/place and visual grounds.
- `abbreviations`: written form and possible expansion (expansion is only in this list).
- `notes`: short English account of what this page states/computes/asks; its own explicit uncertainty with exact phrases; page/date/title evidence; math-triggered reading decisions. Do not claim to prove a statement merely by transcribing it.
- `check_events`: actual mathematical checks, with statement id, type, outcome and method. Allowed types: targeted proof check; independent re-proof; computation or formal certificate; used and rechecked in this run; carried as background without fault found; refuted, with the refined statement’s id. State if no proof was attempted.
- `crops`: path, bbox, rotation, scale/output size, and reason for each crop; `workflow_feedback`: what in this brief needs improvement.

Return a short message giving your report paths and the main disputed readings. Do not wait for the other readers. You are finished after this one page.
