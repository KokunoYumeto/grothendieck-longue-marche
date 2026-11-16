# Discrete mixed conjugates have trivial intersection

Proposed geometric lemma for the actual ambient group Γ=Γ_0,[12].

    H_T ∩ g H_5 g^{-1} = 1 for every g∈Γ.

Here H_T=C_P(T), H_5=C_P(D), T=A4 acts regularly on the twelve
marks, and D=C5 is the fixed cyclic action of B28. This strengthens
the discrete intersection at g=1. It does not assert the corresponding
identity for profinite conjugators or closures.

## Proof

Suppose h is a nonidentity element of the intersection. It is pure and
commutes with both T and D'=gDg^{-1}.

The cyclic covering quotient is a four-punctured sphere: two punctures
are the two fixed poles, and two are the free orbits of five marks.
The pure cyclic centralizer is a finite-index free subgroup of its pure
four-point mapping-class group. The quotient monodromy is faithful on
H5, as in B28. A nonidentity pure four-point mapping class is either
pseudo-Anosov or a nonzero power of a peripheral Dehn twist.

If it is pseudo-Anosov, its lift is pseudo-Anosov. All ramification
points are marked in this cyclic cover, so the pulled-back invariant
measured foliations give the required pseudo-Anosov representative
directly on the twelve-punctured surface. This type is unchanged by g.

If it is peripheral, a nonzero power of its lift is a multitwist.
There are two topological types in the actual H5 family. At u=0 or∞,
one fixed pole and a free orbit of five marks coalesce, giving one
essential curve separating six marks from six marks. At u∈μ5 there
are five disjoint two-point collisions, giving five essential curves.
All displayed twist coefficients are nonzero. Thus its canonical
reduction system has either one or five components; the same is true
after taking a nonzero power or conjugating by g.

In this reducible case T acts on that finite canonical reduction system.
Every action of A4 on one or five objects has a fixed object: possible
nontrivial transitive orbit sizes dividing five are3 and4, and an orbit
of size2 is impossible because A4 has no index-two subgroup. A curve
fixed by T has two complementary disks. Their permutation defines a
homomorphism T→C2, which is trivial. Each side would therefore contain
a T-invariant proper nonempty subset of the twelve marks. This
contradicts the transitivity of the given T action. The reducible case
is impossible.

In the pseudo-Anosov case, its centralizer acts on the two invariant
measured foliations by positive reciprocal scale factors. The scale
homomorphism has finite kernel. To recall the precise reason, choose
the canonical foliation-preserving representatives: an element of
scale1 which fixes a separatrix fixes that dense leaf pointwise and
therefore is the identity. The kernel acts freely on the finite set
of separatrices, so is finite. This is the finite-kernel part of
McCarthy's proof, Lemmas2–4, and works with marked singularities as
well as ordinary singularities. Every finite subgroup of the
centralizer maps trivially to the positive scale group. Hence both
T and D' lie in one finite subgroup E of Γ.

By Nielsen realization and the finite rotation-group classification
on the sphere, a finite subgroup containing A4 and an element of
order5 must be A5: cyclic and dihedral groups contain no A4, A4 has
no5-element, and S4 has no5-element. The twelve marks then form its
unique exceptional orbit of size12. B7/B52's discrete quotient
triangle argument gives C_Γ(E)=1. But h centralizes E, a contradiction.

This proves the displayed identity for every discrete g.

## Sources and scope

John D. McCarthy, *Normalizers and centralizers of pseudo-Anosov mapping
classes*, original manuscript5 March1982, revised8 June1994, primary
author copy:
https://users.math.msu.edu/users/mccarthy/publications/normcent.pdf

Theorem1 and especially the scale homomorphism, finite symmetry kernel,
and faithful representative argument in Lemmas2–4 were opened and read
directly. The primary introduction states the compact negative-Euler
characteristic case. The proof above spells out the punctured-surface
adaptation actually needed here; it does not silently replace that
stated scope. The finite sphere-group and twelve-point realization
inputs are the already checked B7/B52 sources.

No conclusion of profinite malnormality is inferred. Nor is either H_T
or H5 claimed individually malnormal; their peripheral multitwists have
large centralizers in the ambient group. General hyperbolic or relatively
hyperbolic product-separability theorems have not been applied to Γ,
which is not supplied with an appropriate ambient structure here.
