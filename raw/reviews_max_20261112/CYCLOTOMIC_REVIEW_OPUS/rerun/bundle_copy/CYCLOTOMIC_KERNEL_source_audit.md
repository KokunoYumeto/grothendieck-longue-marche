# CYCLOTOMIC_KERNEL: source and proof audit

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 12 November 2026. Verification means the stated version and specified passages were opened; it does not mean that an inaccessible publisher version was inspected. No claim of priority is made.

The requested Stix publisher-text collation remains unfinished. The supplied 2008 version and the 2012 author manuscript are the versions used for mathematical content. The source records below retain that limitation.

# Arithmetic and inertia contribution: source and proof audit

## Written contribution

- `sections/A_agent.tex`: Statements A1–A8. A1 proves all four arithmetic assertions of A(a); A3 gives the requested all-normal-subgroups inertia criterion and the exact Nakamura/Stix comparison; A4 writes out R2 steps (1)–(3); A5 repairs step (4) by the requested direct route; A6 proves R2 and the independent Stix route; A7 handles germs, open subgroups of Γ°, and larger subgroups; A8 records the exceptional geometric types.
- `sections/E_arithmetic_agent.tex`: AE1 proves the finitely generated specialization assertion and transfers the centralizer proof; AE2 proves corrected H1 with the necessary primewise and zero-centralizer qualifications; AE3 supplies the arithmetic instances and the exact CM-subfield criterion for the universally quantified hypothesis over K^ab; AE4 explicitly refutes the uncorrected H1 using the 3-cyclotomic tower.
- `sections/A_agent_results.json`: twelve rows, one per numbered statement.
- `sections/A_agent_refs.bib`: seven verified entries with exact version information.

## Opened sources

1. User-supplied Stix arXiv:0809.0017v1, complete extracted text, with §§3–5 and Appendix B read in detail. Checked Lemma10; Proposition11; Corollaries12–13; Theorem14 and the final lines of its proof; Remark15(2); Lemma19; Theorem20 and its proof; Corollaries21–22; Proposition43; Proposition44; Theorem45. The literal phrase in Lemma19 is “A number field k such that kQ^ab/Q^ab is finite.” The proof here does not silently reinterpret that phrase: A1 proves the finite-cyclotomic-extension case directly.
2. Stix author manuscript, dated 24 February2012, at https://www.math.uni-frankfurt.de/~stix/research/preprints/STIXcuspsec20120802homepage.pdf. Checked Proposition16(1)–(3); Theorem17; Remark18(1)–(3); Definition26; Lemmas27–28; Definition29; Theorem30; Corollaries31–32, including proofs. Theorem30 is prime-specific and assumes a nontrivial closed pro-ℓ subgroup, whereas Theorem20 of the attached version uses a general nontrivial closed subgroup with procyclicity in the equivalent conditions. Remark18(3) explicitly records G_m having both packets equal to all sections. Publication metadata (ASPM63(2012),519–563) was checked at the author's publication list and the MSJ official volume page.
3. The actual Stix publisher route was attempted through DOI10.2969/aspm/06310519 and Project Euclid's official chapter URL. It returned a security notice, not the article. The MSJ-linked AMS archive timed out and AMS bookstore returned403. Consequently the publisher PDF itself has **not** been inspected. The document always distinguishes the inspected author2012 manuscript from that missing publisher-PDF inspection. No statement is based on a claim that the latter was opened.
4. User-supplied Nakamura, *Galois rigidity of pure sphere braid groups and profinite calculus*, J.Math.Sci.Univ.Tokyo1(1994),71–136. Read §2.1, printed pp.93–97: the setup, cyclotomic normalizer definition, (2.1.1)–(2.1.4), and proofs. Its pro-C scope is stated explicitly rather than inferred by passing from the full group to a quotient.
5. Katz–Lang with Ribet appendix, downloaded from the Princeton author archive, https://web.math.princeton.edu/~nmk/old/AbsFinThm.pdf. Read the complete Appendix, including Theorem1, Theorems2–3, the ramification lemma, and both proofs. The used input is Theorem1: for an abelian variety A over a finite number field k, torsion over k(μ∞) is finite.
6. Murotani–Ozeki author manuscript dated17January2025, https://www.sci.kanagawa-u.ac.jp/math-phys/yozeki/pdf/KTRibet.pdf, shared in the workspace by the covering agent. Read Introduction/Theorems1.1,1.3,1.4 and Corollary1.2; Definition3.1; Theorem3.8 and its proof; Definitions3.11; Lemma3.13; Corollary3.14; Proposition3.15 and its proof; Corollary3.16. The exact field criterion is that K^ab is AVKF precisely when K contains no CM subfield. Primewise finite torsion is sufficient for the Tate-module hypothesis; the total torsion finiteness problem over K(K^{1/∞}) is not assumed.

