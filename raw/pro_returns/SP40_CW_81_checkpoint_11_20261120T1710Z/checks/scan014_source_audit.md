# Scan 014 — source and component audit

Text-only audit of the three reader returns, the packet C sources, and `out/PREAMBLE.tex`. No image was opened; no crop, rendering, compilation, installation, external research, source alteration, or ink decision was performed. All row numbers below are **one-based** within the named JSON array. Paths are relative to `/workspace/scratch/94548b74fbe0`.

## Coverage and exact textual map

| Array | Reader A | Reader B | Reader C | Total |
|---|---:|---:|---:|---:|
| `differences` | 14 | 2 | 2 | 18 |
| `doubts` | 13 | 2 | 2 | 17 |
| `inventory` | 16 | 3 | 3 | 22 |

`packets/014/C_inventory.json` supplies two additional inventory rows. Every row is mapped below. The packet's two doubtful-reading rows are `packets/014/C_doubts.txt:10–11`; its notation rows at lines 4–5 concern `$n$-aires` and the insertion.

The complete B and reader-C `reading.tex` files are byte-identical to `packets/014/C.tex`. Extracting A's four title-node bodies in source order and joining them with one space gives exactly packet C line 2:

```tex
\unsure{décompositions} \inserted{et découpages} $n$-aires d'\unsure{espaces} topologiques
```

| A node | Exact body | Source slice |
|---|---|---|
| `A014T1` | `\unsure{décompositions}` | `out/readers/014/A/reading.tex:8` |
| `A014I1` | `\inserted{et découpages}` | same file, line 9 |
| `A014T2` | `$n$-aires` | same file, line 10 |
| `A014T3` | `d'\unsure{espaces} topologiques` | same file, line 11 |

Thus the source extraction preserves the two exact `\unsure` scopes, the insertion body and marker, the inline-math `n`, the hyphen, the apostrophe, and the unpunctuated endpoint. A's archive comment at line 71 reproduces packet C line 4. No title body is repeated. A's `GUIDE01` is an added graphic corresponding to the attachment already recorded by `\inserted` and packet C's notation row; the insertion macro itself is retained. `out/PREAMBLE.tex:23` expands that macro into angle brackets, and does not draw a leader.

## All difference and doubt rows

Reader paths in this table are `out/readers/014/{A,B,C}/report.json`. The first two physical groups contain the two packet C doubtful-reading rows; each reader independently retains them. All other difference entries occur only in A.

| Physical group / node | Difference row identifiers | Doubt rows | Source correspondence |
|---|---|---|---|
| `A014T1` | A `A014-D01`; B `B014-01`; C `014-C-D01` | A[1], B[1], C[1] | Packet doubt “first main word” |
| `A014T3`, word `espaces` | A `A014-D02`; B `B014-02`; C `014-C-D02` | A[2], B[2], C[2] | Packet doubt “after d'” |
| `GUIDE01` | A `A014-D03` | — | Explicit path for existing insertion attachment |
| `G01` | A `A014-D04` | A[3] | Upper-right title-adjacent spot |
| `G02` | A `A014-D05` | A[4] | Spot below `n` |
| `G03` | A `A014-D06` | A[5] | Spot left of `d'` |
| `G04` | A `A014-D07` | A[6] | Pale point beside `d` stem |
| `G05` | A `A014-D08` | A[7] | Upper blank field, right of centre |
| `G06` | A `A014-D09` | A[8] | Field beneath title |
| `G07` | A `A014-D10` | A[9] | Left field below midpoint |
| `G08` | A `A014-D11` | A[10] | Lower-right separated pair |
| `G09` | A `A014-D12` | A[11] | Faint lower-left trace |
| `G10` | A `A014-D13` | A[12] | Lower-right edge trace |
| `G11` | A `A014-D14` | A[13] | Foot trace left of centre |

Count: six retained-word difference rows plus twelve A graphical additions = 18; six retained-word doubt rows plus eleven A trace-group doubts = 17. A `differences` occupies lines 9–370 and `doubts` lines 371–476; B uses lines 9–78, and reader C uses lines 40–113. A's original-doubt map is at lines 680–683. The two original word doubts have `diff_C=false` in every reader; A's guide and eleven trace groups have `diff_C=true`. All H fields are null and all `diff_H` values are false in these rows.

## All inventory rows

Each cell gives `inventory[index] / element`. Joint assignments explicitly preserve the original main-title or insertion grouping. Packet C rows are in `packets/014/C_inventory.json`; reader rows are in their respective `report.json` files.

