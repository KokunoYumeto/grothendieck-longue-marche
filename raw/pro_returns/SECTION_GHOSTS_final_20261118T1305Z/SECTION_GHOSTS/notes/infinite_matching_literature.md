# Focused infinite-support matching literature check

Date: 18 November 2026. Owner: literature agent.

This is a targeted continuation of P.15. It concerns one actual pro-five predecessor with specified lower local point matches, not arbitrary finite solvable realizations. P.16 is reserved; the source at sections/draft_pal_schlank_matching.tex is an unintegrated proof draft awaiting peer review. No new historical claim is closed.

## Decisive applicable theorem: Pál–Schlank

Pál and Schlank's Theorem 1.2 gives an exact global-image equality for a fixed finite embedding problem with abelian kernel of order prime to the characteristic. It does not merely identify a closure. Its adelic solutions are unramified at almost every place. After choosing a global lift t, apply it to the split finite correction problem M_n semidirect C_n -> C_n, with M_n=(Z/5^n)(3)^b and C_n=im(chi_5^3 mod5^n). This parametrizes corrections to t and does not replace its actual predecessor.

The algebraic Brauer group is H1(Q,M_n^D), with M_n^D=(Z/5^n)(-2)^b. Proposition8.1 evaluates its classes by the global sum of local cup-pairings with the corrections. The new draft proves that this gives exactly E.212's residual matching criterion. All corrections away from five are required unramified. At zero support their Frobenius values remain free; no point with the prescribed predecessor is assumed there. At five the finite correction is free. E.209 then turns a successful global finite correction into a reduction of an integral fixed-source correction, and compactness handles all n within this fixed weight.

### Independent comparison beyond quoting the theorem

The draft constructs the dual of an E.212 failure. For D_n=(Z/5^n)(-2), fixed-S5 H1 and H2 vanish. Finite purity gives a unique global dual class from any finitely supported residue character. If that character annihilates the global Soulé-period vector, global reciprocity and the fact that the weight-three generator generates the entire local H1 at five force the dual class to be locally zero at five. Its Brauer evaluation therefore depends only on the specified support places, not on the unprescribed completion. E.212 makes at most two such places sufficient.

When p^3 and q^3 are both1 modulo5^n, the residue choice (tau_q,-tau_p) has evaluation (tau_q d_p-tau_p d_q)/5^n. This detects incompatible ratios when the periods are units. For nonunit periods the draft uses the full finite annihilator; the simple cross product alone need not detect a divisibility failure.

The reference-zero universal cocycle u(m,g)=m on M_n semidirect G_Q produces the relevant Brauer class as u cup c, modulo the arithmetic base Brauer group. Its nonzero edge class demonstrates that it is not an arithmetic-base class. No assertion that these classes automatically extend from a geometric Brauer group, or automatically pair to zero from the ordinary abelian data, is made.

The nonzero group in P.15 is consequently a space of available tests. Its nonvanishing does not establish nonzero evaluation on the actual ordinary point discrepancies. Conversely, Pál–Schlank does not remove the E.212 condition: that condition is exactly what its pairing measures here.

### Opened primary sources and exact locators

Primary author version: https://arxiv.org/pdf/1602.04998, arXiv1602.04998v2,15May2017,37pages.

- Section1, authorpp1–2: finite embedding problems, kernel conjugacy, weak solutions, and Sol_A's almost-all-unramified condition.
- Theorem1.2, authorp3: exact image equality. Independently inspected the rendered PDF page to verify there is no closure bar.
- Lemma2.2 and Definition2.3, authorpp5–6: algebraic Brauer group and the injective edge map. The introduction has an obsolete definition-number reference; the actual body says Definition2.3.
- Section5, Notation5.1 through Theorem5.4 and proof, authorpp13–15: restricted cohomology product, global annihilator equality, and finite-S proof.
- Section8, proof of Theorem1.2 and Proposition8.1, authorpp27–28: exact image and cup-pairing identification.

Working HTML of the same primary author text: https://arxiv.org/html/1602.04998v2. Direct PDF opens initially returned DisabledError, but clicking ViewPDF from https://arxiv.org/abs/1602.04998 succeeded. The actual proof was opened, not inferred from the abstract.

Live source refs: turn873200784view3 (PDF), turn873200784view4 (HTML), turn964404222view4 (visual statement), turn180026384view1 (exact HTML equality), turn932247982view1 (adelic definition), turn180026384view2 (Theorem5.4/proof), turn964404222view1 (Section8/Proposition8.1), turn344671510view2 (edge map).

Publication metadata: Pál, A., & Schlank, T. M. (2022). The Brauer–Manin obstruction to the local-global principle for the embedding problem. International Journal of Number Theory,18(7),1535–1565. DOI10.1142/S1793042122500786. Independently confirmed by the authors' later published companion paper, reference[6] on p19, https://archive.intlpress.com/site/pub/files/_fulltext/journals/hha/2023/0025/0002/HHA-2023-0025-0002-a001.pdf (turn762840403view3), and author publication-list search result turn384776085search0. The final IJNT PDF returned403; all mathematical locators above are explicitly from the opened author version. The later HHA paper is a different paper, Two theorems on cohomological pairings, and was not conflated with the IJNT article.

