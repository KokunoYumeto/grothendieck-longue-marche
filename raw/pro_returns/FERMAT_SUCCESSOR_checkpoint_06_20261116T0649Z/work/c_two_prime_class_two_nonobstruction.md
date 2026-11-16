# A checked class-two non-obstruction at seven and sixty-one

Date:2026-11-16. This is a finite-stage test requested in the continuing investigation of B.10(a). It does **not** construct a full pro-three section and does **not** identify the local class-two sections with actual cusp packets. Its purpose is to determine whether the already evaluated class-two obstruction can exclude the compatible compact labels from B.42.

## An actual global abelian family

Retain the full cubic N, the unit tangent at O=C0, V=Nab, W the boundary sublattice, and K=Q(ζ). In the B.24 compact basis, e1/3=A0 and e2/3=A2. Thus B.42's point `(1,2)/3` is C2.

Choose an actual unramified-outside-three V-cocycle α0 with compact image β. For example, normalize at complex conjugation and prescribe value `(1,2,0,...,0)` at the actual free generator τ over seven, with its c-conjugate value at the other generator. The actual pro-three action and the free arithmetic group provide this continuous cocycle. It can even be obtained by projecting an actual full unramified N-section, by choosing any N-preimage of that abelian value.

Let π=2−ζ and barπ=3+ζ. The global W-cocycle

\[
\theta=
\operatorname{cor}_{K/\mathbf Q}\bigl(\kappa_3(\pi)e_{C_2}\bigr)
 +\kappa_3(61)e_O
\]

is well defined through the induced boundary module on the conjugate cusps C2,C1. Its restriction to K is

\[
\kappa_3(\pi)e_{C_2}
 +\kappa_3(\bar\pi)e_{C_1}
 +\kappa_3(61)e_O.
\]

Equivalently, choose compatible roots of π and barπ interchanged by c and extend the resulting c-equivariant cocycle with value zero at c. This gives the same descent. Put

\[
\alpha=\alpha_0+9\theta.
\]

Its compact class is β. Its exact abelian tame inertia is9eC2 at the chosen rational seven-adic embedding ζ→2 and9eO at sixty-one. It is zero at every other good prime. By B.42, its compact Kummer labels at the two chosen primes are respectively C2 and O, so there is no compact-label inconsistency.

## The actual B.24 obstruction vanishes

At each prime over seven or sixty-one, B.24 forms the integral numerator

\[
D_q=\alpha(F_q)\wedge\alpha(t_q)
 -\sum_d b_{q,d}k_{q,d}\wedge e_d.
\]

Every term is divisible by nine, because every bq,d is. The numerator has no f1∧f2 component, since the inertia lies in W. No evaluation or replacement of the higher Frobenius word is needed: α(Fq) and each actual framed cusp Kummer representative kq,d are integral, which is enough for this divisibility assertion.

The compact Frobenius matrices at the two conjugate places are

\[
\begin{array}{c|cc}
q&\text{first place}&\text{conjugate place}\\\hline
7&I+3R&I+3R^2\\
61&-5I-9R&4I+9R.
\end{array}
\]

The sixty-one matrices have norm61 and trace−1, and correspond to the roots13,47 of the cyclotomic polynomial; the direct point count is63. In all four cases, `(A_E−I)^−1` has entries in `(1/3)Z3`, and `v3(q−1)=1`. In B.24's exact formula, Z therefore has denominators at most three, and Y* and the gauge correction have denominators at most nine. Every correction is integral whenever Dq is divisible by nine.

The script `work/c_two_prime_class_two.py` checks this without a valuation estimate alone. It constructs the exact45-by45 operator `q^−1 Λ²(F_V)−I`, the full44-column inverse on the zero-compact-determinant numerator subspace, and verifies the exact rational identity

\[
(q^{-1}\Lambda^2(F_V)-I)H=-\operatorname{inclusion}.
\]

For each of the four places the least entry valuation of H is exactly−2. Thus nine times H is three-integral, as claimed. The records are in the accompanying `.out` and `.json` files.

At every other good prime the inertia numerator is zero. Only finitely many local corrections occur, so the decay condition is automatic. The actual global class-two image theorem B.24 consequently gives a lift of α to `H1(Q,N/γ3N)`.

## What this does and does not decide

This is a genuine global class-two section with nonzero abelian inertia in the two specified peripheral directions and with exactly the compact class β. It shows that the class-two obstruction itself cannot rule out those two labels after sufficiently divisible inertia.

It does not show that either local class-two section is the image of an actual full cusp packet. That stronger condition fixes its Frobenius/path origin as well as its abelian inertia, and the proof above deliberately uses no uncomputed local origin identity. It supplies no class-three lift and no compatible inverse limit. In particular it cannot be used as a counterexample to B.10(a). The remaining full problem is the simultaneous nonlinear local cusp matching, including the integral origins at all levels.
