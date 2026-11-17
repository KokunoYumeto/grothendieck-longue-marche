# Actual affine reflection chart and the remaining critical-filling gate

Research proof, twentieth hour. All fundamental groups here are discrete
unless a completion is explicitly named. The base point is the actual
P=(399/200,1/200) of B87--B104, and the involution is the literal based
map of B87, not merely an outer class. This record is not a decision of
the fixed subgroup on the full symmetric surface.

## 1. Exact algebraic isomorphism of the actual open surface

Write U=mu_5 minus {1}. The actual Z is obtained from
X={(v,w) in(C*)^2: v,w unequal to1, v unequal to w, vw notin mu_5}
by deleting, for every u in U, the four curves

 v=u, w=u, vw+(u-1)v-u=0, vw+(u-1)w-u=0.

Define

 a=(2vw-v-w)/(w-v), b=(v+w-2)/(w-v).

The denominator does not vanish on Z. The inverse formulas are

 v=(a+1)/(b+1), w=(a-1)/(b-1).

They give an algebraic isomorphism from Z to the complement in C^2 of
exactly the following divisors:

 a=1, a=-1, b=1, b=-1, a=b, a=-b;
 a-ub-(u-1)=0, a+ub-(u-1)=0,
 a-ub+(u-1)=0, a+ub+(u-1)=0, for every u in U;
 a^2-1-u(b^2-1)=0, for every u in U.

For completeness, b+1=2(w-1)/(w-v) and b-1=2(v-1)/(w-v),
so the old open surface lands where the inverse is defined. Conversely
the six retained lines excluded above force v,w nonzero and distinct,
v,w unequal to1, and vw unequal to1. Direct substitution of each old
factor gives one of the displayed new factors times a unit; the exact
factor identities, including both components of each pullback that
shares an already removed retained factor, are recorded by
code/reflection_coordinates20.py in records/reflection_coordinates20.json.
Thus no extra component has been silently added or removed.

The sixteen further lines are distinct. Within one u their four
constant/slope choices are distinct because u is nonzero and u unequal
to1. Equal slopes for different u would imply u=t or u=-t;
-u cannot be a fifth root of unity when u is. No further line equals a
retained line, since its slope is a nontrivial fifth root up to sign.
The four conics are distinct, since their b^2 coefficients are distinct.
They are nonsingular and irreducible: u and 1-u are nonzero, and the
quadratic equation a^2-u b^2=1-u has nonzero determinant in its
homogeneous three-variable quadratic form. Therefore this is exactly
22 affine lines and four smooth affine conics.

Substitution into the literal involution gives F(a,b)=(a,-b).
The actual base point becomes (199/200,0), and q=vw becomes
q=(a^2-1)/(b^2-1). All inverse and involution identities have exact
rational symbolic checks in the same retained producer and output.

## 2. The actual fixed source and its nineteen punctures

The fixed locus is exactly b=0. Its a coordinate avoids

 0, 1, -1, the eight roots a=+-sqrt(1-u),
 and the eight points a=+-(u-1), for u in U.

These nineteen values are distinct. The quadratic roots are nonzero
and not +-1 since u is neither1 nor0; roots belonging to different u
cannot coincide. The line values are nonzero. Equality u-1=-(t-1)
would give u+t=2, which for unit complex numbers forces u=t=1.
The line values are not +-1, since that would force u=0 or2.
Finally equality (u-1)^2=1-t would give t=u(2-u).
The absolute values then imply |2-u|=1; together with |u|=1 this forces
Re(u)=1, hence u=1, a contradiction. This exhausts possible collisions.
Thus the actual fixed source is the nineteen-punctured affine line,
with the specified base point and group F19. This agrees with the
original source: on v+w=2 one has a=v-1 and b=0.
The image of its fundamental group in pi1(Z) is not asserted injective.

## 3. A finite explicit exceptional set for a genuine equivariant bundle

For a fixed a unequal to +-1, the removed b values are the opposite
pairs with squares in the following fourteen polynomials:

 f_0=1, f_1=a^2;
 Q_u=1+(a^2-1)/u, u in U;
 P_(u,+)=((a+(u-1))/u)^2,
 P_(u,-)=((a-(u-1))/u)^2, u in U.

Every polynomial is nonzero. They are pairwise different. The leading
coefficients distinguish 1, a^2 and each member of the Q family, and
distinguish P values for different u because squaring is injective on
mu_5. For fixed u the two P values have different nonzero linear
coefficients. A P and Q with equal leading coefficient still differ
because Q has zero linear coefficient and P has nonzero linear
coefficient. The same observation distinguishes P from a^2.

