# A relative special-fiber shortcut is false

Research proof, 16 November 2026. This is a counterexample to a proposed
general reduction, not to the actual icosahedral marginal statement.
It is retained separately from the frozen eleventh-checkpoint paper.

## Exact spaces and maps

Let B be the complex affine line with1 removed. In B times the affine
z-line, define the smooth connected algebraic surfaces

    Y={(lambda,z):lambda!=1; z!=0,lambda,1},
    X={(lambda,z):lambda!=1; z!=0,lambda}.

The inclusion j:Y→X fills exactly the divisor U given by z=1,
lambda!=1. Projection to lambda has a generic three-punctured affine
fiber on Y and a generic two-punctured affine fiber on X. At lambda=0,
the two RETAINED punctures0 andlambda coincide; the U puncture1 stays
distinct. All leading fiber degrees are constant. The only finite
exceptional value in B is0, with this retained node. A continuous far
section exists for both projections, for example choose real
z=2+|lambda|, which has modulus larger than |lambda| and is larger than1.

The special fibers are L_Y=C\{0,1} and L_X=C\{0}. Their natural inclusion
commutes with j. Choose z*=2 on lambda=0 as basepoint in all four spaces.
The question is whether the actual image of

    ker[pi1(L_Y,2)→pi1(L_X,2)]

under special-fiber inclusion equals ker[pi1(Y,(0,2))→pi1(X,(0,2))].
The answer is no, even after profinite completion.

## The product chart and the actual source subgroup

Put r=(lambda-z)/(1-z). The inverse is lambda=z+r(1-z). On Y the
conditions are exactly z!=0,1 and r!=0,1. Thus this is an algebraic
isomorphism

    Y ≅ (C\{0,1}) times (C\{0,1}).

It sends the basepoint to(2,2). The special fiber lambda=0 is the graph
of f(z)=z/(z-1). This Möbius transformation fixes2, is an involution,
and permutes the three missing points0,1,infinity. It is therefore an
actual based automorphism of the three-punctured sphere. Write
F=pi1(C\{0,1},2), a free discrete group of rank two. After using f_* to
identify the second factor with the first, the special-fiber image is
precisely the diagonal subgroup

    H={(g,g):g in F} ⊂ F times F = pi1(Y).

This identifies the full source subgroup, not only its normal closure
or abelianized image. In particular the source deletion-kernel image
is contained in H.

## The filled fundamental group, with its comparison proved

Project X to its z coordinate, which ranges over C*. For z!=1, the
lambda-fiber is C minus{1,z}; for z=1 it is C minus{1}. The only
degeneration is the ordinary transverse node of the two deleted
sections lambda=1 andlambda=z. A far continuous section exists.

Choose the two generic fiber meridians p,q and based base loops around
z=0 andz=1. The latter loop is the full twist of these two meridians.
Filling its base disk kills its section lift and imposes exactly the
node relation[p,q]=1: the full twist acts by conjugation withpq, and
triviality of that action is equivalent to this one commutator relation.
The loop about z=0 acts trivially on the two-puncture fiber group.
Indeed the moving puncture z makes a small loop around0 avoiding the
fixed puncture1, and that loop contracts in C\{1}; the far section
has no additional basepoint winding. No other finite degeneration or
degree drop occurs. Ordinary based van Kampen consequently gives

    pi1(X) = <p,q,t | [p,q]=[t,p]=[t,q]=1> ≅ Z^3.

Equivalently X is the complement of the three distinct affine lines
z=0,lambda=1,lambda=z, whose three pairwise intersections are distinct;
the calculation above proves the specific arrangement conclusion used.

Let a,b be a free basis of the first F factor of pi1(Y). Since pi1(X)
is abelian, the nonidentity element

    w=([a,b],1) in F times F

belongs to the ambient deletion kernel. It is outside H because its
second coordinate is1 and its first coordinate is nonidentity. It is
therefore outside the image of the source deletion kernel. This proves
the claimed failure without any conjectural generic-section statement.

## Finite certificate and the completed failure

Map each F to S3, using the same identified basis, by
a→(12), b→(23). This is an epimorphism, and the source graph maps to
the diagonal S3 in S3 times S3. The image of[a,b] is a nonidentity
3-cycle. Thus w maps to(3-cycle,1), outside the diagonal finite subgroup.
The actual symbolic chart identities, the36-element product, its
six-element diagonal, and the nonmembership are checked by

    code/check_special_fiber_relative_counterexample.py
    records/check_special_fiber_relative_counterexample.out
    records/special_fiber_relative_counterexample.json.

The finite quotient proves that w is outside the closure of H, and
hence outside the closure of the source deletion kernel. Its image in
the completion of pi1(X) is still1, since the discrete image already
is1. Therefore equality also fails for the corresponding actual images
in full profinite completions. No completeness of an induced topology
on an infinitely generated kernel is needed for this conclusion.

## Relevance and boundary of the conclusion

The special fiber has only a retained collision; all U punctures stay
transverse and finite. Those facts and the existence of a far section
do not suffice for relative source surjectivity. The missing base value
lambda=1 contains a U triple in the compactified pencil; its monodromy
cannot be discarded. The actual icosahedral ratio pencil has two
excluded base values0 and1, whose transported actions must likewise
be controlled along with its29 finite exceptional values. This example
does not assert that those actual actions fail the needed condition.

CE independently verified the product chart, graph subgroup, abelian
filled group and finite quotient before reading this saved proof.
Root also independently opened Shimada(2010), Corollary1.1 and
Remark1.2 in the author-hosted PDF and the author's publication item36
(retrievals turn684view0 and turn684view1). That primary theorem supplies
the generic-fiber framework, not the false special-fiber conclusion.

Shimada, I. (2010). Generalized Zariski-van Kampen theorem and its
application to Grassmannian dual varieties. International Journal of
Mathematics,21(5),591-637. https://doi.org/10.1142/S0129167X10006252.
Primary source verified: https://home.hiroshima-u.ac.jp/ichiro-shimada/preprints/newZvK/pioneU.pdf.
