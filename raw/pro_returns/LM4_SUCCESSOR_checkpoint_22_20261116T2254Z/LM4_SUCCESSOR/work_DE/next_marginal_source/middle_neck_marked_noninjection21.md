# Actual failure of the natural common K on the three middle necks

Research result, checkpoint21; no formal register change. The claim is
about the natural semicircle marking specified below. It does not
exclude every other possible common subgroup marking and does not
decide the global fixed-source problem.

## 1. Coordinates and the literal selected family

Use B.106's actual Q, with `F(t)=-t`, and put

    Q=(1+q)/(1-q),  Z=(t+1)/(t-1).

The inner base is `Re Q>0` with the old point `Q=1` omitted.
The old fifth-root punctures lie on its imaginary boundary. Set

    c_j=cot(pi*j/5),  lambda_j=2/(1+c_j^2),  j=1,2,3,4.

Then `c_1>c_2>0>c_3>c_4`, with `c_3=-c_2,c_4=-c_1`, and

    Z_Aj=lambda_j (Q-i*c_j),   Z_Bj=1/Z_Aj.

The two remaining moving retained punctures are the roots of
`Z^2-2QZ+1=0`; the retained fixed punctures are `Z=0,infinity`.
These are actual coordinate identities, not a model replacing any
divisor.

For k=1,2,3 consider the strip

    Re Q>0,  c_(k+1)<Im Q<c_k.

All four A/B points in its upper Z half-plane are exactly

    B_1,...,B_k, A_(k+1),...,A_4.

Their F partners lie strictly below. Indeed A_j has imaginary sign
`Im Q-c_j`, while inversion reverses that sign. In the corresponding
unit-circle neck the upper Z half-plane is the lower t half-plane,
because `Im t=-2 Im Z/|Z-1|^2`.

The branch roots have product 1, hence their imaginary parts have
opposite signs unless both are real. If Q is nonreal, neither can
be real. For real `0<Q<1`, they are nonreal conjugates and still
have one root in each half-plane. Therefore throughout the k=1,3
strips there is one selected upper branch. For k=2 use only the
part `0<Re Q<1`, which has the same property, including its real
axis. At the boundary this selects the same branch as the natural
lower t semicircle. The selected five-puncture group is K=F5.

## 2. An actual selected-pair collision inside each strip

For i≠j, the equation A_i=B_j is

    lambda_i lambda_j (Q-i*c_i)(Q-i*c_j)=1.

Its unique root in the right half-plane is

    Q_ij=( |1+c_i*c_j| + i*(c_i+c_j) )/2.

This follows by separating real and imaginary parts; the remaining
real equation is `4 (Re Q)^2=(1+c_i*c_j)^2`. The absolute value is
nonzero for distinct fifth-root indices. Choose the adjacent pair
`i=k+1,j=k`. The selected upper punctures A_(k+1) and B_k therefore
meet at Q_k=Q_(k,k+1), strictly inside their strip. Explicitly, put

    c_1=sqrt(1+2/sqrt(5)),  c_2=sqrt(1-2/sqrt(5)),
    x=(1+1/sqrt(5))/2,     y=(c_1+c_2)/2.

The three target values are

    Q_1=x+i*y,  Q_2=1/sqrt(5),  Q_3=x-i*y.

In particular Q_2 lies strictly between 0 and 1. In q coordinates
they are respectively beta_(1,2), beta_(2,3), beta_(3,4), where
beta_(i,j)=u_i*u_j/(u_i+u_j-1).

Choose the actual neck base point `Q=i Im Q_k` and the horizontal
path `Q(s)=s Re Q_k+i Im Q_k`, `0<=s<1`. Its initial q value lies
in the relevant middle unit-circle arc. For k=1,3, its imaginary
coordinate is strictly between the adjacent c values. For k=2 it
is real, with `0<Re Q<1/sqrt(5)<1`. The complete collision table
shows no earlier mixed collision along these paths. At Q_1 and Q_3
only the indicated unordered pair collides (along with its F mate).
At Q_2 the (1,4) pair collides simultaneously with (2,3), at two
distinct points in the upper half-plane and their two lower mates.
Both upper nodes are retained; neither is ignored.

