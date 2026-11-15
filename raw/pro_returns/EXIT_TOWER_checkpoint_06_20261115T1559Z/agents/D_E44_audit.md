# Independent E.44 audit: the Klein-four forgetting diagram

Auditor: `levels_geometry`. Date: 2026-11-15. Verdict: the specific V4 argument in `B_E44_candidate.md` passes, with the exact topology and conjugator details recorded below. This note does not use the nonsolvable finite-subgroup argument in Boggi–Zalesskii.

## Primary source and the precise p-group input

Read the supplied primary TeX `background/arXiv_src/boggi_zalesskii_2406.08639/main.tex`: Theorem A; Section 2 centralizer and normalizer criteria; Section 3 Brown–Scheiderer comparison; Section 4, including `prop:prime_order`, `orderp`, `inductionok`, and `pcaseproof`. The needed assertion is Theorem A for the full profinite embedding and p=2. It concerns an entire finite 2-subgroup, so applies to V4 jointly. Corollary B and its residual-p hypothesis are not needed.

The mixed ten-point group G contains the pure genus-zero group with finite index. The latter has a finite classifying-space model from the successive configuration fibrations. Thus G is virtually torsion-free of finite cohomological dimension and is of type FP-infinity; finite-module cohomology is finite in every degree. Genus-zero goodness, preserved by finite-index extension through the two Lyndon–Hochschild–Serre spectral sequences, gives the stated comparison for finite modules. Every discrete F2[[Ghat]]-module is the filtered union of its finite invariant submodules: an element has a finite orbit under the profinite action and its F2-span is finite. Continuous cohomology and ordinary cohomology of an FP-infinity group commute with this union. Therefore the source's all-discrete-module hypothesis is met, not just its finite-module version.

The p-group proof uses the order-two Brown decomposition first. Its nonzero H0 summands distinguish the factors indexed by conjugacy classes; the natural restriction map is diagonal on those summands when two discrete classes have the same profinite class. This supplies both surjectivity and injectivity of the class comparison. The order-four step chooses a central subgroup T of order two in H and passes to N(T)/T. The finite central quotient has a common open subgroup with N(T), obtained by an open normal subgroup avoiding T; Shapiro and the finite-quotient spectral sequences justify the displayed cohomology comparison there. The preimage of a finite subgroup of N_G(T)/T is finite, so conjugating H/T into that discrete quotient conjugates the full H into G. This uses no assertion about nonsolvable groups.

Normalizer closure comes from the hereditary subgroup criterion. Centralizer closure then follows without interchanging arbitrary intersections and closures: N_G(H) has its actual finite conjugation map to Aut(H), and C_G(H) is its kernel. The continuous conjugation action of N_Ghat(H) on the finite embedded group H has the same finite image by density; its kernel is the closure of that discrete finite-index kernel. Thus C_Ghat(H)=closure C_G(H).

## The exact centralizer and its full topology

Let H act by a(z)=-z, b(z)=1/z, with its fixed pairs A=(0,infinity), B=(1,-1), C=(i,-i), and the regular orbit D=(z,-z,1/z,-1/z). The mixed group G is the preimage of the centralizer of the complete elementwise permutation representation in S10; N=C_G(H).

Forgetting A,B,C maps G into the preimage of the double-transposition subgroup H_D in the four-point permutation group. This preimage equals C_Gamma04(H_D): the canonical Klein-four group is normal, and the conjugation action is precisely the S4 action on its three nonidentity double transpositions. The centralizer is the product of the pure four-point group and H_D.

The restriction f4:N -> C_Gamma04(H_D) is an isomorphism. Its inverse is the actual family operation that adds the fixed pairs of the three named nonidentity elements of the canonical Klein-four group of a four-point sphere. These six points are distinct and disjoint from the original four. Equivariant isomorphisms extend and restrict uniquely. This is a comparison of the equivariant moduli groupoids, including their finite automorphism groups.

In particular f4^-1 composed with the ordinary forgetting homomorphism G -> C_Gamma04(H_D) is a retraction onto N. Every finite quotient of N therefore pulls back to G. Thus Nhat embeds into Ghat with its full topology and agrees with the centralizer closure furnished by Theorem A. Quotienting its central H gives the full completion of N/H and the named pure Gamma04.

