# Separate rank-upper-bound work after A182

The complete decomposition and rank lower bound in A182 remain stable.
No upper bound for the total Jacobian rank has been established.

## Three exact elliptic ranks

The local certificate `code/point3_fermat8_elliptic_rank_certificate.py`
proves rank one for each of the old elliptics

`E_b: y^2=x^3+b x`, for `b=-6,18,-12`.

The actual degree-two isogeny and its scaled dual are

`phi_b(x,y)=(x+b/x, y(1-b/x^2))` to `E_{-4b}`,

`psi_b(x,y)=(x/4-b/x, y(1+4b/x^2)/8)` back to `E_b`.

Their composition is multiplication by two (the duplication formulas
or literal substitution verify it). The connecting homomorphism on
`E_b` is the squareclass of x, with values 1 at O and b at (0,0).
To see the kernel directly, the x-coordinate of `psi_b(Q)` is
`(y(Q)/(2x(Q)))^2`. Conversely, for `P=(s^2,y)` with nonzero s,
the preimage

`x(Q)=2s^2+2y/s`, `y(Q)=2s x(Q)`

is rational and maps to P. Changing the sign of s changes Q by
the kernel point of psi, so the actual Kummer cocycle is the
square-root cocycle of x. The exceptional point (0,0) lifts exactly
when b is a square, by the two points with x=±2 sqrt(b).

For every prime not dividing b, an odd nonzero valuation of x
contradicts `y^2=x(x^2+b)`: for positive valuation the other factor
is a unit, and for negative valuation the total valuation is three
times that of x. Therefore the connecting squareclasses here are
among `±1,±2,±3,±6`. A class d has the actual covering equation

`N^2=d U^4+(b/d)V^4`,

obtained by `x=d(U/V)^2`, `y=d U N/V^3`. Local primitive coordinates
have at least one of U,V a dyadic unit. Real signs and the complete
residue enumeration modulo at most32 give the following upper bounds:

| b | connecting-image bound |
|---|---|
| -6 | 1,3,-2,-6 |
| 24 | 1,6 |
| 18 | 1,2,3,6 |
| -72 | 1,-2 |
| -12 | 1,-3,6,-2 |
| 48 | 1,3 |

The points `(3,3),(6,18),(6,12)` together with `(0,0)` generate
all four classes in the three original rows. The dual kernel point
generates both classes in each dual row. Thus every upper bound is
an exact connecting image.

The exact index sequence gives

`|E_b(Q)/2E_b(Q)| = |alpha_b| |alpha_-4b|/2 = 4`.

Here the denominator is two because the dual kernel has two rational
points and its nonidentity point is not in phi(E_b(Q)): its connecting
class is the nontrivial class `-4b`. The original rational two-torsion
has order two. Mordell–Weil therefore makes the rank exactly one.

This gives a certified contribution three from the old elliptic factors.
The complete follow-up A185, saved as
`sections/point3_fermat8_prym_ranks.tex`, now proves exact ranks `1,2,2`
for the three Prym surfaces through actual quadratic Weil-restriction
isogenies. Its local certificate is
`code/point3_fermat8_prym_rank_certificate.py`.
The six computed factors therefore contribute exactly eight. An upper
bound for the six remaining genus-two factors is still needed before
concluding anything about `rank(J8)<21`; upper bounds of two for each
would suffice, but they have not been proved.

## A possible exact next descent field, with no rank conclusion

For `G_{A,B}:y^2=A x^5+B x`, choose `c^4=B/A`. Over Q(c),

`u=x+c^2/x`, `v_+=y(x+c)/x^2`, `v_-=y(x-c)/x^2`

satisfy

`v_±^2=A(u^2-2c^2)(u±2c)`.

These are the two degree-two elliptic quotients for the reciprocal
involution `(x,y) -> (c^2/x,c^3 y/x^3)` and its product with the
hyperelliptic involution. Any rank estimate using these maps must
retain the actual quartic-field Galois action. No rank estimate
from those maps has yet been executed or asserted.
