# Independent audit of A.46

Status: **PASS**, 15 November 2026, by the D/E agent, after reading
`notes/root_A46_draft.tex` in full and the exact A.11 statement/proof.

The stronger assertion excluding every one-dimensional **Q_p** subquotient
is correct. After passing to a finite local good-reduction extension k,
crystalline subquotient closure and exactness apply. Dualizing converts a
subquotient of the covariant Tate module into a subquotient of first
cohomology, so all ambient slopes are in (0,1). The p-rank removes slope
zero and polarization symmetry removes slope one; finite extension of
the residue field preserves the normalized slopes.

For a rank-one isocrystal over the maximal unramified subfield k_0, write
phi(e)=a e. If f=[k_0:Q_p], phi^f has eigenvalue Norm(a), whose normalized
slope is v_p(Norm(a))/f=v_p(a), an integer. This calculation is unchanged
by arbitrary ramification of k/Q_p. In an exact sequence of isocrystals,
the characteristic polynomials of phi^f multiply, so a subquotient slope
must be an ambient slope. There is no integer in (0,1).

The coefficient restriction is essential: an E-line after extending
Q_p coefficients need not yield a rank-one k_0-isocrystal. The draft
expressly avoids that false strengthening. The argument includes p=2
and does not use Hodge--Tate sign conventions, weak-admissibility
bookkeeping, semisimplicity, or a splitting of the arithmetic normalizer.

For each finite global extension, restrict its proposed line/subquotient
to a completion above the chosen place, then to a finite good-reduction
extension. This proves the required quantifier. The final normalizer
step is exactly A.11: noncuspidality gives a nonzero proper-homology image,
and inner geometric actions are trivial there, making its rational span
stable under an open arithmetic image.

## Independently opened primary sources

- Brinon--Conrad, *CMI Summer School Notes on p-adic Hodge Theory*,
  <https://math.stanford.edu/~conrad/papers/notes.pdf>, Theorem 5.2.1 on
  printed p.68, Proposition 9.1.6 on p.131, and the discussion before
  Proposition 9.1.9 on p.133. These give subquotient closure, exactness,
  dimension preservation, duality, and the regularity needed for the
  crystalline functor. Opened refs: turn681view0, turn682view2,
  turn683view0.
- Achter--Pries, *Generic Newton polygons for curves of given p-rank*,
  <https://www.math.colostate.edu/~achter/math/hp1113.pdf>, Sections
  2.2.1 and 2.2.3, manuscript pp.3--5. The slope interval, symmetry,
  finite-field extension invariance, and p-rank equality appear
  explicitly. Opened refs: turn682view0, turn683view1.
- Faltings, *Almost etale extensions*, Asterisque 279 (2002),
  <https://www.numdam.org/item/AST_2002__279__185_0.pdf>, Section 5,
  Corollary 4 and Remarks 1--5, printed pp.256--258. Inverting the period
  in the comparison and inverse gives the smooth proper constant
  coefficient comparison; the remarks state Galois/Frobenius
  compatibility and the constant-coefficient passage to Q_p.
  Opened refs: turn684view0, turn685view0, turn685view1.

No numerical experiment is needed for this structural proof.
