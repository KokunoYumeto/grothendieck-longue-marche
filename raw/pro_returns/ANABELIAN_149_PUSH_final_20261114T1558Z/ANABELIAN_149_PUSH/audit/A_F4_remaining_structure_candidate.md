# Structure and exact prime-primary theta pruning for the remaining F4 pair

**Dated supersession, 2026-11-14:** A.C2.25 now proves A1 for the two classes203/302 by an independently verified complete primitive theta packet at conductor7*31*2503*4519. References below to those cases as undecided describe the earlier stage of this particular method; all46 norm identities and all exact structural/primary obstructions remain valid. See sections/A_F4_all_48.tex and audit/A_F4_all_48_root_review.md.

Status: accepted after independent root and degeneration review and integrated as A.C2.24 in sections/A_F4_remaining_structure.tex. No A1 conclusion is asserted for these two curves. Written14November2026. The historical candidate filename is retained.

## 1. The actual models and their Frobenius polynomial

Let alpha²+alpha+1=0 and

    C0/F4: v²+v=z+alpha²(z+1)/(z²+z+alpha).

The coefficientwise-square conjugate gives the other remaining geometric class. Over F16=F2[w]/(w⁴+w+1), alpha=w²+w, these become the normalized triples(1,9,14) and(1,11,13), where w is encoded2. The change x=z+w, y=v+k with k²+k=w gives the first equality directly.

Exact Artin–Schreier enumeration gives #C0(F4)=7 and #C0(F16)=15. The Jacobian Frobenius polynomial is therefore

    P(X)=X⁴+2X³+X²+8X+16.                   (S.1)

The squared Frobenius polynomial is X⁴−2X³+X²−32X+256; #C0(F256)=255 agrees. The count-to-polynomial formula is the already opened Milne2008 III Theorem11.1/Corollary11.4, together with II Theorem1.1. The curve is ordinary by its three simple Artin–Schreier poles, or by the two independent logarithmic Cartier-fixed differentials in normalized coordinates.

## 2. Geometric simplicity and the rational endomorphism algebra

P is irreducible modulo3: its reduction is the tenth cyclotomic polynomial, irreducible there because3 has multiplicative order4 modulo10. Thus P is irreducible overQ. Let its four roots be alpha_i. The exact resultant Res_X(P(X),P(ZX)), after deletion of(Z−1)^4 and squarefree reduction, has primitive integer polynomial

    64 Z⁸+80 Z⁷+108 Z⁶+7 Z⁵+26 Z⁴+7 Z³+108 Z²+80 Z+64.   (S.2)

Its roots are all nontrivial ratios alpha_i/alpha_j. Their number is at most8: write the Weil roots as a,4/a,b,4/b; the four within-reciprocal-pair ratios occur once, and the four cross ratios occur twice. Direct exact gcd calculations exclude every cyclotomic factor of degree at most8.

The full list to be checked is

    1,2,3,4,5,6,7,8,9,10,12,14,15,16,18,20,24,30.

It is exhaustive: phi(n)≤8 permits only primes2,3,5,7, with exponents at most4,2,1,1 respectively; the remaining finite products give exactly the displayed list. The certificate tests all18 cyclotomic polynomials against(S.2), with gcd1 in every case. Hence no two distinct Frobenius roots have a root-of-unity ratio. For every m>0 the four conjugates of alpha_1^m remain distinct, so its minimal polynomial still has degree4. The characteristic polynomial of Frobenius over every finite extension is irreducible. A positive-dimensional proper abelian subvariety would descend to a finite extension and factor that polynomial, so the Jacobian is geometrically simple.

More precisely, its full geometric rational endomorphism algebra is Q(pi), a quartic CM field. To see this without importing a classification theorem, use the injective integral Tate-module map in Milne2008 I Theorem10.15, printedp.49/PDFp.54, reopened in full at turn741view1. Every geometric endomorphism is defined over a finite extension and commutes with some pi^m. The centralizer of pi^m on the four-dimensional rational Tate module is Q_ell[pi^m]=Q_ell[pi], because pi^m still has degree4 and distinct eigenvalues. Thus the rational endomorphism algebra has dimension at most4 and contains the degree-four field Q(pi); equality follows. No assertion that the integral endomorphism ring is maximal is made.

