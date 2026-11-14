# E.74 independent final proof and execution audit

Auditor: `/root/a_structure`. Outcome: **PASS**, with no correction required.

I read the entire actual statement and proof in `research_e74/sections/E_wild_local_layers.tex`. The earlier detailed source and splitting audit is retained in `research_e74/ledger/a_e74_audit.md`. This final audit additionally checks the written integral duality, the degree-two free coordinate, all retained finite-precision maps, and the topological central-fiber assertion.

## Source and cohomological maps

I opened the full author originals of Wingberg, *Free quotients of Demushkin groups with operators*, https://www.mathi.uni-heidelberg.de/~wingberg/agwingberg/paperwingberg/FQD.pdf, and Milne, *Arithmetic Duality Theorems*, https://www.jmilne.org/math/Books/ADTnot.pdf. I read Wingberg's introduction on the actual cyclotomic local/global quotient and Section 3; in this version the orientation factorization is Proposition 3.3, while Lemma 3.2 supplies the Bockstein orthogonality. I read Milne I.2.1, I.2.3 and I.2.8, with their surrounding hypotheses and proofs. The theorem's actual citations and page anchors agree with those sources.

The maximal-pro-three comparison is proved first for the trivial finite module using the five-term injection and the two one-dimensional degree-two groups. Finite-module devissage, exact coprime invariants, and the finite-cohomology Mittag--Leffler property justify every later integral use. Thus no cohomology comparison is inferred merely from the action's factorization.

At finite level the local invariant pairing identifies the Pontryagin dual with the invariant Tate dual. Coefficient reduction is dual to inclusion of those finite Tate duals. Its inverse limit therefore gives exactly the compact coinvariants of A(-1), including torsion. Surjectivity onto Gamma and its generators tau,c give the literal matrix [T-7I | J+I]. The signs and the negative Tate twist agree. The image is compact, so the displayed cokernel requires no closure correction.

## Extra coordinates and ranks

The actual coprime involution and two free-generator lifts construct the stated section of the relative local source. Restriction to that section and to its kernel gives the literal inverse cocycle formula. The two local Kummer unit classes restrict to the dual basis of the relative Frattini quotient. The finite-normal-subgroup argument proves that the chosen r1,r2 normally generate the kernel.

Evaluation on these two elements embeds the equivariant homomorphism group in A squared. The relation and involution equations are closed and homogeneous in the torsion-free lattice, proving saturation. The chosen unimodular coordinate map is therefore legitimate; the proof explicitly retains its dependence on the actual relation submodule and does not claim that its entries were numerically evaluated. Euler characteristic cancels both finite torsion groups and gives the additional free ranks stated. All torsion is retained from E.41.

## Finite precision and actual inverse maps

In degree two the first Hall row is exactly zero in the obstruction matrix and is the primitive elliptic determinant coordinate. On its coordinate-zero lattice, the supplied split maps give the exact identity with scalar108. This proves a three-power torsion bound without projecting rationally across the free line. The saved Smith left matrix has last row exactly the original free coordinate, and its inverse has zero first coordinate on all torsion columns. Consequently subtracting the free coordinate and applying the modular inverse gives the actual integral splitting claimed.

For higher degree the eigenvalue formula and the split embedding/back-map imply the stated all-degree annihilator. In degree three the modulus729 exceeds this bound. Thus the finite Smith maps, digit lifts, and inverses recover the entire compact cokernel; no hidden elementary divisor can occur at a higher precision.

I freshly executed a copied program with a copied E.41 dependency in `a_e74_final_audit/code`. Every JSON field is identical to the reference, with no excluded field. Every array in both saved transformation archives is also identical, including both inverse maps and the split matrices. The execution independently reproduces obstruction groups Z3^5; Z3 plus C3^11 plus C9^4; and C3^63 plus C9^23 plus C27^7.

## Fibers and geometric comparisons

The first nonzero graded coordinate of a twisted lower stabilizer would be fixed by the positive-weight Frobenius T. Its absence of eigenvalue one proves uniqueness of the aligning lower conjugator. Lifting that conjugator and taking the central difference gives the inverse to the displayed central-fiber map, with precisely the central coboundary ambiguity. Finite generation of the relative source makes the cocycle spaces compact; compact geometric orbit spaces are Hausdorff. The resulting continuous bijection is therefore a homeomorphism.

The exact Hall two-cocycle and all quotient-induced maps are retained. This computes every nonempty central fiber and its obstruction group, while leaving the individual higher nonlinear obstruction values unevaluated as explicitly stated.

## Approved strengthening of the absolute/pro-three comparison

I also audited the replacement paragraph beginning “We prove the cohomological comparison,” saved after the first final audit. It proves the comparison directly from the opened local duality theorem. Every element of k(3) lies in a finite Galois three-extension E/k; adjoining cube roots of all of its k-conjugates gives a further finite Galois three-extension of k. Hence k(3) is closed under cube roots and its absolute H1 with F3 coefficients vanishes. Its H2 is the direct limit of the finite local Brauer three-torsion groups. A degree-three step from the unramified tower kills each invariant under restriction, so this direct limit vanishes. Higher finite local cohomology vanishes before taking the limit. Devissage for the trivial action of this kernel and Hochschild--Serre prove inflation in every degree for all finite three-primary modules factoring through D. Exact C2 invariants and the finite inverse-limit comparison then give the stated integral result. This establishes the comparison without invoking Demushkin classification. The updated theorem hash is recorded in audit.json; the unchanged numerical certificates still reproduce exactly.
