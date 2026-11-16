# MPL 133 — Research notes

## Scope and evidentiary conventions

The report concerns all **50 supplied scan pages** of cote **133**, scans **002–054 except 005, 010, and 041**. The transcription was frozen at **2026-11-16 23:01:08 UTC**, with a SHA-256 for every page and the combined fragment; the context-open event was recorded afterwards, within the same UTC second. Subsequent mathematical findings and proposed alternative interpretations belong only to these notes, including findings that conflict with an apparently clear printed or handwritten assertion.

Source quotations are short cues, not replacements for the diplomatic transcription. An uncertain reading remains uncertain when quoted here; `Laborde|Lazard`, for example, records alternatives and does not identify a speaker. The seven printed Laborde pages are attributed to Laborde, the thesis notices to their issuing university, and neither is silently treated as Grothendieck's own prose.

The supplied context consists only of `README.md`, `notes/RESULTS_STATE.md`, `PURSUING_STACKS_CONTENTS.md`, and the typed PS chapters `ps_chapters_VI_VII/ps6.tex` and `ps7.tex`, with a licence file. It contains no scans or full transcriptions of cotes 136, 137, or 153 and no full underlying result CSVs or Lean developments. References to PS identify the **original page and section**, using its `\pspage{...}` markers; these are not archive scan numbers. Absence statements are bounded to these supplied materials and the fifty transcribed pages.

All notes were checked against the supplied context by object, word, or notation, followed by reading relevant passages. The per-note search record is in `records/context_searches.jsonl`; the research support files preserve calculations, exact literature locators, and version/access limitations. Register statuses are the earlier runs' claims except where the register explicitly records review, and this report does not certify an unseen proof or formalization.

## Answers to the planning questions

| Question | Finding from cote 133 and the supplied context | Main evidence and limits |
|---|---|---|
| What does “Witt” mean here? | **Explicitly quadratic Witt theory** on scans 006–009; the finite-G-set/Burnside construction appears separately on 019–029. | `WG(S)` is a group completion of quadratic bundles and `W(S)` a hyperbolic cokernel; a Witt-vector functor is not constructed on these pages (W01–W09, F01). |
| Are operations on finite G-sets present? | **Yes**, with injection operations, all-map operations, symmetric-group actions, induction, and finite-set endofunctors. | Scans 020–027 supply the constructions, but several literal formulas or asserted equivalences require correction or hypotheses; see F02, F04, F05, and F11. |
| Does cote 133 establish B7, integral homotopy from binomial cochains? | **No reconstruction theorem or space-to-cochain functor is established here**; there is a genuine numerical and operations-theoretic connection. | The strongest supplied historical witness is the later PS §119, original pp. 502–503, which asks for a binomial-cochain quasi-isomorphism, and §120, pp. 506–507, which organizes operations; the modern endpoint is qualified in B07–B08. |
| Does 137 mean strictly commutative cosimplicial algebras? | **Not decidable from this package.** | Cote 137 itself is absent; neither scan 003's associativity pentagon nor scan 028's commutatively ringed topos identifies its construction, and strict cosimplicial commutativity must be distinguished from strict DGA commutativity (W14, B06, B10). |
| Are abelian varieties named? | **Yes**, in the algebraic-group/affine-quotient discussion. | Scans 042–044 explicitly name an abelian scheme/“V.A.,” its Picard scheme and dual; this is an extension-theoretic example, not a cochain reconstruction example. |
| Are Chern classes of a Fourier transform named? | **No such example was found in these fifty pages.** | Scan 004 has `c₁ mod2` and `c₁ ?`, scan 009 has Stiefel–Whitney classes, and 042–044 have abelian varieties; the text does not join them through a Fourier transform (W12, B10 and the formal-group notes). |
| How do the two Hua findings fare? | The centre and derived-subgroup criteria have substantial source support and direct ordinary-group proofs; the affine-quotient claim needs corrections and a genuine family. | The cancelled centre reductions cannot be restored, a two-headed arrow on 054 is not automatic, and scan 044 does not say that positive-characteristic extensions split; the formal-group notes examine both supplied IDs explicitly. |

These answers **sharpen or qualify** the guesses in `README.md`, “What our planning document asks of these folders,” rather than treating those guesses as prior mathematical results. In particular, the named abelian varieties answer an occurrence question for **133** and do not answer the original **136/137** example question in **WG2 §2.4 #5**.


## How to use the notes

There are **76 numbered notes**: W01–W16 on quadratic Witt theory and adjacent calculations; P01–P05 on the printed Laborde offprints; F01–F16 on finite sets and representation rings; B01–B11 on the binomial/cochain comparison; G01–G21 on formal and algebraic groups; J01–J05 on Go; and M01–M02 on reused material. Each numbered item's explanatory body is limited to one to four sentences; source, kind, confidence, context, and register fields are metadata. “Own idea” and “own verification” identify calculations made for this report, with their hypotheses and confidence, without any claim of historical novelty.

Longer checks are in [quadratic proof checks](research/quadratic_proof_checks.md), [finite-set calculations](research/finite_sets.md), and [formal/algebraic-group proofs](research/formal_groups.md). The binomial supplement preserves context-search and source-version details. All context paths are relative to the supplied context archive; those source files are intentionally not reproduced in this package. In particular **PS §137 is a section of Pursuing Stacks, not Montpellier cote 137**.

## Quadratic Witt theory and adjacent calculations


### W01 — unpursued implication — cote 133, scans 006–008: which Witt group?

The explicit definition “groupe enveloppant du monoïde commutatif des classes d'isomorphie” makes `WG(S)` the group completion of strictly nondegenerate quadratic bundles under orthogonal sum, and scan 007 defines `W(S)` as the cokernel of the hyperbolic map from the **split** group `K_s(S)`. This supplies a definite quadratic-form meaning of “Witt,” alongside the separate finite-set operations on scans 019–029; it does not identify either construction with a big Witt-vector functor. **Context comparison:** it **differs from and sharpens** the tentative identification in `README.md`, “What our planning document asks of these folders,” and bears on **WG2 §Week #3** in `notes/RESULTS_STATE.md`; the planning entry is explicitly unchecked.

### W02 — reading question / unpursued implication — cote 133, scans 006–007: split versus exact Grothendieck–Witt groups

The words “en tenant compte des suites exactes courtes” distinguish the manuscript's `K_s(S)` from `K(S)`, and the same caution is needed before replacing its `WG(S)` by a modern Grothendieck–Witt group. Zibrowius's symmetric representation group imposes both orthogonal-sum relations and the relation identifying a metabolic object with the hyperbolic object on its Lagrangian (2015, Definition 1.2, p. 1060), whereas that additional relation is absent from scan 006. **Context comparison:** searches for `hyperbol`, `metabolic`, `Witt`, and `quadratic` find no treatment of this distinction in the supplied context; this note **adds** a definition-level restriction to the `README.md` Witt lead rather than borrowing an established result from `RESULTS_STATE.md`.

### W03 — self-flagged / literature comparison — cote 133, scan 006: the λ-ring question

“Même dans ce cas j'ignore si c'est un λ-anneau” asks for the universal product and iterated-exterior-power identities, and the proposed reduction to `B_{O(m)×O(n)}` anticipates the use of orthogonal representation rings in Zibrowius (2015, Introduction and Theorem, pp. 1055–1057). A modern affirmative result holds for the **usual** Grothendieck–Witt ring of schemes over a field of characteristic different from two (Zibrowius, 2018, Theorem 2), and Fasel and Haution (2025, Theorem 1, p. 128) prove the corresponding λ-ring assertion for `GW^0(X)⊕GW^2(X)` on quasicompact quasiseparated schemes over `Z[1/2]`. These theorems do not by themselves settle the manuscript's group completion on every locally ringed topos, because W02 identifies a difference in relations and the ambient categories differ. **Context comparison:** this **adds** later results to the operations agenda of `ps_chapters_VI_VII/ps6.tex`, §120, original pp. 506–507, and **qualifies**, rather than proves, the unchecked **WG2 §Week #3** research plan.

### W04 — own idea — cote 133, scan 006: why the rank can be even

The assertion “les modules quadratiques str. non. dég. sont de rang pair” has a short proof for a connected scheme with a point of residue characteristic two: the polar form becomes alternating and nondegenerate at that point, so its rank is even, and the rank of a vector bundle is locally constant. **Confidence: high for that stated scheme case**, because nondegenerate alternating forms have even dimension and connectedness propagates the rank; an arbitrary locally ringed topos needs a formulation that supplies an appropriate local test. The manuscript's parenthesis “sans unité en général” also requires care with the convention for λ⁰ when the rank-one unit is unavailable. **Context comparison:** this **adds** a proof and a scope qualification to the `README.md` quadratic-Witt lead; the supplied PS chapters and status register contain no matching parity assertion.

### W05 — own idea — cote 133, scan 007: a counterexample to factoring through exact K₀

For “il n'est pas clair que l'hom. précédent se factorise par K(S),” take `S=P¹_C` and the exact sequence `0→O(−1)→O²→O(1)→0`. The function `[(M,q)]↦dim_C H⁰(P¹,M(−1))` is additive under orthogonal direct sum and hence defines a homomorphism from the manuscript's split `WG(S)` to `Z`, but it is `0` on `H(O²)` and `2` on `H(O(−1))⊕H(O(1))`. Thus the hyperbolic map in the literal scan-006 definition does **not** generally factor through exact-sequence `K₀`; **confidence: high**, because this additive invariant directly separates the two proposed classes without any cancellation theorem. **Context comparison:** the supplied context has no hyperbolic-additivity result, so this **adds a negative answer** to the question underlying its Witt lead and explains why W03 cannot silently substitute the usual Grothendieck–Witt theory.

### W06 — own idea — cote 133, scans 007–008: the affine statement without inverting two

The assertion attributed to “Laborde|Lazard dixit,” that `(M,q)⊕(M,−q)` is hyperbolic over an affine scheme, can be justified for a finite projective nonsingular quadratic module: its diagonal is an isotropic direct summand, and the nonsingular pairing identifies a complementary summand with its dual. A quadratic form on a finite projective module `P` lies in `Sym²(P∨)` and lifts through `P∨⊗P∨→Sym²(P∨)` to a bilinear form; modifying the complement by the corresponding linear map makes it isotropic. **Confidence: high under these algebraic hypotheses**, because this constructs a hyperbolic decomposition without division by two; the needed global bilinear lift explains the role of affineness. **Context comparison:** this **adds** a proof to a point absent from the supplied context, and does not identify the uncertain surname from mathematical expectation.

### W07 — own idea — cote 133, scan 008: an equivariant obstruction at two

The caution “ce n'est pas vrai … [pour] le topos classifiant” has a concrete test over `F₂`: let `C₂` interchange the coordinates of `M=F₂²` with `q(x,y)=xy`, and set `F=(M,q)⊕(M,q)`. Its fixed subspace consists of `((a,a),(b,b))`, on which the quadratic form is `a²+b²`, whereas a hyperbolic `H(E)` with the same four-dimensional representation must have `E` the two-dimensional indecomposable permutation representation and has identically zero quadratic form on its fixed subspace. Therefore `F` is not equivariantly hyperbolic, although it becomes hyperbolic after forgetting the action; **confidence: high**, from the two possible two-dimensional `F₂[C₂]` representations and this fixed-space invariant, without claiming that its class is nonzero in the hyperbolic cokernel. **Context comparison:** this **adds** an explicit obstruction to the general-topos version absent from `README.md`, the PS chapters, and `RESULTS_STATE.md`; it also shows why ordinary affine splitting cannot be used equivariantly without checking descent.

### W08 — self-flagged / own idea — cote 133, scan 008: the λ-operations do not descend to W

The question “passerait-elle au quotient ?” has a negative answer already over `C`: `GW(C)=Z`, the hyperbolic plane has class `2` and vanishes in `W(C)=Z/2`, but its second exterior power has the nonzero rank-one Witt class. Consequently `λ²(2)=1` cannot descend through that quotient; **confidence: high**, since it follows directly from ranks and the classification of nonsingular complex quadratic forms. Zibrowius (2018; checked arXiv v2, 2016, Introduction, p. 2) likewise distinguishes exterior powers on Grothendieck–Witt groups from their failure to descend to Witt groups. **Context comparison:** this **adds a negative answer** to a question absent from the supplied PS discussion of λ- and binomial algebras (§120, pp. 506–507), which concerns a different quotient problem.

