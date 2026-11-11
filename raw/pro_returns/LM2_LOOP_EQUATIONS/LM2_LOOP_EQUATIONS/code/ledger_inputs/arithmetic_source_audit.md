# Arithmetic contribution audit

| Task | Statements | Outcome |
|---|---|---|
| Item 3, signs | C.a1–C.a3 | proved, with the uniform 2-adic square criterion refuted |
| Item 3, characterization | C.a12–C.a13 | proved in the stated stronger correct form using additional data |
| Item 5 | C.a4–C.a11 | proved; nonexistence doubt refuted and found withdrawn |
| C(c) | C.a1–C.a3 | proved for ε2, ε3, ε′, ε″ and their product |
| C(e) | C.a12–C.a13 | proved with exact extra-data and conjugacy qualifications |
| C(f) | C.a4–C.a7 | proved: faithful on H and P; centralizers C2 and1 |
| C(g) | C.a8, C.a10 | proved: H2 obstruction, H1 torsor, four realized geometric lifts |
| C(h) | C.a9–C.a11 | proved for fixed tautological gerbe lift; no section conjecture needed |
| Recent results ask3, arithmetic scope | C.a14 | proved limitations; signs trivial on λ=1 |

## Primary material opened

Read the checked LM_P051–053 passages around scans502–530, the LM_C3-150-168 formulas around scans152–168, and the indicated companion passages. Visually inspected scans140-2/522,523,524 and140-3/155. Scans527–530 are **not** in the supplied image set: their continuation was read from the checked transcription only, explicitly distinguished from scan inspection.

Opened attached primary papers: Belyi English (Lemma1 and Corollary; Theorem4 and Corollary), Hoshi–Mochizuki2011 (Corollaries6.3–6.5 and proofs), Minamide–Nakamura version2 (TheoremsA,B,1.1,4.3; CorollaryC; sections3–4), Pop2018 (Definition/Remark2.2, HypothesisH, Theorems2.6,2.7 and examples), Hoshi–Mochizuki–Tsujimura2025 (TheoremsA–C and5.17; Definition5.12; proof reduction), Schneps survey1.4(1),(4). Opened LM3 D/E and bibliography as leads, then replaced the needed claims by direct derivations from the primary sources.

Three web tool requests returned HTTP503, including both search engines and direct primary-source openings. No reference is marked verified based on those failures. The attached primary texts suffice for the claims actually imported here.

## Main corrections

1. The doubt at scan524 is withdrawn at527–528 in the same attached package. The Legendre family supplies the required lift; all four geometric choices arise overQ by twists λ^e(λ−1)^f. The full arithmetic ambiguity is Q*/Q*², not just four elements.
2. The fixed-gerbe converse is elementary through μ2-torsors, and does not need a modular section conjecture or the unattached proof family019.
3. HM2011 Cor6.4 concerns arithmetic action on a fiber group modulo geometric monodromy. A separate proof is required for Out(SL2Zhat); the contribution supplies one. Its arithmetic centralizer is C2, not trivial: the central transvection h↦(−I)^η(h)h survives.
4. Minamide–Nakamura's theorem explicitly starts at four strands. Substitution n=3 is invalid. We avoid needing that substitution.
5. ε2 is the conductor4 character, not the indicator of all 2-adic unit squares:5 is the finite counterexample modulo8. ε3 is conductor3. Both signs already follow from the displayed norm equations, so class field theory interprets rather than strengthens them.
6. Scan522 formula(34) has an impossible SL2(Z/2)/±1 in the middle where SL2(Z)/±1 is needed. Image inspected; corrected mathematics given without declaring handwriting settled.
7. Pop gives an exact criterion on an infinite category of divisor complements in a surface, even with three designated functions. HMT gives a GT-conjugacy class via maximal AA subgroups, not a canonical embedding or a pair of finite equations.

## Computation actually run

`code/arithmetic_checks.py` with output `.out` and structured `.json`:

- Exhaustive unit norm residues modulo4 and3.
- Complete signs modulo12, and the modulo8 square counterexample.
- Symbolic conjugation matrix identity and Legendre discriminant.
- Symbolic rejection of the five nonidentity anharmonic maps in the Pop hypothesis check.
- Central transvection verified on every element and generators of SL2(Z/n) for n=2,4,6,8,12,24; every possible inner conjugator tested. It is noninner at every tested n≥4.
- Four complements in the modulo4 image of Γ(2), each of order4; common intersection identity and index8 in that image.

## What is not claimed

No full proof of HM, Pop, HMT or Belyi is reconstructed. Their exact statements are cited and their applicability and the deductions needed here are proved. No current classification of all torsion in the profinite GT group has been verified: the attached Schneps survey only gives the multiplier-one lower-central argument, and its older scope is preserved. No theorem about all arbitrary modular sections is inferred from the fixed-gerbe lifting argument. The characteristic2 level-two family is outside the construction; characteristic3 is included over Z[1/2].

## Additional finite audit, completed on parent request

- **B.s4.1:** `arithmetic_s4.py` computes the universal S4 envelope independently by a108-state Schreier transversal, not an assumed simple-group formula or a large-group order oracle. Its V4^9 kernel has rank12, hence order442368; its quotient fixed space has dimension0; N/H has order2. The code prints a nontrivial normalizer tuple and actual conjugators in H proving multiplier-one membership. Finite GT(S4)=GT1(S4)=C2 and the Galois image fills it via the S3 quotient.
- Verified the S3 field proof: the three rational regular covers exhaust S3 generating-pair classes, their quadratic square classes multiply to3, and geometric order108 plus ambient bound216 forces exact constants Q(sqrt3). Ambient centralizer is trivial, so the quotient acts noninner. Complex conjugation fixes this real quadratic constant field, hence acts trivially at this quotient.
- **B.s4.2:** inspected Guillot's actual Proposition4.3, Lemmas4.5–4.7, Theorem4.9 and Lemma4.10. The simple-group theorem applies to A5 and PSL2F7, never S4. Reimplemented exhaustive automorphism checks for both groups in `arithmetic_simple_audit.py`; output orders120 and336, hence Out orders2, verifies the specified outer involutions and every power-class kernel.
- Important logical qualification: rational conjugacy classes in S4 alone do not imply x^k andx conjugate *inside the proper envelope subgroup* H. The extra exact conjugacy calculation is supplied. The finiteGT upper bound already follows without that inference, because coordinate colors are preserved.
- The PSL2F7 figure1024 remains a finite-shadow upper bound; cyclotomic surjectivity realizes the quotient of order2 but does not establish arithmetic surjectivity onto the kernel of order512.

## Full linear modular lift, completed on parent request

**C.a15–C.a16** (`sections/C_SL_lift.tex`) close the gap between the projective congruence action in C.d1 and a genuine action on SL2(Z)^. For P=C2 profinite-free-product C3 and H=SL2(Z)^, every peripheral automorphism with multiplierμ has two central lifts. The one sending the order-four and order-six generators to conjugates of their μth powers has cusp image exactly T^μ: H_ab=C12 with S_ab=3T,R_ab=−2T excludes the alternative −T^μ. Thus this lift is unique with the full cusp specified, composes functorially, and is the arithmetic lift on Galois. The ratio between its linear congruence map and conjugation by C.d1's matrix is a C2-character of H; agreement on the cusp generator forces that character to vanish. Consequently GT0 preserves fullSL congruence kernels, and Galois,GT andGT0 have the same finite outer congruence image, units modulo squares. Code output records all four multiplier classes modulo12 and the distinct alternative-lift cusp images.

The standalone LuaLaTeX parse of C_arithmetic+B_s4 reached all ten pages without a source-syntax error after a local format was built; PDF embedding then failed only because the test font map lacked eufm10. The parent is handling final font configuration and render QA; no standalone test PDF is a deliverable.
