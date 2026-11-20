# SP38_CW_75 — workflow

Each scan was assigned to three fresh subagents using fork_turns=none, with no access in their instructions to other readers or previous page images. Pages were assigned sequentially, after the previous page was adjudicated and committed. The main reader retained returns and viewed adjudication crops. All reader returns, crop metadata, decisions, brief versions, and scripts are included. No OCR or external research was used.

Runtime model label: GPT-6 Astra Pro; reader effort inherited and not independently exposed by the tool. No unsupported effort level is asserted.

## Brief versions

- Scan 002: brief_v01_scan002.md — Initial a–d brief: independent page-only readers, full image and halves once, unresolved crops, complete diplomatic record.
- Scan 003: brief_v02_scan003.md — Cover: R3 retained a possible point before p, while R1/R2 omitted it; added mark-versus-surface guidance. R1 cropped labels the other readers settled from halves; clarified no unnecessary confirmation crops and reporting schema.
- Scan 004: brief_v03_scan004.md — Scan 003 disagreements: cancellation beneath an insertion; leading cursive s versus comma; espace/esp. and de/des; display placement. Also fixed false foliation collation rows and standardized doubt-update flags and inventory categories.
- Scan 004: brief_v04_scan004.md — Added page-specific supplied H TikZ drawing files to packets before scan 004 adjudication. Readers were notified individually; a prose marker alone must not be counted as an absent drawing when its redraw is supplied.
- Scan 005: brief_v05_scan005.md — Scan 004 exposed H’s declared bold/double-stroke font encoding, a possible colon versus surface spots, dummy-index disagreement, and drawing patches versus mathematical interpretation.
- Scan 006: brief_v06_scan006.md — Scan005 readers differed in the placement of the possible question mark, the circled prefix, and shared-baseline layout; left-margin selection made explicit.
- Scan 007: brief_v07_scan007.md — Scan006: interlinear inverse sentence was missed as insertion by two readers; looped Aut superscript resisted expected plus. Clarified H confidence-only exclusion, image-response retries and stopping after report checks without TeX compilation.
- Scan 008: brief_v08_scan008.md — Scan007 report labels conflated new doubts with retained C doubts; map and inverse-pair disagreements reinforced shape-first judgment, and an unmatched opening parenthesis must remain uncompleted.
- Scan 009: brief_v09_scan009.md — Scan008: comments did not implement left tags, all readers detached adjacent two-line brackets and inherited a paragraph boundary; quotient alphabets and small detached marks required local checks. Clarified mathematical versus visual verification.
- Scan 010: brief_v10_scan010.md — Scan009 differences concerned baseline product points, rule extent, adjacent diagram wording and actual marginal slant; clarified their geometrical preservation.
- Scan 011: brief_v11_scan011.md — Scan010: slanted equality, left-start alignment, a whole-label lower R, detached marks, and insertion callouts required explicit geometry; original-doubt mapping and report/text synchronization clarified.
- Scan 012: brief_v12_scan012.md — After scan011: curved-label side and shaft intersection; actual raised insertion geometry; nested-doubt counting; conservative archive-hand attribution.
- Scan 013: brief_v13_scan013.md — After scan012: require tikz-cd for commutative diagrams, restore margin selection, distinguish readable word from uncertain cancellation state, inspect repeated parentheses independently, and return plain final paths without interim links.
- Scan 014: brief_v14_scan014.md — Distinguish actual witness punctuation, prose descriptions versus drawn signs, and spacing refinements from structural placement changes.
- Scan 015: brief_v15_scan015.md — After scan014: distinguish f exits from opening parentheses, check local accents, separate deletion state from letter reading, and keep stepped dividers and two-row correspondence geometry.
- Scan 016: brief_v16_scan016.md — After scan015: distinguish predecessor and live-correction certainty; preserve open boundary ends and comma placement; inspect local accents and short underlines; keep baseline continuation beneath insertion lead.

## Crop counts

