# Independent formula QA after freeze

## Scope and overall finding

Reviewed the frozen typed formulas and the inputs/outputs of scripts/check_reused_root_formulas.py and records/reused_root_formula_checks.json. No images were viewed, no transcription was changed, and no duplicate numerical test was run. The reported numerical results are correct; the main qualification is that the scan005 examples test one clause of an already inconsistent literal definition.

These are mathematical checks of the frozen wording, not proposed transcription emendations. They do not establish the intended source text, its authorship, or hypotheses that may have appeared on a preceding leaf.

## 1. Scan005: two separate defects in the displayed contraction rule

**Locus:** scan005:12,16. The condition \(h\ne i\ \text{ou}\ k\ne i\) includes the entries \((i,k)\) with \(k\ne i,j\), so the unchanged-entry clause already assigns \(m'_{ik}=m_{ik}\), while the next clause assigns \(m'_{ik}=m_{ik}+m_{jk}\). Thus the complete literal definition does not define a matrix; the JSON's A3 and D4 calculations must be presented conditionally as tests of the latter sum clause.

Under that sum clause, contracting an end edge of A3 gives \(m'_{ik}=2+3=5\), whereas the asserted identity would require
\[
-\cos(\pi/5)=-\cos(\pi/2)-\cos(\pi/3)=-1/2.
\]
The left side is \(-(1+\sqrt5)/4\), so the identity fails. Contracting a central-to-leaf edge in D4 analogously gives a three-vertex chain with two labels 5 and Gram determinant \((1-\sqrt5)/4<0\), exactly as reported.

For comparison only, on the forest assumed in the paragraph, at least one of \(m_{ik},m_{jk}\) is 2; retaining the nontrivial edge label gives \(m'_{ik}=\max(m_{ik},m_{jk})=m_{ik}+m_{jk}-2\). That and an unchanged-entry condition requiring both indices to avoid \(i\) would fit the stated Gram argument, but neither correction is a new reading of the frozen page.

## 2. Scan035: the Cartan integer is asymmetric

**Locus:** scan035:8–15. With its explicit convention \(n(u,v)=2(u\mid v)/(u\mid u)\), the JSON's \(u=(1,-1)\), \(v=(0,1)\) gives \(n(u,v)=-1\), \(\|v\|^2/\|u\|^2=1/2\), and \(n(v,u)=-2\). Their reflections have product of order 4, so the literal inference from \(n(u,v)=-1\) to equal lengths and order 3 is false for arbitrary ordered simple roots.

The controlling relations are
\[
\frac{n(u,v)}{n(v,u)}=\frac{\|v\|^2}{\|u\|^2},
\qquad
n(u,v)n(v,u)=4\cos^2\angle(u,v).
\]
The printed list becomes valid if one first chooses \(\|u\|\leq\|v\|\). This is a missing ordering hypothesis in the visible paragraph, not evidence that the source uses the other Cartan convention.

## 3. Scan023: the factor 13 makes the literal exponent equation impossible

**Locus:** scan023:33–42. The factor \(12+1\) forces 13 to divide \(2^7 3^4 5\), which it does not. Equivalently, the remaining product is exactly \(540/13\), so no integer \(m,m'\) can satisfy the printed equation, independently of their sum.

Using \(11+1\), as suggested by the preceding list ending in 11, instead gives \((m+1)(m'+1)=45\). Together with \(m+m'=12\), this gives \(mm'=32\), hence the unordered pair \(\{4,8\}\). The JSON is correct; this is a conditional algebraic reconciliation, not a visual decision between 11 and 12.

## 4. Scans037/049: the weight data force a positive pairing

**Locus:** scan049:7,9,11–30 and scan037:7–35. The eight coordinate columns and eight simple-root expansions used by the script match the frozen displayed data. The recovered simple roots, their squared norms 2, and both sums for \(\rho\) are consistent.

There is also a shorter independent sign check: scan037 explicitly identifies \(\widetilde\alpha=\omega_8\), while scan049 defines the weights as dual to the coroots and identifies coroot coordinates with root coordinates in this normalization. Therefore \((\widetilde\alpha\mid\alpha_8)=1\); equivalently, the recovered \(\alpha_8=\varepsilon_7-\varepsilon_6\) pairs with \(\widetilde\alpha=\varepsilon_7+\varepsilon_8\) to give 1. The displayed \(-1\) in scan049:7 is inconsistent with those same-page/cross-page data.

A positive rescaling of the scalar product cannot reverse this sign. Pairing the negative highest root with \(\alpha_8\) would give \(-1\), but the leaf names the positive highest root; that distinction is a possible source-comparison question, not a correction.

## 5. Scan013: the endpoint formula excludes rank one

**Locus:** scan013:5,7,11–19. The range explicitly permits \(\ell=1\), when \(\widetilde\alpha=\alpha_1\) and \((\widetilde\alpha\mid\alpha_1)=2\). The two endpoint pairings equal 1 for \(\ell\geq2\), when the endpoint simple roots are distinct; the visible formula needs this boundary exception. The remaining A1 statements on this leaf do not fail for that reason.

## 6. Scan015: roadmap wording differs from the computations

**Locus:** scan015:23 versus scan023:6–12 and scan037:29–35. The roadmap promises the sum of positive roots; the later item VII explicitly computes their half-sum \(\rho\). This is a factor-two discrepancy in the roadmap's wording, not a reason to double the later formulas, which are independently consistent with the sums of fundamental weights.

## 7. Scan031: retain the order issue as a collation question

**Locus:** scan031:25–35,41–44 versus scan049:7. The former says the order induced by lexicographic order, while the latter refers to the opposite lexicographic order. Without the missing definition and coordinate-order convention in source no. 10, these words alone do not justify changing a positive system. The orthogonality argument selecting \(\alpha_1,\ldots,\alpha_7\) is unaffected by whether the one nonzero pairing with \(\alpha_8\) is written with either sign; identifying the intended order remains a separate matter.

## 8. Reducibility: distinguish the normalization, proposition, and corollary

**Locus:** scan035:23–33 and scan033:16–40. For reduced systems in the usual sense allowing orthogonal direct sums, the global length assertion needs additional scope: \(B_2\oplus G_2\), with short roots in both components of length 1, has all three squared lengths \(1,2,3\), contrary to the assertion that only \(1,2\) or only \(1,3\) occur. Independently scaling one component can even make the proposed global labels leave \(\{1,2,3\}\).

**The single-rescaling step in scan033 is not by itself a counterexample:** if its diagram hypothesis uses the literal globally normalized labels \(f(v)=\|v\|^2/\lambda^2\), matching labels fixes the relative scales across all components, and one global rescaling does align their Gram matrices. If diagrams are instead normalized separately on each component, the proof needs separate rescalings, although a linear root-system isomorphism can still exist.

The corollary involving the full subgroup of \(\mathrm{GL}(V)\) has a distinct reducible issue even when the literal labels are defined. For \(R=\{\pm e_1,\pm\sqrt2 e_2\}\), the two isolated vertices have labels 1 and 2, so the labeled graph has trivial automorphism group; nevertheless the linear map exchanging \(e_1\) and \(\sqrt2 e_2\) preserves \(R\) and is not a Weyl sign change. Thus \(A(R)/W(R)\) contains the component swap, whereas the labeled-graph automorphism group does not. This example concerns the visible global labels and the explicitly stated \(\mathrm{GL}\) group; an irreducibility assumption or a componentwise diagram convention would change the scope.