## Exactly two pure classes and the discarded-pair correction

Finite-subgroup realization on the punctured sphere, followed by uniformization, makes every discrete finite H action a Möbius action. For the required elementwise label permutation, normalize A1=0, A2=infinity, B1=1. The involutions become -z and 1/z. Then B2=-1 and C1 is either i or -i. The fourth orbit is determined by its first label z, with the other three -z,1/z,-1/z. The allowed z-domain is the connected sphere minus the six fixed points. Hence the two choices of C1 give exactly the two pure-conjugacy classes.

Apply Theorem A to F(H). Its conjugator can be made pure by removing its finite permutation with a discrete element of G; this changes the resulting discrete H only by discrete conjugation and leaves its elementwise permutation representation fixed. A further pure discrete conjugation puts it in one of the two displayed classes. The remaining correction P=(C1 C2) can be represented by a half-twist supported in a disk containing exactly those two auxiliary points. Forgetting C1,C2 kills this mapping class, so f4 and both q targets discard P. Its permutation commutes with the specified H representation. After this correction F fixes H pointwise, because H embeds faithfully in the permutation quotient. It preserves N and the two choice subgroups.

## The colour quotient and both q maps

For four points with a partition into two unordered pairs, let C4=S2 times S2 preserve the pairs individually, D8 preserve their unordered partition, and V be the normal Klein-four subgroup. Then C4 cap V has order two and C4 V=D8. Consequently inclusion induces

`Gamma04^C4/(C4 cap V) = Gamma04^D8/V = R`.

The same identity holds on full completion: both mixed groups are finite-index subgroups and the quotient kernels are the indicated finite subgroups. V is characteristic as the maximal finite normal subgroup. Indeed a finite normal subgroup intersects the torsion-free pure group trivially; their commutator lies in that intersection, so it centralizes the pure group. The latter's centralizer is exactly V, including after completion by the four-point calculation used in E.27–E.28.

For Omega_b, the two b-orbits in D, the stabilizer N_b of {z,1/z} satisfies N=H N_b and H cap N_b=<b>. Thus N_b/<b> -> N/H is an isomorphism, also on full completions. Ordinary forgetting retains A and this b-orbit. The involution b becomes the simultaneous interchange within both retained pairs and is killed by the colour quotient above. This gives q_b. The analogous choice of the a-orbit {z,-z}, retaining B, gives q_a. They use only finite choice stabilizers, ordinary forgetting, and the specified finite quotients.

## Coordinates and the cancellation in Out(R)

Set u=(z^2+1)^2/(4z^2). The named regular-four cross-ratio is lambda=((z^2-1)/(z^2+1))^2=1-1/u. For the two target colour groups, use U=(ell+1)^2/(4ell). Their cross-ratios ell_b=z^2 and ell_a=((z-1)/(z+1))^2 give U_b=u and U_a=u/(u-1).

The target R is the orbifold sphere with an order-two point at U=0 and punctures at U=1,infinity. The source is the ordinary three-punctured u-sphere. Hence q_b is the actual map with group presentation F(x0,x1) -> <x0,x1 | x0^2=1>, so is surjective; on completions its kernel is the closed normal closure of x0^2. The involution S:U -> U/(U-1) fixes the cone and exchanges the two punctures. Thus q_a=S_R q_b=q_b S_X as actual orbifold maps, with the usual explicitly allowed basepoint conjugations.

The source action is the named A by f4 and the target is iota(A): both restrict to the same named index-two pure four-point action, and the trivial centralizer of that subgroup makes the outer extension unique. A commutes outerly with the anharmonic relabelling S_X. Combining the two q diagrams then gives iota(A)S_R q_b=S_R iota(A)q_b up to one inner target comparison. Surjectivity of q_b removes it, giving equality in Out(R). E.28's faithful identity iota(J(A))=S_R iota(A) S_R consequently forces J(A)=A.

The exact rational identities and finite colour-group equalities were independently executed in `code/d_e44_coordinates.py`; its `.json` and `.out` save all results. They certify those finite/algebraic calculations; the group and profinite comparisons are the proofs above.
