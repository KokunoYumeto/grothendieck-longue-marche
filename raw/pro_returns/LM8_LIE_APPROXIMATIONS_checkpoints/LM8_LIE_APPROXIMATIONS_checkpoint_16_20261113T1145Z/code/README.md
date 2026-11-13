# Exact computations and reproduction

## Environment

The executed versions are in ../audit/environment.json: Python 3.12.14,
SymPy 1.14.0, GAP 4.15.1 and SmallGrp 1.7.0. Arithmetic is exact over
integers, rationals, finite fields and finite permutation groups. No numerical
rank threshold is used.

Run Python programs from this directory. Each saves its machine-readable
output beside itself; redirect stdout to the corresponding .out file.
All completed certificates and printed outputs are already included.

## Program map

| Program | Executed scope | Output |
|---|---|---|
| a_small_actions.py | All 24 groups of order at most 12, stated signature boxes, genus-two actions and ineffective pullbacks | .json, a_small_signatures.csv, .out |
| a_profinite_obstructions.py | Exact 48-element boundary witness and vertex-group subgroup lists | .json, .out |
| a_tripod_finite.g, a_tripod_checks.py | All293009 ordered pairs in all250 groups through48; smallest mixed-sign witness D24; all27 derived conjugators in the universal S3 quotient, checked independently | .out and associated JSON certificates |
| a_metabelian_involution.py | All421875 associativity identities and5625 automorphism products in the order75 peripheral involution witness; all inner candidates and15 normalized Haar cases | .json, .out |
| a_metabelian_lift_class2.py, with and without --rational | Complete rank-ten BCH calculation over F5 and Q, integral at5; exact nonmetabelian lift of the specified A.22 involution and its metabelian residues | .json, .out, _5adic.json, _5adic.out |
| a_metabelian_lift_higher.py; a_higher_lift_verify.py | Complete class3 and class4 affine lifting systems with all prior parameters; independent rational and modular rank certificates; unique extendible class3 point | a_metabelian_lift_class{3,4}_{rational,mod5}.json, _system.json, .out; a_higher_lift_verify.json/.out; a_higher_lift_coordinates.csv |
| a_metabelian_lift_class5.py; a_class5_verify.py | Actual integral Hall group coordinates at class5, all20 prior parameters, the full1428-by428 system and90-dimensional solution family; independent exact and mod5 checks, full projection of rank2 with fibres88 | a_metabelian_lift_class5.json, _system.json, .out; a_class5_verify.json, .out |
| g_degree8_nonmet.py | Saturated ambient fifth-adic degree8 plane and exact characteristic-quotient Magnus observables; actual group-word tests modulo125 | g_degree8_nonmet.json, g_degree8_nonmet.out |
| b_signed_source.py | Complete finite reductions of the actual first signed-source image, all affine composition laws and integral cocycle equations; A5 detection-class counterexample and Hensel lifts | b_signed_source.json, b_signed_source.out |
| g_signed_normalizers.py | Exact reductions of both actual signed normalizer images; the rho section law, integral sigma parity restriction, finite nonsplitting, and the primitive q2 kernel line | g_signed_normalizers.json, g_signed_normalizers.out |
| b_lie_core.py 6 | Four-puncture special/inner/point-pushing/normalizer matrices through six | b_sphere_tables.json/.out |
| b_tripod14.py | Tripod matrix calculation through thirteen, exact character dimension at fourteen | b_tripod_dimensions.csv, witnesses JSON, .out |
| b_character_tables.py | Independent S3/S4 Witt characters and odd-generator dimensions | .json, .out, paper table |
| b_pentagon_witness.py | Full pentagon defects, including coefficient 16 for q7 | .json, .out |
| b_modcohom.py | H1/H2 over F2/F3 through nine; consecutive differential products | .json, matrices JSON, .out |
| g_integral_cohomology.py | Actual integral special-outer H1 and H2 at two and three through nine, with the coefficient exact sequence and modular checks | .json, .out |
| b_coverings.py | Initial cyclic-cover and symbolic metabelian Fox audit | .json, .out |
| e_review_fox.py | Independent free-word Schreier/Fox checks through order 24 | .json, .out |
| b_groups24.g | Every group and all generating pairs through order 24 | catalogue JSON, .out |
| b_all_covers24.py | All 9,714 epimorphisms, Schreier words, lattices, Alexander presentations and graded maps | .json, .csv, .out |
| b_normalizer_fill.py | Exact normalizer filling ranks and extra special element | .json, .out |
| b_elliptic_geom.py | All epsilon orbits and geometric brackets to the required degree fourteen | b_elliptic_results.json, .out |
| b_elliptic_normalizer.py | Invariant upper bounds and decisive degree-ten bracket rank | results JSON, .out |
| b_relative47.py | Correct relative source, every target invariant through nine, q7 lifts | .json, .csv, .out |
| b_factor_lifting.py | Exact PSL2(F13) counterexample to cusp preservation by finite-factor lifting, with both full generating subgroups checked | .json, .out |
| g_signed_fermat2.py | Integral rank-five Fermat cocycle, all110592 associativity and2304 comparison identities, exact characteristic-two liftable locus and complete marked polynomial kernel | .json, model JSON, .out |
| c_stack_checks.py | Integral atlas identities and small-characteristic/permutation checks | .json, .out |
| d_checks.py | Word identities, Magnus classes one–four, divided powers and counterexamples | .json, .out |
| d_nonlinear.py | Additive gluing counterexample, Vandermonde identities and closed pinched-ring patching; finite certificates supplementary to the proofs D.12–D.16 | .json, .out |
| d_surface.py | Exact denominator descent, interpolation, and nilpotent examples supplementing the all-base proofs D.17–D.21 | .json, .out |
| d_source50_extract.py | Exact original pages for the section 50 base and group quantifiers | .out, source_checks/140-4/ manifest and concordance |
| e_finite_braids.py | All cyclic power automorphisms through order 1,000 and declared matrix audit | .json, .out |
| e_genuine_shadows.py | Exact marked quotient family, both hexagons and arity-four pentagon | .json, .out |
| e_b3_quotient_export.g | All 1,946 normal kernels with marked B3 quotient order at most 1,000 | e_b3_quotients_complete.json, .out |
| e_b3_hexagons.py | Every finite hexagon candidate, surjectivity, source kernel and exact class-two genuine image | .json, .out |
| e_forgetful_refinement.py | Twenty deletion/cabling composites, four pentagon coordinates and all declared linking refinements | .json, .out |
| e_fake_shadow.py | Independent 54-point permutation certificate for a charming fake shadow | .json, .out |
| e_fake_shadow_arity4.g | Actual arity-four target and pentagon for the explicit fake example | .out |
| e_dll_pentagons.py | Published DLL targets N0, N1 and N2, practical/charming sets and actual pentagons | .json, .out; input e_dll_examples.json |
| e_exceptional_jets.py N | Simultaneous Hall group cycles at N=10,11,12; integral combination and full-word checks | e_exceptional_jets_N.json/.out |
| e_exceptional_lattice.py | Simultaneous integral class-thirteen Hall lift, exact lattice certificate and full-word verification | e_exceptional_lattice_13.json/.out; e_exceptional_matrix_13.json.gz |
| g_exceptional_14.py, g_exceptional_reduce14.py, g_exceptional_local14.py | Complete affine class-fourteen cycle system, exact rank and local congruence solve, integral Hall certificate, and independent full group-word verification | g_exceptional_matrix_14.json.gz, g_exceptional_reduction_14.json.gz, g_exceptional_local_14.json and associated .out logs |
| f_selmer_dimensions.py | Full/metabelian tripod dimensions through eight | .json, .csv, .out, paper table |
| f_elliptic_dimensions.py | Descent, rational point operations, reductions, and unconditional local/global tables through8 using F.16–18 | .json, .csv, .out |
| F_advanced_symbols.py | Exact level-32 Manin symbols, Hecke operators, quadratic twist and odd branch unit certificates for both elliptic curves | .json, .out |
| F_advanced_weight3.py | Weight-three CM modular-symbol lattice, Hecke eigenvalues, the required factor five in distribution, and all branch unit certificates | .json, .out |
| F_advanced_even_branches.py | Compatible level-five, twenty-five and one-hundred-twenty-five measure values and even-branch Iwasawa coefficients | .json, .out |
| F_advanced_cm_powers.py | Exact polynomial Manin symbols for CM powers one through six, integral Hecke eigenspaces and distribution, and required specializations modulo twenty-five | F_advanced_cm_power_1.json through F_advanced_cm_power_6.json and associated .out logs |
| F_advanced_real_sections.py | All real class-two pro2 cocycle orbits modulo2^n through n=8, Alexander involutions, and induced Fermat representatives; the full metabelian conclusion has a separate proof | .json, .out |
| F_advanced_global_sections.py | All390625 abelian pairs modulo5, multiplicative tame symbols at11, class-two obstruction counts, finite fibres and induced Fermat descent | .json, .out |
| F_advanced_unrestricted_sections.py | Exact prime and primitive-root certificates for the unrestricted-ramification cup counterexample; finite obstructions through5^12; the integral obstruction is proved by cochain completion | .json, .out |
| g_f_limit.py | Exact finite checks for the H1 inverse-limit counterexample and its compatible cocycle | g_f_limit_results.json, .out |
| g_special.py | CM character kernels and lower brackets through fourteen | results JSON, .out |
| g_kernel.py | Kernel checks and odd–odd contribution in degree fourteen | results JSON, .out |
| g_arithmetic.py | Ray-class, Minkowski and norm checks; arithmetic dimensions | results JSON, .out |
| g_embedding.py | Exact degree-six invariant, Tate lift, sign and normalization comparisons | results JSON, .out |
| g_degree8.py | Two middle vectors, the Sigma3 lift through degree eight, its Tate commutator, and the failed proposed constraint on the remaining CM scalar | results JSON, .out |
| g_cover_transport.py | Exact third-division polynomial and coprimality certificates for failure of automatic punctured transport from an elliptic Jacobian quotient | .json, .out |

