# E.115 focused independent proof audit

Status: PASS for the scope below. Reviewer: `/root/bc_fermat`.

Reviewed source: `research_e115/sections/E_quartic_mixed_five.tex`, supplied stable SHA256 `eb61b16748ffff2ced871ac1c2619018f86e1ebc02474a25e19579f9923ae01a`. The complete text was read, with the independent derivations concentrated on the actual descent map and the final mixed localizer and Chebotarev argument. This is not a fresh program-execution audit and does not replace the author's or root's complete source/rebuild audit.

## Actual descent

The asserted good-reduction based inertia action, once established by the stated tangential specialization, implies the exact source quotient. For `I=ker(G_Q -> G_{Q,S})`, the field F is unramified outside S, so I lies in G_F. Both conjugated tangent lifts above `gig^-1` centralize the centerless free pro-five geometric group. Their ratio is therefore1. This proves normality of the tangent image of I. The displayed map `e -> ([e],pi(e))` and inverse `([e],g) -> e s_F(pi(e)^-1g)` are actual inverse homomorphisms. The quotient does not require identifying an outer action with a based action. The four-coset formulas descend term by term through this map.

## Mixed localizer, sign and convergence

For the ordered cup `b(g) wedge g e(t)`, direct multiplication of the tame relation gives the exact defect `-p v_p wedge e(F_p)`. The localization convention divides by p and uses `d_p=p^-1 F_M-1`. Since the actual peripheral permutation fixes v_p, its inverse on this vector is exactly `v_p wedge j_r (F_E-1)^-1 h(F_p)`. This verifies E115.21–23, including the sign and arithmetic Frobenius convention.

The boundary from `(V tensor Q5/V)^F` sends u to `(F_E-1)u`. The unique representative in `Z[1/5] intersect [0,1)` has valuation `-m_p`, except that the zero class has representative0. Replacing any other representative by this one changes the candidate correction by an integral uniformly bounded vector multiplied by v_p. The family v_p tends to zero because every finite reduction of the cocycle has finite ramification. Therefore this change is an integral restricted family. The scalar divisibility and decay conditions are precisely equivalent to integrality and restricted convergence of the full tensor correction.

## Actual finite translation image and Chebotarev

The actual residual scalar -I has lifts with eigenvalues in `-1+5Z5`; successive `5^k` powers tend to -I. Closedness gives -I in the actual Tate image. The elementary Sah identity uses the invertible scalar -2 and applies to every finite image Gamma_n acting on V/5. Inflation–restriction therefore forces the nonzero h_1 to remain nonzero on the kernel of rho_n. The translation subgroup is stable under Gamma_n, and residual irreducibility makes its reduction all V/5. Nakayama gives the full V/5^n translation subgroup, proving the actual semidirect image.

The added cyclotomic and Kummer2 extensions have only the one-dimensional composition factors1 and chi on their five-kernels. The first next cyclotomic quotient is nontrivial: the five-Sylow of Gamma_n has exponent at most `5^(n-1)`, while the requisite cyclotomic quotient would have exponent `5^n`; adjoining the degree-four field F cannot supply it. The Kummer and next cyclotomic factors have distinct residual conjugation characters. Their common quotient with the two-dimensional irreducible translation module is zero. These actual normal-field comparisons allow the simultaneous Frobenius prescription used in E115.7. Primitivity survives conjugation, and the local equation forces `m_p >= n`.

For the specified primes, `p=1 mod8`, `v5(p-1)=n`, and2 is a `5^n`th power. The whole five-primary tame symbol of `(2,p)` vanishes at p; its other support at2 has no residue five-part. Hence the separate toric input lifts by the previously proved peripheral criterion. Its mixed inertia vector is primitive, so the exact mixed inequality fails when `n > min v5(r_i)`. The exclusion is transferred only through actual quotient maps retaining this class-two group.

No correction was found in this scope. No claim is made here that a finite experiment alone evaluates an infinite cohomological map.
