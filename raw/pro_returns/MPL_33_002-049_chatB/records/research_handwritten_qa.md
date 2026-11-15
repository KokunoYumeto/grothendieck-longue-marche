# Post-freeze QA: handwritten scans038–048 and early-item corrections

This review used the frozen individual page files, the complete `research_literature.md`, and the already-read supplied context. No images were viewed and no core artifact was changed. Line numbers below are exact individual `.tex` lines, not physical manuscript lines. Square brackets in shortened quotations identify an uncertain reading in the frozen transcription; ellipses shorten quotations only in this research apparatus.

## 1. Important corrections to early research items

| Item | Exact locus | QA finding and recommended treatment |
|---|---|---|
| E26 | 028:2–18 versus 028:21–23 | **Qualify the Kummer NB.** The edge-isomorphism argument concerns arbitrary codimension d under the stated low-degree vanishing. The NB separately begins with the uncertain “si” and a global β in H¹_Y(X,G_m), followed by a degree-two Kummer boundary and vanishing of its image in H²_Y(X,G_m). Do not imply that every codimension-d class has this degree-two preimage or this image-zero statement. |
| E36 | 024:10–12; 028:12,22 | The index-order discrepancy is accurately recorded: X/Y in028:12 versus Y/X in024 and028:22. The gamma/sigma glyph remains uncertain in every occurrence; use it as a named class only after explicitly declaring a notation convention for analysis. Neither the literature's conventional Y/X nor a type check adjudicates the ink. |
| E10 | 010:2 | **Use L17's explicit test.** Mere local constancy and fixed-coefficient freeness are materially different. The rank-one Z/4 local system with sign monodromy on a complex elliptic curve has H⁰=Z/2, so the stronger fixed-ring freeness reading fails already in degree zero; the positive specialization comparator gives local constancy. Frame the final item as a reading/scope question with a conditional own-example, not solely as an unproved positive freeness theorem. |
| E05 / E06 | 006:22–30; 008:6–13 | L01–L03 add a stronger issue than documentary cancellation: arbitrary torsion in the nonproper analytic comparison actually admits the direct-sum/product test, separately from the analytic-constructibility category problem. Preserve both tests if space permits; they concern different literal claims. E05's scan metadata now correctly includes006 and008. |
| E14 | 014:24–27 | The primitive-section multiplier must be a unit, and whether the coordinate isomorphism scales by λ^d or λ^(−d) depends on its direction. Treat the wording as a convention/type question, not a settled sign correction. The referent of “Dém” in28 may be the preceding purity statement; it should not be assigned automatically to the change-of-generator formula. |
| E25 | 026:33–46 | Its conservative reading is correct: the normal codimension-one clause belongs to low-degree vanishing, not unrestricted full absolute purity. Keep this qualification even when adding Riou's stronger theorem for regular pairs. |
| E28 | 028:14–18; 030:11–21 | Its support warning remains warranted: the earlier properness branch may be inherited, but the source on030 does not restate it. A missing standard inclusion of support families is the issue; do not claim that absolutely no homomorphism between the abstract groups could exist. |
| E29 | 032:16–17 | The piecewise twist statement is visible. A locally varying derived shift is an interpretive consequence, not a shift written on032; uniform-boundedness concerns are supported by L12–L13 and should be labeled as such. |

### Suggested replacement for E26's mathematical body

“Alors la suite spectrale implique” uses the local vanishing below2d to give the degree2d edge isomorphism and hence a global supported class. The separate Kummer NB is conditional on a global β in H¹_Y(X,G_m), and its image-zero conclusion concerns the resulting degree-two Kummer class. It should not be applied to arbitrary codimension-d classes merely from the edge isomorphism. The support-forgetting or support-enlarging maps also need their actual support families specified.

## 2. Additional late-page issues not fully covered by L11–L16

### Q01. Derived Hom and the two spectral sequences

**File/scans:** 33:040, lines2–14 and29–38. **Kind:** unproved claim / reading question.

