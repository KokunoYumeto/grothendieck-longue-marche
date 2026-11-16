# Common based monodromy in the actual polynomial pencil

This is an exact certificate for six specified braids and their four
local triple transports. It does not establish the full marginal
source-image equality. The distinction between finite pair identities
and normalization of the whole source kernel is retained throughout.

## 1. The polynomial model and its source

Start with the actual ratio-pencil comparison in
`ratio_pencil_comparison.md`. Scale v,w,s by the original zeta; this
permutes mu5 and makes the distinguished retained root equal1. Put

    t=1+1/lambda,   z=w-1.

The base is C minus{1,2}, and the source is t=0. The twenty generic
finite punctures of the z-line are

    0, -1, 1-t, -t;
    u-1, (u-1)(t-1),                  u in mu5 minus{1};
    roots of z^2+t z+(t-1)(1-q),      q in mu5 minus{1}.

There are twelve retained punctures (the first four and eight
quadratic roots) and eight U punctures. At t=0 precisely0 and -t
merge; all the other eighteen punctures remain distinct. The actual
special fiber therefore has free group F19, and filling its eight U
punctures gives F11.

The two finite covers in the ratio-pencil note are essential. The
ordered source is a degree-two cover of the original s-source and
also a degree-two cover of this special z-line. Each of those cover
characters factors through the corresponding U filling: the new U
meridians have trivial character. Consequently both discrete source
deletion kernels are literally the same kernel inside the common
cover. The same conclusion holds for actual kernels in full source
completions because finite-index subgroup completions embed and the
characters are finite. This does not use full topology of an abstract
infinite-rank kernel. The analogous ambient cover comparison identifies
the actual marginal filling kernel with the ambient U-deletion kernel
in this model.

Here is a specified common basepoint path, rather than an unspecified
change of marking. Fix the original distinguished root explicitly as
zeta=exp(2*pi*i/5), the number denoted u[1] in the certificate. In the
original s-source use the polygon

    2+2i  -->  10+10i  -->  zeta*i*sqrt(9999).

All original source punctures have modulus<2: the new squared values
are u(2zeta-u), of modulus<=3. The first segment stays outside the
disk of radius2; the second has imaginary part at least10, since its
ending imaginary part is cos(2*pi/5)*sqrt(9999)>29. At the
endpoint choose the ordering v=-99zeta,w=101zeta. Lift the source path
backward to fix the original root ordering. In normalized coordinates
the special fiber basepoint is z=100. Continue to the generic fiber
along t=i*y,0<=y<=1/100, keeping z=100 and lifting s^2=vw continuously.
All forbidden q-values stay far from this path. Thus the generic
basepoint t*=i/100,z*=100 is connected to the original one by actual
paths in the stated spaces and covers.

The chosen projection is multiplication by P=1+371i/1000. Along the
short source-to-generic path the two merging points are adjacent in
projection; every other projected real coordinate stays outside
(-.01,.01). The coefficient and projection bounds are checked in
`audit_pencil_geometry.py`. The based whisker convention is as follows.
Use the projected coordinate Pz and the standard Artin cut system on
the ordered punctures: its positive half twist has action
x_i -> x_i*x_(i+1)*x_i^-1, x_(i+1) -> x_i, and the positively oriented
boundary of a disk enclosing consecutive punctures i,...,j is the
based word x_i*...*x_j. This convention can equivalently be fixed by
an order-preserving vertical isotopy to punctures on a horizontal line
and the usual disjoint lower cuts, with the exterior basepoint joined
to their common base by a fixed path outside a large disk.

Choose the disk D= {|Pz|<1/20}. Along the source-to-generic path it
contains exactly the two merging punctures, and its boundary is
disjoint from every strand. Choose one based cut from z=100 to its
lower boundary in the above cut system. Inside D the two standard
meridians are a=x10,b=x11, and its based positive boundary is literally
ab. Transport all the remaining cuts outside D backwards along the
short path, and use the same cut to D for the special puncture. This
defines a concrete free basis of the actual special fiber. Its image
is {x1,...,x9,ab,x12,...,x20}. No claim that an independently chosen
old source lasso system is this basis is needed: the specified common
source path identifies the source group, and filling-kernel images
are unchanged by this explicit source basis change. Thus H is an
actual based source image, not just an abstract free factor suggested
by adjacency.

## 2. Exact rational deformation of the geometric loop data

The four nontrivial roots of unity are replaced by the thirty-decimal
rational complex numbers recorded in `quadratic_pencil_braid.py`.
Nested rational square-root intervals for sqrt5 and sqrt(10+-2sqrt5)
prove error<10^-30 in each real and imaginary coordinate. We deform
the coefficients along straight segments. This is only a deformation
of the configurations on the specified parameter paths; we do not
claim that the entire discriminant arrangement keeps its topology.

The six lassos are based at t*=i/100. Each travels straight to the
northeast corner of the square of half-side1/1000 about its center,
traverses that square counterclockwise, and returns along its whisker.
The centers are1,2 and the four rational approximations to1-u. The
exact original critical clusters lie in those squares. Every segment
has |t|<5. Every puncture has modulus<25. The engine proves on every
closed segment:

* every rational pair difference has modulus>10^-12;
* evaluating a retained quadratic at any rational puncture has
  modulus>10^-12;
* each projected squared root U=P^2 D/4 has modulus>10^-8;
* |t-1|>10^-8.

Each assertion is an exact positivity check for a rational polynomial
on[0,1], using its endpoint signs and its Sturm root count. Distinct
q-values have distance>1. For a rational/quadratic pair the quadratic
residual is the product of its two root differences, and the other
difference is<50. For roots from different quadratics the corresponding
residual is(t-1)(q_i-q_j). These estimates give a uniform pair
separation>2*10^-14 on every segment.

