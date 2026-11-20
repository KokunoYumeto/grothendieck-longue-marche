# Scan006 — exact coefficient computations

The computation uses the explicit ring morphism from the commutative rational-coefficient Laurent polynomial ring Q[P,Q,Q^{-1},x,y] into
Q[P0,P1,P2,Q0,Q0^{-1},Q1,Q2,x0,x1,x2,y0,y1,y2,epsilon]/(epsilon^3), defined on its generators by:

- P maps to P0 + P1 epsilon + P2 epsilon^2/2.
- Q maps to Q0 + Q1 epsilon + Q2 epsilon^2/2.
- Q^{-1} maps to Q0^{-1} - Q1 Q0^{-2} epsilon + (Q1^2 Q0^{-3} - Q2 Q0^{-2}/2) epsilon^2.
- x maps to x0 + x1 epsilon + x2 epsilon^2/2.
- y maps to y0 + y1 epsilon + y2 epsilon^2/2.

The recorded inverse-product coefficients verify the defining relation Q Q^{-1}=1 in the target. These generator images extend by addition and multiplication; the checked relation proves that the displayed assignment is a well-defined ring morphism. The three remaining computations extract its first and second coefficients and compare them with the displayed candidate derivative expressions. All residuals are expanded exact Laurent-polynomial coefficients; denominators are cleared by the displayed Q0 powers. This specifies the algebraic map used in the checks.

These computations do not determine whether any handwritten exponent is 2 or a double prime, whether a cancelled sign is plus or minus, or which factor order the pen writes. Those are separate ink decisions. No formula on the manuscript is rewritten by this calculation.


Executed: 2026-11-20 10:27:09 UTC

## 006-jet-inverse

The image assigned to Q inverse multiplies the image of Q to 1 modulo epsilon^3.

Residual coefficients: `[0, 0, 0]`.

## 006-first-quotient

The epsilon coefficient of the image of P/Q agrees with (P1*Q0-Q1*P0)/Q0^2.

Residual coefficients: `[0]`.

## 006-second-quotient

Twice the epsilon^2 coefficient of the image of P/Q agrees with (P2*Q0^2-Q2*P0*Q0-2*P1*Q0*Q1+2*P0*Q1^2)/Q0^3.

Residual coefficients: `[0]`.

## 006-second-product

Twice the epsilon^2 coefficient of the image of x*y agrees with x2*y0+2*x1*y1+x0*y2.

Residual coefficients: `[0]`.

## 006-factor-correspondences — manual monomial comparison

Recorded: 2026-11-20 11:07:08 UTC. The inclusion of R0 = Q[P0,P1,Q0,Q0^{-1},Q1] into the coefficient ring used above fixes each named generator. Its defining inverse relation is the same Q0 Q0^{-1}=1. Represent a Laurent monomial by (coefficient, exponent of P0, exponent of P1, exponent of Q0, exponent of Q1); multiplication multiplies coefficients and adds each exponent.

The products Q1 P0 and P0 Q1 both give (1,1,0,0,1). The products 2(P1 Q1)Q0^{-2} and (2P1)(Q1 Q0^{-2}) both give (2,0,1,-2,1). This is the explicit correspondence for the factor order and shared-numerator placement considered at 006-01 and 006-61. It records a manual use and recheck of multiplication in the already specified coefficient ring, without claiming a further run of the coefficient-check script. The transcription keeps the physical factor order and fraction placement.
