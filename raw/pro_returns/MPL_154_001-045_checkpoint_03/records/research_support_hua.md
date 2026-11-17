# Research support: Michel Hua’s modernized reading of cote 154

## Scope, provenance, and evidence boundary

This is a **post-freeze research comparison**, prepared after the transcription freeze at **2026-11-17 15:15:39 UTC** and context opening at **15:15:45 UTC**. It does not change, correct, or certify the frozen transcription. No scan image was viewed for this comparison. No transcription, page, doubts, inventory, or hash file was modified.

Read before the comparison: all of `context/notes/RESULTS_STATE.md` and `context/hua_project/README.md`. Read subsequently: **all 2,555 lines / 24,388 words of `context/hua_project/154.modern.tex`**, in numbered chunks, and the frozen page `.tex` files for scans 001–045, excluding the absent/omitted separator scan 011. Truncated tool outputs were reread in smaller chunks. The later portions of Hua’s file are context leads only; they were not substituted for the current frozen pages.

Attribution throughout: **“Hua, modernised reading of cote 154” means Michel Hua’s project’s AI-produced modernized interpretation**, not a verified transcription, an independently established theorem, or a result of our project. The supplied README attributes it to `https://github.com/Commutator-IO/grothendieck-project`. No external literature or Lean code was opened or verified in this support task. Mathematical comments explicitly identified as comparisons or tests below are our analysis, not discoveries attributed to the manuscript.

Locator conventions:

- `Hua:730–747` means lines of `context/hua_project/154.modern.tex`.
- `019:43–49` means lines of frozen `MPL_154_001-045/pages/MPL_154_001-045_154_scan019.tex`; analogous abbreviations are used for the other scans.
- **Hua page p = our scan p+1.** His page 18 is our scan 019, his page 31 is our scan 032, and his page 44 is our scan 045. The cover is our scan 001.
- The current package’s direct overlap with the modernized mathematical discussion ends in Hua’s subsection **“L’indexation”**, lines 1209–1236. **“L’application structurale”**, beginning at line 1238, starts with his page 45 / our scan 046 and is later context.

The modernization itself declares that it supplies implicit hypotheses, corrects mathematical statements, unifies notation, and relegates or removes critical apparatus (Hua:1–28). It also says its literature citations were supplied from memory without checking. Consequently even a beautifully coherent sentence there cannot settle a difficult reading in the frozen text. Several supposed source errors corrected by Hua are **absent from our frozen text**.

## Principal findings for integration

1. **The registered item `154-cyclic-order-determines-position` is supported as an expectation of injectivity, not as a proved theorem or a bijection.** Frozen 019:43–47 gives a canonical map from all non-supercritical relative positions to antipody-compatible polygonal structures on the oriented label set and says it should not be difficult to prove injectivity. The source does not give that proof there. Hua’s detailed treatment agrees about the lack of a manuscript proof but adds a Lean-related statement about full rank-three chirotope contraction data whose translation to the page’s polygon datum is explicitly unformalized.
2. **Nonstable positions are part of the written domain.** The statement is not restricted to stable added pseudolines. Coincidences at arrangement vertices therefore need to be represented in any oriented-matroid comparison. The distinction between a strict cyclic order and a cyclic record with coincident/parallel classes is a real hypothesis issue, not a typographical detail.
3. **Three advertised corrections should not be imported into our transcription or into an account of its defects:** the missing tilde on the supercritical label set; the allegedly incorrect formula for face rotation; and the allegedly incorrect boundary-intersection definition of parallel chords. Frozen 019:7, 032:62, and 035:34 already read differently from the defective versions reported by Hua.
4. **Hua’s treatment of the weighted-polygon transport is stronger than the frozen source warrants without further conditions.** “Un principe général” drops the source’s degree-two condition, and its preceding weight equation reverses the frozen source’s D/D′ labels. Neither its generalized local-system assertion nor the global identification of a relative-position surface should be promoted to a verified theorem.
5. **The package’s primary subject is concrete combinatorial geometry/topology of pseudoline relative positions and their deployment surfaces.** The parent’s independently checked Esquisse §8 comparison is more precise than assigning these pages wholesale to tame topology or to the 1986 forms project. Hua’s explicit Esquisse/cartographic analogy supports broad adjacency but supplies no moderate-category axioms and no 1986 forms identification.

## 1. The registered cyclic-order claim, precisely

### 1.1 What the frozen pages actually say

The setting is a fixed system `Σ=(X,Σ)` of projective pseudolines and its relative positions `P=PR(Σ)` (012:5). The construction excludes the trivial arrangement case (012:25); it distinguishes stable positions (`S∩D` empty), sous-stable positions (`|S∩D|=1`), further critical positions, and the supercritical positions given by the members of Σ itself (013:16; 014:33; 016:14; 017:8–28).

