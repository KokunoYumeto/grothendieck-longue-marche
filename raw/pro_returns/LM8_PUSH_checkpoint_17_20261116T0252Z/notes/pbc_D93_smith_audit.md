# D93 all-depth Smith refinement: independent PBC audit

**Status: PASS.** The complete written addendum and certificate source were read. The retained independent execution reproduces the entire owner JSON byte for byte.

Draft SHA256: `406785cf35f23c6eb81d7a9c49e0883f53edb9dfc195b83fa51ed123566a21fb`.

Certificate SHA256: `3d9b3759bf0f9c47fea68b738b271cdafbfa64cd4ebbf6d753d0edd38f52e004`.

Rerun JSON SHA256: `721fb2829e29360c46a4a5e46cf8cffa2f2480b46471a635e837c35d86997dd1`.

## Actual module retained

The addendum retains D93’s actual arithmetic identification B_Gamma and changes only the finite integral presentation; no new section-existence or higher lifting claim is made.

## Exact u-cubed sequence

Over characteristic zero, multiplication by u^3 has only the t=1 kernel; the integral coefficient equations identify that kernel exactly with Z5 times Norm. Equivariance is u^3 S_chi^3=sigma_chi(u^3), and the norm action is chi^4.

## Tame quotient and homology

The three augmentation pieces of A/I^3 A, including their possible five torsion, have tame weights 1,2,3. Exact order-four averaging kills their homology in every degree. The weighted finite permutation operator 2 sigma has no invariants, so H1(Gamma,I^3 A)=0 and the norm coinvariants inject as an exact C5.

## Largest orbit quotient

Multiplication by two has one nonzero orbit at each exact 5^j order. The weighted-cycle cokernel is C_(5^j); the zero orbit contributes zero. The quotient in D93S.4 is therefore the stated direct sum, with t representing its largest generator.

## Literal lift identity

Expanded t+(2 sigma-1)G equals u^3 f exactly for G=-1-u/3+2u^2/21 and f=4(t+3)/21. The orbit sum is used in R, where t^(2^ell)=t because 5^r divides 2^ell-1.

## Integral norm subtraction

The exact h1 and h2 formulas are divisible by n=5^r. Subtraction of (t^n-1)(W0+W1 u) produces an integral polynomial u^3 Z. Both binomial(n,2) and binomial(n,3) have valuation r, so Z(1)-h3 lies in n Z5.

## Nonzero extension coefficient

The norm coefficient satisfies n k=16c/21-15 Z(1). Terms from S2,S3 vanish modulo five after division by n; the S4 term gives 2c/(3n). Thus k=2c/(21n) modulo five, equal to one because c/n=3 modulo five. The norm has exact order five, so the lift has exact order 5^(r+1).

## All smaller factors split

After scaling the largest lift so 5^r x_r=Norm, replace x_j by x_j-a_j 5^(r-j) x_r. This kills its 5^j multiple. The induced quotient changes are valid triangular automorphisms of the mixed-exponent direct sum. Exact quotient orders and the total group order establish the claimed direct decomposition.

## Executed certificate

The owner run() was imported read-only. All eight literal moment rows and the symbolic polynomial identities passed; the complete independently serialized JSON is byte-identical to the owner output. This supports, and does not substitute for, the all-r extension proof.

The resulting exact group is the direct sum of C_(5^j), j=1,...,r-1, and C_(5^(r+1)). No additional arithmetic-image, section-existence, or higher lifting conclusion is inferred.
