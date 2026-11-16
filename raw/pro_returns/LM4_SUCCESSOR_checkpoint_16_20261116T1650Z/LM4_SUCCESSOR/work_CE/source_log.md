# Primary source log for Parts C and E.1

All URLs below were opened through the web tool. Where a PDF was also downloaded, its local copy is in `sources/`. The log distinguishes source verification from an independent proof of every theorem in that source.

| Source | Primary URL | Exact portion used and audit result |
|---|---|---|
| Kochloukova & Zalesskii (2007), QJM 58, 47–51 | https://mat.unb.br/~pz/arquivos/Claus3.pdf | Theorem 2 and §1.1: restriction theorem is for full profinite groups, with the stated virtual p-cohomological dimension and elementary-abelian hypotheses. Lemma 1 and Corollary 2 read; the fixed-group freeness corollary is pro-p and is used only in that category. |
| Boggi & Zalesskii (2025), BLMS 57, 236–255 | https://arxiv.org/html/2406.08639v2 | Theorem A, hypotheses and proof. Applications in C/E use p=2 and a single involution. Attached primary TeX also inspected. No nonsolvable finite-subgroup intersection step is used. |
| Boggi (2024), Notes on hyperelliptic mapping class groups | https://arxiv.org/pdf/2110.13534 | Birman–Hilden sequence (3); §7, Theorems 7.1 and 7.2. The induced congruence topology in Theorem 7.1 gives the actual injectivity used in E.4. |
| Boggi (2014), On the procongruence completion of the Teichmüller modular group | https://arxiv.org/pdf/0910.4305 | Theorem 4.5 and proof through Lemma 4.6: full profinite twist lattice and cut-stabilizer exact sequence. |
| Boggi (2020), Congruence topologies on the mapping class group | https://arxiv.org/pdf/1804.06322 | Theorem 1.4(ii), Corollaries 4.5 and 4.7 and proofs; all-finite formation only for the comparison used here. |
| Engler, Haran, Kochloukova, & Zalesskii (2004), JLMS 69, 317–332 | https://www.math.tau.ac.il/~haran/Papers/dehz.pdf | §1 projectivity and Sylow criteria; Theorem 2 and proof via Theorem 5; Lemmas 5.1 and 5.3. The finite-generation hypothesis on the normal free pro-p subgroup is essential in C.1. |
| Morales (2024), Math. Ann. 390, 1507–1540 | https://link.springer.com/article/10.1007/s00208-023-02785-6 | Propositions 2.14–2.15: torsion-free lower-central quotients and residual lower-central separation for pro-p surface groups. |
| Wilkes (2019), JPAA 223, 1617–1688 | https://api.repository.cam.ac.uk/server/api/core/bitstreams/85a7dfb3-ae1a-4f65-b9cf-a088742b052d/content | Accepted manuscript dated 19 June 2018, 73 pages: Propositions 5.7, 6.16 and §3 cup-product/relative-sequence compatibility, particularly Proposition 3.5. |
| Feit & Thompson (1963), Pacific J. Math. 13, 775–1029 | https://msp.org/pjm/1963/13-3/pjm-v13-n3-p01-p.pdf | Main theorem on p.775 opened. Used as the established odd-order theorem; entire proof not independently reaudited. |
| Stukow (2016), C. R. Math. 354, 1029–1031 | https://www.numdam.org/item/CRMATH_2016__354_10_1029_0.pdf | p.1030: orientation-double centralizer quotient, unique positive lift, and hyperelliptic lift. |
| Farb & Margalit, Primer, author version 5.0 (2011) | https://pagine.dm.unipi.it/~a019210/Farb%20Magalit_Primer%20on%20Teichmuller%20theory.pdf | Proposition 2.3 and proof; Lemma 3.17 signed multitwist uniqueness; Proposition 3.20 and its cutting-kernel proof. |
| Andrew, Hensel, Hughes, & Wade (2026), Problems on handlebody groups | https://samhughesmaths.github.io/Preprints/2025NASHSHRDW.pdf | Paragraph immediately following Problem 19 says the genus ≥3 mapping-class congruence subgroup problem remains open. Used only to document current literature status. |
| Haran (1993), J. Algebra 156, 219–236 | https://www.tau.ac.il/~haran/Papers/cohdim.pdf | Definition of real projectivity and Proposition 2.2 with proof. Open projective index-two subgroup plus self-centralizing involutions is the criterion used. |
| Jarden (1982), Arch. Math. 39, 496–500 | https://www.math.tau.ac.il/~jarden/Articles/paper36.pdf | Pages 496–498 visually read, including Theorem 1.2, Lemma 2.1 and proof of Theorem 4.1. Rank-two torsion-free index-p extension is impossible, giving actual prime-order lifts. |

## Search scope and unsuccessful approaches

