# Exact factorization of the direct folded-pentagon detector

Let P=Gamma_{0,5}, let q:P->Gamma(2)<SL2(Z) be the literal folding map sigma1,sigma3->U and sigma2->L0, and let M be the kernel of its signed mod12 reduction. The previous exact target was T=P/(M' M^6), of order192*6^102. A.4.12 gives the actual detected modular quotient J, with kernel W=C3^8 over SL2(Z/12). Write J(2) for the image of Gamma(2), of order192*3^8.

The actual map P->J(2) sends M into W. It therefore kills M' and M^3, and in particular kills M' M^6. By the first isomorphism theorem it induces a surjective map T->J(2). This is the literal map induced by the same U,L0 images; no identification of source completions or inverse map is involved.

The five insertion pairs are (A12,A23 A24), (A13 A23,A34), (A23,A34), (A12 A13,A24 A34), (A12,A23), with A12->U^2, A23->L0^2, A34->U^2, A13->L0 U^2 L0^-1, A24->U L0^2 U^-1. Each insertion F2->P followed by the quotient T->J(2) is the same literal pair evaluated in J(2). The two-cycle and both retained three-cycle insertion maps commute with it as well.

Consequently every finite source residue and actual E0 conjugator pair in the executed certificate test_fivepoint_cm_level.json projects to a solution of these equations in J(2), with its source-frame parity unchanged. The 24 previously retained framed formal solutions (12 of each parity) therefore cannot be excluded by replacing only the five-point target with J(2). This is a proved factorization limiting that proposed repeat calculation; no additional finite survival run was needed, and no full lift of those formal solutions is asserted.

The new result A.4.12 is nevertheless useful because it realizes the decisive global CM-centralizer residue restriction on the explicit characteristic surface quotient P8 of order32*3^45. That realization was the missing map in the previous surface attempts, and supports A.4.13's actual three-division reconstruction.