R1/R2/R3 counts are the crops each reader made and inspected. Main-created counts only new adjudication crops; main-inspected also includes reused reader crops. Original supplied page/halves are excluded. A shared crop may settle several neighboring details in one locus.

| Scan | R1 | R2 | R3 | Main-created | Main-inspected |
| --- | ---: | ---: | ---: | ---: | ---: |
| 2 | 3 | 2 | 2 | 0 | 2 |
| 3 | 12 | 14 | 16 | 10 | 22 |
| 4 | 20 | 19 | 19 | 7 | 27 |
| 5 | 16 | 16 | 18 | 14 | 33 |
| 6 | 24 | 22 | 21 | 11 | 35 |
| 7 | 15 | 10 | 15 | 9 | 25 |
| 8 | 22 | 23 | 27 | 18 | 44 |
| 9 | 14 | 11 | 14 | 5 | 21 |
| 10 | 16 | 18 | 18 | 8 | 27 |
| 11 | 11 | 13 | 13 | 10 | 24 |
| 12 | 17 | 18 | 21 | 7 | 27 |
| 13 | 13 | 16 | 15 | 9 | 25 |
| 14 | 19 | 16 | 17 | 6 | 28 |
| 15 | 20 | 21 | 22 | 9 | 32 |

## First brief

# Independent reader brief v01 — first used scan 002

You are one of three independent readers of ONE page. Do not inspect any other reader's files, communicate with other readers, or view another page. Read only your packet, the three images it names, the conventions, and the supplied notation snapshot. Main reader adjudicates your return. Do not delegate.

## Inputs and authority

The packet directory contains `metadata.json` (image paths, scan and witness mapping), `C.tex`, `H.tex`, `C_context.md` (earlier doubts/notes for this page), and `S.json` (sweep statements, if any). `briefs/conventions.md` gives the exact diplomatic conventions; `PREAMBLE.tex` defines allowed macros. Read both. Current task overrides the older prompt's workflow: use the whole image and TWO supplied halves, one viewing of each, then necessary tight crops. No OCR, recognition library, PDF text layer, web, published text, or expected mathematical reading. Ink alone decides. Witness H's macro syntax alone is not a difference. An H editorial heading or note is not itself manuscript text; inspect ink for it.

## Workflow a–d

a. View the whole page once for layout: every block, display, drawing, diagram, margin, deletion, insertion and foliation. Record dimensions so later boxes use original whole-image coordinates.

b. View each full-resolution half once, in order. Read every line against C and H, word by word and symbol by symbol. Check spelling and accents, endings, punctuation, abbreviation, alphabets, indices, exponents, inequalities, primes versus exclamation marks, underlines, brackets, insertions and deletion state. Agreement of witnesses is not evidence. Do not enlarge or reopen a whole half. Anything settled by the halves needs no crop in your own reading.

c. List what remains open, including C's doubts and consequential small symbols, slanted notes, crowded or crossed text. Make ONE tight crop per unresolved place with a line of context; enlarge to a few thousand pixels with LANCZOS, autocontrast, sharpen when faint, and rotate if slanted. You may use Pillow for these explicitly requested image operations. Store the crop and its original bounding box and rotation. Inspect it visually with view_image. Do not crop a decided place again. Keep distinct loci distinct, without multiplying crops of one locus. If no crop is needed say so. Mark uncertainty honestly, even if all witnesses propose a plausible reading. Never leave ink out for being uncertain.

d. Return a complete page reading using the exact C conventions, with every diagram/drawing in TikZ/tikz-cd. Start from C's page if helpful but visually verify every item, not only disagreements. Record EVERY substantive difference from C or H, EVERY C doubt resolved or retained, and every S row confirmed or overturned. Follow the mathematics enough to catch malformed formulas, contradictory signs, indices or arrows; re-examine ink and preserve written errors. Give brief mathematical notes, and distinguish reading a claim from actually checking it.

## Output (write only inside your assigned reader directory)

Write `reading.tex`, `report.json`, and optional `report.md`. JSON fields:

