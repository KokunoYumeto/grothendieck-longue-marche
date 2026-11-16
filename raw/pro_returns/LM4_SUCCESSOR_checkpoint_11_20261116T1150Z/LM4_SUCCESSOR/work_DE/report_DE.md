# Parts D and E.2 outcome report

| Task | Outcome | Exact place |
|---|---|---|
|LM4 C.88|Proved with independent compact-core collapse argument and exact map/inverse isometry.|D.1–D.2|
|LM4 C.92|Proved, with the based Epstein theorem and all orientation exceptions checked.|D.3, D.6|
|LM4 C.90 and C.91|Proved for compact quotient, including nonorientable quotients.|D.4–D.5|
|Every compact family for arbitrary noncompact quotient contracts with a uniform tail|Unresolved. No false transfer from compact-open topology is made.|D.9|
|Remaining arbitrary-frontier and infinite-component comparisons|Unresolved, each comparison stated precisely.|D.10–D.12|
|Controlled metric reduction|Filled hulls preserve invariant diameter; an inner-diameter metric has controlled disk neighborhoods and preserves positive based homotopy groups.|D.13–D.14|
|Arbitrary simply connected frontier, trivial operators|Known contractibility without local connectedness, by Fabel1998 with exact original topology.|D.15|
|Global equivariant compression over a compact quotient core|Impossible for infinitely generated Q; this blocks the direct Fabel compression method, not the contraction statement.|D.16|
|Joint parameter-relative controlled map filling|Proved for compact connected locally path-connected based parameter spaces, with one uniform C0 tail; injectivity remains unproved.|D.17|
|Five-point holomorphic classification|Verified; explicit β parameter and enhancement values supplied.|E.30–E.31|
|Every finite antiholomorphic automorphism has order2|False in original scan35. Exact orders6 and10 occur; possible orders are2,6,10.|E.32|
|Real-involution types1,3,5 and dimensions2|Verified, with complete counts and generic real parameter ranges.|E.33–E.34|
|Reflection sections and finite subgroup census|Five-point reflection sections verified;20 finite subgroup classes independently reconstructed.|E.35–E.36|
|542 objects in9 orbits|Verified for the nine decorated S5-sets.|E.37|
|1620 arrows in14 orbits|1620 arrows and14 named families are consistent; actual orbit count16. Original word“orbites” after14 is crossed out, so R9 overstates the manuscript's clean assertion.|E.38|
|Square pyramid not real|False for undecorated configuration; oriented decoration may explain scan31. Scan36 explicitly gives a real structure.|E.39|
|Stable-tree counts1,10,15 and subsidiary counts|Verified.|E.40|

## Main proofs and corrections

The exact group for the noncompact quotient is a subgroup B_p of the pointed compact-open identity component, endowed with the stronger metric given by uniform distances of the actual point-fixed lifts and their inverses. We independently prove the image characterization and its compact-parameter uniform-tail criterion. A new proof organization supplies a global evaluation section for every quotient using compactly supported vector fields along prescribed paths upstairs. Consequently C is homeomorphic to O×F in the original boundary topology. Compact quotient contractibility follows from the verified pointed compact-surface theorem. Compact quotient support and the trivial operator are also settled subcases. These arguments do not settle the general noncompact tail.

The countersequence in LM4 C.92 remains a counterexample only to a topology shortcut. Every map in that sequence is individually connected to the identity by the displayed allowed isotopy; it is not a nontrivial loop. We did not assert otherwise.

In the census, the holomorphic full groups are1,C2,C4,D3,D5, while the finite subgroup census has20 classes. These must be distinguished. The involution parameter β=t²+t⁻² has enhancement values−2,−10/3,18. The square-plus-edge case queried on scan35 hasβ34 and remainsC2; the tetrahedron-plus-axis case hasβ−14 and remainsC2. Six exact algebraic examples were checked by enumerating every Möbius and anti-Möbius candidate.

For K={0,∞,μ3}, σ(z)=ω/conjugate(z) has order6 and no fixed point. For K=μ5, τ(z)=ζ5/conjugate(z) has order10 and no fixed point. These refute the original finite-antiautomorphism inference, while preserving the correct real-*involution* classification. The symmetric-square shorthand also needs qualification: a real point of Sym² includes a nonreal conjugate pair, so the full real locus is not the all-five-real stratum.

Direct visual audit of the original PDF matters for the orbit count. Scan33 has a visible cancellation of the word“orbites” after14. The diagram has14 named families. The360-arrow family has a free120-object source and therefore decomposes into three120-orbits. The other13 families are transitive, so there are16 orbits, with5×60+11×120=1620 arrows. The corrected paper attributes the overstatement to R9's summary, not to a clean uncancelled manuscript assertion.

## Open work and attempted approaches

D.9 remains the exact universal noncompact deformation problem. The required estimate is sup over both parameter and homotopy time of lift displacement outside a common compact quotient core, tending to zero. We inspected the2014 compact-base uniform deformation theorem and the2018 isolated-product-end theorem. Their extra hypotheses are not automatic here. A quotient contraction in the compact-open topology need not satisfy this estimate. A null lifted triangulation contracts the pointwise skeleton stabilizer, but a controlled deformation of the actual embedding family into it has not been supplied. Geodesic interpolation does not preserve arbitrary homeomorphisms or arbitrary operator equivariance. A possible counterexample based on distant paired annular twists was considered; the basic radial models admit scalar shear isotopies and do not yield an obstruction. An exotic compactification would need an explicit continuity proof and a nonzero loop invariant; neither has been found.

D.10 needs extension across arbitrary original frontiers. A continuous single-valued prime-end boundary quotient need not exist for a non-locally-connected frontier, so the general question cannot be encoded solely by a boundary equivalence relation. Original approach limits and inverse continuity must be retained. D.11 needs mutually compatible nonfixed boundary values, extension over all incident open orbits, and uniform inverse control across infinitely many inequivalent accumulating components. D.12 is the remaining general admissible level-zero comparison. These are not presented as proved or refuted.

## Files and verification

