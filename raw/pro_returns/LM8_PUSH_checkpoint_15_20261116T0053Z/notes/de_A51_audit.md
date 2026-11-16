# Independent audit of A.51

**Verdict: PASS.** I read the full `notes/fgh_A51_draft.tex`, the actual covering and isotypic-factor arguments in `sections/A_heisenberg_normalizers.tex`, and the complete exact program `notes/fgh_heisenberg_polarization.py`. I independently reran the program without overwriting its JSON. The retained independent stdout is `code/de_A51_polarization_audit.out`.

## Actual cover, rotation, and cup pairing

The class-two exponent-three quotient of the rank-two free group has order27. Every epimorphism to H3 identifies this quotient, so the actual connected H3-cover established in A.50 has the square-cover kernel used by the certificate. The square elliptic model is compatible with the base CM quarter rotation.

The displayed rotation sends a vertex v(g) to v(alpha(g)x), the square centre m_g to m_alpha(g), and each radial corner to the next corner. Its horizontal and vertical edge formulas respect the actual square boundaries, have order4, and cover quarter rotation of the square torus. It and the actual order-four automorphism of A.50 are complements of the same odd deck group in the group above the four base rotations. Coprime complement conjugacy therefore identifies them up to an actual deck transformation. The entire deck-span of the elliptic quotient is unchanged; its complementary B^3 is the same isotypic factor, and the noncentral order-three projector chooses an isogenous copy of B.

I checked the cup sign independently. A positively oriented triangle has order (centre,a,b). If a<b, cyclically ordering it as (a,b,centre) preserves orientation; if a>b, it reverses orientation. The ordered first edge differs from the stored edge by the corresponding sign, and the second ordered edge is minus the radial edge to the larger vertex. The product is exactly minus epsilon times the two specified cochain values. Multiple global edges cause no problem for the ordered triangular complex.

The spanning-tree gauge removes every coboundary uniquely, and the remaining linear equations compute the actual H1. The independent exact run reproduces rank20, the nonsingular alternating cup matrix with determinant1, every deck/rotation relation, all projector ranks, and the retained F-basis cup matrix. The projectors are rational expressions in actual Jacobian endomorphisms; the calculation does not assign an unproved geometric interpretation to a numerical subspace.

## Hodge and quaternion steps

I checked all listed differential orders. At a finite branch point, dx has order2 and z order1; at infinity, x,y,z,dx have orders -6,-9,-8,-7. The ten listed forms, including the invariant elliptic differential, are holomorphic and independent. The central multiplicities are3 and6. Removing the three translates of the displayed elliptic differential from the larger multiplicity leaves B with balanced F-signature(1,1). Inverse pullback exchanges the two embeddings but preserves this balance.

The Hermitian formula is linear in the first variable and conjugate-linear in the second, using kappa-adjoint=-kappa for the symplectic pairing. Its displayed matrix is diag(-1/6,1/3). The Hodge circle has determinant1 over F and preserves this form; it lies in SU(h), without any required equality with that full group. The anti-linear matrix [[0,-2],[-1,0]] is six times the adjugate anti-linear operator for this diagonal form. The determinant-one isometry equations directly verify commutation. Its square is2 and it anticommutes with kappa, yielding the actual rational quaternion algebra (-3,2).

I independently reopened Milne, *Shimura varieties and moduli*, https://www.jmilne.org/math/xnotes/svhIP.pdf, Theorems4.4 and7.12, printed489 and508 (`turn765view0`, `turn767view0`, `turn767view1`). The categorical equivalence gives precisely the rational full-faithfulness needed after clearing lattice denominators; it is not a conjectural Hodge-cycle assertion. The opposite-algebra convention on cohomology leaves the same quaternion algebra. The usual rigidity of abelian-variety homomorphisms gives definition over a finite algebraic extension.

## Reduction and cusp criterion

The quadratic extension Q3(sqrt(-3))/Q3 is ramified, and a unit norm has square residue. Thus2 is not a norm, proving the quaternion algebra is division at3. Every nonzero unital module over it has Q3-dimension at least4. After semistable reduction and definition of the endomorphisms, the torus character space tensored with Q3 has dimension at most2 and inherits a unital action, so it is zero. This gives potential good reduction. The same argument applies to the étale part of the special three-divisible group, of dimension at most2, giving three-rank0. I suggested explicitly adding the Q3 tensor in the toric sentence. The Néron extension and specialization argument is the already verified Serre–Tate input; the dimension argument itself is checked here.

The elliptic factors have the stated special three-rank0, and isogeny invariance passes the conclusion to the full Jacobian. Pullback of the principal divisor3(T-U) along the totally ramified cubic map gives exactly9(P_T-P_U). Such torsion specializes to zero in the good special Jacobian with three-rank0.

After separating the marks, the stable compact-type model has the same good Jacobian. A positive-genus component embeds under the Abel map; its intersections with images of other components occur at nodes. Distinct smooth marks with equal Abel image must therefore lie in the same rational subtree, including their marked endpoint components. The nine distinct cusps ensure that each selected cusp has a partner. This is exactly the already proved A.42 sufficient criterion, including its integral fixed-inertia conclusion at every coefficient prime.
