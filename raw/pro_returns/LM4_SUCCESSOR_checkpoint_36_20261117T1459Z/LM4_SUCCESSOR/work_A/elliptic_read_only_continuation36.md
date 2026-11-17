# Exact elliptic continuation preserved after the checkpoint35 pause

This note records the complete conversation-level calculations made while writers were paused, and the scope of their independent reviews. It does not modify any checkpoint35 source. The formal counterparts of the three saved35 proofs are A121–A123. Root's separate A124 contains the new torsion theorem; the actual pure-derived strengthening is separately A125.

## 1. Literal negative-section action on the cubic

In the actual full completion of B1,3, write

\[
K=[Y,X]=\sigma\tau^2\sigma,\quad L=\tau^{-1}\sigma^{-1},\quad
F_b=\phi(\sigma^2,\tau^2),\quad B_u=u(\sigma^2,\tau^2),
\]
\[
W=u(YX^{-1}Y^{-1},K)\,Y\,u(X,K)^{-1},\qquad \Pi_u=LWB_u.
\]

The actual elliptic involution attached to the original negative full-GT pair has

\[
\Theta(\sigma)=F_b\sigma^{-1}F_b^{-1},\qquad
\Theta(\tau)=\tau^{-1},\qquad \Theta(K)=K^{-1}.
\]

The original norm on the two embedded free pairs, with its actual parameter and duality retained, gives

\[
\Theta(W)=K^{-1}W,\qquad \Theta(B_u)=B_uF_b^{-1}.
\]

Consequently

\[
\Theta(\Pi_u)
=\tau F_b\sigma F_b^{-1}K^{-1}WB_uF_b^{-1}
=\tau^{-1}F_b\sigma^{-1}F_b^{-1}WB_uF_b^{-1}.
\]

For the second equality put A=Theta(sigma). Applying Theta to K gives K^{-1}=A tau^{-2}A, so tau A^{-1}K^{-1}=tau^{-1}A. This is a literal group identity with all factors retained.

Equivalently, put

\[
D_b=\Theta(L)K^{-1}L^{-1}
    =\tau^{-1}F_b\sigma^{-1}F_b^{-1}\sigma\tau .
\]

Then

\[
\Theta(\Pi_u)=D_b\Pi_u F_b^{-1}.
\]

The two separately normalized involutions in the external semidirect product are

\[
a_F=F_b^{-1}\Theta=B_u^{-1}\Theta B_u,\qquad
a_D=D_b^{-1}\Theta=(LW)\Theta(LW)^{-1},
\]

and their exact relation is

\[
\Pi_u a_F\Pi_u^{-1}=a_D,\qquad \Pi_u^3=1.
\]

The norm identities also give Theta(F_b)=F_b^{-1} and Theta(D_b)D_b=1. At phi=u=1 these formulas reduce to Theta(Pi0)=Pi0. In general the displayed equation does not identify a_F with a_D, or Theta(Pi_u) with Pi_u. The later torsion theorem constructs a different coherent C2 twist; it does not erase this distinction.

CE independently checked the complete factor order, including the reversed-pair norm for B_u and the simplification using K^{-1}=A tau^{-2}A, during the pause. This is a preserved conversation review, not a claim that a hash-bound source review existed before this note was saved.

## 2. Conditional restriction of the boundary automorphism

The frozen source elliptic_boundary_power_automorphy35.md proves that an endomorphism of the full free profinite group E on X,Y sending [Y,X] to its unit power is an automorphism. Its proof uses a proper actual open subgroup containing the image, the degree-one boundary in its finite once-punctured-torus cover, the nonzero primitive boundary class in the integral and completed abelianizations, and the elementary Hopfian argument.

The further restriction argument, now printed in A123, was independently checked by root, CE and DE during the pause. For the actual candidate, the Y-parity character is preserved and the index-two subgroup V2 is invariant. The original H=Fhat(p,q) is an actual free factor of V2. Under the conditional automorphism eta its image is another free factor and is contained in H, because eta(p)=p^d and eta(q)=u(p,q)^{-1}q^du(p,q). Restrict the free-factor retraction V2 to eta(H) to H, and compose with the inverse of eta on H. This is a surjective endomorphism of finitely generated H, hence injective. The retraction is then injective, forcing eta(H)=H. Its restriction is the original psi_d.

No boundary equality was proved by this argument. The exact equivalence between that equality, the original specified third-cusp equation, and Theta eta=eta c_ell remains the preceding bridge.

## 3. Torsion proof audit and the new derived strengthening

The complete root route was checked during the pause: the actual reduced group is the lift group of S3 on Conf2(T minus 0), its pure subgroup is free rank three by free rank two, and characteristic finite fiber targets supply the required full topology. The actual finite-type cohomology comparisons satisfy the full prime-order completion theorem. Ordinary cellular cochains on the contractible four-dimensional universal cover give a unique fixed vertex for every order-three lift and exclude order two. The eight nonzero three-torsion labels are distinguished by actual torus displacement modulo three. This yields the unique continuous pure transporter, the exact C6 twist, and its nonabelian H1 constancy. The new whole-source receipt for A124 binds those claims to its saved36 bytes.

The proposed additional conclusion that these transporters lie in the actual pure derived subgroup was deliberately withheld from A124 until the actual integral pure abelianization was checked. The complete independent argument is now A125: three explicit intersection tori kill the three meridians in H1 of the actual torus complement, giving Z^4; the three-cycle has two standard rank-two blocks and no fixed vector on Zhat^4. That exact computation, together with the original pure-word evaluations, proves the derived assertion and the entire cyclic H1 statement. It does not evaluate the remaining C2 class.

## 4. Exact next based comparison

The torsion equation always has the literal form

\[
\Pi_u=p_u\Pi_0p_u^{-1},\qquad
WB_u=(L^{-1}p_uL)\,Y\,p_u^{-1}.
\]

A forget-one-strand map is defined on the actual pure group. Its interaction with conjugation by L includes the actual permutation and based braid whiskers. Those maps must be derived explicitly before the displayed equation is projected; no unbased cyclic replacement, disappearance of a Brunnian kernel, or equality of the resulting elliptic boundary word is asserted here.
