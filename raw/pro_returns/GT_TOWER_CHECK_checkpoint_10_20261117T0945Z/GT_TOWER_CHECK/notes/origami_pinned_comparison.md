# The retained tangential comparison for the two-step origami

Primary source reopened: Möller, arXiv math/0311308v2, 11 October2004, Proposition4.2, Remark4.3, Theorem7.1, and Sections7.1–7.4, especially PDF pages15–19. Source URL: https://arxiv.org/pdf/math/0311308 . The journal reference is retained as Moeller2005. The current proof B.4.3 establishes the explicitly defined outer orbit invariant. It does not identify an unspecified comparison path with the source's tangential path.

## Exact coordinate comparison now checked

For P(x)=4x(x−1), the family X_t has equation y²=(P²−(1−t))(P−1). The change

u=(2x−1)/sqrt(2), v=y/sqrt(2)

over Q(sqrt(2)) gives the Q-model

v²=(u²−1)(4u⁴−4u²+t).

Conjugation of sqrt(2) changes the original coordinates by the actual automorphism (x,y)↦(1−x,−y). At t=0, the new model has two rational components v=±2u(u²−1) meeting at the three rational nodes u=−1,0,1. The original model's two nodes (1±sqrt(2))/2 are conjugate. This coordinate calculation keeps the quadratic form and its automorphism explicit; it is not a criticism of the primary theorem, whose orbifold splitting and quilt must be compared before identifying arithmetic base points.

With w=v/2 and r=u−a, the exact total-degree-two local equations are

- a=0: w²−r²+t/4=0;
- a=1: w²−4r²−tr/2=0;
- a=−1: w²−4r²+tr/2=0.

Completing the square in either outer-node equation gives the leading smoothing term −t²/64. The coordinate z=(u+1)/(1−u), with the reciprocal at infinity, has node derivatives 1/2,2,−1/2. These are exact algebraic calculations. Their conversion into the deformation coordinates fixed by the HLS quilt remains to be proved. In particular no Kummer exponent is read off from these coordinates without that comparison.

## What remains

The outer conjugator of B.4.3 must be compared with the source's particular tangential splitting. The finite automorphism of the quadratic form above is part of that data. A maximal-pants centralizer description alone does not choose its finite component or its three procyclic exponents. The next exact step is to construct the quilt deformation coordinates for this rational nodal form and compose the two quadratic choice-subgroup witnesses with that base-point transport. No equality with Möller's pinned relation is currently promoted to a theorem.

Executed source: code/check_origami_rational_node_form.py, with its actual output. The initial failed structural SymPy equality assertion and its output are retained separately with suffix _initial. It was replaced by an expanded polynomial equality; the mathematical formula did not change. The final program verifies every displayed polynomial and word-coordinate comparison above.