### W09 — reading question — cote 133, scan 008: the ideal notation

The live sentence “On voit que α(K(S)) est un idéal” uses `K(S)` after scan 007 has questioned whether `α` even factors through that group. W05 shows why it matters whether the intended expression is the image of `K_s(S)`, or a later quotient in which exact-sequence relations have been imposed; the frozen transcription retains the written `K(S)`. **Context comparison:** no supplied context passage resolves this notation, so this note **adds a reading/definition question** rather than silently repairing the source from modern conventions.

### W10 — withdrawn in the same text — cote 133, scan 009, compared with scan 004

“Un calcul facile montre que w∘α=1” and the proposed factorization through `W(S)` are both struck out on scan 009 and must not be reported as the author's final assertion. The preceding rank-two computation on scan 004, “w₁=α … ∂(−1)” and “c₁ ?,” already points to possible nontrivial characteristic classes of a hyperbolic plane. **Context comparison:** this **adds a documented withdrawal** to the quadratic-Witt lead in `README.md`; no such withdrawal or characteristic-class statement is reproduced in the supplied `RESULTS_STATE.md`.

### W11 — own idea — cote 133, scans 004 and 009: a rank-one-normalization test of the withdrawn claim

On the étale site of `Spec R`, for `R` the real numbers, the hyperbolic plane is isometric to `⟨1,−1⟩`, so rank-one normalization and the Whitney product formula give `w(H(R))=1+∂(−1)≠1`, although its Witt class is zero. **Confidence: high**, because `−1` is not a square in `R` and the nonzero Kummer class is exactly the manuscript's `α`; this is a direct obstruction to the cancelled descent claim. Laborde (1976, §III, p. 50) provides the relevant étale characteristic classes and their normalization and orthogonal-sum properties for schemes where two is invertible. **Context comparison:** the supplied context contains no matching characteristic-class example, so this **adds an explanation** of W10 rather than attributing a reason for the deletion to Grothendieck.

### W12 — own idea — cote 133, scan 004: the Chern-class test

The question “c₁ ?” can be tested with `L=O(1)` on `P¹_C`: analytically the hyperbolic complex quadratic bundle `L⊕L⁻¹` has a real rank-two orthogonal reduction given by the underlying oriented real two-plane bundle of `L`, and the Stiefel–Whitney class of that reduction is `w₂=c₁(L) mod 2≠0`. The underlying real rank-four bundle of the complex vector bundle `L⊕L⁻¹` instead has `w₂=0`, so these two real bundles must be distinguished (Laborde, 1976, §I, p. 47, for orthogonal reduction; Hatcher, 2017, Proposition 3.8, p. 83, for realification). **Confidence: high for this complex example**, from the transition-function reduction to `SO(2)` and the equality of the mod-two Euler class with the second Stiefel–Whitney class; this does not establish the formula for every ringed topos. **Context comparison:** this **adds** a concrete line-bundle example to **WG2 §2.4 #5**, but **differs** from its proposed Fourier-transform example: scan 004 writes a Chern class without mentioning a Fourier transform or an abelian variety.

### W13 — unproved claim / literature comparison — cote 133, scan 009: the surviving universal formulas

The surviving “Les arguments habituels de splitting montrent” concerns universal formulas for tensor and exterior powers in terms of Stiefel–Whitney classes **and ranks**, followed by a proposed λ-homomorphism to `H⁰(S,Z)×(1+Ĥ^{*+}(S,F₂))`. A proof must specify the operations on that target and justify the splitting map's injectivity for the chosen cohomology theory; Laborde (1976, §§II–III, pp. 49–50) establishes the rank-one splitting construction and the Whitney-sum axioms, not the entire displayed λ-ring target. **Context comparison:** this **adds** a characteristic-class realization to the operations program in `ps6.tex`, §120, pp. 506–507, but neither that context nor **WG2 §Week #3** supplies the missing target construction.

### W14 — unpursued implication / evidence limit — cote 133, scan 003: associativity is visible, strict commutativity is not

The parenthesized products, arrow labelled `a`, and pentagon show an associativity/coherence problem for a multiplication `p`, together with an `Ext¹(π₀,π₀,π₀;π₁)` obstruction expression. They do not specify a cosimplicial algebra, a strict commutative multiplication, or a comparison with integral singular cochains. **Context comparison:** this **adds evidence of a coherence problem** beside the general operations in `ps6.tex`, §120, pp. 506–507, but does **not decide** the separate cote-137 hypothesis in `README.md` or the unchecked **WG2 §Week #3** plan.

### W15 — own idea — cote 133, scan 004: a possible abutment for the Ext–Tor display

For the isolated display `E₂^{pq}=Ext_B^p(Tor_q^A(M,B),N)`, the usual interpretation for a commutative ring map `A→B`, an `A`-module `M`, and a `B`-module `N` abuts to `Ext_A^{p+q}(M,N)` by derived tensor–Hom adjunction. **Confidence: high for those ordinary module hypotheses**, using the hyper-Ext spectral sequence for the bounded-above complex `M⊗_A^L B` (Stacks Project, n.d., Tag 07A9, Example 21.32.1); no abutment is written on the leaf. **Context comparison:** this **adds a candidate completion**, kept outside the transcription, to the same derived tensor/Hom formalism in `ps_chapters_VI_VII/ps7.tex`, §136, original pp. 567–568, equations (1)–(2).

### W16 — own idea / contextual correction — cote 133, scans 004 and 007; supplied PS §122

The quadratic-form and splitting questions on these scans invite comparison with `ps6.tex`, §122, original p. 517, equation (18′), where the context claims that `0→V′→Sym²(V′)→Λ²(V′)→0` has no `Aut(V)`-equivariant splitting for `dim V≥2` over `F₂`. At dimension two, however, `q=x²+xy+y²` is invariant under the generators `x↔y` and `x↦x+y, y↦y`, and its polarization is the generator `x∧y`, giving an equivariant splitting for the **finite group** `GL₂(F₂)`. **Confidence: high**, by these explicit substitutions; this does not give a `GL₂` group-scheme splitting or settle dimensions at least three. The comparison thus **contradicts the stated low-dimensional threshold in the supplied context**, not any assertion on the frozen scans, and is not an upgrade or rederivation of a `RESULTS_STATE.md` result.

## The printed Laborde offprints

### P01 — unpursued implication / attribution — cote 133, scans 011–017

“Note … de M. Olivier Laborde” identifies two printed offprints, not handwritten theorems of Grothendieck: the graded Skolem–Noether note occupies scans 011–013, and the quadratic-form/Clifford/signature note scans 014–017. Their presence supports a concrete quadratic-form setting for the cote's title but does not by itself establish which printed claims Grothendieck accepted. **Context comparison:** this **adds bibliographic specificity** to the `README.md` description “tirés à part (1974)” and **differs** from its finite-G-set emphasis; no Laborde theorem is separately registered in `RESULTS_STATE.md`.

### P02 — own idea — cote 133, scan 012, printed p. 448: the even-conjugator claim

The printed Theorem 1 requires “s∈U(A₀),” but under the ordinary superalgebra convention take `A=B=End_Q(Q^{1|1})`, `f=id`, and `g=Ad(S)` with the odd invertible matrix `S=((0,1),(1,0))`. This `g` preserves the grading and exchanges `e₁₁,e₂₂`, whereas every even invertible matrix is diagonal and fixes both idempotents, so no even `s` can conjugate `g` to `f`. **Confidence: high under that explicit grading convention**, since this is the very `END(V)` model used in the printed proof; the parity distinction is retained in Elduque and Villa (2008, §2.2, Proposition 8 and Remark 10; accessed 2007 preprint pp. 4–5). **Context comparison:** this **adds a counterexample to the literal printed claim**, with no matching theorem in the supplied context; it is not a correction to the frozen text or a claim that an erratum has been found.

### P03 — own idea — cote 133, scan 013, printed p. 449: graded tensor cancellation

Theorem 3 says that an isomorphism between `A⊗C` and `B⊗C` implies one between `A` and `B`; under the standard graded tensor product, take `A=C=End_Q(Q^{1|1})` and `B=End_Q(Q^{2|0})`. Both tensor products are graded-isomorphic to `End_Q(Q^{2|2})`, while `dim A₁=2` and `dim B₁=0`, so the factors are not graded-isomorphic. **Confidence: high**, from the elementary identity `End(V)⊗̂End(W)≅End(V⊗̂W)` and the displayed even/odd dimensions; a repair would have to change the cancellation statement or add a hypothesis. **Context comparison:** this **adds a separate counterexample** to the printed offprint, a subject absent from the supplied PS chapters and status register, and does not affect the manuscript's own spelling or theorem statement.

### P04 — reading question — cote 133, scans 012–013: printed index and tensor-factor anomalies

The frozen print readings include `B_i V_i⊂V_{i+j}` on scan 012 and a diagram beginning `B⊗A→A⊗A*` with labels `f⊗1,g⊗1` on scan 013. Standard degree bookkeeping suggests `V_j` in the former and an opposite-algebra factor in the latter, but those are research questions about the printed passage rather than permissions to normalize it. **Context comparison:** the supplied context has no parallel version of these offprints and therefore **adds no independent reading evidence**; P02–P03 show that merely correcting these local symbols would not settle the more substantial parity issues.

### P05 — unpursued implication / convention warning — cote 133, scans 014–017

The second offprint explicitly studies `LW(A)=ker(Witt(A)→BW(A))`, giving signature kernels `(8Z)^r` and the examples “Witt(Z)=8Z” and “Witt(Z[i])=0.” Those examples must be read with its nonsingular **quadratic** convention and its Clifford/Brauer–Wall map, not silently exchanged for a symmetric-bilinear Witt group over a ring where two is not invertible. **Context comparison:** this **adds arithmetic and Clifford examples** absent from the supplied context and **differs** from the tentative finite-set/Witt-vector identification in `README.md`; no Fourier-transform example occurs in these offprints.


## Finite-set operations and representation rings

### F01 — unpursued implication / literature comparison — cote 133, scans 006–009, 020

**Exact cues:** “Groupes de Witt et variantes.” (006); “groupe de Witt” (007); “anneau des $G$-ens. finis virtuels” (020).

The source has two distinct constructions: scans 006–009 concern strictly nondegenerate quadratic modules, their group completion, and a quotient by hyperbolic forms, whereas scan 020 starts the Burnside ring of finite $G$-sets. Dress and Siebeneicher's later relation with Witt **vectors** uses completed Burnside rings and, in the cyclic case, almost finite sets, so it is a pertinent comparison rather than an identification already supplied here (Dress & Siebeneicher, 1986, p. 1; 1988, abstract; 1989, abstract). The exact context relationship is a qualification of `context/README.md`, “What our planning document asks of these folders,” and **WG2 §Week #3**: these pages confirm finite-set operations and a quadratic Witt construction, but do not themselves construct a Witt-vector functor. The $W_2$ extension in `context/ps_chapters_VI_VII/ps6.tex`, VI §119, original p. 501, belongs to the power-series side of this distinction.

### F02 — own idea / counterexample — cote 133, scan 019

**Exact cue:** boxed $2\lambda^2(E)+E=E^2$.

The boxed identity cannot hold in the ordinary Burnside ring, independently of the uncertain $\mathcal P_i$: for the free two-point $C_2$-set $u$, one has $u^2=2u$, so it would require $2\lambda^2(u)=u$, impossible in the free abelian group $\mathbb Z\{1,u\}$. Under the subset interpretation the second operation is $1$, whereas the reciprocal of the symmetric-power series has second coefficient $u-1$, agreeing with the convention used by Bouc and Rökaeus (2009, introduction and Theorem 1.1). **Confidence: high**, because orbit decomposition proves the divisibility obstruction without deciding the uncertain symbol. No matching identity or correction was located in the supplied PS chapters or register; VI §120, original pp. 506–507, is only a general contextual discussion of extra ring operations.

### F03 — own idea / reconstruction of the surviving decomposition — cote 133, scans 020–023

**Exact cues:** “$\operatorname{Mon}(I_n,E\amalg F)$” (021); “$T^n(E)=\operatorname{cl}_n(\operatorname{Hom}(I_n,E))$” (022).

