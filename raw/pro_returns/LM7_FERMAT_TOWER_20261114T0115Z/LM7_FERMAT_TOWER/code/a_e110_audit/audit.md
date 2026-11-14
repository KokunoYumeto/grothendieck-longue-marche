# Independent full audit of E.110

**Reviewer:** a_structure. **Status:** PASS. No mathematical or source correction requested.

## Frozen scope and execution

I read all 650 lines of `research_e110/sections/E_pure_tower_complete.tex`, all 492 lines of the portable Python source, and all 34 lines of its GP source. The audited theorem SHA256 is `23e7f7efcee8b9123363d30f8b1fe76763b38e2370d763bdf1e4cac17f7aae38`. All 45 files in the final manifest were hash-checked before execution.

I made a separate source/input copy and ran the complete `--gp` reconstruction. The full Python source, GP source, GP text output, Python stdout, and JSON certificate reproduce the frozen bytes exactly, with no excluded fields. The fresh PARI binary has different serialization bytes. A separate literal PARI program reads both binaries and verifies equality of the entire resulting GEN vector, including all seven components. That is the actual comparison map; no partial BNF projection or ignored numerical component is used. `rebuild_comparison.json` retains these facts, and `compare_binary.gp/.out` retain the complete binary check.

The executed arithmetic includes the actual four-place character matrix, its inverse on every element of the sum-zero hyperplane, conjugation and its fixed line, all 27 mixed unit products, characteristic-zero multiplication matrices, exact norm polynomials, wild determinant norms, 166 rational primes with 792 compatible pure-root transitions, and 531,441 full positional inverse checks. These checks are finite arithmetic certificates. The all-level and topology claims below were separately reviewed as proofs.

## Fields, local characters, and class induction

The Newton-polygon argument retains the literal branches `alpha_1=rho*zeta^j`. At j=0 the shifted constant has normalized K_3 valuation two; at j=1,2 it has valuation one. For degree 3^(d-1), every intermediate binomial coefficient lies strictly above the indicated segment. Its denominator is 3^(d-1) in each case. This proves the full local degree and total ramification, so the three M-primes and the two pure primes are the actual persistent chains. The residue-degree-one norm maps used later are thereby fixed.

At the first level, only the seventeen-prime ramifies in M_1/K. The root zeta is a cube in F_289 and every K-unit is an everywhere local norm. The Hasse norm theorem and the ambiguous formula give zero three-primary ambiguous classes. A finite nonzero three-group with a three-group action has nonzero fixed points, proving the initial three-class vanishing.

The three literal units are certified independently by their integral monic polynomials with constant term a unit. Their local characters use the common root zeta and arithmetic reciprocity. The cyclotomic norm formula and skew-symmetry calibrate the wild sign; the tame value at seventeen is the negative logarithm. The actual matrix D has first-three-row determinant -8 and image exactly the four-coordinate sum-zero hyperplane. Its conjugation is the negative place permutation, so the fixed line is exactly (0,t,-t,0). The included pure unit has value (0,2,1,0); consequently the explicit E65 scalar is nonzero and has the stated inverse.

The transfer in E110.20 is the literal Kummer norm projection formula followed by `inv composed with Cor = inv`. Every completion over the four initial places has the full relative degree, and the norm of alpha_d is alpha_1. Hence the included units retain their four characters at every height without an extra degree multiplier. Four totally ramified places and image size 27 give ambiguous three-class order one inductively. Ideal extension from F_d to M_d followed by norm is multiplication by two; this is injective on the relevant primary class group. The strongly ambiguous exact sequence then identifies the unit norm quotient with the entire character image. The quotient is killed by three, which justifies discarding no hidden prime-to-three class contribution. Exact C2 invariants, together with the actual inverse `N^(1/2)`, yield the pure norm quotient of order three.

## Principal divisors and complete norm systems

At every finite pure level, the class group order is a three-adic unit. For a prime ideal of class order h, the map sending that prime to the completed element a^(1/h), where (a)=p^h, is a genuine section of the completed divisor map. The induced filtration on the unit kernel follows because a power root of a unit has zero valuations. This proves the entire finite-level completed sequence before taking its norm limit.

The surviving divisor chains are exactly the actual integral affine-Frobenius fixed chains. An orbit whose three-part grows without bound has zero mass under compatible residue-degree norm maps. The two three-chains, the seventeen-chain and the P_0 chains have residue degree one throughout. This proves both the divisor module and the rational norm formula.

