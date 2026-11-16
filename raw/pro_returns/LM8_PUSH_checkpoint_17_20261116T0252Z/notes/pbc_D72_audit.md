# Independent audit of D.72

**Verdict: PASS.** Read the complete candidate
`notes/de_class2_compact_draft.tex` on 2026-11-15. This audit is relative to
the already checked integral Hall-coordinate input in D.68 and the actual
generic cusp statements D.70/D.71; it does not replace their proofs.

The new finite-support step is sound. At a good place away from the coefficient
prime, the affine abelianization has proper weights one and boundary weights
two, with the indicated arithmetic-Frobenius convention. A degree-j free Lie
factor is a rational subquotient of the j-fold tensor product, so all its
eigenweights are at least j. For j at least three this excludes the tame
eigenvalue q, even when the boundary points are nonsplit and even without
semisimplicity. An unrestricted integral central one-cocycle restricts to a
homomorphism on inertia; its tame value b satisfies F(b)=q b. Torsion-freeness
therefore forces its entire inertia restriction to vanish. Killing the closed
normal closure is justified by the associated affine representation. This
proves actual cocycle factorization through one fixed finite-ramification
quotient, rather than merely a statement about rational cohomology classes.

Finite H1 for each finite coefficient, finite H0 and its Mittag--Leffler
property, and the coefficient exact sequence give compact integral H1 with
finite reduction modulo ell. Compact Nakayama then gives finite generation.
Adding actual coboundaries of a lattice basis proves finite generation and
uniform compactness of the actual Z1 module. The argument uses neither a
degree-two cohomological-dimension assertion at real places nor vanishing of
torsion in H1, so it includes ell=2.

The actual-coboundary submodule in a finite coefficient parameter module is
indeed closed: Noetherianity makes it finitely generated, and the basis map
from a compact finite power of Z_ell has exactly that submodule as image.
This does not assert that all global coboundaries form a closed subspace.
Choosing primitives of its finite basis and extending the coordinate inverse
rationally preserves finite polynomial cochain families. Rational Hall
denominators are bounded at each fixed class and absorbed into the finite
list of cochains; the parameter polynomials can therefore be integral.
The induction covers every exact lift because two central lifts differ by
an actual one-cocycle, including its coboundary part.

The positive-weight argument also excludes fixed elements in V and L2.
Twisting changes neither associated graded action. Thus the class-two
stabilizer is trivial, and exact representatives are quotiented precisely
by the compact kernel to class two. The resulting fibres are compact
Hausdorff. Separate higher-stage liftability gives nonempty compact exact
fibres; every finite compatibility condition is met at its highest stage,
so the inverse-limit construction gives an actual continuous pro-ell
cocycle. The uniform topology assertion follows because each finite
ell-group quotient is nilpotent and factors through a finite class.
Compact conjugator sets resolve the remaining inverse-limit conjugacy issue.

The rank-two metabelian extension uses its actual integral Alexander/Hall
coordinates, and only asserts compactness and compatibility, not generic
singleton metabelian fibres. The final nested-image argument proves finite
failure and uniform exclusion off a cusp neighborhood once D.70 or D.71
supplies the actual singleton full pro-ell fibre. The all-prime product is
explicitly the pronilpotent tower. No implication that pro-prime quotients
jointly distinguish arbitrary full profinite geometric elements is used.

No mathematical correction is required. In particular, fixing class two is
essential: the degree-two proper-proper factor can have eigenvalue q, as it
does for a punctured elliptic curve, so the proof does not claim compactness
after fixing only the abelian cocycle.