* `scan`, `reader`, `start_utc`, `end_utc`, `images_viewed` (three paths), `reading_file`, `crop_count`.
* `findings`: array of `{id,place,c,h,final,evidence,confidence,kind,marked_in_H,diff_c,diff_h,bbox,crop,doubt_action,s_id,math_note}`. `bbox` uses original whole-image pixels [left,top,right,bottom], even if the evidence is a half. `crop` is a relative path within out, or empty for half-settled. `diff_c/diff_h` are booleans. `doubt_action` is resolve/retain/empty. Confidence high/medium/low. `kind` is one of: misread word; misread symbol or index; omission; text not on the page; deletion state (struck given live or live given struck); insertion or placement; abbreviation expanded or spelling modernised; readable ink left as `\\ill{}`; drawing or diagram; other. Give actual witness text, not just 'wrong'. Do not count absent H page as omission.
* `inventory`: array of `{sheet_kind,hand,element,kind,position,first_words_or_objects,transcribed}`. Use kind text/display/diagram/drawing/margin note/insertion/deletion; complete top-to-bottom, including both large blocks and their correction elements. `transcribed` is yes. Archive foliation is a comment, not an mspage or independent live text.
* `notation`: array of `{sign,reading,ink,place}` for recurring glyphs observed; `abbreviations`: array of `{written,expansion}` (expansions in notes only).
* `notes`: brief English page content, titles/dates/counts, the author's own doubt words, and mathematics-triggered reading decisions. `checks`: actual mathematical checks, if performed, each with statement, event type, reasoning and outcome. Leave empty if merely reading. `unresolved`: remaining actual doubts with place, reading, alternatives and confidence.

Retain original paragraphing, don't normalize shorthand, don't turn all underlines into headings. Each reader may have different crop needs: report yours honestly. Don't guess what the other readers will say. Final message: saved paths, completion, crop count, and a short list of your most consequential findings.


## Last brief

# Independent reader brief v16 — first used scan 016

You are one of three independent readers of ONE page. Do not inspect any other reader's files, communicate with other readers, or view another page. Read only your packet, the three images it names, the conventions, and the supplied notation snapshot. Main reader adjudicates your return. Do not delegate.

## Inputs and authority

The packet directory contains `metadata.json` (image paths, scan and witness mapping), `C.tex`, `H.tex`, `C_context.md` (earlier doubts/notes for this page), and `S.json` (sweep statements, if any). `briefs/conventions.md` gives the exact diplomatic conventions; `PREAMBLE.tex` defines allowed macros. Read both. Current task overrides the older prompt's workflow: use the whole image and TWO supplied halves, one viewing of each, then necessary tight crops. No OCR, recognition library, PDF text layer, web, published text, or expected mathematical reading. Ink alone decides. Witness H's macro syntax alone is not a difference. An H editorial heading or note is not itself manuscript text; inspect ink for it.

## Workflow a–d

a. View the whole page once for layout: every block, display, drawing, diagram, margin, deletion, insertion and foliation. Record dimensions so later boxes use original whole-image coordinates.

b. View each full-resolution half once, in order. Read every line against C and H, word by word and symbol by symbol. Check spelling and accents, endings, punctuation, abbreviation, alphabets, indices, exponents, inequalities, primes versus exclamation marks, underlines, brackets, insertions and deletion state. Agreement of witnesses is not evidence. Do not enlarge or reopen a whole half. Anything settled by the halves needs no crop in your own reading.

c. List what remains open, including C's doubts and consequential small symbols, slanted notes, crowded or crossed text. Make ONE tight crop per unresolved place with a line of context; enlarge to a few thousand pixels with LANCZOS, autocontrast, sharpen when faint, and rotate if slanted. You may use Pillow for these explicitly requested image operations. Store the crop and its original bounding box and rotation. Inspect it visually with view_image. Do not crop a decided place again. Keep distinct loci distinct, without multiplying crops of one locus. If no crop is needed say so. Mark uncertainty honestly, even if all witnesses propose a plausible reading. Never leave ink out for being uncertain.

