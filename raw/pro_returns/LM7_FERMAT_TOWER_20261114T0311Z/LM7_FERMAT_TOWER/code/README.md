# Reproducing the mathematics and paper

The `.out` files contain actual saved output from the accompanying programs. The `.json` and `.csv` files retain exact coefficients, witnesses and coverage data. The programs use integers, rational numbers and finite rings. Elapsed-time fields are measurements that vary with the machine; all mathematical coefficients and certificates are exact.

## Requirements

Use Python 3 with SymPy and NumPy, a C++17 compiler available as `g++`, and TeX Live with LuaLaTeX, BibTeX, Latin Modern and the standard AMS/table packages used by the master source. The mathematical programs use no external group-theory system. The finite fundamental-unit computations in E.52 additionally use PARI/GP; version2.19.0 was executed, and its official source hash is recorded in `ledger/e_two_line_source_evidence.json`. Every `bnfinit` result used in those calculations is certified by `bnfcertify`. The programs can be run from any current directory. The small-group input is supplied, so reproducing the mathematical results with the listed runtimes installed does not require network access. The optional PDF rendering check also uses Poppler's `pdftoppm`, PyMuPDF and Pillow. Runtime versions for the original calculations are recorded in `runtime_versions.json`; the added PARI version and source provenance are recorded separately as just specified.

## Mathematical programs

