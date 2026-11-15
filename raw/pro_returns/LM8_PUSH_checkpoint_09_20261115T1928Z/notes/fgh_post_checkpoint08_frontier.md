# Notes-only directions after A.51

No statement below is registered. Included sources and registers remain frozen for checkpoint08.

## More punctures on the same Heisenberg curve

Let C and q be the proper genus10 curve and cubic elliptic map of A.50. For m at least1 put X_m=C minus q^{-1}(E[3m]). The composite [3m]q gives an actual finite etale cover of U of degree27m². It has27m²−18 cusps: the nine points above E[3] remain totally ramified, while all9m²−9 other target torsion points have three preimages. The genus remains10, and the Euler characteristic is −27m².

Every map used in A.50 remains an actual map from this smaller affine curve: removing extra points cannot introduce a preimage of a deleted target cusp. The proper Jacobian and its exact elliptic/non-CM decomposition are unchanged. Thus the same proof should give all-prime procyclic normalizer recognition for every X_m. At each of the original nine cusps, the rational joining paths supplied by A.51/A.42 survive separating additional marks, so their full fixed subgroups should remain selected inertia at every coefficient prime. Newly removed cusp packets require their own pointed-path argument. No claim is made that their individual divisor differences are torsion in J_C.

## A concrete residual Heisenberg-five cover

The general odd-prime analogue is the smooth normalization of z^p=psi_p(x) above E:y²=x³−x, where psi_p is its p-division polynomial. Its divisor is the sum of all nonzero E[p] minus(p²−1)O. It is cyclic of degree p over E, totally ramified at all p² torsion points, so the composite [p]q has degree p³, p² cusps, and genus1+p²(p−1)/2.

Translations by E[p] lift because translating the division-polynomial divisor changes it by p² times a torsion-point difference, and p times that difference is principal. The lifts form a central extension of E[p] by mu_p. It is nonabelian because a nontrivial inertia at the single branch point of an elliptic cover is a commutator. Negation [-1] lifts with z fixed. It acts by minus one on E[p] and trivially on the central mu_p; therefore the pth-power homomorphism from E[p] to mu_p equals its own negative and vanishes for odd p. Hence the deck group is the exponent-p Heisenberg group. This gives another direct model of the characteristic class-two exponent-p cover.

For p=5, psi_5(x) is

    5x^12−62x^10−105x^8+300x^6−125x^4+50x²+1.

In s=x² it factors as

    (5s²−2s+1)(s⁴−12s³−26s²+52s+1).

Thus the proper genus is51, there are25 cusps, and the degree is125. A.22 supplies the coefficient-five fixed subgroup. The complete all-prime fixed and normalizer classifications of this particular cover have not been proved in the present work. A.49 provides different complete examples of genus51 and does not identify them with this Heisenberg cover. No least-index assertion among all remaining covers is intended.

Every difference of two branch cusps is killed by p², by pulling back p(T−U) along q. The curve has potentially good reduction away from p: after potential good reduction of E, the p-torsion branches remain disjoint and the cyclic-p normalization is tame. At residue p one must establish the actual pointed reduction; the rational-path criterion cannot be inferred merely from the deck group or the torsion exponent. For p=5 the original elliptic curve is ordinary, so the p-rank-zero argument of A.51 does not apply unchanged.


## Exact wild charts at three (candidate extension, unregistered)

At each finite two-torsion point T=(a,0), a in {0,1,−1}, let delta=3a²−1. Choose eta²=−3, rho⁴=eta, and z0³=f(a), where f=3x⁴−6x²−1. In the actual function field make the polynomial coordinate substitutions

    x=a+rho² U,  y=rho X,  z=z0(1+eta V).

The exact integral affine equations are

    X²=delta U+3a rho² U²+rho⁴ U³,
    z0³(V+eta V²−V³)=2delta U²+4a rho² U³+eta U⁴.

Their reduction eliminates U=X²/delta and gives

    z0³(V−V³)=(2/delta)X⁴.

Thus each chart has a smooth geometrically integral special affine component whose smooth projective completion has Artin–Schreier genus three. This is an algebraic chart, not merely a power-series approximation. In the Jacobian matrix, the first equation has unit U-derivative and the second has unit V-derivative on the special fibre. Its generic function field is exactly K(C). Normal projective compactification and regular resolution therefore preserve this positive-genus component; after first making C semistable, minimal-model factorization and stable contraction cannot remove a positive-genus component. The three charts restrict to distinct base valuations centered at the three finite two-torsion points.

For the main component, choose pi³=3 and z=−1+pi u. The exact equation is

    u³−pi² u²+pi u=x⁴−2x²,  y²=x³−x.

The reduction u³=x⁴+x² is irreducible over k(E), because its right side has nonzero differential (x³−x)dx. Its function field is k(E)^(1/3); its normalization is the Frobenius twist of the supersingular elliptic curve E. Thus the main component has genus one and maps purely inseparably with degree three to E. Together with the three genus-three components this exhausts genus ten. A51 already proves compact type. On a regular semistable model dominating these charts the actual map to the good model of E exists, and every other component is rational. Each genus-three component contracts to its associated nonzero two-torsion point.

For odd m, write 3m=3^h n with n prime to3 and odd, h≥1. E[3m] specializes onto E[n], with 3^(2h) torsion points in every reduction class. None of E[n] is a nonzero two-torsion point. The marked source points over each such reduction class can only lie on the main component or rational subtrees attached to its unique Frobenius preimage. There are 3^(2h+1) source marks in a nonzero class, and 3^(2h+1)−18 in the origin class (at least9). Separating these sections gives a rational marked tree in each class, with no positive-genus vertex on a joining path. A42 would prove the full fixed-inertia theorem at every added cusp and coefficient prime. A50 already gives normalizers for every m. Even m is not covered by this argument because its reduction set contains the three genus-three tail centres.

Primary model support opened: Liu, Algebraic Geometry and Arithmetic Curves, §§8.3.2,9.2.1, Theorem9.3.21, and Stacks Lemma109.24.2 (tag0E97 within tag0E8C), whose proof explicitly resolves and contracts only rational exceptional components. A precise final citation and independent audit are still required before registering the extension.