d. Return a complete page reading using the exact C conventions, with every diagram/drawing in TikZ/tikz-cd. Start from C's page if helpful but visually verify every item, not only disagreements. Record EVERY substantive difference from C or H, EVERY C doubt resolved or retained, and every S row confirmed or overturned. Follow the mathematics enough to catch malformed formulas, contradictory signs, indices or arrows; re-examine ink and preserve written errors. Give brief mathematical notes, and distinguish reading a claim from actually checking it.

## Output (write only inside your assigned reader directory)

Write `reading.tex`, `report.json`, and optional `report.md`. JSON fields:

* `scan`, `reader`, `start_utc`, `end_utc`, `images_viewed` (three paths), `reading_file`, `crop_count`.
* `findings`: array of `{id,place,c,h,final,evidence,confidence,kind,marked_in_H,diff_c,diff_h,bbox,crop,doubt_action,s_id,math_note}`. `bbox` uses original whole-image pixels [left,top,right,bottom], even if the evidence is a half. `crop` is a relative path within out, or empty for half-settled. `diff_c/diff_h` are booleans. `doubt_action` is resolve/retain/empty. Confidence high/medium/low. `kind` is one of: misread word; misread symbol or index; omission; text not on the page; deletion state (struck given live or live given struck); insertion or placement; abbreviation expanded or spelling modernised; readable ink left as `\\ill{}`; drawing or diagram; other. Give actual witness text, not just 'wrong'. Do not count absent H page as omission.
* `inventory`: array of `{sheet_kind,hand,element,kind,position,first_words_or_objects,transcribed}`. Use kind text/display/diagram/drawing/margin note/insertion/deletion; complete top-to-bottom, including both large blocks and their correction elements. `transcribed` is yes. Archive foliation is a comment, not an mspage or independent live text.
* `notation`: array of `{sign,reading,ink,place}` for recurring glyphs observed; `abbreviations`: array of `{written,expansion}` (expansions in notes only).
* `notes`: brief English page content, titles/dates/counts, the author's own doubt words, and mathematics-triggered reading decisions. `checks`: actual mathematical checks, if performed, each with statement, event type, reasoning and outcome. Leave empty if merely reading. `unresolved`: remaining actual doubts with place, reading, alternatives and confidence.

Retain original paragraphing, don't normalize shorthand, don't turn all underlines into headings. Each reader may have different crop needs: report yours honestly. Don't guess what the other readers will say. Final message: saved paths, completion, crop count, and a short list of your most consequential findings.

## Refinements after scan 002

* Sideways writing may need rotation for an open reading, but do not crop an already legible label only to confirm it again. Record why each crop was needed. The cover course-label crop was unnecessary for two readers.
* A small detached point may be punctuation, pen debris or a surface spot. Compare its placement, colour and shape with nearby writing; report uncertainty if that cannot be settled. Do not invent punctuation from every dark pixel, and do not dismiss a visible point merely because grammar disfavors it. The cover count produced the first disagreement.
* `findings` should contain substantive witness differences, every C doubt disposition, S decisions and new doubts. Put routine agreements in coverage/inventory rather than making a findings row for every agreed word. Use strings for unresolved alternatives and notes.
* Findings need a usable original-image bbox even when the half settled the reading, so the main reader can make an adjudication crop when needed. State whether an exact glyph difference is semantic or merely equivalent LaTeX notation.

## Refinements after scan 003

