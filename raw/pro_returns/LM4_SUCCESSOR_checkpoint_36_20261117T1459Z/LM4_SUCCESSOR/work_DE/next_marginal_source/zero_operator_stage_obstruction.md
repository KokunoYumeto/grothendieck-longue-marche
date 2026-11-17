# The zero-base direction cannot satisfy the present product-one stage criterion

This is an obstruction to a sufficient proof mechanism, not to the actual
whole-source kernel equality.

On Y and on both actual filled surfaces Y_c and Y_b, the rational map

\[
\rho(v,w)=\frac{w(v-1)}{1-w}
\]

has values in `C\{0,1}`. Indeed zero is excluded by `w!=0` and `v!=1`,
the denominator is nonzero, and

\[
\rho-1=\frac{vw-1}{1-w}
\]

does not vanish. On the actual source `v=2-w`, the map is literally
`rho=w`. Its based map on source groups is thus the actual w projection
followed by filling all source punctures except0 and1.

The literal product-one generator b maps to the inverse peripheral
generator at1, with the same source whisker. In the local coordinates
`t=w-1`, `q=(vw-1)/(w-1)^2`, one has `rho-1=-t q`. Fixing the actual
corner t and making the positive q-loop therefore makes a positive
rho-loop about1. The already certified inverse-conjugator convention
identifies that positive loop with `b^-1`.

Suppose an actual source element h satisfies

\[
hbh^{-1}=k b k^{-1},\qquad k\in J_c
\]

(or even `k in R_c`, or in the both-family ambient kernel). Since rho
factors through the corresponding filling, its image kills k. Hence
`rho_*(h)` commutes with the nontrivial peripheral `rho_*(b)` in F2.
The centralizer of a free-basis peripheral in the discrete free group is
its cyclic subgroup. Consequently

\[
\rho_*(h)\in\langle\hbox{peripheral at1}\rangle.
\]

In particular h has zero winding around w=0 on the actual source. A
source correction that retains nonzero zero-base winding cannot satisfy
the strong stage hypothesis, regardless of which previously controlled
deleted-kernel subgroup is used for k. The five corrected positive
operators satisfy this restriction; the missing zero operator does not.

There is an elementary completed version of the winding obstruction.
For each integer m>=2, map F2 to the upper-unitriangular Heisenberg group
over Z/m by sending the 0-peripheral to `(1,0,0)` and the 1-peripheral to
`(0,1,0)`, with multiplication

\[
(x,y,z)(x',y',z')=(x+x',y+y',z+z'+xy').
\]

Commuting with the 1-peripheral forces x=0 modulo m. Thus a source element
of the actual completion satisfying the same conjugacy equation has
zero w=0 winding in Zhat. This uses only genuine finite quotients of the
specified twice-punctured plane, not an assumed full topology on an
abstract source image.

This result does NOT show that b fails to normalize J_c or I. A source
operator may preserve those whole kernels while sending b to a different
retained direction. It shows that the particular induction in B.83 and
the all-positive extension, which requires every source operator to send
b to a conjugate by an element of the controlled kernel, cannot by itself
cover the entire source operator family. A genuinely coupled retained-
direction argument or a different geometric comparison is still needed.

Exact symbolic witness: `check_zero_operator_heisenberg.py/.out` and
`zero_operator_heisenberg.json` verify both commutator signs over
Z[x,y,z], hence the statement for every finite modulus.