| Program | Calculation and retained evidence |
|---|---|
| `a_finite.py` | Modular subgroup, quotient actions for every divisor of24, order32 subgroup, and congruence quotient witnesses. |
| `a_schemes.py` | Integral coordinate identities, finite fibers and the finite central-extension law. |
| `a_braid.py` | Normalized braid/congruence intertwiners and level12 action images. |
| `a_mixed_module_explore.py` | The exact two-dimensional quotient modules of the rank97 congruence lattice, with saved relation matrices. |
| `a_mixed_prime_cover.py` | Mixed-prime covers over the order2304 quotient, including the rank385 kernel and all quotient edge coordinates. |
| `a_mixed_prime_generate.py` | The correction and generation equations for the mixed-prime action, with exact finite witnesses. |
| `a_mixed_prime_compatible.py` | The compatible mixed-prime lift, all385 basis images and the54,658-letter cusp word; exact maps to the common quotient. |
| `b_fermat_modules.py` | Integral Fox modules, cusp maps, deck/permutation matrices and Smith forms for levels1–8. |
| `b_freeness.py` | Finite scheme-action stabilizers, including bad-characteristic examples and the diagonal kernel. |
| `b_splitting.py` | The actual splitting cochain and all finite multiplier/permutation pairs for the specified levels; cohomology Smith data. |
| `c_cuspidal_exponent.py` | Cuspidal relation-lattice Smith forms and the exact exponent certificates for levels3,4,5,7. |
| `d_metabelian.py` | Exact Lyndon-basis special derivations, inner quotient, invariant subspaces and metabelian images through weight10. |
| `d_gamma.py` | Independent Fox projection on every Lyndon basis word through weight10 and the full-GT gamma line. |
| `d_kummer_soule.py` | Rational-prime Kummer annihilators and every requested Soulé character residue through prime50. |
| `d_kummer_measure.py` | Independent Fox/Schreier coefficient extraction and exact metabelian commutator identities. |
| `d_local_cm.py` | Exact local Kummer indices and the two local CM norm images, with the finite dihedral intersection witness. |
| `d_lifting.py` | The exact A5 quotient, all normal closures and the two five-cycle conjugacy classes detecting the peripheral failure of an unrestricted profinite lift. |
| `d_cm_shadow.py` | The 576-element congruence quotient, its rank97 Bass–Serre module, every one of48 conjugator pairs, all saved mod2/mod3 correction and generation witnesses, and the finite GT0 hexagons. |
| `d_cm_refine.py` | The integral correction map with Smith cokernel C2, its augmented unimodular image, all24 compatible witnesses through powers of2 and3, and384 general-m hexagon checks. |
| `d_cm_class2.py` | The rank4656 central three-layer, its rank135 averaged coordinates, all correction and centralizer freedom, and the exact rank130 final test. |
| `d_cm_class2_two.py` | The full rank4753 central two-layer, multiplier and all52 lower centralizer directions; exact final correction rank4748 and survivor certificates. |
| `d_cm_quadratic_search.py` | Five quadratic obstructions on the98-dimensional homology-correction space, a rank97 alternate CM witness, and direct evaluation of its470844-letter corrected cusp word. |
| `d_cm_exponent4.py` | A full lift in the truncated Magnus model modulo4, including the exact15-dimensional obstruction map and the1,816,936-letter corrected cusp word. |
| `d_cm_pro2_class2.py` | The stabilized two-level correction module, its surjective15-dimensional obstruction map, and a checked next word modulo8; certificates for the entire relative class-two pro2 tower. |
| `d_cm_rank4_refine.py` | The actual rank4 relative completion, full degree6 Magnus layer of dimension690, the240-dimensional third-commutator image, and the two initial correction ranks. |
| `d_cm_rank4_centralizer.py` | All152 generators of the lower centralizer, every same-action correction, and separating functionals proving the two earlier selected central representatives nongenuine. |
| `d_cm_rank4_joint.py` | The rank28 simultaneous correction, the replacement cusp word checked in both complete Magnus models, exact common-quotient orders, and the stable compatibility retaining the new class3 kernel. |
| `d_cm_rank4_degree7.py` | The full1860-dimensional third-commutator image through degree7, its50-dimensional obstruction quotient, all65 simultaneous correction equations, and direct evaluation of the4,903,248-letter replacement in both complete Magnus models. |
| `d_cm_degree7_reduction.py` | The explicit reduction map to the previous degree6 target and its nonzero central action difference, keeping the unchanged homology and CM data separately recorded. |
| `d_cm_degree8_seed.py`, `d_cm_degree8_linear.py`, `d_cm_degree8_magnus.py`, `d_cm_degree8_centralizer.py` and `d_cm_degree8_sylow.py` | The degree8 cusp error, all lower centralizer directions, the exact separating functional, forty independent Magnus identities, and the relative pro2 Sylow/Frattini comparison. The full sparse linear certificate is retained. |
| `d_cm_degree8_high.py`, `d_cm_degree8_common.py`, `d_cm_degree8_gamma3.py`, `d_cm_degree8_joint.py`, `d_cm_degree8_reconstruct.py`, `d_cm_degree8_joint_word.py`, `d_cm_degree8_stable.py` and `d_cm_degree8_stable_word.py` | The exact common quotient and abelian correction group, all139 coupled obstruction coordinates, the12,921,196-letter replacement, and an18,077,708-letter continuation retaining its full degree8 action. |
| `d_cm_rank4_structure.py` | The exact elliptic cover and all 18 deck matrices, 54 cusp conjugacies, 1296 extension-cocycle identities, the integral filling map and the retained compact Tate matrix modulo 16. |
| `d_cm_rank4_odd_lift.py` | Both marked surface basis changes, every boundary automorphism and inverse, four integral cusp shears, the complete group SL2 modulo 16, the norm-one CM unit, and the Frobenius point counts and principal-unit generation proving the full compact arithmetic CM image. |
| `d_cm_elliptic_pair.py` | Both pointed quartic curve maps and deck actions, the cyclic-twelve compact homology comparison with Smith diagonal(1,1,1,1), the exact normal-core characters, all six joint arithmetic unit pairs and18 gauge-sign checks. |
| `d_jacobi.py` and `d_jacobi_field.cpp` | Every good prime/level pair for primes≤50 and levels≤12, with exact cyclotomic coefficients, norms and both arithmetic-model point counts. Bad reduction is recorded. |
| `e_depth.py` | Two independent depth-two Ihara-bracket models, actual rational Galois ranks through weight14 and the weight12 period relation. |
| `e_smallgroups.py` | Every ordered generating pair in all74 group models of order≤24; 9714 epimorphisms, integral cycle bases, Smith indices, deck characters, relation-module ranks and lower-central ranks. |
| `e_obstructions.py` | The three-letter covering witness, real quartic obstruction, D8 cup-product witness and cubic cusp checks. |
| `e_cubic_abelian.py` | Cubic Weierstrass map, framed-cusp extension data, toric retraction, exact Smith forms, finite-field/eta coefficients and the even-level D8 witness. |
| `e_cubic_class2.py` | The order19683 cubic quotient, its exact group law, all729 central lift pairs and the local obstruction at109. |
| `e_splitting.py` | The order162 extension, all associativity triples and candidate section pairs, the actual cocycle, and local section conjugacy counts. |
| `e_boundary.py` | Boundary-source lattice comparisons and all384 finite inverse-unit certificates. |
| `e_rational_pairs.py` | The complete rational-pair tame criterion, 40000 positive pairs, 101124 signed rational pairs, and the explicit three-class fibers. |
| `e_completed_pairs.py` | Continuous residue representatives and change-of-cochain identities, coefficient transitions, 40000 rational comparisons, and actual primes for the inverse-limit obstruction. |
| `e_intrinsic_obstruction.py` | The intrinsic cubic Heisenberg quotient, its arithmetic origin term and all central lift choices at the prime above7. |
| `e_arithmetic_kernel.py` | All cyclotomic divisor trace maps through conductor24, 203 tower compositions, 603 equivariance checks and free-Lie ranks through degree8. |
| `e_intrinsic_positive.py` | Integral conjugation eigenlattices, exact Euler orders, rank and torsion computations for the full-lifting unramified cubic family. |
| `e_intrinsic_finite.py` | The exact cubic norm polynomial, explicit Heisenberg field construction, all729 generator assignments and all153 conjugacy orbits. |
| `e_cuspidally_central.py` | The determinant-one cusp comparison and the rank44 kernel from the full intrinsic class-two quotient. |
| `e_intrinsic_class2.py` | All64 framed cusp values, the integral Tate and exterior-square matrices, the primitive determinant line, local obstruction matrices, and the exact Smith presentation of every full intrinsic class-two fiber. |
| `e_intrinsic_lattice_explore.py` | Independent exploratory invariant-lattice computation; its opposite peripheral sign is related to the final lattice by the explicit basis map diag(I2,-I8). |
| `e_intrinsic_19.py` | The exact rank44 local Smith exponents at both primes over19, proving the full class-two lift in E.38. |
| `e_next_depth.py` | A finite class-three quotient of order3^30, exact modular solution lattices, and a directly checked annihilating row excluding every next lift of the E.38 class. |
| `e_riemann_correction.py` | Exact cubic residue characters at the primes over7 and19, detecting the nonzero local Frobenius correction word in the arithmetic inertia product. |
| `e_lie3_fibers.py` | All330 integral Hall brackets and their arithmetic actions, complete Smith transformations modulo729, an independent invariant calculation, and the proved torsion bound for every nonempty class-three lifting fiber. |
| `e_unramified_sections.py` | All three degree-four graded lattices and arithmetic matrices, their exact ranks/traces, and split-lattice certificates for the all-degree unramified section coordinates. |
| `e_tame_module.py` | Ninety-six exact affine-orbit systems for the local arithmetic module quotient, both augmentation equations, actual tame relations, and28 forced-binomial cases. |
| `e_infinite_obstructions.py` | The full prime family through1000, independent cubic point counts, both primary CM matrices at every eligible prime,38 rank44 Smith forms, and additional inert/split checks of the exact universal exponent. |
| `e_higher_images.py` | The degree-three local obstruction matrices over K at2 and over rational Q2, full Smith transformations and independent determinant checks, with proved precision bounds, for the general higher-image criterion. |
| `e_tame_classes.py` | All tame-local conjugacy classes of H, with48 independent finite Smith systems,36 actual group-ring and weighted-integral transition maps, and checks of both explicit representative families. |
| `e_norm_sections.py` | Exact finite Galois actions, 78,732 cocycle identities, 13,122 inverse-deck comparisons, actual transfer/norm maps, and radical field factorizations for every global H fiber. |
| `e_global_zero.py` | Forty exact cyclotomic-unit identities, norm maps through conductor81, five centered annular decompositions, and five compatible free-group cokernels for the complete zero-first-coordinate H family. |
| `e_cyclotomic_norms.py` | Exact cyclotomic resultant and norm identities, pairwise coprimality, and the independently ramified infinite family of global sections. |
| `e_first_three.py` | Integral normal forms, actual Frobenius normalizations, field factorizations, and ideal-norm transitions for first Kummer coordinate3. |
| `e_unramified_first.py` | All nonzero multiples of the first Kummer coordinate3: exact coordinate recovery, integral involution identities, arithmetic root orbits and ideal-norm transitions. |
| `a_elliptic_kernel.py` | The actual elliptic multiplication-by3 covering, its integral class3 Hall lattice, the rank332 comparison kernel, and the cuspidally central and outer Tate transfers. |
| `e_two_line.py`, `e_two_units.gp` and `e_two_units_probe.gp` | Every nonzero first multiple of the Kummer class2: eight certified number fields, fundamental units and exact unit-norm matrices, right inverses, kernel coordinates, residue corrections and valuation-chain checks. |
| `a_class3_frobenius.py` and `a_class3_local.py` | The actual class3 arithmetic action of the rank2 quotient, its exact root transport, every coefficient of the local tame defect and all nonempty local fibers at2. |
| `a_combined_quotient.py` | The exact common quotient joining the elliptic and rank2 class3 actions, its actual cusp image and integral strict filtration, kernel rank329, and all72 common-action identities. |
| `e_two_prime_first.py` | The actual two-prime arithmetic presentation in its Kummer image, fifteen orbit systems, thirty-nine exact normal-form recoveries, integral Frobenius divisions, and11,172 independent mixed residue tests. |
| `e_prime17_norm.gp` and `e_prime17_norm.py` | The certified degree-six radical field, its complete class group and S-units,31 outside-prime norm columns,41 independent norm determinants,9 ideal-lattice identities and exact Smith kernel/cokernel coordinates. |
| `e_frattini17.gp` and `e_frattini17.py` | The unconditionally certified degree-eighteen Frattini field, all ten Kummer coordinates, exact Frobenius matrices,450 uniform cubic-residue comparisons at50 inert primes, and full deeper matrices at269,809,1187. |
| `a_elliptic_frobenius.py` and `a_elliptic_rank13.py` | The actual rank-thirteen elliptic quotient, its complete commutator-module ring, all comparison kernels, exact Frobenius and path transport, with1331 associativity,144 group/action and156 power identities. |
| `a_elliptic_local.py` | Every local section class over Q2(zeta3), all9 Smith systems,108 finite-coordinate round trips,54 tame sections,108 normalization identities,486 lower lift tests and the81 lower-stabilizer values. |
| `e_frattini_fixed_module.py` | The exact involution-fixed Fox module for the inert-prime calculation: all81 vectors, their cyclic ranks, explicit independent generators and annihilating relations, the18-column involution,162 semilinear identities, the ten-generator Schreier basis and three Frobenius-square maps giving the exact Dirichlet-density counts. |
| `a_cubic_audit.py` | Independent Smith and framed-point checks of the cubic generalized-Jacobian calculation. |

