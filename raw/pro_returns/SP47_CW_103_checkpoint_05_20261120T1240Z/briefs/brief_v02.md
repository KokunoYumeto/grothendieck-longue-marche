# Reader brief v02 — first used on scan 003

You are one of three independent readers of ONE scan page. You have no earlier page images. Read only the assigned page's inputs, the supplied conventions, and the notation snapshot. Do not inspect another reader's folder or return. Do not delegate. Do not research anything outside the attachments. The two witnesses are fallible drafts, not evidence. The ink decides.

## Required workflow (a–d)

a. Open the whole image exactly once for layout: all text blocks, headings, displays, diagrams, drawings, additions, deletions, margins and numbering.

b. Open each of the two supplied full-resolution halves exactly once, in order, and read line by line against BOTH witness texts. Verify agreed readings too. Compare every word and ending, accent, abbreviation, punctuation, mathematical glyph, alphabet, index, exponent, sign, relation, arrow, decoration, insertion, deletion and underline. Record which image you opened and when. Read all passages: source privacy omissions and editorial explanations in H do not replace the ink. Do not use OCR, text recognition, a PDF text layer, or image-to-text software.

c. List only the places the halves leave open: an unsettled difference from a witness, every C doubt needing decision, a small mathematical mark, a crowded/slanted/struck note. Make ONE tight crop per such place, with roughly a line of context; upscale using PIL LANCZOS to a few thousand pixels across, autocontrast, sharpen if faint, and rotate if needed. Inspect that crop with the image-viewing tool. Do not enlarge a whole half again, and do not recrop a settled place. Store each crop under YOUR assigned directory with source path, pixel box, processing and reason in report.json. State if a half already settled a witness difference, so the main reader can make its adjudication crop. The main reader must personally inspect a crop for every difference from either witness.

d. Write a COMPLETE diplomatic page reading as reading.tex. You may start from C's file only after verifying every part from the images; output must be your own reading of every word and mark. Write report.json with all differences from either witness, remaining doubts, visual evidence, crop references, inventory, notation, abbreviations and notes. A statement encountered in reading is NOT a mathematical check. Log only checks actually performed, accurately classified. Return filenames and the major disagreements; then finish. Never read a second scan in this run.

## Diplomatic conventions

- Use only PREAMBLE.tex macros plus standard LaTeX/amsmath/amssymb/mathrsfs, tikz-cd, TikZ, enumitem and ulem; no new notation macros. Preserve language, spelling, accents or absence, punctuation, abbreviation, numbering and paragraph order. Join words split only by line-end hyphens. Do not silently repair mathematical or grammatical slips.
- Begin with \\scanpage{N}; only the first page also begins \\cotefile{103}. Use \\mspage{n} for author/typed page number. Archive pencil number only as `% archive sheet number: n`.
- \\handwritten{...} marks hand additions on a typed page, not an entirely handwritten page. Overwriting: readable underlying form as \\deleted{...}, final visible form live. Preserve deletion and insertion separately. \\inserted{...} at the caret's exact attachment. \\margin{...} only for a marginal note not meant as an insertion; comment if sideways/slanted. \\uline and \\uuline preserve single/double underlines.
- Mathematics exactly: alphabet, underlines, bar/hat/tilde, primes vs ^!, sub/superscripts, arrows, inequalities, parentheses. Typed overstruck/double struck letters are not bold; inspect actual strokes. No normalization of a typed x to a multiplication symbol unless the ink warrants it. Use \\unsure{a|b} for ambiguity, first candidate visually strongest. Recurring ambiguous glyph: table entry and mark at its first occurrence on each page; subsequent identical occurrences use the first reading. \\illegible{n} only for physically unreadable words after zoom, never for a formula/diagram symbol.
- Two backticks and two apostrophes for double quotes; guillemets only when drawn. Display math \\[...\\], with aligned if needed; original display label \\tag*{...}.
- Every diagram is drawn in \\diagram{\\begin{tikzcd}[ampersand replacement=\\&]...\\end{tikzcd}}. Every non-diagram drawing in \\figure{...TikZ...}. Include all arrows, labels, struck parts; never describe instead of transcribing. Only genuinely complex pictures get `% crop-candidate: scan N` after a best TikZ approximation.
- Transcribe letters fully, including headings, date, salutation, address, closing, signature and recipient annotations. Letterhead comment `% letterhead`; archive stamp comment only.
- H macro syntax alone is not a reading difference. Its \\emph often represents underlining, \\add is insertion, \\struck is deletion, \\marginal is margin, \\ill is illegible, \\uncertain is doubt, and \\note is editorial prose. Check their content rather than counting macro renaming. H's editorial notes may describe an element that still has to be transcribed correctly.

