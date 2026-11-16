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

Formal assembly sources: section_D.tex, section_E2.tex. Register: results_DE.csv (28 rows). Bibliography: references_DE.bib. Primary-source provenance: source_log_DE.md. Exact programs and stdout are attached in work_DE; root may relocate them under code/ while preserving names and references. The additional B.4(c) sources are B_separability.tex and B_product.tex, registered in B_separability_results.csv (five rows: B.46–B.49, B.52).

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
