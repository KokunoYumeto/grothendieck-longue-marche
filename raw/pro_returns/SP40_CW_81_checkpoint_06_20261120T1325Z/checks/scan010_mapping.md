# Scan 010 — source and inventory coverage

Complete draft: root supplied all 28 local decisions; `main_adjudicated=false` awaits root review/commit. There are **24 C differences**, **0 H differences**, **5 original C doubt rows retained**, **20 remaining local doubt records**, and **77 merged inventory elements**. H is `desc`; it contributes no text-collation rows.

All 66 report rows (A 19, B 25, C-reader 22), all 33 reader doubt rows, all 249 inventory source rows including witness C, and all 34 non-equal reader-TeX opcodes are mapped. Exact choices, IDs, rows, reports, TeX, audits, and fingerprints are retained in the JSON.

## Local decision / source-row map

| Decision | Local identity | A report rows | B report rows | C-reader report rows | C source-doubt row | C diff |
| --- | --- | --- | --- | --- | --- | --- |
| 010-D01 | Lower-left graph, first endpoint of first edge | A010-D01 | B01 | C010-D01 | 1 | yes |
| 010-D02 | Final middle disk, projecting trace and detached blob | A010-D02 | B02, B10 | C010-D02a | 2 | yes |
| 010-D03 | Foot, left angular trace crossing the final graph | A010-D02 | B02 | C010-D02b | 2 | no |
| 010-D04 | Foot, right angular trace: existing principal paths | A010-D02 | B02 | C010-D02c | 2 | no |
| 010-D05 | Lower second disk, diagonal-stroke state and graphic wrapper | A010-D03 | B03 | C010-D03, C010-D03G | 3 | yes |
| 010-D06 | Upper seventh graph, middle vertex and its projecting hook | A010-D04 | B04, B08 | C010-D04 | 4 | yes |
| 010-D07 | Upper edge, paired detached traces and their geometry | A010-D05, A010-D10 | B05, B13, B14 | C010-D05a, C010-D06 | 5 | yes |
| 010-D08 | Right middle open space, existing main pale curl | A010-D05 | B05 | C010-D05b | 5 | no |
| 010-D09 | Right middle open space, existing pair of tiny flecks | A010-D05 | B05 | C010-D05c | 5 | no |
| 010-D10 | Lower-middle graph, first vertex | A010-D06 | B06 | C010-D12 | — | yes |
| 010-D11 | Final lower graph, first vertex | A010-D07 | B07 | C010-D13 | — | yes |
| 010-D12 | Final middle disk, small detached spot above outer lower arch | A010-D08 | B09 | C010-D10 | — | yes |
| 010-D13 | Upper variant disk, fragments and dots beside descending stroke | A010-D09 | no local row; TeX absence retained | no local row; TeX absence retained | — | yes |
| 010-D14 | Right middle open space, smaller pale trace above-right of main curl | A010-D11 | B15 | C010-D08 | — | yes |
| 010-D15 | Right angular foot group, internal pale diagonal | A010-D12 | B20 | C010-D14 | — | yes |
| 010-D16 | Below right angular foot group, detached short dash | A010-D13 | B25 | no local row; TeX absence retained | — | yes |
| 010-D17 | Right angular foot group, upper dark upright fragment | A010-D14 | B21 | C010-D15 | — | yes |
| 010-D18 | Right angular foot group, separate spot near (1567,921) | A010-D14 | B22 | C010-D15 | — | yes |
| 010-D19 | Below/right of upper second graph, pale curved trace | A010-D15 | B16 | C010-D07 | — | yes |
| 010-D20 | Gap between lower first and second disks, pale diagonal | A010-D16 | B18 | C010-D09 | — | yes |
| 010-D21 | Far-right margin level with lower row, pale irregular patch | A010-D17 | no local row; TeX absence retained | C010-D17 | — | yes |
| 010-D22 | Lower first disk, faint left continuation of horizontal trace | A010-D18 | B19 | C010-D16 | — | yes |
| 010-D23 | Lower second disk, small pendant at lower-left outline | A010-D19 | B11 | C010-D11 | — | yes |
| 010-D24 | Lower second disk, pale descending trace above pendant | no local row; TeX absence retained | B12 | no local row; TeX absence retained | — | yes |
| 010-D25 | Above upper fourth disk, pale descending trace | no local row; TeX absence retained | B17 | no local row; TeX absence retained | — | yes |
| 010-D26 | Right angular foot group, detached upper-left spot near (1550,894) | no local row; TeX absence retained | B23 | C010-D15 | — | yes |
| 010-D27 | Right angular foot group, detached right patch near (1603,930) | no local row; TeX absence retained | B24 | no local row; TeX absence retained | — | yes |
| 010-D28 | Final lower disk, detached short mark near (1165,877) | no local row; TeX absence retained | no local row; TeX absence retained | no local row; TeX absence retained | — | yes |

