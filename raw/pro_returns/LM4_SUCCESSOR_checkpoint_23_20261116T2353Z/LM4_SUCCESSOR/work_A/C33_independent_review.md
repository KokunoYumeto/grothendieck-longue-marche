# Independent review of the pro-p pentagon integrality argument

**Reviewed source:** `work_CE/research_C33_metabelian.txt`, 2026-11-16, approximately 04:22 UTC.

**Verdict:** passed for the stated hypothesis D=1+24c2(f) nonzero. The exclusion of D=0 is a separate relative-pro-p braid argument and is not covered by this review.

## Integral coefficient and comparison

For the free pro-p group on x,y, its closed commutator subgroup is the closed normal closure of [x,y]. In the completed integral Magnus module over Lambda=Z_p[[a-1,b-1]], that commutator has vector w0=(1-b)e1+(a-1)e2. The submodule Lambda*w0 is compact and therefore closed. Its uniqueness follows from the domain property and a nonzero coordinate of w0. Thus a commutator word f has a unique integral coefficient F(a,b). Swapping x,y changes w0 to its negative and interchanges the variables; the duality relation therefore gives F(a,b)=F(b,a). The corresponding affine evaluation is obtained first on discrete words and then coefficientwise by continuity. This is compatible with the canonical prounipotent comparison, with no assertion of an unproved closed-subgroup freeness theorem.

## Independent affine calculation

I used the cyclically rotated hexagon C z^m B y^m A x^m=1, where A=f(x,y), B=f(y,z), C=f(z,x), and m=(mu-1)/2. Set a=1+T and x=(a,T), y=(a^(-1),0), z=(1,-T), using affine multiplication (d,v)(e,w)=(de,v+d*w). Put

    k=T(1-a^(-1)), P=F(a,a^(-1)),
    W=F(1,a), Q=F(1,a^(-1)).

The translation part of the hexagon is exactly

    T^2 W - mT + kQ + a^(-m)kP + 1 - a^(-m) = 0.

Applying a -> a^(-1) and multiplying by a gives

    T^2 W + mT + kQ + a^(m+1)kP + a - a^(m+1) = 0.

Their difference is

    mu*T + (a^(m+1)-a^(-m))*(kP-1) = 0.

For nonzero mu this proves exactly

    1 - T(1-a^(-1))F(a,a^(-1))
      = mu*a^m*T/(a^mu-1).

Thus the main identity agrees with the CE derivation under an independently expanded product convention.

## The first denominator

Let R(T) denote the integral left side and H(T)=(a^mu-1)/(mu*T). Then R*H=a^m. Since mu is integral over Z_p and p is odd, m is integral. For n<=p-2 the coefficient of T^n in H has denominator (n+1)!, a p-unit. The coefficient of T^(p-1) in a^m has denominator (p-1)!, also a p-unit. The recurrence at degree p-1 therefore forces the coefficient

    product_(j=1)^(p-1)(mu-j) / p!

to be integral. No binomial integrality in higher degree is used. Hence the numerator lies in p*O_E. Its difference from mu^(p-1)-1 has coefficients divisible by p, so D^((p-1)/2)-1 lies in p*O_E. Since this last expression lies in Q_p, the intersection p*O_E intersect Q_p=p*Z_p proves Euler's criterion over the base residue field. D is a nonzero square modulo p and therefore a square unit in Z_p.

This argument excludes nonzero p-divisible D and nonsquare units. It does not take a limit at mu=0, and the written proof correctly avoids such a limit. It also does not assert the full profinite pentagon-to-hexagon implication.
