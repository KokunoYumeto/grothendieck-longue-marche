# Topology research support: scans 145–153

Prepared 2026-11-18 by GPT-6 Astra Pro, topology_research; effort setting inherited and not exposed. This is research support for the root editor, not another transcription. No scan image was opened, no frozen transcription was altered, and no claim of independent handwriting verification is made. Page locators below are scan numbers; `TeX l.` identifies exact lines in the frozen per-page source, not inferred handwritten line numbers.

## Context and status discipline

The supplied `context/README.md` is preliminary. Its claim that the ZIP contains only a README is superseded by the additions dated 17 November; the actual accompanying files include `notes/RESULTS_STATE.md` and Hua's modernised reading. `context/hua_project/README.md` explicitly describes the latter as an AI-produced interpretation, not a transcription or our result.

The following register entries are used only as contextual statements, without attempting their proofs: **EXIT_TOWER E.T3** and **IMPL P3** are open; **LM4 C.12** and **LM4_SUCCESSOR D.9** are open; **WG2 B15 (§1.2)** and **WG2 B13 (§1.2)** are unchecked planning items; **EXIT_ONE_TYPE P1d1** and **P4e** are marked Proved by their return, and the same state file reports a review of the EXIT_ONE_TYPE return with no wrong statements found, but supplies neither the proofs nor detailed referee coverage. **BISITE G.10** is marked Proved by its return, with no referee verification stated here. No state entry is upgraded by this research support.

All proposed items were searched in the two context texts; exact search terms and line hits are in `topology_context_search.tsv`. The supplied Hua file uses page numbers one less than our scan numbers in these passages.

## Candidate note items

### T01 — 119, scan 146, theorem, TeX ll. 5–20 — unproved claim

The paired comparison arrows assert an equivalence after describing a two-category whose Hom categories are “discrètes”; proving this requires the functors on arrows and the elimination of nontrivial 2-morphisms, not just a representation of quotient objects. **Context:** Hua, modernised reading of cote 119, “L'énoncé” (`119.modern.tex` ll. 252–316), restates the proposed equivalence without proving it; this bears on **Hua finding 119-foliation-quotient-topos-equivalence** and only indirectly on the open **EXIT_TOWER E.T3** (cote 143, scans 29–31). Kock–Moerdijk's Theorem 7.1 presents every étendue by a locally simply connected local equivalence relation on a locale, but does not by its statement alone identify the exact two categories written here [P1].

### T02 — 119, scan 146, fibre conditions, TeX ll. 14–17 — reading question

The frozen transcription reads “à fibres locᵗ connexes et connexes,” including the second connectedness condition, whereas Hua's “L'énoncé” (ll. 269–275) treats a third condition as unreadable. This adds a concrete condition to **Hua finding 119-foliation-quotient-topos-equivalence**, but does not turn it into the local simple-connectivity hypothesis of Kock–Moerdijk. The precise meaning of “mult. top.” and of these fibre conditions remains necessary before using the note to model the open modular-topos comparison **EXIT_TOWER E.T3**.

### T03 — 119, scan 145, quotient and holonomy margin, TeX ll. 6–16 — reading question

The word “holonomie” does not by itself identify the proposed quotient with the holonomy classifying topos. **Context:** Hua's opening summary (ll. 86–89) makes that identification, while its later footnote in “L'énoncé” (ll. 296–303) acknowledges the distinction between holonomy and invariant-sheaf monodromy; the latter caution is supported by the primary 1996 Kock–Moerdijk abstract [P2]. Thus the pages support a quotient-topos programme but do not settle which groupoid is intended, bearing on **Hua finding 119-foliation-quotient-topos-equivalence** rather than solving **EXIT_TOWER E.T3**.

### T04 — 119, scans 145–146, theorem and date — unpursued implication

The “Mars 1986” date makes the relationship to the pre-existing SGA 4 exercise and the later étendue presentation theorem a precise historical question, with no priority conclusion warranted. **Context:** the finding-level **119-foliation-quotient-topos-equivalence** in `RESULTS_STATE.md` l. 498 still reports that a search found no reference, but Hua's own revised preamble (ll. 46–54) and “L'énoncé” (ll. 280–303) already cite partial antecedents and later results. This is an internal difference between the supplied context layers, not a claim that the complete equivalence has been found in the literature; SGA 4 itself was not rechecked in this subtask.

