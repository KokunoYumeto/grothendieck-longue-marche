# Oda comparison for frozen cote 57, scans 285–292, 294, 297, 311, 313

## Scope and source

This is post-freeze mathematical comparison, not a new transcription or a visual audit. The frozen manuscript text was read without changing its page fragments or scan records. No manuscript source image was consulted. The supplied context README and RESULTS_STATE were read first; their earlier-run assertions remain claims at their stated review status.

**Primary printed source:** Tadao Oda, *The first de Rham cohomology group and Dieudonné modules*, Annales scientifiques de l’École Normale Supérieure, 4e série, 2, no. 1 (1969), 63–135, supplied as context/Oda_1969_first_de_Rham_cohomology_Dieudonne_modules.pdf. The PDF has 74 pages: PDF page 1 is the NUMDAM cover; for article pages, **printed page = PDF page + 61**. Locators below give both numbers. Text extraction was used only on this printed contextual source, with rendered-page verification of the principal formulas. No external web source was needed.

“Printed result” below means a result actually stated and proved by Oda. “Comparison” or “own observation” marks an inference for the present manuscript. A common subject does not establish historical dependence or prove a manuscript construction.

## 1. Igusa, the full Picard scheme, and Hodge asymmetry

**Manuscript locations:** scan 285 names the Igusa example and contrasts the dimension of \(H^1(X,\mathcal O_X)\) with the dimension of the reduced Picard variety; scans 287–288 ask for either sign of \(h^{0,1}-h^{1,0}\), variation in families, nonflat Picard schemes, and failure of a suitable abelian subscheme; scan 311 proposes studying the modular family of the Igusa surface.

**Printed source:** Oda’s introduction, printed p. 64 / PDF 3, explicitly cites Igusa [20], [21] when explaining why the reduced Picard variety does not recover degree-one de Rham cohomology in characteristic \(p\). It also warns that even the full Picard scheme corresponds, in general, only to a canonical subspace of that cohomology. The proved comparison is Corollary 5.12, printed p. 131 / PDF 70, supplemented by the remark on printed p. 132 / PDF 71:
\[
D M(\operatorname{Pic}_{X/k}[p])
\hookrightarrow H^1_{\mathrm{dR}}(X),\qquad
\operatorname{im}=\bigcap_{n\geq0}\ker(d\circ V^n).
\]
Here \(k\) is perfect of characteristic \(p\), \(X\) is smooth and proper, and \(X(k)\ne\varnothing\); \(V\) is the Cartier operator in Oda’s construction. This is not a general identification with all of \(H^1_{\mathrm{dR}}(X)\).

**Comparison:** Oda supports the distinction between reduced Picard dimension, infinitesimal Picard structure, and de Rham information. He does not compute the quotient construction in scans 285–286 or prove the requested asymmetry and family examples in scans 287–288. **Own conditional observation:** in the basic scan-285 example with the symmetry action and characteristic 2, the derivative of \([-1]\) is the identity; inserting this into the displayed formulas of scan 287 gives \(h^{0,1}=h^{1,0}=\dim A+\dim B\), although the reduced Picard dimension is only \(\dim B\). Thus the particular nonreduced-Picard example and the later requested Hodge-asymmetry examples are distinct steps in the manuscript’s argument.

Oda’s bibliography, printed p. 134 / PDF 73, identifies the Igusa references as “A fundamental inequality in the theory of Picard varieties,” PNAS 41 (1955), 317–320, and “On some problems in abstract algebraic geometry,” PNAS 41 (1955), 961–967. These are bibliographic leads, not independently consulted sources in this note.

## 2. Tangent Picard information and the two Hodge terms

**Printed result:** the first remark after Corollary 5.12, printed p. 132 / PDF 71, identifies
\[
(k,\sigma^{-1})\otimes_k
D M(\operatorname{Pic}_{X/k}[F])
\simeq H^1(X,\mathcal O_X).
\]
Its commutative diagram places this above the canonical subspace of \(H^1_{\mathrm{dR}}(X)\), whose intersection with \(H^0(X,\Omega^1_{X/k})\) is identified by Corollary 5.12 with \(D M(\operatorname{Pic}_{X/k}[V])\). The diagram has no terminal zero above \(H^1(X,\mathcal O_X)\); its assertion of exact columns does not assert surjectivity onto that top term.

