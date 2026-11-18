# Limits of the remaining tower arguments

This recovery note records arguments reviewed before the final stopping review. It does not introduce a new numbered result or change an Open status.

## The fixed rational reference cannot persist at every coefficient precision

The finite catalog in E.215 uses literal agreement, at a specified finite five-power precision, between the changed abelian pair and the rational reference (83/256,173/256). At a newly introduced support prime q, the rational reference has valuation zero, whereas the completed ordinary pair has a fixed nonzero integral valuation m_q. Agreement modulo fifth powers to precision 5^n requires 5^n to divide m_q. Since m_q is a fixed nonzero integer, this fails whenever n>v_5(m_q). Thus one cannot apply the same finite-reference normalization indefinitely at increasing coefficient precision to an already frozen ordinary pair.

A rational prefix does not automatically provide a replacement reference section: its two multiplicative coordinates need not add to one. It is therefore not a rational point of the tripod merely because its individual coordinates are rational. A replacement argument would have to construct and retain an actual arithmetic section independently.

This limitation does not exclude an all-depth ordinary section. It prevents a particular finite-catalog argument from proving one.

## A literal failure of the ordinary class-six Lie lattice

Let L be the free class-six Lie algebra over Z_5 on X,Y, with its ordinary Hall lattice, and work in its rational Malcev group. Conjugation by x=exp(X) acts by

Ad(x)(Y) = sum_{j=0}^{5} (ad X)^j(Y)/j!.

The degree-six term is (ad X)^5(Y)/120. The numerator is primitive: its leading associative word X^5Y has coefficient one. Since v_5(120)=1, this term does not belong to the ordinary degree-six Z_5 lattice. Hence Ad(x)(Y) is not in L.

Scaling the entire lattice by five does not fix this. The degree-six part of Ad(x)(5Y) is (ad X)^5(Y)/24, which is not in 5L. Consequently exp(5L) cannot be normal under x. A stable replacement must admit at least the divided degree-six direction (ad X)^5(Y)/5. We do not claim that this calculation forces every degree-six direction to be divided.

Such a replacement changes reduction modulo five: bracket terms and the divided fifth-adjoint term no longer have the ordinary free-Lie comparison used in the formal calculation. Thus the ordinary free-Lie cyclic-cohomology argument cannot simply be transferred to the actual integral group at this class.

This proves failure of that lattice mechanism. It proves neither nonzero cyclic cohomology for a corrected actual module nor failure of ordinary section lifting.

## Status of the class-five calculation

The formal class-five module calculation and a proposed scaled-lattice realization were investigated. They were not promoted to an ordinary interpolation theorem, a nilpotency-class jump, or an infinite compatible branch. The final independent-review status is recorded separately in the provenance notes. Any reviewed formal vanishing remains confined to the specified module and group.

## Coefficient precision and geometric nilpotency class

The relative results E.216 and E.217 retain an already specified geometric nilpotency class while increasing a finite coefficient modulus. They do not produce a lift from geometric class r to r+1. The latter still requires the actual global obstruction and the simultaneous local support-matching equations. The all-weight vanishing of fixed-ramification H2 for regular odd coefficients removes one part of that step, but it does not solve those H1 matching equations.

## The local detector is not a finite-support theorem

E.218 separates an interior point section from a cusp section over a fixed finite field by a finite characteristic pro-ell quotient with ell different from the characteristic. Its use against a construction that freezes a prescribed reference Frobenius at increasing depth is valid only when that same local prescription is actually retained. An arbitrary global section above ordinary abelian data does not automatically carry that prescription. Therefore the local detector does not settle A.2, A.3, or the universal exclusion questions.

## Verification provenance

The mathematical limitations above were reviewed in conversation. This file is a fresh transcription after restoration of checkpoint08 into a new workspace. It is not claimed to be byte-identical to the earlier chat blocks or lost working notes.
