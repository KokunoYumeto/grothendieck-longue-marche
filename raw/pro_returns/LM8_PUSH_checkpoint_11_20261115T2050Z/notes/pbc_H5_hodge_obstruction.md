# H5 differential calculation and the balanced-determinant obstruction

Independent calculation requested by the geometry agent; 2026-11-15. This note is not an included or registered theorem. The differential calculation is intrinsic to the stated curve. Its consequence for the labels `A2,B8` is conditional only on the proposed, separately checked isogeny decomposition.

Let `E: y²=x³−x`, let `O` be its origin, and let `C` be the smooth normalization of

\[
z^5=\psi_5(x).
\]

The fifth division polynomial has divisor

\[
\operatorname{div}(\psi_5)=\sum_{P\in E[5]\setminus\{O\}}P-24O.
\]

Thus the degree-five cyclic cover is totally ramified at the 24 nonzero five-torsion points and at `O`, and nowhere else. Riemann–Hurwitz gives genus 51. Write `omega=dx/(2y)` and let the central generator act as `z -> zeta_5 z`.

## Exact eigendifferentials

For `j=1,2,3,4`, a differential in central character `zeta_5^(-j)` has the form

\[
h\,\omega/z^j,\qquad h\in\mathbb C(E).
\]

At each finite branch point, the orders of the pulled-back `omega` and of `z` are 4 and 1. Holomorphy therefore requires

\[
5\operatorname{ord}_P(h)+4-j\ge0,
\]

which is equivalent to `h` being regular there. It must also be regular at every other finite point. At the point above `O`, `omega` has order 4 and `z` has order −24. Thus the allowable pole order of `h` at `O` is

\[
\left\lfloor\frac{24j+4}{5}\right\rfloor=5j.
\]

Consequently the eigenspace is exactly

\[
H^0(E,\mathcal O_E(5jO))\,\omega/z^j,
\qquad \dim=5j.
\]

The four nontrivial central-character dimensions are therefore **5,10,15,20**. The central-invariant part is the one-dimensional elliptic differential, giving total genus 51.

## Necessary obstruction for the proposed B8 factor

Suppose, as in the independently proposed Heisenberg decomposition,

\[
J_C\sim E_i\times B_{10}^{\,5},\qquad
B_{10}\sim A_2\times B_8,
\]

where `F=Q(zeta_5)` acts on `B10`, `A2` has full CM by `F`, and `K=F(i)=Q(zeta_20)` acts on `B8` with rank two on its rational first homology.

The nontrivial Heisenberg simple representation has dimension five over `F`. The four `F`-embedding dimensions of `H^(1,0)(B10)` are therefore **1,2,3,4**, up to their indexing order. The CM factor `A2` contributes either 0 or 1 at each `F` embedding.

If `B8` were balanced `(1,1)` at every `K` embedding, its two embeddings over each fixed `F` embedding would contribute total 2. Then `B10` would have only totals 2 or 3 at every `F` embedding, contrary to its actual totals 1 and 4. Therefore **the rank-two K-Hodge structure of B8 is not balanced at every embedding**. Its K-determinant cannot be a Tate line at every embedding. The balanced-determinant/quaternion argument used for the earlier factor cannot simply be repeated here.

This obstruction does not depend on the signs chosen for the Fourier intertwiner, on assigning the two residual eigenvalues `+i,-i`, or on an exact polarization computation.

## Additional intrinsic order-four counts

The natural order-four automorphism is `tau:(x,y,z) -> (-x,iy,z)`; the division polynomial is even. Since `tau(omega)=i omega`, a basis of `L(dO)` consisting of `x^a` (`2a<=d`) and `yx^b` (`3+2b<=d`) gives the following `tau` eigenvalue multiplicities on the above eigendifferentials:

| j | d=5j | eigenvalue 1 | eigenvalue −1 | eigenvalue i | eigenvalue −i |
|---|---:|---:|---:|---:|---:|
| 1 | 5 | 1 | 1 | 2 | 1 |
| 2 | 10 | 2 | 2 | 3 | 3 |
| 3 | 15 | 3 | 4 | 4 | 4 |
| 4 | 20 | 4 | 5 | 6 | 5 |

For the Fourier normalization with eigenvalue multiplicities `(2,1,1,1)` at `(1,-1,i,-i)` and residual `T` eigenvalues `−1,+i,−i`, this would give residual holomorphic multiplicities

| j | T=−1 (A2) | T=i (B8) | T=−i (B8) |
|---|---:|---:|---:|
| 1 | 0 | 1 | 0 |
| 2 | 0 | 1 | 1 |
| 3 | 1 | 1 | 1 |
| 4 | 1 | 2 | 1 |

The last table is a comparison under that explicit Fourier convention, not a substitute for checking the actual factor projector. The earlier necessary obstruction already follows without it.
