# Scan 004 — independent reader R3

## Deliverables and scope

The complete diplomatic reading is in `reading.tex`; all structured findings, including exact witness strings, evidence, confidence, bounding boxes, and prior-question decisions, are in `report.json`. Saved crop coordinates and transforms are in `crops/metadata.json`.

Only the assigned brief, packet files, three source images, and this reader’s own files were inspected. No other reader, page, shared result, OCR, or outside source was consulted.

**Source views:** whole image once, half A once, half B once: **3 source-image views**. Two unresolved places were cropped and each crop viewed once: **2 crop views**, **5 image views total**. There were no repeat source views, repeat crop views, recrops, rotations, or contrast changes. Both crops were enlarged to 2,400 pixels across with LANCZOS and saved as JPEG quality 95, subsampling 0.

The whole image is 1678 × 2039 pixels. Half A has origin (0, 0), size 1678 × 1099. Half B has origin (0, 939), size 1678 × 1100. Their overlap is whole-image y = 939–1099. Every box below uses whole-image coordinates `[left, top, right, bottom]`.

No clock was captured before the first source view. The earliest recorded clock is **2026-11-20T09:20:24.507317+00:00**, taken during crop preparation. `started_utc` explicitly records this limitation rather than presenting an estimated start as fact. The completion timestamp is recorded in `report.json`.

## Complete reading

The typed page number is **2.**

> I realize that I cause you a lot of trouble and work by asking every time for further explanation and that my assistance in writing the exposé is not very large. Therefore I suggest that you answer this letter only in case it is clear from my questions that I have really a misconception of your new set-up (and it would not surprise me if I have...). Otherwise I shall try to work out your theory as good as I can and make a preliminary manuscript which we can discuss when I am at Bures (I plan to come June 2). In any case, I hope to complete the definite version during my stay in Bures.

The final **e** in **definite** is a blue handwritten insertion following the black typed **definit**, encoded as `definit\handwritten{\inserted{e}}`.

The closing occupies two distinct typed lines, followed by a blue signature:

> With kind regards,  
> Sincerely yours,  
> J.P. **[Murre uncertain]**

There is no separate full stop after the surname. The grey handwritten archive number **3**, at the extreme bottom left, is encoded only as `% archive sheet number: 3`.

## Collation differences

There are **3 differences**, all against H. There is **no substantive change of letters or manuscript state against C**. The final-e insertion wrapper and narrower signature uncertainty wrapper add explicit encoding without changing C’s underlying reading.

| ID | Place | C | H | R3 reading and evidence | Whole-image box | View |
|---|---|---|---|---|---|---|
| R3-004-01 | Top centre | `\mspage{2.}` | Omitted | Typed **2.**: rounded upper arc, descending diagonal, flat foot, and a separate baseline period. High confidence. | `[765,68,808,100]` | Half A |
| R3-004-02 | Signature ending | No terminal period | `J. P. Murre.` | The surname’s connected final stroke ends with a short horizontal flourish and has no separate following dot. Remove H’s terminal period. High confidence for punctuation; surname remains uncertain. | `[799,718,965,789]` | `crops/02_signature.jpg` |
| R3-004-03 | Bottom-left archival number | `% archive sheet number: 3` | Omitted | Grey **3**, formed by two right-facing curved lobes with a narrow waist. High confidence. Retained as an archival comment. | `[23,1983,51,2017]` | Half B |

H has no uncertainty flag at any of these places. Its ordinary ellipsis character expresses the same three-dot count read in C and the image, so it is not a substantive difference. H’s single-line presentation of the closing is not counted because the brief excludes line-wrapping differences. Its lack of a handwritten wrapper around the final e does not omit the letter or move it, so that wrapper-only difference is likewise excluded.

## Every prior C question

