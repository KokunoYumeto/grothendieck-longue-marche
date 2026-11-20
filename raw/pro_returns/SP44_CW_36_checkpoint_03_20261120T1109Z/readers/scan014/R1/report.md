# Scan 014 — independent reader R1

## Scope and timestamps

- Recorded UTC start: **2026-11-20 10:12:08 UTC** (first clock checkpoint, immediately after reading the brief/preamble/packet).
- UTC end: **2026-11-20 10:29:51 UTC**.
- Assigned page only: scan 014, handwritten manuscript page **5**, archive sheet number **13**.
- Read in full: `briefs/brief_v05_scan014.md`, the exact `/workspace/scratch/a62c50f64437/SP44_CW_36_work/PREAMBLE.tex`, and `packets/scan014/packet.md`.
- No other page, reader return, published text, OCR, text recognition, web resource, or LaTeX compilation was used. The supplied crop helper was read only to confirm its documented transformations and output path.

The complete diplomatic page is in `reading.tex`. The complete comparison, inventory, notation list, uncertainties and empty mathematical-check log are in `result.json`; the latter is not just a list of amendments.

## Main reading decisions

The scan preserves conspicuous forms that a normalized French transcription would change: **Onnsuppose**, **lesfibres**, **da point**, **da classe**, **définit**, **Im résulte**, and **Soient X un schéma**. The letter before `e` in `de/se` remains uncertain despite a preference for `de`. Both capitals in the inserted fibre morphism are visibly **X**. They have not been changed to a mathematically expected domain.

The cancelled upper passage is largely recoverable through the x-outs, including **pouvoir que l'hypothèse sérieuse b). Soit z un cycle**. The crop supports `pouvoir`, without an additional r before v; the strange syntax has not been repaired. The last old `a` is legible but its cancellation boundary is not secure, so an in-place cancelled/live alternative is retained. A full stop after **de S)** is visible at the edge and is supplied against C's omission.

Both cohomology expressions have a missing right parenthesis in the source: D1 closes twice after n where three closings would be needed; the inline i-star group closes three times after n where four would be needed. The printed expressions are reproduced with those omissions. The crossed coefficient subscript looks mechanically repeated, rather than a separately drawn pen ell; `chi|ell` is marked at the first occurrence and the first candidate is used thereafter. H's global note about the machine chi-shaped ell is credited, so this is not counted as an H alphabet error.

The larger lower **g** in the inline group is pen work, but its predecessor remains **f/g**. The older degree under the live 1 is **0-like**, still uncertain. The coefficient remains **underlined Z/Q**: a Z diagonal is visible together with rounded/tail-like strokes, without a secure old-Z/new-Q order.

In the proof, the overprinted curve and product capitals remain open. The `mathbb` forms are a diplomatic rendering of visible multiple impressions, not a claim that an intentional blackboard-bold alphabet was being used. The repeated products have literal baseline typewriter **x**, not a free-standing centered multiplication sign. The old **d** beneath the initial c of **construction** is sufficiently distinct to remove C's doubt about that old letter.

In section 4, the handwritten assumption has a capital-sized **Alg.** The cancelled extra letter in **hyp…erplanes** has a detached acute and an e-like bowl/middle bar: I read **hyp\deleted{é}erplanes**, against C's k/x candidates. Before P^1_k, there is a cancelled S-like letter followed by a separate visible x-out cell; `Sx` records that cancellation ink, not a recovered old lexical x. The open-base capitals remain overprinted and ambiguous, including a B-like literal outline. The final map label favours **j**, because of the detached dot and low leftward hook, but f remains possible. The target S is clipped and remains marked uncertain. A separate final full stop is visible.

A fine vertical trace above/through b in **fibres** was inspected. It may be pen retracing of the ascender or an incidental trace; there is no securely independent authorial letter or instruction. I have kept `fibres`, entered the trace in the inventory and added a local TeX comment. I have not invented a new character or independent drawing from it.

## Actual visual workflow

1. Opened `A36-01_36_scan014.jpg` **once**, for layout only. Recorded a single full-page typescript, two displays, interlinear replacements, extensive machine x-outs, pen emphasis, pen mathematical additions, top-right 5 and bottom-left 13. No diagram or independent semantic drawing was visible.
2. Opened `A36-01_36_scan014_a.jpg` **once**, and read every line and formula against both C and H.
3. Opened `A36-01_36_scan014_b.jpg` **once**, and read every line and formula against both C and H. The halves overlap; the b-half starts at whole-image y=995. I did not reopen or enlarge either half.
4. Listed the remaining cancelled/overprinted/small-glyph loci and made the **22** tight crops below with the supplied helper, `--scan 14 --reader R1`. Each crop was created once and actually inspected once with `view_image`. No image delivery was truncated, and no resend was needed.

