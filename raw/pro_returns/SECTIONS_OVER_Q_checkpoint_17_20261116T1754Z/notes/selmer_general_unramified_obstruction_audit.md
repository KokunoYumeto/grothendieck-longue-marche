# A.204 source and execution audit

Source: `sections/selmer_general_unramified_obstruction.tex`.

Certificate: `code/selmer_weight_four_inertia_certificate.py`, with retained output/data.

## General actual map

For each fixed class `r` and coefficient prime, keep the integral Hall coordinates of A.65 and set only the highest coordinates to zero to obtain the continuous map `L_r`. Its defect is the actual central-extension obstruction with coefficients `Z_l(r+1)^(b_(r+1))`. The local full point/cusp lift is aligned with the specified lower section by lifting an actual geometric conjugator.

For the three actual cusp meridians, the central correction is the explicit continuous map

`F_(r,c)(u,m)=u c^m u^-1 L_r(p(u c^m u^-1))^-1`.

It vanishes at `m=0` on the entire compact conjugator group. A finite-subcover argument gives uniform smallness as `m -> 0`; this is independent of the local choices of `u`. The global abelian finite quotients force the actual tame exponents `m_q` to tend to zero. Hence the aligned local corrections have inertia values forming a literal `c0` family.

The strict cochain residue telescopes in weight `r+1` to `(q^r-1)z(T)`. The raw global defect therefore has primitive `-z_q(T_q)` in the actual restricted product. The exact localization sequence A.65.8 places the full obstruction in the unramified image, including its continuous derived-limit contribution. A.65.7 gives the stated annihilator `2 |K_(2r)(Z)|`; this does not assert any further even K-group vanishing.

## Weight-four conclusion and verified source pointers

The complete relevant proofs in A.61 and A.65 were reread. Their exact new arithmetic input is already verified in the parent bibliography:

- Charles Weibel, *The K-book*, VI, Theorem 8.2: odd-primary arithmetic étale comparison.
- VI, Theorem 9.11, case `n=6`, and Examples 10.3: the weight-four dyadic kernel under real restriction is the two-primary part of `K_6(Z[1/2])`, which is zero.
- Localization identifies the relevant primary part with `K_6(Z)=0`.

Thus the unramified obstruction vanishes for odd coefficients. At two its restriction to the actual real group is injective. The retained real full point/cusp lift makes that restriction zero, so the dyadic obstruction vanishes too. Taking the product of the continuous coefficient primitives gives an actual class-four section projecting to the specified class-three representative.

The conclusion is global lifting. It does not assert that the new lift has the original local images, nor that the iteration can be repeated without a newly proved local matching condition.

## Executed finite algebra

The degree-four Magnus certificate recomputes the Hall commutators, verifies `[D,y]=[F,x]`, the primitive extraction matrix `diag(1,-1,1)`, and all three cusp conjugation corrections. Each correction vanishes at exponent zero, and `24*correction/m` has integral polynomial coefficients. It also checks 130 exact strict-residue telescoping identities.

All tests pass. These finite computations illustrate and verify the actual fourth-layer maps; the general all-weight uniform limit is the compactness argument in the source, not an inference from finitely many weights or residue samples.
