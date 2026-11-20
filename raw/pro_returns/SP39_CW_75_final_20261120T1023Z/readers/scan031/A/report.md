# Scan 031 — independent reader A

- UTC start recorded: 2026-11-20T09:50:13Z, immediately after loading the brief and allowed textual inputs and before the first image opening.
- UTC end: 2026-11-20T09:56:36+00:00.
- Identity: independent reader A; model inherited; effort not exposed.
- Overall confidence: high for the printed and typed text. Medium for the double-struck heading initial and handwritten group alphabet; the underlying deleted e remains doubtful. The origin of the opaque corner shape remains unassigned.

## Scope and source-view sequence

I read the complete v05 brief and only this scan's C.tex, H.tex, C_prior_questions.md, supplied notation snapshot, PREAMBLE.tex, and the crop helper implementation. References in prior notes to other scans supplied no visual evidence in this reading. I did not inspect another reader's material, consolidated decisions, other-page images, OCR, a text-recognition system, or external research.

The visual sequence was exactly: **full scan once → supplied half a once → supplied half b once → each of five tight crops once**. Full and half images were not reopened or enlarged after their prescribed opening. All crops were made with crop.py's documented positional interface, width 2800, rotation 0, using the whole-page source. The exact bounds, source basename, processing, and creation times are in crops.tsv. The fifth crop addresses the still-open opaque mark beside the archive number observed in the full/half reading; the physical left and bottom edges are retained in it.

## Layout and complete inventory

This is a typescript on printed university/institute stationery. The printed header occupies the upper left; the empty printed dateline is at upper right. A centered course heading and separated long rule precede an underlined topic heading. Two typed paragraphs occupy the body. The second paragraph contains a pale overwritten letter and a handwritten group capital with a low typed index. Two detached small marks occur toward the right margin between two physical text lines. Archive number 30 and an adjacent opaque oblique shape occupy the lower-left corner. No displayed equation or connected mathematical diagram occurs.

| Element | Position | Hand / medium record | Representation |
|---|---|---|---|
| University name, two lines | Upper left | Print | Both lines transcribed; serif face |
| First short rule | Beneath DU LANGUEDOC | Print | Horizontal rule |
| Institute, street address, postal line | Upper left | Print | All three lines transcribed; sans-serif face |
| Second short rule | Beneath postal line | Print | Horizontal rule |
| Montpellier, le and blank date space | Upper right | Print | Printed words and blank completion preserved |
| Course heading | Upper center | Typewriter | COURS C4 1977-78 de A. GROTHENDIECK |
| Long course rule | Below heading | Hand unassigned | Separated full-span line |
| Topic title | Left body margin | Typewriter | Complete title |
| Topic underline | Directly below title | Hand unassigned | Underline retained |
| Paragraph one | Upper body | Typewriter | Complete text |
| Paragraph two | Middle/lower body | Typewriter | Complete text |
| Pale underlying e candidate | First icosaèdre of paragraph two | Typewriter, overwritten | Deleted unsure e immediately before live c |
| Group capital | After groupe alterné, next physical line | His hand | Handwritten Fraktur A |
| Low index | Right of group capital | Typewriter | Subscript 5 |
| Detached pair | Right margin between alterné and following line | Unknown hand | Two separate filled shapes in TikZ |
| Opaque oblique shape | Lower-left corner, immediately left of 30 | Unknown hand / origin unassigned | Filled contour in TikZ |
| Archive number 30 | Lower-left corner | Unknown hand | Archive comment |

The two detached shapes have been geometrically represented without a proposed verbal meaning. The opaque corner mark also has a geometric representation; its physical origin is left open. The scattered peripheral discolorations observed in the halves have no textual reading assigned.

## Line-by-line reading record

This records the lines actually read from the supplied halves. It also identifies the printed rules, punctuation, accents, wrapping, and local signs checked. Ordinary body line wrapping is joined in page.tex.

