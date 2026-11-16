# Author flags, revisions, titles, and sheet register

## Scope and citation convention

This is a text-only research inventory of **all 46 frozen fragments**, cote **43**, scans **94–142 excluding 99, 111, 127**. The frozen combined file is 90,482 bytes, SHA-256 `8cc87ac8ae8524120878313eac5ae82f44f3905d93d1812d9c0d34f034c0ece5`; the freeze recorded by the project is **2026-11-16 23:04:08 UTC**. No scan image was read for this inventory, and no page, combined transcription, doubts file, or inventory was changed.

A locator such as **43:98:L12–19** means cote 43, scan 98, physical lines 12–19 of `pages/MPL_43_094-142_43_scan098.tex`; the `\scanpage` line is line 1. Quotes are short extracts of the frozen text. The visible-number discussion below reports the **transcribed marks**, not a new visual attribution of their hand or purpose. Symbols inside `\unsure{...}` remain uncertain readings; that editorial wrapper by itself supplies no evidence that the writer doubted the mathematics.

I read `context/README.md` and `context/notes/RESULTS_STATE.md` before using the context, then read every frozen fragment and searched the supplied context. The companion JSONL contains 46 page-specific query groups **P094 … P142** and nine refinements **R01 … R09**, with exact queries, counts, matching locators, bounded excerpts, and extraction limits. Every flag and correction below inherits its scan's P-query group; the final revision census explicitly associates all encoded deletions and insertions with those same searches. Literal searches include cancelled text and bibliographies, so an occurrence is classified by its local context before it is used.

**Evidence status.** The README calls the earlier `MPL_16+47+54+44` transcription, doubts, and research notes first-pass material, not a newly audited witness. This inventory uses their literal text and retains the prior notes' status as leads. `RESULTS_STATE` labels are retained exactly at the level available in that file; unseen source packages named there have not been read. Oda's supplied PDF is a printed primary witness, searched through `pdftotext -layout`, with no OCR or image inspection. The PDF extraction has 74 text pages, including its cover; two extraction warnings and line-wrap limitations are recorded in the JSONL.

## Context comparison key

Here **T** = `context/MPL_16+47+54+44_transcription.tex`, **N** = `context/MPL_16+47+54+44_notes.md`, **D** = `context/MPL_16+47+54+44_doubts.md`, **S** = `context/notes/RESULTS_STATE.md`, and **O** = `context/Oda_1969_first_de_Rham_cohomology_Dieudonne_modules.pdf`. These are file names, not independent authorities for every assertion in the earlier notes.

| Key | Exact supplied comparison points and their scope | Search and status limits |
|---|---|---|
| **K1 — derived functors** | T **16:30**, lines 1221–1233, gives the complex built from `H^s(K^{\otimes r},G_m)` under a purely inseparable field extension and calls it acyclic. T **16:37**, lines 1451–1461, gives the injective-hull sheaf construction through stalk maps; **16:39**, lines 1528–1540, discusses Matlis injective hulls; **16:41**, lines 1589–1611, treats coherent internal Ext and a boundedness exercise for derived Hom. O **PDF p.57**, lines 3–14, invokes a generalized Leray spectral sequence for hypercohomology. | P094–P098, R01, R06. Exact searches `Greenberg`, `Néron-Weil`, `application continue`, `transforme injectifs en injectifs`, `Hom_{S/k}`, and `acyclique` found no matching context line. The cited constructions supply specific comparison material; this inventory establishes no map identifying them with the functor under examination in 43:96–98. N **16:30:1**, **16:37:1**, **16:39:1**, **16:41:1** remain prior research leads. |
| **K2 — Witt and finite-group objects** | O **PDF p.19**, printed p.80, §3 lines 30–45, introduces the perfect field, the infinite Witt ring scheme, its operators, and the length-`n` Witt schemes; **PDF p.3**, lines 25–43, announces the Dieudonné functor and Cartier-dual computation of Theorem 3.19. | P096, P102, P112, R07. These are object-level matches for Witt/finite-group calculations. The exact local quotient `W_n(K)/F^mW_n(K)` and the 43:102 question were not located by the recorded queries; no equality with the source's `\mathbb V` functor is asserted. |
| **K3 — Fourier and shifted duality** | T **47:3–4**, lines 2087–2215, constructs `\Phi_\mathcal L` and a convolution/tensor comparison; **47:6**, lines 2300–2324, records a shifted direct image with a determinant line; **47:11**, lines 2550–2557, records the checked-input/dual-output formula with `[n]`. | P100, P106, P114, P130, P136, P138, R06. N **F6** and **F7** retain the admitted lemma and unfinished compatibility check at **47:7–8**; N **F20** is labelled an editorial reconstruction and has an unresolved convention for the checked input. No specific comparison morphism to the local/global Ext diagrams of cote 43 is proved here. |
| **K4 — Cartier, Frobenius, abelian duality** | T **54:3**, lines 2611–2652, displays the Hodge/tangent extensions and asks for the duality proof; **54:5**, lines 2694–2701, compares Cartier duality and Frobenius kernels; **54:7**, lines 2716–2730, gives the Frobenius–Verschiebung diagram and ends with a reconstruction question. O **Theorem 1.1**, **Corollary 1.3**, and **Theorem 3.19** are named comparison results located by R07. | P109, P112, P117, P119, P120, P132, P133. N **D01–D05** are earlier research claims/leads; their stronger interpretations are not promoted to newly checked results by this inventory. The correspondence of particular pairings and degree shifts remains an item for the main mathematical notes. |
| **K5 — Jacobians and Néron words** | T **44:2**, lines 2782–2803, is headed “Programme de travail” and contains Th.1–4; **44:4**, including its “Néron” margin, and **44:8**, lines 2974–2979, discuss cycle Jacobians and openly unproved statements. T **16:21**, line 886, uses “Néron--Sévéri”. | P096, P102, P122, P131, P133, P142. S **WG2 §2.3 #12** is an **unchecked question/plan item**; **WG H9** is an **unchecked hunch**. The shared names are reported with their objects; they are not used to settle the Néron-functor, local-class-field, or curve-duality checks in this packet. |
| **K6 — flatness and completion** | T **54:4**, lines 2658–2677, contains cancelled and revised generic-freeness/flatness material; **54:6**, lines 2707–2710, gives Proposition A and its amended universal flatness condition. T **44:3**, lines 2809–2840, contains a cancelled graded-completion argument and a surviving marginal exactness/faithfulness assertion. T **16:56**, lines 2032–2040, records faithfully flat descent and completed-local-ring statements. | P108, P110, P115, P116, P121, P125, P129, P134, P137; R03–R04. N **D06–D07** are earlier research leads. Searches `Cohen`, `équidimension`, `associated prime`, `\operatorname{Ass}`, and `semicontinu` return no matching context line; `Ass` occurs in a tensor-associativity label at 47:4. The specific length inequality and associated-prime question at 43:110 remain separately located. |
| **K7 — ramification and class-field references** | T **16:52**, lines 1912 and 1920–1922, plans the different/trace comparison and a Kummer description of totally tamely ramified extensions. T **16:28**, lines 1159–1177, and O **PDF p.74**, line 15, contain class-field bibliographical entries. | P102, P113, R09. S **CYCLOTOMIC_KERNEL C1**, **LM6 B.22**, **LM6 F.43** retain their labels **Proved (the return's claim)**; **FLAGGED_149 B9** and **LM6 B.27** retain **Open (the return's claim)**. Their source documents are not supplied. No status change follows from the cancelled inertia/Galois text at 43:113. |
| **K8 — support and formal completion searches** | The precise graded-completion witness is T **44:3** (K6). O **PDF p.44**, lines 37–45, calls two Picard-group objects formal completions at the origin; O **PDF p.73**, lines 43–44, contains the bibliographical entry *Local cohomology*. | P123, P125, P135, P136, P138, P140; R04, R06. The `local cohomology` hit is a bibliography entry. Searches `i_!`, `j_!`, `H_U`, `H_Y`, `H_x`, `triangle exact`, `hensel`, and `hensél` found no matching supplied-context line. These limited text searches furnish no answer to the particular arrows/shift question. |
| **K9 — typed-sheet and title comparisons** | T **47:2** has the convolution/Fourier cover title; **54:2** has the uncertain “Dualité en Cohomologie des V. A.” title; **44:2** has “Programme de travail”. S **WG2 §1.1 #3** describes a folder-level plan and is **unchecked**. | P101, P103, P105, P118, P122, P124, P126, P131, P134, P137, P139, P141, P142; R02, R08. `S-homotopy`, `intrinsic join`, `Stiefel`, `James`, `Spanier`, `Cassels`, `Schémas de Hilbert`, `Fidèle platitude`, `faisceaux mous`, `faisceaux fins`, `III-49`, `III-42`, and `n° 239` had no exact match. Broader `Lang` and `Df` searches produced bibliographical/differential-text hits; these do not identify the reused typescript. |

The context corpus therefore supplies concrete neighboring constructions and bibliographical leads, alongside many exact no-matches. A no-match here means only **no line matching the recorded literal or regular expression in these supplied text representations**; it makes no claim about all mathematics, all archive sheets, or an unseen cited work.

## A. Author questions and explicitly deferred work

The following entries include every explicit author question-mark locus, every located “admet…”, “à vérifier”, “J'ignore”, “faudrait”, “sans doute”, and comparable deferred-proof instruction, plus the distinct uncertainty clauses on the reused English typescript. “Possible reading” means the decisive word or sign is itself inside `\unsure` in the frozen text. Administrative and chapter-placement questions are kept in the census with their actual scope.

