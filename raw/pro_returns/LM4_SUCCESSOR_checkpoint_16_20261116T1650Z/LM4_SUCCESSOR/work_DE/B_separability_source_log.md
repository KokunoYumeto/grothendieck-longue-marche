# Part B.4(c): refined product and source audit

## Outcome

The main icosahedral intersection remains undecided, but the actual unrefined product is now proved closed. B.46 states the exact paired Minasyan criterion. B.47 independently reconstructs a fully explicit counterexample to the implication from one closed product to equality of profinite intersections, with an exact PSL2(F8) finite witness. B.48 checks newer individual separability and product theorems with their actual hypotheses. B.49 reduces every actual refined product to simultaneous A5-homomorphism conjugacy under each finite-index subgroup L of the pure mapping class group. B.52 proves the actual unrefined product is a finite word-equation locus, using the four pure conjugacy classes of labelled A5 embeddings and a braid rotation residue to select the unique required class. Equations B.52.7–B.52.8 then isolate the remaining finite-index obstruction exactly. This does not confuse one torsion conjugacy class, a finite subgroup conjugacy class, and a marked homomorphism.

## Primary sources opened and used

1. Ashot Minasyan (2023), *On double coset separability and the Wilson–Zalesskii property*, Bulletin LMS55(2),1033–1040, DOI10.1112/blms.12775. Publisher full text https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/blms.12775 and complete author PDF https://www.personal.soton.ac.uk/am4x07/rs/wz-property.pdf opened. Read Theorem1.1, Proposition2.4, Proposition3.1, Corollary3.2, Example4.1 and their full proofs. Source theory uses arbitrary formations, but our statements use the full profinite topology. B.46 gives its own short proof for the actual trivial-intersection specialization. B.47 reconstructs the example without requiring any global LERF or goodness assertion about its ambient group.
2. Francesco Fournier-Facio (2025), *A note on separability in outer automorphism groups*, Proceedings Edinburgh MS68,705–711, DOI10.1017/S0013091525000045. Publisher full7-page PDF and HTML opened. The author is Fournier-Facio, not Minasyan. Read full proof: TheoremC and CorollaryD, Proposition2.1, Corollary2.2, Lemmas2.3–2.4. The general theorem removes geometric hypotheses on H, but preserves conjugacy separability of its full preimage in Aut(G). The finite quotient construction comes from Hagen–Sisto Proposition2.5.
3. Mark Hagen and Alessandro Sisto (2023), *Some examples of separable convex-cocompact subgroups*, Bulletin LMS55(5),2242–2257, DOI10.1112/blms.12848. Publisher PDF opened via institutional repository https://pure.hw.ac.uk/ws/portalfiles/portal/94298401/Bulletin_of_London_Math_Soc_2023_Hagen_Some_examples_of_separable_convex_cocompact_subgroups_1_.pdf . A direct urllib retrieval returned403, so arXiv2206.11084 was retrieved and saved. Read Theorem1.1, Section2.1 (all finite-type surface curve-graph characterization), Proposition2.5 with full characteristic-quotient proof, and the proof of Theorem1.1. The actual groups have multitwists and fail convex cocompactness; passing to finite index does not remove those powers.
4. Ashot Minasyan and Lawk Mineh (2025), *Quasiconvexity of virtual joins and separability of products in relatively hyperbolic groups*, Algebraic & Geometric Topology25(1),399–488, DOI10.2140/agt.2025.25.399. Complete author PDF https://www.personal.soton.ac.uk/am4x07/rs/sep_qc_products_in_rh.pdf retrieved. Publication metadata checked on author's publications page and Southampton record. Read Theorem1.2 and Corollary1.4 with its proof in Section15. Proof separates unwanted elements from finitely many translates of a relatively quasiconvex virtual join; QCERF and double-coset-separable peripheral groups are indispensable stated hypotheses. No appropriate ambient relative-hyperbolic structure or faithful profinite embedding for the generated subgroup of the actual two factors is proved.
5. Lawk Mineh (2026), *Product separability in central extensions*, Groups, Geometry, and Dynamics, online17September2026, DOI10.4171/GGD/998; preprint arXiv2504.15762. Official publisher https://ems.press/journals/ggd/articles/14300050 and author PDF https://lawk-mineh.github.io/files/Product_separability_and_extensions.pdf opened; completePDF retrieved. Read Theorems1.1,1.3, the proof of1.3 in Section3, and centrality discussion. The author publications list still labels2025; publisher publicationdate2026 is used. Theorem1.3 requires an actual central extension, finitely generated central kernel, double-coset-separable quotient, and LERF total group. These are not established for a useful common ambient group for H_T,H_5.
6. Juan González-Meneses (2011), *Basic results on braid groups*, Annales Mathématiques Blaise Pascal18(1),15–59, DOI10.5802/ambp.293. Complete publisher PDF https://ambp.centre-mersenne.org/item/10.5802/ambp.293.pdf opened and downloaded. Read Section2.2 pp.28–31, especially the exact capping identification on p.29 and the torsion-freeness proof; also Section4.3 on the center. In B.52 torsion-freeness ensures that the fifth-power exponent of a lift of nonidentity order-five torsion is nonzero modulo five. No profinite braid torsion claim is used.
7. Michał Stukow (2004), *Conjugacy classes of finite subgroups of certain mapping class groups*, Turkish Journal of Mathematics28(2),101–110. Primary arXiv:math/0510214 text reopened for Theorem4, with Section2's Nielsen-realization and regular-action argument. Theorem4 says the A5 subgroup has one conjugacy class; the possible two-class exceptions are cyclic order two and certain dihedral groups. For twelve marks the geometric proof reduces to the unique twelve-point icosahedral orbit. Bibliography entry DE_Stukow2004 is in references_DE.bib.
8. Steven Kerckhoff (1983), *The Nielsen realization problem*, Annals of Mathematics117(2),235–265. Previously checked primary source, SectionIV/Theorem5 for punctured surfaces, as recorded in source_log_DE.md and references_DE.bib. Used only for discrete realization, never for a claimed profinite fixed point.

## Exact computation

`check_separability_example.py` uses standard Python and field arithmetic over F2[u]/(u3+u+1). It enumerates all504 determinant-one matrices, checks generator orders2,3 and product order7, enumerates9conjugacy classes, and verifies each nontrivial normal closure is the full group. Thus simplicity and the finite quotient are checked without a library identification. `check_separability_example.out` is actual stdout; `.json` records every class representative, size, element order, and normal-closure size. The proof, not the code alone, excludes a congruence quotient via the composition factors of SL2(Z/m). A short independently proved corollary restricts to Gamma(3), of free rank three: the ambient group becomes torsion-free, both factors become free, the product remains congruence-closed, and the same congruence kernel survives. This removes torsion in the factors as a possible explanation for the failure; no goodness assertion is made.

`check_marked_a5.py` uses standard Python and exact permutations. It constructs the twelve-point action A5/D, verifies the group and centralizer orders, enumerates all240 compatible (automorphism, puncture permutation) descriptions, and verifies the four free A5 orbits of size60. After fixing the named puncture, each orbit has five descriptions and one rotation multiplier r=1,2,3,4. It also constructs all60 canonical words and180 Cayley-table relators for the explicit presentation used in B.52. `check_marked_a5.out` is actual stdout; `marked_a5_certificate.json` records every word, relator and representative; `marked_a5_relators.txt` is the plain list. All checks pass. The script makes no topological assertion; the exact braid invariant and the labelled-conjugacy implication have independent proofs in B_product.tex.