The complete braid audit is stated in E.14–E.17. Its full shadows live on
explicitly declared arity-four refinements and project to the original
bounded braid quotients. This is distinct from enumerating every arity-four
conductor with an exactly prescribed arity-three kernel, or identifying
every global GT image. Full genuine images are determined for all 1,000
cyclic quotients and 354 noncyclic quotients with class-two H. The remaining
592 noncyclic genuine images have only the stated certified sublists.

## Commands

Representative executions are:

~~~sh
python a_small_actions.py > a_small_actions.out
python a_profinite_obstructions.py > a_profinite_obstructions.out
python b_lie_core.py 6 > b_sphere_tables.out
python b_tripod14.py > b_tripod14.out
python b_character_tables.py > b_character_tables.out
python b_pentagon_witness.py > b_pentagon_witness.out
python b_modcohom.py > b_modcohom.out
gap -q -A b_groups24.g > b_groups24.out
python b_all_covers24.py > b_all_covers24.out
python b_relative47.py > b_relative47.out
python e_exceptional_jets.py 12 > e_exceptional_jets_12.out
python f_selmer_dimensions.py > f_selmer_dimensions.out
python f_elliptic_dimensions.py > f_elliptic_dimensions.out
python g_special.py > g_special.out
python g_kernel.py > g_kernel.out
python g_arithmetic.py > g_arithmetic.out
python g_embedding.py > g_embedding.out
python g_degree8.py > g_degree8.out
~~~

