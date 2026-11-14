# Independent full-prompt coverage audit

## Scope and conclusion

This audit reads the complete upload/PROMPT(20261113-205800).md, the current root integration program, the assembled Sections A–F, the results and readings registers, the replacement integrated report, Montpellier's report, and the late F.23/F.51 corrections. It checks whether the explicit questions are actually answered, rather than treating a row identifier as sufficient evidence. It incorporates the prior independent mathematical audits in work/spheres/independent_audit.md and the new stack audit in work/spheres/F51_independent_audit.md.

The 48 required opening, lead, lettered, added EXIT, and LM8 entries now have explicit counterparts. The substantive late correction is F.51: independent atlas germs do not in general reconstruct an intrinsic neighbourhood of a nonproper analytic stack, and even the intrinsic covering-germ equivalence can fail. The proper étale replacement and the synchronized actual-neighbourhood construction have complete proofs. F.13/F.18/F.19/F.26/F.27 have been scoped accordingly, and the statement about the branch atlas in F.34 is explicitly a statement about its actual Hausdorff space.

The one direct source obligation still not fulfilled is the literal FLAGGED_149 comparison in EXIT added task 6, registered as F.45. F.44 also remains Open as a concrete further arithmetic test over Q^solv. The prompt's F(b) expressly asks for delimitation of proved and open intermediate field ranges. Its field-range comparison is supplied; the audit does not turn the additional Q^solv attack into a newly imposed demand to prove reconstruction over every field.

The two repairs identified during this audit have been written, with proofs:

- F.23 now has an explicit old-resolution comparison in work/montpellier/F23_old_kernel.tex: exact discrete and profinite kernels at both exceptional tails, rather than only the new model's injectivity. Its polynomial and finite quotient checks have been executed.
- work/root/B_background_audit.tex explicitly verifies the supplied LM3b H.7 cohomology calculation and distinguishes it from CATHOT D.1's bounded contractible-object construction. It is to be inserted after B.3, without a new statement identifier.

The final integration has now been checked to include both insertions, F.51 and its metadata, and the saved F.46 and folio corrections listed below. No mutation of the root report was made by this audit.

## Required coverage table: all 48 entries

“Covered” means that a proof, or a complete refutation with its corrected theorem, is supplied in the listed statements. It does not mean that every original assertion was true.