## Main route attempts and exact limits

- Individual centralizer separability follows already by detecting a nontrivial commutator in a finite quotient; the full topologies from B.28 extend it to all finite-index factor subgroups. It is therefore not the missing step.
- The product of the two embedded free subgroups cannot be treated as a product in an abstract free group unless a common ambient free group and the correct induced topology are proved. No such common ambient embedding was established.
- A profinite product factorization for g in the discrete pure group does force the generated subgroup T and gDg^-1 to be a finite A5: conjugate by the profinite first factor and use residual finiteness. B.49 proves this useful strengthening and keeps the pure-conjugator restriction. B.52 now proves pure conjugacy for L=P, in fact identifies the actual product as a finite word-equation locus independently of completed centralizer comparisons. The remaining assertion is marked homomorphism conjugacy under every finite-index L. The four P-orbits split further under L; their classification alone does not settle the new condition.
- No action of the full profinite mapping class group on a profinite tree or complex with a unique A5 fixed point and controlled stabilizer was constructed. A discrete Teichmuller fixed point alone does not give one.
- Search strings included Hagen Sisto2025/2026 subgroup separability mapping class groups; Minasyan outer automorphism separability; mapping class group double coset separability; symmetric mapping class subgroup separability; profinite A5 fixed complex; centralizers double coset conjugacy separability; product separability central extensions. Strong primary-source search was used for the recent results. The search itself is not evidence of a universal literature nonexistence result.

## Local primary files
- Minasyan2023.pdf: 324518 bytes; SHA256 `6e42ff65073152788424ca4f0ac867ddb55f43f85f988ebd03b63b9b12a79db8`.
- FournierFacio2025.pdf: 471390 bytes; SHA256 `faf4cf70902eca697854f3c583ffd4080afbd72448f164df0988267900c4eb4e`.
- HagenSisto2023.pdf: 609449 bytes; SHA256 `71d0b77be8bedc6b026d66820b90e7597bc810c203a0e6d6c27d0bd883e05094`.
- MinasyanMineh2025.pdf: 1119420 bytes; SHA256 `a82cabb6bae3be1867c893e6b8d30156803bc0749afca9c509376300757eb58b`.
- Mineh2026.pdf: 302052 bytes; SHA256 `8359194a1a11b4510092c34c742bfc798b140f778c24b28365109799f3e82ee8`.
- GonzalezMeneses2011.pdf: 1029537 bytes; SHA256 `a4c396b2ad06040efc55a82ccdaec4dc579d7b4dcb464a855178a6b9dc8d30ea`.


## B.52 scope clarification and geometric complement (02:40 UTC)

The source and register now explicitly extend pure-product closure to the full centralizer product by finite coset unions. The named rank-two cyclic factor is F_5^v, the vertex-fixing complement in the subgroup fixing the two poles and preserving the two free five-orbits. The cyclic-cover peripheral monodromy is (d,d^-1,1,1), so all pure four-puncture base classes lift commuting with d. Unique deck normalization at v splits this subgroup as C5 times F_5^v and identifies F_5^v with F2. Its pure kernel is H_5, of index five. A loop of lambda around zero in the family {0,infinity} union mu5 union {z:z^5=lambda} verifies the five quotient permutations. Thus the exact chosen F_T F_5^v product is closed; arbitrary complements and finite-index refinements remain separate.


## Component QA at checkpoint 02 (02:49 UTC)

Both latest component PDFs were rebuilt twice with the private LuaLaTeX format and contain no unresolved citation/reference warnings. B_separability_review.pdf has nine pages (109691 bytes), zero overfull boxes; the initial draft had five overfull boxes above 2pt, maximum 24.483pt. DE_review.pdf has nineteen pages (160027 bytes), exactly three overfull boxes, respectively 1.13306pt, 0.58992pt and 1.06087pt, all below the requested 2pt threshold. The earlier D.17 29.651pt overflow has been removed. The changed full-centralizer/geometric-complement page and D.17 boundary proof page were freshly rasterized and visually reviewed; equations, margins and text are legible. Latest logs are B_separability_review_build_latest_0.out / _1.out and DE_review_build_latest_0.out / _1.out. Image checks are qa_B_scope-8.png and qa_D_boundary-10.png, supplemented by earlier reviewed spreads. All finite certificate scripts had passed before this purely textual scope clarification.


## Main-route attempts after checkpoint02 (02:50–03:10 UTC)

1. **Framing refinements.** A fifth-power exponent beta^5=Z^m defines only m modulo5 independently of the lift. Changing the lift changes m by a multiple of5. Pure conjugation preserves the same residue, so refining the braid framing does not distinguish the many smaller-subgroup conjugacy orbits. Even total exponent cannot detect a nontrivial commutator in H_T; some finite quotient detects such a commutator by residual finiteness. This blocks that proposed elementary extension of B.52, not the desired continuity itself.
2. **Wilton–Sisto2024, arXiv2410.00556v2.** Primary abstract and full HTML opened at https://arxiv.org/html/2410.00556v2. TheoremA assumes every hyperbolic group residually finite and proves mapping-class CSP. The introduction explicitly records genus0 CSP already established. Their omnipotence argument does not furnish the simultaneous finite-subgroup conjugacy/refined-product statement required here. No conditional result is promoted to an unconditional proof.
3. **Kalka–Teicher–Tsaban, arXiv1402.5541v5 (27October2026).** Primary abstract opened at https://arxiv.org/abs/1402.5541. The current version solves the discrete double-coset problem for arbitrary parabolic braid subgroups by simultaneous conjugacy in B_(n+1). The actual finite-group centralizers here are not identified with those parabolics, and a decision procedure is not finite-quotient separation. No theorem from this source is used as an input.
4. **Aougab–Bray–Dowdall–Hoganson–Maloni–Whitfield2025.** Author PDF https://math.vanderbilt.edu/dowdalsd/papers/GF-RAAGs.pdf opened, TheoremsB/C and Section8 inspected. Their separated reducible-subgroup combinations do not apply to these two irreducible symmetry centralizers without a new comparison. The Section8 word separability concerns curve-graph distance, not profinite subgroup separability.
5. **Margalit–Winarski2021.** Primary publisher article https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/blms.12456 opened, Theorems2.1–2.3 and discussion of partial markings inspected. The regular/full-ramification Birman–Hilden theorem does not directly survive forgetting five unramified preimages of the moving puncture.
6. **Koch–Pilgrim–Selinger2014.** Primary author PDF https://public.websites.umich.edu/~kochsc/KPS.pdf (9May2014), and earlier author PDF https://people.math.harvard.edu/~kochs/KPS.pdf, opened. Proposition6.2(2) assumes the full marked preimage A=f^-1(B); its proof uses an isometric Teichmüller pullback. Our seven-point subset is not that preimage. Their Theorem6.3 concerns equal marking counts and does not itself decide our4-to7 marking case.

### B.56 discovery and exact certification

