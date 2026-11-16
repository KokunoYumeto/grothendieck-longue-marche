# Arithmetic audit of the fourth-factor prime recursion

This records the arithmetic extension requested after A.62. It makes no assertion about a fifth central lifting obstruction. The construction uses the same three coefficient fields, ordinary local limits, and triangular CRT procedure as A.59 and A.62.

Fix a positive integer C divisible by 24. Choose J at least 6 and at least every prime divisor of C, and put

\[
n_j=(j+J)!,\qquad D_j=24C n_j^4,\qquad
E_j(Q)=C n_j(Q^2-1)(Q^3-1)(Q^4-1).
\]

The coefficient invariant remains a=3u^24, b=-2v^24, c=w^24 with disjoint prime supports outside 2 and 3. Every update exponent is divisible by 24n_j. The initial coefficients (3,-2,1) have the exact unit solution (1,1,1).

## The new local image calculation

Let p divide n=n_j, s=v_p(n), and write

\[
F(z)=\exp\bigl(Cn(z^2-1)(z^3-1)(z^4-1)\log z\bigr).
\]

On z=1+p^s w this has the form

\[
F(1+p^s w)=1+A f(w),\qquad
A=24Cn p^{4s},\qquad h=v_p(A)=5s+v_p(24C).
\]

The exact polynomial and logarithmic factors are

\[
\frac{((1+t)^2-1)((1+t)^3-1)((1+t)^4-1)}{24t^3}
=1+3t+\frac{49}{12}t^2+\frac{19}{6}t^3
 +\frac{35}{24}t^4+\frac38t^5+\frac1{24}t^6,
\]

\[
V(t)=\frac{((1+t)^2-1)((1+t)^3-1)((1+t)^4-1)}{24t^3}
      \frac{\log(1+t)}t
=1+\frac52t+\frac{35}{12}t^2+\frac{15}{8}t^3+\cdots.
\]

Each coefficient of degree k is a sum of seven rational terms whose denominator p-adic valuation is at most v_p(24)+floor(log_p(k+1)). The degree-one coefficient is exactly 5/2. Substituting t=p^s w gives

\[
V(p^s w)\in
\begin{cases}
1+p^s\mathbf Z_p\langle w\rangle,&p\text{ odd},\\
1+2^{s-1}\mathbf Z_2\langle w\rangle,&p=2.
\end{cases}
\]

For p=3, the bound uses s>=2; for p=2 it uses s>=4. These follow from J>=6. For example, at p=3 and k>=2 the required inequality is ks-1-floor(log_3(k+1))>=s. At p=2 and k>=2 it is ks-3-floor(log_2(k+1))>=s-1. At the other primes the denominator 24 is a unit and the inequality is immediate. The bounds tend to infinity with k, so these are restricted power series.

In exp(Aw^4V(p^s w)), every term of exponential degree r>=2, after division by A, has coefficient valuation at least (r-1)h-v_p(r!). This is at least s for odd p and at least s-1 for p=2. Consequently

\[
f(w)=
\begin{cases}
w^4+p^sR(w),&p\text{ odd},\\
w^4+2^{s-1}R(w),&p=2,
\end{cases}
\qquad R\in\mathbf Z_p\langle w\rangle.
\]

For odd p, the map

\[
t\longmapsto\frac{f(1+pt)-f(1)}p
\]

equals 4t modulo p, with every nonlinear coefficient divisible by p. It is a bijective restricted power series on Z_p by the elementary contraction/Hensel argument. Thus F maps z=1+p^s(1+pZ_p) exactly onto F(1+p^s)+p^{h+1}Z_p.

For p=2 use w=1+4t. Here

\[
\frac{(1+4t)^4-1}{16}=t+6t^2+16t^3+16t^4.
\]

The correction 2^{s-1}(R(1+4t)-R(1))/16 is a restricted series all of whose coefficients are divisible by 2, because s>=4. The normalized map is therefore t+2G(t), with G an integral restricted series, and is bijective on Z_2. The exact image is

\[
F\bigl(1+2^s(1+4\mathbf Z_2)\bigr)
    =F(1+2^s)+2^{h+4}\mathbf Z_2.
\]

The derivative at z=1+p^s has valuation

\[
\delta_j(p)=4s+v_p(96C).
\]

For odd p this is h-s; for p=2 it is h-s+2. The above expansions show that the leading derivative has exactly this valuation. The error requirement

\[
H_j(p)=2\delta_j(p)+j+3
\]

exceeds the exact image depth: by 3s+v_p(24C)+j+2 at odd p, and by 3s+v_p(24C)+j+3 at 2. It also exceeds 2v_p(D_j). Therefore a common local input, followed by an adjustment in any unit coefficient, solves aF(q)+bF(r)=cF(s) on the permitted balls. Arbitrarily fine later CRT approximation is allowed exactly as in A.62.

## Triangular residues and the new primes

At p dividing n impose v_p(Q-1)=v_p(n). At p not dividing n impose Q nonzero and Q^r not congruent to 1 modulo p for r=2,3,4. Here p>=7. Process every prime up to a bound containing the new small-prime cutoff and all old coefficient primes, with sufficient CRT precision to fix the earlier prime-power factors of each p-1.

For a prime ell dividing n, LTE gives

\[
v_\ell\bigl((Q^2-1)(Q^3-1)(Q^4-1)\bigr)
 =3v_\ell(n)+v_\ell(24),
\]

including ell=2 because Q is 1 modulo 16. Thus v_ell(E_j(Q))=v_ell(D_j). For ell not dividing n, the noncritical residue conditions make both valuations zero. Each exponent map modulo a later prime therefore has exactly the D_j-power image.

At a small high-error prime p not dividing n choose a generator of this common image. Every exponent map has a primitive preimage: write N=p-1, g=gcd(e,N), M=N/g; solve (e/g)k=t modulo M and lift that unit k to a unit modulo N. A primitive residue has order p-1>4, so satisfies all three noncritical conditions.

At a large prime, the forbidden input equations have at most 2+3+4=9 roots. For each of the three coordinate maps there are at most nine forbidden target values. A common scaling of a unit D_j-Fermat point avoids all at most 27 forbidden target values. For p>(D_j+1)^4 and D_j>=2, the D_j-power subgroup has size at least (p-1)/D_j>27: indeed ((D+1)^4-1)/D=D^3+4D^2+6D+4>=40. The same noncritical analytic inverse as in A.62 then gives an exact local triple.

The three radical fields for b/c, a/c, and -a/b retain maximal abelian subfield Q(mu_n), because the coefficient shapes are unchanged. All CRT classes are 1 modulo n, so the exact Chebotarev intersection argument is unchanged.

For each fresh coefficient prime Q the imposed conditions give

\[
\gcd(D_{j+1},Q-1)=n_j.
\]

At an old prime divisor of n_j, the left valuation is precisely v_p(n_j); at a newly introduced factor of n_{j+1}, the noncritical residue excludes Q=1; the fixed factors 24C already divide n_j. Thus the n_j-th and D_{j+1}-th power subgroups of the residue field coincide. Splitting the three old radical ratios gives the three new local unit points exactly as in A.62. Every later update is an n_j-th power, so no mutual congruences between the three new primes are needed.

The all-place invariant, ordinary nonzero local limits, and infinite valuation support follow by the same explicit maps as A.62: local coefficient products converge because n_j eventually annihilates every finite unit quotient, their high-precision sum errors tend to zero, and the numerator/denominator ratios produce the ordinary completed unit pair. This completes the arithmetic audit. A claim about the next nilpotent lifting layer requires its separate global central-obstruction argument.
