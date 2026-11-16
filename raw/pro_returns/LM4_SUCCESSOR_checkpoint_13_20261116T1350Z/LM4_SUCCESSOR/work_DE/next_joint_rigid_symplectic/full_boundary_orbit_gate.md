# Actual full theta5: a boundary-orbit gate (post-B68 research note)

This is a new conditional route, not a theorem of injectivity. Formal B sources are frozen for checkpoint08.

Let F6=F(f0,...,f5), and let L=F(f0,f2,f3,f4,f5), so F6=F(f1)*L. Move label5 to the final PB6 strand as in B68. Write the resulting Birman fiber as F(x1,...,x5), B=x1...x5. The exact extracted antiword for f1 is q B^-1 q^-1, q=x3 x5. Inverting the extraction and conjugating the fiber identification by q^-1 therefore sends f1 to B literally. B is primitive in F5, so this fiber is F4*<B>.

For an actual source braid g, its Artin action sends x6 to Q_g x6 Q_g^-1. After killing x6, let D_g be its action on the first five generators. The actual fiber conjugation automorphism is alpha_g(x)=Q_g^-1 D_g(x) Q_g. It satisfies alpha_g(B)=Q_g^-1 B Q_g because the total Artin boundary is fixed. After the q normalization, alpha'_g=Inn(q^-1) alpha_g Inn(q), and

R_g=q^-1 alpha_g(q) Q_g^-1,
alpha'_g(B)=R_g B R_g^-1.

Kill B by x5=(x1 x2 x3 x4)^-1. Let beta_g be the quotient automorphism and rho_g the image of R_g in F4. The source acts affinely on F4 by

v -> beta_g(v) rho_g,
rho_(gh)=beta_g(rho_h) rho_g.

The exact actions are retained in full_boundary_orbit_action.json, freshly calculated by boundary_orbit_full.py with genuine stdout. The f1 action and vertex are both trivial after this quotient, so the affine action factors through L. Its five generator vertices are:

- f0: (-4,-3,-2);
- f2: (1,2,3,4);
- f3: (1,2,3,4,-3,-2,-1);
- f4: (-3,2,3);
- f5: (-1).

The normal closure M=<<B>> in F4*<B> is free on the conjugates of B indexed by F4, and M_ab has one integral basis vector for every such index. The image of l f1 l^-1 has abelianization the basis vector indexed by rho_l. Thus if rho:L->F4 is injective as a SET MAP, every finite set of these images has independent classes in M_ab. Such a finite set generates a subgroup of the free group M; if there are n elements, its rank is at most n, and the independent abelianizations force rank at least n. The induced epimorphism F_n onto that rank-n free subgroup is an isomorphism by Hopficity. Therefore the entire free normal closure <<f1>> in F6 injects under theta5.

If theta5 had a nontrivial kernel N, its intersection with the nontrivial normal subgroup <<f1>> would be nontrivial. Indeed choose n in N nonidentity; some element of <<f1>> does not commute with n, since centralizers of nontrivial elements of a free group are cyclic and <<f1>> is nonabelian. Their commutator lies nontrivially in both normal subgroups. This contradicts the preceding injection. Consequently freeness of the affine orbit of1 would prove discrete theta5 injectivity.

The exact remaining discrete gate is therefore trivial stabilizer of1 for this particular affine F5 action on F4. Neither the distinct generator vertices nor any finite orbit sample proves it. The stronger full induced profinite topology is a separate unresolved requirement. In particular, no inference of free-profinite injection is made from an abelianized normal-closure module.


## Gate refuted and actual full relation obtained

The actual orbit is not free: rho(f0^-1 f2^-1)=rho(f5). Further exact unquotiented computation upgrades this collision to the full theta5 relation [f5^-1 f1^-1 f0^-1 f2^-1,f1]=1. The proof and complete fresh certificate are full_theta5_noninjection_proof.md and refute_full_theta5.py/.out. Thus the conditional criterion above is sound but its hypothesis is false for this actual action. The stronger relation refutes theta5 and theta5-hat injection; the completed-kernel closure comparison remains separate.