For an explicit field description, put s=pi+4/pi. Equation(S.1) gives s²+2s−7=0, hence s=−1±2sqrt2. Solving pi²−s pi+4=0 yields

    Q(pi)=Q(sqrt2, sqrt(−7+4sqrt2)).          (S.3)

The conjugate quadratic discriminants multiply to17. This is a non-Galois quartic CM field: if both square roots lay in it, it would contain both sqrt2 and sqrt17, making it the totally real biquadratic field, contrary to the nonreal Weil roots.

Consequently C0 has no nonconstant map to an elliptic curve and no nonconstant map to an abelian variety of two-rank zero, even after extending constants. Any such map induces a nonzero Jacobian quotient; geometric simplicity and ordinariness exclude these respective targets. This blocks direct targets on the original curve, not targets after an admissible étale cover.

Also Aut(C0 over the algebraic closure)=C2. Its three normalized coefficients are distinct, so the coefficient-permutation classification leaves only the identity base map and the hyperelliptic involution. In particular the original curve has no nontrivial odd-order Galois quotient, including no odd-order Galois elliptic quotient.

## 3. Uniform prime-primary packet bounds from the actual F4 Frobenius

Let ell be odd. Choose m with P(X) dividing X^m−1 modulo ell. Then Frobenius^m acts trivially on J[ell], so the genus-two fixed-field theorem A.C2.12 puts every ell-primary theta point in J(F_(4^m)).

Suppose integers e≥1 and a polynomial B(X) of degree at most3 satisfy

    (X^m−1) B(X) = ell^e mod(P(X), ell^(e+1)).   (S.4)

In the actual endomorphism ring this says

    (pi^m−1) B(pi) = ell^e (1+ell R(pi))

for an integral polynomial R (the exact R need not be displayed). On geometric ell-primary torsion,1+ell R(pi) is invertible: its inverse is the convergent ell-adic geometric series, or its finite truncation at each torsion level. It commutes with pi. A pi^m-fixed ell-primary point is therefore killed by ell^e. Thus(S.4) gives a uniform exponent bound on every ell-primary theta point, not merely on observed rational points.

The companion-matrix code finds m by exact factorization modulo ell, and produces B from an adjugate over a sufficiently high finite ell-adic quotient. It then checks(S.4) directly modulo ell^(e+1), so neither a numerical inverse nor an unverified module structure is used. Cayley–Hamilton and faithfulness of the Tate action supply P(pi)=0.

The exact results are:

| ell | splitting exponent m | theta order divides | B coefficients, ascending |
|---:|---:|---:|---|
| 3 | 10 | 3 | [4, 1, 6, 0] |
| 5 | 52 | 5 | [18, 9, 6, 19] |
| 7 | 12 | 7 | [17, 46, 7, 48] |
| 11 | 610 | 11 | [76, 7, 93, 72] |
| 13 | 42 | 13 | [81, 150, 123, 166] |
| 17 | 1224 | 289 | [1121, 4202, 390, 3232] |
| 19 | 180 | 19 | [341, 50, 82, 278] |
| 23 | 132 | 23 | [90, 363, 491, 378] |
| 29 | 11788 | 29 | [425, 801, 273, 143] |
| 31 | 120 | 31 | [379, 567, 530, 11] |
| 37 | 24660 | 37 | [1116, 23, 450, 215] |
| 41 | 140 | 1681 | [66658, 64498, 20991, 27342] |
| 43 | 924 | 43 | [1238, 65, 550, 591] |
| 47 | 23 | 2209 | [68200, 85019, 58876, 86032] |
| 53 | 702 | 53 | [2277, 11, 505, 1824] |
| 59 | 1740 | 59 | [851, 1200, 2335, 1832] |
| 61 | 111660 | 61 | [3236, 2301, 2389, 134] |
| 67 | 2244 | 67 | [201, 915, 1051, 1020] |
| 71 | 1260 | 5041 | [157405, 262215, 277523, 203927] |
| 73 | 1332 | 73 | [4521, 1064, 2697, 1508] |