Read large JSON files structurally instead of printing the entire minified
contents. In the class-twelve jet, combined_jet.hall_coordinates and the
seven fixed q7 exponents give the explicit integral word. Its Bezout
certificate is also in the paper. The later class-thirteen certificate
retains every variable of weights eight through thirteen simultaneously;
its exact denominators, Bezout coefficients and integral Hall exponents
are in e_exceptional_lattice_13.json. The sparse matrix is preserved in
e_exceptional_matrix_13.json.gz. Both group equations were independently
re-expanded and verified in the associative Magnus algebra.

The class-fourteen calculation retains all fixed quadratic terms and every
variable of weights eight through fourteen. Its exact 5,030-by-2,497
matrix has rank 2,066 and nullity 431. The definitive integral certificate
is g_exceptional_local_14.json; it records the 2,079 nonzero Hall
coordinates and the zero full-word defects. A successful reproduction,
with python-flint 0.9.0 available, is:

~~~sh
python g_exceptional_14.py build
python g_exceptional_reduce14.py --rank-only
python g_exceptional_local14.py
python g_exceptional_14.py verify g_exceptional_local_14.json
~~~

The two interrupted class-fourteen HNF approaches are retained in their
separate logs and status JSONs. They are superseded for existence by the
exact local-congruence calculation and its integral Bezout combination.
At this class, multiplying an affine right side would not multiply the
leading group term, because its quadratic terms must scale quadratically.
No such scaling argument is used.

The all-degree exceptional-prime theorem B.14d is independent of these
finite jets. Its proof uses the integral free-Lie module decompositions
of Bryant–Kovács–Stöhr and Kovács–Stöhr, norm surjectivity, the cohomology
exact sequence for the actual special-outer kernel lattice, and convergence
of successive automorphism corrections. The nonzero modular H1 groups
do not give an obstruction to this integral lifting problem.

## Additional Part E reproduction details

The finite permutation programs use NumPy 2.3.5 and the shared exact
right-action table implementation e_braid_core.py. The independent fake
example does not require GAP, LINS, SmallGrp or the quotient export.
e_dll_examples.json contains the original six permutation lists for each
published target, decoded as data from the official PackageGT archive;
its metadata records the original composition convention. The package
code was not executed. The audit explicitly handles the change from the
original functional-composition convention to the regular right action.

The exhaustive GAP search uses LINS 0.9 (15 March 2024):

https://gap-packages.github.io/LINS/doc/chap2.html

