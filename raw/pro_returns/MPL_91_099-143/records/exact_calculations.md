# Exact calculation checks

Checked 2026-11-15 11:58:12 UTC; exact symbolic arithmetic with SymPy 1.14.0.

These checks concern the explicit examples in the research notes. They do not alter or complete the frozen transcription.

1. RN142-02: quadratic substitution coefficients, degrees 0 through 4: a0**2*a2prime + a0*a1prime + a0prime; 2*a0*a1*a2prime + a1*a1prime; 2*a0*a2*a2prime + a1**2*a2prime + a1prime*a2; 2*a1*a2*a2prime; a2**2*a2prime. PASS.
2. RN135-03: (1+epsilon/t)(1-epsilon/t) reduced modulo epsilon^2 is 1. PASS.
3. RN142-04: (t+epsilon)^3 modulo (epsilon^3,t^3) is 3*epsilon**2*t + 3*epsilon*t**2, a nonzero basis expression. PASS.
4. RN139-03: transpose(X) A + A X = (a+d) A; the three displayed kernel basis matrices vanish under this map and parametrize X with d=-a. PASS.
5. RN139-02: in characteristic 2, the second-coordinate difference is X1**2*Y2 + X2*Y1**2; it is nonzero and has zero image modulo total degree >=3. The first-coordinate difference is zero. PASS.

Direct proof checks recorded in the notes: RN135-02 gives the equality-stage map and its identical inverse; RN142-03 uses the coefficient equation 2 h_1 = 1 in Z. No floating-point or statistical calculation is used.