The local transition polygon is formed from specializations and generizations. Its edge and corner weights encode a polygon of total size `2n` (017:33–47). Frozen 018:5–9 constructs the expanded polygon `P̂(D)` and states a **canonical bijection between the oriented pseudoline labels Ĩ and its edges**, compatible with antipodies. This is a local label-to-edge bijection, not the later assertion about injectivity of the set of positions.

For the supercritical case `D=Δ_{i0}`, a separately weighted polygon has order `2(n−1)` (018:13–37; 019:5). Frozen 019:7–11 gives a bijection from **Ĩ with the i0 pair removed** to the **vertices** of this polygon, dependent on an orientation of Δ; reversing that orientation composes the bijection with antipodism. The edge/vertex distinction and this orientation dependence should both remain visible.

Frozen 019:43–47 then states the map

\[
\operatorname{PR}(\Sigma)\setminus\Sigma
\longrightarrow
\{\text{polygonal structures on }\widetilde I
\text{ compatible with antipodism}\}.
\]

Its exact proof-status wording is: **“il ne devrait pas être difficile de montrer que cette application est injective.”** The page next asks how the polygons vary along specialization arrows (019:49) and how to recover the entire embedded, weighted, directed graph from the polygonal structures (020:7). Those are additional tasks, not consequences already proved by the sentence.

| Feature | What can be attributed to the frozen source |
|---|---|
| Arrangement | A fixed labeled system Σ; the initial nontriviality exclusion remains relevant. No general-position or simple-arrangement hypothesis is inserted at 019. |
| Domain | `PR(Σ)\Σ`: every non-supercritical position, including nonstable positions. |
| Labels | `Ĩ`, the set of **oriented** fixed pseudolines, with involution reversing their orientations (018:5–9). |
| Target | Polygonal structures compatible with this involution. “Cyclic order” is a modernization; a polygonal structure is naturally read without a chosen direction unless an orientation is separately chosen. |
| Conclusion | Expected **injectivity**. No surjectivity, no characterization of realizable orders, and no bijection between all orders and positions is stated. |
| Proof | Not supplied at 019. The package develops transport constructions afterward, but does not exhibit a completed proof of this injectivity claim. |
| Important distinction | The source-target injectivity `P̃→P×P` at 012:25–29 has an explicit argument about recovering a specialization triangle. It is a different map and is not a proof of 019’s assertion. |

The register entry is `Hua, findings register, 154-cyclic-order-determines-position`, `RESULTS_STATE.md:471`: **conjecture/candidate; their search found no reference; intake “new to us.”** The comparison supports the statement-level intake while narrowing its wording to the precise map and keeping its status unchanged.

### 1.2 What Hua adds

Relevant subsection: **“Le polygone déployé, et l’ensemble Ĩ”**, Hua:691–762, especially 730–747. Hua calls the map canonical, reproduces the expectation of injectivity, and says the dossier does not prove it (730–739).

A newer footnote (740–747) reports a partial Lean verification in `lean/Grothendieck/Folder154.lean`, theorem `problem17_holds`: two one-element extensions of the same rank-three chirotope with the same contraction at the new element, up to sign, agree up to reorientation of that element. **Hua expressly says the translation from the page is not formalized** and names the pseudoline/chirotope correspondence and cyclic-order/contraction correspondence as missing. No Lean file was supplied in the approved context or inspected here; this remains a report by Hua’s project about its formalization.

The elementary algebraic reason the chirotope statement is plausible should not be confused with the translation problem. Fix representatives of rank-three chirotopes on `E∪{e}` with the same nonzero deletion on `E`. Values on triples entirely in E are fixed by that deletion. Every remaining value, up to alternation, is `χ(i,j,e)`, which is exactly the value of the rank-two contraction by e. Thus **full signed contraction data**, including zeros, determines all new triple values. This is a comparison of data, not a proof that the manuscript’s polygon records precisely those data or that equality of such data is the manuscript’s intended relative-position equivalence.

There are at least four translation obligations:

1. Specify the equivalence relation on added pseudolines: labeled combinatorial equivalence, isotopy relative to the arrangement, or a stronger fixed-realization condition. The systematic isotopy definition in Hua:1989–2001 comes from his page 87 / our scan 088, outside this frozen package.
2. Relate orientation of the fixed pseudolines, coorientation in a spherical lift, orientation of the added line, and the global sign of a contraction without silently identifying these choices.
3. Show exactly how `P̂(D)` and its marking recover `χ(i,j,e)`, including the value zero when D contains the intersection of `D_i,D_j`.
4. Distinguish a labeled polygon up to dihedral symmetry from a directed cyclic order. Reorientation of the added element and reversing the polygon’s orientation must be matched to the stated quotient.

### 1.3 A finite test worth performing, not a claimed counterexample

