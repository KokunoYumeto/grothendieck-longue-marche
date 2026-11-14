# Exact perfection test for an actual common residual fibre product

Let A and B be perfect groups, with specified epimorphisms f:A->Q and g:B->Q. Write R=A x_Q B and K=ker f. All homology groups below have integral coefficients and all maps are induced by the displayed homomorphisms. There is a natural isomorphism

R_ab = coker(H_2(A) direct-sum H_2(B) -> H_2(Q)),

where the two maps can be taken with opposite signs; their image sum is independent of that choice.

Proof: the extension K->R->B has [R,K]=[A,K], because the projection R->A is onto. Its five-term homology sequence gives

H_2(B) -> K/[A,K] -> R_ab -> H_1(B)=0.

The extension K->A->Q gives

H_2(A) -> H_2(Q) -> K/[A,K] -> H_1(A)=0.

Naturality under the literal map of extensions (K,R,B)->(K,A,Q) identifies the first transgression with H_2(B)->H_2(Q)->K/[A,K]. Taking the resulting cokernel proves the asserted isomorphism.

Consequences retain their exact hypotheses:

* A specified splitting of f makes H_2(A)->H_2(Q) onto, hence R is perfect.
* A perfect kernel K gives K/[A,K]=0, hence R is perfect.
* If Q is the actual product A5^t, its universal central cover is SL2(F5)^t with kernel C2^t. A complete central-lift test of this cover pulled back to A computes the actual transgression H_2(A)->C2^t. Perfection of that pullback proves this map is onto and therefore proves R perfect, independently of B's multiplier map.

The last condition cannot be replaced by the two projection groups being perfect. For instance, the actual fibre product SL2(F5) x_A5 SL2(F5) has an extra central C2 quotient, exactly as the displayed cokernel predicts.

## Primary source for the A5 cover

Robert Steinberg, Lectures on Chevalley Groups, Section7, Theorem10 and its Corollary2(b), state that for finite |k|>4, excluding SL2(9), SL2(k) has trivial Schur multiplier and SL2(k)->PSL2(k) is universal. Applied to k=F5 and the actual PSL2(F5)=A5 map, this gives the binary-icosahedral universal extension with kernel {+I,-I}. The direct product comparison follows from the integral degree-two Kunneth formula and H_1(A5)=0.

The complete primary-text transcription was independently opened at
https://math.soimeme.org/~arunram/Resources/LOCGS7CentralExtensions.html,
Theorem10 and Corollary2(b), with the latter at the displayed Section7 lines98--103. The 2016 publisher edition is Robert Steinberg, Lectures on Chevalley Groups, University Lecture Series66, AMS, DOI10.1090/ulect/066; the publisher contents identify Chapter7 as pages47--59. The publisher PDF access returned403 in this session. The exact transcribed theorem was read, rather than inferred from a general table.

An alternative finite-presentation proof is available once its order is certified: the binary-icosahedral presentation <r,s | r^2=s^3=(s^{-1}r)^5> has exponent matrix [[2,-3],[-3,5]] of determinant1. An actual coset enumeration of order120 together with an onto matrix realization in SL2(F5) proves that presentation. A perfect balanced n-generator/n-relator presentation has H_2=0: the free abelian group on relators maps onto R/[F,R], and the composite to F_ab is a unimodular n-by-n map, forcing both maps to be isomorphisms; the Hopf kernel is zero. No such new enumeration was run here, so this alternative is a described verification route, not an additional computational result.

The peer's complete presentation test retains every generator sign freedom and every central relation discrepancy. This is the appropriate finite calculation for the specific common residual, after its actual maps to A5^t have been identified.

## Original primary scan and direct pullback proof

The original Yale scan was subsequently opened independently at
https://www.math.utah.edu/~ptrapa/math-library/steinberg/steinberg-yale-notes.pdf.
Section7, Corollary2(b), and the explicit SL_n-to-PSL_n universal-cover example occur at PDF indices88--89. This verifies the precise statement directly in Steinberg's original notes, in addition to the transcription above.

The direct product universality also has an elementary comparison: images of distinct perfect factors in a central extension commute, because their cross commutators are central and factor through their abelianizations. Thus the product of the displayed universal covers has the universal property for the actual product A5^t.

For the certified common quotient Q=A5^3, put K=ker(C6->Q) and A=C6/[C6,K]. This is a perfect central extension of Q. The universal U=SL2(F5)^3 maps to A; its image is onto because A is the product of that image and its central kernel, and A is perfect. The full pullback C6 x_Q U maps onto K/[C6,K] by (g,u)->gbar*phi(u)^(-1). The value is central, so this is an actual homomorphism. Perfection of the pullback therefore forces K=[C6,K]. For any perfect C_L->Q, its actual residual fibre product R=C6 x_Q C_L then satisfies [R,K]=[C6,K]=K, while R' maps onto C_L; hence R=KR'=R'.

The peer reports the complete pullback certificate now passes: all720615 Schreier relations plus10 original-generator relations have rank13 in the ten generator-exponent columns and three central columns. Independent word/permutation/matrix replay checks the13 retained basis rows. There are30 independent central choices on the ten generator lifts; each changes one of the three central columns by one generator-exponent column, so all these choices are retained by this same rank test. The peer owns the execution artifacts and theorem integration; this ledger records the exact comparison proof audited here.
