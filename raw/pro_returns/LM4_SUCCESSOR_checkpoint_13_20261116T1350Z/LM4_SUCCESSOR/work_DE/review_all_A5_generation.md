# Independent adversarial review: every canonical A5 generation test

Reviewed 16 November 2026, approximately05:35–05:42UTC. Inputs were `work_CE/research_A5_generation.txt`, C.28 and C.35 in `work_CE/C_further.tex`, the finite certificate and retained output, and the primary restriction theorem cited below. No formal source was edited during the checkpoint freeze.

## Outcome

The proposed proof passes in its stated scope: for an actual involution of the full GT0 group and its canonical R1 word u, every continuous epimorphism to A5 remains surjective after the substitution `(x,y) → (x,u^-1*y*u)`. The argument uses full duality of u, the actual involution, the three-cusp section incidence, and a one-section count for a different involution with nontrivial mod-two action. It does not prove generation in every finite group or generation of the full profinite free group.

An independent certificate was written as `check_review_A5_generation.py`, with actual output in the corresponding `.out` file. It uses permutations on five letters and imports no code or data from the proposed certificate. Its orbit numbering differs, so comparisons should use passports and five-cycle class equality.

## Finite classification and kernel stability

The independent enumeration finds2280 ordered generating pairs, in19 free Aut(A5)-orbits of size120. They divide as8 mixed3/5 cases,6 cases with one order2 generator,1 case with both generators of order3, and4 cases with both generators of order5. The last four have passports `(5,5,3)` twice, `(5,5,5)` and `(5,5,2)`. The two different-five-class cases are precisely `(5,5,2)` and one `(5,5,3)`.

For each of the nine critical orbits, the certificate tests every finite possible value F of the negative conjugating word. Subject to the actual third-peripheral conjugacy class, it checks the pair `(a^-1,F^-1*b^-1*F)`, its original quotient-kernel orbit, and the unique inducing automorphism. Every candidate preserves the kernel and induces an inner automorphism. This directly checks the finite statement used in the proof; it does not infer kernel stability from generator orders alone.

Every equal-order generating pair admits a unique swapping automorphism. It is inner in the `(3,3,5)` case and in the two equal-five-class cases, and outer in the two different-five-class cases. Thus the inner/outer distinctions needed for the remaining three cases are correct. The outer automorphism interchanges the two five-cycle classes, while inversion preserves each; consequently the negative action in the critical cases is inner. Its conjugator h satisfies `h²=1` because A5 is center-free, and is nontrivial because it inverts an odd-order element.

All59 subgroups of A5 are enumerated independently. The maximal proper subgroups have orders6,10,12, with counts10,6,5, and all are self-normalizing. None of the order12 subgroups contains an element inverting one of its3-cycles. The centralizer of an element of order3 or5 is its cyclic subgroup; its normalizer has twice that order. The code checks directly that two involutions in each such odd dihedral normalizer commute exactly when they coincide.

## The two full involutions

Writing `iota(x)=y`, `iota(y)=x`, C.35 gives `iota(u)=u^-1`. Hence `v=Inn(u^-1)iota` is an actual involution, and it swaps x with y'=u^-1*y*u. The identity `iota alpha=Inn(f) alpha iota`, together with `alpha(u)=f^-1*u`, gives

```
alpha v = Inn(alpha(u)^-1*f^-1) iota alpha
        = Inn(u^-1) iota alpha
        = v alpha.
```

Thus tau=alpha*v is an actual involution. It is nonidentity because its action on H1(F,F2) is the swap. Inner modifications do not change peripheral exponents, so tau sends the third cusp to a conjugate of its inverse. In the finite quotients used below, stability of the relevant kernel under alpha and iota implies stability under v and tau; this is checked before their induced automorphisms are used.

## The one-section lemma and its consequence