## Original C doubt rows

| Source row | Explicit local identities | Status |
| --- | --- | --- |
| 1 | 010-D01 | retained; source row counted once |
| 2 | 010-D02, 010-D03, 010-D04 | retained; source row counted once |
| 3 | 010-D05 | retained; source row counted once |
| 4 | 010-D06 | retained; source row counted once |
| 5 | 010-D07, 010-D08, 010-D09 | retained; source row counted once |

Row 2 covers only the final-middle projecting trace/blob and the two principal foot traces. Row 5 covers only the upper pair, existing right curl, and right flecks. New local spots, strokes, and graph endpoints keep their own identities. Shared crop references do not transfer doubts between neighboring marks.

## Inventory coverage

| Merged ID | Object / local identity | Witness C IDs | A IDs | B IDs | C-reader IDs |
| --- | --- | --- | --- | --- | --- |
| 010.I01 | near top edge above sixth disk — two detached ink traces | 010.01 | 010.01 | 010.01 | 010.01 |
| 010.I02 | top row 1 — disk with one chord | 010.02 | 010.02 | 010.02 | 010.02 |
| 010.I03 | below top disk 1 — one dot | 010.03 | 010.03 | 010.03 | 010.03 |
| 010.I04 | top row 2 — disk with two chords | 010.04 | 010.04 | 010.04 | 010.04 |
| 010.I05 | below top disk 2 — two dots | 010.05 | 010.05 | 010.05 | 010.05 |
| 010.I06 | top row 3 — disk with crossed strokes and solid point | 010.06 | 010.06 | 010.06 | 010.06 |
| 010.I07 | above third disk — OK | 010.07 | 010.07 | 010.07 | 010.07 |
| 010.I08 | below top disk 3 — short line | 010.08 | 010.08 | 010.08 | 010.08 |
| 010.I09 | top row 4 — disk with three slanting chords | 010.09 | 010.09 | 010.09 | 010.09 |
| 010.I10 | top row 5 — disk with three curved edge cuts | 010.10 | 010.10 | 010.10 | 010.10 |
| 010.I11 | below top disks 4 and 5 — grouping brace below upper disks 4 and 5 | 010.11 | 010.11 | 010.11 | 010.11 |
| 010.I12 | inside first oval — three dots | 010.12 | 010.12 | 010.12 | 010.12 |
| 010.I13 | top row 6 — narrow disk with crossing and lower arc | 010.13 | 010.13 | 010.13 | 010.13 |
| 010.I14 | below top disk 6 — encircling oval | 010.14 | 010.14 | 010.14 | 010.14 |
| 010.I15 | inside second oval — short line and dot | 010.15 | 010.15 | 010.15 | 010.15 |
| 010.I16 | top row 7 — disk with bold central segment | 010.16 | 010.16 | 010.16 | 010.16 |
| 010.I17 | above top disk 7 — OK | 010.17 | 010.17 | 010.17 | 010.17 |
| 010.I18 | below top disk 7 — three vertices in a line | 010.18 | 010.18 | 010.18 | 010.18 |
| 010.I19 | top row 8 — disk with filled triangular region | 010.19 | 010.19 | 010.19 | 010.19 |
| 010.I20 | above top disk 8 — OK | 010.20 | 010.20 | 010.20 | 010.20 |
| 010.I21 | below top disk 8 — triangle with three filled corners | 010.21 | 010.21 | 010.21 | 010.21 |
| 010.I22 | between parentheses far right — ou | 010.22 | 010.22 | 010.22 | 010.22 |
| 010.I23 | top row 9 inside parentheses — small oval and crossed strokes | 010.23 | 010.23 | 010.23 | 010.23 |
| 010.I24 | middle row 1 — disk with four near-vertical cuts | 010.24 | 010.24 | 010.24 | 010.24 |
| 010.I25 | middle row 2 — three chords and small lower arch | 010.25 | 010.25 | 010.25 | 010.25 |
| 010.I26 | middle row 3 — four peripheral arcs | 010.26 | 010.26 | 010.26 | 010.26 |
| 010.I27 | below middle disks 1–3 — grouping brace | 010.27 | 010.27 | 010.27 | 010.27 |
| 010.I28 | below first middle group — four dots | 010.28 | 010.28 | 010.28 | 010.28 |
| 010.I29 | between middle groups — two isolated flecks | 010.29 | 010.29 | 010.29 | 010.29 |
| 010.I30 | middle row 4 — broad disk with crossing near upper left | 010.30 | 010.30 | 010.30 | 010.30 |
| 010.I31 | middle row 5 — narrow crossed disk, two curved cuts | 010.31 | 010.31 | 010.31 | 010.31 |
| 010.I32 | middle row 6 — crossed disk with two upper-left cuts | 010.32 | 010.32 | 010.32 | 010.32 |
| 010.I33 | middle row 7 — crossed disk and two lower arches; superposed traces separately inventoried | 010.33 | 010.33 | 010.33 | 010.33 |
| 010.I34 | open space to the right of seventh middle disk — existing main pale curl | 010.34 | 010.34 | 010.34 | 010.34 |
| 010.I35 | below middle disks 4–7 — long brace | 010.35 | 010.35 | 010.35 | 010.35 |
| 010.I36 | below right middle group — one line and two dots | 010.36 | 010.36 | 010.36 | 010.36 |
| 010.I37 | above hatched lower disk — ? | 010.37 | 010.37 | 010.37 | 010.37 |
| 010.I38 | bottom row 1 — two distinct black intersections | 010.38 | 010.38 | 010.38 | 010.38 |
| 010.I39 | above bottom disk 1 — OK | 010.39 | 010.39 | 010.39 | 010.39 |
| 010.I40 | below bottom disk 1 — two separate edges | 010.40 | 010.40 | 010.40 | 010.40 |
| 010.I41 | bottom row 2 — disk with crossing and repeated diagonal strokes | 010.41 | 010.41 | 010.41 | 010.41 |
| 010.I42 | inside bottom disk 2 — diagonal hatching across the chords | 010.42 | 010.42 | 010.42 | 010.42 |
| 010.I43 | bottom row 3 — horizontal bold segment and top loop | 010.43 | 010.43 | 010.43 | 010.43 |
| 010.I44 | bottom row 4 — horizontal bold segment and right loop | 010.44 | 010.44 | 010.44 | 010.44 |
| 010.I45 | below bottom disks 2–4 — grouping brace | 010.45 | 010.45 | 010.45 | 010.45 |
| 010.I46 | below lower middle group — two joined edges and an isolated dot | 010.46 | 010.46 | 010.46 | 010.46 |
| 010.I47 | bottom row 5 — disk with four continuous major interior runs and two adjoining thickened segments | 010.47 | 010.47 | 010.47 | 010.47 |
| 010.I48 | above bottom disk 5 — OK | 010.48 | 010.48 | 010.48 | 010.48 |
| 010.I49 | below bottom disk 5 — line with four vertices | 010.49 | 010.49 | 010.49 | 010.49 |
| 010.I50 | below and across last graph — faint angular line with thick dark corner | 010.50 | 010.50 | 010.50 | 010.50 |
| 010.I51 | far lower right — second angular line with dark lower edge | 010.51 | 010.51 | 010.51 | 010.51 |
| 010.I52 | below upper disks 4 and 5 — oval enclosing three dots | 010.11 | 010.11 | 010.11 | 010.11a |
| 010.I53 | around upper-right variant — two drawn parentheses enclosing ou and variant disk | 010.22 | 010.22 | 010.B.52 | 010.22a |
| 010.I54 | above final middle disk — projecting broken dark/pale trace | — | — | 010.B.55 | 010.33a |
| 010.I55 | inside final middle disk left of crossing — detached tapered dark blob | 010.33 | 010.33 | 010.B.54 | 010.33b |
| 010.I56 | inside final middle disk above outer lower arch — small detached dark spot | — | 010.53 | 010.B.56 | 010.33c |
| 010.I57 | right middle open space below main curl — two tiny detached flecks | 010.34 | 010.34 | 010.34 | 010.34a |
| 010.I58 | right middle open space above-right of main curl — separate smaller pale trace | — | 010.34 | 010.B.63 | 010.34b |
| 010.I59 | below/right of upper second graph — pale detached curved trace | — | 010.58 | 010.B.61 | 010.52 |
| 010.I60 | between lower first and second disks — pale diagonal trace | — | 010.59 | 010.B.62 | 010.53 |
| 010.I61 | below lower-left outline of lower second disk — small pendant stroke | — | 010.62 | 010.B.58 | 010.54 |
| 010.I62 | inside right angular foot group — separate pale diagonal | — | 010.55 | 010.B.65 | 010.55 |
| 010.I63 | upper part of right angular foot group — short darker upright fragment | — | 010.57 | 010.B.66 | 010.56 |
| 010.I64 | beside upper right angular-foot fragment near (1567,921) — separate small dot | — | 010.57 | 010.B.67 | 010.56 |
| 010.I65 | above-left of upper right angular-foot endpoint near (1550,894) — small gray spot | — | — | 010.B.68 | 010.56 |
| 010.I66 | right of upper right angular-foot endpoint near (1603,930) — small gray patch | — | — | 010.B.69 | — |
| 010.I67 | inside first lower disk — pale horizontal trace with faint left continuation | — | 010.61 | 010.B.64 | 010.57 |
| 010.I68 | far-right margin level with lower row — pale irregular patch | — | 010.60 | — | 010.58 |
| 010.I69 | lower-left archive margin — 9; % archive sheet number: 9 | — | 010.52 | 010.B.53 | 010.59 |
| 010.I70 | beside descending stroke of upper variant disk — short fragments and two detached dots | — | 010.54 | — | — |
| 010.I71 | lower second disk above its small pendant — pale descending vertical trace | — | — | 010.B.59 | — |
| 010.I72 | above upper fourth disk — broken pale descending trace and darker small piece | — | — | 010.B.60 | — |
| 010.I73 | below right angular foot group — detached short slanted dash | — | 010.56 | 010.B.70 | — |
| 010.I74 | above/right of middle vertex under upper seventh disk — projecting short hook | — | — | 010.B.57 | — |
| 010.I75 | below lower rim of first middle disk — existing pale descending continuation from about (192,503) to (195,556) | 010.24 | 010.24 | 010.24 | 010.24 |
| 010.I76 | above/left of upper variant disk — existing pale curved arc from about (1548,116) toward (1584,102) | 010.23 | 010.23 | 010.23 | 010.23 |
| 010.I77 | inside final lower disk near (1165,877) — small detached short upright/slanted mark | — | — | — | — |