| ID | Frozen locus and short quote | Mathematical or documentary scope; context result |
|---|---|---|
| **F01** | **43:94:L32–42**, “Il faudrait prouver alors que” | The requested proof concerns comparison of the displayed `H^i(k,G)` with the corresponding sheaf cohomology and then the parallel Ext comparison, with perfectness of `k` written into the request. The earlier “règles de calcul” is part of that program. **P094; K1**: no exact quasi-group/Galois-comparison wording located. |
| **F02** | **43:95:L2–4**, “Il faudrait aussi … étudier”; “cohomologie galoisienne” | The author explicitly leaves open the calculation of `H^i(k,G)` by Galois cohomology in the “quasi” setting. **P095** returns no occurrence of the exact French or English Galois-cohomology query in the supplied representations; **K1** contains a nearby, explicitly specified cohomological construction. |
| **F03** | **43:96:L21–24**, “application continue”; “formelles … ! ? !” | The punctuation accompanies the proposed continuous-map interpretation and direct-image explanation of the Néron functor's formal properties. **P096, R01; K1–K2** give no matching `application continue`/Greenberg statement; the punctuation belongs to the transcribed margin, outside `\unsure`. |
| **F04** | **43:97:L19–27**, “transforme injectifs en injectifs”; “à vérifier” | Preservation of injectives by `\mathcal N` is explicitly pending; the attempted adjoint argument that follows is cancelled. **P097; K1**, especially T 16:37–39, supplies injective-hull constructions but no identification with this functor. |
| **F05** | **43:98:L12–19**, “si on admet”; “vérifier” | The first spectral sequence is introduced through the acyclicity of internal `Hom_S(F,G)` for the relative `H^0_{S/k}` functor when `G` is injective. The extra phrase “et pour `H^0_S`” is cancelled at L14. **P098; K1** retains both the stated acyclicity condition and its unsettled status. |
| **F06** | **43:98:L26–32**, “et admettant”; “vérifier” | A second, separately marked gate is the acyclicity of `Hom_{S/k}(F,G)` for `H^0(k,-)`, used for the following global Ext spectral sequence. **P098; K1**: the two gates should retain separate locators and functors. |
| **F07** | **43:102:L9–12**, marginal `?`; “10) Application 2” | The question mark is next to the outline's proposed autoduality application involving `W_n(K)/F^mW_n(K)` after a cancelled `H^1` formulation. Its exact attachment is reported by proximity in the frozen stream. **P102; K2** locates Witt objects in Oda, without a matching local-quotient statement. |
| **F08** | **43:102:L24–28**, marginal `?` at L26 | This mark accompanies the comparison and the positive-degree claim about `k`-groups and the written `J(K)/J(V)'` expression. **P102; K5, K7** finds Jacobian/class-field words, but no located proof of this particular comparison. |
| **F09** | **43:104:L2–3**, circled “parfait ?” | Perfectness is explicitly questioned beside the `k ← V → K` setup. **P104; K2** records Oda's explicit perfect-field framework, which is a hypothesis at that cited locus; no morphism comparison settling this margin is supplied. |
| **F10** | **43:104:L20–29**, “`T^0` transforme injectifs en `\Gamma^0_k`-acycliques ??” | The double question mark is attached directly to property (i). Properties (ii), concerning cohomological dimension, and (iii), concerning residue-field extension, stand under the same proposed-property block; they have no separate question mark. **P104; K1–K2** preserves that distribution of the evidence. |
| **F11** | **43:106:L29**, “Comment obtient on le carré du bas ?” | The open construction is the lower square linking the named Cartier/Serre/Pontryagin dualities and derived functors; the following Ext formulas are the author's working route. **P106; K3–K4** supplies explicit duality diagrams in the context, without a verified identification of this square. |
| **F12** | **43:110:L4–16**, marginal `?` at L16 | The question mark sits with Proposition 6.7, its fibre-length upper-semicontinuity claim, and inserted hypotheses. **P110; K6** locates other flatness drafts, while the stated inequality and its hypotheses remain specific to this reused typed sheet. |
| **F13** | **43:110:L19–23**, “(réf)” twice; “il reste … à prouver” | Two references are placeholders: constructibility of the length function and the reduction to a specialization/DVR argument. The proof then begins; the placeholders themselves are not citations to identified results. **P110; K6** has no exact `longueurs`/semicontinuity match. |
| **F14** | **43:110:L60–62**, “J'ignore si les assertions sont vraies” | The author explicitly questions the assertions without already assuming flatness over `Y` at maximal points of the fibre `X_y`. This uncertainty governs a substantial hypothesis issue, not an editorial illegibility. **P110; K6**; the main notes separately examine the literal flatness conclusion at L35–36. |
| **F15** | **43:110:L62–65**, “Question liée”; “prouver `\mathfrak m\in\operatorname{Ass}M/tM` !” | This is the linked local-algebra problem, with a noetherian local ring, module, element `t`, associated-prime condition, full support, and a written dimension condition; some individual symbols remain uncertain. **P110, R03; K6** returns no `associated prime` or `\operatorname{Ass}` context match. |
| **F16** | **43:112:L39–42**, `??` in the `G_m` row | The two question marks are beside the oval containing `K^*` and `0` in the Greenberg/cohomological table. **P112; K2, K4** supplies finite-group and Witt comparison objects, not a located resolution of this table cell. |
| **F17** | **43:112:L44–47**, `\mathbb Z\qquad??` | The second questioned row is the `\mathbb Z` calculation, alongside its following `H^1(K,\mathbb Q/\mathbb Z)` term. **P112; K1–K2** keeps the two questioned rows separately located. |
| **F18** | **43:116:L40–44**, cancelled “J'ignore”; “équidimensionnalité” | A cancelled Remarque 2.7 asks whether the equidimensionality conditions of “1.1. ii)” are essential, and adds a reference to equality in 2.6; the same deleted block names Proposition 2.8 on continuity of Cohen–Macaulay properties. **P116, R03; K6** yields no exact equidimensionality/Cohen match. The cancellation is recorded without assigning a reason for it. |
| **F19** | **43:118:L7–9**, `\unsure{(?)}`; “Pourrait passer au Chap 0 ?” | The first sign is an uncertain reading beside “Morphismes réguliers”; the clear second question concerns placement of that topic in chapter 0 of a cancelled outline. **P118, R08; K9** gives no matching chapter-placement note. This is a structural-plan question. |
| **F20** | **43:118:L48–59**, “Bott September 1963 ?” | This question belongs to the cancelled administrative list, alongside “James September 1963” and talk/mailing-list items. **P118, R02, R08; K9** finds no matching list; the date string is recorded as text and supplies no chronology for the surrounding mathematical sheets. |
| **F21** | **43:120:L44–49**, marginal `?` after (ii) | The mark follows the displayed `H^1(K,{}_nB)`/`Ext^1_{k-gr}(\mathcal A,\mathbb Z/n\mathbb Z)` comparison. The neighboring divisibility/torsion-freeness statement (i) and incomplete (iii) are retained separately in its local scope. **P120; K4** locates dual abelian finite-group material; no matching local-field formula was found by R06. |
| **F22** | **43:121:L36**, `\unsure{Joube\|doute}` | This margin may read “doute”, but the frozen alternatives do not justify counting it as a secure author doubt. The nearby text is the Euler-characteristic/Hilbert-polynomial discussion, with a separate leading-coefficient correction. **P121, R08; K6, K9**: no exact `Euler-Poincaré` or `III-42` match. |
| **F23** | **43:123:L7–9**, `\operatorname{Ext}_{\unsure{m}}(M,A)\overset{?}{=}D(M)` | The equality to the dual object is explicitly questioned; even the Ext subscript remains a transcription uncertainty. **P123; K8** has a completion witness and a local-cohomology bibliography entry, with no located answer to this particular equality. |
| **F24** | **43:123:L24–32**, two arrows labelled `?`, then `\unsure{U}\ ?` | The questions concern arrows between Ext groups for nested supports/formal neighborhoods and the underwritten `U` location; all three literal signs are retained as distinct positions. **P123; K8** records the precise limited search and the shared completion objects. |
| **F25** | **43:125:L24–31**, the final arrow `\overset{?}{\mathrel{-}}` | The author questions the final comparison after the displayed support-cohomology map from a formal scheme to its completion along `Z`; the target expression is unfinished. **P125; K8** locates graded and Picard completions, but no matching arrow statement. |
| **F26** | **43:128:L8**, “définis comme les `C`-groupes ?”; “Cela est-il équivalent … ?” | Two explicit questions concern the definition of `k`-groups and comparison with Weil functors/schemes on algebraic `k`-sets. **P128, R05; K3** locates “faisceau de Weil” at T **47:3, 47:6** for an invertible kernel; this inventory establishes no equivalence of the source definitions from those word matches. |
| **F27** | **43:128:L18**, `\unsure{nous admettrons}`; finite `dim \unsure{ch.}` | The text admits finite cohomological dimension of `f_*` while setting up its derived functors on complexes bounded to the left. Both the admission phrase and abbreviation have editorial uncertainty, which remains visible. **P128, R05; K1, K3** yields no literal `cohomological dimension` statement for this functor. |
| **F28** | **43:129:L42–43**, `\unsure{(Montrer} … propriétés)` | Within a wholly cancelled draft, the concluding transfer of properties along polynomial extension is followed by an uncertain instruction to show it for certain properties; the list of properties is absent. **P129; K6** provides related local/regularity material, with no specific named property supplied for this gap. |
| **F29** | **43:130:L3–12, L19–29**, “il reste à définir”; “si nous définissons un élément” | The cancelled first route and the surviving replacement both isolate the trace-like map from `Rf_*S\sigma` to `\sigma` as the construction needed to obtain the displayed comparison by composition; the coefficient retains its frozen `\sigma\|\tau` uncertainty. **P130; K3–K4** supplies derived-duality material but no constructed map identified with this one. |
| **F30** | **43:130:L31–39**, marginal `\unsure{préciser}` | The margin is a possible author instruction to specify the theorem's scope, next to its successive “fini”, “affine”, “sans composantes abéliennes”, and “de type fini” formulations. **P130; K3–K4** keeps these exact restrictions; the word itself remains uncertain. |
| **F31** | **43:135:L4–12**, “On doit prouver” | The stated proof obligation is the degree-shifted Ext comparison for a Weil sheaf concentrated at a closed point, after identifying its `T(G)` value in the geometric case. **P135; K4, K8** records the comparison search; no henselian/local-support proof was located in the supplied context. |
| **F32** | **43:135:L13–15**, “Il est sans doute vrai” | The author tentatively identifies the written Ext with an Ext over the henselization of `\underline O_{C,x}`; “local” is deleted, and a finite closed-support hypothesis is inserted. **P135, R04; K8** has no `hensel`/`hensél` match. |
| **F33** | **43:135:L18–38, L45–53**, “i.e. : vérifions”; “On est ramené à prouver” | The next proof obligation is the comparison for extension by zero, followed by the boxed `H^i(U;\widehat F)`/shifted Ext formula and an exact-sequence reduction. At L51–53 the writer says it is checked by an easy calculation for `F=\mu_n`, then replaces unrestricted `n` by `n` prime to `p`; the page ends mid-continuation. **P135; K8**: preserve both the announced calculation and its narrowed range. |
| **F34** | **43:136:L31, L34–44**, `\unsure{2\|?}` on an arrow; clear marginal `?` | The arrow label at L31 has an unresolved `2\|?` reading, while the L34 question mark is clear and accompanies the comparison of exact triangles with shifts `n-1` and `n-2`. The later box at L61 writes an `m+1` shift, an internal witness relevant to reconciliation with 43:140. **P136, R06; K3, K8** provides no matched support triangle in the supplied context. |
| **F35** | **43:138:L14–18**, vertical `\simeq ?` | The question follows a cancelled isomorphism attempt below the dual localization/cohomology diagram; the displayed degrees have their own insertions above. **P138; K8** finds no matching `H_U`/support-comparison statement. |
| **F36** | **43:140:L35–39**, boxed `\overset{?}{\simeq}` followed by `???` | The precise question is the unshifted comparison between `\underline H^*_{Y/k}(i_!G)` and `\underline H^*_{U/k}(G)`. This is the main unresolved degree/support locus, to be compared with the explicit `m+1` at **43:136:L61**; the main notes separately supply a concrete degree-zero test. **P140, R06; K8**: the context's `local cohomology` occurrence is bibliographical. |
| **F37** | **43:101:L6–9**, “will be given in a future publication” | The reused typed page postpones an attack on determining the `q_k` in (6.5), through the algebraic structure of `J(X)`. This is an explicit deferral in the typed source, whose author is not named on the face; the main researcher’s external identification is documented in R03. **P101, R02; K9** finds no matching homotopy witness. |
| **F38** | **43:101:L52–53**, “It would seem reasonable to suppose” | The reused typescript proposes that the maps `Df` and `\Delta` have the same `S`-homotopy type, after its intrinsic-join and tangent-bundle construction. **P101, R02; K9**; exact homotopy terms have no context match, and differential `dF` text in the PDF is not treated as this map. |
| **F39** | **43:103:L50–52**, “we make no assertion for the case `n<2k`” | This is an explicit limitation of Theorem (6.5) in the real case, with the sentence continuing at **43:101:L4**. It limits the typed source's claim; it is not silently expanded into an author conjecture about the omitted range. **P103, R02; K9**. |
| **F40** | **43:105:L36**, “(to appear)” | The Milnor–Spanier bibliography entry carries a publication-status reservation. It is retained for exhaustive documentary coverage, with no mathematical uncertainty or manuscript date inferred from it. **P105, R02; K9**. |
| **F41** | **43:132:L23–38**, “On va définir”; “associé à un hom” | This is a construction announced for the pairing/comparison, with the auxiliary hom marked by a circled star and a final unfinished “c)”. Read with the explicit trace construction left at **43:130:L19–29**; **P132; K3–K4** supplies neighboring Cartier/Picard and derived-duality material, not a completion of the announced construction. |