### T05 — 119, scan 146, final question, TeX ll. 24–30 — reading question

The frozen question is “Quelles propriétés obtient-on avec des feuilletages ???,” whereas Hua's conclusion to “L'énoncé” (ll. 317–323) asks which varieties or multiplicities occur as quotients. This changes the apparent research target from a realization problem to properties obtained from foliations, and the real/complex analytic regularity variants on the page should be retained in either investigation. It bears on **Hua finding 119-foliation-quotient-topos-equivalence**; no result-state entry supplied here answers the literal properties question.

### T06 — 119, scan 148, collar map, TeX ll. 16–18 — reading question

The frozen reading is a left-pointing isomorphism `C ← B×I` labelled φ and then `dot C=φ(B×{1})`, so that displayed image formula is type-correct with this arrow direction. **Context:** Hua, “I. Colliers” (ll. 351–360), chooses the opposite direction and then supplies an inverse to repair the image formula; that repair is not required by this frozen reading. The difference is local to the collar definition and has no direct settled-results ID; **WG2 B13 (§1.2)** is a related but unchecked neighbourhood-comparison lead.

### T07 — 119, scan 148, subtitle and strictness line, TeX ll. 6–9, 46 — reading question

Two differences from Hua's addendum introduction and “I. Colliers” (ll. 327–333, 357–362) require collation: the frozen text keeps underlined “quelconque” live with “modéré/modérée” inserted, and reads `dot C` as bordant in `(C minus dot C)`. The latter cannot literally be an inclusion of that boundary in the displayed ambient complement, whereas scan 149 gives the different, coherent exterior `X minus (C minus dot C)`; the manuscript is frozen, so neither the exterior nor a deletion of “quelconque” has been imported. **Context:** this refines Hua's interpretation; **WG2 B13 (§1.2)** remains an unchecked related lead, not a solution to the reading problem.

### T08 — 119, scan 148, Conj. a–b, TeX ll. 49–53 — conjecture

“Existe Collier” and contractibility of the space of strict collars are separate assertions, and “bordant” needs an intrinsic definition before either can be tested outside manifolds. **Context:** Hua, “I. Colliers” (ll. 345–378), invokes the manifold collar theorem; Brown's Theorem 2 indeed proves existence of collars for manifold boundaries [P3], which is a conditional special case rather than a proof of the full moderate-space statement. This bears on the neighbourhood programme **WG2 B13 (§1.2)** but adds a choice-space requirement beyond its coarse boundary data.

### T09 — 119, scan 148, Conj. c, TeX ll. 55–60 — conjecture

The phrase “induisant l'identité de B (et ‘libres’ sur dot C)” makes the allowable automorphism group decisive: for a closed manifold B, unrestricted smooth product automorphisms with the lower end fixed are pseudo-isotopies. **Context:** Hua, “I. Colliers” (ll. 377–396), raises this obstruction; Hatcher–Wagoner's introduction defines the smooth group and notes the comparison of PL and smooth component sets [P4], but this check does not identify Grothendieck's unspecified moderate automorphisms or topology with either one. The result is a conditional obstruction test, not an unconditional refutation, and is methodologically related to the open deformation-topology issues **LM4 C.12** and **LM4_SUCCESSOR D.9**, not a solution to them.

### T10 — 119, scan 148, possible refinement of Conj. c — own idea

**Confidence high for the stated restricted model:** if the allowed maps preserve the projection to a compact base B and are increasing homeomorphisms on each interval fibre, the formula `(b,u) ↦ (b,(1−t)h_b(u)+tu)` contracts the group to the identity because convex combinations with the identity remain strictly increasing and fix both endpoints. This directly checks the restricted repair suggested by Hua, “I. Colliers” (ll. 389–394), while the page itself does not impose that restriction. It leaves the unrestricted choice-space problem and the open **LM4_SUCCESSOR D.9** unchanged.

