# The Montpellier Manuscripts: a place for everything

11 November 2026, by Claude (Fable 5.2), continuing `ORGANIZATION_RECOMMENDATION.md` (Claude Fable 5.2, 10 November,
adopted by the user). That file placed the first tranche (ranks 0-11) with care and the rest in one table. This file
gives every one of the 178 cotes (16,074 site pages) a book, a chapter, a position in the reading order, a route and a
package, and says what follows each book once it is transcribed. Machine-readable: `PLACEMENT_EVERYTHING.csv`, one row
per cote (plus one row for cote 110).

Basis: `ORGANIZATION_RECOMMENDATION.md`, `PLAN_EVERYTHING.md`, `SECTIONS_STATE.md`, `MANIFEST.csv` and `MANIFEST.json`
(the archive's notes), the prompt template and the check of package 1. All 178 PDFs are now on disk. Pages opened to
settle a placement (nothing transcribed): cotes 93, 129, 133, 152, 153, 155. Every other placement rests on the
archive's titles and notes.

Conventions. "Pages" are the site's page counts. Each PDF has one cover sheet before them, so a cote of n pages has
scans 2 to n+1; package boundaries are given in scan numbers, as the packager names them (`MPL_1_002-050`). "Rank" is
the transcription rank of the earlier file; "T" marks the clean-typescript route, which is outside the ranking.

## 1. The shape in brief

| Part | Chapters | Cotes | Site pages | Route |
|---|---|---|---|---|
| Front door: the Esquisse, annotated | 2 | 3: 119 (the Esquisse), 161-3, 161-4 | 398 with all of 119 | API (119); Pro |
| I. Elements, continued | 8, on his plan of the EGA | 51 | 3,158 | Pro; API for 24, 25 |
| II. Cohomology and motives | 9 | 29 | 2,397 | Pro; API for 129 |
| III. The Long March | 7 | 17 | 2,922 | 1,584 done (140); Pro |
| IV. Maps and polyhedra | 6 | 20 | 1,954 | Pro |
| V. Tame topology and the geometry of forms | 5 | 18 | 1,319 | Pro |
| VI. Stacks and derivators | 7 | 34 and the slot of cote 110 | 3,702 | 2,135 done through the printed edition (157); API for 134, 162-5; Pro |
| Workshop | 3 | 6: 1, 66, 68, 139, 162-1, 162-6; and the rest of 119 | 224 | Pro; concordance only for 139 |
| **All** | **47** | **178** | **16,074** | |

By route: Pro mode 10,761 pages (94 of them sent already: packages 1 and 2); API, clean-scan route, 1,592; done 3,719
(*La Longue Marche* 1,584, *Les Dérivateurs* 2,135); concordance only 2.

Pro prompts for everything: **134 at 90 scans a package, 254 at 45**, the two packages already sent included
(132 and 252 still to send). These are upper bounds: blank sheets drop out at packaging (about 8 % in the
pilot), and typed sheets found by the inventory of section 4 move to the API route.

## 2. A place for everything: the books, chapter by chapter

The books are the reading order: front door, I to VI, workshop; inside a book the chapters in order; inside a chapter
the positions in order. The archive's own order (cote, scan) stays as the second index.

### Front door: the Esquisse, annotated

The reader's first page. D.1 is the Esquisse of January 1984, cut out of the CNRS dossier (cote 119) and linked section by section to the books; the rest of the dossier is filed in the Workshop. D.2 holds the two texts in which he explains to beginners; each is also the first reading of a book (161-4 of Book I, 161-3 of Book VI).

**D.1. The Esquisse, annotated** (313 pp.). Links: Every book (each section of the Esquisse links to one); Longue Marche edition and book (Esquisse §2).

| Pos. | Cote | Pages | Contents | Rank | Route |
|---|---|---|---|---|---|
| 1 | 119 | 313 | The CNRS dossier of 1984: the Esquisse (57 pp.), activity report, course programmes 1973-74 and 1978-79, CV 1972, letters | T | API (clean-scan route) |

**D.2. Two presentations in his explaining voice** (85 pp.). Links: Open Mathematics Courses; EGA edition (French transcription and translations) I (161-4); SGA 4 edition (161-3).

| Pos. | Cote | Pages | Contents | Rank | Route |
|---|---|---|---|---|---|
| 1 | 161-4 | 31 | Introduction to algebraic geometry, a presentation for beginners (perhaps for Vietnam) | 16 | Pro mode |
| 2 | 161-3 | 54 | Topos, a presentation for beginners | 16 | Pro mode |

Book total: 398 site pages.

### Book I. Elements, continued (EGA V and after)

The chapters follow his plan of the EGA after chapter IV as our records give it (projective methods; construction techniques; group schemes and torsors; Picard schemes; residues and duality; intersections and Riemann-Roch; étale cohomology). The plans themselves (26, 48, 102, 35) are transcribed at rank 3; they fix the final chapter numbers and titles, and a folder moves if his plan puts its subject elsewhere. Opening text: the plan, with each chapter marked written, drafted or unwritten; then "Nouveau EGA V" (25).

**I.0. The plan, and complements to EGA 0-IV** (316 pp.). Links: EGA edition (French transcription and translations) 0_III, 0_IV, IV; French-school site.

| Pos. | Cote | Pages | Contents | Rank | Route |
|---|---|---|---|---|---|
| 1 | 26 | 10 | EGA VI: plans, notations, open problems | 3 | Pro mode |
| 2 | 48 | 5 | Plan of EGA VII | 3 | Pro mode |
| 3 | 21 | 28 | Chapter 0_III, unpublished typescript with notes | 3 | Pro mode |
| 4 | 22 | 29 | 0_IV complements: Cohen rings, differentials, formally smooth algebras | 3 | Pro mode |
| 5 | 23 | 98 | EGA IV complements, with letters of 1966 and 1968 | 3 | Pro mode |
| 6 | 32 | 47 | Corrections, references and additions (SGA 4 among them), with Deligne's notes | 21 | Pro mode |
| 7 | 37 | 99 | Re-editions of SGA 4-7 and EGA I-II, letters 1967-71 | 24 | Pro mode |

**I.V. Chapter V: hyperplane sections and projective methods** (268 pp.). Links: EGA edition (French transcription and translations) II, IV §§16-21; SGA 7 edition (XVII-XVIII); French-school site.

| Pos. | Cote | Pages | Contents | Rank | Route |
|---|---|---|---|---|---|
| 1 | 25 | 184 | "Nouveau EGA V", annotated typescript, with a 1965 letter to Dieudonné | T | API (clean-scan route) |
| 2 | 24 | 76 | EGA V, English translation materials (Blass, 1987) | T | API (clean-scan route) |
| 3 | 125 | 8 | Projective duality (before 1970) | 22 | Pro mode |

**I.VI. Chapter VI: construction techniques (descent, representable functors, Hilbert and Hom)** (382 pp.). Links: FGA edition (Bourbaki 190, 195, 212, 221); SGA 1 edition (VI, VIII); EGA edition (French transcription and translations) III-IV; Stacks-format lessons in the Open Mathematics Courses.

| Pos. | Cote | Pages | Contents | Rank | Route |
|---|---|---|---|---|---|
| 1 | 102 | 13 | General study of functors (Sch)° → (Ens), with a typescript for EGA VI | 3 | Pro mode |
| 2 | 126 | 34 | Faithfully flat descent | 22 | Pro mode |
| 3 | 127 | 23 | Non-flat descent | 22 | Pro mode |
| 4 | 128 | 31 | Non-flat descent, formal modules (cf. Murre-Levelt), with Deligne's notes | 22 | Pro mode |
| 5 | 131 | 41 | Functors representable by quasi-finite schemes (c. 1971) | 22 | Pro mode |
| 6 | 98 | 43 | Hilbert schemes, norms | 20 | Pro mode |
| 7 | 91 | 142 | Around Néron and Greenberg-Néron; Hom functors by non-projective methods (letter 1967) | 20 | Pro mode |
| 8 | 41 | 13 | Construction of étale morphisms ("Chap. V") | 21 | Pro mode |
| 9 | 39 | 19 | "Elementary" functions and structures: formal schemes, preparation theorem | 21 | Pro mode |
| 10 | 42 | 6 | Lattices of local rings | 21 | Pro mode |
| 11 | 55 | 17 | Analytic spaces | 19 | Pro mode |

**I.VII. Chapter VII: group schemes and torsors** (301 pp.). Links: SGA 3 edition; FGA edition.

| Pos. | Cote | Pages | Contents | Rank | Route |
|---|---|---|---|---|---|
| 1 | 45 | 79 | Semisimple groups (typescript 1961, notes) | 19 | Pro mode |
| 2 | 27 | 36 | SGA 3, complements XII-XVII | 24 | Pro mode |
| 3 | 28 | 10 | Algebraic groups (SGA 3), "Demazure 5.2.1970" | 24 | Pro mode |
| 4 | 160 | 22 | Group schemes (the subject of SGA 3 III) | 24 | Pro mode |
| 5 | 46 | 94 | Group schemes and principal bundles, miscellany | 19 | Pro mode |
| 6 | 40 | 27 | Affine calculations on principal affine bundles | 21 | Pro mode |
| 7 | 53 | 33 | Algebraic groups (letter 1973) | 19 | Pro mode |

**I.VIII. Chapter VIII: Picard schemes, Jacobians, abelian schemes, elliptic curves** (864 pp.). Links: FGA edition (Bourbaki 232, 236); SGA 2 edition; SGA 7 edition (I, VII-IX); Book III ch. 6 (elliptic curves).

| Pos. | Cote | Pages | Contents | Rank | Route |
|---|---|---|---|---|---|
| 1 | 57 | 314 | "Picard": annotated typescript and letters of 1962 | 23 | Pro mode |
| 2 | 59 | 27 | Construction of invertible sheaves on Picard schemes | 19 | Pro mode |
| 3 | 58 | 66 | "Lefschetz-Grauert" theory, applications to π₁ and Pic | 19 | Pro mode |
| 4 | 43 | 207 | Duality of groups, generalized Jacobians (1961-c. 1968) | 19 | Pro mode |
| 5 | 49 | 9 | Picard of abelian schemes | 19 | Pro mode |
| 6 | 50 | 10 | On Lang's book | 19 | Pro mode |
| 7 | 51 | 22 | "Good reduction" (Shimura-Koizumi) | 19 | Pro mode |
| 8 | 52 | 13 | Torelli theorem | 19 | Pro mode |
| 9 | 62 | 96 | Elliptic curves, generalities, "old draft" (from 1963) | 23 | Pro mode |
| 10 | 63 | 100 | Formulary for elliptic curves (notes, typescript, article copies) | 23 | Pro mode |

**I.IX. Chapter IX: residues, duality, local cohomology** (65 pp.). Links: SGA 2 edition; EGA edition (French transcription and translations) III; French-school site.

| Pos. | Cote | Pages | Contents | Rank | Route |
|---|---|---|---|---|---|
| 1 | 101 | 42 | Local cohomology | 20 | Pro mode |
| 2 | 94 | 23 | Duality of modules; construction of sheaves of modules | 20 | Pro mode |

**I.X. Chapter X: intersections, Chern classes, Riemann-Roch** (86 pp.). Links: SGA 6 edition; French-school site (Borel-Serre 1958).

| Pos. | Cote | Pages | Contents | Rank | Route |
|---|---|---|---|---|---|
| 1 | 2 | 44 | Riemann-Roch, "notes antiques" (before 1958) | 25 | Pro mode |
| 2 | 90 | 24 | K_G(X) | 20 | Pro mode |
| 3 | 97 | 18 | Chern classes of representations (letter 1966) | 20 | Pro mode |

**I.XI. Chapters XI-XII: étale cohomology, fundamental group, monodromy** (876 pp.). Links: SGA 1, SGA 4, SGA 5, SGA 7 editions; Book III (fundamental groups).

| Pos. | Cote | Pages | Contents | Rank | Route |
|---|---|---|---|---|---|
| 1 | 29 | 216 | Fundamental group, around SGA 1, 4 and 7 (letters 1959, 1967, 1969) | 24 | Pro mode |
| 2 | 31 | 101 | SGA 4, "résidus de rédaction", with Deligne's notes | 21 | Pro mode |
| 3 | 33 | 180 | "SGA 1965. MS brouillon" | 21 | Pro mode |
| 4 | 35 | 5 | Plan of SGA 7 | 3 | Pro mode |
| 5 | 36 | 84 | "SGA 7 (ma part)", with Deligne's notes | 21 | Pro mode |
| 6 | 34 | 209 | SGA 7 notes | 21 | Pro mode |
| 7 | 122 | 34 | Isolated singular point of the fibre (c. 1968-71) | 22 | Pro mode |
| 8 | 123 | 47 | Around Kostant (1969) | 22 | Pro mode |

Book total: 3,158 site pages.

### Book II. Cohomology and motives

Order: de Rham and crystals, Barsotti-Tate groups, Gauss-Manin, then cycles, motives and their Galois groups, tensor categories, L-functions, and last the notes of 1974-76, which lead into Book VI. Opening text: the 1967 talks (cote 7).

**II.1. De Rham cohomology and crystals** (280 pp.). Links: Stacks-format lessons in the Open Mathematics Courses; French-school site (Dix exposés).

| Pos. | Cote | Pages | Contents | Rank | Route |
|---|---|---|---|---|---|
| 1 | 7 | 71 | Notes for the talks of November-December 1967 on crystals | 7 | Pro mode |
| 2 | 5 | 52 | Crystals and de Rham cohomology: generalities, letter to Deligne (1965) | 7 | Pro mode |
| 3 | 6 | 66 | Letter to Tate (May 1966), with typescript and notes | 7 | Pro mode |
| 4 | 4 | 11 | Torsion in crystalline cohomology | 7 | Pro mode |
| 5 | 8 | 80 | "Cristaux (1970)": scribbles and calculations | 7 | Pro mode |

**II.2. Barsotti-Tate groups** (222 pp.). Links: SGA 7 edition (IX); French-school site (Montréal lectures; Illusie 1985).

| Pos. | Cote | Pages | Contents | Rank | Route |
|---|---|---|---|---|---|
| 1 | 9 | 28 | Barsotti-Tate groups and crystals (to summer 1969) | 7 | Pro mode |
| 2 | 100 | 52 | Good reduction of abelian varieties via the Barsotti-Tate group (1967-68) | 7 | Pro mode |
| 3 | 129 | 114 | Notes of the Montréal seminar of 1970 (Delale, Labute, Hakim, Messing), typed | T | API (clean-scan route) |
| 4 | 161-5 | 28 | Barsotti-Tate: annotated offprints 1967-69, notes | 15 | Pro mode |

**II.3. Gauss-Manin connections, Picard-Fuchs equations, the Cartier operation** (235 pp.). Links: Book I ch. VIII (elliptic-curve formulary, cote 63); French-school site (Katz 1970).

| Pos. | Cote | Pages | Contents | Rank | Route |
|---|---|---|---|---|---|
| 1 | 93 | 235 | Gauss-Manin connections, Picard-Fuchs equations, Cartier operation ([1972]-1981) | 15 | Pro mode |

**II.4. Duality on abelian varieties, intermediate Jacobians** (25 pp.). Links: Book I ch. VIII; French-school site.

| Pos. | Cote | Pages | Contents | Rank | Route |
|---|---|---|---|---|---|
| 1 | 47 | 10 | Convolution product and Fourier transform on abelian varieties | 2 | Pro mode |
| 2 | 54 | 7 | Duality in the cohomology of abelian varieties | 2 | Pro mode |
| 3 | 44 | 8 | Intermediate Jacobians (letter to Serre, 1964) | 2 | Pro mode |

**II.5. Algebraic cycles and the standard conjectures** (281 pp.). Links: Standard-conjectures card; SGA 7 edition (vanishing cycles); SGA 5 edition; French-school site.

| Pos. | Cote | Pages | Contents | Rank | Route |
|---|---|---|---|---|---|
| 1 | 16 | 55 | Algebraic formalism of correspondences, Poincaré-Hodge algebras (letters 1966-67) | 2 | Pro mode |
| 2 | 14 | 131 | Algebraic cycles: conjectures of Hodge, Tate, Lefschetz, Weil | 6 | Pro mode |
| 3 | 11 | 57 | Formalism of correspondences | 13 | Pro mode |
| 4 | 56 | 38 | Lefschetz-Hodge, vanishing cycles (1962) | 13 | Pro mode |

**II.6. Motives and their Galois groups** (506 pp.). Links: Book III (the same Galois group through fundamental groups: Longue Marche §§1-5, 35-36); French-school site.

| Pos. | Cote | Pages | Contents | Rank | Route |
|---|---|---|---|---|---|
| 1 | 13 | 51 | Motivic Galois group (letter 1965) | 6 | Pro mode |
| 2 | 12 | 167 | Generalities, motivic Galois subgroups (1964?-c. 1971); source of "Motifs" | 6 | Pro mode |
| 3 | 15 | 227 | Arithmetic theory, Galois theory of motives (1965) | 6 | Pro mode |
| 4 | 18 | 61 | Motives and Hodge theory (c. 1969-72) | 6 | Pro mode |

**II.7. Tensor categories** (207 pp.). Links: French-school site (Saavedra; Deligne-Milne); Book VI ch. 1.

| Pos. | Cote | Pages | Contents | Rank | Route |
|---|---|---|---|---|---|
| 1 | 10 | 197 | Tensor categories (notes, typescripts) | 13 | Pro mode |
| 2 | 155 | 10 | A ⊗-category with a fibre functor over an extension k'/k: "exprimer la rigidité de C" (1984) | 5 | Pro mode |

**II.8. L-functions, heights and local symbols** (118 pp.). Links: SGA 5 edition (XIV-XV); French-school site.

| Pos. | Cote | Pages | Contents | Rank | Route |
|---|---|---|---|---|---|
| 1 | 60 | 69 | L-functions: functional equation, geometric case | 13 | Pro mode |
| 2 | 130 | 49 | Heights and local symbols (c. 1971) | 22 | Pro mode |

**II.9. 1974-76: Witt groups, universal operations, the divided-power de Rham complex** (523 pp.). Links: Book VI ch. 4 (Pursuing Stacks ch. VI, schematization); Stacks-format lessons in the Open Mathematics Courses.

| Pos. | Cote | Pages | Contents | Rank | Route |
|---|---|---|---|---|---|
| 1 | 133 | 53 | Witt groups and quadratic forms, operations on the Burnside ring, formal groups (1974-75) | 22 | Pro mode |
| 2 | 137 | 85 | Dévissage of semi-simplicial ∂-perfect complexes, multiplicative structures (1975-76) | 8 | Pro mode |
| 3 | 136 | 375 | The divided-power de Rham complex (1975-76; the 1976 IHES lecture) | 8 | Pro mode |
| 4 | 153 | 10 | "Analyseurs": composition on k⟨T⟩, W(Ω), integer-valued polynomials (from 1982) | 5 | Pro mode |

Book total: 2,397 site pages.

### Book III. The Long March

Order by date around the manuscript: the 1978 origins, the drafts, the Longue Marche itself, the two paginated texts that continue it, the dated notes of 1981-83, the neighbouring folders, and last the arithmetic of maps, which leads into Book IV. Opening text: the fundamental anabelian conjecture, stated (Longue Marche §5).

**III.1. Origins, 1978-80: Teichmüller groupoids and the Galois action** (254 pp.). Links: Longue Marche edition and book (§§19-25).

| Pos. | Cote | Pages | Contents | Rank | Route |
|---|---|---|---|---|---|
| 1 | 146 | 133 | Teichmüller groupoids (from 1978) | 1 | Pro mode |
| 2 | 142 | 121 | Galois action on Teichmüller (from 1978) | 1 | Pro mode |

**III.2. Towards the manuscript, 1980-81** (121 pp.). Links: Longue Marche edition and book.

| Pos. | Cote | Pages | Contents | Rank | Route |
|---|---|---|---|---|---|
| 1 | 143 | 33 | Paradigms of algebraic curves, provisional version (c. 1980-81) | 4 | Pro mode |
| 2 | 145 | 37 | "Printemps 81 (vieille rédaction)" | 4 | Pro mode |
| 3 | 140-1 | 36 | Draft of the Longue Marche | - | done (second pass finishing) |
| 4 | 141 | 15 | Kummer theory?; a note on bi-tensors (from 1980) | 4 | Pro mode |

**III.3. La Longue Marche à travers la théorie de Galois (1981)** (1,548 pp.). Links: Longue Marche edition and book (this is its text); Esquisse §2.

| Pos. | Cote | Pages | Contents | Rank | Route |
|---|---|---|---|---|---|
| 1 | 140-2 | 574 | Part I, §§1-37 (ms. pp. 1-292) | - | done (second pass finishing) |
| 2 | 140-3 | 695 | Part II, variations on the loop equation (ms. pp. 293-650) | - | done (second pass finishing) |
| 3 | 140-4 | 279 | Part II, continued (ms. pp. 650 bis-787) | - | done (second pass finishing) |

**III.4. The structure at infinity of the moduli spaces, and the paginated sequel** (324 pp.). Links: Longue Marche edition and book (§§26-34); Book V ch. 3 (stratified structures).

| Pos. | Cote | Pages | Contents | Rank | Route |
|---|---|---|---|---|---|
| 1 | 147 | 189 | Structure at infinity of the M(g,ν) (ms. pp. 1-90, with contents) | 1 | Pro mode |
| 2 | 149 | 135 | Untitled paginated text (ms. pp. 1-67) | 1 | Pro mode |

**III.5. Teichmülleries, 1981-83** (254 pp.). Links: Longue Marche edition and book; letter to Faltings (1983).

| Pos. | Cote | Pages | Contents | Rank | Route |
|---|---|---|---|---|---|
| 1 | 144 | 183 | "Teichmülleries", 1981-82, with letters | 4 | Pro mode |
| 2 | 148 | 71 | Teichmüller (1983) | 4 | Pro mode |

**III.6. Elliptic curves, conformal surfaces, uniformization** (289 pp.). Links: Longue Marche edition and book (§37, §53); Book I ch. VIII (cotes 62, 63).

| Pos. | Cote | Pages | Contents | Rank | Route |
|---|---|---|---|---|---|
| 1 | 64 | 156 | Moduli of elliptic curves in characteristic ≠ 2 (1980-82) | 12 | Pro mode |
| 2 | 67 | 100 | Surgery of conformal surfaces (1977-84; letter to Bers 1984) | 12 | Pro mode |
| 3 | 159 | 33 | Projective connections and uniformization | 12 | Pro mode |

**III.7. The arithmetic of maps, 1976-78** (132 pp.). Links: Book IV ch. 2; Esquisse §3; Longue Marche edition and book.

| Pos. | Cote | Pages | Contents | Rank | Route |
|---|---|---|---|---|---|
| 1 | 138 | 132 | Maps: arithmetic study (1976-77?) | 10 | Pro mode |

Book total: 2,922 site pages.

### Book IV. Maps and polyhedra

From the courses to the research notes: icosahedron, maps, graphs and complexes, regular polyhedra over rings, polygons and cyclotomy, quadrics and quadratic forms. Opening text: the icosahedron course of 1977-78 (75, 161-6).

**IV.1. The icosahedron and the courses of 1976-78** (65 pp.). Links: Open Mathematics Courses (course material); Esquisse §4.

| Pos. | Cote | Pages | Contents | Rank | Route |
|---|---|---|---|---|---|
| 1 | 161-6 | 33 | Graphs, icosahedron (c. 1973-77) | 10 | Pro mode |
| 2 | 75 | 32 | C4 and DEA courses 1977-78 (icosahedron, regular polygons) | 10 | Pro mode |

**IV.2. Maps on surfaces** (233 pp.). Links: Open Mathematics Courses; Book III ch. 7; Esquisse §3.

| Pos. | Cote | Pages | Contents | Rank | Route |
|---|---|---|---|---|---|
| 1 | 76 | 62 | Cellular n-maps (c. 1977) | 10 | Pro mode |
| 2 | 88 | 15 | Standard maps | 10 | Pro mode |
| 3 | 70 | 125 | Geometric realisations of combinatorial structures, "old drafts" | 10 | Pro mode |
| 4 | 132 | 31 | Embeddings in surfaces (Ladegaillerie, 1974) | 18 | Pro mode |

**IV.3. Graphs, cubic complexes, convex polyhedra** (314 pp.). Links: Open Mathematics Courses.

| Pos. | Cote | Pages | Contents | Rank | Route |
|---|---|---|---|---|---|
| 1 | 69 | 119 | Cubic graphs (from 1976) | 14 | Pro mode |
| 2 | 74 | 135 | Cubic complexes | 14 | Pro mode |
| 3 | 89 | 20 | Combinatorial hexagon, (3,3)-sets | 18 | Pro mode |
| 4 | 87 | 40 | Convex polyhedra | 18 | Pro mode |

**IV.4. Regular polyhedra over rings and finite fields** (758 pp.). Links: Open Mathematics Courses; Esquisse §4.

| Pos. | Cote | Pages | Contents | Rank | Route |
|---|---|---|---|---|---|
| 1 | 86 | 32 | Regular polyhedra (from 1977) | 14 | Pro mode |
| 2 | 72 | 112 | Regular polyhedra and hyperpolyhedra, any dimension (from 1978) | 14 | Pro mode |
| 3 | 85 | 97 | 2-polyhedra and 1-polygons | 14 | Pro mode |
| 4 | 79 | 296 | Triangulated regular 2-polyhedra and rank-2 modules over Z/nZ and Z (from 1980) | 14 | Pro mode |
| 5 | 83 | 221 | Icosahedra, bi-icosahedra, Azumaya algebras of rank 4 (1982-86) | 14 | Pro mode |

**IV.5. Regular polygons and cyclotomy** (157 pp.). Links: Open Mathematics Courses.

| Pos. | Cote | Pages | Contents | Rank | Route |
|---|---|---|---|---|---|
| 1 | 73 | 28 | Polygons (from 1976) | 18 | Pro mode |
| 2 | 78 | 129 | Regular polygons and cyclotomic polynomials (from 1977) | 18 | Pro mode |

**IV.6. Quadrics, quadratic forms, SO(3)** (427 pp.). Links: Open Mathematics Courses; Book II ch. 9 (Witt groups, cote 133).

| Pos. | Cote | Pages | Contents | Rank | Route |
|---|---|---|---|---|---|
| 1 | 77 | 157 | Affine quadrics, quadratic extensions (from 1977) | 18 | Pro mode |
| 2 | 82 | 78 | SO(3) ≃ GP(1) (c. 1982) | 18 | Pro mode |
| 3 | 84 | 192 | Quadratic forms (1982-c. 1986) | 18 | Pro mode |

Book total: 1,954 site pages.

### Book V. Tame topology and the geometry of forms

By date, which is also the logical order: tame topology (1973-79), the plane-topology folders, stratified spaces (1981-82), the geometry of forms (1986). Opening text: Esquisse §5.

**V.1. Tame topology, 1973-79** (96 pp.). Links: Esquisse §§5-6.

| Pos. | Cote | Pages | Contents | Rank | Route |
|---|---|---|---|---|---|
| 1 | 121 | 72 | Tame topology (letter 1974) | 5 | Pro mode |
| 2 | 120 | 24 | Tame topology (1973, 1978-79) | 5 | Pro mode |

**V.2. Jordan, immersions, pseudolines** (348 pp.). Links: Esquisse §5; Book IV ch. 2.

| Pos. | Cote | Pages | Contents | Rank | Route |
|---|---|---|---|---|---|
| 1 | 71 | 47 | Jordan theorem (1976), with a manuscript by Contou-Carrère | 18 | Pro mode |
| 2 | 81 | 54 | Immersions of the disc and the circle (from 1981) | 18 | Pro mode |
| 3 | 80 | 72 | Systems of pseudolines (from 1981) | 18 | Pro mode |
| 4 | 154 | 175 | Systems of pseudolines (1983-84) | 18 | Pro mode |

**V.3. Stratified spaces and stratified topoi, 1981-82** (184 pp.). Links: Book III ch. 4 (cote 147); Esquisse §5; SGA 4 edition (topoi).

| Pos. | Cote | Pages | Contents | Rank | Route |
|---|---|---|---|---|---|
| 1 | 150 | 98 | Stratified spaces and conical neighbourhoods; unfolding (Dec. 1981-Jan. 1982) | 5 | Pro mode |
| 2 | 151 | 74 | Stratified topos (1981) | 5 | Pro mode |
| 3 | 152 | 12 | Category of word types; plane trees (from 1982) | 5 | Pro mode |

**V.4. Vers une géométrie des formes (1986): the final state** (397 pp.). Links: Esquisse §§5-6.

| Pos. | Cote | Pages | Contents | Rank | Route |
|---|---|---|---|---|---|
| 1 | 156-1 | 26 | I. Towards a geometry of (topological) forms (5 June 1986) | 11 | Pro mode |
| 2 | 156-2 | 18 | II. Topological realisations of networks | 11 | Pro mode |
| 3 | 156-3 | 40 | III. Networks via cuttings | 11 | Pro mode |
| 4 | 156-5 | 48 | V. Algebra of figures | 11 | Pro mode |
| 5 | 156-8 | 126 | VIII. Analysis situs, fourth version | 11 | Pro mode |
| 6 | 156-9 | 139 | IX and IX bis. Workshops ("ateliers") | 11 | Pro mode |

**V.5. The three earlier versions of Analysis situs** (294 pp.). Links: Book V ch. 4.

| Pos. | Cote | Pages | Contents | Rank | Route |
|---|---|---|---|---|---|
| 1 | 156-4 | 88 | IV. Analysis situs, first version | 17 | Pro mode |
| 2 | 156-6 | 93 | VI. Analysis situs, second version | 17 | Pro mode |
| 3 | 156-7 | 113 | VII. Analysis situs, third version | 17 | Pro mode |

Book total: 1,319 site pages.

### Book VI. Stacks and derivators

One line from 1958 to 1991. Opening text: the Tapis de Quillen (1968).

**VI.1. Categories, universal algebra, topos (1958-73)** (225 pp.). Links: SGA 4 edition; front door (161-3).

| Pos. | Cote | Pages | Contents | Rank | Route |
|---|---|---|---|---|---|
| 1 | 161-1 | 19 | Categories | 16 | Pro mode |
| 2 | 161-2 | 111 | Universal algebra, or categories (c. 1963-73) | 16 | Pro mode |
| 3 | 19 | 95 | Topos (1958-73) | 16 | Pro mode |

**VI.2. The Tapis de Quillen (1968)** (84 pp.). Links: Dérivateurs companion; Pursuing Stacks ch. I-II.

| Pos. | Cote | Pages | Contents | Rank | Route |
|---|---|---|---|---|---|
| 1 | 162-5 | 68 | Tapis de Quillen: typescript of September 1968, notes, offprint | T | API (clean-scan route) |
| 2 | 111 | 16 | Tapis de Quillen: annotated copies | 9 | Pro mode |

**VI.3. Gr-categories and the Sính correspondence (1974-75)** (75 pp.). Links: Pursuing Stacks ch. I and the Breen letters; SGA 7 edition (I, biextensions).

| Pos. | Cote | Pages | Contents | Rank | Route |
|---|---|---|---|---|---|
| 1 | 103 | 17 | Correspondence on Sính's thesis (1974) | 9 | Pro mode |
| 2 | 135 | 58 | Categories and Gr-categories (c. 1974) | 9 | Pro mode |

**VI.4. Pursuing Stacks (1983)** (837 pp.). Links: Dérivateurs companion; arXiv 2111.01000 and SMF vol. I as checks.

| Pos. | Cote | Pages | Contents | Rank | Route |
|---|---|---|---|---|---|
| 1 | 134-1 | 6 | Letters with Breen, Deligne, Quillen (1974-76, 1984) | T | API (clean-scan route) |
| 2 | 134-2 | 184 | Ch. I, Take off; provisional contents, appendix, letters | T | API (clean-scan route) |
| 3 | 134-3 | 93 | Ch. II, Reflections on homotopical algebra | T | API (clean-scan route) |
| 4 | 134-4 | 100 | Ch. III, Homotopy structures | T | API (clean-scan route) |
| 5 | 134-5 | 132 | Ch. IV, Asphericity structures | T | API (clean-scan route) |
| 6 | 134-6 | 124 | Ch. V, Homology and cohomology | T | API (clean-scan route) |
| 7 | 134-7 | 112 | Ch. VI, Schematization | T | API (clean-scan route) |
| 8 | 134-8 | 86 | Ch. VII, Linearization of homotopy types | T | API (clean-scan route) |

**VI.5. The dossier around Pursuing Stacks (1982-84)** (261 pp.). Links: Dérivateurs companion (ch. XI-XII, XVI); Pursuing Stacks by section.

| Pos. | Cote | Pages | Contents | Rank | Route |
|---|---|---|---|---|---|
| 1 | 104 | 16 | Stacks 1 | 9 | Pro mode |
| 2 | 105 | 52 | Stacks 2 | 9 | Pro mode |
| 3 | 106 | 16 | Stacks 3 | 9 | Pro mode |
| 4 | 107 | 25 | Closed models | 9 | Pro mode |
| 5 | 108 | 5 | Miscellany, list of questions | 9 | Pro mode |
| 6 | 109 | 37 | Tables, corrections and preparation of an edition (1983-84) | 9 | Pro mode |
| 7 | 110 | ? | Not in the open archive (see section 2) | - | not in the open archive (slot reserved) |
| 8 | 112 | 4 | Linearization | 9 | Pro mode |
| 9 | 113 | 12 | Abelianization | 9 | Pro mode |
| 10 | 114 | 5 | Asphericity | 9 | Pro mode |
| 11 | 115 | 14 | Functorial "correspondences", duality of topoi | 9 | Pro mode |
| 12 | 116 | 10 | Mapping cone | 9 | Pro mode |
| 13 | 117 | 25 | Homotopy theories (1983) | 9 | Pro mode |
| 14 | 118 | 40 | Cohomology properties of maps in (Cat) | 9 | Pro mode |

**VI.6. Les Dérivateurs (1990-91), the manuscript** (2,135 pp.). Links: Dérivateurs companion and our transcription of the printed edition (concordance from scan to edition page).

| Pos. | Cote | Pages | Contents | Rank | Route |
|---|---|---|---|---|---|
| 1 | 157-1 | 270 | Ch. I-IV, with the general summary | - | done through the printed edition; concordance only |
| 2 | 157-2 | 441 | Ch. V-VIII | - | done through the printed edition; concordance only |
| 3 | 157-3 | 355 | Ch. IX-XII | - | done through the printed edition; concordance only |
| 4 | 157-4 | 408 | Ch. XIII-XVI | - | done through the printed edition; concordance only |
| 5 | 157-5 | 661 | Ch. XVII-XIX | - | done through the printed edition; concordance only |

**VI.7. Around the derivators (1990-91)** (85 pp.). Links: Dérivateurs companion (the notes it needs to close).

| Pos. | Cote | Pages | Contents | Rank | Route |
|---|---|---|---|---|---|
| 1 | 158 | 85 | Around the derivators (c. 1990-91) | 9 | Pro mode |

Book total: 3,702 site pages.

### Workshop: papers and early notes

What belongs to no programme, and the tools: the concordance (cote and scan to book, chapter and position: `PLACEMENT_EVERYTHING.csv` is its first state), the timeline, and the register of questions.

**W.1. Functional analysis (1953)** (149 pp.). Links: French-school site (thesis, Résumé).

| Pos. | Cote | Pages | Contents | Rank | Route |
|---|---|---|---|---|---|
| 1 | 1 | 149 | Functional analysis: notes, letter of 1953 | 0, 25 | Pro mode |

**W.2. Documents, lists and side topics** (75 pp.). Links: Question register (cote 66).

| Pos. | Cote | Pages | Contents | Rank | Route |
|---|---|---|---|---|---|
| 1 | 66 | 4 | "Problèmes": thesis topics of 1964 | 25 | Pro mode |
| 2 | 68 | 55 | Positional games (1978-83) | 25 | Pro mode |
| 3 | 162-1 | 9 | Borrowed papers: a list of names and references | 25 | Pro mode |
| 4 | 162-6 | 5 | Isolated documents | 25 | Pro mode |
| 5 | 139 | 2 | The Émile Picard medal (1977) | - | concordance only |

**W.3. Concordance, timeline, question register.** No cotes of its own. Also filed here: the part of cote 119 outside the Esquisse (activity report of 1984, course programmes, CV of 1972, "Fonctions holomorphes I, II" of 1973-74, letters of 1968, 1972 and 1991, offprints).

Book total: 224 site pages.


### The items asked about by name

- **Clean typescripts.**
  - 25, "Nouveau EGA V" (184 pp.): Book I, chapter V, position 1; the text Book I starts from. API route, first in
    that route. Checks: the Circle's scans of the prenotes and the Blass translation.
  - 24, the English translation materials (76 pp.): Book I, chapter V, position 2. API route. It is filed as a
    witness to 25, and its English is kept apart from our own translation.
  - 119, the CNRS dossier (313 pp.): the Esquisse (57 pp.) is the front door, D.1; the rest (activity report, course
    programmes, CV, "Fonctions holomorphes", letters, offprints) is Workshop W.3. API route; the handwritten notes of
    1986 inside it, if the inventory finds more than a few sheets, join the Pro package of rank 25.
  - 162-5, Tapis de Quillen (68 pp.): Book VI, chapter 2, position 1, the opening text of the book. API route for
    the typescript; its handwritten notes of 1968 join the Pro package of rank 9 that holds 111.
- **Pursuing Stacks, 134-1 to 134-8 (837 pp.)**: Book VI, chapter 4, one position per chapter of the typescript,
  the letters (134-1) first. API route. The arXiv edition (2021) and SMF volume I check the typed text; what the
  archive copy adds is his handwritten annotations and the notes in 134-8, and the edition page records each of them.
- **Les Dérivateurs, 157-1 to 157-5 (2,135 pp.)**: Book VI, chapter 6. No transcription of the manuscript: the
  printed edition is transcribed by us and the companion is written on it. The manuscript enters as a concordance
  (chapter and manuscript page to scan), so that each page of our text links to its scan, and as the witness for the
  places where the companion doubts the edition. Cote 158 (85 pp., rank 9) is chapter 7 and is transcribed in Pro mode.
- **La Longue Marche, 140-1 to 140-4 (1,584 pp.)**: Book III. 140-2 to 140-4 are chapter 3, the centre of the book;
  the draft 140-1 is chapter 2, position 3, between the spring 1981 draft (145) and the Kummer note (141). Done; the
  second pass is finishing. Our edition and book are the text of this chapter.
- **The medal, cote 139 (2 pp.)**: Workshop W.2, last position. Concordance only: one line and the two images.
- **Cote 110.** The archive's listing passes from cote 109 ("Tables", 37 pp.) to cote 111 ("Tapis de Quillen", 16 pp.)
  inside the dossier "Autour de Pursuing stacks"; no title, date, page count or file is given for 110, so the manifest
  has no row and nothing was downloaded (`DOWNLOAD_PRIORITY.txt` names it; no such file exists on the site's list).
  The open numbering has other gaps of the same kind (3, 17, 20, 30, 38, 61, 65, 92, 95, 96, 99, 124, and 162-2 to
  162-4), and the fonds has about 28,000 pages of which about 18,000 are open, so 110 is probably a folder that is not
  communicable; that is an inference, not a statement of the archive. Grothendieck assembled this dossier in its
  present order, so 110 sat between the tables for an edition of *Pursuing Stacks* and the 1968 typescript. Its slot is
  kept: Book VI, chapter 5, position 7. Nothing to transcribe; one question to the archive when we next write to it.

## 3. Placements changed from the earlier file, and why

Ranks 0-11 keep their content and order (they are the adopted first tranche). Changes of book inside them do not
move a package.

| Cote | Earlier | Here | Why |
|---|---|---|---|
| 155 | Book V (rank 5, with stratified spaces) | Book II, chapter 7, with cote 10; rank 5 kept | Opened: a ⊗-category C over k with a fibre functor to modules over an extension k', the algebra U ⊗ U of its endomorphisms, and "Exprimer la rigidité de C". It is Tannakian reconstruction, written in 1984; the archive filed it by date |
| 153 | Book V (rank 5) | Book II, chapter 9, with 133; rank 5 kept | Opened: operations F∘G on k⟨T⟩, W(Ω), the polynomials T(T-1)…(T-n+1)/n! and the ring they span in Q[T]. Algebra of universal operations, not stratified spaces; it links to schematization (*Pursuing Stacks* VI) |
| 133 | "I, II" (rank 22) | Book II, chapter 9, position 1 | Opened: a pentagon for ⊗ with a class in Ext², the Witt group W(G), operations τⁿ on the ring of finite G-sets, formal groups; dated 1974-75, the two years before the de Rham notes |
| 129 | Workshop, rank 25, Pro | Book II, chapter 2; API route | Opened: clean typed chapters of the Montréal seminar on Barsotti-Tate groups, lightly annotated. It needs no Pro run and belongs with 9 and 100 |
| 161-5 | Workshop, rank 25 | Book II, chapter 2; rank 15 | Barsotti-Tate offprints with his annotations; the archive itself cross-refers it to cote 100 |
| 130 | "I, II" (rank 22) | Book II, chapter 8, with the L-functions (60) | Heights and local symbols are arithmetic of cycles and L-functions, not foundations |
| 132 | Workshop, rank 25 | Book IV, chapter 2; rank 18 | Ladegaillerie's embeddings of graphs in surfaces: the Esquisse (§3) names this as his way into maps in 1974 |
| 2 | Prelude (Workshop), rank 25 | Book I, chapter X; rank 25 kept | Riemann-Roch is the subject of that chapter of his plan, which otherwise holds only 90 and 97 |
| 160 | Workshop, rank 25 | Book I, chapter VII; rank 24 | Group schemes, the subject of SGA 3 III by the archive's note |
| 122, 123, 125 | "I, II" (rank 22) | Book I: 125 in chapter V, 122 and 123 in chapters XI-XII | Projective duality belongs with hyperplane sections; the isolated singular point and the Kostant folder (1968-71) belong with SGA 7 |
| 138 | "III, IV" | Book III, chapter 7, the last chapter | One slot is needed. It is the arithmetic study; it ends Book III and hands over to Book IV. The other map folders (76, 88, 70, 75, 161-6) are Book IV |
| 119 | Prelude and documents | Split: the Esquisse is the front door; the rest is Workshop W.3 | The front door is one text, not a dossier |
| 111, 103 | In the dossier 103-118 | 111 with 162-5 (chapter 2); 103 with 135 (chapter 3) | They are a 1968 typescript and 1974 letters; by date they precede *Pursuing Stacks*. His dossier order stays in the cote index |
| 32, 37 | Remaining SGA folders | Book I, chapter 0, with the EGA complements | Corrections and re-editions concern the printed EGA and SGA as a whole, not one chapter |
| 152 | Book V (rank 5) | Kept in Book V, chapter 3, with a link to Book IV | Opened: "Arbres plans", trees with an isotopy class of embeddings in a surface, on listing paper, with drawings. The transcription decides whether it belongs with maps |
| 93 | Book II, rank 15, "content not yet known" | Book II, chapter 3 of its own; rank 15 kept | Opened: it starts with the typed formulary of Deligne after Tate, then typed sheets and handwritten notes alternate. An inventory separates the typed sheets (API) first |

Units of rank that changed: rank 15 gains 161-5; rank 18 gains 132; rank 24 gains 160; rank 25 loses 129, 132, 160
and 161-5; 129 leaves the Pro route.

## 4. The package list for everything, in transcription order

Rules used.

- A package holds up to the package size in scans (90 or 45) and is one Pro prompt.
- A cote's scan run is split only when it is longer than a package. A run up to a tenth over the size (99 at 90, 49
  at 45) stays whole: with blank sheets left out it fits.
- A long cote is cut into full packages from its start; its tail and the small cotes of the same rank fill packages
  together, largest first, so that the rank needs as few prompts as possible. No package mixes ranks.
- The packager moves a cut by a few scans to the nearest break in his own pagination (a new N°, a new date).
- Scan numbers are those of each cote's PDF. P001 and P002 are the two packages already sent.

| Rank | Unit | Pages | Packages at 90 (cote: scans of its PDF) | n | Packages at 45 | n | Context zip |
|---|---|---|---|---|---|---|---|
| 0 | Pilot | 49 | P001 = 1: 2-50 (done) | 1 | P001 = 1: 2-50 (done) | 1 | none |
| 1 | Around the Long March, the main texts | 578 | P002 = 147: 3-47 (sent)<br>P003 = 147: 48-137<br>P004 = 147: 138-190; 142: 92-122<br>P005 = 149: 2-91<br>P006 = 149: 92-136; 146: 92-134<br>P007 = 146: 2-91<br>P008 = 142: 2-91 | 7 | P002 = 147: 3-47 (sent)<br>P003 = 147: 48-92<br>P004 = 147: 93-137<br>P005 = 147: 138-182<br>P006 = 147: 183-190; 142: 92-122<br>P007 = 149: 2-46<br>P008 = 149: 47-91<br>P009 = 149: 92-136<br>P010 = 146: 2-46<br>P011 = 146: 47-91<br>P012 = 146: 92-134<br>P013 = 142: 2-46<br>P014 = 142: 47-91 | 13 | our Longue Marche text, notes and contents (as package 2 had) |
| 2 | 1960s test | 80 | P009 = 16: 2-56; 47: 2-11; 54: 2-8; 44: 2-9 | 1 | P015 = 16: 2-46<br>P016 = 16: 47-56; 47: 2-11; 54: 2-8; 44: 2-9 | 2 | none |
| 3 | EGA drafts and plans | 188 | P010 = 21: 2-29; 22: 2-30; 26: 2-11; 35: 2-6; 48: 2-6; 102: 2-14<br>P011 = 23: 2-99 | 2 | P017 = 21: 2-29; 26: 2-11; 35: 2-6<br>P018 = 22: 2-30; 102: 2-14<br>P019 = 23: 2-46<br>P020 = 23: 47-91<br>P021 = 23: 92-99; 48: 2-6 | 5 | table of contents of our EGA edition; EGA 0_III and 0_IV |
| 4 | Around the Long March, the dated notes | 339 | P012 = 144: 2-91<br>P013 = 144: 92-184<br>P014 = 148: 2-72; 141: 2-16<br>P015 = 143: 2-34; 145: 2-38 | 4 | P022 = 144: 2-46<br>P023 = 144: 47-91<br>P024 = 144: 92-136<br>P025 = 144: 137-184<br>P026 = 148: 2-46<br>P027 = 148: 47-72; 141: 2-16<br>P028 = 143: 2-34<br>P029 = 145: 2-38 | 8 | Longue Marche text; returns of rank 1 |
| 5 | Stratified spaces and tame topology | 300 | P016 = 150: 2-99<br>P017 = 151: 2-75; 152: 2-13<br>P018 = 153: 2-11; 121: 2-73<br>P019 = 155: 2-11; 120: 2-25 | 4 | P030 = 150: 2-46<br>P031 = 150: 47-91<br>P032 = 150: 92-99; 153: 2-11; 121: 47-73<br>P033 = 151: 2-46<br>P034 = 151: 47-75; 152: 2-13<br>P035 = 155: 2-11; 120: 2-25<br>P036 = 121: 2-46 | 7 | returns of cote 147 (rank 1); Esquisse §§5-6 |
| 6 | Motives: cycles, Galois theory, Hodge | 637 | P020 = 14: 2-91<br>P021 = 14: 92-132; 15: 182-228<br>P022 = 13: 2-52<br>P023 = 12: 2-91<br>P024 = 12: 92-168<br>P025 = 15: 2-91<br>P026 = 15: 92-181<br>P027 = 18: 2-62 | 8 | P037 = 14: 2-46<br>P038 = 14: 47-91<br>P039 = 14: 92-132<br>P040 = 13: 2-46<br>P041 = 13: 47-52; 12: 137-168<br>P042 = 12: 2-46<br>P043 = 12: 47-91<br>P044 = 12: 92-136<br>P045 = 15: 2-46<br>P046 = 15: 47-91<br>P047 = 15: 92-136<br>P048 = 15: 137-181<br>P049 = 15: 182-228<br>P050 = 18: 2-46<br>P051 = 18: 47-62 | 15 | returns of rank 2 (cote 16) |
| 7 | Crystals | 360 | P028 = 5: 2-53; 9: 2-29<br>P029 = 6: 2-67<br>P030 = 7: 2-72; 4: 2-12<br>P031 = 8: 2-81<br>P032 = 100: 2-53 | 5 | P052 = 5: 2-46<br>P053 = 5: 47-53; 8: 47-81<br>P054 = 6: 2-46<br>P055 = 6: 47-67<br>P056 = 7: 2-46<br>P057 = 7: 47-72; 100: 47-53<br>P058 = 8: 2-46<br>P059 = 9: 2-29; 4: 2-12<br>P060 = 100: 2-46 | 9 | none |
| 8 | The 1976 de Rham notes | 460 | P033 = 137: 2-86<br>P034 = 136: 2-91<br>P035 = 136: 92-181<br>P036 = 136: 182-271<br>P037 = 136: 272-361<br>P038 = 136: 362-376 | 6 | P061 = 137: 2-46<br>P062 = 137: 47-86<br>P063 = 136: 2-46<br>P064 = 136: 47-91<br>P065 = 136: 92-136<br>P066 = 136: 137-181<br>P067 = 136: 182-226<br>P068 = 136: 227-271<br>P069 = 136: 272-316<br>P070 = 136: 317-361<br>P071 = 136: 362-376 | 11 | return of 137 (for 136); Pursuing Stacks ch. VI |
| 9 | Around Pursuing Stacks and the derivators | 437 | P039 = 158: 2-86; 108: 2-6<br>P040 = 103: 2-18; 112: 2-5; 117: 2-26; 118: 2-41<br>P041 = 104: 2-17; 106: 2-17; 111: 2-17; 113: 2-13; 115: 2-15; 116: 2-11<br>P042 = 105: 2-53; 109: 2-38<br>P043 = 107: 2-26; 114: 2-6; 135: 2-59 | 5 | P072 = 158: 2-46<br>P073 = 158: 47-86; 108: 2-6<br>P074 = 103: 2-18; 107: 2-26<br>P075 = 104: 2-17; 112: 2-5; 117: 2-26<br>P076 = 105: 2-46<br>P077 = 105: 47-53; 109: 2-38<br>P078 = 106: 2-17; 111: 2-17; 135: 47-59<br>P079 = 113: 2-13; 115: 2-15; 116: 2-11<br>P080 = 114: 2-6; 118: 2-41<br>P081 = 135: 2-46 | 10 | Dérivateurs chapter summaries and companion (for 158); Pursuing Stacks contents (for 103-118, 135) |
| 10 | Maps and their arithmetic | 399 | P044 = 138: 2-91<br>P045 = 138: 92-133; 70: 92-126<br>P046 = 76: 2-63; 88: 2-16<br>P047 = 70: 2-91<br>P048 = 75: 2-33; 161-6: 2-34 | 5 | P082 = 138: 2-46<br>P083 = 138: 47-91<br>P084 = 138: 92-133<br>P085 = 76: 2-46<br>P086 = 76: 47-63; 88: 2-16<br>P087 = 70: 2-46<br>P088 = 70: 47-91<br>P089 = 70: 92-126<br>P090 = 75: 2-33<br>P091 = 161-6: 2-34 | 10 | Longue Marche notes; Esquisse §3 |
| 11 | Geometry of forms, final state | 397 | P049 = 156-8: 2-91<br>P050 = 156-8: 92-127; 156-5: 2-49<br>P051 = 156-1: 2-27; 156-2: 2-19<br>P052 = 156-3: 2-41; 156-9: 92-140<br>P053 = 156-9: 2-91 | 5 | P092 = 156-8: 2-46<br>P093 = 156-8: 47-91<br>P094 = 156-8: 92-127<br>P095 = 156-1: 2-27; 156-2: 2-19<br>P096 = 156-3: 2-41<br>P097 = 156-5: 2-49<br>P098 = 156-9: 2-46<br>P099 = 156-9: 47-91<br>P100 = 156-9: 92-140 | 9 | Esquisse §§5-6; the later packages also get the returns of the earlier ones |
| 12 | Long March periphery | 289 | P054 = 64: 2-91<br>P055 = 64: 92-157; 67: 92-101<br>P056 = 67: 2-91<br>P057 = 159: 2-34 | 4 | P101 = 64: 2-46<br>P102 = 64: 47-91<br>P103 = 64: 92-136<br>P104 = 64: 137-157<br>P105 = 67: 2-46<br>P106 = 67: 47-91<br>P107 = 67: 92-101; 159: 2-34 | 7 | Longue Marche text (§37, §53); returns of ranks 1 and 4 |
| 13 | Motives: tensor categories, correspondences, Lefschetz, L-functions | 361 | P058 = 10: 2-91<br>P059 = 10: 92-181<br>P060 = 10: 182-198; 60: 2-70<br>P061 = 11: 2-58<br>P062 = 56: 2-39 | 5 | P108 = 10: 2-46<br>P109 = 10: 47-91<br>P110 = 10: 92-136<br>P111 = 10: 137-181<br>P112 = 10: 182-198; 60: 47-70<br>P113 = 11: 2-46<br>P114 = 11: 47-58<br>P115 = 56: 2-39<br>P116 = 60: 2-46 | 9 | returns of ranks 2 and 6 |
| 14 | Regular polyhedra over rings | 1012 | P063 = 79: 2-91<br>P064 = 79: 92-181<br>P065 = 79: 182-271<br>P066 = 79: 272-297; 86: 2-33; 69: 92-120<br>P067 = 83: 2-91<br>P068 = 83: 92-181<br>P069 = 83: 182-222; 74: 92-136<br>P070 = 72: 2-91<br>P071 = 72: 92-113<br>P072 = 85: 2-98<br>P073 = 69: 2-91<br>P074 = 74: 2-91 | 12 | P117 = 79: 2-46<br>P118 = 79: 47-91<br>P119 = 79: 92-136<br>P120 = 79: 137-181<br>P121 = 79: 182-226<br>P122 = 79: 227-271<br>P123 = 79: 272-297<br>P124 = 83: 2-46<br>P125 = 83: 47-91<br>P126 = 83: 92-136<br>P127 = 83: 137-181<br>P128 = 83: 182-222<br>P129 = 72: 2-46<br>P130 = 72: 47-91<br>P131 = 72: 92-113<br>P132 = 86: 2-33; 85: 92-98<br>P133 = 85: 2-46<br>P134 = 85: 47-91<br>P135 = 69: 2-46<br>P136 = 69: 47-91<br>P137 = 69: 92-120<br>P138 = 74: 2-46<br>P139 = 74: 47-91<br>P140 = 74: 92-136 | 24 | returns of rank 10 (75, 161-6) |
| 15 | Gauss-Manin; Barsotti-Tate offprints | 263 | P075 = 93: 2-91<br>P076 = 93: 92-181<br>P077 = 93: 182-236; 161-5: 2-29 | 3 | P141 = 93: 2-46<br>P142 = 93: 47-91<br>P143 = 93: 92-136<br>P144 = 93: 137-181<br>P145 = 93: 182-226<br>P146 = 93: 227-236; 161-5: 2-29 | 6 | none |
| 16 | Popular presentations, categories, topos | 310 | P078 = 161-3: 2-55; 161-4: 2-32<br>P079 = 161-1: 2-20; 161-2: 92-112<br>P080 = 161-2: 2-91<br>P081 = 19: 2-96 | 4 | P147 = 161-3: 2-46<br>P148 = 161-3: 47-55; 161-4: 2-32; 19: 92-96<br>P149 = 161-1: 2-20; 161-2: 92-112<br>P150 = 161-2: 2-46<br>P151 = 161-2: 47-91<br>P152 = 19: 2-46<br>P153 = 19: 47-91 | 7 | none |
| 17 | Geometry of forms, earlier versions | 294 | P082 = 156-4: 2-89<br>P083 = 156-6: 2-94<br>P084 = 156-7: 2-91<br>P085 = 156-7: 92-114 | 4 | P154 = 156-4: 2-46<br>P155 = 156-4: 47-89<br>P156 = 156-6: 2-46<br>P157 = 156-6: 47-94<br>P158 = 156-7: 2-46<br>P159 = 156-7: 47-91<br>P160 = 156-7: 92-114 | 7 | returns of rank 11 (156-8 is the final version of these chapters) |
| 18 | Rest of the combinatorial block, pseudolines, embeddings | 1023 | P086 = 71: 2-48; 87: 2-41<br>P087 = 73: 2-29; 78: 92-130<br>P088 = 77: 2-91<br>P089 = 77: 92-158; 89: 2-21<br>P090 = 78: 2-91<br>P091 = 80: 2-73<br>P092 = 81: 2-55; 132: 2-32<br>P093 = 82: 2-79; 84: 182-193<br>P094 = 84: 2-91<br>P095 = 84: 92-181<br>P096 = 154: 2-91<br>P097 = 154: 92-176 | 12 | P161 = 71: 2-48<br>P162 = 73: 2-29<br>P163 = 77: 2-46<br>P164 = 77: 47-91<br>P165 = 77: 92-136<br>P166 = 77: 137-158; 89: 2-21<br>P167 = 78: 2-46<br>P168 = 78: 47-91<br>P169 = 78: 92-130<br>P170 = 80: 2-46<br>P171 = 80: 47-73<br>P172 = 81: 2-46<br>P173 = 81: 47-55; 132: 2-32<br>P174 = 82: 2-46<br>P175 = 82: 47-79; 84: 182-193<br>P176 = 84: 2-46<br>P177 = 84: 47-91<br>P178 = 84: 92-136<br>P179 = 84: 137-181<br>P180 = 87: 2-41<br>P181 = 154: 2-46<br>P182 = 154: 47-91<br>P183 = 154: 92-136<br>P184 = 154: 137-176 | 24 | none |
| 19 | Jacobians, abelian varieties, Picard notes | 577 | P098 = 43: 2-91<br>P099 = 43: 92-181<br>P100 = 43: 182-208; 59: 2-28; 53: 2-34<br>P101 = 58: 2-67; 51: 2-23<br>P102 = 49: 2-10; 52: 2-14; 55: 2-18<br>P103 = 50: 2-11; 45: 2-80<br>P104 = 46: 2-95 | 7 | P185 = 43: 2-46<br>P186 = 43: 47-91<br>P187 = 43: 92-136<br>P188 = 43: 137-181<br>P189 = 43: 182-208; 55: 2-18<br>P190 = 58: 2-46<br>P191 = 58: 47-67; 51: 2-23<br>P192 = 59: 2-28; 52: 2-14<br>P193 = 49: 2-10; 53: 2-34<br>P194 = 50: 2-11; 45: 47-80<br>P195 = 45: 2-46<br>P196 = 46: 2-46<br>P197 = 46: 47-95 | 13 | none |
| 20 | Other 1960s folders | 292 | P105 = 90: 2-25; 91: 92-143<br>P106 = 91: 2-91<br>P107 = 94: 2-24; 97: 2-19<br>P108 = 98: 2-44; 101: 2-43 | 4 | P198 = 90: 2-25; 97: 2-19<br>P199 = 91: 2-46<br>P200 = 91: 47-91<br>P201 = 91: 92-136<br>P202 = 91: 137-143; 94: 2-24<br>P203 = 98: 2-44<br>P204 = 101: 2-43 | 7 | none |
| 21 | SGA drafts | 686 | P109 = 33: 2-91<br>P110 = 33: 92-181<br>P111 = 31: 2-91<br>P112 = 31: 92-102; 39: 2-20; 40: 2-28<br>P113 = 32: 2-48; 41: 2-14; 34: 182-210<br>P114 = 42: 2-7; 36: 2-85<br>P115 = 34: 2-91<br>P116 = 34: 92-181 | 8 | P205 = 33: 2-46<br>P206 = 33: 47-91<br>P207 = 33: 92-136<br>P208 = 33: 137-181<br>P209 = 31: 2-46<br>P210 = 31: 47-91<br>P211 = 31: 92-102; 40: 2-28<br>P212 = 32: 2-48<br>P213 = 39: 2-20<br>P214 = 41: 2-14; 34: 182-210<br>P215 = 42: 2-7; 36: 47-85<br>P216 = 34: 2-46<br>P217 = 34: 47-91<br>P218 = 34: 92-136<br>P219 = 34: 137-181<br>P220 = 36: 2-46 | 16 | contents of our SGA 4, 5 and 7 editions |
| 22 | Descent, heights, Witt groups, singularities | 320 | P117 = 126: 2-35; 133: 2-54<br>P118 = 127: 2-24; 128: 2-32<br>P119 = 130: 2-50; 131: 2-42<br>P120 = 122: 2-35; 123: 2-48; 125: 2-9 | 4 | P221 = 126: 2-35; 133: 47-54<br>P222 = 127: 2-24<br>P223 = 128: 2-32<br>P224 = 130: 2-50<br>P225 = 131: 2-42<br>P226 = 133: 2-46<br>P227 = 122: 2-35; 125: 2-9<br>P228 = 123: 2-48 | 8 | none |
| 23 | Old elliptic-curve notes, the Picard typescript | 510 | P121 = 62: 2-97<br>P122 = 63: 2-91<br>P123 = 63: 92-101; 57: 272-315<br>P124 = 57: 2-91<br>P125 = 57: 92-181<br>P126 = 57: 182-271 | 6 | P229 = 62: 2-46<br>P230 = 62: 47-91<br>P231 = 62: 92-97; 63: 92-101<br>P232 = 63: 2-46<br>P233 = 63: 47-91<br>P234 = 57: 2-46<br>P235 = 57: 47-91<br>P236 = 57: 92-136<br>P237 = 57: 137-181<br>P238 = 57: 182-226<br>P239 = 57: 227-271<br>P240 = 57: 272-315 | 12 | return of cote 64 (rank 12) |
| 24 | Remaining SGA folders, group schemes | 383 | P127 = 27: 2-37; 28: 2-11; 29: 182-217<br>P128 = 29: 2-91<br>P129 = 29: 92-181<br>P130 = 37: 2-100<br>P131 = 160: 2-23 | 5 | P241 = 27: 2-37; 37: 92-100<br>P242 = 28: 2-11; 160: 2-23<br>P243 = 29: 2-46<br>P244 = 29: 47-91<br>P245 = 29: 92-136<br>P246 = 29: 137-181<br>P247 = 29: 182-217<br>P248 = 37: 2-46<br>P249 = 37: 47-91 | 9 | contents of our SGA 3 edition |
| 25 | Early notes and remnants | 217 | P132 = 1: 51-140<br>P133 = 1: 141-150; 66: 2-5; 68: 2-56; 162-1: 2-10; 162-6: 2-6<br>P134 = 2: 2-45 | 3 | P250 = 1: 51-95<br>P251 = 1: 96-140<br>P252 = 1: 141-150; 66: 2-5; 68: 47-56; 162-1: 2-10; 162-6: 2-6<br>P253 = 2: 2-45<br>P254 = 68: 2-46 | 5 | none |
| | **All** | | | **134** | | **254** | |

Counts by tranche (90 / 45): ranks 0-11, 53 / 100; ranks 12-20, 55 / 104; ranks 21-25,
26 / 50; all, **134 / 254**.

What lowers these counts further: blank sheets (about 8 %); typed sheets inside cotes 10, 57, 93, 63, 37, 29, 12, 15
and 21, which go to the API route once the inventory has listed them (10 and 57 alone are 511 pages, up to 6 packages
at 90 or 11 at 45).

**The API route, in order** (no Pro prompt): 25; the Esquisse pages of 119; 162-5; 24; 129; 134-1 to 134-8; the rest
of 119; then the typed sheets that the inventory takes out of the Pro cotes. 1,592 pages before those sheets.

**Context zips.** The last column names what each rank's packages get, on the model of package 2 (our Longue Marche
text, opened only after the transcription is finished). Ranks without one: 2, 7, 15, 16, 18, 19, 20, 22, 25.

