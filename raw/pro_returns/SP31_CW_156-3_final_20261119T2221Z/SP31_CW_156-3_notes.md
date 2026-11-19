# Research notes — SP31, cote 156-3, scans 002–025

## Scope, sources and status

These notes concern all 24 supplied scans, manuscript pages 1–24. The transcription was frozen at **2026-11-19 21:46:48 UTC**, before the context was opened; none of the research findings or suggested repairs below changes its words, symbols, deletion states or drawings. Root alone read every image twice in sequence; the supporting research workers read only frozen text and supplied context after the freeze.

The source abbreviations used beside every item are:

- **E**: `SP31_CW_156-3_context/Esquisse_cote119_copy1_API_transcription.tex`; `119/nn` means that file’s exact scan-page tag. The packet calls this an API transcription not checked by eye, so it is a textual comparison source here, not fresh image evidence.
- **RS / RESULTS_STATE**: `SP31_CW_156-3_context/notes/RESULTS_STATE.md`, read before these notes. IDs are preserved below; their statuses remain claims of the earlier returns unless the register expressly says otherwise. Underlying files not included in this packet were not consulted.
- **S**: `SP31_CW_156-3_sweep3/readings/156-3.md`, with its `156-3_CHECK_EVENTS.tsv`, `156-3_CORRECTIONS.tsv`, `156-3_INTEGRATION.md` and `STUDY.md` where named. The sweep’s 156-3 research reader explicitly reports no image viewing; its mathematical claims and editorial corrections therefore require their own checks.
- **C01/C02/C03**: the three `J156-3-0n_notes.md` files under the supplied witness-C folders, audited item by item in the standing sections below.

The context links are structural where the exact vocabulary is absent: searches of E find no réseau, tronçon, biordre or pro-objet after joining line-end hyphenation. Per-note searches and the passages actually compared are documented in `research/note_context_search.tsv`, `research/context_search.tsv` and `research/context_links.md`; a lexical match alone is never treated as a mathematical identification. All displayed proofs and counterexamples are bounded checks of supplied claims, not claims of novelty or a completed literature review.

**Interpretation used for mathematical checking.** “Tronçon” in the proofs below means the coherent prose order axioms: at least two elements, global upper and lower directedness, divisibility, and the stated local direction of nonempty strict cones. This does not silently repair the visible variable slips on009, the weak-between shortcut on012, the closed brackets on011, or the endpoint ambiguities on018. “Marked frontier” means finite order-bound data under an explicitly stated consistent relative-endpoint convention; it is not automatically a canonical topological frontier.

## Principal findings and context implications

| Finding | Scope and evidence | Main notes |
|---|---|---|
| The ordered-model reconstruction works with precise hypotheses. | Strict betweenness recovers the order up to opposite using global directions and density; prescribed pair cut partitions recover strict betweenness. The literal weak-between degeneracy shortcut needs repair. | SP31-N012-03, N013-03, N016-01/03; `research/math_checks.md` MC16–MC17 |
| The currently written network axioms leave important information undetermined. | Doubled rational lieux give two different singleton cuts with the same moderate complement; fixed indiscrete partitions admit two different frontier assignments. | SP31-N003-02, N004-02 |
| The unrestricted difference theorem fails. | In doubled Q, two closed moderate upper sets of the same moderate complement have a non-moderate intersection; no least upper set exists. Restricting upper sets to those compatible with Y is a proposed refinement, not a proved replacement theorem. | SP31-N021-04; `research/join_check.md` |
| The canonical topology does not recover total order or force T₀ or sobriety. | The strict-coordinate order on R² is non-total with Euclidean topology; the doubled rational line fails T₀ and sobriety. Whether every T₀ tronçon is sober remains unproved here. | SP31-N009-01, N022-03, N023-01/02/03 |
| Finite marked boundaries and order-cut components have to be distinguished from topological ones. | A valid order interval has an infinite topological perimeter in the R² example; rational intervals are not topologically connected. | SP31-N018-02/04, N019-01, N022-01 |
| The join of compatible finite unions has a positive order-theoretic proof. | The proof uses divisibility and chain-ordered endpoint gaps to force an input convex piece into one output component; the finite-boundary statement uses the explicit endpoint convention. | SP31-N020-01; `research/join_check.md` |
| The supplied sweep’s ordinary product-order model is inadmissible. | Its strict upper cone at (0,0) is not downward directed. The strong-coordinate order is explicitly a different construction. | SP31-N009-02; MC01–MC02 |

**S14.** The packet README’s proposed finite-cut/pro-object interpretation receives genuine ingredients from Dec₁–Dec₂: finite class sets and coherent refinement maps (006). It still lacks an intrinsic realization theorem, topology recovery and an appropriate cofiltered index; the naive index of finite chains fails the common-refinement condition when two lieux are incomparable (007). This is a precise obstruction to that index, not a refutation of every possible S14 construction.

**B10 and the broader register.** E119/57–58 note(6) and RS entries `MPL_150_001-043 Q4b`, `MPL_150_085-099+151_001-031 K02`, `MPL_151_032-075 Q4-02` and `MPL_150_044-084 T05` contain the supplied compact tame/PL claims; the present scans contain no proof of that comparison. E119/33,41 asks for stronger comparisons of isomorphism spaces, while E119/58–59 requires composition maps beyond adjoining pair tubes for multiplicities; neither follows from recovering an order on a fixed set. No concrete solution to the nine explicitly open RS entries is claimed: the relevant contribution is the bounded order and topology analysis, not a new status for unrelated LM4, RESIDUE, PATHS or exit questions.

## Page-by-page notes

Each numbered item has one kind and a one-to-four-sentence principal note, followed by its context relation, relevant register IDs and actual check status. “Unproved claim” describes how a claim is presented in the manuscript; the accompanying check may verify a precisely stated interpretation, identify a missing hypothesis or refute the broad formulation. “Self-flagged” records the author’s own question or reservation, independently of its answer in these notes.

### Scan 002 — manuscript page 1

#### SP31-N002-01 — A new axiomatics, with a bounded objective

**Kind:** conjecture. **Locus:** opening and data (a).

“Je voudrais définir une autre axiomatique” announces a replacement presentation of networks on a set of lieux: moderate pairs are primitive, and finite moderation is defined pairwise. This adds a concrete cut-based test case to the Esquisse’s program of reconstructing stratified objects from pieces, but the present page does not define a general form or give a reconstruction equivalence. S14 is therefore motivated here, not established.

**Context and relation:** E 119/27,32–34: pièces de construction; axiomatique; provisional systems. S §1.1 restates the current proposal.

**Relevant IDs:** `WG2 B15 (§1.2)`; `MPL_150_044-084 Q9`; `S14 (packet README)`

**Check in this run:** carried as background without fault found. Carried with the stated limits; no independent proof is claimed for this item.

#### SP31-N002-02 — The finite moderate sets form a flag complex

**Kind:** own idea. **Locus:** definition of finite moderate T.

The condition “P₂(T)⊂S₀” makes the finite moderate subsets exactly the cliques of the graph with vertex set L and edge set S₀, so they form an abstract simplicial complex determined by its edges. This is a useful finite combinatorial organization of the input, but supplies neither the complement partitions nor the attachment maps needed for geometric reconstruction. In particular it should not be identified with the flag-indexed spaces of the Esquisse merely because both constructions use finite flags.

**Context and relation:** E 119/36–37,58–59: Drap(I), pair tubes, and additional composition data.

**Relevant IDs:** `WG2 §3.1 #2`; `STRATA A.4`; `EXIT_ONE_TYPE P4e`

**Check in this run:** targeted proof check. Every subset of a clique is a clique; the edge relation alone specifies the finite moderate-set complex. No realization theorem checked.

**Own-idea confidence and reason:** High for the combinatorial statement: it is an immediate consequence of the displayed pairwise definition; no novelty claim.

#### SP31-N002-03 — GF III in the frozen text versus CF III in the context

**Kind:** reading question. **Locus:** upper-right enclosed annotation.

The frozen transcription reads “GF III,” whereas S’s title and later cross-reference call this part “CF III.” That discrepancy is an editorial reading question, not permission to change the now-frozen letter; the G reading was based on the inward foot visible in the enlarged annotation. The later page 156-7/071 is not among the present images, so the context supplies a nomenclatural lead only.

**Context and relation:** S title, §1.7 and §3; STUDY §4 and appended 156-3 reading; later 156-7/071 is reported there.

**Relevant IDs:** `S14 (packet README)`

**Check in this run:** carried as background without fault found. Post-freeze contextual discrepancy recorded; no TeX change and no later image inspected.

### Scan 003 — manuscript page 2

#### SP31-N003-01 — The complement-recovery question is answered in the margin, but not safely proved

**Kind:** self-flagged: a step he himself marks as unverified. **Locus:** long oblique margin; lower NB.

“Question : T est-il connu quand on … C_L(T) ?” is followed by “l’inverse est-il vrai ? Oui” and a short attempted proof, then repeated as an affirmative NB. The proof needs a point in T′ outside T to be compatible with every point of T, a condition not supplied merely by T and T′ each being moderate. Thus this is a question the manuscript locally answers, whose answer must still be tested rather than silently treated as an open question or a valid theorem.

**Context and relation:** S §1.1 explicitly notices the missing compatibility; E 119/28–29 contrasts primitive pieces with actual geometric complements.

**Relevant IDs:** `PATHS E.10`; `EXIT_ONE_TYPE P4e`

**Check in this run:** targeted proof check. Checked the logical use of membership in C(T); individual moderation of T and T′ does not imply their union is moderate.

#### SP31-N003-02 — A valid tronçon with two different singleton cuts having the same complement

**Kind:** own idea. **Locus:** C(T) definition and affirmative margin.

Take L=Q×{0,1}, ordered by (q,i)<(r,j) exactly when q<r; its two points a=(q,0), b=(q,1) at one level are incomparable, yet C({a})=C({b}) is the set of all other levels. This model satisfies the prose local/global directedness and divisibility axioms of scan 009, and its finite-chain gap partitions satisfy Dec₁–Dec₂, while no finite moderate set is maximal. Consequently the current axioms do not make T↦C(T) injective, even within the ordered model; the margin’s universal affirmative answer needs an additional separation hypothesis.

**Context and relation:** S §1.1 raises but does not settle this issue; S §1.5 / SA21-R3-08 supplies the doubled-line model for a different question. E 119/34 emphasizes testing provisional axioms.

**Relevant IDs:** `WG2 B15 (§1.2)`; `MPL_150_044-084 Q9`

**Check in this run:** targeted proof check. Explicit twin-singleton counterexample verified, including the applicable cut finiteness/refinement axioms; see research/math_checks.md. Refines the scan003 assertion.

**Own-idea confidence and reason:** High: both complements and all stated hypotheses have explicit descriptions; not claimed new in the literature.

#### SP31-N003-03 — “Connected components” are initially equivalence classes

**Kind:** unproved claim. **Locus:** data (b), last paragraph.

The classes of R_T are named “comp. connexes de C(T)” before a topology on L has been chosen. Their topological interpretation is therefore extra content, not a consequence of having an equivalence relation, and later interval examples over Q show why the distinction matters. The corresponding register warnings about component-only data are analogies, not proofs about this manuscript.

**Context and relation:** E 119/12 uses actual cell-complement components; E 119/28–29 retains boundary and attachment maps. S §1.4 revisits the issue at scan019.

**Relevant IDs:** `PATHS E.10`; `EXIT_ONE_TYPE P4e`

**Check in this run:** carried as background without fault found. Carried with the stated limits; no independent proof is claimed for this item.