### Question-mark provenance and negative census

The mechanical census finds **30 literal `?` characters** in the frozen page files. **28** are outside `\unsure` and occupy **21 scan/line loci**; the other two are the uncertain `(?)` at **43:118:L7** and the uncertain arrow label `2\|?` at **43:136:L31**. Repeated `??` and `???` are counted as characters, not as separate mathematical questions. The clear marks inside cancelled blocks at 118:9 and 118:51 remain author punctuation in cancelled material.

Words such as “on vérifie” in a supplied proof, “répondant à la question” at **43:124:L6**, and “Tout revient à prouver” followed by the typed proof at **43:141:L8–12** do not, by themselves, assert that the writer left the result unverified. They have been checked in the sequential reading and are accounted for in the sheet register. No occurrence of “je présume” was found in the frozen text. Every fragment lacking a listed flag still appears in that register; no completeness claim is made for illegible content beyond what the frozen transcription records.

## B. Explicit withdrawal and material revisions

This table gives mathematical scope to the main cancelled/replaced passages. The exhaustive macro census in section D retains **every one of the 241 encoded `\deleted` or `\inserted` occurrences**, including small verbal repairs, nested edits, and cancelled whole blocks. A whole-block cancellation records the writer's cancellation of that draft state; its presence alone does not specify the reason or prove a mathematical falsity.

