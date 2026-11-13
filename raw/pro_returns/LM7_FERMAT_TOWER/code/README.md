# Reproducing the mathematics and paper

The `.out` files contain actual saved output from the accompanying programs. The `.json` and `.csv` files retain exact coefficients, witnesses and coverage data. The programs use integers, rational numbers and finite rings; the elapsed-time fields in the Jacobi-sum output are the only numerical measurements that vary with the machine.

## Requirements

Use Python 3 with SymPy and NumPy, a C++17 compiler available as `g++`, and TeX Live with LuaLaTeX, BibTeX, Latin Modern and the standard AMS/table packages used by the master source. The mathematical programs use no external group-theory system. They can be run from any current directory. The small-group input is supplied, so reproducing the mathematical results does not require network access. The optional PDF rendering check also uses Poppler's `pdftoppm`, PyMuPDF and Pillow. Exact runtime versions are recorded in `runtime_versions.json`.

## Mathematical programs

| Program | Calculation and retained evidence |
|---|---|
| `a_finite.py` | Modular subgroup, quotient actions for every divisor of24, order32 subgroup, and congruence quotient witnesses. |
| `a_schemes.py` | Integral coordinate identities, finite fibers and the finite central-extension law. |
| `a_braid.py` | Normalized braid/congruence intertwiners and level12 action images. |
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
| `a_cubic_audit.py` | Independent Smith and framed-point checks of the cubic generalized-Jacobian calculation. |

Every mathematical program is documented in its module header and in the matching numbered statement. Its actual `.out` file is included alongside it.

Run a program with its ordinary Python command, for example:

```bash
python code/e_depth.py > code/e_depth.out
python code/e_smallgroups.py > code/e_smallgroups.out
python code/d_metabelian.py > code/d_metabelian.out
python code/d_gamma.py > code/d_gamma.out
```

`d_gamma.py` imports the shared Lyndon routines from `d_metabelian.py`; run the latter first to refresh its saved image bases. Other mathematical programs consume only their supplied inputs or generate the data they need.

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