The graph crossing at each target is transverse. At A_i=B_j its
derivative difference is `lambda_i+lambda_j/Z_Aj^2`. Vanishing would
force Z_Aj to be purely imaginary, contrary to its strictly positive
real part. The target is away from the retained branch and old
punctures, also by B.106's complete factorization.

## 3. Based vanishing arcs, not only peripheral labels

Along each compact truncated path the selected five points stay in
the upper Z half-plane and all their partners stay below. The retained
fixed points lie on its boundary. Use one basepoint in that half-plane
outside a large compact set containing the puncture trajectories,
and use the literal punctured-half-plane bundle along the path.
This gives based transport of its entire F5 group. It agrees at the
neck with the natural annular-sector disk and its lower t lift,
up to a single common basepoint connector.

Near the endpoint choose disjoint small collision disks entirely in
the upper half-plane. The actual vanishing arc joining A_(k+1) to
B_k lies in its collision disk. Transport that arc and its two
meridian whiskers back through this same half-plane bundle. Thus
both transported meridians lie in the actual initial K. They form
part of a geometric free basis of K; their commutator is nontrivial.
For k=2 choose either one of the two disjoint upper collision disks.
The simultaneous second node does not alter the free-basis argument.

The ordinary local node complement imposes exactly the commutator
relation for these two meridians when its critical base disk is
included. It follows that the nontrivial K commutator becomes
trivial in the actual inner regional group.

After an arbitrarily short regular-neck transport from the boundary
to `Q=epsilon+i Im Q_k`, this nullhomotopy already lies in the inner
bad piece. All moving Z points then have positive real part, and
the remaining path/vanishing-arc construction can be made in the
upper-right quadrant. The initial boundary punctures themselves
are not asserted to lie in that open quadrant. Hence the
natural K map into that bad orbifold vertex is itself noninjective.
There is no use of an arbitrary unbased conjugacy of meridians.

The same proof applies to the outer bad vertex with the horizontal
path `Q(s)=-s Re Q_k+i Im Q_k`. Its target is the other root of the
same actual collision equation. All selected points now have negative
real part, and the actual comparison takes place in the upper-left
quadrant after a short regular-neck transport. For k=2 use
`-1<Q<0`, so the branch roots are still nonreal. The collision table
is reflected by `Q -> -conjugate(Q)` and has no earlier point on
these paths either. Thus the same natural K is noninjective in
both bad vertices. The two nontrivial killed words need not be
the same based commutator: their transported vanishing arcs may
pass on opposite sides of the other selected punctures.

Any other neck basepoint in the same middle arc has the same result
after the literal critical-free transport along that arc. Throughout
the arc the selected label set is unchanged, and the common gap
connector can be transported with it.

## 4. Scope

The first and last arcs select an unmixed family and admit the
one-family bundle detector. The three middle natural semicircle
markings instead have the explicitly proved local-node kernels on
both sides, with their based words kept distinct.
Consequently those natural K maps cannot be used as injective edge
maps for a global five-neck amalgam. An alternative compatible
marking or a different comparison would require a new proof.

No claim is made that all possible common rank-five subgroups fail,
that the full boundary groups inject, or that the actual global
fixed-source equality is false. All actual critical fibers remain
present throughout the argument.

Exact checker: `check_middle_neck_nodes21.py`, its genuine adjacent
stdout/stderr, and `middle_neck_nodes21.json`. It verifies the three
coordinates, all ten inner critical coordinates, the horizontal-path
incidences including the simultaneous (1,4)/(2,3) pair, and the
algebraic branch inequalities without numerical sampling.
