# Independent audits performed after Part A

## D.15–D.18

The comparison through the elliptic moduli stack was checked with the central scalar quotient retained. The rigidification by the global involution removes quadratic twists. At the fixed Legendre parameters, the displayed coordinate changes give the indicated quadratic twists of the rational CM curves; the rational level-two structures fix their descent. No full-torsion-field equality before the stated scalar quotient was used.

For D.16, the projective torsion field over each CM field contains the Weber-value field, hence its maximal abelian extension, and the commuting CM linear representation gives the reverse containment. The index-two joint-image argument was checked through the common biquadratic quotient and the explicit dihedral field Q(i, fourth-root(3)). The class-field and CM theorems are supplied with opened source evidence by the Part D author.

For D.17, the local image tables in `d_local_cm.py` and its saved output agree with the claimed index two at 2 and 3 after the first relevant layers. The valuation-parity obstruction and the lifting of unit norm classes were checked against the exact local fields used.

D.18 initially left an upper-unipotent change of basis possible: replacing a basis by U(b) changes the upper-right coordinate by b(1−chi). This was reported to the author. The final proof fixes compatible positive real Tate roots and the period ratio on the real interval, and now removes that ambiguity. The formal Tate-series base change was also added. In that specified basis, q=lambda²/256 times a formal unit with constant coefficient1 gives the coefficient −8 kappa_2. Conjugation by diag(−1,1) gives the opposite sign in the manuscript's opposite-loop basis.

## E.22

The combination with A.19 was checked. The minimum-approximation arithmetic image of G_Qcyc is abelian, so actual commutators are killed. The actual graded Galois classes supplied in E.3 can be moved into G_Qcyc by taking their commutators with an element having chi_l=1+l; the nonzero rational leading classes remain nonzero. Their mutual commutator has the displayed nonzero weight-eight outer class. The characteristic maximal-unipotent quotient of the relative completion gives the required map on outer automorphism groups, so the non-descent conclusion follows.

## Cubic abelian section computation

The primary source was opened directly:

- Mirela Çiperiani and Jakob Stix, *Weil–Châtelet divisible elements in Tate–Shafarevich groups I: The Bashmakov problem for elliptic curves over Q*, https://web.ma.utexas.edu/users/mirela/CiperianiStix-BashmakovDivSha.pdf .
- Theorem18(2), printed page18, PDF page index17, states that an elliptic curve over Q of analytic rank zero has maximal divisible Weil–Châtelet subgroup isomorphic to Q/Z. The restrictions on good primes and irreducibility apply to the additional direct-sum assertion involving Sha, not to this isomorphism.
- Section1.4.2, printed page4, distinguishes the maximal divisible subgroup `Div` from the intersection of all multiples `div`. The deduction uses `Div` throughout.

For the generalized Jacobian extension by the quasi-trivial torus, H¹(Q,T)=0 makes its H¹ inject into the elliptic H¹. The extension class is killed by3, so its connecting homomorphism is killed by3. It vanishes on the whole maximal divisible subgroup by internal 3-divisibility. This proves equality of the maximal divisible subgroups, not merely the inclusion of individually divisible elements.

For the Kummer inverse limit, the quotient transition maps on G(Q)/m are surjective. Their first derived inverse limit therefore vanishes along the factorial cofinal sequence. The finite groups H⁰(Q,G[m]) also have vanishing first derived inverse limit, giving the comparison with continuous H¹ of the full Tate module. The final term is Hom(Q/Z,H¹(Q,G)), hence Zhat. A lift of1 supplies a continuous Zhat-linear splitting. The completion of the countable free abelian group is explicitly the group of sequences in a product of Zhat that tend to0 modulo every integer, rather than the unrestricted product.

The later toric projection was checked as an actual algebraic group morphism. With the stated cusp frame its restriction is (a N(A)/N(C), b N(B)/N(C)); its section is (a,b) mapped to (a,b,1,1,1). The kernel torus is parametrized by (A,B,C) mapped to (N(C)/N(A),N(C)/N(B),A,B,C). The displayed frame relation has toric image (1,−1), and subtracting the section of this point gives exactly the claimed kernel relation. Its first lambda valuation is−1, so it removes a free generator without changing the finite unit torsion. The author was asked to retain the affine basepoint translation by the Kummer class of (1,−1), and to distinguish the inclusion U_3 into the torus from the covering map, whose group homomorphism is multiplication by3 after this projection.

## E.26

The additional class-two splitting proof and complete finite enumeration were supplied in `sections/E_splitting.tex` and `code/e_splitting.py`. This is a direct group calculation, with no appeal to an unverified reference. Its integral and rational coefficient comparisons and the failure of the permutation swap to preserve the marked-depth ideal are explicit.

## E.28 and E.31

The inherited cubic lattice has generators A=3X, B=3Y, C=[X,Y], so its commutator coefficient is9. At Q_109 the coefficient-mod27 action is trivial, and the Kummer pair(6,109) has Frobenius and tame-inertia vectors(1,0),(0,1). All central choices have commutator9C, contradicting the tame relation in the exponent27 quotient. The exact map from the intrinsic class-two group to this inherited quotient was checked; it also kills the intrinsic metabelian and stated marked-depth kernels. The Puiseux map t=s^3 fixes the ramified tangent comparison and the factor3 in the two coordinate maps.

