# LM3_TEICHMULLER_TOWER — research and verification report

**AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed.**  
**Research cutoff:** 11 November 2026.

## Deliverable and status register

This package develops Parts A–F of the attached prompt. The paper contains **110 numbered assertions: 57 Proved, 30 Known, 11 Refuted, and 12 Open**. The bibliography has **53 distinct entries**, each explicitly marked verified or unverified; in the present package every cited source was opened. The reading register contains **42 records** of mathematical or contextual evidence bearing on the manuscript. An opened source is not thereby an independently certified proof.

The paper's principal result is a distinction, followed through all the constructions: the arithmetic-image quotient introduced in §29 is identified with G_Q for every hyperbolic type, while the earlier normalizer quotient is a different group. Its genus-zero comparison leads to GT_0 at the isolated tripod and to GT at the subsequent levels. The conjecture G_Q=GT remains separate.

The categorical part constructs an actual pro-object of finite categories, proves cofinality of the transporter quotients, compares its finite representations with finite boundary-constructible sheaves with their stalks, and computes the decorated genus-zero tower automorphism group using the exact Harbater–Schneps theorem. The positive-genus construction retains stack isotropy. The remaining higher-completion and elliptic automorphism comparisons are stated explicitly, with the point where the argument stops.

## How to read the status labels

| Label | Meaning |
|---|---|
| Proved | The exact assertion is proved in this paper. If it is a conditional implication, its antecedent is stated explicitly and is not certified by that label. |
| Known | The exact imported theorem is supplied with an opened primary source, theorem number and checked scope. We do not claim to have reconstructed every historical proof. |
| Refuted | A complete counterexample is given. Computable finite components are checked by attached programs. An invalid proof alone is never labelled a refutation. |
| Open | Either an established open mathematical problem, a new unrefereed claim not fully certified in this audit, or an exact comparison left unresolved here. The statement and notes distinguish these meanings. |

The established open problems include the high-genus congruence question B.3 and the profinite arithmetic equality E.8. The audit-unresolved comparisons are B.7, B.14, C.8, D.23, E.14, F.16 and F.18. D.7, D.13 and E.26 record the three supplied 2026 claim families and the exact limits of their verification. None is removed from the register after proving a special case.

## Main corrections to the supplied leads

- **Lead1:** The Russian result is contextually Belyi's theorem, and it supplies faithfulness. But the revised arithmetic-image quotient has surjectivity by definition. The earlier normalizer problem is the GT-like realization problem; the two cannot be substituted for one another.
- **Lead2:** The relative Hom theorem has the stated sub-p-adic hypotheses and geometric-inner ambiguity. The literal maximal-open-normalizer criterion for cusp groups is false; the correct theorem includes the cyclotomic conjugation condition. The absolute open-Hom deduction is conditional only at the specified base-field reconstruction step.
- **Lead3:** Faithfulness holds for affine and proper hyperbolic curves over the specified fields. Hoshi–Mochizuki Corollary6.4 supplies the stronger faithfulness modulo the orientation-preserving geometric monodromy image, resolving the manuscript's “peut-être ... faux” question positively in that formulation.
- **Lead4:** CSP, normality of the geometric image, and properness of that image in all loop-preserving outer automorphisms are distinct assertions. The older attached genus-two paper does not prove the closed case; the later theorem does. The exceptional nonhyperbolic types are treated explicitly.
- **Lead5:** Both full and procongruence Birman sequences have exact positive forms. The arithmetic-image filling sequence is proved. The unrestricted ambient outer-automorphism row marked “??” is a stronger lifting statement, not automatically a corollary of those exact sequences or of configuration-space cuspidalization.
- **Full étale topos:** Killing peripheral inertia reconstructs a fundamental-group quotient and its covering theory, not the whole small étale topos. The correct reconstruction first uses arithmetic anabelian Isom to recover the open curve, then its proper model and an explicit basis for the full étale site.
- **Companion packages:** We retain the actual transitions and the distinction between natural isomorphisms and arbitrary natural transformations. We do not refute GALOIS F.4's qualified split-representation statement. We use Jansen and BGH directly for the categorical and geometric comparisons rather than treat the companion review as authority.

## The 2026 proof packs

The full main texts of families019 and031 and §§2–5 of008 were examined, with the external primary inputs used in our deductions checked individually. Conditional deductions are written out. The remaining new technical arguments are identified in the detailed audits below.

The supplied Lean comparator for008 ends with a placeholder and is not itself a checked proof. The current search also found Willwacher's subsequent October2026 proof treatment, which was opened. We report that development and its verification scope. We do not infer that an unrefereed statement is false, nor that a subsequently published preprint has been fully checked merely because its principal theorem agrees with the claim.

The rational implications distinguish GRT_1 from G_m⋉GRT_1, pro-l realizations from full profinite groups, and Zariski density from topological density. The all-weight rational bound would not establish exhaustion of every finite quotient of GT, which is the actual profinite requirement.

## Input and search record

Only the files supplied in this conversation and primary public mathematical sources were used. The original ZIP was extracted without modifying it. Primary paper PDFs were converted to text for search; scanned pages were rendered or inspected where extraction was insufficient. The individual reports specify their inspected scan numbers, exact theorem locations and version discrepancies.

Current searches covered the named authors and titles in the prompt, the full/procongruence distinction, genus-two congruence, normalizers and inertia, relative and absolute Hom, cuspidalization and sections, automorphisms at the five requested types, the recent tower papers and the October2026 Deligne–Drinfeld literature. We make no novelty claim based on a negative search.

## Reproducibility and build

The results and reading CSVs are generated from the audit fragments and checked against every numbered statement in the TeX sections. Citation aliases are normalized before the bibliography is built; the validation checks every cited key and every status. The finite programs were rerun successfully. Their limits are part of their output and the paper.

**Build status: PASS.** LuaHBTeX 1.18.0 and BibTeX; final stable build has no warnings, undefined citations or references, missing characters, or overfull/underfull boxes. The delivered PDF matches all 110 registered statement identifiers and status labels.

PDF pages: 76. All computation programs passed: True. Missing citation keys: 0. Undefined references: 0. Overfull boxes: 0.

All 76 final pages were rendered at 90 dpi and inspected in seven contact sheets. Pages 1, 9, 24, 32, 50, 53, 61, 65, 69 and 75 were additionally inspected at full rendered size. The notation tables, long equations, categorical formulas, proof-audit tables and bibliography showed no clipping, overlap or missing glyphs. An independent text-bounds check found no blocks outside the page safety margins.

---

## Detailed audit: Parts A and F




# Parts A and F: construction and verification report

## Scope and interpretation

Part A fixes the conventions that determine every later comparison. The manuscript's homeomorphism group preserves the puncture set; it is not pure and does not impose orientation. We separate the permutation and orientation characters, the discrete mapping class group, its abstract profinite completion, and its geometric image in continuous outer automorphisms. The modular object in §26 retains isotropy and unordered punctures. In particular the labelled three-point moduli object is Spec Q, whereas the unordered stack is B S3. This distinction matters in the computation of the early normalizer quotient.