## Corrections and reductions proved here

- R2 is proved. Its original step(4) omits an orbit-separation issue and an existence argument for its chosen covering. A5 repairs both. Distinct C-orbits are obtained from finite derangements. If a covering H≥C has exactly two cusps, every C-element dies in the compactified fundamental group, so a nontrivial compact étale cover retains C and supplies at least three cusps. The two products zz′ and z²z′ then give the contradiction.
- The direct step(4) argument proves a geometric lemma: a closed subgroup all of whose nonidentity elements are inertia lies in one inertia group. It does not require cyclotomic triviality and therefore also handles H1.
- The claim about divisible abelian points follows from a direct Kummer cocycle calculation and normality; the compact-coefficient inflation-restriction step is not left formal. The number-field Kummer injectivity needed there is proved by reductions modulo powers of one good prime, avoiding any finite-generation shortcut.
- Divisible units over finite cyclotomic extensions are exactly roots of unity. The proof uses an explicit element of the open cyclotomic image and the cocycle identity (t−1)f(q)=(q−1)f(t), together with a direct proof of injectivity of number-field Kummer theory.
- H1 must retain prime components. For a fixed cusp, the centralizer is the product over primes at which χ_ℓ is identically1. Triviality of the entire character is unnecessary. When no prime component is trivial, every centralizer is1, including those of cuspidal sections.
- For normal Δ satisfying the Tate hypothesis, the fixed field and all its finite extensions are AVKF by the same Kummer argument. This proves uniqueness of a fixed cusp even when its centralizer is zero, and proves descent of cuspidality to the full section. For a nonnormal Δ with no trivial prime component, that additional uniqueness assertion remains outside the proved statement; the exact assertion is recorded in AE2.
- Finitely generated characteristic-zero fields are handled by spreading an abelian variety over a geometrically integral number-field model. Torsion and division points extend as sections of finite étale schemes after cyclotomic extension of constants, and evaluation injects torsion into a number-field cyclotomic fibre. This writes out the specialization map and why it is injective.
- For Δ=G_{K^ab}, the universal Tate hypothesis holds exactly when K has no CM subfield. This is the quantified field statement required by H1, with a failure witness after a finite extension constructed in the opened Theorem3.8 proof.

## Computations run

`code/A_boundary_checks.py` was run successfully; its full output is `code/A_boundary_checks.out`. It verifies average fixed-coset count1 and existence of derangements for S2 throughS6; it verifies the three-cusp two-product calculation for all nonzero coefficients modulo3,5,7,9,15,25; and it records the mod2 failure of replacing the torsion-free integral calculation by one small finite quotient. These are checks of finite instances, not a substitute for the profinite proof.

## Remaining requirement in this contribution

The actual publisher PDF of Stix2012 remains unopened owing to the observed publisher access failure. The author2012 theorem statements and numbering have been checked directly. PartA(f) is handled by the parent, not by these files. The arbitrary-nonnormal-Δ zero-centralizer cusp-uniqueness extension is stated exactly but not proved or refuted here. No section-conjecture surjectivity is assumed, and no new priority is claimed.


## Ihara and Kodani source verification

7. Hisatoshi Kodani, *Arithmetic topology on braid and absolute Galois groups*, Kyushu University doctoral thesis, March 2017, https://catalog.lib.kyushu-u.ac.jp/opac_download_md/1806826/math0211.pdf. The PDF title page supplies March 2017 (the repository cover assigns the academic year 2016). Read section 4.3, printed pp. 71–73 (PDF pp. 77–79), in full. Lemma 4.3.1 states the rank-one module result and attributes it to Ihara's Theorem 2(i); equation (4.3.2) defines the Galois scalar; Theorem 4.3.3 identifies it with the reduced Gassner representation and proves the explicit coefficient formula. The intervening paragraph constructs the inverse limit of Tate modules of Fermat Jacobians and its rank-one module identification. Theorem 4.3.4 states the exact Jacobi-sum specialization with the nonzero a,b,a+b and primitivity conditions. Download: `background/literature/new/kodani2017.pdf`; extraction: `source_text/kodani2017.txt`.
8. Yasutaka Ihara, *Braids, Galois Groups, and Some Arithmetic Functions*, Proceedings ICM Kyoto 1990, Volume I (1991), pp. 99–120. Read the official IMU-hosted full-volume PDF at https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1990.1/ICM1990.1.ocr.pdf, specifically sections 6.1–6.4, printed pp. 114–117. Section 6.1 uses the tangent at 0 towards 1 and explicitly compares the older tangent-at-infinity convention in its footnote. Section 6.4, printed p. 116, states that the abelianized derived subgroup is free of rank one over the completed group ring with generator the commutator, and formula (6.4.1) gives its Galois scalar. Printed p. 117 identifies the abelian covering as the Fermat curve, gives its map to the thrice-punctured line, and explains the Jacobian-torsion relation. The source's unnumbered Jacobi-sum theorem describes the value as essentially a Jacobi sum; the exact normalization is therefore taken from Kodani Theorem 4.3.4 if needed. Download: `background/literature/new/ihara_icm1990_volume1.pdf`; extraction: `source_text/ihara_icm1990_volume1.txt`. This is a direct original-author source, not solely a later citation.
9. Ihara's original *Profinite braid groups, Galois representations and complex multiplications*, Annals of Mathematics 123 (1986), pp. 43–106, DOI 10.2307/1971352: metadata checked on the official Annals page https://annals.math.princeton.edu/1986/123-1/p03 and the author's publication list. The full 1986 article has not been opened; its theorem content is supported here by the opened 1991 original-author account and Kodani's reproduced statements and proofs. No verified-content claim is made about the unread 1986 full text.