| ID | Frozen locus; short extract | Scope and supplied-context comparison |
|---|---|---|
| **C01** | **43:94:L3–8**, “quasi groupes quasi-algébriques”; “finis surjectifs” | The opening object/topology description is revised through deleted nouns and a deleted “surjectifs” before the surviving finite-surjective phrase. **P094; K1** finds no matching quasi-group definition. |
| **C02** | **43:95:L9–10**, cancelled `N.B.` | The short cancelled note has uncertain wording and an illegible token. Its cancellation is recorded without extracting a definite withdrawn theorem. **P095; K1**. |
| **C03 — overt withdrawal** | **43:96:L35–38; 43:97:L2–3**, “Non, car le foncteur … ne commute pas aux limites inductives” | The writer expressly retracts the preceding compatibility-with-inductive-limits note, giving noncommutation of `\mathbb V:k-alg→V-alg.` as the reason; the cancelled sentence continues on scan 97. **P096–P097; K1–K2** preserves this stated reason and does not replace `\mathbb V` by another functor. |
| **C04** | **43:97:L21–27**, cancelled adjoint/Hom argument | The attempted argument using an adjoint `\mathcal N^*` and a Hom comparison is crossed out below the injective-preservation check. **P097; K1**; the still-visible “à vérifier” remains active evidence of the pending step. |
| **C05** | **43:98:L14, L17**, “et pour `H^0_S`”; deleted total degree | The first acyclicity assumption loses the extra `H^0_S` clause, and the following spectral-sequence notation contains a deleted degree candidate. **P098; K1**; both edits are localized rather than harmonized with the second spectral sequence. |
| **C06** | **43:100:L23, L49–56**, deleted `\Gamma_{K/k}`; inserted `R^*f_{K/k}`, `E^*` | The margin and outline record competing/revised functor labels. **P100; K3** supplies explicit derived-functor notation elsewhere, while this inventory retains the local replacements as written. |
| **C07** | **43:101:L22, L59**, plus sign; “up to homotopy type” | The inserted plus and marginal qualification limit the typed join/suspension formula's sense. **P101; K9** has no matching intrinsic-join text. |
| **C08** | **43:102:L5–7, L10, L16–17, L30–34**, “(sur corps `k` fini)” | The Lang application acquires the finite-base-field restriction; an earlier `H^1` label in the autoduality item and tensor/Hom scratchwork are cancelled. **P102; K2, K5, K7**; exact `Lang` matches in the context are kept at their own bibliographical/object loci. |
| **C09** | **43:104:L20, L24–25**, deleted “Question”; “excepte”/“exclut” | The overwritten heading and lexical correction are retained, while the double question mark on (i) remains clear. **P104; K1**. |
| **C10** | **43:106:L9, L47**, `\mathcal G` to `\mathcal C`; deleted `(-1)` | The category label is revised, and the first argument of one Ext expression loses a twist. **P106; K3–K4**; this is concrete shift/convention evidence, not a new calculation of the square. |
| **C11** | **43:107:L21, L30–38**, deleted finite-group description and pairing | The writer changes the group description to the ordinary finite group `\mathbb Z/n\mathbb Z` and replaces a pairing line. **P107; K4**; the exact old/new fragments remain in the census. |
| **C12** | **43:108:L3–36**, cancelled corollary; “propre” → “de type fini” | The entire corollary draft is cancelled; within it, properness is replaced, continuity wording is amended, and a further argument is struck. The cancelled homology diagram at L56–62 is retained separately. **P108; K6**: no matching component-count semicontinuity statement was located. |
| **C13** | **43:109:L45**, deleted `\mathbb Z/n\mathbb Z`, surviving `{}_n\mu` | The coefficient in the written Ext calculation is explicitly replaced; the page also cancels several working cohomology terms. **P109; K4** supplies Cartier-group comparison objects without silently changing this coefficient back. |
| **C14** | **43:110:L4–15, L25–36, L38–52**, added support/domination/fibre conditions | Hypotheses are materially edited; the component-domination phrase is inserted into the lemma's assumptions while a related conclusion is cancelled. **P110; K6**; the main notes examine the literal surviving flatness claim at L35–36, keeping the author's `J'ignore` at L60 in view. |
| **C15** | **43:112:L4, L13, L33, L37**, `(n,p)\ne1` → `(n,p)=1`; deleted `\wp` readings | The table has a prime-to-characteristic correction, a crossed-out `\mathbb Q/\mathbb Z` complex, and cancelled candidate operators in its `\alpha_p` row. **P112; K2–K4** records the corresponding object searches, with unresolved glyphs left unresolved. |
| **C16** | **43:113:L2–40**, cancelled Galois draft; inserted “invariant”, “galoisienne” | Inside the cancelled draft, normality/Galois qualifications are added to the generated decomposition/inertia subgroup and corresponding completely split or unramified subextension. **P113; K7** links the explicitly located ramification material and preserves the prior RESULTS_STATE labels. |
| **C17** | **43:115:L12–15, L20–29**, inserted “projectif”; cancelled deduction | The Chow-lemma step directly inserts projectivity into the chosen morphism and deletes the later attempted deduction of it; direct-image labels and a support reference are also repaired. The Leray citation at L29 leaves an internal section number blank. **P115; K1, K6**; the matching “Leray” occurrence in Oda is a separate cited application. |
| **C18** | **43:116:L6, L25–26, L40–44**, revised spectral term; cancelled Remarque/Proposition | Besides the pending equidimensionality question F18, the page has a replaced term and an inserted circled “est le …” margin. **P116; K6**; uncertainty in the omitted qualifiers is retained. |
| **C19** | **43:117:L19, L32–33**, cancelled “Vue d'ensemble”; “multiplicative” → “abélienne” | The label under the `2\alpha(A^0)` contribution is amended to the abelian component, while the separate multiplicative contribution remains. **P117; K4** gives the finite/abelian duality comparison loci. |
| **C20** | **43:118:L2–34, L48–60**, cancelled 15-part outline and administrative list | The whole mathematical outline and the later working list are cancelled, with nested earlier deletions preserved. **P118; K9**; the visible `September 1963` strings remain documentary text rather than a date assigned to this packet. |
| **C21** | **43:119:L14–24, L39–40**, replaced cohomology term; cancelled `Q:` definition | The diagram replaces a crossed-out `H^1(K,{}_{\infty}B)` slot with `H^0(K,B)\otimes\mathbb Q/\mathbb Z`, and a tentative definition of `Q` is struck. **P119; K4** locates torsion/Cartier objects but no exact local-field sequence. |
| **C22** | **43:120:L44**, inserted “sans torsion” | The dual of the divisible `H^1(K,A)'` is explicitly labelled torsion-free after a deleted candidate; the nearby comparison is then question-marked in (ii). **P120; K4**. |
| **C23** | **43:121:L8, L25–31**, “si `A` est local”; marginal `>` beside `\ge0` | The Euler-characteristic text receives a local-base qualification and a proposed strict leading-coefficient sign, alongside revisions to the coherent-module/polynomial wording. **P121; K6, K9** retains those exact interventions and the uncertain “Joube/doute” margin. |
| **C24** | **43:128:L6, L8, L14–26**, inserted `H^i\simeq Ext^i`; “-schémas” | The Weil/group setup has local definition and derived-notation insertions as well as the explicit questions F26–F27. **P128; K1, K3** records the context's specific use of an invertible “faisceau de Weil”. |
| **C25** | **43:129:L2–45**, cancelled draft; inserted “régulier”, “local”, “A-suite” | The polynomial-ring dimension draft is wholly cancelled, retaining several strengthened hypotheses/descriptions and a nested deleted corollary. Its final property-transfer instruction is incomplete and uncertain (F28). **P129; K6**. |
| **C26** | **43:130:L2–14, L21, L33–39**, `Ext^0` → `Hom^0`; “faisceau de Weil”; “de type fini” | The cancelled first route is replaced by the composition construction, the degree-zero class is relabelled `Hom^0`, and the theorem's object/range qualifications are repeatedly amended. **P130; K3–K4** keeps the uncertain “préciser” in scope. |
| **C27** | **43:131:L2–8**, active `V`; cancelled `IV\|VI` and cover title | The Roman mark and crossed-out Hilbert/Picard title form a cover revision, including a cancelled parenthetical about fundamental groups. **P131; K5, K9**; see the full title register. |
| **C28** | **43:132:L10, L18–26**, `fini`; `D(\Delta\sigma)`; deleted `-2` | The text inserts `H_f^0(G_m)\simeq G_m`, narrows the coefficient group, replaces a tensor description by the written multiplicative-type construction, and deletes the degree shift `-2` in one target Ext. **P132; K3–K4**. |
| **C29** | **43:133:L16, L22, L25, L42**, deleted “Jacobienne”; `p` → “Frobenius” | The characteristic-`p` table receives the Frobenius label and the closing Ext insertion; the local deleted words do not erase the surrounding surviving Jacobian self-duality remarks. **P133; K4–K5** gives the exact context comparison loci. |
| **C30** | **43:134:L2–5**, deleted `V`; “Fidèle platitude / Descente fid. plate / Applications” | Both the Roman mark and this cover heading are cancelled. **P134; K6, K9** locates a faithfully flat descent statement at T 16:56 but no matching cover phrase. |
| **C31** | **43:135:L10–14, L19–20, L33–40, L47, L51–53**, “quelconque” → “premier à `p`” | The finite-support and extension-by-zero discussion changes coefficients, local wording, and auxiliary formulas; its final calculation explicitly narrows the order `n` to the prime-to-`p` range. **P135; K4, K8**; this restriction stays attached to the announced calculation in F33. |
| **C32** | **43:136:L11, L20, L31, L60**, cancelled coefficients and superscript `m` | The support-duality working page deletes candidate coefficient/Ext labels and repeated outer superscripts; the separate clear question at L34 survives. **P136; K3, K8**; the later `m+1` inside the box remains unchanged. |
| **C33** | **43:138:L4–6, L14–18**, inserted `3-i`, `2-i`; `Ext` → uncertain `\underline H` | The degree annotations and cohomology labels are explicitly revised, and the lower isomorphism attempt is cancelled/questioned. **P138; K8** locates no matching support diagram. |
| **C34** | **43:140:L2**, cancelled `H^i(C,` | Only an initial incomplete cohomology attempt is deleted at the top; the bottom boxed question remains the salient active uncertainty. **P140; K8**. |

## C. Titles, covers, reused sheets, and page counts

The supplied selection has **49 scan numbers in the inclusive range**, with the three requested omissions, hence **46 actual sheet fragments**. The inventory classifications are **27 text**, **11 reused_typed**, **4 cancelled_draft**, and **4 cover**. The four cover faces are **122, 131, 134, 142**; the last two cancelled-cover headings are still part of the title evidence.

Every fragment carries the transcribed number `scan−1`, yielding the marks **93–141 with gaps 98, 110, 126** in this selected set. Additional typed numbers are recorded below. These visible marks, section/theorem numbers, references, and lists are not converted into a claimed total extent for any constituent work. **No explicit “N pages” or “N feuilles” extent statement was located in the 46 frozen fragments.** The physical selection count above is the only page total calculated here.

The archive description quoted in `context/README.md`, line 9, is “Dualité des groupes. Jacobiennes généralisées etc : notes et copies de notes manuscrites (s.d.).” with a supplied approximate date range. That is package metadata, not a date demonstrated for any one of these sheets. The cancelled `September 1963` lines at 118:49/51 are the only explicit calendar strings located in this packet outside references; their scope remains the administrative list. Bibliographical dates at 105 are recorded as bibliographical data only. The prior reused-sheet observations **S: MPL_136_095-141 1.5; MPL_136_189-234 R008; MPL_136_235-281 N16** retain their **first-pass lead** status and establish no provenance for these sheets.

The table below records every sheet. “No explicit flag” is a census result about the frozen wording, not an assertion that all displayed mathematics has been proved. Full source/correction references are in A, B, and D; each row links the exact contextual search group for its words/objects.

