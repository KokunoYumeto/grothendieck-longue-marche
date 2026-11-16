# A68 source and computation ledger — unregistered candidate

Status: registered after full independent root and DE proof/source/exact-certificate audits PASS, including the separately written all-intermediate addendum. The checkpoint13 frozen paper was not changed; approved integration occurred after its23:00 save. Original candidate files remain preserved.

## Fresh primary sources

* **verified:** Qing Liu, *Courbes stables de genre 2 et leur schéma de modules*, Mathematische Annalen295(1993),201–222. Author PDF: https://www.math.u-bordeaux.fr/~qliu/articles/genre2.pdf . Printed203 defines the Igusa and auxiliary I4/I12 conventions; printed204, Theorem1(V*) and(V), is the precise residue-two stable-fibre criterion. The original PDF was opened through web retrieval (`turn1098view1`); its downloaded original pages203 and204 were rendered locally and **actually viewed**, not merely inferred from OCR. They are PDF pages4 and5 counted from1. The full third-party PDF and its two page PNGs are excluded source-cache files, with exact paths and SHA256 values recorded in `notes/fgh_C8_Liu_source.json`. The additive constant in the j-sum formula is literally 2^6·3^3, as seen on the original page; it vanishes in characteristic2.
* **verified:** Andrzej Dąbrowski and Mohammad Sadek, *Genus two curves with everywhere good reduction over quadratic fields*, printed3, equation(3), all five Igusa–Clebsch-to-Igusa conversion formulas. Primary publisher PDF https://journals.sns.it/index.php/annaliscienze/article/download/6999/2547/4995 , opened as `turn1098view0`. Printed2 also gives J10=2^-12 times the discriminant, including the quintic leading-coefficient convention. No claim from this paper's residue>5 minimization section is used at2.
* **verified:** SageMath primary implementation https://github.com/sagemath/sage/blob/develop/src/sage/schemes/hyperelliptic_curves/invariants.py , normalized transvectants, Clebsch A/B/C and conversion to Igusa–Clebsch invariants; opened as `turn1088view0`, exact portions `turn1089view0`, `turn1090view0/1`. Our program independently implements the displayed rational differentiation formulas; it is not an invocation of Sage or a floating approximation.
* **verified:** PARI official documentation https://pari.math.u-bordeaux.fr/dochtml/ref/Hyperelliptic_curves.html , `genus2igusa` example for x^5+3x²−4 (opened `turn1086view0`). The independent transvectant program reproduces all five values after the explicitly checked uniform weighted rescaling from P to4P; the official documentation gives the example values but does not itself state this conversion. PARI's `genus2red` routine is not used; its residue-two scope is insufficient for the present claim.

## Existing proved inputs, reread

* A37, `sections/A_C4_fixed.tex`, paragraph “The possible unpointed special fibres”: the minus-six C4 Jacobian has potential good reduction of2-rank0 at2; the actual elliptic factors have j among1728,8000,10976,128, all reducing to0.
* A41, final torsion-divisor criterion, and A42: potential good Jacobian with p-rank0 and p-primary cusp differences imply rational cusp-joining paths, then the all-prime fixed-group conclusion. The new proof supplies every stated hypothesis.
* A59: actual dihedral geometric Galois closure is nilpotent, so all-prime normalizer classification is already proved.

## Exact executed computations

`notes/fgh_C8_compact_type_certificate.py/.json/.out` checks the actual genus-two quotient equation and differential pullbacks, the seven-dimensional differential determinant modulo Phi8, all Igusa invariants, a primary normalization example, all five Liu criterion valuations, and each exact cusp divisor. It returned PASS. The earlier `notes/fgh_C8_frontier.py/.json/.out` independently checks the actual degree16 map, D16 relations, cyclic4 elliptic factorization, and equality after elliptic duplication.

The finite computation is not used as a substitute for the all-degree geometric fixed-group theorem. The full proof is `notes/fgh_A68_draft.tex`; its status remains candidate until independent audits.

Canonical proof: sections/A_dihedral_eight_fixed.tex. Canonical executed programs: code/a_dihedral_eight_fixed.py, a_dihedral_eight_maps.py, a_dihedral_eight_intermediates.py, with JSON and stdout. Independent ledgers: notes/root_A68_audit.md and notes/de_A68_audit.md; the latter also records the complete intermediate addendum audit. Integration hashes are in notes/fgh_A68_integration.json.
