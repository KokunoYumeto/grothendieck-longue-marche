# Independent review of S03–S05

**Outcome:** no substantive mathematical error found in S03–S05 after the period/solution-versus-de-Rham convention was clarified. The independent exact checks pass. Neither the source notes nor any frozen transcription was edited by this reviewer.

## S03: exact differential and Schwarzian

The sign in the exact differential is correct. For $q=x(x-1)(x-u)$ and $\omega=dx/y$, $y^2=q$, differentiation at fixed $x$ gives $\partial_u\omega=\omega/[2(x-u)]$ and $\partial_u^2\omega=3\omega/[4(x-u)^2]$. The independent rational calculation confirms the positive right-hand side $d_x(R/y)$ with $R=x(x-1)/(2(x-u))$.

For $f''+Pf'+Qf=0$, the substitution $f=e^{-\frac12\int P\,du}v$ gives projective potential $Q-P'/2-P^2/4$. Thus a ratio of independent solutions has Schwarzian $2Q-P'-P^2/2$, equal here to $(u^2-u+1)/(2u^2(u-1)^2)$. This is local away from $u=0,1,\infty$, with a chosen holomorphic ratio chart; it is a modern comparison and does not identify a connection in the manuscript.

## S05: the two connection conventions

The newly added convention is correct. In the de Rham basis $(\omega,\eta=x\omega)$, write $\nabla e=eG$ with row basis $e$ and coefficient columns; an independent exact-form reduction gives

$$
G=
\begin{pmatrix}
-\frac1{2(u-1)}&-\frac1{2(u-1)}\\
\frac1{2u(u-1)}&\frac1{2(u-1)}
\end{pmatrix}.
$$

Changing to $(\omega,\nabla_\partial\omega)$ uses

$$
H=
\begin{pmatrix}
1&-\frac1{2(u-1)}\\
0&\frac1{2u(u-1)}
\end{pmatrix},
\qquad H^{-1}(GH+H')=A^T.
$$

The determinant is a unit on the smooth Legendre base with two inverted, including characteristic three. Therefore the coefficient-column de Rham connection is $\partial+A^T$, and its dual period/solution connection is $\partial-A$. Their p-curvatures satisfy $\psi_{\mathrm{dR}}=-\psi_{\mathrm{solution}}^T$ in these dual bases. The original displayed matrix is correctly retained for the solution connection.

## S05: independent characteristic-three calculation

The recurrence $B_{n+1}=B_n'-AB_n$ computes $(\partial-A)^n$ on constant basis columns. Since $\partial^3$ is a derivation in characteristic three and annihilates the generator $u$, it vanishes on $\mathbb F_3(u)$, so $B_3$ is the p-curvature matrix.

Independently expanding the differential operator gives the characteristic-three matrix

$$
-A''+A'A+2AA'-A^3,
$$

which agrees exactly with the matrix in S05. Its lower-left entry is the unit $-1/[u^2(u-1)^2]$, and its square is zero. At $u=-1$ the companion and de Rham matrices are respectively

$$
\begin{pmatrix}0&0\\-1&0\end{pmatrix},
\qquad
\begin{pmatrix}0&1\\0&0\end{pmatrix}.
$$

The coefficient of $x^2$ in $q$ is $-(1+u)$, so the stated Hasse-polynomial normalization is correct. The companion has the nonvanishing horizontal vector $(u+1,1)^T$, including at $u=-1$; vanishing of its first coordinate does not force the p-curvature tensor to vanish.

**Interpretive limitation:** specialization here means the value of the base-connection p-curvature tensor at the supersingular parameter and its tangent direction. It is not the p-curvature of a Gauss–Manin connection over an isolated point $\operatorname{Spec}\mathbb F_3$, nor of a separately introduced connection on the individual elliptic curve.

## S04 and source boundary

This reviewer carried the general Katz nilpotence and Cartier-descent theorems as published background already checked by the root/author; the general proofs and their hypotheses chain were not independently audited again. The rank-two companion computation independently illustrates nonzero square-zero p-curvature, but does not prove the general Gauss–Manin theorem or identify the historical S20 connection.

The original C1–C2 formulas were checked independently, not merely by accepting their assertions. The companion-to-de-Rham gauge calculation and the closed third-power expansion use a separate certificate, *connections_review_certificate.py*, whose complete successful output is in *connections_review_output.txt*. Explicit finite-field coefficient reduction is used after specialization: SymPy's cancel(constant, modulus=3) by itself leaves integer constants unreduced, so raw integer specialization without that final reduction would be misleading. This is a computation-convention limitation, not a mathematical error in S05.

Actual review events are in *connections_review_events.tsv*.
