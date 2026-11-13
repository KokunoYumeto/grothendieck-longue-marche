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
| b_lie_core.py 6 | Four-puncture special/inner/point-pushing/normalizer matrices through six | b_sphere_tables.json/.out |
| b_tripod14.py | Tripod matrix calculation through thirteen, exact character dimension at fourteen | b_tripod_dimensions.csv, witnesses JSON, .out |
| b_character_tables.py | Independent S3/S4 Witt characters and odd-generator dimensions | .json, .out, paper table |
| b_pentagon_witness.py | Full pentagon defects, including coefficient 16 for q7 | .json, .out |
| b_modcohom.py | H1/H2 over F2/F3 through nine; consecutive differential products | .json, matrices JSON, .out |
| b_coverings.py | Initial cyclic-cover and symbolic metabelian Fox audit | .json, .out |
| e_review_fox.py | Independent free-word Schreier/Fox checks through order 24 | .json, .out |
| b_groups24.g | Every group and all generating pairs through order 24 | catalogue JSON, .out |
| b_all_covers24.py | All 9,714 epimorphisms, Schreier words, lattices, Alexander presentations and graded maps | .json, .csv, .out |
| b_normalizer_fill.py | Exact normalizer filling ranks and extra special element | .json, .out |
| b_elliptic_geom.py | All epsilon orbits and geometric brackets to the required degree fourteen | b_elliptic_results.json, .out |
| b_elliptic_normalizer.py | Invariant upper bounds and decisive degree-ten bracket rank | results JSON, .out |
| b_relative47.py | Correct relative source, every target invariant through nine, q7 lifts | .json, .csv, .out |
| c_stack_checks.py | Integral atlas identities and small-characteristic/permutation checks | .json, .out |
| d_checks.py | Word identities, Magnus classes one–four, divided powers and counterexamples | .json, .out |
| e_finite_braids.py | All cyclic power automorphisms through order 1,000 and declared matrix audit | .json, .out |
| e_genuine_shadows.py | Exact marked quotient family, both hexagons and arity-four pentagon | .json, .out |
| e_exceptional_jets.py N | Simultaneous Hall group cycles at N=10,11,12; integral combination and full-word checks | e_exceptional_jets_N.json/.out |
| f_selmer_dimensions.py | Full/metabelian tripod dimensions through eight | .json, .csv, .out, paper table |
| f_elliptic_dimensions.py | Descent, rational point operations, reductions, local/conditional global tables | .json, .csv, .out |
| g_special.py | CM character kernels and lower brackets through fourteen | results JSON, .out |
| g_kernel.py | Kernel checks and odd–odd contribution in degree fourteen | results JSON, .out |
| g_arithmetic.py | Ray-class, Minkowski and norm checks; arithmetic dimensions | results JSON, .out |
| g_embedding.py | Exact degree-six invariant, Tate lift, sign and normalization comparisons | results JSON, .out |
| g_degree8.py | Two middle vectors and the exact remaining scalar ambiguity | results JSON, .out |

Later complete marked B3 quotient enumeration and further Hall experiments
are documented in sections/E_report.md and their own source/output files.
A running or failed experiment is not counted as a finished certificate.

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
certificate is also in the paper.

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

root_metadata.py and the Part-specific generators write their own ledgers.
assemble_package.py validates statement IDs, normalizes readings, merges
bibliographies, records every checkpoint change, and writes the report.
build_paper.py runs LuaLaTeX/BibTeX and checks overflow, citations and glyphs.

The workspace had TeX binaries but incomplete format/font-module setup.
A local format, official CTAN Lua modules and font map were supplied.
A normal complete TeX Live installation uses the ordinary top-level
README build commands. The mathematical source is portable.