Formal assembly sources: section_D.tex, section_E2.tex. Register: results_DE.csv (28 rows). Bibliography: references_DE.bib. Primary-source provenance: source_log_DE.md. Exact programs and stdout are attached in work_DE; root may relocate them under code/ while preserving names and references. The additional B.4(c) sources are B_separability.tex, B_product.tex and B_rigid7.tex, registered in B_separability_results.csv (six rows: B.46–B.49, B.52, B.56).

The source-excerpt duplicates listed in source_log_DE.md should be omitted as copies of attachments. The source log records the original PDF hash and the archival page-number correction. With the private runtime supplied by root, DE_review.pdf compiles to19 pages, with no undefined citations or errors. The separate B_separability_review.pdf is a component review. Final pagination and visual QA belong to the assembled paper.

## Further uniform-tail progress

D.13 proves a controlled hull lemma after a uniformly equivalent Euclidean choice of disk metric: Fill(A) is Q-natural and has exactly the same d_Q diameter as A. Components of d_Q-balls are simply connected, so individual small loops fill in the same ball. This removes an elementary metric small-loop obstruction. The unresolved step is a continuous, equivariant ambient extension of these controlled point-trajectory fillings; no group contraction is inferred from the pointwise lemma.

D.14 strengthens this by passing to the Q-invariant inner-diameter metricρ. Its balls are path connected and admit open disk neighborhoods U(u,r) with Bρ(u,r) ⊂ U(u,r) ⊂ Bρ(u,2r). Every sphere in a radius-r ball fills in a radius-2r ball. Every based compact locally path-connected parameter family in the original group remains continuous with a uniformρ tail. The inclusion of the resulting uniform-tail group induces isomorphisms on all positive homotopy groups. This is a comparison in the direction needed for sphere-family contractions, but no controlled ambient-isotopy theorem has yet been matched to all its hypotheses. Further sources checked include Černavskiĭ's explicit distinction of topologies, Hamstrom's compact-surface survey, and the Burago–Lu–Ozuch higher-regularity compact-torus theorem; none yields the missing arbitrary C₀-tail estimate.

D.15 adds a literature-settled arbitrary-frontier subcase. Fabel (1998), Theorem1.1, proves that the full orientation-preserving pointwise stabilizer of any nondegenerate nonseparating proper continuum in S² is an absolute retract homeomorphic to ℓ². Thus trivial operators cause no arbitrary-frontier obstruction for a simply connected domain with at least two complementary points, even with a non-locally-connected frontier. We retrieved and read the full paper, including its inner-diameter control and nested-disk compression. Those compressions are not Q-equivariant, so this does not decide the general centralizer.

D.16 locates an algebraic obstruction to one direct adaptation: any Q-equivariant continuous map of O into the preimage of a compact quotient subsurface induces the identity on Q through that subsurface's fundamental group. It therefore forces Q to be finitely generated. For infinitely generated Q, a global equivariant compression into a compact quotient core cannot be the missing cutoff construction. A family-dependent deformation of homeomorphisms is a different matter and remains undecided.

## Joint controlled map filling (D.17)

The remaining map-selection step can be completed for every based compact connected locally path-connected metric family (in particular all sphere families). D.17 constructs a jointly continuous Q-equivariant homotopy of continuous interior maps, relative to every identity parameter and the point x, with displacement at most128 eta for one positive eta in C0(N). It uses an adapted lifted triangulation and coordinatewise Tietze extensions inside the open disks supplied by D.14. The compact-core collapse lemma then proves joint identity extension to the actual closed disk. This settles joint continuity in the evaluated point at the level of maps. Injectivity, hence a homotopy through homeomorphisms, remains unproved; D.9 remains Open. The register now has28 rows.

## Additional route B.4(c) progress

B.46 gives Minasyan's exact paired criterion, with an independent proof of the trivial discrete-intersection specialization: closed HJ plus equality of the closure intersection is equivalent to closure of every one-factor finite-index refinement. B.47 supplies the explicit M2(Z) semidirect SL2(Z) counterexample, checks the full induced topologies, and witnesses its nontrivial intersection by a computed quotient PSL2(F8) of order504. The corollary with Gamma(3) retains the failure with both factors free of rank3 and a torsion-free ambient group. Thus factor freeness and individual separability do not remove the missing refinement.

B.48 checks the precise hypotheses of Fournier-Facio2025, Hagen–Sisto2023, Minasyan–Mineh2025 and Mineh2026. Their established conclusions do not give the required products for these symmetric subgroups. B.49 expresses each refined-product question as simultaneous conjugacy of the actual A5 embedding under the specified finite-index subgroup L.

B.52 proves a new, substantive part of the actual route: H_T H_5 itself is closed in the full profinite topology of the pure twelve-puncture mapping class group. Indeed it is exactly a finite word-equation locus. The proof classifies the four pure conjugacy classes of A5 embeddings with the same elementwise permutation action. In the central extension B11 to the stabilizer of one named puncture, a lift beta of order-five f satisfies beta^5=Z^m. The residue m modulo5 is well defined, nonzero by braid torsion-freeness, and invariant under conjugacy fixing the puncture. It distinguishes the four classes. The prescribed conjugacy of D by a pure g forces the original class, so the unique full A5 conjugator is pure. This converts the finite A5 relators into the exact product-membership equations; residual finiteness separates every failed equation.

The full product C_Gamma(T) C_Gamma(D) is therefore closed as a finite union of translates. The literal rank-two product is also closed for the following specified geometric choice: F_5^v is the subgroup of the cyclic centralizer fixing both poles, preserving both pentagon orbits and fixing one named vertex of the first pentagon. The covering sequence identifies F_5^v with the pure four-puncture sphere group F_2. It contains H_5 with index five; F_T contains H_T with index twelve. Hence F_T F_5^v is a union of sixty translates of the closed pure product. This does not assert the same result for arbitrary other complements which fail to contain H_5.

