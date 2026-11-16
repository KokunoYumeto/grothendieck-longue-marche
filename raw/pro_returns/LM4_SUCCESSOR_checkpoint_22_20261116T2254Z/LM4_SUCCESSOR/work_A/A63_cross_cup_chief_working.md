# Actual cross-cup chief directions beyond the integral tower

Complete working proof for review. The actual quotient and kernel stability have independently passed CE review. The negative square and literal frames on this new quotient remain unresolved; this note does not promote them.

## 1. An explicit finite group, with the twist retained

Let k=F8 and V=k^36 be the actual monomial H-module. Put A=V^4 and T=(V^(2))^6. The superscript means that every monomial scalar is squared, while the permutation is unchanged. Coordinatewise Frobenius identifies V^(2) with V as an F2[H]-module, but not as the same literal k-representation; retain this twist throughout.

Index the six T coordinates by1≤i<j≤4. On N=A×T define

    (a,z)(b,w)=(a+b,z+w+c(a,b)),
    c(a,b)_ij=a_i*b_j,

where * is coordinatewise multiplication in k on the36 weight positions. Bilinearity proves associativity. The inverse is(a,z+c(a,a)); the square is(0,c(a,a)); and the commutator is

    [a,b]_ij=a_i*b_j+a_j*b_i.

Each T coordinate and each weight coordinate is attained by a commutator of two single-row/single-weight vectors. Hence N'=T and Phi(N)=T, with N/Phi(N)=A. The H-action on A is the original monomial action and on T uses squared scalars. This preserves c literally, so gives a strict H-action on N. The finite group has order2^1080. This is an actual group law, not only a graded Lie bracket.

T is a direct sum of six simple twisted modules. Its invariants and coinvariants under H vanish, already under the relevant normal odd subgroup. In particular[T,H]=T.

## 2. Actual source generators and the residual image

Use the four normalized cusp cocycles from A62, reduced modulo2. Their source values are e(s)=0 and e(r)=(e1(r),...,e4(r)) in A, with r-norm zero. In characteristic2 the vector a=r*e(r) satisfies(1-r)a=e(r). Choose v=(a,0) in N. In N⋊C take

    S=(1,s_C),    R=v(1,r_C)v^-1.

Then S²=R³=1 exactly, and the affine cocycle is literally the chosen four cusp cocycles. The universal property of Pi=C2 coproduct C3 gives a continuous source homomorphism q:Pi→N⋊C.

Its residual image q(R_original) projects onto A. Otherwise a nonzero H-linear map from the missing semisimple quotient of V^4 to V would give a nonzero linear combination of the four cusp classes that vanishes on R_original. That cocycle would inflate from C, contradicting H1(C,V)=0. By the finite2-group Frattini theorem, the residual image is all N. Thus the source map is onto the actual semidirect extension N⋊C.

## 3. Pairing with all integral abelian data

Write A_infty=L_infty^4⊕V^4 for the actual abelian residual quotient retained by A62, with the binary s-coordinates separate. Its projection onto A reduces the free cusp coordinates modulo2. Form the actual pro-two fiber product

    B=A_infty ×_A N.

Its derived subgroup is T: the projection to N is onto, and A_infty is abelian. Its abelianization is A_infty, so its Frattini quotient is V^8. Pair the two actual source cocycles; their common A-values agree literally. The image of the original residual R in B projects onto all V^8, by the complete original eight-class calculation. B is a finitely generated pro-two group, so the pro-two Frattini theorem makes that image all B.

Let W_infty=intersection W_n, the kernel of the actual map to A_infty⋊C. The preceding surjectivity proves

    q(W_infty)=T.

For U_infty=intersection[W_n,Pi], there are inclusions

    [W_infty,Pi] ⊂ U_infty ⊂ W_infty.

Taking q-images gives T=[T,H]⊂q(U_infty)⊂T. Therefore

    q(U_infty)=T

exactly. No interchange of commutators and an inverse limit is assumed.

Consequently the actual joint source quotient is the full fiber product

    E=D_infty ×_(A⋊C) (N⋊C),

with kernel T over D_infty. Surjectivity follows directly: lift a chosen D_infty element by Pi, and correct its N-coordinate by an element of U_infty, whose q-image is all T.

## 4. Nonsplitting, including continuous sections

Let P_infty be the residual group of D_infty over C. Its closed derived subgroup M_infty is globally central in D_infty, by A62; equality with the inverse-limit center follows because the closed derived subgroup surjects onto every finite center M_n.

Suppose the extension E→D_infty had a continuous section. Its projection to N⋊C would restrict to a homomorphism eta:P_infty→N inducing the full cusp projection onto A. Since A=N/Phi(N), eta is onto N. Hence eta(P_infty')=N'=T.

On the other hand, every element of M_infty=P_infty' is central in D_infty. Its image under the section commutes with the entire section image, whose C- and H-projections are onto. Its N-projection lies in T and is H-fixed. Therefore eta(M_infty)⊂T^H=0, a contradiction. This excludes continuous sections; no chosen splitting of D_infty over C was used.

For every nonzero k-linear functional ell:T→V^(2), the corresponding quotient group still has nonzero commutator image equal to the simple target. The same argument proves nonsplitting of that pushout. Thus the six extension classes are k-linearly independent and can be retained simultaneously in the actual source quotient. They are six directions, not an exhaustive count of all next extensions.

## 5. Exact cohomology and kernel stability

Initial-base acyclicity and continuous Hochschild–Serre give

    H1(D_infty,V^(2))
      =Hom_C(P_infty^ab,V^(2)) ≅ k^8.

Its inflation to H1(Pi,V^(2)) is the actual complete eight-class isomorphism. The five-term sequence for U_infty therefore makes transgression injective on Hom_Dinfty(U_infty,V^(2)); its image is the kernel of H2(D_infty,V^(2))→H2(Pi,V^(2)).

The six coordinate extension classes are literally the cup products e_i cup e_j, i<j, using the H-equivariant pairing V⊗V→V^(2) given by coordinatewise multiplication. The corresponding two-cocycle is e_i(g)*(g e_j(h)), exactly the pullback of c above. Thus the actual quotient proves six nonzero independent cross-cup directions in the stated H2 kernel, beyond the integral coefficient tower.

The full h0 of A62 fixes the four cusp cohomology classes. The coefficient-twisted c-action is minus identity integrally and hence identity modulo2; its induced intertwiner on V^(2) is the squared monomial intertwiner. Naturality of cup products shows that h0 and c preserve the six classes with these coefficient identifications. Naturality and injectivity of transgression then preserve their actual residual homomorphisms, and in particular their joint source kernel. Therefore E is stable under the actual full h0 and c. This stability does not solve the next norm equation.

## 6. The next square gate, still open

The negative square is already one on D_infty and on the coefficient T. Thus its discrepancy on E is a genuine continuous D_infty→T cocycle. Literal tau inversion kills its cusp restriction. With the fixed old s-frame, its restriction at s is a coboundary: the old normalizer square is now an element of T. Since the relevant H1 restriction is exactly the same four s plus four cusp decomposition, the square cocycle is a global coboundary. It is therefore inner by a vector in T^tau, of dimension24 overk.

This does not force that vector to vanish. The coefficient negative action is the identity on T^tau, so the obvious cusp-fixed inner corrections have zero norm. A complete calculation must retain every allowed action and frame correction and distinguish a zero cohomology class from a zero literal square. No square vector, full negative involution, or new literal-frame lift is asserted here.
