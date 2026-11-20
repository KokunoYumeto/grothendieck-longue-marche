# Independent single-page reader brief, version 04

Read ONLY your assigned page. You are one of three independent fresh readers. Do not inspect any other reader's files, root decisions, or any other page's images. Do not spawn further agents. Your task is complete after returning this page.

Inputs: the supplied whole-page JPEG, its _a and _b halves, packet C.tex and H.tex, packet C_questions.md, briefs/conventions.md, PREAMBLE.tex, and the current notation table in briefs/notation.md. The current user prompt supersedes the older C prompt's procedural instructions. H page number = our scan minus one. C and H are unverified AI witnesses; neither agreement nor mathematical plausibility proves a reading. No OCR, text-recognition, web, external editions, or image-based automatic extraction.

## a. Layout
View the whole image once with the image viewer. Identify every text block, display, diagram, drawing, margin, insertion and deletion. Record dimensions so later crops use original-image coordinates.

## b. Read the halves
View each half once, line by line, comparing every word, accent, abbreviation, punctuation, glyph, index, exponent, arrow, underline and textual state with C and H. Do not reload/enlarge a whole half. Follow the mathematics to notice potential problems, but read the ink rather than repairing what it says. Preserve abbreviations and slips. Read all agreement loci too. H's \emph may stand for source underlining and its different macro syntax alone is not a reading difference. C's doubtful readings must each be reconsidered and reported, even when retained. Every deleted word remains transcribed, with doubt if covered.

## c. Targeted crops
List loci the halves leave unresolved: C doubts, contested wording, tiny mathematical signs, overwritten words and crowded or slanted notes. Crop each unresolved locus ONCE, tightly with a line of context, and view it. Use out/scripts/crop.py (Pillow LANCZOS, autocontrast, sharpening, optional rotation); target a few thousand pixels across. One crop per locus; never recrop a decided locus. If a witness difference is already settled by the halves, report its bounding box and half evidence; root will decide it on a crop. Give bounding boxes in whole-image coordinates, or explicitly name the half used. Do not silently extrapolate letters or normalize alphabets. For a recurring ambiguous glyph mark its first occurrence per page and record all candidates.

## d. Return and save
Write under your assigned out/readers/PAGE/Rn/ directory, nowhere else. Save:

1. reading.tex: COMPLETE diplomatic LaTeX page, in C's macros, starting with the scan marker. You may edit a copy of C after checking every part against ink. Retain C's paragraph structure where the ink supports it. Do not add a new notation macro. No explanatory prose replaces a drawing; use TikZ or tikz-cd with ampersand replacement=\&.
2. report.json: fields `page`, `reader`, `viewed` (whole/a/b paths), `reading_file`, `differences` (list), `c_doubts` (list), `inventory` (list), `remaining_doubts` (list), `notes` (list), `notation` (list), `abbreviations` (list), `math_checks` (list), `crop_count`, and `workflow_feedback`.

Each difference has `id`, `place`, `C`, `H`, `reading`, `evidence` (actual strokes or layout), `confidence` high/medium/low, `kind`, `marked_in_H`, `c_changed`, `h_changed`, `crop` (relative to out, or null), `bbox` and `bbox_source`. Include EVERY substantive disagreement against either witness, not only C edits. Distinguish typewritten plain letters, underlined sheaf letters, script and double-struck letters. Record an omission even when H mentions it only in an editorial note. Differences solely of macro syntax are excluded.

`kind` is one of: misread word; misread symbol or index; omission; text not on the page; deletion state (struck given live or live given struck); insertion or placement; abbreviation expanded or spelling modernised; readable ink left as \ill{}; drawing or diagram; other.

For `c_doubts`, give each C doubt's place, C reading, your decision, evidence, crop/bbox and confidence. For inventory give `sheet_kind`, `hand`, `element`, `kind` (text/display/diagram/drawing/margin note/insertion/deletion), `position`, `first_words_or_objects`, `transcribed` yes. Record each distinct element, including deletions and insertions; do not merely claim completeness.

Notes in English: what this page states, computes, asks or records; its explicit hesitations with quotations; dates/title/page counts; any mathematical issue that caused an ink recheck. Mathematical checks must accurately distinguish a targeted proof/computation actually performed from a statement merely read. Do not claim a theorem was verified because its wording was transcribed. Record unresolved doubts in place in reading.tex. Final response gives paths and concise findings, not the entire file.

No claim that strokes are clear unless you viewed them. If an image cannot be viewed, report the blockage rather than substituting witness text. Work carefully to completion with no clock-based shortcut.

## Refinements first used on page 2 (123/002)

- Preserve the actual staggered positions of words in margin notes, including words written above and to the right of a parenthesis. A grammatical phrase reconstructed from their meaning is not a substitute for placement. Use a TikZ layout when needed.
- A cancellation boundary may leave adjacent punctuation live. Inspect commas on both sides of a struck clause separately.
- Make a crop tight enough that one contested mark is readable at its displayed size: a whole long line resized to 3,000 pixels can still hide a small serif. Report whether a supposed overbar is detached from the letter or is the top serif; distinguish a detached superscript stroke from a pen terminal explicitly.
- Use specific difference loci rather than a single page-wide claim about alphabets. List formula groups separately, while ignoring mere changes of equivalent macro syntax.

## Refinements first used on page 3 (123/003)

- Save the complete reading.tex as soon as the image decisions are ready, before writing the longer report. Save report.json when complete. This permits comparison and protects already completed reading work during interruptions. If interrupted, resume this same page from retained context and saved evidence; report any lost context, and do not claim observations you no longer have.
- Inspect the baseline beneath a raised typed replacement. A covered or overtyped letter can survive beneath the new letter; retain a tentative reading if the underlying trace supports one. Do not assume the corrected word exhausts the ink.
- When setting c_changed and h_changed, quote the actual supplied C/H string. Check that a claimed missing state marker is truly absent. Equivalent macro syntax alone is not a substantive difference; a genuinely different alphabet, underline or insertion/deletion state is.
- Use the exact sheet_kind enum in the prompt: text, reused_typed, typescript, letter, list, cancelled_draft or cover. Use `C` (not C_reading) for the witness text in c_doubts. Give remaining_doubts fields place, reading, alternatives and confidence. Abbreviations need form and expansion, with the expansion explicitly editorial.
- Be concise in report prose while retaining every locus and inventory element. One precise description of visible strokes is more useful than repeated general cautions. Keep all three readings independent; saving early does not authorize consulting another reader.

## Refinements first used on page 4 (123/016)

- If a raised interlinear addition has no caret fixing its linear attachment, preserve its physical position above the nearby word in a small TikZ text layout. State the unresolved attachment in the doubts list. A comment saying that an arbitrarily linearized phrase was raised does not by itself preserve the ambiguous geometry.
- A handwriting wrapper alone, around the same glyph with no changed alphabet or state, is a macro-only difference and is excluded from the change/collation counts. Audit the medium in the inventory. Count a medium discrepancy when a witness explicitly calls a typed word handwritten or vice versa; do not infer a wrong medium solely from a missing wrapper in H’s different macro system.