| Source line/block | Reading and inspection record |
|---|---|
| Header 1 | UNIVERSITE DES SCIENCES ET TECHNIQUES. Capitals have visible serifs; no uppercase accent is visible. |
| Header 2 | DU LANGUEDOC. Same serif capitals, then a short horizontal rule. |
| Header 3 | INSTITUT DE MATHEMATIQUES. Larger sans-serif capitals; no uppercase accent. |
| Header 4 | Place Eugène Bataillon. Grave in Eugène; capitalization retained. |
| Header 5 | 34060 MONTPELLIER CEDEX. The 6 has an upper return and closed lower bowl; the final digit is 0. A second short rule follows. |
| Dateline | Montpellier, le. Comma present, and date space empty. I inspected the spaces following the printed words. |
| Course heading | COURS C4 1977-78 de A. GROTHENDIECK. One hyphen joins the years; one point follows A. The initial's alphabet was deferred to its crop. The other capitals were read individually. |
| Course rule | One continuous long rule, spanning roughly the heading width, about one typing line below it. |
| Topic | Géométrie de l'icosaèdre. Upright typed letters; acute and grave accents inspected; full close underline. |
| Paragraph 1, line 1 | Il est étrange que l'icosaèdre, étudié depuis plus de deux mille ans — accents on étrange, icosaèdre and étudié, comma after icosaèdre. |
| P1, line 2 | dans des contextes et des optiques très divers, ne semble jamais avoir été — très and été accents, plural divers, comma. |
| P1, line 3 | étudié systématiquement du point de vue combinatoire, ni de celui des réali- — two accents at the opening; comma; line-wrap hyphen after réali. |
| P1, line 4 | sations géométriques sur des corps (voire des anneaux) généraux. Ce "cours" — joins réalisations; both parentheses, full stop, and two high quotation strokes on each side of cours. |
| P1, line 5 | se voudrait une investigation commune sur ce thème, en partant de l'intuition — grave on thème, comma, apostrophe. |
| P1, line 6 | combinatoire la plus naïve, exemplifiée sur des modèles en carton (avec un — diaeresis in naïve, acute in exemplifiée, grave in modèles, comma, opening parenthesis. |
| P1, line 7 | coloriage convenable des arètes). — single grave accent on arètes, closing parenthesis, full stop. |
| Paragraph 2, line 1 | Nous aborderons donc la théorie de l'icosaèdre d'un point de vue — théorie and icosaèdre accents; pale extra stroke at c deferred to crop. |
| P2, line 2 | combinatoire d'abord, en explicitant dans le détail le dictionnaire entre la — apostrophe, comma, accent in détail. |
| P2, line 3 | géométrie combinatoire de l'icosaèdre orienté, et celle de l'ensemble "orienté" — both accent forms, comma, paired high quotation strokes. |
| P2, line 4 | à cinq éléments (les cinq couleurs coloriant les arètes !) - ce qui donnera — à and éléments accents, second grave in arètes, spaced exclamation mark, parenthesis, one short dash. |
| P2, line 5 | en même temps une motivation et une inspiration géométrique pour étudier le — circumflex in même and acute accents. |
| P2, line 6 | groupe des automorphismes commun aux deux situations, savoir le groupe alterné — commun as written, comma, acute in alterné. |
| P2, between lines 6–7 | Two separate compact dark marks at the right, outside the text; deferred to crop. |
| P2, line 7 | Handwritten group capital with low 5, then (qui est aussi le plus petit groupe simple non abélien). La question de — alphabet deferred to crop; parentheses, accent, full stop retained. |
| P2, line 8 | construire des "réalisations géométriques" de l'icosaèdre combinatoire, comme — two paired quotation signs, accents, apostrophe, comma. |
| P2, line 9 | "polyèdre régulier" sur le corps des réels, ou sur tout autre corps, sera — both quote pairs and accent types, two commas. |
| P2, line 10 | l'occasion à la fois d'approfondir la compréhension de la structure combinatoire, — apostrophes, à, acute in compréhension, final comma. |
| P2, line 11 | et de nous familiariser avec les notions de géométrie vectorielle et affine — complete line and accent checked. |
| P2, line 12 | (voire de géométrie projective) sur des corps de caractéristique quelconque. — parentheses, no intervening comma after projective), accents and final point. |
| Lower-left corner | 30 read as archive number. The adjacent dark oblique shape was deferred to an edge-preserving crop. |

## Differences from C and H, including every C doubt

The structured review has one locus per distinction, with H_marked false throughout: the supplied H has no uncertainty marker at these loci. Its introductory handwriting note is a statement of medium/alphabet, not a doubt mark. H's single archive wrapper difference and its alternate literal-double-quote syntax are excluded as representation-only differences.