The promising route was to ask whether retaining a rigid seven-point subset yields an injection of H_T. Every one of the fourteen parameter punctures remains a collision in that family, so the simple removable-peripheral argument for four-point maps does not settle it. Numerical braid discovery and a Birman point-pushing/Stallings probe then found a relation: the image of the +1 meridian is conjugate to the image of the -1 meridian by the alpha meridian. This relation was subsequently certified independently of numerical extraction. The final standalone rational program specifies all path coordinates exactly; for each of18segments and15pairs it isolates all real crossing roots, checks signs and order, and records the data in rigid7_exact_certificate.json. Exact Artin action verifies the58/36/14-letter braid relation. The final proof uses only this certificate, nonzero source homology and the exact tetrahedral permutation action.

González-Meneses2011 Sections1.6–1.6.1, pp22–24, were reread at the faithful Artin-action and word-problem statements. This is the already archived primary PDF and bibliography entry DE_GonzalezMeneses2011. The formal source is B_rigid7.tex; the result register is B_separability_results.csv, now six rows. No priority is claimed.


## B.56 final component QA (03:20 UTC)

The ordered parameter was renamed S_T to match B.18; the coarse curve C_T retains its earlier meaning. The B component rebuilt successfully to twelve pages, 126814 bytes, with zero overfull boxes and no LaTeX citation/reference warnings. All three pages containing B.56 (qa_B56-09.png, -10.png, -11.png) were independently opened and visually checked after that change; formulas, the braid arrays, margins and the final common-kernel proof are legible. The final log is B56_review_final.out. The initial new-section overflows of6.06491pt and17.66316pt have both been eliminated.


## Complete scope of the B.4(a) test obstruction (B.56)

The intrinsic P3 tripod tests are identically trivial on every pure geometric mapping class and hence on the completed pure group: forgetting to three punctures gives the trivial pure mapping class group. The three P4 recipes for the named tetrahedral T also vanish identically on H_T and its completion. B.30 supplies tetrahedral descent to the pure four-special-point quotient; filling any of its three cone points yields a pure mapping class of a three-special-point sphere, whose geometric outer action is trivial. The third target remains C3 amalgam C3. These intrinsic maps agree with B.53 on the common A5-centralizing domain, but do not assume a general H_T element extends to an automorphism of B. Consequently h lies in the intersection of every test family named in B.4(a), and k additionally lies in all495 four-point kernels. This proves that the combined test route is not faithful; a full description of that common kernel is still not supplied, and K itself remains undecided.

Independent peer review of B.57's finite and topological support is recorded in review_B57_finite_topology.md, with check_B57_cusp_topology.py/.out/.json. All five original cusp colorings, sixty distinct tripod supports, and exact C3*C3 peripheral normal forms pass. The central-extension lifting and multiplier input are explicitly outside that peer review.

Expanded B.56 QA (03:28 UTC): after adding the correctly typed P3/P4 scope, B_separability_review.pdf has13 pages and130067 bytes; two passes yield zero overfull boxes and zero LaTeX warnings. The newly added proof on pages11–12 was rasterized and visually reviewed as qa_B56_alltests-11.png and -12.png. Build logs are B56_alltests_build_0.out and _1.out.


## Discrete common-kernel rank in B.56

All twelve rigid seven-point kernels are equal by T equivariance. Since each smaller rigid subset is contained in a seven-point subset and the P3/P4 recipes are zero, the discrete intersection in B.4(a) is exactly ker(f_S0). It is nontrivial by h. The certified beta_+ is b sigma_3^2 b^-1 for b=[-2,-1,-4,-2,-1,4], so its seven-point mapping class is an essential Dehn twist of infinite order. The kernel consequently has infinite index in F13; the standard covering-core argument proves it is free of countably infinite rank. The intersection with all495 four-point kernels contains k and is also a nontrivial normal subgroup of infinite index, so has the same abstract rank. The completed test intersection is exactly ker(hat f_S0), but its identification with the closure or the full completion of the discrete kernel is explicitly not claimed. The image's induced profinite topology would need a separate proof.


## Shusterman primary-source check and exact application (03:36 UTC)

Mark Shusterman (2016), *Free subgroups of finitely generated free profinite groups*, Journal of the London Mathematical Society93(2),361–378, DOI10.1112/jlms/jdw001. Publisher metadata was opened; first publication18February2016. The complete primary preprint arXiv1501.01227v1 (6January2015) was opened and downloaded from https://arxiv.org/pdf/1501.01227. Read Theorem1.2 (PDFp3), Section2 definition of a convergent profinite basis (pp5–6), Proposition3.2 and its proof, Lemma3.3 and proof, and Corollaries3.4–3.7 (pp8–11). Corollary3.7 is the exact finite-word theorem: a closed infinite-index subgroup of a finite-rank free profinite group is free of rank aleph0 if it contains a closed normal subgroup meeting the abstract free subgroup on a basis nontrivially. Both test kernels in B.56 satisfy this with the normal subgroup equal to the kernel itself and with words h and k. Normality alone would not suffice. The source's proof passes through actual finite embedding problems and Iwasawa's criterion, not a closed-subgroup Nielsen–Schreier assertion.

Local file Shusterman2015.pdf: 239331 bytes; SHA256 `0acca4ccc9018d0afd9e2cf040f4c31485f0b6d6a2855efec314a36a3e6a36ce`. Bibliography entry DE_Shusterman2016. The formal citation explicitly indicates that theorem numbering was checked in the preprint.


## Profinite common-kernel type determined (B.56, 03:36 UTC)

Shusterman's finite-word theorem applies to both completed test kernels. They are closed normal subgroups of the finitely generated free profinite group hat(H_T), have infinite index because the essential twist beta_+ has infinite image, and contain the nontrivial discrete words h and k. A basis of the discrete free group H_T is a profinite basis of its completion. Thus the theorem's extra finite-word hypothesis is met, and both completed intersections are free profinite of countably infinite rank. This determines their abstract topological group types; it does not identify either embedded kernel with the closure or full completion of the corresponding discrete kernel. The convergent-basis convention is explicit. No general claim that every closed normal subgroup of a free profinite group is free is used.

The final B.56 prose also separates the two infinite-rank completion conventions explicitly. Each discrete kernel is an abstract free group on countably infinitely many generators, so its full profinite completion has uncountably many index-two open subgroups and is not metrizable. Each completed test kernel is closed in the metrizable finite-rank free profinite group hat(F13), so is metrizable. They therefore cannot be the full profinite completions of the discrete kernels. Equality with the embedded closures remains a different, unproved induced-topology question.


## Component source freeze for checkpoint03 (03:38 UTC)

B_rigid7.tex, B_separability_results.csv and B_separability_references.bib now include the full discrete and profinite countable-rank conclusions with Shusterman's exact finite-word hypothesis. The final B component has13 pages,135665 bytes, zero overfull boxes and zero LaTeX warnings. Newly changed pages12–13 were rasterized and visually reviewed as qa_B56_profinite-12.png and -13.png; the theorem application, topology distinction and new bibliography entry are legible. Logs: B56_final_freeze_build_0.out and _1.out. The final D/E component has19 pages,160014 bytes, no warnings and only the same three overfull boxes below2pt. All mathematical source changes for this checkpoint are complete. A possible subsequent all13-meridian monodromy computation will be developed separately before any new formal claim.