### T11 — 119, scan 149, Conj. c and “Alexandroff ?”, TeX ll. 23–27 — self-flagged

The parenthetical “Alexandroff ?” flags both a possible reference and the contractibility step. **Context:** Hua, “II. Cônes autour d'un point” (ll. 423–440), identifies Alexander's radial contraction; for the compact cone model the construction and continuity were checked directly below, supporting that conditional case without deciding the whole unspecified moderate category. The primary bibliographic reference is Alexander's 1923 paper [P5], and the general parameter-topology caution is adjacent to open **LM4_SUCCESSOR D.9** rather than an application of it.

### T12 — 119, scan 149, Conj. a–b, TeX ll. 19–21 — conjecture

Existence of one cone and contractibility of the space of strict cones must remain separate: a local conical model does not itself compare all embedded choices parametrically. **Context:** Hua, “II. Cônes autour d'un point” (ll. 423–440), discusses local conic structure and a contraction for automorphisms of a fixed cone, but the latter is not the varying-cone statement in b). This is the same distinction between a geometric presentation and coherent choice data that matters to **EXIT_ONE_TYPE P1d1** (cote 147, scans 179–180; return marked Proved and generally reviewed), whose result is carried as background rather than rederived.

### T13 — 119, scan 150, α and β, TeX ll. 13–31 — unproved claim

The two displayed natural transformations and the NB “Pour définir α et β” ask for coherence of the forgetful-and-gluing comparison, not merely equivalence of object sets. **Context:** Hua, “III. Le système des onze équivalences” (ll. 447–503), explicitly omits the two 2-arrows from its reconstructed diagram, while the frozen transcription records them and the written, unresolved `PBR`. This adds a specific coherence problem to the contextual analogy with **EXIT_ONE_TYPE P1d1**; it neither proves the eleven/fourteen count nor establishes the tower-finality proposal **IMPL P3**.

### T14 — 119, scan 150, multipairs, TeX ll. 33–57 — own idea

**Confidence medium:** the phrase “I un ensemble fini variable” suggests testing whether the six-category comparison is natural under relabelling and under varying marked components, rather than proving a separate statement for each fixed I; those compatibility maps are necessary for later gluing constructions. **Context:** Hua, “III. Le système des onze équivalences” (ll. 498–503), restates the multipointed variant without supplying those maps, while **IMPL P3** asks an open finality question for the Teichmüller tower and **EXIT_TOWER E.35** claims recovery from a labelled sewing system. This is a structural link, not evidence that scan 150 states the two-level principle or proves the cited tower claims.

### T15 — 119, scan 151, sublevel construction, TeX ll. 11–19 — unproved claim

“ε petit [et admissible]” leaves the admissibility, properness and comparison range to be specified before `f⁻¹([0,ε])` is a controlled tubular neighbourhood. **Context:** Hua, “IV. Voisinages tubulaires” (ll. 514–525), identifies the rug-function method; Durfee's primary abstract confirms its algebraic and semialgebraic level-set setting [P6], but the full isotopy-independence theorem was not reread here. The page adds an explicit choice of geometric function to **WG2 B13 (§1.2)** and should not be used to upgrade that unchecked planning item.

### T16 — 119, scans 148, 151, scope of moderate spaces — reading question

The frozen paragraphs do not state the global compactness convention or the opening “Y fermée” that Hua supplies in its notation preamble and “IV. Voisinages tubulaires” (ll. 20–25, 507–508). A continuous real-valued f with zero set Y would imply closedness in the construction, but the definition through `X/Y` precedes that construction, so scope should be separated from a convenient model. This adds a hypotheses question beside **WG2 B13 (§1.2)** and the noncompact caution in open **LM4_SUCCESSOR D.9**; it does not change the frozen wording.

### T17 — 119, scan 151, gluing diagram, TeX ll. 31–42 — reading question

