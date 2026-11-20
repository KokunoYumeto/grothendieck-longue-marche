# Scan 014 — independent reader C

Start: **2026-11-20 14:55:36 UTC**. End: **2026-11-20 15:02:13 UTC**. The start clock was obtained in the initial read batch, before visual inspection. Only this page's packet and permitted context were read.

## Visual audit

Whole image viewed once for layout; upper half a and lower half b each viewed once. All three local crops were viewed once. No OCR, external research, compiler, renderer, format builder or installation was used. H is empty and `hua_has` is `nothing`.

| Physical item | Direct reading and state | Evidence / outcome |
| --- | --- | --- |
| Addition above first line | `et découpages`, attached before n | `02_insertion_and_naires.png`, full box [1135,28,1565,180]. Raised accent and descending letters checked. The long lead-in curves down into the gap immediately before n; C's insertion is retained. |
| First main line, first word | `\unsure{décompositions}` | C doubt **first main word**, retained. `01_first_word.png`, [860,90,1295,195]; target [881,96,1268,188]. Initial d, raised accent, co-like low strokes, long p-descender and later tall loop support the candidate; compressed medial joins remain unresolved. No alternative word supplied. |
| First main line, ending | `$n$-aires` | Crop 02: rounded n, single short hyphen, a and raised i stroke, joined ending. Same reading as C. |
| Second main line, opening | `d'\unsure{espaces}` | C doubt **after d'**, retained. `03_second_line.png`, [930,182,1565,305]; word target [1003,214,1167,274]. Apostrophe, low initial shoulder, long p-descender and low joined final strokes checked; internal letter separation remains unresolved. |
| Second main line, ending | `topologiques` | Crop 03 contains full descenders and blank endpoint space. Tall t/l, descending p/g/q, terminal joined letters checked. No final full stop supplied. |
| Page field | No additional legible text, diagram, deletion or margin note identified | Both halves inspected. Minute isolated point-like spots are recorded separately below; no word or mathematical relation assigned. |
| Lower left foot | Archive numeral `13` | Half b, [79,1257,124,1292], maps to full [79,2412,124,2447] by adding y=1155. Clear 1 followed by 3. Retained comment; archive item added to the inventory. |

## Witness / doubt account

C has two actual doubtful-reading rows; both are retained once, with their original primary readings. Both `diff_C` values are false. No lexical, punctuation, insertion-state or cancellation-state change is proposed. H has no page text, so every H entry is null and every `diff_H` value is false.

The complete proposed `reading.tex` is text-identical to C. Its two `unsure` markers agree with the report. No mathematical check was performed; `check_events` is empty.

## Small surface observations for root review

Three isolated point-like shapes appear in the title crops: [1537,50,1549,62] above/right of the insertion; [1309,161,1323,174] under n; and [939,219,952,231] left of d'. The lower-half open field also contains two minute dark flecks around full [1566,1789,1582,1805]. No letter candidate, secure punctuation attachment, hand or origin was established for these spots. They are documented without a supplied character. Their coordinates are explicit so root can inspect them; they are not presented as lexical additions.

## Final source-component map

There are no original C TikZ paths and no proposed graphical variants. The checked insertion and guide are represented by the unchanged source component `\inserted{et découpages}`; guide bbox [1272,79,1503,167]. The archive number remains `% archive sheet number: 13`. No local TikZ fragments, dimension maps, path combinations or new path components occur. Inventory order follows the addition, main title, then archive foot numeral, with original inventory identifiers retained in provenance.

## Direct source verification

Macros are confined to `scanpage`, `unsure`, and `inserted` from PREAMBLE, plus ordinary inline math. Braces, math delimiters, crop filenames, C source-row mapping, H-empty state and report/reading agreement checked directly. All generated files are within this reader's assigned directory.