## Explicit embedded kernel and incomparability (B.56, after checkpoint03)

The all13-meridian extension is now integrated into B_rigid7.tex and the result register. A rational fan of thirteen disjoint square petals supplies an actual geometric free basis; exact segment–rectangle tests and rational sqrt(3) brackets certify this basis, including the cyclic order and the infinity meridian. The standalone exact Sturm program covers78 path segments and records all680 reduced braid letters. Its output is ALL EXACT CHECKS PASS (80.69seconds). The three earlier words are literally unchanged.

The rigid kernel is exactly ker(theta:F13→PB6), with theta specified on this basis. Capping first gives preimage of the central full twist; the pair-linking map on the two normalized constant strands 4,6 then proves that the image meets that cyclic subgroup trivially. The same map to Zhat removes the central closure in the completed formula, so the completed test kernel is exactly ker(theta-hat). The supplied finite-word membership utility uses Artin's faithful action, with an exponent shortcut. It does not claim computable membership for arbitrary profinite elements or equality with the closure of the discrete kernel.

The rigid and all495 four-point kernels are now proved incomparable. The degree4 covering cross-ratio for {1,2,3,5} detects h after filling the eight order3 parameter punctures. Conversely, the384-letter B.19 balanced commutator w has a noncentral Burau image over F101 under the rigid monodromy. The actual6×6 matrix and all representation checks are supplied. The common word k=[h,w] has776letters. Neither these words nor the nonfaithfulness of their test families gives an element of K.

The new files, actual stdout and SHA256 hashes are documented in next_B56/README.md. They were developed separately during the checkpoint03 source freeze and integrated only after root confirmed ZIP creation. The primary Artin/capping input remains González-Meneses2011, Sections1.6,2.2,4.3, already opened and archived; no new literature claim is needed for the elementary pair-linking or checked matrix arguments.


## All13 extension QA (03:57 UTC)

The integrated B component rebuilt twice to16pages and150311bytes, with zero overfull boxes and zero LaTeX warnings. The initial draft had one33.86365pt overflow in the isolated review and one15.11322pt overflow after integration; both were fixed by shortening paragraph leads. The final three extension pages13–15 were rasterized at100dpi and opened for visual inspection: all formulas, the13-column word table, the6×6 matrix, margins and text are legible. The final logs are B56_all13_final_build_0.out and _1.out; image checks are qa_B56_all13-13.png through -15.png. The pair-linking and Burau auxiliary checks and finite-word selftest were rerun after their final edits and passed.


## B.58: exact abelian refinements (04:27 UTC)

The completed B.56 source prompted a full orbit-pair valuation computation. check_full_pair_linking.py normalizes labels2,4,6 to infinity,0,1 and computes orders of all55 rational differences at the13 algebraic exceptional points, using Q(i,sqrt3) exactly. The15-row rigid restriction equals the independent braid-linking certificate. Both matrices have rank6; full_pair_linking_certificate.json includes all rational functions, valuations and an explicit integral reconstruction of6 times the full matrix. Actual output check_full_pair_linking.out reports ALL EXACT CHECKS PASS,45.082seconds.

Root suggested the stronger ambient computation. check_ambient_rigid7_abelian.py forms each of168 covectors e_ca-e_cb+e_ba+e_ij-e_ia-e_ja in66 formal pair variables, checks the vertex relations and exact coordinate equation M A=R, and obtains a168-by54 matrix for the actual pure mapping-class homology. Rank54, Smith factors all1, transpose Hermite form identity, and a determinant-minus1 minor are all checked. Its integer inverse is stored in ambient_rigid7_abelian_certificate.json and independently verified by ordinary integer arithmetic. Root's separate code/verify_B58_certificate.py additionally reconstructs all twelve subsets directly from the six order-five subgroups, and verifies both inverse products. The proof uses the elementary configuration-space normalization and forgetful fibrations, with no new external theorem required.

The result proves the actual centralizer has trivial image in every finite abelian quotient of P. Combined with B.52's unique discrete factorization and B.28's actual profinite intersection, it proves closure of every two-factor refinement whose two finite-index subgroups contain [P,P]. No step assumes all495 four-point maps vanish on K; only the established rigid-seven vanishings are used.

## Additional main-route literature checks, without application

The full author PDF of Merladet Uriguen and Minasyan, Virtual retractions in free constructions (Trans.AMS379(2026),7209-7250, DOI10.1090/tran/9667), was opened at https://www.personal.soton.ac.uk/am4x07/rs/VR_and_free_constr.pdf. Read the introduction's Corollaries1.1,1.3 and Theorems1.5,1.6. The distinction between cyclic virtual retractions (VRC) and retractions for every finitely generated subgroup (LR) is explicit. The graph-of-groups hypotheses are not proved for the ambient mapping class group, and a cyclic retraction does not produce the desired free-factor product separability. No theorem from this source is applied.

Udall, Combinations of parabolically geometrically finite groups and their geometry (Groups Geom.Dyn.20(2026),905-969, DOI10.4171/GGD/850), official65-page PDF https://ems.press/content/serial-article-files/53275, was opened at its introduction and main combination theorem. It proves geometric combination and undistortion under a large-projection hypothesis, rather than product separability in an arbitrary ambient mapping class group. No matching verified hypothesis or profinite conclusion was obtained for the actual tetrahedral/cyclic factors. The recent Veech-extension literature likewise supplies geometric/hierarchical structure, not a verified finite-quotient separation step here.

Encoding a finite-level conjugator label simply by adjoining the corresponding finite quotient to Gamma does not remove the residual q_U(K) ambiguity. A finite-cover argument would need a new comparison between geometric and profinite marked conjugators at that level; the existence of the unique discrete marked icosahedral point alone does not provide that comparison. No new formal equivalence is promoted as a solution.

## B.59 integral degree-two computation and primary source (04:36 UTC)

Opened and read Kaabi--Vershinin, *On Vassiliev invariants of braid groups of the sphere*, primary IHES PDF https://preprints.ihes.fr/storage/vas_in_c.pdf, especially Theorem2.2(ii), pp4--5 (PB_n=PM_{n+1}×Z), integral infinitesimal braid presentation(3.1)--(3.2), and Theorem3.1(ii), pp5--6. This distinguishes pure sphere mapping classes from sphere braids and their central2-torsion. ArXiv metadata https://arxiv.org/abs/1202.3557 dates preprint16Feb2012. The author's own2012/2014 conference abstract reports a2011 journal version58:213--232, but the citation deliberately uses the directly verified2012preprint. Primary archived as KaabiVershinin_vassiliev_primary.pdf; SHA-2563122f2ed3a1f48c769755c4c940a9df4014b477594f33a778dadb10c6a20db7a,214953bytes.

All B59 matrix arithmetic uses exact integers/rationals in SymPy. Ambient C240×165 rank159, Smith159ones; N165×6 primitive integer kernel, six-row unit minor plus inverse. Geometric generators explicitly generate Torder12 and A5order60. Three induced six-dimensional kernel action matrices satisfy orders2,3,5 and preserve N exactly. Their stacked fixed equations have rank5/Smith(1,1,1,1,1,0); primitive fixed vector v=(1,1,2,1,-1,1), ambient Nv has45 nonzero entries and a unit coordinate. Data: ambient_rigid7_class2_certificate.json and rigid7_class2_invariants_certificate.json; executable code and actualstdout retained. Formal theorem does not claim ambient degree-two injectivity, nor K=0, nor K⊂closure(gamma3), nor realization of the remaining possible central direction.