The displayed outer complement retains a doubtful first `dot V/V`, while Hua, “IV. Voisinages tubulaires” (ll. 532–543), explicitly replaces the expression by the exterior of V with its boundary retained. That corrected expression yields the mapping-cylinder model, but the correction belongs to interpretation, and the two readings must remain distinguishable when citing the page. The actual link map φ is additional data of the kind retained by **EXIT_ONE_TYPE P1d1** and missing in the coarse-maquette limitation **EXIT_ONE_TYPE P4e** (cote 149, scan 133; both return claims with the review qualification above).

### T18 — 119, scan 151, a–b, TeX ll. 44–49 — unproved claim

“Rigidification Y-admissible existe” and “La classe d'homotopie ... bien déterminée” require comparison maps when the boundary dot V varies; existence of a deformation retract for one chosen V does not alone identify these varying-domain homotopy classes. **Context:** Hua, “IV. Voisinages tubulaires” (ll. 545–562), offers a triangulated mapping-cylinder argument for existence and a fixed-V retraction argument for homotopy uniqueness, so the precise comparison between choices remains to be made. The new issue is geometric choice coherence, not a reproof of **EXIT_ONE_TYPE P1d1**.

### T19 — 119, scan 152, equisingular case, TeX ll. 5–19 — conjecture

“Je présume” attaches to both choosing φ fibrant and obtaining an equivalence of infinity-isotopic categories, while Hua's “V. Le cas équisingulier...” (ll. 566–590) interprets fibrant as locally trivial. Mather's first isotopy lemma has explicit properness and stratified-submersion hypotheses [P7], and Ayala–Francis–Tanaka supply an unzip/link reconstruction under proper constructible embedding and conical-smoothness hypotheses [P8]; neither statement alone defines the manuscript's “équi-singulier.” The pages therefore give a geometric antecedent and a comparison problem for **EXIT_ONE_TYPE P1d1**, not an unconditional proof of it.

### T20 — 119, scan 152, regularity margin, TeX ll. 27–29 — self-flagged

The margin explicitly says “Je présume que X\Y régulier implique que Y régulier,” with the additional closure proviso, whereas Hua's discussion at ll. 589–590 records only a partially unread margin. If stripped of the surrounding equisingularity requirement, the implication fails for the union Y of the coordinate axes in X=R²: X\Y is a 2-manifold and Y lies in its closure, but Y has four local branches at the origin. This is a checked counterexample to the unqualified implication, not to an undefined equisingular version; **EXIT_ONE_TYPE P1d1** already stresses stratified link data rather than complement regularity alone.

### T21 — 119, scan 152, dimension proposal, TeX ll. 31–38 — self-flagged

“Il faudrait arriver à imposer des conditions suppl.” and “Peut être qque chose du genre suivant” explicitly leave the condition `dim φ⁻¹(y)=c(y)−1` provisional. **Context:** Hua, “V. Le cas équisingulier...” (ll. 592–608), restates it, while **EXIT_ONE_TYPE P4e** already claims that coarse boundary data do not determine links (cote 149, scan 133); these pages add a proposed dimension filter, not missing link homotopy or monodromy data. A proof of essential uniqueness would need to specify allowed maps and controlled variation, so equal fibre dimension should not be silently promoted to a classification theorem.

### T22 — 119, scan 153, general pairs, TeX ll. 5–11 — reading question

The frozen text reads doubtful “On peut rien/bien trouver” and inserted “quelconques,” whereas Hua's “V. Le cas équisingulier...” (ll. 602–608) paraphrases a dream and reports the qualifier as an uncertain “emplies.” The actual request appears to be a category of arbitrary pairs described through a boundary map subject to conditions reflecting the preceding dimension requirement. It adds scope to the analogy with **EXIT_ONE_TYPE P1d1** but supplies no proof that the class of pairs falls within that return's reconstruction hypotheses.

### T23 — 119, scan 153, filtration revision, TeX ll. 24–30 — withdrawn in the same text

