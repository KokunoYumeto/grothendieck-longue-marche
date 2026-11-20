# Independent reader brief v08 — first used scan 008

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
