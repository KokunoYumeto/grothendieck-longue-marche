# Independent review: cyclic theta difference bounds

**Reviewed:** audit/A_cyclic_theta_difference_candidate.md, Sections 1–5, and code/A_cyclic_theta_difference_checks.py with its JSON output, 14 November 2026.

**Conclusion:** the uniform difference bound and both primitive-rank lower bounds pass independent review. I reran the exact integer program; it returned PASS for 500 odd orders and the stated lower bounds 14 and 80 at 127 and 257.

## The geometric difference bound

For a nonzero degree-zero class \(T\) on a smooth genus-two curve, two distinct representations \(T=[P-Q]=[P'-Q']\) yield the distinct linearly equivalent degree-two divisors \(P+Q'\) and \(P'+Q\). If the formal divisors coincided, either the pairs would coincide or one of the original differences would be zero. The latter is excluded by \(T\ne0\).

Distinct effective equivalent divisors of degree two give the unique hyperelliptic pencil. Hence \(Q'=\iota(P)\) and \(P'=\iota(Q)\). A possible second ordered pair is uniquely determined. This works at ramification points as well; the assertion is set-theoretic and does not assume transverse theta intersections.

The Abel embedding is injective, so each ordered pair of indices in the theta packet gives a distinct ordered pair of curve points. At a fixed nonzero index difference there are at most two such pairs. Summing gives
\[
|S|(|S|-1)\le 2(n-1),
\]
with the claimed exact integer bound \(b(n)=\lfloor(1+\sqrt{8n-7})/2\rfloor\).

## Character-orbit bookkeeping

Every primitive doubling orbit has length \(\nu=\operatorname{ord}_n(2)\). For the genus-two characteristic-two cover, the already checked one-dimensional Frobenius-cycle calculation A.C2.5 says exactly that an orbit contributes either its entire length or zero, according as it avoids or meets theta. Thus at most \(|S|\) primitive orbits are killed.

When \(-1\) lies in the doubling subgroup, theta symmetry requires each killed primitive orbit to contain two distinct packet indices \(i,-i\). They are distinct because \(n\) is odd and \(i\) is a unit. Hence at most \(\lfloor |S|/2\rfloor\) primitive orbits are killed. Nonprimitive packet elements and a possible origin consume the packet bound without helping to kill primitive orbits, so their presence cannot invalidate either estimate.

At 127, the order of two is seven, the packet bound is sixteen and there are eighteen primitive orbits. The resulting rank is at least \(7(18-16)=14\). At 257, the order is sixteen, \(2^8=-1\), the packet bound is twenty-three and there are sixteen primitive orbits. At most eleven can be killed, giving rank at least \(16(16-11)=80\).

At prime conductor every surviving nontrivial character is faithful. The conclusion about deck faithfulness therefore follows from either positive rank bound. It applies to geometric two-primary torsion and its étale Tate module, exactly as stated.

## Program and interpretation

The program uses integer square roots and directly verifies both inequalities defining \(b(n)\); it does not use a floating-point approximation. It computes the multiplicative order and the membership of minus one directly, verifies Euler-phi divisibility by that order, and checks primality of the two displayed conductors through trial factorization. The rerun produced the same JSON values.

These are genuine impossibility statements for the specified primitive-rank-zero cyclic-cover method. They do not give point-section collisions, do not refute A1, and do not exclude using another conductor on the same curve. That distinction is explicit throughout the candidate.
