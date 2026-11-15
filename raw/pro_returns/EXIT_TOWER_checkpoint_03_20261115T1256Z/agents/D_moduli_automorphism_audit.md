# Independent audit of algebraic automorphisms of the open moduli stacks

This note checks the table requested by the root agent, for algebraic automorphisms over an algebraically closed field of characteristic zero, modulo 2-isomorphism. We embed the field in C for the analytic upper bounds; every listed automorphism is algebraic. It does not change `sections/E_topos.tex`.

## Verdict

The proposed table is correct for the open stacks: (0,3) gives 1; (0,4) gives S3; (1,1) gives C2; (1,2) gives 1; (2,0) gives C2; every other stable type gives S_n. The two C2 groups are automorphisms of the stack over the identity of its rigidification. They are proved by the torsor calculation below.

## Analytic upper bound and exact source

Ivanov, *Isometries of Teichmüller spaces from the point of view of Mostow rigidity*, Theorem A, gives all Teichmüller isometries as mapping classes except spheres with at most four punctures and tori with at most two. The closed genus-two action has its hyperelliptic kernel and is used after rigidification. Its local file is `research_sources/Ivanov2001Royden.pdf`.

The needed metric comparison was independently opened in Earle–Kra–Krushkal, *Holomorphic motions and Teichmüller spaces*, Trans. AMS 343 (1994), 927–948, Theorem 4, page 936. It applies to every Fuchsian group. Its proof uses the holomorphic-disc lifting theorem, Theorem 2 on page 932, and Proposition 1 on pages 934–935. Equation (9) on page 934 gives invariance of the Kobayashi function under biholomorphisms. Thus every biholomorphism in Ivanov's range is an orientation-preserving mapping class. These statements and proofs were read in the author-uploaded full text at https://www.researchgate.net/publication/265823226_Holomorphic_Motions_and_Teichmuller_Spaces . The exact retrieval, bibliography metadata, and locations are saved in `research_sources/EarleKraKrushkal1994_checked_source.json`. The official AMS PDF returned 403. Bibliography key: `D_EarleKraKrushkal1994`.

For an effective analytic quotient [T/H] with T contractible, a stack automorphism lifts to the universal orbifold cover T. The lift conjugates H to itself. Conversely such a normalizing biholomorphism descends, and two lifts give 2-isomorphic maps exactly when they differ by H. The group is therefore N_Aut(T)(H)/H. For a faithful pure mapping class group in the nonexceptional range, its normalizer is the full orientation-preserving mapping class group, and the quotient is S_n.

The analytic comparison detects algebraic 2-isomorphisms here. The moduli-stack diagonal is finite and unramified, so the isomorphism sheaf between two algebraic maps is finite and unramified over their source. A holomorphic section selects an open-and-closed component of this finite cover. Connected components of finite complex algebraic spaces are preserved by analytification; this component is algebraic, and its finite degree-one map to the normal source is an isomorphism. Apply this on an atlas and descend the unique resulting section. Thus the analytic upper bound is also an algebraic upper bound modulo 2-isomorphism. Over Qbar the same conclusion follows by faithfully flat extension to C; all finite-cover components are geometrically defined over the algebraically closed field.

## The exact inverse for M_1,2 = [M_0,5/S4]

An object of the right side is a smooth genus-zero curve pi:P→S, an effective relative etale divisor D of degree four, and a section r disjoint from D. (The four branch points are unordered and r is distinguished.) Put N=r^*O_P(r). The canonical section of O_P(D) trivializes its restriction at r. Since O_P(D−4r) has relative degree zero, evaluation along r gives the canonical isomorphism

    O_P(D) = O_P(4r) tensor pi^*N^(−4).

Set L=O_P(2r) tensor pi^*N^(−2). Its restriction at r is canonically trivial, and the preceding isomorphism identifies L^2 with O_P(D), with canonical defining section s satisfying s|_r=1. Form the double cover

    E = Spec_P(O_P direct-sum L^(−1)),  u^2=s.

It is smooth of genus one. Above r the two sections u=+1 and u=−1 give an ordered pair (p,q). This construction commutes with arbitrary base change and with isomorphisms of (P,D,r).

Conversely, on a smooth genus-one family with distinct ordered sections (p,q), use p as origin and take the involution j(x)=p+q−x. It exchanges p and q. Its quotient P has genus zero, its branch divisor D has degree four, and the common image r of p,q misses D. The double cover is canonically recovered by the construction above: p fixes the trivialization of the covering line at r, and a degree-two covering line with this trivialization is uniquely L. Any isomorphism of quotient data lifts uniquely once p is fixed; the other lift exchanges p and q. Hence both composites are canonically isomorphic to the identity functor, including on arrows. There is no residual mu2 gerbe in this equivalence.

