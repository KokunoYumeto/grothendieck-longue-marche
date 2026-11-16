# Full cyclic rigid map: a nontrivial exact kernel word and kernel types

Research proof prepared after B68 during the formal checkpoint08 freeze. No frozen theorem/register source is changed here. This concerns the actual map theta5 from B65, not the previously proposed intermediate quotient Q.

## 1. Actual word and exact finite certificate

Let H5=F(f0,f1,f2,f3,f4,f5), the geometric free source of the actual cyclic family. B28 identifies its full profinite completion with its embedded closure in the ambient pure mapping class group. B61 fixes the common base, the six geometric meridians, and their certified full eleven-strand braids. B65 deletes five strands to give

    theta5 : H5 -> PB6,

with finite label order (4,11,5,1,10,6), capping point label2, and fixed linking ell_(4,6)=0. The joint kernel of all twelve rigid-seven restrictions on H5 equals ker(theta5): two maps are zero and the ten remaining maps have this same transported kernel. The same assertion holds after full completion by B65.

Put

    g = f5^-1 f0^-1 f2^-1,
    h = f5^-1 f1 f5,
    k = h^-1 g = f5^-1 f1^-1 f0^-1 f2^-1,
    w0 = [k,f1].

With signed index j meaning f_(j-1), the source word is

    (-6,-2,-1,-3,2,3,1,2,6,-2).

It is freely reduced of length10 and therefore nonidentity in the free group H5. A direct finite witness, independent of normal forms, sends f1 to (12), f5 to (23), and the four other generators to1. The word maps to the nontrivial three-cycle (123) in S3. In particular its image in the full free profinite completion remains nonidentity.

The standalone program `refute_full_theta5.py` reads the original common-base eleven-strand braid words. It imports no discovery code, performs its own strand deletion and free-word/Artin operations, and checks the actual six-strand substitution. The reduced braid word has length132. Its six Artin images are exactly

    ((1,), (2,), (3,), (4,), (5,), (6,)).

Artin's faithful action therefore proves theta5(w0)=1 in PB6 itself, before capping. The complete substituted braid, the six source braids, all six Artin images and the S3 data are retained in `full_theta5_noninjection_certificate.json`. `refute_full_theta5.out` is genuine standard output from the fresh run.

Consequently both theta5 and its continuous extension theta5-hat are noninjective. This is not merely a failure of an abelian, nilpotent or homology representation.

## 2. Structural derivation in the actual Birman fiber

Move label5 to the final strand by tau=(sigma3 sigma4 sigma5), conjugating each braid as tau^-1 b tau. The finite order becomes (4,11,1,10,6,5). The last-strand Birman kernel is free of rank5.

Write B=x1 x2 x3 x4 x5 and q=x3 x5 in its standard free coordinates. Reading the last Artin conjugator and then killing x6 gives an antihomomorphism on this kernel, as already checked in B67/B68. Inverting that word gives the actual fiber homomorphism. For f1 the extracted antiword is q B^-1 q^-1. Conjugating the genuine fiber identification by q^-1 therefore sends f1 to B literally.

For a general source element s, write its last Artin image as Q_s x6 Q_s^-1 after the indicated strand transport, and let D_s be the induced Artin action after killing x6. Its actual conjugation action on the free fiber is

    alpha_s(x) = Q_s^-1 D_s(x) Q_s.

The Artin boundary is fixed, giving alpha_s(B)=Q_s^-1 B Q_s. In the q-normalized fiber the action is alpha'_s=Inn(q^-1) alpha_s Inn(q), and

    alpha'_s(B) = R_s B R_s^-1,
    R_s = q^-1 alpha_s(q) Q_s^-1.

The exact actions computed from the actual braid words give

    R_(f5^-1) = B^-1 x1 B,
    R_g = B^-1 x1 B x1^-1 B.