**Cotes to look at before packaging** (an inventory of versos and of typed or printed sheets; the unrelated sheets
are left out of the package and listed in the concordance):

| Cote | Rank | What to settle before packaging |
|---|---|---|
| 144 | 4 | versos hold Philippe Cornu's C4 course notes |
| 155 | 5 | versos: letters of 1984, a typed contract |
| 15 | 6 | typescript part; versos are Bourbaki exposés |
| 12 | 6 | typescript part; versos are Bourbaki exposés |
| 136 | 8 | versos of 1975 (agenda, letters); two loose sheets |
| 64 | 12 | versos are letters of 1980-82 (scan 40 is a 1982 circular) |
| 10 | 13 | largely typescript: typed sheets go by the API route |
| 83 | 14 | versos are typescript pages of Récoltes et Semailles |
| 93 | 15 | opens with Deligne's typed formulaire; typescript copies and a 1981 offprint among the notes |
| 161-5 | 15 | printed offprints: only the annotations and the notes are transcribed |
| 84 | 18 | versos are Récoltes et Semailles typescript and listings |
| 43 | 19 | versos are bibliographies and Bourbaki exposés |
| 33 | 21 | versos include other people's typescripts and Bourbaki exposés |
| 57 | 23 | versos are printed Bourbaki exposés, EGA I pages, a 1956 list |
| 63 | 23 | copies of printed articles and a typescript |
| 29 | 24 | typescripts and letters among the notes |
| 37 | 24 | typescripts and letters: typed sheets by the API route |
| 68 | 25 | versos: a staff table, a draft page of Récoltes et Semailles |