**Own research question; confidence high that it tests the missing hypothesis, no verdict on injectivity.** Take three fixed straight projective lines in general position. Compare an added line through exactly one of their three vertices with its two small perturbations off that vertex. In the contraction description the first has a zero pair-value and the two perturbations have opposite nonzero values. Determine precisely what the manuscript’s expanded polygon and its label involution assign to all three cases. Check whether zero/parallel-class information survives, and whether the intended “antipodism” is the ordinary half-turn of a strict polygon or a more decorated operation.

This test is suggested by the written domain, not by an established contradiction. A mere cardinality comparison of strict orders with positions would be premature until the intended polygon datum and the exact `PR` equivalence are fixed. It should be recorded as a test for the registered candidate, not as a refutation or a novelty claim. Later Hua:2391–2418 discusses a cube of independent generizations and explicitly leaves its compatibility with a two-dimensional surface unresolved; that reinforces the need to identify the model before transporting theorems between descriptions.

## 2. Detailed comparison in the current scan range

The following entries use “supports” for agreement at the level of the **frozen first-pass text**, not independent facsimile verification.

### H01. Five variants and the cost of admitting exceptional positions

**Hua subsections:** “X₀ : les positions supercritiques exclues” (409–418), “X₁ : une face par position supercritique” (420–443), “X′₁ : un petit disque à la place du sommet” (445–460). **Frozen anchors:** 002:8–23; 003:3–27; 004:3.

The frozen text supports the five-variant inventory, the `4n` exceptional-valence statement, the parity counts `6(n−1)` and `2(n−1)`, the `2n_i` qualification outside the simple/stable case, and valence three on the exceptional faces of X′₁. Hua usefully distinguishes these variants but does not prove they realize one common parameter-space topology. His footnote comparing `4n` with a later straight-line dual count `2(n−1)` is an unresolved comparison between constructions, not a correction of 002:9.

**Direct difference:** Hua:453–455 says specialization arcs have arbitrary combinatorial length. Frozen 004:3 explicitly gives length **1/2**, with a possibly iterated subdivision. Preserve the half-length and the uncertainty about subdivision; do not replace either by “arbitrary.” Frozen 003:13 also records a change from the orientation cover to the cover of rives, which is useful evidence that the two covers are not being identified without choices.

### H02. Local-system obstruction and ultimate covers

**Hua subsections:** “Le défaut commun” (462–470), “X₂ : éclater le sommet” (472–504), “X₃ : une bande de Möbius à la place de D_i” (506–520), “Les déploiements ultimes” (522–536). **Frozen anchors:** 004:21–22; 005:5–13; 007:3–7; 009:4–10; 010:4–6.

The basic distinction between local transport away from supercritical loci, ramification, new weight-two transitions, the Möbius-band modification, and the structural-map problem is supported. Frozen 009:4 also asserts the two families of homeomorphic underlying surfaces, a point the modernization does not emphasize. Frozen 007:3 gives the explicit proposed **ramification index n**, which should be retained as a manuscript claim.

Hua:492–504 adds its own monodromy explanation: if a puncture loop equals the later full turn, its action is `t↦t−2(n−1)` on `Z/2n`, of order n. This arithmetic is consistent with the source’s index, but identification of that particular loop with the later loop is an **extra assumption expressly acknowledged by Hua**. It does not resolve the source’s admitted uncertainty at 007:7. Hua also says X₂ is obtained from **X′₁** by cutting faces (476–478), whereas frozen 007:3 reads **X₁**. Treat that as a comparison question.

### H03. Specialization triangles and the first injectivity argument

**Hua subsection:** “Les flèches de spécialisation” (547–587). **Frozen anchors:** 012:7–31; 013:16.

The source supports a specialization graph, the map `(D,T)↦(D,D′)`, the change `D′∩S=(D∩S)∪{s}`, and an argument that the triangle is recovered from its source and target. Hua smooths a crossed-out definition and difficult connective prose into a clean definition and proof. This is a legitimate interpretive reconstruction but not a license to remove the deletions and doubtful text from an edition. The initial nontriviality restriction matters. The resulting injectivity concerns **an arrow’s uniqueness between specified endpoints**, distinct from §1/scan019’s encoding of positions by polygon structures.

### H04. Failed lower bound, corridors, and immediate generizations

**Hua subsection:** “Au moins trois transitions” (589–637). **Frozen anchors:** 013:16–29; 014:12–33,48; 015:4,23–29; 016:12–16.

The frozen text supports the stable-case triangle argument, the failure of the first sous-stable argument, and the repair by including supercritical positions and corridor specializations. However Hua:598–602 describes the counterexample as avoiding two **quadrilaterals**; frozen 014:31 says two **couloirs**, then adds that D cuts a third longitudinally. That is a substantive reading difference, not an agreed description of the figure.