The latter is exactly R_(f5^-1) B R_(f5^-1)^-1. Since f1 is B in the genuine fiber homomorphism, this proves that R_g is the actual fiber image of h=f5^-1 f1 f5. Hence conjugation by h^-1 g fixes B, so [h^-1 g,f1] has identity image. The program independently evaluates this complete braid word, avoiding any reliance on an unverified action or antihomomorphism convention.

This derivation arose from an exact collision in the affine boundary orbit. After killing B, the vertices of f0^-1 f2^-1 and f5 agree. That collision alone would only refute the sufficient orbit-injectivity gate. The additional full, unquotiented equality R_g=theta5(h) is the decisive step that produces an actual source relation. No inference from a relation module alone is used.

## 3. Infinite image and exact abstract kernel types

Let

    N5 = ker(theta5) <= F6,
    M5 = ker(theta5-hat) <= F6-hat.

Both are normal and nontrivial, by w0. They have infinite index. Indeed the same exact certificate calculates that the actual braid theta5(f5) has

    ell_(4,5)=1,  ell_(4,6)=0.

Each full twist has value1 under both linking homomorphisms. Their difference therefore descends to PB6/<full twist> = PMod_(0,7), and takes value1 on the spherical image of f5. The image of theta5 in the actual sphere group is consequently infinite; its completed image has an infinite procyclic quotient. This avoids an inference from an unverified torsion or center assertion in the completion.

A nontrivial normal subgroup of infinite index in a finite-rank free group has infinite rank. One elementary proof uses its regular covering of the finite rose. If the subgroup were finitely generated, the cover would have finite core. A nonempty cyclically reduced word in the normal subgroup labels a reduced closed loop at every vertex, by normality. Thus every vertex belongs to the finite core, forcing finite index, a contradiction. Since F6 is countable, its kernel N5 is a free group of exactly countably infinite rank.

For M5, use the exact finite-word theorem already verified from the primary source in B56: Shusterman (2016), Theorem1.2 (Corollary3.7 in the primary preprint), *Free subgroups of finitely generated free profinite groups*, Journal of the London Mathematical Society93(2),361–378, DOI10.1112/jlms/jdw001, primary preprint https://arxiv.org/abs/1501.01227.

The hypotheses are all explicit here:

1. The ambient F6-hat is finitely generated and free profinite, with the six specified geometric meridians as a profinite basis.
2. M5 is closed and has infinite index, by the linking quotient above.
3. M5 contains a closed normal subgroup containing a nontrivial finite word in that basis: take the closed normal closure of w0, contained in M5 by continuity. Its nontriviality is certified by the S3 quotient.

Therefore M5 is a free profinite group of countably infinite rank in the theorem's convergent-basis sense. It is not legitimate to omit hypothesis3 and appeal merely to closed normality and infinite index.

## 4. Scope and remaining comparison

B65 identifies N5 and M5 with the actual joint discrete and completed kernels of all twelve rigid-seven tests restricted to H5. Thus those test families fail to be faithful on the cyclic subgroup, in addition to the previously proved tetrahedral failure in B56.

The conclusion does not assert that M5 equals the closure of N5 in F6-hat. That is a further induced-topology/kernel-closure comparison for the actual image of theta5. Nor is M5 the full profinite completion of the abstract countably generated free group N5: the latter has uncountably many maps to C2 and is not metrizable, whereas M5 is closed in the metrizable F6-hat.

The six exact source braid words still give a terminating membership test for every discrete word: substitute them and evaluate the faithful Artin action. The fixed linking ell_(4,6)=0 removes the full-twist ambiguity in the capped sphere target, both discretely and after completion, as proved in B65. The new relation and rank statements do not by themselves give a finite presentation or normal generating set for the image.

Finally w0 is not an element of the residual centralizer K. It is a nonidentity actual pure mapping class in H5, while the actual pure A5-centralizer is trivial by B7. Residual finiteness preserves its failure to commute with some A5 element. No nonidentity element of K and no equality of the two source lifts in the full ambient completion is constructed here.
