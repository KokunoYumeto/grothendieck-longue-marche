# Part A: mathematical return and audit

This report covers the assigned Part A, Item 1, Lead 2, and the Part A follow-up after LM2. It is a component of the combined return; its completion claims refer to these rows only.

| Requested row | Statements | Outcome |
|---|---|---|
| Item 1 | A.2–A.4, A.17–A.18 | Proved: exact level 12; group of order 32; typed finite quotient and action maps. |
| Lead 2 | A.2–A.4 | Proved in precise form: the action determines the index-three lattice, whose inverse image gives the congruence kernel of order 32. |
| A(a) | A.1, A.5, A.7–A.8, A.10–A.12, A.14 | Definitions and comparison maps established, with source revisions recorded. |
| A(b) | A.5–A.9, A.11–A.14 | Literal false formulas and sequences refuted; corrected sequences and maps proved over arbitrary rings. |
| A(c) | A.2–A.4 | All requested finite computations run and their suggested assertions proved. |
| A(d) | A.10, A.14–A.16 | All requested point groups, multiplication laws, smoothness, flatness, and actual comparisons with §48 proved. |
| A after LM2 | A.17–A.18 | Genuine normalized images, canonical outer images, and scalar lattice images computed; C.d1 checked independently at 12 and proved for every modulus by a braid argument. |
| Support for E follow-up 3 | A.19 | The normalized cyclotomic arithmetic minimum approximation has abelian image; its exact kernel group is exhibited. |

## Main findings

The free subgroup Π₀ has index 12 in SL₂(ℤ), but its congruence level is 4. The additional lattice

`M₀ = {(c₀,c₁) ∈ ℤ² : c₀+c₁ = 0 modulo 3}`

has inverse image Π₀₀ of index 36 in SL₂(ℤ). It is the normal closure of δ = λ₁λ₀⁻¹, and also Π₀ intersected with the commutator subgroup of SL₂(ℤ). Its exact congruence level is 12. Chinese remainders identify its reduction with `V₄ × Q₈`, of order 32. The quaternion identification is certified by the unique involution and six order-four elements.

There are three different finite quotient maps, all given explicitly. SL₂(ℤ/12) has order 1152 and quotient of order 36 by this kernel. The actual reduction of GL₂(ℤ) has determinant ±1, order 2304, and quotient of order 72. The full GL₂(ℤ/12) has order 4608, and quotient of order 144. The commutator `[λ₀,λ₁] = [[1,4],[4,5]] modulo 12` proves that full reduction does not factor through the minimum metabelian modular quotient; reduction followed by quotient by the order-32 group does.

The corrected multiplier scheme is four open affine lines, and the corrected N is the explicit scalar semidirect product `Ga² ⋊ O₁₂*`. The lattice equation must be imposed in the vector group of M₀. Imposing it only after the map to M introduces a coordinate `z` with `3z=0`; the corrected N is its schematic closure `z=0` away from 3. The old fine scheme of scan 41 maps isomorphically to this corrected N over ℤ by `k=ν′−a₁`, `ν″=a₁`. This resolves the precise finite-stage comparison left in LM1 E.20, including bad-characteristic fibres.

The final normalizer bisection has explicit central cocycle `(a+b)b′ modulo 2`, the pullback of the dihedral extension `1 → C₂ → D₈ → C₂² → 1`. The early literal definition (171) reaches only the equal-sign two-component subgroup; its asserted surjection to all four components is false. The later formula (212) supplies the corrected full bisection. Actual central quotient morphisms relate the earlier and final versions of Γ and M.

Each of the three final distinguished subgroups is a graph isomorphic to Γ, with eight geometric components and relative dimension two. All are smooth and flat at both 2 and 3. Their point groups have orders 32 over F₂ and 72 over F₃, and the exact group laws and localization parametrizations are written in A.15. A.16 constructs character-base pullbacks from the §48 matrix groups and homomorphisms with specified norm-one kernels. The old and new fibres are then compared using these actual maps and coordinate rings.

For the standard Belyi/braid normalization, all of G_Q, GT-hat, and GT-hat₀ have level-12 matrix image

`{ [[μ,t],[0,1]] : μ = 1,5,7,11; t = 0,4,8 }`,

of order 12. Its genuine conjugation image in Aut(GL₂(ℤ/12)) also has order 12; its image in Out(GL₂(ℤ/12)) is trivial. Its canonical outer image in Out(SL₂(ℤ/12)) has order four, and its scalar image on M/12M has order four. The arithmetic kernel field is exactly `Q(ζ₁₂, cube_root(2))`. This equality is proved by the tangential Puiseux expansions of the Legendre three-division polynomial, independently of a pointwise Kummer-coordinate identification.

## What was read

