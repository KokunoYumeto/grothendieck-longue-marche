# Sources opened for Part B and the birational tasks C(e)--(f)

## Verified primary sources and exact locations

1. Dan Haran and Moshe Jarden, *Compositum of Galois extensions of Hilbertian fields*, Ann. Sci. ENS (4) 24 (1991), 739--748. Publisher archive PDF opened and downloaded: https://www.numdam.org/article/ASENS_1991_4_24_6_739_0.pdf. Theorem 2.4, Corollary 2.5 and proofs inspected. Web retrieval refs include `turn8view1`, `turn11view2`, `turn11view3`. The theorem's hypotheses allow infinite Galois extensions of a Hilbertian field. It is used only in its separable-closure form, with the actual fields and the Galois correspondence written out.
2. Moshe Jarden, *Almost locally free fields*, Journal of Algebra 335 (2011), 171--176, DOI 10.1016/j.jalgebra.2011.03.021. Author manuscript dated 25 September 2010 opened at https://www.tau.ac.il/~jarden/Articles/paper99.pdf. Definition (2) in introduction, Proposition 2.5, its proof, and Proposition 2.6 inspected. Publication metadata checked at publisher (`turn27search0`). The exact input is: K Hilbertian, N/K algebraic Galois, N not separably closed; then G_N is almost locally free. Taking two generators excludes a nontrivial abelian normal subgroup of G_K. Web refs `turn8view0`, `turn12view0`, `turn12view1`.
3. Hiroaki Nakamura, *Galois rigidity of pure sphere braid groups and profinite calculus*, J. Math. Sci. Univ. Tokyo 1 (1994), 71--136. Attached PDF opened and converted to text. Corollary (1.3.4) gives center-freeness for pro-C completions of finite-rank free groups of rank >=2 and surface groups of genus >=2; C is a full class of finite groups. Theorem (1.3.2) and its proof, Corollary (1.3.3), and surrounding hypotheses also read.
4. Jakob Stix, *On cuspidal sections of algebraic fundamental groups*, arXiv:0809.0017, attached version. Section 1.3, Proposition 8, Lemma 10, Proposition 11, Corollary 12, Theorem 14 and Remark 15 read. This contribution uses this version's numbering and labels it explicitly. The 2012 author manuscript is verified separately; the publisher PDF remains inaccessible as recorded in the arithmetic source audit.
5. Akio Tamagawa, *The Grothendieck conjecture for affine curves*, Compositio Math. 109 (1997), 135--194, DOI 10.1023/A:1000114400142. Attached published PDF opened. Read Conjecture (0.1)(ii) as the formulation of Theorem (0.3), Theorem (6.3), Theorem (7.2), Remark (7.3)(i). The quoted theorem has k finitely generated over Q and smooth geometrically connected affine hyperbolic curves; it is an isomorphism theorem with target geometric-inner conjugacy.

## Opened basic-numbered source

6. Wulf-Dieter Geyer, *Field Theory*, Luxembourg Winter School on Galois Theory, 15--24 February 2012. https://math.uni.lu/~wiese/galois/Geyer.pdf. Web open failed but direct download succeeded; the actual PDF and extracted text were read. Section 4, Theorem 1 gives number fields Hilbertian; Theorem 2(a) rational function fields, (d) finite extensions, (e) infinite finitely generated fields, (g)(2) abelian extensions of Hilbertian fields. This is an author's numbered exposition of classical results, not a claim that Geyer originated them.

## Supplemental inspected material, not relied on as authority

- Jarden--Shlapentokh, *On decidable algebraic fields*, author manuscript, introduction p.2, confirming the reference to Fried--Jarden Theorem 13.3.5 and Proposition 13.2.1. https://www.math.tau.ac.il/~jarden/Articles/paper105.pdf opened (`turn26view1`), but the final proof uses the directly inspected numbered Geyer statements, rather than claiming to have opened those pages of Fried--Jarden.
- Search results on absolute-Galois centralizers led to MathOverflow discussions and the Minamide--Tsujimura RIMS1973 preprint. These were useful for locating Hilbertian results. No proof relies on a forum response or on the inaccessible Fried--Jarden book text.
- The supplied R3 sketch and reader's notes were read line by line; they are audited in B1, not treated as authority.
- Scans 13--15 and 45 were read in the supplied transcription. Scan 127 lower half was also inspected as an image: both formula subscripts read L. The mathematical replacement by U is explicitly separated from that visual evidence.

## Searches and scope of originality

Queries included "absolute Galois centralizer normal subgroup", "centralizer Galois abelian extension Hilbertian", "Hilbertian prosolvable normal subgroup", "Weissauer 13.9.1", and "Jarden Almost Locally Free Fields" using both search engines where needed. No exact separately stated version of R3 was located in the opened primary sources. B2 is explicitly derived from Haran--Jarden and Jarden, with no priority claim. The direct R3 proof uses a proved elementary split-prime existence argument instead of citing Chebotarev.

## Exact computation run

`code/B_field_certificates.py` was executed with Python 3 and SymPy. Its stdout is `code/B_field_certificates.out`. It verifies:

