# Integral cochains, divided powers, and the binomial comparison

Research support for MPL_137_045–086, prepared after the transcription freeze of **2026-11-17 21:38:33 UTC**. This investigation read the frozen transcription as text, the supplied context, and published primary mathematical sources; it did not inspect manuscript images, perform OCR, or change transcription files. The scan numbers below are the package's scan numbers, one greater than the archive foliation in this range.

## Conclusion and scope

**Scans 063–074 supply a framework for multiplicative cochains, and scans 075–086 supply a framework for polynomial operations; these pages do not establish recovery of integral homotopy types.** Their most useful contribution to bridge B7 is to separate several structures that a compressed historical narrative can accidentally identify: the tensor product transported from the simplicial models, the usual total tensor product of complexes, multiplication up to homotopy, polynomial representability by divided powers, and a later binomial theory of integer-valued functions. This conclusion concerns the assigned scans and the frozen reading, not the whole unpublished corpus.

The direct historical passage from a divided-power expectation to a binomial replacement is in the supplied *Pursuing Stacks*, VI §119, original pp. 500–504. The modern results indexed below provide comparison targets; their hypotheses and their different conclusions about objects, maps, and derived points must remain visible. No equivalence between Grothendieck's entire multiplicative formalism in cote 137 and one of those modern homotopy theories has been constructed in this investigation.

## 1. Primary-source reference and locator index

The full theorem statements, hypotheses, comparisons, and bibliography are consolidated in the [final research notes](../MPL_137_045-086_notes.md), at the note IDs below. This index records the passages consulted without repeating their paraphrases or bibliographic entries; page numbers are printed/internal pages, not zero-based PDF indices.

