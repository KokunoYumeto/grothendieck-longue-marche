# Part A coverage map

Statement numbers below are the current A counter; labels are stable. “Settled” means the stated clause is proved or refuted. “Incomplete” identifies the precise remaining mathematical task. Results using the supplied 2026 theorems retain those sources' unrefereed status.

## A(a): the functor, morphisms, rigidity, slimness

| Requested clause | Coverage and result | Status / remaining case |
|---|---|---|
| Conjectures 5.5 / 5.5 bis and category B: objects and functor, scans 21–24, 28–31, 43 | A.1 `A:typed-functor`: exact groupoid, extension, local decomposition, Kummer, and base-change maps. | Settled construction. |
| 1-morphisms and degree condition, scans 44, 50, 54 | A.5 `A:two-morphisms`, A.25–26 `A:positive-degree-open`, `A:relative-hom`. | Settled, including the common Kummer multiplier and actual ramification integers. |
| 2-morphisms, scans 50–52 | A.5: naturality forces the missing right factor mu inverse; independent S3 certificate. | Settled; literal printed formula requires the indicated correction. |
| Aut(f,alpha)=1, scan 34 | A.6 `A:abstract-rigidity` refutes the unrestricted preliminary category; A.7 `A:geometric-centralizer` proves the required geometric/open-image rigidity. | Settled with the exact ambient hypothesis distinguished by actual centralizer groups. |
| Discrete Hom-categories for open geometric image, scans 52–53 | A.7 and corrected A.5 transformation law. | Settled. |
| Slim G_K in characteristic zero, scans 54,109 | A.23–24 `A:local-embedding`, `A:slim`: valuation, weak approximation, and Kummer proof. | Settled for finitely generated K/Q. |
| Slimness in characteristic p | A.24. | Settled: true in positive transcendence degree; finite fields give the explicit counterexample G=Zhat. |

## A(b): case taxonomy, absolute Hom, kernels

| Requested clause | Coverage and result | Status / smallest remaining case |
|---|---|---|
| Case I: points to points, scans 55–56 | A.3 `A:section-eight-cases`: explicit transporter quotient maps to Hom_K(L,L′) by alpha inverse restriction. | Settled. |
| Case II: curve to point, scans 57–61 | A.3: affine-envelope factorization; exact empty-boundary Hom restriction and later relaxation. | Settled. |
| Case III: point to curve, scans 61–65 | A.3 and Part B: exact section-class map; affine tangential counterexample to uncorrected surjectivity. | Incomplete globally for corrected proper point-section surjectivity. Supplied local T1 handles finite p-adic fields. |
| Case IV(a): proper target, scan 65 | A.3, with F.31 `F-local-dichotomy`: open or trivial geometric image, then dominant map or section factorization. | Dominant part settled over sub-p-adic fields; full local case settled using T1. Global constant-image case retains the proper section problem. |
| Case IV(b): proper source to affine target, scan 66 | A.2 `A:proper-affine`: local trichotomy, properness, Jacobian Tate duality, then exact field-extension square. | Settled for finitely generated K/Q and finite p-adic fields, using supplied local T1. No openness/injectivity assumption on the local-to-global Galois map. |
| Case IV(c): filling the boundary | A.3 and A.28 `A:kummer-ambiguity`: literal B has no nonempty-to-empty boundary map; the later filling category has the explicit quotient and relative-to-proper H2 compatibility. | Settled for the specified filling and dominant morphisms; unrestricted global constant-section terms remain as in III. |
| Case IV(d): both boundaries nonempty, scan 67 | A.25 proves positive peripheral degrees force open image through every intermediate cover; A.26 applies Mochizuki with recovered Kummer data and degrees. | Settled over sub-p-adic fields. |
| Absolute open Hom over number fields; LM3 D.11–D.12 | A.37–38 `A:absolute-geometric`, `A:absolute-hom`: geometric kernel preservation, actual field embedding, cartesian arithmetic group, relative Hom, uniqueness. | Settled using supplied unrefereed 2026 Galois open-Hom theorem. |
| Check Uchida's non-surjective open-map step | A.38: original 1981 pp.595–597 and Proposition 1 explicitly assume open image and allow finite target extension. | Settled source check; no certification of the entire 2026 paper is claimed. |
| Absolute Hom over finite p-adic fields | A.39–40 `A:local-absolute-isom`, `A:local-absolute-hom-open`. Explicit dimension-zero Jarden–Ritter fields; positive RNS curve Isom and injective open-Hom reduction. | Incomplete for noninjective open homomorphisms of hyperbolic arithmetic curve groups. The field counterexample is not a curve counterexample. |
| Full outer-action kernel for positive transcendence degree | A.41–42 `A:constant-kernel`, `A:family-kernel-quotient`: exact constant-family kernel, good divisorial inertia, quotient by that inertia, universal-family congruence kernel. | Incomplete for general nonconstant families; the exact remaining quotient is monodromy/congruence kernel. |
| Single-prime kernels, including ell=2 | A.43–45 `A:proprime-kernels`, `A:regular-prime-kernel`, `A:kernel-open`. All kernels nontrivial; constant inverse-image and good inertia formulas; exact tripod kernel for odd regular primes via Sharifi–Brown. | Incomplete for general curves, tripod ell=2 and irregular primes. The conditional January 2026 CM kernel result is not used as a theorem. |