Define Delta explicitly to be {1,-1}, the roots of the fourteen
polynomials, and the roots of all their nonzero pairwise differences.
It is a finite set. All nineteen fixed-source punctures belong to it.
Let U_a=C minus Delta, based at199/200. This is an actual regular
base value: code/check_reflection_regular_base20.py evaluates all fourteen
polynomials in Q(zeta_5), checks every value nonzero and every one of
the91 differences nonzero, and checks a unequal to+-1. Its complete
values and genuine output are records/reflection_regular_base20.json
and .out. An initial API-indexing error and failed source are retained;
the corrected exact computation finishes successfully. No basepoint
change or unrecorded whisker is required.

Over U_a all fourteen squares are nonzero and distinct. Local choices
of their square roots therefore give28 distinct finite punctures,
paired by b -> -b. Isotopy extension of a finite moving configuration
in C supplies a locally trivial bundle Z_U -> U_a with fiber the
28-punctured affine line, based at b=0. The trivializations can be made
equivariant: work in the quotient coordinate z=b^2, move its fourteen
punctures while fixing0 and infinity, and lift the isotopy through the
branched double cover. The lift fixing0 is continuous through the
branch point and commutes with b -> -b. This also proves the actual
geometric, rather than only group-theoretic, equivariance.

The map a -> (a,0) is a global pointwise fixed section on U_a.
As pi2(U_a)=0, the homotopy sequence and this section give

 1 -> F28 -> pi1(Z_U) -> pi1(U_a) -> 1,
 pi1(Z_U)=F28 semidirect pi1(U_a),

with the actual action coming from the section. The source subgroup
is fixed literally. In the fiber the quotient orbifold is the affine
z-line with fourteen punctures and the single order-two cone at0.
Its orbifold group is C2*F14, and the original F28 is its index-two
subgroup. The specified involution represents that cone factor.
The reduced-word normal form gives its centralizer C2, so its fixed
subgroup in F28 is trivial. It follows that the fixed subgroup of
pi1(Z_U) is exactly the actual section image pi1(U_a).

This regular-bundle result also holds in full profinite completion:
finite-index characteristic subgroups of F28 are cofinal and each
finite quotient extends to a finite semidirect quotient of the total
group, exactly as in B87.4. Thus the completed extension is exact with
its actual full induced fiber topology and completed section splitting.
Completion of C2*F14 is C2 amalgam Fhat14, whose cone centralizer is
C2 by the already verified full-category theorem B' of
Herfort and Ribes(1985) used in B87. No assertion about a noncofinal
family of pro-p tests is involved. Hence the completed fixed subgroup
is the closure of the section, with its full profinite topology.

## 4. Why this does not complete the full fixed-subgroup comparison

The actual surface Z includes allowed fibers at critical a values.
The inclusion Z_U -> Z is onto on fundamental groups: a loop in the
smooth real four-manifold can be moved off the finitely many complex
one-dimensional fibers by transversality, and its base point can be
kept fixed. This surjectivity does not imply fixed-element lifting.
If K_a is its actual normal kernel, fixed lifting through this quotient
requires neutrality of the resulting nonabelian H1(C2,K_a) classes.
Neither triviality of the generic fixed fiber group nor surjectivity
of the ambient map proves that requirement.

At a critical value outside the nineteen source punctures, b=0 still
belongs to the surface and the section extends across a small base
disk. Thus its small base lasso dies when that fiber is inserted.
The local collision points occur in pairs b0,-b0 with b0 nonzero.
Their actual van Kampen relations must still be imposed on the fiber;
the section extension does not prove that those relations cannot create
new fixed elements.

At a zero of Q_u the conic is tangent to the a fiber at b=0 and the
source has a puncture. At a zero of P_(u,+) or P_(u,-), two opposite
lines meet at b=0 and the source again has a puncture. The critical
fiber is generally not wholly deleted. These source lassos do not
extend through b=0 and must not be killed as extending section loops.
At a=0 the retained pair a=+-b meets on the deleted source; at a=+-1
the entire a fiber is removed. Multiple other collisions at these
same critical values must be retained in any complete local model.

Consequently the reflection chart yields an exact new projection and
an equivariant generic fixed-subgroup computation. The remaining work
is the actual critical-filling transfer, discretely and in completion.
It has not been proved by this coordinate change. A proposed theorem
for reflection-discriminant complements cannot be substituted without
identifying this particular marked divisor complement and its maps.