Every mathematical program is documented in its module header and in the matching numbered statement. Its actual `.out` file is included alongside it.

Run a program with its ordinary Python command, for example:

```bash
python code/e_depth.py > code/e_depth.out
python code/e_smallgroups.py > code/e_smallgroups.out
python code/d_metabelian.py > code/d_metabelian.out
python code/d_gamma.py > code/d_gamma.out
```

`d_gamma.py` imports the shared Lyndon routines from `d_metabelian.py`; run the latter first to refresh its saved image bases. For the degree8 calculation, run `d_cm_degree8_seed.py` before `d_cm_degree8_centralizer.py`; the latter uses the shared exact linear routines. The Magnus and Sylow checks have their own saved output. Other mathematical programs consume their supplied inputs or generate the data they need.

For the structural relative pro-two comparison, run `python code/d_cm_rank4_structure.py` and then `python code/d_cm_rank4_odd_lift.py`. The first reconstructs the retained D.33 conjugators from the included certificates. The second checks the boundary generators and the exact arithmetic computations used to realize the whole compact CM torus. Their finite checks accompany the full pro-two existence and comparison proofs in D.34 and D.35.

To regenerate the finite unit certificate with an installed PARI/GP executable, run `python code/e_two_line.py --gp /absolute/path/to/gp`. Without this argument the Python program independently checks the supplied GP output and performs its exact polynomial and matrix verification. The GP programs and their real output are included; the PARI installation itself is not redistributed.

For E.59, run `gp -q e_frattini17.gp` from the `code/` directory, then
`python e_frattini17.py`. The GP script recreates and unconditionally certifies
the actual field and Kummer coordinates; the Python script uses only the
standard library and independently checks the finite-field and exact-polynomial
certificates. Run `python e_frattini_fixed_module.py` for the separate complete
fixed-module and Dirichlet-density count. Earlier exploratory programs and
their actual outputs are retained under `code/research_prime17/`, with their
status explained in its README. No final script depends on an exploratory
binary checkpoint.

For E.61, run `python code/e_full_local_cusps.py`. It checks the actual
eleven-module tame relation, its literal word preimage, all27 cusp-line
comparisons, the detecting cover of degree19683 and genus59050,
54 cusp-inertia formulas, and120 exact finite local parameter quotients.
The proof supplies the good-reduction, finite-cover and Jacobian maps
used to classify the full ramified local source.

For E.62, run `python code/e_second_norm_obstruction.py`. It checks every
unit of the residue field with289 elements, its cube and ninth-power
images, the complete torsion transitions and the integral valuation
lattices modulo3,9,27,81. The explicit global class lifting through the
first norm transition fails at the next; the local inverse limit and
every toric fiber are evaluated in the proof.

For E.64, run `gp -q code/e_complex_norm_criterion.gp` and save its output
as `code/e_complex_norm_criterion_gp.out`, then run
`python code/e_complex_norm_criterion.py`. The GP script unconditionally
certifies the degree-six class group and units and computes58 actual
prime contractions into the degree-eighteen field. Python independently
checks1508 finite-field norms,124 characteristic-zero norms and six
Eisenstein expansions. The full proof supplies the norm tests at every
layer and the two separate completion exactness arguments. Both programs
were rerun from fresh copies, reproducing every exact certificate value.

For D.37, run `python code/d_cm_fermat_exponent4.py` and then
`python code/d_cm_fermat_cover_matrices.py`. The first program's import
chain recreates the joint affine base, all576 admissible base choices,
the linear correction tables, both exact retained conjugators, and the
generating exponent-twelve witness. The second evaluates its actual
cubic, quartic and cyclic-twelve compact-cover actions in two independent
word models. Every program in the six-script chain also has its own
saved output and JSON certificate. The independent audit reproduces all
six exact certificates and verifies the673392-letter final cusp word.

The Jacobi-sum calculation is the largest computation:

```bash
python code/d_jacobi.py > code/d_jacobi.out
```

It compiles the C++ helper automatically. The largest directly enumerated field is `F_(47^5)`, with229,345,007 elements. Its discrete-log array uses about0.92GB of memory. Semiprimitive cases use the separately proved quadratic-extension Gauss-sum formula; the smaller such cases are also enumerated independently. These choices and every field's primitive polynomial are retained in `d_jacobi.json`.

`e_fetch_groups.py` is a provenance refresh tool. It fetches the primary GroupNames permutation models and writes `e_group_input.json`. That exact input is already included. The mathematical enumeration reads the supplied input, closes each permutation model itself, verifies its order and verifies pairwise nonisomorphism for the two-generated models.

## Ledgers and document build

The metadata programs and `assemble.py` do not replace mathematical verification. They collect the current statements and check the correspondence between source, status, coverage rows and bibliography keys.

```bash
python code/a_metadata.py > code/a_metadata.out
python code/d_ledger.py > code/d_ledger.out
python code/assemble.py > code/assemble.out
python code/build_pdf.py > code/build_pdf.out
```

The B/C and supplemental E metadata are supplied directly as JSON in `ledger/`. `assemble.py` reads those files and regenerates the required results/readings CSVs, combined bibliography, coverage JSON and report. Thus the `sections/` and `ledger/` directories belong with the master TeX source when reproducing the deliverable.

On a normal TeX Live installation, `build_pdf.py` uses the stock LuaLaTeX format. The execution host used here had the LuaHBTeX binary and Type1 fonts but lacked the generated format and optional OpenType loader. The build script therefore contains a local Type1-format preparation route. It changes no system file and downloads nothing. The paper also compiles with ordinary LuaLaTeX.

The final build performs BibTeX and three LuaLaTeX passes. It rejects undefined citations or references, missing characters and overfull boxes. `pdf_qa.py` renders every page with Poppler, checks every numbered statement heading against the CSV, and records page geometry and contact sheets. Visual inspection is recorded in `qa/visual_review.md`; the program itself does not claim to perform that inspection. Build logs are supplied; the temporary TeX format cache and individual page PNGs are not needed in the archive.

`build_certificate.json` records the source and PDF hashes for the successful build. After rendering and reviewing that build, `package.py` creates the single ZIP, includes a per-file SHA-256 manifest, and reads the archive back to check both CRCs and all file hashes. It rejects a PDF whose source files or review hash have changed. Run it without redirecting its output: it writes `code/package.out` itself before completing the archive checks.

## Interpretation of the finite results

