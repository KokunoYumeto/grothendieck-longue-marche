# Scan 004 — independent reader R2

## Complete reading

The full diplomatic transcription is in `reading.tex`; structured findings are in `report.json`. The page is a typed English letter continuation, numbered **2.**, with a blue final **e** added to **definit**, two typed closing lines, and a blue signature best read **J.P. Murre** with retained uncertainty. The separate archival **3** is recorded only as a comment.

All nine body lines were read against both witnesses, including agreed wording, the black acute in **exposé**, the three dots in **I have...)**, **set-up**, **as good as I can**, **June 2**, and every typed closing punctuation mark. No other word or sign discrepancy was found.

## Views and evidence

Exactly **3 source views** were used: whole image once, half a once, half b once, in that order. Exactly **2 tight crops** were made and viewed once each, after the halves. Total image-view calls: **5**. No OCR, outside source, other page, other reader or shared result was inspected.

The source is 1678 × 2039 pixels. Half a maps to whole coordinates `[0, 0, 1678, 1099]`; half b maps to `[0, 939, 1678, 2039]`. Every reported box uses whole-image coordinates. Pixel alignment, without text recognition, is recorded in `view_log.json`.

| Crop | Whole-image extraction box | Purpose | Operations |
| --- | --- | --- | --- |
| `crops/01_definite.jpg` | `[425, 512, 670, 612]` | Blue final e and faint mark above it | Autocontrast; LANCZOS to 2400 px wide; unsharp mask; no rotation |
| `crops/02_signature.jpg` | `[691, 645, 1045, 807]` | Initials, compressed surname and terminal punctuation | Autocontrast; LANCZOS to 2400 px wide; unsharp mask; no rotation |

Both crops are JPEG quality 95, chroma subsampling 0. Each has coordinate and transformation metadata in the adjacent JSON file. No recropping or repeated image view was used.

## Witness discrepancies

There are **5 reported discrepancies**, all against H; **0 substantive discrepancies against C**. The explicit insertion wrapper around the final e clarifies a state already recorded by C and is not counted as a C error. One of the five rows concerns archival metadata rather than the letter’s authorial text.

| ID | Finding | Evidence and whole-image box |
| --- | --- | --- |
| R2-004-01 | H omits typed page **2.** | Half a; `[764, 65, 810, 103]`. Rounded typed 2 and separate black period. |
| R2-004-02 | H prints **definite** without the actual handwritten completion state. Read `definit\inserted{\handwritten{e}}`. | Crop 01; `[438, 560, 598, 603]`. Black typing ends at t; the narrow blue loop supplies e; no deletion is present. |
| R2-004-03 | H flattens the two closing lines and signature into one line. | Half a; `[289, 606, 1040, 792]`. Three separate vertical levels; the closing shifts right from the valediction. |
| R2-004-04 | H adds a period after **Murre**. None is visible. | Crop 02; `[800, 716, 964, 792]`. Dots occur after initials; the surname ends in a continuous low stroke, with no detached final dot. |
| R2-004-05 | H omits the lower archival **3**. | Half b; `[22, 1979, 53, 2018]`. This is an annotation/metadata discrepancy; the transcription uses only an archive comment. |

H has no uncertainty flag at any of these places. Its ellipsis character is equivalent to the three visible dots and is not counted as a substantive difference. Initial spacing and ordinary body line wrapping are likewise not counted.

## Every supplied C question or note

| Supplied question or assertion | Independent decision |
| --- | --- |
| Final e of definite; possible faint accent-like mark | Final e is certainly blue handwriting added after typed definit. The faint grey speck above does not resolve into an accent. No accent is transcribed. Crop 01. |
| Page 2 and June 2 are typed | Confirmed separately in half a. Both black numerals share a rounded top, narrow middle and flat foot. |
| Signature J.P. Murre remains uncertain | Retained as `\handwritten{\unsure{J.P. Murre}}`. Crop 02 supports the initials and capital M; the joined low ending cannot be fully letter-separated. |
| Preserve as good as I can | Confirmed in half a. The unusual wording is kept without correction. |
| No separate mathematical step marked unverified | Confirmed as a descriptive note. The page contains letter prose, no mathematical expression or proof step. |
| No title; June 2 has no year; visible page 2. | Confirmed. The archive 3 is a separate lower annotation. |

The structured report splits the two numeral checks into separate records, giving seven C-question/note records in total. The supplied S witness contains no rows, so `s_rows` is empty.

## Retained doubt and adjudication point

**One unresolved doubt:** the complete signature reading **J.P. Murre**. The initials have two visible dots. The capital M is tall and multi-stroked; the following low joined movements are compatible with **urre**, but the last letters are not independently cleanly separable. Confidence in the complete reading is **medium**. No second complete name is justified by the allowed image. The transcription retains C’s uncertainty.

The main reader should retain that doubt unless independent allowed evidence resolves the ending. The absence of a terminal surname period is clear even while the exact letter sequence remains uncertain.

## Complete inventory

| Element | Hand / state | Position | Representation in reading.tex |
| --- | --- | --- | --- |
| E01 | Typewriter | Top centre | `\mspage{2.}` |
| E02 | Typewriter | Upper-page nine-line prose paragraph | Entire paragraph, with original spelling, punctuation and wording |
| E03 | Blue handwritten insertion, hand identity unestablished | Final body line, after definit | `\inserted{\handwritten{e}}` |
| E04 | Typewriter | First closing line, left of centre | `With kind regards,\\` |
| E05 | Typewriter | Second closing line, farther right | `Sincerely yours,\\` |
| E06 | Blue handwritten signature | Third closing/signature line | `\handwritten{\unsure{J.P. Murre}}\\` |
| E07 | Light-grey archival handwriting, hand identity unestablished | Bottom-left paper edge | `% archive sheet number: 3` |

There are no visible deletions, displays, diagrams, drawings, letterheads or stamps. The rest of the lower page is blank. No blue accent or punctuation completion was observed elsewhere in the typed body. The blue correction and signature are not assumed to establish the same hand merely because their ink colours agree.

## Content, dates and mathematical checks

The writer apologises for the trouble caused by his requests for explanations and his limited assistance in writing the exposé. He requests a reply only if the questions expose a misconception of the new set-up. Otherwise he plans to develop a preliminary manuscript for discussion in Bures, arrive on **June 2**, and complete the definite version during his stay. The page supplies no year or full letter date.

No mathematical claim was proved, computed or used. Pure visual reading is not entered as a proof check; `check_events` is empty.

## Brief feedback

The brief leaves the discrepancy status of omitted archival metadata somewhat open. This report labels the archive-number omission explicitly so that it can be excluded from an authorial-text-only count. The explicit insertion wrapper is required by the brief but is not treated as a substantive difference from C’s correctly positioned handwritten e.