The definitions of N and its quotient change in §29. We use separate superscripts for the full normalizer and the arithmetic image. This resolves a central ambiguity in the prompt: surjectivity from G_Q to the revised image quotient is definitional, whereas surjectivity onto the independently defined GT-like normalizer quotient is additional mathematics. A.9 proves the comparison maps and A.10 proves the torsor assertion without assuming normality in the whole ambient automorphism group.

The covering operation is a correspondence involving the stabilizer of the covering subgroup and a chosen lift. It is not a canonical homomorphism of all outer automorphism groups. A.4 retains deck ambiguity. The filling operation on the surface group is different from the Birman map on mapping class groups. A.3 and Part C distinguish them.

A.13 writes out the universal-lift construction of §21. The kernel over the discrete mapping class group is a direct product A^circ×Π in the specified pullback, so this gives mathematical evidence for the doubtful multiplication symbol. We explicitly use a universal principal A-space, for example Milnor EA, for the homotopy-quotient argument. An arbitrary contractible free topological A-space without a principal-bundle hypothesis would not justify that argument.

## Corrections in exceptional types

The type (0,2) exposes two distinct signs. Inversion z↦1/z exchanges the punctures and preserves orientation; conjugation z↦bar(z) fixes the punctures and reverses orientation. Both induce -1 on the fundamental group Z. Thus rho_pi=rho_permutation·epsilon. The literal identification of these two rho maps on scan225 is false, and so is the rank-one determinant-one assertion on scan227. The table in A.11 is the corrected statement, retaining the independent orientation datum. The torus determinant-one statement remains valid.

The fundamental groups of (0,3) and (1,1) are both free of rank two, but their peripheral structures are different. The once-marked torus and unmarked torus have the same mapping class group SL2(Z); forgetting the mark does not have an injected Z² point-push kernel. Real and nonorientable cases are described separately, and finite elliptic isotropy is retained at primes2 and3.

## The profinite category constructed in Part F

We take Jansen's category with its actual transporter composition. Its arrows smooth nodes; the opposite category has arrows of degeneration. We use a finite skeleton indexed by stable labelled trees. This is an equivalence of categories, not groupoid completion.

F.2 defines a strict pro-object using all finite objectwise composition congruences. Its transition functors keep the objects and are surjective on Hom sets. The inverse-limit category in profinite sets is proved equivalent to this pro-object at the level of continuous functors and natural isomorphisms. The finite-object hypothesis and actual transitions are used in the proof.

F.3 supplies a finite counterexample to inverting arbitrary natural transformations: [1] and a point become indistinguishable under that operation, although their set-valued representation topoi have respectively three and two subobjects of the terminal object. The category and its noninvertible arrows therefore cannot be replaced by its fundamental groupoid. This respects the CATHOT warning rather than treating it as a substitute for the exit category.

F.4 distinguishes finite representations, arbitrary representations factoring through one finite stage, and all continuous discrete actions. The continuous action of Zhat on the disjoint union of Z/m!Z for all m has no common finite quotient. The attached GALOIS F.4 is not refuted: Hoyois explicitly calls the finite-stage objects split and distinguishes them from the classifying topos.

The main completion argument is F.5–F.7. Boggi's profinite curve complex is taken from its actual definitions, with closures of curves and multicurves in the profinite surface group. We use the stabilizer theorem and multitwist normalizer theorem in the procongruence group, and only then use genus-zero CSP to identify the full completion. F.6 proves that a discrete stabilizer inherits its full profinite topology by comparing the cutting extension before and after completion. This is stronger than residual finiteness.

For a finite-index normal V in G_n, the finite quotient category has the same stable-tree objects and Hom sets given by the finite images of the transporters modulo the finite images of their source multitwist groups. F.7 proves these quotients are cofinal among all finite functors. In genus zero a nonempty transporter is one stabilizer coset, because labels identify the relevant source submulticurve uniquely. A finite functor is therefore controlled by finitely many restrictions to stratum automorphism groups; the full induced stabilizer topology supplies one ambient V killing their kernels. This proves the proposed transporter completion, not just a candidate formula.

Forgetting, clutching and relabelling extend using actual finite congruences and their pullbacks. Relabelling is retained as a coherent pseudo-action. No splitting of a symmetric-group extension is introduced.

## Geometric comparison and Galois action

BGH's stratified Riemann existence theorem, applied with Jansen's exit calculation, gives the finite constructible-sheaf comparison. We retain the stalk/evaluation functors. Covariant finite representables recover each finite Hom set; inverse limits recover the profinite Hom sets. Thus the finite-set exodromy object is the category we constructed.

We distinguish this result from the full stratified infinity-categorical profinite completion. BGH identifies that stronger object, but interchanging strict finite-category completion with nerve and full profinite homotopy completion requires an additional argument. F.18 states the precise remaining comparison. The first nontrivial test is n=4. This is an audit limitation, not an asserted counterexample.

Galois descent acts by inverse pullback to give a left action. It is coherent and continuous on finite data and is compatible with the maps defined over Q. Local Kummer covers give the common cyclotomic exponent on all node inertia. The action is faithful from the open four-point stratum and remains so at higher levels through surjective forgetting.

For q_{12,34}, forgetting the fifth mark sends the two independent node twists to the same primitive twist. The kernel on Zhat² is the diagonal (a,-a), hence the lifting groupoid is B Zhat. Its H^1 with F_l coefficients is nonzero, which proves failure of the homotopy-smoothness test. This is not claimed to be a failure detectable by ordinary set-valued connectedness. Galois acts on the difference twist by its common cyclotomic exponent.

## Automorphisms and rational limitations

F.12 proves detection by the open stratum: outgoing coset bimodules recover multitwist stabilizers, their normalizers recover stratum automorphisms, and injective postcomposition recovers every crossing arrow. Inertia-preserving group automorphisms extend using the profinite curve complex and its incidence. F.13 then reduces the decorated two-level automorphism theorem exactly to Harbater–Schneps, with its common inertia exponent and coherent symmetric-group condition. Centre-free stratum groups make the compatibility isomorphisms unique and establish coherence. F.14 extends the result to the full genus-zero decorated boundary tower.

The resulting group is GT, containing the faithful G_Q action. Equality with the arithmetic subgroup remains the profinite question E.8. It would be incorrect to claim that the categorical construction identifies the revised arithmetic image with all automorphisms merely by definition.

For (1,1) and (1,2), F.15 proves the analogous strict transporter completion and stack comparison. Stabilizer quotients retain finite graph and half-edge symmetries. The boundary object of the one-point elliptic category has group C2; passing to a coarse moduli space would erase it. The cofinality argument works with finite unions of closed transporter cosets. F.16 states the precise positive-genus automorphism comparison not completed here; it does not misreport existence of positive-genus GT actions as open.