### Scan 004 — manuscript page 3

#### SP31-N004-01 — Recovering boundary data and all cuts from two-point cuts

**Kind:** conjecture. **Locus:** “Je prévois” and numbered 1°, 2°.

“Je prévois que les axiomes impliquent” separates two expectations: frontier data (c) should follow from the partitions (b), and all partitions should follow from the two-point partitions. Scans 011–016 later give a recovery argument in the ordered model, but do not supply the full intrinsic axioms for arbitrary network data. The Esquisse’s explicit warning that some triple composition maps are not determined by adjacent pair data marks a limit on extending this special reconstruction pattern to general stratified objects.

**Context and relation:** E 119/58–59, note (7), especially the NB about the undetermined long-edge map; S §2 lists the general axiom task as open.

**Relevant IDs:** `EXIT_ONE_TYPE P4e`; `STRATA B.1`; `MPL_150_044-084 N18`; `156-3-betweenness-from-cuts`

**Check in this run:** carried as background without fault found. Carried with the stated limits; no independent proof is claimed for this item.

#### SP31-N004-02 — The displayed provisional axioms do not yet determine the frontier

**Kind:** own idea. **Locus:** data (c), compared with 005–006.

Let L be infinite, let every pair be moderate, and give each C(T)=L\T one indiscrete equivalence class for every finite T. Both frontier assignments ∂C(T)=∅ and ∂C(T)=T satisfy ∂C(T)⊂T and Dec₂, and Dec₁ has one class; the finite/cofinite and maximal-finite premises on scan005 never arise. Hence the displayed axioms alone leave (c) underdetermined even when every R_T is fixed, identifying a missing requirement rather than refuting his prediction about a completed axiom system.

**Context and relation:** E 119/34: provisional axioms may require additions after concrete tests; S §2 leaves the general (c)-from-(b) task open.

**Relevant IDs:** `MPL_150_044-084 Q9`; `S14 (packet README)`

**Check in this run:** targeted proof check. Two distinct frontier structures on identical pair and partition data checked against exactly the currently displayed axioms; detailed hypothesis boundary in research/math_checks.md.

**Own-idea confidence and reason:** High under the explicitly stated axiom list; a stronger unwritten intended axiom could exclude the example.

### Scan 005 — manuscript page 4

#### SP31-N005-01 — The discrete example is not a universal finiteness conclusion

**Kind:** unproved claim. **Locus:** Ex 1 and final Axiome.

The page specifies a discrete network and proposes that a maximal finite moderate T must be all of L, with the resulting structure discrete. This rules out finite maximal cuts in a nondiscrete infinite model, but does not assert that L itself is finite or that every complete moderate-pair graph has the discrete partition structure. The distinction matters for the countermodel in SP31-N004-02 and for any proposed finite reconstruction of an infinite form.

**Context and relation:** E 119/32–34: local moderate models and provisional axioms; S §1.1 summarizes this discrete test.

**Relevant IDs:** `MPL_150_044-084 Q9`; `WG2 B15 (§1.2)`

**Check in this run:** carried as background without fault found. Carried with the stated limits; no independent proof is claimed for this item.

### Scan 006 — manuscript page 5

#### SP31-N006-01 — Finiteness is a provisional choice of axioms

**Kind:** self-flagged: a step he himself marks as unverified. **Locus:** opening: finiteness hypotheses.

The qualification “peut-être provisoires” applies to the severe finiteness hypotheses introduced here. It is a reservation about which axiom system to adopt, not a missing proof of Dec₁, which is being imposed. This is closely parallel to the Esquisse’s admission that concrete tests may force extra or different axioms.

**Context and relation:** E 119/34: “plausible provisoire”; S §1.1.

**Relevant IDs:** `MPL_150_044-084 Q9`

**Check in this run:** carried as background without fault found. Carried with the stated limits; no independent proof is claimed for this item.

#### SP31-N006-02 — Dec₂ gives a coherent finite-set refinement system

**Kind:** unpursued implication. **Locus:** Dec₁–Dec₂ and inclusion diagram.

For T⊂S, the unique containing component in Dec₂ defines a map from the finite class set of C(S) to that of C(T). For T⊂S⊂U, the direct map and the composite agree by the same uniqueness, so the written axiom already gives coherent transition maps on the inclusion category of moderate cuts. This is a genuine ingredient for S14, although neither cofilteredness of that category nor a geometric reconstruction theorem follows.

**Context and relation:** E 119/36–37: a system indexed by flags with additional maps and structure; packet README S14.

**Relevant IDs:** `WG2 B15 (§1.2)`; `STRATA A.4`; `S14 (packet README)`

**Check in this run:** targeted proof check. Transition-map composition follows from uniqueness of the containing R_T class, using nonempty equivalence classes; only this formal coherence checked.

### Scan 007 — manuscript page 6

#### SP31-N007-01 — The ordered example has finite cut pieces, not necessarily topologically connected pieces

**Kind:** unproved claim. **Locus:** Ex 2, component list and n+1 count.

The “n+1 composantes connexes” are the successive order gaps of a finite chain, with frontier labels recorded underneath. Density and absence of endpoints make those order pieces nonempty, but on Q the corresponding ordinary order-topological intervals are not connected. Read this as the model’s prescribed cut partition unless an additional topological connectedness hypothesis is given; the frozen final interval’s closing bracket and absent plus sign remain diplomatic readings.

**Context and relation:** E 119/12 and119/28–29 distinguish actual geometric pieces; S §1.2, with the topological refinement in SA21-R3-06.

**Relevant IDs:** `PATHS E.10`; `WG2 B15 (§1.2)`

**Check in this run:** carried as background without fault found. Carried with the stated limits; no independent proof is claimed for this item.

#### SP31-N007-02 — The obvious finite-chain index is not generally cofiltered

**Kind:** own idea. **Locus:** finite chains as moderate cuts; compared with 010.

If u and v are incomparable, their singleton cuts have no common upper bound in the poset of finite moderate subsets, because a finite chain cannot contain both. Thus reversing the inclusion refinement order does not automatically give the cofiltered index required for the naive pro-object version of S14. A larger category of cuttings or a compatibility restriction might address this obstruction; the broad planning guess is not refuted.

**Context and relation:** E 119/36–37; packet README S14; research/context_links.md CTX-OWN1.

**Relevant IDs:** `WG2 B15 (§1.2)`; `STRATA A.4`; `S14 (packet README)`

**Check in this run:** targeted proof check. The missing common refinement is a direct consequence of finite moderation being the chain condition; no claim about every possible pro-object presentation.

**Own-idea confidence and reason:** High for this specific index obstruction; alternative indexing constructions remain open.

### Scan 008 — manuscript page 7

#### SP31-N008-01 — Order reversal loses orientation but preserves the cut data

**Kind:** unpursued implication. **Locus:** opening paragraph and interval cases.

“Elle ne dépend que du biordre” asserts invariance when the order is replaced by its opposite. The same comparable pairs and the same unlabeled interval pieces survive, while their left/right ordering is reversed; this explains why the later reconstruction aims at an order up to reversal. It is a statement about these data on L, not an isotopy or homotopy equivalence of the spaces envisioned in the Esquisse.

**Context and relation:** E 119/33,36: comparison of categories and flag systems is stronger and different; S §1.2.

**Relevant IDs:** `156-3-order-from-betweenness`; `MPL_121_001-048 Q4.3`

**Check in this run:** carried as background without fault found. Carried with the stated limits; no independent proof is claimed for this item.

#### SP31-N008-02 — Finite unions introduce a second level of moderation

**Kind:** unproved claim. **Locus:** Partie modérée and final frontier sentence.

A moderate part is now a finite union of mutually compatible disjoint tronçons, and its boundary is declared to be the disjoint union of their boundaries. This advances beyond finite moderate subsets of lieux, so the two uses of moderate should not be conflated. S reports that 156-7/071 later renames the classes, but that retrospective terminology is context only and was not imported into the transcription.

**Context and relation:** E 119/32–34 concerns axioms for moderate parts; S §1.2 and SA21-K3-01, citing later156-7/071.

**Relevant IDs:** `MPL_150_044-084 Q9`; `S14 (packet README)`

**Check in this run:** carried as background without fault found. Carried with the stated limits; no independent proof is claimed for this item.

#### SP31-N008-03 — The instruction to rewrite beyond the line is taken up later

**Kind:** self-flagged: a step he himself marks as unverified. **Locus:** slanted “refaire” instruction; closed-sub-tronçon discussion018,025.

“Refaire, sans se borner à une ligne” explicitly calls for a more general formulation and ends with an unfinished sentence about the boundary. Scans018 and025 take up that request, but the later topology difficulties and canceled boundary block show that the boundary issue remains unsettled in this excerpt. This is a locally pursued revision request, not an overlooked instruction still wholly untouched.

**Context and relation:** E119/34–35 on provisional axioms and boundary meanings; S§1.2,1.4–1.6 gives the subsequent sequence.

**Relevant IDs:** `MPL_150_044-084 Q9`

**Check in this run:** carried as background without fault found. Carried with the stated limits; no independent proof is claimed for this item.

### Scan 009 — manuscript page 8

#### SP31-N009-01 — The order axioms do not force a linearly ordered or one-dimensional object

**Kind:** own idea. **Locus:** Definition and conditions a–d.

On R² define u≤ₛv to mean u=v or both coordinates of u are strictly smaller than those of v. This non-total order is directed both ways, divisible, and has directed nonempty strict cones, so it satisfies the prose tronçon conditions; its strict intervals are ordinary open rectangles. Thus those conditions alone admit a model with the Euclidean plane as canonical topology, a concrete limit on inferring one-dimensional geometry from the name tronçon.

**Context and relation:** S §1.2 intends non-total examples, but its ordinary product-order example needs the distinction in SP31-N009-02; E 119/32–34 supplies only a broad axiomatic program.

**Relevant IDs:** `MPL_150_044-084 Q9`; `WG2 B15 (§1.2)`; `S14 (packet README)`

**Check in this run:** targeted proof check. Verified the explicitly different strong-coordinate order using coordinatewise bounds with positive gaps; interval basis identified. See research/math_checks.md.

**Own-idea confidence and reason:** High: all order axioms and the interval basis are directly checked; no novelty claim.

#### SP31-N009-02 — The sweep’s ordinary product-order example fails a written axiom

**Kind:** reading question. **Locus:** local directedness condition a; S §1.2.

S says that R² with the product order satisfies the tronçon axioms, but in the usual coordinatewise order x=(1,0) and y=(0,1) both lie strictly above a=(0,0) and have no common lower bound still strictly above a. This violates the displayed requirement that L_{>a} be downward directed. The strong-coordinate order of SP31-N009-01 is a separate valid model, not a silent reinterpretation of S’s ordinary product example.

**Context and relation:** S §1.2 and STUDY’s appended156-3 discussion; SA21-R3-11 later uses ordinary product boxes outside the current image range.

**Relevant IDs:** `MPL_150_044-084 Q9`

**Check in this run:** targeted proof check. Three-point coordinate obstruction refutes S’s example under the usual product order. Its outside-range consequence is not used as a verified counterexample here.

#### SP31-N009-03 — The written variables are not silently corrected in the mathematical reading

**Kind:** reading question. **Locus:** axiom a and dual a′.

The frozen text contains the literal “a>a” in the expanded a-clause and “a,y≤z<a” in the dual conclusion. The surrounding prose clearly states the local directedness requirements, but the written quantified expansions contain variable slips if read literally. The examples and proofs in these notes explicitly use those prose requirements; changing the formulas to the expected variables would be an editorial emendation.