* A long stroke crossing a short word beneath an interlinear replacement needs a deletion-state crop even if the letters themselves are readable. Scan 003 produced live que versus canceled que; the main crop shows the crossing.
* Do not detach the first cursive s of a word such as sur as a comma unless an additional punctuation stroke exists. Keep a doubt when the crop cannot distinguish them.
* Preserve actual side-by-side display layout and wrapped ends, not just formula content. Scan 003 comparisons were on one baseline; only the last phrase wrapped.
* H’s page markers are editorial archive identifiers. Their numerical offset from scan numbers, or their representation as comments in C, is not a collation difference. H uncertainty removed with the same reading is not itself a substantive H difference.
* Set diff_c=true for an added, removed or reordered C doubt mark as well as for wording, state or placement changes; the final counts will identify these as editorial updates rather than all calling them errors. Do not count macro-only H differences.
* Inventory sheet_kind must be one of text, reused_typed, typescript, letter, list, cancelled_draft, cover. Use his hand for the course manuscript, unnamed hand where identity is uncertain, typewriter or print as appropriate. Start with cotefile only on scan 002.
* When compressing spellings such as espace/esp. or de/des, list the alternatives the ink allows; do not resolve a horizontal exit stroke from grammar alone.

## Witness H drawing supplement — first used during scan 004

The page packet may also contain H_drawings/. These are H's supplied TikZ redraws for this very page, identified by their header’s PDF-page number. Read those files as part of witness H. Do not count H's prose drawing marker as a missing drawing when its supplied redraw exists; compare that actual geometry, dots, labels and topology with the ink. Do not count stylistic coordinate/scaling differences. Do not reopen the whole page/halves already viewed: use your recorded visual reading, or one tight crop for any genuinely new open drawing locus.

## Refinements after scan 004

- H’s batch header declares that double-stroke number fields use `\mathbf{Z}`, `\mathbf{R}`, `\mathbf{C}`, `\mathbf{F}`, `\mathbf{P}`. The corresponding C `\mathbb` is not a substantive witness difference. Inspect the ink alphabet, but do not count the declared macro encoding as error.
- Preserve weak or extra signs in a formula even when their syntax is awkward. A consistency calculation may identify a reading risk but never decides a dummy index by expected notation.
- Adjacent detached dark points can be punctuation or surface spots: compare their height, colour and form. Mark doubt when not settled.
- Keep the graph redraw’s visible ink patches and detached strokes, without declaring them graph vertices or edges unless the page does.
- Keep report evidence concise, but complete: each actual witness difference, every C doubt disposition, every S row. State a short ink reason and exact usable bbox.

## Refinements after scan 005

- If a possible question mark stands over a particular letter, preserve that exact placement in the alternative; do not move it to the end of the word. State whether the mark is secure or may be part of the letter.
- A margin macro alone does not select the left margin. Use standard LaTeX margin selection when the drawing or reference arrow is visibly on the left.
- Inspect enclosures and insertion connectors as well as their text. Distinguish a circled prefix from ordinary parentheses and preserve an actual circle in TikZ when it is a visible independent mark.
- Keep tight-crop output batches small enough to be displayed without truncation. A failed image emission is not a visual inspection; retry that file, without creating a second crop.

## Refinements after scan 006

- When a reading differs only by confidence while the same primary wording remains, do not count an H collation difference. A new, removed or reordered C doubt still counts as a C editorial update.
- A short interlinear sentence can be an insertion even without an arrow: inspect its size and position relative to the surrounding full-sized lines. Preserve the entire sentence and its actual order. If insertion state remains unresolved, crop enough neighboring line context to decide it.
- Superscripts may be letterlike even where a familiar group symbol is expected. Keep the observed alternatives; a proof check cannot supply the glyph.
- Your task ends after the complete reading and report have been checked for completeness and obvious brace/environment balance. No LaTeX compilation is required; do not install or rebuild a TeX runtime.
- If a tool image response fails or is truncated, retry that existing crop once output is available; do not count it viewed until actually displayed. After a runtime interruption, resume from your last recorded visual step, without reopening the whole or either half.

## Refinements after scan 007

- Distinguish an original C doubt from a new doubt you add. Use doubt_action=retain/resolve only for a doubt already present in C; leave it empty for a new doubt and explain the addition. Every original C doubt still needs an explicit disposition.
- When a mathematical base differs in height or descender from a nearby occurrence, compare the visible shapes and preserve the alternatives. An expected inverse or repeated variable cannot supply a missing descender.
- Preserve unmatched written parentheses or other manuscript irregularities, without completing them. Record them briefly in the notes.

