# Reader brief v011 — first used on scan 030

You are one of THREE independent readers of ONE page in a diplomatic second pass. Do not read another reader's files or ask another reader; do not open other pages' images, witnesses, reports, or source notes. Your task ends with this page. The main reader will adjudicate all differences. Read slowly and completely, from the INK, with both draft witnesses beside it. No OCR, text recognition, external research, published text, or mathematical reconstruction.

Inputs: the assigned packet's metadata.json, C.tex, H.tex, C_prior_questions.md, C_marked_loci.md, C_inventory.json; this brief, conventions.md, PREAMBLE.tex; and the supplied notation snapshot. Only metadata.json gives this page's image paths. H may be description only: then it is not a textual witness; do not generate H collation rows for that page.

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
 "c_doubts": [{"locus":"...", "c":"...", "decision":"resolved|retained", "reading":"...", "evidence":"...", "crop":"...", "c_mark_ids":["C001"]}],
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

## Collation equivalence clarification after scan 013 (v005)
- When H explicitly marks a clipped initial as supplied and our tentative reading gives the SAME letters with unsure, do not count a change solely for that equivalent cautious presentation. Record the clipping in C doubt outcomes. Distinguish this from H supplying an entire absent word/suffix that our reading leaves unreadable, adding unsupported punctuation, omitting a correction, or giving different letter alternatives; those are substantive differences. State which case applies.

## Prose punctuation encoding clarification after scan 015 (v006)
- A single prose dash encoded as - versus --, or the same three dots encoded literally versus \ldots, is not by itself a new reading. Preserve the actual source form in our text, but do not count H typography/code alone as a collation difference. Count genuinely different visible punctuation marks (for example guillemets versus paired upright quote strokes), extra/absent marks, or an ink-supported difference in symbol identity. Explain any borderline classification.

## Explicit C-mark coverage after scan 018 (v007)
- Also read your packet’s C_marked_loci.md. This is a mechanical list of every unsure/illegible macro in C.tex, supplementing the earlier C questions, which can be incomplete. It supplies no reading. Every numbered C mark needs an explicit resolution or retention.
- In each c_doubts entry add `"c_mark_ids": ["C001", "C002"]` for the mark(s) that the outcome covers. One physical locus may cover several IDs or a duplicate prior question. Together the entries must cover every ID in C_marked_loci.md. Unmarked C questions still receive outcomes, with an empty ID list. No extra crop is needed merely to populate these IDs.

## Visible state versus emphasis after scan 018 (v007)
- A visible underline is a source state, not merely generic emphasis. H's emph is not equivalent to uline unless the supplied H style actually makes it an underline. The supplied H style uses ulem with normalem, so ordinary emph is italic. Record that state difference when the source is visibly underlined; do not extend prose-dash equivalence to it. Likewise retain the literal capital in Lim even if H uses a conventional lower-case limit operator.
- If H explicitly declares that a type of mark (such as typewriter superpositions) is outside its scope, record the actual difference but acknowledge that declaration. Do not describe a declared scope omission as a hidden or unmarked uncertainty.

## H uncertainty flags after scan 023 (v008)
- marked_in_H is true only when H explicitly marks doubt, illegibility, or supplied doubtful text at that locus (including an editorial note expressly saying illisible). An ordinary note describing a correction, insertion, superposition or drawing is not a doubt mark. The add/struck state macros alone are not doubt marks. This flag is independent of whether H accurately acknowledges the mark.

## Graphic cancellation after scan 023 (v008)
- A cancelled block’s enclosing border and long oblique strokes are source graphics. Reproduce their actual geometry in TikZ around the complete text; a deleted macro or a comment describing the frame does not reproduce those marks. Short ordinary insertion calls may be encoded by the insertion’s correct attachment; nested call lines whose geometry distinguishes punctuation must be drawn. Inventory should classify an ordinary insertion leader as an insertion, not claim an undrawn standalone drawing.

## Precise uncertainty scope and validation after scan 024 (v009)
- Apply marked_in_H to the exact differing words or marks. An illegibility mark on a neighbouring cancellation does not mark doubt on a separately written reference accent or an added live abbreviation. If H explicitly locates its doubtful reading in a physical oval, retain that physical-locus correspondence when reporting relocation.
- The installed TeX engines have no LaTeX formats or package tree, and this limitation is already documented centrally. Do not repeat optional compile attempts. Validate fragment scope, balanced groups/environments, report fields and paths without reopening source images; main handles aggregate validation.


## Physical order and local ink checks after scan 025 (v010)
- Interleave inventory entries in physical top-to-bottom reading order. Do not group all deletions before all insertions. When a margin oval is alongside the middle of a tall graphic, preserve that vertical relationship, preferably within the same TikZ coordinate system; anchoring it before or after the whole graphic moves it.
- Rotate slanted marginal text upright in its one crop. Plan that transformation before viewing; do not make a second crop merely to rotate a settled locus.
- Check every repeated subscript and accent locally. On scan 025 all three readers missed a visible acute on the final et, although other occurrences genuinely lacked it. A notation-table pattern never settles the next occurrence.
- In report reading fields use the exact valid LaTeX of reading.tex. A prime is an apostrophe or superscript, not a bare mathematical prime command after the baseline letter. Confirm that every difference in the full reading has a change row; one reader on scan 025 omitted one otherwise correctly read subscript discrepancy.


## Orientation derivatives and punctuation after scan 027 (v011)
- If a source is upside-down, rotate each whole/half before its single view. Put these full-view derivatives outside SP45_CW_37_work, in the workspace oriented_views/scanNNN/reader directory; they are supplied-source derivatives and must not enter deliverable ZIPs. Record the transformation and original-source bbox mapping. Keep only the tight evidence crops in your reader output.
- Inspect whether an added punctuation mark is handwritten. On scan 027, the main comma crop showed a long curved handwritten comma that two readers included as ordinary typed punctuation and one omitted. Encode its hand state as well as its presence.