**Context and relation:** S §1.2 restates the prose conditions in repaired mathematical form; E has no tronçon definition.

**Relevant IDs:** `156-3-order-from-betweenness`

**Check in this run:** carried as background without fault found. Literal-versus-intended formula distinction recorded after freeze; no manuscript formula edited.

### Scan 010 — manuscript page 9

#### SP31-N010-01 — Flags of lieux are not the Esquisse’s enriched flag system

**Kind:** unpursued implication. **Locus:** S₀=Drap₂ and Modf=Drap displays.

The identification of moderate finite sets with flags makes the ordered example’s admissible cuts combinatorially explicit. In E119/36 the flags instead index spaces attached to strata, together with retractions, embeddings and fibrations. The common notation therefore supports a comparison of organization, not an identification of data or an automatic application of the finite-poset realization results.

**Context and relation:** E119/36–37; S§1.2.

**Relevant IDs:** `STRATA A.4`; `STRATA B.1`; `WG2 B15 (§1.2)`

**Check in this run:** carried as background without fault found. Carried with the stated limits; no independent proof is claimed for this item.

#### SP31-N010-02 — A type mismatch in the final set-builder remains a reading question

**Kind:** reading question. **Locus:** last equality.

The final displayed comprehension literally has S⊂P_f(L), where the prose and neighboring flag formula suggest a finite subset S of L. S’s summary uses the mathematically coherent finite-chain interpretation, but that does not change the recorded subset sign. A future critical edition should distinguish a notational slip from a different intended domain rather than normalizing it inside this diplomatic text.

**Context and relation:** S§1.2, “the finite tame parts are the finite chains”; E119/36 uses flags in a different domain.

**Relevant IDs:** `156-3-order-from-betweenness`

**Check in this run:** carried as background without fault found. Carried with the stated limits; no independent proof is claimed for this item.

### Scan 011 — manuscript page 10

#### SP31-N011-01 — The recovery assertion is fulfilled later in the ordered model

**Kind:** unproved claim. **Locus:** “Je dis que l’on récupère”.

The page asserts recovery of the biorder from data (a) and the pair-cut part of (b), and scans012–016 supply the intervening betweenness arguments. This supports the two Hua findings listed in RESULTS_STATE as claims about data already arising from a tronçon. It does not yet solve the converse realization problem for abstract pair relations and abstract partitions, which scan017 explicitly leaves to be formulated. This run checks the coherent argument in MC16–MC17, with the degeneracy correction of SP31-N012-03 and the prescribed open-cut interpretation.

**Context and relation:** RESULTS_STATE, final Hua findings section; S§1.3, SA21-R3-01 and03; E119/58–59 gives a structural contrast.

**Relevant IDs:** `156-3-order-from-betweenness`; `156-3-betweenness-from-cuts`; `EXIT_ONE_TYPE P4e`

**Check in this run:** targeted proof check. The manuscript recovery step was checked after freeze in research/math_checks.md MC16–MC17: corrected weak betweenness and prescribed open cut partitions are explicit hypotheses; the literal TeX is unchanged.

#### SP31-N011-02 — Closed displayed intervals conflict with the complement definition

**Kind:** reading question. **Locus:** component list after the finite enumeration.

Several middle entries are written with closed brackets [s_i,s_{i+1}], although C(S) was defined to exclude every point of S. Read literally, those sets cannot be classes in a partition of C(S), because they contain the removed endpoints. S summarizes the cut pieces as open gaps, so the notes record the conflict without changing the visible brackets or assuming that the page meant closures.

**Context and relation:** S§1.2 and§1.3; comparison with current003,007; E119/12 on actual complement components.

**Relevant IDs:** `156-3-betweenness-from-cuts`

**Check in this run:** targeted proof check. Checked the set-theoretic incompatibility of included endpoints with C(S)⊂L∖S; suggested open-gap interpretation remains an editorial reading question.

#### SP31-N011-03 — The extreme-gap sentence also needs qualification

**Kind:** reading question. **Locus:** “les seules non vides éventuelles”.

The phrase “les seules non vides éventuelles” is followed by the lower ray when s₁ is a least element and the upper ray when s_n is a greatest element. Those rays are empty under precisely the parenthetic conditions, so the literal adjective and its explanation pull in opposite directions. The correct combinatorial count must treat empty extreme gaps separately, without repairing this phrase in the transcription.

**Context and relation:** S§1.2 compresses the interval calculation; current010 identifies the extremities.

**Relevant IDs:** `156-3-betweenness-from-cuts`

**Check in this run:** targeted proof check. A strict ray below a least element or above a greatest element is empty; the literal wording is not used as a nonemptiness theorem.

### Scan 012 — manuscript page 11

#### SP31-N012-01 — Strict betweenness determines comparability using density

**Kind:** unproved claim. **Locus:** Lemme and disjointness criterion.

The proof first recovers “a et b disjoints” from existence of a point strictly between them, explicitly invoking “divisibilité !” This isolates the hypothesis that turns the ternary relation into the binary comparability relation; the reconstruction claim is already registered by Hua and carried by SA21-R3-01. The present contribution is the precise manuscript route and its hypothesis, not a new claim of priority or a literature theorem. This run checks the coherent argument in MC16–MC17, with the degeneracy correction of SP31-N012-03 and the prescribed open-cut interpretation.

**Context and relation:** RESULTS_STATE finding156-3-order-from-betweenness; S§1.3/SA21-R3-01; E119/36 shares flag language but contains no proof of this order statement.

**Relevant IDs:** `156-3-order-from-betweenness`

**Check in this run:** targeted proof check. The manuscript recovery step was checked after freeze in research/math_checks.md MC16–MC17: corrected weak betweenness and prescribed open cut partitions are explicit hypotheses; the literal TeX is unchanged.

#### SP31-N012-02 — Strict and non-strict betweenness must remain separate

**Kind:** reading question. **Locus:** long NB with R and barred R.

The NB says that knowledge of R “implique” knowledge of the non-strict relation, then uses a small-cardinality flag condition in its reformulation. The opposed-arrow shape remains uncertain in the frozen text, and H’s stronger verb équivaut is not its literal wording. Independently of that graphic doubt, SP31-N012-03 shows that the small-cardinality alternative includes a repeated-endpoint triple which is not weakly between, so a formal restatement needs an explicit degeneracy correction.

**Context and relation:** S§1.3 states the strict relation; E119/58–59 is a comparison of different low-arity coherence data.

**Relevant IDs:** `156-3-order-from-betweenness`; `156-3-betweenness-from-cuts`

**Check in this run:** carried as background without fault found. Carried with the stated limits; no independent proof is claimed for this item.

#### SP31-N012-03 — The small-cardinality shortcut includes a forbidden repeated-endpoint triple

**Kind:** own idea. **Locus:** NB, “drapeau de cardinal ≤2”.

The triple (a,b,c)=(0,1,0) in the ordinary rational order has a flag {a,b,c} of cardinal2, but b is neither weakly nor strictly between the equal endpoints a=c. Thus the NB’s small-cardinality alternative is too broad if treated as an equivalence defining weak betweenness. The repaired degeneracy condition requires b=a or b=c together with comparability of the remaining endpoints, with the all-equal case included; the strict-relation reconstruction can then be examined separately.

**Context and relation:** S§1.3/SA21-R3-01 and RESULTS_STATE finding156-3-order-from-betweenness carry the reconstruction, but do not record this literal degeneracy defect; E supplies no corresponding order formula.

**Relevant IDs:** `156-3-order-from-betweenness`

**Check in this run:** targeted proof check. Substituted the repeated-endpoint triple into both the written shortcut and weak-order inequalities; refinement is explicit and leaves the frozen NB unchanged.

**Own-idea confidence and reason:** High: an elementary three-entry substitution; not a claim of a new general theorem.

### Scan 013 — manuscript page 12

#### SP31-N013-01 — A chosen oriented pair is the reconstruction seed

**Kind:** unproved claim. **Locus:** opening choice and criterion for u≤v.

Choosing an “origine” a in {a,b} fixes which of the two opposite orders is being recovered. The page describes the rays and middle interval from betweenness, then uses exterior x and y to test u≤v; directedness is what supplies common exterior bounds. SA21-R3-01 carries the reconstruction as checked in the earlier sweep, while this edition preserves the manuscript’s actual formulas and doubts instead of replacing them with that summary. This run checks the coherent argument in MC16–MC17, with the degeneracy correction of SP31-N012-03 and the prescribed open-cut interpretation.

**Context and relation:** S§1.3/SA21-R3-01; RESULTS_STATE finding156-3-order-from-betweenness; E119/36 provides only a structural comparison.

**Relevant IDs:** `156-3-order-from-betweenness`

**Check in this run:** targeted proof check. The manuscript recovery step was checked after freeze in research/math_checks.md MC16–MC17: corrected weak betweenness and prescribed open cut partitions are explicit hypotheses; the literal TeX is unchanged.

#### SP31-N013-02 — Recovery and intrinsic realization are different problems

**Kind:** own idea. **Locus:** orientation choice and four-condition test; compare017.

A useful next test is to separate recovery of an order from data known to come from one, from existence of an order realizing arbitrary proposed relations and pair partitions. The seed orientation and the four-point test suggest checking compatibility as the seed pair changes, but the manuscript does not prove that such local checks suffice. This could organize the open axiomatization request on017 without promoting the special recovery theorem into a general realization theorem.

**Context and relation:** E119/58–59 distinguishes adjacent pair tubes from the extra triple composition map; research/context_links.md CTX-OWN2.

**Relevant IDs:** `156-3-order-from-betweenness`; `156-3-betweenness-from-cuts`; `EXIT_ONE_TYPE P4e`

**Check in this run:** carried as background without fault found. Carried with the stated limits; no independent proof is claimed for this item.

**Own-idea confidence and reason:** Medium: the distinction is explicit in the manuscript, but sufficiency of any proposed compatibility test is unproved.

#### SP31-N013-03 — Only global directions and density are needed for this recovery

**Kind:** unpursued implication. **Locus:** anchor-pair reconstruction013 and lemma014.

After a comparable pair a<b is oriented, strict betweenness recovers the anchor sets L_{≤a} and L_{≥b}, and common lower and upper bounds let the corrected weak-between test decide every u≤v. The explicit proof in research/math_checks.md MC16 uses density only to recover comparability from strict betweenness; if comparability is supplied separately as on015, even density is unnecessary for this stage. The local strict-cone axioms do not enter this recovery, which sharpens the hypothesis accounting without answering the intrinsic realization question.

**Context and relation:** S§1.3/SA21-R3-01,02; RESULTS_STATE finding156-3-order-from-betweenness; E119/58–59 is a structural contrast, not the source of this proof.

**Relevant IDs:** `156-3-order-from-betweenness`

**Check in this run:** targeted proof check. Checked the explicit anchor-set formula and both implications, including repeated endpoints, against MC16; this is a manuscript proof check, not a re-proof of unrelated register entries.

### Scan 014 — manuscript page 13

#### SP31-N014-01 — The finite lemma is a local proof step, not an open conjecture

**Kind:** unpursued implication. **Locus:** Lemme, rewritten proof, “OK” and NB.

The page reduces its comparison to a chain on “2, 3, ou 4” elements and ends the revised proof with “OK.” It therefore supplies a local proof step for the preceding reconstruction claim rather than merely restating an unresolved question; SA21-R3-02 records an earlier targeted check. The final NB distinguishes the roles of divisibility and two-sided directedness, which a later axiomatization should preserve. This run checks the coherent argument in MC16–MC17, with the degeneracy correction of SP31-N012-03 and the prescribed open-cut interpretation.