Every transfer from a finite, graded or rational calculation is proved in the corresponding statement. In particular, the Lie tables are not used to assert a full profinite lift without its lifting theorem, the rational inherited depth quotient has its specified comparison with the integral quotient, and the CM image computation retains the additional dihedral-field relation. Unfinished requested classifications remain labelled Open in the paper and INCOMPLETE in the report.

## Split-prime mixed section fibers (E.56)

Run `python code/e_split_prime_first.py`. The retained output and JSON check
36 actual Frobenius normalizations, 15 full finite orbit systems,
81 coordinate recoveries, 1458 integral series coefficients and 11172
equivalent prime criteria. The program uses exact standard-library integer
and rational arithmetic. The complete proof and an independent copied-run
audit are retained with the section and ledgers.

For E.65, run `gp -q code/e_pure_norm_fields.gp` and the two Python programs
`e_pure_norm_local.py` and `e_pure_norm_verify.py`. The independent root run
reproduced every one of the49 structured PARI records and both complete JSON
certificates. The exact all-degree wild matrix is accompanied by the first
three finite matrices, actual character tests and the first unit-norm basis.
The exploratory shape/domain failures and their actual output are retained.

E.66 is a complete proof with the retained E.61 finite certificate; its full
independent proof audit is appended to `ledger/a_independent_audits.md`.

For D.38, run the four `d_cm_fermat_degree8_*.py` programs in the order
`module`, `image`, `joint`, `covers`. The joint program imports and executes
the first two. They compute the exact common quotient, the2117-by2938
integral system, the simultaneous generating shadow and every compact-cover
map. All four mathematical certificates were freshly reproduced, excluding
only elapsed-time fields. Actual root output is retained in the three
`root_d38_*.out` files.

For E.67, run `python code/a_marked_local.py`. Root and D separately reran
the complete certificate and read the full proof. The finite moment Smith
form, literal nonlifting word, nonunit centralizer checks and weighted trace
valuations are recorded in JSON; the full D audit is in
`ledger/d_e67_audit.md`.

For E.69, run `python code/e_coherent_units.py`. It verifies the entire
residue-unit calculation and the literal first two base norm preimages;
it does not calculate the eventual universal norm index. Root reproduced
the complete certificate and checked the actual Kato inverse-system map,
finite-index reduction, compact product and positional section comparison.

For E.68, run `python code/a_unramified_local.py`. It uses the retained
`e_unramified_sections.py` Hall routines and evaluates all three actual
quotient factors and both kernel factors through degree4. The952 exact
sequence certificates include Smith maps and their inverses. The actual
E54 nonlinear action supplies500 independent normalizer checks and the
complete2187-class triangular comparison. Root and D freshly reproduced
the entire JSON with no field excluded and independently read the full
proof; their reports and actual stdout are included.

For E.70, run `python code/a_central_orbits.py`. It verifies the actual
rank9 mod3 quotient and the primitive arithmetic scalar quotient; all
scalar pairs, coboundaries and signed phase transitions through729 are
checked, with378 coherent character divisions. Root freshly reproduced
every certificate field and audited the full constructive product map
and its inverse. The finite torsion quotients and the torsion-free
compact inverse limit are related by their exact retained transition maps.

For E.71, run `python code/e_marked_other_cusps.py`. The entire residue
plane cubic at q4 is enumerated, all9 literal tangent polynomials are
checked, and all648 compact Kummer obstructions are retained. A separately
reran the copied program and audited the complete proof and every actual
path, coset, coinvariant and full-section map; no field differs in the
independent JSON. The proof handles every good place and every nonzero
three-adic inertia exponent, including nonunits.

For E.72, run `gp -fq code/e_norm_divisors.gp` and save its output
as `code/e_norm_divisors_gp.out`, then run `python code/e_norm_divisors.py`.
The certificate checks138 actual polynomial factorizations,171 weighted
prime-norm transition systems,366 cofinal divisibility tests, and the
saturated rank-three positional norm kernel. Root reproduced all69 GP
records and every JSON field, and read the full completed-divisor,
compact-fiber, class-order and positional comparison proof. The higher
class matrices and the stable norm exponent remain unevaluated data.

For E.73, run `python code/a_global_gluing.py`. It verifies the explicit
Shapiro inverse and Hochschild--Serre cocycle, the positive local-relator
coordinate under every lift change in the tested groups, and all 27
characters of the actual cubic Kummer quotient. The exact output is
`a_global_gluing.json`; the independent root rerun matches every field.
The infinite presentation and sufficiency are proved in the paper.

For D.39, run `d_cm_fermat_homology_module.py`, then the matching
`_image.py`, `_lift.py`, `_seed.py` and `_covers.py` with Python from
the code directory. Each writes its matching JSON; save its stdout to
the matching `.out`. The module calculation exhausts the exponent-eight
common quotient. The remaining programs verify the integral signed system,
its retained J48 seed, all1153 basis images and the exact compact-cover maps.
Imports repeat predecessor checks and update only their elapsed-time fields.
Root reran all five in a separate directory; all mathematical fields match.

For E.74, run `python code/e_wild_layers.py`. It reconstructs the actual
E41 Hall matrices and verifies the complete Smith transformations and
inverse maps. The degree2 and degree3 arrays are retained in the two
`e_wild_layers_r*_transforms.npz` files at moduli81 and729; the paper
proves these precisions suffice. Root and A freshly reran the computation
and compared every JSON field and every array with no exclusions. The
unsuccessful earlier integer-Smith attempts are preserved separately with
their exact termination/provenance records. The materialized diagonal-only
attempt was also freshly executed by root and again reached its explicit
20-second SIGALRM without producing a Smith result.


## Statements D.41, E.76 and E.77

`python code/d_cm_symmetric_completion.py` reconstructs all marked PGL2(F7) and PSL2(F7) elements, simplicity and centralizer checks, and both joint images. `python code/a_wild_nonlinear.py` reconstructs the finite relative Lie, Fox, weighted Magnus and nonlinear central-defect certificates.

`python code/e_cyclotomic_basechange.py` verifies the retained exact arithmetic export. Add `--gp /absolute/path/to/gp` to rebuild all eight number-field stages before verification. The recorded complete rebuild used PARI 2.19.0 and unconditional `bnfcertify=1`. Each stage retains actual output and all exact ideal/coordinate data. `norm_index_attempts/` contains explicitly identified earlier successful and failed searches and the actual PARI binary data used by those searches.

The archive includes the actual E.74 NPZ transformation certificates and retained PARI BIN data, as well as JSON, text outputs and source programs. Compiled executable binaries and third-party papers are excluded. Root audits retain independent execution results; the E.76 full structured export and the E.77 entire JSON match exactly with no exclusions, while D.41 excludes only elapsed time from equality.

## Statement D.42

Run `python code/d_cm_relative_pronilpotent.py --source-code code` and `python code/d_cm_relative_kernel.py` from the archive root. Both use the standard library. The first reads the retained D.37 graph and D.39 exact odd paths, checks every source equation and all 1153 and 1513 integral cycle projections, and records the nonzero common conjugator. The second independently enumerates the actual PGL2(F11) and PSL2(F11) groups, conjugacy classes, normal closures and loop orders. Root freshly ran both programs in a separate directory; the full JSON certificates agree apart from their elapsed-time fields.

## Statement E.78