**Comparison:** this is a precise source for distinguishing the two infinitesimal pieces relevant to scan 287’s difference
\(\dim t_{A'}^\Gamma-\dim(t_A)'^\Gamma\)
and scan 297’s tangent/cohomology diagrams. It gives a suitable framework for comparing the group actions after checking their variance and Frobenius twists; it does not itself compute the dimensions of the invariant spaces or their behavior under specialization.

**Earlier contextual witness:** the supplied cote-54 transcription, scan 3, has \(t_B=H^1(A,\mathcal O_A)\), \(t_A=H^0(A,\Omega^1_A)^\vee\), and the associated degree-one cohomology extension. This is a real thematic overlap with scans 287 and 297, but the earlier transcription has not been independently visually reviewed in this task.

## 3. What the full finite group scheme \(A[p]\) determines

**Printed result:** Corollary 5.11, printed p. 131 / PDF 70, for an abelian variety \(A\) over a perfect field of characteristic \(p\), gives a canonical isomorphism of left Dieudonné modules
\[
M(A[p])\simeq H^1_{\mathrm{dR}}(A).
\]
It identifies \(\ker F=\operatorname{im}V\) on this module with \(H^0(A,\Omega^1_A)\), and identifies the corresponding module exact sequence with
\[
0\longrightarrow H^0(A,\Omega^1_A)
\longrightarrow H^1_{\mathrm{dR}}(A)
\longrightarrow H^1(A,\mathcal O_A)
\longrightarrow0.
\]
Proposition 5.1, printed pp. 118–119 / PDF 57–58, proves Hodge–de Rham degeneration for abelian varieties over a field; Corollary 5.2, printed p. 119 / PDF 58, does so for proper smooth curves. These are not statements for arbitrary smooth proper varieties or relative base change.

**Comparison with scans 287 and 297 and earlier cote 54:** the full finite group scheme, including its Dieudonné structure, supplies more information than its geometric points or an ordinary rational Tate module. This independently checks the narrow Oda theorem invoked in the earlier context notes at 54:7:4 and D05, where the manuscript asks whether its extension can be recovered from the \(p\)-torsion. Matching that particular restricted-Lie extension, its \(p\)-operation, and all variance conventions remains an additional task; this note does not promote the whole earlier contextual interpretation to a proved claim.

Oda’s remark after Corollary 5.11 says the result was conjectured in Grothendieck [15]. The bibliography identifies [15] as *On the de Rham cohomology of algebraic varieties* (1966). This locates Oda’s own historical reference, but does not identify the present manuscript sheets with that published conjecture.

## 4. Scans 291–292: duality retains finite information; the covariant Tate module does not

**Printed result:** Definitions 3.5–3.8 and Proposition 3.9, printed pp. 82–84 / PDF 21–23, use \(W=W(k)\), \(C=\operatorname{Frac}(W)/W\), and
\[
D(M)=\operatorname{Hom}_W(M,C),\quad
M^t=\operatorname{Hom}_W(M,W),\quad
T_p^{\mathrm{Oda}}(M)=\operatorname{Hom}_W(C,M).
\]
Proposition 3.9(i) gives the finite-type/cofinite-type duality and its free/divisible restriction; (ii) says \(D\) is a duality on finite-length modules; (vii) gives
\[
(D M)^t\simeq T_p^{\mathrm{Oda}}(M)
\]
for modules of cofinite type. Taking \(k=\mathbb F_p\) and retaining the underlying module algebra gives the same duality pattern as the manuscript.

The notation must not be silently identified:

| Construction | Scans 291–292 | Corresponding Oda construction |
|---|---|---|
| Contravariant dual into \(\mathbb Q_p/\mathbb Z_p\) | \(T_p(M)\) | \(D(M)\), after the specialization just described |
| Covariant inverse limit of \(p^n\)-torsion | \(T^p(M)\) | Oda’s \(T_p(M)\) |
| Integral dual of the contravariant dual | \(\operatorname{Hom}(T_p(M),\mathbb Z_p)\) | \((D M)^t\) |

**Own elementary example:** applying the covariant \(T^p\) to
\[
0\to\mathbb Z/p\mathbb Z\to\mathbb Q_p/\mathbb Z_p
\xrightarrow{p}\mathbb Q_p/\mathbb Z_p\to0
\]
gives \(0\to0\to\mathbb Z_p\xrightarrow{p}\mathbb Z_p\), with finite cokernel \(\mathbb Z/p\mathbb Z\). This illustrates precisely the manuscript’s loss of finite groups and failure of exactness before passing to the isogeny category. Separately, finite group schemes in characteristic \(p\) can lose information even on taking geometric points: \(\mu_p\) has only the identity geometric point but is a nontrivial finite group scheme.

**Qualification to the written equivalence on scan 292:** there \(M,N\) are divisible groups of finite corank, but the fixed finite \(p\)-group \(H\) must be nonzero for condition (i bis) to detect the claimed saturated injection. If \(H=0\), tensor injectivity is automatic; alternatively one can quantify over all finite \(H\). This is a mathematical qualification of the frozen statement, not a change to its reading.

**RESULTS_STATE connection:** FLAGGED_149 B9 concerns whether compatible \(p\)-primary differences on all prime-to-\(p\) covers force equality. The present comparison explains why replacing finite \(p\)-primary information by a rational Tate module cannot by itself settle such a question. Oda does not address that hyperbolic-curve problem, and B9 remains at the registry’s open/unreviewed status.

## 5. The Albanese/divisible part versus the extra Picard information

**Printed results:** Theorem 4.4, printed pp. 105–106 / PDF 44–45, assumes a perfect field of characteristic \(p\), proper \(X\), a \(k\)-point, \(H^0(X,\mathcal O_X)=k\), and proper \(\operatorname{Pic}_{X/k}^{\tau}\). Its part (2) identifies the module attached to all \(p\)-primary Picard torsion with \(I(X)\); part (5) identifies the module attached to the \(p\)-divisible group of \((\operatorname{Pic}^0_{X/k})_{\mathrm{red}}\) with the submodule of \(p\)-divisible elements of \(I(X)\). Part (4) computes reduced Picard dimension from \(H^1(X,W_X)/V H^1(X,W_X)\).

Proposition 4.9, printed p. 113 / PDF 52, under the same hypotheses, says
\[
I(\operatorname{Alb}X)\hookrightarrow I(X)
\]
has exactly the \(p\)-divisible part as image; dually
\[
H_1(X_{p\text{-flat}})\twoheadrightarrow
H_1((\operatorname{Alb}X)_{p\text{-flat}})
\]
has the \(p\)-torsion submodule as kernel. Thus the reduced abelian part and the additional finite-length information are explicitly separated in Oda’s theory. This bears on scans 285–288 and 291–294, without giving a relative flatness theorem.

## 6. Scans 289–290: special-fibre divisibility is a saturation question

**Printed results:** Corollary 1.3, printed pp. 69–70 / PDF 8–9, gives \(\operatorname{Pic}^{\tau}=\operatorname{Pic}^{0}\) for an abelian scheme when its Picard scheme exists, and identifies the kernel of a dual isogeny with the Cartier dual of the original kernel. The former assertion is the absence of torsion in the Néron–Severi group, not the absence of torsion points on the abelian variety. Proposition 1.8, printed p. 74 / PDF 13, identifies the \(p\)-divisible group of the dual abelian scheme with the Serre dual; Proposition 1.10, printed p. 75 / PDF 14, gives base-extension compatibility and faithfulness for the indicated map from homomorphisms to homomorphisms of \(p\)-divisible groups.

**Comparison:** the manuscript’s assertion that a section of \(\operatorname{NS}_{C/S}\) becomes divisible by \(p\) on the special fibre does not conflict with torsion-freeness of each abelian fibre’s Néron–Severi group. It concerns whether a specialization image is \(p\)-saturated. Oda’s faithfulness and duality statements do not say that divisibility lifts through specialization and do not prove the finite-subgroup construction on these sheets.

**RESULTS_STATE connection:** “Hua, findings register, 57-ns-p-divisibility-generization” directly points to these two scans, using their earlier numbering 288–289. The frozen witness explicitly discusses equal as well as unequal characteristic, so the registry’s mixed-characteristic formulation is narrower than the manuscript’s stated reach. The registry’s comparison with Maulik–Poonen Example 3.12 was not verified here; neither that comparison nor the subgroup construction is promoted to a proved result by the Oda comparison.

## 7. Scans 294, 311, 313: pointwise divisibility does not answer the relative questions

**Printed result with crucial hypotheses:** Proposition 2.1, printed p. 79 / PDF 18, works over a characteristic-\(p\) base with a section of \(X/S\) and \(\eta_*\mathcal O_X=\mathcal O_S\). It compares Frobenius-twisted Picard functors and the Picard functor of the Frobenius twist of \(X\), factoring multiplication by \(p\). Its final identification of Verschiebung assumes that the Picard functor is representable and flat over the base and that its Frobenius is an epimorphism. Corollary 2.2 on the same page gives the corresponding Frobenius–Verschiebung duality for abelian schemes.

**Comparison:** flatness here is a premise, so this proposition cannot justify passing from the pointwise divisibility invoked on scan 294 to flatness of the relative Picard scheme. The field results in Theorem 4.4 and Corollary 5.12 likewise do not resolve scan 311’s universal openness, flatness, or suitable abelian-subscheme questions, or scan 313’s separatedness, variation, and correspondence-representability questions. Compatibility of the particular construction in Proposition 1.10 with base extension must not be expanded into a claim that formation of the reduced Picard variety commutes with arbitrary base change.

**A related but different meaning of “flat”:** Theorem 4.12, printed p. 115 / PDF 54, identifies \(H^1(X_{\mathrm{flat}},G_X)\) with \(\operatorname{Hom}_{\mathcal A}(M(G),I(X))\) for algebraically closed \(k\), \(H^0(X,\mathcal O_X)=k\), and commutative finite-type \(G\) killed by a power of \(p\). Corollary 4.13, printed pp. 115–116 / PDF 54–55, identifies these torsors with \(\operatorname{Ext}^1(X,G)\) for an abelian variety \(X\). These results provide a method for retaining finite flat group-scheme information of the kind appearing in scan 297; flat cohomology is not an assertion of relative flatness of \(\operatorname{Pic}_{X/S}\).

## Locator and search record

The printed PDF text was searched for the following terms; spelling and accents are unstable in extraction, so theorem numbers are the reliable anchors.

| Search terms | Exact useful location |
|---|---|
| Igusa; not reduced; Picard variety | Introduction, printed 64 / PDF 3; bibliography, printed 134 / PDF 73 |
| Cartier duality; no torsion | Corollary 1.3, printed 69–70 / PDF 8–9 |
| Serre dual; base extension | Propositions 1.8 and 1.10, printed 74–75 / PDF 13–14 |
| Picard; flat; epimorphism; Verschiebung | Proposition 2.1, printed 79 / PDF 18 |
| cofinite; Tate module; divisible | Definitions 3.5–3.8 and Proposition 3.9, printed 82–84 / PDF 21–23 |
| irregularity; p-divisible elements | Theorem 4.4, printed 105–106 / PDF 44–45 |
| Albanese; p-torsion elements | Proposition 4.9, printed 113 / PDF 52 |
| principal homogeneous; flat; Ext | Theorem 4.12 and Corollary 4.13, printed 115–116 / PDF 54–55 |
| degenerate; abelian scheme | Proposition 5.1 and Corollary 5.2, printed 118–119 / PDF 57–58 |
| Cartier operator; canonical injection | Theorem 5.10, printed 126 / PDF 65; Corollaries 5.11–5.12 and remark, printed 131–132 / PDF 70–71 |

Earlier contextual transcription/notes searches used Igusa, Dieudonn, p-divis, p-primary, Tate, tangent, and the exact cote-54 scan locators. The substantive earlier overlap is cote 54 scans 3 and 7, especially notes 54:7:4 and D05; its prior review status is preserved. The Oda comparison supplies no evidence resolving WG2 §2.4 #4’s request for a completed second Fourier-transform witness or earlier forms of cote-44 Theorems 1–7. It also does not bear directly on the unchecked centralizer hunch WG H1 merely because both discussions mention Tate modules.