The proof on scan 021 makes the injection interpretation of $\tau^n$ explicit, whereas scan 022 separately defines $T^n$ using all maps; the latter decomposes by the kernel partition of a map. The partition type on scan 023 requires the stabilizer $\prod_i(S_i\wr S_{\alpha_i})$, its action on the set of blocks, and restriction/inflation before induction, as detailed in the finite-set supplement, Appendix C; the simpler induction formula across scans 022–023 is cancelled in the source. **Confidence: high** for this reconstruction on actual finite sets, because it follows by separating maps according to their exact kernel, but it is an editorial reconstruction and not a recovered uncancelled theorem. No specific match was found in `context/ps_chapters_VI_VII/ps6.tex`, `ps7.tex`, or the established register entries; the relationship to VI §120, original pp. 506–507, is only that both organize operations.

### F04 — own idea / counterexample — cote 133, scan 021

**Exact cue:** “polynô- / miale homogène de degré $n$” (the line break is in the frozen file).

For $G=1$, $H=S_n$, and a set of cardinality $r$, the operation is $q^n_{S_n}(r)=\binom rn$, so for $n=2$ it is polynomial of degree two but not homogeneous under ordinary scalar multiplication. This is a precise link to the binomial polynomials discussed in `context/ps_chapters_VI_VII/ps6.tex`, VI §119, original p. 502, and to the binomial-operation discussion in VI §120, original p. 506; it does not establish the cochain comparison asked on original p. 503. **Confidence: high**, since $q^2_{S_2}(1)=0$ and $q^2_{S_2}(2)=1$; an unstated filtration or arity convention could motivate a different use of “homogeneous,” but is not supplied here. This bears on the unchecked **WG2 §Week #3** comparison, rather than settling an existing register theorem.

### F05 — own idea / counterexample — cote 133, scans 024–025

**Exact cues:** “sommes disjointes finies” and “des foncteurs de la forme $H_I$” (025).

The first definition of a special functor includes $h_1\amalg h_1$, but this cannot be a direct summand of any single $H_I$: evaluation at a singleton gives two points on the first side and exactly one point for $H_I=\operatorname{Hom}(I,-)$, whatever the cardinality of $I$. Thus the stated “ou encore” equivalence needs qualification; allowing finite coproducts of the $H_I$ repairs this particular obstruction, while merely taking $I$ larger does not. **Confidence: high**, because the contradiction is an evaluation of finite sets and is independent of the uncertain spelling of “sommants.” No matching special-functor statement was found in the supplied context or RESULTS_STATE register.

### F06 — unpursued implication / literature comparison — cote 133, scans 024, 026

**Exact cues:** “applications injectives” (024); “$\coprod_{n\geq0}\operatorname{Mon}(I_n,E)\mathbin{\wedge}_{\mathfrak S_n}X_n$” (026).

The finite $S_n$-sets $X_n$ are species data, but the displayed extension uses injections into $E$, whereas Joyal's analytic extension uses all maps $I_n\to E$ (Joyal, 1986, Chapter 1, Definition 1, p. 127; Chapter 2, Definition 1, p. 131). In modern language the source formula is the left Kan extension of species along the inclusion of finite bijections into finite injections, and its value is naturally $\coprod_{S\subseteq E}X[S]$, as verified in the finite-set supplement, Appendix D. **Confidence: high** for this coend identification, because the injections with a fixed image form a free $S_n$-torsor; this is a structural comparison, not a claim of historical dependence. No species/FI passage was located in the supplied context files `ps6.tex` or `ps7.tex`, and finite sets with injections should not be identified with the ordered semisimplicial category $\Delta_{\mathrm{inj}}$ merely because both use injections.

### F07 — own idea / scope check — cote 133, scan 026

**Exact cues:** “Sommes disjointes finies” and “où $\forall n$, $X_n$ est un $\mathfrak S_n$-ens. fini”.

The marginal statement is one-way (“Tout foncteur distingué…”), and is correct with finitely supported species data chosen from the finite defining coproduct. Without adding finite support, the displayed formula still has finite values on every finite $E$, since only $n\leq |E|$ contribute, but describes a larger class: $X_n=1$ for every $n$ gives all subsets of $E$ and cardinality $2^{|E|}$, rather than a finite-degree polynomial. **Confidence: high**, because each finite coproduct of $h_I/H$ has polynomial cardinality and cannot equal this exponential sequence. No finite-support convention or matching clarification was found in the supplied context or register, so it should not be silently inserted into the transcription or attributed to the manuscript.

### F08 — unpursued implication — cote 133, scan 026

**Exact cues:** “est dit une équivalence” and “de cardinal $\geq n$”.

Here an equivalence means that a specified natural transformation becomes an isomorphism on every sufficiently large finite set, and the two listed closure properties follow pointwise. No source assertion here identifies this class with a homotopy equivalence class or with a fundamental localizer of small categories. No matching eventual-isomorphism construction was located in the supplied PS chapters; neither **WG H6** nor an unrelated localizer result should be attached as a theorem about these functors.

### F09 — unpursued implication / context comparison — cote 133, scan 027

**Exact cue:** “a des opérations $\amalg,\times,\circ$”.

The explicitly non-full category of injection-preserving endofunctors is equipped with sum, product, and composition, which gives a concrete operations framework. Its closest supplied contextual parallel is `context/ps_chapters_VI_VII/ps6.tex`, VI §120, original pp. 506–507, where the unary ring of an analyzer carries composition and coaddition/comultiplication, but the manuscript does not identify its endofunctor category with that ring or with the integer-valued-polynomial plethory. Consequently this is evidence relevant to the unchecked comparison **WG2 §Week #3**, without resolving the separate claim about cote 153 in `context/README.md`.

### F10 — reading question / notation distinction — cote 133, scans 028–029

**Exact cues:** “$\overset{n}{\bigotimes}E$” (028); “coefficient de $\rho_1^n$” and “coefficient de $\rho_n$” (029).

The symbol $\tau^n$ is now used for a tensor-power class with symmetric-group action, so it should not be conflated with the earlier injection construction merely because the notation agrees. The formula on scan 028 uses monomial symmetric functions expressed in elementary symmetric functions, with the source itself specifying their weighted homogeneity; this differs from ordinary homogeneity in the cardinality variable tested in F04. The closest supplied context is `context/ps_chapters_VI_VII/ps6.tex`, VI §120, original p. 506, which separately names exterior-power and Adams-type operations; no counterpart of the representation-valued formula or its coefficient-independence assertion was located there or in `ps7.tex`.

### F11 — own idea / counterexample — cote 133, scan 029

**Exact cues:** “lin. indép.”; “si $k$ est un anneau local”.

For $k=\mathbb F_2$, the exact-sequence representation Grothendieck group has $\rho_1^2=[\mathbb F_2[S_2]]=2\rho_2$, since the regular two-dimensional module has a trivial submodule and trivial quotient. Thus the claimed independence fails for $X=\operatorname{Spec}\mathbb F_2$, and being local—or even having $K_0(k)=\mathbb Z$—does not make the induction ring polynomial on the $\rho_i$. **Confidence: high** under the exact-sequence $K$-group interpretation used on scan 028 and distinguished from split $K_s$ on scan 007, because the required module and exact sequence are explicit; the argument would not by itself apply to a split representation Green ring. No matching modular representation-ring result was found in the supplied PS chapters or register.

### F12 — unpursued implication / own integral-lattice check — cote 133, scan 029

**Exact cue:** “Pour quels anneaux $k$”.

Over $\mathbb C$, the ordinary induction ring $\bigoplus_n R_{\mathbb C}(S_n)$ is identified by the Frobenius characteristic with the integral symmetric-function ring $\Lambda_{\mathbb Z}=\mathbb Z[h_1,h_2,\ldots]$, sending $\rho_n$ to $h_n$; the integral-lattice check is in the finite-set supplement, Appendix E. This characteristic-zero comparison is compatible with the coefficient extraction on scan 029, while F11 prevents its unrestricted extension to local base rings; **confidence: high for the complex case**, by the Schur-basis and Jacobi–Trudi calculation in the supplement. Kannan et al. (2024, §2.1) explicitly record the induction product, characteristic map, Schur/Specht correspondence, and the image of the trivial representation, using a rational completed convention; Joyal (1986, Chapter 4, §4.1, pp. 145–146) also explicitly assumes characteristic zero for tensor species. No classification of all admissible base rings is supplied by these references or by the local counterexample, and no matching classification was located in the supplied PS context.

### F13 — own idea / obstruction to a proposed splitting — cote 133, scan 028

**Exact cue:** “Si $\xi$ est effectif, s'agit-il d'un” followed by the uncertain words “sommant” and “direct”.

An identity of $K$-classes does not on its own furnish an effective summand or a natural direct-sum decomposition of tensor powers; already the usual symmetric/antisymmetric separation over $\mathbb Z$ encounters a factor of two on mixed tensors. **Confidence: high** for that obstruction, since $e_1\otimes e_2+e_2\otimes e_1$ and $e_1\otimes e_2-e_2\otimes e_1$ span an index-two sublattice of the mixed-tensor plane, but this does not settle every possible interpretation of the manuscript's marginal question. The distinction is between a natural Schur-type splitting and mere equivariant decompositions after choosing bases, some of which do exist. No matching splitting claim was located in the supplied PS chapters or register.

### F14 — own idea / proof of the closure assertions — cote 133, scan 025

**Exact cues:** “les $\varprojlim$ finies”; “le composé de deux foncteurs spéciaux est spécial”.

The closure claims for finite coproducts of the $h_I$ admit direct proofs: $h_I\times h_J$ decomposes into finitely many representables according to the overlap pattern of two injections, and the terminal functor is $h_\varnothing$. Connectedness and Yoneda identify a map from $h_I$ to a finite coproduct of representables with one chosen summand and an injection into $I$, so an equalizer retains either an entire source summand or none, establishing closure under finite limits. Composition similarly decomposes into representables by the finitely many component choices and kernel patterns of the labelled tuples involved, retaining only patterns satisfying the outer injection's distinctness conditions. **Confidence: high**, by these explicit finite decompositions, which do not use the false single-$H_I$ summand equivalence in F05; no matching closure proof was located in the supplied PS chapters or RESULTS_STATE entries, and VI §120, original pp. 506–507, supplies only the broader operations/composition comparison.

### F15 — reading question / grading clarification — cote 133, scan 020

**Exact cue:** “$\tau^1(E)=\operatorname{cl}_0(E)$” (the deleted intervening $E$ remains recorded in the frozen file).

The written index is $0$, although the preceding definition places $\tau^1(E)$ in the degree-one summand $k_1(G)$. Since $S_1$ is trivial there is a canonical identification $k_1(G)\cong k_0(G)$ of underlying groups, which can explain the notation, but the two summands remain distinct in the displayed graded direct sum. Thus this is a grading clarification, not a reason to silently change the frozen index to $1$; neither the supplied context files `ps6.tex` and `ps7.tex` nor any RESULTS_STATE entry supplies evidence about the ink.

### F16 — own idea / register scope check — cote 133, scans 024–026

**Exact cues:** “catégorie des ensembles finis” and “applications injectives” (024); “sommes disjointes finies” (025).

The source category is FI, with automorphism groups $S_n$, whereas the nonempty ordinal-injection category in **PRETOT A.12** and **TOTASPH C.10** has only identity automorphisms, so their registered results are not statements about the category defined here. Likewise **TOTASPH E.6** concerns filtered colimits of representable presheaves, while scan 025 uses finite coproducts: already $h_\varnothing\amalg h_\varnothing$, regarded as a presheaf on $\mathcal E^{\mathrm{op}}$, has a category of elements with two nonempty components and is not a filtered-colimit example of that criterion. **TOTEX2 D.1/D.2** record distinctions between filteredness, exactness, total asphericity, and quasi-filteredness, and serve here only to prevent conflating these properties or importing an ordinal-injection example without checking hypotheses. **Confidence: high** for these boundary checks, from the automorphism groups and disconnected category of elements; the exact context is context/notes/RESULTS_STATE.md, those five IDs, and no identification transferring their claims to these FI functors was located in context/ps_chapters_VI_VII/ps6.tex or ps7.tex.


## Binomial operations and integral homotopy

### B01 — The binomial adjective belongs to the rank target

**Kind:** reading question / scope of the assertion. **Cote/scan:** 133/006. **Frozen cue:** “augmenté vers ‘l'anneau binomial’ $H^0(S,\mathbb Z)$”; “j'ignore si c'est un $\lambda$-anneau”.