Hua:624–631 initially calls both stable and sous-stable positions “immediate” generizations, then limits the count to `2ν` for immediate ones. Frozen 015:25 explicitly says the stable ones **are not immediate**, since they factor through sous-stable ones; 015:27–29 preserves the adjustment `4ν→2ν`. An account should retain this correction rather than state both types are immediate. Hua:620–622 calls the repaired lower bound asserted without another proof; frozen 016:12 does supply an informal component-by-component reason. Its adequacy still needs checking, but “no argument at all” would overstate the absence.

### H05. Structural surface, weights, and terminology

**Hua subsection:** “Orientations, plongement cellulaire, poids” (639–689). **Frozen anchors:** 016:14–16; 017:4–47; 018:5–9.

The source supports local polygonal orders, orientation transport, the intended cellular embedding of Γ in `Str(Σ)`, and edge/corner weights totaling `2n` at ordinary positions. Hua’s general map construction later explains how such graph data produce a combinatorial surface. This does not by itself identify that surface with every later space called `Rel(Σ)`.

**Reading difference:** Hua:658–661 reads **“critiques extérieurs”** and proposes supercritical positions as the referent. Frozen 017:28 reads **“critiques extrémaux.”** The natural extremality interpretation is compatible with all arrows arriving, but no change or resolution of this word is made here. Hua’s `Tr(D)` is its own notation, while the source uses `Pol(D)` for the transition polygon; its replacement should always be signaled when explaining the comparison (Hua:52–61,267–275,584–587).

### H06. Expanded polygon and its labels

**Hua subsection:** “Le polygone déployé, et l’ensemble Ĩ” (691–762). **Frozen anchors:** 018:5–17,29–37; 019:5–11,30–49; 020:7,21,53–57.

The `2n`/`2(n−1)` counts, label bijections, antipody statements, and identity `ν+ν₀=n` are supported. **Hua’s correction of a missing tilde (720–723) does not apply to the frozen reading**, which already has it at 019:7. The injectivity issue is analyzed separately above.

For transport, Hua:753–762 gives a streamlined canonical isomorphism compatible with weights. Frozen 020:53–57 places part of this discussion beside **“annulé; cf plus bas!”**. Later augmented polygons are introduced because naïve transition-polygon comparison is inadequate. A clean summary should not make the early transport paragraph look like an unchanged final construction.

### H07. Enlarged polygons, new vertices, and a reversed equation

**Hua subsection:** “Le polygone Tr*(D)” (767–803). **Frozen anchors:** 022:5–17,32–47; 023:14,33–37; 024:11–31; 025:5–21.

The source supports adding antipodal/free transitions, enlarging the polygon again, the possible failure of surjectivity of `Pol*(D)→Pol*(D′)`, nonnegative weights including zeros, and the attempt to recover maps from orientation plus one distinguished vertex image. Frozen 025:5–7 preserves the self-correction **“mais si!”**.

There are three precise differences:

- Hua:780–781 says a new pseudo-specialization can arise when the adjoining face is a **couloir**. Frozen 023:14 says **a square**.
- Hua:776–777 says a zero-weight edge occurs between **two generizations**. Frozen 023:37 instead gives an edge from a generization to an adjacent pseudo-specialization, and another case involving an antipodal specialization and a specialization. The detailed source examples add necessary specificity.
- **Hua:782–791 reverses the frozen equation’s labels.** At 024:11, b is absent from `Pol*(D)` and present on the corresponding arc of `Pol*(D′)`. At 024:14–16, the coarse weight in D equals the three finer weights in D′. Hua prints the coarse weight in D′ and finer weights in D, then says it has corrected the source. Relative to our frozen reading, that is a contradiction, not a correction to adopt.

### H08. The general local-system principle

**Hua subsection:** “Un principe général” (805–824). **Frozen anchor:** 025:23, with 025:15–21 as its immediate setup.

Hua states a theorem-shaped principle for **any** map with nonnegative weights and constant total N at vertices. Frozen 025:23 includes an additional clause that the **true vertices are of order 2** and explicitly permits isolated ends/free edges. Hua’s own footnote quotes the clause but omits it from the displayed general formulation.

The defensible comparison is: the source asserts a local-system construction in its specified setting; Hua broadens and systematizes it. To prove the broader version one must show not only that edge transport is well defined but also that transport around each filled face is trivial. Constant polygon size alone establishes neither condition. This matters for later comparisons with coherent gluing or coefficient categories: an edgewise system on a graph is not yet descent data on the filled surface. No theorem status is assigned here.

### H09. Dual disks and exceptional transport

**Hua subsections:** “La carte duale : les disques Δ(D) (24 décembre)” (826–848), “Vers une position supercritique (25 décembre)” (850–866). **Frozen anchors:** 026:5–9; 028:4–10; 029:4–13.

The frozen text supports the change to dual disks, the unwanted artificial boundary double points after folding, a surface with boundary before filling, and holes corresponding to vertices after filling. It adds the qualification **“avec un grain de sel”** at 028:6. Hua’s more categorical exposition should retain the tentative status of this construction.