1. **031-A-01 — H's printed-header omission.** The complete university/institute header, two short rules, address, postal code and Montpellier, le are read from half a. H identifies the stationery in a note without transcribing the printed block. That absence is recorded once for the whole block. C's words agree.
2. **031-A-02 — C's printed face for the first two lines.** The university's two small-capital lines show terminal serifs. The larger institute/address block has its own sans-serif face. C makes the entire block sans serif. page.tex preserves the visible division. This is a typography distinction, not a new word reading.
3. **031-A-03 — heading initial.** Crop shows a thick right limb and a second offset projection at the lower-right foot. I retain C's `\mathbb A` under the supplied convention for double-struck typed letters. H has ordinary A. The heading letter was judged from its own strokes; no other-page A was consulted. Confidence medium.
4. **031-A-04 — course rule.** C's lowered full-span underline preserves the visible detached rule. H has the course-heading text without the rule. Half a settles its span and placement. No crop was made of this settled place.
5. **031-A-05 — topic underline.** C preserves the underline; H sets the words in italic. The source's close underline beneath upright typed letters is clear in half a.
6. **031-A-06 — underlying e candidate.** A pale sloping crossstroke survives inside the live c of the first icosaèdre in paragraph two. I retain `\deleted{\unsure{e}}` before the c. The faint trace supports the e candidate without fully settling the erased glyph. Thus diff_C is false, diff_H true, unresolved true. H's text supplies only the live word.
7. **031-A-07 — short dash.** The dash following arètes !) occupies approximately one typing cell. I retain C's one hyphen-like stroke; H uses `--`. Half b settles this.
8. **031-A-08 — group alphabet.** The crop shows a folded upper return, rounded outer left limb and broken angular inner return descending to the right foot. I read handwritten `\mathfrak A`, resolving C's `\mathfrak A|\mathcal A` doubt. H's Fraktur reading agrees. The low 5 is preserved separately as typed. Confidence medium. No group-theoretic argument supplies the alphabet reading.
9. **031-A-09 — detached right-margin pair.** Both witnesses omit two compact dark shapes centered about (1582,1659) and (1577,1666). The upper is to the right and is slightly elongated; the lower is roughly triangular. page.tex contains a margin TikZ rendering. I assign no punctuation value, verbal reading, or authorial hand.
10. **031-A-10 — opaque lower-left shape.** Both witnesses omit the connected irregular oblique dark shape left of archive 30. Its crop preserves the physical left/bottom edge. page.tex reproduces its contour in a left margin figure. Geometry is visible, with medium confidence in the coarse contour. The origin remains unresolved; no deleted textual content is asserted.

No other word, accent, punctuation, paragraph, index, or live/deleted-state difference was found against the supplied witnesses. In particular, the supplied C and H already agree on **arètes** both times; both grave accents were independently read. The two quotation strokes were counted at every side of each of the four quoted phrases. The 5 is low to the right of the handwritten capital. There is no added comma after projective).

## Crops and coordinate evidence

All coordinates are in the 1689 × 2366 whole-page source. All five crops use output width 2800, rotation 0, autocontrast, LANCZOS enlargement and UnsharpMask(1.0,130,3), as recorded by crop.py.

| Crop filename | Bounds [x0,y0,x1,y1] | Decision |
|---|---|---|
| scan031_A_heading_initial.png | [780,518,1110,583] | Retain double-struck heading A; medium |
| scan031_A_overtyped_icosaedre.png | [954,1240,1270,1320] | Retain deleted unsure e; medium |
| scan031_A_group_capital.png | [238,1643,650,1727] | Resolve handwritten Fraktur A and low typed 5; medium |
| scan031_A_right_margin_pair.png | [1430,1582,1689,1728] | Two geometric marks, origin unassigned; high for presence/placement |
| scan031_A_archive_corner.png | [0,2245,145,2366] | Archive 30 and adjacent opaque shape; medium for contour, origin unresolved |

Half-settled differences have approximate full-source boxes in review.json: complete header [145,125,1128,344]; serif university lines [145,126,660,181]; long rule [490,602,1104,622]; topic underline [258,727,668,770]; short dash [1170,1465,1301,1504]. These were sent to the main reader together with crop names. No additional enlargement was used to revisit a decided place.

## Mathematical reading and actual checks

I read the inline expression as a handwritten Fraktur capital A with a low typed 5, inspected its alphabet and attachment, and preserved the surrounding mathematical claims verbatim. **No proof or numerical calculation occurred.** Reading the assertion about the smallest simple nonabelian group is recorded only as a source-reading event. Accordingly check_events is empty. No conditional theorem, hypothesized correction, or mathematical reconstruction is proposed.

Static file checks passed: brace balance after removing comments; four unescaped dollar delimiters; properly nested minipage, center and tikzpicture environments; paired control/display delimiters with backslash-run parity; required JSON locus fields; and five manifest entries whose crop files exist. No compiler or TeX format builder was invoked. These are transcription-file checks, not mathematical checks.

## Proposed notation records and abbreviations

- Heading `\mathbb A` has its own offset right-foot evidence and a separate following period.
- The local group capital is recorded as handwritten `\mathfrak A`, with the typed low 5 outside the handwritten wrapper.
- The pale overwritten glyph remains `\deleted{\unsure{e}}` immediately before live c.
- All four quote pairs use two high strokes at either end.
- Both arètes accents are graves.
- C4, A. and CEDEX remain exactly as written, without expansions in the transcription.

## Workflow problem and improvement

The initial combined file-write tool call failed **before process creation** with `exec-server transport disconnected`. A subsequent pwd call succeeded; I wrote the same intended material in smaller calls. I informed the main reader. The failure caused no new source opening, repeated crop, additional witness access, or compilation. The final four required files are present. Keeping write calls modest in size is the only practical improvement identified in this session.