The finite-index condition is still exact and unresolved: for g=h(g)j(g) in the actual product and normal U of finite index, g belongs to the closure of the U-refinement if and only if the image of h(g) modulo U lies in the image of K. Actual refined membership requires that image to be trivial. This is stated as B.52.7–B.52.8; neither the four-class census nor unrefined closure is promoted to a proof that K=1.

Exact finite outputs: check_marked_a5.py constructs the240 compatible descriptions, checks four orbits of60, verifies their four distinct rotation multipliers, and writes all180 Cayley-table relators. The standard output and JSON/text certificate accompany the TeX. The separate B_separability_source_log.md and B_separability_references.bib record all primary checks, including González-Meneses2011 for the exact braid capping extension.


## Component QA at checkpoint 02 (02:49 UTC)

Both latest component PDFs were rebuilt twice with the private LuaLaTeX format and contain no unresolved citation/reference warnings. B_separability_review.pdf has nine pages (109691 bytes), zero overfull boxes; the initial draft had five overfull boxes above 2pt, maximum 24.483pt. DE_review.pdf has nineteen pages (160027 bytes), exactly three overfull boxes, respectively 1.13306pt, 0.58992pt and 1.06087pt, all below the requested 2pt threshold. The earlier D.17 29.651pt overflow has been removed. The changed full-centralizer/geometric-complement page and D.17 boundary proof page were freshly rasterized and visually reviewed; equations, margins and text are legible. Latest logs are B_separability_review_build_latest_0.out / _1.out and DE_review_build_latest_0.out / _1.out. Image checks are qa_B_scope-8.png and qa_D_boundary-10.png, supplemented by earlier reviewed spreads. All finite certificate scripts had passed before this purely textual scope clarification.


## A certified failure of the rigid seven-point route (B.56)

The retained set S={1,2,3,4,6,9,12} is one pole pair with its first pentagon in the exact labels of B.18. The ordered tetrahedral parameter curve is P1 minus fourteen points. Let e_minus and e_plus be positive meridians about u=-1 and u=1, and e_alpha a positive meridian about alpha=((sqrt(3)-1)/2)(1+i), with the explicit rational polygonal stems in B_rigid7.tex. The word h=e_alpha e_plus e_alpha^-1 e_minus^-1 is nontrivial already in integral homology, where its class is e_plus-e_minus. After retaining S, however, its braid is the identity in B6. The three braid words have lengths58,36,14; their composite reduces to the identity in Artin's faithful action on the free group F6.

The path-to-braid calculation is fully certified. The standalone program certify_rigid7_monodromy.py uses exact rational coordinates, rational real-root isolation for every crossing, exact derivative and imaginary-part signs, and exact endpoint orders. It excludes collisions and poles on all eighteen path segments. Its stdout and the468823-byte polynomial/interval certificate are retained. Earlier floating-point discovery files remain explicitly marked exploratory. check_rigid7_labels.py independently verifies that A5 has order60, the twelve rigid seven-point sets form one regular T orbit, and all twelve rigid pentagons and twenty-four rigid six-point sets are contained in them. Because H_T centralizes T, all twelve seven-point kernels are equal. Hence this single h defeats all these necessary tests, and it remains nonidentity after full profinite completion.

This also sharpens the four-point obstruction. With w from B.19, k=[h,w] is killed by every rigid five/six/seven-point map and every one of the495 four-point maps. It is nontrivial because [h] is nonzero in H1, [w]=0, and a nontrivial free-group centralizer is cyclic. Thus the two entire test families remain jointly insufficient. Neither h nor k belongs to K: their discrete pure mapping classes are nonidentity, and the discrete A5 centralizer is trivial. This establishes a precise obstruction to the proposed seven-point injectivity route, without a claim about the unresolved completed A5 centralizer.


## B.56 final component QA (03:20 UTC)

The ordered parameter was renamed S_T to match B.18; the coarse curve C_T retains its earlier meaning. The B component rebuilt successfully to twelve pages, 126814 bytes, with zero overfull boxes and no LaTeX citation/reference warnings. All three pages containing B.56 (qa_B56-09.png, -10.png, -11.png) were independently opened and visually checked after that change; formulas, the braid arrays, margins and the final common-kernel proof are legible. The final log is B56_review_final.out. The initial new-section overflows of6.06491pt and17.66316pt have both been eliminated.


## Complete scope of the B.4(a) test obstruction (B.56)

The intrinsic P3 tripod tests are identically trivial on every pure geometric mapping class and hence on the completed pure group: forgetting to three punctures gives the trivial pure mapping class group. The three P4 recipes for the named tetrahedral T also vanish identically on H_T and its completion. B.30 supplies tetrahedral descent to the pure four-special-point quotient; filling any of its three cone points yields a pure mapping class of a three-special-point sphere, whose geometric outer action is trivial. The third target remains C3 amalgam C3. These intrinsic maps agree with B.53 on the common A5-centralizing domain, but do not assume a general H_T element extends to an automorphism of B. Consequently h lies in the intersection of every test family named in B.4(a), and k additionally lies in all495 four-point kernels. This proves that the combined test route is not faithful; a full description of that common kernel is still not supplied, and K itself remains undecided.

Independent peer review of B.57's finite and topological support is recorded in review_B57_finite_topology.md, with check_B57_cusp_topology.py/.out/.json. All five original cusp colorings, sixty distinct tripod supports, and exact C3*C3 peripheral normal forms pass. The central-extension lifting and multiplier input are explicitly outside that peer review.

Expanded B.56 QA (03:28 UTC): after adding the correctly typed P3/P4 scope, B_separability_review.pdf has13 pages and130067 bytes; two passes yield zero overfull boxes and zero LaTeX warnings. The newly added proof on pages11–12 was rasterized and visually reviewed as qa_B56_alltests-11.png and -12.png. Build logs are B56_alltests_build_0.out and _1.out.


## Discrete common-kernel rank in B.56