| A physical group(s) | Reader A | Reader B | Reader C | Packet C |
|---|---|---|---|---|
| `A014I1`, attachment represented by `GUIDE01` | [1] / `014.02` | [1] / `014.B.01` | [1] / `014.02` | [2] / `014.02` |
| `GUIDE01`, explicit graphic | [3] / `014.A.GUIDE01` | included in insertion row above | included in insertion row above | included in insertion row above |
| `A014T1` + `A014T2` | [4] / `014.01a` | [2] / `014.B.02`, jointly with T3 | [2] / `014.01`, jointly with T3 | [1] / `014.01`, jointly with T3 |
| `A014T3` | [6] / `014.01b` | same [2] | same [2] | same [1] |
| `G01` | [2] / `014.A.G01` | — | — | — |
| `G02` | [5] / `014.A.G02` | — | — | — |
| `G03` | [8] / `014.A.G03` | — | — | — |
| `G04` | [7] / `014.A.G04` | — | — | — |
| `G05` | [9] / `014.A.G05` | — | — | — |
| `G06` | [10] / `014.A.G06` | — | — | — |
| `G07` | [11] / `014.A.G07` | — | — | — |
| `G08`, both fills | [12] / `014.A.G08` | — | — | — |
| `G09` | [13] / `014.A.G09` | — | — | — |
| `G10` | [14] / `014.A.G10` | — | — | — |
| `G11` | [16] / `014.A.G11` | — | — | — |
| Archive `13`, comment | [15] / `014.A.archive` | [3] / `014.B.03` | [3] / `014.03` | Already in C.tex; absent from packet inventory |

This covers all 22 reader rows and both packet rows without creating extra inventory records for a joint assignment. Inventory source slices: A `report.json:477–674`, B `report.json:79–113`, C `report.json:114–148`.

## Graphic commands and origin map

Every `source_command` string in A `notes.final_source_component_map` occurs exactly once in A `reading.tex`. There are **13 visible graphic commands**: twelve `\fill` commands in eleven trace groups plus one `\draw` for `GUIDE01`. There are also twelve invisible `\path[use as bounding box]` commands: one global and eleven local. Counting those layout paths produces 25 path-producing commands altogether. There are fifteen nodes: four title nodes and eleven trace-wrapper nodes.

| Component | A `reading.tex` command line(s) | Fixed origin | Local rectangle |
|---|---|---|---|
| `GUIDE01` | 13 | direct full-scan coordinates | global `(0,0)–(1760,2470)` |
| `G01` | 17 | (1538,52) | (0,0)–(8,8) |
| `G02` | 22 | (1311,162) | (0,0)–(9,10) |
| `G03` | 27 | (940,221) | (0,0)–(9,9) |
| `G04` | 32 | (983,213) | (0,0)–(8,8) |
| `G05` | 37 | (1425,727) | (0,0)–(8,8) |
| `G06` | 42 | (1073,912) | (0,0)–(9,8) |
| `G07` | 47 | (240,1384) | (0,0)–(10,8) |
| `G08` | 52–53 | (1568,1791) | (0,0)–(15,17) |
| `G09` | 58 | (231,1889) | (0,0)–(8,10) |
| `G10` | 63 | (1705,2276) | (0,0)–(10,8) |
| `G11` | 68 | (735,2423) | (0,0)–(11,13) |

The source map is explicitly `full(x,y)=(origin_x+u,origin_y+v)`, followed by `(X,Y)=(0.006x,-0.006y)` centimetres. Both levels use the same units. The inner picture's `baseline={(0,0)}` fixes its baseline to the local rectangle's top edge, and the enclosing zero-separation `anchor=base west` places that left baseline at the declared origin. Positive local y therefore runs downward; the local height is below that baseline. The local rectangles start at x=0 and contain every endpoint and control point. Their widths exceed the ordinary 1pt node minimum even before the qualifier is added. No source-level origin shift or local overflow of the drawn paths was found.

### Bounding-box qualifications

1. **Qualified-node extent:** `out/PREAMBLE.tex:18` appends `\textsuperscript{?}` after the argument of `\unsure`. That extra glyph extends the node above and to the right of the inner trace canvas. The local rectangle describes the trace picture, while the enclosing node also includes that qualifier. The baseline anchor preserves the trace origin despite this added extent. Explicit `black!…` fill options set the traces' grayscale; the surrounding orange group does not replace those explicit fill colours.
2. **Observed locus versus generated contour:** A labels the contours approximate in `report.json:1009`. Its `full_scan_bbox` values identify recorded source loci. Numerically computed cubic extrema of the commands slightly exceed seven of those locus boxes, while remaining inside every fixed local rectangle:

