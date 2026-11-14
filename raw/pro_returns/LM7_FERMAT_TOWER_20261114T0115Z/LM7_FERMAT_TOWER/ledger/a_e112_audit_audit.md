# Independent E.112 audit

**Result: PASS.** I read the complete 521-line proof, all 213 lines of the Python driver, and all 74 lines of its GP source. I independently rebuilt the arithmetic from copied sources, compared every textual/JSON output without exclusions, compared the entire deserialized PARI object and all 156 retained components, and wrote a separate exact coefficient verifier. No mathematical correction is requested.

## Audited snapshot and execution

The audited theorem is `research_e112/sections/E_quartic_five_cohomology.tex`, SHA256 `3b9c685b92d973c3e6ced92bf1d79c9e0cc1a84488ed9878aca84b09a30d10a4`. The Python source has SHA256 `38a6d7568efd616e4d19b04d21e6799ebdeb65ba46c519993f297d4c348fad20`; the GP source has SHA256 `47b816a946fc253b8b6ca4b922bd785026bf118eb5c779e1d041e7b88ba5a47b`. `input_snapshot.json` records the complete seven-file snapshot.

The fresh command was:

```text
python a_e112_audit/fresh/code/e_quartic_five_cohomology.py --gp /workspace/scratch/e34c61ec5a35/research_e52/vendor/pari-2.19.0/gp > a_e112_audit/fresh/code/e_quartic_five_cohomology.out
```

It exited 0. The entire Python stdout and JSON are byte-identical to the retained author output, as is the entire GP stdout. The copied source hashes are unchanged. `comparison.json` records all comparisons. The two binary serializations have different hashes; `compare_binary.gp` reads both complete objects and proves exact PARI equality of the whole twelve-record vector and each of its 156 components. No binary field, cache or numerical component is excluded from this equality.

The independent `check_maps.py` imports no author program. Its custom exact Gaussian/radical arithmetic checks 12 cleared-denominator point/duplication identities and 32 actual radical rotations. It independently enumerates the six character kernels, proves they cover all sixteen characters, checks 256 Fourier inverse identities and 96 norm/fixed-module inverse identities modulo 5^5, and tests every vector modulo 25 for 70 chosen inert Frobenius matrices: 43,750 fixed-vector/projector cases. It also reconstructs the Tate-untwisted character lists and verifies the central finite free rank 66. Its complete source, stdout and JSON are retained.

## Literal division fields and coefficient characters

The two independent Eisenstein arguments are valid. The first extension is unramified at the other Gaussian prime because its polynomial discriminant has support only at 2 and its own radicand prime; the second radicand therefore retains valuation one. The resulting degree 16 over K, degree 32 over Q, and stated semidirect conjugation law follow from the actual radical maps.

The displayed points really lie on the two indicated elliptic curves. Their actual duplication identities identify the two CM eigenlines with eigenvalues 2 and -2 modulo 5, rather than merely identifying an abstract order-four character. The coordinates recover i and both radicals. The Weil pairing supplies the inclusion of mu_5. The explicit quadratic-twist isomorphism and its inverse give precisely V chi_2 = T_5 E_2.

Consequently the second Tate character is 2^(-s). The U(-1) characters are 2^(r+s) and its inverse. The correct fixed character field is K(ab), the vector (1,1), while the cyclotomic field corresponds to (1,3). I checked this sign separately in the independent verifier.

## Certified small fields and the class-group transfer

Every subfield map is retained as an actual polynomial substitution in the degree-32 algebra. The exceptional real-radical compositum retains both its radical and its copy of K. All twelve fresh default `bnfcertify` calls returned 1. The class numbers and the local (e,f) lists reproduce the full table exactly.

For a kernel C of order four, ideal extension and norm satisfy N j = 4 and j N = sum_C. The inverse on C-invariants is (1/4)N; this proves both inclusions of the claimed invariant isomorphism on the five-primary class group, including at ramified primes. The six kernels cover every character of the group (C4)^2. The integral Fourier idempotents exist over Z_5 and sum to the identity. Their images vanish by those six fixed-module computations. This proves the full five-primary class group vanishing without a certified computation of the full degree-32 class number.

## Finite-S cohomology and all finite exponents

The residue characters of N(-1), for every indicated N, factor through exactly the listed faithful degree-four character fields. The actual local degree tables show full degree-four image at both 2 and 5, so their fixed spaces vanish. In the V case the inverse characters have the same kernels; in the twisted cases the E_2 field gives the same argument through its actual twist map.

The restriction/corestriction comparison for the order-32 extension is valid on the S-ramified source: the normal closure over Q of any extension of L unramified outside S_L is still unramified outside S. Thus the corresponding source subgroup is exactly G_(L,S_L). Averaging annihilates the positive-degree quotient-group cohomology, and (1/32)cor is the inverse on invariants.