| Source key | Final notes | Consulted passages |
|---|---|---|
| **[T20] Toën** | **R04**; bibliography **T20** | [Journal PDF](https://epiga.episciences.org/6822/pdf): Théorème 0.1, pp. 2–3; §1, p. 4; Definition 2.1; Corollaire 3.4, p. 9; Théorème 4.1, p. 11; §5, pp. 13–14. |
| **[H24] Horel** | **R05–R06**; bibliography **H24** | [Author PDF](https://geoffroy.horel.org/binomial.pdf), internal pagination: Definition 1.1/§1, pp. 3–4; Theorem 3.7, p. 7; Remark 3.11, p. 8; Theorems 5.4 and 6.1, p. 13; Remark 8.5, p. 19. See the final bibliography for the distinction between consulted versions. |
| **[M06] Mandell** | **R07**; bibliography **M06** | [Article PDF](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/mandell2.pdf): Main Theorem, p. 213; Theorems 0.1–0.2, pp. 214–215; accompanying discussion, pp. 214–216. |
| **[BF04] Berger–Fresse** | **M09–M10**; bibliography **BF04** | [arXiv v2 PDF](https://arxiv.org/pdf/math/0109158): Theorem 2.1.1, p. 30; §2.2.8, p. 35. |
| **[BW05] Borger–Wieland** | **R15**; bibliography **BW05** | [Journal PDF](https://maths-people.anu.edu.au/~borger/papers/_all/PlethysticAlgebra.pdf): §1; §2.14, p. 260. |

## 2. What the frozen pages actually supply

| Scans | Textual anchor | Bounded interpretation |
|---|---|---|
| **063–064** | “résolutions droites … \(\Sigma\)-injectives de \(\Psi^0\)” and a unique homotopy class between resolutions | Relative homological algebra supplies comparison maps and independence up to homotopy. This is the mechanism used in the later cup-product construction. |
| **065–066** | Tensor product “composante par composante”; transported product “notation \(*\), pour éviter des confusions” | The monoidal product being transported is specified. It cannot silently be replaced by the usual tensor product of complexes. |
| **066–067** | Maps \(F(X)\otimes F(Y)\to F(X\otimes Y)\), a unit map, and constraint diagrams; “str. mul. demi-simpliciale” | The text gives symmetric lax monoidal data on the functor, in modern terminology, and explicitly chooses a name to avoid confusion with another meaning of multiplication on complexes. |
| **068–069** | Compatibility with half-cosimplicial operations and differentials, plus unit, associativity, commutativity | The multiplication is more structured than a single cochain-level bilinear map. Its precise translation into a modern cosimplicial or operadic category remains a comparison problem. |
| **069–071** | “\(K\) n'a pas d'unité pour \(*\)!”; the factorization arrow is marked “?” | The construction itself detects a missing unit object and passes to a larger category. The question mark should not be suppressed by a modern blanket equivalence claim. |
| **072** | “défini à homotopie près”; “attention aux signes !”; “le tout à homotopie près” | The obtained map \(C^\bullet\otimes_B C^\bullet\to C^\bullet\) has the stated laws up to homotopy, and induces a graded algebra on cohomology. These words do not assert a strict ordinary commutative DGA. |
| **073–074** | Deleted “non tronqué”, inserted “jusqu'au degré \(n\) … incl.”; “complexe tronqué”; “Car. 0” | The de Rham comparison on this page has an explicit degree bound. The final characteristic-zero sentence does not remove that bound or assert integral space reconstruction. |
| **075–077** | Outer-variable additivity; the weight-uniqueness argument is cancelled; the grading becomes “structure supplémentaire” | The author notices arithmetic ambiguity in scalar weights and responds by retaining a chosen grading. This is relevant to integral operations, but it is not yet the integer-valued polynomial ring. |
| **078–084** | Representability \(P_n(X,Y)=\operatorname{Hom}(\Gamma^nX,Y)\), stronger tensor universal properties, \(\alpha_{p,q}:\Gamma^{pq}\to\Gamma^p\Gamma^q\) | The claimed equivalence concerns polynomial categories and tensor-PD categories. Its word “équivalence” concerns those algebraic structures, not an equivalence between spaces and cochain objects. |
| **085–086** | A question about maps \(\Gamma^p\Gamma^q(M)\to\Gamma^{pq}(M)\); “et non seulement comme application ensembliste” | The requested PD multiplication has the opposite direction to the earlier \(\alpha\). The final enrichment question asks for additional polynomial structure on morphism modules. |

### Three meanings of commutativity

The following distinctions are explanatory, not proposed alterations of the transcription.

1. A commutative cosimplicial ring is a diagram of ordinary commutative rings with cofaces and codegeneracies. For a simplicial set, \(A^n=\operatorname{Map}(X_n,\mathbb Z)\) has a pointwise product in each degree. That product combines two functions on the **same** set \(X_n\).
2. A strictly graded-commutative DGA has multiplication \(C^p\otimes C^q\to C^{p+q}\), the differential Leibniz rule, and the signed commutativity identity as an actual equality. This multiplies elements of **different cochain degrees**, and is a different assertion.
3. An \(E_\infty\)-cochain algebra specifies operations in all arities and homotopical degrees, with coherent compatibility. A graded cohomology ring or isolated homotopies do not specify that structure.

**Elementary calculation here, using [BF04, §2.2.8].** On the oriented interval take \(f(0)=0,f(1)=1\) and \(e([01])=1\). Then \((f\smile e)([01])=0\), while \((e\smile f)([01])=1\). Degreewise commutativity therefore does not make the ordinary cup product commutative. This makes no claim about other models of the interval.

Consequently, scan 072 fits naturally beside modern coherent cochain constructions, but the phrase “up to homotopy” alone does not certify all required coherences. Conversely, the existence of a strictly commutative cosimplicial function ring is compatible with failure of the ordinary cup product to be strictly commutative. No contradiction is present, and there is no need to attribute a false strict-DGA claim to the manuscript.

## 3. Divided powers and binomial operations are different

For clarity, write
\[
\operatorname{Int}(\mathbb Z)=\{f\in\mathbb Q[t]:f(\mathbb Z)\subseteq\mathbb Z\}.
\]
This is a ring of **polynomials**, not the ring of all functions \(\mathbb Z\to\mathbb Z\). Its elementary member \(\binom t2=(t^2-t)/2\) already distinguishes it from \(\mathbb Z[t]\). The binomial operation is defined on every ring element in its intended category; divided powers are ordinarily additional operations on a specified ideal or positive-degree part.

**Elementary separation, performed here.** The binomial ring \(\mathbb Z\) does not admit divided powers on its entire unit ideal: the divided-power identity \(2\gamma_2(1)=1\) would require an integral half. Conversely, the free divided-power algebra \(\Gamma_{\mathbb Z}(\mathbb Zx)\), with its standard divided powers on the augmentation ideal, is not a binomial ring: it has free abelian basis \(\gamma_n(x)\), and
\[
\frac{x(x-1)}2=\gamma_2(x)-\frac{x}{2}
\]
is not integral in that basis. Thus even very familiar PD examples cannot be relabelled binomial examples; a comparison requires a construction and hypotheses.

### Exact associated-graded calculation

**A standard elementary calculation checked here, not a novelty claim and not attributed to the manuscript.** Set \(F_d=\{f\in\operatorname{Int}(\mathbb Z):\deg f\leq d\}\), with \(F_{-1}=0\), and \(b_n(t)=\binom tn\). The Newton expansion
\[
f(t)=\sum_{n=0}^d (\Delta^n f)(0)b_n(t),\qquad
\Delta f(t)=f(t+1)-f(t),
\]
has integral coefficients for integer-valued \(f\); conversely every \(b_n\) takes integral values on all integers, including negative ones. Thus \(F_d=\bigoplus_{n=0}^d\mathbb Zb_n\), so the degree-\(n\) quotient is free on \(\overline{b_n}\). The leading term of \(b_n\) is \(t^n/n!\), and comparison of leading coefficients gives
\[
\overline{\binom tm}\,\overline{\binom tn}
=\binom{m+n}{m}\,\overline{\binom t{m+n}}.
\]
Consequently \(\gamma_n(x)\mapsto\overline{b_n}\) is an isomorphism
\[
\Gamma_{\mathbb Z}(\mathbb Zx)\xrightarrow{\sim}
\operatorname{gr}_F\operatorname{Int}(\mathbb Z)
\]
of **unital graded \(\mathbb Z\)-algebras**, without rationalizing either side. This is polynomial-weight grading with ordinary commutativity, not cohomological grading with Koszul signs. This is not an isomorphism between the original filtered ring and its graded ring: \(t^2=2b_2+t\), while the homogeneous divided-power relation is \(x^2=2\gamma_2(x)\).

### What substitution retains and loses

For nonconstant one-variable polynomials over \(\mathbb Q\), \(\deg(f\circ g)=\deg(f)\deg(g)\): positive-degree substitution does **not** itself lower the degree. Its leading symbol is determined by the two leading symbols; specifically, for \(m,n\geq1\),
\[
\sigma_{mn}(b_m\circ b_n)
=\frac{(mn)!}{m!(n!)^m}\,\overline{b_{mn}}.
\]
The coefficient is integral (it counts partitions into \(m\) unlabeled blocks of size \(n\)) and is the familiar divided-power iteration coefficient. This positive-degree fact does not recover lower-degree terms or operations involving constants.

For an explicit loss of information, let \(b=b_2\) and \(c=b_2+t\). They have the same degree-two symbol, but \(c\circ b-b\circ b=b\) and \(b\circ c-b\circ b=(t+1)b\); the degree-four symbols agree while the operations differ. More sharply, \(b(1)=0\) and \(c(1)=1\): composition with the constant polynomial \(1\) does **not** descend to a well-defined operation \(\operatorname{gr}_2\times\operatorname{gr}_0\to\operatorname{gr}_0\) from leading symbols. These are two polynomial lifts, not two asserted fully compatible binomial structures.

Accordingly, recovering a binomial system from this PD associated graded requires additional lower-degree lifting/extension data and verification of composition, constant, and unit identities. Passing to homotopy theory also requires the relevant coherent derived data; the graded-ring calculation proves no existence, uniqueness, or homotopy-recovery theorem. **Confidence: high** for the algebraic statements and counterexamples; **medium** that such a filtered refinement is the productive categorical comparison for these scans, since no functorial construction, base-change theorem, or homotopical comparison has been built here.

The additional composition structure in [BW05] makes this a sharper future question than merely asking whether the same denominators appear. Scans 081–086 already foreground composition and polynomial dependence on morphisms, so a comparison preserving those operations is more plausible than one based only on underlying graded modules; this is a research proposal, not a claimed historical identification.

## 4. The 1983 correction in supplied context

The supplied `context/ps_chapters_VI_VII/ps6.tex`, **VI §119, original pp. 500–504**, records an abandoned divided-power expectation after a discussion with Illusie and then poses a binomial comparison. The local example is an extension with cocycle \(aa'\): a polynomial splitting would require
\[
P(a+a')-P(a)-P(a')=aa',\qquad
P(t)=\tfrac12t(t-1)+ct.
\]
That expression is integer-valued for suitable integral \(c\) but is not a polynomial with integral coefficients. This is a direct reason to enlarge the allowable functions, rather than simply add a name to an existing PD structure.

On original p. 503, the proposed comparison is
\[
\operatorname{Sym}^{\rm bin}_{\mathbb Z}(L_*^\vee)
\longrightarrow \operatorname{Maps}(L_*,\mathbb Z),
\]
where the components of \(L_*\) are free of finite type. It is posed as a question about a quasi-isomorphism under \(H_0(L_*)=0\), with possible further \(H_1(L_*)=0\), and reduction to \(K(\mathbb Z,n)\), \(n\geq1\), is suggested. This precise question is a closer bridge to the modern Eilenberg–Mac Lane comparison than the truncated statement of scan 073; it is a later revision, not a theorem available to read backwards into the 1970s manuscript.

**VI §120, original pp. 506–507**, explicitly distinguishes PD structures, binomial structures, lambda operations, and operations of Adams type before discussing analyzers. The current assignment contains no verified reading of cote 153, so the planning conjecture that its analyzer is exactly the binomial plethory remains unverified here.

## 5. Context matches, differences, and candidate notes

`context/README.md` and all of `context/notes/RESULTS_STATE.md` were read before this report was written. Searches used the terms `binomial`, `commutativ`, `cosimp`, `divided`, `pleth`, `Horel`, and `Toën/Toen`, plus the cote/scan identifiers. The following status labels preserve the supplied distinctions between checked results, leads, planning guesses, and Hua's modernized interpretation.

### IC01 — Multiplication uses the transported tensor product

**Anchor:** scans 065–069, “notation \(*\), pour éviter des confusions” and “str. mul. demi-simpliciale”; **kind:** scope clarification; **confidence:** high. The product is transported from degreewise simplicial tensoring and is packaged as compatible functorial maps before the ordinary cochain cup product appears. This supports **MPL_133 B06**, a supplied lead about strict cosimplicial versus strict DGA commutativity, but does not by itself prove equivalence with a modern integral model category. **Context relation:** sharpens the README/B7 planning guess rather than confirms its strongest reading.

### IC02 — The cochain laws on scan 072 are explicitly up to homotopy

**Anchor:** scan 072, “le tout à homotopie près”; **kind:** proved scope of the textual assertion; **confidence:** high. The page supports a product on cochains with the named laws up to homotopy and the resulting graded algebra on cohomology. **Hua, modernised reading of cote 137, “Le cup-produit”**, gives the same interpretation, while his preceding **“Foncteurs multiplicatifs”** labels the \(E_\infty\) comparison as his own rapprochement. The present pages support that comparison as a research direction; they do not supply the missing operadic identification automatically.

### IC03 — The de Rham comparison has a degree bound

**Anchor:** scans 073–074, “jusqu'au degré \(n\) … incl.” and “complexe tronqué”; **kind:** limitation; **confidence:** high. This is a bounded cohomological/homotopical comparison, not reconstruction of a space from all cochains and operations. **Hua, “Le complexe de De Rham à puissances divisées”**, also retains truncation; his related earlier comparison with the folder's p. 3 is credited to his project, not established anew here. **Context relation:** limits the B7 planning claim and the **WG2 §2.4 #5** integrality thread; no supplied result is closed by it.

### IC04 — “PD” still conceals an extra structure question

**Anchor:** scans 084–086, “quand et comment” and the maps \(\Gamma^p\Gamma^q\to\Gamma^{pq}\); **kind:** explicit open question; **confidence:** high. The tensor-PD category axioms already contain the reverse-direction composition maps, so the name does not make the later multiplication automatic. Frozen scan 086 already asserts that the canonical structure exists in the example; **Hua, “Questions ouvertes”**, adds an explanation of its construction for modules, with \(q\geq1\). **Context relation:** supports the qualification in **137-polynomial-categories-pd-tensor-categories**, a candidate from Hua's project, while leaving the abstract problem open.

### IC05 — Integer-valued polynomial comparison is a later repair

**Anchor:** scans 073, 085 and supplied PS VI §119, pp. 500–504; **kind:** historical comparison; **confidence:** high for the distinction, medium for the proposed developmental connection. The 1983 text explicitly changes the candidate algebra of functions after the failed integral comparison, whereas these assigned scans remain in the divided-power and polynomial-category formalism. This is the precise sense in which cote 137 can be preparatory to B7 without already containing its solution. **Context relation:** reinforces the supplied lead **MPL_133 B05**, “1983 correction and a new question”; it does not verify the unseen cote 133 itself.

### IC06 — Three modern reconstruction claims must remain separate

**Anchor:** scan 072's homotopy qualifier and scan 084's algebraic equivalence; **kind:** literature boundary; **confidence:** high. Object recognition, faithfulness of maps, and full faithfulness are distinct assertions, as final notes R04–R07 record. The modern theorem matching a strong integral reconstruction claim uses specific derived algebraic structure and hypotheses absent from the corresponding assertions on these scans. **Context relation:** B7 should cite the exact appropriate modern theorem, not use the combined names Toën–Mandell–Horel as interchangeable evidence.

### IC07 — A filtered comparison is a concrete next question

**Anchor:** scans 076–077's arithmetic weight problem and scans 081–086's composition maps; **kind:** new research proposal; **confidence:** medium. The rank-one associated-graded calculation in §3 suggests asking whether the homogeneous divided-power formalism admits a filtered enlargement whose lower terms encode integer-valued binomial operations. This would have to preserve substitution and morphism enrichment, not only graded multiplication. **Context relation:** no matching proved result was found in `RESULTS_STATE.md`; this is a proposal prompted by B7 and the supplied PS §119–120 discussion, not a new theorem about cote 137.

### IC08 — Two differences from Hua deserve reading notes

**Anchor:** scans 066 and 073; **kind:** reading question; **confidence:** high that the two frozen texts differ, unresolved as to the manuscript image. **Hua, “Foncteurs multiplicatifs”**, calls the unit map an isomorphism and says “à unité forte”, but the frozen scan 066 has an unmarked arrow \(\alpha\), while its constraint isomorphisms are marked. **Hua, “Le complexe de De Rham à puissances divisées”**, gives a negative sentence about operations without a PD structure, whereas frozen scan 073 reads a positive “On en peut affirmer encore” followed by uncertain wording. These are points for the primary transcriber's image-based doubt record, not authority to modify the frozen transcription.

## 6. What would still have to be proved

The following are **our comparison obligations**, not statements attributed to Grothendieck:

| Desired conclusion | Work still required |
|---|---|
| Identify the multiplicative objects with strict commutative cosimplicial algebras | Specify exactly the indexing category meant by the half-simplicial notation and the functorial reconstruction, including degeneracies if used; prove compatibility with the specified monoidal product. Do not infer the presence or absence of degeneracies merely from the historical label. |
| Pass to a coherent cochain model | Construct a compatible normalization/operadic comparison and verify higher coherence, units, and weak equivalences. The binary product calculation alone is insufficient. |
| Pass from homogeneous PD operations to binomial functions | Supply the filtered or otherwise enriched construction, including lower-degree terms and substitution; the elementary examples in §3 rule out simple identification. |
| Infer homotopy reconstruction | Specify the derived category or infinity-category, derived mapping spaces, the class of spaces, and the recovery functor; then prove the appropriate unit or object-recognition statement. |
| Upgrade the degree-\(n\) de Rham comparison | Establish compatibility as \(n\) varies and the relevant convergence/completion statement; the isolated truncated comparison does not supply it. |

The supplied **GALOIS G.6**, **GALOIS E.11**, and **RESIDUE I.7** leads concerning higher coefficients for bare derivators are not resolved by this argument: the manuscript here explicitly chooses tensor and operation data. That methodological resemblance can be noted, but no inference from these pages eliminates an enhancement hypothesis in those other projects.

## 7. Retrieval references for the main writer

These tool references are for re-opening the sources in the parent session, not a substitute for the final notes and bibliography linked in §1:

- Toën: `turn873914924view0` (Théorème 0.1), `turn873914924view1` (Théorème 4.1 and finite type), `turn873914924view2` (§5 and Corollaire 5.1).
- Horel: `turn548259591view1` (intro and Theorem 5.4), `turn403951859view0` (Theorem 6.1), `turn808217570view0` (Remark 3.11 and derived adjoint), `turn808217570view1` (Remark 8.5), `turn148441417search0` (publisher dates).
- Mandell: `turn403951859view2` (Theorems 0.1–0.2 and non-fullness); `turn670694650view0` (full article).
- Berger–Fresse: `turn864638053view0` (version history), `turn417431680view0` (Theorem 2.1.1), `turn401145399view0` (§2.2.8).
- Borger–Wieland: `turn808217570view2` (§2.14).