**Context and relation:** S§1.3/SA21-R3-02; RESULTS_STATE finding156-3-order-from-betweenness; E119/34 on testing proposed axioms.

**Relevant IDs:** `156-3-order-from-betweenness`

**Check in this run:** targeted proof check. The manuscript recovery step was checked after freeze in research/math_checks.md MC16–MC17: corrected weak betweenness and prescribed open cut partitions are explicit hypotheses; the literal TeX is unchanged.

#### SP31-N014-02 — “Trois” remains a textual slip, not an edited numeral

**Kind:** reading question. **Locus:** four variables x,y,u,v in the lemma.

The manuscript names x,y,u,v and writes “trois”; the ink-based edition retains that number. SA21-K3-02 explicitly proposed quatre from the mathematical count without checking this image, so its proposal belongs in commentary. The later allowance of 2,3,4 distinct values also shows why counting variable names is not itself an image-reading argument.

**Context and relation:** S§1.3 and SA21-K3-02; no matching Esquisse passage.

**Relevant IDs:** `156-3-order-from-betweenness`

**Check in this run:** carried as background without fault found. Carried with the stated limits; no independent proof is claimed for this item.

### Scan 015 — manuscript page 14

#### SP31-N015-01 — Binary cut partitions can recover the ternary relation in the model

**Kind:** unproved claim. **Locus:** “On va voir maintenant” and Première condition.

The data here consist of comparable pairs and, for each pair, the unlabeled partition of its moderate complement; the triple must first be a flag. The reconstruction on016 then uses incidence of those parts as subsets of L, not merely the numbers or abstract isomorphism types of the parts. This is the exact scope of Hua’s156-3-betweenness-from-cuts finding and is weaker than reconstructing a stratified space from bare component counts. This run checks the coherent argument in MC16–MC17, with the degeneracy correction of SP31-N012-03 and the prescribed open-cut interpretation.

**Context and relation:** RESULTS_STATE finding156-3-betweenness-from-cuts; S§1.3/SA21-R3-03; E119/58–59 retains maps as part of reconstruction data.

**Relevant IDs:** `156-3-betweenness-from-cuts`; `EXIT_ONE_TYPE P4e`; `MPL_150_044-084 N18`

**Check in this run:** targeted proof check. The manuscript recovery step was checked after freeze in research/math_checks.md MC16–MC17: corrected weak betweenness and prescribed open cut partitions are explicit hypotheses; the literal TeX is unchanged.

#### SP31-N015-02 — The abandoned J-definition is a draft layer

**Kind:** withdrawn in the same text. **Locus:** cancelled final display015; replacement016.

The definition beginning J_{abc}= is crossed out on015, while016 proceeds with three explicitly indexed components X_{\{a,b\}}, X_{\{b,c\}}, X_{\{c,a\}}. The cancelled expression is evidence of the route to the argument, not an additional live definition to reconcile with the later symbols. This also limits any reconstruction based on H’s presentation of that display as live text.

**Context and relation:** S§1.3 summarizes the three-X formulation; E119/36 has no corresponding notation.

**Relevant IDs:** `156-3-betweenness-from-cuts`

**Check in this run:** carried as background without fault found. Carried with the stated limits; no independent proof is claimed for this item.

#### SP31-N015-03 — The punctuation after R is an editorial doubt, not a definite author question

**Kind:** reading question. **Locus:** condition heading after R(a,b,c).

The frozen mark after R(a,b,c) is unsure between a colon and a question mark. Its presence must be recorded, but it cannot support a certain additional self-flagged open question; the subsequent “On gagne !” still records the author’s claimed completion of the comparison. C’s standing list is therefore supplemented with a reading question rather than a new definite interrogative.

**Context and relation:** S§1.3 gives the argument as a recovery proof; E119/58–59 concerns different low-arity data.

**Relevant IDs:** `156-3-betweenness-from-cuts`

**Check in this run:** carried as background without fault found. Carried with the stated limits; no independent proof is claimed for this item.

### Scan 016 — manuscript page 15

#### SP31-N016-01 — The middle element is characterized by disjoint incident-pair components

**Kind:** unpursued implication. **Locus:** three intersections, “divisibilité !”, “On gagne !”.

