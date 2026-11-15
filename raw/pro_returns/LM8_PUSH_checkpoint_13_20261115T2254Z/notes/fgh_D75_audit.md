# Independent complete audit of candidate D.75

**Verdict: PASS.** I read all 301 lines of `notes/de_compact_axis_draft.tex`, checked the actual D.35/D.39 action and the complete compact-kernel construction in `sections/D_alexander_separated.tex` (D.63), inspected the exact certificate, and independently reran it. Output is retained at `notes/fgh_D75_certificate_rerun.out`. No substantive correction is needed.

## Actual quotient and integral dual

Setting v=0 in D.35 gives exactly t^{a(g)} χ(g) S_χ(t) f(t^χ). The beta series is literally1 on this axis because it is1+uvB_g. Thus the Tate twist by−1 removes the extra χ, and multiplication by u identifies the actual module with the augmentation ideal of Z_5[[Z_5]] under affine pushforward. This is an integral homeomorphism, not a rational leading-term comparison: multiplication by u is a continuous bijection from a compact module to the closed augmentation ideal.

The augmentation splits by the Dirac measure at0. Hence continuous functionals on its kernel extend, and the dual is precisely locally constant Q_5/Z_5-valued functions modulo constants. Compactness of Z_5 makes every such function finite valued and ensures factorization through an actual finite quotient. The Cartier dual twist agrees with the untwisted dual of M_a(−1).

## Exact arithmetic image

For Q and Q_5 the cyclotomic image is all Z_5^×. A primitive Kummer class remains nonzero modulo5 after restriction to kerχ: inflation-restriction has kernel H^1(Z_5^×,F_5(1))=0, and a central multiplier2 makes the Sah argument integral modulo5. Restriction is an additive homomorphism with compact image; a nonzero mod5 value forces the entire Z_5 image. Dividing the original class by its exact power of5 and then changing by an integral coboundary therefore gives exactly the claimed full affine subgroup, rather than only a subgroup with the same tangent space.

The local normalizing translation is divisible by5^r after the global normalization: evaluate the coboundary equation on an actual local element with χ=2. This point is essential to the inclusion of the global ball basis into the local one, and the draft proves it explicitly.

## All invariant classes, including possible additive defects

An invariant function modulo constants can initially have a translation defect c(h). Pure multiplier2 fixes the function exactly by evaluation at0. Comparing translation by h and2h then gives c(2h)=c(h)=2c(h), so the defect vanishes, without assuming that the function itself was invariant at the outset.

The actual invariant functions for finite depth d are arbitrary functions on the d+1 unit orbits of Z/5^d, modulo constants. The ball indicators give an integral basis over Q_5/Z_5. At infinite depth continuity forces the values on small shells eventually to equal the value at0, giving the direct sum, not a direct product. The divisibility of the local translating element preserves the first r ball functions. This proves the exact quotient of local by global invariants with no hidden change of basis or finite-level survival assumption.

## Passage to the retained compact global term and splitting

The stable axis quotient induces an injection of discrete Cartier duals. Its local-invariant subgroup meets the ambient global-invariant subgroup exactly in its own global invariants. The resulting quotient injection therefore dualizes to a genuine continuous surjection from ker(L_5→T_s). D.63 gives a continuous surjection from the retained compact term K_s to that kernel, so composition gives the stated compact quotient.

The local H^2 and global-invariant duals are taken through the actual finite filtration. Local H^1 finiteness kills the derived inverse limit; invariants commute with the increasing union of finite discrete duals. Thus the computation is not inferring an integral class from an isolated finite-level class. Finally the discrete dual of the claimed quotient is a direct sum of Q_5/Z_5, which is divisible and injective over the PID Z_5. A retraction exists in the discrete module category; its Pontryagin dual supplies the continuous compact splitting. The draft does not assert a splitting of the nonseparated H^2 quotient.

## Parameters, examples and independent computation

The local Kummer basis κ(5),κ(6) is exact. The coefficient λ_p=log(p^4)/(4log6) is integral for every p≠5. Since the global coefficients tend to0, the local sum converges independently of order even under infinite ramification. The local divisibility is the minimum of the two coordinate valuations. For101 this gives depth1. The log ratio log16/log81 is a unit congruent to3 modulo5, and the two-term global class has local value0 while remaining globally primitive.

I inspected the certificate's finite affine orbits, triangular integral ball-function defect matrices, rational logarithm truncations with explicit valuation bounds, and prime examples. The independent rerun passed. These finite computations support, but are not substituted for, the continuous proof.

## Primary source verification

**verified:** Milne, *Arithmetic Duality Theorems*, second edition, original author PDF https://www.jmilne.org/math/Books/ADTnot.pdf, freshly reopened as `turn962view0`. Theorem I.2.1 and Corollary I.2.3 were inspected at `turn963view0`–`turn963view1`; they give finite-module local duality and local H^1 finiteness. The global input is already the audited D.63 application of I.4.10; I also reopened its references in the same primary text (`turn963view2`). No additional conjectural duality, rational comparison, or global section-lifting theorem is used.

The remaining complementary compact factor and the first finite-derived obstruction are expressly left undetermined. The claim is exactly the stated direct factor of the retained compact obstruction.
