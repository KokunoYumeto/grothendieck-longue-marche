# Actual ratio pencil for the positive marginal

Research status: the coordinate comparison and critical-value list below
are proved and checked exactly. The transported van Kampen words and the
uniform normalization of the actual source kernel are not yet proved.
Nothing here closes the original profinite A5 centralizer problem.

## 1. Coordinate isomorphism and finite covers

Write mu5 for the fifth roots of unity and fix the original zeta in mu5.
The positive marginal surface has base

    Y = C minus ({0} union mu5 union (-mu5))

and fiber the p-sphere punctured at0,1,infinity and the five values

    p_u(s)=((u-s)/(u+s))^2,  u in mu5.

Set q=s^2 and t=s(1+p)/(1-p). The inverse is p=(t-s)/(t+s).
All denominators are nonzero in the stated complements. The seven
finite forbidden t-values are +s,-s and(q+u^2)/(2u),u in mu5.
The ordered-root double cover v+w=2t,vw=q is therefore exactly

    Eord = {(v,w,s): s^2=vw;
            v,w notin {0} union mu5; v!=w; vw notin mu5}.

Ordering v,w is an unramified degree-two cover because the discriminant
is excluded. Forgetting s is a separate unramified degree-two cover,
because vw is nonzero. These two covers must not be silently discarded.
The actual source p=(zeta-s)/(zeta+s) becomes the line

    v+w=2zeta,

with its stated s^2=vw pullback. Thus its ordered lift is the actual
finite cover of the source, not a newly chosen unbased line.

Filling the four U punctures in the original marginal removes precisely
the eight conditions v!=u,w!=u for u in mu5 minus{zeta}. It retains
v,w!=0,zeta, v!=w and all five product exclusions vw notin mu5.
In particular the product hyperbolas remain retained divisors.

The map back to the original coordinates gives the based transport:
start from the previously certified original (s,p) basepoint, choose
one of the two roots v,w, and carry that choice continuously. Any later
generic-pencil basepoint must be connected by a specified path in this
ordered cover. No arbitrary change of root ordering is identified with
the identity.

## 2. The pencil and its full critical-value bookkeeping

Put z=w-zeta and lambda=(v-zeta)/(w-zeta). Then

    w=zeta+z,  v=zeta+lambda*z.

The retained conditions force lambda!=0,1 and z!=0. Over this base the
retained fiber punctures are

    0, -zeta, -zeta/lambda,
    b(lambda)=-zeta(lambda+1)/lambda,

and the eight roots of

    lambda*z^2+zeta(lambda+1)z+zeta^2-q=0,
                    q in mu5 minus{zeta^2}.

The eight U punctures are c_u and c_u/lambda, where c_u=u-zeta and
u ranges over mu5 minus{zeta}. The special source is lambda=-1.
There b(lambda) merges with0, and every other puncture remains distinct.
The generic fibers have12 retained and20 total finite punctures; the
source fiber has11 retained and19 total finite punctures.

The finite exceptional values inside C minus{0,1} are exactly:

* lambda=-1, where the two retained punctures0 and b meet;
* eight retained discriminant values, two roots for each q!=zeta^2 of
  lambda^2+(4q/zeta^2-2)lambda+1;
* eight U/zero double points, at1-u/zeta and its inverse;
* twelve U/U/product-hyperbola triple points, at
  (u-zeta)/(v-zeta), for distinct u,v in mu5 minus{zeta}.

The exact cyclotomic certificate proves that these sets are disjoint,
that the double and triple sets respectively have8 and12 distinct
members, and that every discriminant is separable and shares no root
with any other displayed polynomial or event. In particular none of
the U events is lambda=-1. The four triple points on the retained
hyperbola vw=zeta^2 occur at lambda=-u/zeta.

There are no omitted finite collisions. Two product-hyperbola punctures
with different q cannot meet. Product punctures cannot meet a zero
puncture because q!=0. A U/retained-zeta intersection lies over0 or
infinity, outside the pencil base. U/U intersections have product in
mu5, hence are exactly the stated triples; equal U labels meet over1,
also outside the base. The leading fiber degree is constant away from
lambda=0.