On this same scan the proposed canonical filtration changes from cancelled “plus” to inserted “moins” fine, and the relative paragraph also cancels “plus fine”; the change concerns the extremal or compatibility property, not merely style. **Context:** Hua's short “Filtrations” discussion (ll. 610–618) does not preserve the precise revision or fully resolve the relative version. This adds a concrete order-of-filtrations problem to **WG2 B15 (§1.2)** and **BISITE G.10** (the latter a return-claimed finite-poset dictionary), without rederiving either contextual statement.

### T24 — 119, scan 153, invariance conclusion, TeX ll. 30–33 — own idea

**Confidence high for this category warning:** the semialgebraic homeomorphism `t ↦ (t²,t³)` from R to the cusp shows why an embedded smooth Whitney stratification is not automatically invariant under all moderate homeomorphisms: the cusp needs its origin separated as a zero-dimensional smooth stratum, whereas the line does not. **Context:** Hua, “Filtrations” (ll. 614–618), invokes minimal Whitney and intrinsic topological stratifications as positive analogies, but they answer different notions of regularity. Thus scan 153's “invariants de la structure modérée” calls for an intrinsic regularity definition or a narrower isomorphism category; **WG2 B15 (§1.2)** remains a related unchecked bridge, not a resolution.

## Direct targeted checks performed

### TC1 — Projection-preserving interval automorphisms

Let B be compact Hausdorff and h(b,u)=(b,h_b(u)) a homeomorphism of B×[0,1], fixing both ends, with each h_b increasing. Set H_t(h)(b,u)=(b,(1−t)h_b(u)+tu). The fibre maps remain continuous strictly increasing surjections with fixed endpoints; the product map is a continuous bijection from a compact space to a Hausdorff space and hence a homeomorphism. The formula is jointly continuous in (t,h) in the compact-open topology; it preserves the identity, starts at h and ends at identity. In a semialgebraic model the formula preserves definability for any given definable parameter family. This proves only the restricted model in T10, not the manuscript's full automorphism assertion.

### TC2 — Compact-cone contraction

Let Y be compact metrizable, C(Y) its closed cone with radius r∈[0,1], and G the group of homeomorphisms fixing both the base Y and the apex. For 0<t≤1 let δ_t identify C(Y) with r≤t and define H_t(h)=δ_t h δ_t⁻¹ on that smaller cone and the identity for r≥t; set H_0(h)=identity. The definitions agree on r=t since h fixes Y, inverses use the same formula with h⁻¹, and the apex remains fixed. A compatible cone metric has the diameter of r≤t tending to zero, giving a bound independent of h at t=0, while ordinary compact-open continuity gives joint continuity for t>0; hence this is a strong contraction with H_1(h)=h. In a linear semialgebraic cone, the formula also preserves definability of a given definable family. This checks the compact-cone case invoked by Hua; it does not prove existence/contractibility of *embedded cone choices*, the choice of mapping-space topology for all moderate objects, or any noncompact generalization.

### TC3 — Failure of unqualified complement-regularity implication

For X=R² and Y={xy=0}, X\Y is the disjoint union of four open quadrants, so is a 2-manifold. The complement is dense, so Y⊂closure(X\Y). Every sufficiently small punctured neighbourhood of the origin in Y has four connected components, whereas an interior point of a 1-manifold has two, so Y is not regular there in the manifold sense. The pair is not equisingular along Y, because the local branch pattern changes at the origin; that is precisely why the example refutes only the condition with equisingularity omitted.

### TC4 — Cusp versus line and the category of regular strata

The map R→C={(x,y):y²=x³}, t↦(t²,t³), is a continuous semialgebraic bijection with continuous inverse t=y/x away from the origin and inverse 0 at the origin. If C were a C¹ embedded one-manifold near the origin, its limiting tangent would be the x-axis, so projection onto x would be a local coordinate and therefore injective; but (t²,t³) and (t²,−t³) have the same x for arbitrarily small nonzero t. Thus the origin is not part of a one-dimensional embedded C¹ stratum through the cusp, while R itself is smooth; the distinction disappears for intrinsic topological manifold regularity.

## Primary bibliography and precise verification limits