The whole image is **1679 × 2150** pixels; each supplied half is **1679 × 1155** pixels. All boxes in `result.json` and below are in **whole-image coordinates**. Half-settled differences also have whole-image boxes. Crops use autocontrast, LANCZOS scaling, `UnsharpMask(1,110,3)` and JPEG quality 90, as implemented by the supplied helper. No rotation was needed for these near-horizontal loci.

| Viewed crop | Whole-image box `[x0,y0,x1,y1]` | Saved enlargement |
|---|---|---|
| `top_old_clause.jpg` | `[428, 124, 902, 192]` | 2400 px; rotation 0° |
| `top_fixed_clause.jpg` | `[214, 195, 982, 260]` | 2400 px; rotation 0° |
| `point_end.jpg` | `[1190, 203, 1669, 272]` | 2400 px; rotation 0° |
| `cancelled_upper.jpg` | `[213, 271, 1628, 337]` | 2400 px; rotation 0° |
| `cancelled_lower.jpg` | `[212, 334, 1064, 402]` | 2400 px; rotation 0° |
| `first_cohomology.jpg` | `[580, 543, 1135, 625]` | 2400 px; rotation 0° |
| `inline_group.jpg` | `[501, 675, 981, 755]` | 2400 px; rotation 0° |
| `restriction_cancelled.jpg` | `[365, 723, 1315, 814]` | 2400 px; rotation 0° |
| `sans_doute.jpg` | `[1133, 818, 1421, 884]` | 2400 px; rotation 0° |
| `de_definit.jpg` | `[447, 975, 936, 1043]` | 2400 px; rotation 0° |
| `trace_old.jpg` | `[1306, 1051, 1642, 1116]` | 2400 px; rotation 0° |
| `adherence_old.jpg` | `[202, 1119, 638, 1184]` | 2400 px; rotation 0° |
| `curve_old.jpg` | `[1020, 1120, 1193, 1188]` | 2400 px; rotation 0° |
| `product1.jpg` | `[1237, 1199, 1532, 1268]` | 2400 px; rotation 0° |
| `product2.jpg` | `[1044, 1269, 1208, 1341]` | 2400 px; rotation 0° |
| `construction.jpg` | `[412, 1473, 744, 1539]` | 2400 px; rotation 0° |
| `sur_k.jpg` | `[1302, 1603, 1558, 1695]` | 2400 px; rotation 0° |
| `finaldisplay.jpg` | `[556, 1822, 856, 1922]` | 2400 px; rotation 0° |
| `fibres_mark.jpg` | `[366, 1897, 520, 1984]` | 2400 px; rotation 0° |
| `hyperplanes.jpg` | `[855, 1918, 1119, 1990]` | 2400 px; rotation 0° |
| `base_S.jpg` | `[1351, 1916, 1550, 1995]` | 2400 px; rotation 0° |
| `finalmap.jpg` | `[1393, 1997, 1673, 2103]` | 2400 px; rotation 0° |

Actual viewing order was the order in the table: two crop images per tool output, with each output inspected before continuing. The crop JSON sidecars record source filename, box, operations and creation UTC.

## Compact line-by-line coverage

The labels here are local reporting labels; they are not introduced into the transcription. Approximate y values refer to the whole image. Every physical text line, interlinear insertion and display was covered. The full running reading, including every word, is in `reading.tex`.

