# A.198 source and execution audit

Status: complete source and exact certificate; parent integration remains separate.

## Files and scope

- Source: `sections/point3_genus2_toric_fibre.tex`.
- Certificate: `code/point3_genus2_toric_certificate.py`.
- Retained execution: the matching `_output.txt` and `_data.json` files.

This statement describes the actual affine-cover abelian quotient above the four compact two-adic classes proved in A.192. Its first comparison uses a selected sheet of the cyclic-eight cover and conjugacy by that cover's geometric group. It does not classify full metabelian sections from their compact data. Its explicit global torus section has the complete original pair `(3,-2)` and is the point-three image at two, but fails local point/cusp matching at 571. The last failure is proved in a specified finite arithmetic quotient, and is invariant under downstairs geometric conjugacy.

## Verified primary source

Shinichi Mochizuki, *Topics in Absolute Anabelian Geometry I: Generalities*, Journal of Mathematical Sciences, University of Tokyo 19 (2012), 139–242:

<https://www.ms.u-tokyo.ac.jp/journal/pdf/jms190201.pdf>

The published PDF was opened and the exact Proposition A.8(ii),(iii), printed pp.232–234, read. Part (ii) supplies the semi-abelian Albanese and the degree-zero boundary character lattice; part (iii) gives the torsion-free geometric abelianization comparison. Here the geometric group of the affine genus-two curve with six punctures is free profinite of rank nine, so its abelianization is already torsion free. Passing first to a finite splitting field of the boundary gives the stated split character calculation; functoriality descends it with the literal permutation action. The existing verified bibliography entry is `BIR_MochizukiAlbanese2012`.

The finite and continuous Kummer comparisons, the odd-degree branch Weil pairing, and the dyadic compact locus are used in their already proved forms A.169, A.186, and A.192. The current proof writes the new torus/isogeny/cohomology maps explicitly rather than importing a categorical comparison.

## Maps checked in the source

1. For `C: y^2=x^5-54x`, the principal boundary lattice is `2 Z^5 + Z(1,1,1,1,1)`, of index 16. The functions `x-r` and `y` realize every generator. The five branch classes have their single sum relation; their actual Weil-pairing signs identify the kernel with `J[2]`.
2. With the origin `P=(3,9)`, the units are `a=x/3`, `b=(x-theta)/(3-theta)`, `c=y/9`, and `c^2=a N(b)`. On the boundary torus the morphism is `(u,v) -> (v^2,u N(v))`. Its degree is 16. The reverse isogeny is defined by `Psi(Phi(g))=2g`, so the finite Tate cokernel map is literally `a -> Psi(a_1)`.
3. Both global and finite-local Tate invariants vanish. This gives uniqueness of the residual boundary-torus cohomology class, and retains the two-element framing kernel of the unit data. The proof makes no vanishing assertion for real Tate invariants.
4. The finite and infinite tangent constants are calculated in the parameters `y` and `-x^2/y`. The compact coordinates are explicitly translated from the infinity origin to the point `P` origin. The four dyadic unit tests and the selected half of each two-divisible class use the actual inertia lines.
5. The original functions give `t/3=a^4/N(b)` and `(1-t)/(-2)=1/N(b)`. Thus the original relative pair is `(8u-2Nv,-2Nv)`. The separate modulo-eight criterion is `Nv in 4 Qhat_2^*`, after excluding the possible minus sign using the exact tame quartic norm at three. No cancellation by two is used without that torsion check.
6. The explicit norm-one class uses the exact convergent cross product of the two odd log coefficients of `(a-theta)/(a+theta)`, for `a=1,3,5`. The cross product is an infinite-series identity. The finite truncations certify integrality and the odd last coordinate; they are not the proof of the zero logarithm. The retained tails give `lambda=(38,29,103) mod256`.
7. At 571, the literal local algebra is `Q_571 x Q_571 x K_2`, with `K_2` the unramified quadratic field. The finite unit-valuation vector is `(2,2,0) mod4`, while every ordinary or rational cusp image has at most one nonzero coordinate or a diagonal vector. The proof treats the nonrational boundary factors through the actual fixed-sheet condition.
8. The finite quotient is derived from a Nielsen basis and all nine Schreier generators. It is `(Z/4)^8 semidirect C32`, of order `2^21`; the last factor cyclically permutes the eight lamps. Its nilpotency class is exactly 12 because `(v-1)^11=2 sum(v^j)` is nonzero and `(v-1)^12=0` in the actual module.

## Executed certificate coverage

The standard-library/SymPy certificate checks the integral unit lattice, the torus and reverse maps, all sixteen branch-sign vectors, normalized functions and tangent constants, four independent truncation precisions, literal odd-power log decompositions, the field norm and 571 factorization, all finite valuation patterns, the group maps, and the augmentation identities. It exits successfully and retains five PASS lines plus structured exact data.

No external submission, large prime recursion, or exhaustive search for global sections is part of this certificate. The global section is supplied by the explicit continuous torus Kummer cocycle, and its failure of local matching is the exact finite 571 obstruction.

## Peer review

Both local-preprint and birational-main independently read the complete saved source and reported mathematical PASS before their separate executable reruns. Their final execution clearances are to be recorded by the parent alongside the main statement audit.
