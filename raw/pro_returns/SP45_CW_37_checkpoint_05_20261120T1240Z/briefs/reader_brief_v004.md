# Reader brief v004 — first used on scan 010

You are one of THREE independent readers of ONE page in a diplomatic second pass. Do not read another reader's files or ask another reader; do not open other pages' images, witnesses, reports, or source notes. Your task ends with this page. The main reader will adjudicate all differences. Read slowly and completely, from the INK, with both draft witnesses beside it. No OCR, text recognition, external research, published text, or mathematical reconstruction.

Inputs: the assigned packet's metadata.json, C.tex, H.tex, C_prior_questions.md, C_inventory.json; this brief, conventions.md, PREAMBLE.tex; and the supplied notation snapshot. Only metadata.json gives this page's image paths. H may be description only: then it is not a textual witness; do not generate H collation rows for that page.

## Workflow, exactly once per source view
1. Read the textual inputs. Look at the WHOLE image ONCE with view_image for layout (text blocks, displays, margins, additions, cancellations, drawings). This view counts as actual image inspection only if emitted and seen.
2. Look at half _a ONCE and half _b ONCE, line by line against C AND H. Read EVERY word, abbreviation, accent, punctuation mark, symbol, index, exponent, arrow, deletion, insertion and marginal note. Agreement between witnesses supplies no evidence. Settle everything the halves settle; do not reopen/re-enlarge a whole half.
3. List unresolved loci. Crop each unresolved locus ONCE from the source using PIL: tight word/formula and surrounding line; upscale using LANCZOS to about 2000–3500 pixels across; autocontrast/sharpen if needed; rotate upright if slanted. View the crop. Each crop must have a unique name and documented original coordinates, source, transforms, and locus. No repeat crop of a decided place. A C doubt always gets an explicit resolution or retention; no need to crop if the half settles it. Follow the mathematics as a detector of suspicious indices/signs/arrows, but never repair the page to make the mathematics true.
4. Write the COMPLETE page reading in our LaTeX macros as reading.tex in your assigned output directory. Copy C as a base if helpful only AFTER checking every element against the ink; your output is a full, independently verified reading, not just proposed edits. Write report.json (schema below). Summarize your principal findings and counts, then finish. Do not edit shared deliverables or other readers' directories.

## Fidelity priorities
Keep every typed error, strange accent, abbreviation, singular/plural, underlining, deletion state, insertion placement and source question mark. Every letter in a heading/functor is checked separately for single/double strike. Distinguish actual overtyping correction from mere heavier or doubled same-letter type. His double quotes are ``...'' (not guillemets unless drawn). Join line-end hyphenations; keep real word hyphens. Typescript capitals are not bold. In doubt, give visible candidates with unsure, not a contextual restoration. No illegible for mathematical symbols; no omission. Diagrams in tikz-cd and drawings in TikZ, never just descriptions. H's editorial descriptions are not source text. Same reading in different macro syntax is not a collation difference; real state (strike/insertion/underline), spelling, omission or placement IS a difference. Do not declare an abbreviation wrong merely because H includes normal nonbreaking spaces or different line wrapping.