Searches covered finite-order automorphisms of free and surface profinite groups, projective groups with a procyclic quotient, finitely generated normal subgroups of free pro-p groups, real mapping-class centralizers, genus-three congruence status, and the exact genus-at-most-two stabilizer comparison. Literature was used for precise primary statements, not for a claim of novelty. No source found in these searches computes the six requested congruence-kernel fixed groups or H1 sets. This search result is not itself a proof of mathematical openness.

The freely available Jarden PDF has no useful extracted text; the first three pages were rendered and visually inspected. `Jarden-1.png` through `Jarden-3.png` document that reading. The irrelevant search hit arXiv:2004.06402 and unsuccessful mirror requests are not cited or used.

## Lead 8 / LM6 A.50–A.52 audit (2026-11-16, second-hour work)

- Stix, *On cuspidal sections of algebraic fundamental groups*, primary arXiv PDF https://arxiv.org/pdf/0809.0017, opened full profinite convention (§1.2), boundary homology sequence (§3.2), Proposition11 and Corollaries12–13, essentially cyclotomic normalizer definition (§5.2), Theorem20 and proof. Tool sources turn141view1, turn143view0–2; earlier openings turn103view0, turn106view0–1, turn107view0–1, turn108view0. Corrected LM6A14's Corollary7 citation: it concerns Kummer theory, not inertia separation.
- Serre, *Abelian l-Adic Representations and Elliptic Curves*, primary scanned 1989 reprint, https://www.math.mcgill.ca/darmon/courses/18-19/gs/serre-mcgill.pdf. Read II29–30, III7, III9, III11, III32. Tool sources turn141view2 and earlier turn103view1, turn106view2–4, turn107view2–4, turn108view1–2. Local algebraicity and unit-character calculation are stated with exact hypotheses.
- Boggi, published 23 September2026, *A congruence subgroup property for symmetric mapping class groups*, volume20 article35, https://link.springer.com/article/10.1007/s40863-026-00558-y. Opened published normalizer sequence, Proposition2.1, Lemma2.2, Proposition2.4, §§3.1–3.2; compared supplied CongSym.tex lines315–479. Sources turn134view0, turn141view0. Only p-group specialization is used, where BZ TheoremA directly replaces Proposition2.4. The V4/C3 induction rechecks LM4F7.4–6 and proves full induced topology separately from density.
- Boggi–Zalesskii2025, https://arxiv.org/html/2406.08639v2, reopened exact TheoremA finite p-subgroup statement and TheoremC/CorollaryD extra normalizer hypotheses. Sources turn134view1, earlier turn115view0–1. Our A4 proof does not assume those extra hypotheses circularly.
- Exact new arithmetic model checked by standalone code/check_tetra_field.py and output. Earlier exploratory inline run's tetra_field_probe.out is retained as an intermediate; the standalone script reproduces its identities and adds exhaustive seven-subset cardinality verification.

These searches and audits precede the conditional arithmetic conclusion. The full-topology induction and cusp-free conclusion overlap earlier LM4F7–F8 and are explicitly described as independent rechecks, not novel claims. The actual abelianity question remains Open (B.34).

## Exact lift ambiguity (B.42–B.45)

- Read the complete relevant construction in supplied LM7_PUSH_checkpoint_09/sections/E_relative_cm_lift_agent.tex, especially E58.20–22, and its canonical-frame law in E_cm_character_agent.tex E65.12/14. E58 fixes relative conjugators as well as the relative automorphism; our proof therefore kills both cocycles, not just an outer action. Read all of LM7_tower/sections/D_arithmetic_replacement.tex to retain its actual N12-relative data; did not assume the level12 compact curve is CM.
- Collins2007, *On Jordan's theorem for complex linear groups*, primary publisher metadata/abstract https://www.degruyterbrill.com/document/doi/10.1515/JGT.2007.032/html (turn157view1), published article reproduced at https://www.academia.edu/83869254/On_Jordans_theorem_for_complex_linear_groups (turn158view0). Opened TheoremA, §2 and §4. The exact bound for degree97 is98!, and its classification-dependent primitive-group input is accepted explicitly as an established theorem. Publisher PDF and Oxford repository retrieval failed; the publicly reproduced published text provided the theorem and proof. No access-control bypass used.
- Osada1987, *The Galois groups of the polynomials x^n+a x^s+b, II*, primary PDF https://www.jstage.jst.go.jp/article/tmj1949/39/3/39_3_437/_pdf/-char/ja, tool turn156view0, and metadata turn170view0. Read Proposition1/local inertia, Theorem3, Corollary1 p442. DOI10.2748/tmj/1178228289. Our S10000 polynomial is a direct elementary specialization; its complete local proof is written in B44.
- Discovery searches used system2 (turn154search*) followed by system1 (turn156search*) when primary access had gaps. Search results on Osada's earlier Journal of Number Theory paper were not used as theorem authority. The small S5 quotient is proved by exact finite-field factors and a primitive transposition argument.
- code/check_lift_ambiguity.py verifies F3 irreducibility via gcd(x^9−x,f)=1, the F2 degree2+3 square-free factorization, exact integer Jordan rank bounds608 and419, 10000!/2>576^576, and the Eisenstein/Hensel coefficient conditions of the sparse degree10000 polynomial. Output saved, every check PASS. No degree10000 splitting-field computation is claimed.

