# Post-freeze mathematical checks

UTC: 2026-11-17 23:21:27 UTC

These checks address interpretations in the notes, never alter a reading, and make no novelty claim.

## Scans 049/051/055: conic calculation

For x'=-x(x²-3y²), y'=y(y²-3x²), z'=z³:

    x'²+y'²+z'² = (x**2 + y**2 + z**2)*(x**4 + 2*x**2*y**2 - x**2*z**2 + y**4 - y**2*z**2 + z**4)

The remainder modulo x²+y²+z² is zero. The reduction of the sextic expression therefore uses the conic relation; it is not an identity between the two displayed polynomials on all of affine three-space.

The parametrization (1-t²,2t,1+t²) satisfies x²+y²-z²=0 (checked expression = 0). Its all-plus expression is 2(1+t²)², so the two conic conventions require a coordinate change.

## Scan 047: rational dihedral map

    u(t) = -(t - 1)**2/(4*t)
    du/dt = -(t - 1)*(t + 1)/(4*t**2)
    u(t)-1 = -(t + 1)**2/(4*t)

These show double zero at t=1 and double preimage of 1 at t=-1; simple poles at 0 and infinity. Composing t=x_n^n adds the stated order-n ramification there in characteristic zero (or with the required prime-to-characteristic assumptions).

## Scan 085: conditional free-word check, nu=2

Set lambda0=a, lambda1=b, lambda2=(ab)^-1. Take the displayed q2 first as lambda0 lambda1, which is the frozen first reading of its uncertain initial subscript.

    product of images = a b^-1 a^-1 b

This is a nonempty reduced free word, hence disproves the relation for that reading. The same obstruction is flagged by Hua's modernized reading; this check is an independent elementary verification, conditional on the uncertain index.

If instead q2=lambda1:

    product of images = 1
    t(a)=a, t(b)=a^-1 b^-1
    t²(b)=a^-1 b a = a^-1 b a

Thus this alternative repairs the product relation but yields t²=Int(a^-1), not the identity as an actual automorphism. It has order two in the outer group. Relation preservation alone does not establish the manuscript's asserted lift of a Z/2 action to the actual automorphism group.