The full development prompt and the relevant checked transcriptions and research notes for C4 scans 20–95 were read. The actual attached images inspected are scans 20, 35, 41, 59, 60, 61, 62, 63, and 64. The formula revisions on scans 51–58 and 65–94 are based on the supplied transcriptions; their images are absent from this attachment. The readings ledger states that limitation at each affected row and does not declare the handwriting settled.

The matrix source anchor in the prompt is incorrect: attached scan 20 concerns the general §50 extension construction. The Fermat section and displayed λ matrices occur at scan 33, folio 664, in the transcription. The paper's dictionary uses that corrected anchor.

LM1 E.15–E.16 and E.24 were independently checked through the amalgam presentation, integral affine cocycle, and a direct coordinate comparison. LM1 B.2–B.5 were checked through their equations: the quadratic norm forms, determinant maps, graph subgroups, and bad fibres are derived again in A.16. LM2 C.d1, C.r1, and C.a16 were read independently. The new braid proof avoids importing the unopened Herfort–Ribes theorem from the prior return.

Three primary sources were opened and checked: Kirschmer–Leedham-Green §4 equation (1); Lochak–Schneps Lemma 5; and Harbater–Schneps Proposition 4, with its explicit full profinite braid application and arithmetic normalization. Their exact URLs, theorem locations, and verification evidence are in `a_source_evidence.json`; all three bibliography entries are marked verified. No claim of novelty or priority is made.

## Computations run

| Program | What it verifies | Saved results |
|---|---|---|
| `a_finite.py` | All level-12 matrices; normal closure and normality; actual integral GL image; quotient orders; action for every N dividing 24; Bass–Serre graph; all signed LM2 C.d1 matrix solutions; D₈ cocycle; raw point counts. | `a_finite.out`, `a_finite.json` |
| `a_braid.py` | All finite commutator values in the normalized braid action; generation test; twelve distinct intertwiners; three-division polynomial specialization and leading Puiseux cubic. | `a_braid.out`, `a_braid.json` |
| `a_schemes.py` | Integral coordinate identities; chart multiplication; central cocycle; counterexamples to literal formulas; raw bad fibres; explicit finite group isomorphisms of the stabilizers. | `a_schemes.out`, `a_schemes.json` |
| `a_metadata.py` | Matching statement ledger, readings ledger, coverage rows, and local source evidence. | `a_metadata.out` and `ledger/a_*.json` |

Every mathematical computation described in A has been run and its assertions passed. The proofs explain the infinite and scheme-theoretic conclusions independently of finite sampling.

## Corrections to the source and prior notes

The pushout ring requires the factor N in the term Nxy. Equality of evaluations does not imply equality of sections. The full evaluation kernel retains all residue components, not only the N-torsion additive component. The integers ±5 are affine representatives rather than global integral unit sections. For the representative `(−5)^a 5^b`, the correct mixed coefficients in ν′ and ν″ are −6ab and −4ab. The second-pass note checking consistency of two later equations missed their incompatibility with this earlier product representative. The scan 61 signs, the scan 76 exponent, the literal scan 82 image, and the missing quotient in scan 87 have explicit mathematical corrections.

The final line of (194) without the question mark also requires correction: `N_rho / μ_rho` retains a C₃ kernel, whereas `N_rho^? / μ_rho` is γ. The invariant σ-line is generated by λ₀+λ₁, resolving the λ₁+λ₂ subscript in (204). In the expression `U=x u_μ`, the variable x belongs to the geometric group; inserting u_μ into x again is a type error and is replaced by the graph equation U=a.

## Independent audit of D.15–D.18

The projective CM field argument was checked separately. The ±1 quotient field contains the Weber values, so CM reciprocity places the full maximal abelian extension inside it; the commutative CM-linear Tate image gives the reverse inclusion. The residue-unit adjustment by μ₆/±1 and μ₄/±1 fills the stated individual target factors. The intersection argument is complete: two distinct abelian index-two subgroups force the derived group to have order at most two, and the splitting field of X⁴−3 realizes that nontrivial possibility over both imaginary quadratic fields. The Hilbert-90 local valuation-parity calculation and the saved finite norm tables agree.

The initial pointwise −8κ₂ identification had a possible shear ambiguity. This was sent to the D author and corrected by fixing positive real Tate roots and the Legendre branch-cut period ratio. The resulting choice matches the braid normalization in A.17; the local monodromy matrix alone would not have fixed it. With that correction, no further gap was found in these four claims.

## Remaining questions in this component

No mathematical row assigned to Part A remains undecided in this component. The manuscript's absent images remain an editorial limitation, explicitly separated from the algebraic proofs and counterexamples. Broader realization and splitting questions assigned to other parts are not declared solved here.
