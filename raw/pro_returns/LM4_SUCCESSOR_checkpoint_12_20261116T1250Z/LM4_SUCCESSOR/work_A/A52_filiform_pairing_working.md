# The c-paired filiform layer and its compatible two-step refinement

Status: independently reviewed by the parent and CE, and incorporated as formal A.52. The single-head A51 construction and exact first/second/third scalar bounds have passed CE's independent review. This note supplies the separate c-stability and frame argument; it does not infer a full negative norm solution.

Use the actual map q:Pi->G2=P:H of A51, and form (q,q c). Write Q for its joint image and Hbar for the corresponding joint head image in H times H. Both images are stable under the coordinate interchange induced by c. The head Hbar has a normal7-subgroup Nbar and quotient C6 (the second head's C6 coordinate is the negative of the first). In particular it is an odd relative quotient retained in C, and h_C acts identically on Hbar.

## 1. Distinct module supports, with actual commutator witnesses

In the first head, the top central T direction has C6 character2; in the c-pullback it has character4. This can be seen directly from the degree-four free Lie brackets, but no graded recognition assumption is necessary. The exact head script now constructs actual Pi words a,b in the commutator subgroup whose first-head abelian coordinates are (1,0),(0,1), while their second-head coordinates lie on the interchanged axes. The words

    t1=[a,[a,[a,b]]],
    t2=[b,[b,[b,a]]]

have respective head images (T^e,1) and (1,T^f), with e,f nonzero mod7. These are central in Nbar. The exact exponents and group coordinates are printed in the certificate.

Consequently the four simple F2[C]-modules

    V_+, V_+^vee, V_-, V_-^vee

are mutually nonisomorphic: t1 distinguishes the first pair from the second, t2 distinguishes the second from the first, and the positive/negative seventh-root Frobenius orbits distinguish a module from its dual. They remain distinct over the odd subgroup Jbar=Nbar:C3. There are no cross alternating invariants between the two head blocks. Hence the paired odd/full exterior-square coinvariant dimensions are4 and2, respectively; in each block s exchanges the two odd invariant lines.

The image of R in each factor G2 is P. Its image in the direct sum of the four simple modules is a subdirect C-submodule, hence the entire sum by their nonisomorphism. Commutators then recover every central coordinate in P times P. Therefore

    q_pair(R)=P times P,
    Q=(P times P):Hbar.

The second equality is literal with the inherited action: the joint image projects onto Hbar and contains its complete kernel P times P. In particular the pair S=(S,S) is the pure head lift of s, because the two normalized s-vectors vanish.

## 2. Exact scalar refinements

Let Gbar be the quotient of Q by both two-dimensional centers, and put W=R intersect ker(Pi->Gbar). The same all-nonzero-class argument as A51 gives H1(C,V_i)=H1(C,V_i^vee)=0 for each block. The initial central refinement has centerF2^2, obtained by identifying the two central generators inside each block. The second has centerF2^4 and is exactly

    E2=Pi/W2 = Q times_Hbar C,
    W1/W2=(C2)^2.

The third scalar step stabilizes: W3=W2. The proof is blockwise the A51 argument. The old four-dimensional center is Nbar-trivial, which kills its tensor pairing with the four simple modules. The next center is an exterior-square quotient; Jbar acts trivially by odd-order semisimplicity, so dimension at most4. This bound is already attained.

No assertion here concerns a potentially incompatible arbitrary selection of all affine cocycles. The construction uses one actual nonzero cocycle in each of V,V^vee and its literal c-pullback; those four modules are distinct, and their joint quotient has just been identified.

## 3. The full retained frames and negative square

On E2 define the positive automorphism by

    psi=(identity_Q,h_C).

It is well defined because h_C induces identity on Hbar. It fixes the actual cusp literally. It retains the actual s-frame: the finite S is pure, so every element of C_Hbar(s) has a pure lift centralizing S in Q. Thus the projection of the old s-frame may be matched by a finite centralizer.

It retains the r-frame as well. The kernel P times P is a2-group and the actual r-lift has order3. Any head centralizer element conjugates that lift to another order3 lift over the same head element; the coprime complement theorem conjugates the two by the kernel. Hence C_Q(r)->C_Hbar(r) is surjective, and the required finite frame can be chosen. The two chosen finite frames and the old frames lie in the actual fiber product E2; no formal frame datum is substituted for an actual automorphism.

The negative companion is

    b=(c_Q,b_C),

where c_Q is the coordinate-interchange action induced by the actual c and b_C=h_C c_C is A33's retained involution. Their head actions agree, and both components square to1. Thus b is an actual involution of E2, with the same normalized parity-one data as the old tower.

Only now apply the central refinement criterion A3. Since W3=W2, the actual central refinement for N=W2 is E2 itself, and psi has the required literal peripheral frames. A3 gives a full positive h inducing psi on E2. The full negative a=h c therefore has involutory image on E2, but its full square is still only known to lie in the retained framed kernel.

## 4. Retaining earlier finite layers

For any finite collection of the A47/A48 perfect layers and the stabilized A49/A50 layers, let R_old be its stabilized residual inside R. Relative perfectness was proved in those results. The abelianization of R/R_old has only the old six-dimensional and21-dimensional simple modules (perfect heads add none). None of the new42-dimensional simple modules is a quotient of that abelianization. Equivalently, the degree-four central7 directions used above act trivially on the old modules and nontrivially on the corresponding new ones.

For any nonzero cohomology class in H1(Pi,V_i), the affine R-image is V_i. If R_old were killed, that simple module would be a quotient of (R/R_old)^ab, a contradiction. Thus R_old still maps onto every new simple module and its paired central cover. The entire all-nonzero-class inflation argument, actual-center calculation, two-step stabilization and frame gluing therefore apply over the enlarged base. Finite unions and compactness retain all preceding requirements.

This proves a further compatible family of actual parity-one involutory images. It also proves that the first scalar step can be nontrivial even in such a family. Neither cofinality nor a full involution has been proved.
