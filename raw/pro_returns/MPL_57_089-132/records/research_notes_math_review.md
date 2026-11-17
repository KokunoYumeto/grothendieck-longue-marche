# Mathematical review of the completed research notes

**Review date:** 2026-11-17.  
**Reviewer:** delegated post-freeze mathematical/context reviewer.  
**File reviewed:** MPL_57_089-132_notes.md, especially C01–C13, D01–D09, E01–E09, the standing-question tables, the research-register table, and the limited published comparisons.

## Outcome

**No blocking mathematical issue remains in the reviewed scope.** The final wording incorporates the precision changes reported during review: the nonintegral-localization caution in D01, explicit edge hypotheses in D07, the published gluing hypotheses in E07, and the distinction between \(k^\times\) and the group functor \(\mathbf G_m\) in E09. C13 is explicitly a test of the opposite-fibre density inference and is not presented as a counterexample satisfying the complete Picard hypothesis of the manuscript corollary.

This review does not certify every asserted manuscript theorem. In particular, the full generic-hyperplane torsor theorem, the Seshadri argument under the exact edited hypotheses, and the general relative-existence construction remain incomplete written arguments in the research notes. The notes correctly distinguish those limitations from the explicit elementary deductions that can be checked here.

No source image was opened in this review. No page transcription, combined transcription, doubts file, inventory, freeze manifest, or main notes file was edited by this reviewer. The only files written were this report and the separate context_hyperplane_review.md memo.

## Checks and dispositions

| Notes | Mathematical issue checked | Final disposition |
|---|---|---|
| C01, C05, C06 | Fibrewise \(S_2\), separability/\(R_0\), integrality, and the global-functions/rigidification assumptions are different hypotheses. | The final notes preserve the mismatch between the opening statement and later uses of integral fibres. They do not silently replace the source by Hua's stronger modern statement. |
| C02, C07, C10 | Effectiveness, normalization by a uniformizer, vanishing of a vertical difference, and the cancelled proof version. | The positive-divisor restriction and cancelled non-effective reduction remain authorial limitations. The live Cartier objective is not said to have been withdrawn merely because one proof version was cancelled. |
| C03–C04 | Closure of the rational Picard section, countability/discreteness, Main Theorem, and universal openness. | The notes identify the missing finiteness and fibre arguments instead of treating the compressed sketch as a completed proof. |
| C08–C09 | Functorial valuative extension versus representability; relative complete intersections over a normal base versus absolute local complete-intersection hypotheses. | The proposed weakenings remain questions. No published absolute theorem is asserted to settle the relative question automatically. |
| C11–C13 | Density of the simultaneous smooth locus and properness after restriction to it. | Both obligations are correctly separated. The insertion on scan114 suggests applying the theorem on all of \(R\); this is a qualified reading/proof question, not a transcription change. |
| D01–D02 | Rank-one intersections, regularity of \(f\), reduced \(A/fA\), valuation vectors, and the nonintegral notation. | The final D01 now describes the source's argument and its notation warning. D02 does not assert that every valuation vector is realized or diagonal. |
| D03–D04 | The nonaffine counterexample and the local nilradical argument. | Both are valid explicit editorial deductions with high confidence; neither is attributed to a completed source proof. |
| D05–D07 | The “Non démontré” and reducedness warnings; propagation of exponents across an incidence graph. | The warnings remain visible. D07 now requires integral edge intersections meeting both \(D(f)\) and \(Y\), together with the relevant compatible unit factorizations. Its medium-confidence status correctly concerns a conditional completion proposal. |
| D08–D09 | Literal triviality, pullback from a base, a relative Picard class, and the closed equality/triviality locus. | The final notes keep these distinctions and retain the uncertain universal degree-zero hypothesis and the visible component-count assumption. |
| E01–E04 | Conditional descent hypotheses, functor bases, the cancelled Weil-restriction factor, the third rigidification condition, and affine Hom/Isom parameters. | The notes do not claim unconditional Picard-scheme existence. They identify the additional source condition c) and target \(P\), and leave parameter representability as a separate obligation. |
| E05 | Joint dependence of condition b) on \(\varphi\) and \(\psi\). | The dependency objection is correct. The proposed simultaneous equalizer on \(K\times_S L\) is conditional on E04's affine separated parameter targets; suppressed dependence over \(K\) remains an explicitly allowed explanation of the shorthand. |
| E06 | Connectedness, intersection rational points, and the final restart on scan131. | The note matches the live restart and unfinished last line; it does not promote the cleaned modern narrative into a finished manuscript proof. |
| E07–E08 | Exact scope of the cited existence results and the scheme/algebraic-space distinction. | The final hypotheses and conclusions are correctly qualified. No chronology or verification of the manuscript's edited construction is inferred from the published comparators. |
| E09 | Gluing two rational components at two nodes. | The final note distinguishes the kernel on \(k\)-points from the kernel of Picard functors and correctly identifies the latter as a torus in this example. |

