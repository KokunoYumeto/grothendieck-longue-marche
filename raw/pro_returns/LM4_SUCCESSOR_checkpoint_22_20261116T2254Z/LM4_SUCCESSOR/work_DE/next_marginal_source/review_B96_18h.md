# Independent complete B96 proof audit

Status: PASS. We read `work_CE/B96_old_translate_cohomology_proposed.tex`
completely and checked the actual finite formulas independently.

## All-word comparison

The geometric-push convention is an antihomomorphism:
alpha_uv=alpha_v alpha_u. With the old base B=F6 and its actual
fixed-source double-cover subgroup B0, every odd word is bt for t in
B0. Therefore its module is S_t(alpha_b(L_ret)), after removing the
actual group-unit inner correction. All such corrections act inside
an already G-stable submodule; no operator is discarded on a mere
conjugacy-class comparison.

The eleven returned source generators are the literal Schreier basis
of B0. The actual source filling is F19=F8*F11 onto F11, so the eight
source seed images and their eleven signed operator orbits generate
the actual I as a subgroup. This does not presume that the image of
F19 embeds or that I is an ambient normal closure.

The canonical second-sheet lasso uses alpha_b^{-1}. The independent
odd-direction audit checks both directions and all actual half-words.
Positive alpha_b gives the branch-square source image of those second-
sheet words. Since that source operator is invertible and belongs to
the even source group, the two cosets supply exactly the required
orbits of all eight seeds. The elementary product/inverse difference
identities then prove that the sum of the individual cohomology images
is precisely J_I.

The right-defect naturality argument is correct and necessary: chosen
free-factor meridians can acquire mixed conjugators. Naturality of
h^{-1}F(h) in the actual mixed-kernel abelianization extension proves
the induced action on H1(P), without a strict factor-preservation
assumption before quotienting.

## Exact orbit-sum kernel

Every generic-fiber conjugation already factors through G, so B91's
remaining old transports give exactly Lbar=sum_w M_w. Each actual
summand is F-stable with its inherited, possibly twisted coefficient
action. The external direct sum D_old retains duplicate word labels;
its image sum is not treated as an internal direct sum.

The finite-group cochain complex commutes with these algebraic direct
sums. Thus H2(D_old)=0, and the image of H1(D_old) in H1(P) is exactly
J_I. The connecting map H1(Lbar) onto H2(K_old) is surjective, with
kernel the image of H1(D_old). Hence the map to H1(P)/J_I descends
canonically, with image exactly U/J_I. The invariant-kernel representative
z=(1+F)p gives the stated intrinsic anti-chain d(p); changes of p or
of the representative change its value only by the specified source
ideal or a coboundary.

No identity between K_old and B92's differently marked Z2 is used.
The final whole-previous-sum criterion is properly quantified. Pairwise
overlap tests alone do not supply it, and augmentation-adic approximation
does not prove actual discrete ideal membership.

## Exact finite formula check

`check_odd_translate_independent.py/.out` independently verifies both
actual directions, all42 full-basis discrepancy identities, all16 cone
normal forms, eight full two-chain boundaries and exact source witnesses.
The additional executed `check_B96_displayed_formulas.py/.out` checks
all four displayed second-sheet F13 words, all eight literal diagonal
signs in the table, and S=Inn(p1) alpha_b^2 on all21 fiber generators.

The theorem proves all individual translates and the exact residual
kernel map. It does not prove that the residual map vanishes, identify
any completed coefficient module, or solve the nonlinear fixed-source
and main centralizer questions.