The established rational analogue is defined separately using algebraically enriched completed parenthesized braid/chord-diagram groupoids and their operadic operations, with Drinfeld and Bar-Natan's exact theorems. Its motivic consequence has exactly the conditional status of E.20. We corrected an initial draft that too quickly identified these groupoids with termwise unipotent boundary transporters. A quotient U/Delta is a homogeneous space, generally not a torsor, and completion does not make a smoothing arrow invertible. An additional enriched boundary-automorphism comparison would need its own proof.

## Sources read and editorial scope

The complete prompt and the supplied manifest were read. For Part A the transcriptions from LM_P021, LM_P023, LM_P026, LM_P027 and LM_P033 were read in the relevant sections, with the following manuscript images inspected directly: scans204,205,320,321,325,326. The owners of B/D/E additionally inspected the scans listed in their reports. We do not claim image evidence for a scan absent from the archive. In particular scan261's proposed switched-subscript correction is mathematical evidence, not a visual reading.

The root reading register includes the base-point enumeration at204; equality of the empty-set stabilizer at206; pointed versus punctured at222; cylinder signs at225–227; the U versus universal-cover symbol and product at252; the action inverse at253; homotopy indices at258; genus reductions at260; the impossible varying-genus Teichmüller chain at261; the extra-point index at263; and a typed groupoid Hom at266. The last is an editorial observation outside the deductions. The closure terminology at321 and doubtful folio328 are also recorded. A grammatical or symbol alternative with no mathematical consequence is not silently used to alter a theorem.

Primary sources actually opened for A/F include:

- Farb and Margalit (2012), Theorems4.6,8.1,8.8,10.6 and §10.6.3. The book supplies the Birman, Dehn–Nielsen–Baer and Teichmüller-coordinate inputs; their scopes were checked.
- Jansen (2023), Construction3.18, Proposition3.23, Corollary6.6 and Theorem6.7 in the supplied v2. We use the stable-type condition of the definitions rather than reproduce the misprinted inequality in the final sentence of Theorem6.7.
- Barwick, Glasman and Haine (2020), Proposition12.6.4, Corollaries12.6.6–12.6.7, Proposition13.9.17 and Corollary13.9.19, in both the supplied source and opened primary PDF.
- Boggi (2020), Definitions3.3–3.4, Theorems3.5–3.6 and4.2, Corollaries4.3 and4.7; the class of finite quotients and full/procongruence substitution were checked.
- Boggi and Funar (2023), Theorem4.11, Corollary4.12 and Proposition7.2, for multitwists, normalizers and incidence.
- Boggi (2026), arXiv2011.15075v6, Proposition3.5 and the specific tower statements checked in Part E.
- Harbater and Schneps (2000), introductory definition and Main Theorem, with the four-point/five-point distinction.
- Hoyois (2018), the notation before Definition2.10, Theorem3.13 and Corollary3.20, especially the meaning of split representations.
- Drinfeld and Bar-Natan through the exact original-source checks in Part E.

We searched these primary sources and the supplied/current tower literature before formulating the completion and automorphism deductions. No claim of novelty or priority is made. The 2026 status check opened the current records and original texts identified in E's report.

## Reproducible finite checks and review

The standard-library program af_checks.py checks:

- the three-versus-two subterminal count;
- a seventeen-arrow finite model of C4 with open group S3 and inertia orders2,2,3;
- every composable triple in that model and every composable pair under the sign quotient transition;
- the four stable-tree types at n=4 and twenty-six at n=5, with every fifth-point forgetting image;
- the node-difference kernel and its stability under all unit multipliers modulo every m from2 through24;
- the nonzero finite Hom models for the H^1 obstruction;
- the torus relations S²=(ST)³=-I and detection of the central involution modulo4.

The infinite statements are proved in the paper, not extrapolated from those bounds. The code records exactly what was enumerated.

Independent reviews within this AI-produced work checked A.4/A.8/A.10; the added A.11/A.13 corrections; F.5–F.14's stabilizer, cofinality, detection and coherence arguments; F.1–F.4 and F.9–F.11's coefficient and descent claims; and F.15's graph-isotropy extension. These are internal checks, not human refereeing or independent external certification. Their concrete corrections were incorporated. The final build and validation record is in the main report.





---



# Parts B and C: research, proof, and reading audit

**Production credit:** AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed for any argument or formulation.

## Delivered work

The completed research text is in `sections/B.tex` and `sections/C.tex`, with 28 numbered statements: 16 Proved, 3 Known, 5 Refuted, and 4 Open. `BC_results.json` gives the statement-by-statement register and dependencies. `BC_readings.json` records ten places where mathematical type checking or scope bears on the transcription. `BC_references.bib` supplies the bibliography entries unique to these sections; the shared Hoshi–Mochizuki 2011, Mochizuki 1999, and Mochizuki 2006 entries are supplied by Part D.

The word **Open** has two expressly different scopes in the paper. B.3 is the established literature-open congruence problem in genus at least three. B.7, B.14, and C.8 give exact unrestricted comparisons not settled by this audit; the text does not misrepresent failure to locate a theorem as proof that every individual instance is an established open problem.

## Main corrections to the leads

1. **Normality is not CSP.** The congruence problem asks whether the abstract profinite completion maps injectively onto its geometric image. Normality asks how outside automorphisms conjugate that image. B.1 separates them. B.5 refutes normality of the full extended geometric group already at `(0,3)`, using complex conjugation in the faithful Galois subgroup and the splitting field of `t^3−2`. This counterexample does not decide normality of the oriented geometric subgroup. The self-normalizer conjecture marked “ultra-faux” is treated as withdrawn; the annotation alone is not used as a proof of falsity of a different claim.

2. **The attached 2009 Boggi paper does not supply the closed genus-two theorem.** Its main theorem is explicitly the open-surface case. Theorem 1.4(ii) of Boggi's *Congruence topologies on the mapping class group* supplies the subsequent closed result. The primary publisher gives publication year 2020, although the retrieved arXiv PDF prints July 12, 2021. The paper's statement, proof location, and publisher metadata were checked separately. Boggi's September 2026 article confirms the genus-at-most-two range and adds symmetric centralizer results without solving general high-genus CSP.

3. **Finite-cover injectivity for actual discretizations can be proved without CSP.** Conjugacy separability plus Grossman's Property A makes a discrete free or surface lattice self-normalizing in its completion. This yields the manuscript's raw injectivity assertion for normal covers; passing to the core proves it for arbitrary finite covers. The complete image criterion is also proved: the deck outer action must come from discrete orientation-preserving peripheral automorphisms. Center-free extension theory constructs the candidate extension; Kerckhoff's Theorem 7 makes it Fuchsian; torsion-freeness makes it a surface group; the simple-loop centralizer theorem verifies its peripheral structure. None of these final steps is silently inferred from the underlying abstract-group extension.

4. **Raw restriction can fail to be onto.** The degree-two map `z↦z²` from the four-punctured sphere to the three-punctured sphere supplies an explicit covering. Its deck involution acts nontrivially on the upstairs pure mapping class group `F₂`. Its centralizer in the geometric closure is not open, so its conjugacy orbit is uncountable, whereas the discrete mapping class group is countable. A conjugating element outside the countably many acceptable closed conjugator sets gives a lattice that cannot extend. The text specifies the element by a nested-clopen construction. The failure concerns raw discretizations; the two upstairs models have the same closure prediscretization.

