# Filling only the retained product-one divisor

Research proof for independent review, 2026-11-16 approximately13:04UTC.
This is an exact localization of the existing marginal gap, not a claim
that the original source image is full.

## Actual spaces and maps

Use the normalized ordered surface of B78:
Y={(v,w): v,w notin {0} union mu5, v!=w, vw notin mu5}.
Let U be the union of the eight deleted vertical/horizontal divisors
v=u or w=u, u in mu5\{1}. Write Y0 for their filling, retaining
v=0,w=0,v=1,w=1,v=w and all five product hyperbolas.
Let P denote the product-one divisor vw=1 and let Y+ and Y0+ be
obtained by filling P in Y and Y0 respectively. All other conditions
remain as just specified. Every inclusion is the literal inclusion of
these complex surfaces, with the same common source basepoint and
comparison paths of B78. The source is S={v+w=2} intersect Y.
Since v+w=2 and vw=1 force v=w=1, a point still excluded by the
other retained divisors, S is UNCHANGED by filling P. Its U-filling
S0 is also unchanged. Thus pi1(S)=F19 and pi1(S0)=F11 still apply.

Put G=pi1(Y), G0=pi1(Y0), G+=pi1(Y+), G0+=pi1(Y0+).
All four ambient filling maps are onto, with kernels the normal
closures of the actual positive meridians of the filled components.
This follows by transverse perturbation of loops and null-homotopy
disks; no injection of a divisor fundamental group is assumed.
Let R=ker(G->G0), Pker=ker(G->G+), R+=ker(G+->G0+).
Let N=ker(pi1(S)->pi1(S0)), and I be its actual image in G.

## The source becomes generic in the ratio pencil

Keep B78 coordinates lambda=(v-1)/(w-1), t=1+lambda^-1, z=w-1.
The base remains B=C\{1,2}. Filling vw=1 removes precisely the
puncture z=-t from B78's generic twenty-puncture list: the other
factor z=0 of the product-one equation was already removed by
v=1 or w=1 and remains removed. The nineteen punctures of Y+ are

  0,-1,1-t;
  u-1,(u-1)(t-1), u in mu5\{1};
  z^2+t*z+(t-1)*(1-q)=0, q in mu5\{1}.

At t=0 these nineteen punctures are pairwise distinct. The old
merging product-one puncture -t is exactly the removed one. Every
remaining potential coincidence is excluded by the B78 cyclotomic
collision list, or directly by u+v!=2 for distinct/nonidentity unit
roots and q!=1. Hence the actual source S is now a generic fiber.
After filling U the same statement holds with eleven punctures.
Both pencils have constant degree, only finitely many critical
values in B, and a common far-point section. There is no finite
escape value. A continuous section is obtained by taking z on a
fixed ray beyond a continuous root bound for all punctures.

## Exact generic-fiber kernel equality

Remove the union Sigma of the two finite critical sets from B.
The two total spaces over B\Sigma are bundles with fibers F19
and F11, with the same section. Their groups are the semidirect
products of those fiber groups by pi1(B\Sigma). The fiber filling
kills exactly N, the normal closure of the eight U meridians.
Every monodromy preserves N: it preserves the union U and the
retained punctures, and descends to the actual filled-fiber
monodromy. Thus the quotient of the first semidirect product by
N is exactly the second.

Restoring all critical fibers imposes, in each group, the actual
variation relations and kills the section-based loops of Sigma.
Under F19->F11, the first variation relations map exactly to the
second. A value at which the filled pencil is smooth contributes
identity monodromy there; its projected relations are trivial.
Retained base loops of B are the same on both sides. Consequently
G+ / image(N) is G0+, with precisely the geometric filling map.
In particular image(N) is normal in G+ and equals R+.
This is proved using the generic source in Y+, not by applying a
relative-special-fiber theorem to Y.

## Localization of the unresolved obstruction

The map R->R+ is onto, since R is the ambient normal closure of U,
and G->G+ is onto. The previous paragraph says that I also maps
onto R+. Therefore

  R = I * (R intersect Pker),

as a subgroup product (the second factor is normal in R).
The induced map of right-coset spaces

  (I intersect Pker)\(R intersect Pker) -> I\R

is bijective. Thus I=R if and only if R intersect Pker is contained
in I. This is the interaction of the U-filling with the retained
product-one filling. It is not eliminated by merely knowing that
I normally generates R or that selected U meridians are normalized.

The same proof applies to the ACTUAL compact images in full
completions. Completing a quotient presentation replaces each
normal closure by its closed normal closure. The image of the
compact source kernel is the closure of its discrete image.
Both R and Pker complete here as ambient closed kernels, not as
abstract completions of infinitely generated discrete groups.
Surjectivity, subgroup products, and the displayed coset comparison
then follow by compactness. The latter is a homeomorphism because
it is a continuous bijection between compact Hausdorff spaces.

In particular every actual finite quotient of G that kills the
product-one meridian has equal images of I and R. A separating
finite quotient must retain that meridian. No stronger assertion
about arbitrary finite quotients, uniform normality, or K=1 follows.

## Relation to existing work

B78 already reduces the full marginal equality to normalization
by its based missing product-one direction. This geometric filling
argument explains why that direction is essential and gives an
explicit two-kernel localization. It does not claim a new solution
or replace the whole-kernel normality gate. All previous finite
covers identifying this ordered model with the original marginal
remain those of B78; filling P is used only as a diagnostic quotient.