Hua says the definition of `I(D′,s)` is unreadable (861–865). Our frozen 029:10–13 reads enough to describe it as the combinatorial identification of the two antipodal arcs. This adds a source-level definition, albeit with uncertain typography for I and some uncertain connecting words. Also Hua quotes the dual map as “plus instructive”; frozen 026:9 reads **“plus intuitive”**. Neither is resolved here from context.

### H10. General maps and orientation-reversing edge gluing

**Hua subsections:** “La donnée, et la surface” (876–916), “Les repères et les trois involutions” (918–966), “La surface à bord, et le cas des pseudo-droites” (968–995). **Frozen anchors:** 031:4–16,37–41; 032:4–25,37–64; 033:4–6; 034:3–9.

This is among the strongest direct agreements: graph plus local polygonal orders plus orientation-torsor transport, low-valence caveats, dual polygonal disks, orientation-reversing boundary identification, barycentric flags, and involutions. The formulas in frozen 032:22–25 give the three involutions; 032:54–63 gives vertex/face rotations and their product. These can be discussed as explicit combinatorial machinery present in the source, with finite/local hypotheses stated when using compactness.

**Critical correction-of-a-correction:** Hua:949–956 says the source wrongly labels `σ₂σ₀` as `ρ_f` and repairs this from a later page. Frozen 032:62 instead reads

\[
\rho_{\mathrm{som}}\rho_f=\sigma_2\sigma_0=\sigma,
\]

consistent with 032:55. There is no need to repair that frozen formula. Hua’s literature labels “signed rotation system” and “cartographic group” are modern comparisons, and its historical attributions to Heffter/Edmonds/Ringel/Stahl/Tutte/Lins are unverified in this task. The Esquisse comparison is useful but should use the parent’s checked primary source, not these memory citations.

### H11. Chord axioms and sufficiency

**Hua subsection:** “Le disque Δ_L et son système de cordes” (1000–1033). **Frozen anchors:** 034:11; 035:28–41.

The source supports cutting off a Möbius neighborhood, the complementary disk, topological chords meeting at most once and crossing internally, a parallelism equivalence, paired endpoint packets, and the assertion that the necessary combinatorial conditions are sufficient. **No proof of sufficiency is supplied at 035:37.** Hua is appropriately cautious about this and proposes the missing Möbius-band gluing check (1024–1030).

However Hua’s claimed textual correction at 1015–1022 does not match the frozen reading. Frozen 035:34 has **`i=j or δ_i∩δ_j=∅`**, not the boundary-intersection expression `∂d_i∩∂d_j=∅` quoted by Hua. The frozen text also marks the bracketed endpoint statement as suppressed (035:35), with an inserted uncertain **“non-antipodiques”** inside it. Hua confidently describes antipodal endpoint blocks. That difference bears directly on the earlier polygon/antipody issue and should remain a reading question, not be decided from mathematical convenience.

### H12. Transition, inertia, and shrinking arcs

**Hua subsection:** “Les arcs de transition” (1035–1081). **Frozen anchors:** 035:39–41; 036:3–25,73; 037:3,21–37; 038:3,25–27,64.

The conditions `|σ|≥2`, consecutive boundary vertices, concurrence/exhaustion at t, avoidance of generization arcs, exceptional corridors, and alternating transition/inertia structure are supported. But the modernization changes some descriptions: Hua:1067–1069 stops shortened exceptional arcs at the **first subsequent vertices**, whereas frozen 038:3 says the **midpoints of the extreme constituent edges**. Hua:1075 says **“écarter les brins”**, while frozen 038:27 says **“croiser les brins.”** The latter is particularly relevant to what becomes a specialization after generization. Preserve the exact frozen operations and flag these differences for future image-led review.

### H13. First gluing choice, square circuits, and remaining holes

**Hua subsections:** “Le recollement, première version” (1083–1117), “Les trous, et les positions supercritiques” (1119–1153). **Frozen anchors:** 038:78; 039:3,60,135,200; 040:3–24,43; 041:3–7; 042:3–5,27–36; 043:3–5.

The source explicitly changes its mind about the “obvious” orientation transport and chooses the opposite identification; it then claims square face circuits. Frozen 040:7 initially says one mixed side, while 040:18 corrects the final count to **two**. Hua retains the final count. The source also explicitly says the construction is incomplete because supercritical disks have been omitted (040:43), recognizes overlapping exceptional generization arcs (042:36), and proposes duplicating D by its contact elements `(D,s)` (043:3).

