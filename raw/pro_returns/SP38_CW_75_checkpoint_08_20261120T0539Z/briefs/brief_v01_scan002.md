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