| Prior question | Decision | Evidence and location |
|---|---|---|
| Final e in definite and the faint higher mark | Resolved: blue e added after typed t; no deletion or accent established. | Crop 01 shows a blue loop and lower sweep after black **definit**. No underlying black letter is resolved. The faint grey speck above has no coherent accent shape. Word box `[438,562,593,595]`. |
| Page-number 2 is typed | Confirmed. | Half A: black typewriter form, followed by a period; `[765,68,808,100]`. |
| June 2 numeral is typed | Confirmed. | Half A: black rounded top, diagonal transition and flat foot matching the page numeral; `[886,517,1052,553]`. |
| Signature J.P. Murre | Partly resolved, surname doubt retained. | Crop 02: J and P each have a following separate dot. The surname begins with a large M but its remaining low joined strokes do not certify the two r letters and final e individually; `[799,718,965,789]`. |
| as good as I can rather than an editorial correction to as well as I can | Confirmed exactly as written. | Half A: **g-o-o-d** is individually visible, and the next line begins **as I can**. No overwriting or deletion. |
| No separate mathematical step marked unverified | Confirmed as a page inventory finding. | One prose body paragraph, closing, signature; no mathematical display, diagram, or proof step. The blank lower half has no continuation. |
| No title; June 2 with no year; typed page 2. | Confirmed. | The top has only **2.**; the body parenthesis ends **June 2).** No separate date or title block occurs in either half. |

`S.json` is an empty array, so there are **0 S rows** to adjudicate.

## Retained doubt

**Signature surname: `J.P. \unsure{Murre}` — medium confidence.**

The first initial has a curved leading arm and long descending stroke, followed by a distinct dot. The next initial has a stem and upper bowl, followed by another dot. These support **J.P.** without requiring the uncertainty wrapper to cover the initials. The surname begins with a large three-stroke **M** and continues as low connected humps and a final sweep. **Murre** is the best complete reading, but the compressed medial and terminal strokes prevent certification of every letter. No other complete stroke-supported surname candidate was identified. This is the one point that remains for main-reader adjudication.

## Complete element inventory

| Element | Kind and hand | Position | Transcription |
|---|---|---|---|
| E01 | Typed text | Top centre | `\mspage{2.}` |
| E02 | Typed text | Nine body lines in upper portion | Complete paragraph beginning **I realize that I cause you a lot of trouble** |
| E03 | Insertion, unnamed blue-ink hand | Final body line, after **definit** | `\handwritten{\inserted{e}}` |
| E04 | Typed text | Beneath body, indented left | **With kind regards,** on its own line |
| E05 | Typed text | Next line, farther right | **Sincerely yours,** on its own line |
| E06 | Blue handwritten signature | Beneath closing | `\handwritten{J.P. \unsure{Murre}}` |
| E07 | Margin note, unnamed grey-pencil/grey-ink archival hand | Extreme bottom left | `% archive sheet number: 3` |

All seven inventory assertions are represented in `reading.tex`. No cancellation, drawing, diagram, letterhead, stamp, or further marginal text is present. The remaining lower sheet is blank apart from the archival number and ordinary paper/scan marks. The name **Murre** is retained as a reading, not established through an external identification.

## Crop record

| Crop | Unresolved question after halves | Whole-image crop bounds | Final dimensions |
|---|---|---|---|
| `crops/01_definite.jpg` | Final letter’s ink/state and faint higher mark | `[434,545,766,605]` | 2400 × 434 |
| `crops/02_signature.jpg` | Initials, surname strokes, and punctuation | `[695,645,1039,797]` | 2400 × 1060 |

Each target glyph, including the signature’s long descender, lies fully inside its crop. Crop 02 includes the closing line above for context. No further cropping was required.

## Notation, content, and mathematical checks

The typed accent in **exposé** appears black, with no distinct blue hand addition. **Set-up** retains its internal hyphen. There are exactly **three** periods before the parenthesis in **I have...).**, followed by the sentence period after the parenthesis. The two signature initials each retain a dot. **J.P.** is not expanded because this page supplies no full forenames.

The letter asks for an answer only if the writer’s questions show a misconception; it then describes a preliminary manuscript, a planned visit to Bures on June 2, and completion of the definite version during that stay. The author’s words **“and it would not surprise me if I have...”** express a possible misconception, not a mathematical proof check.

No independent proof, computation, or mathematical verification was performed or is claimed. `check_events` is empty. No mathematical normalization was applied to the prose.

## Brief feedback

The report keeps the missing initial timestamp explicit. A future brief could specify a clock capture at task receipt or an accepted unavailable-time representation.

The archival **3** is visible but omitted by H; I have counted this as a collation omission while retaining it only in the required comment. The brief could specify whether archival metadata omissions should instead be excluded from the substantive difference count. The textual reading is unaffected by that counting choice.