B59 rank/Smith witness strengthened: selected159×159 minor determinant−1 with its complete integer inverse checked in both multiplication orders, archived in ambient_rigid7_class2_certificate.json. Actual rerun15.834s, allchecksPASS.

Parent independent formal review passed at04:38UTC. Root code/verify_B59_certificate.py/.out independently verifies CN=0, primitive kernel minor, rank159mod101, fixedrank5mod101, primitive w and consistent60-element action. Full class-two topology and refinement proof reviewed.

## B.60 actual geometric class-two lifts and review

No additional literature theorem is used. The cyclic family is explicit: poles0,infinity; fixed orbit zeta^i; moving orbit u zeta^i. Quotient isotopy extension gives actual pure mapping classes commuting with D. Positive meridian pair-linkings are exact rational divisor orders; normalization uses B58's matrix. The two165-coordinate commutator identities were independently recomputed by root from the original H1 columns, not from the stored bracket matrices. Full profinite topology follows from B59's central coordinate lattice, with a primitive coefficient of w. The supplied a is proved outside the rigid kernel using an actual finite Burau quotient, not a failed Artin computation. Source/register reflect quotient-only scope.

## B.61 degree-three construction and topology audit

Primary Kaabi--Vershinin integral infinitesimal braid presentation is used for the free-group forgetting filtration. All required low-degree injectivity is additionally checked through full graded Artin-derivation reconstruction, with the rank990 free-Lie tower basis. Exact Magnus expansions, logarithms and BCH operations use integers/rationals; formal identities are independently tested on braid relations, inverses, products and a weight-three group commutator. The final displayed integer words are separately evaluated, so the conclusion does not infer integral subgroup membership from rational or mod101 ranks.

Torus-real independently audited the abstract obstruction and nilpotent topology. Root agent was notified of the actual19-generator common-marking certificates, then the complete integer lift certificate. Morales2024, *On the profinite rigidity of free and surface groups*, DOI10.1007/s00208-023-02785-6, publisher full text https://link.springer.com/article/10.1007/s00208-023-02785-6 was independently opened here; Section3 opening and Theorem3.2 with proof confirm full induced profinite topology for polycyclic subgroups and the stronger pro-p nilpotent statement. This supports the obstruction analysis, but the final positive B61 procyclic claim needs only the explicit words and B59's central coordinate lattice, avoiding a hidden completion/intersection assumption.

Root accepted the scoped theorem after independently rerunning all728 tetrahedral and39 cyclic triple powers, complete990-coordinate reconstruction, class3 equality and rigid cancellation (25.47s). The review is `records/root_review_B61.md`. The strengthened common-base certificate was rerun successfully in25.92s, including degree-eight field verification, root separations and the exact minimum squared segment distance1/10000. No claim about an actual K element or a compatible all-degree tower is made.


## B.62: primary geometry and exact nonnilpotent certificate (06:03 UTC)

1. Jean-Marc Gambaudo and Étienne Ghys (2005), Braids and signatures, Bulletin de la Société Mathématique de France133(4),541–579, DOI10.24033/bsmf.2496. Primary PDF https://www.numdam.org/article/BSMF_2005__133_4_541_0.pdf opened and Sections2.2–2.3 read, including Proposition2.1 and its integral chain calculation on pp550–553. The proposition is phrased over real relative cohomology; the proof computes the free integral branched-cover chain module before specialization. We use the integral identification together with an explicit unimodular matrix check, not a real-conjugacy-only assertion.
2. TaraE.Brendle, DanMargalit and AndrewPutman (2015), Generators for the hyperelliptic Torelli group and the kernel of the Burau representation at t=-1, Inventiones Mathematicae200,263–310, DOI10.1007/s00222-014-0537-9. Full publisher primary https://link.springer.com/article/10.1007/s00222-014-0537-9 opened. The introduction subsection Hyperelliptic Torelli vs Burau explicitly identifies the odd-strand branched disk cover, splits unreduced Burau into its trivial line and the homology representation, and states the full twist acts as-I.
3. CharalamposStylianakis (2018), Congruence subgroups of braid groups, International Journal of Algebra and Computation28(2),345–364, DOI10.1142/S0218196718500169. Primary institutional accepted manuscript https://eprints.gla.ac.uk/159155/1/159155.pdf opened, Theorem5.1 and its proof on manuscriptpp11–12 read. For odd primep≥3 it gives the pure braid image Sp(2g,Fp). We apply onlyg5,p3. The broad introductory sentence about prime surjectivity is not used without this explicit hypothesis. Publication metadata checked at https://eprints.gla.ac.uk/159155/.

The geometric full-sphere extension is established directly by preservation of the double-cover character; deck ambiguity is killed projectively. The actual subgroup words and relative marking are the already accepted B.61 certificates. The original exact finite calculation is next_finite_symplectic/prepare.py, enumerate.cpp, analyse.py; all standard output and complete matrix/kernel certificates are retained. Root code/verify_B62_symplectic.py independently repeats the calculation on the invariant hyperplane and verifies its integral change of basis to the discovery quotient model. Both source matrices include the zero fixed-pair(4,6) linking row, essential to pass from P_ab to full55-pair zero. The topology argument uses only finite-free abelian exactness and the continuous map from the source completion onto its closure.


B.62 component QA complete:27pages218251bytes, zero overfull boxes or unresolved citation/reference warnings. Pages23–25 rasterized and visually reviewed; qa_B62.md records the checks. The explicit fixed-pair assertion was included in the last successful finite-certificate rerun.


## B.63: first3-adic lift, actual words and topology (06:17 UTC)

No new literature theorem is required: the integral branched-cover representation is B.62's primary-verified model; the geometric19 words and common marking are B.61's exact certificate. Full mod-nine identity-fibre images are computed from all Schreier generators over the actual mod-three finite groups, so they are exhaustive upper bounds. The six displayed T words belong literally to normal<h>; the nine displayed C5 words are commutators. Their independent vectors attain both full image upper bounds. This supplies actual integral-source-zero witnesses without relying on reduction of an unsaturated integral kernel. The initial HNF calculation (source indices6 and3) is retained as an independent cross-check only.

The smaller subgroup M9 is defined using the actual projective image Q9=q9(P), not by an unproved surjectivity assertion for the full symplectic group overZ/9. B.62 gives q3(K)=1, so finite-image continuity places q9(K) in the exact common identity fibre. The inverse image M9 is open, generally finite-index refinements need not be normal, and the B52 ambiguity proof applies directly. Here nonnormality is explicitly certified by conjugating X0 with the actual tetrahedral generator e1. No passage to a normal quotient with trivial K image is made.