Run `python code/a_wild_class3.py` with Python3 and SymPy. The program reconstructs all symbolic Hall operators and source errors, checks their independent Magnus expansions, and verifies the actual source/root transports, both lower lifting maps, fibre coordinates and the intrinsic cusp-family obstruction. It requires no saved binary input. Root read the full proof and relevant original source, then reran the program in a separate directory; the entire JSON certificate agrees exactly with no exclusions.

## Statement E.79

Run `python code/e_sclass_norms.py` for exact verification of the retained arithmetic and lattices. Add `--gp /absolute/path/to/gp` to reconstruct its three E.76 dependency stages and four new arithmetic stages before verification. The rebuild uses `bnfcertify(B)` at default flag0 with return value1, complete S-unit generators and exact ideal identities. It retains all seven stage outputs and `e_sclass_coordinates.bin`. Root independently repeated every stage: all18 structured export records and the entire summary JSON agree with no exclusions. The complete regenerated PARI BIN object also agrees; the original and regenerated binary serialization bytes are separately hashed in the audit.

## D.43: full simple-even relative family

Run `python code/d_cm_simple_even_family.py` with the Python standard library. The exact certificate enumerates A7, both distinct marked even kernels, the separating source word, its complete normal closure, and the factor-swapping residual. Root read the full family proof and freshly ran a copied program; the complete JSON agrees after removing only `summary.elapsed_seconds`. The exact common quotient and compatible family conjugator are proved in the paper.

## E.80: joint wild quotient and rational descent

Run `python code/a_joint_wild.py` with Python3 and SymPy. It reconstructs the actual scheme identities, Hall operators, integral filtration maps and both Smith inverses. Complete finite images have orders6561,19683,6561; the certificate also checks the restriction and inverse gauges, descended section examples and all displayed family values. Root freshly reran a copied program after reading the full proof; the complete JSON and stdout are byte-identical.

## E.82: all nine intrinsic cusp-family obstructions

Run `python code/e_cusp_family_obstruction.py` with Python3, NumPy and SymPy. It imports the included `e_cusp_local_smith.py` and reads the retained E41 Hall code plus the E74 JSON and degree-three NPZ transformations. It reconstructs all nine complete kernels, actual obstruction generators, exact rational Smith maps and inverses,405 particular central correction columns and the joint residual quotient. A separate proof audit and a full rerun from copied source and copied inputs give byte-identical complete JSON and stdout, with no timing exclusions. Actual interrupted and completed intermediate attempts are in `code/e82_attempts/`; the independently developed local Smith proof and its standalone calculation are in `code/e82_local_smith_audit/`.

## E81: the prime73 class and twenty-seven S-corrections

Run `python code/e_prime73_capitulation.py --gp /absolute/path/to/gp` with Python3, SymPy and PARI/GP2.19.0. The driver rebuilds three retained E76 dependencies and five owned arithmetic stages in an isolated directory, then verifies all36 exported records, four integer Smith/inverse systems,729 genus congruences and27 literal principal cubes. The completed arithmetic outputs and all four generated binary objects are included. No degree54 BNF is used.

The full root source/proof audit and fresh eight-stage rebuild are recorded in `ledger/root_e81_audit.json`. The complete text and JSON outputs agree byte for byte. The four binary serialization files have different bytes but equal complete PARI objects, including all11,6,14,27 components. Actual source, outputs and fresh objects are retained in `code/e81_root_rebuild/`; its semantic comparison program preserves the exact absolute paths used in that audit, which can be redirected to the two retained sets to reproduce the comparison. All unsuccessful and interrupted search programs retain their actual outputs and explicitly limited interpretation.

## E83: the intrinsic-to-joint obstruction map

Run `python code/a_joint_intrinsic_image.py` and `python code/a_joint_intrinsic_coordinates.py --source-code code --cusp-certificate code/e_cusp_family_obstruction.json`. The first requires Python3 and SymPy; the second also requires NumPy and the retained E41, E74 and E82 inputs. They compute the complete4x330 Hall map, both natural H2 coordinate maps, their kernel inverses and the induced character on the full joint cusp quotient. All660 tensor expansions,405 cusp columns,6561 kernel-coordinate triples and every saved inverse identity pass. Root read the complete proofs and programs and reran both from copied source and four copied inputs: all source, stdout and JSON bytes agree. See `ledger/root_e83_audit.json` and the actual rerun files in `code/e83_root_rebuild/`.

## D44-D45: exact source comparisons and the recorded-action exclusion

Run `python code/d_cm_anabelian_even.py`. For the rank-two comparison run, in order, `d_cm_solvable_even_boundary.py --source-code code`, `d_cm_rank2_boundary_test.py --source-code code`, `d_cm_rank2_degree9.py`, `d_cm_rank2_centralizers.py`, and `d_cm_rank2_boundary_test.py --source-code code --elliptic-correction --output-stem d_cm_rank2_elliptic_corrected`, each through Python3. The first two source-dependent commands take the archive code directory as shown. Python uses only its standard library; the boundary program compiles the retained C++17 helper with `g++` in a temporary directory and checks108 independent tuple-Cauchy path evaluations before the full-word pass.

Root read both complete proofs and all Python/C++ sources and reran all six commands from copied source and15 copied inputs. Every full JSON certificate agrees after excluding only its elapsed_seconds field. Actual rerun programs and output are in `code/d44_d45_root_rebuild/`, and the detailed audit is `ledger/root_d44_d45_audit.json`. Its extra `verify_separator.py` is preserved exactly as run: it reads a child `code/` directory, so reproduce it in the original audit layout or point that variable to the adjacent retained certificates. This independent ascending-pivot calculation verifies the displayed four-term functional, ranks47 and48, all150 killed columns, the exact elliptic masks, both long-word lengths and six zero cusp defects.

D45 excludes a full profinite lift of the entire recorded normalized D39 action, including D40-D44 extensions retaining it. The previous quotient constructions remain valid, and the prescribed CM pair remains open for a replacement action.


## D52 and E94--E96

D52 uses the three Python programs d_cm_symplectic_search.py, d_cm_invariant_repair.py and d_cm_full_class2_search.py in that order. All use the exact retained D51 diagnostic input. The full invariant equations, word collection, pairing over F2, continuation and exponent-eight residual are proved in the paper. The separate peer map computes120 conjugator-pair parameters,102 redundant parameters and18 actual homology derivations. Root comparisons exclude only elapsed time.

E94: run python code/e_mu27_comparison.py --gp /absolute/path/to/gp to rebuild all six stages. PARI/GP2.19.0 and SymPy are used. All complete text/JSON outputs compare byte for byte, and all three complete PARI objects compare equal; serialization hashes are retained separately.

E95: run python code/a_cusp_kummer.py, python code/a_toric_wild.py, then python code/a_toric_residues.py. The first two default to the adjacent dependency files; --source-code accepts another exact dependency directory. All six complete JSON/stdout files were independently reproduced byte for byte. The full residue list, inverse maps and48 exact Smith systems are retained.

E96: run python code/e_global_zero_free_elliptic.py. It reads the exact adjacent early cusp export, intrinsic class-two JSON and wild-layer JSON. The final E95 coefficient and path fields were proved byte-for-field equal to that input. Both full output files were independently reproduced byte for byte, and a separate symbolic audit verifies the universal identities. The recorded freeze program preserves the author staging/metadata generation procedure. Historical and failed attempts remain with their actual outputs and explicit scope.