## Independent checks of the parent's additional sections

`sections/A_root.tex`, Statement A9: checked the change-of-generators identity [(ab)^{-1},b]=(ab)^{-1}[a,b]^{-1}(ab), its unit scalar on the metabelian module, and the invariance of that scalar over the full cyclotomic kernel. Checked the nine-vertex Fermat cover chain and the functional with value 1−omega; it kills all boundary cycles and detects the commutator integrally. This supplies an explicit map from the commutator to a nonzero Fermat-Jacobian Tate class, rather than relying on a categorical comparison.

`sections/E_root.tex`, Statements E1–E3: checked the pro-5 tangential involution t_n↦−t_n (where t_{n+1}^5=t_n), its Galois invariance and exact order two, the class-two additive splitting with one-half commutator correction, the CM eigenspace argument over Q(i), and the elimination of the central shear. Checked the normalized primitive procyclic subgroup, its maximality, and its non-inertia projection. Checked that the last lower-central layers consist of actual fixed elements for the abelian Galois kernel, while the displayed non-inertia witnesses do not form a compatible inverse-limit family. The first lifting obstruction is explicitly a continuous cocycle in the third lower-central layer; its arithmetic value is not claimed to have been computed. Supplementary proof paragraphs are in `sections/E_class2_review.tex`.

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

# Source and computation record: D(c)–(e), local contribution to E(d)

Prepared for the combined research paper by the cyclotomic-coverings workstream. This record describes opened sources and actual computations; it claims no priority. The mathematical contributions are in `sections/D_agent.tex` (D1–D13) and `sections/E_local_agent.tex` (D14–D15). The bibliographic entries are in `sections/D_agent_refs.bib`; every entry is marked **Verified** there. The shared Nakamura entry is maintained by the inertia workstream.

## Outcome and scope

| Requested part | Delivered result | Remaining task |
|---|---|---|
| D(c), abelianization | D1 gives the exact equal-class pairs, including the proof that a distinct pair forces a split genus-zero boundary. | None for the stated cyclotomic base. |
| D(c), explicit pair | D3 proves equality of the fibre Galois sets for every prescribed two-step cover; 7,800 exact finite checks were run. D4 supplies a degree-81 finite étale cover separating the full sections. | None for this pair. |
| D(c), all hyperbolic curves | D2 proves full point-section injectivity over every finite extension of the cyclotomic base and every finitely generated extension. | Section surjectivity is not part of this injectivity result. |
| D(d), Theorem 1 | D8, using B12, proves the open-subgroup centralizer assertion in the full stated field generality. | None in that assertion. |
| D(d), Theorem 2 | D6 proves faithfulness for morphisms of fields over the specified cyclotomic base. | No claim about unrelated actions on the coefficient field is substituted. |
| D(d), Theorem 3 | D7 refutes the cyclotomic extension by the points 1 and ζ6 of Gm; D1, D2 give the precise replacements for curves. | None for this refutation. |
| D(d), Proposition 54 and precisions | D9 transfers the hyperbolic packet and centralizer statements and retains the type (0,2) counterexample. | No exhaustion of all sections is inferred. |
| D(d), Conjecture A | D5 refutes the proposed extension by the proper genus-four curve t⁶+2y³+4=0. It has no cyclotomic rational point and has a continuous section, with section existence proved. | None for this refutation. |
| D(e) | D10 proves common finite covers and canonical functorial completion; D11 proves continuous descent with the exact finite-extension quantifiers; D12 describes automorphisms for proper curves. | **Unfinished:** no construction or exclusion of a discontinuous number-field action normalizing no finite-level deck group; no affine commensurator-completion theorem proved. D13 gives the exact cocycle problem for U03. |
| E(d) | D14 computes the entire maximal prime-to-p fixed group for good marked reduction, integral points avoiding the boundary, integral tangent sections and all their cuspidal twists. | **Unfinished:** the full group even in the specified U03/Q5 example, and both groups for the specified bad-marked-reduction example. D15 proves the exact nonabelian H¹ lifting obstruction. |

