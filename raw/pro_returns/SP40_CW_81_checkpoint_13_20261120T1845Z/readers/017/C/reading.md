# Scan017 — independent C-reader audit

Reader model: **GPT-6 Astra Pro**. Effort is **not separately exposed**. This reader label is separate from witness C. Start recorded at **2026-11-20 17:09:20 UTC**, before the assigned packet or images were read.

## Visual reading method

The whole scan was viewed once for layout, then supplied half a once and half b once for the complete line-by-line comparison. Fourteen local crops were each viewed once. Crop 14 addresses the accent in the main opening word; it did not repeat a previously cropped or decided place. No settled image or locus was reopened.

Coordinates below refer to the original full scan, top left origin. The full scan is 1685 × 2363; half a is 1685 × 1261; half b is 1685 × 1262. The recorded mapping is `x_full = x_b`, `y_full = y_b + 1101`, with `1101 = 2363 − 1262`. Half a has zero offset. This is the required half-location translation, with no image alignment calculation.

`crop_log.json` records every fixed rectangle and resulting image size. Processing was PIL crop, RGB conversion, autocontrast, and fourfold LANCZOS enlargement. Only the marginal-note crop was rotated, by −45° using BICUBIC with expansion before enlargement. No sharpening, OCR, numerical image comparison, curve fitting, compiler, renderer, package installation, external research, or delegation was used.

## Line-by-line audit

| Physical line or element | Ink retained in the selected reading | Reading status and witness points |
|---|---|---|
| Heading | **Cas particuliers**, one underline | Complete title and underline read on half a. C underline and H emphasis convey this same marked span. |
| Opening line | `Supposons que ∀i∈I,` followed by cancelled `E_i est/soit rare dans X.` | E and rare are resolved locally. The verb remains `est|soit`. The separate full stop after crossed X is present; H omits it. |
| Raised opening addition | `on ait` | Raised above the crossed clause. Insertion state is explicit in the selected reading; H gives the words live without an addition marker. |
| Parenthetical, over two physical lines | `(si Σ_i⁺ Σ_i⁻ sont les deux comp. conn. de X∖Σ_i)` | `si` is recovered against H `où`. The signed symbols, abbreviation points and written `Σ_i` in the complement are retained. |
| Crossed sentence | `Alors on trouve que` | The full sentence remains cancelled; `trouve` remains doubtful because the strike merges its low strokes. The long q descender is retained as part of the word. |
| First equality | `overline(Σ_i⁺) = Σ_i⁺ ∪ E_i` | The closure rule, plus signs and i indices are visible. The space after E_i supplies no separate comma; H has a comma. |
| Second equality | `overline(Σ_i⁻) = Σ_i⁻ ∪ E_i` and M01 at the right | The distant small triangular point is drawn once and qualified. A period reading remains an alternative. The dot of the i is separately present in the letter. |
| Assertion line | `Alors je dis qu'on a` | The apostrophe, `on` run and small final `a` are visible. H gives `Alors je dis que`. Reading this sentence produced no proof-check event. |
| Third equality | `overline(Σ_12) = Σ_12 [G01] E_1 ∪ E_2` | G01 preserves the shared left stem and two right returns of the overdrawn first join. Cup is primary; amalg remains an alternative. The join after E_1 is a simple cup. |
| Dividing rule | G02 | A gently bowed line with a small hooked right end. C's straight rule is replaced by the literal approximation; H has no corresponding entry. |
| Angled left note | `introduire|introduisons la partition Π|π_j = {deleted unsure Σ E_j, Σ_j⁺, Σ_j⁻}` | The note is complete through its closing brace. Word ending, case of pi, and overwritten predecessor remain qualified. An edge trace from nearby main writing supplies no further marginal word. H's final marginal ill placeholder is counted once with the local predecessor reading. |
| Cancelled new beginning | `Supposons` | One complete cancelled word, read on half a. |
| Soit line | `Soit J⊂I tel que I=J⨿{i}.` | The capital J, singleton i, square-form join, and final point are visible. The C/H amalg/sqcup syntax gives the same local square-form reading. |
| Main paragraph, first physical line | `Consid[e|é]rons la partition`, with inserted `Π_J`, then `de` | The complete first word is readable, with accent presence left locally open. G03 preserves the bent guide under the raised name into `de`. |
| Main paragraph, next line | `X` deleted `définie`, live `définie par les` overwritten `Σ/E_j (j∈J),` | The cancelled word resolves C `des parties|définie` to `définie`. The earlier Sigma predecessor remains doubtful under the live E. The comma after the condition is present. |
| Intersection line | qualified cancelled/live `et`, then `intersection des partitions`, raised `ternaires Π_j`, then `de X` | The longer word resolves to `intersection`. The opening glyph and cancellation target retain an explicit deleted-et/live-et state choice. G04 retains both caret branches. H's cancelled/added intersection sequence is collated once at the opening cluster. |
| Following physical line | `(j∈J) définies par les E_j`, then a crossed `E|∈`, then `(j∈J)` | The isolated two-lobed sign stays qualified. H's internal ill placeholder is one corresponding parent entry. |
| Lower display | `X=E_j⨿coprod_{α∈π_0(X∖E_j)} Σ_j^α` | The large square-form join, coproduct, alpha, pi and lowered ring are readable on half b. M03 preserves a separate short mark near the Sigma head/alpha. A dotless j node avoids a second printed dot while its attachment remains uncertain. |
| Right of lower display | M02a and M02b | Two separate small dark pieces, diagonally spaced. Both are drawn under a local qualification, with hand, role and surface origin unestablished. |
| Lower paragraph, first physical line | `-- c'est aussi la partition définie par` | All words read on half b, including the faint low strokes in `aussi`; no expansion is supplied. |
| Following line | `celle de bigcup_{j∈J} E_j en les E_j,` | The open cup, j∈J limit, both E_j forms and trailing comma are retained. |
| Next line | `et la partition`, raised `Π_J` with ring, `de X∖[G06]_{j∈J} E_j intersection` | The first raised ring remains circle/zero. G05 reproduces the curved insertion guide. The transverse stroke in G06 is visible inside the cup mouth; its role stays locally qualified. |
| Binary-partition line | `des partitions binaires Π_{J,j}` with raised ring, inserted `(j∈J)`, `induites` | The two indices and comma are distinct. The second ring retains the first ring's uncertainty under the first-occurrence convention. G07 carries the long connected hook over `induites`; its left portion is the curve represented by H's added opening parenthesis. |
| Last physical line and raised correction | `sur`, inserted `U_[qualified full subscript states]=`, `X∖bigcup_{j∈J} E_j par les Π_j (g|j∈J). Pour` | U's old/live J/j sequence and a single retraced J remain explicit alternatives. G08 reaches the full lower endpoint beside `sur`. There is one closing parenthesis and a full stop; H adds a second close. The last variable remains g/j. `Pour` resolves from the local o and ur strokes. No following sheet was inspected or used. |
| Lower-left archive numeral | `16` | Kept solely as `% archive sheet number: 16`. Attribution remains undetermined. |

