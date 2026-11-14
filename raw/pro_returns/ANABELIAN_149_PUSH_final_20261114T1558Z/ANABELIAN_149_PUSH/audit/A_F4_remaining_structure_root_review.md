# Root review of the remaining F4 pair

Date: 14 November 2026, approximately 14:20 UTC.

The full candidate `audit/A_F4_remaining_structure_candidate.md` has
been read, together with the reviewed fixed-field lemmas A.C2.12 and
A.C2.14. The independent degeneration review and certificate were
also read. The structural theorem is approved for integration as
A.C2.24 within its stated finite scope. Neither remaining curve is
asserted to satisfy or violate A1.

## Arithmetic and geometric structure

Root reran `code/A_F4_remaining_structure.py`: the actual descended
F4 curve has counts 7 and 15 over F4 and F16, giving
P(X)=X^4+2X^3+X^2+8X+16. Its exact root-ratio resultant has the
displayed squarefree degree-eight polynomial. All eighteen possible
cyclotomic factors of degree at most eight are excluded. Irreducibility
of P modulo three and the absence of root-of-unity ratios imply that
every Frobenius power still has irreducible degree-four minimal
polynomial. A proper geometric abelian subvariety would descend to
a finite field and supply a proper factor, which is impossible.

The rational geometric endomorphism assertion uses the tensor
Tate-module injection, not just faithfulness on individual maps.
Every geometric endomorphism commutes with a Frobenius power;
all those centralizers are the same four-dimensional algebra
Q_l[pi]. The endomorphism algebra contains Q(pi), already of
degree four, so equality follows. No claim that its integral order
is maximal is needed. The explicit CM field and its failure to be
Galois follow from the two negative discriminants whose product
is 17, as stated in the candidate.

The no-elliptic-target and no-two-rank-zero-abelian-target consequences
are valid for this original curve. Its three distinct simple-pole
coefficients leave no nonidentity branch permutation preserving its
Artin–Schreier equation; a nonconstant square-plus-itself correction
cannot alter a simple pole without introducing a pole of even order.
Thus the geometric automorphism group is exactly the hyperelliptic
involution group. These statements do not constrain arbitrary covers
of the curve.

## Odd-degree isogeny transfer

The comparison is specifically with the quadratic twist of A.C2.13's
split-branch theta-seven curve. Its Frobenius polynomial is the same
P, as independently counted in the degeneration certificate. Since
Q(pi^m)=Q(pi), there is one rational polynomial R_m valid in
Q[X]/(P) recovering pi from pi^m. A homomorphism defined over
F_(4^m) therefore intertwines the original F4 Frobenius operators.

On geometric two-torsion those operators have respectively one and
three nonzero fixed points. An odd-degree isogeny would induce an
isomorphism on this torsion, contradicting equivariance. Thus no
odd-degree geometric isogeny between this particular pair exists.
Both rational Jacobian groups have order 28; their two-primary
groups are correspondingly C4 and C2 times C2. The argument does
not exclude other isogenous Jacobians or a useful nonabelian cover.

## Uniform primary and mixed-support bounds

The exact congruence (X^m-1)B(X)=ell^e modulo (P,ell^(e+1))
lifts, since P is monic, to an endomorphism identity with right
side ell^e(1+ell R(pi)). The second factor is invertible on
ell-primary torsion. The fixed-field theta lemmas apply first;
then the displayed identity bounds the entire relevant primary
component. In mixed support the whole theta point must first
be fixed by the common Frobenius power. The candidate makes
this necessary step and does not infer mixed emptiness from
separate primary emptiness.

Root reran `code/A_F4_remaining_structure_degeneration.py`.
Its independent field arithmetic and quotient-polynomial arithmetic
passed the counts over F4, F16 and F256, the eighteen cyclotomic
exclusions, all thirty primary/mixed congruences, and the distinct
two-torsion permutations. It does not import the author's packet
matrix inversion. The complete geometric Hankel exclusions at
the specified finite bounds remain explicitly linked to their saved
outputs; these finite bounds do not imply a universal exclusion.

## The complete conductor-73 packet

Root also reran `code/A_F4_remaining_primitive_packets.py`.
The complete degree-two coordinate polynomial has roots 8 and 14
over F16. The two Artin–Schreier fibres give four theta points,
and the exact Cantor computation gives the multipliers
{1,27,46,72}, missing four of the eight primitive doubling orbits.

The author's subsequent conceptual proof is valid and should be
the main proof in the paper. The two Artin–Schreier constants have
trace one over F16, so all four points lie over F256 and the square
of actual F4 Frobenius acts by the hyperelliptic involution, hence
inversion on their theta classes. The 73-primary subgroup of
J(F256) has order 73, because #J(F256)=2^7*7*73. It is cyclic.
Thus Frobenius acts on its generator by k with k^2=-1 modulo 73,
so k=27 or -27. Its orbit is precisely the four theta classes.
Since 2 has order nine modulo 73, these occupy four distinct
doubling orbits out of eight. The remaining stable cohomology
has rank 4*9=36. Any other cyclic line has no theta point and
primitive rank 72. The uniform 73-primary exponent bound also
excludes primitive zero rank at higher 73 powers. These statements
close this conductor route without deciding A1.

## Primary source independently reopened

Milne, J. S. (2008). *Abelian varieties* (Version 2.0).
https://www.jmilne.org/math/CourseNotes/AV.pdf

Root reopened Chapter I, Theorem 10.15 (printed p.49 / PDF p.54),
which states the tensor injection with torsion-free cokernel;
Chapter II, Theorem 2.1 (printed p.79 / PDF p.84), and its
Tate-Hom explanation on printed p.81 / PDF p.86. Web records:
turn795view0, turn796view0 and turn796view2. The endomorphism
dimension proof needs only the former. If the two curves are called
members of the same isogeny class, the latter supplies that additional
standard implication from their common irreducible Frobenius polynomial.

All conclusions are restricted to the displayed models, primes,
supports and comparison isogeny. No failure of the universal
point-separation statement follows.