The coefficient deformation changes a projected square by<24*10^-30.
Its square-root branch therefore moves by<10^-23, using the recorded
lower bound on its modulus; rational punctures move by still less.
This is much smaller than the pair separation. Hence the six computed
braids are exactly the braids of the original cyclotomic family on
these specified paths. In particular, splitting a multiple critical
value in the rational coefficient model does not alter its enclosing
loop braid.

## 3. Complete crossing equations and rational interval verification

Write a projected quadratic pair as c+-sqrt(U), where c=-Pt/2 and
U=A+iB has rational polynomial coefficients on each segment. The
projection-crossing candidates are complete:

* two rational punctures: equality of their real affine functions;
* the two roots of one quadratic: B=0;
* a quadratic root and rational puncture with real offset h from c:
  4h^2(h^2-A)-B^2=0;
* two quadratic pairs U_i=A+iB,U_j=C+iD: with delta=C-A and
  N=B^2-D^2, the equation N^2-4AN*delta-4B^2*delta^2=0.

Their degrees are at most1,2,4 and6, respectively. All real roots in
(0,1) are isolated by rational Sturm intervals. Overlapping intervals
from different equations must have an actual common polynomial root;
the program checks this by a gcd/root-count calculation. Roots at a
segment endpoint are separately excluded or flagged, not silently lost.

At every rational sample, real and imaginary square-root bounds use

    Re(sqrt(A+iB))^2=(sqrt(A^2+B^2)+A)/2,
    Im(sqrt(A+iB))^2=(sqrt(A^2+B^2)-A)/2.

The analytic branch is tracked by the exact odd-multiplicity crossings
of the negative real axis. A derivative bound10^8, proved from the
same polynomial coefficients and radicand lower bound, encloses each
crossing height. Thus every comparison of projected order and every
over/under sign is rationally certified. Extraneous algebraic
candidates give no change of order and are rejected. Simultaneous
crossings are accepted only when their strand pairs are disjoint;
the corresponding generators commute. The ending order is checked
against the independent endpoint calculation.

The initial cut-handling failure is retained in
`quadratic_pencil_braid.failed_principal_cut.out/.err`. The corrected
engine evaluates immediately before a candidate interval and uses
the derivative bound over it. The successful output is a genuine
rerun. No missing stdout was reconstructed.

## 4. The actual words and common free basis

The initial strand labels in projection order are

    [6,8,15,17,13,4,1,19,10,0,3,11,18,2,5,12,16,14,9,7].

In this order the merging meridians are a=x10 and b=x11. Put
c=x10*x11 and retain b=x11 as the missing generator. Rewriting
x10=c*b^-1 is a literal Nielsen change of basis. The special-fiber
free factor H consists of all nineteen new basis generators exceptb.
The eight U basis indices are

    [1,2,6,9,12,15,19,20].

The exact braid lengths and exponent sums are:

| Loop | Reduced word length | Artin exponent |
|---|---:|---:|
| retained t=1 |240|128|
| retained t=2 |242|26|
| b triple1 |72|6|
| b triple2 |184|6|
| b triple3 |140|6|
| b triple4 |56|6|

All six words are pure. The exponent sums match the independently
derived local cluster types. At1 there are ten- and six-point clusters
and four extra pair twists from second-order tangencies. At2 there
are four triples and one retained double collision. Each of the four
filled b-triple circles is verified by the faithful Artin action to
be the positive full twist on its three actual consecutive strands.

The common whisker Artin actions and their inverses are checked on all
twenty free generators. The transported b meridians have H-conjugators

    h1=4 7 8 9,
    h2=2 3 4 5 7 8 9,
    h3=9 16 20^-1 16^-1,
    h4=9.

These are literal words in the new free basis, not just conjugacy
classes. Some transported U meridians contain b. After normalizing by
h_i and performing the displayed local Hurwitz changes, however, the
central products are P_i Q_i b (or cyclically b P_i Q_i), where

    P1=(7 8 9)^-1 6 (7 8 9),       Q1=10 12 10^-1,
    P2=(2 3 4 5 7 8 9)^-1 1 (2 3 4 5 7 8 9),
    Q2=(10 12 14 15 16 17 18) 19 (10 12 14 15 16 17 18)^-1,
    P3=16 20 16^-1,                Q3=9^-1 2 9,
    P4=15,                        Q4=9.

The resulting finite pair-normalization relations are exact. These
eight words together with the eleven retained H generators form a
triangular Nielsen basis: solve9,15 first; then20,2; then6,12; finally
1,19. This observation is useful for analyzing the partial presentation.
It still does not prove b-normality of the entire H-normal closure of
the U generators. Arbitrary retained H-conjugates remain part of that
condition, and the other filled monodromy relations may be essential.

## 5. Files and exact scope

The producer is `quadratic_pencil_braid.py`, with actual `.out/.err`.
`ratio_pencil_braids.json` retains all thirty segment polynomial,
root-isolation and crossing-height records. `ratio_pencil_words.json`
is the concise word list. `audit_pencil_geometry.py/.out` and
`pencil_geometry_audit.json` verify the coefficient and common-source
marking bounds. `extract_pencil_transports.py/.out` and
`pencil_triple_transports.json` contain the literal transported meridians
and both inverse-action checks.

The source/kernel comparisons are actual finite-cover comparisons,
and the six braid words are exact. Neither the full source-image
equality nor a nonidentity element of the original completed
intersection follows. The root/CE counterexample B76 explicitly
refutes replacing this calculation by a broad relative special-fiber
lemma.