Cotes 64, 33 and 57 are the three the earlier file named; the others are added from the archive's notes on versos.

## 5. What follows each book once transcribed

The stages of `PLAN_EVERYTHING.md` apply to every book: (3) second pass by Claude subagents, each package against its
scans, then one global pass per chapter; (4) edition on GitHub per book and chapter, diplomatic French and reading
text, anchored to cote and scan; (5) English translation with glossary, locked formulas and unit checks;
(6) development. The second pass also writes, for every chapter, the header of each page (what it is, date, how far
he took it, what became of it), the entries of the question register, and the concordance rows. A chapter is
published when its packages have passed; a book does not wait for its last chapter.

| Book | Second pass: its checks | Edition | Translation | Development: the aim | Question register: first sources |
|---|---|---|---|---|---|
| Front door | The Esquisse against the printed French text | The Esquisse with each section linked to the chapters behind it; 161-3 and 161-4 as reading texts | English of the Esquisse, 161-3 and 161-4 first: they are what a new reader opens | No development of its own. The annotation states, for each paragraph of the Esquisse, which folders stand behind it and what became of the claim | Every programme statement of the Esquisse, each linked to its book |
| I | Each draft against the printed EGA, SGA and FGA by number: the first output is the map of what the drafts contain that print does not | By chapter of his plan. Chapter V from 25, collated with 24 and the Circle's prenotes | After the map, so that only what is not in print is translated in full; the rest is cited to our EGA and SGA editions | "EGA V and after": the unwritten chapters written out with proofs in Stacks format, his plan as table of contents, what EGA I-IV, SGA and FGA contain cited and not redone, each part's author and model named. First chapters: V (from 25) and VI (construction techniques), where his drafts are fullest | The open problems for EGA VI (26); the thesis topics of 1964 (66) |
| II | Outside witnesses: the letters to Tate, Deligne, Coates and Serre, and "Motifs" (Elbaz-Vincent) for part of 12 | By chapter; chapter 9 (136, 137) as one text with his own pagination restored | Whole book: almost none of it is in print in any language | His route to motives set beside Saavedra, Deligne, Jannsen, André and Voevodsky; for each standard conjecture, what it would give and what stands without it; the Fourier transform of cote 47 beside Mukai's; a reconstruction of the 1976 lecture from 136 and 137; for 93, whether it holds his own statement on p-curvature | The questions on cycles in 14; the conjectures of 16; every "?" of 12, 13, 15 |
| III | The global pass of the Longue Marche (`LM_GLOBAL_PASS.md`): same notation, same hand | Chapters added to the Longue Marche repository around the manuscript | Same glossary and notation table as the Longue Marche | The Longue Marche book, with chapters 1, 4 and 5 as its chapters on Teichmüller groupoids, the boundary and the anabelian questions; each conjecture with its status today (Nakamura, Tamagawa, Mochizuki, Pop; Grothendieck-Teichmüller theory) | The "conjecture hâtive" and its revision; the notes files of the Longue Marche packages |
| IV | The course texts at the CSG for 69 and 75; every enumeration and table recomputed by script | By chapter; drawings redrawn, with the scan beside them | Whole book | A self-contained text from the cube and the icosahedron to regular polyhedra over finite fields and to maps; lessons for the Open Mathematics Courses come from it chapter by chapter; comparison with Ji (2023) and with the dessins literature | His statements in Esquisse §§3-4 that nobody had taken the programme up: each open point listed |
| V | For 156, the four versions against each other: 156-8 is the base, the variants of 156-4, 156-6 and 156-7 are recorded against it | Chapter 4 as the text of 1986 in its final state; chapter 5 as an apparatus of variants, not three more texts | Chapters 1-4; chapter 5 only where a variant says something the final state does not | The axioms of tame topology and the dévissage of stratified spaces, compared with o-minimality and exit paths; for the geometry of forms, first a faithful account of what the text does, then what can be proved from it | The axioms he asks for in Esquisse §5; every "à expliciter" of 150 and 151 |
| VI | *Pursuing Stacks* against the arXiv and SMF editions; the *Dérivateurs* manuscript only at the places the companion marks as doubtful | Chapters 1-3, 5 and 7 are new text; chapter 4 is the typescript with his annotations; chapter 6 is the concordance to our transcription of the printed edition | Chapters 1-3, 5, 7; *Pursuing Stacks* is in English already | The companion to *Les Dérivateurs* closed with 158 and carried backwards through the dossier of 1982-84 to *Pursuing Stacks* and the Tapis de Quillen: one account of how the question of 1968 became the derivators | The list of questions (108); the questions of 113-118 that reappear in *Les Dérivateurs* XI-XII and XVI |
| Workshop | Cote 1 against the thesis and the Résumé | Cote 1 as one text; documents as a list with images | Cote 1; the thesis topics | None planned. The concordance, the timeline and the register are built here | The thesis topics of 1964 (66), each with its status today |

Order of the work after transcription: it follows the ranks, so the first chapters to pass the second pass are
Book III chapters 4 and 1, Book II chapters 4 and 5 (cote 16), Book I chapter 0, Book V chapters 3 and 1. Book I's
map against print and the question register start with the first of these and grow with each chapter.

## 6. Points left open

- The chapter numbers of Book I follow our record of his plan; ranks 3 (26, 48, 102, 35) settle them.
- 152 and 93 are placed from a few pages; the transcription may move them.
- Cote 110: ask the archive.
- The packager needs a multi-cote option (several cotes in one zip, one output file per cote).