| Explicit prompt entry | Actual answering statements | Coverage assessment |
|---|---|---|
| Opening item 1: §14 mixed topos and cohomology | B.1–B.13 | Covered. The mixed gluing is identified, the effective-image defect is calculated, and the unqualified scan-129 claim is refuted. |
| Opening item 2: §16 hole filling and van Kampen | C.1–C.8 | Covered. The exact ambient two-category, surjective-boundary hypothesis, Cartesian squares, pushout, acyclicity, operators and transitivity are explicit. |
| Opening item 3: §20 spheres and two-isotopy | D.1–D.16 | Covered. Includes the requested extension, pair invariant, dimension-five classification, fidelity bounds and arithmetic losses. |
| Opening item 4: Montpellier cotes 149 and 147 | F.1–F.51 | Mathematical constructions and corrections covered, including the late stack counterexample. The literal external-source obligation in F.45 remains incomplete. F.44 records the additional field test. |
| Lead 1 | A.1–A.22; E.1–E.6 | Covered. Discrete multi-Galois recognition is separated from pro-Galois recognition; finite automorphism groups are not imposed on the manuscript's discrete definition. |
| Lead 2 | B.1–B.4, B.9 | Refuted with replacement. The mixed topos is not the logarithmic topos; objects, points and the coefficient comparison are written explicitly. |
| Lead 3 | C.1–C.5; E.7 | Covered in exact scope. The manuscript's surjective-boundary pushout is valid even in all ordinary topoi; the unrestricted profinite and higher-shape substitutions are refuted. |
| Lead 4 | D.1–D.3, D.11–D.16 | Refuted with replacement. The topological two-type is established; the crossed-module quotient, its stackification, and BPGL2 are distinguished. |
| A(a): 1.1 and exactness axioms | A.1–A.4 | Covered. Boolean pointless counterexample, separate sufficiency of local connectedness and enough points, and explicit exactness/atom axioms all have proofs. |
| A(b): all numbered §1 propositions and 1.12 | A.5–A.8 | Covered. The five conditions, sums/quotients qualification, pointed uniqueness, and full Hom groupoid including centralizers are explicit. |
| A(c): 2.1, 2.2 and the tower | A.9, A.22; E.1–E.4 | Covered. No points are needed under the stated splitting hypothesis; every stage and its universal property are constructed, with the ordinary/higher change of language specified. |
| A(d): the two examples, alpha and beta | A.10–A.12 | Covered with correction. Both requested phenomena are constructed. Literal beta needs a point in every component; alpha's fullness/faithfulness are exact neighbourhood-limit conditions. |
| A(e): the unwritten pro/profinite section | A.15–A.21 | Covered. Analogues of recognition, points, universal covers, Hom and the envelope are supplied; étale schemes, nonnormal examples and §7 diagrams are included. |
| A(f): induction, faithful groupoids, pairs and the field case | A.13–A.14 | Covered. The two-cell equation is explicit and the Hom groupoids are thin. Profinite induction requires open image, not bare injectivity. |
| B(a): exact manuscript definition and logarithmic comparison | B.1–B.2, B.9 | Covered. Open and closed parts, gluing functor, quotient-by-inertia formula, comparison morphism, points and cohomology are all present. |
| B(b): torsion comparison and every curve exception | B.3–B.8 | Covered in the stated smooth-curve setting. The full geometric exceptions and coefficientwise arithmetic defect are given. The requested full p-torsion counterexample has a false premise; the tame replacement has the explicit Artin–Schreier failure. |
| B(c): orientation/support formulas and trace | B.10–B.12 | Covered with exact corrections. Filled group, effective support group, coefficient restriction and the supplied orientation identification are distinguished; the trace is constructed. |
| B(d): mixed maps, torsors, operator splittings and rigidity | B.12–B.13 | Covered. Both kinds of target stratum, the torsors, comparison cells and fixed-subgroup automorphisms are explicit. Uniqueness is within an isomorphism class. |
| C(a): diagrams, pushout category and transitivity | C.1–C.4 | Covered. Both squares and the precise pushout universal property are proved; independent counterexamples delimit the generic profinite and higher homotopy interpretations. |
| C(b): the two acyclicity maps | C.5; B.3–B.8 | Covered. Local acyclicity and the global genus/boundary table are exact, including the one-cusp distinction. |
| C(c): actions, torsors, component factor and quotient | C.6–C.8 | Covered. Discrete actions are treated directly; profinite extensions/protorsors replace the nonexistent continuous regular discrete torsor. |
| C(d): exterior groups, transporter square and operators | C.9–C.12 | Covered with refutations. The compositional centralizer defect and the degree/label uniqueness defect are exhibited; transporter and operator constructions retain all comparison data. |
| D(a): central cover and independent pair | D.1–D.3 | Covered. Relative uniqueness of the Pin-plus extension is proved; unrigidified ambiguity is not hidden. The orientation and gerbe are independent in the two-type. |
| D(b): dimension three and next Postnikov stages | D.4–D.9 | Covered. Both low-dimensional routes are present; the first failure is on S4; the fourth and fifth stages retain homotopy witnesses and the loop action. |
| D(c): all four fidelity notions and sharp bounds | D.10 | Covered. The cumulative mapping-space conditions are stated and the common sharp uniform bound is dimension at most one. The S2 test disproves larger bounds. |
| D(d): arithmetic forms and Azumaya two-category | D.11–D.15 | Covered with refutation of the requested bare-gerbe classification. The replacement includes the rank-two twisted module, fppf characteristic-two construction, field image and exact automorphism loss. |
| E(a): common higher shape construction | E.1–E.2, E.5 | Covered. Shape exists without points; actual stages require the stated constancy condition, and the pro-stage is retained otherwise. |
| E(b): first stage and Postnikov comparison | E.3–E.4, E.13 | Covered. The first-stage topos is distinguished from the truncation of objects; locally contractible finite stages and the hypercompletion qualification are proved. |
| E(c): every A–C statement and finite-homotopy tests | E.6–E.15; F.43 | Covered. E.14 lists every A–C statement; the n=4 and n=5 upgrades include the extra goodness, completed fibre and finite-congruence steps. |
| F(a): six viewpoints and faithfulness of fields | F.1–F.3 | Covered. All morphisms/two-cells and forgotten data are named; finite constants survive even when the geometric group is trivial. Faithfulness holds in all characteristics. |
| F(b): scheme faithfulness, full reconstruction and curve experiment | F.4–F.7, F.37–F.38, F.44, F.46–F.47, F.49–F.50 | Covered as the requested delimitation. Relative faithfulness is proved in every characteristic, so the demanded Frobenius refutation is impossible. Positive and negative field/base ranges and the proper-curve experiment are explicit. The Q^solv test is honestly recorded as additional unresolved territory. |
| F(c): quasi-Galois characterization and profinite variant | F.8–F.10, F.21, F.24 | Covered. Finite components and accessible gluing are stated; the arbitrary-product criterion and the Cantor counterexample are proved. Finite tame representations and the (37)/(38) system are identified. |
| F(d): both gluing versions, analytic category and stacks | F.11–F.14, F.25, F.51 | Covered after the material F.51 correction. Space-level and proper étale-stack gluing are proved; the unrestricted intrinsic stack interpretation is refuted and the synchronized replacement is proved. Boolean coslices do not force thinness. |
| F(e): triple crossing, corrected corollaries and sharp depths | F.15–F.18 | Covered. The program performs fundamental-group presentation/Tietze calculations, not merely abelianized Betti ranks. Depth k+2 is proved sharp, and (247)/(254) are correctly separated. |
| F(f): tangential functor, arithmetic tube and exactness | F.19–F.23, F.39, F.48, F.51 | Covered in corrected scope. The literal §53 comparison is recovered, open strata and the transgression are explicit, and nonproper intrinsic stack tangential equivalence is now explicitly refuted. The cusp old/new comparison is supplied by the late F.23 insertion. |
| F(g): all elementary pieces, maps, Scholie and Remords | F.26–F.30; F.51 scope | Covered. The 4^I elementary pieces and all generating ambient incidences are listed; all three reconstruction routes and the first fibre obstruction are separated. Stack comparisons inherit F.13/F.51's scope. |
| F(h): §13 local stratifications | F.31–F.34 | Covered. Separatedness, failure of the sheaf property, all-degree Segal homeomorphisms, failure of axiom e alone and the controlled conical replacement are proved. Both specified tests are computed. |
| Added F(h)(1): finite sub-germs versus inertia injection | F.35 | Covered. The compact-subgroup argument proves both directions and explains open-and-closed sub-germs and descent after extending constants. |
| Added F(h)(2): punctured-completion invariance and two examples | F.40–F.42 | Covered with refutation of the proposed archimedean failure. Properness is exactly retained; both specified examples have explicit homology/shape calculations. |
| EXIT added task 1: exit category and quasi-Galois interpretation | F.8–F.10, F.21, F.24 | Covered. The Hom double cosets and flag composition are constructed geometrically and compared with the finite profinite system. |
| EXIT added task 2: three routes and comparison fibre | F.13–F.14, F.26–F.30; F.51 scope | Covered in corrected geometric scope. Full pro-topos descent, aspherical shape reconstruction and ordinary glued-topos shape are distinct; the fibre's first possible group has the required cokernel formula. |
| EXIT added task 3: all flags and finite truncations | F.15–F.18 | Covered. Full topoi use the full diagram; finite k-types use the sharp bound. The curve and higher-dimensional (254) statements include actual full topoi. |
| EXIT added task 4: arithmetic homotopy sequence and open stratum | F.21 | Covered. The profinite Chern transgression is retained; O(1), the conic and the global-inertia sufficient condition decide the left exactness question. |
| EXIT added task 5: roots and stable cusp quotient | F.22–F.23 with F23_old_kernel.tex | Covered after the late insertion. The asserted finite-root kernel equality is refuted. The original cusp has exact nonzero rank-two kernels, the stable vertical meridian is injective, and the marked projective corner is separately proved. |
| EXIT added task 6: stable towers and literal external return rows | F.39, F.45, F.48; F.44 B2 supplement | Mathematical common theorem and recovered CYCLOTOMIC rows covered. Literal FLAGGED_149 F11–F16/F25 remains unlocated and unauthenticated. This remains the direct unmet source obligation. |
| LM8 E.10 intake | F.12, F.19, F.26, F.48 | Covered. Covering germs, finite part, normal directions and the rank-r coordinate model are independently derived. |
| LM8 E.11 correction | F.12–F.14, F.48 | Covered. The annular degeneration proof is reproduced and the full neighbourhood is retained as a pro-object. |
| LM8 coherent étale-limit lead | F.36 | Covered. The exact coherent-site descent hypotheses and SGA4 theorem numbers are stated; the strict henselian punctured field gives the nondegenerate classifying topos. |

