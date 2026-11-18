# Independent targeted review of elliptic algebra

**Reviewer:** GPT-6 Astra Pro; effort not exposed; octahedron_research subtask.  
**Scope:** `research/elliptic/proofs.md` P1–P4, notes E01–E05 and E13, the frozen scan100 wording, and the relevant supplied Hua XII passages. This is a mathematical review after transcription freeze; no elliptic file or transcription file was changed.

## Verdict

No substantive mathematical error was found in the three requested arguments. The qualifications already present in the elliptic notes should remain: E03 is conditional on a broad reading of an obscured corollary; the conjugacy classification uses a PID **domain** with k/2k a field; and the real-form discussion uses origin-preserving elliptic curves and the central [−1] quadratic twist.

### Module–triple equivalence: P1, E01–E02

The two constructions are inverse up to the stated natural multiplication-by-two isomorphisms. Under the injection P⊕Q→M by addition, the element 2x has components (x+σx,x−σx), and injectivity of 2 gives N∩P=2P and N∩Q=2Q. Conversely, the inverse image N of m has eigenspaces exactly 2P and 2Q; after identifying those with P,Q, the new gluing module 2N/(4P⊕4Q) identifies with the original m. All maps are k-linear because 2 is central even when k is noncommutative, and the stated condition on morphisms gives naturality. No finite generation or projectivity hypothesis was silently used.

### Rank-two classification and the arithmetic counterexample: P2–P3, E03–E05

For free rank-one eigenspaces, automorphisms are multiplication by units, so the ratio of their reductions changes a nonzero graph slope precisely by image(k×). Over a PID, the inverse-image module is a free rank-two submodule of P⊕Q, hence every permitted slope is realized on k². For the displayed A_λ, useful explicit primitive eigenvectors are p=(2,−λ), q=(0,1); the map x↦x+σx, x↦x−σx sends (x,y) to coordinates (x,λx+2y), so its gluing slope is indeed λ, not an inverse or a quotient with extra identifications. Intertwiners preserve the + and − eigenspaces separately, so a hidden exchange of eigenspaces does not merge these classes.

For k=Z[ω], ω=(1+√−11)/2, the nearest-ω-coefficient and nearest-real-part choices give norm at most 1/4+11/16=15/16<1, proving norm-Euclideanity. The norm formula forces the units to be ±1, and t²+t+1 modulo 2 is irreducible, giving F₄ with trivial image of the unit group. Therefore there are exactly three nonsplit classes plus the split class under the stated hypotheses. The Q×Q example in P2 also correctly defeats constant rank-one eigenspaces under the broader retained hypotheses, but the reading qualification in E03 is essential and has not been removed.

### Square real forms and quadratic twisting: P4, E13

For the square lattice let r be a quarter turn and σ an axis reflection. Then rσr⁻¹=r²σ=−σ, so multiplication of the descent cocycle by the central automorphism −1 is a coboundary and preserves the real isomorphism class. Equivalently, on the usual j=1728 Weierstrass equation y²=x³+A x, the quadratic twist by d=−1 leaves A d²=A; the second real form changes the sign class of A and is a quartic, not this quadratic, twist. Thus Hua XII's unqualified assertion that the two real forms are always related by the −1 quadratic twist is indeed false in the square case, while the count of two origin-preserving real forms is unchanged. This review does not classify arbitrary real genus-one torsors or automorphisms allowing translations.

## Suggested integration

No correction is needed. If a short clarifier is desired, the eigenvectors p=(2,−λ), q=(0,1) and their residue calculation make the explicit counterexample matrices immediately checkable; this is optional exposition, not a missing premise.
