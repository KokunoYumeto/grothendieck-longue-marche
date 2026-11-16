# The full dihedral centralizer and its actual orbifold parameter

Research derivation, 16 November 2026. This sharpens the full-group setup;
no finite-index refined product or actual K element is obtained here.

Write D=<d>≅C5 and J=<d,r>≅D5 for B65's actual subgroups. The centralizer
C=C_Gamma(D) fixes the two D-fixed punctures p=1,q=3 individually, since
their local rotation residues are +1 and -1 modulo5. It may interchange
the two free D-orbits A,B. Quotienting the cyclic cover gives

    1 → D → C → Q4 → 1,

where Q4 fixes p-bar,q-bar individually and preserves the pair {A-bar,B-bar}.
Every Q4 class lifts: its action preserves the cyclic monodromy with values
+1,-1,0,0 at these four punctures. The lifted action on D is trivial.

The image r-bar is the canonical Klein-four double transposition
(p-bar q-bar)(A-bar B-bar) in the four-point mapping-class group. The pure
four-point group centralizes that Klein four group, and the only allowed
extra permutation in Q4 is (A-bar B-bar), which fixes r-bar by conjugation.
Therefore every element of Q4 commutes with r-bar. Thus [c,r] belongs to
D for all c∈C. Put delta(c)=[c,r]. Since D is central in C, delta is a
homomorphism C→D; on D it is the squaring map, because r inverts D.
Consequently

    rho(c)=delta(c)^(-1/2)*c

is a homomorphic retraction onto C_Gamma(J). The half power is unique in
C5. Its kernel is D, and D∩C_Gamma(J)=1. We obtain an actual direct product

    C_Gamma(D) = D × C_Gamma(J),     C_Gamma(J) ≅ Q4.

This splitting is distinguished by the chosen reflection r. It is not
silently identified with B52's vertex-fixing rank-two complement.

Normalize the ordered quotient configuration to {0,infinity,1,t}. The
interchange of the two ordinary orbit labels sends t to1/t. Thus Q4 is
the orbifold fundamental group of

    q=t+2+t^(-1) ∈ P1 \ {4,infinity}, with one cone point of order2 at q=0.

Hence Q4≅C2*Z. In the actual pure cyclic family t=u^5, so

    q=(u^5+1)^2/u^5.

This is an orbifold covering of degree10 from S5=P1\{0,infinity,mu5}.
The deck transformations are u↦zeta*u and u↦1/u. The five points u^5=-1
lie over the order-two cone point and have ramification index2. The five
removed points u^5=1 lie over the cusp4 and have index2; the two removed
points0,infinity lie over the cusp infinity and have index5. The total
ramification18 agrees with Riemann–Hurwitz for a degree10 map.
Consequently H5 is the normal index10 kernel of C2*Z→D5. With orbifold
meridians e at0 and t0 at4, the quotient is

    <e,t0 | e^2=1> → <e,t0 | e^2=t0^2=(e*t0)^5=1> ≅ D5.

In particular the image of C_Gamma(J) on the original ten non-pole labels
is the right regular D5 action, and the pole labels are fixed. The pure
kernel is exactly H5.

The valid prime-order-five full-topology/density comparison identifies
C_(Gamma-hat)(D) with C-hat. The direct product above completes literally,
and r acts by inversion on D and trivially on C_Gamma(J). Therefore

    C_(Gamma-hat)(J) = C_Gamma(J)-hat ≅ (C2*Z)-hat.

This gives the complete dihedral comparison without exchanging two
uncontrolled completed intersections or assuming a nonsolvable theorem.

For the common-involution quotient, the full group C_Gamma(J) must be
placed in Q8-tilde: it fixes the ordinary pole-orbit label and may permute
the other five ordinary labels, while preserving the unordered branch
pair. Q8-tilde is the finite extension of the earlier Q8 by S5. Choosing
the unique lift fixing original label1 splits its deck extension. The
image of C_Gamma(J) on the five non-pole r-orbits is the faithful degree-five
D5 action on <r>\J. Its intersection with the label-fixing Q8 is therefore
exactly H5. All these inclusions inherit the full topology from the
valid C2 and C5 comparisons. The coarse C2*Z itself is not a subgroup of
the original label-fixing Q8.

A retraction from a finite-index subgroup of Q8-tilde onto this C2*Z,
compatible with the tetrahedral subgroup, has not been constructed.
The direct-product retraction rho has domain C_Gamma(D), a subgroup of
infinite index in the ambient mapping-class group. It cannot be used as
an ambient finite-index retraction. The finite-index product/intersection
problem remains exactly the one identified in B46 and B52.
