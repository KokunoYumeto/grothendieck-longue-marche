# Part D and manuscripts 019/031: audit report

Produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed. The primary manuscript, later sources, and previous LM3 report were treated as sources to check, not as certificates.

## Deliverables and scope

`DG.md` contains D.1--D.14 and G.1--G.7. `DG_results.csv` has one row for each of these 21 statements; `DG_readings.csv` records nine places where the mathematics affects a provisional reading. `DG_refs.bib` contains 13 opened primary sources, with the exact theorem or proposition checked in each entry. The word *verified* in that bibliography means that the source was opened and the stated portion checked; it does not certify every argument in the source.

The independent program is `code/dg_checks.py`, with its successful output in `code/dg_checks.out`. It requires Python 3.10 or later and SymPy, and runs with `python code/dg_checks.py` from the deliverable directory. It has no network or file-writing dependencies.

## Main mathematical conclusions

The first assertion of scan 483 is proved for every affine hyperbolic type over a number field. For a peripheral-class-preserving automorphism the determinant on first homology is the common peripheral exponent raised to `g+n-1`. The class-two calculation and the Pfaffian identity are integral, including at 2 and 3. Comparing with the actual Galois determinant makes each candidate exponent potentially cyclotomic prime by prime. Nakamura's finite-cover weight argument, followed by Boggi--Zalesskii's normalizer result, identifies every candidate cusp. For type (1,1), the primitive commutator in the full profinite second lower-central quotient gives exact cyclotomicity without a finite twist. An independent cross-review by the covering/elliptic agent confirmed the full profinite proof and the precise applicability of the cited normalizer theorem.

This proves uniqueness of a whole loop structure in the automorphism orbit of the standard one. The stronger statement for an arbitrary maximal procyclic subgroup is not a consequence. We prove the virtual homology detection needed for Lead 6, formulate its exact weight-one/weight-two dichotomy, and identify the missing implication as potential cyclotomicity on one nontrivial prime component. The smallest unresolved case in this argument is a once-punctured elliptic curve over a number field. A concrete counterexample exists in its class-two pro-5 quotient for the CM curve `y^2=x^3-x` over `Q(i)`: a primitive CM eigenline is represented by a maximal procyclic subgroup whose normalizer maps onto the entire arithmetic group. Compatible lifts through all higher quotients are not supplied and are not asserted.

The reductions to Pop and Hoshi--Mochizuki--Tsujimura retain the extra data those theorems require. Pop uses cofinally many open localizations of M0,5 and the restricted maps `s,t,t-s`; the difference is not a global forgetting map. HMT uses the exact AA predicate with its Belyi diagrams, all relevant covers, Kummer conditions, function fields and second-configuration compatibility. Its answer determines the conjugacy class of the arithmetic subgroup; selecting one copy requires a marking.

For geometric sections we define the ambient centre-free extensions and the conjugation action, retaining their actual arithmetic domains. The stabilizer of the resulting family is exactly G_Q, already at the tripod level, by self-commensuration and the curve Isom theorem. This is an equality under a precise marking hypothesis, not an intrinsic recognition theorem for all abstract sections. Kummer classes, the Nakamura--Schneps cocycle of 2 and their stated relations are then preserved with the correct cohomological ambiguity.

Curve centralizers are Aut_K(U), with the actual moduli dependence and the nonsplit-conic qualification in type (0,4). These are distinguished from Nakamura's centralizers for the *moduli spaces* M0,m. The dominant-morphism category and an explicit essential-image construction are derived: rational Belyi postcompositions allow the prescribed boundary to be included over the original number field, so no hidden extension-of-constants or descent step is used.

## Manuscript obligations

All requested obligations assigned here are proved independently:

- 019 Proposition 5.2: the two rational components, the l parallel nodes with their thicknesses, the toric uniformization and character of slope one, the logarithmic root estimate including p=2 and p dividing m, and a root on the entire inverse image after one algebraic multiplication pullback.
- 031 Lemma 3.1: the polynomial zero estimate by translated components and affine Bezout, then the interpolation determinant and product formula. No Leopoldt conjecture is used.
- 031 Proposition 4.3: the finite quotient amplification, its signed character space, the Frobenius-generation contradiction and the projection that needs only U-equivariance.
- 031 Proposition 5.3: unramified Kummer completion, one finite-character eigenspace of an S-unit group, and a bound independent of both the auxiliary prime and the degree of its twist-killing extension.

G.7 proves the further consequence 031 Theorem 4.4: surjectivity and equality of cyclotomic logarithms for infinitely many auxiliary primes. The exact full cyclotomic criterion in Hoshi Theorem 3.4 was opened; finite logarithmic discrepancies are not silently ignored.

No gap was found in the designated obligations. The scope note distinguishes these proved propositions from automatic certification of the entire 019 or 031 theorem. Remaining reproduction tasks are identified exactly, without labelling an unperformed audit a mathematical gap or creating a spurious Open row.

## Primary sources and scans inspected

For Nakamura 1994, we read Theorems A and B and the complete statements and proof around Theorem 2.1.1 and Lemmas 2.1.2 and 2.1.4. For Boggi--Zalesskii, Proposition 3.6 explicitly permits every nonzero profinite exponent, including a single-prime component. We read Mochizuki 1999 Theorems A/16.5 and C/19.1; Pop 2018 Definition/Remark 2.2 and Theorems 2.6--2.7; the specified HMT definitions and reconstruction theorems; Nakamura--Schneps Theorems 1.1, 1.2, 2.1 and Lemma 2.3; Belyi Theorem 4 and its proof; and Baker--Rabinoff Sections 4.1--4.2, 4.5.2, Proposition 6.1 and Corollary 6.6. The journal originals of Uchida 1979 and 1981 and the revised primary Hoshi 2025 manuscript were opened online. The targeted 019 and 031 source passages were read in the supplied October 2026 versions.

Scans 479 and 483--488 were inspected visually. The mathematics strongly supports the inserted qualification *dominants* and the word *etales* in scan 484; it does not settle spelling, a barred-I convention or the uncertain 245/246 folio numeral. The two different assertions in scan 483 are preserved as different statements.

## Independent computations

The program checked 20, 500 and 12,500 Heisenberg conjugation cases modulo 5, 25 and 125, including integral CM eigenbases; all six tripod Mobius functions in Pop's difference identity; the generic integral 4-by-4 Pfaffian identity; 1,225 strict exponent inequalities for `2<=n<=50`; and 1,949 cyclic-character/stabilizer cases for cyclic orders through 30. Every check succeeded. These finite calculations verify the specific algebraic examples and bounds; they are not used as substitutes for the infinite or analytic proofs.