Root independently opened Theorem1.2, Sol_A's definition, Lemma2.2/Definition2.3 and Section8/Proposition8.1, and confirmed exact image rather than closure. This source verification is not yet a full review of the new P.16 comparison. Cohomology targeted review was requested after E.214 becomes stable.

## Infinite sets in approximation theorems: the quantifier actually supplied

### Ivanov2016

The published Theorem5.3 permits an infinite set T, but prescribes full local H1 only on a finite set T0. Its T-term is a direct sum of inertia cohomology, so it has finite support and supplies no infinite list of Frobenius values. It assumes the complement S\T is p-stable in the stated extension, with a stabilizing field inside K_S. Theorem5.9 has a finite prescribed local set and kills its cokernel only in a direct limit over enlarged base fields. Neither statement retains the required infinite Frobenius tuple over Q. Choosing a large allowed ramification set does not alter that conclusion.

Opened final publisher PDF: https://msp.org/ant/2016/10-1/ant-v10-n1-p01-p.pdf. Theorem5.3 printedp22; Theorem5.9 printedpp24–26; Theorem5.1 printedpp20–21. The first two cover sheets explain the PDF-page shift. The theorem was first read in the author version https://arxiv.org/pdf/1309.2800, then rechecked in the published text. Live refs: turn964404222view2 (published5.3), turn504991080view6 (published5.9), turn344671510view1 (article PDF). Verified metadata: Ivanov,A.(2016), Algebra & Number Theory10(1),1–36, DOI10.2140/ant.2016.10.1.

### Wingberg's stably saturated infinite sets

Theorem2 genuinely treats an infinite set T, assuming it is stably saturated. Its corestricted free pro-p product maps to Gal(k(p)/k^T(p)), a relative kernel over the field where T splits. The theorem does not supply extension of a chosen homomorphism from that kernel to the whole arithmetic group with its required conjugation action. Ordinary support of density zero is not a proof of stable saturation. Theorem1's explicit CM example uses primes inert over the maximal real subfield; it is not the original family's support primes, which split in Q(zeta5). Thus the theorem is not a prescription of our local point paths.

Opened primary author PDF dated15June2014: https://www.mathi.uni-heidelberg.de/~wingberg/agwingberg/paperwingberg/Sat-2013.pdf. Theorems1–2 authorp2; Proposition2.5 and proof authorp16, with restricted-product definitions on p15. Live refs turn493392816view1, turn931647292view2, turn931647292view3. Author publication page https://www.mathi.uni-heidelberg.de/~wingberg/agwingberg/paperwingberg/wingberg41-en.html (turn932247982view2) explicitly calls it a Heidelberg preprint. ArXiv1512.01694 was posted5December2015 (turn762840403view1). No journal status asserted.

### Tavernier2025

Theorem1.4 is an equidistribution result for finite constant abelian groups and continuity sets in an adelic space, retaining a Brauer–Manin condition. Its displayed limiting proportion can be zero and does not itself give a point in a prescribed infinite singleton tuple. Corollary1.5 gives density with restricted ramification types; its finite Grunwald conditions do not fix our cyclotomic module and nonabelian predecessor. It does not imply a compatible pro-five correction tower.

Opened primary preprint https://arxiv.org/pdf/2507.00448, version1,1July2025,35pages: Theorem1.4 authorp5 and Corollary1.5 authorp6. Live refs turn931647292view4 and turn931647292view5; abstract/version metadata turn762840403view2. No journal publication status asserted.

## Scope of the search and the separate compiler query

Queries used included:

- infinite embedding problems prescribed local solutions number fields pro-p approximation infinitely many primes
- pro-p embedding problem infinitely many local conditions Frobenius prescribed number fields
- section conjecture pro-l sections local approximation infinite ramification cyclotomic cohomology
- Ivanov stable sets primes weak approximation cohomology infinite sets local conditions PDF
- Wingberg saturated sets primes infinite prescribed local extensions theorem PDF
- Pál Schlank Brauer Manin embedding problems weak approximation abelian kernel theorem pdf

Both search engines were used sequentially; mathematical conclusions rely on opened primary texts. Broad projectivity and the already-audited finite-S theorems were not used as fresh evidence.

The additional exact queries for BCV/HCF/KFU with Grothendieck and for finite branch covariance produced no pertinent primary mathematical source. No numerical functions for the missing historical A4.57 inputs were recovered. This limited retrieval outcome neither supplies a bound nor refutes the original claim. The prior compiler audit remains authoritative.

No images or downloaded review PDFs were saved in notes. P.16 is an unintegrated draft, and no result/check-event row is being added before checkpoint08 is saved.