Here $WG(S)$ is the group completion of strictly nondegenerate quadratic modules, with an asserted pre-$\lambda$ structure and an augmentation to the binomial ring of locally constant integers. The passage does not assert that $WG(S)$ itself is binomial, and explicitly leaves stronger $\lambda$ identities unresolved. It supplies a connection between rank and operations, not a construction of integral cochains or a confirmation of the claim about cote 137 in **WG2 §Week #3**.

**Context-search metadata:** `binomial`, `lambda`, augmentation-related context: `context/ps_chapters_VI_VII/ps6.tex`, §119, original pp. 502–503; §120, pp. 506–507. — **Differs and adds:** the later text proposes binomial coefficient operations and a cochain comparison; 006 names a binomial augmentation target

### B02 — The finite-set ring is not generally binomial

**Kind:** own idea / elementary obstruction. **Confidence:** high, because the obstruction is an explicit calculation in a free abelian group. **Cote/scan:** 133/019–021. **Frozen cue:** “$k_0(G)$ anneau des $G$-ens. finis virtuels” (020).

For $G=C_2$, write $u$ for its free orbit; decomposition into the two transitive orbit types gives $A(C_2)=\mathbb Z\{1,u\}$ and $u^2=2u$. Thus $u(u-1)=u$ is not divisible by $2$, whereas binomiality requires the falling factorial of order two to be divisible by $2$ (Horel, 2025, Definition 1.1). Consequently, binomial formulas after forgetting a group action do not make the finite-$G$-set ring a binomial ring, and B7 cannot be obtained merely by relabeling the construction in 020. This is a separate consequence of the same $C_2$ example used in F02 to test 019.

**Context-search metadata:** `binomial`, `operations`: `context/ps_chapters_VI_VII/ps6.tex`, §119, p. 502; §120, p. 506. — **Differs:** general finite-$G$-set rings are not the binomial rings contemplated later; the $C_2$ calculation contradicts a proposed identification, not an explicit claim in these PS passages

### B03 — A genuine numerical specialization is available

**Kind:** own idea / structural comparison. **Confidence:** high for the counting identification; no claim of a homotopy-theoretic construction. **Cote/scan:** 133/021, 024, 026. **Frozen cue:** “$q_H^n(x)=q_H\tau^n(x)$” (021); “$\operatorname{Mon}(I,E)/H$” (026).

With trivial $G$ and $H=\mathfrak S_n$, the orbits of injections $I_n\hookrightarrow E$ are exactly the $n$-element subsets of $E$, so the induced cardinality operation is $r\mapsto\binom rn$. This gives a concrete numerical-polynomial comparison with the binomial expressions in *Pursuing Stacks* §119, p. 502. The later passage adds a proposed comparison of cochain complexes on p. 503; that homotopical step does not occur in the cited cote 133 construction.

**Context-search metadata:** `binomial expressions`, `Symbin`, `Maps`: `context/ps_chapters_VI_VII/ps6.tex`, §119, pp. 502–503. — **Repeats the numerical pattern and adds a new task:** falling factorial operations reappear; a quasi-isomorphism question is added

### B04 — Composition is a useful lead, but not yet an identified plethory

**Kind:** own idea / literature comparison. **Confidence:** high for the structural resemblance; identification of the manuscript object with a specific plethory is unproved. **Cote/scan:** 133/024–027. **Frozen cue:** “$\underline{\operatorname{End}}(\mathcal E,\mathcal E)$” and “a des opérations $\amalg,\times,\circ$” (027).

The manuscript object is a category of finite-set endofunctors with disjoint union, product, and substitution, while *Pursuing Stacks* §120, pp. 506–507, explicitly adds the algebra and coaddition/comultiplication data for operations on rings. Borger and Wieland (2005, §§1.1, 1.8, 2.14) formalize a plethory as a monoid for biring composition and describe the binomial quotient of the symmetric-function plethory by $\psi_n=e$ for all $n\geq1$. This is an illuminating modern comparison, but 027 does not itself supply the required decategorification, biring structure, or identification with integer-valued polynomials. Because cote 153 is absent, the more specific planning claim about its “analyseur” remains unverified.

**Context-search metadata:** `analyzer`, `composition`, `Delta`: `context/ps_chapters_VI_VII/ps6.tex`, §120, pp. 506–507. — **Adds and differs:** the later object carries ring-level cooperation data, beyond the finite-injection endofunctor category on 027

### B05 — The strongest supplied bridge is a correction and a new question in 1983

**Kind:** unpursued implication / contextual withdrawal and replacement question. **Cote/scan:** 133/006, 021, 027; the substantive cochain passage is in the supplied later text. **Frozen cue:** “l'anneau binomial” (006). **Context cue:** “The question is whether this is a weak equivalence” (*Pursuing Stacks*, §119, p. 503).

In *Pursuing Stacks* §119, pp. 500–502, Grothendieck withdraws the earlier polynomial/divided-power comparison and exhibits the extension with multiplication on $1+at+bt^2$ modulo $t^3$, whose polynomial splitting would require $P(a+a')-P(a)-P(a')=aa'$. The solution $P(t)=\binom t2+ct$ is not in $\mathbb Z[t]$, motivating integer-valued rational polynomials instead. He then asks whether $\operatorname{Sym}^{\mathrm{bin}}_{\mathbb Z}(L_*^\vee)\to\operatorname{Maps}(L_*,\mathbb Z)$ is a quasi-isomorphism for degreewise finite free $L_*$ with $H_0=0$, possibly also $H_1=0$, suggesting reduction to $K(\mathbb Z,n)$. This is an explicit proposed binomial-cochain bridge in the supplied context, not an established theorem in cote 133 and not evidence that an unspecified construction in cote 137 already has all the needed properties.

**Context-search metadata:** `W_2`, `polynomial`, `weak equivalence`: `context/ps_chapters_VI_VII/ps6.tex`, §119, pp. 500–503. — **Adds:** a counterexample and a replacement conjecture absent from the reviewed cote 133 pages; it contradicts an earlier PS comparison hope, not a binomial-cochain theorem in 133

### B06 — Strict cosimplicial commutativity must be distinguished from strict DGA commutativity

**Kind:** unpursued implication / literature comparison. **Cote/scan:** 133/028–029 as the closest reviewed multiplicative construction. **Frozen cue:** “Sur Topos loc. annelé (commutativement) $X$” (028).

The word “commutativement” here qualifies the ringed topos; the displayed object is built from $K(B_{\mathfrak S_{nX}})$, rather than a cosimplicial cochain algebra of spaces. Degreewise function rings $[n]\mapsto\mathbb Z^{X_n}$ are strictly commutative cosimplicial rings, whereas normalization does not make them strictly commutative integral DGAs preserving all cohomology operations (Horel, 2025, Introduction). Thus the usual strict-DGA obstruction does not refute the proposed reading of cote 137, but neither does 028 confirm that reading.

**Context-search metadata:** `cochain`, `semisimplicial`, `commutative`: `ps6.tex`, §119, p. 503, and §120, pp. 506–507; `context/ps_chapters_VI_VII/ps7.tex`, §134, p. 557. — **Differs:** cochain and schematic-model frameworks appear in the later text; the $K$-theory target on 028 is a different construction

### B07 — A precise modern endpoint for B7

**Kind:** unpursued implication / literature comparison. **Cote/scan:** 133/006, 021; direct historical context in *Pursuing Stacks* §119. **Frozen cue:** “l'anneau binomial” (006).

Horel's model uses quasi-isomorphisms in cosimplicial binomial rings, with realization $\mathbf R\operatorname{Map}(A,\mathbb Z)$; the unit is an equivalence for connected nilpotent finite-type spaces and is Bousfield–Kan $\mathbb Z$-completion for connected finite-type spaces (Horel, 2025, Theorems 3.7, 5.4, 6.1). Proposition 4.2 proves the numerical-cochain comparison for $K(\mathbb Z,n)$, $n\geq1$, closely matching the reduced case proposed on original PS p. 503. The forgetful functor to ordinary cosimplicial rings is fully faithful before localization but not after localization (Remark 3.11). Accordingly, the modern endpoint supports B7 with these hypotheses and this derived category; the manuscript evidence still does not construct the intervening equivalence.

**Context-search metadata:** `Symbin`, `K(\bZ,n)`, `1-connectedness`: `ps6.tex`, §119, p. 503. — **Adds:** modern results answer a precisely delimited later comparison question; no implication back to an unconstructed 133 functor is justified

### B08 — Toën supplies a different, precisely qualified Witt/binomial connection

**Kind:** unpursued implication / literature comparison. **Cote/scan:** 133/006–008, 020–021. **Frozen cues:** “Groupes de Witt et variantes” (006); “hom de groupes” (021).

Toën (2020, Definition 2.1 and Proposition 2.2) identifies the Hilbert group $\mathbb H=\operatorname{Spec}\operatorname{Int}(\mathbb Z)$ with the simultaneous fixed subgroup of all Frobenius maps on big Witt vectors. Corollary 3.4 makes $K(\mathbb H,n)$ the affinization of $K(\mathbb Z,n)$ for $n\geq1$, with the corresponding integral cohomology comparison. Theorem 0.1 concerns simply connected finite-type spaces and gives the homotopy-sheaf formula $\pi_i(X)\otimes\mathbb H$, a functorial retraction on integral points, faithfulness, and injectivity on equivalence classes—not a fully faithful reconstruction theorem. This connection is relevant to the later binomial proposal but does not identify the quadratic-form Witt group of 006 or the graded completed target of 021 with big Witt vectors.

**Context-search metadata:** `W_2`, `binomial`, `polynomial`: `ps6.tex`, §119, pp. 501–503. — **Adds and differs:** later Witt power-series and binomial structures are relevant; 006 defines a quadratic-form group

### B09 — A conditional test of the finite-local-system hunch

**Kind:** own idea / conditional obstruction to the planning inference. **Confidence:** high under the explicitly stated ordinary-local-system interpretation. **Cote/scan:** 133/006–008. **Frozen cue:** “le topos classifiant” (006); “$B_{O(n)}$” (008). **Results-state lead:** **WG H6**, marked unchecked in the supplied index.

If the supplied excerpt's $W_{\mathrm{fd}}(k)$ uses equivalence of ordinary categories of finite-dimensional $k$-local systems, the map $S^2\to *$ belongs to it because both categories are $\operatorname{Vect}_{\mathrm{fd}}(k)$. Nevertheless $H^2(S^2;k)=k$ and $H^2(*;k)=0$, so this map cannot be inverted by a proposed schematization retaining characteristic-zero cohomology; the rationalization property of Toën's affinization gives the same obstruction (Toën, 2020, §1, item 4, pp. 4–5). This challenges that literal interpretation of the identification in WG H6, not its unseen subclaims or a strengthened definition involving derived local systems. The classifying-topos tests for quadratic-module operations on 006–008 do not supply such a strengthening.

**Context-search metadata:** `local systems`, `localiz`, `locally constant`, `Postnikov`: `ps6.tex`, §110, original pp. 443–444. — **Differs and adds a necessary distinction:** the PS passage separates the fundamental-group stage from higher Postnikov stages and their cohomology; it does not state the localizer characterization in WG H6

### B10 — Keep the cote 136/137 application question open

**Kind:** reading question / results-state reconciliation. **Cote/scan:** 133/009, 028–029. **Frozen cue:** “classes de Stiefel Whitney” (009); “$K(X,*)$” (028).

The reviewed characteristic-class and $K$-theory passages do not provide an example involving the Chern classes of a Fourier transform on an abelian variety, so they cannot answer the question indexed as **WG2 §2.4 #5** about cotes 136–137. The entries **MPL_136_047-094 §2**, **MPL_136_189-234 §2**, **MPL_136_095-141 L06**, and **MPL_136_235-281 §86** point toward cochain constructions and literature comparisons, but the supplied index expressly treats these as first-pass leads. In particular, an additive or weightwise truncated comparison in such a lead is not yet evidence for a strictly commutative cosimplicial algebra or the derived binomial reconstruction in B07.

**Context-search metadata:** `Fourier`, `Chern`, `De Rham`, `cochain`: `ps6.tex`, §119, pp. 502–503; `ps7.tex`, §134, p. 557. — **Differs:** these are general linearization/comparison discussions, not the requested abelian-variety/Fourier example; the unchecked index entries cannot fill that evidentiary gap

### B11 — A literal overstatement about the binomial basis

