# Independent audit of D.70

Auditor: `/root/pbc_groups`. Completed2026-11-15 before checkpoint09 capture; draft remains unregistered during the source freeze.

**PASS**, using the explicitly stated established D.24/D.56 for the final full-profinite comparison and the primary Hoshi/Milne inputs independently opened in the D.66/D.67 audits. I read the complete `notes/de_numberfield_cusp_baire_draft.tex` and checked all new number-field and higher-genus steps.

## Integral peripheral comparison

The geometric affine pro-ell group is free, and eliminating a different boundary generator makes the selected cusp generator primitive. The boundary permutation quotient has its one total-sum relation; with at least three geometric cusps, any two individual peripheral lines have zero intersection. Its selected rational peripheral line is primitive, so both B/I and V/I are integral torsion-free lattices.

At a marked good place away from ell, an unramified extension splits the boundary. The boundary quotient then has only positive cyclotomic Frobenius eigenvalues. The proper Tate module has zero fixed vectors because the local ell-primary torsion injects into the finite reduction group. These statements give integral H0(V)=H0(V/I)=0, locally and globally, rather than just rational vanishing. The continuous cohomology exact sequence is legitimate because the underlying finite free coefficient sequence has a continuous integral splitting. It gives the needed peripheral H1 injections.

Hoshi's actual good-reduction inertia alternative and the primitive Magnus centralizer apply in arbitrary rank. The disjoint peripheral lines identify the selected cusp even if other cusps are not rational; unramified splitting does not change inertia. The local peripheral H1 injection identifies the actual cusp parameter. After its inertia adjustment, the conjugator has fixed abelian image and therefore lies in H=P'. This proves the integral H-coboundary assertion at nonzero valuation places. At zero valuation, nonzero specialized cusp inertia would have nonzero primitive abelian image and is impossible. The cartesian specialization square therefore also gives actual zero inertia.

## Topology and fresh-prime perturbations

The principal ideal subgroup is a finite-index free subgroup of the free divisor group. The multiplicative group splits abstractly into its finite roots of unity and a countable free group, including the finite unit-rank part. Its ell-power completion is the discrete finite ell-primary torsion factor times uniform c0. This is the intrinsic ell-adic topology, independently of the chosen splitting.

Compatible roots of the free generators give a continuous linear actual cochain selection on c0. Choosing a representative separately on each finite torsion component is valid and avoids asserting a linear torsion section. Valuation maps are continuous, with finite support modulo every power, because a finite-exponent Kummer class has a genuine number-field representative.

For every finite place v, the class number h makes h*v principal. Removing the torsion component of alpha_v leaves its divisor unchanged and gives an element of the chosen free factor. Hence ell^M*kappa(alpha_v) is an ACTUAL cochain perturbation divisible by ell^M, preserves the torsion component, and changes only the v-valuation by h*ell^M. Choosing a fresh place where the original valuation is divisible by ell^(M+v_ell(h)+1) gives a nonzero new coordinate of exactly the stated valuation. This verifies the density step even when ell divides the class number; no principal-prime restriction is silently added to Chebotarev.

## Finite capture and actual descent

The iterated Frattini quotients have the required exponent bounds and cofinal topology. Fixed torsion component plus free parameters modulo ell^m fixes both the actual finite action and its finite ramification support. At every omitted inertia prime, the full local coboundary reduces trivially because the inner cusp exponent is divisible by that quotient's exponent. Thus the ACTUAL finite cocycle, not just its class, factors through the fixed finite-ramification Galois group. Its finite cocycle set is finite by bounded-degree finite-extension finiteness.

The exceptional finite cocycle produces a real element of its finite affine image with identity action and nonidentity translation. The corresponding conjugacy class is suitable for Chebotarev. The fresh perturbations satisfy all finite tests, and their finite support and nonzero coordinates make the condition open. Finite valuation-support loci are closed with empty interior by the same alpha_v perturbations, so removing their countable union preserves a dense G_delta.

The surviving integral cocycle descends continuously through the actual compact action image. A nonzero inertia subgroup of inner cusp powers is normal there, because every action sends the cusp generator to a unit power. Its fixed subgroup in P' is trivial. The actual local H-coboundary makes the descended cocycle trivial on this subgroup, and the nonabelian cocycle identity then kills every value. The argument includes nonprimitive valuation exponents.

## Full and Fermat scope

The product of the actual component Kummer cocycles is a continuous full procyclic cusp cocycle. The countable product of the residual loci is a dense G_delta in the stated product topology. D.24 applies to two actual full sections, one in the fixed rational cusp packet, and gives the full-profinite uniqueness claim. There is no claim that geometric pro-prime quotients detect arbitrary geometric elements.

The actual Fermat map t=-(X/Z)^n and 1-t=-(Y/Z)^n is the degree-n^2 etale Kummer cover off its3n geometric cusps. For odd n the displayed three cusps are rational. At the selected cusp the local equation is exactly t=-u^n, so the abelian parameter is (kappa(-1)+n*a,0), with the sign term retained at two. The proof is in the actual source group and makes no invalid prime-to-ell open-subgroup inference. Its infinitely ramified generic locus excludes a=0 and changes no statement about D.20's zero-abelian metabelian families.

No mathematical blocker or necessary correction found. This audit supplies no numerical first finite obstruction and no classification outside the stated generic cusp fibres.

## Hypothesis sharpening confirmed

After the initial audit, the owner weakened the hypothesis to at least THREE GEOMETRIC boundary points with ONE chosen k-rational cusp. This is valid without changing the proof. Only the selected peripheral line needs to be G_k-stable; the other boundary points are split over an unramified extension at a marked good place. The zero-intersection argument compares geometric cusp lines and forces the selected, already rational cusp. Thus the stronger three-rational-cusps assumption was unnecessary. The Fermat application remains unchanged.