Original programs and outputs: next_3adic_symplectic/first_lift.py/.out, rigid_lift.py/.out, short_cyclic_witnesses.py/.out. The standalone verify_short_words.py/.out imports no discovery code and uses the invariant-covector hyperplane integral model. Root code/verify_B63_first_lift.py/.out independently reconstructs both finite transversals and all Lie vectors, checks the actual short words and literal rigid relation, and verifies the solvable derived plane. Exact JSON certificates retain all source words, matrices, transversals, ranks and nonnormality witness.


## B.64 primary logarithm source and exact lattice (06:30 UTC)

Dixon, J.D., duSautoy, M.P.F., Mann, A., and Segal, D. (1999), Analytic Pro-p Groups, second edition, Cambridge Studies in Advanced Mathematics61, Cambridge University Press, DOI10.1017/CBO9780511470882. Publisher chapter metadata was opened. The complete primary text from the institutional copy https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/ddsms.pdf was read at Proposition6.22 (pp111–112), Theorem9.8 and its full proof (pp222–224), and Theorem9.10 (pp226–227). These check the strict p-adic convergence radius, powerful Lie-lattice construction and exact Frattini generation statement. The proof retains its own matrix-lattice and successive-cube argument. Read-copy SHA256: 0687140b1c8c529c32320765c77dcf432d70e7178ba7a23aa71b26565d56187e. The full book and extracted text are not redistributed.

The exact integral A5 lattice is computed from root’s already certified12-strand beta2/beta3, through ker(epsilon)/Z·1. The commuting and symplectic Lie equations are solved overQ and saturated at3, with primitive mod3 bases independently checked. Explicit order multiplication identifies the level3 Eichler order and its actual ambient3O filtration. The rational centralizer decompositions give derived dimensions6/9; the actual squared B63 commutator words give all corresponding lattice directions. No inference of modular semisimplicity, no arbitrary closed-subgroup logarithm assumption and no full-source torus upper bound is needed. Root and CE reviewed the complete proof, including the ramified-block determinant argument.


## B65--B66 reconstructed after execution-environment replacement

The original seventh-hour versions were not included in checkpoint06 and are not represented as byte-preserved. Complete mathematical proofs have been reconstructed from retained conversation. B65's finite data were freshly evaluated against the verified checkpoint06 original common-base braid words by next_joint_rigid_symplectic/check_B65_reconstructed.py; its actual .out and complete JSON are retained. The Q/Birman action was likewise freshly evaluated by reconstruct_Q_birman.py, including its antihomomorphism correction.

For B66, the following primary sources were reopened on 16 November 2026 after recovery. Hain--Matsumoto, https://arxiv.org/pdf/math/0006158, Appendix A: TheoremA.6 (PDF p35), LemmaA.7 and proof (p36), CorollaryA.11 (p37). These give the canonical discrete/pro-ell/full-unipotent comparison and rational-point based Galois action. Web refs turn552view0, turn553view1/2/3. Publisher https://www.cambridge.org/core/journals/compositio-mathematica/article/weighted-completion-of-galois-groups-and-galois-actions-on-the-fundamental-group-of-p1-01/94239BA21D3B20D154B3D024CB3C8996 independently confirms 139(2),119--167, November2003 and DOI10.1023/B:COMP.0000005077.42732.93; the online2007 date is distinct (turn554search0/6). The DOI resolver itself was inaccessible in this retry, so no success is claimed for that URL.

Stacks https://stacks.math.columbia.edu/tag/0BQ8, Theorem58.6.2(3), explicitly makes the pointed functor diagram strictly commutative; https://stacks.math.columbia.edu/tag/0BTX, Lemma58.14.3, gives the geometric--arithmetic exact sequence. Both primary pages reopened completely (turn552view1/2). The remaining B66 eigenprojection argument is supplied in full in the reconstructed proof; it is not attributed as a published theorem about this configuration.


## B67 exact internal certificate

This is a new explicit counterexample derived from the actual certified B61 monodromy and the exact Birman action. Complete files are next_joint_rigid_symplectic/refute_Q_injection.py/.out and Q_noninjection_certificate.json. The program checks action composition, the antihomomorphic push convention, actual PB5 identity, actual PB6 nonidentity, the free-product syllables and the finite S3 witness. Root independently reran and accepted the complete proof and code. It is a refutation of the proposed intermediate Q injection only; no inference to failure or success of full theta5 injectivity is made.


# B68 primary-source and finite-certificate log

Accepted after root full proof review, independent certificate rerun, and primary-source check. Verification date: 2026-11-16.

## Heusener and Weidmann (2019)

Published primary full text:
https://www.degruyterbrill.com/document/doi/10.1515/jgth-2018-0118/html

Author preprint:
https://www.math.uni-kiel.de/algebra/de/weidmann/research/material-research/whiteheadfoldings-pdf

The publisher confirms Journal of Group Theory 22(1), 15–21, DOI
10.1515/jgth-2018-0118, print year 2019 (online 2018).
Section 1 defines a separable set by conjugacy into factors of a nontrivial
free product. Published Corollary 3.5 states that such a set has disconnected
Whitehead graph or a cut vertex. This is exactly the required proper-free-factor
criterion, stronger than Corollary 3.4 for primitive elements. The preprint
uses different numbering (Corollary 3.3).

Fresh primary retrievals: turn571view0; turn573view2; turn573view4. The
source graph uses the pairs (x,-y) for cyclic adjacent x,y; our (-x,y)
graph is obtained by reversing every vertex sign.

## Kra (1981)

Original primary article scan:
https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6295-11511_2006_Article_BF02392465.pdf

DOI: https://doi.org/10.1007/BF02392465

The first-page footer and article pagination confirm Acta Mathematica 146
(1981), 231–270. Theorem 2′ (pp. 231–232) identifies irreducible point pushes
with essential loops; the next paragraph identifies irreducible maps with
pseudo-Anosov maps. Section 9 (p. 252) explicitly identifies essential loops
with filling loops. Theorem 2(b), pp. 252–253, is the detailed statement.
The underlying six-punctured sphere is nonexceptional for this application.

Fresh primary retrievals: turn571view1; turn573view1; turn573view3.

## Exact computation

`next_joint_rigid_symplectic/verify_full_Q_word_filling.py` reads the restored
common-base eleven-strand source words, performs its own strand deletion and
Artin/free-word operations, and recomputes the 144-letter fiber word.
It separately verifies both compositions with the inverse for each of six
Whitehead automorphisms. It verifies the final 15-edge graph is connected and
stays connected after any vertex deletion, saving all eleven spanning trees.
The genuine run output is `verify_full_Q_word_filling.out`; exact words and
witnesses are in `full_Q_word_filling_verification.json`.

The earlier exhaustive Whitehead minimization was discovery only. The proof
uses the six explicit verified automorphisms and does not require that the
final word be minimal. The extraction convention is an antihomomorphism;
inverting it gives the actual free-fiber homomorphism. Inversion preserves
the free-factor and filling conclusions used here.

No full theta5 injection, completed-kernel identification, or profinite
pseudo-Anosov centralizer conclusion is asserted.


## B69–B70: actual full cyclic kernel (checkpoint09 work)

The complete new finite certificate reads original B61 eleven-strand words and independently implements strand deletion and faithful Artin action; it does not import the discovery action engine. refute_full_theta5.py/.out and full_theta5_noninjection_certificate.json prove the actual PB6 identity, source nonidentity in S3, exact full Birman conjugator equality, and the infinite spherical-image linking witness. Root independently reread and reran the full certificate; CE independently inspected it.

