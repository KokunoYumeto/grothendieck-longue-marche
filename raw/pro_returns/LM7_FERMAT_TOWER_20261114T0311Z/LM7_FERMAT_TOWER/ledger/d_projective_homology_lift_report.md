# D.50 — complete two-adic homology extension

## Proved result and exact source

The actual D.49 action extends across its entire remaining two-adic homology kernel over the actual group \(G_3\), whose order is \(576\cdot3^{97}\). The proof uses the same actual arithmetic element \(h\), its parameter \(f_h\), and its nonzero normal elementary three-subgroup \(A\). It does not substitute a finite guess for that parameter.

For \(K_3=\ker(\widehat B\to G_3)\), put \(U=K_3^{\mathrm{ab},(2)}\) and \(U^-=(1-e_A)U\). Its rank is
\[
 w=\frac{|G_3|}{6}\left(1-\frac1{|A|}\right)\ge |G_3|/9>0.
\]
The exact image of the old full-source kernel in the complete two-adic homology extension is \(U^-\). The exact common marked quotient is consequently \(\mathcal J_\infty/U^-\), and the new actual source is
\[
 \widehat B/(\mathfrak R_h\cap\mathfrak K_\infty)
 =\mathcal W_h\times_{\mathcal J_\infty/U^-}\mathcal J_\infty.
\]
Its projection onto the complete D.49 source has kernel \(U^-\). Both projection kernels and the full kernel from \(\widehat B\) are recorded in (D.50.5). Every previously retained action, normalized parameter and comparison is preserved through this literal projection.

## Initial repair includes generation

The first cusp correction is onto because the moving module has zero \(G_3\)-coinvariants. This first step gives a peripheral endomorphism; generation is then proved by a separate explicit repair.

The proof specifies both vertex-module bijections and the complete edge chain map in the actual Bass–Serre graph. The displayed path identity verifies that its restriction is the actual homology action, including the basepoint transport. The nilpotent Fitting part of the edge map lies in the moving cycle module and is a direct summand of the regular group module. It is therefore projective.

The regular-module projection composed with the path cocycle is an explicit derivation. The full inflation–restriction comparison is included; the proof does not leave the needed class unspecified. The exact cusp order is 36. The fixed cusp cycle has zero projection onto the nilpotent Fitting part, so the derivation's cusp value has zero cyclic norm. Projectivity after restriction to the cusp cyclic group gives an actual solution of the norm equation without division by 36. The resulting inner-derivation correction preserves the exact cusp and changes the two conjugators by specified elements of the moving kernel.

On homology the repaired map is \(T+e\): it is \(T\) on the invertible part and \(1+T\) on the nilpotent part. This proves generation and hence an automorphism at the first level.

## Exact higher common quotients and inverse limit

At level \(2^k\), the already retained joint source has common marked quotient
\[
 \mathcal J_k/(2^{k-1}W_k)
 =\mathcal J_{k-1}\times_{\mathcal J_{k-1}/W_{k-1}}
                    (\mathcal J_k/W_k).
\]
This follows from the original source kernels and their preimages; no unsupported interchange of images and intersections is used.

The lower and D.49 conjugators agree as elements in the common quotient. They lift simultaneously, and a correction in \(2^{k-1}W_k\) kills the exact cusp error. The unchanged invertible reduction modulo two proves generation by the determinant criterion over \(\mathbb Z/2^k\). Thus the actual conjugators, automorphisms and inverses form compatible systems. Their inverse limit proves the claimed complete two-adic lift.

The retained source contains the full loop abelianization and has kernel inside \(\widehat F''\). Consequently the new parameter has an actual \(\widehat F'\) preimage, and the full parameter and CM normalization descend exactly to D.49.

## Explicit next remaining finite kernel

The full-source kernel is still nonzero. The next finite quotient is the actual class-two exponent-four quotient of \(K_3\), with abelianization \((\mathbb Z/4)^\rho\) and commutator module \(\bigwedge^2_{\mathbb F_2}(U/2U)\). Actual preimages \(z_i\in\mathfrak R_h\) of a basis of \(U^-\), and \(x_j\in K_3\) of a basis of \(U\), give
\[
 [z_i,x_j]\in\mathfrak R_h\cap\mathfrak K_\infty
 \quad\longmapsto\quad \bar u_i\wedge\bar v_j .
\]
The resulting image contains \(W_1\wedge V\), of dimension
\[
 w(\rho-w)+\binom w2>0.
\]
This is an explicit inclusion with actual source elements. The theorem does not claim equality with the whole remaining image or a lift through this next quotient. Full profinite GT0 realization remains unresolved.

## Independent runnable finite verification

The program code/d_cm_projective_repair.py uses only Python's standard library and has no input files. Run it from any directory; its JSON is written beside the program. Its marked base is the actual product \(A_5\times(S_3\times C_3)\), of order 1080. This is a separate finite verification of the repair and induction, not an asserted evaluation of the enormous arithmetic \(G_3\).

The complete graph has 181 cycles and moving rank 120. The first fixed-seed endomorphism has rank 141 and a projective nilpotent Fitting part of dimension 48. The program builds and verifies its regular-module retraction, all 181 actual cycle maps, equivariance and idempotence. The repaired rank is 181. A faithful edge-cocycle group calculation checks both torsion relations and the exact cusp identity before and after repair. The repaired action is nonidentity.

The program then uses the actual integral averaging idempotent, with 3 inverted modulo 16, and lifts the same conjugators through exponents 2, 4, 8 and 16. Every torsion and cusp identity, unchanged parity and moving-summand membership is checked.

Author validation: a fresh copied-source execution passed; the complete JSON equals the original after excluding only /summary/elapsed_seconds. Display, control-character and environment lint passed. Parent independent audit is pending. The proof contains the symbolic argument for the actual arithmetic \(G_3\), including its nontrivial base conjugator coordinates.

## Independent root verification

Root and bc_fermat independently read the entire proof and source and reran exact copies. All mathematical fields of the full JSON and stdout agree; only the elapsed-time field is excluded. Both audits checked the actual regular-edge map, Fitting projection and projectivity, full cyclic correction, all higher common quotient kernels, generation, compatible conjugators, and the precise nonzero residual inclusion. No correction was required.
