# Nonconstant literal-relative endomorphism of the full small étale topos

Status: independently reviewed by root and promoted to F.17 (Refuted, for the literal assertion). This addresses literal R27/F2 only, not the corrected closed-point-preserving problem.

Let k have characteristic zero, X = Gm,k with coordinate t, Z = {t=1}, U = X minus Z, and T = Spec(O^h_{X,1}). Write j:U→X and i:Z→X. Let K_h be the fraction field of T, D=G_{K_h}, I its inertia group, so D/I=G_k.

The coordinate u=t−1 induces Spec(K_h)→Gm,u. The homomorphism D→π1(Gm,u) is an isomorphism: it is identity on G_k, and on geometric kernels it is the Kummer isomorphism I=Zhat(1)→Zhat(1). All ramification of a strict henselian equal-characteristic-zero trait is tame. Let E=π1(U); the morphism u:U→Gm gives E→π1(Gm)≅D. It defines a geometric morphism q:U_et→BD with the specified relative structure over BG_k. On the local decomposition group at 1 the composite is the identity D→D.

For every continuous discrete D-set B, the stalk calculation for j_* gives a canonical G_k-equivariant isomorphism

    i* j* q*(B) ≅ B^I.

Indeed its geometric stalk is the invariants under the fundamental group of the punctured strict henselization at 1; the preceding local decomposition map identifies this action with I. The residual G_k action also agrees. This works for every D-set, not merely finite sets: each D-set is a disjoint union of finite orbits, and the punctured strict henselian trait is connected. Equivalently calculate sections directly as equivariant maps from its geometric fibre functor.

Grothendieck/Artin gluing identifies X_et with triples (A,C,v), A∈BG_k, C∈U_et, v:A→i*j*C. It identifies T_et with triples (A,B,v), A∈BG_k, B∈BD, v:A→B^I. Define

    Φ*(A,B,v) = (A,q*B, A→B^I ≅ i*j*q*B).

This is a functor on the full topoi. Finite limits and all colimits of the triple categories are computed on the A and B/C components; the connecting maps are induced by the gluing functors. Hence Φ* preserves finite limits and all colimits. A right adjoint can also be written explicitly: for (A',C,v') in X_et, put B=q_*C, use the natural map B^I≅i*j*q*q_*C→i*j*C, and take A=A'×_{i*j*C}B^I. The resulting triple (A,B,A→B^I) is Φ_*(A',C,v'). Therefore Φ*:T_et→X_et is the inverse image of a geometric morphism Φ:X_et→T_et. The constructions commute with the structural inverse image from BG_k, so Φ is relative with its commutation isomorphism.

Compose with T_et→X_et. The generic open of T pulls back to U, and the closed stratum pulls back to Z, with identity on BG_k. Thus the resulting endomorphism Ψ has point map

    Ψ(1)=1;  Ψ(x)=the generic point for every x≠1.

It is nonconstant on underlying points. It is not induced by an algebraic k-morphism: the closed rational point 2 maps to the generic point. In particular it is not closed-point preserving. Since X is smooth, absolute weak normalization makes no change.

Primary sources opened: Cornut, Morphing etale spaces (arXiv:2412.07358, 2024), author-hosted PDF https://webusers.imj-prg.fr/~christophe.cornut/papers/MorphES.pdf, introduction pp.1–2. It states the full sheaf triple equivalence, cites SGA4 IV9.5, and gives precisely the henselian-DVR D-set/inertia description. The original SGA4 IV scan from Orgogozo's CNRS page returned 502/503 and was not represented as opened. Cornut's primary author-hosted paper was opened directly and independently by root. No restricted finite-cover functor is passed off as the full topos.
