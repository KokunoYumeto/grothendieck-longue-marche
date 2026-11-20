# Scan 005 — independent reader A

## Visual reading audit

The whole page, half a, and half b were each viewed once. Nine local crops were then generated and each viewed once. I read every physical line of the paragraph against C and H. All boxes in report.json and crop_manifest.json are on the original 1231 × 1678 scan; half b begins at y = 759. No OCR, outside research, other page, other reader file, or delegation was used.

| Physical line / area | Readable ink and audit | Remaining doubt |
| --- | --- | --- |
| 1 | Underlined **NB**; `Si σ est un automorphisme`. Initial a, tall t, p descender, h, dotted i and final group support **automorphisme** after crop 01. | Tiny isolated point below the middle of the word: visible, intention unresolved; conservatively retained. |
| 2 | `du corps des complexes, et si`. The comma follows complexes. | None identified. |
| 3 | `f est ``spécial'', alors f^σ est ...`. Both pairs of quotation ticks, comma, raised σ and final crossed t-like stroke were read. | Contracted **égalmt** remains strongest; **également** retained as the supplied doubtful alternative after crop 02. |
| 4 | `spécial -- donc Aut(C) opere sur`. The C has a doubled left portion. The first **opere** has no detached accent in crop 03. | None retained for opere. |
| 5 | `l'ens des f spèciaux. Mais il`. No point follows **ens**. The accent near the plural word descends right; crop 04 supports **spèciaux**. The separate upper point within the word is retained by its dotted i. | None retained for the grave accent reading. |
| 6 | `opère par l'intermédiaire de`. The second **opère** has a visible separate grave accent. | None identified. |
| 7 | `Aut(Q̄), car si f=P/Q spécial,`. Parentheses, bar, comma after Aut, equals and slash, plain P/Q, and final comma were read. Crop 09 confirms the compressed spécial and its rising accent. | Crop 05 leaves ordinary versus deliberately double-stroked barred Q unresolved. |
| 8 | `les coeff. de P,Q sont des`. Definite point after the f crossbar; comma between P and Q. | Crop 08 shows a pale short trace below the terminal part of coeff.; its intention is unresolved and its shape is conservatively retained. |
| 9 | Underlined `nbs algébriques. Il revient au = de`. The long single underline, period, dotted i and crossed final t in **revient**, and two bars of the prose **=** were read. | None retained for revient or the equality sign. |
| 10 | `dire que les zéros de P,Q sont`. Accent above zéros and comma between capitals read. | None identified. |
| 11 | `des nbs algébriques, i.e. le diviseur`. Comma, i-dot, and both abbreviation punctuation marks read. | None identified. |
| 12 | `de f est`, with no completion or terminal punctuation. The de-to-f connection and final est strokes were checked in the context of crop 07. | None in the three written items. |
| Lower isolated marks | Definite dark short left stroke and definite separate dark right dash. | The faint trace above the left stroke leaves `-` versus `=` unresolved; a separate very pale horizontal trace just to its right is also conservatively retained with uncertain intention. |
| Bottom left | Archive numeral **4**, recorded only as a TeX comment. | None identified. |

## Collation result

The report has thirteen local records. Four resolve C’s uncertainty qualifications: **automorphisme**, **opere**, **spèciaux**, and **revient**. C’s **égalmt / également**, ordinary/double-stroked barred Q, and lower **dash / equals** remain unresolved. C’s notation-table entries alone were not treated as uncertainty loci.

The principal proposed differences from H are the contracted primary reading **égalmt**, unaccented first **opere**, **ens** without a point, grave-accented **spèciaux**, literal **au = de**, and the omitted lower isolated marks. H’s full **également** remains an explicit alternative at the compressed word; the primary difference there is consequently qualified. H’s barred double-stroked Q remains a supported alternative, so no confirmed glyph difference is asserted there. H’s `emph` macros at **NB** and **nbs algébriques** are emphasis counterparts and are not counted as collation changes. H’s final note is editorial apparatus.

Three additional detached shapes are proposed conservatively for review: the point under **automorphisme**, the pale short trace below **coeff.**, and the pale short trace beside the lower left mark. Their occurrence in the scan is recorded separately from the unresolved question of deliberate writing. Each appears with `unsure` in reading.tex and has a precise original-image box in report.json.

## Mathematical reading

The symbols and the progression from coefficients to zeros and divisor were followed while reading. The text is transcribed as written, including its unfinished ending. I performed no calculation or proof verification and made no mathematical repair; `check_events` is empty.

## Deliverables

- `reading.tex`: complete proposed page, with explicit remaining doubts and candidate detached traces.
- `report.json`: all local collation records, inventories, notation, crop coordinates, and honest view counts.
- `crops/01_automorphisme.png` through `crops/09_special_quotient.png`: the nine local enlarged views.
- `crop_local.py`, `crop_manifest.json`, `make_report.py`: reproducible local crop and report records.
