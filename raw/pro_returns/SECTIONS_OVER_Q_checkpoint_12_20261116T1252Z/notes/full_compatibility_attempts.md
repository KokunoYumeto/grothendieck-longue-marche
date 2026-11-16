# Exact compatibility checks, fifth hour

## The fixed-depth congruences do not give one fixed ghost

The actual backward moduli in A.65 satisfy
`M_(r-1) = D B_r M_r D_r^old`, with `D=(R!)^(h_R+1)`.
In particular, the initial modulus `M_1(R)` is divisible by `R!` for
every `R>=2`. Their divisibility is cofinal among all positive integers.
The map from the power completion to each `Q*/(Q*)^N` is part of its
definition. A single pair satisfying every one of the initial
point-3 congruences of that construction therefore has
`A/3=1` and `B/(-2)=1` in the full power completion: both ratios have
trivial image modulo every `N`. This is an actual calculation of
the intersection of the specified congruence kernels. The existing
proof cannot be promoted to a fixed infinitely supported pair by
imposing all its initial congruences at once. A.81 and A.86 retain
the separate, fixed-pair obstruction instead.

## The two-coefficient deformation and all coefficient primes

B.16 fixes the two residual representations of the actual curve
`E_3` and constructs local split Tate curves with parameter `q^M`,
where `M` is a positive integer chosen for those two coefficients.
At a prime `q>3`, the residual representation of `E_3` is unramified
for every coefficient prime different from `q`. The residual tame
inertia of the literal Tate curve `q^M` is nonzero at every such
coefficient prime not dividing `M`. Since `M` has only finitely many
prime divisors, the same fixed-residual construction cannot provide
these local Tate modules at all coefficient primes. This verifies
the failed passage using the actual inertia map, rather than an
unspecified distinction between finite and infinite systems.

A second attempted passage introduces a new coefficient only after
finitely many local curves have been fixed. Weak approximation can
select a rational elliptic curve whose residual representation
matches those finitely many local targets. This alone supplies no
control at its other bad primes. At those primes the already
constructed representations have fixed finite reductions; the new
local Tate valuations and Frobenius eigenvalues would have to match
those reductions. The approximation argument supplies no such
matching. Thus neither attempt proves an all-coefficient family.
The exact missing step is simultaneous residual local realization
with control at every newly ramified prime. No existence or
nonexistence result for that step is asserted here.

## The completed old-coordinate refinement under investigation

The new candidate construction refines one existing coordinate
`X_i=U Y^h` and uses the actual update
`a_i -> a_i U^(n_i)`, `n_i -> h n_i`. Its local reciprocity input
concerns `X_i` itself. It cannot be inferred merely from the
constant symbols in `T-c_i=a_i X_i^(n_i)`.

A.88 verifies a stronger input for its initial local points: every
coordinate character in its fixed quadratic boundary field has
zero evaluation at every place separately. The intended induction
keeps that property by taking the new root close to one at
controlled places, equal to one at newly introduced fibre primes,
and choosing unit-coordinate points at every remaining sufficiently
large good prime. Mixed exponents and full divisibility cofinality
are being audited in A.90; this note does not replace that proof.

The old open curve has four punctures, including infinity. Its
comparison with the tripod forgets the third finite puncture.
A failure to extend its completed coordinates across a fourth
finite puncture does not establish a counterexample to either
principal assertion A1. Any full-section obstruction must specify
this exact old open curve and its actual finite Kummer cover.
