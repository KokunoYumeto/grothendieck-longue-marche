### E.51: every first coordinate unramified outside three

E.51 computes the entire global H-section fiber for each first class
3r kappa_3(3), with r a nonzero three-adic integer. Writing r=3^k e and
M=3^(k+1), its coordinates are Z3 times the restricted sequence group on
the eligible rational primes, times Z3^((M-1)/2), times Z3[[Z]]. The second
toric coordinate is exactly b3 kappa_3(3) plus the restricted sum of the
prime Kummer classes. The allowed primes are precisely p other than3
with v3(ord_p(3)) at most k+1. E.47 already evaluates the zero fiber,
so together these results cover every first class unramified outside3.

The actual arithmetic automorphism (a,v(T)) to (ea,v(T^e)) handles the
unit part of r. It also transports the finite root torsors by i to e i;
the induced isomorphisms of finite etale algebras identify the exact
norm systems for the two first cocycles. The integral normal form uses
the inversion-fixed part of Z3[C_M] and the remaining series T^M Wf(W²).
Its proof divides only on specified closed principal ideals and retains
all (M-1)/2 finite augmentation-zero parameters.

The localization comparison uses the finite arithmetic modules themselves:
their action over Q(zeta3) factors through the free unramified pro-three
group, and their filtration by trivial finite three-modules gives the
required higher-cohomology vanishing. Finite H1 then supplies the exact
inverse-limit sequence. The local invariant measures are either zero or
the saturated lattice3 Z3 delta_x at the unique fixed point; the restricted
sequence condition follows at level zero and is sufficient at every level.

The residue lifts are also constructed in fields. In the cofinal range
n=d+k+1, the root algebra factors into Q(3^(1/3^d)) and
Q(3^(1/3^d) zeta_(3^(d+j))) for j=1,...,k+1. The actual arithmetic element
rho with cyclotomic value1 and Kummer value minus2 proves the precise
degrees of these factors. Every vertical layer containing zeta3 is cyclic
cubic and ramified only at the unique prime3. The ambiguous and strongly
ambiguous class formulas prove that its class number has trivial
three-primary part and its unit norm is onto. The pure radical factor is
handled by its actual quadratic extension and the integral projector.
Thus each degree-one prime chain has a norm-compatible principal divisor
lift, corrected by actual unit norms, with zero valuations elsewhere.

The original Lemmermeyer paper was reopened: Theorem1 formulas1 and2,
Proposition1, and the complete proof of the strong-ambiguous formula.
The finite localization and continuous-cohomology comparisons are those
already verified against the original sources in E.44 and E.49.

The program ran successfully with64 exact normal-form recoveries for
M=3,9,27,81 and16 arbitrary Laurent inputs requiring genuine unit-denominator
division. It checks512 initial three-integral series coefficients in those
arbitrary cases,12 exact field factorizations and actual arithmetic root
orbits through degree729, and8,770 ideal-norm transitions at61 primes for
four first-coordinate valuations. In the tested prime range below300,
raising k from0 to1 newly permits19,37,127,181,199; k=2 newly permits109;
k=3 newly permits163. These computations accompany the uniform proof.

Agent A read the full proof and code and independently executed a copied
program. Its JSON certificate matched exactly. The audit checked the
arithmetic root action, cyclic class-number induction, actual unit norms,
normal form, full arithmetic localization and inverse-limit topology.
The root-torsor transport sentence suggested in that audit has been added.
The exact intrinsic geometric kernels remain on the coverage ledger;
this theorem asserts the complete section calculation for H.
