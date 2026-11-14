# Literal theta distribution on the actual principal cusp lattice

This is a further integral comparison in the E120 marking.  The
norms are function-field norms for the actual endomorphism [pi],
pi=1+3zeta3.  The operator which appears on proper cohomology is
retained with its Smith factors 3,9; it is not cancelled.

## Exact function identity

Write theta=theta_pi from theta_pi_moments.md, so

    div(theta)=7[O]-sum_(T in E[pi])[T],
    theta=3D(x+y)^3/((x+y)^3+pi*z^3), D=1+2zeta3.

It is an even function.  In the original parameter s=z/x at O,

    theta=(-D/(9pi)) s^6+terms of higher order.

Let f be any of the eight normalized cusp functions in
a_cusp_unit_symbols.json, and write div(f)=sum_t r_t[t].  The actual
divisor of the product of translated theta functions is

    div(product_t theta(Q-t)^r_t)
        =7 div(f)-[pi]^* [pi]_* div(f).

It is therefore the divisor of f(Q)^7/(Norm_pi f)([pi]Q).  To determine
the constant, use the full tame product of {theta,f}.  At O it is
(-D/(9pi))^r_O because the leading coefficient of f is one and
6r_O is even.  At a nonzero cusp t it is theta(t)^r_t.  At each
nonzero point T of E[pi] it is f(T), because theta has order -1.
All other tame values are one.  Weil reciprocity gives

    (-D/(9pi))^r_O product_(t neq O) theta(t)^r_t
                      product_(T neq O in E[pi]) f(T)=1.         (D1)

The leading coefficient of (Norm_pi f)([pi]Q) at Q=O is the product
of f(T) over the six nonzero pi-kernel points.  Comparing the leading
terms and using theta(-t)=theta(t), (D1) proves the literal identity

    product_t theta(Q-t)^r_t
             = f(Q)^7 / (Norm_pi f)([pi]Q).                      (D2)

The scalar is one, rather than an unnamed constant.  This proof uses
the actual divisor, local tangent and norm conventions; it introduces
no analytic branch or rational regulator identification.

Since pi fixes every point of E[3], the divisor of Norm_pi f equals
div(f).  The complete scalar is

    Norm_pi f=c_f f,
    c_f=(3D)^r_O product_(t neq O)theta(t)^(-r_t).                 (D3)

Here pi*(-D/(9pi))=-D/9 and its inverse is 3D.  The eight actual
values, in the already retained unit order, are

    729, 1/729, 729, 9 zeta3^2, 9 zeta3^2, 9 zeta3^2, -27, -27.

## Independent finite algebra checks

The program a_theta_principal_distribution.py computes the six-point
products in (D1) without assuming (D1) or (D3).  On
Y^2=X^3-27/4, the pi-kernel has X-polynomial X^3+c with c=-27/pi.
For each literal line A(X)+bY, first take the product over the two
Y signs, A(X)^2-b^2(X^3-27/4).  Its norm from
Q(zeta3)[X]/(X^3+c) is the determinant of its actual three-by-three
multiplication matrix.  The program multiplies those norms with the
retained line powers and the sixth power of the function's scalar.
It verifies all eight complete tame products and all eight constants.

It also evaluates both sides of (D2) at the exact ordinary point
P=(1,v), v^2=-23/4.  Every theta(P-t) uses the actual elliptic addition
formula.  The point [pi]P is computed by the already verified Velu
map and its pi-scaling, and satisfies the exact curve equation.  All
eight function identities hold in the literal degree-four field
Q(zeta3,v).  This finite check complements the divisor-and-constant
proof; it is not being used to infer a rational-function identity
from finitely many samples.

## The literal symbol and cohomology operator

Apply (D2) to g and take its symbol with f.  Bilinearity and the
projection formula for the actual transfer give

    (7 Norm_pi-1){f,g}
       =Norm_pi(sum_t ord_t(g){f,theta(Q-t)})
          +{c_f,c_g}+{f,c_g}+{c_f,g}.                            (D4)

Every constant term is displayed.  For example,
Norm_pi{f,[pi]^*g}={Norm_pi f,g}={c_f f,g}, which fixes the direction
and sign of the last term.  Equation (D4) is an identity in the
actual function-field K2 group.  It therefore applies to the retained
tame-corrected linear combinations, with their explicit constant
corrections carried along.  No unspecified proper lift is introduced.

On the proper coefficient H^*(2), columns in the original Tate basis,
the isogeny pullback and transfer are respectively

    [pi]^*=A_E^T,
    [pi]_* =7 A_E^-T=[[-2,-3],[3,1]].

Their two compositions are 7I.  Consequently the exact coefficient
operator on the left of (D4) is

    7[pi]_* -I=49A_E^-T-I=[[-15,-21],[21,6]],
    inverse=(1/117)[[2,7],[-7,-5]].                             (D5)

It has local Smith factors 3,9.  It is also precisely the action of
the marked norm-seven tau minus the identity on this proper
coefficient.  The code saves the complete Smith transformation maps
and inverse pairs.  The comparison respects the actual elliptic
filling and the Q/K twist through the matrices already recorded in
elliptic_tor_symbol.md.

Thus (D4) gives an exact bridge from the principal-cusp symbols to
translated theta symbols, including every norm constant.  To obtain
the unknown intrinsic handle coefficient from it, the latter symbols'
proper class must still be evaluated through the integral logarithm
torsor.  Their replacement by the rational first-moment projection
would omit (D5)'s three-primary cokernel.  The explicit Tor symbol
already retained supplies a generator of the surviving C3 term, but
the coefficient in the actual action has not been determined by (D4).

The first program execution stopped at a QZ reflected-division
coercion before any mathematical identity was tested.  Its source
and output are retained in
history/a_theta_principal_distribution_field_coercion.*.  The final
program uses explicit QZ and quadratic-field embeddings throughout.