For E.31 the unit-frame element t=(7,7,1,1,3+zeta) has minimum pro-3 toric image zero. The actual rational function h=(x+y)/(x+zeta y) has the displayed divisors, and the frame at the conjugate cusp is the conjugate of3+zeta. At the chosen O tangent its leading factor is zeta/lambda^3, retaining the Kummer translation by zeta. The target mod3 toric pair is therefore(kappa_zeta,kappa_7). At the prime3+zeta, zeta reduces to4 inF7, and the Frobenius/tame values are2,1. The class-two exponent3 Heisenberg quotient has commutator2C for every central lift, contradicting the tame exponent7 relation. The arithmetic based-path change and its affine origin were explicitly requested and retained. The comparison kills gamma3 and the second derived subgroup without requiring surjectivity of the induced curve map.

The independent program `code/a_cubic_audit.py` checks these finite groups, all729 central choices for E.28, all9 central choices for E.31, and the Eisenstein-integer identities used by the intrinsic witness.

## E.29 and E.32

The rational-pair proof was supplied as E.29, with the source anchor corrected to section51.16, scans172--178, folios733v--736v, equations371--379. The root independently audited the central factor9, the integral Steinberg argument, the tame-symbol injection, and the threefold central fibre.

The full completed-pair proof was supplied as E.32. The Part B/C author independently read its complete proof and opened the relevant Milne and Jannsen sources. The audit checked the order of direct and derived inverse limits, the exact restricted-sequence support complex, the chain-level Frobenius defect and its coboundary sign, and the explicit completed Kummer pair with a nonzero inverse-limit obstruction despite zero finite and local obstructions. No gap was found.

## E.33

The continuous unipotent completion and its transition maps were independently checked. Compact unipotent images at primes away from ell kill wild inertia; the tame relation gives Ad(F)N=qN, and the unipotence of Ad(F) forces N=0. Thus every such representation factors through the group unramified outside ell. The finite-coefficient Euler characteristic, Leopoldt for abelian number fields, and bounded orders of the second cohomology groups give vanishing after tensoring with Q_ell, with the finite first cohomology groups supplying the required inverse-limit comparison. The central-extension argument gives the injection from unipotent-completion H² into continuous Galois H², and the least-degree relation argument proves freeness.

Sharifi's author notes, https://math.ucla.edu/~sharifi/notes/iwasawa-ch01.html , were opened at Theorems1.5.7, 1.5.17 and 1.5.21. These give the rank formula, Brumer's linear-independence input, and its application to abelian fields. For a CM cyclotomic field the logarithms of units span precisely the conjugation-even trace-zero subspace; the displayed trace and odd-projection map therefore gives the asserted quotient. Local reciprocity identifies the actual transition with norm, hence with trace on logarithms. The degree multiplier on the scalar factor, surjectivity of trace, and compatible free-generator construction were checked. A clarification concerning a continuous set-theoretic section in the central-extension argument was sent to the author.

## E.34

Hain--Matsumoto, https://arxiv.org/pdf/math/0006158 , section8.5, PDF page27 (printed page28), was opened directly: the based pro-ell action with the specified tangent is unramified outside ell. The actual cubic Puiseux tangent restriction therefore supplies the claimed unramified based action. Over Q(zeta3), the IA automorphism group is pro3, so the action and every abelian cocycle factor through the maximal pro3 group. Kummer theory gives two generators, and the finite-coefficient Euler characteristic gives H²=0. The inflation injection and the resulting free pro3 presentation were checked, including the minimal-generator pullback needed in the embedding argument.

The semidirect product with C2 has 3-cohomological dimension one. Solvability of the finite embedding problems and compactness of the finite sets of sections then lift every unramified abelian class to the full intrinsic pro3 kernel. The complex-conjugation ranks, fixed torsion, Euler characteristic and finite generation give Z3^6 plus C3^3, and the actual split toric morphism gives the stated image and kernel. No gap was found.

## D.24 and D.25

For D.24 the product quotient to the metabelian group and A5 is surjective by the explicit absence of a common quotient. The outer automorphism of A5 exchanges its two classes of 5-cycles, so a lift acting trivially on the whole metabelian quotient fails the indicated peripheral condition. The precise unrestricted lifting result was opened in Bleher--Chinburg--Lubotzky, https://arxiv.org/pdf/2004.08860 , Lemma2.3 and Corollary2.4, printed page5 / PDF index4. The argument makes no assertion that all lifts of a given metabelian action fail the peripheral condition.

For D.25 the full E3 four-torsion field and the projective E4 three-torsion field were checked as Q(i,r), r^4=3/4. The recovery of the global sign from the rational point of order3 gives the exact map from projective level12 to the full four-torsion representation. The Bass--Serre chain model has 576 edges, 480 vertices and cycle rank97. The saved linear calculations modulo2 and3 have the displayed ranks and centralizer reductions. The conjugator correction by x^(b-a) gives a commutator-valued f, preserves the two CM invariants and the fixed cusp, and supplies the two finite hexagon equations. The surviving twelve extra CM-coset actions are actual nonarithmetical finite shadows; their genuine full-profinite lift is not supplied by this calculation. No gap was found in the finite result.

