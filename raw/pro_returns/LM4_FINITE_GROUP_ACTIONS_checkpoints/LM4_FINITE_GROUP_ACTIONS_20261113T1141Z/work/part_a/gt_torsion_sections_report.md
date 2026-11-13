# D.28: prime-order sections and exact fixed-subgroup comparison

The full proof is in `gt_torsion_sections.tex`. Its input is a homomorphism from C_p to the actual full profinite GT_0 whose p-adic multiplier is one, which includes every odd prime p. The normalized GT_0 representation is itself a homomorphism into Aut(Fhat2), so the semidirect product used here has the given order-p action without an additional lifting assumption.

The three cusp normalizer extensions split. This is proved through the exact map E → F2^(p) × C_p, then an explicit coordinatewise solution of the cyclic norm equation. At the prime p the required exponent is divisible by p because of that quotient map; at another prime the norm is either p, a unit, or zero with a necessarily zero target exponent.

The profinite Brown theorem gives the finite equality

    sum over section classes (1 + dim H1(fixed subgroup,F_p)) = dim H^n(E,F_p) <= 3.

Each cusp section contributes at least two because its fixed subgroup contains the p-primary component of a primitive cusp and a nonzero restricted homology functional detects it. Thus all cusp sections are conjugate. Two independent cusp classes then force that one fixed subgroup to have first cohomology dimension at least two, exhausting the bound. There are no other section classes. The actual closed fixed subgroup C is projective and its maximal pro-p quotient has rank two. Its map to F2^(p) is onto by the two independent cusp images and hence is an isomorphism. This section establishes the maximal pro-p comparison. D.32 then applies the three-cusp finite-cover rank argument to this exact subgroup and proves C=Fhat2. Thus every homomorphism C_p to full GT_0 covered by D.28 is trivial; in particular all odd-prime torsion is excluded.

The need for D.32's third-cusp hypothesis is demonstrated by an actual order-three automorphism. Let u be one in every prime coordinate except seven and a primitive cube root at seven. The substitution beta(x)=x^u, beta(y)=y^u has order three and a proper fixed subgroup, but the same Brown argument gives C_beta^(3) ≅ F2^(3). The missing third cusp is explicitly detected in the order-fourteen dihedral group: x=s, y=sr, and u=9 modulo14 give x^u y^u=r while (xy)^u=r^2, which are not conjugate. This is a proved obstruction to using the maximal pro-p quotient to identify the full fixed subgroup.

## Executed finite checks

`code/gt_torsion_sections.py` checks the norm-image equality at all six moduli 2*3^k*7^j with 1≤k≤3 and 1≤j≤2. It also constructs the order-fourteen dihedral quotient, checks all 14^3 associativity instances, computes the full conjugacy class of r, and verifies the displayed nonconjugacy. Output is in `code/gt_torsion_sections_output.json` and the captured stdout file. These computations certify the finite arithmetic and the failed diagonal-power candidate; the full section theorem is proved in the TeX argument.

## Primary source audit

Dessislava H. Kochloukova and Pavel A. Zalesskii, *Automorphisms of pro-p groups of finite virtual cohomological dimension*, Quarterly Journal of Mathematics 58(1) (2007), 47–51, DOI 10.1093/qmath/hal018. The complete seven-page author manuscript at https://mat.unb.br/~pz/arquivos/Claus3.pdf was opened and Theorem2, Section1.1, equations(1)–(6), manuscript pages3–4, were checked. Its main restriction formula is explicitly for profinite groups. Publisher metadata was independently opened. The corresponding bibliography entry preserves the author-manuscript numbering.

The further statement about torsion multipliers in Leila Schneps's older GT survey is only an unproved parenthetical in Section1.4(4), printed page190, in the source inspected. No proof or cited result there establishes the multiplier restriction for full GT_0, so D.28 does not import it. D.34 and D.42 now prove the relevant global multiplier restrictions by the explicit cover arguments in this paper, independently of that parenthetical.
