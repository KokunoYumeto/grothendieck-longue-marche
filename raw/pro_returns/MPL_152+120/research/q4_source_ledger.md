# Q4 source and search ledger

This ledger accompanies `q4_shiota.md`. Research began only after the frozen transcription and after reading `context/README.md` and `context/notes/RESULTS_STATE.md`; the supplied 38 images were never opened by this worker. All external source downloads and rendered images remain in `research_sources/`, outside the deliverable tree. The source records below distinguish a directly checked primary text from metadata or an unsuccessful access attempt.

## Primary texts actually used

| ID | Exact source URL | Checked location | Retrieval / web references | Local evidence |
|---|---|---|---|---|
| S1 | https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/EsquisseFr.pdf | §5, printed pp. 29–30 = PDF pp. 25–26: comparison map and subsequent authorial proof-status paragraph; preceding printed p. 28 also read | `turn10view0`; focused reads `turn14view1`, `turn17view4`; final verification `turn57view0` | `research_sources/esquisse-fr.pdf`, `.txt` |
| S2 | https://arxiv.org/pdf/1002.1508 | v3; Lemma 1.1 and conjugacy discussion p. 2; definitions and Lemma 1.2 p. 3; Theorem 2.1 p. 5; Complement p. 17; definitions/Lemma 3.3 pp. 36–37 and portions of proof read | `turn10view1`; theorem `turn14view2`; Complement `turn17view1`; Lemma 3.3 `turn14view3`; Lemma 1.1 final verification `turn57view1` | `research_sources/shiota-1002.1508.pdf`, `.txt` |
| S2 published metadata | https://link.springer.com/article/10.1007/s00222-013-0467-y | Title, abstract/Theorem 1.1 description, volume 196 (2014), pp. 163–232; no claim of full publisher-text access | `turn22view0` | No separate download |
| S3 | https://arxiv.org/pdf/1310.5489 | Exact identifier https://arxiv.org/abs/1310.5489v3 ; definitions pp. 2–3; extension hypotheses p. 5; Corollary (i) p. 6; isotope definitions p. 8; uniqueness and Supplement p. 9; standard-model definition p. 11; Theorem 4 p. 13; Statement 9 p. 19; Corollary proof p. 41 | `turn10view2`; targeted `turn17view5`; Supplement final verification `turn57view2` | `research_sources/shiota-1310.5489.pdf`, `.txt` |
| S4 | https://www.researchgate.net/publication/228392940_An_introduction_to_O-minimal_geometry | Author-uploaded full text of Coste, *An Introduction to O-minimal Geometry*: §5.7, definitions preceding Theorem 5.22 and theorem/proof pp. 61–63; Corollaries 5.25 and 5.27 plus adjacent limitation also inspected | `turn44view0`; exact theorem `turn45view1`; proof `turn45view2`; final verification `turn57view3` | Web full text; page labels the upload author content |
| S5 metadata | https://www.jstor.org/stable/i340835 | Journal table of contents: Hardt, *American Journal of Mathematics* 102(2), 291–302 (1980) | `turn29search0` | No full text obtained |
| S6 | https://grothendieck.umontpellier.fr/121.pdf | Scans/PDF pp. 30–37 (footer numbers 29–36; handwritten pp. 31–38); scans/PDF pp. 70–73 (footer numbers 69–72; handwritten pp. 71–74) | Official archive URL established by the tame-axioms worker; that worker downloaded the PDF, this worker directly inspected the specified pages | `research_sources/121-ranged.pdf`; own renderings `research_sources/q4-121-pages/pdf030.png`–`pdf037.png`, `pdf070.png`–`pdf073.png` |

### Exact use and limits