## E.35

Milne's author text, https://www.jmilne.org/math/CourseNotes/CFT.pdf , IV.3.14, printed page137 / PDF index145, was opened directly. The formal punctured-disc tangent gives the pure-x Kummer homomorphism q_g, and the displayed arithmetic isomorphism (n,g) to (n q_g,g) was checked with its inverse and its identity restriction on the geometric group. The factor-set calculation, alternating-cup coboundary sign, cyclic-algebra norm criterion and explicit norm polynomial agree.

The degree27 construction was checked on all displayed generators. The argument excluding gamma from L_A(beta) uses the independence of the two cube classes and is valid; the commutator acts by zeta^(-1), fixing the stated central convention. Both dependent cases are treated explicitly. The central character differences of all lifts and the exact subgroup created by geometric conjugation give the quotient by the span of A and b, including zero- and one-dimensional spans. The two examples agree with the intrinsic local obstruction and the norm of 1+cube-root(2). No gap was found.

## D.26

The complete proof in `sections/D_cm_refine.tex` was read independently. The finite shadow multiplier is odd and invertible modulo three. Its commutator word reduces to the identity modulo four, which fixes the sign in the lifted braid identity. A subgroup of SL2(Z/12) surjecting to the global-sign quotient contains the center: otherwise its lift of the displayed projective involution would have square both one and minus one. This supplies the generation hypothesis in the matrix calculation and proves invariance of every indicated kernel. Thus the isolation assertion is obtained at each exponent, rather than inferred from the first two characteristics.

The integral cusp equation, the augmented Smith form, the corrections over Z2 and Z3, the averaging construction at the other primes, and the fiber product over the common quotient Q were checked. They construct one continuous automorphism of the homology quotient. The density argument chooses a discrete level-six gauge agreeing simultaneously with the global conjugator and its abelianization modulo36; the resulting finite gauge therefore extends. The explicit normal core of a quotient N→S3 gives a finite quotient below G6 which kills neither the first commutator of the chosen basis nor the full subgroup [N,N]. This proves precisely that the homology refinements are not cofinal among all finite quotients.

An independent rerun of `code/d_cm_refine.py` reproduced Smith multiplicities (1 repeated96 times,2), the surjective augmented matrix (1 repeated97 times), all24 compatible pairs, the12 extra CM pairs, and384 general-m hexagon identity checks. No gap was found in D.26, and no genuine full profinite lift was inferred.

## E.36

The original Borne--Emsalem--Stix paper was opened directly at https://arxiv.org/pdf/1301.4429 (version2). Definition2.3 and Remark2.4 show that the singleton rational cusp O is a torsion sub-packet. Section3.2 and Proposition3.5 identify the exact cuspidally central arithmetic extension. Theorem5.10, including its proof on printed pages12--13, applies to every full proper-curve section over Q.

Extending a T3E cocycle by zero at all other primes gives an actual full section to which that theorem applies. Projecting its lift gives the required once-punctured class-two section. Pairing this with the prescribed generalized-Jacobian cocycle uses the actual based map induced by the open immersion and abelianization. Its map on the nine cuspidal coordinates has determinant one. The full intrinsic exterior-square kernel is free of rank44, and its surviving elliptic commutator is Z3(1).

The finite rational torsion of the generalized Jacobian proves H0(Q,V)=0, so geometric conjugation introduces no stabilizer quotient beyond central coboundaries. The entire fiber is therefore a torsor under the stated restricted-sequence form of H1(Q,Z3(1)). An independent rerun of `code/e_cuspidally_central.py` verified the exact inverse cusp maps, Smith diagonal, and exterior-square rank44 kernel. No gap was found.

## Elementary cubic CM image and integral basis check

For the conductor27 elliptic curve, the proposed direct proof of image 1+3Z3[zeta] was checked. Rationality of its full three-torsion over K=Q(zeta) gives the inclusion. The actual Frobenius over the prime2 is minus two, using the degree-two characteristic polynomial and residue degree two. At either prime over7 the trace and norm identify the scalar as 1+3zeta or 1+3zeta². The logarithms of these two elements, divided by three, reduce to a basis of Z3[zeta]/3; since log is an isomorphism on 1+3Z3[zeta], they topologically generate the full group.

The integral complex-conjugation basis also checks once P is shown to generate E[3] over O/3. A lift t has c(t)=epsilon t with epsilon congruent1 modulo3 and epsilon times its conjugate equal1. Multiplication of t by the unique square root of epsilon in1+3O yields a c-fixed O-basis. For the semiabelian lattice embedding j=[3I;U], equivariance forces the lower-left block to be (UA_E−A_TU)/3. The author was asked to retain the exact Weil-pairing sign in U or the explicit common-sign basis map diag(I2,−I8); the latter conjugates the two candidate representations and leaves their exterior-square invariant factors unchanged.
