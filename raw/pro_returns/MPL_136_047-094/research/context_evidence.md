# Context evidence for the research notes

This memo was prepared **after** the page stream was frozen (16 November 2026, 14:05:35 UTC) and the context archive was opened (14:05:42 UTC). It uses the supplied context texts and, for cross-reference only, the frozen LaTeX transcription; it contains no new image reading and does not revise the transcription. “PS p.” below means the pagination explicitly encoded by `\pspage{...}` in the supplied *Pursuing Stacks* typescript, not a cote-136 scan number. Line ranges identify the supplied source files.

## Scope and evidential status

`context/README.md`, lines 14–25, expressly describes the proposed integral cochain model, “constructions universelles,” the “topos de De Rham,” lecture plan, and the abelian-variety/Fourier-Chern examples as **planning questions**. The first 45 scans of cote 136 are absent from this context: the README says that their return had not arrived. The only supplied retrospective specifically entitled “De Rham complex with divided powers” is the **title of §94**, at `context/PURSUING_STACKS_CONTENTS.md`, line 120; chapter V itself is absent. Thus neither §94's contents nor a complete 1976 lecture outline can be recovered from this archive by inference from that title.

`context/notes/RESULTS_STATE.md`, lines 5–8, distinguishes a run's self-reported Proved/Refuted/Known/Open status from intake and referee review. The source files named at lines 133–149 are **references to records elsewhere**, not files present in the supplied archive. In particular, the detailed statements/proofs behind the register's abbreviated rows cannot be silently treated as read or independently checked.

The most direct register connections are **WG2 §2.4 #5**, **WG H6**, and **WG2 §Week #3** (lines 123–125). WG2 §2.4 #5 explicitly links the 1976 divided-power notes with integrality questions from other cotes; it calls the link a thread, not a statement. WG H6 is a conjectural finite-dimensional-local-system/schematization identification in characteristic zero; none of the 1976 constructions alone settles it. WG2 §Week #3 records a research assignment across cotes 137, 133, 153 and PS, rather than a mathematical result.

## Direct context anchors

### CX01 — The missing retrospective

**Location:** `context/PURSUING_STACKS_CONTENTS.md`, line 120, §94 (chapter V).

**Evidence:** The title calls §94 a retrospective on the divided-power de Rham complex and on linearization and arbitrary change of ground ring. It is the closest contextual title to scans 048–094, but its text is not included; citing it establishes the existence/topic of a later retrospective only.

**Relation:** Cote 136 adds direct manuscript evidence on the construction, its revisions and local questions. **IDs:** WG2 §2.4 #5; WG2 §Week #3. These remain unchecked planning entries.

### CX02 — Universal divided-power linearization in a different model

**Location:** `context/ps_chapters_VI_VII/ps6.tex`, §111, lines 350–413, PS pp. 450–451.

**Evidence:** The text proposes a universal map from a unipotent bundle represented by a module, with `exp(x)=sum x^(i)`, then notices that the sum is infinite and replaces the direct sum by the completion `prod_i Gamma_k^i(M)`. It claims independence of the chosen presentation and explicitly says that induced maps are compatible with **diagonal maps, not multiplication** (lines 398–405).

**Relation:** This is a useful comparison with Γ-based universal constructions on scans 074, 078, 083–091, but it is not the same construction or the same universal property. In particular, it cannot certify multiplicativity of the Stokes comparison on scans 065–072. **IDs:** WG2 §2.4 #5; WG H6 only as a later schematization question, not as a consequence.

### CX03 — Derived Γ needs projective or flat input

**Location:** `context/ps_chapters_VI_VII/ps6.tex`, §111, lines 628–672, PS pp. 455–456.

**Evidence:** After considering a morphism of semisimplicial modules and applying Γ componentwise, the text invokes projectivity to pass from quasi-isomorphism to homotopy equivalence. It explicitly retracts the earlier assertion that componentwise Γ always computes the derived functor; a projective resolution is needed, with flatness proposed as possibly sufficient.

**Relation:** The passage supplies a later warning germane to the projectivity condition `p≥1` on scan 078 and the flatness/universal tensor conditions on scans 080, 083, 089, 094. It does not identify the respective hypotheses or prove the 1976 claims. **IDs:** WG2 §2.4 #5; **MPL_134-8_043-087 R033** and **PRETOT A.1** are methodological analogues concerning tensor-flatness and acyclicity tests, not established reductions of this problem.

### CX04 — A retracted comparison that must not be conflated with the 1976 complex

**Location:** `context/ps_chapters_VI_VII/ps6.tex`, §119, lines 2896–2950, PS pp. 500–501.