Analytically the deck group of this quotient is H, the preimage of the point stabilizer S4 under Mod_0,[5]→S5. Its normalizer is itself: the normalizer of S4 in S5 preserves its unique fixed point and therefore is S4; pulling back gives the claim. Ivanov's theorem applies to T_0,5. Thus Aut(M_1,2)=1. The label swap is naturally 2-isomorphic to identity by the same involution j(x)=p+q−x.

## Gerbe automorphisms: exact descent calculation

Let G→B be a mu2-banded gerbe. Every automorphism of mu2 is trivial in characteristic zero. An equivalence F over the identity of B therefore preserves the band. Choose local objects x_i of the gerbe. The torsors Isom(x_i,F(x_i)) glue on overlaps because the band is central. They define a mu2-torsor P on B. Conversely P acts on every object x by contracted product P tensor x. These constructions are inverse up to natural isomorphism, and composition corresponds to tensor product of torsors. Consequently the group of equivalences of G over identity B, modulo 2-isomorphism over B, is exactly H^1(B,mu2). This argument requires no neutralization of G over B. In the applications B has trivial generic inertia, so a 2-automorphism of its identity is trivial; forgetting the chosen identity comparison introduces no further quotient.

## M_1,1

Write M_1,1=[Spec k[a,b,Delta^(−1)]/G_m] with weights 4,6 and Delta=−16(4a^3+27b^2). The rigidification B has weights 2,3. Its coarse space is A1_j, with stack orders 3 at j=0 and 2 at j=1728. An automorphism of B must preserve the two points separately, so its coarse affine automorphism is identity. The local root-stack chart has tangent character of order r, forcing an automorphism over the identity coarse chart to act trivially on mu_r; the remaining scalar lift is a 2-isomorphism. These local isomorphisms agree on the dense scheme locus and glue. Thus Aut(B)=1.

The localized polynomial ring is factorial, and its only homogeneous units are c Delta^m. Hence equivariant line bundles give Pic(B)=Z/6. Global units on B are k^*. The Kummer sequence, with k algebraically closed, gives H^1(B,mu2)=Pic(B)[2]=C2. The gerbe calculation therefore gives Aut(M_1,1)=C2.

The explicit nontrivial element is

    T(L,a,b)=(L^7, Delta^2 a, Delta^3 b).

The new discriminant is Delta^7. Thus T^2(L,a,b)=(L^49,Delta^16 a,Delta^24 b), and multiplication by Delta^(−4):L^49→L supplies a canonical isomorphism with identity. On the rigidification, multiplication by Delta^(−1):(L^2)^7→L^2 identifies its map with identity. On the mu4 stabilizer it raises an element to the seventh power, hence inverts it, whereas on mu6 it is identity. This proves nontriviality modulo 2-isomorphism.

## M_2,0

The quotient by the canonical hyperelliptic involution gives a mu2-gerbe M_2→B=[M_0,6/S6]. It is a gerbe over the entire stack: etale locally every genus-zero family with six distinct branch points has a square-root covering line; two such double covers are locally isomorphic, and their relative automorphisms are exactly the deck mu2. The genus-zero quotient data is the rigidification because an automorphism of a hyperelliptic curve descends to the quotient, and every automorphism of branch data lifts etale locally, uniquely up to the deck involution.

The orbifold universal cover of B is T_0,6 and its deck group is the full orientation-preserving six-punctured sphere mapping class group. Ivanov plus Earle–Kra–Krushkal therefore gives Aut(B)=1.

To compute H^1(B,mu2), use the sphere mapping class group presentation with braid generators sigma_1,...,sigma_5, ordinary braid relations, the spherical relation

    sigma_1 sigma_2 sigma_3 sigma_4 sigma_5^2 sigma_4 sigma_3 sigma_2 sigma_1 = 1,

and the full-twist relation (sigma_1 sigma_2 sigma_3 sigma_4 sigma_5)^6=1. In the abelianization all generators coincide; the remaining relations have lengths ten and thirty, so the abelianization is Z/10. Equality follows also in the reverse direction because sending every sigma_i to 1 modulo 10 satisfies every displayed relation. Thus there are exactly two characters to C2. The nontrivial one is the sign of the permutation of six branch points. Finite etale/topological comparison identifies this with H^1(B,mu2).

The corresponding automorphism of M_2 twists each hyperelliptic double cover by the sign torsor of its six branch points. It is algebraic and has square naturally isomorphic to identity. The gerbe calculation proves it is nontrivial and exhausts all automorphisms. No splitting or neutrality of the hyperelliptic gerbe has been assumed.

## Remaining elementary types

M_0,3 is a point. M_0,4 is P1 minus {0,1,infinity}, whose automorphisms are exactly its six cross-ratio transformations: an automorphism extends to P1 and permutes its three missing points. Label permutations S4 act through S3 with Klein-four kernel. These give the remaining entries of the table.

## Scope checked

The two ghost involutions are automorphisms of the open algebraic stacks. Their inclusion in a decorated or compactified automorphism problem must use the actual forgetful map from that problem to the open stack. The calculation here is the exact open-stack group requested for the root's structured algebraic comparison.