D13 and D15 have status `Open` in the machine-readable result ledger and explicit partly-settled/unfinished headings in the paper. These statuses record the work left in this response; they do not assert a literature-wide impossibility result.

## Primary sources opened and used

### Tsujimura: AVKF and cyclotomic fields

**Verified.** Shota Tsujimura, *Birational anabelian Grothendieck conjecture for curves over arbitrary cyclotomic extension fields of number fields*, Advances in Mathematics 435 (2023), article 109380, DOI `10.1016/j.aim.2023.109380`. The opened primary text was the author preprint RIMS-1957 of 24 February 2022:

<https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1957.pdf>

The paper uses the numbering of this opened text and says so in the bibliography.

- Proposition 1.2(ii): a finitely generated extension of an AVKF field is AVKF.
- Proposition 4.2: for a hyperbolic curve over an AVKF field of characteristic zero, its geometric points are separated by germs of the point-defined sections; its stated bijection has the subset of point-defined germs as target.
- Theorem 4.7 was also read to check scope. It assumes TKND–AVKF in characteristic zero and an additional surjection from the multiplicative group to Z in its birational reconstruction setting. That theorem was not used as a section-surjectivity assertion.

D2 supplies its own positive-genus covering and descent proof, and compares it with these statements. In particular, it does not turn the target of Proposition 4.2 into all section germs.

### Hoshi–Mochizuki–Tsujimura

**Verified.** Yuichiro Hoshi, Shinichi Mochizuki and Shota Tsujimura, *Combinatorial Construction of the Absolute Galois Group of the Field of Rational Numbers*, Journal of Mathematical Sciences, The University of Tokyo 32(1) (2025), 1–125:

<https://www.ms.u-tokyo.ac.jp/journal/32-1-1.pdf>

Both the downloaded author manuscript dated 29 July 2024 and the published text were opened. The following statements were checked in the published text:

- Definition 3.3(vi), the ISC condition: the point-defined geometric-conjugacy decomposition classes of every hyperbolic curve over every finite extension distinguish its rational points.
- Proposition 6.4, printed p.108: an AVKF subfield of Qbar satisfies ISC and the paper's CS condition.
- Proposition 6.3(i), printed p.103: the stated sparse Galois extensions of a number field's compositum with Qab satisfy its AVKF conclusions. Its exact sparsity hypothesis is retained; no arbitrary larger-extension inference is made.

Only Proposition 6.4 and Definition 3.3(vi) are needed in D2. Published bibliographic year and volume were checked rather than inferred from the author-manuscript date.

### Elliptic-curve arithmetic used for the degree-81 cover

**Verified.** James S. Milne, *Elliptic Curves*, second edition, World Scientific, 2021, author-hosted text:

<https://www.jmilne.org/math/Books/EC2.pdf>

- II, Proposition 6.3: prime-to-characteristic n-torsion is a rank-two Z/n-module.
- II, Proposition 6.4: the characteristic polynomial and determinant of an elliptic endomorphism on the Tate module, with determinant its degree.
- V, Proposition 8.1: the ℓ-adic torsion representation is unramified at good primes different from ℓ.
- V, Proposition 8.3: the Frobenius trace at such a prime is p+1−#E(Fp).

The text at II pp.70–71 and V pp.220–221 was opened. These statements are applied to Y²=X³−432, ℓ=3, p=7. The calculation #E(F7)=9 is independently enumerated. The commutator with complex conjugation fixes Q(μ∞) because cyclotomic extensions are abelian; the proof does **not** require an unverified invocation of Kronecker–Weber.

### The no-point curve and section-existence proof

**Verified.** Pete L. Clark, *Abelian points on algebraic curves*, arXiv `math/0604263`, version 1, 11 April 2006:

<https://arxiv.org/pdf/math/0604263>

Theorem 1: for p≡−1 modulo 3 and integers a,b,c prime to p, the diagonal cubic aX³+bpY³+cp²Z³=0 has no point over Qp^ab. D5 uses p=2, a=b=c=1 and reproduces the valuation obstruction directly in every Q(μN); the local abelian-field theorem is not a substitute for that comparison. The proper map from the genus-four curve is explicitly [t²:y:1].

**Verified.** James S. Milne, *Class Field Theory*, version 4.03, 6 August 2020:

<https://www.jmilne.org/math/CourseNotes/CFT.pdf>