## D53–D54 and E97–E99 reconstructed stages

The main programs and exact adjacent inputs are retained in this directory. Run D53 in order: `d_arithmetic_correction_graph.py`, `d_cm_same_action_obstruction.py`, `d_cm_same_action_word.py`; then D54: `d_cm_reduced_invariant_equations.py`, `d_cm_invariant_zero_loci.py`, `d_cm_doubled_class2.py`. Their complete fresh comparisons exclude only named elapsed-time fields and compare all stdout prefixes.

Run E97 with `python code/e_unit_norm_coset.py --gp /absolute/path/to/gp`. It rebuilds the certified lower degree-six data and the exact upper degree-eighteen arithmetic. The GP-stage output is `e_unit_norm_coset_gp.out`; the same-stem `.out` is the Python verifier output. The complete PARI object comparisons and raw binary hashes are in the root audit.

Run E98 in order: `python code/e_global_split7_explore.py --source-code code`, `python code/e_global_split7_residues.py`, `python code/e_global_split7_central.py --source-code code`, `python code/e_global_split7_normal_forms.py --source-code code`. Python3, SymPy and NumPy are required. Each stage reads exact retained certificates, and the final stage includes all14 character rows and the global nonlifting witness. The historical interrupted program is preserved with its actual output and provenance; its final replacement is the complete four-stage pipeline above.

Run E99 with `python code/a_s23_intrinsic.py --source-code code`. This executes all81 strata, all4782969 finite residue pairs,405 actual tame words and40 central inverse round trips. The proof's actual rho1 definition is the sole presented source clarification; it changes no numerical file. All E98/E99 fresh full-file comparisons are byte-identical, with no exclusions.


## D55 and E100

Run `python code/d_arithmetic_relative_h2.py` and `python code/d_cm_boundary_norm.py`; these independent programs read the retained D48, D51, D52 and D54 JSON certificates. Run `python code/a_s23_full.py --source-code code` for every E100 Hall/Chen action, nonlinear coordinate and rational descent check. The root reconstruction is byte-identical for E100; D55 excludes only the identified elapsed-time fields. The peer D55 verifier checks the actual maps independently.


## E102 integral degree-four kernel

Run `python code/e_kernel_degree4_smith.py --input code/a_s23_full.json`. This constructs every exact modular Smith map and its inverse, proves the detected486 pivots attain the rank bound, and retains the exact integer lift in the NPZ. Python3 and NumPy suffice. The complete copied-source/input reconstruction is byte-identical for stdout, JSON and NPZ. The separately coded peer verifier uses successive mod3 Schur blocks and checks actual integral maps at3^9.


## D56, E101, E103 and E104

D56 runs its seven programs in the order recorded in d_arithmetic_detecting_quotient_manifest.json, beginning with d_arithmetic_sign_quotient.py and ending with d_arithmetic_affine_homology.py. All read the adjacent frozen D53 graph and the preceding actual outputs. The fresh complete rebuild and independent row-matrix map verifier are retained.

Run `python code/e_unit_norm_complete.py --gp /absolute/path/to/gp` for all five E101 arithmetic stages and the complete independent rational checks. Python3, SymPy and PARI/GP are required; the three exact dependency GP files are adjacent in code. All full stdout/JSON bytes and all five complete PARI objects were independently compared.

Run `python code/a_quartic_odd.py --gp /absolute/path/to/gp` for E103, including the owned GP field/elliptic computation. All literal isogeny, torus, coset, Shapiro and norm-coordinate checks are retained.

Run `python code/e_two_prime_full_family.py --input code/a_s23_full.json` for E104. It checks all173 applicable primes through2000 and the full displayed finite coordinate identities; the all-prime proof uses the actual source maps.


## E106: third ordinary tower layer

Run `python code/e_next_unit_characters.py --gp /absolute/path/to/gp` from any directory after extraction. The program uses the six complete files in the archive's inputs directory; Python3, SymPy and PARI/GP are required. It recertifies the B1 input, computes the two actual prime Frobenii, and verifies the entire character/class-map certificate. Complete author and root outputs are retained. The historical wrapper output is a new isolated replay, labelled with its exact provenance.


## E105, E107 and D57 completed calculations

E105: run `python code/a_quartic_frames_explore.py`, `python code/a_quartic_class2.py` and `python code/a_quartic_toric_cups.py`. The exact author and two independent copied executions are retained. Python3 and SymPy are required.

E107: run `python code/e107_bundle/code/e_stable_ordinary_phase.py`. Its three immutable inputs are in the sibling `inputs` directory within that bundle. This isolation preserves the exact input-hash metadata of both E106 and E107. The independent peer verifier is `code/e107_peer_audit/a_e107_rank_phase.py`. The raw/scaled-exponent test amendment and the citation-only proof amendment have separate records.

D57: run the six `code/d_arithmetic_*.py` programs in the order given by `ledger/d_arithmetic_class2_repair_manifest.json`: rank9 seed, geometry, conjugators, invariant module, local transgression, affine boundary. Python3, NumPy and SymPy are required. Both D56 JSON inputs are included. Complete final author and root copied replays are preserved, with comparisons excluding only elapsed_seconds. Every historical attempted program retains its actual output; nested local helpers retain their actual captured stdout. Files ending `.py.md` are source snapshots without a separate claimed execution; files ending `.patch.md` preserve exact patch bytes.

Archived audit and integration drivers retain their original staging paths and record the historical execution. The final mathematical programs above are the portable rerun entry points. Source-retrieval programs record access outcomes; raw third-party documents are excluded from the archive.


## E108--110 and D59

E108: run `python code/a_quartic_w_slice.py`; the exact E105 input is in
`inputs/a_quartic_class2.json`. Full author/root replays and an independent
coefficient/source audit are preserved.

E109: run `python code/e_quartic_ceresa_shadow.py`. The final full replay is
byte-identical in stdout and JSON. Its separate independent coefficient and
finite-point program is under `code/d_e109_audit/code/`.

E110: run `python code/e110_bundle/code/e_pure_tower.py --gp /absolute/path/to/gp`.
The isolated sibling inputs retain the author's exact input-hash map. Without
`--gp` the saved certified base output is checked. The two complete fresh
replays retain all text/JSON identities; the binary certificates were compared
by PARI `read`, with exact full GEN identity rather than raw-byte equality.
Both actual diagnostic failures in the root replay are retained with their
capture provenance. The `_gp.out` files have byte-exact `.out` aliases for their
corresponding GP source names.

D59: run `python code/d_arithmetic_free_characters.py`. Its two exact arithmetic
inputs are beside the source. The full fresh output comparisons exclude only
the explicitly named elapsed-seconds fields. The missing final719 group in the
printed bound was corrected by exact integer arithmetic; the earlier proof,
manifest, actual correction program and all audits remain preserved.

The recorded audit/integration helpers retain their original staging paths.
Source snapshots without a separate execution are marked `.py.md` or `.tex.md`.
Third-party source PDFs and source-page images are excluded from this package.


## E111–E114 and D60

