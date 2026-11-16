# C31: exact primary separation of the positive certificate search

Research/computation plan, 2026-11-15 around20:58 UTC. **C31 is Open.**
The existing full-modulus search and every old basis are retained.

The already proved annihilator is `M=2^14*3^8`. Let K be the actual
source-centralization kernel, whose torsion subgroup is `H_2(G,Z)`.
Write T for the target class. It is torsion. Every allowed correction
`[c,s]`, with c centralizing the image of s in G, has exponent dividing2
in K, because s squared is central in the cover. Likewise each allowed
`[d,r]` has exponent dividing3. These are precisely the genuine
centralizer commutators already retained in the source input; the two
power-word corrections remain forbidden.

Suppose an ORIGINAL-presentation identity proves

`T + S = 0 in K/2^14 K`,

where S is a sum of the s-commutators, and another proves

`T + R = 0 in K/3^8 K`,

where R is a sum of the r-commutators. Then R vanishes in the first
quotient and S vanishes in the second: their orders are coprime to the
respective moduli. Thus `T+S+R` belongs to
`2^14 K intersect 3^8 K = M K`. It is also torsion, and
`tors(K) intersect M K=0` by the proved Hopf-annihilator argument.
Consequently `T+S+R=0` integrally. **A single primary success is not a
lifting certificate. Both exact primary identities and all used original
source-row replays are mandatory.**

An explicit combined identity is available. Choose integers A,B with
`A*2^14+B*3^8=1`. Multiply the first original integer identity by
`B*3^8` and the second by `A*2^14`, then add. The target coefficient is
exactly1, the residual is a multiple of M in every free central
coordinate, and the s/r coefficients agree with the primary labels
modulo2/3 respectively. This permits a direct integer verification of the
combined certificate, independently of the two processed row lattices.

## Proper coordinate bounds

If an original diagonal bound is d and the new modulus is m, use the
coordinate bound `g=gcd(d,m)`. This is not asserted to be an integral
source relation by itself. Retain integers A,B with `A*d+B*m=g` and the
already proved ORIGINAL power-consistency rows whose integer combination
is d times that coordinate. Subtracting an integer multiple of A times
those actual rows leaves a multiple of m. This proves the new coordinate
elimination modulo m, without adding an unproved relation to the cover.
Full-modulus coordinates simply use the modulus row. The independent
source replay still checks every proper-bound row that the proof uses.

On the current176-generator source, m=3^8 leaves7,649 nonzero coordinates:
7,416 with full modulus,233 with bound3, and7,927 killed modulo3^8.
For m=2^14 the active count is14,521:7,416 with full modulus and7,105
with bound2;1,055 are killed. The three-primary run needs only the9
order-three frame corrections, while the two-primary run uses the71
order-two corrections. These counts concern exact projected coefficient
systems, not actual quotient descent or a nonlifting assertion.

The22,343 already collected original identity leaves can be reused in
their retained order, so this test need not repeat the expensive source
word collection. Any later additional original rows can be appended.
No existing proof log or paused state is overwritten.
