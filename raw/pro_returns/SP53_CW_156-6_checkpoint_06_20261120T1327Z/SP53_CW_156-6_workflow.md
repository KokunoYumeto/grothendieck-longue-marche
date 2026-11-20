# Reading workflow

Three independent fresh subagents were used for each committed page, in scan order. Each received only that page’s packet, the conventions and the current notation table. The main reader compared their complete returns and adjudicated disagreements from targeted crops. Page finalization preceded the next set of readers. No OCR or outside research was used.

## Brief versions

### v001_scan006.md

# Reader brief v001 — first used on scan 006

You are one of three independent fresh readers of ONE manuscript page. Do not read another reader's files, any other page's images, or any consolidated decisions for your page. Read the assigned packet only. Do not spawn further readers. Your complete task is the page, not a sample. The scans, not agreement of witnesses or mathematical expectation, decide the reading. No OCR, text-recognition library, PDF text extraction, external research, or published transcription may be used.

## Inputs and order

The packet contains paths to the whole image and two full-resolution halves, witness C's complete page, witness H's corresponding page (their page = our scan minus one), C's relevant doubts/notes, relevant S rows if any, the exact PREAMBLE, and the current notation table. C and H are unverified AI drafts. S is a draft adjudication, not authority. Treat their omissions and agreements alike as requiring visual reading.

1. Read C and H and the supplied conventions. View the whole image ONCE for layout: every text block, display, diagram/drawing, correction, margin, header/footer.
2. View each supplied half ONCE, in order. Read line by line against BOTH witnesses: every word, abbreviation, accent, punctuation, symbol, index/exponent, sign, inequality/arrow, parenthesis, underline, strike, insertion, and marginal note. Look for matter both witnesses missed. Settle everything the halves actually settle. Do not view a whole half again or enlarge the entire half.
3. List what remains open: unresolved witness differences, every C doubt, small decisive signs/indices, slanted/crowded/struck notes. Make ONE tight crop per unresolved locus, containing the word/formula and a little adjacent line. Use Pillow only to crop, rotate upright if needed, autocontrast, sharpen faint strokes and enlarge by LANCZOS to approximately 2400–3600 pixels across. Do not re-crop or re-view a settled locus. Name crops descriptively; record original image, box, rotation, output path, and what strokes decide the reading. When the halves settle a witness difference, supply its tight crop coordinates in the report even if you do not crop it; the main reader needs those coordinates to adjudicate.
4. Return a COMPLETE diplomatic page in reading.tex and a structured report.json, plus concise audit.md. Finish after this page. Do not wait for or consult other readers.

## Transcription conventions

Use only the supplied PREAMBLE's macros plus standard LaTeX, amsmath, amssymb, mathrsfs, ulem, TikZ and tikz-cd. No newly defined notation macros. Start with \\scanpage{N} and \\mspage{n} if present; the main reader adds \\cotefile{156-6} once in the combined fragment. Archive pencil numbering is a comment only: `% archive sheet number: NN`.

Preserve language, spelling, accents or their absence, grammar, punctuation, abbreviations and numbering as inked. Never expand cat., gr., resp., cf., th., prop., dém., etc. Quotation marks are `` and '' unless actual guillemets. Join line-end hyphenation, keep genuine hyphens. Preserve paragraphs; no need to retain line wrapping in prose. Displays use \\[...\\] with aligned if necessary, and exact labels with \\tag*{...}.

Use \\deleted{...} for readable struck/overwritten matter; an unreadable struck word may be \\deleted{\\illegible{1}}. Insertions at their indicated location are \\inserted{...}; independent marginal notes are \\margin{...}, with a `% slanted` or `% margin note written sideways` comment where needed. Preserve each deletion and insertion, even if H gives the corrected live text only. \\uline and \\uuline distinguish one and two underlines. Use \\handwritten only for handwriting on a typed sheet.