For ell in

    3,5,7,11,13,19,23,29,31,37,43,53,59,61,67,

the bound is ell itself, and the complete geometric Hankel tests already show theta[ell] empty. Hence the entire ell-primary theta packet is empty for each of these primes. The n31 test is in A_theta_F4_moduli_other_orbits.json, the n43 test is in A_theta_F4_remaining_multi_orbits.json, and the other listed prime tests are in A_theta_F4_moduli_scan.json. This prunes all higher powers of those primes, including169 and343. Separate primary exclusions do not by themselves exclude mixed orders, as the earlier exact15 example demonstrates; Section6 below supplies additional mixed-support certificates.

The bound at7 is particularly sensitive to using the actual Frobenius. Passing first to F16 gives an integral order generated only by pi², and the same sufficient inversion certificate has the weaker bound343. Using pi itself gives m=12 and exponent7, with B=[17,46,7,48] modulo49. No equality of the two integral orders is presumed.

The candidates17²,41²,47²,71² have not been eliminated merely by empty first-level tests. The subsequently completed geometric theta73 calculation is now addressed in Section7: it excludes primitive rank zero for every cyclic73-power cover, without excluding other conductors or A1.

## 4. Reproducibility and limits

code/A_F4_remaining_structure.py/.json supplies exact point counts, the root-ratio resultant/cyclotomic proof, and all actualF4 congruences. It calls the explicit modular certificate routine in code/A_F4_remaining_frobenius_packets.py; the latter's standalone output records the separately labeled squared-Frobenius version. The actualF4 packet data are also retained in code/A_F4_remaining_frobenius_packets_F4.json.

This is structural information about the two undecided classes and a finite list of exact method obstructions. It neither rules out all suitable cyclic covers nor proves or refutes A1 for them. A genuinely new separating cover or another method is still required.

## 5. Why the obvious odd-isogeny transfer from A.C2.13 fails

The quadratic Artin–Schreier twist overF4 of the A.C2.13 curve has the same polynomial(S.1) as C0. Its three hyperelliptic ramification points remain rational. Therefore Frobenius acts trivially on its geometric two-torsion: the three nonzero classes are the differences of the three ramification points.

For C0, Frobenius fixes the point at infinity and exchanges the other two. Its action on J[2] is the corresponding nontrivial transposition. There is one fixed nonzero two-torsion class, whereas all three are fixed for the split-branch comparison curve. Both rational Jacobian groups have orderP(1)=28. Their two-primary subgroups are consequently C4 and C2×C2, respectively.

This difference cannot disappear for a geometric isogeny of odd degree. Indeed for every m the preceding root-ratio calculation gives Q(pi^m)=Q(pi). Hence there is a rational polynomial R_m such that X=R_m(X^m) moduloP(X). Any geometric homomorphism between the two Jacobians is defined over some finite extension and intertwines their m-th Frobenius powers. Applying the same polynomialR_m shows that it intertwines their original fourth-power Frobenius as well. An odd-degree isogeny would induce a Frobenius-equivariant isomorphism on their geometric two-torsion, contradicting the two different actions.

Thus every geometric isogeny between these two isogeny-class members has even degree. This blocks direct transport of the known theta-seven construction through an odd Jacobian isogeny. It does not rule out a new map from an odd étale cover of C0, especially one whose total normal closure is nonabelian.

## 6. Entire mixed-primary packets, not only the first squarefree level

The finite-support fixed-field lemma in A.C2.14 is stronger than the separate prime-primary statement: if a Frobenius power sigma fixes J[ell] for every ell in a finite set S of odd primes, it fixes every theta point whose order is supported on S. Apply this to sigma=pi^m, where m is a common multiple of the exact splitting exponents in Section3. For each ell in S, verify(S.4) at this same m. The ell-primary component of a sigma-fixed theta point is killed by the resulting ell^e. Hence the order of the original point divides N=product(ell^e). A complete empty theta[N] test therefore excludes every S-supported order, with arbitrarily high powers allowed.