- **P1.** A. Kock and I. Moerdijk, *Every étendue comes from a local equivalence relation*, Journal of Pure and Applied Algebra 82 (1992), 155–174, §6 and Theorem 7.1. Author-hosted full text: https://tildeweb.au.dk/au76680/EECER.pdf . Checked the introduction, local-kernel construction and theorem statement; not a complete independent reproof.
- **P2.** A. Kock and I. Moerdijk, *Spaces with local equivalence relations, and their monodromy*, Topology and its Applications 72 (1996), 47–78, https://doi.org/10.1016/0166-8641(95)00101-8 . Checked the publisher abstract, specifically the monodromy/holonomy distinction; full paper retrieval was blocked by HTTP 403.
- **P3.** M. Brown, *Locally Flat Imbeddings of Topological Manifolds*, Annals of Mathematics 75 (1962), 331–341, Theorem 2, p. 339. Primary article mirror: https://www.maths.gla.ac.uk/~mpowell/Brown%20collars.pdf . Checked the exact boundary-collar theorem statement.
- **P4.** A. E. Hatcher and J. B. Wagoner, *Pseudo-isotopies of compact manifolds*, Astérisque 6 (1973), introduction and summary, https://numdam.org/item/AST_1973__6__1_0.pdf . Checked the smooth pseudo-isotopy definition and the introduction's explicit PL/smooth component comparison; did not recompute the K-theoretic obstructions or infer a theorem for unspecified moderate automorphisms.
- **P5.** J. W. Alexander, *On the Deformation of an n Cell*, Proceedings of the National Academy of Sciences 9 (1923), 406–407, https://doi.org/10.1073/pnas.9.12.406 ; primary article record https://pmc.ncbi.nlm.nih.gov/articles/PMC1085470/ . Bibliographic identity checked; the compact-cone extension is verified directly in TC2.
- **P6.** A. H. Durfee, *Neighborhoods of Algebraic Sets*, Transactions of the American Mathematical Society 276 (1983), 517–530, https://www.jstor.org/stable/1999065 . Checked the primary abstract's algebraic/semialgebraic level-set scope; attempted AMS full-PDF retrieval failed, so no full proof verification is claimed.
- **P7.** J. Mather, *Notes on Topological Stability*, §11, Proposition 11.1 (first isotopy lemma), primary notes mirror https://webhomes.maths.ed.ac.uk/~v1ranick/surgery/mather.pdf . Checked properness, Whitney stratification and stratumwise submersion hypotheses, and the §8 control-data definition; no complete independent reproof.
- **P8.** D. Ayala, J. Francis and H. L. Tanaka, *Local structures on stratified spaces*, author-hosted version https://math.montana.edu/dayala/documents/AFT1.pdf , §7.3, especially Corollary 7.3.7 and Proposition 7.3.10. Checked the unzip/link pushout and its proper constructible/conical-smooth setting; the published paper is Advances in Mathematics 307 (2017), 903–1028, as confirmed on the author's publication page, https://www.math.montana.edu/dayala/index.html . No equivalence with Grothendieck's undefined category is asserted.

## Check-event integration

`topology_check_events.tsv` contains conservative candidate events. Most contextual and literature uses are **carried as background without fault found**, not theorem verification. Four explicit arguments TC1–TC4 were checked in this subtask; TC3 and TC4 refute only the precisely qualified stronger inferences, never the full unspecified manuscript programme. Root should replace Txx/TCx by final note IDs when integrating the final `CHECK_EVENTS.tsv`.


### TC5 — One-leaf circle diagnostic (follow-up check)

For E=F=S¹ with the one-leaf foliation and the identity map to F, the bracketed leafwise-homeomorphism condition in the frozen scan 145 is satisfied. Every transversal is a point, so all holonomy germs are trivial and the holonomy groupoid is the pair groupoid; the monodromy groupoid retains homotopy classes of paths and has isotropy π₁(S¹)=Z. The standard transitive-groupoid comparison gives equivariant-sheaf topoi Set and Set^Z respectively. This is the targeted proof check recorded under N06, not a claim to identify the intended quotient or to re-prove the Kock–Moerdijk theorem; the follow-up scope review was by topology_research, 2026-11-18 02:04:06 UTC.
