# Scan 014 — independent reader B

Start: **2026-11-20 14:55:27 UTC**, obtained before reading the packet. H is empty (`hua_has=nothing`). Only scan014 and its supplied packet were inspected.

## Visual reading audit

| Physical line or element | Direct reading and state | Decision / evidence |
|---|---|---|
| Whole sheet | Title at upper right; extensive blank field; archive numeral at lower left | Whole image viewed once for layout. No date or manuscript page number read. |
| Upper addition | `et découpages` | Readable; acute retained. Crop **03_insertion_guide.png**, full bbox **[1138,28,1515,175]**, preserves the complete guide. Its left end bends down to the gap before n-aires. The insertion macro remains attached there. |
| First main line, first word | `\unsure{décompositions}` | **C doubt retained**, medium confidence. Initial d, curved acute, c/o, descending p and tall internal stroke are visible; compressed intervening joins leave the full word qualified. Crop **01_first_word.png**, full bbox **[860,83,1292,195]**. |
| First main line, end | `$n$-aires` | Readable n, separate short hyphen, and aires. Checked on half a and crop 03. No exponent or index supplied. |
| Second main line, opening | `d'\unsure{espaces}` | d and detached apostrophe readable. **C espaces doubt retained**, medium confidence: long p descender and surrounding low joins support the word but do not independently isolate every letter. Crop **02_second_line.png**, full bbox **[925,180,1565,305]**; local word bbox **[995,195,1175,279]**. |
| Second main line, end | `topologiques` | Readable t, descending p, tall l, long lower g return and q descender with compressed final joins. No terminal punctuation read. Crop 02 contains the full endpoint. |
| Lower half | Archive `13` at foot | Half b read once. Full bbox **[77,2408,128,2451]**, or half-b bbox **[77,1253,128,1296]**. Preserved as the required comment, and added to the inventory. |

Ordinary wrapping of the two main title lines is joined in the transcription. The insertion remains marked and attached before n-aires. No deletion, independent margin note, displayed formula, diagram, or separate drawing was identified. The apparent rule beneath the upper addition is the continuous insertion guide whose left end descends to the insertion gap.

## C doubt map and witness changes

- **C source doubtful row 1**, “first main word”: `décompositions` retained under `\unsure`; report **B014-01**, `diff_C=false`.
- **C source doubtful row 2**, “after d'”: `espaces` retained under `\unsure`; report **B014-02**, `diff_C=false`.
- The two notation-table rows are notation entries, not additional source doubts.
- No C textual reading change is proposed. H supplies no text; no H collation row or claim of an H omission is made.
- C's archive-number comment is already correct; its omission from C's inventory is repaired in the updated inventory.

## Small observed patches

Crop 02 shows a tiny gray fleck left of d at full bbox **[940,220,950,232]**. Crop 03 shows a tiny pale detached patch below n at **[1308,160,1324,174]**. Neither yields a supported letter or word candidate. Their hand, role and surface origin remain undetermined. They are documented for adjudication without a supplied character. The bits touching crop 01's lower edge and crop 02's upper edge belong to the neighboring title lines already transcribed.

## Final source-component map

| Visible component | Final source | Status |
|---|---|---|
| Main title | `reading.tex`, line 2 | All words retained after viewing; both C word doubts retained. |
| Upper insertion text and attachment | `\inserted{et découpages}`, immediately before `$n$-aires` | Conventional insertion representation; the guide's attachment is recorded by crop 03. No separate graphical variant proposed. |
| Archive numeral | `% archive sheet number: 13` | Read directly and inventoried. |

C has no TikZ paths. No source drawing path was removed or substituted; the final graphical-variant map is empty.

## Method and validation

Whole image, half a and half b were each viewed once. One tight crop was made for each of the two original doubtful words, plus one for the insertion guide and adjacent title-ending detail. Each resulting crop was viewed once, with no recrop. Crops use PIL LANCZOS enlargement, autocontrast and light unsharp masking; `make_crops.py` records exact source boxes.

All decisions use visible ink. No mathematical check was performed (`check_events=[]`). No OCR, internet, external source, other reader file, other-page image, compiler, renderer, format builder or installation was used. Structural source checks and agreement of the final reading/report were performed before return.

End: **2026-11-20 15:00:29 UTC**. Structural checks passed.