**Kind:** own idea / contextual correction. **Confidence:** high, by the polynomial definition and a cardinality argument. **Cote/scan:** 133/006, 021. **Frozen cues:** “l'anneau binomial” (006); “$q_H^n(x)=q_H\tau^n(x)$” (021).

The numerical specialization on scan 021 invites comparison with the claim in `ps_chapters_VI_VII/ps6.tex`, §119, original p. 502, that binomial expressions form a basis of “all integer-valued functions on $\mathbb Z$”. Taken literally this is false: their finite integral linear combinations are polynomial functions and form a countable set, whereas all functions $\mathbb Z\to\mathbb Z$ form an uncountable set. The definition of $\operatorname{Sym}^{\mathrm{bin}}$ on original p. 503 supplies the intended polynomial setting. This **contradicts only the overbroad contextual wording**, adding a scope correction to the unchecked **WG2 §Week #3** comparison, without altering any transcription.

**Context-search metadata:** `integer-valued`, `binomial`, `Symbin`, `all.*functions`: `ps6.tex`, §119, original pp. 502–503. — **Contradicts the literal wording and clarifies the scope:** binomial polynomials span integer-valued polynomial functions, not all functions


## Formal groups, affinization, and crossed modules

The checks distinguish the manuscript's **largest affine quotient** from the Chevalley affine **subgroup**. For the ordinary-group calculations, write $N\triangleleft G$, $N'\leq Z(G)$, $C=N\cap N'=\pi_1$, $Q=G/NN'=\pi_0$, $M=G/N'$, $M'=G/N$, and $K=G/C$; conjugation gives $\theta:M\to\operatorname{Aut}(N)$. The derived-subgroup notes G18–G21 additionally assume $G'\subseteq N$, so $Q$ is abelian; the prime in the manuscript's $M'$ names a second quotient and does not mean the derived subgroup of $M$.

### G01 — The first splitting assertion needs its formal category

**Kind:** own idea / conditional counterexample.  
**Source:** 133, scan 036.  
**Exact cue:** “Extension d'un \(p\)-divisible par un lisse”.  
**Note:** If “p-divisible” means an arbitrary Barsotti–Tate fppf sheaf over a characteristic-p field, the unrestricted splitting assertion fails: Mazur and Messing (1974, I §1.8) give \(\operatorname{Ext}^1(P,\mathbb G_a)\simeq\operatorname{Hom}(\omega_{P^D},\mathcal O)\), which need not vanish. The formal-group supplement, Appendix D makes this explicit for \(P=\mathbb Q_p/\mathbb Z_p\), without identifying the manuscript's intended formal category or deciding its a-torique variant. This differs from the formal/schematic comparison in ps6.tex, §117, PS pp. 494–496, which itself warns against interchanging those categories.  
**Confidence and reason:** high for the conditional modern-category diagnostic, by direct construction; unresolved for the manuscript's intended scope  
**Register:** background qualification for **Hua: 133-centre-and-derived-group-from-two-crossed-modules**, not a verification of its formal-group assertions  

### G02 — Unipotence remains a question

**Kind:** self-flagged / unproved claim.  
**Source:** 133, scans 036–038.  
**Exact cues:** “annulé par une puiss. de \(p\)”; “Question \(DG\cap Z(G)\) est-il”; “unipotent ?”.  
**Note:** Scan 036 distinguishes the proposed p-power-torsion conclusion from the stronger unipotence question, and scan 038 retains a question mark for \((\operatorname{Dér}G)_{\mathrm{ab}}\). Neither the anti-affine classification nor the ordinary-group tests below prove these formal assertions, the proposed maximal a-torique subgroup, its base-change properties, or algebraizability after isogeny. This adds specific centre/derived-group questions to ps6.tex, §113, PS pp. 468–469; §117, PS pp. 494–496, supports retaining the categorical qualification.  
**Confidence and reason:** high as an observation of explicit qualifications; no resolution claimed  
**Register:** limits what is verified in **Hua: 133-centre-and-derived-group-from-two-crossed-modules**  

### G03 — Completion and algebraization are separate inputs

**Kind:** reading question / unproved claim.  
**Source:** 133, scan 039, with 036–038.  
**Exact cue:** “extension centrale de \(\widehat H\) par \(\mathfrak z\)”.  
**Note:** The construction asks for a central extension of the completion of a smooth connected linear algebraic group by a commutative formal group. A finite-type algebraic-group structure theorem does not by itself algebraize that extension, identify its proposed divisible part, or establish the earlier unipotence assertions. This adds an extension problem to ps6.tex, §117, PS pp. 494–496, whose distinction between schemes and completions supports keeping those questions separate.  
**Confidence and reason:** high for the evidence boundary; no algebraization theorem asserted  
**Register:** related background to **Hua: 133-centre-and-derived-group-from-two-crossed-modules**; no formal-group theorem established

### G04 — The cocycle calculation has an explicit PS analogue

