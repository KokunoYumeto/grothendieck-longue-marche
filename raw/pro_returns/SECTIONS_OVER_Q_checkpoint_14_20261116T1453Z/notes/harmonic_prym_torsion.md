# Exact global torsion of the A.150 Prym elliptic factor

Let K=Q(sqrt(2)), M=7*13*23*139*1119169, and
E_b: Y^2=X^3+bX with b=1146(1+sqrt(2))^2 M^2.

The two explicit residue homomorphisms are

- Z[sqrt(2)] -> F_17, sqrt(2) -> 6;
- Z[sqrt(2)] -> F_31, sqrt(2) -> 8.

The discriminant -64b^3 is a unit at both primes. Direct complete point
enumeration gives orders 10 and 32, respectively. The retained certificate
is work/code/harmonic_prym_torsion_certificate.py and its output is in the
adjacent file with suffix _output.txt.

For a good-reduction local elliptic curve, its reduction kernel has the
formal parameter filtration. Multiplication by any integer prime to the
residue characteristic has unit linear term and is invertible on that
kernel. Thus reduction is injective on torsion of order prime to the
residue characteristic. This is the exact map used here.

For a prime ell other than 17 and 31, the ell-primary global torsion injects
into both displayed residue groups, so its order divides gcd(10,32)=2.
The 17-primary part injects at 31 and is zero; the 31-primary part injects
at 17 and is zero. Hence all torsion has order at most two. The actual
point (0,0) is nonzero of order two, so

E_b(K)_tors = {O,(0,0)}.

This proves the exact global torsion group independently of the unresolved
Mordell-Weil rank and of the higher-descent pairing computation.