5. **Raw finite-cover injectivity does not transfer to puncture filling.** Conjugating a four-punctured-sphere lattice by a nonintegral profinite power of the inertia being killed produces a different lattice with the same filled image. B.15 gives the full argument. This refutes the filling extension of the prompt's raw-injectivity assertion, not the strict or closure prediscretization assertion.

6. **The two positive Birman sequences are established in every hyperbolic target type.** C.2 proves the full profinite exact sequence directly, including why the completion of the point-pushing kernel embeds. C.3 uses Boggi 2020 Corollary 4.7 for the procongruence sequence, including closed targets. C.4 explicitly proves invariance of the congruence kernel under adding a puncture. This prevents a hidden use of high-genus CSP.

7. **The revised arithmetic quotient is genuinely Galois.** For the arithmetic-image definition introduced in §29, Hoshi–Mochizuki Corollary 6.4 shows that arithmetic and geometric monodromy intersect trivially over a number field. A curve of any fixed marked type exists after a finite extension, which is enough: the remaining kernel over `Q` would be a finite normal subgroup of `G_Q`, excluded by slimness. Thus C.5 identifies the revised quotient canonically with `G_Q` in every hyperbolic type. This is not a claim of surjectivity onto a full normalizer or onto `GT`. C.6 then proves arithmetic filling exactness by quotienting the arithmetic moduli Birman sequence by the matching congruence kernels.

8. **The double-hat row remains a distinct issue.** C.7 constructs the genuine-automorphism map supplied by a distinguished cusp, with its precise representative ambiguity. C.8 proves that its being an isomorphism is equivalent to the full outer exact sequence and to the relevant unrestricted prediscretization filling bijection. Thus the manuscript's “??” is located exactly: full ambient surjectivity and a kernel consisting only of point-pushing. The smallest hyperbolic target test is `(0,4)→(0,3)`. Hoshi–Mochizuki's configuration-space theorem has additional fiber and cuspidal compatibility hypotheses; it cannot simply be substituted for this isolated single-surface statement.

9. **The full étale topos requires more than finite covers.** C.10 gives a complete counterexample to the substitution of the classifying topos of the fundamental group for the full small étale topos: the former has only two subterminal objects, whereas the curve has all its Zariski open subsets. C.11 gives a correct reconstruction theorem over a fixed sub-p-adic field, on the geometric essential image. Relative anabelian reconstruction first recovers the open curve; its function field recovers the proper model; opens in normalizations in all finite separable function-field extensions give a basis for the whole étale site. The proof uses Zariski's main theorem with checked Stacks tags. It does not assert a recognition theorem for arbitrary abstract extensions, nor use the section conjecture.

10. **Arbitrary-base sections are not disjoint points.** C.12 states the valid field-valued point-deletion formula. C.13 gives the constant family `U×U→U`, with diagonal and constant-2 sections, which meet at `2`. This is the concrete geometric obstruction the manuscript itself recognizes in scans 433–435. The earlier general formulation is preserved as withdrawn rather than quietly treated as a theorem.

## Sources actually read and verification depth

### Manuscript

The complete task prompt was read. The transcriptions in packages LM_P033 through LM_P044 were read for the assigned questions, with particular attention to scans 320–326, 347–363, 367–380, 395–420, 421–430, and 433–435. The associated research notes were treated as leads, not authority. Images of scans 322, 348, 352, 395, 399, and 418 were inspected where the mathematical interpretation depends on the writing. Scan 358's image was not present at the supplied image path, so its audit entry claims mathematical type evidence only.

The relevant folio mapping is: 350–351 →177; 352–353 →178; 354–355 →179; 356–357 →180; 358–359 →181; 360–361 →182; 362–363 →183. Scans 395–396 are folio200, 397–398 folio201, 399–400 folio202. Scans 417–418 are folio211, 419–420 folio212, 421–422 folio213, and 429–430 folio217. Scans 433–434 are folio219 and scan435 folio220. The transcriptions sometimes also insert a lower running scan number as `mspage`; those were not mistaken for the top manuscript folio.

The exact phrase “tout le topos étale…” quoted by the prompt was not located verbatim in scans 395–420. The relevant construction continues into scans 421–430. The text identifies this fact and does not invent a quotation.

### Primary mathematical sources

