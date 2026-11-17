# The local source-modified w=1 motion

This is a local datum only. It does not specify the global common whiskers
of the w-pencil and is not a source-normality assertion.

Put w=1+epsilon and translate the v-coordinate by1. In a small disk about
v=1 the three actual fiber points and the source are

    source S=−epsilon;
    product-one P=−epsilon/(1+epsilon);
    constant-one X=0;
    diagonal D=epsilon.

For epsilon=r exp(2 pi i t), 0<r<1/4, divide all four coordinates by
epsilon. The moving rotation contributes the positive full4 twist.
In the divided coordinates S=−1,X=0,D=1 are fixed and
P=−1/(1+epsilon). Its displacement from S is epsilon/(1+epsilon), which
winds once positively and remains in the disk of radius r/(1−r)<1/3
about S. Hence the residual motion is exactly one source/product full
twist. In the local real order S,P,X,D,

    beta = Delta4^2 sigma1^2.

A half-turn of the disk gives order D,X,P,S and beta=Delta4^2 sigma3^2.
This preserves orientation. The source is now last, so the same exact
Birman convention as B81 applies: the inverse of the last Artin
conjugator is the actual fiber homomorphism. If p is the image of
sigma3^2, p=x3^-1 in this chosen free basis. The central full4 twist acts
trivially on the source-based three-puncture fiber. Therefore the actual
local source action is exactly Inn(p). Forgetting the source gives the
full3 twist on P,X,D. All statements are verified by faithful Artin
identities in w1_local_source_monodromy.py/.out/.json.

The full w=1 fiber also has four disjoint nodes: each constant v=u,
u!=1, meets the product point v=u/w. Thus the full13-strand motion has
this four-point source cluster together with four two-point full twists.
The exponent counts are22 with the source and14 after forgetting it:
14+4*2 and6+4*2, respectively. This is a local-type count; no complete
based13-strand word or global operator identity has yet been asserted.

For an efficient global common-marking computation, use z=wv, since
w never vanishes on the base. Then the twelve fiber points and source are

    0; w*u (u in mu5); w^2; u (u in mu5); source w(2−w).

All trajectories are polynomials of degree at most2 along a linear w
segment. The base critical values are0 and plus/minus mu5. The five
negative-root values are filled ordinary nodes. The source adds w=2,
four values2−u and eight roots1 plus/minus sqrt(1−u), u!=1. The original
source F19 is obtained after filling the five negative-root base loops.
This polynomial model retains the distinction between the source point
and the nearby product-one point at w=1.
