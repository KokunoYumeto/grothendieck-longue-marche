# E.85 — compatible joint sections and the full intrinsic central fibre

The E80 family now has a complete intrinsic existence criterion: it has an actual intrinsic class-two preimage exactly when `N+M=2 mod3`. The incompatible direction is E83. The new positive direction starts with a full intrinsic cusp section, constructs its actual joint normalization, and uses a literal Hall right inverse for the central coefficient map.

## An actual origin

A fixed pro-three path to the rational cusp B0 is adjusted by a fixed lift of an explicitly displayed joint conjugator. Its full inertia image is exactly `(y,y)`. The cusp norm identity then forces the horizontal class-two constants to be `(N,M)=(2,3)` after left multiplication by the specified cusp power. The unknown third-degree path coordinates remain symbolic throughout; none is assigned a numerical value.

For a compatible pair, write `n=N-2`, `m=M-3` and `ell=(n+m)/3`. The literal Hall vector

`(2 ell-n)[f2,f1] - ell[B0,f1]`

maps to `(n,m)`. Right multiplication of the full cusp horizontal value by this central vector therefore gives the required intrinsic class-two section. The complete target conjugacy relation is `(N,M)->(N-48b,M-48b)`. Its compatible classes are parametrized by `t=N-M+1`, with inverse `(2+t/2,3-t/2)` and the actual normalizing conjugator `b=(N+M-5)/96`.

## The whole fibre over the intrinsic abelian origin

The result computes more than the original forty-five-parameter cusp slice. Let alpha0 be the actual intrinsic abelian section just constructed. Its entire class-two fibre is

`P x K2 = (Z3^24 x C3^9 x C9^5) x Z3^22`.

The actual representative is `(u0 w_z, d w_a)`, where `a` lies in the exact saturated kernel of `(1-J2)(T2-7)`. The full gauge changes only `z`, by `(1-T2)b` for `b` fixed by `J2`. The absence of any abelian stabilizer makes this the complete geometric-conjugacy fibre over alpha0.

The target central fibre has coordinates `(rho,sigma,epsilon)` in `Z3 x Z3 x C3`. These record the horizontal difference, the common relative central coordinate, and the horizontal half-sum modulo three. The actual coefficient map has image

`Z3 x 3Z3 x 0`.

It has index nine and cokernel `C3^2`. Its kernel, and every fibre over this image, is

`Z3^44 x C3^9 x C9^5`.

The two image directions have literal splitting vectors:

`z_* = -[f2,f1]/2`,

`a_* = -[B0,f1] + [B0,f2] - [B0,A1]`.

Their images are `(1/2,-1/2)` and `(3,3)`. The full inverse coordinates are also given in the retained E82 Smith basis and E75 relative-kernel basis. One unit equation solves the first free Smith coordinate; a second solves the eleventh relative coordinate. All fourteen torsion coordinates and forty-four other free coordinates remain independent.

The smaller slice `a=0` has fibres `Z3^23 x C3^9 x C9^5`. The theorem states its actual inclusion into the larger fibre. It does not identify other intrinsic abelian preimages with alpha0.

## Exact computation

The program recomputes all ninety alternating tensor images from the four actual unit characters. It checks the derived image lattice of index three, both arithmetic intertwiners, every full Smith inverse pair, the exact relative-kernel basis and inverse, and both splitting vectors. Four symbolic class-three norm identities retain all unknown central path entries. There are 729 target-family checks and 1,296 exact coordinate inverse checks. All actual outputs are retained, including the full matrices and hashes of every arithmetic input.

The next comparison is the kernel of the first-degree map `H1(Q3,V)->H1(Q3,J1)` and the class-two obstruction on its other abelian preimages. The fixed abelian fibre evaluated here supplies an actual origin and exact central transport for that continuation.

## Independent root verification

Root independently read the entire proof and program, checked every frozen manifest file, and freshly ran a copied program against six copied arithmetic inputs. The complete program, stdout and JSON are byte-identical with no exclusions. The integration adds the explicit global-path/local-source typing through the same based Gamma action, as confirmed by the author. PASS.