https://github.com/gap-packages/LINS

It calls LowIndexNormalSubgroupsSearchForAll with bound 1000 and the
unrestricted default options. SmallGrp is used only for optional labels;
unsupported identification data never remove a quotient. The authoritative
export is e_b3_quotients_complete.json. The GAP export script writes a path
relative to the parent of LM8_LIE_APPROXIMATIONS and should be run there;
the newer Python programs resolve their files relative to their own path.

The class-thirteen lattice program additionally uses python-flint 0.9.0.
In the recorded workspace it was invoked with PYTHONPATH pointing to
/workspace/scratch/d761ff801cc9/e_optional_deps. A clean reproduction can
install the stated dependency normally. Its untransformed Hermite form,
prime-unit column minors and integral Bezout combination avoid constructing
a large unimodular transformation matrix. Every reconstructed solution is
checked against the original matrix before the independent group-word check.

### Retained incomplete attempts

e_b3_all_quotients.json is a deliberately retained, truncated preliminary
export. It is not valid complete JSON and is not an authoritative quotient
table. Its log completed the 1,946-kernel search, but its slower export was
interrupted. e_b3_quotient_export.g and e_b3_quotients_complete.json supersede
that attempt. Intermediate equation-audit checkpoint files are likewise
superseded by the complete e_b3_hexagons.json.

e_exceptional_hnf_13.out records the stopped transformed-Hermite attempt
after its rank calculation; it contains no solution certificate.
e_exceptional_extend12.out records an alarm-stopped attempt to extend one
fixed class-twelve word using only weight-thirteen corrections. That attempt
gives no obstruction or existence conclusion. The successful simultaneous
class-thirteen certificate supersedes both for existence. Neither stopped
runs nor higher-class work in progress count as completed certificates.

## Limits and checks

The direct weight-fourteen tripod matrix exceeded available memory; its
failure log is retained. The successful degree-fourteen computation uses
proved character identities, checked against matrices in lower degrees.
The rank-seven relative source dimensions are computed by exact characters;
explicit lift formulas prove surjectivity in every weight, and the program
exhausts every smaller target invariant through nine.

Analytic ranks and global nonvanishing are primary source inputs, identified
separately from the exact computations. Metadata generation and document
assembly are not independent mathematical verification.

## GAP installation used here

Official GAP 4.15.1 core archive:

https://github.com/gap-system/gap/releases/download/v4.15.1/gap-4.15.1-core.tar.gz

SHA256: 2a81d008e1638f638a035b1cd981ca39436bdabbef8c29b15b24fceb2af678e4

SmallGrp 1.7.0:

https://github.com/gap-packages/SmallGrp/releases/download/v1.7.0/SmallGrp-1.7.0.tar.gz

The required-packages archive came from the same official GAP release and
its published checksum was checked. Configure/make required a writable
task-specific TMPDIR. An initial GitHub source checkout lacked autoconf;
the official release archive was used instead. A reader with standard
GAP and the listed packages does not need to rebuild them.

## Document assembly

The additional integral class-three and class-four calculation in F.22
is checked by F_advanced_integral_layers.py using only the Python standard
library. Its JSON and output log certify the cyclotomic discriminant,
Minkowski bound, character multiplicities, finite residue orders, Hall
bases, and 78,120 explicit cocycle recurrence equations. The finite
section counts are consequences of the proved cohomology calculation,
not an enumeration of an absolute Galois group presentation. Run it with
the command python code/F_advanced_integral_layers.py from the project root.

The actual class-five obstruction and cusp separation in F.23--F.24
are checked by F_advanced_class5.py, also using only the Python standard
library. Its JSON and output log retain the PB4 Artin representation,
all twelve presentation checks, the actual five-factor pentagon and its
determinant-minus-five minor, both integral local coordinate changes,
all 6250 local parameter checks, the 11-by-11 integral logarithm lattice,
and exact cyclotomic Kummer identities. The arithmetic cohomology and
the simultaneous global fourth-layer shift are proved in the paper.
The arbitrary global class-three frame-difference function remains
an explicitly identified coordinate problem; the relative Fermat
class-five sets and the unit-cusp separation are fully evaluated.
Run python code/F_advanced_class5.py from the project root.

root_metadata.py and the Part-specific generators write their own ledgers.
assemble_package.py validates statement IDs, normalizes readings, merges
bibliographies, records every checkpoint change, and writes the report.
build_paper.py runs LuaLaTeX/BibTeX and checks overflow, citations and glyphs.

The workspace had TeX binaries but incomplete format/font-module setup.
A local format, official CTAN Lua modules and font map were supplied.
A normal complete TeX Live installation uses the ordinary top-level
README build commands. The mathematical source is portable.

