# Exact Hankel criterion for odd theta torsion on ordinary genus-two curves

Status: the complete elementary criterion and the exact five-torsion
application are integrated in A.C2.18 after root review. Broader bounded
scans remain audit evidence until their exact scopes are reviewed. Written 14 November 2026.

Let k be algebraically closed of characteristic two and let

C: y²+y=φ(x)=a x+b/x+c/(x+1),  abc≠0.

Write W0,W1,W∞ for its three ramification points and
Bθ=W0+W1−W∞ for the locally exact differential theta characteristic.
The curve is ordinary of genus two, and its symmetric theta is
Θ={O(R−Bθ):R∈C(k)}.

## 1. A complete geometric criterion

Let n≥3 be odd, put d=(n−3)/2, and let R=(t,β), t≠0,1,
β²+β=φ(t). Then n[R−Bθ]=0 if and only if there is a nonzero
function h in

L(W0+W1+(n−2)W∞)

vanishing to order at least n at R. Indeed any such function has a
pole divisor bounded by an effective divisor of total degree n, so
its divisor must be exactly

nR−W0−W1−(n−2)W∞.

Dividing by u^((n−1)/2), u=x(x+1), gives n(R−Bθ).
Conversely multiplication of a function with divisor n(R−Bθ) by
that power of u gives the required h.

The pole space has dimension n−1=2d+2 and the basis

1,x,...,x^d, y,xy,...,x^d y.

The listed functions have the required poles and are independent;
Riemann–Roch gives the dimension since n>2g−2. Thus

h=A(x)+B(x)(y+β),  deg A,deg B≤d.

For an odd-torsion theta point, R cannot be a ramification point:
2W and 2Bθ are canonical at each W, so [W−Bθ] is killed by two.
The origin is not on ordinary theta. Hence the t-chart exhausts
all points relevant to odd n; no theta point at infinity is omitted.

## 2. The local power series and rectangular matrix

Let z=x+t and expand

y+β=Σ_(i≥1) y_i z^i.

The branch is uniquely determined by its zero constant term, since
the derivative of Y²+Y is one. The coefficients satisfy

y_i = a δ_(i,1)+ b/t^(i+1)+c/(t+1)^(i+1)
      + (y_(i/2))² if i is even,

with the final term absent for odd i.
This follows by comparing coefficients in
Y²+Y=φ(t+z)+φ(t); the expansion of 1/(t+z) has all coefficients
t^(-i-1) in characteristic two.

Write B(t+z)=Σ_(j=0)^d b_j z^j. The coefficients of A(t+z)
uniquely cancel the first d+1 coefficients of B(t+z)Y(z).
The remaining vanishing conditions are

Σ_(j=0)^d b_j y_(i−j)=0,  i=d+1,...,n−1.

Thus n[R−Bθ]=0 if and only if the (d+2)×(d+1) matrix
(y_(i−j)) has nontrivial kernel, equivalently all its maximal
minors vanish. A vector with B=0 is not a spurious solution:
then A would have degree at most d yet vanish to order n at an
unramified finite coordinate, so it would be zero too.

Put D=t(t+1) and P_i=D^(2i)y_i. These are polynomials given by

P_i=b t^(i−1)(t+1)^(2i)
    +c t^(2i)(t+1)^(i−1)
    +a δ_(i,1)D²
    +(P_(i/2))²  when i is even.

The final term is absent for odd i. Multiplying row i by D^(2i)
and column j by D^(−2j) changes the matrix into (P_(i−j)).
Since D≠0, this preserves rank. Therefore the geometric
theta-n coordinates are precisely the zeros away from 0,1 of
the gcd of all maximal minors of this polynomial matrix.

Not all minors are identically zero: that would put every
unramified R on the finite group J[n], contradicting injectivity
of the Abel map. Removing all factors t and t+1 from the gcd
therefore gives a nonzero polynomial with exactly the desired
geometric zero set. Multiplicities are not needed here.
This is a complete algebraic-closure test, not a finite rational
point search.

## 3. Exact implementation and bounded scan scope

code/A_theta_F4_scan.py implements this criterion using the exact
F4 polynomial arithmetic and fraction-free determinant routine
in code/A_theta_three_power_experiment.py. F4 polynomials are
represented by two binary coefficient masks for 1 and α, where
α²+α+1=0. Euclidean division and gcd are exact. The Bareiss
determinant uses row swaps and exact division by the prior pivot;
row-swap signs disappear in characteristic two.

The algorithm computes all d+2 maximal minors unless the current
gcd is already a unit after removing branch factors. That early
termination is conclusive, since adjoining further minors can
only decrease the gcd. A positive answer is issued only after
all maximal minors have been included.

For n=3,5,7,9,13, the ten unordered nonzero F4 coefficient triples
give the following geometric existence table. An entry means
torsion killed by n, not necessarily of exact order n.

| (a,b,c), with α²=α+1 | Successful n in {3,5,7,9,13} |
|---|---|
| (1,1,1) | 3,9 |
| (1,1,α) | 9 |
| (1,1,α²) | 9 |
| (1,α,α) | none |
| (1,α,α²) | 7 |
| (1,α²,α²) | none |
| (α,α,α) | 3,9 |
| (α,α,α²) | 7 |
| (α,α²,α²) | 7 |
| (α²,α²,α²) | 3,9 |

The JSON includes the degrees and coefficient masks of every
residual gcd, and the degree of each computed minor.
The subsequent scripts were run by exact imports of the same
criterion; outputs are code/A_theta_F4_gap_scan.json and
code/A_theta_F4_gap_scan2.json. They find, for (1,α,α),
no theta torsion killed by

11,17,19,23,25,27,29,31,21,33,35,37,39,41,43,47,49,

while n=15 and45 both have residual polynomial t⁴+t+α.
These are bounded exact calculations. They do not assert
absence at all prime powers, any universal cutoff, or failure
of A1. The positive n=15 case is independently certified by
an explicit divisor in audit/A_theta_fifteen_candidate.md.

## 4. A short symbolic theta-five exclusion for the remaining example

For a=1,b=c=α, the first four polynomials are

P1=t⁴+t²+α,
P2=t⁸+α²t⁴+αt+α²,
P3=α(t⁴+t²),
P4=t¹⁶+αt¹⁰+αt⁹+αt³+α²t²+α.

At n=5 the rectangular matrix is

[[P2,P1],[P3,P2],[P4,P3]].

Its first maximal minor equals

P2²+P1P3=(t⁴+t+α)^4.

Any common zero therefore satisfies f=t⁴+t+α=0.
Modulo f, with D=t²+t, the four polynomials become

(P1,P2,P3,P4)=(D,D+1,αD+α²,αD+1).

The other minor is then

P2P3+P1P4=α²≠0.

Thus the curve has no theta-five point, with no untested field
extension or numerical enumeration. The universal identities
are checked in code/A_theta_fifteen_certificate.py and independently
in code/A_theta_fifteen_root_independent.py.

