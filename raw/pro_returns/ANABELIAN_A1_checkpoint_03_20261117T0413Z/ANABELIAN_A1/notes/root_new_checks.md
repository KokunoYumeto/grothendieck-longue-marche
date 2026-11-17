# Independent checks after checkpoint02

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed.

## Cyclic13 cover of the characteristic-two genus-two curve

Read B.LIT7 in full. The coordinate transformation is x=1/X, y=Y/X²; it identifies Y²+X²Y=X⁵+X with y²+y=x³+1/x. The chosen point is infinity in the polynomial model. The two Artin–Schreier poles have orders3 and1, giving genus2 and2-rank1. The canonical divisor is2P, which supplies the leading coefficient64 in every nontrivial quadratic twisted L-polynomial.

Implemented a different group-law algorithm in code/c0_cyclic13_verify.py: addition of one fixed rational point by CRT, local first and second Taylor jets, conjugate cancellation, and exact degree-three reduction. It imports no arithmetic from the Cantor producer. Every Mumford output is checked. All64 rational point projections, all13 subgroup elements, and all point-class orders agree. Independent Newton sums give H64(U)=U⁴−U³−80U²−64U+4096 and class number3952. Occupancies are16,4,...,4, hence all12 nontrivial twisted polynomials are1+12T+64T² and the relative class number is77¹². The Newton slopes of the new factor are1/3 and2/3. The irreducibility of H2 and its slope-zero root exclude a geometric supersingular factor of the old Jacobian as well. Thus this cover cannot map to a positive-genus supersingular curve, while no conclusion about every other cover of this base is made.

## Nonabelian finite norm mechanism

Read B.NA1 and reran its independent verifier. Three explicit5×5 matrices overF7 generate25920 elements. The20 conjugacy classes and all19 nontrivial normal closures are verified, proving simplicity directly. The faithful module has16807 elements, so no regular orbit; the sole proper normal-step relative module is nevertheless nonzero. This is a finite representation example, not a Jacobian realization.

## Lower-central tower, B.CF12–13

Read the complete mixed-characteristic draft independently. The metabelian kernel calculation retains the actual strict-local number field, not a completion. The two-puncture Kummer obstruction to supported scaling is valid. For the lower-central union, compactness identifies the quotient with the maximal pronilpotent quotient; its tame factor is central. The finite image of the residual subgroup intersects the torsion-free radical Kummer group trivially. This gives the exact cyclotomic eigenrelation after the two injective restrictions. Baker–Brumer then forces torsion forp≥5. The p2 andp3 radical towers have nilpotent finite Galois groups, and the displayed elements are nontorsion. The primary Rousseau1969 source was opened independently: Théorème, printed pp1–2, exact hypothesis algebraic p-adic units with Q-independent logs, conclusion Qbar independence. No reconstruction theorem follows merely from this kernel result.

## Solvable finite norm mechanism (proof review before final inclusion)

Induction on derived length passes. The last derived subgroup N is characteristic abelian, hence F-stable. The e_N splitting preserves F-fixed parts. The commuting normal-subgroup idempotents e_K and exact N-character-kernel projectors split into orthogonal atoms permuted byF. A nonzero fixed choice on each available atom orbit simultaneously realizes every common N-stabilizer. Quotient induction gives KN after each norm; combining with N∩K yields exactlyK. Constant-deck relative-class-number reformulation and semilinear common-stabilizer formulation must remain distinct. Feit–Thompson original ChapterI §1 main theorem was opened independently to justify its use for characteristic2 odd-order deck groups.

## Infrastructure interruption

At03:40–03:44UTC, sandbox launches failed with a disk-full error before any command ran. A requested elevated read-only disk check was automatically rejected by environment policy. The ordinary workspace interface recovered without escalation. The workspace itself occupied360MB; the global disk then had1.8GB free. No checkpoint or mathematical certificate was deleted, and no out-of-workspace cleanup occurred.

## Further mixed-characteristic point-function checks

Read CF14–17 in full. CF14’s finite normal enlargement and H1-vanishing by a central tame element prove rationality of the scalar from an actual Kummer value. CF15’s distance identity forces a common positive exponent, then exponent one by the triangle inequality and the inverse map. CF16’s norm residue is weighted by residue degree, not ramification; branch values contribute zero residues, and fibre evaluations are actual norm products. CF17’s three squared-distance potentials recover a real-analytic function on the complex plane minus finitely many points. The dense-centre identity gives F_zbarz=0 and F_zF_barz=0, hence holomorphic or antiholomorphic; the remaining singularities are removable and growth is polynomial. Interpolation gives coefficients in E. Integer shifts in the antipolynomial identity force complex conjugation to centralize G_E, excluded by the already checked valuation argument. These are point-function theorems only; the full inverse-image functor and arbitrary-source assertions remain unproved.

Read B.LIT8–10. The small-genus cubic theta obstruction uses the exact pole inequality 3(g−1)≤2g for g=2,3. The reflection quotient proof now includes the unique fixed point, different2g+2, genus calculation and complementary pullback images. The fixed-function postcomposition obstruction is precisely a fibre-gcd and Riemann–Hurwitz statement. The positive uniform odd-r construction is an étale Kummer pullback; the two explicit Fermat maps and the Hermitian norm count q³+1 prove the supersingular target. None settles the arbitrary-source B5 quantifier.
