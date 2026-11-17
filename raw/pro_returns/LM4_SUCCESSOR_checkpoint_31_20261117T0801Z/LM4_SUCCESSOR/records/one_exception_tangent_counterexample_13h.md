# One exceptional retained tangency does not give relative kernel surjectivity

Research proof, independently checked by CE on16November2026 at approximately13:12UTC. A formal statement B80 is being prepared. This example refutes a proposed general shortcut for the actual marginal problem; it is not a counterexample to that marginal equality.

## The exact relative diagram and its projective boundary

Let X=C^2\{y=x^2}, let D={y=2x-1}∩X, and let Y=X\D. Let the source line be L={y=0}. Its intersections with X and Y are respectively S0=C\{0} and S=C\{0,1/2}, using x as coordinate. All inclusions and fillings are literal inclusions, based at x=-1,y=0. Put

  G=pi1(Y), G0=pi1(X), H=pi1(S), H0=pi1(S0),
  R=ker(G→G0), N=ker(H→H0), I=image(N→G).

The filling maps are surjective. R is the ambient normal closure of a positive meridian of D, and N is the source normal closure of the puncture x=1/2. This follows directly by perturbing loops away from D and null-homotopy disks transversely to D. The deleted divisor is connected: the affine line D loses its tangent point with the parabola, namely(1,1).

In P^2 retain both the parabola yz=x^2 and the infinity line z=0. The source projective line y=0 has only one exceptional intersection with this retained boundary: its order-two tangency with the parabola at(0,0). Its point at infinity is[1:0:0], which lies neither on the parabola nor on the deleted line y=2x-z. It meets the retained infinity line transversely there. Its intersection with the deleted line is the transverse point(x,y)=(1/2,0), outside the retained boundary. Thus the example has exactly the proposed single retained exceptional point and otherwise generic source-boundary intersections.

## A connected actual eight-sheeted cover

Set u=x-1 and v=y-2x+1. Then

  Y={(u,v):v≠0, v≠u^2}.

Let W={(a,b)∈C^2:a*b*(a^2-b^2)≠0} and define

  u=(a^2+b^2)/2,     v=(a^2-b^2)^2/4.

We have u^2-v=a^2b^2, so this map lands in Y. Given(u,v)∈Y, the two distinct nonzero numbers a^2,b^2 are u±sqrt(v). Their two orders and four independent square-root choices give exactly eight points of W. The map is the restriction of a finite polynomial map: a and b are integral over C[u,v], being roots of z^4-2u*z^2+(u^2-v). Its Jacobian is

  -2*a*b*(a^2-b^2),

which never vanishes on W. Hence it is an actual finite unramified cover of degree eight. The complement W of four complex lines is connected, for example by perturbing polygonal paths away from those real-codimension-two lines.

The eight signed permutation matrices act freely on W and transitively on each fiber, so the deck group is D8=(C2)^2⋊S2 of order eight. The chosen basepoint has a lift

  a0=i*(sqrt(6)+sqrt(2))/2,
  b0=i*(sqrt(6)-sqrt(2))/2.

It satisfies a0-b0=i*sqrt(2), x=-1 and y=0. The connected cover therefore gives a specified surjective monodromy q:G→D8 after this marking. Using the opposite convention for deck multiplication replaces this by its inverse convention and does not change any of the subgroups below.

## The complete source image

In the covering coordinates,

  4*y=((a+b)^2+2)*((a-b)^2+2).

The pullback of the source is exactly the four lines a±b=±i*sqrt(2), with their intersections with the deleted covering lines removed. They are disjoint within W: intersections of two distinct lines from different signs force a=0 or b=0, and parallel opposite lines do not meet.

Write c=i*sqrt(2). The component through the chosen lift is a-b=c. Parameterize it by b=t and a=t+c. Its map to the source is

  x=t*(t+c).

Its domain is C\{0,-c,-c/2}. The first two removed values lie over x=0, with nonzero derivatives c and-c. The third lies over x=1/2, where the map has simple ramification; that point is removed from S. Thus this is a connected unramified two-sheeted cover of S. Its deck involution is

  (a,b)↦(-b,-a),  denoted U=-swap.

Equivalently, the stabilizer in D8 of the affine line a-b=c is exactly {1,-swap}. The source monodromy image is therefore q(H)=<U>≅C2. The positive meridian of x=1/2 maps to U, whereas the meridian of x=0 maps to the identity because both of its removed preimages are unramified. Since N is the source normal closure of the first meridian,

  q(I)=q(N)=<U>≅C2.

This calculation covers the whole source group, not only selected generator images or its abelianization.

## The ambient deletion-kernel image and an actual separator

The positive ambient meridian of the deleted divisor v=0 is conjugate to U in D8. Since R is its full ambient normal closure and q(G)=D8,

  q(R)=normal_D8<U>={1,-1,swap,-swap}≅C2×C2.

In particular take F=diag(-1,1). Direct multiplication gives

  F*U*F^(-1)=swap,     swap∉<U>.

F is realized by a retained-parabola meridian. For a completely specified whisker in the covering space, hold b=b0 and move a from a0 to ε=1/10 along the polygon

  a0 → 1+a0 → 1+ε → ε.

This avoids 0, b0 and-b0. Follow the half-circle ε*exp(pi*i*t),0≤t≤1, and then the F-image of the reversed polygon. The projected path is a loop based at(-1,0), with monodromy F. Near a=0 its normal coordinate is a^2, so the projected half-circle is a single positive retained meridian. A source lasso about x=1/2 may use the polygon -1→-1+i→1/2+i→1/2+i/10 and a small positive circle. It has monodromy U by the degree-two source calculation. Their conjugate has image swap and cannot belong to I.

Thus I is strictly smaller than R, although the source has only one exceptional retained boundary point. The finite difference has orders two and four in a fully specified quotient of order eight.

## Full-completion comparison and verification

The actual covering monodromy q is a finite quotient of G and extends continuously to its full profinite completion. The closed ambient deletion kernel is the closed normal closure of the same meridian, so its image is the same four-element group. The actual compact image of the completed source deletion kernel has image the same two-element group. Hence the completed-image equality fails as well. No completion of an unproved abstract subgroup intersection is used.

The exact producer code/root_checks/check_one_exception_tangent_counterexample.py checks the polynomial source factorization, covering Jacobian, source map and deck transformation, every signed permutation, both full finite subgroup images, and the separating conjugate. It ran successfully; genuine stdout is in the adjacent .out file and its full certificate is records/one_exception_tangent_counterexample_certificate.json. CE independently derived the connected source cover, its two unramified x=0 preimages, and its unique ramified x=1/2 preimage before reading this note.

This is a counterexample to the one-exceptional-point relative principle, including its actual full-completion formulation. The actual marginal surface has the additional normal-generation property inherited from LM4 F21, which excludes a nilpotent separator there. The present example does not satisfy that additional property and does not decide the actual marginal normality question.