| Label / y | Coverage and observations |
|---|---|
| Page mark / 67 | Handwritten 5, separate from the typed body. |
| I0 / 100 | Entire inserted `a) et b) vérifiés … induit`; bars, both X capitals, colon, pen arrow and surrounding pen placement guide read. The guide's large curved ends are not parentheses. |
| T1 / 157 | `Onnsuppose`, cancelled `que le morphisme induit`, `pour lesfibres en s-bar (point géométrique`; no extra spacing inserted into the joined forms. |
| T2 / 227 | Cancelled `fixé`, live `de S`, cancelled comma/clause, `au dessus da point générique de S).`; accent and exact underline extent, closing parenthesis and full stop checked. |
| T3 / 298 | Entire x-cancelled `si S est irréductible pour avoir le maximum de chances de pouvoir que`; surviving accents, letter sequence and cancellation state examined. |
| I1 / 353 | Typed replacement `Soit` above the old line; it is not handwriting. |
| T4 / 370 | Cancelled `l'hypothèse sérieuse b). Soit z un cycle a`, with uncertain final cancellation boundary; live `z ∈ Z^n(Y) tel que le cycle`; pen membership and superscript n checked. |
| T5 / 442 | `induit sur Y_sbar soit algébriquement équivalent à zéro, et à fortiori`; bar, all accents and comma read. |
| T6 / 515 | `cohomologiquement équivalent à zéro. Donc da classe`; retained initial d of da. |
| D1 / 583 | Complete displayed u(z) membership, H^1, R^{2n−1}, f-star, underlined Z, crossed subscript and `(n))`; separate pen membership/star and actual parenthesis count recorded. |
| T7 / 659 | `est définie. Ceci posé, je dis que cette classe est`, cancelled `une classe de torsion`; continuous pen underline begins at cette and crosses the old phrase. |
| T8 / 712 | Underlined `contenue dans`, full i-star group with old degree and old f/g, live g/star, ambiguous underlined coefficient and three final closings; underlined `modulo une classe de torsion`, then comma and du. |
| I2 / 742 | Typed, then cancelled `On applique 2) à i_sbar/i`; terminal index left open after its one crop. |
| I3 / 769 | Typed, then cancelled interlinear `si,`; distinguished from the old main-line clause. |
| T9 / 783 | `moins si on`, cancelled `suppose S japonais de dimension 1, ou même`, then live `se permet de`; comma and cancelled status preserved. |
| I4 / 840 | Typed `probablement` and faint pen placement guide; the guide is not added punctuation. |
| T10 / 849 | `remplacer S par un ouvert non vide(restriction`, cancelled `sans doute`, live `inutile, mais`; no blank cell between vide and parenthesis. |
| T11 / 888 | `cet énoncé nous suffira pour ce qu'on veut en faire).`; paragraph closes before indented proof. |
| T12 / 941 | `Pour le voir, on applique 2) au morphisme i_sbar. La courbe C et`; exact index and punctuation checked. |
| T13 / 1012 | `le cycle Z'' peuvent de/se définit déjà sur une extension finie K de k(s),`; double prime, uncertain first cell, final t and comma preserved. |
| T14 / 1083 | `Un argument de trace permet de supposer que K=k(s), et`, cancelled `quitte à prendre`; capital Un after comma retained. |
| T15 / 1155 | Cancelled `l'adhérence du cycle`, `on peut supposer que`, overprinted curve capital, cancelled `et Z`, `est une courbe propre`; all cancellation cells and overprints accounted for. |
| T16 / 1225 | `et lisse relative sur S lui-même, et Z'' un cycle sur` first overprinted-capital product, comma, cancelled `Alors`, `et que`; literal x and subscript S checked. |
| T17 / 1297 | `la formule z=i*(z')+z'' est valable sur` second product, full stop, `Elle implique une`; pen star, prime and both product components read. |
| T18 / 1368 | `décomposition analogue de u(z), qui est la somme de i*(u(z')) et de`; all parentheses, prime and pen star checked. |
| T19 / 1438 | `u(z''), de sorte qu'il suffit de prouver que u(z'') est nul. Or u(z'')`; all three double-prime occurrences and punctuation read. |
| T20 / 1510 | `induit par` old d/live c of construction, `2) l'homomorphisme nul H^1(C_sbar) → H^{2n−1}(Y_sbar). Im`; degrees, bars, pen arrow and final m checked. |
| T21 / 1579 | `résulte donc bien de 1) que u(z'') est nul, cqfd.`; comma, abbreviation and full stop preserved. |
| I5 / 1635 | Entire pen `sur k Alg. clos` and its guide, attached after m before the existing comma. Capital-sized initial and abbreviation point retained. |
| T22 / 1674 | `4. Soient X un schéma projectif et lisse de dimension m, prenons`; plural verb and separate section number retained. |
| T23 / 1744 | `un pinceau de Lefschetz, de façon à obtenir une variété éclatée non`; accents and comma read. |
| T24 / 1811 | `moins projective et lisse` X with pen tilde, `et un morphisme`; no display is supplied for this ordinary line. |
| D2 / 1880 | Pen-tilde f, colon, pen-tilde X, pen arrow, cancelled S and x-out cell, ordinary typed P^1_k; every visible component retained. |
| T25 / 1954 | `dont les fibres sont les sections hyp[deleted é]erplanes du pinceau. Soit` ambiguous overprinted capital `un`; acute on old é and the unassigned fine trace above b examined. |
| T26 / 2030–2075 | `ouvert non vide de P^1_k au dessus duquel` pen-tilde X `soit lisse, et soit` final inline map; ordinary text placement, j/f, Y, equality, pen tilde, restriction stroke, repeated overprinted base, arrow, clipped target and final period recorded. |
| Archive mark / 2101 | Bottom-left 13, recorded only in the required comment. |

Observable paragraph cues are retained: an opening paragraph surrounding D1, a new indented proof beginning `Pour le voir`, section 4 with its own opening, D2, and the following ordinary text continuation. The final map remains inline at the text margin; no centered display is invented for it.