## Refinements after scan 008

- A comment about a left display tag does not position it. Use existing standard LaTeX/amsmath facilities to reproduce the actual side. Preserve small two-line brackets beside prose when written there; do not detach them simply because C used a display.
- Read paragraph boundaries from indentation and spacing. Ordinary manuscript line endings are joined; do not inherit a C paragraph break without checking it.
- Include detached hooks, loops and separate divider strokes. Keep their physical placement and uncertain purpose; do not invent an intended mathematical meaning.
- Inspect each quotient’s alphabet independently. A visibly single-stroked Z can differ from a later doubled Z on the same page; the notation table must record the local variation.
- Separate actual mathematical checks from visual bracket or transcription verification. Only the former belong in mathematical checks.

## Refinements after scan 009

- Preserve the height of a written multiplication point when it is visibly on the baseline; equivalent mathematical notation can still differ in placement. Do not count declared macro equivalents as wording errors.
- A side rule may begin beside a continuation rather than the opening line of its paragraph. Record both endpoints and keep the display alignment.
- Reproduce a visibly slanted marginal note in its geometry, rather than merely commenting that it is slanted. Keep adjacent instruction words on the diagram baseline where written.
- Record a faint detached mark without inventing its purpose when writing versus surface trace is unresolved. The first-occurrence uncertainty convention applies to recurring mathematical glyphs, not automatically to different compressed words.

## Refinements after scan 010

- Record the UTC start before reading. If a timestamp was not captured, say so rather than inventing it. On scans after 002, do not copy the repeated cotefile marker from C.
- Number the original C doubts in their order (C01, C02, ...), or provide an explicit mapping. Keep the final reading.tex, findings and unresolved list synchronized after your self-check; a resolved doubt must not remain accidentally in one of them.
- A drawn equal sign can be slanted and displaced from a vertical connector. Two display lines may align at their left starts rather than their relation signs. A subscript label can occupy a separate line below the whole expression. Read these positions from ink.
- Raised clauses may carry visible curved callout strokes. Preserve the clauses with inserted and reproduce their actual raised placement and connectors in TikZ; the macro alone does not draw the connector. Keep following baseline text in place.
- Report prose apostrophes as apostrophes, not mathematical prime commands. Distinguish literal lettering from a formula's prime marks.
- Definite detached strokes can be drawn without assigning them a function. Doubt about a stroke's purpose alone is not a doubtful minus sign; doubt about whether a faint point is writing should be stated separately.

## Refinements after scan 011

- Diagram labels may sit inside a curved return or intersect its shaft. Reproduce the observed side; default tikz-cd label placement is not automatically correct. Preserve a visible small offset between successive display starts.
- Ensure the LaTeX geometry agrees with your report: an insertion described as above its canceled predecessor must actually be placed above it, not simply raised after it. No new crop is needed if the half or existing crop already settled that geometry.
- In nested C uncertainties, explicitly map the outer and inner doubts, but avoid counting the same nested letter change twice as separate changes to both the whole expression and its argument.
- For a foliation or other archive addition, use unnamed hand unless the supplied evidence identifies its writer. A different ink or pencil alone does not name a person.

## Refinements after scan 012

- Keep commutative diagrams in tikz-cd. It may be placed in an outer TikZ picture for adjacent text or special geometry; generic TikZ arrows alone should not replace the required diagram environment.
- After selecting the left margin for a note, restore normal margin selection before a later right-margin annotation. Match the described placement in the actual code.
- A word may be readable while its deletion state remains doubtful. Keep those alternatives explicit; do not treat heavier cursive joins alone as a definite cancellation.
- Check each occurrence of a parenthesis independently. A missing opening curve must not be supplied merely because a neighboring occurrence or the mathematical grammar suggests it.
- Return final file paths as plain text, with no clickable links. Only the main agent will offer the single final ZIP download.

## Refinements after scan 013