## Actual-K Sylows and the real action (B.50–B.51)

- Herfort–Ribes1985, *Torsion elements and centralizers in free products of profinite groups*, published primary text reproduced at https://www.academia.edu/104225124/Torsion_elements_and_centralizers_in_free_products_of_profinite_groups, opened TheoremsA′,B′ and their proofs, pp157–160, tool turn185view0. Uses existing root/A-agent key A_HR1985. Only one finite factor C2 is used.
- The real action is calculated directly from symmetric loops about ±i: complex conjugation exchanges a free basis, and the based extension is Z*C2. Full finite-index completion gives Zhat amalg C2. No unproved real section conjecture is used.
- Additional search for a theorem forcing Galois-stable finitely generated subgroups to be open or cyclic found no applicable primary theorem (system2 turn182search*, system1 turn184search*). No such theorem is asserted. Recent unrelated section-conjecture claims were not used.
- The suggested general self-normalizing property for finitely generated nonabelian Sylows in Fhat2 is false: F_2^(p)×F_2^(q) is two-generated projective, hence a closed retract. The explicit Heisenberg quotient in code/check_normalizer_model.py checks both nonabelian Sylows, their full normalizers, cross commutation and generation; all PASS. The infinite embedding follows from the Sylow cohomological criterion already sourced in C.1, not finite-quotient evidence.

## Additional full-versus-pro-p splitting search
Queries for full virtually free profinite finite-order fixed subgroups and Galois-stable finitely generated subgroups were run (web refs turn191–192). No applicable full splitting/finite-generation theorem was found. Opened primary arXiv0712.4244 PDF, turn207view0: Herfort–Zalesskii, Theorem1.1, Lemma2.4 and Section5/Lemma5.1. The theorem is explicitly pro-p; the last section demonstrates failure of the free-product conclusion in the full category. This is a limitation check, not use of its theorem to settle C.1 or C.3.
# B.54: actual pro-seven seed, insertion, and averaging

- **Furusho (2003)**, *The Multiple Zeta Value Algebra and the Stable Derivation Algebra*, Publ. RIMS 39(4), 695–720, DOI 10.2977/prims/1145476044. Opened the author-hosted published PDF at https://www.math.nagoya-u.ac.jp/~furusho/paper/SDA=NZ.pdf, especially §5 pp.718–719 (web refs turn246view0, turn248view0–1), and publisher metadata at https://www.jstage.jst.go.jp/article/kyotoms1969/39/4/39_4_695/_article/-char/en (turn252view2). Checked the functional c_m and its image as normalized Soulé character divided by (m−1)!. The stated Lie generation conjectures are not used.
- **Nakamura, Sakugawa, and Wojtkowiak (2017)**, *Polylogarithmic analogue of the Coleman–Ihara formula, I*, Osaka J. Math. 54(1), 55–74, DOI 10.18910/61898. Read primary arXiv 1410.1045v3 formulas (1.1)–(1.2) and then opened the actual version of record https://ir.library.osaka-u.ac.jp/repo/ouka/all/61898/ojm54_01_055.pdf (turn253view1), confirming the same formulas at pp.55–56 and publication metadata (turn252view1). The exact denominator is p^(m−1)−1, and the finite Kummer product at p=7,n=1,m=3 is the seed used in B.54. The initially found OCU mirror returned HTTP429; the Osaka version of record subsequently succeeded.
- **Sharifi**, *Soulé characters in the work of Ihara*, RIMS Kôkyûroku 2120, author-hosted primary lecture/article PDF, consulted for the relationship between characters and graded Galois images. Not used as an independent proof of nonvanishing: B.54 supplies the explicit mod29 Kummer calculation.
- **Lazard (1954)**, *Sur les groupes nilpotents et les anneaux de Lie*, Ann. Sci. ENS 71(2), 101–190, DOI 10.24033/asens.1021. Primary NUMDAM metadata opened (turn253view0). The browser PDF fetch failed its size limit (10,944,604 bytes), but a subsequent local primary download succeeded. Read Chapter II §4, Theorems4.2–4.3, Corollary4.4 and Lemma4.5 with their proofs at pp.175–179 from the downloaded text. Lemma4.5 gives exactly the class-less-than-p scope used in B.54. B.54 also describes its finite class-four, exponent-seven model by the truncated tensor/BCH formulas. Local copies of this PDF, Furusho2003 and the NSW2017 version of record are saved under sources/.
- **Finite independent certificate:** code/check_pants_average.py and .out run successfully. It checks epsilon→21 and epsilon^4→7 modulo29, the Kummer line character b^(−2) and conjugation character b^3, the degree-three denominator, all three pair-insertion Lie formulas and non-innerness, the A5 action on twelve C5 cosets, six antipodal pairs each repeated ten times, and all220 tripod counts. It does not infer an infinite automorphism from the graded calculation: that existence is proved by pro-seven fixed-point lifting and R2 in B.54.

