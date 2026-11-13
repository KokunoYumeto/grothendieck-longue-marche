# Exact cyclic-double-cover Kummer sign audit

Date: 2026-11-13. Status: source and coefficient comparison proved; integrated
checkpoint text is unchanged. This note preserves the inherited sentence and
specifies the convention map needed to use it.

## Primary source

Nakamura--Schneps, *On a subgroup of the Grothendieck--Teichmüller group acting
on the tower of profinite Teichmüller modular groups*, author PDF
<https://webusers.imj-prg.fr/~leila.schneps/newGT.pdf>.

At the beginning of §2 the Kummer character is defined using positive roots:
`sigma(2^(1/n)) = zeta_n^rho_2(sigma) 2^(1/n)`.
Equation (2.1) gives `sigma(gamma)=f_sigma(x,y)^(-1) gamma` and hence
`sigma(x)=x^chi`, `sigma(y)=f_sigma^(-1)y^chi f_sigma`.
The paragraph following (2.1) says explicitly that this `f_sigma(x,y)` is
Ihara's `f_sigma(x^(-1),y^(-1))`.

Equation (2.4), author PDF page 9 (PDF index 8), writes
`f_sigma = A_sigma(xbar,ybar) * [x,y]` in the metabelian commutator module.
The commutator is `xyx^(-1)y^(-1)` and `*` is left conjugation.
Lemma 2.3 states exactly

    rho_2(sigma) = -A_sigma(-1,1).

No claim about all-GT matrix characters is used here.

## Literal coefficient morphism

Let `H_2=ker(Fhat -> C_2)`, with x mapping to the generator and y to zero.
Its free generators are `x^2`, `y`, `xyx^(-1)`. The map used in D.5 is

    delta_2(x^2)=x, delta_2(y)=y, delta_2(xyx^(-1))=1.

Let `c_2` be the y-coordinate after this map. On `Fhat'`, it is a continuous
homomorphism to `Zhat`, so kills `Fhat''`. The two boundary coordinates of an
element of `Fhat'` in `H_2^ab` sum to zero. Conjugation by x interchanges those
coordinates, and conjugation by y fixes them. Moreover

    [x,y]=(xyx^(-1))y^(-1),    c_2([x,y])=-1.

Consequently the induced module morphism has x acting by -1 and y by 1:

    c_2(A * [x,y]) = -A(-1,1).

Combining this actual coefficient map with NS Lemma 2.3 proves, in their
specified geometric convention,

    c_2(f_sigma) = rho_2(sigma) = kappa_2(sigma).

This also proves the comparison modulo every integer, in particular modulo 3
for the rank-five Fermat-conic quotient used in the new A6 computation.

## Exact inversion morphism and the inherited sentence

The continuous free-group automorphism `iota(x)=x^(-1)`,
`iota(y)=y^(-1)` preserves `H_2` and satisfies

    delta_2 o iota|H_2 = iota o delta_2.

The identity is checked on the three displayed free generators: the third
maps to `x^(-2)(xyx^(-1))^(-1)x^2`, which delta_2 kills. It follows that
`c_2(iota(f))=-c_2(f)`. Thus the explicitly stated NS--Ihara change of free
generators reverses the coefficient. In the Ihara variables related by this
map, `c_2(f_sigma^Ihara)=-kappa_2(sigma)`.

The inherited D.5 proof currently contains the following sentence:

> The sign convention there is rho_N=-c_N, and on the stated Galois
> normalization it is rho_N=kappa_N. This is an equality of the specified
> coefficients.

For N=2 this is incompatible with using the NS geometric f without the
displayed inversion map. The finite distribution equations and finite literal
`c_N` values do not use that Kummer-sign identification and remain unchanged.
The parent and the A6-source agent were informed; no frozen manuscript file
was edited by this audit.

## Dependency inventory

The following inventory was checked against the integrated TeX and the
literal coefficient/matrix programs. It distinguishes a printed label from
an input used in a computation.