Hua’s prose makes the compact completion read more finished than the local text’s “on peut songer”/“on a ce qu’il faut” exploratory sequence. Record it as the proposed remedy and its claimed consequence, not a final proof of the precise `Rel(Σ)` theorem. Frozen 043:3 specifies a square in the nonsimple contact case; Hua:1148–1149 says just a polygon. Hua’s quote **“ce qui est un triomphe!”** is not in our frozen text, which reads **“qu’à cela ne tienne!”**. Hua:1131–1133 also reports a duplicated σ in the graph tuple; frozen 041:3 has an uncertain origin letter `o|α` as the fourth entry, not a second σ.

### H14. Axioms and incidence geometry at the package boundary

**Hua subsections:** “Les axiomes” (1166–1207), “L’indexation” (1209–1236). **Frozen anchors:** 044:3–60,82–86; 045:3–27.

The frozen page supports compact X with K and L, quartic K vertices, even L valences, exceptional circles, a choice of marked rive, crossing conditions, multiplicities, and the total `2n` boundary formula. It also records substantial cancellations, additions, and uncertainty. Hua restores the crossed-out epsilon definition from his later page170 (1195–1197); that is a declared normalization across versions, not a reason to un-delete frozen 044:48. The date at 044:3 remains **31.11.83|31.12.83** in the frozen record, whereas Hua fixes 31 December.

Hua:1177–1179 says the “neighbors” of an exceptional edge are exceptional. Frozen 044:18 more specifically says the **opposite** edge is exceptional while an ordinary edge exists at each vertex. Do not broaden this to every incident neighbor. At 044:22 the marked-rive datum is said to follow from other data; the source asks to reconsider its placement. Hua’s cleaned axiom list conceals some of that provisional organization.

The incidence scheme at 045 indexes faces by all non-supercritical positions, ordinary edges by immediate specializations, **and exceptional edges by sweeps between positions neighboring D_i** (045:5–13). Hua:1216–1218 compresses this to immediate specialization pairs and omits the explicit alternative. Ordinary vertices involve two specialization triangles and an intervening arc (045:15–21); exceptional vertices correspond to flags `(s,a)` of Σ (045:23). The assertion that this builds the cellular incidence structure is at 045:25. The corollary identifying components of K₀ with I and with `D̃_i` begins at 045:27 but its final sentence is unfinished in this package. Hua’s orientation-dependent completed corollary (1233–1236) goes beyond the available last word; do not present the completion as fully read on 045.

## 3. Reading questions generated by the comparison

These are **future image-led questions** only. None was resolved by consulting an image or by editing the frozen text.

| Priority | Frozen anchor | Question and why it matters |
|---|---|---|
| High | 018:5–11; 019:43–47; 035:34–35 | What exactly is the antipodism of the expanded polygon at a nonstable position? How do coincident crossing groups survive? Hua’s strict cyclic-order gloss may suppress data. |
| High | 019:7 | Our frozen reading already includes the tilde. Hua’s no-tilde reading is a disagreement between readings, not evidence that our text needs correction. |
| High | 024:11–16 | Verify D versus D′ and which polygon lacks b before any later proof uses the additivity formula. The frozen equation is internally consistent; Hua reverses it. |
| High | 025:23 | The exact “2-carte” and order-two-vertices clause is crucial to the asserted local-system principle. Which face-boundary compatibility is intended? |
| High | 032:62 | Our source has the product `ρ_somρ_f`; Hua omits its first factor when diagnosing an error. Keep our reading unless the image proves otherwise. |
| High | 035:34–35 | δ versus d versus ∂d, and the deleted bracket with uncertain “non-antipodiques,” determine the chord conditions. Do not repair from plausibility. |
| Medium | 004:3; 038:3 | Half-length and midpoint conventions versus Hua’s arbitrary length/next-vertex versions affect the subdivision used in gluing. |
| Medium | 007:3 | X₁ versus X′₁ as the cut-and-identify predecessor of X₂. |
| Medium | 014:31 | Couloirs versus quadrilaterals in the counterexample; the third longitudinal crossing is present in our text. |
| Medium | 017:28 | “Extrémaux” versus Hua’s “extérieurs”; distinguish a reading question from the interpretation of terminal vertices. |
| Medium | 023:14,37 | Square versus corridor, and the exact adjacent types permitting zero weight. |
| Medium | 026:9; 029:10–13 | “Intuitive” versus “instructive”; precise I notation and whether the surviving quotient definition is readable enough. |
| Medium | 038:27 | “Croiser” versus “écarter” the strands: operation and direction of generization. |
| Medium | 041:3 | Fourth graph datum is uncertain o/α in our text; Hua removes it as a repeated σ. |
| Medium | 043:3 | “Qu’à cela ne tienne” versus Hua’s “triomphe,” and exact bigon/square assertion. |
| Medium | 044:3,18,22,48; 045:27 | Preserve uncertain date, opposite-edge condition, reorganization of marked-rive axiom, deleted epsilon, and unfinished corollary. |

