# Independent audit of B.41: an action deformation invisible to the Ross extension

Date: 2026-11-16. Inspected draft: `work/b_arbitrary_action_deformation_proof.tex`. Verdict: the mathematical construction and its stated nongeometric scope pass. Precision suggestions were sent to the Part B author; no B-owned manuscript was edited.

## Independently reconstructed finite data

The program `deliverable/code/c_B41_exact_audit.py` reconstructs the six written terms of b directly and reconstructs every boundary derivation column from the unique actual translation matrix carrying the origin to that cusp. It does not use the saved derivation columns as construction inputs. It checks the resulting Delta against the author's saved data only after reconstruction.

All 54 geometric equivariance identities and both arithmetic identities hold as **unreduced integer identities**. This additionally removes any question about inferring integral equality merely from a finite modulus. Delta's largest absolute entry is six; the largest geometric inner correction entry is twelve. The pure boundary vector z has thirty nonzero Hall coordinates, with coefficient one at `(3,2,5)`. Output and metadata are `deliverable/code/c_B41_exact_audit.out` and `.json`. A direct replay of the author's original program is separately saved as `work/c_replay_B41.out`.

## Continuous action deformation

For an integral map delta from V to A=gamma3/gamma4, the formula `n -> n delta(n_ab)` is an actual central automorphism: it respects multiplication because A is central and delta is additive. Its inverse is obtained by negating delta. It is identity on N/gamma3 and on gamma2/gamma4. Conjugation by an actual arithmetic automorphism acts on these maps by `Lie3(rho) delta rho_V^{-1}`. Thus the cocycle identity for psi is exactly the action identity for `rho'_g=D_{psi(g)} rho_g`. This does not use a class-three logarithm or an exponential with a forbidden denominator.

The coefficient line has type `Z3(2) epsilon` by the independently checked arithmetic identities. The c-normalized cocycle with tau-value one and conjugate-tau-value minus one exists continuously by the actual free pro-three arithmetic source. Pullback retains the original G_Q arithmetic coordinate. All gamma2/gamma4 action data, including the complete eta extension and its actual geometric action, are unchanged.

The formula `Delta(e_P)=3[e_P,B_P]` explicitly makes every peripheral image conjugate to itself under the central automorphism. At the origin B_O=0, so the chosen based inertia is fixed literally. The geometric commutator defect is inner, with the stated integral degree-two parameter. Therefore the claimed preservation is preservation of the outer geometric compatibility, not an unsupported assertion of a new algebraic-curve realization.

## Nineteen-adic obstruction

The actual cusp input has tame inertia x with abelianization e_A0. The additional action on its Frobenius relation contributes exactly `19 b_F Delta(e_A0)`. Changing a central Frobenius lift has no effect; changing the central inertia lift by y contributes `(Phi_A-19)y`. Since `Delta(e_A0)=3z` and Phi_A acts by `19^3` on the pure boundary Lie cube, the unique rational correction is

\[
y=-\frac{3b_F}{19^2-1}z=-\frac{b_F}{120}z.
\]

The operator is rationally invertible on all of A by the strict degree-three weight bound, so other components cannot supply a second solution. The Kummer rows give `b_F=1 mod3` at the selected root zeta=7 modulo19. The primitive Hall coefficient of z makes the displayed correction have valuation minus one. This proves nonexistence of a local integral lift for the changed action, while the actual action admits the original full cusp section. Geometric conjugation of the class-two representative cannot change liftability because every N2 conjugator lifts to N3.

## Cusp-origin shift and its scope

For a rational cusp P, B_P has the same arithmetic eigencharacter as the cocycle coefficient, so `delta_P(g)=3 b_g B_P` is a genuine global central class-two cocycle. Its sign is correct: the new action contributes `3 chi(g) b_g [e_P,B_P]`, while conjugation by the degree-two displacement `+3 b_g B_P` contributes the negative bracket and cancels it. The map `ad_{e_P}:Lambda2 V -> Lie3 V` is injective for primitive e_P, so this displacement is forced after the abelian origin and the chosen peripheral generator have been fixed.

Suggested wording refinement: those last two choices should be explicit when the text calls the origin shift forced. Without them, a cusp packet admits tangent twists and changes of representative. Also the scalar49 statement concerns `Lambda2(T_V)`, not the ten-dimensional matrix T_V itself.

The rational nonvanishing argument is sound using the arithmetic- and c-stable rational compact/boundary splitting. A possible coboundary normalized at c has c-fixed conjugator. Its pure Lambda2 W component is multiplied by49 under tau, and cannot produce the nonzero c-anti-invariant B_A0. The other rational summands contribute nothing to a pure boundary target because their Frobenius-minus-one maps are invertible. This excludes hidden mixed conjugators.

The shifted class-two origin lifts globally because the remaining central obstruction lies in H2(Gamma,A)=0. A central correction does not change its peripheral normalization. Consequently the construction preserves the existence of formal peripheral packets while changing their marked class-two origins, exactly as asserted.

Finally `b(tau bartau^{-1})=2` follows from the cocycle identity with coefficient49, and its cyclotomic character is one. Finite Chebotarev approximation preserves the unit valuation of b and makes `v3(p-1)` arbitrarily large. The same local correction therefore detects every nonzero scalar multiple of the deformation if the actual marked A0 origin and its twists are fixed. This is a valid insufficiency theorem for the Ross-extension data; it does not determine the actual arbitrary-input lifting image in B.5.

The final typeset B.41 at `deliverable/sections/B_arbitrary_action_gap.tex` incorporates the three precision edits. The promoted independent certificate was replayed against `deliverable/code/b_arbitrary_action_deformation_matrices.npz` and passed.