- **Boggi (2009), attached arXiv v6:** Section2's full profinite exact sequence, Propositions2.2–2.6, Theorem2.8, Theorem3.5, and the explicit open-surface qualification were read. The low-genus results are imported established theorems; their whole historical proofs are not reproved here.
- **Boggi (2020), [primary PDF](https://arxiv.org/pdf/1804.06322), [publisher metadata](https://www.sciencedirect.com/science/article/pii/S0021869319306313):** Theorem1.4(ii), Proposition2.4(ii), Theorems3.5–3.6, Theorem4.2, Corollary4.3, Theorem4.4, Corollaries4.5 and4.7, and Remark4.8 were checked. The stabilizer and multitwist results were supplied to Part F with their scope. The Birman corollary's deduction from center and centralizer structure was followed, while the full proof of the imported curve-complex machinery was not independently reconstructed.
- **Boggi (2026), [primary publisher full text](https://link.springer.com/article/10.1007/s40863-026-00558-y):** Introduction and TheoremA/CorollaryB were checked for current status and the symmetric-centralizer range. No broader theorem was inferred.
- **Paris (2009), [primary PDF](https://arxiv.org/pdf/math/0703703):** Property A's definition and attribution to Grossman in the introduction, Theorem3.2 for free-group conjugacy p-separability, and Theorem4.1 (=1.7) for closed surfaces were checked. The original Grossman paper's full proof was not obtained, and no claim to have checked it independently is made. B.8's deduction from these statements is written out.
- **Kerckhoff (1983), [primary journal page](https://annals.math.princeton.edu/1983/117-2/p02), [paper scan](https://poisson.phc.dm.unipi.it/~camponovo/Kerckhoff-NielsenRealizationProblem-1983.pdf):** Theorem5 and the extension to general Fuchsian groups culminating in Theorem7, p258, were checked. The proof of Theorem7 from finite-group realization and center-free extension theory was followed. The deep Nielsen realization theorem is imported, not re-proved.
- **Boggi–Zalesskii (2019), [primary PDF](https://arxiv.org/pdf/1408.5419):** Definition1.3 confirms that simple peripheral curves are included; Lemma3.1(ii) supplies torsion-freeness in the surface case; Proposition3.6 supplies normalizers of nonzero powers of algebraically simple elements; Theorem3.7 supplies the completed graph-of-groups decomposition. The proof of Proposition3.6 through finite-order nodal-Fuchsian quotients was read. The underlying solenoid machinery is imported. The exact centralizer statement was supplied to Part D.
- **Hoshi–Mochizuki (December2011 attached version), nodally nondegenerate representations:** Theorem6.1 and Corollaries6.4–6.5, pp61–67, were read directly, including their proofs and scope. Part D verifies the deeper imported prerequisites. C.9 uses the stronger configuration bounds in Theorem6.1 rather than the earlier incomplete proper-case injectivity range.
- **Mochizuki (2010), [primary university publication](https://ir.library.osaka-u.ac.jp/repo/ouka/all/12138/ojm47_03_651.pdf):** Definition1.1(ii), Theorem4.1, and Corollary4.2 were checked. These are cited as configuration-space results, not unrestricted single-surface automorphism results.
- **Hoshi–Mochizuki (2012), TopicsI, attached primary text and [publication metadata](https://doi.org/10.2969/aspm/06310659):** TheoremA and Corollary1.9 were checked for the implication from higher F-admissible lifts to FC-admissibility.
- **Mochizuki (1999), relative Hom/Isom theorem, and Mochizuki (2006), Galois slimness:** These shared inputs were checked by Part D and communicated with exact source numbers. C.11 imports the former; C.5 imports the latter. The 2006 numbering differs by version: published Corollary2.2 is preprint Corollary1.3. The text now specifies both.
- **Stacks Project, [02LR](https://stacks.math.columbia.edu/tag/02LR) and [05K0](https://stacks.math.columbia.edu/tag/05K0):** Both exact statements and proofs were opened. They are Lemmas37.43.2–37.43.3, the relevant normalization and finite-factorization forms of Zariski's main theorem.

Searches also checked the primary literature on symmetric quasi-special outer automorphisms, procongruence automorphisms, and the newer configuration/cuspidalization results for a theorem removing the unrestricted single-surface hypotheses. No such theorem was located. This negative search result is not represented as a proof that no such theorem exists.

## Computation and limits of the checks

`code/bc_counterexamples.py` runs without third-party dependencies and writes the reproducible data in `code/bc_counterexamples_output.json`. All assertions pass. It checks:

- the discriminant of `t³−2`, the six-element permutation group, and the conjugate of the complex-conjugation transposition outside its order-two subgroup;
- explicit order-two and order-three matrices generating `SL₂(F₈)` of order504, its conjugacy-class sizes, and simplicity by exclusion of proper class unions whose cardinalities divide504, providing a finite noncongruence witness for the unpunctured torus;
- the deck permutation and distinct curve partitions in the degree-two cover;
- compatible Chinese-remainder approximations to the profinite integer used in B.15;
- the two-versus-three subterminal count and the intersection of the two explicit sections.

The program does not claim that finitely many CRT residues prove nonintegrality. It does not claim to distinguish dense discrete lattices by a finite quotient. The uncountable-orbit and self-normalizer arguments, which are the actual proofs, are in the paper. The finite computations support precisely the finite claims identified above.

## Remaining issues stated exactly

B.3: the kernel of `hat P_(3,0)→Out(pi_(3,0))` and its higher-genus analogues. B.7: whether the full ambient loop-preserving group normalizes the oriented geometric subgroup, already the `S₃` normalizer comparison at `(0,3)`. B.14: the inverse-image and factorization conditions for unrestricted prediscretization bijectivity under finite covers, with the degree-four characteristic cover of the tripod specified. C.8: full surjectivity and the exact point-pushing kernel for the unrestricted single-surface filling map. The manuscript's direct recognition of admissible splittings for arbitrary abstract acting groups is not claimed to have been supplied; C.11 proves the reconstruction of the full topos on the geometric essential image by the established arithmetic Isom theorem instead.

The parent requested an independent check of A.4, A.8, and A.10. Their lift correspondence, raw/outer quotient distinction, two-to-one orientation quotient, and right torsor construction are mathematically consistent as written. A.4's cited folio interval for scans350–356 should be177–180, and that correction was communicated. No files belonging to Parts A, D, E, or F were modified.




---



# Part D: arithmetic, inertia, sections, and source audit

## Scope and principal conclusions

Part D supplies 23 numbered statements. The distinction between `Known`, `Proved`, `Refuted`, and `Open` is literal: a proved implication whose antecedent is a new unverified claim is not recorded as an unconditional theorem. `Open; claimed` for proof packs 019 and 031 records the limit of this independent audit, rather than claiming to disprove the preprints or to establish that no expert verification exists. All arithmetic groups in the main assertions are full profinite étale groups. The geometric pro-p variant of the relative Hom theorem retains the full arithmetic quotient.

The literal inertia-normalizer assertion in §34 is false. The whole geometric fundamental group already has an arithmetic normalizer projecting onto the Galois group, and a proper characteristic nonprocyclic subgroup gives a second counterexample. Rational-point section images furnish a further obstruction if one allows arithmetic instead of geometric subgroups. Nakamura's actual recognition theorem adds the cyclotomic conjugation law. This law must not be silently removed.

The relative open Hom theorem is established, and its Isom consequence proves the proposed equivalence between *geometrically admissible* effective lifts and rational points. It does not prove that all sections are admissible. A complete tangential-section example on the rational tripod refutes unrestricted affine section surjectivity onto interior points.

For absolute open Hom, the source's geometric kernel does map into the target's geometric kernel unconditionally. Its image in the open target Galois subgroup is topologically finitely generated, closed, and normal, and Mochizuki's published Theorem 2.4 makes it trivial. Thus 031 is needed only to reconstruct an embedding of the base fields from the resulting open Galois homomorphism. The relative Hom theorem then finishes a rigorous conditional reduction. The exact conjugacy ambiguity is all target inner conjugacy in the absolute formulation, versus geometric inner conjugacy with a specified map to the same arithmetic quotient.

Faithfulness is known for every hyperbolic curve over a number field or p-adic local field, including proper curves. Hoshi–Mochizuki Corollary 6.4 proves the stronger statement needed for the revised arithmetic-image Teichmüller quotient, while Corollary 6.5 separates injectivity of total universal monodromy from the geometric congruence problem. Part D proves the finite-field-of-definition and ordered/unordered deductions explicitly. The quotient is by the orientation-preserving geometric image. Replacing it by an extended mapping-class group kills complex conjugation and may destroy normality, so it is a different assertion.

## Audit of proof pack 019

**Source read.** The complete main text *The p-adic section conjecture*, dated October 6, 2026, was read, including the new analytic and stable-model arguments and the deductions in Sections 7–8. The companion *Étale covers with a prescribed exterior sheet* was inspected for its statement and role but its complete proof was not independently audited. It is not used as an established theorem here. No Lean statement is needed, and no claim is made that a Lean file certifies the geometric argument. Corollary 8.4's additional arithmetic input is deliberately not used.

**Exact new bottleneck.** Theorem 1.2 is a statement about a specified embedding into a specified valued completion: the separable function-field extension must lie in the completion of the proper étale tower inside the chosen completion of the separable closure. An abstract field embedding is insufficient for the subsequent decomposition-group identification. The all-sheet formulation is also necessary. A local analytic lift on one selected sheet does not automatically give the asserted inclusion of the full algebraic extension.

**External inputs checked in primary sources.** Amini–Baker–Brugallé–Rabinoff, Theorem 7.7, was checked with the definitions of tame coverings and marked branch points. Mochizuki–Tsujimura, Theorem A and Proposition 2.4(iv), was checked in the opened RIMS 1974 version of June 16, 2023; the 019 bibliography calls its revision 2024, and that version distinction is retained. Baker–Rabinoff, Proposition 6.1 and Corollary 6.6, was checked together with the period-pairing discussion. These statements supply specific model, covering, and divisor-lifting tools. They do not automatically combine into the simultaneous analytic approximation assertion of 019.

**Proof components tested.** The model domination step, graph-bridge case, need to retain exterior sheets, normality used at the final extension step, compatibility of marked branch loci, and dependence on the fixed valuation were followed. The toric/annular root constructions and their interaction with stable-model refinements require uniform choices across the sheets and all relevant finite extensions. This audit has not independently established that uniform construction in the complete generality of Proposition 5.2 and the resulting Theorem 1.2. No explicit counterexample or decisive erroneous line was found. Consequently D.7 remains `Open; claimed`, with the precise assertion and the remaining verification task stated.

**What is proved conditionally.** D.8 gives a complete proof from the specified-embedding completion assertion to the proper local section theorem. It checks the passage from completions to decomposition groups and uses the exact statements of Koenigsmann's Proposition 2.4(2) and Pop–Stix's Theorem 26. The rank-one exclusion is reproduced using two inequivalent henselian valuations and the elements

\[
q_r=d+(1-d)\frac{z^r}{1+z^r},\qquad z=p^N/t.
\]

The valuations make this element a square at one henselian valuation and force the nonsquare constant class at the other. The quantitative Hensel threshold explicitly includes residue characteristic 2. Rank two, the horizontal coarsening, rational residue degree, and triviality of horizontal inertia in a proper étale tower are then treated separately. Injectivity is justified by the Jacobian Kummer map and the vanishing of the intersection of all integer multiples in the compact p-adic group.

D.9 proves the exact conditional global statement through Harari–Stix's Theorem 2.1 and Remark 2.2(1), in the February 11, 2011 primary preprint numbering. Modified adeles retain real connected components and omit complex places. The real section theorem is checked in Bresciani–Vistoli's primary note. Stoll's 2017 erratum is incorporated, including disconnected torsors and the treatment of real places. This argument identifies localized global sections with the finite-cover descent set; it does not show that this set is always the rational diagonal.

**Modular consequence.** D.10 combines the conditional local theorem with Stoll's Corollary 8.8, its erratum, Stix's finite-support Corollary 5, and Mazur's Introduction Theorem (7), page 35. When the compactification X_1(N) has genus at least two, a section of Y_1(N) compactifies to the section of a unique rational cusp. This is the precise consequence available for an N_{1,1} moduli section provided its image is contained in the open modular subgroup over G_Q itself. Restricting an arbitrary section to an open G_L only yields a section over L; the cited rational-point theorem over Q cannot automatically be applied over L. Compactified cuspidality does not prove the original affine section is a cuspidal section, and it does not prove that moduli sections do not exist. Tangential sections at rational cusps show why the distinction matters.

## Audit of proof pack 031

**Source read.** The complete October 5, 2026 main text, Sections 1–6, including each new lemma and proposition used in Theorem 1.1, was read. The proof was examined as a chain of arithmetic separation arguments rather than accepted from its abstract. No Lean formalization is used.

**External inputs checked.** Uchida's 1979 isomorphism theorem and Lemma 3 were opened in the primary four-page paper. Uchida's 1981 paper was opened in its entirety, including the local three-case alternative, Proposition 1, Proposition 2, Theorem 1 for source field Q, and Theorem 2 under its local condition. Hoshi's Theorem 3.4 was checked in the revised primary preprint, and its published 2025 metadata was verified. Its hypothesis of compatibility with cyclotomic characters is retained. The cited conjecture and the later known partial theorems must not be conflated.

**New arguments examined.** The zero estimate in Lemma 3.1, determinant bounds, and the numerical condition exceeding n(n−1) were followed. Proposition 3.2's passage from vanishing on infinitely many degree-one primes to vanishing of additive characters was tested against its Frobenius averaging and corestriction requirements. The construction of equivariant projections, regular-module components, and normalizer-kernel separation in Proposition 4.3 was followed. Proposition 5.3's uniform bound 2[K:Q]+2 depends on the multiplicity of one character in the relevant S-unit module, rather than a bound by the total extension degree. The Kummer prime choices and valuation independence in Lemma 5.4 and the final compactness argument producing a single conjugator were checked. No Leopoldt conjecture was silently inserted.

The generality and uniformity of the new zero/separation estimates are not independently established by this audit. Reading and tracing these arguments is evidence about their structure, not a substitute for reproducing the new arithmetic lemma in all its cases. No explicit contradiction, counterexample, or fatal gap was found. D.13 therefore records the unrestricted theorem as `Open; claimed` and identifies the exact remaining verification work. D.12 gives the complete implication from that theorem to absolute open Hom for number-field hyperbolic curves. D.11, which supplies geometric-kernel preservation, is unconditional and uses an earlier published theorem.

## Exact theorem numbering and version issues

| Source | Exact statement used | Version note |
|---|---|---|
| Nakamura (1994) | Theorem (2.1.1); Lemma (2.1.2); Corollaries (1.3.3)–(1.3.4) | Attached published text |
| Mochizuki (1999) | Theorem A = Theorem 16.5 plus following Remark; Theorem C = Theorem 19.1 | Attached published text |
| Mochizuki (2006) | Theorem 2.4; Corollary 2.2; Lemma 3.2; Proposition 3.3; Theorem 3.1 | Published journal numbering. Author PDF labels them 1.5, 1.3, 2.2, 2.4, 2.1. Journal PDF prints pages 57–71; repository metadata lists 57–72. |
| Hoshi–Mochizuki (2011) | Corollary 6.3(i), Corollary 6.4, Corollary 6.5 | Attached PDF pages 64–67 |
| Matsumoto (1996) | Theorem 2.1 and its Conjecture 2.1, printed page 191 | Actual primary scan inspected; the theorem proves the affine number-field case |
| Belyi (1980 English translation) | Theorem 4, page 255; unnumbered corollary, page 256 | Original Russian publication 1979 |
| Boggi–Zalesskii (2019) | Proposition 3.6 | Full pro-S group; nonzero profinite exponents; algebraically simple generators |
| Harari–Stix (2012 publication) | Theorem 2.1; Remark 2.2(1) | Numbering of opened February 11, 2011 author preprint |
| Pop–Stix (2017 publication) | Theorem 26; Section 6.1 | Numbering of opened August 11, 2011 author preprint |
| Stix (2015 publication) | Corollary 5 | Opened February 27, 2014 preprint |
| Stoll (2007) | Corollary 8.8 | Used with March 29, 2017 erratum |
| Mazur (1977) | Introduction Theorem (7), page 35 | Distinguished from (7′) and the complete torsion classification in (8) |

Every bibliography entry in D's fragment is marked `verified` or, where needed, described as a verified source with an unverified new proof. Source verification means that the relevant primary text was opened; it does not turn an unrefereed argument into an established theorem. The shared Boggi–Zalesskii bibliography key is supplied by Parts B–C.

## Manuscript and computational audit

The scans actually inspected are 483, 485, 496, 500, 501, 504, and 505. Readings are recorded separately in `D_readings.json`; doubtful typography is not silently resolved. In particular, the normalizer claim cannot be repaired by choosing Γ versus Γ+, and the folio245/246 discrepancy is retained. The endomorphism-versus-automorphism phrase on scan501 does not affect the rank-one calculation: the weaker endomorphism hypothesis suffices.

`code/d_counterexamples.py` is executable using the Python standard library. Its recorded output checks generation and perfectness of A5, the small finite normalizer model, the discriminant and derived-group data used for an S3 Galois quotient, and the abelian centralizer of the CM matrix modulo 2,3,4,5,8,9. The profinite conclusions are proved in D.2 and D.20; no finite computation is presented as a proof of an unbounded inverse-limit assertion.

The small nonhyperbolic types (0,0), (0,1), (0,2), and (1,0) are handled explicitly. The hyperbolic types (0,3) and (1,1) share the abstract geometric group Fhat2 but have different inertia systems. Real sections are indexed by connected components, and real Galois groups are not slim. Nonorientable topological quotients are distinguished from geometric complex-curve groups. None of the stated characteristic-zero Hom, proper local conditional, faithfulness, or simple-loop centralizer results excludes p=2 or p=3. The modular stack's 2- and 3-isotropy is retained rather than discarded via a coarse space.




---



# Part E: comparison and proof audit

## Principal corrections

The manuscript does not use one fixed group throughout §§26–36. Section 26 defines a normalizer quotient. Section 29 changes to the image of arithmetic universal monodromy. Scan 370 announces the arithmetic approach; scan 371, not scan 370, contains the instruction to call the image M and explicitly calls the induced Galois map surjective. Thus the revised conjecture asks injectivity. The normalizer conjecture additionally asks that all compatible normalizing automorphisms be arithmetic. The strong assertion that the normalizer equals all loop-preserving outer automorphisms is a third assertion.

The positive orientation convention is essential. The actual quotient in scan 371 equation (12) has positive geometric denominators. A nearby missing superscript is retained in the readings register; the explicit quotient is unambiguous. Quotienting by the full extended mapping class group would kill complex conjugation. No conclusion in E depends on restoring that doubtful occurrence.

Hoshi–Mochizuki's nodally nondegenerate theorem, Corollary 6.4, as proved/applied in D.17, identifies every revised arithmetic quotient with G_Q. This uses the actual procongruence geometric image and does not assume the congruence subgroup property in arbitrary genus. It makes the revised cyclotomic abelianization claim a consequence of Kronecker–Weber. Scan 479's unnamed Russian result is identified contextually as Belyi; the name is not read from the handwriting. Belyi's three-branch-point theorem is Theorem 4, with the faithfulness corollary following on printed page 256, not Theorem 1.

## Normalizer and tower comparisons

E.6 supplies a general centre-free pullback lemma: conjugation embeds a normalizer quotient in the outer automorphism group of the universal-curve group. This avoids identifying a surface normalizer with an automorphism group of the wrong level.

For the full permutation convention, the early quotient at (0,3) is GT_0, the symmetry-and-hexagon group. It is the S3 centralizer in the loop-preserving exterior automorphisms of F2hat. The pure convention would have trivial geometric subgroup and a different normalizer problem. For (0,n), n≥4, the universal curve is P0,n+1hat. HMM's intrinsic theorem gives Out=GT×S_(n+1), and normalizing the point stabilizer S_n leaves precisely GT after quotient. The converse uses the actual compatible tower action. This proves the stated comparisons at (0,4) and (0,5).

Harbater–Schneps's exact results are Main Theorem (a),(b), Theorems 2 and 3, Proposition 7 and Proposition 8. The prescribed common exponent and relabelling centralizer are retained. The braid formulation also retains inclusion and doubling maps; an arbitrary pair of unrelated outer automorphisms is not a two-level tower action.

For (1,1), E.10 supplies an independent comparison proof using Minamide–Nakamura. The universal-curve group is P1,2hat=B4hat/central full twist, whose outer automorphism group is GT. The characteristic Cardano–Ferrari kernel K is the profinite free product of three C2 factors; its unique parity homomorphism gives the characteristic once-punctured elliptic surface kernel. The two-chain peripheral element is zeta3 squared, preserved with the GT multiplier. These checks give both inclusions, rather than inferring a normalizer theorem solely from the statement Out(P1,2hat)=GT.

For (1,2), E.11 gives an exact reduction to A/S2 in Out(P1,3hat). The group A must preserve the universal-curve kernel, its peripheral structure and the permutation action. Boggi's current action gives GT into this quotient. Automatic preservation of nonseparating inertia by arbitrary A is the precise remaining step in our audit; E.14 does not claim that no related theorem exists in the literature.

The arithmetic equality G_Q=GT remains separate. We did not verify a primary profinite counterexample proving GT strictly smaller than GT_0. Historical assertions of strictness were not promoted into a proof, and rational or finite-shadow calculations were not substituted. This limitation does not affect the distinction between the early and revised groups.

## Current all-genus and reconstruction results

Nakamura–Schneps (2000), Definition 1.1 and Theorems 1.2–1.4, give their named refinement with additional equations and quilt compatibility. Hatcher–Lochak–Schneps (2000) Theorems A–C are respectively Lemma 7, Theorem 4 and Theorem 5 of §3; their Lambda is a multiplier-one subgroup with an additional genus-one relation. Its action is not an assertion about all G_Q with its full cyclotomic character.

Boggi arXiv:2011.15075v6 (22 April 2026), §2.8 and Theorem 6.23, identifies the particular procongruence outer surface-embedding functor's automorphism group with GT. Corollary 6.24 gives an injection into the corresponding full profinite functor; equality is Conjecture 6.21. The objects, embedding maps and outer target convention are part of the theorem. This is not automatically a theorem about all path torsors, quilts, covering maps or degeneration bimodules. Lochak–Nakamura–Schneps arXiv:2602.12462v1, Theorem 1.1, independently supplies full GT actions on the profinite groups of types (g,0),(g,1); Theorem 2.1 records the full-twist formulas. We checked the cited primary statements, not the complete proofs of these new preprints.

Pop's finite tripod theorem retains a cofinal birational localization system and three designated functions. The relevant exact results are Definition/Remark 2.2, Definition 2.5 and Theorems 2.6–2.7 of the attached 24 December 2018 text. Discarding the localization objects and retaining M04,M05 alone does not preserve the hypotheses.

Collas's November 2026 survey was used as a locator. We opened Hoshi–Mochizuki–Tsujimura's original 2025 paper and checked Theorem C(ii), with Definitions 3.3 and 5.12: maximal closed AA subgroups characterize the GT-conjugacy class of G_Q. This does not say GT itself is arithmetic. Neither that theorem nor family019 classifies every admissible moduli-stack splitting.

E.17 states the exact conditional modular consequence of family019 Corollary 8.5 and Mazur's Theorem (7): an affine modular section compactifies to a rational cusp section in the specified genus range. It proves neither affine cuspidality nor nonexistence; tangential cusp sections exist. Part D retains the unrefereed premise and its scope.

## Rational chain and family008

The rational object is the Malcev/prounipotent completion of the pure parenthesized braid groupoids with its permutations, cabling, deletion and reassociation operations. It is not arbitrary locally constant D(Q) coefficients, not the discrete surface group, and not indiscriminate unipotent completion of all mapping class groups. Drinfeld §§5–6, Propositions 5.1 and 5.5, and Bar-Natan Proposition 3.4, Theorems 1–3, Corollary 4.1, identify the filtered GT and graded GRT actions; choosing an associator identifies the two noncanonically.

Brown's established motivic injection is the lower bound. The exact explicit containment in grt is also checked in the published Brown (2021), §1.4.2. Family008 Corollary 5.4 supplies the claimed opposite dimension bound. E.20 proves the conditional dimension squeeze, weight completion, exponentiation and torus extension. The resulting arithmetic equality is labelled **claimed (OpenAI, 2026, unrefereed)** when this manuscript supplies the premise.

The realization arrows are G_Q → GThat → GT_ell → GT(Q_ell). The first is injective; the second is not injective, because the arithmetic pro-ell action is unramified outside ell; the third is injective by the free pro-ell Magnus comparison. GT_ell is a group of pro-ell pairs with scalar in Z_ell^times, and need not itself be a pro-ell group. Neither compact image is onto, dense or open in the full rational group with its inverse-limit ell-adic topology. The scalar obstruction proves nondensity; Brown's arbitrarily high noncompact additive one-parameter subgroups exclude openness. No surjectivity assertion about the arithmetic image inside GT_ell is made.

Hain–Matsumoto is used with its exact chain: Theorem 7.3 (weighted completion, initially with weight one), Theorem 8.4 (graded image), Lemma 8.5 (weight-one disappearance in the outer action), Remark 8.6 (Soulé classes), Theorem 9.8 (mixed Tate factorization), and Appendix A Theorem A.6/Corollary A.10 (unipotent comparison). Zariski density in finite-dimensional algebraic quotients is kept separate from ell-adic topological density.

The actual profinite counterpart needed is exhaustion of every finite quotient; E.22 proves its equivalence with surjectivity by compactness. E.23 gives the rigorous counterexample 1⊂C2 to transfer from unipotent equality to profinite equality. The conditional abelianization calculation gives additive odd-weight lines for GRT1 and G_m for the full semidirect group GRT. Only the latter corresponds to the cyclotomic statement.

### What was read and checked in 008

Sections 2–5 were read, including the saturated Z_(2) lattice, free-fibre presentation, special derivation identity, filtered normal-form comparison, type-B3 deletion representation, leading-term detection, Ore extension, Vandermonde/divisibility argument and free-Lie elimination. The paper distinguishes ordinary Lie elements from all primitive characteristic-two elements; this distinction is retained. Division by w+1 in §2 takes place over Q before reduction. The plus/minus hyperplanes are distinct rational arrangement labels before reduction and are not merged in characteristic two.

Independently established in this deliverable: saturation and dimension transfer, W1=W2=0, the conditional dimension squeeze, completion and abelianization arguments, and the bounded deletion check. Selected entries of the §3 tables and selected boundary cases in §4 were checked. We did not independently rederive the entire all-weight normal-form induction of Proposition 3.2 or the coefficient-detection induction of Proposition 4.4. These remain imported steps. The alternative lower bound and graph-complex consequences of §§6–8 were not used.

The attached Lean comparator was read in full. Its theorem main ends with `by sorry`. No separate Lean repository was retrieved, built or kernel-checked. This refutes a claim that the attachment itself is a checked proof; it does not refute mathematical freeness.

### Computations

`code/e_deletion_checks.py` is standalone and uses exact integer/rational arithmetic. `audit/E_computation.json` records nine rational hyperplanes, thirteen codimension-two flats, all 364 words of length at most five on the three-letter alphabet, and 13,104 zero commutator checks. It also computes the free odd-generator Lie dimensions through weight 30 and verifies the finite C2 multiplication table. The dimension list is a computation of the proposed free-Lie bound, not of W itself. The bounded deletion test does not prove its all-length extension.

### Current status search

As of 11 November 2026, Willwacher arXiv:2610.15592v4 (28 October 2026), *The Deligne–Drinfeld conjecture after OpenAI*, gives a subsequent primary proof treatment and states the freeness result as Theorem 1.1. We opened it and read the principal statements and reduction, not a complete independent all-weight proof audit. Accordingly the deliverable does not report an absence of subsequent mathematical work, but retains conditional use of the supplied upper bound. A seminar listing or a search abstract alone was not used as certification. This new rational literature does not settle G_Q=GThat.

## Source verification register

The BibTeX fragment records exact opened sources and scope in each note. Attached texts checked directly include Belyi, Harbater–Schneps, Hoshi–Minamide–Mochizuki, Nakamura (1994), Nakamura–Schneps, Hatcher–Lochak–Schneps, Brown (2012), Hain–Matsumoto, Drinfeld, Pop, Collas and family008. HLS pages were rendered and visually inspected because extraction was poor. Scan324 and scans370–371,479 were visually inspected. Part D supplies its separately verified Hoshi–Mochizuki and Mazur applications.

Additional original sources opened online include Minamide–Nakamura's full paper, Boggi v6, Lochak–Nakamura–Schneps 2026, Hoshi–Mochizuki–Tsujimura 2025, Bar-Natan's author text, Brown's published 2021 text and Willwacher v4. Opening and checking a cited statement is distinguished from independently certifying the entire proof. Unopened abstracts and secondary attributions have not supplied mathematical conclusions.

## Independent review of Part F

The finite-category cofinality argument in F.6–7 uses a substantive full-induced-topology theorem and works: unique labelled submulticurves make each genus-zero transporter a single stabilizer coset, and finite-functor kernels can be extended to finite ambient group quotients. It does not rely on residual finiteness alone. F.12's detection argument uses the multitwist normalizer and the injectivity of postcomposition into the open object. F.13–14's genus-zero coherence argument can use centre-free stratum groups and the surjectivity of forgetting.

The principal qualification identified in review concerns the initial F.17 draft: unipotent transporter quotients are homogeneous spaces, generally not torsors, and a termwise Malcev completion of a boundary category with smoothing arrows is not literally the parenthesized braid groupoid. The exact established rational statement is obtained by defining the enriched analogue through completed PaB/PaCD with their operadic data. A further comparison to all termwise-completed boundary transporter data would require proof. This issue was sent to the parent for incorporation. The general higher-completion comparison and the elliptic decorated-diagram comparison are correctly kept distinct and unresolved in the current draft.




---

