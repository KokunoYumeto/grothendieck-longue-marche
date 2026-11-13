# Class-14 extension of the exceptional-prime Hall calculation

**Proved.** The prescribed, unscaled \(q_7\) has an integral Hall group lift through class **14**, satisfying both genuine group-cycle equations. The complete affine matrix has rational rank **2,066** and nullity **431**. The integer solution was verified against every original matrix equation and every associative-word coefficient of both group products. The numbered statement is **B.14b** in `sections/g_exceptional_14.tex`.

## Exact mathematical reduction

Use the existing integral Lyndon group commutators
\(C_w=[C_u,C_v]=C_uC_vC_u^{-1}C_v^{-1}\), where \(w=uv\) is the standard Lyndon factorization. Let \(Q_w\) be the seven fixed weight-seven coefficients of \(q_7\) recorded in `e_hall_core.py`. The Hall word is ordered first by weight and then lexicographically:

\[
 f=\left(\prod_{|w|=7}C_w^{Q_w}\right)
       \left(\prod_{8\le |w|\le14}C_w^{u_w}\right).
\]

Every one of the 2,497 variables \(u_w\) is retained. No particular class-13 solution is fixed, and none of the earlier homogeneous freedoms is discarded.

Put \(x=1+X\), \(y=1+Y\), and \(z=(xy)^{-1}\) in the integral Magnus algebra truncated after degree 14. For each of the four substitutions
\[
 (x,y),\quad(y,x),\quad(z,x),\quad(y,z),
\]
write \(a_w=C_w-1\), and let \(a_{w,7}\) be its degree-seven part. Each substitution preserves the minimum degree of a Hall commutator.

For a weight-seven factor, every integer exponent, including a negative exponent, satisfies
\[
 C_w^{Q_w}-1
 =Q_wa_w+\binom{Q_w}{2}a_{w,7}^2
       \pmod{\text{degree}>14}.
\]
Consequently, the fixed initial Hall word has deviation
\[
 S+R,\qquad
 S=\sum_{|w|=7}Q_wa_w,
 \quad R=\sum_w\binom{Q_w}{2}a_{w,7}^2
       +\sum_{v<w}Q_vQ_wa_{v,7}a_{w,7}.
\]
All products are in the specified order. The term \(R\) is homogeneous of degree 14.

For an unknown factor of weight at least eight,
\[
 C_w^{u_w}-1=u_wa_w\pmod{\text{degree}>14}.
\]
An interaction between such a factor and the fixed initial word has degree at least \(8+7=15\); an interaction of two unknown factors has degree at least \(8+8=16\). This proves, before any linear solve, that the two actual group-cycle equations through class 14 are **affine linear in all the unknown exponents**. This assertion uses the fixed value of \(q_7\), not a linear approximation to it.

If \(F_i\) denotes the deviation of the fixed initial word in substitution \(i\), and \(L_i\) its degree-seven part, the fixed right sides are computed from
\[
 D_2=F_1+F_0+L_1L_0,
 \qquad
 D_3=F_2+F_3+F_0+L_2L_3+L_2L_0+L_3L_0.
\]
These are exactly the deviations of
\(f(y,x)f(x,y)\) and \(f(z,x)f(y,z)f(x,y)\) when all higher unknowns are zero. The additional quadratic corrections have, respectively, 2,048 and 9,200 nonzero associative-word coefficients. Their contributions must not be omitted.

The resulting equation \(Au=b\) uses all Lyndon-word coefficients in weights seven through fourteen for both cycles. It has 5,030 rows and 2,497 columns. The entire portion in weights at most thirteen, including the right side, was checked coefficient by coefficient against the independent class-13 matrix and agrees exactly.

The exact rank calculation gave 1,776 reversible unit pivots and a residual matrix of size \(2787\times721\), with exact rank 290. Thus the complete rank is \(1776+290=2066\), and its homogeneous solution space has dimension \(2497-2066=431\). A modular row basis for the residual matrix has the same rank as the independent characteristic-zero calculation.

## Why the Lyndon equations suffice

A product of group-like Magnus series is group-like. If such a product is not the identity, its first nonzero homogeneous deviation is primitive for the ordinary tensor coproduct, hence a homogeneous free Lie element over \(\mathbf Q\). The standard Lyndon bracket basis is triangular with leading coefficient one, so its Lyndon-word coefficients detect every nonzero free Lie element. Induction on the first nonzero degree therefore shows that vanishing of every chosen Lyndon coefficient makes the complete group-cycle defect vanish through degree fourteen.

For the rank calculation, the same argument applies to the homogeneous variation with all weight-seven coefficients zero: products of two unknown deviations then start in degree sixteen. Thus the kernel of the chosen Lyndon matrix is exactly the kernel of the full associative-word matrix over \(\mathbf Q\). Its rank is the rank of the complete homogeneous cycle system, not merely a lower bound from a selected subsystem.

## Exact integral elimination and certification

