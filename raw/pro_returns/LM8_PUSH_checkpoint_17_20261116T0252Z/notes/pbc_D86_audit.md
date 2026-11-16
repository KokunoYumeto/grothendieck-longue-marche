# Independent D86 audit

Status: **full proof and independently executed certificate PASS**. This candidate remains unregistered during the checkpoint-14 canonical freeze.

Audited draft: `notes/de_sha_cusp_infinite_torsion_draft.tex`, SHA-256 `dd6f314fe25fa126a3635099dcca302277050fb2398107d912a03f0b813882de`.

## 1. Actual images and coinduction

Primitive away-five inertia gives the full rank-one translation lattice. The common local gauge gives 5H locally. Translation coinduction identifies the actual restriction map with B^D into R^D, and its complete kernel with the displayed connecting quotient.

## 2. Eisenstein ideal identification

Multiplication by u identifies J=u Lambda/(uS) with Lambda/(S)=O[[v]]. The annihilator is exactly (S), using cancellation in Lambda. This retains the actual u factor in every action.

## 3. Exact torsion/boundary sequence

Cancellation of vw in O[[v]] gives E=vwA/(uvwA)=F5[[v]]. Modulo v, w=u is a nonzero divisor, proving (v) intersection (w)=(vw); the two boundary modules are O with finite quotient F5.

## 4. Torsion-layer action

The original Alexander multiplier and substitution on the actual P generator give chi^(-1) S1^2 S2^2 S12. On u=0 modulo five this is chi-bar times S_gamma(1+v)^3, with beta exactly trivial on the axis.

## 5. Countable product coinvariants

Multiplication by v^3 identifies E with the twisted group-ring ideal. The omitted three jets have nontrivial C4 characters, so exact C4 averaging removes them. Continuous twisted invariant functions are finitely supported shell functions; duality yields the compact product of F5.

## 6. Finite boundaries

The exact reflection gauge gives the two augmentation-square modules for C5. Their actions factor through C4 and their coinvariants are Z5 each. The finite cokernel has nontrivial C4 weight.

## 7. Snake map and topology

The image of the finite-rank Q-invariants in exponent-five E-coinvariants is finite, and quotienting removes only finite dimension. Continuous lifts of a Z5^2 basis split the free compact quotient; this does not assume injection of E-coinvariants.

## 8. Restriction-kernel exponent

D77 supplies exactly two additional divisible local boundary factors. Their injection fills the rank-two maximal divisible subgroup: its dual is a surjection Z5^2 to itself. The residual connecting kernel is therefore countable direct-sum F5, giving the genuine upper bound.

## 9. Independent lower classes

The actual J/uJ quotient has action chi-bar times S_gamma. Its invariant dual has infinitely many shell coordinates. Intersection with the divisible boundary image has F5 dimension at most two, so the connecting image is infinite.

## 10. Concrete global cochains

The coefficient-of-u extension in R/5R restricts to the given functional on J, has finite v support, and its coboundary lies in B^D. Inflation through the actual operator image is injective in degree one.

## 11. Uniform Frobenius primitive

For h=0 mod5, the first-u extension itself works. For chi not 1 mod5, integral translation conjugation removes h. In the remaining case the degree-one symbol of chi^(-1)rho-1 is h-bar*u; it injects every homogeneous piece and yields a surjective dual map M_(n+1) to M_n.

## 12. One finite global level

The c0 condition makes the primes with nontrivial inertia on M_(n+1) finite. All other primes use the same uniform Frobenius bound. At the exceptional nonzero-inertia primes, D43 plus the audited finite-duality/ML argument kills H1(D); finitely many additional primitives fit one common finite module. Previously valid primitives remain valid on inclusion.

## 13. Remaining factors and scope

D77 gives one unchanged zero-axis product and two local depth-one factors. The compact K splitting is distinct from the nonseparated unrestricted cochain quotient. The example kappa(26) has global primitive coefficients and logarithm-depth one. No torsion assertion is made about H1 or the whole section fibre.

## Execution gate

The complete certificate source was read and independently executed through runpy under a non-main module name, preserving the author output byte-for-byte. All mathematical JSON fields agree, including 540 exact low-symbol operator injections, first-u equivariance, shell dimensions, both integral boundary gauges, and Smith diagonal (1,1,1,0). The independent result is notes/pbc_D86_independent_rerun.json and the execution/hash ledger is notes/pbc_D86_independent_rerun.out. Source SHA-256 d0e082fc0e749e6fafef592e5d1a645c001a30378012a36b180be71f61da0fe9; both author and independent result SHA-256 3aeb3b16c72728a5116c8881e05435bcdf7bf7f048f98c14961ba99b066cd6c1. Runtime 1.1443 seconds. The samples support the formulas; the infinite cohomological conclusions rely on the full proof audited above.
