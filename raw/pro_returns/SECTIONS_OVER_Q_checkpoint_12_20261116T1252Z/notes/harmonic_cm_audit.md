# The exact intermediate harmonic curve and a nonzero cocycle

The complete formal comparison is saved in
work/sections/harmonic_tripod_bridge.tex.
Its Selmer-fibre bijection and finite quotient maps were independently
audited by the root and the birational agent.

## The intermediate morphism

For old punctures 0, 1, 1/2, write a_i=R-c_i and
T-c_i=a_i X_i^4. Put W=X_0 X_1 X_(1/2). The literal morphism is

    C_4 -> D_R,
    (T,X_0,X_1,X_(1/2)) -> (T,W),
    D_R: W^4=F(T)/F(R), F(T)=T(T-1)(T-1/2).

Geometrically it is the quotient of the mu4^3 radical cover by the kernel
of the product homomorphism mu4^3 -> mu4. Its degree is 16. At the three
finite branch points the map on inertia has exponent 1; at infinity it has
exponent 3. All four exponents are invertible modulo 4. The proper
normalizations therefore give an etale degree-16 cover, with genera 33 and
3 respectively.

For a new c with F(c)/F(R)=-r^2, the class

    alpha=((T-c)/(R-c),2r)

already extends to the genus-three curve D_R. At the new fibre every
fourth root w of -r^2 contains sqrt(2r), as
((1-w^2/r)w)^2=2r. Its only pole is at the unique infinity point with
order four.

Over L=Q(sqrt(2r)), the two points at T=c satisfying
w^2-sqrt(2r)w+r=0 define Z_+. Put D_c=Z_+-2P_infinity.
Then D_c+sigma(D_c)=div((T-c)/(R-c)). The literal Jacobian cocycle is zero
on G_L and [D_c] on its other coset, with the same HS sign convention as
A.88. Pulling this divisor back through C_4 -> D_R gives exactly the
degree-32 fibre partition and degree-zero cocycle on C_4.

This identifies the map whose kernel needs to be understood:

    H^1(Q,Jac(D_R)) -> H^1(Q,Jac(C_4)).

No vanishing of that map on the displayed class is inferred from local
searches.

## A concrete obstruction on the intermediate curve

For R=32/81, c=25/34, the squareclass of 2r is 210. The rational base
point T=R,W=1 has alpha evaluation zero. At Q2 there is an actual point
with

    T=7,
    W^4=20726199/1904,
    (T-c)/(R-c)=-17253/937.

The fourth-power target has valuation -4 and normalized unit 1 modulo
16, so its root exists in Q2. The normalized first entry has odd unit
3 modulo 8; the second entry 210 has valuation 1 and odd unit 1 modulo
8. The quaternion invariant is therefore 1/2.

Thus the normalized Brauer class and its Jacobian cocycle on D_R are
nonzero. The harmonic CM symmetry does not make this intermediate
cocycle a coboundary.

This local point does not lift to the old C_4: already T/R=567/32 has
valuation -5, which is not divisible by four. The nonzero evaluation
therefore does not provide an obstruction for the completed old triple.

The exact executed certificate and output are
work/code/harmonic_cm_descent_certificate.py and
work/code/harmonic_cm_descent_certificate_output.txt.

## Search outputs retained

work/code/harmonic_tripod_candidate_search.py checked the original R=2,
c=-1/48 candidate at 2,3,5,7,97: 4,968 exact trials, 265 actual local
points, no variation.

work/code/harmonic_tripod_family_search.py checked 462 harmonic covers
whose deleted-coordinate squareclass spans avoid -1: 103,488 exact
dyadic trials, 11,850 actual local points, no nonzero evaluations.

The parent's broader all-bad-prime doubling search and independent-point
E_34 search are retained separately. None of these finite negative
searches is a general constancy proof.