Files: `check_ratio_pencil.py`, its actual `.out`, and
`ratio_pencil_data.json`. An initial failed structural-expression
comparison is retained separately; replacing it by equality after
polynomial expansion gives the successful exact run.

## 3. An exact finite van Kampen program, not yet its evaluated words

The ordered surface without the s-cover is the complement over
B=C minus{0,1} of the zero set of the following degree20 polynomial in z:

    z(z+zeta)(lambda*z+zeta)(lambda*z+zeta(lambda+1))
    * product_{q!=zeta^2}
       (lambda*z^2+zeta(lambda+1)z+zeta^2-q)
    * product_{u!=zeta}(z-c_u)(lambda*z-c_u).

The leading coefficient is lambda^10, nonzero on B. A continuous
far-point section exists on all B: choose a positive real z larger
than1 plus the maximum modulus of every root in the fiber. The maximum
over the unordered root set is continuous. The same section works
after filling U. It extends over all29 finite exceptional values.

Choose a generic lambda0 near -1, a path from the actual source
basepoint into that fiber, and a distinguished meridian basis for its
20 punctures. Over the complement of the29 exceptional values the
bundle presentation is F20 semidirect F31. Filling those base values
kills the29 section lifts and imposes their actual pointed monodromy
relations. The two base generators around0 and1 remain. Thus there is
an exact finite presentation with20 fiber generators, two retained base
generators, their monodromy actions, and the29 families of based
monodromy relations. The analogous filled presentation starts withF12.

This use of a generic fiber is justified by the ordinary van Kampen
gluing and also fits Shimada's generalized theorem: the projection is
a submersion on the open surface, every fiber is a nonempty irreducible
punctured affine line, and pi2(B)=0. It does not replace the special
fiber by a generic one. The original s-cover must subsequently be
recovered by the actual winding character of vw modulo2.

That character is explicit with the far-point section just chosen. It
is1 on each of the two zero-puncture meridians z=-zeta and
z=-zeta/lambda,0 on every other fiber meridian,1 on the section loop
around lambda=0, and0 around lambda=1. For the base loops this follows
by homotoping (zeta+lambda*R)(zeta+R) to lambda*R^2, with R larger than
all root moduli. Filling U preserves this character.

The actual marginal kernel and R already lie in the ordered cover:
each U meridian has zero ordering character, and its source-ordering
character factors through the old-source filling. Thus the same is
true of their source conjugates. Both also lie in the s-cover because
q is fixed on the original fiber. Their equality may therefore be
tested after these specified injections, provided their complete
source images, including conjugates arising from the other ordering
coset, are retained. Finite-index subgroup completions embed with the
full induced topology; this finite-cover observation does not replace
the unresolved source-image equality.

Near lambda=-1 choose peripheral generators a,b for the two retained
punctures that merge. The special-fiber generator maps to ab, up to
the orientation/order fixed by the chosen whiskers; all other19-minus1
generators persist. Hence its generic-fiber image is the explicitly
embedded free factor generated by ab and the other18 punctures inside
F20=F(ab,other18)*F(b). The local van Kampen relation is[a,b]=1.

At a U/zero double point the two local meridians commute. At a triple
point with local U meridians x,y and retained hyperbola meridian h,
the local relations make xyh central in the local subgroup. With this
order convention they imply

    h x h^-1 = y^-1 x y,
    h y h^-1 = y^-1 x^-1 y x y.

Thus the local h normalizes the local two-generator U subgroup. This
is a true local identity; it does not yet assert that all occurrences
of h are the same based global element, nor that it normalizes the
entire special-fiber U-kernel.

## 4. The precise remaining global issue

To obtain the desired actual marginal equality, one must transport the
29 monodromies and the special-fiber inclusion in one common marking.
The triple-point conjugating paths are essential. It is insufficient
to note that the special degeneration itself meets only retained
boundary, or to use generic-fiber surjectivity alone. One needs a
uniform identity showing that the extra retained direction preserves
the image of the entire special-fiber U-kernel, including conjugates
by all retained source words. A finite batch of peripheral conjugates
does not establish that invariance.