All twelve rigid seven-point kernels are equal by T equivariance. Since each smaller rigid subset is contained in a seven-point subset and the P3/P4 recipes are zero, the discrete intersection in B.4(a) is exactly ker(f_S0). It is nontrivial by h. The certified beta_+ is b sigma_3^2 b^-1 for b=[-2,-1,-4,-2,-1,4], so its seven-point mapping class is an essential Dehn twist of infinite order. The kernel consequently has infinite index in F13; the standard covering-core argument proves it is free of countably infinite rank. The intersection with all495 four-point kernels contains k and is also a nontrivial normal subgroup of infinite index, so has the same abstract rank. The completed test intersection is exactly ker(hat f_S0), but its identification with the closure or the full completion of the discrete kernel is explicitly not claimed. The image's induced profinite topology would need a separate proof.


## Profinite common-kernel type determined (B.56, 03:36 UTC)

Shusterman's finite-word theorem applies to both completed test kernels. They are closed normal subgroups of the finitely generated free profinite group hat(H_T), have infinite index because the essential twist beta_+ has infinite image, and contain the nontrivial discrete words h and k. A basis of the discrete free group H_T is a profinite basis of its completion. Thus the theorem's extra finite-word hypothesis is met, and both completed intersections are free profinite of countably infinite rank. This determines their abstract topological group types; it does not identify either embedded kernel with the closure or full completion of the corresponding discrete kernel. The convergent-basis convention is explicit. No general claim that every closed normal subgroup of a free profinite group is free is used.

The final B.56 prose also separates the two infinite-rank completion conventions explicitly. Each discrete kernel is an abstract free group on countably infinitely many generators, so its full profinite completion has uncountably many index-two open subgroups and is not metrizable. Each completed test kernel is closed in the metrizable finite-rank free profinite group hat(F13), so is metrizable. They therefore cannot be the full profinite completions of the discrete kernels. Equality with the embedded closures remains a different, unproved induced-topology question.

Final D component after the one-word D10 prose correction: DE_review.pdf has19 pages and160014 bytes, no warnings, with the same three overfull boxes below2pt. Log DE_review_final_0329.out. D.9 remains Open after the additional primary Hatcher2026 check recorded in source_log_DE.md.


## Component source freeze for checkpoint03 (03:38 UTC)

B_rigid7.tex, B_separability_results.csv and B_separability_references.bib now include the full discrete and profinite countable-rank conclusions with Shusterman's exact finite-word hypothesis. The final B component has13 pages,135665 bytes, zero overfull boxes and zero LaTeX warnings. Newly changed pages12–13 were rasterized and visually reviewed as qa_B56_profinite-12.png and -13.png; the theorem application, topology distinction and new bibliography entry are legible. Logs: B56_final_freeze_build_0.out and _1.out. The final D/E component has19 pages,160014 bytes, no warnings and only the same three overfull boxes below2pt. All mathematical source changes for this checkpoint are complete. A possible subsequent all13-meridian monodromy computation will be developed separately before any new formal claim.


## Explicit embedded kernel and incomparability (B.56, after checkpoint03)

The all13-meridian extension is now integrated into B_rigid7.tex and the result register. A rational fan of thirteen disjoint square petals supplies an actual geometric free basis; exact segment–rectangle tests and rational sqrt(3) brackets certify this basis, including the cyclic order and the infinity meridian. The standalone exact Sturm program covers78 path segments and records all680 reduced braid letters. Its output is ALL EXACT CHECKS PASS (80.69seconds). The three earlier words are literally unchanged.

The rigid kernel is exactly ker(theta:F13→PB6), with theta specified on this basis. Capping first gives preimage of the central full twist; the pair-linking map on the two normalized constant strands 4,6 then proves that the image meets that cyclic subgroup trivially. The same map to Zhat removes the central closure in the completed formula, so the completed test kernel is exactly ker(theta-hat). The supplied finite-word membership utility uses Artin's faithful action, with an exponent shortcut. It does not claim computable membership for arbitrary profinite elements or equality with the closure of the discrete kernel.

The rigid and all495 four-point kernels are now proved incomparable. The degree4 covering cross-ratio for {1,2,3,5} detects h after filling the eight order3 parameter punctures. Conversely, the384-letter B.19 balanced commutator w has a noncentral Burau image over F101 under the rigid monodromy. The actual6×6 matrix and all representation checks are supplied. The common word k=[h,w] has776letters. Neither these words nor the nonfaithfulness of their test families gives an element of K.

The new files, actual stdout and SHA256 hashes are documented in next_B56/README.md. They were developed separately during the checkpoint03 source freeze and integrated only after root confirmed ZIP creation. The primary Artin/capping input remains González-Meneses2011, Sections1.6,2.2,4.3, already opened and archived; no new literature claim is needed for the elementary pair-linking or checked matrix arguments.


## All13 extension QA (03:57 UTC)

The integrated B component rebuilt twice to16pages and150311bytes, with zero overfull boxes and zero LaTeX warnings. The initial draft had one33.86365pt overflow in the isolated review and one15.11322pt overflow after integration; both were fixed by shortening paragraph leads. The final three extension pages13–15 were rasterized at100dpi and opened for visual inspection: all formulas, the13-column word table, the6×6 matrix, margins and text are legible. The final logs are B56_all13_final_build_0.out and _1.out; image checks are qa_B56_all13-13.png through -15.png. The pair-linking and Burau auxiliary checks and finite-word selftest were rerun after their final edits and passed.


## Main product progress at degree one (04:27 UTC)

B.58 gives a new family of actual refined-product results. The twelve rigid-seven forgetful maps induce a split integral injection Z^54 to Z^168 on the first homology of the full pure twelve-puncture mapping class group. A completely specified168-by54 matrix has54 Smith factors equal to one, and an explicit54-row minor has determinant minus one; its integer inverse is stored and independently multiplied out. The certificate also reconstructs the exact Mobius-normalization covectors, avoiding the central order-two sphere-braid lattice. Root independently reconstructed the twelve subsets from the six order-five subgroups and verified both inverse products in code/verify_B58_certificate.py.