The two enclosing ovals, braces, five OK labels, ou and both parentheses, question mark, twelve graph groups, all disk drawings, isolated flecks, faint residual paths, and archive 9 comment are explicitly covered. I75/I76 make two existing faint paths explicit without changing transcription. I77 is root-only D28. Unknown residual marks have `undetermined hand`; the archive numeral retains the readers’ `another unnamed hand`.

## Counting and source discrepancies

D05 counts one physical change for removal of the generic horizontal rule while retaining cancellation/hatching uncertainty. Its invisible phantom copy creates no duplicate drawing count. D06 groups the middle vertex and projecting hook; D07 groups the two upper-edge refinements. D28 has no invented reader report row.

The final lower disk has four major runs already drawn in C/A/B/C-reader. Witness C/A/B inventory says “three strokes with two bold segments at an angle”; C-reader says “disk with four strokes and two adjoining thickened segments”. Root confirmed four in own crop02. This is an inventory-only correction with diff_C=false; the separate newly observed short mark near (1165,877) is counted only as D28.

D10 exact primary choices: A/C-reader `\circ|\bullet`, B `\bullet|\circ`; root chose A/C-reader. D11: A `\circ|\bullet`, B/C-reader `\bullet|\circ`; root chose B/C-reader. A’s lower-second-disk source lacks the outer unsure wrapper, which B/C-reader and root include. D15 preserves the shorter root-supported course with an in-place unsure wrapper; B’s longer proposed continuation remains recorded in provenance. D22 includes the half-read faint extension and root’s interrupted gray-patch refinement.

Root reports 15 distinct successful reader crops plus 2 own crops, total 17. One failed context-truncated B05 output attempt was followed by a successful retry and is excluded from seen-image counts. Check events remain empty.