| Result | Exact input used | Effect of the D.5 sentence |
|---|---|---|
| D.5 theorem | Literal `delta_N`, its y-coordinate `c_N`, Enriquez Theorem8.1 and Remark8.6 | Distribution identities do not use a Galois sign. The proof's quoted arithmetic-identification sentence requires the convention correction above. |
| E.6 and earlier distribution tests | Literal tuples `(q delta_N(w),c_N(w))` | No arithmetic sign is used in the finite equations or correction images. |
| E.25 | `bc_distribution_quartic.py` computes y exponents directly in its `delta` routine; all five equations use `c_N` | Its complete coefficient sets, orders, matrices, and word-preimage assertions are unchanged. Its final paragraph attributes the label `rho_N=-c_N` to D.5; this attribution needs correction or an explicit convention label. |
| E.25 quartic labels | The JSON field `admissible_rho3_mod4` is computed as `-b % 4`, and the statement explicitly defines `rho_3=-c_3` | These are negative-coefficient labels. The assertion that every quartic residue occurs, and that both even residues occur after the parity restriction, is invariant under sign. The present N=2 audit does not establish an N=3 geometric Kummer identification. |
| E.26, E.28, E.31, E.33, E.36--E.37, E.41--E.42 | Literal Schreier, Hall, norm, source-kernel, and supported-power maps | No `c_2`/Kummer identification is an input. |
| E.29 | Actual NS Theorem2.5, evaluated at `x=[[1,2],[0,1]]`, `y=[[1,0],[-2,1]]`; positive-root `rho_2` | Independent of D.5. The matrix is `M_k=[[1,-8k],[-8k,1+64k^2]]` for chi=1. The three residue labels and all actual matrix values remain unchanged. |
| E.38 | The same NS Theorem2.5 with its actual sign at chi=1 mod4, and literal signed modular evaluation | Independent of D.5. The three signed matrices `I`, `[[1,4],[4,5]]`, `[[1,8],[8,5]]` modulo12 remain unchanged. |
| E.43 | E.38's signed matrix and actual Galois selection, followed by the prosolvable-residual correction | No cyclic-distribution coefficient is used; no matrix, source map, fibre, or generation comparison changes. |
| E.44 and E.47 | Literal Magnus/Hall lattice calculations; simultaneous GL comparison is inherited from E.43 | No cyclic-distribution sign is used. The symbols `rho_1,rho_2` occurring among E.47's algebraic residue variables are separate polynomial coordinates, not Kummer characters. |
| E.46 | The actual GL-to-Hurwitz source quotient and E.38's arithmetic choice | No D.5 sign input. |
| E.49 | Literal prime-three symplectic source/target arrays and simultaneous conjugators | No Kummer coefficient input. |
| E.50 | Literal source/residual/signed-Q20/common-quotient arrays and the same actual Galois element from E.43 | No D.5 sign input. The exact Q20 bits, theta matrices, common quotient order72000, target arrays and correcting subgroup remain unchanged. |

The specific arithmetic-index programs checked were
`de_ferrari_a5_compare.py` and `de_ferrari_sl2_5_modular.py`.
The former constructs its three Galois values directly from the parameter
`-8*kappa2`; the latter constructs the three displayed `M_k` matrices
directly. Neither reads the distribution program or its `c_2` values.
E.29.13 has index rows 0: `{0,1,2,3,16,17,18,19}`,
1: `{4,5,6,7,20,21,22,23}`, and
2: `{8,9,10,11,12,13,14,15}`. They remain the positive-root Kummer labels of
NS Theorem2.5, without a sign change.

No E50 file or other integrated certificate was changed during this audit.

## Other independent audit completed in this turn

D.43 in `sections/D_inverse_base_agent.tex` was read in full. Its residual
intersection, exact descent kernels, compact inverse system, nested literal
conjugators, whole-source Hopficity, and final two-stage quotient comparison
all pass. The parent and arithmetic agent received this result.