The primary author manuscript of Kochloukova and Zalesskii(2007), *Automorphisms of pro-p groups of finite virtual cohomological dimension*, was reopened at https://mat.unb.br/~pz/arquivos/Claus3.pdf. Its Theorem2, manuscript pp3–4, is explicitly a theorem about full profinite groups: for an open subgroup of finite cohomological p-dimension and no elementary abelian subgroup of rank2, the restriction map to order-p subgroup normalizers is a dense embedding in sufficiently high degrees. The proof immediately explains why finite source cohomology makes that map an isomorphism with a finite product. Thus the paper's title imposes no pro-p restriction on the theorem used here.

For E=Fhat2 semidirect_sigma C2 with regular mod-two H1-module, the two-row Hochschild–Serre sequence gives `H^n(E,F2)=F2*u^n` for every n≥2. The section prevents the only transgression; the positive cohomology of the regular module vanishes. Every finite subgroup injects into C2, and each section normalizer contributes at least one dimension to the restriction product. The primary theorem therefore gives exactly one conjugacy class of sections. E-conjugacy and F-conjugacy of these sections agree: a conjugator's nontrivial quotient label can be removed using an element of the section itself. No assertion about a centralizer and no torus peripheral hypothesis is needed.

If sigma acts trivially on q:F→Q, the section sigma maps to the central element `(1,c)` in Q×C2, and so does every section. If `sigma(z)=k*z^-1*k^-1`, the element `k^-1*sigma` in E inverts z. Its square lies in the full procyclic centralizer of z and is fixed by inversion, hence is one. It and its product with z are local involutory sections; both have image `(1,c)`. Their product is z or z^-1, proving q(z)=1. This uses the already established full centralizer of the primitive boundary, and does not assume that sigma literally fixes the chosen peripheral representative.

## Elimination of the proper images

For mixed orders3 and5, no proper subgroup can contain both. For a pair containing an order2 generator, a proper image is A4, S3 or D5 according to its orders. The inner involution h normalizes the image, so self-normalization puts it inside that image. A4 is excluded by the3-cycle inversion check. In the odd dihedral cases h centralizes the substituted order2 generator and is nontrivial, so it equals that generator.

The relevant full section then has central image in A5×C2. More explicitly, the three full classes represented by alpha, x*alpha and y'*alpha have distinct mod-two labels00,10,01. C.28's triangle incidence forces the third cusp's local classes to be the latter two. If one has central finite image, the product of the two third-cusp reflection images has order at most2, contradicting its actual order3 or5. Thus the incidence argument uses the correct full classes and survives passage to a finite quotient, where different full section classes may merge.

In a proper cyclic image of order3 or5, write b'=a^r. The induced v swaps a,b' and has square one, so r²=1. Different five-cycle classes require r=2 or3 and are immediately impossible.

In each remaining equal-class case the original swapping automorphism is Inn(t), for a nontrivial involution t of A5. If r=1, v fixes a and is an inner involution lying in its odd cyclic centralizer; hence v is the identity and q(u)=t. Choose arbitrary lifts A,B to SL2(F5), and a lift T of t. Conjugation by T swaps A and B up to central signs. Since u is a full commutator word, multiplying either input by a central sign has no effect on its value U; this follows from its zero continuous abelianization. Full duality consequently gives `U*Ad(T)(U)=1`. But U=±T, and the independent matrix check confirms that every lift of a nontrivial projective involution has square−I. Hence the left side is−I, a contradiction. No assumption that the swapping automorphism fixes chosen lifts exactly is needed.

If r=−1, the induced alpha and v are commuting inner involutions inverting the same odd cyclic subgroup. Commutation of inner automorphisms implies actual commutation of their conjugators because A5 has trivial center. The odd-dihedral check makes those conjugators equal. Thus tau=alpha*v acts trivially on the finite quotient. Its mod-two action is regular and it reverses the primitive third cusp; the one-section consequence makes the nontrivial third-cusp image trivial, the final contradiction.

The mechanisms cover all19 kernel orbits. The proof does not require choosing compatible finite values of u independently, nor does it assert that every candidate satisfying finite necessary conditions comes from a full word. It starts with the actual canonical full word and rules out every possible proper A5 image.