`g_exceptional_reduce14.py` first chooses only coefficients \(+1\) or \(-1\) as elimination pivots. A pivot equation is normalized to
\[
 u_j=b_i-\sum_{k\ne j}a_{ik}u_k.
\]
Substitution into every remaining equation is reversible over \(\mathbf Z\). The solved equations are recorded for exact integer back-substitution. This removes one independent equation and one variable per pivot while preserving all integral solutions in the other variables. Hence the full rational rank is the number of unit pivots plus the exact rank of the residual matrix.

For the residual matrix, a modular row basis is independently certified by an exact characteristic-zero rank calculation. The successful integral solve uses rational minors and exact finite local congruences. On independent residual rows write
\[
 Bv+Ct=y,\qquad v=\beta-St,\quad
 \beta=B^{-1}y,\quad S=B^{-1}C.
\]
If \(p^d\) clears the \(p\)-denominators of \(\beta,S\), the condition that \(v\) be \(p\)-integral for \(t\in\mathbf Z_p^{431}\) is exactly
\[
 p^dSt\equiv p^d\beta\pmod{p^d}.
\]
This is an exact finite criterion, not an approximation with a chosen numerical precision. The solver only inverts unit pivots and divides a trailing system by \(p\) after checking that every right side is divisible too. It verifies the answer against the original congruences and every residual rational equation.

For \(p=2,3\), the required exponent is \(d=1\). The exact rational solutions have prime-unit denominators of respectively 129 and 108 decimal digits. Their greatest common divisor is one. The recorded integer Bezout combination therefore gives an integral residual solution. Integer back-substitution supplies all original Hall coordinates, and every row of the original matrix is checked exactly. The whole local solve and reconstruction took 8.393 seconds.

The final verification regenerated the four substituted Hall words, expanded every associative-word coefficient, included all fixed quadratic terms and ordered cycle products, and verified the two actual group equations. Both defects were exactly zero. An independent check of the fixed powers used repeated multiplication and inverse factors, avoiding the binomial-power formula for this check. This exhibits an actual integral word modulo \(\gamma_{15}\), with the same unscaled \(q_7\), and implies consistency over \(\mathbf Z_p\) for every prime \(p\). The word has 2,079 nonzero Hall coordinates, including its seven fixed weight-seven coordinates; its largest exponent has 242 decimal digits. The independent word verification took 314.456 seconds.

**Scaling caveat.** At class 14, scaling a linear-system right side does not scale the leading \(q_7\) in the original group problem: the fixed square terms scale quadratically. Neither a full-matrix nor a reduced-matrix denominator is to be called a minimum leading multiplier. The computation asks directly whether the unscaled prescribed \(q_7\) admits an integral extension.

## Files

- `code/g_exceptional_14.py`: complete affine matrix construction and independent full group-word verification; also retains the direct full-matrix HNF method as a reproducible fallback.
- `code/g_exceptional_matrix_14.json.gz`: exact complete sparse matrix, right side, ordered quadratic corrections, and fixed defects.
- `code/g_exceptional_reduce14.py`: reversible sparse unit elimination and exact residual rank; use `--rank-only` to avoid the superseded HNF attempt.
- `code/g_exceptional_reduction_14.json.gz`: recorded elimination equations and exact residual system.
- `code/g_exceptional_local14.py`: successful exact finite-congruence local solve and integer reconstruction.
- `code/g_exceptional_local_14.json`: complete integral certificate, every local denominator and Bezout coefficient, all Hall coordinates, and final status `Proved`.
- `code/g_exceptional_14_verify.out`: full independent group-word verification log.
- `sections/B_class14_results.json`, `sections/B_class14_coverage.json`: the statement and task-coverage ledgers for this calculation.

## Retained unsuccessful lattice approaches

The first residual HNF was stopped after the exact local method had already produced the integral certificate. Its log, matrix, and rank remain in `g_exceptional_reduce14.out`, `g_exceptional_reduction_14.json.gz`, and `g_exceptional_lattice_14.json`; the JSON explicitly records that HNF did not finish. A primitive row-content refinement passed every divisibility check but produced only five extra unit pivots, reducing the residual rank from 290 to 285. Its redundant HNF was stopped as well. The files `g_exceptional_primitive14.out`, `g_exceptional_primitive_reduction_14.json.gz`, and `g_exceptional_primitive_lattice_14.json` preserve this attempt and its interrupted status. Neither interrupted HNF is used as an existence certificate.

With python-flint 0.9.0 installed, reproduce the successful calculation from the deliverable root by running:

```sh
python code/g_exceptional_14.py build
python code/g_exceptional_reduce14.py --rank-only
python code/g_exceptional_local14.py
python code/g_exceptional_14.py verify code/g_exceptional_local_14.json
```

No infinite integral lift is claimed from this finite calculation.

The subsequent uniform argument in B.14d independently proves the actual infinite pro-2 and pro-3 symmetry lifts, using all-degree integral cohomology vanishing and convergent group corrections. The finite class-14 certificate remains an independent calculation; it is not used to extrapolate that infinite conclusion. Full profinite assembly remains a distinct issue.