## Report schema (valid UTF-8 JSON)
{
 "scan": 3, "reader": "r1", "model": "GPT-6 Astra Pro", "effort": "inherited; not independently exposed", "started_utc": "...", "ended_utc": "...",
 "views": [{"path":"...", "role":"whole|a|b", "viewed_once":true}],
 "coverage": "Specific concise account of all blocks actually read, including margins and deletions; say if any part remains unviewed.",
 "changes": [{"locus":"specific source line/block", "c":"exact C reading", "h":"exact H reading or [description only]", "reading":"your final reading", "diff_c":true, "diff_h":false, "kind":"one allowed H kind below", "marked_in_H":false, "confidence":"high|medium|low", "evidence":"actual letters/strokes/marks observed, half or crop", "crop":"relative crop path if any", "bbox":[x0,y0,x1,y1], "mathematical_consequence":"if any"}],
 "c_doubts": [{"locus":"...", "c":"...", "decision":"resolved|retained", "reading":"...", "evidence":"...", "crop":"..."}],
 "unresolved": [{"locus":"...", "reading":"...", "alternatives":["..."], "confidence":"...", "reason":"..."}],
 "inventory": [{"sheet_kind":"text|reused_typed|typescript|letter|list|cancelled_draft|cover", "hand":"his hand|another named or unnamed hand|typewriter|print", "element":"unique short id", "kind":"text|display|diagram|drawing|margin note|insertion|deletion", "position":"...", "first_words_or_objects":"...", "transcribed":"yes"}],
 "notes": [{"id":"s003-note01", "text":"English description of what the page states/calculates/asks or dates/counts, source words for doubts, and any math-triggered reading decision.", "basis":"specific page locus; distinguish observation, inference, proof check"}],
 "notation": [{"sign":"...", "latex":"...", "locus":"...", "evidence":"...", "alternatives":"..."}],
 "abbreviations": [{"form":"...", "expansion":"tentative expansion, here only"}],
 "check_events": [{"statement_id":"...", "date":"UTC date/time", "who":"model, effort, this reader run", "type":"actual permitted check event type", "outcome":"exactly what was checked; transcription alone is NOT proof checking"}],
 "crops": [{"path":"relative to work root", "source":"...", "bbox":[...], "transforms":"...", "locus":"..."}],
 "brief_feedback": "any ambiguity/omission in brief that affected the reading, else none"
}

Allowed kind: misread word; misread symbol or index; omission; text not on the page; deletion state (struck given live or live given struck); insertion or placement; abbreviation expanded or spelling modernised; readable ink left as \\ill{}; drawing or diagram; other.
Allowed check event type: targeted proof check; independent re-proof; computation or formal certificate; used and rechecked in this run; carried as background without fault found; refuted, with the refined statement's id. Never label mere transcription as a mathematical check. If no mathematical checking occurs, state that and leave check_events empty; main reader will record the epistemic status of consolidated notes. Inventory must include every meaningful text block/display/correction/marginal drawing, not only differences. All actual differences from C or H must be in changes, including resolved doubt marks; C doubt retentions are also recorded in c_doubts.

## Clarifications after scan 003 (v002)
- Log the real UTC start time before the first source view; do not reconstruct an exact start time later.
- For EVERY reported discrepancy, provide a tight whole-source bbox even when the halves settle it and you do not crop it. Include the identifying word/row label along with a pointer or grouping mark, so the main reader can locate its attachment from one crop.
- Crop paths in report.json are relative to SP45_CW_37_work, not relative to your reader directory. JPEG at quality 95–96 is suitable; do not keep duplicate format copies. Do not spend further image views on a settled place.
- Distinguish a visible character from an uncertain underprint and from uncertain strike order. Heavy/doubled type alone is not evidence of a different earlier character. Use only alternatives the actual strokes support; do not invent chronological certainty.
- H may correctly describe a drawing in an editorial note without drawing it. Record that as drawing or diagram when our transcription actually reproduces it, while acknowledging that the verbal description may be accurate. Differences in doubt state are recorded as such, not automatically called errors.
- Keep the report precise and compact: full source reading in reading.tex, all loci and evidence in report.json, without repeating the entire page in narrative. Complete coverage remains mandatory. All source margins and numbers must still be inspected even on a short letter.

## Scope clarification after scan 004 (v003)
- Only scan 003, the first page of the complete package, starts with \cotefile{37}. Every later reading.tex starts with its \scanpage{N}; do not add another cotefile merely because you are a fresh reader. This is a fragment-scope rule, not a reading decision.

## Margin placement clarification after scan 009 (v004)
- The supplied margin macro uses the document default (right-hand margin). If the source has a LEFT marginal note or drawing, use standard LaTeX \reversemarginpar before it and \normalmarginpar afterward. Keep a grouping bar/pointer with its words when the source places them together; a separate centred figure changes the source placement. Record actual relative geometry, not merely the words.