- Quote the actual C/H token span before counting punctuation. A period outside inline math still belongs to the formula's sentence; do not report it absent merely because it lies outside the dollar delimiters.
- If H describes visible signs in a prose note but omits them from its actual display, compare that drawn geometry separately from the note's proposed reading. Declared alphabet macro equivalents remain excluded.
- Different spacing choices within the same correct structural relation need not count as collation errors. Preserve observed broad gaps while distinguishing them from moved blocks, wrong baselines or missing strokes.


## Refinements after scan 014

- Separate the exit of the final f from a supposed opening parenthesis. Compare the actual independent strokes; a formula must not acquire a missing delimiter from mathematical syntax.
- Check accents independently from a compressed word ending. An expanded word and a restored accent are distinct editorial choices; preserve both alternatives where the ink leaves them open.
- A cancellation crossing et may coincide with the t crossbar. Report readable letters and deletion state separately, without letting grammar decide whether the word was struck.
- Keep a stepped divider beside the annotation it bends around. Preserve meaningful two-row correspondence layout while joining ordinary prose line wraps.


## Refinements after scan 015

- The certainty of an overwritten predecessor and the certainty of its live correction are independent. If their shared contour leaves one uncertain, mark that object separately rather than letting the expected formula decide it.
- Preserve the visible open ends of an annotation boundary, especially at the sheet edge. Keep a separate comma in its actual relation to the text and boundary instead of placing it after the whole drawing.
- Inspect accents and short underlines independently from the word. A local ending need not inherit the spelling or confidence of another occurrence. Keep baseline text below an interlinear connector beneath that connector in the actual TikZ layout.


## What worked and what did not

Scan 002: independent readers agreed on the difficult title accent but one noticed a possible dot in the count. Main retained that uncertainty after viewing its crop. The full-resolution halves settled C₄/DEA for two readers; subsequent briefs discourage a second confirmation crop once a half settles a locus.

Scan 003: the three independent returns caught a state error in a confident C reading (que under de plus), yet disagreed on its status. The main crop settled cancellation. Their alternatives for crowded formula marks usefully exposed uncertainty that a majority vote would hide. A readable abbreviation and a full word could not be safely distinguished in one torsor condition. H editorial page markers initially appeared as false collation differences; these were excluded and the brief corrected. Main inspection used 12 reader crops plus 10 new crops, each once.

During scan 004 packet preparation, H drawing headers were used to match all five supplied redraws to scans 004, 005, 006, 008 and 016. They were added to the relevant packets and all three active scan-004 readers were notified before completion. This avoids falsely treating H prose drawing markers as missing drawings.

- Scan 004: reading H’s separate supplied drawing prevents false omissions. Its double-stroke font declaration likewise excludes a macro-only difference. Three readers disagreed about a tiny colon, index and noun ending; main crops supplied explicit decisions or retained doubt. There is no value in forcing agreement where the ink stays compressed.

Scan005: all three readings were useful for a single-letter deletion, an internal comma and a compressed insertion. Majority agreement did not resolve these. A failed seven-image emission was retried in smaller batches without new crops; only actual inspections are counted. The mathematical uniqueness check was explicitly conditional and did not supply wording.

During scan006, an exec runtime replacement interrupted the readers while showing crop outputs. Live-agent status alone did not reveal the stalled turns. A follow-up resumed each same-page context; each reader explicitly reported that the page and halves were not reopened and existing crops, not new crops, were used for interrupted displays. Resumptions are logged in their own work records. No new independent reader or completed reading is claimed for a resumed context.

- Scan 006: all three complete readings were compared; small context crops settled placement that isolated word crops could not. A looped superscript and several compressed endings remained explicitly uncertain. The runtime interruption delayed readers; resuming their existing contexts preserved independence and avoided reopening full images. Optional TeX compilation was stopped because it was outside the reading task and no formats were installed.

## After scan 007