# B.57: exact common-resolvent-kernel counterexample

- **Wilson, Parker, and Bray, primary ATLAS A9 entry:** https://brauer.maths.qmul.ac.uk/Atlas/alt/A9/, opened 16 November2026 (turn263view0). The entry states order181440, Mult=2, Out=2, and specifies the double cover2.A9. This verifies the established Schur multiplier H2(A9,Z)=C2 used in B.57. The theorem about universal central covers is reduced in the proof to the free-presentation universal property, and its application to arbitrary central refinements is proved there.
- **Original Schur (1911) paper:** metadata for *Über die Darstellung der symmetrischen und der alternierenden Gruppe durch gebrochene lineare Substitutionen*, J. reine angew. Math.139,155–250, DOI10.1515/crll.1911.139.155, was found and opened via Geodesic/EUDML. The publisher PDF redirected to a robot-check page (turn263view1), so it is not represented as read. B.57 cites the opened primary ATLAS entry, not an unread original proof.
- **Independent finite certificate:** code/check_common_kernel_alt9.py exhaustively enumerated all181440 elements generated by the specified pair, checked that all are even, checked cycle types(7,1,1) for all three tripod meridians, supplied even conjugators for the outer transposition, and checked the trivial joint S9 centralizer from all14 candidates in the first centralizer. It also checked the A5 orbit of60 triples with one antipodal pair, distinct cusp-support patterns, and A4 normal closure orders4,12,12. Output is saved alongside the code.
- **Infinite steps are explicit proofs:** q(V)=M is proved by iterated commutators and normality, without commuting intersections and images. The extension of the finite outer action to the actual central refinement uses its canonical finite perfect subgroup M#, not an arbitrary convenient covering group. The full lift uses the closed-normal central criterion of A.3/A.34, whose finite count is the refereed R2 input.


B.57 lifting audit: independently read supplied LM7_PUSH_checkpoint_09/sections/D_pronilpotent_lift_agent.tex in full, especially D50.6–16, the explicit modular-source maps D50.9, and compact conjugator cylinders. For arbitrary closed normal N the actual auxiliary source q-dagger kills [N,B], so the central-refinement automorphism gives its new epimorphism and literal conjugators; the proper-fibre count then meets each finite constraint on B/N and generation. The separate D50.17 joint-generation condition [E,A]=A is not used. Clarified that the full lift retains alpha on B/N and projected conjugators, not necessarily the whole selected alpha-sharp.

Post-B57 arithmetic-normalizer search: opened primary Hoshi2014 PDF https://www.ms.u-tokyo.ac.jp/journal/pdf/jms210201.pdf (turn282view0), introduction pp153–156 and the precise elasticity hypothesis at p156. Its result is about a finitely generated subgroup normal in an open geometric subgroup, which is unavailable for a Sylow normalizer surjecting the arithmetic quotient. The source is logged as a checked non-applicable route, not cited as a proof of K triviality. Also inspected the author's primary publication list and search coverage for pro-p/pro-l arithmetic normalizers; no stronger applicable theorem was identified.

### C28 operadic pure-braid corollary
Primary Boavida de Brito–Horel–Robertson2019 publisher PDF opened at https://msp.org/gt/2019/23-1/gt-v23-n1-p07-s.pdf (web turn308view0–2). Read definitions6.10–6.12, Lemma7.1 actual arrow presentation, Prop7.3 full profinite GT identification, Prop7.7 ribbon extension, §11 strand-deletion and Lemma11.3. Bibkey CEBHR2019 shared with agent A. C28 itself does not presume a GT0 action in arity4. Own standalone C28 check:3pages, exit0, one4.22pt overflow removed by a paragraph split, then zero overfull boxes.

