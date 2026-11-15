# Independent focused audit of A.54

Auditor: `/root/pbc_groups`, 2026-11-15, completed before checkpoint09.

**Verdict: PASS** for the full new geometry/endomorphism argument and exact finite certificate, using the report's established A.11/A.22 normalizer/fixed-group inputs. I read `notes/fgh_A54_draft.tex` in full. I independently executed the exact certificate with a separate output destination: `notes/pbc_A54_certificate_rerun.json` and `.out`. The rerun passed every asserted exact identity and finite-field test.

## Cover and factor identification

The divisor of the division polynomial gives the actual connected degree-five Kummer cover, with 25 total ramification points and genus51. Translation lifts form a central extension of E[5] by the deck C5. Nontrivial peripheral inertia makes the extension nonabelian; equivariance of the fifth-power map under the involution acting by -1 on E[5] and trivially on C5 makes that map zero. Thus the geometric group is the exponent-five Heisenberg group.

The rational matrix algebra M5(Q(zeta5)) gives actual isogeny idempotents and the multiplicity factor of dimension10. The displayed Fourier matrix has the claimed conjugation rules, square, and trace. The two actual quotient genera force residual multiplicities (0,1,2,2), giving factors of dimensions2 and8.

The explicit rational identity for x((2-i)P) and the constant -35-120i was checked symbolically. It identifies the degree-five map to D_lambda, including its constant twist; it is stronger than agreement of branch data. The subgroup is an actual noncentral order-five subgroup and is stable under tau. For a sigma-stable such subgroup, the invariant vector is even in its index, so A^2 acts as +1. Therefore sigma on the quotient's multiplicity homology is exactly T^2. This identifies the SAME A2 and B8 in J_D, rather than merely factors of the same dimensions.

The cyclic20 birational model follows by recovering y and z from W=yz and their coprime powers, then x from y. The automorphism delta=tau c^4 has the stated powers. Its primitive20 projector excludes the original elliptic factor and A2, and selects exactly B8. The quotient by sigma gives the genus-two CM curve and type {1,2}.

## Hodge and Frobenius checks

The four valuation inequalities give the fractional-part differential formula. The resulting dimensions (0,1,1,1,1,1,1,2) contain both a balanced embedding and an unbalanced conjugate pair. Thus no balanced-determinant or quaternion conclusion is used.

The coefficient field and character convention are fixed consistently at each split prime. The q and q^2 sums were independently rerun, including all bins, the norm formula over the quadratic finite extension, determinants, and discriminants. The relative Frobenius polynomial is on the same primitive20 rank-two K-module.

Every residue in the square-class table was checked, including the indicated root of Phi20 and its nonzero quadratic character. The nonsquare discriminants give fields; the nonsquare product proves the two quadratic extensions of the FIXED K are unequal. At each persistent-field witness, trace is a unit and determinant is nonzero with positive valuation. The two roots therefore have different valuations, so their quotient is not a root of unity and no positive power becomes scalar. Hence every Frobenius power generates the same global quadratic K-field.

## Excluding every CM factor

The maximal CM sub-Hodge structure is functorial under all endomorphisms, hence K-stable. A proper nonzero CM part would have K-rank one, and its quotient would also have K-rank one with faithful unital K-action. The latter is itself CM; polarizable semisimplicity would make the whole B8 CM. This avoids assuming a chosen K-stable polarization complement.

If all of B8 were CM, the K-linear Hodge endomorphism algebra has K-dimension at least two by the torus representation. A balanced embedding bounds that dimension by two; consequently it is a quadratic etale K-algebra. After defining its basis over a finite extension, specialization is faithful and its image commutes with a positive Frobenius power.

The centralizer of K and that Frobenius power in the rational special-fibre endomorphism algebra embeds faithfully into the auxiliary Tate-module centralizer. On every K-component the operator has two distinct eigenvalues, so this bounds its K-dimension by two. It already contains the persistent quadratic field L_q and is therefore EQUAL to L_q as a GLOBAL K-algebra. The specialized Hodge algebra has the same dimension and must equal it at both places, contradicting the globally distinct square classes. No comparison of only one local completion is substituted for this argument; no Tate-isogeny surjectivity theorem is used.

## Nonsplit-prime line exclusion

The CM type {1,2} has trivial stabilizer. Labelled Hodge--Tate weights at all embeddings force its four Galois characters to remain pairwise distinct on every open global subgroup. A Q_ell-line in any power of this CM factor would require one character to be invariant along a full local coefficient-field orbit. For ell not congruent1 modulo5 every such orbit has size greater than one, including ramified ell5, contradicting distinctness. The no-CM factor has no potentially stable rational line by the stated Ruppert input. The remaining line must project nontrivially to the original elliptic factor, where the actual [5]q map and established base normalizer theorem exclude it.

The split-prime scope and the separate full pro-five fixed-group scope are accurately retained. Literal TeX errors in the initial draft were reported to the owner; they do not change the mathematics.