**Kind:** unpursued implication / context comparison.  
**Source:** 133, scan 040.  
**Exact cue:** \(\Psi(x+y)-\Psi(x)-\Psi(y)=\varphi(x,y)\).  
**Note:** This is a coboundary equation for a chosen additive-coordinate cocycle, so the allowed functions \(\Psi\) matter. The same mechanism appears in ps6.tex, §119, PS pp. 501–502, through \(P(a+a')=P(a)+P(a')+aa'\), whose rational solutions do not supply an integral polynomial splitting. It does not identify cohomology computed with formal series, polynomial cochains, and discrete group cochains; §117, PS p. 495, explicitly separates the first two already in degree one.  
**Confidence and reason:** high, from the displayed equations and stated coefficient restrictions  
**Register:** conceptual background only  

### G05 — Affine quotient and affine subgroup use different conventions

**Kind:** reading question / literature comparison.  
**Source:** 133, scan 042.  
**Exact cue:** “le plus grand quotient affine de \(G\)”.  
**Note:** The manuscript's \(M=G_{\mathrm{aff}}\) is the affinization quotient \(G/G_{\mathrm{ant}}\), whereas Brion uses \(G_{\mathrm{aff}}\) for the affine subgroup in the Chevalley sequence. The central anti-affine kernel and the smooth/perfect-field qualifications match Brion (2016, Theorems 1–2 and §5.1). No matching Chevalley or anti-affine classification was found in the supplied PS chapters; ps6.tex, §117, PS pp. 494–496, discusses a different formal/schematic distinction.  
**Confidence and reason:** high; the manuscript defines its quotient notation explicitly  
**Register:** prerequisite for **Hua: 133-affine-quotient-not-constructible**  

### G06 — The central-product reconstruction is checkable

**Kind:** own idea / verification.  
**Source:** 133, scan 042.  
**Exact cue:** \(G=Z.L\).  
**Note:** With \(Z=G_{\mathrm{ant}}\), \(L\) the Chevalley affine subgroup, and \(\mathfrak z=L\cap Z\), multiplication gives \(G\simeq(L\times Z)/\{(u,u^{-1}):u\in\mathfrak z\}\), verifying the reconstruction once the extensions and embeddings are fixed. This is an application of the Rosenlicht decomposition under the smooth connected perfect-field hypotheses (Brion, 2016, Theorem 5.1.1). It adds a finite-type algebraic-group construction beyond ps6.tex, §113, PS pp. 468–469, and §117, PS pp. 494–496.  
**Confidence and reason:** high; multiplication is onto and its kernel is the displayed antidiagonal intersection  
**Register:** structural background for **Hua: 133-affine-quotient-not-constructible**; no novelty claim

### G07 — Characteristic-zero injectivity has a dual-space qualification

**Kind:** reading question / literature comparison.  
**Source:** 133, scan 043.  
**Exact cue:** “Il faut \(\varphi_0\) injectif, \(\varphi_1\) injectif”.  
**Note:** The modern characteristic-zero vector test uses \(U^*\hookrightarrow H^1(A,\mathcal O_A)\), and the torus test uses an injective character-lattice map to \(A^\vee\) (Brion, 2009, Propositions 2.1 and 2.3). Scan 043 calls \(t\) the tangent space, so the convention for \(W(t)\) and its Cartier dual needs checking before identifying the displayed map with the modern one. These classification data add to, rather than repeat, ps6.tex, §117, PS pp. 494–496.  
**Confidence and reason:** high for the literature tests; the handwritten variance convention remains unresolved  
**Register:** supports the characteristic-zero premise of **Hua: 133-affine-quotient-not-constructible**  

### G08 — Finite unipotent intersections do not contradict semi-abelianity

**Kind:** own idea / distinction between subgroup objects.  
**Source:** 133, scan 043.  
**Exact cue:** “\(\mathfrak z_u\) est fini”.  
**Note:** Positive-characteristic anti-affine groups are semi-abelian, but \(\mathfrak z=L\cap Z\) is not necessarily the smooth affine part of \(Z\) (Brion, 2009, Propositions 2.2 and 3.1(ii)). A finite possibly non-smooth unipotent part of this intersection therefore does not contradict that theorem. This adds a distinction absent from the unipotent-bundle discussion of ps6.tex, §117, PS pp. 494–496.  
**Confidence and reason:** high; the subgroup objects differ and the intersection quotient is only finite  
**Register:** qualification for **Hua: 133-affine-quotient-not-constructible**  

### G09 — The general Cartier-dual formulation is not fully checked

**Kind:** unproved claim / scope question.  
**Source:** 133, scans 042–044.  
**Exact cue:** \(\operatorname{Ext}^1(A,\mathfrak z)=\operatorname{Hom}(D(\mathfrak z),\underline{\operatorname{Pic}}_{A/k})\).  
**Note:** The torus and characteristic-zero vector checks do not alone establish this formula for every affine commutative group scheme or the universal existence assertion at the top of scan 044. A general statement must specify the formal/fppf category for the dual, Hom, and Picard functors. This differs from the more restricted coefficient discussions in ps6.tex, §115, PS pp. 482 and 488, and §117, PS pp. 494–496.  
**Confidence and reason:** high for this limitation; no general duality assertion refuted  
**Register:** an unchecked surrounding assertion, unnecessary for the concrete families below  

### G10 — Preserve the “groupe affine” inconsistency

**Kind:** reading question.  
**Source:** 133, scan 044.  
**Exact cue:** “groupe affine lisse à fibres connexes sur base \(S\)”.  
**Note:** Literally, an affine group is its own largest affine quotient, whereas the next example is a nontrivial extension of an abelian scheme by \(\mathbb G_a\). This internal hypothesis/reading inconsistency belongs in the research notes and does not authorize changing the frozen word “affine”. The constructibility passage in ps7.tex, §137, PS p. 577, concerns sheaf operations and does not resolve it.  
**Confidence and reason:** high conditional on the frozen reading; no replacement word supplied  
**Register:** **Hua: 133-affine-quotient-not-constructible** omits this wording issue  

### G11 — An infinite-prime family proves the intended nonconstructibility

**Kind:** own idea / family construction.  
**Source:** 133, scan 044.  
**Exact cue:** “constructible en général”.  
**Note:** For \(A:y^2=x^3-x\) over \(S=\operatorname{Spec}\mathbb Z[1/2]\), its universal vector extension has affine-quotient dimension zero at the generic point and one at every closed point, as proved in the formal-group supplement, Appendix B. The generic singleton is not constructible, since every constructible subset containing it contains a nonempty open, and every such open contains closed points. A single DVR specialization would not prove this, and ps7.tex, §137, PS p. 577, concerns a different sheaf-theoretic constructibility question.  
**Confidence and reason:** high; arbitrary-base existence/base change and an explicit infinite-prime topological argument are given  
**Register:** verifies a precise intended form of **Hua: 133-affine-quotient-not-constructible**, subject to G10  

### G12 — Affine quotient \(\mathbb G_a\) does not mean split extension

**Kind:** own idea / correction of the supplied register gloss.  
**Source:** 133, scan 044.  
**Exact cue:** \((G_s)_{\mathrm{aff}}\simeq G_a\).  
**Note:** Hua's supplied summary adds a trivial special-fibre extension, whereas the manuscript only asserts the displayed affine quotient. The universal-extension family can remain nonsplit in every fibre; splitting after pullback by \([p]\) is different (Mazur & Messing, 1974, I §§1.9–1.10; Brion, 2009, Remark 2.4). This adds a quotient-versus-extension distinction to the splitting example in ps6.tex, §119, PS pp. 501–502.  
**Confidence and reason:** high; the universal class remains a nonzero identity after base change  
**Register:** differs from the supplied wording of **Hua: 133-affine-quotient-not-constructible**; no unseen full Hua proof assessed  

### G13 — The blanket equal-characteristic claim has a counterexample

**Kind:** own idea / counterexample.  
**Source:** 133, scan 044.  
**Exact cues:** “en égalis. car.”; “constructible”.  
**Note:** For a fixed complex elliptic curve \(A\), the Poincaré \(\mathbb G_m\)-extension over \(S=A^\vee\) has fibrewise affine quotient \(\mathbb G_m\) at torsion parameters and \(1\) at nontorsion parameters. The infinite torsion locus on a complex elliptic curve is not constructible, so this refutes the blanket equal-characteristic assertion under the intended non-affine interpretation illustrated in the paragraph; it does not refute the tautological statement for literally affine \(G\). The formal-group supplement, Appendix B verifies the family and computes its functions, while ps7.tex, §137, PS p. 577, concerns sheaf constructibility and supplies no matching claim.  
**Confidence and reason:** high; the Poincaré biextension gives a genuine smooth connected family, and the calculation reduces to powers of a degree-zero line bundle  
**Register:** a further qualification to **Hua: 133-affine-quotient-not-constructible**, whose summary addresses mixed characteristic only  

### G14 — The \(H^3/H^2\) pattern requires compatible classes

**Kind:** unpursued implication / literature comparison.  
**Source:** 133, scans 036 and 046.  
**Exact cues:** “indétermination dans \(H^2(\pi_0,\pi_1)\)”; “Obstruction dans \(H^3(B_{\pi_0}/X,\pi_1)\)”.  
**Note:** For ordinary crossed modules with fixed homotopy groups and action, their Postnikov \(H^3\) classes must agree; compatible equivalences modulo 2-isomorphism then have the \(H^2\) ambiguity expressed by normalized cochains (Baez & Lauda, 2004, Theorem 43 and Corollary 44). Reversible butterflies provide the corresponding modern comparison (Aldrovandi & Noohi, 2009, Definition 4.1.5, Theorem 4.2.1, Lemma 5.2.1). This repeats the obstruction-theoretic direction of ps6.tex, §115, PS pp. 482 and 488, but does not replace its relative/quasi-coherent coefficients with discrete coefficients.  
**Confidence and reason:** high for ordinary groups with fixed data; relative representability unchecked  
**Register:** exact hypothesis qualification for **Hua: 133-centre-and-derived-group-from-two-crossed-modules**  

### G15 — The corrected centre test holds for ordinary groups

**Kind:** own idea / verification.  
**Source:** 133, scan 047.  
**Exact cues:** \(\operatorname{Cent}(K)/(N'/\pi_1)\); “\(\psi_G\) injectif”.  
**Note:** For \(N\triangleleft G\), \(N'\le Z(G)\), \(C=N\cap N'\), and \(Q=G/NN'\), put \(\zeta=\operatorname{im}(Z(G/C)\to G/N')\cap\ker\theta\), where \(\theta:G/N'\to\operatorname{Aut}(N)\) is conjugation; commutators give \(\ker(\psi:\zeta\to\operatorname{Hom}(Q,C))=Z(G)/N'\). Hence the injectivity criterion is correct, and the inserted \(Z(K)\) matters before additionally imposing \(G'\subseteq N\). This adds a centre test to ps6.tex, §113, PS pp. 468–469; the formal-group supplement, Appendix C gives a proof and a counterexample to the uncorrected formula.  
**Confidence and reason:** high; lift independence and the kernel are checked directly  
**Register:** ordinary-group verification of the centre portion of **Hua: 133-centre-and-derived-group-from-two-crossed-modules**  

### G16 — The nonabelian and sign warnings are substantive

**Kind:** self-flagged / own verification.  
**Source:** 133, scan 049.  
**Exact cues:** “on suppose \(\pi_0\) commutatif ?!”; “au signe près”.  
**Note:** A central extension of an abelian \(Q\) gives an alternating commutator pairing \(Q\times Q\to C\), but for nonabelian \(Q\) a general commutator need not lie in \(C\). Restriction to \(Z(Q)\times Q\), as the marginal repair proposes for the image of \(\zeta\), is well-defined, and reversing the pairing order changes the sign. This matches the convention \([a,b]=aba^{-1}b^{-1}\) in ps6.tex, §113, PS p. 468, while adding the necessary extension hypotheses.  
**Confidence and reason:** high, by projection to \(Q\) and centrality of the kernel  
**Register:** qualification of the twisting formula in **Hua: 133-centre-and-derived-group-from-two-crossed-modules**  

### G17 — The cancelled reduction must stay cancelled

**Kind:** withdrawn in the same text / own counterexample.  
**Source:** 133, scans 049–052.  
**Exact cues:** “(annulé!)”; “annulé” (the following question mark is uncertain in the frozen text).  
**Note:** The proposed preliminary condition \(N'=Z(H)\), \(H=NN'\), is not necessary for \(N'=Z(G)\): take \(G=S_3\), \(N=A_3=G'\), and \(N'=1\), so \(Z(G)=1\) but \(Z(H)=A_3\). This supports preserving the cancellations rather than adding the withdrawn reduction to the live scan-047 criterion. It adds a test case beyond ps6.tex, §113, PS pp. 468–469, without suggesting that the subsequent derived-group argument was also cancelled.  
**Confidence and reason:** high; every subgroup is directly computable  
**Register:** prevents overstatement of **Hua: 133-centre-and-derived-group-from-two-crossed-modules**  

### G18 — Derived surjectivity is an ordinary-group identity

**Kind:** own idea / verification.  
**Source:** 133, scans 052–053.  
**Exact cue:** \(N/DG\simeq\eta/\lambda_G(\pi_0\otimes\pi_0)\).  
**Note:** Under \(G'\subseteq N\triangleleft G\) and \(N'\le Z(G)\), with \(Q=G/NN'\), \(N_0=[G,N]\), \(\eta=N/[G,N]\), and the image of the commutator map \(\lambda:Q\otimes Q\to\eta\) is \(G'/[G,N]\). Thus the displayed cokernel identity and the criterion \(N=G'\iff\lambda\) onto hold, with alternation allowing factorization through \(\bigwedge^2 Q\). This adds an explicit quotient calculation to ps6.tex, §113, PS pp. 468–469, without requiring the formal-group assertions of scans 036–038.  
**Confidence and reason:** high; the image is generated by exactly the defining commutators of \(G'\)  
**Register:** ordinary-group verification of the derived portion of **Hua: 133-centre-and-derived-group-from-two-crossed-modules**  

### G19 — The equivalences marked “Vérifier” hold in this setting

**Kind:** own idea / verification.  
**Source:** 133, scan 054.  
**Exact cues:** “que \(dN=DM\)”; “Vérifier”.  
**Note:** With G18's hypotheses and \(C=N\cap N'\), surjectivity of \(\lambda_0:Q\otimes Q\to N/(C[G,N])\) is equivalent to \(N=G'C\), hence to \(N/C=(G/C)'\), and also to \(dN=(G/N')'\). The last step intersects \(NN'=G'N'\) with \(N\), using \(G'\subseteq N\). This verifies the flagged ordinary-group calculation and adds it to ps6.tex, §113, PS pp. 468–469, without removing the frozen “Vérifier”.  
**Confidence and reason:** high; the formal-group supplement, Appendix C gives the quotient and intersection steps  
**Register:** precise verification within **Hua: 133-centre-and-derived-group-from-two-crossed-modules**, not a blanket group-scheme theorem  

### G20 — The residual epimorphism is not automatic

**Kind:** own idea / counterexample to automatic surjectivity.  
**Source:** 133, scan 054.  
**Exact cues:** \(\overline\lambda_G:P\twoheadrightarrow\); “est un épi”.  
**Note:** Once \(\lambda_0\) is onto, the remaining condition is genuinely \(\lambda(P)=C_*\), where \(P=\ker\lambda_0\) and \(C_*=\operatorname{im}(C\to\eta)\); the earlier two-headed arrow does not prove it. For \(G=C_p\times C_p\), \(N=N'=C_p\times1\), \(\lambda_0\) is onto zero but the residual map is zero into nonzero \(C_*\). This adds a check beyond ps6.tex, §113, PS pp. 468–469, and agrees with the manuscript's explicit condition c).  
**Confidence and reason:** high; both example and cokernel identity are elementary  
**Register:** preserves the remaining condition in **Hua: 133-centre-and-derived-group-from-two-crossed-modules**  

### G21 — Commutative twists are invisible to these tests

**Kind:** own idea / consequence.  
**Source:** 133, scans 049 and 053–054.  
**Exact cue:** \(\lambda_{G_1}=\lambda_G+\beta c_E\).  
**Note:** With the fixed quotient/action data and hypotheses of G15/G18, twisting by a central extension changes the tests by the stated images of \(c_E\), so a commutative extension has \(c_E=0\) and changes neither centre injectivity nor derived surjectivity. This does not assert that the reconstructed groups are isomorphic. It adds a limitation of the tests to the central-extension discussion of ps6.tex, §119, PS pp. 501–502.  
**Confidence and reason:** high; commutators add in the fibre product and antidiagonal quotient  
**Register:** consequence within **Hua: 133-centre-and-derived-group-from-two-crossed-modules**; no new status claim


## Go calculations and reused material



### J01 — own idea — cote 133, scan 030: a check of the scoring identity

From the written “N=P+Q,” “N′=P′+Q′,” and “ε=N−N′,” elementary subtraction gives `Q′−Q=P−P′−ε`, and therefore `D=2(P+T)−v²−ε` under the leaf's complete partition `P+P′+T+T′=v²`. **Confidence: high**, since this is a formal consequence of the displayed definitions, and it supports the minus-sign alternative in the existing doubt without changing that reading. **Context comparison:** searches for Go, goban/go-ban, prisoners, territory, and the scoring notation find no comparable discussion in the supplied context, so this **adds an independent arithmetic check**, with no relevant `RESULTS_STATE.md` ID.

### J02 — own idea — cote 133, scan 030: the partition assumption matters

The boxed equality “P+P′+T+T′=v²” assumes that every empty intersection is assigned to one player's territory. If `U` intersections are unassigned while the remaining definitions stay unchanged, the same calculation instead gives `D=2(P+T)+U−v²−ε`; **confidence: high**, by replacing the partition equality with `P+P′+T+T′+U=v²`. **Context comparison:** this **adds a hypothesis check** to a topic absent from the supplied context, rather than claiming that the manuscript uses any present-day scoring rules.

### J03 — self-flagged / unproved claim — cote 133, scans 031 and 034

The question “est-elle indépendante de la suite du jeu?” on scan 031 asks whether the last-move parameter `ε` is forced by a position, while scan 034 later asserts a rule using the inequalities between `t−2ρ` and `t′−2ρ′`. That later rule is not proved here: it needs a precise account of which subsequent moves preserve the supposedly fixed territorial decomposition and when a move can alter the number of groups or eyes. **Context comparison:** the supplied context contains no Go argument, so these leaves **add an unresolved dependence question and a proposed answer**, with no established result in the status register settling it.

### J04 — unproved claim — cote 133, scans 032–033: completion of the rules

“Cas du ‘Ko’ cf plus bas” and the prohibition on skipping a turn leave a proof obligation about legal moves, repetition, and termination, because these five supplied Go leaves do not state a complete repetition rule. The claim that filling an eye lets the opponent capture “de proche en proche … tous les pions de A” also requires a global argument beyond the local capture immediately described. **Context comparison:** this **adds a missing-definition and proof question** on a topic absent from the supplied PS chapters, README research targets, and `RESULTS_STATE.md`; it does not replace the handwritten rules with a modern rule set.

### J05 — withdrawn in the same text — cote 133, scan 034

“Si blanc joue dernier … chacun exactement 2 yeux, donc T′=2ρ′” is cancelled, whereas the two subsequent inequalities remain live. The cancellation must be preserved when assessing the proposed last-move criterion: the exact-two-eyes assertion is not an available lemma for it. **Context comparison:** this **adds a source-state qualification** absent from the supplied context; no prior result is being contradicted or independently rederived.

### M01 — own idea / provenance — cote 133, scans 048 and 050

The reused notices are dated “19 juin 1975” and “5 Juin 1975” and concern, respectively, Marie Marteau's animal-biology thesis and Marc Nanard's applied-mathematics thesis. **Confidence: high** that these are printed document dates, but only **medium** that they provide termini post quos for particular handwritten leaves, because a front/back or reuse relation must be established from the physical archive rather than inferred from adjacent scan numbers alone. **Context comparison:** this **adds dated material evidence** consistent with the broad `README.md` catalogue description “1974-[à partir de 1975]”; it does not date every mathematical passage in the cote.

### M02 — reading question / provenance — cote 133, scan 018

The mathematical header `K_n(…)=K(…×…)` is written over a reused computer listing whose faint middle columns remain the least recoverable printed material in this package. The listing's job number and surviving strings do not establish an algorithm for the finite-set constructions on the following leaves. **Context comparison:** the supplied context contains no parallel listing, so this **adds a provenance and legibility limit** without inventing a mathematical relation or discarding the nonmathematical text.


## Standing register I: steps explicitly questioned, qualified, or withdrawn

The table records authorial question marks and verbal qualifications separately from a transcriber's doubt marks. It also includes explicitly advertised proof obligations and withdrawn shortcuts; a phrase such as “il est bien connu” is labelled an unproved claim rather than misreported as an admission of doubt. The longer notes explain the mathematical status.

| Cote / scan | Author's words or marked expression | State and research issue |
|---|---|---|
| 133 / 004 | “Je dis que”; `w₂ … c₁ mod2`; `c₁ ?` | Assertion followed by an explicit question at the rank-two calculation; the equality/relation sign itself remains uncertain in the transcription (W12). |
| 133 / 006 | “j'ignore si c'est un λ-anneau (et pas seulement un pré-λ-anneau)” | Explicit uncertainty about both universal product and iterated-operation identities (W02–W03). |
| 133 / 007 | “il n'est pas clair que l'hom. précédent se factorise par K(S)” | Explicit doubt about exact-sequence relations, resolved negatively for the literal split group by W05. |
| 133 / 007 | “il n'est pas clair si on a φ(E)=φ(E′)+φ(E″)” | The nonsplit-extension version of the same question; “non splittée” is an insertion (W05). |
| 133 / 008 | “paraît (Laborde\|Lazard dixit)” | Reported assertion about affine hyperbolicity without inverting two; attribution remains uncertain (W06–W07). |
| 133 / 008 | “à vérifier” | Marginal check at the proposed direct construction of the Witt equivalence relation with hyperbolic stabilization. |
| 133 / 008 | “et si on dispose d'un ‘th de Witt’” | Explicit additional hypothesis before cancelling a hyperbolic summand; not an unconditional cancellation theorem. |
| 133 / 008 | “passerait-elle au quotient ?” | Explicit question about descending the pre-λ structure; W08 supplies a negative field example. |
| 133 / 009 | “Un calcul facile montre que w∘α=1” | **Deleted**, together with the factorization through `W(S)` and the splitting margin; W10–W11 keep the withdrawal explicit. |
| 133 / 009 | “Les arguments habituels de splitting montrent” | Surviving unexpanded argument for characteristic-class formulas; the target λ structure still needs definition (W13). |
| 133 / 015, printed p. 1600 | “On vérifie sans peine à l'aide de la s. e.” | Laborde's printed claim about the Brauer two-torsion term; this is not a handwritten admission of uncertainty by Grothendieck. |
| 133 / 019 | `λ^i(xy)= ?` | Explicit blank product-law question after the boxed λ/symmetric-power calculations (F02). |
| 133 / 021 | “polynômiale homogène de degré n” | Unproved asserted homogeneity; ordinary scaling fails in the trivial-group numerical specialization (F04). |
| 133 / 022–023 | Induction expression with `φ`, inside `\deleted{…}` | A proposed reconstruction of the all-map operation is withdrawn; the surviving kernel-partition count is a different piece of evidence (F03). |
| 133 / 028 | “Si ξ est effectif, s'agit-il d'un …”; “sommant direct?”; “H. Weyl — ξ?” | Explicit effectivity/direct-summand question; several words and the last symbol remain uncertain (F13). |
| 133 / 029 | “Il est facile [sans doute] de vérifier”; “lin. indép.” | Unexpanded expectation about coefficient independence, with “sans doute” itself an uncertain reading; F11 gives an exact-K₀ obstruction. |
| 133 / 029 | “Pour quels anneaux k”; “Est-ce vrai si k est un anneau local” | Explicit classification question and proposed sufficient hypothesis; locality does not suffice for exact representation K₀ (F11–F12). |
| 133 / 031 | Marginal `?`; “est-elle indépendante de la suite du jeu?” | Question about the final-move parameter and its proposed compensation (J03). |
| 133 / 032–033 | “Cas du ‘Ko’ cf plus bas”; “de proche en proche … tous les pions de A” | Promised rule and unexpanded global capture argument; no complete repetition rule is given on the supplied Go leaves (J04). |
| 133 / 034 | “Si blanc joue dernier … exactement 2 yeux” | **Deleted**; the subsequent last-move inequalities remain live and unproved (J03, J05). |
| 133 / 036 | “à isogén. près du moins…”; “G (lisse) est … (isogénie) … ?” | Qualification of a splitting assertion and an explicitly questioned structure consequence. |
| 133 / 036 | “Question DG∩Z(G) est-il … unipotent … ?” | Explicit strengthening sought beyond quasi-unipotence; surrounding terminology and some words remain uncertain. |
| 133 / 036 | “Traiter cas π₀ p-divisible”; “Dire quels sont les L₁→L₀ possibles”; “Condition pour que G soit linéaire” | Tasks still to be carried out; the reconstruction diagrams do not discharge them. |
| 133 / 037 | “on doit avoir”; “En fait, on doit avoir mieux … Cent(D₀) unipotent” | Expectation of a stronger unipotence conclusion beyond the boxed quasi-unipotence statement. |
| 133 / 038 | `(Dér G)_ab unipotent ?` followed by “voire\|quasi fini” | Explicit question and an uncertain proposed strengthening; not a theorem with stated hypotheses. |
| 133 / 040 | `?` on three arrows, two read with `\unsure` | Comparison diagram remains tentative; authorial marks and uncertain reading of marks are both retained. |
| 133 / 043 | “On voit … aisément”; “il est bien connu” | Unexpanded claims about the maximal affine quotient and its positive-characteristic unipotent part, to be tested with exact hypotheses. |
| 133 / 044 | “tjrs vérifié”; “est tjrs vérifié”; “est vérifié sss” | Broad realizability assertions for the dual/Picard data; these are assertions, not explicit proof sketches. |
| 133 / 044 | “constructible en général”; “en égalis. car. résiduelles … ‘constructible’” | Claimed contrast between mixed and equal characteristic; the family-level and equal-characteristic tests are developed in the formal-group notes. |
| 133 / 046 | “Obstruction dans H³”; “Indétermination dans H²” | Stated obstruction/ambiguity groups without a cocycle construction or a representability argument on the leaf. |
| 133 / 047 | “il est clair alors que”; `ψ_G injectif` | Unexpanded centre criterion; the ordinary-group proof in the formal-group notes supplies its mechanism. |
| 133 / 049 | “On doit trouver, au signe près” | Explicit sign qualification for the change in the centre pairing under an extension twist. |
| 133 / 049 | “on suppose π₀ commutatif ?! Que faire sinon ?” | Explicit missing-hypothesis question; the proposed restricted pairing uses the central image `π₀*`. |
| 133 / 049–051 | “On peut simplifier encore cette condition …” and its continuation | **Deleted** proposed centre reduction; do not use the cancelled `ψ₀` construction as an established criterion. |
| 133 / 051 | Marginal `?`; “(annulé!)” | The later `ζ₀` discussion is questioned and cancellation affects the preliminary injectivity reduction; exact strike scope remains as transcribed. |
| 133 / 052 | “(annulé?)” | Uncertain cancellation marker on the continuation of the centre reduction, before the new `N=DG` discussion. |
| 133 / 053 | “on a évidemment”; “on trouve” | Unexpanded cokernel and twisting claims for the derived subgroup; ordinary-group verification is given separately. |
| 133 / 054 | “Vérifier” | Explicit check of `λ₀` surjectivity against `N/π₁=DK` and `dN=DM`; the hypotheses matter. |
| 133 / 054 | “qui s'écrit de façon évidente” | Unexpanded variation formula for the residual pairing; the already drawn two-headed arrow must not pre-empt the following epimorphism condition. |

## Standing register II: title sheets, numbering, and counts

Counts labelled **calculated** below come from the supplied sequence, not from a count written by the author. The fragment preserves the visible foliation with `\mspage`; attribution or dating of those pencilled numerals is not assumed.

| Cote / scan(s) | Visible title or numbering | Count and qualification |
|---|---|---|
| 133 / 002 | “groupes Witt / et formes quadratiques,” with “groupes” and “quadratiques” uncertain; foliation `1` uncertain | Cover/title sheet; no written total page count. |
| 133 / 006 | “Groupes de Witt et variantes.”; foliation 5 | Internal heading; scans 006–009 give four supplied pages under this heading, **calculated**, not a written “4 pages.” |
| 133 / 011–013 | “Théorème de Skolem-Nother pour les algèbres d'Azumaya graduées sur un anneau semi-local.” | Printed pp. **447–449**, three supplied pages; `C. R. Acad. Sc. Paris`, vol. 279, issue dated **16 September 1974**, with “Séance du 24 juin 1974” on 013; archive foliation 10–12. |
| 133 / 014–017 | “Formes quadratiques, algèbres de Clifford et signatures.” | Printed pp. **1599–1602**, four supplied pages; vol. 278, issue dated **24 June 1974**, with “Séance du 4 février 1974” on 017; archive foliation 13–16. |
| 133 / 018 | `JOB 289` on the reused listing; mathematical header above it | One supplied reused printed sheet, foliation 17; the job identifier is not a page count or mathematical title. |
| 133 / 030–034 | “jeu de go complet (sur go-ban v×v),” with the letter `v\|ν` uncertain | Five supplied leaves, **calculated**; foliation 29–33, no separate written total. |
| 133 / 035 | “Groupes formels”; foliation 34 | Divider/title sheet; the heading repeats on 036. |
| 133 / 036–044, excluding omitted 041 | “Groupes formels” on 036; foliation 35–39, 41–43 | Eight mathematical leaves after the divider, **calculated**; missing scan 041 was declared blank in the prompt, not silently skipped. |
| 133 / 045 | “Fourbis auxiliaires / cohomologiques / pour groupes / Formels”; foliation 44 | Divider/title sheet for the following auxiliary group-cohomology material; no written total. |
| 133 / 046, 047, 049, 051, 052, 053, 054 | Internal pages **1, 2, 3, 4, 5, 6, 7**; the 5 on 052 is uncertain/clipped | Seven internally numbered mathematical pages, **calculated**; outer foliation 45, 46, 48, 50–53 is separate from this internal sequence. |
| 133 / 048 | University thesis notice, “19 juin 1975”; animal biology; foliation 47 | One interleaved printed notice, not internal page 3 or an omitted mathematical page. |
| 133 / 050 | University thesis notice, “5 Juin 1975”; applied mathematics; foliation 49 | One interleaved printed notice, not internal page 4 or an omitted mathematical page. |
| Entire supplied package | Scans 002–054 excluding 005, 010, 041; outer foliation generally scan minus one | **50 supplied scan pages**, calculated as 53 positions minus three declared blanks; there is no cover statement “50 pages.” |

The inventory classifies 002, 035, and 045 as covers/title sheets; scans 011–018, 048, and 050 as reused printed/typed material; and the remaining 37 as text. Partial cancellations on mathematical sheets are recorded element by element rather than labelling an entire sheet a cancelled draft when it also has live material. The inventory-only classification of 035 and 045 was corrected after the freeze; none of the 51 frozen TeX hashes was changed.

## Results-state reconciliation

| Supplied ID | Status actually supplied | What these pages and this report add |
|---|---|---|
| **WG2 §Week #3** | Unchecked question/plan item | Confirms the quadratic-Witt and finite-set-operation material, identifies concrete failures of some formulas, and places the stronger binomial-cochain proposal in PS §119 rather than inventing one in 133. |
| **WG2 §2.4 #5** | Unchecked question/plan item | Locates abelian varieties at 042–044 and a Chern-class calculation at 004, without a Fourier-transform example; leaves the original 136/137 question open. |
| **WG H6** | “Believe” / unchecked hunch | B09 supplies the conditional `S²→*` obstruction to the literal ordinary-local-system interpretation; no claim is made about unseen strengthened formulations. |
| **MPL_136_047-094 §2** | First-pass returned-package research lead | The indexed functorial complexes/comparison maps remain a lead; 133 does not identify their multiplication or derived binomial structure. |
| **MPL_136_189-234 §2** | First-pass returned-package research lead | A claimed weightwise truncated additive comparison cannot, without further work, be upgraded to full integral homotopy reconstruction. |
| **MPL_136_095-141 L06** | First-pass literature-comparison lead | Retains the relevance of integral-cochain benchmarks but does not substitute an unread earlier research report for a primary theorem. |
| **MPL_136_235-281 §86** | First-pass reference/source-qualification lead | Supports the need for precise hypotheses and versions; the present references were checked at the locators stated here. |
| **TOTASPH E.6** | Proved, as the return's claim | Its filtered-colimit-of-representables criterion is different from the finite-coproduct classification in 024–026; no new proof or automatic application is claimed. |
| **PRETOT A.12; TOTASPH C.10** | Proved/refuted claims respectively; PRETOT also has a later reviewed-run summary | Concern ordered `Δ_inj`, not the finite-set injection category with symmetric-group automorphisms in 024; the category identification must not be conflated. |
| **TOTEX2 D.1; TOTEX2 D.2** | Proved/refuted; intake “CONSISTENT”; later run-level review information supplied | Their separation results are acknowledged as registered and are not rederived from the finite-set pages; eventual isomorphism on 026 is a different construction. |
| **Hua, findings register, 133-centre-and-derived-group-from-two-crossed-modules** | Conjecture/unsearched; “Lean card: partly proved”; intake “new to us” | Centre and derived criteria are checked against 046–054 with ordinary-group proofs; cancelled arguments, commutativity hypotheses, and the residual surjectivity condition are separated. |
| **Hua, findings register, 133-affine-quotient-not-constructible** | Conjecture candidate; source excerpt truncated; intake “new to us” | The characteristic contrast is checked, the unsupported splitting-at-specialization addition is removed from the interpretation, and an actual nonconstructible family is supplied; no unread formalization or novelty claim is endorsed. |

The remaining GALOIS, BISITE, RESIDUE, CATHOT, POLES, and implication entries were read as part of the supplied register, but no precise new theorem-to-theorem implication from these fifty pages is claimed. Matching a term such as “centre,” “extension,” “finite,” or “equivalence” is not enough to identify a result across different categories.

## Reference and version qualifications

References follow author–date APA conventions, with exact sections or theorem locators in the notes. Horel's journal article was published in 2024; numbered technical statements here were checked in **arXiv:2211.02349v2 (23 March 2025)**, with the publisher's abstract and metadata checked separately, and are cited as Horel (2025). Dress–Siebeneicher (1988, 1989) are used only at the accessible indexed publisher-abstract level, with the one-page 1986 announcement independently read; no numbered theorem in their inaccessible full papers is claimed checked. Other version qualifications are retained in the references and supplements.

The manuscript and supplied context remain the primary evidence for what Grothendieck wrote: **cote 133**, scan numbers in each note; **Pursuing Stacks**, the supplied chapter VI–VII files and original page/section markers; **README.md** and **notes/RESULTS_STATE.md**, named headings and IDs. The externally checked 2021 PS edition record is bibliographic context, not a substitute for the supplied text or its pagination. The two Laborde offprints are cited from the supplied scans. Source PDFs and the supplied archives are not included in the deliverable.

## References

- Aldrovandi, E., & Noohi, B. (2009). Butterflies I: Morphisms of 2-group stacks. *Advances in Mathematics, 221*(3), 687–773. https://doi.org/10.1016/j.aim.2008.12.014  
     Author version: https://webspace.maths.qmul.ac.uk/b.noohi/papers/Butterflies1.pdf — Definition 4.1.5, Theorem 4.2.1, Lemma 5.2.1; printed pp. 26 and 38–39.

- Baez, J. C., & Lauda, A. D. (2004). Higher-dimensional algebra V: 2-groups. *Theory and Applications of Categories, 12*, 423–491. https://arxiv.org/abs/math/0307200  
     Author version: https://math.ucr.edu/home/baez/hda5.pdf — §8.3, Theorem 43 and Corollary 44, printed pp. 61–62; normalized 2-cochain equation and 1-cochain equivalence.

- Bertolin, C. (2010). *Extensions and biextensions of locally constant group schemes, tori and abelian schemes* (arXiv:1007.3875) [Preprint]. https://arxiv.org/abs/1007.3875  
     Checked version: https://arxiv.org/pdf/1007.3875 — Lemma 1.2.2 (torus-torsor representability), the immediately following discussion of the dual abelian scheme as the extension sheaf, and Proposition 2.2.3 (biextensions and homomorphisms into the dual). These provide the actual Poincaré family in the formal-group supplement, Appendix B.2.

- Borger, J., & Wieland, B. (2005). Plethystic algebra. *Advances in Mathematics, 194*(2), 246–283. [https://doi.org/10.1016/j.aim.2004.06.006](https://doi.org/10.1016/j.aim.2004.06.006)

- Bouc, S., & Rökaeus, K. (2009). A note on the λ-structure on the Burnside ring. *Journal of Pure and Applied Algebra, 213*(7), 1316–1319. https://doi.org/10.1016/j.jpaa.2008.11.028

- Brion, M. (2009). Anti-affine algebraic groups. *Journal of Algebra, 321*(3), 934–952. https://arxiv.org/abs/0710.5211  
     Checked v3: https://arxiv.org/pdf/0710.5211 — Propositions 2.1–2.3, Remark 2.4, Theorem 2.7, and Proposition 3.1(ii). The specific distinctions used are cited at the notes, not inferred from the title alone.

- Brion, M. (2016). *Some structure theorems for algebraic groups* (arXiv:1509.03059v3) [Preprint]. https://arxiv.org/abs/1509.03059  
     Checked version dated 12 December 2016: https://arxiv.org/pdf/1509.03059 — Theorems 1–2; Theorem 5.1.1; §5.4, equations (5.4.2)–(5.4.4) and Proposition 5.4.10; Proposition 5.5.2. This identifies the checked version rather than guessing later publication pagination.

- Dress, A. W. M., & Siebeneicher, C. (1986). The cyclotomic identity and the cyclic group. *Séminaire Lotharingien de Combinatoire, B14Sd*, 1. https://www.mat.univie.ac.at/~slc/opapers/s14Sdress.pdf

- Dress, A. W. M., & Siebeneicher, C. (1988). The Burnside ring of profinite groups and the Witt vector construction. *Advances in Mathematics, 70*(1), 87–132. https://doi.org/10.1016/0001-8708(88)90052-7

- Dress, A. W. M., & Siebeneicher, C. (1989). The Burnside ring of the infinite cyclic group and its relations to the necklace algebra, λ-rings, and the universal ring of Witt vectors. *Advances in Mathematics, 78*(1), 1–41. https://doi.org/10.1016/0001-8708(89)90027-3

- Elduque, A., & Villa, O. (2008). The existence of superinvolutions. *Journal of Algebra, 319*(10), 4338–4359. https://doi.org/10.1016/j.jalgebra.2007.10.044 — Proposition 8 and Remark 10 checked in the authors' 2007 preprint, §2.2, pp. 4–5: https://arxiv.org/abs/0704.3127

- Fasel, J., & Haution, O. (2025). The stable Adams operations on Hermitian K-theory. *Geometry & Topology, 29*(1), 127–169. https://doi.org/10.2140/gt.2025.29.127 — Theorem 1, p. 128; publisher PDF checked.

- Grothendieck, A. (2021). *Pursuing stacks* [Transcription of a 1983–1984 manuscript; arXiv:2111.01000]. arXiv. [https://arxiv.org/abs/2111.01000](https://arxiv.org/abs/2111.01000)

- Hatcher, A. (2017). *Vector bundles & K-theory* (Version 2.2, November 2017). [Author’s PDF](https://pi.math.cornell.edu/~hatcher/VBKT/VB.pdf). — Proposition 3.8, numbered p. 83; checked version.

- Horel, G. (2024). Binomial rings and homotopy theory. *Journal für die reine und angewandte Mathematik, 2024*(813), 283–305. [https://doi.org/10.1515/crelle-2024-0039](https://doi.org/10.1515/crelle-2024-0039)

- Horel, G. (2025). *Binomial rings and homotopy theory* (arXiv:2211.02349v2) [Versioned preprint; first version 2022]. arXiv. [https://arxiv.org/abs/2211.02349v2](https://arxiv.org/abs/2211.02349v2)

- Joyal, A. (1986). Foncteurs analytiques et espèces de structures. In G. Labelle & P. Leroux (Eds.), *Combinatoire énumérative* (Lecture Notes in Mathematics, Vol. 1234, pp. 126–159). Springer. https://curien.galene.org/Damien/LNM-1234-Joyal.pdf

- Kannan, S., Serpente, S., & Yun, C. H. (2024). Equivariant Hodge polynomials of heavy/light moduli spaces. *Forum of Mathematics, Sigma, 12*, Article e34. https://doi.org/10.1017/fms.2024.20

- Laborde, O. (1974a). Formes quadratiques, algèbres de Clifford et signatures. *Comptes rendus de l'Académie des sciences de Paris, Série A, 278*, 1599–1602. — Supplied primary source, cote 133, scans 014–017; printed issue 24 June 1974, presentation noted as 4 February 1974.

- Laborde, O. (1974b). Théorème de Skolem-Nother pour les algèbres d'Azumaya graduées sur un anneau semi-local. *Comptes rendus de l'Académie des sciences de Paris, Série A, 279*, 447–449. — Supplied primary source, cote 133, scans 011–013; title spelling retained, printed issue 16 September 1974, presentation noted as 24 June 1974.

- Laborde, O. (1976). Classes de Stiefel-Whitney en cohomologie étale. In *Colloque sur les formes quadratiques (Montpellier, 1975)* (*Bulletin de la Société mathématique de France. Mémoire*, No. 48, pp. 47–51). Société mathématique de France. https://doi.org/10.24033/msmf.201 — §§II–III, pp. 49–50; primary PDF checked at https://www.numdam.org/article/MSMF_1976__48__47_0.pdf

- Mazur, B., & Messing, W. (1974). *Universal extensions and one dimensional crystalline cohomology* (Lecture Notes in Mathematics, Vol. 370). Springer. https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/mazur-messing.pdf  
     Checked: I §1.8 (Barsotti–Tate groups over p-nilpotent bases), §1.9 and Proposition 1.10 (abelian schemes and universal extensions), and §2.6, Proposition 2.6.7 with the proof's explicit arbitrary-base-change statement; printed pp. 8–11 and 24–25.

- Noohi, B. (2008). *On weak maps between 2-groups* [Preprint, author version dated 25 June 2008]. https://webspace.maths.qmul.ac.uk/b.noohi/papers/Maps.pdf  
     Checked: Theorem 14.1; §15.1, Remark 15.1 and Example 15.2; printed pp. 33 and 37–38. The author lists it as a preprint/work in progress: https://webspace.maths.qmul.ac.uk/b.noohi/research.html.

- Stacks Project Authors. (n.d.). Spectral sequences for Ext (Tag 07A9, Example 21.32.1). *The Stacks Project*. Retrieved November 16, 2026, from https://stacks.math.columbia.edu/tag/07A9

- Toën, B. (2020). Le problème de la schématisation de Grothendieck revisité. *Épijournal de Géométrie Algébrique, 4*, Article 14, 1–21. [https://doi.org/10.46298/epiga.2020.volume4.6060](https://doi.org/10.46298/epiga.2020.volume4.6060)

- Zibrowius, M. (2015). Symmetric representation rings are λ-rings. *New York Journal of Mathematics, 21*, 1055–1092. https://nyjm.albany.edu/j/2015/21-49v.pdf — Introduction, Theorem, and Definition 1.2 checked in the journal text.

- Zibrowius, M. (2018). The γ-filtration on the Witt ring of a scheme. *The Quarterly Journal of Mathematics, 69*(2), 549–583. https://doi.org/10.1093/qmath/hax050 — Theorem 2 and the Witt-quotient qualification checked in the author's arXiv v2 (11 August 2016), https://arxiv.org/abs/1411.3198v2; journal bibliographic metadata checked separately.