| Scan | Inventory sheet kind | Exact number registrations | Title/headings and count evidence | Flag/revision census; context search |
|---|---|---|---|---|
| **94** | text | `\mspage{93}` @ L43 | No separate title; opening description of the T-category; “règles de calcul” at L32–37. | F01; C01; **P094** |
| **95** | text | `\mspage{94}` @ L11 | No separate title; continuation “Il faudrait aussi” at L2; cancelled N.B. at L9–10. | F02; C02; **P095** |
| **96** | text | `\mspage{95}` @ L39 | “foncteur fondamental … dit de Néron” at L2; no extent statement. | F03; C03; **P096** |
| **97** | text | `\mspage{96}` @ L32 | No separate title; previous cancelled note continues at L2–3; Néron derived functors. | F04; C03–C04; **P097** |
| **98** | text | `\mspage{97}` @ L42 | No separate title; relative Hom/Ext and two spectral-sequence gates. | F05–F06; C05; **P098** |
| **100** | text | `\mspage{99}` @ L63 | Outline items **1–8** at L25–62; “Dualité de Cartier”, “Dualité de Serre-Pontrjagin”, “Le th. de dualité”. These are item numbers. | C06; no explicit question flag; **P100** |
| **101** | reused_typed | `\mspage{100}` @ L2; `\mspage{22.}` @ L3 | Typed continuation of (6.5); “Pembroke College, Cambridge.” at L60–61; author not named on the face; external identification in R03. | F37–F38; C07; **P101** |
| **102** | text | `\mspage{101}` @ L43 | Outline items **9–14** at L2–22, continuing scan 100; Lang/Serre/Tate comparison table L36–41. | F07–F08; C08; **P102** |
| **103** | reused_typed | `\mspage{102}` @ L2; `\mspage{21.}` @ L3 | Typed “Remark” L4, LEMMA (6.3) L24, LEMMA (6.4) L37, THEOREM (6.5) L45. Typed page 21 continues on typed page 22 at scan 101. | F39; **P103** |
| **104** | text | `\mspage{103}` @ L42 | No separate title; category/functor diagram and proposed properties (i)–(iii). | F09–F10; C09; **P104** |
| **105** | reused_typed | `\mspage{104}` @ L2 | “REFERENCES” L3; entries **1–16**. Their numbering and publication page ranges count references/cited pages. | F40; no mathematical question flag; **P105** |
| **106** | text | `\mspage{105}` @ L56 | No separate title; Cartier/Serre/Pontryagin square; “Comment obtient on le carré du bas ?” L29. | F11; C10; **P106** |
| **107** | text | `\mspage{106}` @ L43 | No separate title; pairing and Ext scratch calculations. | C11; no explicit question flag; **P107** |
| **108** | cancelled_draft | `\mspage{107}` @ L2 | Cancelled “Corollaire” with uncertain number 4/2.9.10 at L3; cancelled homology diagram L56–62. | C12; no literal author question mark; **P108** |
| **109** | text | `\mspage{108}` @ L62 | Case headings “2°) G=mu_p” L2, “3°) G=alpha_p” L22, repeated “3°) G=G_m” L26. The repeated item number is preserved. | C13; no explicit question flag; **P109** |
| **110** | reused_typed | `\mspage{109}` @ L66 | “IV 7 Oubli au n° 7.6.” L2; Proposition 6.7 L4; Lemme 6.8 L25. These are internal labels, with no extent count. | F12–F15; C14; **P110** |
| **112** | text | `\mspage{111}` @ L55 | No separate title; finite-group/Greenberg table. | F16–F17; C15; **P112** |
| **113** | cancelled_draft | `\mspage{112}` @ L41 | No separate title; whole local-reciprocity/Galois draft cancelled. | C16; no literal author question mark; **P113** |
| **114** | text | `\mspage{113}` @ L59 | No separate title; boxed Ext/cohomological pairings and unfinished displays. | No explicit question flag; edits at L40/L48; **P114** |
| **115** | reused_typed | `\mspage{114}` @ L2; `\mspage{III-49}` @ L3 | Typed page III-49, starts mid-word L4 and ends mid-Corollaire 1 L34–35. | C17; an internal Leray reference remains blank at L29; **P115** |
| **116** | text | `\mspage{115}` @ L45 | No separate title; spectral diagram, then cancelled “Remarque 2.7” and “Prop. 2.8. Continuité des Cohen-Macaulay” L40–44. | F18; C18; **P116** |
| **117** | text | `\mspage{116}` @ L43 | Cancelled marginal “Vue d’ensemble” L19; displayed items (3), (2), (1) L7–16. | C19; no explicit question flag; **P117** |
| **118** | cancelled_draft | `\mspage{117}` @ L66 | Cancelled mathematical outline numbered **1–15** L3–33; cancelled administrative list L48–60, with September 1963 strings. | F19–F20; C20; **P118** |
| **119** | text | `\mspage{118}` @ L45 | No separate title; torsion-cohomology diagrams and Q,N scratch definitions. | C21; no explicit question flag; **P119** |
| **120** | text | `\mspage{119}` @ L50 | No separate title; 1°/2° and (i)/(ii)/(iii) L38–49, with (iii) unfinished. | F21; C22; **P120** |
| **121** | reused_typed | `\mspage{III-42}` @ L2; `\mspage{120}` @ L38 | Typed page III-42; Proposition 13 L12, equations (15)/(16), Théorème 2 L25. | F22 possible reading; C23; **P121** |
| **122** | cover | `\mspage{121}` @ L7 | **Cover:** “Corps de classes / et dualité / des Courbes Algébriques” L3–5; last line underlined. | No explicit flag; P122 title search; **P122** |
| **123** | text | `\mspage{122}` @ L48 | No separate title; support/Ext diagrams and a questioned duality expression. | F23–F24; **P123** |
| **124** | reused_typed | `\mspage{84}` @ L2; `\mspage{123}` @ L9 | Typed “THEOREME 3” L4, partition of unity; marginal “n° 239” L3. | No explicit unresolved flag; **P124** |
| **125** | text | `\mspage{124}` @ L33 | No separate title; formal-scheme/completion diagram, “complété formel le long de Z” L28. | F25; **P125** |
| **126** | reused_typed | `\mspage{78}` @ L2; `\mspage{125}` @ L17 | Typed section **“3. Faisceaux mous”** L4; “DEFINITION 1” L12; marginal “n° 239” L3. | No explicit unresolved flag; **P126** |
| **128** | text | `\mspage{127}` @ L32 | Cancelled uncertain “Schémas” L2; C-group setup starts L4. | F26–F27; C24; **P128** |
| **129** | cancelled_draft | `\mspage{128}` @ L46 | Cancelled “Proposition” L3 and “passer au N° précédent” margin L4; Cor/Dem labels within wholly cancelled draft. | F28 possible instruction; C25; **P129** |
| **130** | text | `\mspage{129}` @ L40 | “Th.” (i) L33 and (ii) L39; trace/comparison construction precedes it. | F29–F30; C26; **P130** |
| **131** | cover | `\mspage{130}` @ L10 | **Cover:** active over/underlined **V**, cancelled uncertain **IV/VI** L2; cancelled “Schémas de Hilbert, de Picard” L4; cancelled parenthetical “sans théorie des relations … avec les groupes fondamentaux” L6–8. | C27; no extent statement; **P131** |
| **132** | text | `\mspage{131}` @ L39 | No separate title; labels a), b), circled star, final c) at L25/30/38. | F41; C28; **P132** |
| **133** | text | `\mspage{132}` @ L49 | No separate title; cohomological table, marginal “autodualité de la Jacobienne” L43. | C29; no explicit question flag; **P133** |
| **134** | cover | `\mspage{133}` @ L6 | **Cover:** cancelled over/underlined **V** L2; cancelled “Fidèle platitude / Descente fid. plate / Applications” L3–5. | C30; no extent statement; **P134** |
| **135** | text | `\mspage{134}` @ L54 | No separate title; point-support and extension-by-zero argument; uncertain omega)/a) marker L35. | F31–F33; C31; **P135** |
| **136** | text | `\mspage{135}` @ L74 | No separate title; “triangle exact de complexes de k-groupes” L27, support/duality diagrams. | F34; C32; **P136** |
| **137** | reused_typed | `\mspage{136}` @ L23; centered `- 37 -` @ L2 | Typed page “- 37 -” L2, marginal “n°338” L3; PROPOSITION 9 begins at L22. | No explicit unresolved flag; **P137** |
| **138** | text | `\mspage{137}` @ L21 | No separate title; revised dual localization diagram. | F35; C33; **P138** |
| **139** | reused_typed | `\mspage{138}` @ L11; centered `- 88 -` @ L2 | Typed page “- 88 -” L2, marginal “n° 239” L3; PROPOSITION 8 L6 and “Exercices. 1)” L10. | No explicit unresolved flag; **P139** |
| **140** | text | `\mspage{139}` @ L41 | No separate title; functor/support diagrams and boxed comparison question. | F36; C34; **P140** |
| **141** | reused_typed | `\mspage{140}` @ L13; centered `- 87 -` @ L2 | Typed page “- 87 -” L2, marginal “n° 239” L3; PROPOSITION 8 L6, LEMME 2 L10. Its lemma continues at scan 139. | No explicit unresolved flag; **P141** |
| **142** | cover | `\mspage{141}` @ L6 | **Cover:** “Dualité de Tate- / Cassels” L3–4; line-break hyphen retained. | No explicit flag; P142 title search; **P142** |

### Ordering and count observations

The typed numbers **21 → 22** correspond to scans **103 → 101**; **87 → 88** correspond to **141 → 139**. The III-42/III-49 and 78/84 labels are sparse visible witnesses, without their intervening typed pages in this selection. The two sheets numbered 87 and 88 both print “PROPOSITION 8”, which is preserved; no editorial renumbering is inferred. Roman V on the two covers and “IV 7” on scan 110 are recorded as marks, without converting them into chapter chronology.

The supplied-context title comparisons are K9 and query groups P122/P131/P134/P142. The actual topic headings and repeated page numbers in this register establish what is present in the selected faces; the README’s archive-level date range and publication dates in references are not used to date their writing.

## D. Exhaustive deletion/insertion census

Each row gives one encoded revision marker, including markers nested inside a wholly cancelled block. Exact fragment line spans identify the complete text; quoted bodies below retain their TeX spelling, with line breaks shown as **⏎** and an explicit **[excerpt]** label when shortened to 180 characters. These short excerpts locate an edit; they do not replace its full frozen reading. Every row inherits the page-specific context search shown in the last column, and the material interpretations are in section B.