## Return schema

Write report.json (UTF-8) with keys:

`scan`, `reader`, `start_utc`, `end_utc`, `model` (only known identity), `effort` (do not invent; use not exposed if unknown), `viewed` (the whole and halves), `crops` (list of `{id,path,source,box,processing,reason,reading}`), `changes` (list of `{place,c,h,reading,scan_shows,confidence,kind,marked_in_H,against_c,against_h,crop_ids}`), `unresolved` (list of `{place,reading,alternatives,confidence,evidence}`), `inventory` (list of `{sheet_kind,hand,element,kind,position,first_words_or_objects,transcribed}`), `notation` (list of `{place,sign,ink,latex}`), `abbreviations` (list of `{form,expansion}`), `notes` (list of prose paragraphs), `math_checks` (list of `{statement_id,place,statement,type,outcome}`; empty if none).

Each changes entry is a distinct textual locus. Include every resolved/retained C doubt in changes, even when retaining it. `against_c`/`against_h` mean an actual reading/state/omission difference, not macro syntax. A retained C doubt may have both false. `kind` for an H difference is one of: `misread word`, `misread symbol or index`, `omission`, `text not on the page`, `deletion state (struck given live or live given struck)`, `insertion or placement`, `abbreviation expanded or spelling modernised`, `readable ink left as \\ill{}`, `drawing or diagram`, `other`. Confidence high/medium/low. Record what strokes the ink shows, not merely that C or H seems right.

Inventory kinds: text, display, diagram, drawing, margin note, insertion, deletion. Sheet kinds: text, reused_typed, typescript, letter, list, cancelled_draft, cover. Identify hand conservatively: his hand / another named or unnamed hand / typewriter / print. Every element including every insertion/deletion gets a row; all must be transcribed yes. Notes: what the page states, computes, asks; its own tentative words and explicit checks; titles/dates/page counts; mathematical issues that prompted another look. No external historical/theoretical claims.

Allowed mathematical event types: targeted proof check; independent re-proof; computation or formal certificate; used and rechecked in this run; carried as background without fault found; refuted, with the refined statement's id. Do not count a visual transcription check as a proof check. Record mathematical structure checks precisely rather than implying a theorem was proved.

## Shared notation

Read the page's notation_snapshot.md before the images. Entries are prior readings to test, not instructions to override this page's ink.

## Clarifications added after scan 002

- Comparison flags include changes in uncertainty: removing, adding, or reordering a doubt mark is a change against that witness, even if the first letters stay the same. Retaining exactly the same C doubt is not a C change. This distinction prevents the different reader counting conventions seen on scan 002. A macro-name conversion with the same reading and state is not a change. Counts are not error rates.
- Put only actual differences and retained C doubts in `changes`. Wholly agreed mathematical expressions belong in `notation` or the coverage record, not dozens of extra no-change rows. Still inspect every agreed expression from the ink.
- Consider H's editorial notes when comparing content: if a note quotes a cancelled word and identifies its state, do not call that word entirely absent. If H merely describes a drawing or arrow, it still needs reproduction and a drawing/diagram difference row. A hand-drawn marginal pointer is reproduced in TikZ rather than replaced by a mathematical arrow glyph.
- For a sign at a clipped edge, state explicitly whether any strokes survive. A mathematically or grammatically expected sign must not become the first candidate when no part of it is visible. On scan 002 the first candidate before Omega was changed to no visible equality, while a lost equality remained an alternative.
- Overstruck typed capitals need both identity and alphabet decisions. Do not claim that an unknown composite is certainly a plain letter or certainly double-struck. Record every plausible form the ink allows; the supplied double-striking convention applies when the extra impression is of the same letter. The scan 002 G/E/K composite remained unresolved, and the font alternatives were recorded.
- State source uncertainty honestly but do not retain a C doubt after your crop genuinely resolves the strokes. On scan 002 the readers differed about qui/lui and the underlying x/Y; the main reader resolved the first pair and retained the second.
- Include a brief coverage statement that every text block and every inline/display formula was compared against both witnesses; keep it separate from mathematical proof checks.