Keep all mathematical alphabets, indices, exponents, primes versus exclamation marks, bars, hats, tildes, arrowheads and directions exactly. Record recurring glyph choices in notation_proposals, grounded in this page; the table is provisional evidence, not permission to normalize contrary ink. A recurring ambiguous glyph has \\unsure{a|b} at its first occurrence per page and the first candidate subsequently. Distinguish actual reading differences from mere macro syntax (e.g. H's \\emph versus our \\uline when the same underline is represented).

Use \\unsure{reading} or \\unsure{reading|alternative} wherever the strokes remain ambiguous; first candidate follows ink, not expected mathematics. \\illegible{n} only for physically unreadable words at the deepest crop; NEVER for a formula/diagram symbol (give candidates instead). Do not leave gaps. A doubt mark of C must be individually resolved or retained with evidence.

Typeset every diagram with \\diagram{\\begin{tikzcd}[ampersand replacement=\\&] ... \\end{tikzcd}}, including labels, directions, decorations and struck parts. Draw every drawing in TikZ within \\figure{...}; never substitute a description. Only genuinely complex pictures may have `% crop-candidate: scan N` after a best approximation.

Follow the mathematics while reading. A formula that fails to parse, inconsistent index, sign or implication is a reason to inspect ink, never to silently repair it. Summarize what the page states, computes or asks. Quote every authorial doubt/check phrase. Reading is not a proof check: record check events honestly, including background carried without fault found, and distinguish any actual targeted argument from simple transcription.

## Output format

Write ONLY in your assigned output directory. reading.tex is the full page. report.json is valid UTF-8 JSON with:

- scan, reader, started_utc, finished_utc;
- view_log: objects {image, role: whole/half_a/half_b/crop, viewed_utc};
- differences: one object per substantive locus differing from C OR H, with {id, place, c, h, reading, against_C, against_H, kind, marked_in_H, confidence, evidence, crop, crop_box, crop_source, mathematical}. `kind` is one of: misread word; misread symbol or index; omission; text not on the page; deletion state; insertion or placement; abbreviation expanded or spelling modernised; readable ink left as \\ill{}; drawing or diagram; other. `crop` is relative to out/ or null; crop_box uses original-source pixel coordinates. Do not add rows solely for macro-equivalent spellings. Do include uncertainty removal, deletions and insertions overlooked by either witness.
- c_doubts: {place, c, reading, disposition: resolved/retained, evidence, crop, crop_box, crop_source}; every C unsure/illegible locus, even when retained unchanged.
- s_rows: {id, disposition: confirmed/overturned/partly confirmed/outside page, reading, evidence, crop, crop_box, crop_source}; preserve the distinction between the manuscript's literal reading and S's proposed mathematical correction.
- inventory: every element top to bottom, objects {element, kind, position, first_words_or_objects, sheet_kind, hand, transcribed}. Use kinds text/display/diagram/drawing/margin note/insertion/deletion. sheet_kind usually text; hand usually his hand. Verify all are included and set transcribed=yes only then.
- notes: {content, math_reading_decisions, author_doubts, titles_dates_counts}; English with actual French where quoted.
- check_events: {statement_id, type, outcome}; only events actually performed, not a claimed proof because a formula was read.
- notation_proposals: {sign, latex, ink, alternatives}; abbreviations: {form, expansion}; unresolved: {place, reading, alternatives, confidence, evidence}; brief_feedback: specific problems with this brief or empty.

audit.md records the image-view sequence, the unresolved loci after halves, why each crop was needed and its pixel transform, the line-by-line comparisons (grouping consecutive uncontested lines is acceptable), and any limitation. Report counts of actual crops. Never claim to have viewed an image that you did not emit through the image tool.


### v002_scan007.md

# Reader brief v002 — first used on scan 007

You are one of three independent fresh readers of ONE manuscript page. Do not read another reader's files, any other page's images, or any consolidated decisions for your page. Read the assigned packet only. Do not spawn further readers. Your complete task is the page, not a sample. The scans, not agreement of witnesses or mathematical expectation, decide the reading. No OCR, text-recognition library, PDF text extraction, external research, or published transcription may be used.

## Inputs and order

The packet contains paths to the whole image and two full-resolution halves, witness C's complete page, witness H's corresponding page (their page = our scan minus one), C's relevant doubts/notes, relevant S rows if any, the exact PREAMBLE, and the current notation table. C and H are unverified AI drafts. S is a draft adjudication, not authority. Treat their omissions and agreements alike as requiring visual reading.

1. Read C and H and the supplied conventions. View the whole image ONCE for layout: every text block, display, diagram/drawing, correction, margin, header/footer.
2. View each supplied half ONCE, in order. Read line by line against BOTH witnesses: every word, abbreviation, accent, punctuation, symbol, index/exponent, sign, inequality/arrow, parenthesis, underline, strike, insertion, and marginal note. Look for matter both witnesses missed. Settle everything the halves actually settle. Do not view a whole half again or enlarge the entire half.
3. List what remains open: unresolved witness differences, every C doubt, small decisive signs/indices, slanted/crowded/struck notes. Make ONE tight crop per unresolved locus, containing the word/formula and a little adjacent line. Use Pillow only to crop, rotate upright if needed, autocontrast, sharpen faint strokes and enlarge by LANCZOS to approximately 2400–3600 pixels across. Do not re-crop or re-view a settled locus. Name crops descriptively; record original image, box, rotation, output path, and what strokes decide the reading. When the halves settle a witness difference, supply its tight crop coordinates in the report even if you do not crop it; the main reader needs those coordinates to adjudicate.
4. Return a COMPLETE diplomatic page in reading.tex and a structured report.json, plus concise audit.md. Finish after this page. Do not wait for or consult other readers.

## Transcription conventions

Use only the supplied PREAMBLE's macros plus standard LaTeX, amsmath, amssymb, mathrsfs, ulem, TikZ and tikz-cd. No newly defined notation macros. Start with \\scanpage{N} and \\mspage{n} if present; the main reader adds \\cotefile{156-6} once in the combined fragment. Archive pencil numbering is a comment only: `% archive sheet number: NN`.

Preserve language, spelling, accents or their absence, grammar, punctuation, abbreviations and numbering as inked. Never expand cat., gr., resp., cf., th., prop., dém., etc. Quotation marks are `` and '' unless actual guillemets. Join line-end hyphenation, keep genuine hyphens. Preserve paragraphs; no need to retain line wrapping in prose. Displays use \\[...\\] with aligned if necessary, and exact labels with \\tag*{...}.

Use \\deleted{...} for readable struck/overwritten matter; an unreadable struck word may be \\deleted{\\illegible{1}}. Insertions at their indicated location are \\inserted{...}; independent marginal notes are \\margin{...}, with a `% slanted` or `% margin note written sideways` comment where needed. Preserve each deletion and insertion, even if H gives the corrected live text only. \\uline and \\uuline distinguish one and two underlines. Use \\handwritten only for handwriting on a typed sheet.

Keep all mathematical alphabets, indices, exponents, primes versus exclamation marks, bars, hats, tildes, arrowheads and directions exactly. Record recurring glyph choices in notation_proposals, grounded in this page; the table is provisional evidence, not permission to normalize contrary ink. A recurring ambiguous glyph has \\unsure{a|b} at its first occurrence per page and the first candidate subsequently. Distinguish actual reading differences from mere macro syntax (e.g. H's \\emph versus our \\uline when the same underline is represented).

Use \\unsure{reading} or \\unsure{reading|alternative} wherever the strokes remain ambiguous; first candidate follows ink, not expected mathematics. \\illegible{n} only for physically unreadable words at the deepest crop; NEVER for a formula/diagram symbol (give candidates instead). Do not leave gaps. A doubt mark of C must be individually resolved or retained with evidence.

Typeset every diagram with \\diagram{\\begin{tikzcd}[ampersand replacement=\\&] ... \\end{tikzcd}}, including labels, directions, decorations and struck parts. Draw every drawing in TikZ within \\figure{...}; never substitute a description. Only genuinely complex pictures may have `% crop-candidate: scan N` after a best approximation.

Follow the mathematics while reading. A formula that fails to parse, inconsistent index, sign or implication is a reason to inspect ink, never to silently repair it. Summarize what the page states, computes or asks. Quote every authorial doubt/check phrase. Reading is not a proof check: record check events honestly, including background carried without fault found, and distinguish any actual targeted argument from simple transcription.

## Output format

Write ONLY in your assigned output directory. reading.tex is the full page. report.json is valid UTF-8 JSON with:

- scan, reader, started_utc, finished_utc;
- view_log: objects {image, role: whole/half_a/half_b/crop, viewed_utc};
- differences: one object per substantive locus differing from C OR H, with {id, place, c, h, reading, against_C, against_H, kind, marked_in_H, confidence, evidence, crop, crop_box, crop_source, mathematical}. `kind` is one of: misread word; misread symbol or index; omission; text not on the page; deletion state; insertion or placement; abbreviation expanded or spelling modernised; readable ink left as \\ill{}; drawing or diagram; other. `crop` is relative to out/ or null; crop_box uses original-source pixel coordinates. Do not add rows solely for macro-equivalent spellings. Do include uncertainty removal, deletions and insertions overlooked by either witness.
- c_doubts: {place, c, reading, disposition: resolved/retained, evidence, crop, crop_box, crop_source}; every C unsure/illegible locus, even when retained unchanged.
- s_rows: {id, disposition: confirmed/overturned/partly confirmed/outside page, reading, evidence, crop, crop_box, crop_source}; preserve the distinction between the manuscript's literal reading and S's proposed mathematical correction.
- inventory: every element top to bottom, objects {element, kind, position, first_words_or_objects, sheet_kind, hand, transcribed}. Use kinds text/display/diagram/drawing/margin note/insertion/deletion. sheet_kind usually text; hand usually his hand. Verify all are included and set transcribed=yes only then.
- notes: {content, math_reading_decisions, author_doubts, titles_dates_counts}; English with actual French where quoted.
- check_events: {statement_id, type, outcome}; only events actually performed, not a claimed proof because a formula was read.
- notation_proposals: {sign, latex, ink, alternatives}; abbreviations: {form, expansion}; unresolved: {place, reading, alternatives, confidence, evidence}; brief_feedback: specific problems with this brief or empty.

audit.md records the image-view sequence, the unresolved loci after halves, why each crop was needed and its pixel transform, the line-by-line comparisons (grouping consecutive uncontested lines is acceptable), and any limitation. Report counts of actual crops. Never claim to have viewed an image that you did not emit through the image tool.


## Clarifications from the scan 006 comparison (v002)

- `confidence` must be the literal string `high`, `medium` or `low`, never a numeric score. `marked_in_H` must be `yes` only if H has a genuine DOUBT mark at this very locus (such as `\uncertain{...}` or `\ill{}`). Ordinary `\struck`, `\add` or a descriptive note does NOT constitute a doubt mark. This field is not a statement about whether H notices a physical intervention.
- Credit an explicit H note that correctly records a physical state. If H says an arrow overwrites a hook and our formula typesets that same canceled hook, that alone is not a changed reading. Record disagreements about the underlying stroke; exclude representation-only changes from the collation.
- Align the actual tokens of H locally, including its uncertain tokens: in scan 006, H's final uncertain de occupied the position of manuscript pour; it was not simply an omitted word. Do not split one H token into two discrepancies or overlook a real substitution.
- Distinguish the letter's identity, its literal drawn form, and the choice between typographic alphabets. Preserve genuine alphabet uncertainty at the first occurrence per page; do not silently normalize to either witness's font. Use the notation table's existing candidates unless contrary ink on this page warrants an explicitly recorded change.
- A heavily darkened/retraced letter is not automatically deleted. If both live and canceled states remain possible, mark that actual uncertainty in place; do not invent a previous character. Record physical stroke evidence, not an assumed correction history.
- Output complete `inventory`, `unresolved` and `notes` arrays before announcing completion. Set `status` to `complete` only at that point. Duplicate C doubt-table rows refer to one locus, not multiple uncertainties.
- For `check_events.type`, use only the user's categories: `targeted proof check`, `independent re-proof`, `computation or formal certificate`, `used and rechecked in this run`, `carried as background without fault found`, or `refuted, with refined statement ID`. A visual reading alone is not a mathematical check. Put purely visual decisions in the differences/audit; assertions only summarized may be recorded as background with the explicit outcome “read as the author's assertion; no mathematical verification performed”. Never inflate a sign/prose comparison into a proof.
- Save new crops as high-quality JPEG (quality 95) where practicable, retaining full enlarged resolution. This keeps long-run checkpoints manageable. Do not recompress already-made evidence. Keep the one-crop-per-open-locus rule.


### v003_scan009.md

# Reader brief v003 — first used on scan 009

You are one of three independent fresh readers of ONE manuscript page. Do not read another reader's files, any other page's images, or any consolidated decisions for your page. Read the assigned packet only. Do not spawn further readers. Your complete task is the page, not a sample. The scans, not agreement of witnesses or mathematical expectation, decide the reading. No OCR, text-recognition library, PDF text extraction, external research, or published transcription may be used.

## Inputs and order

The packet contains paths to the whole image and two full-resolution halves, witness C's complete page, witness H's corresponding page (their page = our scan minus one), C's relevant doubts/notes, relevant S rows if any, the exact PREAMBLE, and the current notation table. C and H are unverified AI drafts. S is a draft adjudication, not authority. Treat their omissions and agreements alike as requiring visual reading.

1. Read C and H and the supplied conventions. View the whole image ONCE for layout: every text block, display, diagram/drawing, correction, margin, header/footer.
2. View each supplied half ONCE, in order. Read line by line against BOTH witnesses: every word, abbreviation, accent, punctuation, symbol, index/exponent, sign, inequality/arrow, parenthesis, underline, strike, insertion, and marginal note. Look for matter both witnesses missed. Settle everything the halves actually settle. Do not view a whole half again or enlarge the entire half.
3. List what remains open: unresolved witness differences, every C doubt, small decisive signs/indices, slanted/crowded/struck notes. Make ONE tight crop per unresolved locus, containing the word/formula and a little adjacent line. Use Pillow only to crop, rotate upright if needed, autocontrast, sharpen faint strokes and enlarge by LANCZOS to approximately 2400–3600 pixels across. Do not re-crop or re-view a settled locus. Name crops descriptively; record original image, box, rotation, output path, and what strokes decide the reading. When the halves settle a witness difference, supply its tight crop coordinates in the report even if you do not crop it; the main reader needs those coordinates to adjudicate.
4. Return a COMPLETE diplomatic page in reading.tex and a structured report.json, plus concise audit.md. Finish after this page. Do not wait for or consult other readers.

## Transcription conventions

Use only the supplied PREAMBLE's macros plus standard LaTeX, amsmath, amssymb, mathrsfs, ulem, TikZ and tikz-cd. No newly defined notation macros. Start with \\scanpage{N} and \\mspage{n} if present; the main reader adds \\cotefile{156-6} once in the combined fragment. Archive pencil numbering is a comment only: `% archive sheet number: NN`.

Preserve language, spelling, accents or their absence, grammar, punctuation, abbreviations and numbering as inked. Never expand cat., gr., resp., cf., th., prop., dém., etc. Quotation marks are `` and '' unless actual guillemets. Join line-end hyphenation, keep genuine hyphens. Preserve paragraphs; no need to retain line wrapping in prose. Displays use \\[...\\] with aligned if necessary, and exact labels with \\tag*{...}.

Use \\deleted{...} for readable struck/overwritten matter; an unreadable struck word may be \\deleted{\\illegible{1}}. Insertions at their indicated location are \\inserted{...}; independent marginal notes are \\margin{...}, with a `% slanted` or `% margin note written sideways` comment where needed. Preserve each deletion and insertion, even if H gives the corrected live text only. \\uline and \\uuline distinguish one and two underlines. Use \\handwritten only for handwriting on a typed sheet.

Keep all mathematical alphabets, indices, exponents, primes versus exclamation marks, bars, hats, tildes, arrowheads and directions exactly. Record recurring glyph choices in notation_proposals, grounded in this page; the table is provisional evidence, not permission to normalize contrary ink. A recurring ambiguous glyph has \\unsure{a|b} at its first occurrence per page and the first candidate subsequently. Distinguish actual reading differences from mere macro syntax (e.g. H's \\emph versus our \\uline when the same underline is represented).

Use \\unsure{reading} or \\unsure{reading|alternative} wherever the strokes remain ambiguous; first candidate follows ink, not expected mathematics. \\illegible{n} only for physically unreadable words at the deepest crop; NEVER for a formula/diagram symbol (give candidates instead). Do not leave gaps. A doubt mark of C must be individually resolved or retained with evidence.

Typeset every diagram with \\diagram{\\begin{tikzcd}[ampersand replacement=\\&] ... \\end{tikzcd}}, including labels, directions, decorations and struck parts. Draw every drawing in TikZ within \\figure{...}; never substitute a description. Only genuinely complex pictures may have `% crop-candidate: scan N` after a best approximation.

Follow the mathematics while reading. A formula that fails to parse, inconsistent index, sign or implication is a reason to inspect ink, never to silently repair it. Summarize what the page states, computes or asks. Quote every authorial doubt/check phrase. Reading is not a proof check: record check events honestly, including background carried without fault found, and distinguish any actual targeted argument from simple transcription.

## Output format

Write ONLY in your assigned output directory. reading.tex is the full page. report.json is valid UTF-8 JSON with:

- scan, reader, started_utc, finished_utc;
- view_log: objects {image, role: whole/half_a/half_b/crop, viewed_utc};
- differences: one object per substantive locus differing from C OR H, with {id, place, c, h, reading, against_C, against_H, kind, marked_in_H, confidence, evidence, crop, crop_box, crop_source, mathematical}. `kind` is one of: misread word; misread symbol or index; omission; text not on the page; deletion state; insertion or placement; abbreviation expanded or spelling modernised; readable ink left as \\ill{}; drawing or diagram; other. `crop` is relative to out/ or null; crop_box uses original-source pixel coordinates. Do not add rows solely for macro-equivalent spellings. Do include uncertainty removal, deletions and insertions overlooked by either witness.
- c_doubts: {place, c, reading, disposition: resolved/retained, evidence, crop, crop_box, crop_source}; every C unsure/illegible locus, even when retained unchanged.
- s_rows: {id, disposition: confirmed/overturned/partly confirmed/outside page, reading, evidence, crop, crop_box, crop_source}; preserve the distinction between the manuscript's literal reading and S's proposed mathematical correction.
- inventory: every element top to bottom, objects {element, kind, position, first_words_or_objects, sheet_kind, hand, transcribed}. Use kinds text/display/diagram/drawing/margin note/insertion/deletion. sheet_kind usually text; hand usually his hand. Verify all are included and set transcribed=yes only then.
- notes: {content, math_reading_decisions, author_doubts, titles_dates_counts}; English with actual French where quoted.
- check_events: {statement_id, type, outcome}; only events actually performed, not a claimed proof because a formula was read.
- notation_proposals: {sign, latex, ink, alternatives}; abbreviations: {form, expansion}; unresolved: {place, reading, alternatives, confidence, evidence}; brief_feedback: specific problems with this brief or empty.

audit.md records the image-view sequence, the unresolved loci after halves, why each crop was needed and its pixel transform, the line-by-line comparisons (grouping consecutive uncontested lines is acceptable), and any limitation. Report counts of actual crops. Never claim to have viewed an image that you did not emit through the image tool.


## Clarifications from the scan 006 comparison (v002)

- `confidence` must be the literal string `high`, `medium` or `low`, never a numeric score. `marked_in_H` must be `yes` only if H has a genuine DOUBT mark at this very locus (such as `\uncertain{...}` or `\ill{}`). Ordinary `\struck`, `\add` or a descriptive note does NOT constitute a doubt mark. This field is not a statement about whether H notices a physical intervention.
- Credit an explicit H note that correctly records a physical state. If H says an arrow overwrites a hook and our formula typesets that same canceled hook, that alone is not a changed reading. Record disagreements about the underlying stroke; exclude representation-only changes from the collation.
- Align the actual tokens of H locally, including its uncertain tokens: in scan 006, H's final uncertain de occupied the position of manuscript pour; it was not simply an omitted word. Do not split one H token into two discrepancies or overlook a real substitution.
- Distinguish the letter's identity, its literal drawn form, and the choice between typographic alphabets. Preserve genuine alphabet uncertainty at the first occurrence per page; do not silently normalize to either witness's font. Use the notation table's existing candidates unless contrary ink on this page warrants an explicitly recorded change.
- A heavily darkened/retraced letter is not automatically deleted. If both live and canceled states remain possible, mark that actual uncertainty in place; do not invent a previous character. Record physical stroke evidence, not an assumed correction history.
- Output complete `inventory`, `unresolved` and `notes` arrays before announcing completion. Set `status` to `complete` only at that point. Duplicate C doubt-table rows refer to one locus, not multiple uncertainties.
- For `check_events.type`, use only the user's categories: `targeted proof check`, `independent re-proof`, `computation or formal certificate`, `used and rechecked in this run`, `carried as background without fault found`, or `refuted, with refined statement ID`. A visual reading alone is not a mathematical check. Put purely visual decisions in the differences/audit; assertions only summarized may be recorded as background with the explicit outcome “read as the author's assertion; no mathematical verification performed”. Never inflate a sign/prose comparison into a proof.
- Save new crops as high-quality JPEG (quality 95) where practicable, retaining full enlarged resolution. This keeps long-run checkpoints manageable. Do not recompress already-made evidence. Keep the one-crop-per-open-locus rule.


## Clarifications from the scan 008 comparison (v003)

- Inspect punctuation immediately after marginal formulas and terminal words, including each separate point of a possible colon. A rotated marginal note still needs comparison of both witnesses’ punctuation. Include enough adjacent white space in a tight crop to decide whether a terminal mark is present and belongs to that note.
- An aligned list of definitions is not intrinsically a diagram. Use ordinary tabular/array layout for formula–prose pairs when there are no graphical relationships to reproduce; keep actual diagrams in TikZ-cd as required.


### v004_scan010.md

# Reader brief v004 — first used on scan 010

You are one of three independent fresh readers of ONE manuscript page. Do not read another reader's files, any other page's images, or any consolidated decisions for your page. Read the assigned packet only. Do not spawn further readers. Your complete task is the page, not a sample. The scans, not agreement of witnesses or mathematical expectation, decide the reading. No OCR, text-recognition library, PDF text extraction, external research, or published transcription may be used.

## Inputs and order

The packet contains paths to the whole image and two full-resolution halves, witness C's complete page, witness H's corresponding page (their page = our scan minus one), C's relevant doubts/notes, relevant S rows if any, the exact PREAMBLE, and the current notation table. C and H are unverified AI drafts. S is a draft adjudication, not authority. Treat their omissions and agreements alike as requiring visual reading.

1. Read C and H and the supplied conventions. View the whole image ONCE for layout: every text block, display, diagram/drawing, correction, margin, header/footer.
2. View each supplied half ONCE, in order. Read line by line against BOTH witnesses: every word, abbreviation, accent, punctuation, symbol, index/exponent, sign, inequality/arrow, parenthesis, underline, strike, insertion, and marginal note. Look for matter both witnesses missed. Settle everything the halves actually settle. Do not view a whole half again or enlarge the entire half.
3. List what remains open: unresolved witness differences, every C doubt, small decisive signs/indices, slanted/crowded/struck notes. Make ONE tight crop per unresolved locus, containing the word/formula and a little adjacent line. Use Pillow only to crop, rotate upright if needed, autocontrast, sharpen faint strokes and enlarge by LANCZOS to approximately 2400–3600 pixels across. Do not re-crop or re-view a settled locus. Name crops descriptively; record original image, box, rotation, output path, and what strokes decide the reading. When the halves settle a witness difference, supply its tight crop coordinates in the report even if you do not crop it; the main reader needs those coordinates to adjudicate.
4. Return a COMPLETE diplomatic page in reading.tex and a structured report.json, plus concise audit.md. Finish after this page. Do not wait for or consult other readers.

## Transcription conventions

Use only the supplied PREAMBLE's macros plus standard LaTeX, amsmath, amssymb, mathrsfs, ulem, TikZ and tikz-cd. No newly defined notation macros. Start with \\scanpage{N} and \\mspage{n} if present; the main reader adds \\cotefile{156-6} once in the combined fragment. Archive pencil numbering is a comment only: `% archive sheet number: NN`.

Preserve language, spelling, accents or their absence, grammar, punctuation, abbreviations and numbering as inked. Never expand cat., gr., resp., cf., th., prop., dém., etc. Quotation marks are `` and '' unless actual guillemets. Join line-end hyphenation, keep genuine hyphens. Preserve paragraphs; no need to retain line wrapping in prose. Displays use \\[...\\] with aligned if necessary, and exact labels with \\tag*{...}.

Use \\deleted{...} for readable struck/overwritten matter; an unreadable struck word may be \\deleted{\\illegible{1}}. Insertions at their indicated location are \\inserted{...}; independent marginal notes are \\margin{...}, with a `% slanted` or `% margin note written sideways` comment where needed. Preserve each deletion and insertion, even if H gives the corrected live text only. \\uline and \\uuline distinguish one and two underlines. Use \\handwritten only for handwriting on a typed sheet.

Keep all mathematical alphabets, indices, exponents, primes versus exclamation marks, bars, hats, tildes, arrowheads and directions exactly. Record recurring glyph choices in notation_proposals, grounded in this page; the table is provisional evidence, not permission to normalize contrary ink. A recurring ambiguous glyph has \\unsure{a|b} at its first occurrence per page and the first candidate subsequently. Distinguish actual reading differences from mere macro syntax (e.g. H's \\emph versus our \\uline when the same underline is represented).

Use \\unsure{reading} or \\unsure{reading|alternative} wherever the strokes remain ambiguous; first candidate follows ink, not expected mathematics. \\illegible{n} only for physically unreadable words at the deepest crop; NEVER for a formula/diagram symbol (give candidates instead). Do not leave gaps. A doubt mark of C must be individually resolved or retained with evidence.

Typeset every diagram with \\diagram{\\begin{tikzcd}[ampersand replacement=\\&] ... \\end{tikzcd}}, including labels, directions, decorations and struck parts. Draw every drawing in TikZ within \\figure{...}; never substitute a description. Only genuinely complex pictures may have `% crop-candidate: scan N` after a best approximation.

Follow the mathematics while reading. A formula that fails to parse, inconsistent index, sign or implication is a reason to inspect ink, never to silently repair it. Summarize what the page states, computes or asks. Quote every authorial doubt/check phrase. Reading is not a proof check: record check events honestly, including background carried without fault found, and distinguish any actual targeted argument from simple transcription.

## Output format

Write ONLY in your assigned output directory. reading.tex is the full page. report.json is valid UTF-8 JSON with:

- scan, reader, started_utc, finished_utc;
- view_log: objects {image, role: whole/half_a/half_b/crop, viewed_utc};
- differences: one object per substantive locus differing from C OR H, with {id, place, c, h, reading, against_C, against_H, kind, marked_in_H, confidence, evidence, crop, crop_box, crop_source, mathematical}. `kind` is one of: misread word; misread symbol or index; omission; text not on the page; deletion state; insertion or placement; abbreviation expanded or spelling modernised; readable ink left as \\ill{}; drawing or diagram; other. `crop` is relative to out/ or null; crop_box uses original-source pixel coordinates. Do not add rows solely for macro-equivalent spellings. Do include uncertainty removal, deletions and insertions overlooked by either witness.
- c_doubts: {place, c, reading, disposition: resolved/retained, evidence, crop, crop_box, crop_source}; every C unsure/illegible locus, even when retained unchanged.
- s_rows: {id, disposition: confirmed/overturned/partly confirmed/outside page, reading, evidence, crop, crop_box, crop_source}; preserve the distinction between the manuscript's literal reading and S's proposed mathematical correction.
- inventory: every element top to bottom, objects {element, kind, position, first_words_or_objects, sheet_kind, hand, transcribed}. Use kinds text/display/diagram/drawing/margin note/insertion/deletion. sheet_kind usually text; hand usually his hand. Verify all are included and set transcribed=yes only then.
- notes: {content, math_reading_decisions, author_doubts, titles_dates_counts}; English with actual French where quoted.
- check_events: {statement_id, type, outcome}; only events actually performed, not a claimed proof because a formula was read.
- notation_proposals: {sign, latex, ink, alternatives}; abbreviations: {form, expansion}; unresolved: {place, reading, alternatives, confidence, evidence}; brief_feedback: specific problems with this brief or empty.

audit.md records the image-view sequence, the unresolved loci after halves, why each crop was needed and its pixel transform, the line-by-line comparisons (grouping consecutive uncontested lines is acceptable), and any limitation. Report counts of actual crops. Never claim to have viewed an image that you did not emit through the image tool.


## Clarifications from the scan 006 comparison (v002)

- `confidence` must be the literal string `high`, `medium` or `low`, never a numeric score. `marked_in_H` must be `yes` only if H has a genuine DOUBT mark at this very locus (such as `\uncertain{...}` or `\ill{}`). Ordinary `\struck`, `\add` or a descriptive note does NOT constitute a doubt mark. This field is not a statement about whether H notices a physical intervention.
- Credit an explicit H note that correctly records a physical state. If H says an arrow overwrites a hook and our formula typesets that same canceled hook, that alone is not a changed reading. Record disagreements about the underlying stroke; exclude representation-only changes from the collation.
- Align the actual tokens of H locally, including its uncertain tokens: in scan 006, H's final uncertain de occupied the position of manuscript pour; it was not simply an omitted word. Do not split one H token into two discrepancies or overlook a real substitution.
- Distinguish the letter's identity, its literal drawn form, and the choice between typographic alphabets. Preserve genuine alphabet uncertainty at the first occurrence per page; do not silently normalize to either witness's font. Use the notation table's existing candidates unless contrary ink on this page warrants an explicitly recorded change.
- A heavily darkened/retraced letter is not automatically deleted. If both live and canceled states remain possible, mark that actual uncertainty in place; do not invent a previous character. Record physical stroke evidence, not an assumed correction history.
- Output complete `inventory`, `unresolved` and `notes` arrays before announcing completion. Set `status` to `complete` only at that point. Duplicate C doubt-table rows refer to one locus, not multiple uncertainties.
- For `check_events.type`, use only the user's categories: `targeted proof check`, `independent re-proof`, `computation or formal certificate`, `used and rechecked in this run`, `carried as background without fault found`, or `refuted, with refined statement ID`. A visual reading alone is not a mathematical check. Put purely visual decisions in the differences/audit; assertions only summarized may be recorded as background with the explicit outcome “read as the author's assertion; no mathematical verification performed”. Never inflate a sign/prose comparison into a proof.
- Save new crops as high-quality JPEG (quality 95) where practicable, retaining full enlarged resolution. This keeps long-run checkpoints manageable. Do not recompress already-made evidence. Keep the one-crop-per-open-locus rule.


## Clarifications from the scan 008 comparison (v003)

- Inspect punctuation immediately after marginal formulas and terminal words, including each separate point of a possible colon. A rotated marginal note still needs comparison of both witnesses’ punctuation. Include enough adjacent white space in a tight crop to decide whether a terminal mark is present and belongs to that note.
- An aligned list of definitions is not intrinsically a diagram. Use ordinary tabular/array layout for formula–prose pairs when there are no graphical relationships to reproduce; keep actual diagrams in TikZ-cd as required.


## Clarifications from the scan 009 comparison (v004)

- Quote glyphs are a reading issue: raised paired strokes versus lateral guillemets must be compared and recorded. They are not merely equivalent macro spellings.
- A punctuation point present in both witnesses is not a difference merely because one places it inside a text macro and the other outside it. Compare the visible content before adding a row.
- When the uncertainty concerns live versus canceled or overwritten state, show those state alternatives in the transcription itself. A bare doubt on readable letters does not express an uncertain cancellation history.
- Include enough vertical context in a tight crop to distinguish a possible accent from ink belonging to the neighboring line. Reuse an already adequate crop rather than making another of the same locus.


### v005_scan011.md

# Reader brief v005 — first used on scan 011

You are one of three independent fresh readers of ONE manuscript page. Do not read another reader's files, any other page's images, or any consolidated decisions for your page. Read the assigned packet only. Do not spawn further readers. Your complete task is the page, not a sample. The scans, not agreement of witnesses or mathematical expectation, decide the reading. No OCR, text-recognition library, PDF text extraction, external research, or published transcription may be used.

## Inputs and order

The packet contains paths to the whole image and two full-resolution halves, witness C's complete page, witness H's corresponding page (their page = our scan minus one), C's relevant doubts/notes, relevant S rows if any, the exact PREAMBLE, and the current notation table. C and H are unverified AI drafts. S is a draft adjudication, not authority. Treat their omissions and agreements alike as requiring visual reading.

1. Read C and H and the supplied conventions. View the whole image ONCE for layout: every text block, display, diagram/drawing, correction, margin, header/footer.
2. View each supplied half ONCE, in order. Read line by line against BOTH witnesses: every word, abbreviation, accent, punctuation, symbol, index/exponent, sign, inequality/arrow, parenthesis, underline, strike, insertion, and marginal note. Look for matter both witnesses missed. Settle everything the halves actually settle. Do not view a whole half again or enlarge the entire half.
3. List what remains open: unresolved witness differences, every C doubt, small decisive signs/indices, slanted/crowded/struck notes. Make ONE tight crop per unresolved locus, containing the word/formula and a little adjacent line. Use Pillow only to crop, rotate upright if needed, autocontrast, sharpen faint strokes and enlarge by LANCZOS to approximately 2400–3600 pixels across. Do not re-crop or re-view a settled locus. Name crops descriptively; record original image, box, rotation, output path, and what strokes decide the reading. When the halves settle a witness difference, supply its tight crop coordinates in the report even if you do not crop it; the main reader needs those coordinates to adjudicate.
4. Return a COMPLETE diplomatic page in reading.tex and a structured report.json, plus concise audit.md. Finish after this page. Do not wait for or consult other readers.

## Transcription conventions

Use only the supplied PREAMBLE's macros plus standard LaTeX, amsmath, amssymb, mathrsfs, ulem, TikZ and tikz-cd. No newly defined notation macros. Start with \\scanpage{N} and \\mspage{n} if present; the main reader adds \\cotefile{156-6} once in the combined fragment. Archive pencil numbering is a comment only: `% archive sheet number: NN`.

Preserve language, spelling, accents or their absence, grammar, punctuation, abbreviations and numbering as inked. Never expand cat., gr., resp., cf., th., prop., dém., etc. Quotation marks are `` and '' unless actual guillemets. Join line-end hyphenation, keep genuine hyphens. Preserve paragraphs; no need to retain line wrapping in prose. Displays use \\[...\\] with aligned if necessary, and exact labels with \\tag*{...}.

Use \\deleted{...} for readable struck/overwritten matter; an unreadable struck word may be \\deleted{\\illegible{1}}. Insertions at their indicated location are \\inserted{...}; independent marginal notes are \\margin{...}, with a `% slanted` or `% margin note written sideways` comment where needed. Preserve each deletion and insertion, even if H gives the corrected live text only. \\uline and \\uuline distinguish one and two underlines. Use \\handwritten only for handwriting on a typed sheet.

Keep all mathematical alphabets, indices, exponents, primes versus exclamation marks, bars, hats, tildes, arrowheads and directions exactly. Record recurring glyph choices in notation_proposals, grounded in this page; the table is provisional evidence, not permission to normalize contrary ink. A recurring ambiguous glyph has \\unsure{a|b} at its first occurrence per page and the first candidate subsequently. Distinguish actual reading differences from mere macro syntax (e.g. H's \\emph versus our \\uline when the same underline is represented).

Use \\unsure{reading} or \\unsure{reading|alternative} wherever the strokes remain ambiguous; first candidate follows ink, not expected mathematics. \\illegible{n} only for physically unreadable words at the deepest crop; NEVER for a formula/diagram symbol (give candidates instead). Do not leave gaps. A doubt mark of C must be individually resolved or retained with evidence.

Typeset every diagram with \\diagram{\\begin{tikzcd}[ampersand replacement=\\&] ... \\end{tikzcd}}, including labels, directions, decorations and struck parts. Draw every drawing in TikZ within \\figure{...}; never substitute a description. Only genuinely complex pictures may have `% crop-candidate: scan N` after a best approximation.

Follow the mathematics while reading. A formula that fails to parse, inconsistent index, sign or implication is a reason to inspect ink, never to silently repair it. Summarize what the page states, computes or asks. Quote every authorial doubt/check phrase. Reading is not a proof check: record check events honestly, including background carried without fault found, and distinguish any actual targeted argument from simple transcription.

## Output format

Write ONLY in your assigned output directory. reading.tex is the full page. report.json is valid UTF-8 JSON with:

- scan, reader, started_utc, finished_utc;
- view_log: objects {image, role: whole/half_a/half_b/crop, viewed_utc};
- differences: one object per substantive locus differing from C OR H, with {id, place, c, h, reading, against_C, against_H, kind, marked_in_H, confidence, evidence, crop, crop_box, crop_source, mathematical}. `kind` is one of: misread word; misread symbol or index; omission; text not on the page; deletion state; insertion or placement; abbreviation expanded or spelling modernised; readable ink left as \\ill{}; drawing or diagram; other. `crop` is relative to out/ or null; crop_box uses original-source pixel coordinates. Do not add rows solely for macro-equivalent spellings. Do include uncertainty removal, deletions and insertions overlooked by either witness.
- c_doubts: {place, c, reading, disposition: resolved/retained, evidence, crop, crop_box, crop_source}; every C unsure/illegible locus, even when retained unchanged.
- s_rows: {id, disposition: confirmed/overturned/partly confirmed/outside page, reading, evidence, crop, crop_box, crop_source}; preserve the distinction between the manuscript's literal reading and S's proposed mathematical correction.
- inventory: every element top to bottom, objects {element, kind, position, first_words_or_objects, sheet_kind, hand, transcribed}. Use kinds text/display/diagram/drawing/margin note/insertion/deletion. sheet_kind usually text; hand usually his hand. Verify all are included and set transcribed=yes only then.
- notes: {content, math_reading_decisions, author_doubts, titles_dates_counts}; English with actual French where quoted.
- check_events: {statement_id, type, outcome}; only events actually performed, not a claimed proof because a formula was read.
- notation_proposals: {sign, latex, ink, alternatives}; abbreviations: {form, expansion}; unresolved: {place, reading, alternatives, confidence, evidence}; brief_feedback: specific problems with this brief or empty.

audit.md records the image-view sequence, the unresolved loci after halves, why each crop was needed and its pixel transform, the line-by-line comparisons (grouping consecutive uncontested lines is acceptable), and any limitation. Report counts of actual crops. Never claim to have viewed an image that you did not emit through the image tool.


## Clarifications from the scan 006 comparison (v002)

- `confidence` must be the literal string `high`, `medium` or `low`, never a numeric score. `marked_in_H` must be `yes` only if H has a genuine DOUBT mark at this very locus (such as `\uncertain{...}` or `\ill{}`). Ordinary `\struck`, `\add` or a descriptive note does NOT constitute a doubt mark. This field is not a statement about whether H notices a physical intervention.
- Credit an explicit H note that correctly records a physical state. If H says an arrow overwrites a hook and our formula typesets that same canceled hook, that alone is not a changed reading. Record disagreements about the underlying stroke; exclude representation-only changes from the collation.
- Align the actual tokens of H locally, including its uncertain tokens: in scan 006, H's final uncertain de occupied the position of manuscript pour; it was not simply an omitted word. Do not split one H token into two discrepancies or overlook a real substitution.
- Distinguish the letter's identity, its literal drawn form, and the choice between typographic alphabets. Preserve genuine alphabet uncertainty at the first occurrence per page; do not silently normalize to either witness's font. Use the notation table's existing candidates unless contrary ink on this page warrants an explicitly recorded change.
- A heavily darkened/retraced letter is not automatically deleted. If both live and canceled states remain possible, mark that actual uncertainty in place; do not invent a previous character. Record physical stroke evidence, not an assumed correction history.
- Output complete `inventory`, `unresolved` and `notes` arrays before announcing completion. Set `status` to `complete` only at that point. Duplicate C doubt-table rows refer to one locus, not multiple uncertainties.
- For `check_events.type`, use only the user's categories: `targeted proof check`, `independent re-proof`, `computation or formal certificate`, `used and rechecked in this run`, `carried as background without fault found`, or `refuted, with refined statement ID`. A visual reading alone is not a mathematical check. Put purely visual decisions in the differences/audit; assertions only summarized may be recorded as background with the explicit outcome “read as the author's assertion; no mathematical verification performed”. Never inflate a sign/prose comparison into a proof.
- Save new crops as high-quality JPEG (quality 95) where practicable, retaining full enlarged resolution. This keeps long-run checkpoints manageable. Do not recompress already-made evidence. Keep the one-crop-per-open-locus rule.


## Clarifications from the scan 008 comparison (v003)

- Inspect punctuation immediately after marginal formulas and terminal words, including each separate point of a possible colon. A rotated marginal note still needs comparison of both witnesses’ punctuation. Include enough adjacent white space in a tight crop to decide whether a terminal mark is present and belongs to that note.
- An aligned list of definitions is not intrinsically a diagram. Use ordinary tabular/array layout for formula–prose pairs when there are no graphical relationships to reproduce; keep actual diagrams in TikZ-cd as required.


## Clarifications from the scan 009 comparison (v004)

- Quote glyphs are a reading issue: raised paired strokes versus lateral guillemets must be compared and recorded. They are not merely equivalent macro spellings.
- A punctuation point present in both witnesses is not a difference merely because one places it inside a text macro and the other outside it. Compare the visible content before adding a row.
- When the uncertainty concerns live versus canceled or overwritten state, show those state alternatives in the transcription itself. A bare doubt on readable letters does not express an uncertain cancellation history.
- Include enough vertical context in a tight crop to distinguish a possible accent from ink belonging to the neighboring line. Reuse an already adequate crop rather than making another of the same locus.

## Clarification from the scan 010 comparison (v005)

- A substantive difference in a drawing's geometry must appear in the differences report as well as reading.tex. Compare open versus closed outlines, gaps, free ends, crossing strokes and approximate proportions. If you change a closed witness ellipse to an open arc, record that locus and its evidence; the main reader must adjudicate it. Credit the witness for an enclosure it explicitly describes, while identifying the specific shape difference.


### v006_scan012.md

# Reader brief v006 — first used on scan 012

You are one of three independent fresh readers of ONE manuscript page. Do not read another reader's files, any other page's images, or any consolidated decisions for your page. Read the assigned packet only. Do not spawn further readers. Your complete task is the page, not a sample. The scans, not agreement of witnesses or mathematical expectation, decide the reading. No OCR, text-recognition library, PDF text extraction, external research, or published transcription may be used.

## Inputs and order

The packet contains paths to the whole image and two full-resolution halves, witness C's complete page, witness H's corresponding page (their page = our scan minus one), C's relevant doubts/notes, relevant S rows if any, the exact PREAMBLE, and the current notation table. C and H are unverified AI drafts. S is a draft adjudication, not authority. Treat their omissions and agreements alike as requiring visual reading.

1. Read C and H and the supplied conventions. View the whole image ONCE for layout: every text block, display, diagram/drawing, correction, margin, header/footer.
2. View each supplied half ONCE, in order. Read line by line against BOTH witnesses: every word, abbreviation, accent, punctuation, symbol, index/exponent, sign, inequality/arrow, parenthesis, underline, strike, insertion, and marginal note. Look for matter both witnesses missed. Settle everything the halves actually settle. Do not view a whole half again or enlarge the entire half.
3. List what remains open: unresolved witness differences, every C doubt, small decisive signs/indices, slanted/crowded/struck notes. Make ONE tight crop per unresolved locus, containing the word/formula and a little adjacent line. Use Pillow only to crop, rotate upright if needed, autocontrast, sharpen faint strokes and enlarge by LANCZOS to approximately 2400–3600 pixels across. Do not re-crop or re-view a settled locus. Name crops descriptively; record original image, box, rotation, output path, and what strokes decide the reading. When the halves settle a witness difference, supply its tight crop coordinates in the report even if you do not crop it; the main reader needs those coordinates to adjudicate.
4. Return a COMPLETE diplomatic page in reading.tex and a structured report.json, plus concise audit.md. Finish after this page. Do not wait for or consult other readers.

## Transcription conventions

Use only the supplied PREAMBLE's macros plus standard LaTeX, amsmath, amssymb, mathrsfs, ulem, TikZ and tikz-cd. No newly defined notation macros. Start with \\scanpage{N} and \\mspage{n} if present; the main reader adds \\cotefile{156-6} once in the combined fragment. Archive pencil numbering is a comment only: `% archive sheet number: NN`.

Preserve language, spelling, accents or their absence, grammar, punctuation, abbreviations and numbering as inked. Never expand cat., gr., resp., cf., th., prop., dém., etc. Quotation marks are `` and '' unless actual guillemets. Join line-end hyphenation, keep genuine hyphens. Preserve paragraphs; no need to retain line wrapping in prose. Displays use \\[...\\] with aligned if necessary, and exact labels with \\tag*{...}.

Use \\deleted{...} for readable struck/overwritten matter; an unreadable struck word may be \\deleted{\\illegible{1}}. Insertions at their indicated location are \\inserted{...}; independent marginal notes are \\margin{...}, with a `% slanted` or `% margin note written sideways` comment where needed. Preserve each deletion and insertion, even if H gives the corrected live text only. \\uline and \\uuline distinguish one and two underlines. Use \\handwritten only for handwriting on a typed sheet.

Keep all mathematical alphabets, indices, exponents, primes versus exclamation marks, bars, hats, tildes, arrowheads and directions exactly. Record recurring glyph choices in notation_proposals, grounded in this page; the table is provisional evidence, not permission to normalize contrary ink. A recurring ambiguous glyph has \\unsure{a|b} at its first occurrence per page and the first candidate subsequently. Distinguish actual reading differences from mere macro syntax (e.g. H's \\emph versus our \\uline when the same underline is represented).

Use \\unsure{reading} or \\unsure{reading|alternative} wherever the strokes remain ambiguous; first candidate follows ink, not expected mathematics. \\illegible{n} only for physically unreadable words at the deepest crop; NEVER for a formula/diagram symbol (give candidates instead). Do not leave gaps. A doubt mark of C must be individually resolved or retained with evidence.

Typeset every diagram with \\diagram{\\begin{tikzcd}[ampersand replacement=\\&] ... \\end{tikzcd}}, including labels, directions, decorations and struck parts. Draw every drawing in TikZ within \\figure{...}; never substitute a description. Only genuinely complex pictures may have `% crop-candidate: scan N` after a best approximation.

Follow the mathematics while reading. A formula that fails to parse, inconsistent index, sign or implication is a reason to inspect ink, never to silently repair it. Summarize what the page states, computes or asks. Quote every authorial doubt/check phrase. Reading is not a proof check: record check events honestly, including background carried without fault found, and distinguish any actual targeted argument from simple transcription.

## Output format

Write ONLY in your assigned output directory. reading.tex is the full page. report.json is valid UTF-8 JSON with:

- scan, reader, started_utc, finished_utc;
- view_log: objects {image, role: whole/half_a/half_b/crop, viewed_utc};
- differences: one object per substantive locus differing from C OR H, with {id, place, c, h, reading, against_C, against_H, kind, marked_in_H, confidence, evidence, crop, crop_box, crop_source, mathematical}. `kind` is one of: misread word; misread symbol or index; omission; text not on the page; deletion state; insertion or placement; abbreviation expanded or spelling modernised; readable ink left as \\ill{}; drawing or diagram; other. `crop` is relative to out/ or null; crop_box uses original-source pixel coordinates. Do not add rows solely for macro-equivalent spellings. Do include uncertainty removal, deletions and insertions overlooked by either witness.
- c_doubts: {place, c, reading, disposition: resolved/retained, evidence, crop, crop_box, crop_source}; every C unsure/illegible locus, even when retained unchanged.
- s_rows: {id, disposition: confirmed/overturned/partly confirmed/outside page, reading, evidence, crop, crop_box, crop_source}; preserve the distinction between the manuscript's literal reading and S's proposed mathematical correction.
- inventory: every element top to bottom, objects {element, kind, position, first_words_or_objects, sheet_kind, hand, transcribed}. Use kinds text/display/diagram/drawing/margin note/insertion/deletion. sheet_kind usually text; hand usually his hand. Verify all are included and set transcribed=yes only then.
- notes: {content, math_reading_decisions, author_doubts, titles_dates_counts}; English with actual French where quoted.
- check_events: {statement_id, type, outcome}; only events actually performed, not a claimed proof because a formula was read.
- notation_proposals: {sign, latex, ink, alternatives}; abbreviations: {form, expansion}; unresolved: {place, reading, alternatives, confidence, evidence}; brief_feedback: specific problems with this brief or empty.

audit.md records the image-view sequence, the unresolved loci after halves, why each crop was needed and its pixel transform, the line-by-line comparisons (grouping consecutive uncontested lines is acceptable), and any limitation. Report counts of actual crops. Never claim to have viewed an image that you did not emit through the image tool.


## Clarifications from the scan 006 comparison (v002)

- `confidence` must be the literal string `high`, `medium` or `low`, never a numeric score. `marked_in_H` must be `yes` only if H has a genuine DOUBT mark at this very locus (such as `\uncertain{...}` or `\ill{}`). Ordinary `\struck`, `\add` or a descriptive note does NOT constitute a doubt mark. This field is not a statement about whether H notices a physical intervention.
- Credit an explicit H note that correctly records a physical state. If H says an arrow overwrites a hook and our formula typesets that same canceled hook, that alone is not a changed reading. Record disagreements about the underlying stroke; exclude representation-only changes from the collation.
- Align the actual tokens of H locally, including its uncertain tokens: in scan 006, H's final uncertain de occupied the position of manuscript pour; it was not simply an omitted word. Do not split one H token into two discrepancies or overlook a real substitution.
- Distinguish the letter's identity, its literal drawn form, and the choice between typographic alphabets. Preserve genuine alphabet uncertainty at the first occurrence per page; do not silently normalize to either witness's font. Use the notation table's existing candidates unless contrary ink on this page warrants an explicitly recorded change.
- A heavily darkened/retraced letter is not automatically deleted. If both live and canceled states remain possible, mark that actual uncertainty in place; do not invent a previous character. Record physical stroke evidence, not an assumed correction history.
- Output complete `inventory`, `unresolved` and `notes` arrays before announcing completion. Set `status` to `complete` only at that point. Duplicate C doubt-table rows refer to one locus, not multiple uncertainties.
- For `check_events.type`, use only the user's categories: `targeted proof check`, `independent re-proof`, `computation or formal certificate`, `used and rechecked in this run`, `carried as background without fault found`, or `refuted, with refined statement ID`. A visual reading alone is not a mathematical check. Put purely visual decisions in the differences/audit; assertions only summarized may be recorded as background with the explicit outcome “read as the author's assertion; no mathematical verification performed”. Never inflate a sign/prose comparison into a proof.
- Save new crops as high-quality JPEG (quality 95) where practicable, retaining full enlarged resolution. This keeps long-run checkpoints manageable. Do not recompress already-made evidence. Keep the one-crop-per-open-locus rule.


## Clarifications from the scan 008 comparison (v003)

- Inspect punctuation immediately after marginal formulas and terminal words, including each separate point of a possible colon. A rotated marginal note still needs comparison of both witnesses’ punctuation. Include enough adjacent white space in a tight crop to decide whether a terminal mark is present and belongs to that note.
- An aligned list of definitions is not intrinsically a diagram. Use ordinary tabular/array layout for formula–prose pairs when there are no graphical relationships to reproduce; keep actual diagrams in TikZ-cd as required.


## Clarifications from the scan 009 comparison (v004)

- Quote glyphs are a reading issue: raised paired strokes versus lateral guillemets must be compared and recorded. They are not merely equivalent macro spellings.
- A punctuation point present in both witnesses is not a difference merely because one places it inside a text macro and the other outside it. Compare the visible content before adding a row.
- When the uncertainty concerns live versus canceled or overwritten state, show those state alternatives in the transcription itself. A bare doubt on readable letters does not express an uncertain cancellation history.
- Include enough vertical context in a tight crop to distinguish a possible accent from ink belonging to the neighboring line. Reuse an already adequate crop rather than making another of the same locus.

## Clarification from the scan 010 comparison (v005)

- A substantive difference in a drawing's geometry must appear in the differences report as well as reading.tex. Compare open versus closed outlines, gaps, free ends, crossing strokes and approximate proportions. If you change a closed witness ellipse to an open arc, record that locus and its evidence; the main reader must adjudicate it. Credit the witness for an enclosure it explicitly describes, while identifying the specific shape difference.

## Clarification from the scan 011 validation incident (v006)

- Do not attempt LaTeX compilation or build any engine formats. The supplied C-session conventions expressly prohibit compilation in this environment. Check JSON, braces, math delimiters, environment pairing and allowed macro usage structurally only. A compile attempt is not an additional required gate. Report any accidental attempt honestly; do not retry it.


### v007_scan014.md

# Reader brief v007 — first used on scan 014

You are one of three independent fresh readers of ONE manuscript page. Do not read another reader's files, any other page's images, or any consolidated decisions for your page. Read the assigned packet only. Do not spawn further readers. Your complete task is the page, not a sample. The scans, not agreement of witnesses or mathematical expectation, decide the reading. No OCR, text-recognition library, PDF text extraction, external research, or published transcription may be used.

## Inputs and order

The packet contains paths to the whole image and two full-resolution halves, witness C's complete page, witness H's corresponding page (their page = our scan minus one), C's relevant doubts/notes, relevant S rows if any, the exact PREAMBLE, and the current notation table. C and H are unverified AI drafts. S is a draft adjudication, not authority. Treat their omissions and agreements alike as requiring visual reading.

1. Read C and H and the supplied conventions. View the whole image ONCE for layout: every text block, display, diagram/drawing, correction, margin, header/footer.
2. View each supplied half ONCE, in order. Read line by line against BOTH witnesses: every word, abbreviation, accent, punctuation, symbol, index/exponent, sign, inequality/arrow, parenthesis, underline, strike, insertion, and marginal note. Look for matter both witnesses missed. Settle everything the halves actually settle. Do not view a whole half again or enlarge the entire half.
3. List what remains open: unresolved witness differences, every C doubt, small decisive signs/indices, slanted/crowded/struck notes. Make ONE tight crop per unresolved locus, containing the word/formula and a little adjacent line. Use Pillow only to crop, rotate upright if needed, autocontrast, sharpen faint strokes and enlarge by LANCZOS to approximately 2400–3600 pixels across. Do not re-crop or re-view a settled locus. Name crops descriptively; record original image, box, rotation, output path, and what strokes decide the reading. When the halves settle a witness difference, supply its tight crop coordinates in the report even if you do not crop it; the main reader needs those coordinates to adjudicate.
4. Return a COMPLETE diplomatic page in reading.tex and a structured report.json, plus concise audit.md. Finish after this page. Do not wait for or consult other readers.

## Transcription conventions

Use only the supplied PREAMBLE's macros plus standard LaTeX, amsmath, amssymb, mathrsfs, ulem, TikZ and tikz-cd. No newly defined notation macros. Start with \\scanpage{N} and \\mspage{n} if present; the main reader adds \\cotefile{156-6} once in the combined fragment. Archive pencil numbering is a comment only: `% archive sheet number: NN`.

Preserve language, spelling, accents or their absence, grammar, punctuation, abbreviations and numbering as inked. Never expand cat., gr., resp., cf., th., prop., dém., etc. Quotation marks are `` and '' unless actual guillemets. Join line-end hyphenation, keep genuine hyphens. Preserve paragraphs; no need to retain line wrapping in prose. Displays use \\[...\\] with aligned if necessary, and exact labels with \\tag*{...}.

Use \\deleted{...} for readable struck/overwritten matter; an unreadable struck word may be \\deleted{\\illegible{1}}. Insertions at their indicated location are \\inserted{...}; independent marginal notes are \\margin{...}, with a `% slanted` or `% margin note written sideways` comment where needed. Preserve each deletion and insertion, even if H gives the corrected live text only. \\uline and \\uuline distinguish one and two underlines. Use \\handwritten only for handwriting on a typed sheet.

Keep all mathematical alphabets, indices, exponents, primes versus exclamation marks, bars, hats, tildes, arrowheads and directions exactly. Record recurring glyph choices in notation_proposals, grounded in this page; the table is provisional evidence, not permission to normalize contrary ink. A recurring ambiguous glyph has \\unsure{a|b} at its first occurrence per page and the first candidate subsequently. Distinguish actual reading differences from mere macro syntax (e.g. H's \\emph versus our \\uline when the same underline is represented).

Use \\unsure{reading} or \\unsure{reading|alternative} wherever the strokes remain ambiguous; first candidate follows ink, not expected mathematics. \\illegible{n} only for physically unreadable words at the deepest crop; NEVER for a formula/diagram symbol (give candidates instead). Do not leave gaps. A doubt mark of C must be individually resolved or retained with evidence.

Typeset every diagram with \\diagram{\\begin{tikzcd}[ampersand replacement=\\&] ... \\end{tikzcd}}, including labels, directions, decorations and struck parts. Draw every drawing in TikZ within \\figure{...}; never substitute a description. Only genuinely complex pictures may have `% crop-candidate: scan N` after a best approximation.

Follow the mathematics while reading. A formula that fails to parse, inconsistent index, sign or implication is a reason to inspect ink, never to silently repair it. Summarize what the page states, computes or asks. Quote every authorial doubt/check phrase. Reading is not a proof check: record check events honestly, including background carried without fault found, and distinguish any actual targeted argument from simple transcription.

## Output format

Write ONLY in your assigned output directory. reading.tex is the full page. report.json is valid UTF-8 JSON with:

- scan, reader, started_utc, finished_utc;
- view_log: objects {image, role: whole/half_a/half_b/crop, viewed_utc};
- differences: one object per substantive locus differing from C OR H, with {id, place, c, h, reading, against_C, against_H, kind, marked_in_H, confidence, evidence, crop, crop_box, crop_source, mathematical}. `kind` is one of: misread word; misread symbol or index; omission; text not on the page; deletion state; insertion or placement; abbreviation expanded or spelling modernised; readable ink left as \\ill{}; drawing or diagram; other. `crop` is relative to out/ or null; crop_box uses original-source pixel coordinates. Do not add rows solely for macro-equivalent spellings. Do include uncertainty removal, deletions and insertions overlooked by either witness.
- c_doubts: {place, c, reading, disposition: resolved/retained, evidence, crop, crop_box, crop_source}; every C unsure/illegible locus, even when retained unchanged.
- s_rows: {id, disposition: confirmed/overturned/partly confirmed/outside page, reading, evidence, crop, crop_box, crop_source}; preserve the distinction between the manuscript's literal reading and S's proposed mathematical correction.
- inventory: every element top to bottom, objects {element, kind, position, first_words_or_objects, sheet_kind, hand, transcribed}. Use kinds text/display/diagram/drawing/margin note/insertion/deletion. sheet_kind usually text; hand usually his hand. Verify all are included and set transcribed=yes only then.
- notes: {content, math_reading_decisions, author_doubts, titles_dates_counts}; English with actual French where quoted.
- check_events: {statement_id, type, outcome}; only events actually performed, not a claimed proof because a formula was read.
- notation_proposals: {sign, latex, ink, alternatives}; abbreviations: {form, expansion}; unresolved: {place, reading, alternatives, confidence, evidence}; brief_feedback: specific problems with this brief or empty.

audit.md records the image-view sequence, the unresolved loci after halves, why each crop was needed and its pixel transform, the line-by-line comparisons (grouping consecutive uncontested lines is acceptable), and any limitation. Report counts of actual crops. Never claim to have viewed an image that you did not emit through the image tool.


## Clarifications from the scan 006 comparison (v002)

- `confidence` must be the literal string `high`, `medium` or `low`, never a numeric score. `marked_in_H` must be `yes` only if H has a genuine DOUBT mark at this very locus (such as `\uncertain{...}` or `\ill{}`). Ordinary `\struck`, `\add` or a descriptive note does NOT constitute a doubt mark. This field is not a statement about whether H notices a physical intervention.
- Credit an explicit H note that correctly records a physical state. If H says an arrow overwrites a hook and our formula typesets that same canceled hook, that alone is not a changed reading. Record disagreements about the underlying stroke; exclude representation-only changes from the collation.
- Align the actual tokens of H locally, including its uncertain tokens: in scan 006, H's final uncertain de occupied the position of manuscript pour; it was not simply an omitted word. Do not split one H token into two discrepancies or overlook a real substitution.
- Distinguish the letter's identity, its literal drawn form, and the choice between typographic alphabets. Preserve genuine alphabet uncertainty at the first occurrence per page; do not silently normalize to either witness's font. Use the notation table's existing candidates unless contrary ink on this page warrants an explicitly recorded change.
- A heavily darkened/retraced letter is not automatically deleted. If both live and canceled states remain possible, mark that actual uncertainty in place; do not invent a previous character. Record physical stroke evidence, not an assumed correction history.
- Output complete `inventory`, `unresolved` and `notes` arrays before announcing completion. Set `status` to `complete` only at that point. Duplicate C doubt-table rows refer to one locus, not multiple uncertainties.
- For `check_events.type`, use only the user's categories: `targeted proof check`, `independent re-proof`, `computation or formal certificate`, `used and rechecked in this run`, `carried as background without fault found`, or `refuted, with refined statement ID`. A visual reading alone is not a mathematical check. Put purely visual decisions in the differences/audit; assertions only summarized may be recorded as background with the explicit outcome “read as the author's assertion; no mathematical verification performed”. Never inflate a sign/prose comparison into a proof.
- Save new crops as high-quality JPEG (quality 95) where practicable, retaining full enlarged resolution. This keeps long-run checkpoints manageable. Do not recompress already-made evidence. Keep the one-crop-per-open-locus rule.


## Clarifications from the scan 008 comparison (v003)

- Inspect punctuation immediately after marginal formulas and terminal words, including each separate point of a possible colon. A rotated marginal note still needs comparison of both witnesses’ punctuation. Include enough adjacent white space in a tight crop to decide whether a terminal mark is present and belongs to that note.
- An aligned list of definitions is not intrinsically a diagram. Use ordinary tabular/array layout for formula–prose pairs when there are no graphical relationships to reproduce; keep actual diagrams in TikZ-cd as required.


## Clarifications from the scan 009 comparison (v004)

- Quote glyphs are a reading issue: raised paired strokes versus lateral guillemets must be compared and recorded. They are not merely equivalent macro spellings.
- A punctuation point present in both witnesses is not a difference merely because one places it inside a text macro and the other outside it. Compare the visible content before adding a row.
- When the uncertainty concerns live versus canceled or overwritten state, show those state alternatives in the transcription itself. A bare doubt on readable letters does not express an uncertain cancellation history.
- Include enough vertical context in a tight crop to distinguish a possible accent from ink belonging to the neighboring line. Reuse an already adequate crop rather than making another of the same locus.

## Clarification from the scan 010 comparison (v005)

- A substantive difference in a drawing's geometry must appear in the differences report as well as reading.tex. Compare open versus closed outlines, gaps, free ends, crossing strokes and approximate proportions. If you change a closed witness ellipse to an open arc, record that locus and its evidence; the main reader must adjudicate it. Credit the witness for an enclosure it explicitly describes, while identifying the specific shape difference.

## Clarification from the scan 011 validation incident (v006)

- Do not attempt LaTeX compilation or build any engine formats. The supplied C-session conventions expressly prohibit compilation in this environment. Check JSON, braces, math delimiters, environment pairing and allowed macro usage structurally only. A compile attempt is not an additional required gate. Report any accidental attempt honestly; do not retry it.


## Clarifications from the scan 013 comparison (v007)

- A repeated alphabet disagreement needs one differences row per written occurrence, with tight coordinates for each half-settled occurrence. Retain a single first-occurrence alphabet doubt per page as already directed; the reporting rows document the individual places, not repeated new doubts.
- Compare a recurring relation glyph's visible geometry, not only its inferred meaning or macro name: central openings, free ends, extra uprights and horizontal caps can differ even when the intended relation is the same. Record each occurrence that differs visibly. An enclosure can straddle a label rather than place the whole label strictly inside; report gaps, hatch counts and connected prose strikes precisely. Reuse an already adequate crop, and do not re-view or re-crop settled places.


### v008_scan016.md

# Reader brief v008 — first used on scan 016

You are one of three independent fresh readers of ONE manuscript page. Do not read another reader's files, any other page's images, or any consolidated decisions for your page. Read the assigned packet only. Do not spawn further readers. Your complete task is the page, not a sample. The scans, not agreement of witnesses or mathematical expectation, decide the reading. No OCR, text-recognition library, PDF text extraction, external research, or published transcription may be used.

## Inputs and order

The packet contains paths to the whole image and two full-resolution halves, witness C's complete page, witness H's corresponding page (their page = our scan minus one), C's relevant doubts/notes, relevant S rows if any, the exact PREAMBLE, and the current notation table. C and H are unverified AI drafts. S is a draft adjudication, not authority. Treat their omissions and agreements alike as requiring visual reading.

1. Read C and H and the supplied conventions. View the whole image ONCE for layout: every text block, display, diagram/drawing, correction, margin, header/footer.
2. View each supplied half ONCE, in order. Read line by line against BOTH witnesses: every word, abbreviation, accent, punctuation, symbol, index/exponent, sign, inequality/arrow, parenthesis, underline, strike, insertion, and marginal note. Look for matter both witnesses missed. Settle everything the halves actually settle. Do not view a whole half again or enlarge the entire half.
3. List what remains open: unresolved witness differences, every C doubt, small decisive signs/indices, slanted/crowded/struck notes. Make ONE tight crop per unresolved locus, containing the word/formula and a little adjacent line. Use Pillow only to crop, rotate upright if needed, autocontrast, sharpen faint strokes and enlarge by LANCZOS to approximately 2400–3600 pixels across. Do not re-crop or re-view a settled locus. Name crops descriptively; record original image, box, rotation, output path, and what strokes decide the reading. When the halves settle a witness difference, supply its tight crop coordinates in the report even if you do not crop it; the main reader needs those coordinates to adjudicate.
4. Return a COMPLETE diplomatic page in reading.tex and a structured report.json, plus concise audit.md. Finish after this page. Do not wait for or consult other readers.

## Transcription conventions

Use only the supplied PREAMBLE's macros plus standard LaTeX, amsmath, amssymb, mathrsfs, ulem, TikZ and tikz-cd. No newly defined notation macros. Start with \\scanpage{N} and \\mspage{n} if present; the main reader adds \\cotefile{156-6} once in the combined fragment. Archive pencil numbering is a comment only: `% archive sheet number: NN`.

Preserve language, spelling, accents or their absence, grammar, punctuation, abbreviations and numbering as inked. Never expand cat., gr., resp., cf., th., prop., dém., etc. Quotation marks are `` and '' unless actual guillemets. Join line-end hyphenation, keep genuine hyphens. Preserve paragraphs; no need to retain line wrapping in prose. Displays use \\[...\\] with aligned if necessary, and exact labels with \\tag*{...}.

Use \\deleted{...} for readable struck/overwritten matter; an unreadable struck word may be \\deleted{\\illegible{1}}. Insertions at their indicated location are \\inserted{...}; independent marginal notes are \\margin{...}, with a `% slanted` or `% margin note written sideways` comment where needed. Preserve each deletion and insertion, even if H gives the corrected live text only. \\uline and \\uuline distinguish one and two underlines. Use \\handwritten only for handwriting on a typed sheet.

Keep all mathematical alphabets, indices, exponents, primes versus exclamation marks, bars, hats, tildes, arrowheads and directions exactly. Record recurring glyph choices in notation_proposals, grounded in this page; the table is provisional evidence, not permission to normalize contrary ink. A recurring ambiguous glyph has \\unsure{a|b} at its first occurrence per page and the first candidate subsequently. Distinguish actual reading differences from mere macro syntax (e.g. H's \\emph versus our \\uline when the same underline is represented).

Use \\unsure{reading} or \\unsure{reading|alternative} wherever the strokes remain ambiguous; first candidate follows ink, not expected mathematics. \\illegible{n} only for physically unreadable words at the deepest crop; NEVER for a formula/diagram symbol (give candidates instead). Do not leave gaps. A doubt mark of C must be individually resolved or retained with evidence.

Typeset every diagram with \\diagram{\\begin{tikzcd}[ampersand replacement=\\&] ... \\end{tikzcd}}, including labels, directions, decorations and struck parts. Draw every drawing in TikZ within \\figure{...}; never substitute a description. Only genuinely complex pictures may have `% crop-candidate: scan N` after a best approximation.

Follow the mathematics while reading. A formula that fails to parse, inconsistent index, sign or implication is a reason to inspect ink, never to silently repair it. Summarize what the page states, computes or asks. Quote every authorial doubt/check phrase. Reading is not a proof check: record check events honestly, including background carried without fault found, and distinguish any actual targeted argument from simple transcription.

## Output format

Write ONLY in your assigned output directory. reading.tex is the full page. report.json is valid UTF-8 JSON with:

- scan, reader, started_utc, finished_utc;
- view_log: objects {image, role: whole/half_a/half_b/crop, viewed_utc};
- differences: one object per substantive locus differing from C OR H, with {id, place, c, h, reading, against_C, against_H, kind, marked_in_H, confidence, evidence, crop, crop_box, crop_source, mathematical}. `kind` is one of: misread word; misread symbol or index; omission; text not on the page; deletion state; insertion or placement; abbreviation expanded or spelling modernised; readable ink left as \\ill{}; drawing or diagram; other. `crop` is relative to out/ or null; crop_box uses original-source pixel coordinates. Do not add rows solely for macro-equivalent spellings. Do include uncertainty removal, deletions and insertions overlooked by either witness.
- c_doubts: {place, c, reading, disposition: resolved/retained, evidence, crop, crop_box, crop_source}; every C unsure/illegible locus, even when retained unchanged.
- s_rows: {id, disposition: confirmed/overturned/partly confirmed/outside page, reading, evidence, crop, crop_box, crop_source}; preserve the distinction between the manuscript's literal reading and S's proposed mathematical correction.
- inventory: every element top to bottom, objects {element, kind, position, first_words_or_objects, sheet_kind, hand, transcribed}. Use kinds text/display/diagram/drawing/margin note/insertion/deletion. sheet_kind usually text; hand usually his hand. Verify all are included and set transcribed=yes only then.
- notes: {content, math_reading_decisions, author_doubts, titles_dates_counts}; English with actual French where quoted.
- check_events: {statement_id, type, outcome}; only events actually performed, not a claimed proof because a formula was read.
- notation_proposals: {sign, latex, ink, alternatives}; abbreviations: {form, expansion}; unresolved: {place, reading, alternatives, confidence, evidence}; brief_feedback: specific problems with this brief or empty.

audit.md records the image-view sequence, the unresolved loci after halves, why each crop was needed and its pixel transform, the line-by-line comparisons (grouping consecutive uncontested lines is acceptable), and any limitation. Report counts of actual crops. Never claim to have viewed an image that you did not emit through the image tool.


## Clarifications from the scan 006 comparison (v002)

- `confidence` must be the literal string `high`, `medium` or `low`, never a numeric score. `marked_in_H` must be `yes` only if H has a genuine DOUBT mark at this very locus (such as `\uncertain{...}` or `\ill{}`). Ordinary `\struck`, `\add` or a descriptive note does NOT constitute a doubt mark. This field is not a statement about whether H notices a physical intervention.
- Credit an explicit H note that correctly records a physical state. If H says an arrow overwrites a hook and our formula typesets that same canceled hook, that alone is not a changed reading. Record disagreements about the underlying stroke; exclude representation-only changes from the collation.
- Align the actual tokens of H locally, including its uncertain tokens: in scan 006, H's final uncertain de occupied the position of manuscript pour; it was not simply an omitted word. Do not split one H token into two discrepancies or overlook a real substitution.
- Distinguish the letter's identity, its literal drawn form, and the choice between typographic alphabets. Preserve genuine alphabet uncertainty at the first occurrence per page; do not silently normalize to either witness's font. Use the notation table's existing candidates unless contrary ink on this page warrants an explicitly recorded change.
- A heavily darkened/retraced letter is not automatically deleted. If both live and canceled states remain possible, mark that actual uncertainty in place; do not invent a previous character. Record physical stroke evidence, not an assumed correction history.
- Output complete `inventory`, `unresolved` and `notes` arrays before announcing completion. Set `status` to `complete` only at that point. Duplicate C doubt-table rows refer to one locus, not multiple uncertainties.
- For `check_events.type`, use only the user's categories: `targeted proof check`, `independent re-proof`, `computation or formal certificate`, `used and rechecked in this run`, `carried as background without fault found`, or `refuted, with refined statement ID`. A visual reading alone is not a mathematical check. Put purely visual decisions in the differences/audit; assertions only summarized may be recorded as background with the explicit outcome “read as the author's assertion; no mathematical verification performed”. Never inflate a sign/prose comparison into a proof.
- Save new crops as high-quality JPEG (quality 95) where practicable, retaining full enlarged resolution. This keeps long-run checkpoints manageable. Do not recompress already-made evidence. Keep the one-crop-per-open-locus rule.


## Clarifications from the scan 008 comparison (v003)

- Inspect punctuation immediately after marginal formulas and terminal words, including each separate point of a possible colon. A rotated marginal note still needs comparison of both witnesses’ punctuation. Include enough adjacent white space in a tight crop to decide whether a terminal mark is present and belongs to that note.
- An aligned list of definitions is not intrinsically a diagram. Use ordinary tabular/array layout for formula–prose pairs when there are no graphical relationships to reproduce; keep actual diagrams in TikZ-cd as required.


## Clarifications from the scan 009 comparison (v004)

- Quote glyphs are a reading issue: raised paired strokes versus lateral guillemets must be compared and recorded. They are not merely equivalent macro spellings.
- A punctuation point present in both witnesses is not a difference merely because one places it inside a text macro and the other outside it. Compare the visible content before adding a row.
- When the uncertainty concerns live versus canceled or overwritten state, show those state alternatives in the transcription itself. A bare doubt on readable letters does not express an uncertain cancellation history.
- Include enough vertical context in a tight crop to distinguish a possible accent from ink belonging to the neighboring line. Reuse an already adequate crop rather than making another of the same locus.

## Clarification from the scan 010 comparison (v005)

- A substantive difference in a drawing's geometry must appear in the differences report as well as reading.tex. Compare open versus closed outlines, gaps, free ends, crossing strokes and approximate proportions. If you change a closed witness ellipse to an open arc, record that locus and its evidence; the main reader must adjudicate it. Credit the witness for an enclosure it explicitly describes, while identifying the specific shape difference.

## Clarification from the scan 011 validation incident (v006)

- Do not attempt LaTeX compilation or build any engine formats. The supplied C-session conventions expressly prohibit compilation in this environment. Check JSON, braces, math delimiters, environment pairing and allowed macro usage structurally only. A compile attempt is not an additional required gate. Report any accidental attempt honestly; do not retry it.


## Clarifications from the scan 013 comparison (v007)

- A repeated alphabet disagreement needs one differences row per written occurrence, with tight coordinates for each half-settled occurrence. Retain a single first-occurrence alphabet doubt per page as already directed; the reporting rows document the individual places, not repeated new doubts.
- Compare a recurring relation glyph's visible geometry, not only its inferred meaning or macro name: central openings, free ends, extra uprights and horizontal caps can differ even when the intended relation is the same. Record each occurrence that differs visibly. An enclosure can straddle a label rather than place the whole label strictly inside; report gaps, hatch counts and connected prose strikes precisely. Reuse an already adequate crop, and do not re-view or re-crop settled places.


## Clarifications from the scan 015 comparison (v008)

- When two recoverable letters occupy the same overwritten position, preserve their overlap in LaTeX rather than placing deleted and live letters sequentially. Standard mathord/rlap markup may be used; retain overlap inside each uncertain state alternative as well. Do not infer an earlier letter from a lone unexplained diagonal.
- H may put a gloss in parentheses in its formula while an explicit note correctly places the words under a brace. Compare the actual manuscript punctuation, but distinguish H’s supplied editorial grouping from an asserted extra ink parenthesis. Report the issue and credit its note; the main reader will record the disposition without manufacturing an omission. Actual manuscript parentheses must always be retained.


## Reasons for revisions

# Brief revisions

## v001 → v002, first used on scan 007

Scan 006 readers interpreted `marked_in_H` as any physical-state markup, whereas the requested field means only a doubt mark; the brief now states that distinction explicitly. Two readers supplied numeric confidence, so the required high/medium/low strings are explicit. Readers differed on whether H’s explanatory hook note should count as a collation change; equivalent physical readings are now credited regardless of macro location. They also aligned H’s final uncertain de differently against manuscript pour; the brief asks for local token alignment. The font-choice and retracing ambiguities are separated from letter identity and recoverable previous text. Required check-event categories and non-proof scope are explicit. Complete report fields are checked at completion. New evidence crops use high-quality JPEG to reduce checkpoint size without reducing pixel dimensions; prior PNG evidence is preserved.

The supplied C-context extraction was de-duplicated while scan 006 was in progress; some first readers had already read the duplicated rows. This changed no input reading and no adjudication. A convention reminder about retouching versus recoverable deletion was sent to R2 during scan 006; it supplied no other reader’s reading and did not assert which state the ink showed. Future readers receive the clarification together in the brief.

## v003 — scan 009 onward

Scan 008 readers differed on punctuation in both slanted NB notes. Added explicit attention to adjacent punctuation and crop boundaries. Also clarified that ordinary aligned definition lists are not diagrams; all actual diagrams still require TikZ-cd. No other reading policy changed.

- v004, first used scan 010: the scan 009 comparison found omitted quote-shape differences in R1/R2, a false terminal-period difference caused solely by a text-macro boundary in R1, and an inadequately expressed cancellation-state alternative in R2. The brief now distinguishes these cases and reminds readers to retain vertical context for accent attribution.

- v005, first used scan 011: scan010 R3 drew the enclosing oval with a gap but did not list its difference from C's closed ellipse; R1/R2 retained a closed ellipse. Main confirmed the gap locally. The next brief requires drawing-geometry differences to appear in both transcription and report. The crop helper's JPEG quality was separately aligned to the existing quality-95 instruction; no evidence was recompressed.

- v006, first used scan 012: scan011 R2 attempted an unnecessary LaTeX compilation, which failed for lack of pdflatex.fmt. The inherited C conventions prohibit trying compilation; this had not been restated explicitly in the reader brief. The next brief makes structural-only validation explicit. R1/R3 received the clarification before completing scan011; no format construction or retry was authorized.

- v007, first used scan 014: scan013 reports bundled recurring font occurrences and differed on relation-glyph geometry, cancellation hatch count and whether the old label lay fully inside the frame. The brief now requires separate local rows/coordinates for recurring font differences and distinguishes visible geometry from shared relational meaning; enclosure descriptions must account for labels straddling boundaries.


## Actual crops per page

Counts include separate crops made independently by different readers. Supplied whole pages and halves are not crops in this table. The main reader may adjudicate from a reader’s existing crop without creating another.

| Scan | Brief | R1 | R2 | R3 | Main | Total |
|---|---|---|---|---|---|---|
| 006 | v001 | 16 | 12 | 15 | 3 | 46 |
| 007 | v002 | 12 | 13 | 14 | 7 | 46 |
| 008 | v002 | 15 | 15 | 17 | 3 | 50 |
| 009 | v003 | 15 | 17 | 17 | 6 | 55 |
| 010 | v004 | 14 | 14 | 16 | 13 | 57 |
| 011 | v005 | 13 | 11 | 17 | 9 | 50 |
| 012 | v006 | 11 | 12 | 9 | 8 | 40 |
| 013 | v006 | 17 | 17 | 18 | 13 | 65 |
| 014 | v007 | 10 | 9 | 9 | 18 | 46 |
| 015 | v007 | 14 | 13 | 13 | 12 | 52 |


## What worked and what did not

The independent readings separate agreement about the ink from agreement with a draft. On scan 006, all three readers independently recovered several clear C doubts, while their disagreements about a cancelled article, alphabet choices and dense retracing remained visible in the returns. Targeted main-reader crops resolved the placement of an insertion, the y in déployement and the cancellation before C’est; the main reader retained uncertainty where the strokes did not settle it.

The main reader compares complete page files and all reported differences before commitment. Explanatory witness notes are credited when they record the same physical state. Font alternatives and doubt cleanup are counted as transcription changes, so change counts are not presented as independent estimates of witness error rates.

The first brief did not spell out several field semantics sharply enough. Two readers used numeric confidence, and all treated some ordinary H state markup as a doubt flag. Those fields are corrected explicitly in the consolidated records; the raw independent returns are preserved. Version 002 makes the required semantics explicit. The C context extraction initially repeated table rows and was de-duplicated without changing readings.

Large evidence PNGs on the first page increased checkpoint size. Later readers are asked to retain enlarged pixel dimensions while saving new crops as high-quality JPEG. Existing crops are never recompressed. Separate crops from independent readers remain separate evidence, even where they cover the same locus.

This assessment remains in progress until all 28 pages are adjudicated.

Scan 007: uncertainty about a canceled predecessor was separated from uncertainty about the live letter. Existing reader crops settled the comparison without duplicate crop creation. The main reader made seven additional crops for witness differences settled by readers at half-page scale, and viewed 21 crops in total. Fourteen C doubts were individually adjudicated: five resolved and nine retained.

The page-commit script initially matched crop-view JSON logs as well as decision records. Its glob was narrowed to exact three-digit scan decision filenames; no page or subsequent reading started before the corrected commit succeeded.

### Scan 008

Three independent complete returns used 15, 15 and 17 actual crops. Main adjudication inspected 21 distinct local evidence crops, reusing 18 reader crops and making three new crops for witness differences settled on the halves. A six-image output exceeded the available model context and was not inspectable; those same six files were emitted again in pairs and then inspected. No new crop or whole/half rereading was used for this delivery failure. The main-view list records the 21 successfully inspected distinct files, not the failed delivery as an additional reading.

Marginal punctuation required explicit adjudication: R2 preserved a period after discrètes and a colon after the lower marginal implication that R1/R3 treated differently. The main adopted the visible marks. The brief revision for subsequent pages calls attention to punctuation immediately after marginal formulas and terminal words; no claim is made that the earlier crops clipped the marks. The central list is prose aligned with formulas, not a diagram. Recursive crop counting now includes nested main-crop directories; previously committed counts are unchanged.

The structural validator initially mistook the optional spacing in a table line break (`\\[.45em]`) for a display opener. It now tokenizes control sequences before counting display delimiters. The transcription itself was unchanged; all three committed pages pass structural validation.

### Scan 009

All three complete independent returns were compared before commitment. They made 15, 17 and 17 crops. The main inspected 25 distinct crops: 19 reused reader crops and six new crops for loci settled at half-page scale, including the S attribution line. Two new crops were initially emitted together but the output was truncated and not inspectable; those same files were emitted separately and inspected. No recropping or whole/half rereading resulted. The main-view list counts successfully inspected distinct files only.

The extra point after the opening élément was preserved by R2 alone and confirmed in the crop. R3’s possible canceled equals sign and physical-state uncertainty at the article were retained. R1’s fuller alternatives for the ateliers ending were kept. A claimed terminal-period difference in R1 was excluded because both witnesses already carry the point; its inside/outside text-macro placement is representation only. Actual quote-glyph differences remain recorded. A second existing crop with adjacent vertical context resolved accent attribution for elt without creating another crop.

All 13 C doubts were individually reviewed: nine resolved, four retained. Five other doubts were introduced or retained after comparison, giving nine final unresolved loci. S row SA21-K6-07 was partly confirmed for its local manuscript attribution; its proposed axiom refinement was not mathematically checked. The next brief addresses quote shape, macro-only punctuation differences and explicit uncertain physical states.

During scan 010, R2 noted that the shared crop helper saved new JPEG crops at quality 92 while the brief requested quality 95 where practicable. The helper default was aligned to 95 after all three readers had completed their crops. Previously made evidence was not recompressed or changed. Both qualities retained the full enlarged dimensions.

### Scan 010

The three fresh independent readers returned complete pages and reports, with 14, 14 and 16 crops. Main inspected 29 distinct local crops: 16 existing reader crops and 13 new crops. An attempted two-image delivery of the first two new crops was truncated before they could be inspected; those same files were then emitted separately and inspected, without recropping. Main never viewed a whole page or supplied half. The successful-view record excludes the failed delivery as an inspection.

Main resolved canceled notion and the unaccented connaitre despite a reader's retained doubt, and resolved the canceled lower sign as ll against R3's broader alternatives. Surajoute remains first with surrajoute retained; exemples/exemple and the final hyphen remain uncertain. The extra NB sign keeps explicit live/canceled state alternatives and a trace of its visible angular construction. R3 alone reproduced the enclosure's upper-right gap; the main crop confirmed it and supplied a more faithful oval aspect ratio. That geometry was absent from the reader's differences list, prompting v005's instruction to report drawing differences as well as include them in reading.tex.

There are 32 distinct witness-difference loci, 16 individually reviewed C doubts (8 resolved and 8 retained), 9 final unresolved loci, and 18 inventory elements. Some reader rows bundled separate occurrences or words; the final record separates the two zigzag occurrences, de nature from the extra H article, and que from ceux. No macro-only discrepancy was counted. No mathematical proof or computation was claimed.

During scan 011, R2 attempted a LaTeX compilation after its transcription was complete. This was contrary to the supplied C-session convention “Do not try to compile” (PROMPT.md, assemble-and-check instruction). The engine could not find pdflatex.fmt, and no compilation succeeded or image-based layout validation resulted. The attempt is retained in R2's audit. Main did not retry or build formats; R1/R3 were immediately instructed to use structural validation only. The shared reader brief had not restated this prohibition explicitly; v006 adds it for all subsequent pages. This is a recorded workflow failure, not a successful validation.


### Scan 011

All three independent complete readings were compared. R1/R2/R3 made 13/11/17 crops. Main inspected 25 distinct local evidence crops: 16 existing reader crops and nine new crops for the remaining half-settled witness differences. The first delivery of new main crop 01 was truncated and not inspectable; the same file was emitted separately and inspected, without recropping. No main whole/half view occurred. The successful-view list records 25 files, and all actual crops total 50.

The endings of sophistiquées/sophistiqués, ds/d', the verb entre/reste, the date separator and ces points/ce point were not settled by reader majority or grammar. Their explicit alternatives remain, with entre first after main inspection. R3 alone raised the doubled/retraced first F in (1.17), which main retained. C's missed inner cancellation of the old gloss noun is restored while preserving the whole-gloss cancellation. The terminal abbreviation mark remains uncertain. The brace span, both quotation loci and all recurring family-letter differences were separately covered by local crops.

There are 38 final witness-difference loci and one recorded editorial-layout adjudication. H's sous c) bridge is credited as editorial and excluded from transcription and counts. All 18 C doubts were individually reviewed (10 resolved, 8 retained), with four additional doubts giving 12 unresolved loci and 22 inventory elements. No proof or computation was claimed. The compilation incident described above prompted v006; no further brief change was needed.


### Scan 012

The three fresh readers completed independent readings with 11, 12 and 9 crops. Main inspected 23 distinct local crops: 15 reused and eight new crops for witness differences settled on the halves. The first delivery of R2’s label crop was truncated before inspection at a context boundary; the same file was re-emitted successfully. No new crop, main whole-page view, half rereading or repeat inspection of a decided locus resulted. All actual crops total 40.

Main resolved ordinary marginal membership against R1’s retained prime alternative and adopted R2’s unaccented deployement after inspecting sufficient vertical context. R1/R3’s uncertainty about the diagram’s extra upright is preserved, together with R1’s doubled-looking F. R3’s punctuation uncertainty in inserted de plus is retained. R1’s accent alternatives for the canceled equivalent are retained against R3’s resolved word. The two clear prose compatibility signs were checked separately from the dark diagram occurrence.

There are 41 witness-difference loci, ten individually reviewed C doubts (five resolved and five retained), nine final doubts and 26 inventory elements. All drawing geometry, marginal formulas and physical interventions are represented. H’s literal family-letter note is credited, while the emended displayed formula is recorded as different. R3 and main performed a limited check of the marginal diagonal formula. Main also checked transitivity and diagonal incidence conditionally from the committed (1.17), assuming the stated order property of ≤; no larger reconstruction proof is claimed. Existing v006 covers the remaining disagreements; no further brief revision was needed.


### Scan 013

Three fresh independent readers completed 17, 17 and 18 unique crops. Main inspected 32 distinct local crops: 19 reused reader crops and 13 new crops for the remaining witness discrepancies. No main whole or half image was viewed. The attempted delivery of main crops 08–10 at a context boundary was truncated before inspection; the same files were subsequently emitted successfully, without recropping. Total unique crops: 65.

Main resolved G, unaccented Verifier, the older ≤, ens, minimaux, F and the literal brace-V ending. It retained the layered arrows and other physically ambiguous letters. R1’s proposed underline at figure is the continuous g descender. The cancellation enclosure has four hatches, an upper-left gap, a prose strike continuing past its right side, and the old display label straddling its left boundary. H’s physical notes are credited; geometry and inner-letter disagreements are separately recorded. All eight later family-font occurrences have individual evidence rows. There are 43 witness-difference loci, nineteen C doubts (seven resolved, twelve retained), twelve final doubts and 29 inventory elements.

Main computed the finite-order component of supplied S row SA21-K6-06. This was not a check that the structure satisfies all atelier axioms, the surviving implication under those axioms, or the Atens 2 sufficient condition. These limits are explicit in the notes and CHECK_EVENTS.

The execution environment failed around 12:10 UTC. Work was restored from checkpoint04, the original attachments and the retained conversation. Committed pages006–012 were unchanged. Reader013 post-checkpoint reports were restored by their original readers from their own retained tool-call text, without viewing images again. R1’s final crop17 was reconstructed with its recorded transform; its original image bytes and exact creation second were not recoverable, and this limitation is stated in its audit. A metadata-only auxiliary audit found all 775 checkpoint members present, 771 byte-identical and only four expected post-checkpoint files changed; all 174 source files matched the original ZIP and all 2,870 recorded absolute paths resolved through the restored alias. Structural checks passed. This auxiliary agent did not act as a manuscript reader.

Version v007 adds two reporting clarifications prompted by this comparison: record each differing occurrence of a recurring alphabet separately, and describe actual glyph/enclosure geometry rather than treating the same relational meaning as identical ink. The existing one-crop rule remains unchanged.

Record rendering clarification during scan014: the doubts and unresolved tables now extract the already-recorded alternatives into the Alternatives column, rather than referring generically to the reading cell. A single doubtful candidate says that no alternative was securely recovered. This changes table presentation only; no committed reading or candidate set changed.


### Scan 014

Three fresh independent readers supplied complete texts and final reports, using 10/9/9 unique crops. Main began local adjudication only after all three readers had completed their image inspection and saved full draft readings; all three final reading.tex SHA-256 values were checked against those saved draft hashes and were unchanged. Main inspected 28 distinct local crops: ten reused reader crops and eighteen new crops. Main never viewed the whole or either supplied half. An attempted combined delivery of new crops 01–03 was truncated before inspection; the same files were later emitted successfully, with no recropping. The view log records only successful inspections.

The final record has 37 distinct witness-difference loci (12 against C, 36 against H), one additional adjudication of possible H editorial bracket markup, ten C doubts (five resolved, five retained), eleven inventory elements and nine final unresolved loci. The enclosure's three gaps and the upper compatibility sign's reinforced branches are reproduced. A metadata-only audit independently mapped all 98 reader-difference rows to the completed local adjudications and found no missing textual disagreement. Its small wording cautions are recorded: the d_apres accent is grave, and the formula contains two unprimed F, two F-prime and two G. Reader files remain unmodified.

S SA21-K6-02 is partly confirmed. Literal reflexivity and the surtout insertion are confirmed; the initial accent remains uncertain. Main performed the limited conditional proof with intermediate F-prime=F, assuming reflexivity of both constituent relations. The proposed antisymmetry emendation, its historical C8_0 basis, transitivity and the generated-preorder equivalence were not proved or silently substituted. No LaTeX compilation was attempted on this page. Brief v007 remains sufficient for the next page.


### Scan 015

Three fresh readers completed independent readings with 14/13/13 unique crops. Main compared all complete texts and all 36/37/38 discrepancy rows. The saved draft reading hashes were checked against the final files and were unchanged. Main inspected 27 unique local crops: 15 reused reader crops and 12 new crops. Total unique evidence crops: 52. Two attempted early crop emissions were truncated before inspection and then successfully emitted once; the actual-view log does not count the failed deliveries. No main whole/half view or repeated inspection of a decided locus occurred.

The final record has 37 witness-difference loci (24 against C, 23 against H) and one additional editorial-parentheses adjudication. All eleven C doubts were decided: six resolved and five retained, with two distinct additional doubts giving seven residual loci. Thirty inventory subelements cover the readers’ 27/27/29 entries, including both the canceled X and superimposed live F. A metadata-only auxiliary audit exhaustively mapped the 38-locus union and all inventory/C-doubt entries. Its cautions were incorporated without new image views.

Main retained R2’s avec uncertainty, R1/R3’s fourth-index uncertainty, and R2/R3’s final accent uncertainty. The second map preserves all three states, with overlap represented in the overwritten-X alternative. The literal (1.25) and Dep are retained. Main proved only forward lower-set monotonicity under explicit transitivity, not either injectivity or the reverse implication from atelier axioms. H’s first-X and brace notes receive credit. Its parenthesized inline gloss and combined definition line are treated as editorial representation; its canceled number’s prose attachment is a real placement difference. No LaTeX compilation was attempted.

Version v008 clarifies same-position overwrite markup and distinguishes supplied grouping from manuscript parentheses when H’s own note explicitly supplies the physical layout. This addresses the sequential deleted-X/F markup in R2/R3 and the readers’ differing treatment of H’s parenthesized gloss. The existing figure-wrapper rule remains unchanged. Record rendering now counts crops from both observed main-crop directory conventions, without moving or changing any image.