The formula using `C^bullet(G^bullet)` needs a resolution convention that actually computes derived Hom; termwise injectivity alone in an arbitrary unbounded complex is insufficient, whereas a K-injective target supplies a modern construction. The boxed global/internal-Hom identity is a legitimate equality of derived objects and should not be confused with the separate ordinary-Hom=Ext⁰ statements on18–22. The two spectral-sequence sketches need their totalization and convergence conditions recovered; the first displayed exponents remain `*|p+q` and `1|q`, and “pris terme à terme” does not define the whole second construction. The shifts `(i)` in20–22 are indicated by the Ext relation as complex translations, not silently identified with the Tate twists elsewhere.

**Primary comparisons verified in this QA:** The Stacks Project Authors (n.d.), §21.35 [Tag08J7](https://stacks.math.columbia.edu/tag/08J7), §21.36 [Tag0B6E](https://stacks.math.columbia.edu/tag/0B6E), and §21.32 [Tag07A9](https://stacks.math.columbia.edu/tag/07A9); the ringed-space local-to-global Ext formulation in §20.43 [Tag0BQP](https://stacks.math.columbia.edu/tag/0BQP) explicitly qualifies convergence. These give comparisons and sufficient frameworks, not a decipherment of the draft's exponents.

**Context:** `same_cote_33/MPL_33_098-146_notes.md`, N05, scan104, records bounds for global hyper-Tor/internal Hom; N07, scan106, records the internal-Hom comparison and localization; N34, scan144, records a different missing-H⁰ type issue. Current040 adds an antecedent with explicit spectral-sequence sketches, rather than repeating the later N34 anomaly. Bears on registered **MPL_33_098-146 N08** through boundedness and on the S19 comparison programme.

### Q02. Cohomology of the derived functor is not its value on an arbitrary complex's terms

**File/scan:** 33:042, lines9–12. **Kind:** reading question.

The equality `mathcal H^i(R_!f_*)=R^i_!f_*` naturally identifies the derived functor's cohomology on degree-zero sheaves with the previously defined cohomological functors. It should not be used to replace the hypercohomology of an arbitrary input complex by a single higher direct image of one of its terms or cohomology sheaves. The source suppresses the input, so this is a scope convention to recover, not a correction to a displayed argument.

**Context:** same-cote N11, scan112, and N33, scans138–142, already distinguish literal shorthand from a type-complete derived formula; current042 adds the heart-versus-complex convention. No registered theorem settles the intended convention; relates to **MPL_33_098-146 N08** and S19.

### Q03. The D⁺ base-change argument omits a dévissage step

**File/scan:** 33:044, lines15–27. **Kind:** unproved claim.

The comparison starts with an object `F^bullet` of D⁺, while `(*_i)` is written for a sheaf `F`, and “puisqu'on sait que les (*_i) le sont” suppresses the passage between these cases. A bounded-below hypercohomology spectral sequence or compatible truncation argument supplies that passage, rather than the false identity H^i(Rf_*F^bullet)=R^if_*F. This is an omitted proof step inside the displayed D⁺ claim, separate from L14's modern extension to all D.

**Primary comparison verified in this QA:** The Stacks Project Authors (n.d.), Lemma13.21.3, [Tag015J](https://stacks.math.columbia.edu/tag/015J), provides the bounded-below spectral sequences with finite induced filtrations. The argument still requires compatibility of the comparison map with those constructions.

**Context:** same-cote N12, scan114, explicitly leaves functoriality for derived categories to verify; N04/N07, scans104–106, concern the later base-change/internal-Hom framework. Current044 adds a distinct elementary dévissage obligation. Bears on registered **MPL_33_098-146 §76**, with no status change.

### Q04. The relative duality displays have a base-sheaf mismatch and a surviving shriek

**File/scan:** 33:048, lines12–20. **Kind:** reading question.

The left argument R^if_!F lives on the base S, while the displayed coefficient sheaf is `(Z/nZ)_X` in14 and18; the meaning of Hom also needs to be internal/sheaf-valued to match the sheaf on the right. Line16 retains an exclamation mark in R^(−i)_!f_*(DF) even though it is cancelled in the neighboring duality displays14 and18. Therefore the claimed local constancy of that compact-support term cannot simply be described as the immediate cohomological consequence of the displayed ordinary-direct-image duality; the intended inherited hypotheses or the notation discrepancy must remain explicit.

**Context:** same-cote N30, scans136/140/142, carefully separates ordinary and compact-support finiteness, and N39, scan146, records a source-level factor mismatch. Current048 adds two different literal type/support questions and does not repair either from the context. Bears on registered **MPL_33_098-146 N30**; no claim that the broader duality theorem is false.

### Q05. Recovering Artin finiteness is asserted, not proved on this page

**File/scan:** 33:048, lines2–10 and20–22. **Kind:** unproved claim.

“On retrouve le th. de finitude de Artin” suppresses the passage from compact-support finiteness through duality and the inherited coefficient/smoothness/constructibility hypotheses. The following change from cancelled “finitude” to the uncertain insertion “constructiblt.|constructibilité” matters to the final partial-range claim. L16 correctly tests only a stronger local-constancy interpretation and leaves the plausible weaker constructibility interpretation unresolved; do not present its example as a refutation of the literal ending.

**Context:** same-cote N19, scans112/120, distinguishes the precise locally constant scope; N30, scans136/140/142, identifies a separate finiteness need. Current048 adds this compressed deduction and partial-range proposal. Bears on registered **MPL_33_098-146 N30**, without upgrading the earlier lead.

## 3. Nonduplicated standing-question table: all handwritten scans002–048

“Unproved” here means no proof is supplied at the stated locus, not that the statement is presently unknown. The strict authorial uncertainties/expectations are distinguished from claimed easy proofs, announced exposition, ordinary hypotheses, documentary amendments and the author's expressed judgment of usefulness. The typed sources009 and047 are deliberately excluded from this handwritten table and are handled in the reused-source memo.

| ID | Scan and exact TeX lines | Brief source words | Classification | Disposition / research item |
|---|---|---|---|---|
| H01 |002:3–9|“Étendre le formalisme à des coefficients l-adiques”; “Appliquer les résultats au formalisme des fonctions L”|Announced programme, not a claim of completion|E01; the opening programme is taken up later but no completed adic passage follows merely from it.|
| H02 |004:14–16|“d'où les cor. habituels”|Compressed consequence; proof omitted|E03; no literal authorial uncertainty.|
| H03 |004:43|“n'a pas vraiment d'analogue complet” [the two readings are uncertain]|Conceptual qualification, not an unsolved-step marker|E03; do not turn the reader's word doubts into the author's doubt about a theorem.|
| H04 |006:28|“Utilise en plus [résolution sing. pour l'hyp.] … de projectivité”|Explicit proof dependency; small wording uncertain|E05/L01; the precise resolution/projectivity route is not written out.|
| H05 |006:30|“Gaga plus complet : O.K.”|Claim of assent, not a self-flagged doubt|E06/L01–L03; the scope is questionable despite the author's assent.|
| H06 |008:13|“À prouver que ce sont des isomorphismes”|Explicitly unverified step|E07; both comparison maps remain to be proved here.|
| H07 |008:15|“Devrait aussi se généraliser au contexte rigide analytique”|Expectation / conjecture|E08; no rigid statement or proof is supplied.|
| H08 |008:17–23|“Passant à la limite … on trouverait alors”|Conditional consequence; verification deferred|E09; comparison and neighbourhood continuity are both needed.|
| H09 |010:14|“il y a un abaissement dans le cas affine, qui peut donner des idées fausses”|Warning about interpretation, not a doubtful vanishing claim|E11; distinguish the warning from the reader's uncertain inequality in8.|
| H10 |012:41–42|“cf SGA 1962 ou Notes Hartshorne 1961”; “Suite … exacte … spectrale”|Reference/development outline|E12; external source leads and a compressed localization argument.|
| H11 |012:52 →022:8–43;024:3–38|“Donner définition de la classe fondamentale locale”|Deferred editorial/expository task|E13; definition is supplied later, presentation-independence is separately asserted.|
| H12 |014:28|“Dém presque immédiate par th. du changement de base”|Claimed short proof; omitted detail|E14; no literal doubt.|
| H13 |014:30–34|“Pb sans hypothèse de lissité remplacée par hyp. de régularité”; “quand on dispose de la résolution des singularités (Artin)”|Explicit problem with a conditional claimed route|E15/L04; uncertain scope insertion remains uncertain.|
| H14 |014:36–37|“Il y a aussi un th de pureté relatif sur une base quelconque”|Unproved existence claim|E15/L04; no fully specified relative theorem on this locus.|
| H15 |014:42|“Extension aux div. à croisements normaux”|Unworked extension programme|E16; precise target assertion is not stated.|
| H16 |016:26 →018:3–11|“[Question] de la généralisation”; “Se résoud par l'affirmative lorsqu'on dispose de la résolution des singularités + pureté”|Explicit extension question and conditional claimed solution|E17/E18; coefficient restriction is essential.|
| H17 |018:26–28 →020:3–4|“de façon quasi-triviale du th. du changement de base”; “indépendant du choix de la factⁿ”|Compressed proof of compactification independence|E19; comparison coherence is not expanded.|
| H18 |020:23–35|“on a un hom. can.”; “d'où la covariance”|Construction and consequence asserted|E20; the étale trace/descent check is omitted, not marked doubtful.|
| H19 |024:36–38|“on prouve que cette section ne dépend pas du choix des Y_i”|Unproved presentation-independence claim|E22/L05; key gluing input.|
| H20 |026:3–18|“propriétés caractéristiques”; “sans dim. excédentaire”|Unproved characterization with an explicit restriction|E23/L06; the restriction is a hypothesis, not a conjectural qualification.|
| H21 |026:24–28;034:27|“Compatibilité pour n variable”; “La ‘bonne’ classe se trouve dans … Z_ℓ(d)”|Compatibility asserted / adic programme|E24/E32/L07; no full adic limit proof is supplied.|
| H22 |026:33–46|“Supposons … i<2d”; “C'est la situation du th. de pureté, vrai”|Hypothesis and claimed cases, not an explicit doubt|E25; preserve the weaker low-degree range, especially for normal codimension one.|
| H23 |028:2–18,21–23|“Alors la suite spectrale implique”; “N.B. [si] …”|Compressed implication and a separate conditional Kummer observation|E26 as qualified in this QA; do not merge the degree2d argument with the degree-two NB.|
| H24 |028:32–38 →030:2–8;034:16–25|“Il va résulter du théorème qui va suivre”; “on avait vérifié directement”; “On avait vérifié simplement”|Future theorem promised; earlier curve check reported|E27; framework appears within the package, but the full general trace proof is absent.|
| H25 |032:16–17|“on définit de façon évidente … sur les divers morceaux”|Claimed evident piecewise construction|E29; distinguish local dimensions from a uniform amplitude bound.|
| H26 |032:22–23 →034:2–21|“on peut définir un … hom. canonique”; “Ext. de base”; “Ces conditions caractérisent les hom Tr_f”|Existence, compatibility and uniqueness asserted|E30/L08; “Ext.” here is extension of base, not an Ext functor.|
| H27 |034:24–25|“Si f est à fibres conn. non vides, alors Tr_f est un Isom.”|Claimed theorem under a shorthand hypothesis|E31/L09; geometric-connectedness convention needs recovery, not a literal doubt marker.|
| H28 |036:40–43|“Compatibilité avec les hom traces”; “S'exprime plus aisément quand on dispose de la catégorie dérivée, et s'énonce sous forme plus complète”|Explicit deferred reformulation and unproved compatibility|E33/L10; derived formulation announced next.|
| H29 |038:24–29|“définition directe via résolutions injectives”; “ou … passage au quotient”|Construction alternatives in the flat case|L11; do not misclassify “injectives” as a mathematical error when pullback is exact.|
| H30 |038:31–38|“on ne peut en général définir raisonnablement”; “Rien n'empêche de construire un dérivé droit, Rf*, mais il n'a pas le moindre intérêt”|Range limitation and author's judgment of usefulness|L11; the margin is not an open problem or an assertion that Rf* cannot exist.|
| H31 |038:39–47|“on explique comment construire raisonnablement”; “Ce n'est que si f est de ‘Tor-dim. finie’”|Promised construction plus boundedness condition|L11; modern all-D existence must be separated from preservation of D⁺/Dᵇ.|
| H32 |040:2–14,29–38|“Définition de”; “lié au précédent par”; “pris terme à terme”|Compressed definitions/comparisons, not explicit doubt|Q01; resolution and convergence hypotheses are not supplied on this sheet.|
| H33 |042:15–21|“Reformulation des propriétés [connues]”; “Compatibilité avec extension de la base”|Claimed known properties reformulated|No literal admission of uncertainty; the uncertain word is the reader's. Q02/L12.|
| H34 |042:23–36|cancelled “f est à fibres de dim bornée”; inserted “Y est quasi compact”; “Cela résulte du fait que … de dim coh. finie”|Documentary hypothesis replacement and compressed proof|L12/L13; the replacement gives a route to uniformity, not a retraction of bounded-fibre sufficiency.|
| H35 |044:26–27|“Lorsque f est propre ce est un Isom, puisqu'on sait que les (*_i) le sont”|Claimed proof by cohomological detection|Q03/L14; the bounded-below complex dévissage is omitted.|
| H36 |046:2|“Le th de dualité globale : énoncé général pour un morphisme lisse compactifiable”|Heading announcing exposition|L15; the sheet does not actually contain the theorem, and section19 is not a page count.|
| H37 |048:10|“On retrouve le th. de finitude de Artin”|Claimed consequence with no written derivation|Q05/L15; inherited finiteness and duality hypotheses matter.|
| H38 |048:12–20|“si les R^i_!f_*(F) sont loc [constant\|constants]”; “ce qui implique”; cancelled “finitude” replaced by “[constructiblt.\|constructibilité]”|Conditional consequence and documentary revision|Q04/Q05/L15; the source's sheaf-base and shriek inconsistencies remain visible.|
| H39 |048:22|“On peut généraliser … pour i≤i_0, la conclusion … pour j≥2d−i_0”|Asserted generalization; exact antecedent unresolved|L16/Q05; n'est/est and vaut/reste are reader doubts, and the constructibility/local-constancy distinction must remain explicit.|

The separate cancelled-presentation episodes are006→008,014→016→018,036 within the sheet, and the smaller hypothesis/wording replacements listed above. None supplies an authorial sentence saying that the cancelled mathematical content is false. No literal “à vérifier,” “sauf erreur,” “je présume,” or “admis” appears in this frozen handwritten sequence; the actual explicit flags are those quoted here.

## 4. Primary verification record for the new QA points

All retrieved on 2026-11-15. APA author-date form: **The Stacks Project Authors. (n.d.). _The Stacks Project_. Retrieved November 15, 2026, from the cited stable tag URL.**

| Tag | Exact inspected locator | What was checked | Tool reference for parent reopening |
|---|---|---|---|
|08J7|§21.35, construction before Lemma21.35.1|Internal derived Hom uses a K-injective target; arbitrary first representative is allowed in that construction.|turn63view0|
|0B6E|§21.36|Global RHom equals derived global sections of internal RHom; H^p recovers Ext^p.|turn64view0|
|07A9|§21.32, Example21.32.1|Two Ext spectral sequences under a bounded-above input-complex hypothesis.|turn63view1|
|015J|Lemma13.21.3|Bounded-below Cartan–Eilenberg hypercohomology spectral sequences converge with finite filtrations.|turn63view2|
|0BQP|§20.43|Ringed-space local-to-global Ext spectral sequence with a sufficient boundedness/convergence condition explicitly stated.|turn63view3|

The context searches for Q01–Q05 and the three requested early-item checks are recorded independently in `research_handwritten_qa_searches.json`. They document matches, not assertions that every lexical hit establishes a mathematical relationship.


## 5. Review of the assembled final research notes

Review time: 2026-11-15 13:49:52 UTC. Reviewed the assembled `MPL_33_002-049_notes.md`, all 86 item metadata records, all 95 search-ledger entries, complete register-disposition table, the standing-question section, all nine title/count items, and the higher-risk bodies N10/N26/N36/N49/N50/N51/N82/N85/N86 plus reused-source attribution items.

### Required metadata correction, now verified resolved

- The first review found that LM4 F.7's “cote 30” should be “§30,” and LM4 D.12's “cote 25 bis” and “cote 30” over-specified the supplied untyped locators. A subsequent direct check of the assembled notes verified that the parent had corrected F.7 to **§30** and D.12 to neutral **locator “25 bis” / locator “30”**, with an explicit caveat that the supplied excerpt does not identify archive cotes. This citation-locator issue is resolved; no result status changed.

### Checks passed

- All 32 bold entry IDs from the supplied RESULTS_STATE bullet register occur in the disposition section. Open, proved-run-claim, first-pass-lead, unchecked-plan and intake-not-referee distinctions remain intact; the general referee paragraph is not improperly applied to C.6 or the open rows.
- There are 86 distinct N-items and nine T-items, with no nonexistent N reference found. Body-level internal crossreferences, including N26→N86, N50→N49, N59→N80, N62→N60/N61, N69/N70/N73→N68, and N77→N76, point to the intended topics.
- Every N/T item has one ledger entry and searches all three supplied context files: 95 entries, 285 item/file searches. No missing or duplicate item identity was found.
- **N26 and N86 now correctly separate the codimension-d edge construction from the conditional degree-two Kummer image-zero observation.** N36 accurately preserves the X/Y–Y/X discrepancy without deciding the gamma/sigma glyph.
- **N49 and N50 retain the crucial antecedent distinction.** The punctured-plane example excludes the stronger local-constancy/degreewise-duality interpretation, and explicitly does not refute the plausible constructibility conclusion.
- N51 and N85 retain the two independent source-target/support discrepancies on 048. N40 does not mistake the flat-case injective-resolution wording for an error.
- The standing section captures the literal explicit questions, promises and uncertainty, and separates non-flags in its following paragraphs. Its 19-row short index is supplemented by the 39-row handwritten audit above; the latter also records ordinary hypotheses and omitted-proof phrases and is intentionally broader.
- Title/count verification against frozen text and inventory passes: 48 scans; 24 text, 23 reused_typed, 1 cover; 688 elements with the listed category counts; all marked yes. All 48 mspage entries equal scan−1, with 039 retaining “38.”. All 17 n°391 printed-page mappings match the frozen files, and the four English page numbers 40/34/38/39 are correct.
- The section 19 heading on 046 is not called a page count; no unwritten total is inferred. Tribu 62, n°391, Gray and EGA source identities remain appropriately qualified. Reused/cancelled claims are not silently assigned to the handwritten author's research programme.

### Optional clarity improvements, not blockers

1. N10 could end with an explicit “see N38” crossreference, since N38 now supplies the decisive fixed-ring-freeness scope test; the current text is not false, but a reader should not miss that the issue is actually tested later.
2. In N26's first sentence, identifying its analysis variable F with the written coefficient sheaf μ_n^(⊗d), or saying explicitly “for the displayed coefficient sheaf,” would keep the generic mathematical notation from looking like a transcription of an additional F.

All 49 frozen hashes were rechecked unchanged during this review. No assembled notes, page files, inventory, doubts file or progress log was edited by this reviewer.
