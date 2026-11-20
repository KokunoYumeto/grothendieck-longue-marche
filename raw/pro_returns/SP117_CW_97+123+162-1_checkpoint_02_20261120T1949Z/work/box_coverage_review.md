# Pre-blind box coverage review

The text audit in `scripts/audit_box_coverage.py` is a coverage aid only. It does not read images, infer characters, or decide readings. Root compared its candidates with the written box readings and the inventory. A long insertion or cancellation can occupy consecutive boxes; the complete passage remains in the page file.

## First eleven committed pages

| Page | Candidate | Coverage and disposition |
|---|---|---|
| 123/002 | Bibliographic margin | b02 includes the entire title and th. 9.2.; the apparent mismatch is `\quad` spacing. |
| 123/002 | Oval and leader above title | b01 includes the word and shape. Descriptive text in its first reading was replaced with the page's TikZ representation before the blind reader received it. |
| 123/002 | Three marginal rules | b36, b37, b38. TikZ coordinate formatting differs from the page; the same complete rules are covered. |
| 123/002 | Circular insertion call after correspondant | b39 covers the circle and stem. Root checked existing evidence crop b37, explicitly represented the call in the page, and logged root25. |
| 123/016 | Insertion beginning et x est de la forme | P016.B18 and P016.B19 cover its two lines, including the whole map formula. |
| 123/016 | Cancelled b′ clause | P016.B20 contains the whole clause and formula. The mismatch is the serialization of a prime. |
| 123/018 | espace homogène insertion | b32 and b33 cover the wrapped word pair, with the two cancelled torseur fragments. |
| 123/018 | de stabilisateur and parenthetical question | b34 and b35 contain the full two-line insertion. |
| 123/018 | Cancelled Isom clause | b36 and b37 contain the complete two-line cancellation. |
| 123/019 | Inserted quasi-déployé parenthesis | B10 and B11 together contain all inserted text and the replaced wording. |
| 123/019 | Cancelled i.e. clause | B10 and B11 together contain the complete cancellation. |
| 123/019 | Small square diagram | B07 covers the entire diagram, both doubtful objects, and all four arrows. The text mismatch is TikZ layout options. |
| 123/022 | Bottom NB extension and order | b22, b23, and b24 cover the complete three-line marginal note, including the formula, cancelled suffix, centre label, and order. |
| 97/019 | Slanted margin annotation | b09 covers the complete note. The page positions its lines using TikZ nodes. |

The cover 162-1/002 adds five boxes: title, ruled III, faint parenthetical, isolated nontext trace, and archive number. The trace is an extra audit box; it is not counted as source text or as a drawing.

All 199 insertion, deletion, margin, and manuscript-page-number macro occurrences in the first ten pages were either text-matched by the aid or individually accounted for above. This is not a claim that a text search alone can establish spatial coverage. The image reading and the per-page box/inventory decisions supply that evidence. Handwritten operators, digits, and whole doubtful formulas also have their own boxes in the per-page lists.

## Typescripts 123/028 and 123/040

The rerun after thirteen committed pages examined 266 macro occurrences and returned seventeen textual candidates, all accounted for by the earlier table or below.

| Page | Candidate | Coverage and disposition |
|---|---|---|
| 123/028 | Whole paragraph inside the global cancellation | 028-B042 through 028-B048 cover the full body paragraph in consecutive context boxes. The local cancellations and handwritten signs also have individual boxes 028-B006 through 028-B028. The footnote has context box 028-B049 and detail boxes 028-B030 through 028-B040. |
| 123/040 | Insertion beginning De plus | b09 covers every word and the call mark; b45 covers the complete associated top-note frame. The textual mismatch is the page-level frame serialization. |
| 123/040 | Insertion beginning Par suite | b18 covers every word, both local cancellation/insertion layers, and the call mark; b46 covers the associated bottom note and frame. |

No page's `_first.tsv` will be rewritten after its blind `_second.tsv` has been received. This audit is a check of the mandatory reading scope, not a substitute for reading the boxes from the scan.

## Handwritten-symbol coverage supplement

A separate content check of all 323 handwritten-wrapper occurrences on the first thirteen pages left sixteen textual candidates. Most were portions of an already covered paragraph or diagram. The root inspected the whole-page images of 97/019 and 123/017 and added three explicit formula boxes: 97/019 b32 (Y intersection U), and 123/017 b30,b31 (the two handwritten arrows with their domains and codomains). The current page readings are unchanged. Boxes are selections for the independent second reading; no duplicate first-stage crop was made.