## Material corrections discovered or completed in this audit

### Nonproper analytic stacks

F.51 is a necessary mathematical correction, not an optional example. The original unrestricted sentence “the same theorem holds for analytic DM stacks by étale descent” did not justify the exchange of independent pro-germs and an infinite atlas nerve.

The roots-of-unity example gives an actual failure of the mapping-out universal property. The free variant shows that finite stabilizers alone do not repair it. The parabolic quotient [P1/Z], with g(z)=z/(1+z), gives a covering-group counterexample: its only actual invariant neighbourhood of 0 is P1, its deleted quotient is C*, while its punctured normal stack has fundamental group Z^2. The normal/operator map is the projection (a,b) -> b. All details are independently checked in F51_independent_audit.md.

The proper étale replacement uses relatively compact orbifold charts and compact arrow restrictions; it does not make the false assertion that every arbitrary atlas-neighbourhood contains an invariant one. The actual common-stage atlas diagram and the intrinsic two-open pushout remain valid for every stack.

The current corrected F.13/F.19 texts were read in full and pass this scope audit. F.18, F.26 and F.27 inherit the same restriction. F.20 remains a valid example in the explicitly broader nonproper infinite-isotropy category. The finite mu6 quotient in F.23 is unaffected.

### Original cusp kernels

The earlier F.23 proved injection in the stable quotient but only alluded to a kernel in the old resolution. The new insertion proves the three blow-up substitutions, the tail self-intersections -3 and -2, and the signed plumbing equations h=b^3 and h=a^2. Since the degree map sends b,a,h to 2,3,6, the exact kernels are Z(-3,1) and Z(-2,1), with identical completed formulas. The marked projective corner is a separate rank-two assertion, proved by the infinite puncture commutator in a free group and finite Heisenberg quotients of every order.

