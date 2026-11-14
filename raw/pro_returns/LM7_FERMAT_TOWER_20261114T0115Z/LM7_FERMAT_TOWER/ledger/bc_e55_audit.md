# Independent audit of E.55

Status: PASS.

Read the entire mixed first-coordinate theorem and proof. Reopened Wingberg’s original Theorem2.4 and its proof, including the implication for infinite sets of primes, the K(pi,1) conclusion, and the preceding local realization statement:

https://www.mathi.uni-heidelberg.de/~wingberg/agwingberg/paperwingberg/Riemann-kpi1.pdf

The local group is correctly typed in the relative pro-three quotient over C₂. Its order-two Frobenius component is available there. Wild inertia is killed, the tame pro-three inertia injects by Wingberg’s theorem, and the unramified subgroup injects through its cyclotomic character. The chosen local Frobenius complement fixes the compatible roots of the uniformizer; all three-power roots of3 lie in Q_ell because cubing is an automorphism of its units.

The conjugation choice of c and the explicit change of first cocycle are correct. The anti-c element γ₀cγ₀⁻¹c has cyclotomic character1, vanishing ell-Kummer coordinate, and twice the nonzero three-Kummer coordinate. Its unit power is an actual free Frattini complement to the primitive local Frobenius. The displayed t,σ,ρ action is therefore on actual arithmetic elements.

The free-product isomorphism follows from the stated inertia kernel and the coset-tree comparison. Equivalently, form the continuous induced inertia bundle P×_(<σ>) I, with the identification (pσ^z,t^u)=(p,t^(q^z u)). Its free pro-three product semidirect P maps inversely to D*_3<ρ> by the explicit generator inclusions. On the arithmetic side the same maps send every bundle factor to its actual inertia group. This proves the exact kernel comparison and the full c-equivariant section.

Checked all four cocycle equations, the residual anti-invariant geometric conjugations, both principal-ideal equalities, and the finite orbit count. The numerator in the Frobenius value transforms under inversion by T^(−qA), whereas the denominator transforms by its negative; the quotient is therefore anti-invariant, has augmentation zero, and lies in J. The normal-form division is integral and unique. The even-series parameter for the rho-value and its topology are exact.

The global additive reconstruction retains the actual splitting. Conjugation corrections from its inertia kernel disappear only after passing to the explicitly additive J_A target; the proof does not discard a nonabelian correction. At each further prime the fixed-point measure lattice is3 Z₃ δ_x, and restricted support is both necessary and sufficient in the continuous-bundle topology.

The toric correction E55.14 is exact. Since c fixes σ and the chosen rational Kummer cocycle vanishes on c, κ_p(σ)=−κ_p(σ), hence zero. The reconstructed residue cocycle vanishes on the whole ell decomposition group, so its ell valuation is zero. Its rho-value is zero; κ₃(3)(ρ)=1 then determines the sole remaining coefficient at three. Adding the explicit unramified normal form gives the stated rational prime Kummer coordinate.

A fresh copied execution of e_two_prime_first.py produced JSON identical to the retained certificate: five arithmetic models,15 orbit systems,39 normal-form recoveries,702 integral series coefficients, and11,172 residue/order/discrete-log/affine checks. The fresh source and output are retained in research_e55_bc_audit.

No mathematical correction was required. A precision suggestion was sent to specify that conjugacy by L compares prolongations of the same prime of K_S(3); motion among those primes is governed by the separately imposed quotient-group equivariance.
