# Independent audit of FF.49

Reviewer: finite-field criteria agent. Reviewed the full current
`agent_F/F_elliptic_shear_draft.tex`, the completed-point argument in
`F_genuszero_kernel_draft.tex`, and the dominating Lattès construction in
`F_lattes_kernel_draft.tex`. Result: **approved**, with the boundary repair
now present in the reviewed draft. This is an audit of the stated conclusion,
not a claim that arbitrary positive-genus slice topoi are reconstructed.

## Completed points

Agreement of the actual point function on a branch complement does not by
itself identify individual omitted points of the completion. The original
shortcut therefore required repair. The inserted family of translated
genus-zero quotients supplies it.

On the dominating cover B with group B[N] semidirect H, a pair z != z'
has the same image modulo tau_t H tau_-t only if
z' = h(z) + (1-h)t for some nonidentity h in H. Each such h admits at most
deg(1-h) values of t. Thus N^2 greater than the sum of these degrees makes
the family separate every pair of completed geometric points, including
ramification points. Each quotient is over the original rational base.
FF.47 explicitly realizes the entire completed-point bijection, not just
its restriction to the displayed open. Naturality and separation therefore
identify the completed point map on B, and the finite surjection to the
original elliptic cover gives the same conclusion there.

This argument does not presume that projections of a normalized fibre
product distinguish its branches. They need not do so: the local curves
y^2=x and z^2=x(1+x) have two normalized branches above x=0 with identical
values y=z=0. The translated-quotient argument avoids that issue.

## Integral geometric argument

The compatible Kummer character of a function is an integral Z_ell(1)
character because all roots of unity lie in the constant field. The
coefficient action is fixed. Once the completed points and inertia
exponents are fixed, the difference of the two characters has zero residue
at every geometric point, hence factors through the proper elliptic curve.
The resulting H^1 is free of rank two over Z_ell.

For a principal divisor with one coefficient +1 or -1, the adjustment of a
chosen n-division point by an element of A[n] makes its lifted degree-zero
divisor principal. Summing all its translates gives the pullback of the
original divisor. Consequently f composed with [n] equals a constant times
the product of the translated function h. Every map used here is a map
between realized covering objects over the original base; the naturality
identities therefore do not assume reconstruction of unrelated rational
subfields.

Translations act trivially and [n] acts by n on proper H^1. The integral
identity n b_1(f)=n^2 b_n(h) is therefore valid. Taking n=ell^r, cancelling
in the free module, and allowing all r proves b_1(f)=0. Enlarging constants
to make the finite collections of choices does not change the geometric
class b_1(f). The auxiliary function q with a simple zero away from the
divisor of f reduces an arbitrary f to the two covered cases q and fq.

## Arithmetic descent and norm

After geometric vanishing, the full integral error factors through the
constant Galois group. This is a single compatible integral character,
not an assertion inferred from unrelated finite-level representatives.
The generic slice action and actual realization identify the covering map,
so corestriction commutes with the induced actions. The Kummer norm identity
and the proved rational-base result show that the corestriction of the
error is zero.

For an error inflated from gamma on the constant group, restriction followed
by corestriction is multiplication by the degree of the cover. Inflation
is injective and Hom_cont(G_L,Z_ell(1)) is torsion-free. It follows that
gamma is zero even when ell divides that degree. No division in a finite
coefficient group and no rational point on the genus-one torsor is needed.

Reducing the integral equalities gives all finite Kummer characters. Since
the field contains all roots of unity, these characters determine the full
abelian profinite quotient. The conclusion preserves cyclic covering
objects; it supplies neither their actual point realizations nor the full
nonabelian generic action. The draft states this distinction correctly.

## Same-prime cuspidal addendum

The full `agent_geometric/cuspidal_same_prime_addendum.tex` was also reviewed
and approved. For every open I containing N=ker(K -> K^(r)), its core I_0
contains N. Given a finite r-group quotient I/J, the core M of J intersect
I_0 gives an r-group I_0/M. The image of K downstairs in F/I_0 is an
r-group; its full image in F/M is therefore r-by-r and kills N. Thus every
finite r-quotient of I kills N. Taking pro-r quotients commutes with killing
the specified puncture inertia, and the construction respects Frobenius.
It retains the full proper r-adic H^1 and exact integer Weil polynomial,
without claiming point separation or an integral p-primary exponent bound.