Since every element of the actual residual centralizer K dies in all these rigid maps, K has zero full profinite abelianization. Thus all products (H_T intersect L1)(H_5 intersect L2) are closed whenever each finite-index Li contains [P,P]. This includes every one-factor refinement determined by a finite abelian quotient, with no omission of primes2,3,5. In particular the nonzero degree-one coprime fixed classes in B.20 do not lift from the actual K. Arbitrary nonabelian refinements remain unproved; K is not thereby proved trivial or perfect.

An independent orbit-curve computation compares all55 pair-linking coordinates of the full twelve-point family with the15 coordinates of its specified rigid-seven restriction. Exact valuations over Q(i,sqrt3) at all13 basis meridians give rank6 for both matrices and an integer reconstruction with multiplier6. The restricted matrix agrees with the independently certified13 braid words. This supplies a separate restriction check; the stronger ambient unimodular certificate already proves the result. Formal source: B_abelian_refinements.tex. Scripts, standard output and complete integer/rational certificates are retained in work_DE.

## B.59: class-two refinements (04:36 UTC)

The exact ambient degree-two rigid-seven matrix has size240×165, rank159, Smith factors159 ones and6 zeros. Its primitive integral kernel has rank6. Restriction to the actual A5 action, generated by geometric elements of orders2,3,5, has fixed-equation rank5 with Smith factors five ones. The remaining fixed kernel is one primitive line, generated by v=(1,1,2,1,-1,1) in the certified six-element kernel basis. Its ambient triple vector has45 nonzero coefficients.

B.59 proves that K projects into this one central Zhat direction in the full completion of P/gamma3P. Removing that primitive direction gives Q with abelian rank54 and derived rank164. Every pair of finite-index refinements containing the preimage R of the line is closed. This is a genuinely nonabelian finite-quotient family. The proof includes full-topology justification using integral Malcev coordinates; no pro-nilpotent/full completion substitution and no averaging by60. The one line might still have zero actual K image; no nonzero lift is constructed. Arbitrary class-two and general finite quotients remain open.

Formal: B_class2_refinements.tex. Certificates/code/stdout: check_ambient_rigid7_class2.py/.out, ambient_rigid7_class2_certificate.json; check_rigid7_class2_invariants.py/.out, rigid7_class2_invariants_certificate.json. Parent independent formal review passed. Independent root code/verify_B59_certificate.py/.out checks CN=0, primitive N minor, rank159mod101, fixedrank5mod101, primitivew, and consistent60-element matrix action.

Future direction only: degree-three unrestricted ambient detection cannot be injective by ranks990>12·70=840. Any next step must restrict actual A5 invariants or the tetrahedral image, not repeat an unrestricted injection claim.

## B.60: actual common class-two images

The remaining B59 line cannot be removed merely by restricting to actual subgroup images. The exact tetrahedral word a=[e1e2^-1e3,e5] maps to2w. For the cyclic meridians f0 at0 and f1,...,f5 at1,zeta,...,zeta^4, the explicitly displayed product of seven commutator powers b0 maps to w. Consequently the two actual subgroup images in the full class-two completion share2Zhat w. The particular a has a nonidentity rigid Burau matrix overF101 at t2, so it is not a full rigid-kernel element and no K-lift is inferred. Root independently recomputed both165-coordinate identities directly from original H1 columns and reviewed the geometric-family and full-topology arguments (records/root_review_B60.txt). Formal B_class2_common_image.tex; register updated.

Full11-strand exact13-meridian monodromy completed307.36s. All78 rational pathsegments and crossings certified by Sturm, all13 projections match the earlier6-strand certificate, and all55pair linkings match rational-divisor calculations. Files in next_B59_image. The completed degree3 calculation retains corrections from HT intersect gamma3P and supplies actual integral words, with every comparison at the same geometric marking.

## B.61: explicit class-three common image with rigid vanishing

A complete geometric and algebraic certificate now gives actual words A in HT and B in H5 which agree modulo gamma4P, have nonzero class2 image5091840w, and whose common image vanishes in all twelve rigid-seven class3 quotients. They are distinct in P, since the actual discrete centralizer intersection is trivial. No element of K or compatible tower through all degrees is constructed.

The common base is verified exactly in Q(i,sqrt5,sqrt((5+sqrt5)/2)): tetrahedral parameter i(phi+sqrt(phi+2)), cyclic parameter−phi². Rational interval bounds certify the base-cell homotopies and a uniform separation homotopy replacing fifth roots by rational constants. All full11 and cyclic braid crossings are exact Sturm-certified, with all55pair-linking comparisons.

The degree-three computation includes all thirteen tetrahedral generator logarithms,78 binary brackets, and all ternary brackets. Its lower-layer matrix has rank19/nullity72, so source-abelian and bracket relations are retained. The correction equations and the additional70 rigid equations admit explicit rational solutions. These are converted to actual integer power-commutator words with D=2545920, then separately evaluated in the actual Artin logarithms. The independent evaluation passed25.5s. The completed quotient has a common nontrivial procyclic image detected by5091840w.

Formal B_class3_common_image.tex and register updated. Root independently reran the actual-word evaluator and accepted the scoped theorem; `records/root_review_B61.md` records the25.47s passing evaluation and the geometric marking/topology audit. All code, stdout, complete word exponents, matrices and homotopy certificates are in next_B59_image. The multiplier is D=2^8·3²·5·13·17; its size is an artifact of the chosen rational solution and integral collection, and no optimality is claimed.


## B.62: a nonnilpotent finite quotient killing the actual residual group

The exact common-base monodromy of B.61 gives the projective genus-five homology representation modulo3. The branch cover is canonical under all twelve-puncture sphere mapping classes; the fixed-line quotient and invariant-hyperplane integral models agree. The full twist acts as minus the identity, so projectivization descends to P. Stylianakis2018 Theorem5.1 shows its pure image is PSp10(F3).

The actual tetrahedral/cyclic finite images have orders144/1440 and common groupC3. The tetrahedral derived subgroup has order24 and meets that C3 trivially. Its abelian quotientC6 is detected by source character(3,2,3,3,2,3,2,3,3,3,2,2,3). The seven primitive directions of the full source-H1 kernel all have zero character. B.58 places K in that completed kernel; the identically zero fixed-pair(4,6) linking row removes the central full-twist ambiguity. Consequently q(K)=1, giving closed products for every pair of finite-index refinements containing ker(q). This is an actual nonnilpotent finite quotient, not an intersection of unrelated test targets.