## Comparison ledger and inventory

`result.json` contains **44 comparison rows**: **8 against C**, **35 against H**, including **4 against both** and **5 C-doubt/ink confirmations against neither**. There are **26 rows linked to C doubts**. Resolving a C doubt is counted against C even when the retained first candidate is unchanged, as required. Unchanged uncertainties and mere secondary-alternative ordering are not counted as C corrections.

The exact rows include all recovered cancellations and all source forms that differ from H. H's own notes are credited where they actually identify an old phrase, its source layer or an overprint. In particular, I did not count its note about the cancelled `une classe de torsion` as omitting that old phrase; I did not count equivalent emphasis/underline macros or bold-versus-underlined Z/Q house typography; and I did not count absent handwriting wrappers alone as H reading errors. H's explanatory expectation about the domain of the top map is editorial commentary, not spurious authorial text.

The **66-item inventory** covers every text block, both displays, all interlinear additions and their guides, each cancellation/overprint, all pen stars, memberships, arrows, tildes and underlines, the page and archive numbers, and the uncertain trace above b. There is no independent margin argument, diagram or identifiable free-standing drawing on this page. The uncertain trace is inventoried cautiously, without assigning authorship or promoting it to a semantic figure.

The **12 notation entries** are page-local observations only. The frozen table was used for comparison, never to normalize this page's ink. The **13 unresolved records** include the two product occurrences together and the two repeated base-capital occurrences together; their individual witness-difference rows and evidence boxes remain separate where appropriate.

## Mathematical reading, diagnostics and actual checks

The page's live claim concerns a cycle that is algebraically equivalent to zero on a geometric fibre, its associated class u(z), and containment of that class in the indicated pullback image modulo torsion, after a possible nonempty-open restriction of S. The author explicitly weakens the reservation from cancelled **sans doute** to live **probablement**, followed by the qualification that this formulation suffices for the intended use.

The proof on this page invokes an earlier statement 2), passes through a curve and a cycle over a finite extension K of k(s), cites a trace argument, and asserts that the relevant objects and decomposition can be arranged over S. It reduces to vanishing of u(z''), identifies an induced zero map from H^1(C_sbar) to H^{2n−1}(Y_sbar), and invokes earlier statement 1). Statements 1) and 2) were not in the allowed page packet, so no proof of those claims, the trace step or the claimed vanishing was attempted.

The following were **reading diagnostics**, not theorem checks:

- The top map has X on both sides, while later cycles and a fibre cohomology group use Y. The two printed X capitals were checked and retained.
- Parentheses were counted in D1 and the inline i-star group. Each expression lacks one closing parenthesis; both omissions are retained.
- The products' overprinted first capitals could matter to the claimed domains. Their visible strokes remain unresolved; mathematical expectation has not selected Y.
- The repeated final base letter and j/f map label could be interpreted from the surrounding construction, but their physical readings were left open instead.
- Section 4's field assumption comes from the pen insertion itself, not from an inferred standard setup for a Lefschetz pencil.

**No mathematical check event is claimed.** `check_events` is an empty array. The actual checks performed in this run were visual collation and the non-compiling structural checks listed below. No targeted proof check, independent re-proof, computation, formal certificate or rechecking of a background theorem occurred.

## Structural verification

Performed only structural verification, without compilation:

- All three required files exist and are nonempty.
- `reading.tex` has balanced braces, balanced inline math, exactly two balanced display-math pairs and no unbalanced environments.
- Every command used belongs to the supplied preamble or standard LaTeX/amsmath/amssymb; no new macros, document wrapper or `cotefile` command was introduced.
- The page begins with `scanpage{14}`, retains the handwritten `mspage{5}` and records archive 13 only in a comment.
- JSON parsed successfully and has all required top-level and per-row fields, valid difference/inventory categories, boolean comparison flags and unique IDs.
- All 44 difference boxes have valid whole-image coordinates within 1679 × 2150.
- All 66 inventory items, 12 notation entries and 13 unresolved records have their required fields.
- All 22 cited crop JPEGs exist, are 2400 pixels wide and have matching R1/scan014 sidecars. The image-view list has the whole, both halves and the 22 actually inspected crops.
- The mathematical-check log is empty, consistent with the work actually done. Literal parenthesis omissions in the source formulas were intentionally preserved rather than treated as LaTeX-structure failures.

## Brief feedback

The brief and exact preamble were sufficient for the page. One optional clarification would be useful: how should a reader encode a fine ink-like trace of uncertain authorial status that touches an otherwise legible letter, such as the vertical trace above b in fibres, without inventing a character or inserting a block figure into a word? I recorded it in the inventory, uncertainty list and an in-place TeX comment. This did not justify an additional crop or another view of the half.
