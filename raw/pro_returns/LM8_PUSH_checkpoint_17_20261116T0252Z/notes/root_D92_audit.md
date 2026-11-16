# Root full proof audit of D.92

**PASS; canonical integration approved once the independent PBC audit
also passes.** Root read all 159 lines of
`notes/de_metabelian_rank_one_image_draft.tex`, SHA-256
`479e20545fe1554782265cc176ea488d961391449d99d30f49c1fbd7cf878661`,
and freshly read the actual statements and relevant proofs of D.42,
D.36 and D.83. D.91 has just completed the root's full proof,
source and executed-certificate audit. No new external theorem or
numerical experiment is needed for this exact corollary.

## The rank-one condition is on the actual completed coordinates

The pro-five completion of Q* is the c_0 module on rational primes:
the sign disappears, and at each finite five-power level the prime
coordinates have finite support. Thus the displayed coefficients are
unique. A one-dimensional Q_5 span has a primitive Z_5 generator;
one unit coordinate shows that all its scalar coefficients are
integral and still tend to zero. The resulting eta is an actual
completed Kummer class. This covers infinitely ramified parameters
and nonprimitive individual inertia vectors without choosing a
rational generator or imposing a saturation hypothesis on their span.

If one away-five vector is nonzero, restrict the actual section to
that prime's decomposition group. Local Kummer theory identifies
its tame five-primary inertia coordinate with that vector, up to
a common unit. The other prime Kummer classes have zero inertia
there, and the uniformly convergent completed sum preserves the
identification. The actual unit-tangent action is unramified at
every such prime, including 2. D.42 is explicitly unconditional
for the metabelian quotient and for arbitrary nonzero five-adic
inertia powers. It forces the vector onto a coordinate axis or
the diagonal. Since this vector spans the entire global line,
the coordinate at five and all other prime coordinates must lie
on the same peripheral line. This is the asserted global necessity.
It is not an inference from local section existence to global
section existence.

If every away-five vector is zero, the pair is exactly the stated
pure-five pair, whose global existence is D.36. Conversely each
entire peripheral line has actual completed cusp sections by D.35.
All these pairs have global valuation rank at most one. The zero
pair is included, with its three distinct zero-parameter cusp
packets retained. These observations establish both directions
of the exact image equality.

## Compact kernels and the rational-point boundary

D.91 computes the natural compact second-cohomology kernels on
every peripheral family. D.83 includes the zero away-five lattice
and proves that both S and K vanish on every pure-five pair.
The two formulae agree on the intersections; no infinite-corank
subtraction, first-cohomology rank claim, or higher-derived lift
claim is made. The arithmetic module depends on the abelian pair,
so its compact-kernel calculation applies to the entire fibre,
without identifying its different section classes.

For a rational point t, the pair is (kappa(t),kappa(1-t)). It
cannot be supported only at five: both rationals would then be
signed integral powers of five and would reduce to 1 in F_2,
contradicting their sum 1. This argument is valid in Z[1/5]
and includes negative exponents. Consequently a rational point
in this rank-one locus lies on a peripheral line by the already
proved necessity. The kernel of rational Kummer classes is
exactly {1,-1}, since all integer prime valuations must vanish.
The two axes give t=2 and t=-1; the diagonal gives t/(1-t)=1
and hence t=1/2, while the negative sign would imply 0=-1.
The excluded alternatives are precisely t=0 and t=1. Direct
substitution gives the three displayed Kummer pairs, and all
three do have rank one. This calculation distinguishes abelian
images from actual point-section or cusp-section classes, as
the statement requires. Every section above a nonperipheral
pure-five pair is therefore neither cuspidal nor an ordinary
rational point section, consistently with D.36.

No finite computation is used to extrapolate an infinite
classification. The full written proof is short, exhaustive,
and reduces exactly to already audited actual local and global
section theorems. PASS.