There are also two retained base directions. The actual total group
has the section generators around lambda=0 and lambda=1, in addition
to the generic-fiber generators. Since the source has lambda=-1,
neither base action is supplied merely by source-fiber normality.
Consequently it is sufficient to prove invariance of the entire
special-fiber U-kernel image under b and under both of those based
section generators (and their inverses): the source image already
normalizes its own kernel, these elements together generate the total
group, and the deletion kernel is the normal closure of the U
meridians. Proving invariance under b alone would not suffice unless
the two base actions had been controlled separately. The local motion
near1 involves the U pairs, while0 is an infinity motion; neither
description is a substitute for the common based transport.

The local types can be made more precise. At lambda=1, each of the
four points c_u is a triple collision of the constant U puncture,
the moving U puncture c_u/lambda, and the retained root belonging to
q=u^2. Their derivatives at1 are respectively0,-c_u,-c_u/2, all
distinct. There is also the double collision of the two retained zero
punctures. A positive local loop thus gives four disjoint three-point
full twists and one disjoint two-point full twist. Since1 is excluded
from the base, these twists give a retained action; their variation
relations are not imposed by filling the base point.

At lambda=0 the ten finite limiting punctures are0,-zeta, and four
pairs at c_u: the constant U puncture and the finite root belonging
to q=zeta*u. The latter root has derivative
-u(u-zeta)/zeta, so each pair is a transverse double collision.
Ten other punctures escape. Four are exactly c_u/lambda. The remaining
six have expansions

    -zeta/lambda + d + O(lambda),
                       d in {0} union (-mu5).

The offsets are all distinct. Equivalently, after rescaling by lambda
these six form one retained cluster at -zeta, distinct from the four
escaping U limits c_u. A local braid description, up to the uncomputed
common transport, is therefore a negative full rotation of all20
punctures, compensated by a positive full twist on the ten finite
punctures, a positive full twist on the six escaping retained
punctures, and four positive pair twists in the finite cluster.
Here positive means pair-linking number+1. Its total pair-linking sum
is-126, or Artin exponent-252 in the corresponding convention; the
lambda=1 local braid has pair-linking sum13. These local decompositions
do not show preservation of the special-fiber subgroup or its kernel.

An independent warning from the root/CE review is decisive: the broad
relative special-fiber lemma is false. The complement
Y={(lambda,z):lambda!=1,z!=0,lambda,1}, with U={z=1} filled to X,
has a retained-only collision at the special fiber lambda=0. Yet
Y is (C minus{0,1}) squared under
(z,r=(lambda-z)/(1-z)), and the special fiber is a graph subgroup F2.
The ambient deletion kernel contains a first-factor commutator outside
that graph, detected in S3 times S3. Thus the actual excluded base
actions and transported triple relations above cannot be omitted.

Even if such an identity proves discrete marginal equality, completion
must be made through the actual finite covers and source images. The
original joint two-point interaction kernel remains a further gate.

## Primary source audit

Shimada, I. (2010). Generalized Zariski-van Kampen theorem and its
application to Grassmannian dual varieties. International Journal of
Mathematics,21(5),591--637. https://doi.org/10.1142/S0129167X10006252.
Corollary1.1 and Theorem3.20 of the author-hosted version were checked.
Primary full text opened and checked16 November2026:
https://home.hiroshima-u.ac.jp/ichiro-shimada/preprints/newZvK/pioneU.pdf
(web retrieval turn682view0). Corollary1.1 states the exact generic-fiber
sequence under the smoothness/irreducibility/section condition, and
Remark1.2 makes the section condition automatic when pi2 of the base
vanishes. No special-fiber or profinite-injection theorem is inferred.
Publication metadata was independently verified on the author's
publication list, item36:
https://home.hiroshima-u.ac.jp/ichiro-shimada/publications.html
(web retrieval turn683view0).

The older institutional path and one lecture-note path timed out;
those failures are not used as evidence. The newer author-hosted full
text is the source actually read.