## A(c): boundary and Kummer data

| Requested clause | Coverage and result | Status |
|---|---|---|
| Nonrational cusps and recovery from the geometric inner class of f | A.27 `A:boundary-recovery`, with A.14 and A.24. | Settled: unique cusp, transporter, local map and arithmetic base-path ambiguity recovered. |
| Transp_E(L_i^d,L_i)=E_i, scan 69 | A.14 `A:cyclotomic-normalizer`. | Settled for every positive integer d, including nonrational cusp fields. |
| Kummer data from outer loops and exact ambiguity, scans 47–48 | A.28 `A:kummer-ambiguity`. | Settled: individual units on cusp orbits; common diagonal unit after the privileged compatibility is imposed. |
| Proper Kummer datum and affine-to-proper compatibility, scans 112–113 | A.28. | Settled by the orientation/trace H2 class and the explicit relative cohomology filling map. |

## A(d): conditions (a)–(e)

| Requested clause | Coverage and result | Status / remaining case |
|---|---|---|
| Geometric systems satisfy (a)–(e) | A.30 `A:five-conditions`. | Settled, with the admissible-section addition to (a) explicitly retained for geometric systems. |
| Every multiplier rho, scans 86–87 | A.29 `A:all-multipliers`: full profinite construction, explicit rho=-1 reversal plus Hurwitz substitutions. | Settled. |
| Same handle generators | A.29: central class-two quotient gives (1-rho)omega=0. | Settled: rho=1 for positive genus; every rho for genus zero (no handles). |
| All dependencies among (a)–(e) | A.30–32: (c) follows from the pre-existing local Kummer equivariance/surjectivity; (b) gives the bare section part of (a) with nonempty boundary; explicit countermodels for failure of (e) and of (d). | Incomplete for the rest of the lattice, especially the admissible strengthening of (a) and virtual section existence from the remaining axioms. |

## A(e): inertia, normalizers, commutants