### C29 audit attribution and unsuccessful general recognition searches
Read original LM4D35 in supplied background paper around31893–32130, including its generation proof using D32; our independent cover proof confirms this step and generalizes it. Searches for full unit-peripheral endomorphisms found no more specific theorem used; proof is self-contained and builds on C13. Separately opened Haran1990 primary Closed Subgroups of G(Q) with Involutions (https://www.tau.ac.il/~haran/Papers/closed_subgp_invs.pdf), intro and Prop1.4 (turn323view0–2): gives real-projective embedding, not a full decomposition. Lucchini2001 primary abstract (DOI10.1006/jabr.2001.8927) states full profinite Grushko additivity fails; no rank shortcut used. These failed recognition searches are recorded without adding an unneeded theorem citation.

## 2026-11-16, post-checkpoint03: full invertibility and recognition source audit

- Lochak & Schneps, *Open problems in Grothendieck–Teichmüller theory* (2006), author PDF https://webusers.imj-prg.fr/~pierre.lochak/textes/farb.pdf, opened §0 equations (I)–(III) and §1 Question1.1 in full (web refs turn343view0, turn345view2). The latter asks arbitrary unit pairs and explicitly the constrained case. Publication list https://webusers.imj-prg.fr/~leila.schneps/articles.html confirms Proc. Sympos. Pure Math.74,165–186; an inaccurate secondary volume75 result was not used. Existing shared key A_LS2006 is cited.
- Schneps, *The Grothendieck–Teichmüller group: a survey* (1997), primary https://webusers.imj-prg.fr/~leila.schneps/SchnepsGT.pdf, opened definitions and Lemma1 at pp185–186 (turn343view1, turn345view0–1). Its B3 statement assumes the initial F2 automorphism, so it was not used circularly to obtain C.30. Instead the full hexagon was expanded directly.
- Fresse, *Little discs operads, graph complexes and Grothendieck–Teichmüller groups*, final author manuscript https://pro.univ-lille.fr/fileadmin/user_upload/pages_pros/benoit_fresse/Manuscripts/EnOperadHomotopy-II.pdf, opened pp13–14 (turn352view0, turn355view2). Publication list confirms2019, Handbook of Homotopy Theory407–444 (turn356search0). The text explicitly contrasts the known Malcev unit criterion with the profinite invertibility problem. New key CEFresse2019; citation is source context, not a proof.
- Robertson & Singh, *Grothendieck–Teichmüller symmetries of cyclic operads and tangles*, https://arxiv.org/pdf/2511.05911, version3 dated14Sep2026, opened Definition5.1 and Remark5.2 on pp40–41 (turn352view1, turn355view3). It permits odd nonunit multipliers in the monoid and separately defines its units; it reverses conventions. It is NOT evidence of an unresolved unit-lambda case and is not cited for C.30's proof.
- Wilkes, *Relative extensions and cohomology of profinite groups*, JPAA229(1)(2025)107846, DOI10.1016/j.jpaa.2024.107846. Primary author arXiv https://arxiv.org/pdf/2209.06492 opened §6.8–6.9 (turn335view0–3; publisher preview turn334search0–1, direct publisher page403). The relative free-product recognition of Proposition6.8 and Theorem6.9 is explicitly pro-p; its two surjectivity steps use H1/Frattini and do not solve full marked generation. General relative-projectivity statements supply weak lifting only.
- Haran, *Closed subgroups of G(Q) with involutions* (1990), primary https://www.tau.ac.il/~haran/Papers/closed_subgp_invs.pdf, opened introduction and Proposition1.4 (turn323view0–2). Countably generated real-projective groups embed into a fixed small real-free product; this is an embedding, not a marked isomorphism or full free-product decomposition.

## 04:12–04:19 UTC: C31 primary-source check

- BHR2019 publisher PDF https://msp.org/gt/2019/23-1/gt-v23-n1-p07-s.pdf: Definition6.4 (printed317–318), Proposition7.7 and its two-strand balancing proof (329–330), Proposition8.1 (331), and Proposition7.3 (324–325) directly reopened. References turn399view0, turn401view0–1, turn402view0. The full-twist action is an exact deduction from the cabling formula and ribbon-extension exponent, not inferred from the center.
- Horel2017 primary author PDF https://geoffroy.horel.org/Profinite%20completion%20of%20operads.pdf: Proposition5.10, Corollary5.11 (manuscript34–35) reopened, references turn399view1/turn402view3. Publisher DOI10.1016/j.aim.2017.09.030, volume321,326–390 metadata verified turn404search0 and author page turn404search2.
- Marin2012 https://www.lamfa.u-picardie.fr/marin/arts/kyoto.pdf: Section2.3 and Proposition1, manuscript9–10, read directly (turn401view2/turn402view1). Author publication list turn404search1/3 verifies ASMP63,337–357(2012). No unverified volume title retained.
- Morales2024 primary publisher HTML https://link.springer.com/article/10.1007/s00208-023-02785-6: Lemma8.4 directly reopened (turn401view3/turn402view2).
- DE independently checked full topology, goodness, all finite modules and filtered-colimit passage, and the S_n-orbit quotient. Audit saved by DE in work_DE/review_C31_braid_torsion.md; source PDFs archived there.

## 04:18–04:25 UTC: C32–C33 local parameter work

- Reopened Furusho2010 published Annals PDF, Theorem2 and Corollaries12–13, the following paragraph allowing a quadratic root and expressing possible failure of unit integrality, and Question14. URL https://annals.math.princeton.edu/wp-content/uploads/annals-v171-n1-p13-p.pdf ; references turn418view1/turn421view2. Shared bibkey Furusho2010 is used.
- Cohen2010 primary Cambridge PDF, Example1.1 and explicit Artin formulas, pp465–466, DOI10.1112/S0010437X09004424. Opened turn429view0; author/institutional/publisher metadata turn429search0–3. It supplies the trivial free-kernel abelianization action, not the new p-goodness proof.
- Enriquez–Furusho III primary author arXiv1908.00444v5, Section6.1 integral Magnus comparison and Section6.2 pro-p monoid definitions, Lemmas6.9–6.10/Cor6.11/Prop6.12–6.15 were read (turn421view0/turn422view1). The source explicitly separates monoid and units at odd p. Used for a source-context check only; no unproved proposition from it is needed in C32–C33. Publication is Selecta Math29, article27(2023), author/institutional lists turn429search6,8,10.
- Furusho2011 double-shuffle/gamma paper, Theorem0.5, was opened at turn418view0/turn421view1, and Ihara author publication list at turn425view0. Gamma factorization was investigated but not used: the required integral identity was derived directly from affine hexagons.
- Complete independently auditable algebra is in research_C33_metabelian.txt. Root and A each independently derived its affine identity and accepted the first-denominator comparison and integral Magnus construction. C32 relative topology/cohomology proof follows DE's short outline, then gives every step explicitly; it is independent of the full-goodness-to-pro-p fallacy.

## 04:27 UTC: literal prescribed-root question
Furusho2010 Question14 was directly read in the published Annals PDF, printed555 (turn421view2, lines613–617). Its specified-root wording is answered by C34's actual S4 hexagon evaluation. The example is the same pair from A39, now evaluated with m3mod12. It is not a counterexample to existence of some full root. Code/output: work_CE/code/check_prescribed_root_hexagon.py/.out. Root independently supplied and checked the same x-valued hexagon.

## 04:28–04:35 UTC: relative finite-base investigation
The exact finite S3 pentagon calculation is in code/check_relative_s3_pentagon.py/.out, using the opened primary Cohen2010 Example1.1 Artin presentation. Its1008 homomorphisms impose only k10+k01=0; no full pentagon lift is claimed. The relative pro-3 sign-character obstruction and exact scope are recorded in research_relative_base.txt.
Enriquez–Furusho2012 primary arXiv1103.1188v2 opened (turn434view0), Theorem0.2/3.1 and Theorem0.3/3.4 distinguished: the group-like theorem requires special action. Publisher metadata verified turn433search0, DOI10.1016/j.jpaa.2011.10.009, JPAA216(4)982–995. No unverified use of the abstract as a group theorem.

### 2026-11-16: Morales2024, nilpotent image topology re-read

Reopened publisher primary https://link.springer.com/article/10.1007/s00208-023-02785-6 (web turn459view0/1/2). Section3 opening explicitly gives full induced profinite topology on all subgroups of polycyclic groups; Theorem3.2 gives full induced pro-p topology for every subgroup of a finitely generated nilpotent group. Used only for the independent review of DE's exact class3 obstruction, recorded in review_B59_class3.txt. Existing CEMorales2024 bibliography entry retained; no new citation metadata needed.

### C.37/C.38 source and independent verification, 16 November 2026

The full finite-coefficient restriction theorem used is Kochloukova and Zalesskii(2007), Theorem2, already archived and cited in C.7/C.8/C.28. DE independently reopened the primary author manuscript at https://mat.unb.br/~pz/arquivos/Claus3.pdf, pp3–4, and verified that Theorem2 is explicitly full profinite despite the paper's title. Root independently reopened the same theorem and section1.1. C.37 uses its direct high-degree restriction map with one-dimensional source; no localization or pro-p substitution is needed. The complete reviews are work_DE/review_all_A5_generation.md and the root review record. Matrix enumeration: work_CE/code/check_a5_duality_orbits.py/.out. Independent permutation enumeration: work_DE/check_review_A5_generation.py/.out. C.38 is a formal consequence of the same full one-section statement and needs no additional literature claim. No priority claim is made.

### C.39 and auxiliary representation audit, 16 November 2026

C.39 uses the existing full R1/C28/A44 proofs plus an elementary finite Frattini argument. Its finite classification is independently generated in work_CE/code/check_C39_S4.py/.out. No external finite-group classification theorem is needed beyond the explicitly proved S4/S3 module facts.

For DE's genus-five mod3 homology route, opened primary GAP Character Table Library A5 page https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/ctbltoc/data/A5.html and its decomposition matrix https://www.math.rwth-aachen.de/~MOC/decomposition/tex/A5/A5mod3.pdf (one page, Block1). The degree5 character reduces to the sum of degrees1 and4. Also opened primary ATLAS A5 representation list https://brauer.maths.qmul.ac.uk/Atlas/alt/A5/ (characteristic3 list has degrees3 overF9,4 overF3,6 overF3, and no simple degree5). This verifies the caution that the characteristic-zero degree5 multiplicity-space picture cannot be transferred semisimply to characteristic3. Exact integral lattices and the computed Lie bracket must decide the reduction; no assertion about DE's actual lattice is made.

### C.40 exact finite verification and independent reviews

The proof uses previously verified full R1/A44/A45 and C35/C36/C39 identities; it invokes no external finite realization theorem. The self-contained check_S4_third_cusp.py enumerates GL2(F3), asserts the printed nine matrix representatives, transports full commutator-word values through central input changes, and checks all six common S3 head cases. Exact output is check_S4_third_cusp.out. Root independently reran it to records/root_C40_rerun.out and reviewed the complete proof; A separately read and reran the proof/certificate and saved its review under work_A. Both passed before formal integration. This is an exhaustive necessary-condition proof, not an assertion that all enumerated tables are full words.


### Reconstructed source record after replacement-environment recovery

Before the loss, C42 independently reopened KZ2007's primary author manuscript https://mat.unb.br/~pz/arquivos/Claus3.pdf, Theorem2 and Section1.1, manuscriptpp3–4. It also reopened Pál–Quick2025, Real projective groups are formal, Math.Ann.392,1833–1876, DOI10.1007/s00208-025-03145-2, Theorem2.11 and Remark2.12, where degree-one separation is attributed to Scheiderer Remark12.20.2,p158. These readings and the accepted proof are retained in conversation; the replacement file is a reconstructed log, not a claim that a lost retrieval artifact was restored. Existing keys CEKochloukovaZalesskii2007 and A_PalQuickFormal2025 suffice. C43 uses the already audited Wilkes finite-coefficient surface-pair duality from C6 with its explicitly proved peripheral-orbit augmentation module. No new bibliography entry is required.

### Eighth-hour integral and inverse-limit audits

The integral coefficient proof uses the actual Q6 monomial matrices and exact Galois-ring arithmetic, not a new literature claim. Fresh post-recovery certificates are check_Q6_integral_cusp.py, prepare_Q6_integral_affine.py, prepare_Q6_integral_rframe.py and their executed outputs. The affine data include literal cochain corrections and preserve the stored old frame reductions before the separate central-half adjustment. Independent direct original-law checks of A59's columns and A61's final witness are saved as verify_A59_columns_direct.py/.out and verify_A61_witness_readonly.py/.out; imported output destinations were redirected into work_CE.

A62's all-exponent extension was independently read in full. The review checks the actual nested source kernels, the no-opposite-pair s orientation, the complete integral invariant argument, and the compact maximum-level finite-intersection construction without asserting surjective frame transitions. It also proves that the descending intersection of these relative-perfect source kernels is itself relative-perfect by stabilization in every finite quotient. Detailed reviews are review_A60_integral_frames.txt, review_A59_existential_frame_repair.txt and review_A62_integral_tower.txt. No full negative involution or cofinality is inferred.

## Targeted Coxeter-plane lead after checkpoint08

Heng, E., & Paris, L. (2026). Representations of Coxeter groups over fusion rings and hyperplane complements (arXiv:2511.04836v2, revised21 October2026; to appear in Journal of the London Mathematical Society). Primary abstract and full HTML opened16 November2026: https://arxiv.org/abs/2511.04836 and https://arxiv.org/html/2511.04836v2 . Figure1 explicitly treats I2(5) inside A4; Theorems4.17 and4.20 concern the induced hyperplane-complement embedding, while Section5 connects it with strong admissible/LCM morphisms. This is a possible geometric identification for DE's five-point Coxeter-plane family, not an established full-profiniteness theorem or an already checked based monodromy identification. Sent to DE/root; no formal statement uses it.

Paris, L. (2002). Artin monoids inject in their groups. Commentarii Mathematici Helvetici,77,609–637. Publisher primaryPDF opened: https://ems.press/content/serial-article-files/42946?nt=1 . Section5 records the bipartite type-A formula for the products of odd and even standard generators and invokes Crisp's LCM injectivity theorem. In typeA4 this suggests the discrete I2(5) generators sigma1sigma3 and sigma2sigma4. The full induced profinite topology of that subgroup is still a separate unproved gate in the current application.

## 2026-11-16, noncentral reflection-lifting obstruction

Opened the published primary article Leemans, D., & Schulte, E. (2009),
*Polytopes with groups of type PGL2(q)*, *Ars Mathematica Contemporanea*,
2, 163–171, especially p.170. It identifies the diagonal-field extension
of PSL2(9) with M10 and states that it cannot be generated by involutions.
URL: https://www.dlib.si/stream/URN%3ANBN%3ASI%3ADOC-EP8LP7LI/69b91562-2970-4f96-8be9-6ecf1365b284/PDF .
Also opened the primary ATLAS representation page
https://brauer.maths.qmul.ac.uk/Atlas/v3/group/L29/ and the GAP Character
Table Library entry
https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/ctbltoc/data/A6.2_3.html .
The actual no-involution proof is elementary via determinants over F9;
independent complete matrices/permutations are in
`research_equivariant_R2/check_M10_reflection_obstruction.py`.
The stronger tempting pants-source example is rejected by an explicit
SL2(F9) spin calculation, not promoted to a full action.

## 2026-11-16, classical trace-triple rigidity

Opened McCullough, D., & Wanderley, M. (2013), *Nielsen equivalence of
generating pairs of SL(2,q)*, *Glasgow Mathematical Journal*,55,481–509,
DOI10.1017/S0017089512000675, primary publisher PDF:
https://www.cambridge.org/core/services/aop-cambridge-core/content/view/12B5FCFADCAFE740B31DEE5BB112DB85/S0017089512000675a.pdf/nielsen-equivalence-of-generating-pairs-of-sl2q.pdf .
Theorem8.2, pp490–491, attributes the nonsingular trace-triple conjugacy
result to Macbeath's Theorem3. The exact GL2(k)-conjugacy needed here
is independently proved by the four-dimensional matrix-algebra basis;
no odd-characteristic SL2-conjugacy uniqueness is assumed.
Also opened Goldman's author manuscript, *An exposition of results of
Fricke and Vogt*, arXiv:math/0402103v2, especially the opening theorem
and Section3. It states the characteristic-zero classical version.
The original Macbeath chapter was located as DOI10.1090/pspum/012/0262379,
pp14–32 in *Number Theory*, Proc.Sympos.PureMath.12 (1969), but the AMS
chapter/volume fetch returned access errors; its contents were NOT
represented as independently read. No novelty claim is made for the
trace-rigidity input.


### 16 November2026: binary-icosahedral frame gate

- Primary ATLAS A5 entry opened directly: https://brauer.maths.qmul.ac.uk/Atlas/v3/group/A5/ . It records Mult=2 and 2.A5=SL2(5). This identifies the universal double cover after perfectness, which is proved independently and exhaustively checked in the certificate. Web reference turn661view1.
- Robert Steinberg, Lectures on Chevalley Groups (Yale1967, notes Faulkner/Wilson), Section7(v), (vii), (viii), consulted through Arun Ram's explicitly labelled typed transcription at https://math.soimeme.org/~arunram/Resources/LOCGS7CentralExtensions.html . Its end note identifies the source; updated4July2013. The original1967 scan was not opened. References turn661view0, turn662view0. The needed universal-cover splitting argument is reproduced in A.74, including the profinite-kernel passage.
- A search-returned RiuNet paper mentioning the Schur multiplier of SL2(5) redirected to sign-in and was not used. No secondary search snippet is treated as proof.


### B.83: actual w-pencil controlled filling kernel, 2026-11-16

No new external source is used. The actual common-marking data are work_DE/next_marginal_source/w_pencil_words.json and w_source_adapted_basis.json. Independent producers work_CE/code/verify_w_pencil_independent.py and check_w_normalizer_limitations.py retain genuine stdout and JSON certificates. The exact proof was read completely and accepted by root and independently by DE (review_B83.md). All compact kernels mean actual closed images of completed free-factor source fillings.


### B.86: coupled diagonal and retained product kernels, 2026-11-16

No new external input is used. The actual source entries17,19,21,23, local triple and filled-node peripherals come from work_DE/next_marginal_source/w_source_adapted_basis.json, w_local_markings.json and w_positive_negative_transport.json. Independent producers work_CE/code/check_w_retained_product_nodes.py and check_w_coupled_diagonal_products.py reconstruct the displayed words, both action directions and all three node identities; their genuine stdout and JSON certificates are preserved. Root's research/proof review is records/B86_coupled_block_root_review_16h.md; root and DE subsequently read the complete formal proposal and accepted it. The single zero-source 169-word subgroup test is preserved separately and has no theorem status.


### B.88: exact paired geometric detector,2026-11-16

No external input is needed. The actual common-marked words a,b,z and Z'=a^-1 b^-1 z b a are those of B.86 and the source-adapted w data. The rational maps are defined on the actual Y_b and agree literally on its source. work_CE/code/check_zero_source_equalizer.py verifies all primitive local orders and all32 central-coordinate assignments in the actual UT3(F2) x UT3(F2) quotient. Genuine stdout/stderr and zero_source_equalizer_certificate.json are preserved. Root and DE independently read the complete proof and checker. The earlier169-word membership failure is neither evidence for this theorem nor its proof.