- x^5-x-1 has factors of degrees 2 and 3 modulo 2 and is irreducible modulo 3; discriminant 2869.
- S5 has derived-series orders 120,60,60, so is not solvable.
- S3 has three Sylow-2 subgroups, so is not nilpotent; discriminant of x^3-2 is -108.
- disc_T(T^2-t)=4t, the explicit nontrivial inertia witness in the scan-127 counterexample.

The finite outputs are used only for these finite claims. They are not offered as evidence of the universal birational section assertion.

## Main additional conclusions

- B(c) is proved for every proper Galois extension M/Q, beyond the six listed fields. The boundary case M=Qbar has centralizer G_Q.
- The three marginal doubts of scans 14--15 are answered, and rank one is an actual omitted exception to the blanket free-group statement on scan 15.
- Formulas (32) and (33) remain equivalent with L; they have the common nontrivial value I_v for a decomposition section. The quotient to a hyperbolic model containing the point kills exactly that inertia and gives the corrected zero formula.
- Packet recovery on the nontrivial-centralizer subset already recovers points and open models without assuming that every birational section belongs to that subset. The universal existence statement itself is not proved.

## Follow-up primary sources for C5 and C8

7. Yuichiro Hoshi, *The Grothendieck conjecture for hyperbolic polycurves of lower dimension*, J. Math. Sci. Univ. Tokyo 21(2) (2014), 153--219. Publisher PDF opened at https://www.ms.u-tokyo.ac.jp/journal/pdf/jms210201.pdf (`turn86view0`), following the official contents page https://www.ms.u-tokyo.ac.jp/journal/abstract_e/jms210201_e.html (`turn85view0`). Author's revised July 2014 manuscript also opened at https://www.kurims.kyoto-u.ac.jp/~yuichiro/rims1764revised.pdf (`turn82view0`, `turn84view0`). Published Definition 2.1, Proposition 2.4(i),(ii) on pp.169--172, and Lemma 2.8 on pp.175--176, including proofs, read directly. The hypotheses in these section 2 statements are characteristic zero and the specified normality/noetherian/separated conditions. The sub-p-adic assumption from later section 3 is not needed here. Local files: `background/literature/B_sources/Hoshi2014_published.pdf/.txt` and `Hoshi2014_polycurves.pdf/.txt`.

8. Magnus Carlson and David Corwin, *Cuspidal sections for varieties of arbitrary dimension*, arXiv:2611.09080v1, submitted 6 November 2026. Primary abstract opened in search (`turn64academia7`); the primary PDF https://arxiv.org/pdf/2611.09080v1 was downloaded and read after web PDF open failed. The first page carries arXiv's 6 November 2026 header and a manuscript date of 9 November 2026. Proposition 3.4, Theorem 3.7, and Propositions 4.9, 4.11, 4.12 read. Proposition 4.12's **closure bar** was verified on a rendered image of PDF p.10, since pdftotext drops it. It asserts C_X ⊂ closure(𝒞_{X,f}), not C_X ⊂ 𝒞_{X,f}. Theorem 3.7 also concerns closure. Local files: `background/literature/B_sources/Carlson_Corwin_2611.09080v1.pdf/.txt` and `Carlson_Corwin_page10.png`.

The new geometric argument in `sections/C8_hoshi.tex` derives nonvanishing of boundary diagonal inertia from Hoshi's trait extension criterion by an explicit formal arc. This settles the nonvanishing clause of C(d) for every elementary hyperbolic polycurve and every smooth normal-crossings compactification. It does not assume the converse boundary-factorization assertion. The audit and exact comparison are in `sections/B_followup_audit.md`.

## Prior-hunch scope audit R4/H2

9. Yuichiro Hoshi and Shinichi Mochizuki, *On the combinatorial anabelian geometry of nodally nondegenerate outer representations*, Hiroshima Math. J. 41(3) (2011), 275--342. The attached December 2011 author manuscript `background/literature/hoshi-mochizuki-nodnon/nodnon.pdf` was opened through its extracted text `source_text/hoshi-mochizuki-nodnon.txt`. Definition 2.10(iv) and Lemma 2.11(ii),(iii), manuscript pp.30--32, give the stated local log-group injections and the sum map on node coordinates. Publication metadata checked at the first author's official paper list (`turn101search0`), and the identical author PDF was located at https://www.kurims.kyoto-u.ac.jp/~motizuki/Nodally%20Nondegenerate%20Outer%20Representations.pdf (`turn101search12`). These results are used only for those exact local maps. A global arithmetic log-specialization comparison carrying those maps into the full generic-fibre group for every trait splitting has **not** been verified here.

`sections/E4_prior_hunches.tex` proves H2(a) by the already opened Stix Theorem 20 and computes the branch-swap inversion explicitly on Kummer roots. It records H2(b) and R4's proposed completion as unproved and unused in this deliverable. R4(i)'s monodromy-weight sketch and R4(ii)'s polarized-isomorphism step are not promoted to checked proofs. The finite-field characteristic-p full-group extension is likewise not inferred from a characteristic-zero or prime-to-p source.
