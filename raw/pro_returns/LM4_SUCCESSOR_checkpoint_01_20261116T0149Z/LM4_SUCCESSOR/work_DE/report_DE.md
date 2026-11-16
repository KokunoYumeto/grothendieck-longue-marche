# Parts D and E.2 outcome report

| Task | Outcome | Exact place |
|---|---|---|
|LM4 C.88|Proved with independent compact-core collapse argument and exact map/inverse isometry.|D.1–D.2|
|LM4 C.92|Proved, with the based Epstein theorem and all orientation exceptions checked.|D.3, D.6|
|LM4 C.90 and C.91|Proved for compact quotient, including nonorientable quotients.|D.4–D.5|
|Every compact family for arbitrary noncompact quotient contracts with a uniform tail|Unresolved. No false transfer from compact-open topology is made.|D.9|
|Remaining arbitrary-frontier and infinite-component comparisons|Unresolved, each comparison stated precisely.|D.10–D.12|
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

Formal assembly sources: section_D.tex, section_E2.tex. Register: results_DE.csv (25 rows). Bibliography: references_DE.bib. Primary-source provenance: source_log_DE.md. Exact programs and stdout are attached in work_DE; root may relocate them under code/ while preserving names and references.

The source-excerpt duplicates listed in source_log_DE.md should be omitted as copies of attachments. The source log records the original PDF hash and the archival page-number correction. A local standalone LuaLaTeX build was initially blocked by a missing system format. Root has since supplied a private runtime; final pagination and visual QA belong to the assembled paper.

## Further uniform-tail progress

D.13 proves a controlled hull lemma after a uniformly equivalent Euclidean choice of disk metric: Fill(A) is Q-natural and has exactly the same d_Q diameter as A. Components of d_Q-balls are simply connected, so individual small loops fill in the same ball. This removes an elementary metric small-loop obstruction. The unresolved step is a continuous, equivariant ambient extension of these controlled point-trajectory fillings; no group contraction is inferred from the pointwise lemma.

D.14 strengthens this by passing to the Q-invariant inner-diameter metricρ. Its balls are path connected and admit open disk neighborhoods U(u,r) with Bρ(u,r) ⊂ U(u,r) ⊂ Bρ(u,2r). Every sphere in a radius-r ball fills in a radius-2r ball. Every based compact locally path-connected parameter family in the original group remains continuous with a uniformρ tail. The inclusion of the resulting uniform-tail group induces isomorphisms on all positive homotopy groups. This is a comparison in the direction needed for sphere-family contractions, but no controlled ambient-isotopy theorem has yet been matched to all its hypotheses. Further sources checked include Černavskiĭ's explicit distinction of topologies, Hamstrom's compact-surface survey, and the Burago–Lu–Ozuch higher-regularity compact-torus theorem; none yields the missing arbitrary C₀-tail estimate.