For a<b<c the page identifies the three pieces as L_{>b}, L_{<b} and ]a,c[, and exactly the two pieces indexed by pairs containing b are disjoint. The other two intersections are ]a,b[ and ]b,c[, whose nonemptiness is the explicit use of divisibility. SA21-R3-03 carries this special cut-partition argument as checked; it does not justify calling those pieces ordinary topological components in every model. This run checks the coherent argument in MC16–MC17, with the degeneracy correction of SP31-N012-03 and the prescribed open-cut interpretation.

**Context and relation:** S§1.3/SA21-R3-03; RESULTS_STATE finding156-3-betweenness-from-cuts; E119/58–59 gives a contrasting richer reconstruction.

**Relevant IDs:** `156-3-betweenness-from-cuts`; `PATHS E.10`

**Check in this run:** targeted proof check. The manuscript recovery step was checked after freeze in research/math_checks.md MC16–MC17: corrected weak betweenness and prescribed open cut partitions are explicit hypotheses; the literal TeX is unchanged.

#### SP31-N016-02 — The final symbol and duplicate primes are preserved independently of the argument

**Kind:** reading question. **Locus:** final distinguishing-property paragraph and display.

The frozen page has apparent primes on both prose pair symbols and a pointed wedge in the final formula, whereas the three preceding tests use intersection signs. The component argument suggests two different incident pairs and an empty intersection, but that mathematical reconstruction is not a license to erase a prime or replace the wedge. Any formal restatement should display its notation changes as editorial interpretation.

**Context and relation:** S§1.3 and Hua finding156-3-betweenness-from-cuts use the mathematically normalized intersection test.

**Relevant IDs:** `156-3-betweenness-from-cuts`

**Check in this run:** carried as background without fault found. Carried with the stated limits; no independent proof is claimed for this item.

#### SP31-N016-03 — Density is essential for the disjoint-class middle test

**Kind:** own idea. **Locus:** nonempty intersections labeled “divisibilité !”.

On a three-element total order, each pair complement consists of the third point, so the three selected classes are distinct singletons and all three pairwise intersections are empty. Every permutation of the three-element order gives the same comparable-pair graph and pair partitions, so those data cannot distinguish the middle without an additional hypothesis. This model deliberately lacks divisibility and therefore tests the need for that hypothesis; it is not offered as a tronçon counterexample.

**Context and relation:** S§1.3/SA21-R3-03 and the registered156-3-betweenness-from-cuts claim require divisibility; E119/58–59 does not state this finite-order example.

**Relevant IDs:** `156-3-betweenness-from-cuts`

**Check in this run:** targeted proof check. Computed all pair complements and their singleton partitions in the three-point order; research/math_checks.md MC17.

**Own-idea confidence and reason:** High: the finite example is exhaustive by inspection and explicitly outside the dense class; no novelty claim.

### Scan 017 — manuscript page 16

#### SP31-N017-01 — The largest category exists under the nonempty-directed convention

**Kind:** unproved claim. **Locus:** Remarques 1, conditions a–c′ and conclusion.

“Il y a … plus grande … T” has a direct verification when directed posets are required to be nonempty. The intended tronçon class satisfies the conditions and is stable under nonempty strict cones; conversely the categorical conditions force global directions, divisibility and the two local cone directions. The replacement of non vide by cardinal ≠1 therefore needs the usual nonemptiness convention, rather than an unqualified claim that cardinal ≠1 by itself means cardinal ≥2.

**Context and relation:** S§1.3/SA21-R3-04; E119/32–34 concerns proposed categories with axioms but does not establish this particular class.

**Relevant IDs:** `156-3-order-from-betweenness`; `MPL_150_044-084 Q9`

**Check in this run:** targeted proof check. Checked stability under strict cones and opposite order and the role of the nonempty-directed convention; research/math_checks.md MC08.

#### SP31-N017-02 — Intrinsic axioms for both descriptions are explicitly left to be found

**Kind:** self-flagged: a step he himself marks as unverified. **Locus:** Remarques 2, final paragraph.

“Il faudrait expliciter” asks for conditions on R(a,b,c), and “itou” on S₀ and the pair-cut relations, that characterize biordered tronçons. The preceding recovery argument therefore does not yet constitute an equivalence with an intrinsically axiomatized data category. The Esquisse’s extra composition maps suggest a useful caution about local data, but are not themselves proposed tronçon axioms.

**Context and relation:** S§2, first open task; E119/58–59, note(7), triple composition beyond adjacent pair data.

**Relevant IDs:** `156-3-order-from-betweenness`; `156-3-betweenness-from-cuts`; `EXIT_ONE_TYPE P4e`; `STRATA B.1`

**Check in this run:** carried as background without fault found. Carried with the stated limits; no independent proof is claimed for this item.

### Scan 018 — manuscript page 17

#### SP31-N018-01 — The interval intersection statement can be proved using marked endpoints

**Kind:** unproved claim. **Locus:** intersection paragraph and oblique “argument topologique”.

The assertion that two compatible wide closed sub-tronçons intersect in another such piece, or in the empty set, follows by taking the larger lower bound and smaller upper bound among their chain-ordered endpoints. The new marked endpoints are among the old ones, proving the finite-frontier inclusion under the consistent relative-endpoint convention stated in SP31-N018-04. This order proof does not need the proposed “argument topologique,” whose identification of marked endpoints with topological boundaries fails in general.

**Context and relation:** S§1.4/SA21-R3-05; E119/35 warns that a boundary need not have its familiar manifold meaning; compare current023–025.

**Relevant IDs:** `MPL_150_044-084 Q9`; `PATHS E.10`

**Check in this run:** targeted proof check. Checked intervals, rays, absent bounds and singleton/empty outcomes; research/math_checks.md MC10. Only the marked-bound convention is used.

#### SP31-N018-02 — Marked endpoint data are not the canonical topological boundary

**Kind:** own idea. **Locus:** “frontière relative” and final “est la frontière”.

In the valid strong-coordinate model of SP31-N009-01, [a,b] for a=(0,0), b=(1,1) is the open unit square together with its two opposite corners. Its marked endpoint set has two points, but its closure is the closed square and its topological boundary is the full perimeter; even in an ordinary bounded chain the ambient extremities require a relative-boundary convention. Thus the blanket identification on018 cannot justify the finite-frontier claims, and the later retreat on023–025 is mathematically substantive.

**Context and relation:** E119/35 and58 distinguishes geometric boundary data from an unjustified identification; S§1.5 notices nonclosed segments but does not supply this model.

**Relevant IDs:** `MPL_150_044-084 Q9`; `STRATA A.4`

**Check in this run:** targeted proof check. Computed the interval, its Euclidean closure/interior and marked endpoints in an admissible tronçon. Relative-boundary convention explicitly distinguished.

**Own-idea confidence and reason:** High: the two sets are computed directly in the verified model; an illustrative check, not a novelty claim.

#### SP31-N018-03 — The boundary variable on the upper ray remains literal

**Kind:** reading question. **Locus:** definition of closed sub-tronçon and inserted frontier list.

The upper ray is written with subscript a after a canceled b, while its exception and frontier entry still use b. The consistent mathematical formulation would use one endpoint throughout, but this is an unpropagated correction in the written definition. The research arguments use a named ray endpoint explicitly and do not silently treat the conflicting letters as a new convention.

**Context and relation:** S§1.4 gives a normalized list of closed rays; E has no corresponding tronçon formula.

**Relevant IDs:** `156-3-order-from-betweenness`

**Check in this run:** carried as background without fault found. Carried with the stated limits; no independent proof is claimed for this item.

#### SP31-N018-04 — Relative endpoint labels must be independent of the presentation

**Kind:** reading question. **Locus:** relative-frontier warning; interval/ray/L cases.

If L has minimum m and maximum M, [m,b]=L_{≤b} and [m,M]=L, yet the unqualified displayed cases assign different endpoint sets to these presentations. A coherent relative-bound convention would omit redundant global endpoints for nondegenerate intervals and rays, while retaining the explicitly prescribed frontier {a} for a singleton. The current text does not spell out that normalization, so the positive finite-frontier arguments in these notes state it as an interpretation rather than an ink correction.

**Context and relation:** E119/35 distinguishes uses of boundary; S§1.4 normalizes the interval calculus without discussing this representation issue.

**Relevant IDs:** `MPL_150_044-084 Q9`

**Check in this run:** targeted proof check. Checked equality of interval/ray/L presentations in a bounded dense chain and the conflict between their unqualified endpoint labels.

### Scan 019 — manuscript page 18

#### SP31-N019-01 — The topological connected-component interpretation is false over Q

**Kind:** reading question. **Locus:** Th 1°, bracket “les comp. conn. de U”.

The literal bracket identifies the pieces Tᵢ with connected components, yet in L=Q the single order interval [0,1]∩Q is separated by every irrational cut between two of its points and has singleton topological components. This verifies the need for S’s correction of the interpretation, without changing the bracket or its residual U in the transcription. S’s later quotation from030 is context only; completeness has not been formalized here for all partial orders, so no blanket positive converse is asserted.

**Context and relation:** S§1.4, SA21-K3-06/SA21-R3-06, reporting later156-3/030; E119/12,28–29 uses genuine geometric components.

**Relevant IDs:** `PATHS E.10`; `EXIT_ONE_TYPE P4e`

**Check in this run:** targeted proof check. Irrational-cut separation in Q checked. Refutes the topological reading, not the separate uniqueness of the prescribed interval decomposition.

#### SP31-N019-02 — Uniqueness and boundary union need a combinatorial formulation

**Kind:** unproved claim. **Locus:** Th 1°–2°, definition and margin X⊂Y.

The page states uniqueness of the finite disjoint interval decomposition, the union formula for its finite boundary, and the implication X⊂Y ⇒ relative moderation. Divisibility proves uniqueness: a convex piece crossing two separated components would contain a point in their endpoint gap, outside the union. The full proof in research/join_check.md establishes this combinatorial uniqueness without topological connectedness, and the boundary and compatibility consequences use the consistent endpoint convention of SP31-N018-04.

**Context and relation:** S§1.4 carries the decomposition argument; E119/28–30 additionally retains attachment information, which this uniqueness statement does not provide.

**Relevant IDs:** `PATHS E.10`; `MPL_150_044-084 Q9`

**Check in this run:** targeted proof check. Root checked the separated-component lemma and the two-decomposition containment proof in research/join_check.md; finite marked boundary uses the explicitly stated normalization.

### Scan 020 — manuscript page 19

#### SP31-N020-01 — The join and finite-family corollary are a distinct proof obligation

**Kind:** unproved claim. **Locus:** Prop, “double récurrence,” and Cor.

The margin proposes a “double récurrence” on component counts for the moderate supremum and its frontier inclusion, but does not write the induction. A full order proof is given in research/join_check.md: sort the common chain of endpoints, merge overlapping pieces into their order hulls, and use divisibility to prove that every convex input piece lies in one component of any admissible upper bound. This establishes leastness even against upper bounds whose endpoints are not compatible with the inputs; global directedness handles ray hulls. The finite-family corollary and preservation of compatibility with a third Z then follow from the marked-boundary inclusion, under SP31-N018-04’s explicit normalization.

**Context and relation:** S§1.4 states the calculus; E119/32–34 gives the wider motivation for stability operations on moderate parts.

**Relevant IDs:** `MPL_150_044-084 Q9`; `S14 (packet README)`

**Check in this run:** targeted proof check. Root read and checked the construction, separated-component lemma, arbitrary-upper-bound leastness including rays, and the conditional finite-boundary consequences in research/join_check.md.

#### SP31-N020-02 — His warning excludes a general closure operator on arbitrary subsets

**Kind:** unpursued implication. **Locus:** Attention in the long margin.

“Il n’y a pas en général d’adh. modérée fermée” is witnessed by A={0,1/2,1/3,…} in [0,1]. Every finite union of closed intervals and points containing A contains some [0,d], and removing a small open gap between two successive reciprocals gives a smaller admissible upper set still containing A. Hence there is no least such upper set even though A is topologically closed, so the moderate operations cannot be extended to an arbitrary-subset closure operator without enlarging the family.

**Context and relation:** S§1.4/SA21-R3-07 already checks this warning; E119/32–34 motivates closure properties but supplies no contrary arbitrary-set claim.

**Relevant IDs:** `MPL_150_044-084 Q9`; `S14 (packet README)`

**Check in this run:** targeted proof check. Rechecked the finite-component/pigeonhole argument and the removable-gap construction; research/math_checks.md MC13.

#### SP31-N020-03 — Moderate join can strictly enlarge ordinary union

**Kind:** own idea. **Locus:** Ex [a,b] moderate-union [b,c]=[a,c].

In the strong-coordinate model take a=(0,0), b=(1,1), c=(2,2): the point (1/2,3/2) belongs to [a,c] but to neither [a,b] nor [b,c]. Divisibility and compatible endpoint ordering force every admissible finite closed upper set of the two intervals to put them in the same component, so [a,c] is their moderate join. This supplies a valid non-total test of the manuscript’s distinction, independently of the sweep’s inadmissible ordinary-product example.

**Context and relation:** S§1.4; compare SP31-N009-01/02 and E119/34 on testing axioms in concrete models.

**Relevant IDs:** `MPL_150_044-084 Q9`

**Check in this run:** targeted proof check. Verified the explicit point and interval hull in the admissible strong-coordinate order; research/math_checks.md MC11.

**Own-idea confidence and reason:** High: membership and the necessary merging argument are explicit; not claimed to be a new result.

### Scan 021 — manuscript page 20

#### SP31-N021-01 — The ray-union test is exactly total comparability

**Kind:** unpursued implication. **Locus:** continuation before the separator.

The condition that every b be comparable with every element is exactly total order, so L_{≤b}∪L_{≥b}=L for every b expresses the stated criterion. The moderate union in the underbrace must therefore be distinguished from that ordinary union in the non-total case. This does not imply the converse from closed points to total order later queried on023; the topology sees different information.

**Context and relation:** S§1.4–1.5; E119/33 cautions by comparison that a structure and its topology-level comparison are different tasks.

**Relevant IDs:** `156-3-order-from-betweenness`

**Check in this run:** targeted proof check. Checked the ordinary-ray-union equivalence directly from the definition of comparability; no separation converse inferred.

#### SP31-N021-02 — The assertion about ordinary difference is explicitly replaced

**Kind:** withdrawn in the same text. **Locus:** crossed-out theorem before C_mod; live replacement on021–022.

The statement that a least closed moderate Z contains X∖Y is crossed out and replaced by the requirement that it contain only C_mod(Y,X), points outside Y compatible with Y. The change matters in a partial order because that compatibility restriction can remove points of ordinary difference. It is a substantive withdrawn formulation on the same page, not a completed theorem about arbitrary ordinary differences.

**Context and relation:** S§1.4 presents the corrected moderate-difference version; E119/32–34 supplies only the general program of stable moderate operations.

**Relevant IDs:** `MPL_150_044-084 Q9`

**Check in this run:** carried as background without fault found. Carried with the stated limits; no independent proof is claimed for this item.

#### SP31-N021-03 — The surviving difference theorem needs its frontier convention stated

**Kind:** unproved claim. **Locus:** live least-Z assertion and notation X moderate-difference Y.

The live theorem asserts a least closed moderate Z containing C_mod(Y,X), containment in X, compatibility with Y, and a universal containment property for compatible disjoint closed T. In the total-order test X=[0,1], Y=[1/3,2/3], it gives Z=[0,1/3]∪[2/3,1], which meets Y in its endpoints and is not literal subtraction. This verifies the intended phenomenon in one model, but SP31-N021-04 refutes the unrestricted minimum in a valid non-total model, so the general statement cannot be carried as proved.

**Context and relation:** S§1.4; E119/28–30 retains frontier data in reconstruction; research/math_checks.md MC14.

**Relevant IDs:** `MPL_150_044-084 Q9`; `PATHS E.10`

**Check in this run:** targeted proof check. The explicit total-order example and universal least closed upper set there were checked; the general difference theorem is not certified by this example.

#### SP31-N021-04 — The unrestricted least moderate difference fails in the doubled line

**Kind:** own idea. **Locus:** live minimum assertion021, continued022.

In the doubled rational line let c=(−1,0), a=(0,0), a′=(0,1), b=(1,0), b′=(1,1), d=(2,0), and set X=[c,d], Y=[a,b]. The moderate complement C consists of the X-points at heights below0 or above1; both Z₀=[c,a]∪[b,d] and Z₁=[c,a′]∪[b′,d] are closed moderate supersets, but Z₀∩Z₁=C is not a finite union of closed order intervals. A least upper set would have to equal C, so the displayed unrestricted minimum does not exist; Z₁ is incompatible with Y, suggesting the distinct refinement of minimizing only among upper sets compatible with Y, which has not been proved in general here.

**Context and relation:** S§1.4 states the minimum without this distinction; S§1.5 supplies the doubled-line example for separation, and E119/34 motivates testing provisional axioms rather than accepting the extension.

**Relevant IDs:** `MPL_150_044-084 Q9`

**Check in this run:** targeted proof check. Verified both upper sets, their exact intersection, and the impossibility of a finite closed-interval decomposition cofinal below height0 without a height0 endpoint; research/join_check.md.

**Own-idea confidence and reason:** High for the explicit counterexample: root and context worker checked the set calculations independently; the restricted repair remains an unproved proposal.

### Scan 022 — manuscript page 21

#### SP31-N022-01 — The finite relative-frontier assertion cannot use an arbitrary topological boundary

**Kind:** unproved claim. **Locus:** opening F paragraph and complement identity.

“Alors F est fini” and C_mod(Y,X)=C_mod(F,Z) continue the difference theorem without a full proof. In the total-order test of SP31-N021-03, F={1/3,2/3} verifies the identity and is not isolated in Z; in the strong-coordinate model with X=L and Y=[a,b], the actual canonical topological frontier is an entire square perimeter. Thus the unrestricted statement needs a combinatorial frontier interpretation or stronger hypotheses before it can be used.

**Context and relation:** S§1.4; E119/35,58 on boundary data; compare current018 and the withdrawn block025.

**Relevant IDs:** `MPL_150_044-084 Q9`; `PATHS E.10`

**Check in this run:** targeted proof check. Checked the stated identity in the total-order example and the obstruction to the literal topological reading in the strong-coordinate example; general theorem left unproved.

#### SP31-N022-02 — The ficelle-specific specialization relation is a representation claim

**Kind:** unproved claim. **Locus:** after (9 juin), final paragraph.

For lieux of a topological ficelle the page says b∈closure{a} “équivaut à b⊃a” as subsets of the ambient space. This is not the original tronçon order being identified with an Alexandrov specialization order; it is a separate containment relation on the represented lieux. The local pages give no full construction of that ficelle representation, so this assertion is carried as a manuscript claim and is not used to prove the universal statements about abstract tronçons.

**Context and relation:** S§1.5; E119/36–37 uses strata and indexed spaces but gives no definition of these lieux; RESULTS_STATE has distinct finite-poset/Alexandrov statements.

**Relevant IDs:** `WG2 B15 (§1.2)`; `STRATA 0.1`

**Check in this run:** carried as background without fault found. Carried with the stated limits; no independent proof is claimed for this item.

#### SP31-N022-03 — Cone profiles compute specialization and separation directly

**Kind:** own idea. **Locus:** topology generated by intervals and strict rays.

Write D(x)={z:z<x} and U(x)={z:x<z}; for the stated canonical topology, b∈closure{a} exactly when D(b)⊆D(a) and U(b)⊆U(a). Indeed these inclusions say that every generating strict ray containing b also contains a, and the property survives intersections and unions. Consequently T₀ is injectivity of the pair (D(x),U(x)), while T₁ requires that no two distinct pairs be ordered by simultaneous inclusion, giving a direct test that does not assume an Alexandrov topology.

**Context and relation:** S§1.5 asks about separation; E has no matching cone-profile formula; compare RESULTS_STATE’s finite-poset variance statements only as a contrast.

**Relevant IDs:** `WG2 B15 (§1.2)`; `STRATA 0.1`

**Check in this run:** targeted proof check. Checked the generating-open characterization of closure, then T₀ and T₁; research/math_checks.md MC05.

**Own-idea confidence and reason:** High: a direct equivalence from the displayed generators, with no claim of novelty.

### Scan 023 — manuscript page 22

#### SP31-N023-01 — The unrestricted T₀ question has a checked negative answer

**Kind:** self-flagged: a step he himself marks as unverified. **Locus:** “je ne sais si c’est le cas pour tout tronçon”.

The doubled rational line of SP31-N003-02 has identical canonical neighborhoods for the two points at each rational height, so it is a valid tronçon which is not T₀. This confirms the sweep’s SA21-R3-08 counterexample and separates the abstract order axioms from the stronger representability of ficelle lieux used just above. It does not deny the manuscript’s T₀ assertion for that narrower represented class.

**Context and relation:** S§1.5/SA21-R3-08; E119/34 suggests model-testing of axioms, but contains no T₀ tronçon theorem.

**Relevant IDs:** `WG2 B15 (§1.2)`; `STRATA 0.1`

**Check in this run:** targeted proof check. Verified both the tronçon axioms and saturation of every canonical open in the twin fibres; research/math_checks.md MC03.

#### SP31-N023-02 — Sobriety without T₀ already fails; the refined question remains

**Kind:** self-flagged: a step he himself marks as unverified. **Locus:** “ni si un tronçon … est sobre” and “A/À voir”.

The same two-point fibre is the closure of either twin and is irreducible, with two distinct generic points, so it also answers the literal unrestricted sobriety question negatively. S leaves a sobriety task open, but its viable refinement is whether every T₀ tronçon is sober; that refined question remains unresolved here. The distinction is uniqueness of a generic point, not merely existence.

**Context and relation:** S§1.5 and156-3_INTEGRATION.md packageP3-1; E119/34 supplies the broad provisional-axiom analogy only.

**Relevant IDs:** `WG2 B15 (§1.2)`; `STRATA 0.1`

**Check in this run:** targeted proof check. Checked irreducibility as closure of a point and failure of unique generic point in the doubled-line example; no result claimed for all T₀ tronçons.

#### SP31-N023-03 — Closed points or Hausdorff topology do not force total order

**Kind:** self-flagged: a step he himself marks as unverified. **Locus:** “Ce n’est que lorsque … tot ordonné” and “réciproque ?”.

The strong-coordinate order on R² is non-total but its canonical topology is exactly Euclidean, hence Hausdorff with closed points. It therefore gives a negative answer to the converse queried here and to a necessary-condition reading of “Ce n’est que lorsque,” while preserving the sufficient total-order statement. The same model is sober because a nonempty irreducible closed subset of a Hausdorff space cannot contain two distinct points.

**Context and relation:** S§1.5 restates the total-order clause but does not give this converse counterexample; E119/34 gives no corresponding assertion.

**Relevant IDs:** `WG2 B15 (§1.2)`; `STRATA 0.1`

**Check in this run:** targeted proof check. Verified the open-rectangle basis and disjoint-neighborhood argument for Hausdorff sobriety; research/math_checks.md MC02/04.

#### SP31-N023-04 — The alternative topology is an experiment, not a final choice

**Kind:** withdrawn in the same text. **Locus:** last paragraph023; failure024; choice025.

The construction “une autre topologie” declares order intervals and rays to generate the closed sets, then024 tests the supremum with the first topology. On025 he explicitly returns to the first topology, retaining “fermé” as an abuse of language. The experiment should therefore be tracked as a local sequence ending in a choice, rather than two interchangeable canonical topologies.

**Context and relation:** S§1.5–1.6; E119/33,41 discusses stronger comparison of structures, not this specific topology choice.

**Relevant IDs:** `STRATA 0.1`; `MPL_150_044-084 Q9`

**Check in this run:** carried as background without fault found. Carried with the stated limits; no independent proof is claimed for this item.

### Scan 024 — manuscript page 23

#### SP31-N024-01 — The closure strategy is proposed and then rejected on the same page

**Kind:** withdrawn in the same text. **Locus:** three question-marked closure formulas and “Mais c’est faux”; return025.

“Aura-t-on” asks for closure of an open interval to be its closed interval and analogous ray equalities. The proposed endpoint argument is immediately met by “Mais c’est faux,” with an elementary open complement excluding the whole interior interval while containing its endpoint. The page itself thus flags and rejects this route, and025 abandons the topology experiment rather than announcing these equalities as proved.

**Context and relation:** S§1.6; E119/34 on the need to revise provisional constructions; compare SP31-N024-02 for an independently checked model.

**Relevant IDs:** `MPL_150_044-084 Q9`

**Check in this run:** carried as background without fault found. Carried with the stated limits; no independent proof is claimed for this item.

#### SP31-N024-02 — An explicit valid tronçon realizes the drawn obstruction’s inequalities

**Kind:** own idea. **Locus:** marginal a∉[x,y], ]a,b[⊂[x,y].

In the strong-coordinate model choose x=(0,−1), a=(0,0), b=(1,1), y=(2,2): a∉[x,y] while every point of ]a,b[ lies in [x,y]. In the supremum topology described in the prose, the complement of [x,y] is therefore an open neighborhood of a disjoint from ]a,b[, so a is not in its closure. This verifies the stated obstruction in a valid order model without claiming that the model is the particular topological ficelle drawn in the margin.

**Context and relation:** S§1.6 describes the ficelle obstruction; E119/34 offers no version of the example; research/math_checks.md MC15.

**Relevant IDs:** `MPL_150_044-084 Q9`

**Check in this run:** targeted proof check. All four-point inequalities and the separating open set checked explicitly. No unseen ficelle representation inferred.

**Own-idea confidence and reason:** High: the order and topology computations are explicit and use a previously verified model; no novelty claim.

#### SP31-N024-03 — The displayed list of generators omits an expected complement sign

**Kind:** reading question. **Locus:** second row of the two-line basis display.

The frozen display ends in plain [a,b], whereas the prose “borne sup. des deux” and the later neighborhood complement[x,y] suggest the complement of [a,b] at that place. The mathematical check in SP31-N024-02 concerns the supremum described in the prose, not a silent change of this printed entry. This is an unpropagated-sign reading question for any future critical reconstruction.

**Context and relation:** S§1.6 gives the supremum-topology interpretation; E has no corresponding formula.

**Relevant IDs:** `MPL_150_044-084 Q9`

**Check in this run:** carried as background without fault found. Carried with the stated limits; no independent proof is claimed for this item.

### Scan 025 — manuscript page 24

#### SP31-N025-01 — The final topology choice explicitly permits nonclosed “closed” intervals

**Kind:** unpursued implication. **Locus:** opening “Finalement” and “par abus de langage”.

“On travaillera avec la top. définie d’abord” is the final choice in this excerpt, and the quotation marks on “fermés” acknowledge the terminology’s mismatch with topological closedness. Consequently later uses of closed sub-tronçon should first be read as order-defined objects, with separate checks for closure, boundary and connectedness. This resolves a local choice but not the intrinsic realization problem left on017.

**Context and relation:** S§1.6; E119/35 likewise warns against importing familiar boundary meanings without the appropriate structure.

**Relevant IDs:** `MPL_150_044-084 Q9`; `STRATA 0.1`

**Check in this run:** carried as background without fault found. Carried with the stated limits; no independent proof is claimed for this item.

#### SP31-N025-02 — The lower boundary definition and all its examples are withdrawn

**Kind:** withdrawn in the same text. **Locus:** lower block025; earlier claims018 and022.

The whole block beginning “pose” is canceled, including the attempted canonical-topological boundary formula, cardinality in {0,1,2}, and the interval/ray examples. These formulas must not be cited as the surviving definition at the end of the passage, especially because the valid counterexample in SP31-N018-02 shows that a canonical topological boundary can be infinite. The text ends after this cancellation without a complete replacement definition in the supplied image range.

**Context and relation:** S§1.6 summarizes the return to the first topology but does not retain this entire cancellation as a live theorem; E119/35,58 keeps geometric boundary data explicit.

**Relevant IDs:** `MPL_150_044-084 Q9`; `PATHS E.10`

**Check in this run:** carried as background without fault found. Carried with the stated limits; no independent proof is claimed for this item.

## Standing questions and complete audit of witness C’s notes

Documentary audit completed 2026-11-19 22:04:54 UTC. The authority for all quotations below is the transcription frozen at 2026-11-19 21:46:48 UTC. Source references use archive scan numbers; TeX line numbers refer to the frozen page files.

This audit checks what C’s notes report, how the author marks a step, and whether the same text subsequently answers, revises or abandons it. “Self-answered” and “addressed” describe the manuscript’s presentation; they do not certify a mathematical proof. No RESULTS_STATE result is used here.

The original notes are `codex/J156-3-01/J156-3-01_notes.md`, `codex/J156-3-02/J156-3-02_notes.md`, and `codex/J156-3-03/J156-3-03_notes.md` in the supplied witnesses. Abbreviations C01, C02 and C03 below refer to those files.

**Audit coverage:**50 original C-note items (15 uncertainty/status items, 24 title/numbering rows, 11 global metadata assertions): 4 correct, 46 keep. No original item is dropped wholesale; corrections qualify the quotation or carryover status. Eight additional documentary status items are supplied below.

### 1. Every original item about unverified or provisional steps

#### C01-U01 — KEEP

C source: `C01 line 7`. Original item: Scan 003 asks whether the moderated complement determines T and whether an inclusion reverses.

`Question : $T$ est-il connu quand on \unsure{connait|connaît} $C_{\mathcal L}(T)$ ?` (scan 003, TeX line 20) The same margin continues `l'inverse est-il vrai ? Oui,` (scan 003, TeX line 21), and the lower NB asserts `$T$\deleted{\unsure{est}} est connu quand on \unsure{connait|connaît} $C(T)$` (scan 003, TeX line 37). Keep this as a question that the author answers on the same page, not as an unanswered item; the sketch’s validity is outside this documentary check.

#### C01-U02 — KEEP

C source: `C01 line 8`. Original item: Scan 004 anticipates recovery of datum c from b and of b from the two-point data.

`Je prévois que les axiomes impliquent` (scan 004, TeX line 11) introduces both stated expectations, and `\uline{Axiomes provisoires :}` (scan 004, TeX line 32) remains the live heading. Scans 011–016 subsequently develop recovery for the tronçon/biorder setting, whereas scan 017 still asks for the intrinsic axioms; do not turn that special-case development into a completed general axiom system.

#### C01-U03 — KEEP

C source: `C01 line 9`. Original item: Scan 006 reserves judgment about the finiteness hypotheses.



```tex
peut-être
provisoires
```

(scan 006, beginning at TeX line 5) qualifies the finiteness hypotheses immediately before Dec₁ and Dec₂. This is a live provisional-status reservation, not a statement that either axiom has been disproved, and no explicit removal of that reservation appears later in these 24 pages.

#### C01-U04 — KEEP

C source: `C01 line 10`. Original item: Scan 008 orders a rewriting beyond the case of a line and leaves a marginal sentence unfinished.

`refaire, sans se borner à une ligne : sous tronçon fermé d'un tronçon.` (scan 008, TeX line 12) is retained, and the final words really are `le bord d'un tronçon est défini Comme des` (scan 008, TeX line 12). Add the later history: scan 018 takes up closed sub-tronçons and relative frontier, while scan 025 returns to the terminology and cancels a boundary-definition block; the instruction is acted on, but the initial marginal sentence is not completed in place.

#### C01-N01 — KEEP

C source: `C01 line 12`. Original item: No other explicit verification request is listed for 002,005,007,009; “Axiome” on 005 is a label.

Keep this negative statement in its narrow local sense. `Je voudrais définir une autre axiomatique` (scan 002, TeX line 18) is a programmatic opening, and `\uline{Axiome}` (scan 005, TeX line 43) labels an assumption; neither is an unfulfilled proof-check instruction. The editorial `\unsure` marks on these pages must not be counted as questions written by the author.

#### C02-U01 — KEEP

C source: `C02 line 5`. Original item: Scan 017, circled2, asks for explicit axioms on the ternary relation and the decomposition data.

`\textcircled{2} Il faudrait expliciter` (scan 017, TeX line 27) remains live. The number of “quelle(s) condition(s)” and the biordonné/biordonnien ending remain explicitly uncertain in the frozen TeX, so C’s linguistic caution should be retained; scans 018–025 do not supply the requested complete intrinsic axiom list.

#### C02-U02 — KEEP

C source: `C02 line 6`. Original item: The order-reconstruction question on 013 leads to a lemma and a proof on 014; the older remaining-to-prove sentence is struck.

`quand a-t-on` (scan 013, TeX line 24) leads to the displayed inequality, and `Donc il faut simplement vérifier le` (scan 014, TeX line 3) introduces the lemma. The proof ends with `$x\leq u\leq v$\quad OK` (scan 014, TeX line 26), while `\deleted{il reste à prouver $u\leq v$}` (scan 014, TeX line 26) is canceled. Keep it under “verification undertaken and authorially completed,” not as a still-live “il reste à prouver” obligation.

#### C03-U01 — KEEP

C source: `C03 line 7`. Original item: Scan 023 leaves the T₀ question for an arbitrary tronçon open.

`je ne sais si c'est` (scan 023, TeX line 2) is completed by `le cas pour tout tronçon` (scan 023, TeX line 3). The preceding positive assertion continues the ficelle-lieux case from scan 022; it must not be promoted to a theorem for every tronçon. No answer to the general question is recorded by scan 025.

#### C03-U02 — CORRECT

C source: `C03 line 8`. Original item: Scan 023 also asks about sobriety and the generic-point condition, with an A voir note.

Keep the mathematical question, but update the literal quotation to the frozen form: `\margin{\unsure{A|À} voir,}` (scan 023, TeX line 5). The live question is `ni si un tronçon, avec sa top. canonique, est sobre` (scan 023, TeX line 3), followed by `tte partie fermée \uline{irréductible} aurait un pt générique \dots` (scan 023, TeX line 3). The accent and punctuation of the short marginal tag should not silently be normalized to C’s unqualified sentence form.

#### C03-U03 — KEEP

C source: `C03 line 9`. Original item: Scan 023 asks for the converse of the closed-point conclusion in the totally ordered case.

`les pts sont fermés (réciproque ?)` (scan 023, TeX line 7) is an explicit live question. Its immediate attachment is to closed points; C does not justify transferring the question mark to the following separatedness assertion, and these 24 pages give no explicit answer to that converse.

#### C03-U04 — KEEP

C source: `C03 line 10`. Original item: Scan 024 asks the interval-closure equality after a canceled first wording.

`Aura-t-on` (scan 024, TeX line 15) introduces `\overline{]a,b[}&=[a,b]\quad ?` (scan 024, TeX line 18). Preserve the distinction between the canceled first wording and this live question; its setting is the topology proposed immediately above as the upper bound of two topologies. Link it to the failed argument lower on 024 and the return to the first topology on 025, rather than listing it as an untouched open assertion in the final chosen topology.

#### C03-U05 — KEEP

C source: `C03 line 11`. Original item: Scan 024 asks the lower-ray closure equality with a lower-endpoint qualification.

`\overline{\mathcal L_{<a}}&=\mathcal L_{\leq a}\quad ?` (scan 024, TeX line 19) is retained, as is the insertion `\inserted{(a\ne\unsure{o|0}_{L})}` (scan 024, TeX line 19). C correctly preserves the o/0 uncertainty; the equality is asked, not proved, and belongs to the same subsequently abandoned topology experiment as the neighboring questions.

#### C03-U06 — KEEP

C source: `C03 line 12`. Original item: Scan 024 asks the upper-ray closure equality and questions its upper-endpoint qualification.

`\overline{\mathcal L_{>a}}&=\mathcal L_{\geq a}\quad ?` (scan 024, TeX line 20) and `si $a$ n'est pas plus grand élément ?` (scan 024, TeX line 20) both retain their question marks. No separate resolution of this equality is written before the change of course on 025.

#### C03-U07 — KEEP

C source: `C03 line 13`. Original item: Scan 024 attempts an endpoint-neighborhood argument, then declares the proposed step false and supplies a sketch.

`à prouver (p. ex.)` (scan 024, TeX line 25) introduces the attempted endpoint claim, but the author then writes `Mais c'est faux déjà pour un ens. de lieux associé à une ficelle topologique` (scan 024, TeX line 25). The margin specifies `Il faut avoir que $a\in\complement[x,y]$ mais $]a,b[\,\subset [x,y]$` (scan 024, TeX line 28). Record a failed/withdrawn route in the same text; neither C’s summary nor this audit is an independent verification of the sketch.

#### C03-N01 — CORRECT

C source: `C03 line 15`. Original item: C says018–022 and 025 carry no further explicit question or reservation and treats the other marginal notes as qualifications.

Retain the narrower finding that these pages add no further explicit interrogative of the same kind, but qualify the carryover: scan 021 replaces the canceled ordinary-difference formulation by a moderated-complement formulation, and 025 both changes course and cancels the proposed boundary-definition/examples block. In particular, `Finalement, on travaillera avec la top. définie d'abord` (scan 025, TeX line 2) and `néanmoins par abus de langage` (scan 025, TeX line 2) are substantive scope decisions, not an absence of revision. Scan 020’s double-recurrence annotation is a stated proof method, not a request to verify the argument.

### 2. Every original title/date/numbering row

This table also supplies the consolidated register of headings and manuscript numbers. An internal heading is not a separate title sheet.

| C item and original line | Scan / manuscript number | Decision | Frozen evidence and qualification |
|---|---|---|---|
| C01-T01 / C note line 18 | 002 / 1 | CORRECT | `\uline{Réseaux}\ldots\ via découpages.` (scan 002, TeX line 5) The same sheet carries (8 Juin 86) and GF with underlined III; replace C’s unresolved abbreviation description by the frozen GF reading. Manuscript-number marker: `\mspage{1}` (scan 002, TeX line 3) |
| C01-T02 / C note line 19 | 003 / 2 | KEEP | Continuation; no date or separate title. Manuscript-number marker: `\mspage{2}` (scan 003, TeX line 2) |
| C01-T03 / C note line 20 | 004 / 3 | KEEP | `\uline{Axiomes provisoires :}` (scan 004, TeX line 32) Internal heading; no date. Manuscript-number marker: `\mspage{3}` (scan 004, TeX line 2) |
| C01-T04 / C note line 21 | 005 / 4 | KEEP | `\inserted{Ex 1}` (scan 005, TeX line 22) The same sheet also has the live Axiome label and the discrete-network structure heading; no date. Manuscript-number marker: `\mspage{4}` (scan 005, TeX line 2) |
| C01-T05 / C note line 22 | 006 / 5 | KEEP | `\margin{Finitude}` (scan 006, TeX line 9) Dec₁ and Dec₂ are live labels; the earlier Partie modérée fermée definition heading is canceled. No date. Manuscript-number marker: `\mspage{5}` (scan 006, TeX line 2) |
| C01-T06 / C note line 23 | 007 / 6 | CORRECT | `\uline{Ex \deleted{\unsure{1}}2}` (scan 007, TeX line 4) The live example number is2; the uncertain1 belongs to deleted ink. Drop C’s alternative of a live1. Manuscript-number marker: `\mspage{6}` (scan 007, TeX line 2) |
| C01-T07 / C note line 24 | 008 / 7 | KEEP | `\uline{Partie} \uline{modérée}` (scan 008, TeX line 32) The earlier Tronçons/Tronçon word remains uncertain. These are internal labels, not a title sheet. Manuscript-number marker: `\mspage{7}` (scan 008, TeX line 2) |
| C01-T08 / C note line 25 | 009 / 8 | KEEP | `\uline{Définition}\quad Un ens. ordonné` (scan 009, TeX line 10) The prior Proposition and Définition/Segment formulations are canceled. No date. Manuscript-number marker: `\mspage{8}` (scan 009, TeX line 2) |
| C02-T01 / C note line 20 | 010 / 9 | KEEP | Number9; no title sheet, date or page-total statement. Manuscript-number marker: `\mspage{9}` (scan 010, TeX line 1) |
| C02-T02 / C note line 21 | 011 / 10 | KEEP | Number10; no title sheet, date or page-total statement. Manuscript-number marker: `\mspage{10}` (scan 011, TeX line 1) |
| C02-T03 / C note line 22 | 012 / 11 | KEEP | Number11; no title sheet, date or page-total statement. Manuscript-number marker: `\mspage{11}` (scan 012, TeX line 1) |
| C02-T04 / C note line 23 | 013 / 12 | KEEP | Number12 retains an uncertainty between one and two following points; the numeral itself is12. Manuscript-number marker: `\mspage{12\unsure{..\|.}}` (scan 013, TeX line 1) |
| C02-T05 / C note line 24 | 014 / 13 | KEEP | Number13; no title sheet, date or page-total statement. Manuscript-number marker: `\mspage{13}` (scan 014, TeX line 1) |
| C02-T06 / C note line 25 | 015 / 14 | KEEP | Number14; no title sheet, date or page-total statement. Manuscript-number marker: `\mspage{14}` (scan 015, TeX line 1) |
| C02-T07 / C note line 26 | 016 / 15 | KEEP | Number15; no title sheet, date or page-total statement. Manuscript-number marker: `\mspage{15}` (scan 016, TeX line 1) |
| C02-T08 / C note line 27 | 017 / 16 | KEEP | Number16; no title sheet, date or page-total statement. Manuscript-number marker: `\mspage{16}` (scan 017, TeX line 1) |
| C03-T01 / C note line 21 | 018 / 17 | KEEP | `\uline{Partie fermée} \uline{modérée} de $I$` (scan 018, TeX line 14) The opening Sous tronçon has fermé I inserted. Preserve the written I in this heading. Manuscript-number marker: `\mspage{17}` (scan 018, TeX line 1) |
| C03-T02 / C note line 22 | 019 / 18 | KEEP | `\uline{Th}` (scan 019, TeX line 2) Th, Def and marginal Ex are present; no date. Manuscript-number marker: `\mspage{18}` (scan 019, TeX line 1) |
| C03-T03 / C note line 23 | 020 / 19 | KEEP | `\uline{Cor}` (scan 020, TeX line 19) Prop, Cor, Ex and marginal Dém, Rem, Attention are present; no date. Manuscript-number marker: `\mspage{19}` (scan 020, TeX line 1) |
| C03-T04 / C note line 24 | 021 / 20 | KEEP | `Partie loc. fermée modérée` (scan 021, TeX line 8) The Th label follows; no date. Manuscript-number marker: `\mspage{20}` (scan 021, TeX line 1) |
| C03-T05 / C note line 25 | 022 / 21 | KEEP | `(9 juin)` (scan 022, TeX line 9) The date follows the wavy division and is followed by the circled1 topology entry. No year is written in this date. Manuscript-number marker: `\mspage{21}` (scan 022, TeX line 1) |
| C03-T06 / C note line 26 | 023 / 22 | KEEP | No new date, title or section heading; the A/À voir note is a verification tag. Manuscript-number marker: `\mspage{22}` (scan 023, TeX line 1) |
| C03-T07 / C note line 27 | 024 / 23 | KEEP | No new date, title or section heading; Aura-t-on is a question introduction. Manuscript-number marker: `\mspage{23}` (scan 024, TeX line 1) |
| C03-T08 / C note line 28 | 025 / 24 | KEEP | `\uline{sous-tronçon \inserted{fermé} large}` (scan 025, TeX line 7) The earlier sous-tronçons word is also underlined. The canceled lower boundary block must not be treated as a live definition. Manuscript-number marker: `\mspage{24}` (scan 025, TeX line 1) |

### 3. Every original global metadata assertion

#### C01-G01 — KEEP

C source: `C01 line 27`. Original item: No separate title sheet in002–009.

Keep:002 begins the chapter and immediately continues into mathematical text on the same sheet. The individual-number and heading evidence is registered in section2.

#### C01-G02 — KEEP

C source: `C01 line 27`. Original item: No explicit total page count in002–009.

Keep: the manuscript numerals1–8 are individual page numbers, not an authored total-count statement. The individual-number and heading evidence is registered in section2.

#### C01-G03 — KEEP

C source: `C01 line 27`. Original item: Eight numbered manuscript pages are visible in the batch.

Keep: scans 002–009 carry manuscript numbers 1–8 consecutively. The individual-number and heading evidence is registered in section2.

#### C01-G04 — KEEP

C source: `C01 line 27`. Original item: No second date occurs in that batch.

Keep with its batch scope: the later (9 juin) on 022 means this cannot become a global claim that the consolidated packet has only one written date. The individual-number and heading evidence is registered in section2.

#### C02-G01 — KEEP

C source: `C02 line 12`. Original item: No title sheet in010–017.

Keep: all eight are continuation sheets of mathematical notes. The individual-number and heading evidence is registered in section2.

#### C02-G02 — KEEP

C source: `C02 line 13`. Original item: No written date in010–017.

Keep with its batch scope; the dates on 002 and 022 lie outside this C batch. The individual-number and heading evidence is registered in section2.

#### C02-G03 — KEEP

C source: `C02 line 14`. Original item: No statement of a total page count in010–017.

Keep:9–16 are page numerals, not a total count. The individual-number and heading evidence is registered in section2.

#### C02-G04 — KEEP

C source: `C02 line 16`. Original item: The author’s numbering is consecutive.

Keep: the displayed manuscript numbers are9–16 in archive-scan order, with the trailing punctuation doubt on 12 retained. The individual-number and heading evidence is registered in section2.

#### C03-G01 — KEEP

C source: `C03 line 30`. Original item: No title sheet in018–025.

Keep with the supplied-page scope; the new dated topology discussion starts within022. The individual-number and heading evidence is registered in section2.

#### C03-G02 — KEEP

C source: `C03 line 30`. Original item: No authored total page count in018–025.

Keep: no 8 pages or24 pages statement is carried by these sheets. The individual-number and heading evidence is registered in section2.

#### C03-G03 — KEEP

C source: `C03 line 30`. Original item: The eight sheets are numbered17 through 24.

Keep: these are consecutive manuscript numbers on scans 018–025. The individual-number and heading evidence is registered in section2.

### 4. Standing section: author-marked uncertainty and its subsequent status

#### Still-live questions or provisional reservations in this packet

- **Scan 004 — anticipated reconstruction and provisional axioms.** Keep the two expectations concerning c from b and b from the two-point data, while distinguishing the later tronçon reconstruction from a completed general axiom system (C01-U02).
- **Scan 006 — provisional finiteness.** The reservation concerns the imposed finiteness hypotheses; no explicit withdrawal of that reservation follows (C01-U03).
- **Scan 017 — intrinsic axioms still to be written.** The ternary relation and two-point decomposition presentations require explicit conditions (C02-U01).
- **Scan 023 — arbitrary-tronçon T₀ and sobriety questions.** Keep the two separate questions and the generic-point parenthesis, with the A/À voir reading left marked (C03-U01 and U02).
- **Scan 023 — converse concerning closed points.** Keep the parenthetical question separately from the following separatedness assertion (C03-U03).

#### Self-answered, addressed later, or withdrawn within the text

- **Scan 003 — self-answered on the same sheet.** The complement-recovery question receives the author’s affirmative answer and a reiterating NB. Its mathematical validity is not certified by that documentary status (C01-U01).
- **Scan 008 →018 and 025 — reworking taken up, with further revision.** The instruction to leave the line-only case is followed by the closed-sub-tronçon discussion; the boundary formulation remains a site of revision (C01-U04).
- **Scans 013–014 — verification followed by an author proof.** Preserve the live question and lemma request, but do not revive the canceled remaining-to-prove sentence after the proof’s OK (C02-U02).
- **Scans 024–025 — a proposed topology and a failed closure route.** Keep all three closure questions as questions asked in that experiment; record the author’s failure diagnosis and the ensuing return to the first topology. Do not silently transfer the three questions to the final chosen topology (C03-U04 through U07).


#### Additional status items needed beyond C’s summaries

##### A01 — Scan 011 →016: the anticipated recovery is pursued in a special setting.

`Je dis que l'on récupère la structure dé` (scan 011, TeX line 36) introduces the biorder-recovery claim, and scan 016 concludes `On gagne !` (scan 016, TeX line 28). This is the manuscript’s claimed success for the reconstruction developed there; the intrinsic-axiom request on 017 remains separate.

##### A02 — Scan 015 →016: an announced demonstration is subsequently carried out.

`On va voir maintenant comment la connaissance` (scan 015, TeX line 13) leads into the three-component comparison and `On gagne !` (scan 016, TeX line 28). Add this to the record of announced-and-addressed steps, not to the list of still-open tasks.

##### A03 — Scan 015: a colon/question-mark reading must not become a certain author question.

`R(a,b,c)\unsure{\mathord{:}|\mathord{?}}` (scan 015, TeX line 21) carries an editorial alternative in the frozen transcription. It is a reading question, not documentary evidence of a definite extra self-flagged question mark.

##### A04 — Scan 021: ordinary difference is replaced by moderated complement.

`\deleted{Alors $\exists$ une plus petite partie fermée modérée \inserted{$Z$} contenant $X\setminus Y$.}` (scan 021, TeX line 11) is canceled. The live formulation introduces C_mod(Y,X) and a least closed moderate set containing that set; record a changed formulation without asserting that this documentary change by itself proves the earlier assertion false.

##### A05 — Scan 022: the singleton-closed discussion is revised into a warning.

`\uline{n'est pas} \inserted{\uline{néc$^{\mathrm t}$}} \uline{fermé}` (scan 022, TeX line 15) is the live conclusion after canceled trial wording. This is a substantive qualification, not an additional unresolved interrogative.

##### A06 — Scan 025: the topology experiment is set aside and closed terminology is qualified.

`Finalement, on travaillera avec la top. définie d'abord` (scan 025, TeX line 2) and `néanmoins par abus de langage` (scan 025, TeX line 2) should accompany the scan 024 failure in the standing account. The terminology remains live even though topological closedness is not being asserted for every named sub-tronçon.

##### A07 — Scan 025: the boundary definition and its examples are canceled.

`\deleted{\partial T=}` (scan 025, TeX line 15) begins the canceled lower display, and the later `\deleted{\partial[a,b]=\{a,b\}}` (scan 025, TeX line 28) belongs to the canceled example block. Report this as withdrawn draft material; neither the proposed definition nor its four examples should be quoted as a live conclusion on 025.

##### A08 — Scan 020: a proof-method note and a negative warning are not open verification requests.

`double récurrence sur nb de comp. conn. de $X$ et de $Y$` (scan 020, TeX line 10) records a proposed proof method, while `C'est déjà faux ds le cas standart $L=[0,1]$ !` (scan 020, TeX line 21) records the author’s rejection of a general closure extension. These deserve the main research notes’ unproved-claim/example treatment, but should not be mislabeled as author requests to check a step.

### 5. Standing section: titles, dates and counts

The chapter-opening sheet is scan 002, manuscript page 1. Its title is `\uline{Réseaux}\ldots\ via découpages.` (scan 002, TeX line 5), its date is `(8 Juin 86)` (scan 002, TeX line 7), and its corner inscription includes `GF\,\uline{III}` (scan 002, TeX line 12). It is not a separate blank title sheet: the axiomatic discussion begins below it.

The second written date is `(9 juin)` (scan 022, TeX line 9) on scan 022, manuscript page 21, after the dividing stroke and before the topology discussion. That entry carries no year; the earlier86 should not be silently inserted into its quotation.

The24 supplied scans 002–025 bear consecutive manuscript numbers 1–24; scan 013 retains uncertainty about the point(s) after12. There is **no authored statement of a total page count** and no separate title sheet in the supplied packet. The internal headings are registered in section2.

### 6. Check-event scope and quotation verification

Every quoted fragment was checked as an exact substring of the frozen page TeX before this file was written. The companion `research/C_notes_CHECK_EVENTS.tsv` records documentary checks of the 50 original items and 8 additions; it does not claim image checking, proof checking, or independent mathematical verification. The standing sections reuse those same checked items.


## Check-event and proof-documentation index

`CHECK_EVENTS.tsv` contains a row for every principal note, every relevant RS ID used here, the manuscript loci explicitly checked, source refutations with a named refinement, and the documentary audit of all 50 original C-note items plus eight additions. The source workers’ event records are included with their actual authors and event types; the root’s per-note and cross-reference events are separately identified. Reading while transcribing was not counted as proof checking, and no formal certificate or TeX compilation is claimed.

Detailed proofs and limits are in `research/math_checks.md` and `research/join_check.md`. Exact context anchors and their status limits are in `research/context_links.md`; the 86 checked C-audit quotations are documented in `research/C_notes_quote_checks.json`. The root read and assessed those textual reports before integrating them here; no supporting worker viewed the current manuscript images.