For B70, root reopened the primary Shusterman arXiv:1501.01227 Theorem1.2/Corollary3.7 and its proof. The closed infinite-index completed kernel contains the closed normal closure of a nontrivial finite basis word, so the exact finite-word hypothesis holds. No general closed-normal-subgroup freeness assertion is substituted. The original primary source and verified bibliography entry are already recorded with B56. The discrete infinite-rank proof is supplied directly. The completed-kernel closure equality and actual ambient centralizer K remain unresolved.


## B71: simultaneous full rigid and full3-adic comparison

No new external theorem is needed. B64 already supplies the saturated rank-nine cyclic derived Lie lattice, exact logarithm comparison in the natural integral filtration, and a complete successive-cube generation proof. The new original-word verifier actual_cyclic_rigid_kernel.py recomputes the matrices of nine actual conjugates of B69's word to the twentieth power, using the B62 integral branched-cover model and checking its braid relations/inverses. All source words lie literally in normal<w0>, hence in the actual full rigid kernel, and have exactly zero integral source H1. Their nine principal residues have an explicit integer9-by9 minor of determinant−52.

Root independently reread the full formal proof, checked the B64 lattice/cube hypotheses and compact-surjectivity passage, and reran the original-word certificate successfully. Closures are inside the already embedded finite-rank source completions, not the full completion of the abstract infinite-rank kernel. The resulting equality is in the product of all full rigid target groups and the entire3-adic matrix target. It gives no equality of source lifts in the ambient completion.


## B72: full discrete conjugate disjointness

McCarthy, J.D. (1994), Normalizers and centralizers of pseudo-Anosov mapping classes, author manuscript revised8 June1994, originally5 March1982. The full primary four-page author PDF https://users.math.msu.edu/users/mccarthy/publications/normcent.pdf was reopened and read at Theorem1 and Lemmas1–4. The proof uses the dilation homomorphism with finite symmetry kernel, not only the weaker phrase virtually cyclic. Its introduction says compact negative-Euler surface. The new proof therefore spells out the marked-puncture extension: include one-prong marked separatrices, measure-preserving symmetry fixing a separatrix fixes its dense leaf, and a periodic sphere representative of the identity relative to twelve marks is identity. The bibliography identifies the manuscript status and exact scope as Verified.

The cyclic source comparison is the actual unramified degree5 map of punctured surfaces z↦z^5 and parameter cover u↦u^5 from B28. No ramification point is filled when lifting a pseudo-Anosov foliation. The seven parameter cusps have explicit1-curve or5-curve multitwists. An A4 action on either reduction-system size has a fixed curve; its two sides cannot be swapped because A4 has no C2 quotient, contradicting transitivity on twelve marks. In the pseudo-Anosov case both A4 and the conjugate C5 lie in the common finite symmetry kernel, forcing an actual rigid A5 by the finite sphere-group classification and B52's realization. The conclusion concerns all discrete conjugators only.


## B73–B74: exact common-involution covers and full dihedral centralizer

These proofs need no new external theorem or bibliography entry. B28/B30 already establish the valid prime5/prime2 completed centralizer comparisons and full induced topology. The new eight- and seven-point subgroups are specified by explicit sheet-parity homomorphisms, with indices32/16 and lift sections fixing original labels1/2. The pure cyclic pole-forgetting comparison is proved from identical quotient orbifolds and distinguished local residues; no inference of full topology from discrete injection is made.

For the full D5 centralizer, the exact four-point action shows that the cyclic centralizer commutator with r lies in its central C5. The half-commutator retraction is checked algebraically; the q-orbifold cover has degrees and ramification5+5+8=18. Completion follows from the actual discrete direct product and the valid C5 comparison. The colored eight-point group for the full D5 centralizer is Q8-tilde, not Q8: its five ordinary marks may be permuted, while its pure intersection is exactly H5. Root and CE independently reviewed the underlying notes; root read both complete formal sources and accepted their stated scope.

Primary literature searches for profinite comparison of the Coxeter-plane/folding inclusion were negative in scope, not evidence of a general impossibility. Heng–Paris arXiv:2511.04836v2 Theorem4.20, Proposition5.4 and Corollary5.6 give the homomorphism, spherical discrete injection and geometric realization, respectively; they do not give the required induced profinite topology or finite-index product closure. The exact search log is next_common_involution/source_scope_audit.md.


## Explicit comparison with the supplied LM4 Part F (checkpoint10 audit)

The recovered attached source /workspace/scratch/a50d05093ca1/recovered_background/LM4_return/LM4_FINITE_GROUP_ACTIONS_paper.tex was reread at F11 (from line48647), F12 (from49099), F14 (from49645), and F15 (from50014). F11 already proves the pure C5/D5 centralizer equality, the2+10 rigid-kernel decomposition, and a nontrivial common kernel word. B65 and B69 independently recertify and reformulate those assertions in the successor's exact different common marking and explicit braid words; they are not first noninjectivity results. B70 adds the exact abstract kernel types under the checked finite-word theorem while retaining the closure gap.

The branch-ordered faithful eight-point and seven-point comparisons in B73 rederive attached F12/F14. The current added specifications are the full colored rank-six formulation, sheet indices32/16, chosen lift sections, and transferred all-conjugate/refined-product gate. Root added that attribution explicitly at the start of B73's proof. The full nonpure C5 direct-product and D5=C2*Z splitting in B74 extends the prior pure-family calculation.

The subsequent research cocycle uses the four-moving-point Birman kernel and the nonpure C2*F3 source. It is complementary to attached F14/F15, which already solve all full cocycles in the specified two-point interaction kernel and identify the remaining original-source membership condition. The present reformulation does not bypass that condition or the later F18--F29 drilling analysis. Full comparison is retained in next_common_involution/attached_F_comparison.md; no new formal statement is promoted from it before checkpoint10.


## B75: based four-moving-point cocycle and exact full kernel topology

No new external theorem is needed. The actual Birman fibration gives B4(S0,4); the section is explicit in the source orbifold C2*F3 by filling its two additional cusps. Its full induced topology is proved directly using characteristic finite-index subgroups of the finitely generated kernel and the finite action on each quotient. The original marked permutation certificate verifies the second involution, actual A5 generation, orders3/5 excluding the finite deck discrepancy, and the full permutation centralizer with its pole swap. Exact rational identities verify the based orbifold model and common w=4/5,q=-121. Root read the complete formal proof and accepted both completed zero-set directions.

The source begins by attributing the prior attached F14/F15 two-point correction analysis. The current four-moving-point formulation and nonpure source comparison are complementary; the same unresolved uniform/source-membership gate is retained. The exact finite-cover criterion is an equivalence, not a completed solution.

## 11:38 UTC: reconstructed marginal and ratio-pencil scope

The attached-source tail audit now includes F30--F33, not only F29. Exact locations and scope are recorded in next_common_involution/attached_F_comparison.md. Fresh marginal code was reconstructed from printed geometry because original F23/F24 programs were absent, and all retained stdout comes from actual reruns.

