# Research dossier: additive invariants, multiplicative transport, and S11

Scope: post-freeze research only; no transcription file was changed. Duplicate literature summaries were shortened after integration into the main notes; the primary-source locations and mathematical working proofs are retained. The evidence below distinguishes the frozen scans, supplied context leads, directly checked primary literature, and independent mathematical checks. Every proposed note has at most four sentences; source metadata and proof details are separate.

## Overall assessment

Scans 302–318 give a precise additive universal-property framework and expressly identify the missing multiplicative information; scans 320–325 investigate coalgebra/divided-power compatibility and end with questions or incomplete conditions. They support a functorial algebraic program, but do not establish an ordinary integral commutative PD cochain algebra recovering cup products, PD descent to cohomology, or integral homotopy-type classification. The earlier weighted comparison remains the relevant candidate, with its weights, coefficient algebra, and comparison range retained. The broad unweighted PD reading is already obstructed by the earlier package's O01; the new contribution here is the manuscript's own diagnosis in 311–312 and 318, together with the separate counterexample to the unrestricted convolution-PD question in 324.

## Proposed notes

### C01 — The indexing convention is much better constrained here

**Source:** frozen scans 302–303, 306–308. **Kind/status:** textual observation; high confidence for the convention evidence, not a silent emendation.

Scans 302–303 define the simplex category using the ordered sets \([0,n]\), and 306–308 apply Dold–Puppe normalization and denormalization, which strongly supports the historical use of “semi-simplicial” for objects including degeneracies. This sharpens the unresolved convention question in `context/same_cote_136/MPL_136_235-281_notes.md`, N74 (scan 235), rather than transferring results for modern \(\Delta_{\mathrm{inj}}\)-presheaves without a comparison. The literal `Hom_Ens` and reversed Hom expressions on 303 remain in the frozen text; `Hom_ord` and the later equivalence are interpretive evidence, not replacement readings.

