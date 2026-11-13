# Integer interpolation and integral models: D.17–D.23

## Result

**D.21 proves the positive-power assertion for every quasi-compact quasi-separated base and every separated finitely presented group scheme.** If a section is fibrewise quasi-unipotent, some positive power is the value at 1 of a global additive one-parameter homomorphism. The base may be non-Noetherian, reducible, nonreduced or of mixed characteristic. Neither flatness, smoothness nor affineness of the group is required.

Together with D.14, this gives an exact correction of the manuscript's unrestricted quasi-compact-base assertion in §50.2, scans 10–13: quasi-compactness alone fails on the explicit non-quasi-separated doubled base; adding quasi-separatedness proves the assertion for finitely presented groups. The correction is stated with finite presentation of the group, rather than silently replacing the manuscript's locally finite-presentation hypothesis.

| Stage | Exact outcome | Result |
|---|---|---|
| Rational regular surface | Settled without a linear model | D.17–D.18 |
| Nonnormal rational domain | Settled without finite normalization | D.17 |
| Reducible and nilpotent rational bases | All Noetherian cases settled | D.18 |
| Integer torsion and nonflat arithmetic bases | Arbitrary local-ring localization lemma | D.19 |
| Noetherian bases | All cases settled | D.20 |
| Non-Noetherian qcqs bases | All cases settled by constructible witnesses | D.21 |
| Smooth integral model for compact adelic image and character | Existence with full source derivation | D.22 |
| Literal whole-M integral-point recap; bare model uniqueness | Refuted with explicit corrections | D.23 |

## Proof architecture

D.17 is an integer-value rational-function lemma. In a Krull Q-domain, a cleared Bézout identity bounds every denominator value by one fixed nonzero element. Finite character leaves finitely many divisor valuations. Away from finitely many integer inputs, each valuation of the denominator is its minimum coefficient valuation. Denominator values at good integers consequently differ by units. Vandermonde interpolation, whose determinant is a nonzero rational number, puts the normalized coefficients in the ring.

For a general Noetherian domain, its normalization is Krull by the precise Mori–Nagata statement in Nagata (1996, Lemma 1.2, printed p. 998). A monic equation for (B−1)/(T−n0) produces a new denominator in the original ring with value ±1 at n0. Interpolation descends the numerator. This uses finitely many integral coefficients and does not assume that normalization is finite. Embedding a finite torsion-free module into a finite free module and interpolating its values supplies the module version.

D.18 treats a primary local Q-ring A by embedding it into its Artinian total quotient ring B. Cohen's coefficient-field theorem identifies the reduced field of B with Frac(A/rad A). The saturated filtration I_j=A∩rad(B)^j has finite torsion-free successive quotients; the unsaturated powers of rad(A) are not substituted for it. D.17 removes rational coordinate denominators successively through this filtration. Over B, restriction of scalars and the unipotent reduction kernel give the initial additive parameter, even for a nonflat group. Integer powers of the section meet an affine identity chart for all but finitely many integers. The resulting chart map extends by integer translations, which cover the relative affine line. Schematic density and separatedness verify gluing and the group law. Finite primary decomposition reduces a general Noetherian Q-ring to these cases; uniqueness at 1 gives equality on each full scheme-theoretic overlap in the closed-patching induction.

D.19 handles arithmetic torsion directly. Start with a parameter over A[1/n] and choose an affine identity chart. Its inverse-image complement supplies a denominator with constant term 1. An n-power dilation clears the finitely many coordinate denominators and makes the denominator congruent to 1 modulo n, so the chart covers every fibre over V(n). Further dilations kill finite n-power-torsion relation errors. The initial scheme map is required to take 0 exactly to the identity: this makes the group-law and commutation error polynomials have zero constant coefficients, so dilation kills those errors as well. The remaining value discrepancy commutes with the parameter value, is fibrewise torsion and is trivial after inverting n. Its finitely generated equalizer ideal is both nilpotent and n-power torsion; successive square-zero kernels kill a positive power. No Noetherian assumption is used in this lemma.

D.20 combines the rational theorem with finite-presentation descent to S[1/n], D.19 and the common-dilation descent of D.12. D.21 then removes Noetherianity. For an arbitrary Q-algebra R, first descend the group and section to a finite-type Q-model R0. Each field-valued parameter witness spreads to a finite-type R0-algebra B; Chevalley's theorem gives a constructible image. A parameter over a residue-field extension descends by uniqueness and fpqc descent, so that image lies in the required fibrewise locus. The witness images form a constructible-open cover after pullback to Spec R. Compactness selects finitely many; emptiness of their constructible complement descends to a finitely generated subalgebra R1 by finitely many explicit ring identities. D.18 over R1 supplies the global parameter. Integer localization and D.12 finish arbitrary qcqs bases.