New research files in next_marginal_source/ contain the full 19-lasso/11-action extraction, explicit source words for four killed generators of a Nielsen basis, and a proved coordinate transformation to a 20-puncture ratio pencil. The 29 finite exceptional values are checked over Q(zeta). The full based monodromy words and uniform source-kernel normality remain unresolved. The degree4 finite-cover scan has no witness and is retained only as bounded negative evidence. No new formal claim is promoted from these experiments.

Primary source checked: Shimada (2010), International Journal of Mathematics21(5),591--637, DOI10.1142/S0129167X10006252, Corollary1.1/Theorem3.20 in the author-hosted full text, https://home.hiroshima-u.ac.jp/ichiro-shimada/preprints/newZvK/pioneU.pdf (turn682view0); publication metadata verified on the author publication list (turn683view0). This supports the generic-fiber van Kampen program under checked submersion, irreducibility and pi2(base)=0 hypotheses. It does not imply the special-fiber source-image equality.

## B76 component review and integration

The root-authored B76_proposed.tex was independently reviewed and renamed B_relative_special_fiber.tex. The based chart sends the common basepoint to(2,2); f(z)=z/(z-1) fixes it and is involutory. The filled three-line group is Z^3 by the stated node calculation. The first-factor commutator is excluded from the graph and its full closure by the explicit S3 times S3 quotient. The proof does not assume full topology of an infinite-rank kernel. No new literature entry is required. This is a refutation of a proposed general shortcut only.
# B.78 primary and computational source audit (16 November2026)

Shimada, I. (2010), Generalized Zariski-van Kampen theorem and its application
to Grassmannian dual varieties, International Journal of Mathematics21(5),
591-637, DOI10.1142/S0129167X10006252. The author-hosted full primary text
https://home.hiroshima-u.ac.jp/ichiro-shimada/preprints/newZvK/pioneU.pdf
was reopened (web turn704view0); Corollary1.1, Remark1.2 and the stated
monodromy-relations scope were checked. Author publication list item36,
https://home.hiroshima-u.ac.jp/ichiro-shimada/publications.html
(turn704view1), confirms journal metadata and DOI. Only the generic-fiber
comparison is used. The paper does not supply the unresolved special-source
kernel normality.

The original source marking is the actual positive marginal family in the
attached LM4 F15 and later source-image reductions through F33. The new
polynomial coordinates, finite-cover squares and all31 based lassos are
reconstructed and rerun here; no inaccessible original F23/F24 program or
stdout is asserted to have been recovered. Exact producers and actual
outputs are next_marginal_source/quadratic_pencil_braid.py/.out,
all_filled_pencil_braids.py/.out, audit_pencil_geometry.py/.out and
audit_complete_pencil.py/.out. The combined JSON records input hashes.
The earlier principal-square-root-cut failure is retained separately.
Root reviewed the complete proof, coefficient/marking audit and exact
crossing method; the final B.78 display and swept-square convention
corrections were made before integration. CE independently analyzes the
literal transported relations, with B.77 owned in work_CE.



## B79: complete sum-pencil source and computation audit

The ordered surface, original source path and both actual finite-cover
kernel squares are exactly those of B78; no new literature theorem is
invoked. The generic-fiber van Kampen input is the already verified
Shimada2010 scope. The source remains special, and no relative
special-fiber surjectivity is inferred. The26-value cyclotomic audit,
130-segment crossing certificate, source-disk/Nielsen check and all82
local variation relations were produced by actual reruns, with genuine
stdout retained. Their paths are audit_sum_pencil.py, sum_pencil_braid.py,
check_sum_source_cluster.py and extract_sum_presentation.py in
next_marginal_source. The initial strict-engine multiple-projection
failure is preserved; the final height-cluster resolution supplies a
proved homotopy relative endpoints. Root and CE independently reviewed
the complete proof and exact source marking before integration.

An independent component review of the root's product-one filling
reduction in records/product_one_filling_reduction_13h.md passes: removing
only vw=1 leaves the source unchanged and makes it a generic ratio
fiber, proving I+=R+. The resulting localization R=I(R intersect Pker)
and compact coset comparison are correctly typed. This does not prove
the unresolved original interaction/source-membership condition.


## B81: actual tangent bundle and independent strip audit

No new external theorem is used. The original source and finite-cover
comparison are the same actual objects as B78 and attached LM4 F15--F33.
The unordered quotient (q,T)=(vw,(v+w)/2), all seven-point actions and
four source crossings were reconstructed and genuinely rerun. Producers
and geometry audit are in next_marginal_source, with actual stdout and
JSON hashes. CE independently checked84 Artin action identities in
work_CE/code/verify_tangent_bundle_all_actions.py and580 source words plus
all strip inputs in work_CE/code/verify_tangent_strips.py. Root reviewed
the full proof, index-two lemma, actual compact comparison and source
labeling. The infinity correction is retained explicitly rather than
replaced by its filled retained quotient. B81 establishes the four
specified free-factor intersections only; the entire source-normality
condition is still unresolved.


## B82: actual ordered partial-source comparison

No external source is added. The based family labels and exact source
operators come from the same actual B81 bundle and its ordered cover.
Independent checks in work_CE establish the family marking, all displayed
Nielsen substitutions, the complete partial D-block proof and the exact
rank-six overlap. In particular the h1/h4 formulas were separately
recomputed, and actual source witnesses for U2/U6 were retained. The
restricted D8 certificate and its failure under the missing alpha1-squared
operator are preserved as research, without promoting it to a separator
of the full source image. Root and CE accepted B82 with the explicit
D-squared whole-normalizer limitation.


## B84: all-positive controlled actual kernels

No external theorem is added. The five positive source lifts, their
corrections and both-family source filling are checked in the actual
common w marking. The fourth correction was obtained from one prescribed
169-word membership calculation; its16 factors are substituted exactly
and its F19 source witness is retained. CE independently reconstructed
this word, the third correction, the action restrictions and all relevant
Nielsen inverses. The compact proof uses an abstract free group on the
selected source words and actual quotient detectors, without an unstated
induced-topology assertion. Root and CE independently read and accepted
the full proof. The old zero direction and arbitrary retained-source
operators remain explicitly outside its scope.

## Sixteenth-hour symmetric research and cross-agent primary audit

The exact actual64-node geometry was reconstructed over Q(zeta5), with
a complete involution permutation and genuine executed output. Root's
coordinate simplifications are attributed in the growing note. The
provided LM4 F21/F22 source and B78 cover comparison were independently
reread before using the inherited discrete normal-generation theorem.

Brown--Loday1987 Lemma4.1 and its proof were independently opened in the
primary author PDF at https://groupoids.org.uk/pdffiles/RB-Loday1.pdf.
Its weaker homotopy-fiber hypothesis is exactly the one used in A's B89;
no asphericity of Z or profinite homotopy-excision theorem is assumed.
The finite-extension/full-topology proof is elementary and was audited
independently. No duplicate bibliography entry is added by DE.

Oka--Sakamoto1978 was read in full at the primary J-STAGE PDF
https://www.jstage.jst.go.jp/article/jmath1948/30/4/30_4_599/_pdf.
Its deformation proof applies to the absolute affine-plane complement.
The retained-divisor-relative inference is not used and is separately
refuted by an exact auxiliary countermodel. This source remains a
research-audit entry, not an asserted main-route theorem.
