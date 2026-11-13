# Part 5 audit and integration notes

## Coverage

| Requested line | Statements | Outcome |
|---|---|---|
| Item 5, corollaries and levels | P5a1–P5a3, P5c4 | (246) refuted as a span-only bicolimit; corrected full depth-three theorem proved; unstarred (247) refuted and corrected to X*. |
| Lead 6 | P5a1–P5a3, P5b1–P5b3 | Hexagon and sharp k+2 bound proved; dimension theorem proved with empty-multicurve convention at k≥d. |
| Part 5(a) | P5a1–P5a3 | Refutation plus proved replacements, finite computations executed. |
| Part 5(b) | P5b1–P5b3 | Fibre identification all stable genera for stack classifying spaces; genus-zero connectivity proved; low cases independently checked through Stein Morse theory and exact Levi polynomials. |
| Part 5(c) | P5c1–P5c4 | Complex-of-groups construction, complete n5/n6 presentations, first syzygies and support types, four manuscript elementary cases. |

## Critical distinctions

1. The hexagon answer Z^4 is a **bicategorical** groupoid colimit, equivalently pi_1 of a homotopy colimit. A strict colimit of six arbitrarily chosen one-object groups gives Z^3 and is not the descent calculation. Extra two-isomorphisms coming from depth three are extra data; their inclusion repairs the formula.
2. The general codimension bound is about full piece homotopy types. Replacing each piece with BPi_1 requires aspherical strata. It does not require meridian injectivity. This is distinct from replacing the exit infinity-category by its homotopy category.
3. The poset P_k is infinite, of **isotopy classes** of multicurves. Finite stable labelled trees are its mapping-class quotient. Their homology cannot certify P_k connectivity. Boundary agent independently checked those finite quotient counts, which should be kept separate.
4. At k=d the empty multicurve must be included. It represents the open stratum and makes P_k a cone. Omitting it makes n6,k3 false.
5. Mapping class groups in the explicit presentations fix labelled punctures. Literal boundary circles fixed pointwise add a noncanonical central Z^n factor in genus zero (n≥3).
6. The twenty-four syzygies describe the displayed finite presentation two-complex, as the two-skeleton of an aspherical graph-bundle three-complex. They do not identify its second homotopy with the Steinberg module of the whole boundary thin part.

## Executed computations

- `code/levels_colimit.py` and `levels_colimit_output.txt`: constructs index order complexes; graph spanning-tree presentations; exact Tietze elimination. For C^3 depths≤2: (V,E,F)=(6,6,0), one surviving index generator, Z^3×Z=Z^4. Depths≤3: (7,12,6), no survivor, Z^3. Exact boundary matrices verify sharpness examples k=0,...,4.
- `code/levels_braids.py`, `levels_braids_output.txt`, `levels_braids_actions.json`: free-word reduction, Artin automorphism composition/inverses/braid relations, all six M0,5 and twenty additional M0,6 conjugation identities checked as equal automorphisms in B4 and B5 respectively. Six base relators acting on four fibre generators give twenty-four exact compatibility checks. An initially tempting sign convention failed this check and was corrected: positive conjugation on standard kernel generators uses the mirror Artin word.
- `code/levels_stein.py` and `levels_stein_output.txt`: exact Levi matrices for five and nine arrangement forms. All principal minors have constant term one and positive coefficients. Full determinant has 14 and93 monomials respectively. The paper proves the topological deduction by proper semialgebraic Morse exhaustion and reversing handles. These computations do not purport to enumerate an infinite curve complex.

## Manuscript readings

Scans 147/152 and 147/60 were visually inspected in full. Scan152 shows the unstarred X in (247); mathematics corrects it to X*, without claiming an invisible star was deciphered. The margin's request for two-arrows points toward the missing depth-three coherence. Scan60 has exactly four indecomposable types: (0,4),(1,1),(0,5),(1,2); products are not extra elementary types. Scan151's struck draft was read in the transcription; its depths-through-three clause remains withdrawn. See the contribution CSV for precise reading rows.

## Verified primary literature

- Harer (1988), *The cohomology of the moduli space of curves*, Chapter1 Theorem1.1 (Fenchel–Nielsen coordinates), Chapter3 Lemma3.6 (boundary/curve-complex comparison), Chapter4 Theorem4.1 (wedge-sphere theorem). Full text opened: https://imag.umontpellier.fr/~calaque/GdT-CGEMC-Harer.pdf . Web refs `turn23view0`, `turn24view1`, `turn32view0`, `turn32view1`. I deliberately cite the directly checked 1988 theorem numbering, not a recalled 1986 number.
- Björner–Wachs–Welker (2009), Corollary4.4, rank selection. Author manuscript opened: https://www.math.miami.edu/~wachs/papers/scm.pdf . Refs `turn19view2`, `turn23view3`. The paper supplies its own direct deletion proof to cover the infinite curve complex.
- Fadell–Neuwirth (1962), Theorem1, printed p111, local triviality and section. PDF opened and page111 visually checked locally. https://ncatlab.org/nlab/files/FadellNeuwirth-ConfigSpaces.pdf . Ref `turn19view0`; webpage metadata `turn23view1`. Search OCR incorrectly said1982 and F_(m+1,n+1); actual image says1962 and F_(m+1,n−1).
- Shpilrain (journal2001, arXiv2002), TheoremA, representation(1), parameter1, faithful Artin action. https://arxiv.org/pdf/math/0203167 . Refs `turn19view3`, `turn45view1`. Journal metadata from author's arXiv page: IJAC11(2001),773–778.
- Milnor (1963), *Morse Theory*, Theorem3.2, Remark3.3, Theorem3.5, Theorem7.2 and proof of7.4. https://luis.impa.br/aulas/topdif/Milnor_MorseTheory.pdf . Refs `turn27view0`, `turn32view2`, `turn32view3`. Paper gives its own Hessian/index argument and checks properness/finiteness needed for a boundary comparison.
- Hatcher–Lochak–Schneps (2000), §2 Theorem2 and Remark4, printed p9. Full scanned paper opened and downloaded; pages6,8,9 visually checked. https://webusers.imj-prg.fr/~pierre.lochak/textes/crelle.pdf . Ref `turn45view0`; scan p9 directly states simple connectivity and four elementary support types. Hatcher's1999 preprint version also opened, ref `turn19view4`; actual published numbered theorem is used in the manuscript.

No novelty claim is made. Bibliographic contribution entries all record `verified` and what was actually opened. Downloaded source PDFs are outside the deliverable tree in `research/levels/`; they should not be bundled as authored deliverables.

## Residual review points for integration

- General-position statement for the stack case concerns the classifying space and local Borel approximations, never the coarse quotient.
- `L_{<=r}` is the boundary corner-depth truncation, not deletion of complex codimension-r strata in X; the critical real codimension is d−1.
- If the main paper introduces notation differently, retain the P5 labels or update the contribution register consistently.
- The20-entry action table may need small type or a split table at final compilation; source math is already fully explicit.