| Requested clause | Coverage and result | Status / smallest remaining case |
|---|---|---|
| Literal maximal-subgroup statement, scan 483 | A.13 `A:literal-normalizer`: pi, characteristic opens and commutator subgroup. | Refuted as written. |
| (1) Cyclotomic criterion, maximality, arithmetic normalizers | A.14, with the actual finite-cover weight proof and transporter. | Settled. |
| (1 bis) Cyclotomic-kernel centralizers and implications | A.16–17 `A:cyclotomic-centralizer`, `A:normalizer-implications`; full F.1 proof for all closed arithmetic subgroups projecting openly to ker chi. | Settled; no unsupported virtual splitting. |
| (2) CM eigenline and LM8 G.3–G.13 audit | A.19–20: exact degree-four derivation, class-four lift / class-five obstruction, all-prime pro-ell normalizer theorem, including ell=2. | Settled in those quotients and all maximal pro-prime groups, with exact source hypotheses checked. |
| (2) LM8 G.19 full group when one prime quotient detects A | A.21 `A:cm-detected-normalizer`. | Settled. |
| (2) LM8 G.20–G.22 full common kernel | A.35–36 force the residual subgroup into the strictly smaller R_nil(F′). A.50–53 give character descent, cofinite-support classification, the positive-density prime exclusion, and necessary CM fields. A.61 classifies every normalizer that admits a virtual arithmetic section. A.62 splits its pro-ell quotient and identifies the remaining extension with a pro-prime-to-ell geometric kernel. | Incomplete: a subgroup supported at permitted primes, possibly a single split prime, inside R_nil(F′), with the nonsplitting extension 1→C→B→G_L→1 of A.62 remaining nonsplit after every finite arithmetic extension. No full profinite example is constructed. |
| (2) Arbitrary affine hyperbolic curve | A.50–53: every cofinite-support A is cuspidal; all A are cuspidal when the normalizer field has no CM subfield. Noncuspidal support requires a CM reflex field embedding into Q_ell for each supported prime. A.61 proves cuspidality iff the normalizer has a virtual arithmetic section, using the supplied local theorem. A.62 gives the exact quotient splitting and remaining prime-to-ell lifting problem. | Incomplete for normalizer fields containing CM subfields, permitted prime support, and the explicit prime-to-ell extension of A.62 failing every virtual splitting. |
| (2) Proper hyperbolic curves | A.64 proves the exact finitely generated pro-prime subgroup freeness needed for the surface case. A.65 extends the character descent, CM/prime-support exclusions and quotient splitting, with no boundary alternative. | Incomplete for the remaining CM/sparse-support extension; no nonzero candidate has a virtually split arithmetic normalizer, and none has cofinite prime support or a normalizer field without CM. |
| (3) Uniqueness of invariant cyclotomic loop structure | A.15 `A:unique-loops`: inertia inclusion becomes equality; quotient H2 and abelian rank identify even the previously unspecified surface type. | Settled, also over finitely generated K/Q. |
| (4) Finite p-adic fields | A.18 `A:padic-cusp-reconstruction`: exact Mochizuki 2004 Frobenius reconstruction under arithmetic group isomorphisms. | Settles the replacement explicitly offered in the prompt. The stronger bare local cyclotomic-procyclic classification is not claimed. |
| Dominant full faithfulness, scan 484 | A.26 with A.1, A.5, A.25, A.27–28. | Settled with explicit groupoid and boundary reduction. |
| Full tripod commutant, scan 485 | A.8 `A:tripod-commutant`: center-free arithmetic pullback plus relative Hom. | Settled: S3. |
| Pro-ell commutant, including ell=2 | A.8, using the every-prime version of Mochizuki Theorem A. | Settled: S3 for every prime. |
| Minimal finite solvable length | A.9–12, A.46–49, A.54–60 and A.66–67: m=1 and m=2 fail; a closed Zhat^× family of pure metabelian arithmetic-centralizing classes; exact same-level S_(2,0) counterexample. For m≥5, projected commutant at m−3 equals S3; maximal prosolvable commutant equals S3. A.54–55 give independently checked numerical obstructions at m=3. The structural A.56 excludes the entire IA image. A.57 proves scalar rigidity already at the peripheral metabelian level; A.58 gives the exact image from every m≥3 to m=2 as S3 over every number field. A.59 constructs unrestricted last-layer arithmetic classes and proves every nonidentity one fails the x cusp. A.60 rules out repairing the three peripheral inversions by normal prime-to-ell Haar blocks. A.66 proves elementwise conjugacy-class preservation one derived layer below after the geometric permutation is removed. The independent full profinite rigidity proof in A.67 gives image(C4^peripheral→Out(S3))=S3, also for every higher source level. | Incomplete: smallest same-level m≥3 is undetermined, including whether any finite such m exists. The remaining m=3 question is exactly the kernel of the third-to-second-derived map on the peripheral arithmetic commutant. Its image, including the scalar part, is now settled; A.67 also determines the entire fourth-to-third projection. No same-level kernel has been silently replaced by a projected statement. |

## Leads and the added Part B task

| Clause | Coverage | Status |
|---|---|---|
| Lead 1, full relation to modern Hom/Isom | A.1–5, A.25–28. | Dominant relation proved. The unrestricted reading is refuted by the exact affine point-section counterexample; corrected global proper point-section surjectivity is not silently replaced by Hom. |
| Relevant Lead 2 connection | A.3, A.16–17, A.33–34, with Parts B/F. | Exact section and cyclotomic-kernel maps proved; no global section-conjecture solution claimed. |
| Relevant Lead 4 / metabelian approximation | A.10–11, A.19–20, A.46–49, A.54–60, A.66–67 and computation files. | Exact quotient maps, arithmetic action, finite certificates, elementwise deck-trace rigidity and the fourth-to-third-derived projection recorded. |
| Added B two-section stabilizer / ker Delta / C_phi | A.33–34 `A:two-section-stabilizer`, `A:root-orbit-stabilizer`. | Settled for the explicitly defined ambient action: chosen root gives G_Q(sqrt(-3)), contained in ker Delta; C_phi contains complex conjugation and is not contained in that stabilizer. The full unordered root orbit instead gives G_Q. |

The largest remaining full-profinite normalizer case is now sharply restricted by A.36, A.50–53 and A.61–65, including the proper-target extension. A.63 refutes the abstract inference that the remaining pro-prime-to-ell kernel automatically gives a virtual section. It explicitly supplies no embedding into a curve group. None of the necessary conditions is represented as an existence construction or as a proof of the remaining geometric case.
