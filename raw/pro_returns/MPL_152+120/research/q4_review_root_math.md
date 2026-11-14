# Independent check of the requested algebra and combinatorics

Reviewed `root_152.md` P05, P06, P10–P12 and P16, and `root_q2.md` R02–R03. I read only the frozen text needed for the 152 formulas (scans 4, 5, 7, 8, 10, 11 and 13); no supplied images, new literature search, or edits to the parent's files were made. This checks the displayed constructions, not uninspected external historical assertions.

## Conclusions and qualifications

No mathematical error was found in the explicit calculations. The principal qualification concerns P06: the simultaneous-reversal orbit identifies **isomorphism classes** of torsor data; its stabilizer must be retained in a groupoid-level statement. R03 becomes precisely typed by viewing the ordinary exit category as a locally discrete 2-category and using the stated two-object model.

### P05 — Three edges

For the linearly ordered edge set \(1<2<3\), the adjacent pairs are \(\{1,2\}\) and \(\{2,3\}\). The only two-element orbit of \((1\,3)\) is neither one, and the permutation is not the identity. This verifies the stated finite test. The point \(2\) is fixed, whereas scan 10's boxed criterion belongs to the earlier fixed-point-free setup; P05's wording correctly treats this as a comparison problem involving fixed edges and the boundary convention, not a disproof of that full boxed statement.

### P06 — Torsor and reversal

Write \(r=c(e)\). Equivariance gives \(c(\tau e)=r^{\mathrm{opp}}\), so the orbit \(\{r,r^{\mathrm{opp}}\}\) is independent of the choice of \(e\). Conversely, the free two-element torsor with map \(0\mapsto r\), \(1\mapsto r^{\mathrm{opp}}\) represents this orbit, including the constant-map case.

For fixed underlying tree, the automorphism swapping the two torsor elements preserves \(c\) exactly when \(r=r^{\mathrm{opp}}\). Thus a reversal-fixed system contributes a \(C_2\) stabilizer. The orbit description in P06/P15 is correct at the data/isomorphism-class level; the groupoid retains the action-groupoid stabilizers. The projection from this action groupoid to its discrete orbit set sends that automorphism group \(C_2\) to \(1\) and therefore is not faithful.

### P10 — Cancellation

On one identified set, the two equalities imply \(\rho_C=\rho_C\sigma_C\). Left composition by the inverse permutation gives \(\sigma_C=\mathrm{id}\). The stated nonempty-set condition is necessary: on the empty set the identity permutation is vacuously fixed-point-free. P10 includes the condition and is correct.

### P11 — Permutation functors

With \(\alpha^2=1\), the equations \(b=v\alpha\) and \(v=b\alpha\) are inverse object constructions. For a bijection preserving \(\alpha\) and \(v\),

\[
fb=fv\alpha=v'f\alpha=v'\alpha'f=b'f.
\]

Conversely, preservation of \(\alpha\) and \(b\) gives \(fv=fb\alpha=b'f\alpha=b'\alpha'f=v'f\). The assignment leaves every underlying bijection unchanged, hence preserves identities and composition. The intended objects are finite dart sets with fixed-point-free \(\alpha\); vertex cycles of \(v\) encode graphs without isolated vertices, matching the source's scope. A point tree needs separately recorded vertex data and is already excluded at the relevant contour passage.

### P12 — Disk dual tree

The pairwise-disjoint properly embedded chords have distinct endpoints. After cutting along the previous chords, each remaining chord lies in one disk region and splits it into two; the dual operation replaces one vertex by two joined by the new edge. Starting from one vertex proves connectivity and the counts \(V=n+1\), \(E=n\), or directly proves the tree assertion by induction. Removing a chord merges its neighboring regions, corresponding to **contracting** its dual edge; this is the reversal of the step described in P12.

### P16 — Forgetting cyclic orders

The object assignment preserves the underlying labelled incidence tree. The arrow assignment is the same graph isomorphism, so it preserves identity maps and composition exactly. Fixing the label set and specifying external flags as legs makes the source and target groupoids fully explicit. When matching a particular stable-moduli indexing category, its convention about component vertices and minimum label count should be stated; the displayed forgetful functor itself is valid independently of that further match, which P16 does not claim to have completed.

### R02 — Extension automorphisms

For abelian \(A\), every group homomorphism \(\phi\) fixing \(\{0\}\times A\) pointwise and inducing the identity on the quotient has \(\phi(1,0)=(1,a)\) and

\[
\phi(n,b)=n\phi(1,0)+\phi(0,b)=(n,na+b).
\]

Every such map is invertible, with inverse corresponding to \(-a\). Composition corresponds to addition in \(A\), so the explicit automorphism-group identification is correct. The abelian and pointwise-fixed-band hypotheses in the note are essential to this exact formula and are present.

### R03 — Truncation

In the stated skeletal model, the only nontrivial hom-groupoid is the one-object groupoid with automorphism group \(\mathbb Z\) attached to the displayed arrow. Passing to connected components of this hom-groupoid leaves one arrow; the unique map \(\mathbb Z\to1\) respects vertical composition, and the remaining compositions involve identity arrows. This gives the displayed truncation 2-functor to the locally discrete ordinary category. A functor from that one-object hom-groupoid into a functor category is specified by a functor and an invertible natural transformation representing the generator of \(\mathbb Z\), as claimed.

Recorded after the requested independent review on 2026-11-14.
