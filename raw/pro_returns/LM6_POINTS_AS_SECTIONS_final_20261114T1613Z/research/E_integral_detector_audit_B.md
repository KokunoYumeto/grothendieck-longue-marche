# Independent review of E.37–E.38

Reviewer: sections_b. Reviewed 14 November 2026.

**Result: the saved statements and proofs pass this review.** This is a proof audit with an independently implemented finite certificate, not a claim of formal verification.

Read in full: `sections/E_integral_detector.tex`; the actual class-three localization criterion and its proof in E.18–E.19 of `sections/E_extra.tex`; the normalization and class formula in E.36, `sections/E_kummer_values.tex`; and the root certificate `code/root/zero_slice_inverse_limit.py` before using its input data.

## E.37: coefficient map and obstruction

The tensor formula defines an actual integral map on the free degree-three Lie lattice. For a Hall word it gives

\[
\Phi([[e_i,e_j],e_k])
 =\ell_i\det(p e_j,p e_k)
 -\ell_j\det(p e_i,p e_k)
 -2\ell_k\det(p e_i,p e_j).
\]

The three nonzero values are (6,6,3) at the displayed words. Division by three is therefore valid on the entire integral lattice, and the resulting coefficient (1) proves surjectivity. It is not a division merely on the rational summand. Equivariance survives division because the target is torsion-free.

On the compact determinant, the first-letter contraction gives (2\det(pu,pv)\ell_f(z)=18\ell_f(z)). It kills the (HW^2) summand because either the first factor is compact, where \(\ell_f\) is zero, or the last two factors include a boundary factor, which the compact projection kills. E.36 consequently gives the rational coefficient class (6\kappa_3(3)). The integral group used here is the torsion-free unramified Kummer module, so equality survives integrally. The remaining possible coboundary vanishes: evaluating it at complex conjugation gives (-2b), with both actual cocycles zero there. This also justifies the literal cocycle identity rather than only equality of classes.

The reduction modulo nine is nonzero by the same conjugation normalization: a coboundary zero at conjugation has (b=0\pmod9), while the value at the chosen arithmetic generator is six.

The central class-two cocycle \(\kappa_3(19)w\) is well typed. The detector pushout of its connecting class lands in \(H^2(G_{\mathbb Q},\mathbb Z/9(2))\). At nineteen, the coordinate (\zeta_9\equiv4) gives \(\kappa_3(3)(F_{19})=4\pmod9\), since (3^2\equiv4^4\). Its residue is (6\cdot4\equiv6\), whereas (19-1\equiv0\pmod9\). Thus no central correction exists. The quotient \(N/N''\twoheadrightarrow N/\gamma_4N\), obtained from \(N''\subset\gamma_4N\), supplies the stated implication for metabelian lifts; composing the full geometric group with its pro-three quotient supplies the other implication.

## E.38: exact valuations, global comparison, and finite coefficients

For the normalized Tate cocycle, the commutator identity is

\[
\kappa([\tau,\tau'])
 =(1-7)\kappa(\tau)+(7-1)\kappa(\tau')=-12.
\]

The degree-one arithmetic matrices commute over the CM field. Their commutativity on the rational compact-plus-boundary representation implies commutativity on the actual integral lattice. Hence (\rho_V(r)=1) and the displayed formulas for (g_n) follow. The term \((7^{3^{n+1}}-1)/6\) has valuation (n+1\ge2), so adding (-12) leaves valuation exactly one. The cyclotomic difference has valuation (n+2).

The independently checked matrix (D=R^3-I) has the stated Smith valuations, with maximum six. The algebraic identity

\[
(I+B)^3-I=3B(I+B+B^2/3),\qquad B\in3M_{330}(\mathbb Z_3),
\]

has its final factor in (I+3M_{330}(\mathbb Z_3)). Iteration supplies the bound (3^{n+6}D_n^{-1}) integral at every depth. This uniform conclusion does not rely on sampling finitely many values of (n).

The finite Chebotarev condition is imposed on an actual homomorphism, including the affine Kummer representation. A prolongation can be chosen with the desired representative in the finite image. Modulus (3^{n+8}), together with the denominator bound (3^{n+6}), gives an error in (9M_{330}(\mathbb Z_3)) after multiplying by (D_n^{-1}). The integral Neumann inverse therefore transfers the bound to each selected prime. The same finite conditions retain both exact valuations used in the proof. Conjugation transfers the integrality and valuation statements to the second prime above a split rational prime.

The normalized integral Kummer functions are uniformly bounded. Multiplication by (3^{n+6}) gives uniform convergence of their series, so its sum is a continuous cocycle. At a selected prime (p_n), all other summands are unramified; its tame coefficient is exactly (3^{n+6}). The connecting obstruction therefore has exactly the stated correction

\[
x_n=-3^{n+6}D_{p_n}^{-1}\eta(F_{p_n}).
\]

The integral detector gives

\[
v_3(\Psi x_n)=(n+6)+1+1-(n+2)=6.
\]

The corrections consequently fail to approach zero. E.18–E.19 uses the literal quotient \(\mathcal R(A)/d\mathcal R(A)\), where \(\mathcal R(A)\) consists of families tending to zero. Its rational local correction is unique. Thus an alternative correcting cochain cannot replace this nonrestricted family by an admissible one. Restriction to the CM field detects the global obstruction, because corestriction multiplies by the invertible integer two.

Every finite partial sum has integral corrections of finite support and hence has zero connecting class by that same criterion. For each fixed (m), the infinite connecting cocycle modulo (3^mA) equals that of a finite partial sum. This proves the finite-coefficient lift assertion. The proof does not claim that those lifts are compatible, and the nonzero continuous obstruction proves that a compatible system yielding a continuous lift cannot exist.

## Independent executed certificate

New files:

- `code/B/E_integral_audit.py`
- `code/B/E_integral_audit.out.json`

The code imports only the previously recorded degree-one matrices. It constructs Hall words as tensors in the free associative algebra, performs unit-pivot tensor-to-Hall conversion, and substitutes the degree-one matrix into these tensors. Thus its degree-three matrix construction is independent of the root program's direct Jacobi-reduction routine.

Executed outputs:

| Check | Result |
|---|---|
| Hall dimension | (330) |
| Primitive detector | ((1,0,1)\mapsto2), ((1,0,5)\mapsto2), ((5,0,1)\mapsto1) |
| Untwisted Frobenius/conjugation factors | (49), (1) |
| Smith valuation multiplicities | (1^{132},2^{82},3^{52},4^{49},5^{14},6^1) |
| Determinant valuation | (724) |
| Working precision | (3^{12}) |
| Kummer coordinate at nineteen modulo nine | (4) |
| Obstruction at nineteen modulo nine | (6) |

All pivots are below the working precision. The elimination uses integral invertible row and column operations, so the finite computation certifies the displayed valuations for the integral matrix. No numerical value for the remaining elliptic Ross regulator is inferred.