Root independently recomputed from the original braid words in the different invariant-covector hyperplane basis; code/verify_B62_symplectic.py/.out verifies all group orders/intersections, the integral source kernel, all seven word images and the change matching all nineteen matrices. Root geometric/topological review accepted the scoped theorem. The formal source is B_symplectic_refinements.tex. All primary checks and exact outputs are recorded. No higher3-power, arbitrary finite-quotient or full K conclusion is claimed.


## B.63: exact first3-adic lift and a smaller open refinement

The actual mod-nine projective homology image has tetrahedral and cyclic identity-fibre vector spaces of dimensions6 and9; their intersection has dimension3. The full image upper bounds use1872/8640 Schreier edges over the144/1440 mod-three groups. Six short words in the actual normal closure of B.56 h realize the whole tetrahedral space; nine cyclic commutator words realize the whole cyclic space. Thus these exact source conditions do not shrink the identity-fibre intersection. Three displayed matched pairs have lengths38/94/88 and16/54/54. Both source words have zero ambient integral H1; each tetrahedral word lies in the actual full rigid-test kernel.

The common matrix Lie algebra is solvable: with suitable basis H,E,F, [H,E]=E, [H,F]=-F, [E,F]=0. It is not sl2(F3), and no identification of the full3-adic integral centralizer is inferred. The subgroup W9 of order27 bounds q9(K). Its preimage M9 is a proper, explicitly nonnormal finite-index subgroup of ker(q3). The B52 ambiguity argument proves closed products for every pair of finite-index refinements containing M9. The factor indices for M9 are3888 and1049760. This is a stricter open-subgroup refinement family, not a new normal quotient in which K is proved trivial.

The root independent verifier code/verify_B63_first_lift.py/.out passed in1.3seconds, using an alternate integral ker(epsilon) model and fresh mod-three transversals, independent finite-field elimination, all fifteen short words, three matched pairs, literal rigid-kernel substitution and Lie brackets. It compares discovery matrices only at the end. The standalone work_DE verifier also checks a concrete nonnormality witness. Formal source: B_symplectic_first_lift.tex. No actual nonzero K element, all-level compatible lift, or equality in a joint forgetful finite quotient is asserted.


## B.64: exact Eichler centralizer and the full3-adic representation obstruction

The actual12-strand icosahedral braid representation on closed genus-five homology has character twice the irreducible degree5 character. Its integral-at3 commuting order has a primitive basis I,H,E,F with H²=I,E²=F²=0,[H,E]=2E,[H,F]=-2F,[E,F]=3H and EF=3(I+H)/2. Thus it is exactly the level3 Eichler order[[Z3,Z3],[3Z3,Z3]], with symplectic centralizer its determinant-one group. The natural10-dimensional congruence filtration is3O: its principal group consists of[[1+3a,3b],[9c,1+3d]] of determinant1. Ordinary2-by2 reduction modulo3 would lose the F direction and is explicitly not used.

The full3-adic common-image statement is now proved. Let R_T=normal<h> intersect HT-prime. In the projective principal identity fibre, closure(q(R_T)) intersect closure(q(H5-prime)) is exactly the three-dimensional Eichler principal group. The six/nine squared actual words from B63 lie in the connected derived centralizers, of dimensions6/9. Their logarithms divided by3 form bases modulo3 of the saturated integral Lie lattices. A direct successive-cube approximation then gives the whole two derived principal groups, whose intersection is the A5 principal centralizer. All scalar-log comparisons remain valid even for the ramified3-adic splitting field, because block determinants lie in1+3O_K by eigenvalue integrality.

This proves that the common matrix image survives compatibly at every3-power level while respecting actual rigid-normal tetrahedral words and commutator conditions on both sources. It does not produce equality of the two lifts in Phat or a nonidentity element of K. Root and CE independently accepted the proof. The formal source is B_integral_symplectic_centralizer.tex; exact original matrix/lattice program and output are under next_3adic_symplectic.


## B.63–B.64 final component QA (06:34 UTC)

The final standalone B review has32pages and251493bytes. The bibliography and all references resolve; the sole overfull box is0.48714pt in B63 prose. Pages25–30 were rasterized and visually inspected, including the short word tables, full Eichler-order assertion and ramified logarithm proof. Root independently reran the exact B64 matrix/lattice certificate (records/root_B64_rerun.out); CE independently audited the proof (work_CE/review_B64.txt). The complete check is qa_B63_B64.md. Mathematical sources remain frozen after06:32.


## Seventh-hour recovery: B65 and B66

The execution environment failed around07:43UTC before the checkpoint07 archive existed. Root restored verified checkpoint06 into the replacement environment. The two complete proofs are now reconstructed as B_dihedral_rigid.tex and B_prounipotent_persistence.tex, explicitly identified as reconstructions in source comments. Their register rows and the two verified B66 bibliography entries have been restored mathematically. No byte identity with the unavailable original seventh-hour files is claimed.

B65 proves that the free rank-six pure cyclic centralizer also centralizes the actual D5 generated by its C5 and a named involution r in T. The two D-stable rigid-seven maps are zero; all ten remaining full maps have the same kernel after their actual transports. The exact six-image map theta5 into PB6 has that discrete kernel and its completed map has that completed kernel. Fixed-pair linking removes the center in both categories. The transport d^2r sends omitted branch point2 to11, so two distinct genus-two homology tests need not agree. The freshly rerun check_B65_reconstructed.py/.out verifies every permutation, subset, source-word deletion and linking assertion against checkpoint06 inputs.

B66 uses the actual common K-rational ordered point and strict based Galois functoriality. A single arithmetic element acts as alpha^d on every lower-central graded piece. Its explicit polynomial weight-two eigenprojections give compatible actual source preimages of a nonzero common prounipotent element with degree-two vector w, fixed by A5 and killed by all full rigid tests. This closes the rational prounipotent separation route for the existing line. Unbounded possible denominators prevent an inference of any compact pro-ell or full profinite element.

