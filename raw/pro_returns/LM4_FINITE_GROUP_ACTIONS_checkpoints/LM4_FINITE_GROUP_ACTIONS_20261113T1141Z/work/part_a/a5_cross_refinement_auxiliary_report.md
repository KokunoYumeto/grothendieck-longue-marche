# Auxiliary noncentral refinement: exact outcome

The executed nonsplit extension test gives **no additional exclusion** among the 300 D.38 triangle tuples on the selected nine factors. All 150 tuples in the restricted finite conjugacy model and all 150 outside it survive the simultaneous equations. No numbered claim is assigned.

## Exact construction

The base module is the adjoint module `V = sl2(F5)` of `A5 = PSL2(F5)`. The program enumerates all crossed homomorphisms and finds `dim Z1 = 4`, `dim B1 = 3`, and `dim H1 = 1`. It retains all sixty values of a nonzero cocycle `c`, verifies all 3,600 cocycle identities, and checks that the sixty representation matrices span the full 3-by-3 matrix algebra.

For two factors, the cocycle is

`beta((g,h),(u,v)) = c(g) tensor rho(h)c(v)`.

The TeX note proves its cohomology class is nonzero by restricting a proposed coboundary to the two commuting factors. It also proves `H1(A5 x A5, V tensor V) = 0`. No non-splitting claim is inferred solely from finite samples of the cocycle identity.

The simultaneous refinement uses the six ordered pairs

`(3,13), (5,15), (6,8), (7,8), (11,13), (14,15)`

over the support `{3,5,6,7,8,11,13,14,15}`. Thus the base is exactly `A5^9`, the noncentral kernel is the direct sum of six 9-dimensional tensor modules, and the group has order `60^9 * 5^54`. The six nonzero extension components make the kernel Frattini. Consequently every lift of the specified generating pair generates the full extension.

## Simultaneous systems and counts

The first affine system imposes the exact word maps `theta(X)=Y`, `theta(Y)=X`, `omega(X)=Y`, and `omega(Y)=(XY)^-1`. After quotienting by simultaneous inner conjugation by the module, the solution space has dimension 9 over F5.

For each base tuple `t`, the second system imposes

`T^2 = 1`, `T X T^-1 = X^-1`, and `omega(T) = Y^-1 theta(T)`.

Every one of the 300 systems has dimension 6. Its projection to the 9-dimensional family of symmetry-invariant kernels has dimension 3. Therefore each base tuple has exactly 125 compatible kernels and 125 involutions on each kernel, giving 15,625 pairs per tuple and 4,687,500 pairs altogether. Exactly half lie over the base tuples inside the restricted D.38 conjugacy model, and half lie over the base tuples outside it.

Direct group multiplication on one solution for each of the 300 tuples verifies the symmetry word maps, the involution norm, the inversion equation, and both Harbater–Schneps relations. The linear equations and the exact cancellation proof establish these identities on the whole affine solution sets.

## Scope and remaining obstruction

The extension family is a necessary finite test for an actual GT0 involution: its induced action and the geometric S3 act affinely on the 54-dimensional family of epimorphism kernels, and averaging over the group of order 12 in characteristic 5 supplies a common fixed kernel. The note spells out the target automorphism and kernel identifications used in this argument.

The calculation supplies no compatible inverse system of lifts. It also supplies no solution of the full third-cusp conjugator equation in D.35. Its exact negative conclusion is that this particular nonzero cross-factor extension, including simultaneous peripheral and power conditions, does not separate the two surviving D.38 factor patterns.

The full involution problem now returns to the actual three cusp dihedral subgroups and their incidence triangle: the passage from three conjugacy classes to three coherently chosen generating involutions remains to be proved.

## Reproducible files

- `a5_cross_refinement_auxiliary.tex`: proof of the construction, exact systems, and finite conclusion.
- `code/a5_cross_module.py`: explicit module, cocycle, and nonsplit cross-factor data.
- `code/a5_cross_module_output.json` and `_stdout.txt`: executed data.
- `code/a5_cross_peripheral_lifts.py`: simultaneous symmetry and involution systems.
- `code/a5_cross_peripheral_lifts_output.json` and `_stdout.txt`: all 300 rows and exact dimensions.

The second program reads the first program's JSON output and uses the existing D.38 and D.45 group implementations in the same code directory. Arithmetic is exact over F5; no floating point calculation is used.