The readers disagreed on resolving flat short words, a terminal point, the map letter, a second mathematical base and an ellipsis-like ending. The main comparison retained uncertainty where the crops did not settle it and preferred an s-shaped base despite the expected g. Three reader returns made these disagreements visible. The original C doubts must be distinguished from new doubts: several R1 entries called newly added doubts retained. Brief v08 clarifies that record field. A truncated three-image emission was retried using the existing files in smaller batches, without recropping or counting failed output as visual inspection. All 25 distinct main crops were ultimately displayed. No whole page or half was opened by the main reader.

Scan 008: the three returns differed in tte/toute, origin undertext, the margin separator, missing punctuation, quotient alphabets and tiny hook/loop marks. A comment saying “label at left” did not actually put the tag at left; the main reader corrected the typesetting. All returns detached adjacent two-line brackets and kept C’s paragraph break at an ordinary line boundary; main crops corrected those placements. A new R3 loop was noticed before its final return; the collected hash record distinguishes initial and complete returns. Single-image emissions prevented further truncation. Bracket completeness is a transcription check, not a mathematical proof event.

Scan009: Three returns used 14/11/14 crops; main reused 16 and created 5. Existing crops covered all C doubts, including ones individual readers resolved. Main corrected the corollary rule extent and retained slanted-margin geometry. Low points, overwritten annotation flanks and canceled digits required separate ink decisions. All 23 prior C doubts have dispositions; the sweep equivalence and au plus were confirmed.

Scan010: all three readers completed, but reports took longer than the initial text files. Main waited for complete final returns before image adjudication. Text/report synchronization found a terminal-period omission during readers’ final checks. The R3 geometry findings corrected inherited alignment, while R1 alone recorded an upper gap point. Main used 19 existing reader crops and eight new crops, without viewing the whole or halves. Raised insertion connectors required explicit drawing in the consolidated text.

- Scan 011: all full returns were compared before main crop adjudication. Main used 14 existing reader crops and 10 new crops (including a partial foliation crop solely for disputed hand attribution). Word confidence, canceled underforms, exact label sides and staggered line starts produced differences. Actual TikZ placement must agree with the report: a state macro alone did not reproduce a raised insertion. A foliation numeral cannot establish the identity of its writer. No TeX compilation was performed.

Scan 012: all three final returns were compared before main image inspection. Twenty reader crops were reused and seven new crops covered half-settled witness differences and display geometry. Twenty-one C doubts are explicitly mapped (nine resolved, twelve retained). Word legibility and cancellation state were separated for elle; both independent lower parenthesis occurrences were inspected. A generic TikZ square was replaced with the reader’s matching tikz-cd implementation, and left/right margin selection was checked. H’s broad missing clause and its local accent doubt are not counted twice.

Scan 013: compare the actual witness tokens before counting punctuation. R2's claimed omitted final period was already present in both witnesses; only placement changes were retained. A prose drawing note can acknowledge a sign while leaving its geometry absent from the transcription. Separate that omission from confidence-only disagreement about the sign. A single terminal pen spur is insufficient to choose confidently between a headless shaft and an abbreviated arrow.

Scan 014: all final complete reports were compared before main image review. Main reused 22 crops and made six for missing loci or geometry. R1 counted the last f as an opening parenthesis; the crop supports R2/R3's missing delimiter. Separate accent, word-ending and cancellation-state alternatives prevented silently normalizing compressed text. The two correspondence continuations and the stepped divider needed geometry checks beyond their lexical transcription. SA01-K75-02 was confirmed, with V retained. Algebraic checks upheld the exceptional S5 identity rather than repeating an earlier speculative slip note.


Scan 015: all three complete final returns were compared before the main saw any image. The apparent closed bubble in one return had visibly open boundaries and a separate comma. R2 alone recorded the short underline beneath repeated régulière; R3 supplied the cancellation hook and the distinction between a recoverable old P and its insecure live S correction. Existing crops settled all C doubts; nine new crops covered previously half-settled witness differences. Local accents were assessed separately, and the gravity insertion's baseline continuation was kept beneath its lead. Mathematical qualifications were recorded without changing the written words or signs.