The newer exact Q/Birman note and action certificate were also reconstructed and freshly rerun: next_joint_rigid_symplectic/Q_Birman_reconstructed_note.md, reconstruct_Q_birman.py/.out and Q_birman_reconstructed_certificate.json. They establish an intermediate factorization through Z2*Z2*Z, an exact F3 base, and an explicit rank-four free-fiber action. At that reconstruction stage Q injectivity and the final theta5 comparison were Open; B67 below subsequently refutes the proposed Q injection while retaining the theta5 question. The last-conjugator extraction is explicitly antihomomorphic; inversion corrects it. Full recovery provenance and losses are listed in recovery_ledger_DE.md.


## B67: exact refutation of the intermediate Q injection

The exact Birman action exposes a larger C stabilizer: f fixes C,V=T^-1RT and ST, while (ae)(C)=pCp^-1 with p=V^-1(ST)^-1. Hence w=[(ae)^-1f(ae),c] maps to1 in PB5. Its twelve-syllable free-product normal form and an explicit S3 quotient show it is nontrivial in Q=Z²*Z²*Z and its full completion. The same original source word has a nonidentity PB6 Artin image, so it does not settle theta5. This refutes the proposed intermediate presentation and the associated coset-indexed orbit-family independence, rather than merely leaving them unproved. B_Q_noninjection.tex is integrated in the component review and B.67 is registered Refuted. Root independently reread the full proof/code and reran the certificate successfully. No new general theorem or bibliography is used. Main B remains Open; B69 below subsequently refutes full theta5 injection while leaving the completed-kernel closure comparison unresolved.


## B68: the surviving lift is a filling point push

The B67 word w=[(ae)^-1f(ae),c] dies after deleting label5 but its actual full lift has a last-strand Birman loop of length144 (cyclic length142). Six explicit free automorphisms, each checked against its inverse on all generators, take its conjugacy class to a24-letter word. The associated Whitehead graph has10 vertices and15 edges, remains connected after every vertex deletion, and is therefore not separable by the published Heusener–Weidmann Corollary3.5. This proves nonmembership in every conjugate proper free factor, stronger than nonprimitivity. On the six-punctured sphere a nonfilling loop lies on one side of an essential separating curve, and each side group is a conjugate proper free factor. Hence the loop fills, and Kra's actual point-pushing theorem makes its seven-punctured-sphere image pseudo-Anosov.

The new standalone verifier reads the original common-base eleven-strand words and performs fresh Artin, deletion and free-word operations; it does not rely on the discovery minimizer for the source word. All six automorphism inverses and eleven connectivity spanning trees are retained in the certificate. Root independently reran the verifier, read the complete proof, and opened the published separable-set criterion and Kra's original theorem. Both bibliography entries explicitly record Verified. Formal source: B_Q_filling.tex. This strengthens the geometric description of the surviving full lift; B69 below subsequently refutes full theta5 injection, the completed-kernel closure comparison remains Open, and no profinite pseudo-Anosov-centralizer conclusion is made.

B sources, bibliography and register are frozen after this integration for the checkpoint08 combined build. Further investigation is confined to notes until root releases the freeze.


## B69–B70: the full cyclic test family is not faithful

There is now an actual full theta5 relation, stronger than B67's intermediate counterexample. The reduced ten-letter word [f5^-1 f1^-1 f0^-1 f2^-1,f1] has nontrivial S3 source image but identity Artin action on all six free generators after substituting the actual PB6 monodromy. The braid substitution has length132. Its structural derivation uses the full last-strand Birman action: with f1 normalized to B=x1...x5, the boundary conjugator of g=f5^-1 f0^-1 f2^-1 equals the actual fiber image of h=f5^-1 f1 f5. Hence h^-1g fixes B. This is a literal free-word equality, not only a relation-module identity.

The exact map theta5 and theta5-hat are therefore both noninjective. B65 identifies these with the joint kernels of all twelve rigid-seven restrictions on H5. Their images are infinite by the integral linking difference ell45-ell46, which sends f5 to1 and survives the central full twist. The discrete normal kernel is free of countably infinite rank. The completed closed kernel is free profinite of countably infinite rank by the exact Shusterman theorem, since it contains a nontrivial finite basis word and has infinite index. The full source topology is B28's already checked one. Root independently reran the certificate, checked the full proof, and reopened the primary finite-word theorem; CE independently inspected the certificate.

The exact six monodromy words give the specified embedded kernels and a terminating discrete membership test through Artin's action. No normal generating set or finite presentation of the image is claimed. The comparison M5=closure(N5) remains open, and M5 is not the full profinite completion of the abstract countably generated free group N5. The actual source word is not in K, since the discrete pure A5-centralizer is trivial. Formal source: B_full_cyclic_kernel.tex. The short-lived sufficient affine-orbit criterion was valid, but its actual hypothesis is refuted; the full unquotiented conjugator identity is what upgrades that failure to the actual relation.

The next scoped lead is whether a second exact cyclic relation can realize the remaining primitive degree-two direction w, followed by an actual simultaneous-rigid/matrix comparison. No such second relation has yet been asserted.


## B71: a common image survives the joint full-rigid and full3-adic quotient

The new actual cyclic kernel word supplies the missing full-rigid condition in B64's representation barrier. Nine explicit conjugates u w0^20 u^-1, with u in {1,f0,f1,f2,f3,f5,f0²,f1f0,f4f2}, give logarithm residues spanning the saturated nine-dimensional cyclic derived Lie lattice modulo3. The original-word verifier gives an exact minor determinant−52, a unit modulo3; all words have length200–204 and zero integral source H1. B64's successive-cube argument therefore places the whole cyclic derived principal group in the compact matrix image of normal<w0>, with closures taken inside H5hat.