The exact certificates and saved complete Hankel tests give:

| prime support S | common m | all S-supported theta orders divide N | complete theta[N] result |
|---|---:|---:|---|
| {3,5} | 260 | 75 | empty |
| {3,7} | 60 | 63 | empty |
| {5,7} | 156 | 35 | empty |
| {3,11} | 610 | 33 | empty |
| {7,11} | 3660 | 77 | empty |

Thus, for either of the two remaining curves, there is no theta torsion of order3^a5^b,3^a7^b,5^a7^b,3^a11^b, or7^a11^b, for any nonnegative exponents. The absence of zero from the ordinary Raynaud theta divisor handles the case where both exponents are zero. The statement for the coefficientwise-square conjugate follows by applying that field automorphism to the whole geometric theta locus.

The reproducible driver is code/A_F4_remaining_mixed_packets.py. It checks all five modular Frobenius identities independently of any claim about a cyclic Frobenius lattice, and links the finite bounds to the already saved complete geometric exclusion outputs. Its adjacent JSON contains the exact four coefficients of every polynomial B and the checked remainder modulo ell^(e+1). It neither reruns nor modifies the long scans. The n33 test is in A_theta_F4_moduli_other_orbits.json; n35 in A_theta_F4_moduli_scan.json; n63 in A_theta_F4_remaining_multi_orbits.json; n75 in A_theta_F4_remaining_75_79.json; and n77 in A_theta_F4_remaining_good_mixed.json.

This excludes these entire abelian theta strategies on the two curves. It does not exclude torsion with another prime support, covers whose total normal closure is nonabelian, or A1 itself. In particular an intermediate-cover construction can still introduce new line bundles not pulled back from the original Jacobian.

## 7. Complete theta73 and all73-power primitive factors

The complete geometric Hankel gcd at73 is T²+6T+9=(T+8)(T+14), in the F16 binary encoding above. The Artin–Schreier constants at its two roots are9 and15, both of absolute trace1 overF16. Thus the full locus has four geometric points, all overF256; sixteenth-power Frobenius exchanges the two points above each coordinate. The full norm witnesses are in code/A_F4_remaining_primitive_packets.json, and the original complete gcd is in code/A_theta_F4_remaining_73_89.json. The former's program independently reconstructs each norm and the cyclic packet by exact divisor arithmetic.

A conceptual argument identifies the entire packet without relying on the Cantor calculation. The actual F4 Frobenius is pi:(x,y)↦(x^4+1,y^4+alpha) in normalized coordinates. Its square acts as the hyperelliptic involution on the four points, hence as−1 on their theta classes. The count polynomial gives #J(F256)=2^7·7·73, so its73-primary group is cyclic of order73 and contains all four theta classes. If eta is one of them and pi eta=k eta, then k²=−1 modulo73, giving k=±27. Since pi exchanges the two coordinates, the full theta packet is exactly{±1,±27}. The order of2 modulo73 is9, and these four multipliers occupy four distinct doubling orbits among eight. The corresponding cover has primitive two-rank36 and total rank38. Every other cyclic73 line is theta-empty and has primitive rank72.

Finally, the ell=73 exponent certificate in Section3 puts every73-primary theta point in J[73]. For a cyclic73^a cover with a≥2, every primitive character has exact order73^a and avoids theta, so its primitive rank is phi(73^a)>0. Hence the primitive-zero method cannot work at any73-power conductor on this pair. This does not exclude another prime support or a nonabelian tower, and no A1 counterexample is supplied.

Independent structural review: audit/A_F4_remaining_structure_degeneration_review.md. Independent arithmetic: code/A_F4_remaining_structure_degeneration.py/.json, PASS for all three counts, all18 cyclotomic exclusions and all30 modular packet identities. Root reopened Milne I10.15 (turn795view0/turn796view0), II2.1 and the Tate-Hom discussion (turn796view2), read the full proof, reran the structural and complete73 drivers, and approved the conceptual73 argument. The End0 proof requires only the tensor injection in I10.15 and does not invoke Tate surjectivity.