Each new arithmetic bundle is under code/e111_bundle through code/e114_bundle, and the actual arithmetic group programs are under code/d60_bundle. Run each mathematical Python file from its retained code/ subdirectory; sibling inputs/ are preserved. E111, E112 and E114 accept --gp /absolute/path/to/gp for complete arithmetic rebuilds. E113 accepts that flag for its corroborating local-reduction stage. D60 has the four-stage order and exact frozen raw inputs specified in its manifest.

The root/peer audit directories retain complete copied-source executions. E113 and E114 match every text and JSON byte. E114 raw BIN bytes differ, while PARI read gives exact equality of the entire four-component GEN and all five embedded base components. D60 comparisons omit only elapsed_seconds and rebuild every stage independently. E111 has a complete independent peer rebuild and additional independent maps. E112 has the same full peer replay and an actual root review of all six standalone pages.

The frozen author E111 proof remains in code/e111_bundle/author_proof/; only its specified exponent-comma typoes were corrected for presentation. Historical failed and interrupted programs retain their actual outputs/statuses. Unexecuted snapshots are explicitly .py.md or .tex.md documents. Original third-party PDFs, OCR and compiled executables remain excluded.


## E115, E116, E118 and D61

The isolated bundles code/e115_bundle, code/e116_bundle and code/e118_bundle retain their code/, inputs/ and exact execution records. E115 accepts --input-dir inputs. E116 and E118 accept --gp /absolute/path/to/gp for complete mathematical reconstructions. E118 requires no external input for its final arithmetic certificate; its separate original discovery program keeps its original working-directory paths and exact E112 binary input, documented in the dependency ledger.

D61 retains all four programs and frozen arithmetic inputs under code/d61_bundle. Its manifest specifies the exact four-stage order. Root rebuilt all stages from copied source/inputs; only named elapsed_seconds fields are excluded from complete JSON/stdout comparisons. E115 root replay has no excluded fields. E116 matches all15 complete text outputs and all six decoded PARI GEN objects; raw binary serialization differences are retained. E118's independent no-input reconstruction matches all source/output/JSON bytes, with no exclusions, and its separate order800 group program checks every cocycle identity.

The initial E115 SymPy failure, initial E116 root warning-guard failure, and initial E118 TeX delimiter failure have genuinely empty stdout. Their real nonzero exit status and exact nonempty error evidence are retained. The package gate checks that evidence and its hash; no artificial successful output is inserted. Existing interrupted runs keep their separate actual status records. All .err evidence is archived.

The precise proof, primary-source and fresh-replay scopes are in the root/peer audit directories. Frozen author proofs are retained before literal spacing corrections. Every bibliography entry now carries its own verification note; Nakamura1995's missing printed note was restored from its existing original-source record, without a new source-verification claim.


## E117 and D62

E117 retains both arithmetic programs, all three exact inputs and every actual failure/replay record in code/e117_bundle. The full arithmetic reconstruction accepts --gp /absolute/path/to/gp. Root executed fresh copied sources and inputs: five complete source/text files agree byte for byte, with no excluded fields; the entire deserialized PARI GEN including both complete BNF objects agrees. Raw binary differences and the exact decoding comparison are retained.

D62 retains its four-stage computations and immutable inputs in code/d62_bundle. Root executed each stage in a separate copied directory. Whole JSON and stdout agree after excluding only elapsed_seconds, with empty stderr and unchanged source/input hashes. The independent peer program in code/a_d62_audit uses separate dense Hermitian/F2 and integral Magnus implementations and retains its complete actual results.

The original author result/report/peer ledgers remain byte-exact under each bundle's author_freeze/ledger. Active ledgers additionally record the completed root audits. All proof, source reading, fresh execution and visual scopes are specified in the attached records. The E117 focused peer review does not claim a full support audit or a fresh arithmetic execution. The original D.13, D.19 and E.23 questions remain active.


## E119 and D63

E119 is retained under code/e119_bundle with all eleven mathematical input
sources, twelve complete text outputs, twelve full PARI objects, actual failed
runs and both original author replays. Its full mathematical reconstruction
accepts --gp /absolute/path/to/gp and starts from source-only empty temporary
directories. Root repeated all ten GP stages and compared all twelve complete
text outputs and all twelve entire decoded GEN objects, with no exclusions.
The exact original record remains under code/root_e119_audit.

The later exact-rational export amendment changes twelve ambient Smith-map
entries in modulus-one rows. All other JSON fields, all GP sources/outputs,
all BIN objects and the proof remain unchanged. The entire old author tree
and both old peer runs are preserved. Root read the exact source diff and ran
the corrected complete checker on its own arithmetic outputs in a fresh
directory. Its entire stdout/JSON agrees byte for byte with the amended
author output; both ambient inverse compositions and every changed entry
were independently checked. These new records are in code/root_e119_delta_audit.
The independent peer full proof/source and finite-map audit was also rerun
against all 415 amended manifest entries and retains its exact scope.

D63 is retained under code/d63_bundle with all four mathematical programs,
every actual failed/intermediate attempt, all immutable matrix inputs and
all author replay outputs. Root independently executed each complete program
in a fresh copied directory. Every whole JSON and stdout agrees after
excluding only elapsed_seconds, with all source/input hashes unchanged and
empty stderr. The independently written peer standard-library verifier
reconstructs the Hom systems, full unordered Sylow norms and all 245760
cross-action columns and all 245760 relation columns from the frozen matrices.

The exact frozen author ledgers remain under each bundle's author_freeze/ledger;
active ledgers additionally record the completed root and peer reviews.
Both standalone author PDFs and their owned QA artifacts are retained.
Integrated visual review is recorded separately after the new complete build.
Original D.13, D.19 and E.23 and the three requested-original D.a verification
gaps remain active.


## E121 and D64

E121 is retained in code/e121_bundle with the complete128-file original
freeze,264-file final freeze, exact two-paragraph proof amendment, every
mathematical source, actual attempt and complete arithmetic output. Root
ran all five new GP stages and the exact checker from copied sources and
nine immutable E119 inputs. Seven complete text outputs agree byte for
byte; all seven whole decoded PARI objects agree, with no exclusions.
The raw serialized BIN bytes differ and their exact hashes are recorded.
The proof amendment changes no mathematical computation. The completed
kernel map and inverse, choice ambiguity and actual norm-lift rule are
explicit. Root's separate finite-map verifier imports no author code or
outputs. The independent peer checks full rational genus maps,26244
normal-closure products,12 marked primes,14 principal ideal identities,
732 actual HNF columns, seven units and all28 local characters. Its
interrupted direct-power attempt and earlier successful counter/guard
versions are preserved with their actual outputs and precise scopes.

D64 is retained in code/d64_bundle with the complete original freeze and
the necessary post-word moving-component repair. All25 original code,
input and output files remain unchanged. Root read the full755-line
proof and1248-line mathematical source, then freshly ran all six complete
programs on their exact inputs. Complete JSON and stdout match after
excluding only elapsed_seconds. The separate peer reconstructs marked
integral pairings, all branches/framings, isometries,548 full retraction
coefficients,576 source-basis wedges and full36-term cusp identities.

Exact author ledgers remain in each bundle's author_freeze/ledger.
The active ledgers add the completed reviews and original-task scope.
Every frozen-to-archive mapping points to bytes with its stated hash;
active editorial amendments are recorded separately. All original
D13,D19,E23 questions and the three D.a original-source access gaps remain
active. The integrated paper has its own subsequent visual review.