No representability theorem for Hom_gp(Ga,G) is used. Brion's author PDF (2021, p. 2) explicitly explains why even Hom_gp(Ga,Gm) is not represented by a scheme. The constructible-witness argument avoids that obstruction.

## Manuscript scope correction

Original scan images 211, 212, 213, 215 and 219 were inspected directly. There is a genuine request on scan 213, folio 754, for a smooth model satisfying the preceding factorization and character conditions (45)–(49). It is distinct from the later hypotheses. Scan 215 expressly makes primitive factorization (55) an additional hypothesis. Scans 216–219 add Lie generation, constant components and openness, then define a strengthened integral approximation when these hold. The report does not manufacture a universal existence obligation for all those additional axioms.

A notation discrepancy is preserved: (45) and (47) explicitly have M mapping to integral finite-adèle points M(Ẑ), whereas the parenthetical recap on scan 213 writes M(Z) without a hat. D.22 proves the coherent adelic version. D.23 refutes the literal whole-M integral-point reading: an extended character would take values in Gm(Z)={±1}, contradicting the open cyclotomic image already required in scans 201 and 207. No positive-power proof depends on resolving this discrepancy.

## Smooth-model construction and exact source reduction

D.22 starts from a continuous representation of a profinite group in H(A_f), with H affine of finite type over Q and a specified rational character χ. Compactness gives a stable lattice at every prime, standard outside finitely many primes. The Chinese remainder theorem patches these lattices into a rational global Z-lattice. The character has unit values because each valuation maps a compact subgroup into a finite subgroup of Z. The schematic closure of the graph of χ in GL(L)×Gm is therefore an affine flat model containing the entire compact image and extending χ.

The original Bosch–Lütkebohmert–Raynaud book was opened and checked. Its §7.1 Theorem 5 (printed p. 175) provides group smoothening over a DVR with smooth generic fibre; it has no connectedness hypothesis. The construction by the affine dilatations of §3.2 retains affineness. To retain all Z_p-points while working over Z_(p), §3.6 Proposition 4 (p. 79) first lifts each point, after finitely many dilatations, into a smooth locus. The group-smoothening universal property factors that locus into the canonical smooth model. Thus completion-valued points lift without assuming a Néron model. Only finitely many primes require modification; finite-presentation spreading and patching give the global smooth affine model, and the character extends by composition. Rational points integral at all primes are Z-points, which gives the required discrete factorizations.

The quotient representability proviso in (46) is preserved explicitly. Whenever the quotient is represented, χ factors through it because it is trivial on the relevant schematic closure by generic density. The separate extra conditions (55)–(64) are not asserted to follow from model existence.

D.23 also distinguishes existence from uniqueness of a marked model. For H=Ga⋊Gm and M=Ẑ⋊Ẑ×, the models whose additive coordinates are x and 2x both have the required adelic factorization and character. A generic-identity isomorphism between them would be (z,u)↦(2z,u), which is not an isomorphism at 2. This only refutes uniqueness from the preceding data; it does not invent or refute a theorem with the author's unspecified stronger conditions.

## Sources, checks and exact scope

The primary sources opened for this supplement are Nagata (1996, p. 998, definition and Lemmas 1.1–1.2); Stacks Theorem 10.160.8 (032A), Lemmas 32.10.1 (01ZM) and 32.8.6 (01ZQ), Theorem 29.23.3 (054K), and Lemma 5.23.2 (0901); and Brion's author PDF with its official arXiv version record. The 1955 paper cited by Nagata was not independently retrieved. The proof also uses the source-checked D.11–D.13 lemmas. No novelty or priority is claimed.

The former regular-surface residual display after D.16 has been removed. Its replacement is the paragraph **“Scope after the surface argument”** after D.23 in `sections/D_surface.tex`; `sections/D_nonlinear.tex` now has **“From the curve cases to the quasi-separated theorem”** at the former location. Neither rational surfaces nor non-Noetherian affine bases remain listed as unresolved. D.9 is a proved scope clarification rather than an obsolete compound Open statement.

The complete proofs are in `D_surface.tex`; result, coverage and reading ledgers are in the accompanying JSON/CSV files, with source entries in `D_surface_refs.bib`. `code/d_surface.py` and its JSON/text outputs check the monic-polynomial descent identity in degrees 1–8, the explicit cusp denominator, 27 basis associativity triples for a primary ring whose saturated filtration differs from its naive radical powers, and all multiplication pairs for 16 finite scaling homomorphisms. In particular the characteristic-two nonisomorphism witness in D.23 is checked exactly. These finite certificates supplement the written proofs; no classification of rings or inference of an infinite theorem from samples is claimed. The earlier `code/d_nonlinear.py` certificates remain supplementary as well.