The finite Kummer sequence and the proved S-Picard vanishing identify H^2(mu_5) with the five-torsion Brauer group. Tensoring with N(-1) uses the evaluation map mu_5 tensor N(-1) -> N. The Brauer local invariant map is equivariant with the ordinary permutation action on primes: an isomorphism between local fields preserves the invariant. Its tensor invariant summands are precisely the decomposition-group fixed spaces just shown to vanish. This proves H^2 modulo 5.

Coefficient exact sequences propagate H^0 and H^2 vanishing to every exponent. The Euler characteristic with one positive and one negative real eigenline gives order 5^n for H^1. Reduction maps are onto because their connecting target H^2(N/5) vanishes. Multiplication by 5 factors through the onto reduction to exponent n-1 and the injective coefficient inclusion; hence the quotient by 5 has order 5, which proves cyclicity of the entire group of order 5^n. The compatible generator construction corrects actual cocycles by lifted zero-cochains, so it yields the stated continuous coordinate map and its inverse. Finite cohomology kills the two relevant derived inverse limits.

## Unrestricted primes and topology

For V, V chi_2, V(1), and V(1) chi_2, the integral inertia value at every prime outside S lies in a Frobenius fixed module that is zero by the actual Weil eigenvalues. Vanishing extends to the closed normal closure of these inertia subgroups, which proves the inverse descent to G_(Q,S), including coboundaries.

For U, no split prime has a fixed vector because equality of the two elliptic Frobenius roots would require a_p^2 = 4p. At each inert prime the actual off-diagonal Frobenius entries are units, their product is -p, and the stated fixed-line section and row are integral mutually inverse maps. The independent verifier checks these maps on complete coefficient-vector sets, not only on a chosen generator.

Finite localization is onto the indicated residue value because H^2 over S is zero. Its fibres are nonempty finite sets. Every finite compatibility problem is solved at its largest exponent, so compactness supplies an inverse-limit class. The lifted zero-cochain correction yields an integral continuous cocycle xi_p with the exact tame value w_p. These cocycles have a common integral bound. Therefore the sum over a restricted residue family converges uniformly, with exactly the prescribed inertia values. Conversely every finite coefficient reduction cuts out a finite extension ramified at finitely many primes, which proves the required restricted support. Subtraction of the actual convergent sum leaves the unique finite-S scalar coordinate. Coboundaries have zero inertia at these primes. These facts verify both directions and the coefficient-congruence topology of (E112.18), without replacing the restricted sum by an unrestricted product or by a closed denominator.

The rational comparison follows from compactness of every cochain domain: a continuous Q_5-valued cochain has a single denominator bound. Filtered scalar extension of the cochain complexes is exact. A sequence tending to zero likewise has a single denominator bound. This proves the stated rational versions with their actual maps.

Finally the E.108 coefficient projections and sections give the literal direct summands. The ranks 30 + 15 + 18 + 3 = 66 and the three kinds of residue factors match those maps. The section-fibre statement uses the existing central cocycle action and inverse ratio, with no assertion that every quartic abelian input lifts.

## Primary passages independently reopened and read

- Milne, *Arithmetic Duality Theorems*, https://math.stanford.edu/~conrad/BSDseminar/refs/MilneADT.pdf: II Proposition 2.1 and its complete divisor/Brauer proof, II Remark 2.2(a), II Proposition 2.9 and its complete Galois–etale comparison proof, II Proposition 0.1(f) with proof, II Remark 1.7(b) through the complete local purity argument, and I Theorem 5.1 with its complete proof through Lemmas 5.3–5.4. The comparison is at printed pp.170–172, PDF indices177–179; the purity computation is printed pp.151–152, PDF indices158–159. Retrieval references are retained in `audit.json`.
- Jannsen, *Continuous Étale Cohomology*, https://epub.uni-regensburg.de/26684/1/jannsen12.pdf: Proposition 1.6 and full proof, Lemma 1.15, and Theorem 2.2 with full continuous-cochain proof. These justify precisely the inverse-limit comparisons used here.
- PARI official manual, https://pari.math.u-bordeaux.fr/dochtml/html-stable/General_number_fields.html#bnfcertify: default flag 0 and return value 1 certify the full BNF without the GRH assumption. The weaker flag-1 option is not used in any of the twelve computations.

The retained interrupted whole-field certification and parser failures are outside the proved certificate and were not reused as successes.

## Final author freeze validation

The final author manifest `research_e112/ledger/e_quartic_five_cohomology_manifest.json`, SHA256 `ce7a58496ba4de2512e3f18a6ce794f4a2a3c2c1fdfb3357cfc2736912c02189`, was validated after the audit. All 34 files match their recorded byte sizes and hashes. The theorem and numerical sources/outputs equal the audited snapshot. This validation does not claim a new visual review of the author's standalone PDF.