## E122 and D65

Root read all624 final proof lines and all470 mathematical source lines and performed the complete three-GP/two-Python copied-source replay. All seven whole text outputs match byte for byte and all three complete decoded GEN objects agree, with no exclusions; all171 frozen hashes were rechecked. The independent peer read the same complete proof and sources, then independently checked22 cube/norm identities, ten complete principal divisors, both243-element genus kernels,165 local norm columns, all22 upper characters, the243-element hyperplane and the complete729-element norm quotient. No correction was requested.

Root read all643 final proof lines and all1346 mathematical source lines, then replayed all eight complete programs from eight immutable inputs. All whole JSON/stdout files agree under the explicit clock-only projection; no algebraic field or input hash is excluded, and all actual fresh outputs remain retained. The independent peer read the full proof and all eight sources and independently reconstructed512 modulo-four norm columns,1024 trace columns,2048 coinvariant vectors,3072 orientation identities and80 correction columns. The actual integral source extension, odd-cover/Fourier comparison and post-word moving repair were checked. No correction was requested.

E.122 evaluates the entire B_d positional53 three-primary S-class tower. All actual norms from level2 onward are isomorphisms, giving C9+C3^3 and the same inverse limit through literal norm coordinates; extension is three times the actual norm inverse and the horizontal H action is retained. Twenty-two literal cube/norm witnesses supply the full rank-five local character hyperplane, killing K2; the proved actual recurrence K_d=j_dK_(d-1) gives every later kernel. The complete first embedded unit norm image is the six-row congruence lattice of index729 with actual preimages. Later unit norm quotients are C3^9 and completed kernels are mu3+Z3^(2*3^(d+1)), through explicit local-character/Hilbert90 maps. Coherent positional unit/divisor inverse systems, separate lower factors, and the intrinsic section maps remain active.

D.65 constructs an actual peripheral action on X/J65, extending the retained compact quotient by5752 dimensions and12 coinvariants. The actual signed integral exterior norm divided by two has rank6 in each ten-dimensional compact test; an actual coinduced source correction realizes its entire image, and eight source-involution words kill its rank4 kernels. Both D57 branches, literal small conjugators and complete W_h/metabelian/CM maps survive. The lower Y action is exactly Int(b_t,Y) beta_Y with the displayed derivation and all36 cusp terms. The specified residual J65 has dimension276478 and maps onto the old1918-dimensional compact norm kernel. Its two remaining tested coordinates retain their precise test scope; full residual and profinite realization remain active.

All literal E122 text inputs retain their native filenames, including
inputs/e122_literal_unit_witnesses.txt. The complete arithmetic replay
uses those explicit relative input paths. Exact author ledgers are in
each bundle's author_freeze/ledger; active ledger amendments are recorded
separately. Root and peer execution scopes are not interchanged.

The archive stores exact duplicate QA image bytes once with an explicit
logical-path map. All mathematical sources, inputs and outputs remain
ordinary members. See ARCHIVE_README.md for exact restoration; all prior
logical image bytes and their hashes are retained.


## E123, D66 and E124

Root read the complete640-line proof and all eight final mathematical sources plus their replay driver. All eight stages were replayed from the exact frozen sources and inputs; all text and both JSON outputs agree byte for byte, both whole decoded GEN objects agree, and the standalone nf-only verifier checks all nine ideal identities in certified maximal orders. All304 owned files and8 inputs were hashed before and after. No fields were excluded and no author source was changed. No separate final third-agent audit is claimed.

E.123 evaluates the entire L_d positional53 three-primary S-class tower: actual norms from level2 are isomorphisms on C9^2, with extension3 times the specified inverse and complete horizontal maps. The full coherent divisor image is the kernel of a surjective restricted-support map to C9^2. Literal primes31 and103 give its coordinates and inverse, and compact fibres give coherent lifts. The whole factor is its coherent unit kernel times that divisor module, with the literal total norm and an embedded family of actual H-section classes. Other positional factors and intrinsic section lifts remain active.

Root read the complete final proof and all nine sources, with the actual D58 source intersections, D60 odd transfer and unordered stabilizer, D64 joint surjectivity and D65 ordered repair. All nine programs were independently replayed from ten exact inputs. Entire JSON and stdout agree under the declared elapsed-time-only projection; every mathematical field and input hash remains checked. All144 owned files and10 inputs were hashed before and after, with all fresh raw outputs preserved. No separate final third-agent audit is claimed.

D.66 fills the complete fourth compact comparison block by actual quadratic source automorphisms. The integral projective cover, full quadratic source square and literal small conjugators realize both remaining compact directions. The ordered correction preserves the preceding three blocks, both D57 branches and all W_h maps. The total retained compact quotient has dimension9600 and28 coinvariants; J66 is the specified remaining kernel of dimension274560. Its cusp-radical correction and full profinite realization remain active.

Root read the complete final proof, all nine mathematical sources and their replay driver, and rechecked the actual class-field, ambiguity and Kato reductions. All nine stages were replayed: all whole text, five JSON outputs and generated inputs agree exactly, as do both complete decoded GEN objects with7 and8 components. The residue rank9,729 upper classes,243 lower classes and all729 actual lifts were checked. All153 owned files and8 inputs remained unchanged. No field was excluded and no upper BNF was used. No separate final third-agent audit is claimed.

E.124 gives complete ordinary class groups D2=C9^2+C3 and D3=C27+C9+C3, including actual norm, extension, prime and S-class quotient maps. A literal rank9 residue matrix proves the full completed L2 ordinary-unit basis. Every later norm is onto with kernel in the fixed three-prime subgroup, and both trace compositions equal3. The exact Kato restriction proves a finite h>=2, with coherent three-valuation image3^h Z3 and explicit product coordinates/inverse for the full positional factor. The numerical value of h, a minimal valuation generator, other factors and intrinsic lifts remain active.

## Four frozen elliptic comparisons

Four frozen E120 comparison subresults now have complete root proof/source review and copied-source replay: the integral Tor symbol and torsion class, the theta distribution and integral cokernel of order27, the logarithm torsor with its full basis/tangent transport and actual local class of order27, and the framed principal cubic cover. The latter has the literal norm-seven isogeny lift and full Schreier source map; its next augmentation extension detects both residual intrinsic directions by a determinant-one minor. Their arithmetic coefficients remain unassigned. The root Tor and theta checks additionally reconstruct the asserted finite maps independently. All notes, exact dependencies, failed attempts and actual outputs are retained.

The three exact author ledgers are retained in their author_freeze/ledger
directories; active editorial amendments have an explicit separate ledger.
The E120 author tree remains active: code/e120_frozen229 contains only the
four declared frozen notes, programs, exact dependencies and declared history.
Imported helpers retain their native names and actual execution records.

## Current lossless archive layout

The current extraction instructions are in ARCHIVE_README.md. Complete
byte-identical binary data and historical QA images have explicit logical
path aliases. Every original path and byte string is retained, with the
whole-byte materializer and independently executed restoration checks.
Source programs, text transcripts, JSON records and current main-PDF page
images are ordinary members. Different binary serializations retain their
different complete bytes. Earlier image-only layout descriptions above
record the preceding versions; the current binary alias policy is the one
specified here and in the two current alias manifests.