| Component | Excess beyond reported locus box, in full-scan pixels |
|---|---|
| `G03` | top 0.265986 |
| `G04` | top 0.500000 |
| `G05` | top 0.090170 |
| `G07` | top 0.090170; right 0.130768 |
| `G08` | top 0.265986; bottom 0.047375 |
| `G10` | top 0.154701 |
| `G11` | left 0.154701; top 0.198630 |

For an exact check on the largest excess, G04's first cubic has y-controls `(3,1,1,3)`; at t=1/2 its y is 1.5, giving full y=214.5, whereas its recorded locus starts at y=215. These are subpixel contour/locus discrepancies, with no local-rectangle clipping established. `GUIDE01` has centreline bounds approximately `[1273.244151,81,1497,162]`; its 0.3pt round stroke remains inside its reported `[1270,79,1500,164]` locus.

3. **Title typography:** The map places title baselines. The 9pt font and editorial superscripts determine the typeset glyph extents; the source does not scale each word to its reported image box. The fixed outer rectangle reserves 10.56cm by 14.82cm. `out/PREAMBLE.tex:27` centres the picture in normal document flow. These properties establish a layout proposal, without a rendered layout or scan-to-glyph identity check.

## B/C observations outside difference and doubt arrays

| Observation source | Reported full-scan box | A physical group |
|---|---|---|
| B `notes.small_surface_observations[1]`; B `reading.md:29` | [940,220,950,232] | `G03` |
| B `notes.small_surface_observations[2]`; B `reading.md:29` | [1308,160,1324,174] | `G02` |
| C `notes.surface_observations[1]`; C `reading.md:27` | [1537,50,1549,62] | `G01` |
| C `notes.surface_observations[2]`; C `reading.md:27` | [1309,161,1323,174] | `G02` |
| C `notes.surface_observations[3]`; C `reading.md:27` | [939,219,952,231] | `G03` |
| C `notes.surface_observations[4]`; C `reading.md:27` | [1566,1789,1582,1805] | `G08`, both fills |

The named objects and containing/overlapping source boxes supply these correspondences. B's guide account (`reading.md:10,17,36`; `report.json:155–174`) and C's guide account (`reading.md:11,31`; `report.json:199–215`) map to `A014I1` plus `GUIDE01`; C gives guide box `[1272,79,1503,167]`. Their source files preserve the common insertion macro and add no path. Their direct title accounts map to T1/T2/T3; foot accounts map to the archive comment. Neighboring-line fragments at crop boundaries are explicitly assigned to the already transcribed title in B `reading.md:29` and both reports' crop-boundary notes, so they introduce no extra physical group.

B/C provide no separately located counterpart for G04, G05, G06, G07, G09, G10, or G11. Their general field statements and absence of proposed paths do not resolve those A proposals. The six prose-only surface observations remain part of the review record even though they supply neither a new character nor a formal difference row.

## Items the root record should state explicitly

- The 18 difference rows are exhaustively covered. A's layout conversion to four positioned 9pt nodes inside one fixed picture has no separate difference row; record it as a layout qualification. The literal text extraction above supplies its exact correspondence to the common C/B/C-reader line.
- A adds a separate explicit guide path while retaining `\inserted`. B/C represent the attachment through that unchanged macro. The shared insertion wording and attachment account coexist with this graphical representation difference.
- A's eleven trace groups carry eleven local `\unsure` wrappers; with the two word doubts, A has thirteen wrappers in all. B/C have two. Their prose-only point observations must remain attached to G01/G02/G03/G08 during adjudication.
- The archive inventory addition has no textual difference row because the comment already occurs in C. Its hand attribution differs: A[15] and B[3] use “another unnamed hand”; C[3] uses “undetermined hand.” Root owns that attribution decision. The archive comment itself is the same in all sources.
- A's title inventory splits packet `014.01` into `014.01a` and `014.01b`; the table supplies the complete join. A's graphic rectangles and editorial question marks are layout/qualification elements; their role is stated separately from the proposed source traces.
- The source and mapping checks support a reviewable A proposal. Acceptance or rejection of any trace, guide contour, physical layout, or hand attribution remains with root's image adjudication and final ownpage/record approval.


## Calculation method clarification, recorded by root

The audit agent reported on2026-11-20 that the extrema computation used an inline Python script with standard json/re/math, floating-point scalar cubic coefficients and analytic quadratic derivative roots, a1e-12 tolerance for degenerate derivative coefficients, endpoint inclusion, and output rounded to six decimal places. It captured no UTC clock. The numeric values above are approximate; the explicit G04 midpoint arithmetic is exact. The stroke-containment statement additionally used declared stroke width and coordinate-scale arithmetic. The baseline/origin discussion is static source reasoning. This scope is recorded as SP40-014-SOURCE-GEOMETRY in CHECK_EVENTS; no image observation or contour-to-ink validation is claimed for that source calculation.