The tetrahedral subgroup R_T from B64 already kills every full rigid test. Both actual rigid kernels now realize the same full three-dimensional Eichler principal group in genus-five homology. Consequently their joint images in (the product of all twelve full rigid targets) times PSp10(Z3), restricted to the rigid-identity principal slice, intersect in exactly {1} times that Eichler group. Every rigid coordinate is literally1, and compatibility holds at all3-power levels in each source completion. This is an exact joint quotient statement, not a comparison of separately chosen finite images.

Root independently accepted the complete proof and reran the exact certificate. Formal source: B_joint_rigid_symplectic.tex. The closed normal subgroup is formed inside the finite-rank source completion; neither the full completion of abstract N5 nor the unresolved equality M5=closure(N5) is used. The actual ambient intersection and K remain Open. Further work should therefore address that full ambient topology rather than additional levels of this representation.


## B72: the two actual source groups are disjoint under every discrete conjugation

The geometric distinction between the sources now gives H_T intersect g H5 g^-1=1 for every g in the full twelve-point mapping-class group. The actual index5 four-point comparison classifies a nontrivial cyclic source element as pseudo-Anosov or peripheral. Its seven cusps produce multitwists with exactly one or five reduction curves. A4 has a fixed point in every action on one or five objects, and a fixed essential sphere curve would partition the transitive twelve-point A4 set into invariant parts; A4 cannot exchange the two parts. Thus no such reducible element centralizes T. For a pseudo-Anosov, the common finite symmetry kernel would contain T and the conjugate C5, forcing an actual A5 on twelve marks, whose discrete centralizer is trivial.

The measured-foliation argument is given explicitly for marked punctures, including one-prong separatrices, rather than silently enlarging the scope of McCarthy's compact-surface introduction. Formal source: B_mixed_conjugates.tex. The proof is a full discrete structural strengthening; it does not classify arbitrary profinite elements or prove equality of completed intersections. Neither factor is asserted individually malnormal. The refined product and actual K remain Open.

The accompanying faithful eight-point common-involution setup and its exact branch-homology calculation are retained in next_common_involution. They expose a possible full ambient route, but the extra three first-homology directions are branch-swap anti-invariant and do not by themselves give a new constraint from the original cyclic abelianization. These findings remain research notes.


## B73–B74: faithful common-involution ambient comparison and full dihedral splitting

The actual common involution r gives a faithful comparison of both source completions inside a colored eight-point mapping-class group Q8. Its sheet-parity kernel L8 has index32, and the unique lift fixing original label1 supplies the explicit section. The valid prime-order centralizer comparison identifies its completion with the actual ambient completed r-centralizer. Forgetting the two cyclic poles1,3 is faithful on H5 and its full completion: the before/after cyclic quotient orbifolds are the same, with their two branch points distinguished by rotation residues. The remaining common-involution quotient gives an index16 subgroup L7 of the corresponding colored seven-point group, using the lift fixing original label2. Consequently K embeds faithfully in its pure seven-point subgroup. No injectivity on the whole tetrahedral source or equality of seven-point intersection preimages is inferred.

The eight-point comparison transfers B72's disjointness under every discrete conjugator and B52's unrefined product closure. It also gives an exact remaining condition: every one-sided finite-index refinement (A intersect V)B must be closed in Q8. This condition has not been proved. The original ambient K question therefore remains Open despite the faithful lower-complexity ambient realization. Formal source: B_common_involution.tex.

The full cyclic centralizer admits an explicit half-commutator retraction. Its commutator with r lies in the central C5 and restricts to squaring on C5; correcting by its unique inverse square root gives the direct product C5 times the full D5-centralizer. The latter is C2*Z. The exact orbifold cover q=(u^5+1)^2/u^5 has degree10 and D5 deck group, identifying H5 as its normal index10 torsion-free subgroup. Completing the actual product and taking r-fixed points proves the same full ambient profinite centralizer description, using only the previously established prime5 topology. Its faithful eight-point realization requires Q8-tilde, which permits all permutations of the five nonpole ordinary marks; Q8 has index120 there, and the full D5-centralizer meets Q8 in H5. Formal source: B_full_dihedral.tex. The retraction is defined on an infinite-index centralizer and does not supply an ambient virtual retraction.

Both formal proofs were independently reviewed and accepted before integration. They add no bibliography entries; their covering and completion inputs are the already audited B28/B30/B65 results. The natural finite-index forgetful-retraction candidate is explicitly refuted in next_common_involution/forgetful_retraction_obstruction.md: on H5 it fills four actual parameter punctures, with a nontrivial kernel whose completed comparison is exact for that particular map. This is a research countertest, not an obstruction to every possible virtual retraction.


## B75: an exact split Birman model for the remaining uniform condition

The new four-moving-point model is complementary to attached LM4 F14/F15, which already solve correction in their specified two-point interaction kernel and retain the original-source membership condition. In the colored eight-point group, retain the ordinary labels U,V and the branch pair, and forget the other four ordinary labels. The actual target is Q4=C2*Z and the actual kernel is B4(S0,4). The subgroup G_V of the full dihedral centralizer has presentation C2*F3; its forgetful map fills two explicit cusps and supplies a genuine C2*Z section. Characteristic finite quotients of the finitely generated surface-braid kernel prove the exact completed semidirect product.

Conjugation by the other tetrahedral involution acts trivially on Q4. Its commutator with G_V is therefore a based nonabelian cocycle into the actual braid kernel. The finite-order check order(sd)=3 versus order(rsd)=5 removes the possible nonpure deck discrepancy. The discrete cocycle is injective as a set map, while its completed zero set is exactly K, with fibers hK. Its vanishing is equivalent to a uniform characteristic-finite-cover separation condition, which is still unproved. Pointwise residual-finiteness separation does not supply that uniformity.

Formal source: B_birman_cocycle.tex; original-data finite/rational certificate and genuine output: next_common_involution/check_Birman_cocycle_data.py/.out. Root read the complete proof and accepted its scope. No new bibliography entry is needed. This reformulation does not close the prior source-membership gate and does not claim a new general cocycle-correction theorem. Subsequent work reconstructs the actual positive marginal of attached F23 because its original computation files were not among the recovered inputs.