- VII, Proposition 7.2: every Brauer class of a number field is split by a finite cyclic cyclotomic extension.
- VII, Lemma 7.3: the accompanying construction supplies a totally complex cyclic cyclotomic extension with specified divisibility of the local degrees at a prescribed finite set of places.
- III, Theorem 2.1: the local invariant identifies the nonarchimedean local Brauer group with Q/Z, with restriction multiplying invariants by the local extension degree.
- VIII, Theorem 4.2: the number-field Brauer local-global exact sequence, in particular injectivity into the sum of the local groups.
- II, Proposition 1.30: restriction followed by corestriction multiplies by the subgroup index.

D5 proves the required consequences instead of quoting a bare cohomological-dimension/projectivity assertion. Every Brauer class over a finite extension of Q(μ∞) descends to a number field, and the cyclotomic splitting extension is already contained in that larger field. The proof then establishes H² vanishing for every finite module by the pro-ℓ Sylow reduction and gives a finite Frattini-kernel argument solving the finite embedding problems. Recursive lifting through a countable cofinal characteristic system in the geometric curve group constructs a continuous section. This avoids invoking the freeness of the absolute Galois group of Qab or any section conjecture.

### Poincaré-cover automorphisms in the proper case

**Verified.** Amir Džambić and Gabino González-Diez, *Galois action on Fuchsian surface groups and their solenoids*, Forum Mathematicum 33(2) (2021), 375–395, DOI `10.1515/forum-2020-0148`; opened author text:

<https://arxiv.org/pdf/2006.02817>

- Theorem 7 identifies the holomorphic automorphism group of the inverse-limit solenoid with the Belyaev completion of the uniformizing lattice's commensurator.
- Proposition 3 gives the compact open profinite completion of the lattice, the deck-times-commensurator decomposition and the corresponding coset description.
- The hypothesis used throughout is a **compact** Riemann surface of genus at least two. D12 keeps that hypothesis. The construction around equations (11)–(14) was also read to identify the commensurator map on finite covers.
- The arithmeticity index criterion is explicitly recorded in the opened Introduction, p.3, and used in the discussion of Corollary 11: the commensurator has infinite index over the lattice in the arithmetic case and finite index otherwise. The original Margulis book was not separately opened; no invented Margulis theorem number is supplied.

D12 proves the comparison between the analytic inverse-limit object and the algebraic pro-curve through finite covers. Its use of the compact-surface theorem gives no proof of the affine case. That exact missing extension is retained in D13.

### SGA 1 and the algebraic comparisons

**Verified.** *Revêtements étales et groupe fondamental (SGA 1)*, recomposed and annotated edition, Documents Mathématiques 3, Société Mathématique de France, 2003, arXiv version 2 of 4 January 2004:

<https://arxiv.org/pdf/math/0206203>

The following statements and their surrounding hypotheses were opened:

- XII, Corollary 4.5: full faithfulness of analytification for proper complex schemes.
- XII, **Theorem 5.1**: Riemann existence, finite étale covers of a complex scheme locally of finite type versus finite analytic coverings. The theorem number was checked against the displayed statement. An earlier draft's `5.2` reference was corrected.
- XIII, Corollary 2.9: the local constancy and base-change result for the relevant prime-to-residue-characteristic torsors under smooth proper variation with relative normal-crossings boundary; this also supplies the characteristic-zero algebraically closed base-extension comparison used for finite covers.
- XIII, 2.10: specialization construction.
- XIII, Lemma 2.11: compatibility of specialization with the inertia groups at the boundary.
- XIII, 2.12 and its proof were read for context, especially the prime-to-p fundamental-group comparison.

For D14, the hypothesis is a smooth proper model with **finite étale boundary**. A point section is required to come from a point integral on the open model. A K-rational point reducing into the boundary is not silently covered by the unramified based-action argument. An integral tangent vector is required to have nonzero reduction. The proof then explicitly computes the effect of every completed Kummer twist.

**Verified.** The following Stacks Project statements were opened on 12 November 2026:

| Tag | Number in opened text | Exact use |
|---|---|---|
| [01YV](https://stacks.math.columbia.edu/tag/01YV) | Lemma 32.2.2 | Existence of inverse limits with affine transition maps. |
| [01ZB](https://stacks.math.columbia.edu/tag/01ZB) | Proposition 32.6.1(3) | Factorization of a morphism from a quasi-compact, quasi-separated affine-transition inverse limit to a locally finitely presented target; equality after refinement. |
| [05K0](https://stacks.math.columbia.edu/tag/05K0) | Lemma 37.43.3 | Zariski's main theorem for a quasi-finite separated map. |
| [0BY1](https://stacks.math.columbia.edu/tag/0BY1) | Theorem 53.2.6 | Equivalence between function fields in one variable and normal proper curves with nonconstant maps. |
| [0C0R](https://stacks.math.columbia.edu/tag/0C0R) | Theorem 58.30.3 | Prime-to-p specialization isomorphism for smooth proper curves. |

D10 proves the missing finiteness of the descended common-level map; it is not inferred merely from dominance. D11 identifies the function-stabilizer topology with the Krull topology on the arithmetic group and proves compactness of the section image directly.

### Local centralizers and the scope of Mochizuki's lemma

**Verified, shared primary text.** Hiroaki Nakamura (1994), the paper recorded under the shared key `Nakamura1994`. The text at §2.1, printed pp.94–97, was read from the supplied/extracted source `source_text/nakamura.txt`, and checked with the inertia workstream.

- The full class of finite groups is required to be closed under subgroups, quotients and extensions. All finite groups of order prime to p meet these hypotheses.
- Lemma (2.1.2): in a free pro-C group, the centralizer of a nonidentity element of a free-generator subgroup is that subgroup.
- Corollary (2.1.3) and the peripheral comparison give the needed separation of cusp inertia.
- The last paragraph of the proof of Lemma (2.1.4) handles a single cusp by passing to an unramified compact mod-ℓ homology cover of degree ℓ^(2g). Taking ℓ≠p stays inside the prime-to-p class and creates several cusps.

D14 therefore uses a theorem about the **maximal prime-to-p group itself**. It does not deduce that group's centralizer from the centralizers of the separate pro-ℓ quotients. The boundary-separation proof from A2 is also transferred with its comparison maps and the coefficient ring ∏ℓ≠p Zℓ.

**Verified, supplied primary PDF.** Shinichi Mochizuki, *The Absolute Anabelian Geometry of Hyperbolic Curves*, in *Galois Theory and Modular Forms*, Developments in Mathematics 11, Kluwer, 2004, 77–122. The supplied PDF is in `background/literature/mochizuki-absolute-anabelian/absolute_anabelian.pdf`; its extracted text is recorded below. Lemmas 1.3.7–1.3.9, author-manuscript pp.18–20, were opened.

- Lemma 1.3.7 treats the commensurable terminality of inertia in the indicated full and pro-ℓ groups.
- Lemma 1.3.8 identifies the arithmetic quotient group-theoretically.
- Lemma 1.3.9 starts from an isomorphism of arithmetic fundamental groups of hyperbolic curves over finite extensions of p_i-adic local fields and proves equality of types and preservation of cusp inertia, in full and pro-ℓ geometric groups.

D15 states this arithmetic-isomorphism hypothesis explicitly. The comparison with a specified section is the map q:π→π^(p′), giving q(π^Δ)⊆(π^(p′))^Δ and an H¹ obstruction for equality on each element. The paper does not claim that Lemma 1.3.9 computes these fixed subgroups. A request for the author's public PDF URL returned no usable text; the supplied PDF was the primary text actually used.

## Exact computations and what they prove

### `code/D_coverings.py`

The code uses rational polynomial arithmetic and exact finite enumeration. Its actual output is saved as `code/D_coverings_output.txt`.

1. It simplifies the two-step radicand comparison to the exact zero polynomial and checks all n,m from 1 to 12 and every ζ∈μn: **7,800** branch checks. It verifies the equivariant branch formula from D3. The general identity in the proof, not the finite range by itself, establishes the conclusion for all n,m.
2. It computes in Q[a]/(a⁶−a³+1), with a=ζ18. On Y²=X³−432 it gives 3P=(0,24a³−12), hence P has exact order 9.
3. For the nine points over ζ6, the orders of Q−P are `{1:1,3:8}`. For the nine points over ζ6⁻¹, every Q−P has exact order 9 and has triple 3P. All nine individual rows are printed.
4. It enumerates #E(F7)=9.
5. It verifies the matrix of multiplication by 3+6ω, its Smith form `(3,9)`, and its kernels modulo 9, 27 and 81. Each enumerated kernel has 27 elements and is killed by 9.

The matrix computations support the arithmetic proof that every F-rational 3-power torsion point is killed by 9. The separating conclusion uses that proof and the exact order-9 fibre differences: a point in the second degree-81 fibre would have order 27. The map from an actual arithmetic section to its permutation action on this finite étale fibre is stated in D4; a fixed-point-count discrepancy therefore disproves conjugacy of the full sections.

### `code/D_cyclotomic_counterexample.py`

The code checks the polynomial identity for the morphism to the diagonal cubic, computes gcd(t⁶+4,6t⁵)=1, checks the degree-three ramification calculation giving genus 4, and verifies the residue obstruction for powers of 2 modulo 3. Its saved output is `code/D_cyclotomic_counterexample_output.txt`.

The program is a finite certificate for these algebraic computations. The absence of points at every cyclotomic level and the existence of the continuous section are proved in D5; those infinite assertions are not inferred from a bounded search.

### Local calculations

D14 is proved by unramified pointed specialization, the exact Kummer valuation decomposition and the full-class inertia-centralizer theorem. It does not claim a finite computation of the wild kernel. The root workstream's Heisenberg computations check the relevant finite inner-conjugation formula; they do not settle D15's H¹ lifting classes. The full-group and bad-reduction tasks remain explicitly unfinished.

## Manuscript readings and page-number correction

The scans used for the cyclotomic claims are `scan062_a`, `scan062_b`, `scan063_a`, `scan063_b`, and `scan032_a`. These were visually inspected. The transcript at scan 22 was also checked to determine the groupoid-over-the-base hypothesis of Theorem 2. Earlier broad pages were read with the other workstreams' direct scan checks.

- **Scan 62 is manuscript p.30**, not p.61. The footer/archive count must not be used as manuscript pagination. All local TeX and ledger references were corrected.
- Scans 13–15 correspond to manuscript pp.6–7; scan 22 to p.10; scan 32 to p.15; scan 63 to p.31.
- The words “tous nos beaux énoncés” in scan 62 do not by themselves specify which assertions should survive. D5 and D7 give concrete mathematical refutations of the blanket reading, while D2 and D6–D9 list the assertions proved.
- Theorem 2 is a statement about the functor to groupoids **over the base groupoid**. D6 therefore names its F-linear field embeddings. The proof handles the inner ambiguity through its induced Kummer maps; it does not assume that unrelated coefficient-field embeddings agree.
- Theorem 3's principal assertion is sufficient for the Gm counterexample; no uncertain marginal word is used to manufacture its scope.
- Scan 63 explicitly discusses actions for which normalization of a finite-level profinite deck group is not assumed. D11 proves normalization only after the stated open-stabilizer hypothesis and passage to an open subgroup. D13 retains the unrestricted problem.
- The fixed-point notion used throughout D10–D13 is the inverse limit of the geometric points of the finite-level smooth proper completions. Counting the generic scheme point would change the assertion and is explicitly excluded by that definition.

No reading is declared settled solely by the mathematics. The global editorial ledger records the corresponding mathematical evidence.

## Searches and attempts that did not settle the remaining parts

For D(e), we examined the compact-surface solenoid/commensurator theorem and its finite-level construction, searched the commensurator and universal-cover literature, and proved the rational-function continuity descent directly. A tentative modular-translation idea over a cyclotomic field did not produce a checked number-field semilinear action and is **not** included as a theorem or counterexample. The remaining exact task is the abstract cocycle equation and non-normalization condition in D13, already for U03 over Qbar. The compact theorem's hypotheses do not establish the affine automorphism description.

For E(d), we proved the good-marked prime-to-p answer for points and every cusp twist and compared it with the full group through a genuine nonabelian cocycle. The attempted lift requires vanishing of each class `[h⁻¹σ(h)]` in H¹(Δ,ker q); no proof or computation for all these classes was obtained. The smallest retained good full-group case is U03/Q5 with point 2 or the unit tangent at 0. A concrete bad-marked case is P1 minus {0,1,5,∞} over Q5 with point 2; the boundary sections 0 and 5 meet in the special fibre. Neither its full nor its prime-to-5 fixed group has been computed here.

The supplied research notes, unreviewed transcriber arguments and first-pass manuscript transcription were treated as claims to test, not as theorem sources. In particular, abelianized equality of ζ6 and ζ6⁻¹ was not promoted to equality of full sections: D4 proves the opposite by a finite covering.

## Source files and hashes

Downloaded third-party source PDFs and extracted texts were moved **outside the deliverable package** to `source_text/D_sources/`. They are not redistributed in `code/`. Their SHA-256 records are in `sections/D_source_hashes.json`:

| Source file | SHA-256 |
|---|---|
| Clark2006.pdf | `5f004abba40394d2c98778516f33f417847106f5b884fb16bf7a070e10fd607c` |
| Clark2006.txt | `6e07e36f88572e551dfc52682cc1dd2be4b857a455cc8ef6002430926e909752` |
| HMT.pdf | `321fbfcc4d5bc9900aa6540b5618211b78cdfa72fa539915b069569f4dc053fe` |
| HMT.txt | `36d86a2bd9eb1eabee7116ff1be8ecbc37e9ad6ffaa78d9bb32bca6334214f28` |
| Mochizuki2004.txt | `3eece5e0ed787ca0056902805d7f4cdd23e5907299d3e22e0650955ddb86ecd9` |
| MurotaniOzeki2025.pdf | `ca42c45742442eb182dc44979673aae90eb083ed040f5eea427b830adba7ff13` |
| MurotaniOzeki2025.txt | `b9d4981ca61a0db28fbd71509c19ba1d0c757c42ff5dd8b9f740a0c3932580ab` |
| Tsujimura2022.pdf | `82ccc5e0c87bc36a1e41f09ab8084ee0c59ecd0176b2a14c9a56fe3c6b025342` |
| Tsujimura2022.txt | `9de148c529de72d6692ea5582e88ac5ce576a6ab0f9ce4d48c123b7998a3e9f7` |

Murotani–Ozeki was downloaded for the shared arithmetic-input workstream. Its theorem application and bibliographic record are owned by that workstream; D1–D15 do not cite it as a separate unchecked input. The Milne, Stacks, SGA and solenoid sources were opened through the web reader. A local Milne download was unavailable, but the relevant theorem text was available and read through that reader.

Independent D4 source check: Milne, Elliptic Curves, II, Proposition 6.7 was also opened and used for the faithful endomorphism action on the Tate module.

# Sources and comparison checks for the coordinating contribution

## Opened primary sources

1. Hélène Esnault and Phung Ho Hai, *Packets in Grothendieck's section conjecture*, Advances in Mathematics 218 (2008), 395–416. The published PDF at https://page.mi.fu-berlin.de/esnault/preprints/helene/86-Grothendieck.pdf was downloaded and read. Theorem 5.5 and Lemma 5.6, including proofs and their genus hypotheses, were checked. The supplied older preprint has different text at item 5.6. C2 uses the published formulation and supplies a positive-genus covering comparison for the three-punctured line.
2. Giulio Bresciani, *Some implications between Grothendieck's anabelian conjectures*, Algebraic Geometry 8(2) (2021), 231–267, https://content.algebraicgeometry.nl/2021-2/2021-2-005.pdf. Lemmas 10.9–10.11, Corollary 10.12, Theorem 10.16, and Lemma A.22 were opened. C5 uses finite-index goodness and algebraically closed base-extension invariance, with a separate finite-kernel proof of the required profinite homotopy exactness. No section-surjectivity implication is assumed.
3. SGA 1, the recomposed arXiv text https://arxiv.org/pdf/math/0206203. Exposé XII, Theorem 5.1, was opened at PDF p.266. It identifies finite algebraic étale covers of a complex scheme locally of finite type with finite analytic étale covers. A9 and E1 specify the induced geometric profinite and homology maps.
4. Ihara's 1991 ICM account and Kodani's 2017 thesis were opened directly as recorded in the arithmetic source audit above. A9 identifies the rank-one metabelian module, its scalar Galois action, the Fermat-Jacobian quotient, and the change of generators. The Ihara–Kaneko–Yukinari paper and Nakamura's 2019 exposition were also inspected during source location; their downloaded hashes appear in `fetch_root_sources_output.json`, but no theorem is attributed to an unread original text.
5. Hoshi's 2014 published paper, Proposition 2.4 and Lemma 2.8, was opened independently. C5 and C8 retain its exact normality, characteristic-zero, relative-curve, and strictly henselian trait hypotheses. The later sub-p-adic hypotheses of other statements in that paper are not inserted into these two results.

## Source versions and editorial evidence

The supplied scans, transcriptions, R149 notes, war-game excerpts, and LM3/LM3b returns were audited as claims. Decisive scan images were viewed, including scans 45, 48–49, 53–56, 59–62, 66, 127, 130–131, and Longue Marche scans 433 and 483. Each numbered paper statement includes a manuscript/source passage annotation; the readings CSV records 21 mathematical or editorial interventions.

The word `centralisateur` at scan54 and both `L` subscripts at scan127 remain reported as visible readings. The proved normalizer and model-group replacements are displayed through their actual maps. The word before `cas près` at scan66 remains unresolved. The withdrawal of local injectivity at scan130 is preserved and compared with the explicit blowup matrix. No claim is made that the supplied first-pass transcription has been globally corrected.

## Independent proof audits

The direct R2 orbit-separation proof was checked separately from its Stix-based proof. The arithmetic and birational inverse-limit arguments were cross-reviewed with their actual quotient and valuation maps. C8's diagonal-inertia proof was independently checked against Hoshi's published lemma. D4's degree81 cover, Frobenius/complex-conjugation torsion bound, descent, and connectedness were independently audited. D5's Brauer/cohomology/embedding-problem proof and its recursive continuous section construction were independently audited, including reopening Milne VII.7.2. D10–D11's finite-level factorization and continuous descent maps were checked. E1–E3's genuine tangential involution, integral class-two splitting, normalizer correction, and fixed-layer/lift comparisons were checked independently.

These checks support the proofs as written; they do not remove the explicit open or unfinished items. In particular, neither the publisher Stix PDF nor the global R4/H2 specialization comparison is represented as verified.