The executed program is work/montpellier/code/F23_cusp_certificates.py, with saved output F23_cusp_certificates.out. Its checks passed. The proof, not the finite samples, establishes the profinite kernel statements.

### Supplied three-puncture and bounded-resolution comparisons

The actual LM3b H.6–H.8 source was read. H.7's cochain calculation is correct in its filtered finite-quotient sense. The degree-one map is (s,t) -> (s,t,-s-t), with cokernel A, and the degree-zero map has diagonal kernel A. Peripheral retractions supply the full induced profinite topology. The orientation class agrees with the sphere class. No one finite stage works uniformly for every finite coefficient group, as a prime not dividing its finite open-group order immediately shows.

CATHOT D.1 was read at its actual bounded representability statement and proof. Its contractible diagram objects are not the punctured local terms of the mixed topos. The latter have nontrivial local fundamental groups; the distinction between BH_s and its effective-image BK_s is precisely the defect already calculated in B.3. The requested explicit comparison is now written in B_background_audit.tex.

## Register, source and packaging checks

The final assembled paper has 129 distinct numbered statements and the results file has exactly the same 129 identifiers: 94 Proved, 29 Refuted, 4 Known and 2 Open. There are no missing or extra rows. The 89 reading rows have the requested five-column schema. All 61 bibliography entries carry verification wording, and every citation key used by the sections is present in the bibliography. The final 124-page build log has zero overfull, undefined-reference/citation, or missing-character flags. These counts supersede the initial 128-statement snapshot.

The root report initially still had the checkpoint05 “in progress” placeholders for every F/EXIT/LM8 row. The replacement report has now been read: its 48-row opening table includes all requested items and explicitly records both Open entries. This bookkeeping gap is closed.

The following concrete source edits were communicated to their owners:

- The two F.46 references to the literal display (F44) became incorrect after that display was reassigned to Q^solv. Both have been corrected in F44_point_map.tex to refer to the cyclotomic field and the intermediate-field question directly.
- Scan52 of cote149 is folio25v in the directly inspected sequence: scan51 is folio25, scan53 is folio26. The final F.4–F.7 and F.37–F.38 rows now use the same section2/folio25v coordinates as F.44/F.46/F.47/F.49/F.50. Montpellier also normalized the supplementary manuscript-context rows.
- The report's phrase “technical two-faithfulness assertion at scan250” should read “technical 0-faithfulness assertion.” D.15 distinguishes that literal notion from ordinary nonfaithfulness.
- The early 118-page build log had unresolved citations for the newly added Mochizuki solvably-closed, Jarden and Haran–Jarden entries, although all three keys were already present in the bibliography. The final 124-page build has cleared these warnings.
- Mathematical program outputs exist for the finite counterexamples and computations inspected here, including the actual fundamental-group/Tietze calculation of the triple crossing. The final integration includes the F.23 and F.51 statements and the B background insertion; their source programs and outputs accompany the respective author bundles.

The four Known rows, B.5, D.1, F.7 and F.38, are accompanied by explicit reductions and hypotheses, not mere references. Part D's complete manuscript loci and verified bibliography annotations had already been separately audited. The latest independent foundations audit of D.6–D.9 also passed and is saved in work/foundations/D6_D9_independent_audit.md.

## Completion state

No further unmentioned lettered or added mathematical task was found after incorporating the F.23 and F.51 corrections. This is not a claim that every original manuscript assertion is true, that all intermediate fields are classified, or that the missing FLAGGED source has been verified. The return must continue to distinguish its proved field ranges, the extra residual field test, and the genuinely unfinished literal source audit.

The integrated mathematical coverage and final metadata checks are complete at this freeze point. The root retains final visual verification and packaging, the two registered Open entries remain explicit, and the direct source obligation F.45 is acknowledged. Apart from the report's cosmetic 0-faithfulness wording noted above, no uncommunicated correction remains. This audit does not open new optional mathematical investigations.