## Original C doubtful-row map

The source section is the table headed **Doubtful readings**. Its twelve source rows retain their ordinal identities; the notation and abbreviation tables supply no invented doubt rows.

| Source row | Every named local part | Disposition and report entry |
|---|---|---|
| 01 — first line directly under on ait | E_i/Σ_i; est; rare/dense | E_i resolved D01; verb retained D02; rare resolved D03. |
| 02 — struck sentence above equalities | trouve | Retained D07. |
| 03 — third equality, first join | cup/amalg | Retained D11, with literal retracing geometry G01. |
| 04 — left note | Π_j/π_j; crossed Σ | Both retained separately, D14 and D15. |
| 05 — after de X | des parties/définie | Resolved to cancelled définie, D18. |
| 06 — start of intersection | et; intersection | et and state retained D20; longer word resolved D21. |
| 07 — under E_j and after later E_j | earlier Σ; later E/∈ | Both retained separately, D19 and D23. The first is a genuine table doubt although C.tex omits its unsure marker. |
| 08 — Π_J above de, and binary partition name | first raised ring; second raised ring | Both retained, D26 and D29. The table's qualification reaches the second occurrence although C.tex prints it without another marker. |
| 09 — last parenthesis | g/j | Retained D35. |
| 10 — last word | Pour/Puis | Resolved to Pour, D37, using only this page's crop. |
| 11 — first complement after inserted Π_J | bar/plain union | Stroke presence resolved D28; a separately recorded role qualification remains on literal G06. |
| 12 — above sur, U subscript | predecessor J/j under final J | Retained D32, with complete-state alternatives for old/live forms and single retracing. |

## Graphical record and coordinates

`report.json` records each observed locus box separately from its fixed drawing rectangle. All paths in `reading.tex` use `x=0.01cm, y=-0.01cm`. The declared origin is the listed original full-scan coordinate; the path coordinates are local offsets. Text anchors are base west with zero inner/outer separation. No path extrema or alignment measurements were calculated. Font extents are not claimed to be measured facsimile bounds.

| Component | Declared source origin | Physical parts preserved |
|---|---|---|
| M01 | (1172, 557) | One small triangular point, with period interpretation alternative. |
| G01 | (947, 783) | Shared left stem, inner cup return, outer cup return. |
| G02 | (300, 887) | One connected dividing line, slight curvature and terminal hook. |
| G03 | (1215, 1100) | Curved guide under raised Π_J, with Π_J and de in the local fragment. |
| G04 | (950, 1350) | Curved left caret branch and straight right branch below ternaires Π_j. |
| M03 | (1192, 1627) | One detached short dark piece. Its inner placement is declared by (47, 3) within outer origin (1145, 1624). |
| M02 | (1568, 1738) | Upper-right and lower-left dark pieces, each its own fill path and inventory component. |
| G05 | (770, 1970) | Curved guide beneath the lower raised partition name. |
| G06 | (1115, 1975) | Cup contour and separate transverse line within its mouth. |
| G07 | (1235, 2070) | One continuous hook from the left of induites across its upper line. |
| G08 | (330, 2160) | Guide beneath the U subscript and down beside sur; declared final path endpoint (453, 2294) in full-scan coordinates. |

## Computation and validation scope

The recorded arithmetic is the required half-b offset and the crop enlargement sizes. Exact crop inputs, mappings and output dimensions appear in `crop_log.json` and the report. The cropping scripts, JSON serialization and subsequent structural source checker are all disclosed in the report's `processing_events`.

`check_events` is empty. No mathematical proof, correspondence, algebraic check, theorem, numerical geometry calculation or pixel-difference comparison was carried out. The manuscript assertions alone provide no check event.

The source checker examines braces, environment nesting, display blank lines, macro names, allowed difference categories, unique record identifiers, original source-row references and existing crop references. It produces `structural_check.json`. The complete selected `reading.tex` and `report.json` are then read together before return; compilation and rendering are outside this workflow.

## Completed source review

End recorded at **2026-11-20 17:35:19 UTC**. The structural check passed and the complete TeX/report contents were read together. Two oversized text outputs truncated portions of the report; bounded text sections then delivered every remaining field. The first checker flags came from its treatment of comment-only lines and its omitted standard `\circ` entry; both checker issues were corrected, with no TeX change between those checks. The report preserves both actual check results and their scope.