| Marker | Frozen locus | Encoded state and enclosing context | Exact short body | Context search |
|---|---|---|---|---|
| E001 | 43:94:L4 | deleted | `\unsure{quasi} \unsure{groupes} \unsure{quasi-algébriques}` | P094 |
| E002 | 43:94:L5 | deleted | `\unsure{schémas}` | P094 |
| E003 | 43:94:L7 | deleted | `\unsure{surjectifs}` | P094 |
| E004 | 43:94:L17 | inserted | `$\underline{\operatorname{Ext}}^i_k(F,G)$` | P094 |
| E005 | 43:94:L32 | deleted | `\unsure{calculer}` | P094 |
| E006 | 43:94:L34 | inserted | `quasi-` | P094 |
| E007 | 43:95:L3 | deleted | `\unsure{le}` | P095 |
| E008 | 43:95:L9–10 | deleted | `N.B. Il n'y \unsure{a pas} \illegible{3} \unsure{élémentaire} de ⏎ Weil \unsure{permette}.` | P095 |
| E009 | 43:96:L2 | inserted | `dit \uline{de Néron}` | P096 |
| E010 | 43:96:L8–12 | inserted | `\[ ⏎ \simeq F(\varinjlim_{P}\mathbb V(A^P)) ⏎ =F(\varprojlim_{P}\operatorname{Spec}(\mathbb V(A^P))) ⏎ \qquad\inserted{\operatorname{Spec}(\varinjlim_{P}\mathbb V(A^P))} ⏎ \]` | P096 |
| E011 | 43:96:L11 | inserted; inside inserted | `\operatorname{Spec}(\varinjlim_{P}\mathbb V(A^P))` | P096 |
| E012 | 43:96:L32 | inserted | `cpt` | P096 |
| E013 | 43:96:L35–36 | deleted | `[N.B. $\mathcal N(F)$ est compatible \unsure{avec} les limites ⏎ inductives d'anneaux \unsure{donc si on y tient}, on peut se limiter` | P096 |
| E014 | 43:97:L2–3 | deleted | `dans la catégorie $C'(k)$ aux foncteurs compatibles avec les ⏎ limites inductives.` | P097 |
| E015 | 43:97:L11 | deleted | `\unsure{de}` | P097 |
| E016 | 43:97:L21–27 | deleted | `\unsure{car on va voir} en construisant un adjoint à ⏎ $\mathcal N=\underline H^0_{S/k}$ et constatant que ce dernier est exact ⏎ à gauche : ⏎ \[ ⏎ \operatorname{Hom}(\Phi,\mathcal N(F))\s` **[excerpt]** | P097 |
| E017 | 43:98:L7 | deleted | `\unsure{Alors}` | P098 |
| E018 | 43:98:L7 | inserted | `notons` | P098 |
| E019 | 43:98:L14 | deleted | `et pour $H^0_S$` | P098 |
| E020 | 43:98:L17 | deleted | `\unsure{p+q}` | P098 |
| E021 | 43:100:L10 | deleted | `\unsure{*}` | P100 |
| E022 | 43:100:L23 | deleted; inside margin | `$\unsure{\Gamma}_{K/k}G$` | P100 |
| E023 | 43:100:L46 | inserted | `de Néron-\unsure{Weil}` | P100 |
| E024 | 43:100:L49 | deleted | `$\unsure{\Gamma}_{K/k}$` | P100 |
| E025 | 43:100:L54–56 | inserted | `\[ ⏎ E^*_{K/k}(F,G)\qquad E_{K/k}(G) ⏎ \]` | P100 |
| E026 | 43:101:L22 | inserted | `${}^+$` | P101 |
| E027 | 43:102:L5 | deleted | `et le corps de classes de Serre` | P102 |
| E028 | 43:102:L11 | deleted | `$\unsure{H^1}$` | P102 |
| E029 | 43:102:L16 | deleted | `pour \unsure{un corps}` | P102 |
| E030 | 43:102:L17 | inserted | `(sur corps $k$ fini)` | P102 |
| E031 | 43:102:L22 | inserted | `\uline{Théorie de Rosenlicht locale}` | P102 |
| E032 | 43:102:L30–34 | deleted | `\[ ⏎ \unsure{\mu_p\otimes\mu_p}\\ ⏎ \unsure{\underline{\operatorname{Hom}}(\mu_p\otimes\mu_p,G_m)} ⏎ \unsure{\simeq}\unsure{\operatorname{Hom}(\mu_p,\mathbb Z/p\mathbb Z)} ⏎ \]` | P102 |
| E033 | 43:104:L6 | deleted | `\unsure{quasi}` | P104 |
| E034 | 43:104:L6 | deleted | `\unsure{alg}` | P104 |
| E035 | 43:104:L9 | deleted; inside margin | `$\unsure{T^0}$` | P104 |
| E036 | 43:104:L11 | deleted; inside margin | `\unsure{et}` | P104 |
| E037 | 43:104:L20 | deleted | `\unsure{Question}` | P104 |
| E038 | 43:104:L24 | deleted | `\unsure{excepte}` | P104 |
| E039 | 43:104:L24 | inserted | `exclut` | P104 |
| E040 | 43:106:L9 | deleted | `\unsure{\mathcal G}` | P106 |
| E041 | 43:106:L31 | deleted | `\unsure{Remarque}` | P106 |
| E042 | 43:106:L47 | deleted | `(-1)` | P106 |
| E043 | 43:106:L55 | deleted | `$\unsure{\mathbb Z}$` | P106 |
| E044 | 43:107:L21 | deleted | `$\unsure{H^i(}$` | P107 |
| E045 | 43:107:L30 | deleted | `1) $G$ \unsure{grp} fini` | P107 |
| E046 | 43:107:L34 | deleted | `\unsure{H^{1-i}}(\quad H^i(K,G)\times H^{\unsure{1-i}}(K,\widehat G` | P107 |
| E047 | 43:108:L3–36 | deleted | ` ⏎ \uline{Corollaire} \unsure{4\|2}.9.10. Soit $f:X\longrightarrow Y$ un morphisme \deleted{de} ⏎ \inserted{de type fini,} \deleted{\unsure{propre}} où $Y$ loc. noeth., $y\in Y$, on sup` **[excerpt]** | P108 |
| E048 | 43:108:L4 | deleted; inside deleted | `de` | P108 |
| E049 | 43:108:L5 | inserted; inside deleted | `de type fini,` | P108 |
| E050 | 43:108:L5 | deleted; inside deleted | `\unsure{propre}` | P108 |
| E051 | 43:108:L7 | deleted; inside deleted | `Alors, la fonction $\unsure{y}\mapsto\unsure{\pi_0(y)}$` | P108 |
| E052 | 43:108:L8 | inserted; inside deleted | `Pour tt $z\in\unsure{Z\|Y}$, soit $\pi(z)=\unsure{\mathrm{nb}^{\mathrm{re}}}$ de` | P108 |
| E053 | 43:108:L11 | deleted; inside deleted | `\unsure{continue} \unsure{en} \unsure{y}` | P108 |
| E054 | 43:108:L12 | inserted; inside deleted | `\unsure{$\frac12$} \unsure{continue}` | P108 |
| E055 | 43:108:L13 | deleted; inside deleted | `\unsure{un} \unsure{voisinage}` | P108 |
| E056 | 43:108:L16–17 | deleted; inside deleted | `La \deleted{\unsure{fonction}} \unsure{définie} \unsure{ci-dessus} est &#96;&#96;$\frac12$ continue ⏎ \unsure{semi-inférieurement}'', par la &#96;&#96;\unsure{th.} de connexité''.` | P108 |
| E057 | 43:108:L16 | deleted; inside deleted, deleted | `\unsure{fonction}` | P108 |
| E058 | 43:108:L19–21 | deleted; inside deleted | `\unsure{Il reste} \illegible{4} \unsure{qu'elles sont} ⏎ \unsure{les composantes} \unsure{supérieures} \unsure{à} \unsure{ceux} ⏎ \unsure{connexes} (\unsure{comme} elles sont \unsure{c` **[excerpt]** | P108 |
| E059 | 43:108:L32 | deleted; inside deleted | `$\unsure{X_0}$ \unsure{a} \unsure{fini}` | P108 |
| E060 | 43:108:L33 | deleted; inside deleted | `$\pi(\unsure{X_0})$` | P108 |
| E061 | 43:108:L34 | deleted; inside deleted | `\unsure{donc}` | P108 |
| E062 | 43:108:L56–62 | deleted | `\diagram{\begin{tikzcd}[column sep=small,row sep=large] ⏎ 0\arrow[r]\arrow[dr,dash,bend right=30]& ⏎ N\arrow[r]\arrow[d,dash,bend right=20]& ⏎ M\arrow[r,dash]\arrow[d,dash,bend right=15]` **[excerpt]** | P108 |
| E063 | 43:109:L7 | deleted | `$H^0(k,\mu)$` | P109 |
| E064 | 43:109:L9 | deleted | `H^i` | P109 |
| E065 | 43:109:L40 | deleted | `$k^*$` | P109 |
| E066 | 43:109:L45 | deleted | `\mathbb Z/n\mathbb Z` | P109 |
| E067 | 43:110:L5 | deleted | `de présentation finie` | P110 |
| E068 | 43:110:L5 | deleted | `et` | P110 |
| E069 | 43:110:L6 | inserted | `avec $Y$ loc. noeth.,` | P110 |
| E070 | 43:110:L7 | deleted | `de présentation finie` | P110 |
| E071 | 43:110:L7 | inserted | `cohérent` | P110 |
| E072 | 43:110:L8 | inserted | `de support $X$,` | P110 |
| E073 | 43:110:L9 | deleted | `long` | P110 |
| E074 | 43:110:L9 | deleted | `tota` | P110 |
| E075 | 43:110:L10 | inserted | `sur $k(y)$` | P110 |
| E076 | 43:110:L12–13 | inserted | `On suppose $f$ univ. ouvert en les pts maximaux de $X_{y_0}$, ⏎ et $F_{y_0}$ sans \unsure{idéaux} premiers ass. immergés` | P110 |
| E077 | 43:110:L15 | inserted | `en $y_0$` | P110 |
| E078 | 43:110:L22 | deleted | `\unsure{à prouver}` | P110 |
| E079 | 43:110:L26 | inserted | `de support $X$,` | P110 |
| E080 | 43:110:L27 | deleted | `fibr` | P110 |
| E081 | 43:110:L30 | inserted | `(Supposons que tt comp. de $X$ domine $Y$ et $F_0$ soit $(S_1)$.)` | P110 |
| E082 | 43:110:L35 | deleted | `\unsure{génériques}` | P110 |
| E083 | 43:110:L35 | deleted | `\unsure{que}` | P110 |
| E084 | 43:110:L36 | deleted | `donc toute composante de $\operatorname{supp}F$ domine $Y$,` | P110 |
| E085 | 43:110:L47 | deleted | `pour` | P110 |
| E086 | 43:110:L51 | deleted | `est` | P110 |
| E087 | 43:110:L63 | deleted; inside margin | `\unsure{minimal}` | P110 |
| E088 | 43:112:L4 | deleted | `\unsure{(n,p)\neq1}` | P112 |
| E089 | 43:112:L13 | deleted | `\mathbb Q/\mathbb Z\xrightarrow{n}\mathbb Q/\mathbb Z` | P112 |
| E090 | 43:112:L33 | deleted | `\unsure{\wp}` | P112 |
| E091 | 43:112:L37 | deleted | `\unsure{\wp}` | P112 |
| E092 | 43:113:L2–40 | deleted | ` ⏎ \unsure{ou}, \inserted{pour tt $x\in X$,} \deleted{\unsure{des}}\inserted{un} ⏎ \unsure{élément} \deleted{\unsure{de $\mathcal G_x$}} ⏎ $\lambda_x\in\gamma(\deleted{\unsure{\xi}}\xi_x` **[excerpt]** | P113 |
| E093 | 43:113:L3 | inserted; inside deleted | `pour tt $x\in X$,` | P113 |
| E094 | 43:113:L3 | deleted; inside deleted | `\unsure{des}` | P113 |
| E095 | 43:113:L3 | inserted; inside deleted | `un` | P113 |
| E096 | 43:113:L4 | deleted; inside deleted | `\unsure{de $\mathcal G_x$}` | P113 |
| E097 | 43:113:L5 | deleted; inside deleted | `\unsure{\xi}` | P113 |
| E098 | 43:113:L9 | deleted; inside deleted | `\unsure{de}` | P113 |
| E099 | 43:113:L18 | deleted; inside deleted | `\unsure{Le groupe}` | P113 |
| E100 | 43:113:L18 | deleted; inside deleted | `\unsure{Donne}` | P113 |
| E101 | 43:113:L19 | inserted; inside deleted | `\uuline{invariant} dans $\operatorname{Gal}(K'/K)$` | P113 |
| E102 | 43:113:L21 | deleted; inside deleted | `\uline{plus gr.}\ \unsure{sous-gr.}` | P113 |
| E103 | 43:113:L22 | inserted; inside deleted | `groupe de \unsure{galois\|Galois}` | P113 |
| E104 | 43:113:L23 | deleted; inside deleted | `\unsure{{}_x^{\mathrm{dec}}}` | P113 |
| E105 | 43:113:L25 | inserted; inside deleted | `galoisienne` | P113 |
| E106 | 43:113:L26 | deleted; inside deleted | `\unsure{en}` | P113 |
| E107 | 43:113:L26 | deleted; inside deleted | `$x\in X$` | P113 |
| E108 | 43:113:L33 | inserted; inside deleted | `\uuline{invariant} \unsure{par}` | P113 |
| E109 | 43:113:L35 | deleted; inside deleted | `\unsure{{}_x}` | P113 |
| E110 | 43:113:L37 | deleted; inside deleted | `\unsure{plus}` | P113 |
| E111 | 43:114:L40 | deleted | `\unsure{f_*G}` | P114 |
| E112 | 43:114:L48 | deleted; inside margin | `\unsure{\mathrm{coh}}` | P114 |
| E113 | 43:115:L13 | inserted | `\uline{projectif}` | P115 |
| E114 | 43:115:L13 | inserted | `\uline{et}` | P115 |
| E115 | 43:115:L15 | deleted | `\unsure{et $g$ fermé}, on en déduit (II,4,6,th.3 (ii)) que $g$ est aussi un morphisme projectif; comme $X$ est noethérien` | P115 |
| E116 | 43:115:L17 | deleted | `\unsure{$g$}` | P115 |
| E117 | 43:115:L20 | deleted | `$\unsure{R^qg_*}$` | P115 |
| E118 | 43:115:L23 | inserted | `(FAG,I,2,12,prop.1)` | P115 |
| E119 | 43:115:L26 | deleted | `$\unsure{R^pf_*}$` | P115 |
| E120 | 43:115:L30 | deleted | `\unsure{le}` | P115 |
| E121 | 43:115:L35 | deleted | `\unsure{noethérien}` | P115 |
| E122 | 43:116:L6 | deleted | `\unsure{H^p(\Delta^2H^qA)}` | P116 |
| E123 | 43:116:L25 | deleted; inside margin | `\unsure{qui est}` | P116 |
| E124 | 43:116:L25 | inserted; inside margin | `\figure{\begin{tikzpicture}\node[draw,ellipse]{\uline{est le \unsure{plus gr}}};\end{tikzpicture}}` | P116 |
| E125 | 43:116:L40–44 | deleted | `\uline{Remarque} 2.7. J'ignore si les conditions ⏎ d'équidimensionnalité de 1.1. ii) sont ⏎ essentielles; de $=$ dans 2.6. ⏎  ⏎ \uline{Prop.} 2.8. Continuité des Cohen-Macaulay.` | P116 |
| E126 | 43:117:L19 | deleted; inside margin | `\unsure{Vue d'ensemble}` | P117 |
| E127 | 43:117:L32 | deleted | `\text{multiplicative}` | P117 |
| E128 | 43:118:L2–34 | deleted | ` ⏎ 1. \inserted{Morphismes plats \unsure{etc.}} Changement de base, \deleted{platitude} ⏎  ⏎ 2. $\underset{\longleftarrow}{\operatorname{Lim}}$ de préschémas, propriétés constructibles ⏎  ⏎ ` **[excerpt]** | P118 |
| E129 | 43:118:L3 | inserted; inside deleted | `Morphismes plats \unsure{etc.}` | P118 |
| E130 | 43:118:L3 | deleted; inside deleted | `platitude` | P118 |
| E131 | 43:118:L48–60 | deleted | ` ⏎ $*$ \deleted{James September 1963} ⏎  ⏎ $*$ Bott September 1963 ? ⏎  ⏎ $*$ \uline{Zariski} for Dieudonné: \unsure{Give} a talk at the Colloquium of Harvard ⏎  ⏎ $*$ \uline{Hilton} on the mail` **[excerpt]** | P118 |
| E132 | 43:118:L49 | deleted; inside deleted | `James September 1963` | P118 |
| E133 | 43:118:L57 | deleted; inside deleted | `copy of my talks to Baltimore` | P118 |
| E134 | 43:118:L59 | deleted; inside deleted | `Paper by Eells-Kuiper.` | P118 |
| E135 | 43:119:L14 | deleted | `B\qquad H^1(K,{}_\infty B)\longrightarrow H^1(K,B)\mathrel{-}0` | P119 |
| E136 | 43:119:L20 | deleted | `$H^1(K,A)\longrightarrow$` | P119 |
| E137 | 43:119:L23 | deleted | `H^1(K,{}_\infty B)` | P119 |
| E138 | 43:119:L24 | inserted | `H^0(K,B)\otimes\mathbb Q/\mathbb Z` | P119 |
| E139 | 43:119:L39–40 | deleted | `Q:\ \deleted{H^1(K,B)}\ \operatorname{Ker}\ H^0(K,B)\longrightarrow ⏎ H^0(K,B)\otimes\mathbb Q/\mathbb Z` | P119 |
| E140 | 43:119:L39 | deleted; inside deleted | `H^1(K,B)` | P119 |
| E141 | 43:120:L24 | deleted | `\unsure{\mathbb Z}` | P120 |
| E142 | 43:120:L34 | deleted | `\unsure{H^1(K,A)}` | P120 |
| E143 | 43:120:L44 | deleted | `$\unsure{a\mathbb Z}$` | P120 |
| E144 | 43:120:L44 | inserted | `sans torsion` | P120 |
| E145 | 43:121:L10 | deleted | `\illegible{1}` | P121 |
| E146 | 43:121:L23 | deleted | `\illegible{1}` | P121 |
| E147 | 43:121:L25 | inserted | `\uline{Soit $\underline F$ un $\underline O_X$-module cohérent}.` | P121 |
| E148 | 43:121:L26 | deleted | `\illegible{3}` | P121 |
| E149 | 43:121:L26 | inserted | `égale à` | P121 |
| E150 | 43:121:L26 | inserted | `en $n$` | P121 |
| E151 | 43:121:L28 | deleted | `\illegible{2}` | P121 |
| E152 | 43:121:L35 | deleted | `$\unsure{z}$` | P121 |
| E153 | 43:121:L35 | deleted | `$\unsure{Z}$` | P121 |
| E154 | 43:121:L35 | deleted | `\unsure{et}` | P121 |
| E155 | 43:121:L35 | deleted | `\unsure{les}` | P121 |
| E156 | 43:128:L2 | deleted | `\unsure{Schémas}` | P128 |
| E157 | 43:128:L6 | deleted | `\illegible{1}` | P128 |
| E158 | 43:128:L6 | deleted | `\unsure{petit}` | P128 |
| E159 | 43:128:L6 | deleted | `\unsure{Ils}` | P128 |
| E160 | 43:128:L6 | inserted | `$\simeq\operatorname{Ext}^i(C;\mathbb Z,G)$` | P128 |
| E161 | 43:128:L8 | inserted | `-schémas` | P128 |
| E162 | 43:128:L8 | deleted | `\unsure{les}` | P128 |
| E163 | 43:128:L10 | deleted | `$\unsure{f_*}$` | P128 |
| E164 | 43:128:L14 | deleted | `\unsure{donc}` | P128 |
| E165 | 43:128:L16 | deleted | `\unsure{Rf(E}` | P128 |
| E166 | 43:128:L25 | deleted | `H^{\unsure{i}}_f` | P128 |
| E167 | 43:129:L2–45 | deleted | ` ⏎ \deleted{Proposition} ⏎ \margin{passer au N$^\circ$ \unsure{précédent}} ⏎ \figure{\begin{tikzpicture}\draw[->](0,0)..controls(-.8,1)and(-.8,2)..(.6,2.8);\draw(1,2.6)--(1.5,1.8)--(2.8,` **[excerpt]** | P129 |
| E168 | 43:129:L3 | deleted; inside deleted | `Proposition` | P129 |
| E169 | 43:129:L7 | deleted; inside deleted | `$\dim A=n\quad A$ est de dim` | P129 |
| E170 | 43:129:L7 | inserted; inside deleted | `$A$ est \uline{régulier}, de dim $n$` | P129 |
| E171 | 43:129:L8 | deleted; inside deleted, margin | `$A[t_1--t_n]$` | P129 |
| E172 | 43:129:L10 | deleted; inside deleted | `\unsure{régulière de}` | P129 |
| E173 | 43:129:L10 | inserted; inside deleted | `$A$-suite` | P129 |
| E174 | 43:129:L10 | deleted; inside deleted | `paramètres` | P129 |
| E175 | 43:129:L12 | deleted; inside deleted, margin | `\unsure{(ii)}` | P129 |
| E176 | 43:129:L13 | inserted; inside deleted | `local` | P129 |
| E177 | 43:129:L23 | deleted; inside deleted | `\uline{Cor} $A$ anneau noeth. Alors $\dim A[t_1,-t_n]=\dim A+n$` | P129 |
| E178 | 43:129:L25 | deleted; inside deleted | `(ii) Si $A=k[t_1,-t_n]_{\mathfrak m}$, $\mathfrak m$ maximal, $k$ un corps, \unsure{Alors} $A$ \unsure{est}` | P129 |
| E179 | 43:129:L34 | deleted; inside deleted | `\unsure{Prof}` | P129 |
| E180 | 43:130:L2–14 | deleted | ` ⏎ Soit un elt $\unsure{f\|\varphi}\in\operatorname{Ext}^i(C;G,S\unsure{\sigma\|\tau})$, i.e. un hom de degré $i$ $G\mathrel{-}S\unsure{\sigma\|\tau}$, d'où un hom de degré $i$ $Rf_*G\m` **[excerpt]** | P130 |
| E181 | 43:130:L21 | deleted | `\unsure{\operatorname{Ext}^0}` | P130 |
| E182 | 43:130:L21 | inserted | `\operatorname{Hom}^0` | P130 |
| E183 | 43:130:L23 | deleted | `élément` | P130 |
| E184 | 43:130:L33 | inserted | `un \deleted{\unsure{proalgébrique}} faisceau de Weil` | P130 |
| E185 | 43:130:L33 | deleted; inside inserted | `\unsure{proalgébrique}` | P130 |
| E186 | 43:130:L33 | deleted | `\unsure{tous finis}` | P130 |
| E187 | 43:130:L33 | deleted | `alors` | P130 |
| E188 | 43:130:L39 | inserted | `\figure{\begin{tikzpicture}[baseline=(t.base)]\node[ellipse,draw,inner xsep=6pt,inner ysep=1pt](t){de type fini};\end{tikzpicture}}` | P130 |
| E189 | 43:130:L39 | deleted | `\unsure{est un}` | P130 |
| E190 | 43:131:L2 | deleted | `$\unsure{\mathrm{IV}\|\mathrm{VI}}$` | P131 |
| E191 | 43:131:L4 | deleted | `\uuline{Schémas de Hilbert, de Picard}` | P131 |
| E192 | 43:131:L6–8 | deleted | `(sans théorie des\\ ⏎ relations \unsure{intimes} avec les\\ ⏎ groupes fondamentaux)` | P131 |
| E193 | 43:132:L10 | inserted | `$\underline H^0_f(G_m)\simeq G_m$,` | P132 |
| E194 | 43:132:L18 | inserted | `fini` | P132 |
| E195 | 43:132:L18 | deleted | `\unsure{ab}` | P132 |
| E196 | 43:132:L19 | deleted | `$\unsure{\sigma\|\tau}\otimes\mu_n$ sur $k$ de` | P132 |
| E197 | 43:132:L23 | deleted | `hom` | P132 |
| E198 | 43:132:L26 | deleted | `\unsure{-2}` | P132 |
| E199 | 43:133:L16 | deleted; inside margin | `\unsure{Jacobienne}` | P133 |
| E200 | 43:133:L22 | deleted | `\unsure{p}` | P133 |
| E201 | 43:133:L22 | inserted | `Frobenius` | P133 |
| E202 | 43:133:L25 | deleted | `\unsure{pour tout groupe}` | P133 |
| E203 | 43:133:L42 | inserted | `$\operatorname{Ext}^1(J^0,\mathbb Q/\mathbb Z),\quad\Vert$` | P133 |
| E204 | 43:134:L2 | deleted | `$\overline{\underline{\mathrm V}}$` | P134 |
| E205 | 43:134:L3–5 | deleted | `\uline{Fidèle platitude}\par ⏎ \uline{Descente} fid. plate\par ⏎ Applications` | P134 |
| E206 | 43:135:L2 | inserted | `\unsure{finis}` | P135 |
| E207 | 43:135:L4 | deleted | `$\unsure{T(G)}\simeq$` | P135 |
| E208 | 43:135:L10 | deleted | `\unsure{S}` | P135 |
| E209 | 43:135:L13 | deleted | `\uline{local}` | P135 |
| E210 | 43:135:L14 | inserted | `si $G=G_Y$ (où $Y=\{x\}$),` | P135 |
| E211 | 43:135:L19 | deleted | `$\operatorname{Ext}^*(C,G,\unsure{\sigma\|\tau}\otimes\mu_n)\Longleftarrow H^p(C,\underline{\operatorname{Ext}}^q(G,\unsure{\sigma\|\tau}\otimes\mu_n))$` | P135 |
| E212 | 43:135:L20 | deleted | `\unsure{pour}` | P135 |
| E213 | 43:135:L20 | deleted | `\unsure{G}` | P135 |
| E214 | 43:135:L29 | inserted | `F_U` | P135 |
| E215 | 43:135:L33 | deleted | `($F$ fini plat sur $U$) \unsure{premier à $p$}` | P135 |
| E216 | 43:135:L35 | deleted | `$\unsure{F}$ \unsure{pour}` | P135 |
| E217 | 43:135:L37 | deleted | `\unsure{G}` | P135 |
| E218 | 43:135:L39 | deleted | `N.B. \unsure{bien distinguer}` | P135 |
| E219 | 43:135:L40 | deleted | `\unsure{les groupes}` | P135 |
| E220 | 43:135:L47 | deleted | `$\operatorname{Ext}^{\unsure{i-2}}\longleftarrow$` | P135 |
| E221 | 43:135:L51 | deleted | `\unsure{essentiel}` | P135 |
| E222 | 43:135:L53 | deleted | `\unsure{quelconque}` | P135 |
| E223 | 43:135:L53 | inserted | `premier à $p\ldots$` | P135 |
| E224 | 43:135:L53 | deleted | `\unsure{et ensuite}` | P135 |
| E225 | 43:136:L11 | deleted | `\unsure{S\sigma}` | P136 |
| E226 | 43:136:L20 | deleted | `\operatorname{Ext}^{\unsure{j}}` | P136 |
| E227 | 43:136:L31 | deleted | `\unsure{\infty}` | P136 |
| E228 | 43:136:L60 | deleted; inside margin | `\unsure{m}` | P136 |
| E229 | 43:136:L60 | deleted; inside margin | `\unsure{m}` | P136 |
| E230 | 43:138:L4 | inserted | `3-i` | P138 |
| E231 | 43:138:L5 | deleted | `\unsure{G}` | P138 |
| E232 | 43:138:L5 | deleted | `\operatorname{Ext}` | P138 |
| E233 | 43:138:L5 | inserted | `\unsure{\underline H}` | P138 |
| E234 | 43:138:L5 | inserted | `2-i` | P138 |
| E235 | 43:138:L6 | deleted | `\operatorname{Ext}` | P138 |
| E236 | 43:138:L6 | inserted | `\unsure{\underline H}` | P138 |
| E237 | 43:138:L14 | deleted | `$\underline H^i_{U/k}(G)$` | P138 |
| E238 | 43:138:L15 | deleted | `\unsure{isom}` | P138 |
| E239 | 43:138:L18 | deleted | `\underline H^{i\deleted{\unsure{+1}}}_{S/k}(\unsure{\widehat G\|\widetilde G})` | P138 |
| E240 | 43:138:L18 | deleted; inside deleted | `\unsure{+1}` | P138 |
| E241 | 43:140:L2 | deleted | `$H^i(C,$` | P140 |

## E. Completion and limits

All 46 expected pages were read in scan order as frozen text. The register contains every `\mspage` occurrence and the additional centered typed number marks. The explicit question census, deferred-work clauses, whole cancellations, and all encoded deletion/insertion markers have been checked; source-reading ambiguities remain those recorded by the frozen transcription.

The main notes retain responsibility for mathematical proof or refutation. In particular, this inventory points to the literal flatness sentence at **43:110:L35–36** and the unshifted boxed support comparison at **43:140:L36**, without duplicating the separate degree-zero/module calculations prepared for those notes. No existing RESULTS_STATE status has been updated.

The full-detail outputs are this report and `records/research_flags_titles_searches.jsonl`; the subsequently requested compact assembly register is `records/research_standing_sections.md`. The searches are limited to the supplied context; no external literature, source images, or unsupplied packages have been consulted.

### Provenance update from the main researcher

After completion of this supplied-context-only inventory, the main researcher identified the reused typed witness on scans 103/101/105 with M. F. Atiyah, *Thom Complexes*, published pp.308–310; see main-notes R03 for the primary-source comparison and publication variants. The author is not named on the faces. This update changes no frozen reading and no limited no-match statement about the supplied context.