**Register:** PRETOT A.12 is labelled “Proved (return's claim)” in RESULTS_STATE but concerns a different \(\Delta_{\mathrm{inj}}\) setting; it does not decide this manuscript convention. **Context relationship:** adds evidence to N74; agrees with Hua, modernised reading of cote 136, introductory notation discussion, while relying on the frozen pages.

### C02 — The raw universal invariant is expressly not homotopy invariant

**Source:** frozen scan 306, “ce ne sont pas des invariants du type d’homotopie.” **Kind/status:** textual observation; confirmed.

The author explicitly distinguishes representable invariants \(X\mapsto\operatorname{Hom}(X,K)\) from homotopy invariants and proposes adding structure and inverting arrows induced by homotopy equivalences. Thus the universal-property discussion is not already a proof that the raw construction computes a homotopy type. Its deliberately qualified aim is to retain aspects of that type after localization.

**Register:** follow-ups @305 remains open; WG H6 is an unchecked hunch, not a theorem supplied by these pages. **Context:** `context/hua_project/136.modern.tex`, discussion immediately preceding “L’invariant additif universel”; the frozen text supports Hua's interpretation here.

### C03 — The displayed Hom is a group of chain maps

**Source:** frozen scans 311–312. **Kind/status:** mathematical/textual distinction; confirmed.

The formula \(F(X)\simeq\operatorname{Hom}_{\mathrm{Ch}}(C_\bullet X,K_\bullet)\) is a representability statement for additive invariants, and 312 explicitly identifies this Hom with degree-zero cycles of the total Hom complex. It must therefore be distinguished from the whole cochain complex and from its cohomology. The term “universal additive invariant” does not by itself supply a multiplicative cochain comparison.

**Register:** adds local evidence to MPL_136_047-094 §2 and MPL_136_189-234 §2, both recorded as first-pass observations/leads; does not promote them to reviewed theorems. **Context:** Hua, modernised reading of cote 136, “L’invariant additif universel.”

### C04 — The manuscript itself separates multiplication from scalar structure

**Source:** frozen scans 311–312. **Kind/status:** textual observation; confirmed.

The author says that multiplication on \(F\) cannot be reconstructed from the bare chain complex \(C_\bullet X\), while the \(h\)-module structure can be accounted for by the coefficient object and base change. He makes the additional structures inherited from \(X\) the central subject of the ensuing investigation. This sharpens the distinction between the linear reconstruction and multiplicative reconstruction already raised in `MPL_136_235-281_notes.md`, N40, concerning scan 273.

**Register:** gap g1048 remains open concerning the precise multiplicative reconstruction; the present pages explain why the additive assertion alone cannot settle it. **Context:** Hua, “L’invariant additif universel,” agrees on this separation.

### C05 — Dold–Kan is not a strong monoidal equivalence for the ordinary tensor

**Source:** frozen scan 318, “ne se correspondent pas par DP et ND.” **Kind/status:** literature comparison; directly verified.

Schwede and Shipley (2003, §1) distinguish the symmetric lax shuffle structure from a strong monoidal equivalence; see integrated note N28 for the application.

**Register:** sharpens gap g1048 and follow-ups @305 without settling either. **Context:** Hua's footnote to “L’invariant additif universel” says “n’est pas monoïdale”; the more precise formulation above avoids overlooking the lax structure. **Primary source:** https://homepages.math.uic.edu/~bshipley/monoidalequi.final.pdf ; web ref `turn14view1`, PDF pp. 1–3 / printed pp. 287–289.

### C06 — An elementary size test for the tensor mismatch

**Source:** frozen scan 318. **Kind/status:** own diagnostic; checked directly.

For the chain complex \(K\) concentrated as \(\mathbf Z\) in degree one, its Dold–Kan denormalization \(D(K)\) has degree zero equal to zero and degree one equal to \(\mathbf Z\). Hence \(N(D(K)\otimes_{\mathrm{level}}D(K))_1=\mathbf Z\), whereas \((K\otimes K)_1=0\), so these ordinary tensor constructions cannot be naturally isomorphic as complexes. This does not dispute the shuffle quasi-isomorphism or an equivalence after passing to an appropriate derived setting.

**Register:** an illustrative check of the structural warning, not a solution of gap g1048. **Context:** adds a concrete example to Hua's Dold–Kan footnote.

### C07 — Transporting the tensor is a genuine alternative

**Source:** frozen scan 318, “par transport de structure via DP.” **Kind/status:** modern comparison; directly verified.

Richter (2009, Theorem 7.1) supplies the transported tensor; the manuscript comparison and the separate reading difference are integrated in N30 and Q07.

**Register:** follow-ups @305 remains open; this is a structural analogue, not an identification. **Context:** adds precision to `MPL_136_095-141_notes.md`, L11, and to Hua's discussion. **Primary source:** https://math.mit.edu/~hrm/palestine/richter-divided-power.pdf ; refs `turn15view3`, `turn15view4`.

### C08 — A compatibility with the differential is not the whole descent problem

**Source:** frozen scans 320, 324–325. **Kind/status:** precise proof obligation; directly checked against a standard definition.

Richter (2009, Definition 7.4) separately requires boundary preservation; see N31 for the historical proof obligation.

**Register:** directly addresses the PD-descent clause of follow-ups @305, which remains open for that construction. **Context:** the earlier O01 obstruction does not assume PD descent and therefore cannot serve as its proof. **Primary source:** same Richter PDF, `turn15view3` (Definition 7.4 and following paragraph).

### C09 — The existing integral obstruction must retain its hypotheses

**Source:** frozen scan 318 and the open PD questions on 324–325. **Kind/status:** application of an existing checked diagnostic, not claimed as a new result.

The earlier `MPL_136_095-141_notes.md`, O01, already observes that an ordinary integral cochain algebra with \(z^2=2\gamma_2(z)\) and \(d\gamma_2(z)=z\,dz\) for every positive even cocycle cannot recover the cup-product ring of \(\mathbf{CP}^2\). A cocycle representing its degree-two generator would force its primitive square in degree four to be twice another integral class, and this argument uses one cocycle without assuming that divided powers descend to cohomology. Weights, the coefficient algebra, a restricted PD domain, or the extraction/localization functor can avoid those hypotheses, so the test refutes only the strong unqualified reading.

**Register:** MPL_136_095-141 O01 is listed as an obstruction-test lead; follow-ups @305 explicitly remembers this test. **Context relationship:** the new local contribution is 318's explanation of the tensor obstruction, not rediscovery of O01.

### C10 — There is also a conditional functorial commutativity obstruction

**Source:** frozen scans 306, 311–312, 318. **Kind/status:** literature benchmark; directly verified.

Cenkl (1989, §5, Theorem 2) excludes an integral solution of his specified commutative cochain problem; the hypotheses are retained in N32.

**Register:** confirms the literature content of `MPL_136_095-141_notes.md`, L14; does not settle follow-ups @305's weighted version. **Primary source:** https://msp.org/pjm/1989/140-1/pjm-v140-n1-p02-p.pdf ; refs `turn21view1`, `turn22view0`.

### C11 — Strict commutativity in a diagram category avoids the blanket no-go

**Source:** frozen scan 318. **Kind/status:** modern comparison; directly verified.

Richter and Sagave (2020, Theorems 1.1–1.2) supply the diagram-valued comparison summarized in N33.

**Register:** verifies the structural qualification already recorded in MPL_136_095-141 L11; follow-ups @305 remains a comparison problem. **Primary sources:** https://arxiv.org/pdf/1801.01060 , pp. 2–3 (`turn16view0`); publication metadata `turn21view3`.

### C12 — The homotopy-type benchmark requires specified coherent structure

**Source:** frozen scans 306, 311–312, 318. **Kind/status:** literature comparison; directly verified.

Mandell's (2006) integral E-infinity classification and faithful-but-not-full qualification are integrated in N34.

**Register:** MPL_136_095-141 L06 is a literature-comparison lead; follow-ups @305 remains open; WG H6 remains an unchecked hunch. **Primary source:** https://www.numdam.org/item/PMIHES_2006__103__213_0/ , `turn15view2` (abstract and metadata; theorem content agrees with the earlier package).

### C13 — Binomial reconstruction is a distinct target category

**Source:** frozen scans 318, 320–325. **Kind/status:** literature comparison; directly verified.

Horel's (2024) binomial reconstruction, completion, and forgetful-functor qualification are integrated in N35.

**Register:** follow-ups @304 and @305 remain open; the existing MPL_136_095-141 L10 comparison is confirmed. **Context:** `ps_chapters_VI_VII/ps6.tex`, §119, PS pp. 501–502, distinguishes PD and possible binomial linearizations. **Primary source:** https://geoffroy.horel.org/binomial.pdf , PDF pp. 8, 13–14; refs `turn19view1`, `turn19view2`.

### C14 — Yoneda identifies the universal operation, not its existence

**Source:** frozen scans 320, 323. **Kind/status:** formal calculation; confirmed under the indicated category of modules.

For \(F_A(M)=\operatorname{Hom}_h(A,M)\), a natural transformation \(F_A\to F_A\Gamma^p\) is determined by \(u_p\in\operatorname{Hom}_h(A,\Gamma^p A)\), with value \(f\mapsto\Gamma^p(f)\circ u_p\). This is the Yoneda reduction written on 323 and explains the universal substitutions in the diagrams. It does not alone construct compatible \(u_p\)'s, prove the displayed PD identities, or identify an unrestricted \(\Gamma\)-comonad structure.

**Register:** supports the operations part of follow-ups @305 but settles no cochain comparison. **Context:** Hua, “Gribouillis : coalgèbres et puissances divisées,” is supported on this formal reduction; its page labels must not replace the scans.

### C15 — The PD section contains open questions and unfinished conditions

**Source:** frozen scans 324–325. **Kind/status:** textual observation; confirmed.

Scan 324 asks whether the convolution ideal has divided powers and separately asks about composition and uniqueness of the universal operations; scan 325 leaves conditions (4) and (6) unfinished. These should not be reported as a completed general theorem on convolution PD algebras. Hua's modernised reading, “Gribouillis : coalgèbres et puissances divisées,” likewise recognizes that the calculations end without a stated conclusion.

**Register:** follow-ups @305 is sharpened by explicit remaining algebraic obligations; neither WG2 §2.4 #5 nor the earlier-package observations are promoted to theorems.

### C16 — The convolution-PD question has a negative answer without a hypothesis on A

**Source:** frozen scan 324, “Cet idéal a-t-il des p.d.?” **Kind/status:** reader's counterexample proposed in this research review and independently checked here; high confidence under the counital cocommutative-coalgebra reading.

Take \(A=\mathbf Z1\oplus(\mathbf Z/2)e\) with \(\Delta e=e\otimes1+1\otimes e+e\otimes e\), and the PD ring \(B=\mathbf Z\oplus(\mathbf Z/2)t\oplus(\mathbf Z/4)u\), \(t^2=2u\), \(tu=u^2=0\), with ideal \(J=(t,u)\), \(\gamma_2(at+bu)=a^2u\), and \(\gamma_n=0\) for \(n\ge3\). For \(f(1)=0\), \(f(e)=t\), convolution gives \(f^2(e)=2u\ne0\), but every homomorphism \(v:A\to B\) satisfies \(2v(e)=0\), so \(f^2=2\gamma_2(f)\) is impossible. Thus the ideal \(\operatorname{Hom}_{\mathbf Z}(A,J)\) has no PD structure at all, whereas for finite projective \(A\) the dual-tensor description reduces the problem to flat base change of a PD ideal.

**Register:** settles this unrestricted local question negatively, not the entire weighted cochain program; no pre-existing RESULTS_STATE result is credited for this counterexample. **Context:** adds an explicit restriction to Hua's account of scan 324 and to follow-ups @305's algebraic obligations. **Independent check:** the coalgebra is the quotient of the free coalgebra on group-like elements 1 and g by the coideal generated by \(2(g-1)\); the PD axiom checks are recorded below.

### C17 — The negative degrees of the scan299 tail object are rational Hom groups

**Source:** frozen scan 299, the final boxed coefficient relation, with \(S_h=\Gamma_h(T)\). **Kind/status:** reader's calculation proposed in this research review and independently verified here; high confidence.

For \(d>0\), let \(R_d\) be generated by \(e_i\), \(i\ge d\), subject to \(\binom ji e_j=\binom{j-d}{i-d}e_i\); then \(e_i\mapsto1/\binom id\) identifies \(R_d\) with \(\mathbf Q\). Consequently, for the all-\(\mathbf Z\)-graded right adjoint displayed on 299, \((\varphi_0(M\otimes_h\Gamma_h(T)))_{-d}\cong\operatorname{Hom}_{\mathbf Z}(\mathbf Q,M)\), naturally as an \(h\)-module, with no flatness assumption on \(h\) or \(M\). This sharpens the earlier \(\mathbf Q\)-Laurent example in `MPL_136_235-281_notes.md`, N22; it is not an identification with \(M\otimes\mathbf Q\), and it does not assert anything about the negative-degree multiplication.

**Register:** sharpens the grading issue around gap g1048; retains Michel Hua's project's credit for the earlier finite-tail full-faithfulness finding and does not reprove it as a new result. **Textual limit:** uses the final boxed relation, independently of the unresolved intermediate exponents on frozen 299.

### C18 — Flatness alone does not commute tensor product with the intersection

**Source:** frozen scan 283, the equality involving \(\bigcap_i P_i\otimes s\). **Kind/status:** new diagnostic proposed by the parent researcher and independently checked here; high confidence.

The counital cocommutative coalgebra \(S=\mathbf Z1\oplus\mathbf Q\), with \(\mathbf Q\) primitive, is flat over \(\mathbf Z\). For \(P_n=2^n\mathbf Z\subset\mathbf Z\), the subobjects \(P_n\otimes S\subset S\) are \(2^n\mathbf Z\oplus\mathbf Q\), so \(\bigcap_n(P_n\otimes S)=0\oplus\mathbf Q\ne0=(\bigcap_nP_n)\otimes S\). This disproves a flatness-alone justification of the equality, but does not show that the manuscript's specially iterated \(P_i\)'s fail it.

**Context:** adds an intersection diagnostic alongside the earlier completed-base-change warning in `MPL_136_235-281_notes.md`, N48; the two examples address different limit operations. **Scope:** finite projectivity of S is a sufficient replacement hypothesis for arbitrary-limit preservation, but no claim is made that the manuscript assumes it or that it is necessary.

### C19 — The right adjoint exists for ordinary graded objects in any complete abelian category

**Source:** frozen scan 295, the question-marked representability and component formulas. **Kind/status:** formal construction proposed by the parent researcher and proved explicitly below; high confidence for ordinary graded objects.

Let \(\mathcal A_S\) have objects \(i\in\mathbf Z\) and morphism groups \(\mathcal A_S(i,j)=S_{j-i}\), with composition given by multiplication, and interpret ordinary graded S-objects as additive functors \(\mathcal A_S\to C\). Restriction to the full subcategory \(j\ge N\) has an additive right Kan extension whenever C has small products and kernels, constructed from copies of \(Q_j\) indexed by \(s\in S_{j-i}\) and the additive and S-action relations. No tensor product in C is required, and either C or its opposite being Grothendieck implies the requisite completeness (Stacks Project, Lemma 19.13.2, tag 07D8, together with the definition for the opposite case). This settles the ordinary graded interpretation only: the doubtful “diffs.” on 295 and any differential or derived version require a separate specification of the source category and truncation.

**Context:** strengthens the explicit truncation-adjoint constructions in `MPL_136_235-281_notes.md`, N17, without transferring existence to the different schematic adjoints discussed in PS §124 or N51. **Register:** it does not settle the multiplicative reconstruction in gap g1048. **Primary source for completeness:** https://stacks.math.columbia.edu/tag/07D8 , ref `turn39view2`.

## Independent checks and proofs

### C16: PD axioms and coalgebra

The ring structure is well defined because \(2t^2=4u=0\), and all triple products in J vanish. Replacing an integer representative a of its residue class modulo 2 by a+2k changes a²u by a multiple of 4u, so γ₂ is well defined. For x=at+bu and y=a′t+b′u, γ₂(x+y)−γ₂(x)−γ₂(y)=2aa′u=xy; for c=n+ct+du in B, γ₂(cx)=n²a²u=c²γ₂(x). All higher addition, product, and composition axioms reduce to uJ=u²=0; the only nonzero product condition is x²=2γ₂(x).

The quotient coalgebra is counital and cocommutative: write g=1+e, with Δg=g⊗g and εg=1. The subgroup generated by 2(g−1) is a coideal because Δ(2e)=2e⊗1+1⊗2e+2e⊗e. This secures coassociativity without relying on a direct expansion. The evaluation contradiction proves failure of every possible PD structure on the Hom ideal, not merely failure of the most obvious formula.

### C17: prime-local proof

The factorial identity

\[
\frac{\binom ji}{\binom jd}
=\frac{\binom{j-d}{i-d}}{\binom id}
\]

gives the asserted map \(R_d\to\mathbf Q\). After localization at a prime p, choose j=p^r+d−1 beyond all indices in a finite linear combination; the coefficients \(\binom{j-d}{i-d}=\binom{p^r-1}{i-d}\) are p-units, so the combination becomes one scalar multiple of e_j. Its rational image detects that scalar, proving injectivity after every localization and hence globally. For p^r>d−1,

\[
v_p\binom{p^r+d-1}{d}=r-v_p(d),
\]

so the image contains arbitrarily high p-power denominators for every prime and therefore all of Q. Base-changing the presentation gives \(h\otimes_{\mathbf Z}R_d\), and tensor–Hom adjunction gives the claimed formula for every h-module M. Evaluation at 1 need not be injective: the nonzero quotient map Q→Q/Z sends 1 to zero, so the formula must not be replaced by a naive “rational subgroup of M” statement.

### C18: coalgebra and embedded intersection

Define Δ(1)=1⊗1, Δ(q)=q⊗1+1⊗q, ε(1)=1, and ε(q)=0. Coassociativity and cocommutativity follow immediately on these generators, and the underlying abelian group Z⊕Q is flat because Q is a localization of Z. The inclusion P_n→Z induces the injective map P_n⊗S→S; after identifying P_n with Z by its generator 2^n, this is multiplication by 2^n on S, whose image is exactly 2^nZ⊕Q. This fixes the ambient embeddings required for the intersection calculation and confirms that a flat counital cocommutative coalgebra, rather than merely an unrelated flat module, supplies the test.

### C19: explicit construction without a tensor product in C

Assume C is a locally small additive category with all small products and equalizers; a complete abelian category has these properties. Let S be a unital, associative, nonnegatively graded ring, with each component an ordinary set-sized abelian group; commutativity is not needed for this construction. Let B be the full preadditive subcategory of \(\mathcal A_S\) on the integers at least N, and let \(Q:B\to C\) be additive. For each integer i form

\[
E_i=\prod_{j\ge N}\prod_{s\in S_{j-i}} Q_j.
\]

Here \(S_m=0\) for m<0. Write \(p_{j,s}:E_i\to Q_j\) for a coordinate projection, and define \(R_i\subset E_i\) as the common kernel of the following morphisms:

\[
p_{j,0},\qquad
p_{j,s+t}-p_{j,s}-p_{j,t},\qquad
Q(a)p_{j,s}-p_{k,as},
\]

where j,k≥N, s,t∈S_{j-i}, and a∈S_{k-j}. The family of equations is set-sized, so its common kernel is one kernel into a product. Coordinates with j<i are forced to zero and can be omitted, leaving the degrees \(Q_{i+n}\) for \(n\ge\max(0,N-i)\), as anticipated by the manuscript. A single copy of each \(Q_{i+n}\) is not sufficient for arbitrary \(S_n\); the powers indexed by its elements, or the equivalent additive cotensors, are essential.

For r∈S_{i′−i}, define \(R(r):R_i\to R_{i′}\) by the coordinate formula

\[
p_{j,s}R(r)=p_{j,sr}.
\]

The defining equations make this additive in r, associative, and unital, so R is an additive functor \(\mathcal A_S\to C\). Given an S-linear map f from the tail of P to Q, define \(\widetilde f_i:P_i\to R_i\) by its coordinates \(f_jP(s)\); these satisfy all the displayed relations. Conversely, for an S-linear \(g:P\to R\), take \(f_j=p_{j,1}g_j\) for j≥N. Naturality and the relation \(p_{k,s}=Q(s)p_{j,1}\) when i=j≥N show that these constructions are inverse, naturally in P and Q, giving

\[
\operatorname{Hom}_{\operatorname{Add}(B,C)}(P|_B,Q)
\cong
\operatorname{Hom}_{\operatorname{Add}(\mathcal A_S,C)}(P,R).
\]

Thus R=φ_NQ, with \(\tau_N\varphi_NQ\cong Q\). The proof requires neither coproducts nor a tensor product of objects of C.

For the enriched description, a cotensor \([G,X]\) by an abelian group G exists from products and kernels: choose a presentation \(\mathbf Z^{(J)}\to\mathbf Z^{(I)}\to G\to0\) and take the kernel of \(X^I\to X^J\). Applying \(\operatorname{Hom}_C(T,-)\) proves its presentation-independent universal property

\[
\operatorname{Hom}_C(T,[G,X])
\cong
\operatorname{Hom}_{\mathbf{Ab}}(G,\operatorname{Hom}_C(T,X)).
\]

The same object can therefore be written

\[
(\varphi_NQ)_i
=\int_{j\in B}[S_{j-i},Q_j],
\]

the Ab-enriched right Kan extension end. This notation does not presume that S itself is an object of C or that the manuscript's internal-Hom notation has already been justified. If C is Grothendieck, products exist by Stacks tag 07D8 and kernels already exist; if C^op is Grothendieck, its coproducts give products in C directly. The source's informal representability sentence is thereby replaced by a direct construction, without asserting a blanket representability criterion for arbitrary C or a differential-graded truncation theorem.

## Earlier literature leads retained without new full-text verification

- `MPL_136_095-141_notes.md`, L01, and `MPL_136_235-281_notes.md`, N54/§86, report direct inspection of Cartan (1976), §7, pp. 269–271: weight-r cohomology agrees with ordinary integral cohomology in the stated range, with binomial-weighted products. This subtask verified publisher metadata, not those original printed pages; any use should retain the earlier package's source qualification and not claim a new identification with the manuscript.
- The earlier L02–L03 specify Cenkl–Porter and Garvín et al. ranges and higher multiplicative comparisons. Those are useful targets but were not independently rechecked in this subtask; neither the inclusive Cartan endpoint nor the strict Miller-type endpoint should be silently substituted for the other.
- Miller (1978) and Dwyer (1979) were found bibliographically by the earlier packages, which explicitly did not retrieve the full originals. The tame coefficient/connectivity limitations reported from Scheerer–Tanré (1991), pp. 376–377, remain limitations, not a proof of an unrestricted integral claim.
- Toën (2020), Theorem 0.1, is already discussed with its simply connected finite-type and affine-stack hypotheses in the earlier L09; an attempted primary retrieval here was unsuccessful. Do not recast it as full faithfulness of the manuscript PD construction or as the missing filtered comparison requested in follow-ups @304.

## Primary bibliography and retrieval ledger

Cenkl, B. (1989). Cohomology operations from higher products in the de Rham complex. *Pacific Journal of Mathematics, 140*(1), 21–33. https://msp.org/pjm/1989/140-1/pjm-v140-n1-p02-p.pdf

- Directly checked §5, Theorem 2, pp. 31–33; web refs `turn21view1`, `turn22view0`.

Horel, G. (2024). Binomial rings and homotopy theory. *Journal für die reine und angewandte Mathematik, 2024*(813), 283–305. https://doi.org/10.1515/crelle-2024-0039

- Author PDF: https://geoffroy.horel.org/binomial.pdf ; directly checked Remark 3.11, Theorem 5.4, and Theorem 6.1, PDF pp. 8, 13–14; refs `turn15view1`, `turn19view1`, `turn19view2`. Use theorem numbers because the live author PDF may be a later revision than the 2024 journal pagination.

Mandell, M. A. (2006). Cochains and homotopy type. *Publications Mathématiques de l’IHÉS, 103*, 213–246. https://doi.org/10.1007/s10240-006-0037-6

- Primary journal record and abstract: https://www.numdam.org/item/PMIHES_2006__103__213_0/ ; directly checked classification and faithful/not-full statement; ref `turn15view2`.

Richter, B. (2009). Divided power structures and chain complexes. In C. Ausoni, K. Hess, & J. Scherer (Eds.), *Alpine perspectives on algebraic topology* (Contemporary Mathematics, Vol. 504, pp. 237–254). American Mathematical Society. https://doi.org/10.1090/conm/504/09882

- Publisher PDF hosted at MIT: https://math.mit.edu/~hrm/palestine/richter-divided-power.pdf ; directly checked §7, Theorem 7.1, Corollary 7.2, Definition 7.4, Theorem 7.5, printed pp. 248–250; refs `turn14view0`, `turn15view3`, `turn15view4`. Editors verified in the AMS series catalogue https://www.ams.org/books/conm/529/conm529-endmatter.pdf , ref `turn27search12`.

Richter, B., & Sagave, S. (2020). A strictly commutative model for the cochain algebra of a space. *Compositio Mathematica, 156*(8), 1718–1743. https://doi.org/10.1112/S0010437X20007319

- Author version: https://arxiv.org/pdf/1801.01060 ; Theorems 1.1–1.2, pp. 2–3, ref `turn16view0`. Publisher metadata: https://www.cambridge.org/core/journals/compositio-mathematica/article/strictly-commutative-model-for-the-cochain-algebra-of-a-space/4076D51EAAD865E63F13B718B6026074 ; refs `turn19view0`, `turn21view3`.

Schwede, S., & Shipley, B. (2003). Equivalences of monoidal model categories. *Algebraic & Geometric Topology, 3*, 287–334. https://doi.org/10.2140/agt.2003.3.287

- Author PDF: https://homepages.math.uic.edu/~bshipley/monoidalequi.final.pdf ; directly checked §1, pp. 1–3, especially the caveat following Theorem 1.1; ref `turn14view1`.

The Stacks Project Authors. (n.d.). Lemma 19.13.2 (Tag 07D8). In *The Stacks Project*. Retrieved November 17, 2026, from https://stacks.math.columbia.edu/tag/07D8

- Directly checked: a Grothendieck abelian category has arbitrary products; ref `turn39view2`. The surrounding representability lemma and proof are visible at https://stacks.math.columbia.edu/tag/07D6 , ref `turn38view0`.

### Bibliographic leads not newly used for a technical theorem

Cartan, H. (1976). Théories cohomologiques. *Inventiones mathematicae, 35*, 261–271. https://doi.org/10.1007/BF01390140

- Publisher metadata checked at https://link.springer.com/article/10.1007/BF01390140 ; prior ref `turn2view0`; original §7 not retrieved anew.

Miller, E. Y. (1978). Derham cohomology with arbitrary coefficients. *Topology, 17*(2), 193–203. https://doi.org/10.1016/S0040-9383(78)90025-3

- Bibliography copied from the supplied earlier-package bibliography; no theorem asserted from a newly read original.

Scheerer, H., & Tanré, D. (1991). Exploring W. G. Dwyer's tame homotopy theory. *Publicacions Matemàtiques, 35*, 375–402. https://doi.org/10.5565/publmat_35291_05

- Prior package directly checked §0, pp. 376–377; no fresh theorem verification here.

Toën, B. (2020). Le problème de la schématisation de Grothendieck revisité. *Épijournal de Géométrie Algébrique, 4*, Article 14. https://doi.org/10.46298/epiga.2020.volume4.6060

- Retained as an earlier-package lead; primary retrieval attempted but unavailable in this subtask.