- **S1:** Used for the displayed map of isomorphism families, the two stated comparison levels, the named extensions to map families and systems, and the author's reserved proof status. Q4 does not infer the date of cote 120 from this text.
- **S2:** Lemma 1.1's hypotheses were checked against both worked diagrams; its sources cannot repeat and its arrow system has no directed cycle. In Lemmas 1.2 and 3.3, `Iso` denotes isotopy classes of embeddings, so Q4 does not replace that term with homeomorphisms onto the whole target; those lemmas are retained as checked leads, not silently used to establish Grothendieck's entire comparison.
- **S3:** In the draft, Corollary (i) is used in its same-field case, with inclusion of o-minimal structures. The more general passage assumes an ordered field extension, compatible set-extension correspondences preserving the specified Boolean/product/projection operations and basic field/order relations, and preservation of continuous function graphs. The noncompact result uses the author's standard semilinear models; a full noncompact arbitrary-semilinear uniqueness assertion is not inserted.
- **S4:** This is the author's complete exposition, including a proof of the version actually applied. The exceptional-set refinement, graph-closure relation, and finite-poset rotation calculation are written out independently in Q4's appendices.
- **S5:** Used for bibliographic attribution only. Original Hardt text was not checked; exact mathematical content is sourced to S4.
- **S6:** PDF 30 (footer 29) defines local product/open-embedding data; PDF 31–34 (footers 30–33) develops leaves, filtrations, and admissible systems; PDF 35 (footer 34) labels Conjecture 2 and visibly revises the partition terminology; PDF 36–37 (footers 35–36) sketches a construction for a proper map. The last four inspected pages concern compact C-module/space constructions, finite gluing and a pushout question. No transcription of those external pages is offered as a completed diplomatic reading.

## Unsuccessful accesses and unused leads

| URL / item | Result | Treatment |
|---|---|---|
| https://perso.univ-rennes1.fr/michel.coste/polyens/OMIN.pdf | Web timeout and direct HTTP 503 | Replaced with the author-uploaded full text S4; original URL retained in bibliography |
| https://perso.univ-rennes.fr/michel.coste/polyens/OMIN.pdf | Access failed | No content attributed |
| https://www.jstor.org/stable/2374240 and https://www.jstor.org/stable/pdf/2374240.pdf | Full text unavailable / redirect without article content | S5 metadata only |
| https://www.ams.org/tran/1984-286-02/S0002-9947-1984-0760983-2/S0002-9947-1984-0760983-2.pdf | HTTP 403 | Shiota–Yokoi 1984 theorem not used as a checked source |
| https://arxiv.org/pdf/0806.0476 | Hardt–Lambrechts–Turchin–Volić, §2.1, checked as an additional primary Hardt reference (`turn31view0`) | Not used because S4 gives the precise compatible-subset version required |

An initially guessed AMS identifier ending `-8` and a guessed Coste `Pisa.pdf` path also failed; neither supplies evidence. Citation records identify only the verified source URLs above.

## Context search audit

`q4_context_searches.json` records actual regex searches, hit file, line number, nearest `\\scanpage` where available, and matched text for each Q4 item. Searches covered all supplied context `.md` and `.tex` files, including the status register; the selected context passages were then read, and the research notes give their scan locators and the relation to the new item. An unreviewed status register return is preserved as a claim rather than silently promoted to a theorem.

| Item | Search terms / notation |
|---|---|
| Q4-01 | `isotop`, `comparaison`, `modér`, `système` |
| Q4-02 | `Shiota`, `Hauptvermutung`, `triangul`, `isotop` |
| Q4-03 | `loc.`, `homeom`, `triangul`, `Shiota` |
| Q4-04 | `à prouver`, `axiom`, `admet`, `comparaison` |
| Q4-05 | `trivial`, `fibré`, `fibration`, `voisinage` |
| Q4-06 | `diagramme`, `produit`, `Z_j`, `X_i` |
| Q4-07 | `diagramme`, `trivial`, `système`, `morphismes` |
| Q4-08 | `diagramme`, `morphismes`, `commutatif` |
| Q4-09 | `Z`, `produit`, `fibre` |
| Q4-10 | `Admettant`, `servira`, `trivial` |
| Q4-11 | `équisingul`, `partition`, `diagramme`, `stratifi` |
| Q4-12 | `diagramme`, `morphismes`, `système`, `isotop` |

Final web verification was a batch of exact within-source searches: `IsomT` in S1 (`turn57view0`), `Lemma 1.1` in S2 (`turn57view1`), `Supplement` in S3 (`turn57view2`), and `Theorem 5.22` in S4 (`turn57view3`). Earlier source discovery is represented by the primary URL/access records above; this ledger does not invent a minute-by-minute query history.

## Quotation control

The draft quotes only the brief isotopy-category phrase from S1 and the two-word supplement qualification from S3. Other externally sourced statements are paraphrased with formulas and exact locators; no long external passage is copied. The source labels and article titles serve as bibliography. Quotations from the supplied frozen transcription are kept separate from external-source quotations.

Recorded 2026-11-14, after direct source and context checks. The main draft and this ledger remain research artifacts for parent review; all frozen transcription files are unchanged.