For a fixed compatible divisor family, each finite-level principal preimage is a nonempty compact unit torsor. Every finite collection of norm equations is solved by choosing a lift at the highest level and taking its actual norms. The finite intersection property in the product of those compact torsors supplies an entire coherent lift. This uses compactness of each fibre, and does not require compactness of the restricted divisor module. Chosen coherent prime generators yield the displayed restricted-product splitting: modulo 3^m at each positional level, only finitely many factors survive. The same observation proves continuity, and the ratio of two chosen splittings gives precisely the displayed inverse coordinate change.

## The entire compact unit kernel

The compact inverse limit J_F is torsion-free, since every pure unit completion is finite-free. A finite continuous character factors through a finite positional quotient, and it extends from the image subgroup to the complete finite-level quotient because Q_3/Z_3 is divisible. Agreement after a sufficiently high pullback follows from the descending finite-image system. This proves the exact direct-limit character description even though the norm maps on unit groups need not be onto.

Multiplication by three on J_F is a homeomorphism onto its closed image. A character on that image extends through a finite quotient of J_F, proving three-divisibility of its character group. Choosing a basis of the characters killed by three and successive divisions yields an independent direct sum of Prüfer groups; induction on the order proves spanning. The finite character cylinders are onto, and compactness gives the literal inverse of E110.7. Thus both the product map and its inverse are established topologically.

The rank input is unconditional. I reopened Kato's actual definition of U and Theorem 1.1(1), then the complete rank calculation in Section 3.2, together with the supporting norm/cohomology comparisons. For base F_d, the ordinary unit rank is r_d and there are two three-places, so the three-unit rank is r_d+2. The cyclotomic quotient has rank 2-1 by the kernel/cokernel calculation for the torsion cyclotomic cohomology module. Thus the coherent cyclotomic norm image has rank r_d+1. Theorem 1.1(1) identifies the full false-Tate coherent image up to finite index. Restriction to the actual pure tower, followed by the two valuation kernels, loses at most two ranks. The two nonsplitting residue-degree-one chains prove that vanishing of these valuations at level d persists at all higher levels. The resulting elements are actual ordinary-unit systems, giving projected rank at least r_d-1. These ranks are unbounded. Countability and the established character construction therefore give precisely a countable product of Z_3, with no unproved assertion about stabilization of finite projections.

## Full fixed-first H space and maps

The E46 positional map uses the actual first cocycle 3*kappa_3(17), with the /3 toric projection retained. Pure and complex surviving off-S primes belong to disjoint sets P_0 and P_1. The combined cube condition consequently forces their exponents separately to be multiples of three. Necessity of the displayed toric image follows.

Substituting E110.10 into the two proved norm formulas gives seventeen-exponent e+2b=3B_17, three-exponent B+C+3z-sum(ell_p r_p)=3B_3, and all other exponents 3r_p. This proves sufficiency using the actual Shapiro/norm map. The inverse first reads the unique complex coordinates and the first pure valuation, solves the two displayed equations for e,C, and then uses the pure splitting to recover the unit kernel coordinate. The bounded phase coefficients and restricted prime parameters ensure convergence and continuity of both maps. The kappa_3(7) example has exactly the retained phase 8 and its pure correction, so its comparison to the earlier pure-component-one subspace is literal.

Finally the unit-r automorphism is verified in the actual semidirect law: substitution T -> T^r transports T^a to T^(ra), preserves augmentation and commutes with arithmetic action. Its stated inverse and both scaled toric coordinates follow. The scope remains the actual quotient H and the fixed unit-multiple first classes. No new intrinsic lifting assertion is inferred.

## Primary sources actually reopened

- Kato, *Universal Norms of p-Units in Some Non-Commutative Galois Extensions*, official full original: https://ems.press/content/book-chapter-files/27477. Read the coherent definition and Theorem1.1(1), Sections2.2--2.6, Section3.2 including its unconditional rank proof, Proposition4.2 and its successive-filtration proof, and the comparison proof in Sections5.4--5.5. Exact retrieval references are recorded in audit.json.
- Lemmermeyer, *The Ambiguous Class Number Formula Revisited*, https://arxiv.org/pdf/1309.1071. Read Theorem1, Proposition1 and its exact ideal Hilbert90 map, and the complete ideal/Herbrand derivation in Section3. The printed Am_st typo in the surjectivity sentence is interpreted by the actual constructed ambiguous class, as already documented by the author.
- Milne, *Class Field Theory*, https://www.jmilne.org/math/CourseNotes/CFT.pdf. Read III(29),(30) and the proof of the invariant/corestriction formula, III3.1 with the Res/Cor cup argument, III4.4 with its proof and chosen-root comparison, and the full VIII3.1 cyclic Hasse norm proof. These supply the exact norm and sign maps used above.

No theorem or certificate file was edited during this independent audit.
