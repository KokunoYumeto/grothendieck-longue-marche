# D48: the entire integral affine return tower

## Result and exact scope

`sections/D_return_tower_agent.tex` proves the full integral version of
the D46 affine return cover. It retains the whole previous quotient
Gamma=B/O^p(O^ell F), its prescribed automorphism, its literal normalized
conjugator, and any prescribed old peripheral conjugators.

For distinct primes ell,p at least 5, let a=ord_p(ell) and let
O=Z_ell[zeta_p] be the unramified degree-a integer ring with the chosen
residue root. The actual source is induced from
H_infinity=O^ell semidirect (C_p^ell semidirect C_ell), with
x=(e0,c) and y=(0,n0), through the same six B/F cosets.
Its actual kernel over the finite D46 base D is W=O^(6ell).
The actual joint source with Gamma is Gamma x_D E_infinity.
It is a quotient of the full return cover B/O^ell(O^p(O^ell F)); the proof
does not identify it with that entire return completion.

The normalized fibre above the fixed whole old map is an O^ell torsor.
Its reduction at precision n is exactly an (O/ell^n)^ell torsor, and every
finite normalized map extends to the entire compatible tower. The full
ordinary centralizer union, source generation, normal-core preservation,
and actual automorphism factorization are all retained. Literal profinite
word fibres are separately the cosets of the actual source kernel on F'.

## Integral proof points

1. The primitive p-th root is lifted as an actual root of T^p-1; its
   derivative is a unit. A nontrivial zeta_p^b-1 remains a unit.
2. The same kernel words which form a mod-ell basis in D46 have a unit
   determinant over Z_ell. Their continuous powers therefore span the
   entire actual closed kernel O^(6ell). This proves the exact source
   quotient at every precision, not only an abstract module description.
3. For the cyclic shift C, im(1-C)=ker(sum) and ker(1-C) is the constant
   vector module over every coefficient ring. No division by ell occurs.
   The Y and Z equations are solved using zeta_p-1 and
   1-zeta_p^(-1), both units.
4. The complete base centralizer projections remain onto. Their kernel
   modules are free over O of ranks 3ell,2ell,ell; reduction on the
   invariant modules is onto at every precision.
5. The peripheral product map has an integral right inverse because
   its reduction has a unit full-rank minor. The full finite fibre has
   |W_n| maps. They all generate: the prescribed tau power gives a
   primitive vector in the kernel, its orbit spans the simple reduction,
   and Nakayama gives the whole kernel.
6. Pure H rigidity uses only the integral difference equations and unit
   scalars. It proves preservation of the actual six-coset normal core,
   so all normalized generating maps factor through automorphisms of
   the same E_n, including infinity.
7. The compact old-kernel image maps onto W modulo ell and hence onto W
   integrally. Therefore the actual joint image is Gamma x_D E_infinity.
   The component automorphisms retain the old map exactly.
8. Every normalized map is Inn(w) sigma_0 with w in W^tau=O^ell. The actual
   conjugator is (sws) f_0 w^(-1). Reduction gives the entire finite fibre,
   and compatible maps give exactly one integral parameter. The full
   profinite-word preimage is a coset of ker(F' -> J_infinity,F').

## Stable numerical certificates

The program is `code/bc_return_prime_integral.py`. It depends on the
unchanged D46 model, its saved kernel-word bases, and its complete base
centralizer generators. The two executed pairs have a=p-1, so the actual
integral ring is literally (Z/ell^n)[T]/Phi_p(T). The code does not reuse
a residue-field root matrix as an integral root.

| ell | p | n | modulus | dim W over Z/ell^n | fixed ranks s/r/tau | upper tau order | runtime |
|---:|---:|---:|---:|---:|---|---:|---:|
| 5 | 7 | 2 | 25 | 180 | 90/60/30 | 1750 | 12.141s |
| 5 | 7 | 3 | 125 | 180 | 90/60/30 | 8750 | 10.067s |
| 7 | 5 | 2 | 49 | 168 | 84/56/28 | 3430 | 11.037s |
| 7 | 5 | 3 | 343 | 168 | 84/56/28 | 24010 | 11.462s |

All four runs report `PASS_EXACT_INTEGRAL_RETURN_LAYER`.
Each run replays every saved actual kernel basis word, proves its vector
matrix invertible over the stated ring, constructs an exact right inverse
for the peripheral product map, and checks every remaining centralizer
equation row. It then lifts a complete generating set of each base
centralizer and records each correction in the literal kernel-word basis.
All three centralizer projection indices are 1 in every run.

The output prefix is `bc_return_prime_l{ell}_p{p}_m{n}`, with `.out`,
`.json`, and `.npz`. A minimal replay first supplies the D46 files, then
runs the integral program four times with the parameters in the table.
The four original D46 case outputs and all frozen E51 files remain
unchanged.

## Additional root E52 audit completed during this work

`bc_symplectic_integral_residual_audit.py/.out/.json` gives an isolated
replay of the fixed root residual certificate and checks 20 additional
K2 conjugation identities. All mathematical JSON values matched; the
row-action antihomomorphism, parity coordinates 10/26, rank-three radical,
Smith invariants (1,1,1) and (1,1,4), and determinant 1/6 passed.

`bc_symplectic_integral_source_comparison.py/.out/.json` reconstructs the
induced s/r permutations directly from the integral matrices and exact
endpoint Schreier words. Both frozen finite sources agree literally:
29,952 entries at p=5 and 115,200 entries at p=7 for each generator.
The section gauge is the identity. The independent full proof read of
E52 also passed, including the compact two-parameter residual fibre.
