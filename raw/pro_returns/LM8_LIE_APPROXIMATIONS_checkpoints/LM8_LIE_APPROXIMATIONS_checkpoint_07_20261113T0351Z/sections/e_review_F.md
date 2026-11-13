# Independent review of F.2 and F.4

The formulas in F.2 and F.4 pass the mathematical review, subject to the citation and comparison details below.

## F.2: exact Selmer dimensions

The attached Hain–Matsumoto source and the final published paper put constrained weighted completion in §§9.3–9.4, not §10. The directly applicable result is Proposition 9.6, proved from Proposition 9.3, Theorem 9.5 and the degree-at-least-two Galois H² vanishing. The general generator ranks are in Theorem 7.2. For Q, after excluding the prime p from S and imposing crystallinity at p, there are |S| generators of Tate degree one, one in every odd degree at least three, and none in positive even degrees. Theorem 7.3 is the unconstrained S={p} case; Theorem 8.4 and Lemma 8.5 concern the outer geometric action.

The step from this free constrained Galois Lie algebra to the claimed dimension equality is valid. All weights in Lie U are negative. A cocycle on the reductive G_m can therefore be uniquely killed by U-conjugation: H¹(G_m,U)=1 and U^{G_m}=1. A resulting homogeneous Lie section to Lie U ⋊ u_Gal is freely specified by the Lie U component of the image of each homogeneous free generator of u_Gal. Nontrivial Galois action on U does not impose additional relations because the source Lie algebra is free. This produces the indicated affine parameter scheme, not only an upper bound.

For the etale Selmer interpretation, spell out the Tannakian comparison: a U-torsor with the prescribed unramified and crystalline conditions has its finite coordinate subquotients in the constrained weighted representation category, and conversely. Crystallinity is equivalent to triviality after B_cris extension; the coordinate algebra comparison is therefore compatible with the nonabelian torsor definition. No equality with the entire motivic or Grothendieck–Teichmüller automorphism group is needed.

The based geometric action must also lie in that constrained category. Hain–Matsumoto Theorem 9.8 states crystallinity of the outer action only. In this tripod case the unit tangential action is the canonical Belyi normalization x↦x^χ, y↦f^{-1}y^χf with f in the commutator subgroup. The normalized algebraic section of the peripheral outer automorphism group supplies the based factorization. This should be stated or replaced by an explicit tangential crystalline comparison theorem; the outer theorem by itself is insufficient.

The local formula follows because each Tate graded piece has negative Hodge degree and Frobenius eigenvalue different from 1. Thus F⁰ is trivial and the crystalline torsor variety is U_dR/F⁰. The free metabelian ranks j−1 in degree j≥2, and hence the two metabelian formulas, are correct.

## F.4: unrestricted cohomology and cusp collision

The inverse-limit Kummer formulas are correct. The invariant root groups are finite, so their inverse system is Mittag–Leffler. Tensoring the integral p-adic cohomology with Q_p gives the full continuous Q_p(1) cohomology: every continuous cocycle has bounded image, while a coboundary that becomes trivial after tensoring is killed by a common power of p.

The explicit family description correctly includes infinitely ramified classes: the coordinates a_q must be zero modulo each fixed power at all but finitely many primes, but need not have finite support. For example coefficients p^n on a sequence of distinct primes give a class whose finite reductions have finite ramification while the full class has infinite ramification.

Define the notation widehat(Q×)^p as the **power completion** lim_n Q×/(Q×)^{p^n}. Since Q× has infinite rank, this must not be confused with the maximal pro-p completion indexed by all finite p-group quotients. The corresponding restricted family space is not asserted to be compact.

At the unit tangent in the parameter z at 0, the regularized values of (z,1−z) are (1,1). At the unit tangent in the parameter 1−z at 1 they are again (1,1). Both Kummer classes therefore vanish in the full profinite abelian section set, including its 2-primary part. The parameter sign is essential: replacing 1−z by z−1 with the same coordinate unit would introduce the Kummer class of −1. The stated choice is correct.

## Primary sources inspected

- Hain, R., & Matsumoto, M. (2003). *Weighted completion of Galois groups and Galois actions on the fundamental group of P¹−{0,1,∞}*. Compositio Mathematica, 139(2), 119–167. DOI: 10.1023/B:COMP.0000005077.42732.93. **Verified:** attached arXiv v2 source, and final publisher PDF, especially pp. 144 and 154–157, Theorem 7.2, Proposition 9.3, Theorem 9.5, Proposition 9.6, Theorem 9.8.
  https://www.cambridge.org/core/services/aop-cambridge-core/content/view/94239BA21D3B20D154B3D024CB3C8996/S0010437X03100693a.pdf/weighted-completion-of-galois-groups-and-galois-actions-on-the-fundamental-group-of-p1-01-infinity.pdf
- Deligne, P., & Goncharov, A. B. (2005). *Groupes fondamentaux motiviques de Tate mixte*. Annales scientifiques de l’École Normale Supérieure, 38(1), 1–56. DOI: 10.1016/j.ansens.2004.11.001. **Verified:** final PDF opened; the tangential groupoid construction and normalization in §§5.3–5.4, 5.7–5.16 were inspected. This source is not substituted for the constrained etale completion theorem.
  https://www.numdam.org/article/ASENS_2005_4_38_1_1_0.pdf