## Independent verification of the elementary deductions

### The nonaffine target test

For \(X=\operatorname{Spec}k[x,y]\), \(f=x\), and \(Z=X\times\mathbf P^1\), the section \([x:y]\) is defined on \(D(x)\) and near the generic point of \(V(x)\). If it extended at the origin, its restrictions to the two axes would have the different constant limiting values \([1:0]\) and \([0:1]\); uniqueness of extension into the separated target gives a contradiction. The polynomial example is regular/excellent, \(f\) is a nonzerodivisor, and \(X/f\) is reduced, so the intended ring/divisor conditions are retained.

### Reducedness at the boundary

For the noetherian local ring \(A=\mathcal O_{X,y}\), let \(N\) be its nilradical. Reduced \(A/fA\) gives \(N\subset fA\); if \(n=fa\) is nilpotent, regularity of \(f\) gives \(a\in N\), hence \(N=fN\). Since \(f\) lies in the maximal ideal and \(N\) is finitely generated, Nakayama gives \(N=0\). This establishes precisely the local redundancy claimed in D04, without asserting that the whole extension proposition has thereby been proved.

### The limited density test

For a singular geometrically normal proper variety \(Y/\mathbf C\), the smooth loci of the two projections \(Y\times Y\to Y\) are \(Y\times Y_{\mathrm{sm}}\) and \(Y_{\mathrm{sm}}\times Y\). Their intersection misses fibres over singular points under either projection. This validates C13 as a test of the density inference alone; the note expressly does not claim that the full extra Picard hypothesis has been checked.

### The conditional incidence step

On an integral edge intersection meeting \(D(f)\), compatible factorizations can be compared in its function field. At a point of that edge lying in \(Y\), the factor \(f\) is a nonunit while the restricted coefficients are units, so \(f^{n_i-n_j}\) cannot equal a unit for a positive exponent difference. Thus the exponents agree along an edge, and connectedness gives a diagonal vector once all the explicitly stated factorization and edge hypotheses hold.

### The two-node gluing test

For two copies of \(\mathbf P^1\) joined at two distinct pairs of points, componentwise trivial bundles have two gluing scalars. Changing the component trivializations changes both by the same ratio, leaving their quotient as one multiplicative parameter. This gives \(k^\times\) on points and, by the identical gluing calculation over varying bases, the group functor \(\mathbf G_m\). The revised E09 correctly keeps those two formulations separate.

## Standing tables, attribution, and external-source limits

The standing-question table preserves the difference between live requests, cancelled proof text, uncertain readings, and editorial answers. In particular, the scan120 answers are explicitly editorial, the scan122–123 incidence obstruction remains open as written, and the scan131 restart is not treated as a completed argument. The register table makes no unsupported upgrade to the GT, CM, section-class, higher-Jacobian, or Fourier questions.

The final published comparisons were checked against the exact passages already retrieved by the primary editor and this reviewer. Their placement is appropriate: B03 remains conditional, E07 is a close gluing comparator, and E08 retains its algebraic-space conclusion. The SGA2 inequality-bar caveat honestly reports the extraction limitation and does not claim an unavailable visual check.

The separate context_hyperplane_review.md memo was revised to attribute “sans partie fixe” only to the frozen manuscript, not Hua, and to replace duplicated published theorem summaries with short reference notices. URLs, exact passage locators and the retrieval log remain in that memo; the fuller comparison is in the main notes. No additional literature research was undertaken during this final check.

## Residual limits

There is no outstanding correction requested by this reviewer. The unresolved items are the mathematical and textual obligations already marked in the notes, especially the precise scope of \(G\), the original-field/base-changed distinction, the Seshadri hypotheses and compressed geometric steps, the vertical-divisor factorization, and the affine parameter construction. Final mechanical validation, frozen-file hash verification and ZIP assembly remain the primary editor's separate checks.