**Evidence:** Grothendieck reports Illusie's objection to the expectation that Eilenberg–Mac Lane homology could be calculated by derived Γ, then gives his own degree-one counterexample. The extension represented by `1+at+bt^2` would split polynomially only if a polynomial `P` satisfies `P(a+a')=P(a)+P(a')+aa'`; the required half-integer coefficient prevents a splitting over Z, although ordinary `H^2(Z,Z)` vanishes.

**Relation:** This directly contradicts the particular discrete-versus-schematic comparison under discussion in §111, not automatically the separate divided-power de Rham construction of 1976. A research note may use the example to test overstrong proposed identifications, but must say exactly which functors are being compared. **IDs:** WG2 §2.4 #5; WG H6 as a warning against identifying distinct schematization proposals.

### CX05 — Binomial and divided-power alternatives are distinguished explicitly

**Location:** `context/ps_chapters_VI_VII/ps6.tex`, §119, lines 2951–3036, PS pp. 501–503.

**Evidence:** The discussion distinguishes integral-coefficient polynomials from integer-valued rational polynomials and proposes binomial algebras. Lines 2981–2989 explicitly contrast de Rham linearization using commutative algebras with divided powers with a possible binomial algebra for the unipotent-bundle approach; lines 3000–3036 formulate a comparison from binomial cochains to all set-theoretic cochains, with connectivity restrictions and a possible reduction to `K(Z,n)`.

**Relation:** This is a historical link to later binomial models, not an identification of the symbols Γ in the 1976 and 1983 settings. It strengthens the need to separate additive cohomology comparison, products, divided powers and recovery of homotopy type. **IDs:** WG2 §2.4 #5; WG H6 remains open/unchecked.

### CX06 — Universal operations require a specified algebraic theory

**Location:** `context/ps_chapters_VI_VII/ps6.tex`, §120, lines 3131–3198, PS pp. 506–507.

**Evidence:** Divided powers, λ-operations, binomial operations and Adams-type operations are discussed as different extra structures. The text distinguishes operations on a suitable ideal, as for divided powers, from operations on the entire unital ring, and proposes an analyzer formalism with additive/multiplicative diagonals and composition.

**Relation:** This is an apt later comparison for the missing axioms of the product and divided-power operations on scan 077 and for the categories with all structures on scan 094. It does not supply the axioms omitted in the 1976 passage; those would need to be stated and checked separately. **IDs:** WG2 §2.4 #5; GALOIS G.6/E.11 only for a clearly labelled comparison of how much additional structure a coefficient theory requires.

### CX07 — Three approaches; an adjoint is not automatic

**Location:** `context/ps_chapters_VI_VII/ps6.tex`, §121, lines 3222–3240, PS pp. 507–508; §124, lines 3933–3982, especially 3943–3980, PS p. 521.

**Evidence:** The later text distinguishes divided-power de Rham algebras, additive categories with diagonal maps, and semisimplicial unipotent bundles. In §124, forming a semisimplicial set from a chain complex and then its divided-power de Rham complex is rejected as a candidate over general k because it forgets the original k-module structure; existence of the desired right adjoint is itself doubted.

**Relation:** A cochain-valued construction and a universal quasi-isomorphism such as scan 091's `A -> bar A` do not by themselves define an adjunction recovering homotopy types. **IDs:** WG H6; WG2 §Week #3; GALOIS G.6/E.11 for the limited methodological analogy with unresolved bare-derivator enhancements.

### CX08 — Sheaf weak equivalence versus taking sections

**Location:** `context/ps_chapters_VI_VII/ps6.tex`, §127, lines 4716–4827, PS pp. 535–537 (main discussion begins p. 536).

**Evidence:** The text places models in a topos of sheaves over k and invokes Illusie's weak equivalences. Lines 4753–4767 stress that a weak equivalence of semisimplicial sheaves does **not** automatically induce a weak equivalence on k-valued sections; suitable restrictions on the allowed bundles are proposed to restore this behavior and stability under ring extension.

**Relation:** This is closely relevant to why scans 064, 080–082 and 094 impose flasqueness and universal conditions before taking global sections or applying direct image. It is a later warning about an analogous passage, not the proof of the 1976 acyclicity assertion. **IDs:** WG2 §2.4 #5; BISITE C.1 is the register's general presheaf-model comparison; GALOIS D.2/BISITE A.19 are only comparisons of coefficient scope.

### CX09 — Derived construction versus a naive tangent construction

**Location:** `context/ps_chapters_VI_VII/ps6.tex`, §131, lines 5488–5530, PS pp. 550–551; beginning of §132, lines 5531 onward, PS pp. 551–552.

**Evidence:** Formally simple functors on semisimplicial affine schemes need not have the intended homotopical interpretation. Grothendieck points out that a naive tangent-space calculation for the proposed sphere models would identify their homotopy groups with their homology groups and treats this as a failure requiring a derived replacement.

**Relation:** It offers a warning for any claim that the bigraded algebra of scans 080–094 already carries full unstable homotopy information. There is no direct manuscript identification of this later naive tangent functor with the 1976 complex. **IDs:** WG H6; WG2 §Week #3.

### CX10 — Category of elements and coefficient sums

**Location:** `context/ps_chapters_VI_VII/ps7.tex`, §135, lines 438–493, PS pp. 563–564.

**Evidence:** The text gives `LH(A/X,Z) ≃ LH(A,Z^(X))`, then explains that the relevant left direct image along `A/X -> A` is exact because it is a sum over the discrete fibers. The displayed formula for `f_!F` sums the coefficient fibers `F(a)_u` over `u in X(a)`.

**Relation:** This is a direct later formal analogue of scan 058's slice/category-of-elements description and scan 062's sheaf/cosheaf coefficient construction. The homological sum formula must not be silently used as a proof of the cohomological product/flasqueness claims. **IDs:** BISITE C.1; WG2 §2.4 #5. PRETOT A.1 concerns a different acyclicity recognition problem and should not be presented as the same theorem.

### CX11 — Base ring and ringed-topos formalism

**Location:** `context/ps_chapters_VI_VII/ps7.tex`, §136, lines 616–660, PS pp. 567–568.

**Evidence:** Equation (136.1) expresses the constant-coefficient k-linearization as the integral one tensored **derivatively** with k. The passage places `f*`, `Rf*`, derived tensor and derived Hom in the familiar formalism of arbitrary commutatively ringed topoi.

**Relation:** This supplies a precise later context for the arbitrary-ring and relative constructions on scans 080–082 and 089–094. The derived tensor sign matters: the universal flatness conditions in the manuscript should be compared with the hypotheses that allow ordinary tensor products to represent derived ones. **IDs:** WG2 §2.4 #5; MPL_134-8_043-087 R033 is a first-pass tensor-flatness lead, not a substitute proof.

### CX12 — A nearby self-correction about adjoints and variance

**Location:** `context/ps_chapters_VI_VII/ps7.tex`, §136, lines 692–729, PS pp. 568–569.

**Evidence:** Grothendieck corrects his initial description of `f!` as right adjoint to `Rf*`, distinguishing proper maps and the pair `Rf_!, f!`. He then stresses that a superficially similar four-functor sequence does not consist of adjoints in the usual duality context.

**Relation:** This supports caution when comparing scan 062's sums/products and opposites or scan 091's explicit negative answer for the cosimplicial topos. It is not evidence that the particular 1976 “Non” has the same cause. **IDs:** BISITE C.3 (register claims failure of a general exchange involution); comparison only, since the register's precise morphism classes differ.

### CX13 — Constant and variable coefficient rings cannot be interchanged without proof

**Location:** `context/ps_chapters_VI_VII/ps7.tex`, §138, lines 1230–1320, PS pp. 580–582; especially 1296–1320.

**Evidence:** The text questions compatibility of left direct image with restriction of a variable ring sheaf and gives a failure of the required projective acyclicity. It then separately considers the case where both coefficient rings are constant.

**Relation:** Scan 064 explicitly extends the locally constant coefficient discussion to arbitrary coefficients, and scans 080–094 return to general ring sheaves with stronger hypotheses. These are changes of scope needing separate proofs, not harmless notational variants. **IDs:** GALOIS D.2; BISITE A.19; WG2 §2.4 #5. The first two are listed as run claims, not independent proof of the de Rham assertions.

### CX14 — Products, Steenrod operations, and the richer topos

**Location:** `context/ps_chapters_VI_VII/ps7.tex`, §139, lines 1680–1767, PS pp. 589–591; especially 1717–1760.

**Evidence:** After describing ordinary derived coefficient operations as routine, Grothendieck identifies additive envelopes with diagonals as the broader idea and explicitly asks about Steenrod operations (lines 1742–1745). He then distinguishes the full coefficient theory of a category viewed as a topos from its mere homotopy type (lines 1747–1760).

**Relation:** This is a useful retrospective link for scans 069 and 075–078, where multiplicative/divided-power questions remain unsettled, and for the distinction between arbitrary sheaves and local systems in scans 058–064. It does not say that the 1976 divided-power algebra supplies Steenrod operations. **IDs:** WG2 §2.4 #5; WG H6 remains a separate hypothesis about local systems and schematization.

## Suggested manuscript-to-context map

Each row gives a context search actually performed and a relation that can safely be stated. These are leads for the final notes, not emendations of the source.

| Cote-136 scan(s) and issue | Context search / precise anchor | Safe relation and relevant register ID |
|---|---|---|
| 048–052: cochains, normalized `!`, exterior formulas | `cochain`, `Gamma`, `De~Rham`; CX01, CX05, CX07 | The later retrospective title and distinct linearization proposals contextualize the construction; they do not determine a faded symbol. WG2 §2.4 #5. |
| 054–056: existence, uniqueness and abstract Stokes construction | `integration`, `abelianization`; CX10–CX11 | Later categorical integration uses a different, derived-functor framework; analogy only. WG2 §2.4 #5. |
| 058: `(Delta/X)^op` and the induced topos | `A_{/X}`, `f_!`; CX10, PS §135 (135.8)–(135.11) | A substantive later restatement of the category-of-elements coefficient mechanism. BISITE C.1. |
| 064: arbitrary versus locally constant coefficients | `constant`, `coefficient`, `topos`; CX13–CX14 | Later PS explicitly preserves this distinction; no blanket homotopy-invariance conclusion. GALOIS D.2; BISITE A.19. |
| 062: sheaves/cosheaves and opposite variance | `cosheaf`, `f_!`, `f_*`; CX10, CX12, CX14 | Compare definitions and sums/products; no unsupported symmetry of all properties. BISITE C.3 only as a limited analogy. |
| 064: “à vérifier ce point” on flasqueness | `sections`, `quasi-isomorphism`, `projective`; CX08, CX10–CX13 | Later context confirms that the passage to sections needs hypotheses; it does not verify the marked step. WG2 §2.4 #5; R033. |
| 065–067: comparison chain map induced by Stokes system | `cochain`, `linearization`; CX01, CX07 | Additive comparison should be separated from enriched-algebra comparison. WG2 §2.4 #5. |
| 068: universal coefficient quotient for the Stokes system | `universal`, `Gamma`; CX02 | Different universal constructions: 068 is a representing quotient for admissible integration maps, CX02 a completed polynomial linearization. WG2 §2.4 #5. |
| 069: divided-power quotient and multiplicativity still to study | `De~Rham`, `binomial`, `products`; CX05–CX06, CX14 | Direct evidence that the planning statement's product clause needs an additional argument. WG2 §2.4 #5. |
| 070–072: smooth-singular comparison and local support hypotheses | `sections`, `weak equivalence`; CX08 | Later PS gives a general warning about sections; it supplies neither the missing local argument nor an arrowhead reading. WG2 §2.4 #5. |
| 074–075: transferred structures followed by “est faux” | `multiplications`, `divided powers`; CX02, CX04–CX06 | Two distinct retractions must be kept separate: this one is internal to the 1976 transfer attempt; §119 retracts another comparison. WG2 §2.4 #5. |
| 076–077: exceptional products and axioms left to supply | `operations`, `ideal`, `analyzer`; CX06 | A later framework for organizing extra operations; it does not complete the 1976 axioms. WG2 §2.4 #5. |
| 078: canonical splitting versus projectivity | `projective`, `Gamma`; CX03 | Existence of a split epimorphism does not automatically choose a canonical section; later Γ homotopy invariance also needs a projectivity hypothesis. WG2 §2.4 #5; R033 as a separate projectivity lead. |
| 080: “Faisceautisation du topos De Rham” | `faisceaut`, `topos`, `De~Rham`; CX08, CX11 | The exact heading has no match in context; PS supplies a later sheaf-model setting, not its definition. WG2 §2.4 #5. |
| 081–082: range of cohomology comparison; functoriality | `base`, `ring`, `sections`; CX08, CX11 | Tensor and direct-image compatibility are substantive; a range `j≤i` should not be omitted when summarizing. WG2 §2.4 #5. |
| 083,085: elementary algebras and `(k,L,Phi,u)` | `Gamma`, `universal`, `ground ring`; CX02, CX06–CX07 | Algebraic presentation and coefficient dependence are more precise than a generic “integral model.” WG2 §2.4 #5. |
| 087: “Que peut-on dire” for lambda and mu | `independent`, `isomorphism`, `derived`; CX02, CX08 | A later independence claim is an analogy; scan089 should be used first to see what this manuscript itself provides. WG2 §2.4 #5. |
| 089: universal embedding and transitive derived isomorphisms | `universal`, `projective`, `derived`; CX03, CX08, CX11 | Derived independence is the supported direction; strict canonical chain-level equality would be stronger. WG2 §2.4 #5. |
| 091: De Rham condition, negative cosimplicial case | `opposite`, `cosheaf`, `topos`; CX12–CX14 | Context supports treating variance and coefficient richness carefully, but provides no proof of this particular “Non.” WG2 §2.4 #5; BISITE C.3 only a methodological comparison. |
| 091,094: universal quasi-isomorphism and localization | `adjoint`, `derived category`; CX07–CX09 | The proposed localization belongs to the manuscript's algebraic setup; it does not establish a model category or a homotopy-type classification by itself. WG H6; GALOIS G.6/E.11 only as a structural analogy. |
| 049,051,053: reused English rational homotopy discussion | `linearization`, `rational`, `K(`; CX04–CX07 | Do not merge this copied/typewritten argument with the handwritten integral construction; their assumptions differ. WG2 §2.4 #5. |
| 055,057,059,061,063,071,073,090,092: reused arithmetic/analytic material | `abelian variet`, `abélo`, `Chern`, `Fourier`; no direct match in supplied PS chapters | Arithmetic content on reused leaves cannot establish that the de Rham lecture used those examples. Closest relevant planning record is WG2 §2.4 #5; no register theorem settles attribution. |
| 084: SMF notice with characteristic classes | `Chern`, `Fourier`, `lecture`; no context match | This is a separate meeting announcement, not evidence for a Fourier-Chern example in the lecture. README planning question; no mathematical result ID directly bears on it. |
| 086,088: university thesis notices; 093: isolated foliation | title and pagination searches | Context provides no relation to the mathematical program; record as physical-document evidence without invented mathematical relevance. |

## Negative searches and limitations

Case-insensitive searches across both PS chapter files and the contents file found **no literal Fourier, Chern, “abelian variet...”, “faisceaut...”, “topos de De Rham”, or “De Rham topos”**. Searches for `De~Rham` and divided powers yielded the passages above, while the README supplied the questions themselves. Searches across the frozen page files found no Fourier/Chern phrase or “variétés abéliennes”; scan 090 does contain “groupe abéloïde,” and scan 084 contains a title about characteristic classes of a quadratic module in étale cohomology. These findings are bounded to the supplied pages and should not be inflated into an assertion about the absent first portion of cote 136 or the whole archive.

The context's register contains many results on total asphericity, filtered/exact colimits, localizers and derivators. Most do **not** bear directly on the divided-power construction, and using them merely because the words “cohomology,” “topos” or “semisimplicial” recur would overstate the link. In particular, the reviewed total/exact hierarchy entries do not verify a universal-flasqueness assertion for Γ or Λ in scans 080–094. Where the 1976 pages offer a concrete monoidal construction, they may provide an example or design pattern for the open enhancement questions GALOIS G.6/E.11; they do not solve the arbitrary bare-derivator problem.

## Research directions suggested by the comparison (editorial, not authorial)

1. **Weight and cohomological degree should be tracked independently.** The range-qualified comparison on scans 081–082 and the marked divided-power parameter suggest testing products as maps between weights before collapsing to an unweighted cochain-algebra claim. Confidence: medium; this is motivated by the visible grading and by the manuscript's own product revisions, not by a proof that the resulting structure exists. Context relation: CX05–CX07 distinguish several structured linearizations; bears on WG2 §2.4 #5.

2. **Separate universal acyclicity from choice independence.** Scans 080/089/094 provide hypotheses intended to survive tensoring, whereas scans 087–091 address comparing choices of embeddings. Confidence: high that these are separate proof obligations, medium that the manuscript's proposed comparisons suffice in a suitable enhanced category; context CX08 and CX11 show why sheaf equivalences, sections and base change should be tested separately. Bears on WG2 §2.4 #5 and, by analogy only, GALOIS G.6/E.11.

3. **Do not use the 1983 counterexample as a shortcut.** A useful test program would spell out the functor from the 1976 algebra to the 1983 schematic/cochain construction before importing the W2 obstruction. Confidence: high that this comparison is needed, low that such an identification exists in the desired generality; §119 and §124 explicitly distinguish the approaches. Bears on WG2 §2.4 #5 and WG H6.

4. **Cup products and higher operations require separate comparison data.** Scan 069's multiplicativity question and 075's withdrawal already prevent treating an additive quasi-isomorphism as a fully structured identification. Confidence: high concerning the missing logical implication; no claim that a suitable enriched comparison cannot be built. Context CX14 explicitly leaves Steenrod-operation questions beyond the routine additive formalism; bears on WG2 §2.4 #5.