Printed listings and diagram labels are also a difference in coverage, not mathematical disagreement. Hua intentionally omits computer listings and only summarizes many drawing sheets (Hua:25–28,369–377). Our frozen scans 006,008,010,021,027,030,033 retain this printed material. Their August1982 print dates must not be used as dates of Grothendieck’s mathematical writing.

## 4. Later Hua material: context leads, not current-page results

All entries in this table are credited to **Hua, modernised reading of cote 154** and remain unchecked against later scans in this support task. They record the other subjects in the full modernization, including those outside our register’s established results.

| Exact subsection / range | Subject and cautious use |
|---|---|
| “L’application structurale,” 1238–1390 (his45–46 and associated axioms) | Fold/double-fold map to X, correction `φ⁻¹(X₁)=L∪K₀`, exceptional-index discrepancy, reconstruction from numerical data, local commuting symmetries. These are later continuations of current044–045, not present completed results here. |
| “La structure de K : sommets rouges et noirs, signes,” 1393–1548 | Red/black subdivision, face-edge signs, symmetry bijections, local `(3,3),(3,4),(3,5)` patterns, sign propagation. Hua acknowledges reliance on unproved connectivity and untreated exceptional faces (1534–1547). |
| “Le transport le long d’une chaîne de faces,” 1553–1622; “Les images de π₁,” 1624–1650 | Reflection `t↦l_i−t`, alternating-sum composition, half-turn translation `t↦t−(n−1)`, parity-dependent subgroup bounds. Relevant as a conditional explanation of current007’s ramification claim. |
| “La parité des pas,” 1653–1693; “Les caractères,” 1695–1758 | Orientation and checkerboard characters, `χ*=χ_sχ_a`, `χ_X=χ*χ_c`, proposed triviality of χ_c. Hua itself records corrections and an unresolved later parity-table disagreement. |
| “Les huit façons,” 1763–1787; “Je m’étais mélangé les pinceaux deux fois,” 1789–1805; “Les quatre possibilités,” 1807–1832 | Eight arc identifications reduced to four surface constructions, natural maps versus orientation transport, and the author’s retrospective admission of gluing mistakes. Strong reason not to treat current038–043 as a final global construction. |
| “La surface des positions stables,” 1834–1884 | New stable-only graph, alternative gluing conventions, questionable n-gon quotient and branched-double-cover comparison. This is a different cell assignment from all-position faces in current045. |
| “Le cas des vraies droites,” 1886–1927 | Dual projective arrangement of joining lines of dual points, fixed-realization straight-line positions, and orientation comparisons. This models a restricted parameter problem; it must not be silently equated to all pseudoline extensions. |
| “Une table barrée,” 1932–1949; “Le revêtement principal est connexe,” 1951–1984 | Canceled parity table and later asserted full dihedral monodromy. Hua admits uncertain connective text and differences between surfaces with/without exceptional crossings. |
| “Les positions d’un cercle sur une surface quelconque,” 1987–2015; “Pourquoi deux sortes de sommets seulement,” 2017–2036 | Standard-position circles, isotopy definition, one-rive case, special property PS. Hua says no general local-system descent is clear without control of vertex types. This is a later, sharper warning against reading current025 as universal. |
| “La bande supercritique, et une carte pentagonale,” 2038–2073 | Antipodal correction per exceptional crossing, five-involution pentagonal-map question, exceptional arrangements I_n and III_{p,q}. No resolved interpretation of the pentagonal map is claimed. |
| “L’opération de rotation,” 2087–2117; “La bande supercritique,” 2119–2132 | Explicit rotation on triples, eight local cases, unresolved exceptional sign and hole circuits. Connection to the flag formula is Hua’s interpretation. |
| “Un brouillon barré,” 2134–2147; “La caractéristique d’Euler,” 2149–2174 | Missing “rectification b),” quartic count `s₁=2s₀`, `χ=s₂−s₀`, and `g=1−χ` rather than ordinary orientable genus. Counting needs the intended surface and its cells established first. |
| “Les fuseaux,” 2196–2216; “Les quatre involutions,” 2218–2252; “Le graphe des couples,” 2254–2276; “Le plus petit modèle,” 2278–2298 | Spindles, three two-element torsors, flags, four involutions, and a Klein-four toy model. Several operation meanings and the toy cell counts remain unresolved. |
| “Compter, et balayer,” 2301–2339 | Critical-position counting heuristic and seven-wire permutation sweeps. Allowable sequences/wiring diagrams are Hua’s unverified modern literature comparison; this is not a proof of move completeness or relations. |
| “La structure locale,” 2344–2367; “Les types de fuseaux,” 2369–2389 | X*=Rel with stable faces, sous-stable edges and critical vertices; ambiguous endpoints of an edge; proposed spindle correspondence. This is close to follow-ups@944 but does not settle it. |
| “Le cube des générisations,” 2391–2420 | `2^ν` stable and `ν2^(ν−1)` sous-stable generizations, a project-reported Lean model, and an unanswered specialization question. Hua explicitly says topological representation and the tension with its local-surface description for ν≥3 are not formalized (2415–2418). |
| “Les balayages élémentaires,” 2422–2430; “Les opérations sur un repère,” 2432–2471 | I₁,I₂,I₃,I₇ examples, flag involution relations, duality of orientation conventions, and corrected reading of numbers in a later drawing. Examples alone do not establish generators and complete relations. |
| “Les facettes exceptionnelles (1er janvier1984),” 2473–2490; “Dessins, et les axiomes repris,” 2492–2553 | Revised exceptional facets and boundary-version axioms. The exact-one-summit-per-edge condition has an unreadable possible “sauf” qualifier; interpreting the boundary as replacing K₀ is explicitly Hua’s inference. |

