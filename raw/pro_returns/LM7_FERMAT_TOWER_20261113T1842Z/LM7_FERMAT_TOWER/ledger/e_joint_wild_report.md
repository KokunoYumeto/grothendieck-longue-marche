# E.80 — the conjugate joint cubic quotient over Q3

The actual pair of maps `h=(x+y)/(x+zeta*y)` and its conjugate has an explicitly determined joint geometric image. The proof first fills the three `x=0` cusps and identifies the remaining curve with the connected cubic Kummer cover

`v^3 = h*hbar = -zeta^2*h^2/(h+zeta)`.

This is an exact degree-three étale cover of the four-punctured line; the inverse scheme map is displayed. Its geometric group is the index-three, rank-seven subgroup of a rank-three free pro-three group. The two target maps fill the two different branch punctures. Their common quotient is the `ell=X-Y` character, and the cover imposes the additional congruence `X(f)+X(g) in 3 Z3`. The resulting joint image and every kernel are proved explicitly.

## Actual arithmetic and full conjugacy

The roots used for the second target are the complex conjugates of E.78's actual roots. Their product selects exactly the cubic root `v`, with leading term `s^2/3`. Their ratio and product give both Kummer characters, hence all four actual wild Hall operators. The arithmetic involution is the target swap followed by `x -> x^-1, y -> y^-1` in each factor.

Restriction followed by first projection injects the full Q3 section set into E.78's section set over Q3(zeta3). The image has four exact integral character conditions. A representative with horizontal character sum `H` is normalized by the actual gauge `x^(H/12)`; the remaining gauge is exactly `ker(ell)`. This proves injectivity after the full geometric-conjugacy quotient and gives its continuous inverse. It does not identify conjugacy quotients before performing that normalization.

The abelian section group is `Z3^5 x C3`. Its class-two lifting image is exactly

`L_a*(p_u-1)-L_u*p_a = 0 mod 3`.

Every nonempty class-two fibre has coordinates `Z3^2 x C3`. The class-three image is given by the two evaluated E.78 Hall defects divisible by three; each nonempty fibre has coordinates `Z3^4 x C9^2`. The representative, central correction, residual gauge and coordinate inverse are retained. The displayed two-parameter family has exact error `e^(7*(5-N-M))`, so its class-three fibre is nonempty exactly for `N+M = 2 mod 3`.

## Integral comparison with the intrinsic source

The product truncations and the actual lower central filtration are connected by two explicit finite-kernel maps. The degree-two commutator lattice has Smith list `(1,3)`; the actual degree-three lattice has Smith list `(1,1,3,3)` inside the four-dimensional product-central kernel. Thus the intrinsic third-degree image has index nine. The quotient map is

`(r,s,r',s') -> (r'-r, s+s'-2*r) mod 3`,

and the involution on this quotient is the displayed matrix `[[1,0],[2,-1]]`. An actual determinant-one matrix of four commutator words proves that all four central directions belong to the second commutator subgroup. This supplies the integral group argument and prevents replacing the intrinsic central image by the whole product-central kernel.

The E.80 descended example is proved to be a section of this actual quotient over Q3. Its intrinsic lifting problem is retained through the exact inverse-image kernels. The intrinsic preimage assertion already proved in E.78 over Q3(zeta3) is not imported into the descended family without an additional construction. Root's E.82 separately computes actual intrinsic cusp families.

## Executed certificate

`code/a_joint_wild.py` is self-contained apart from standard Python and SymPy. It uses exact fractions, symbolic identities, integer Smith transformations and a separate finite Hall implementation. Its actual stdout and JSON are retained.

All checks pass:

- Eleven scheme and tangent identities.
- Complete generated finite images at class one modulo 27, class two modulo 9, and class three modulo 3, of orders 6561, 19683, 6561.
- Both integral Smith maps, their inverse matrices, and the determinant-one central commutator basis.
- 1,200 arithmetic action identities.
- 240 actual gauge-normalization and inverse comparisons.
- 62 descended class-two sections and 13 class-three lifts.
- All 36 small members of the explicit descended family, including positive and obstructed cases.

## Sources

The original French SGA 1, Exposé XII, Theorem 5.1 and Corollary 5.2, with the complete relevant proof, was reopened at `https://arxiv.org/pdf/math/0206203`, printed pages 251–254 (PDF pages 266–269, zero indexed). The finite-cover comparison is the only new external input. The fibre-product group proof, exact cyclic-cover character and integral commutator lattices are proved in the section.

The arithmetic coefficient and exact marked-source presentation are the already proved E.54, E.74, E.77 and E.78 results. E.78 retains the actual E.49 change of source marking. All doubtful-reading flags are false; no manuscript decipherment is used to assert the new maps or computations.