A useful global caution comes from the modernization itself: its résumé says what the dossier “establishes” rather confidently (152–162), whereas the final line says the surface is **not finished** (2551–2553), and the detailed sections preserve missing constructions. The detailed caveats should control any synthesis.

## 5. Relation to our supplied register and to neighboring work

**Direct registered claim:** `Hua, findings register, 154-cyclic-order-determines-position`, `RESULTS_STATE.md:471`. Verdict: supported as an unproved expected injection; sharpen domain/target and preserve the nonstable-data issue. The Lean footnote is new interpretive/formalization context from Hua’s modernization, not a status upgrade.

**Direct open follow-up:** `follow-ups @944`, `RESULTS_STATE.md:293`, from `MPL_154_127-176 P05`. Current031–034 supply general graph-to-surface machinery, and current038–045 supply proposed local gluings and incidence descriptions. They sharpen the input required for the surface problem. They do not supply a proof that the later all-position extension structure is two-dimensional, a justified Euler count for that particular structure, or a complete presentation of all sweep moves. Hua’s later cube paragraph makes this distinction more urgent. The register’s Sturmfels–Ziegler homotopy-sphere input remains the register’s literature report in this memo; no claim is made that it proves a homeomorphism or a surface structure.

**Modern coherent-gluing comparison:** `MPL_154_077-126 O01` and `MPL_154_127-176 G09` (register453–456) are appropriate leads. Current025:23,031:37–41,032:22–63,039:60–200 show exactly why gluing conventions, orientation transport, and relations around filled cells must be checked before applying any coefficient-theoretic reconstruction. One may compare the shape of the problem with **STRATA C.8** (register428, a return’s proved claim about a pullback of locally constant coefficient categories), but the necessary input diagram and its coherent identification have not been supplied here. That comparison is not an application of C.8 and does not prove a manuscript assertion.

**No direct settlement of EXIT_ONE_TYPE P3c-general.** This is the open algebraic threefold stratal-zigzag question (register354). A finite pseudoline cell-gluing construction is not a construction of good normal-crossing completions or a stratal zigzag in that category. The current pages may motivate attention to gluing and boundary data; they neither settle nor materially specialize that algebraic problem. The register itself says there are no own results to use and check directly for this package (line16).

**Classification:** bounded agreement with the parent’s checked primary Esquisse§8 identification. The narrow subject is a relative-position/modular-surface problem in combinatorial geometry. Broad tame-topology adjacency is reasonable through finite cell structures, incidence, gluing, and the Esquisse context, but the text is not a formulation of a general category of moderate spaces. No differential/form complex, coefficient-form theory, comparison theorem for such forms, or specific1986 apparatus appears in current001–045. “Neither as primary subject; specifically Esquisse§8 combinatorial geometry of relative-position surfaces” is therefore more precise than labeling this a direct fragment of either formal program. Root should attach its separately verified Esquisse primary citation when making that historical identification.

## 6. Proposed next research actions, all outside transcription

1. Formalize the exact data in scan019’s polygon map, then perform the three-line nonstable/stable test in §1.3. Preserve the registered candidate status until the model matches.
2. Extract a consistent finite combinatorial definition of the construction in031–045, with explicit rules for exceptional arcs, marked rives, low-valence cases, and face boundary relations. Keep separate the structural graph surface, its dual all-position-face surface, and the later stable-face Rel surface.
3. Check polygon-transport holonomy around each actual filling cell before calling it a local system. The order-two condition in025 and the later PS caveat are likely important.
4. For chord sufficiency, write the Möbius-band attachment explicitly, including endpoint-packet ordering and possible multiplicity, and verify every pair of resulting pseudolines crosses once. This would address the precise missing construction, not repair the transcription.
5. Compare any resulting model with primary oriented-matroid extension-space literature only after its signed/unsigned and stable/nonstable quotients are specified. Do not treat Hua’s memory bibliography or his project-reported Lean results as verified replacements for that comparison.

No novelty claim, theorem-status change, transcription correction, or upload is made by this memo.
