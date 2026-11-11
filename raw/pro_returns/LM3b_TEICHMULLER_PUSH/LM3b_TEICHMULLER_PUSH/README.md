# LM3b_TEICHMULLER_PUSH

This package contains the research paper, its statement and reading registers, source bibliography, source sections, and independent computational records. The work is AI-produced by **GPT-6 Astra (OpenAI, ChatGPT Pro mode)**, dated 11 November 2026. No priority is claimed.

The paper distinguishes full profinite groups, pro-prime groups, rational graded Lie algebras, and finite computations. Its numbered **Proved**, **Refuted**, **Known**, and **Open** statements specify the range and hypotheses of each conclusion. The result register is the authoritative index of those statements.

## Package contents

The common filename prefix is `LM3b_TEICHMULLER_PUSH`.

| File or directory | Contents |
|---|---|
| `LM3b_TEICHMULLER_PUSH_paper.pdf` | Rendered research paper |
| `LM3b_TEICHMULLER_PUSH_paper.tex` | Self-contained LuaLaTeX source |
| `LM3b_TEICHMULLER_PUSH_paper.md` | Assembled mathematical text before LaTeX conversion |
| `LM3b_TEICHMULLER_PUSH_results.csv` | One row per numbered statement, including dependencies and unresolved obligations |
| `LM3b_TEICHMULLER_PUSH_readings.csv` | Mathematical evidence concerning doubtful manuscript readings |
| `LM3b_TEICHMULLER_PUSH_references.bib` | Bibliography with source-verification notes |
| `LM3b_TEICHMULLER_PUSH_report.md` | Consolidated research, corrections, validation, and unresolved-obligation report |
| `sections/` | Editable mathematical sections, workstream registers, source lists, and research/audit reports |
| `audit/` | Editorial assembly and PDF-build records |
| `code/` | Independent programs, exact inputs, certificates, and recorded outputs |

## Dependencies

The computation runner requires **Python 3.10 or newer** and **SymPy**. The recorded calculations and final runner validation use Python **3.12.14** and SymPy **1.14.0**. To create an isolated environment on a POSIX system:

```sh
python3 -m venv lm3b-env
. lm3b-env/bin/activate
python -m pip install sympy==1.14.0
```

The full run additionally requires **g++ with C++17 support**. The recorded compiler is GCC **14.2.0**. The C++ sources use GCC facilities, including 128-bit integers and `<bits/stdc++.h>`; `g++` is the supported compiler command. Neither SageMath nor GAP is required. Assertions are enabled by the runner in both languages.

**Pandoc**, **LuaLaTeX**, and the TeX packages named in the supplied `.tex` file are needed only to rebuild the document. They are not dependencies of the mathematical computation runner.

## Quick verification

From any working directory, replace the example path with the extracted package location:

```sh
python /path/to/extracted-package/code/reproduce.py --quick
```

Quick mode runs ten mathematical programs. In particular, it independently reconstructs the finite cover automorphisms and verifies **all 64 dual inconsistency certificates**, checks that the supplied rational candidate bases retain their ranks modulo **65521**, and regenerates their serialized pentagon input. It also reruns the explicit special-derivation witnesses, the elliptic geometric image through degree twelve, the finite homology/coherence checks, the arithmetic algebra checks, the finite scalar and quaternion examples, and the bounded operator-identity check.

Quick mode uses the shipped `fg_candidates.json` and `ceh_pro2_certificates.json` as inputs. It does not regenerate the high-weight rational candidate spaces, rerun the C++ cover search or direct pentagon calculation, or rerun the spherical and elliptic normalizer matrices. No C++ compiler is needed for this mode.

## Full computational reproduction

The default mode reruns **all sixteen independent mathematical programs**:

```sh
python /path/to/extracted-package/code/reproduce.py
```

To select another compiler executable or a writable output directory:

```sh
python /path/to/extracted-package/code/reproduce.py \
  --compiler /usr/bin/g++ \
  --output /path/to/new-run-directory
```

The specified output directory must be new or empty. Without `--output`, the runner creates a unique directory under `reproduction/` in the extracted package. All source and input paths are resolved relative to the runner itself, so the command does not depend on the current working directory.

The runner uses the required ranges and respects these dependency chains:

1. `ab_lie.py 6`, which computes the requested spherical normalizer range through degree six; its unqualified standalone default is only degree four.
2. The other independent special, filling, elliptic, finite, and operator programs listed below.
3. `fg_prepare.py 12` → `fg_certify.py` → the compiled `fg_pentagon.cpp`, with `fg_pentagon_input.txt` supplied on standard input.
4. The compiled `ceh_pro2_cover.cpp`, with an explicit destination for its certificate file → `ceh_pro2_verify.py` applied to that newly generated file.

The runner copies the sources into an isolated temporary tree. Both C++ programs are compiled there with `-O2 -std=c++17`, and their executables are removed when the run ends. The temporary tree is also removed after a failed run. Compiled binaries are not required in the distributed package.

### Results and comparison policy

Each run preserves:

- `report.json`: selected mode, software versions, source hashes, exact subprocess commands, stage timings, comparison results, and overall success or failure;
- `logs/`: each program's standard output and error, plus compiler logs in full mode;
- `generated/`: the newly generated JSON, CSV, and input files that were compared with the recorded artifacts.

The original files in `code/` are left unchanged. The runner checks their hashes again at the end. JSON is compared structurally, CSV as ordered records, and serialized text as whitespace-separated tokens. The dynamic certificate output path in the C++ log is ignored. The independent verifier's certificate hash is checked against the actual certificate bytes used in that run; it is not treated as mathematical data when comparing verifier reports. Elapsed-time text in calculation logs is not compared, because the corresponding mathematical results have structured output files.

A missing output, failed assertion, nonzero process exit, or result mismatch makes the runner exit with status one. A successful run exits with status zero. Exact basis coordinates are part of the recorded data: changing a symbolic-algebra version can change basis choices, so the report records the SymPy version as well as the resulting comparisons.

## Mathematical source and output inventory

All paths in this table are relative to `code/`. The runner captures a fresh log under each program's basename. The shipped `.out` files are the recorded logs of the original individual calculations.

| Program | Computation | Principal recorded artifacts | Quick mode |
|---|---|---|---|
| `ab_lie.py 6` | Rank-two S3 character through degree twelve; rank-three special, filling, point-pushing, and normalizer matrices through degree six | `ab_lie_results.json`, `ab_lie.out` | No |
| `ab_kernel.py` | Filling-kernel indecomposables through degree six; explicit degree-three witness; elliptic ambient dimensions | `ab_kernel_results.json`, `ab_kernel.out` | No |
| `ab_weight5_witness.py` | Integral non-S3-invariant tripod derivation | `ab_weight5_witness.json`, `ab_weight5_witness.out` | Yes |
| `ab_degree3_conjugators.py` | Six integral rank-three conjugator recipes | `ab_degree3_conjugators.json`, `ab_degree3_conjugators.out` | Yes |
| `ab_elliptic.py` | Geometric epsilon-derivation image through degree twelve and explicit degree-seven noninner witness | `ab_elliptic_results.json`, `ab_elliptic.out` | Yes |
| `ab_elliptic_normalizer.py` | SL2 decompositions and the degree-ten normalizer constraint tested in degree fourteen | `ab_elliptic_normalizer_results.json`, `ab_elliptic_normalizer.out` | No |
| `ceh_checks.py` | Rational deck-action checks, finite cover homology, and central coherence calculation | `ceh_checks.json` | Yes |
| `ceh_pro2_cover.cpp` | Finite cover obstruction in the truncated Magnus algebra over F2; generation of dual certificates | `ceh_pro2_certificates.json`, `ceh_pro2_cover.out` | No |
| `ceh_pro2_verify.py` | Independent literal-word reconstruction and verification of all 64 dual certificates | `ceh_pro2_verification.json`, `ceh_pro2_verify.out` | Yes |
| `dg_checks.py` | Finite Heisenberg/CM algebra, tripod identities, integral Pfaffian identity, exponent bounds, and cyclic multiplicities | `dg_checks.out` (JSON) | Yes |
| `fg_prepare.py 12` | Exact rational antisymmetry, cycle, and cabling candidate spaces | `fg_candidates.json`, `fg_prepare.out` | No |
| `fg_certify.py` | Full-rank reduction of the candidate bases modulo 65521 and generation of the C++ input | `fg_certify_results.json`, `fg_pentagon_input.txt`, `fg_certify.out` | Yes |
| `fg_pentagon.cpp` | Direct infinitesimal-braid pentagon evaluation and ranks modulo 65521 through degree twelve | `fg_pentagon.out` | No |
| `fh_finite.py` | Scalar images for 792 finite two-generated abelian types of order at most 500; finite shadows, coinvariants, Q8 character obstruction, and boundary cochains | `fh_abelian_images.csv`, `fh_finite_results.json`, `fh_finite.out` | Yes |
| `quaternion_shadow.py` | Genuine nonabelian Q8 shadow and symbolic verification of its explicit Belyi model | `quaternion_shadow_results.json`, `quaternion_shadow.out` | Yes |
| `g_operator.py` | 7,260 bounded characteristic-two operator-identity checks | `g_operator_results.json`, `g_operator.out` | Yes |

The finite-shadow work contains the complete stated **abelian** enumeration and the independently checked **Q8** example. It is not an enumeration of all nonabelian quotients of order at most 500. The accompanying proof in F.13 also handles characteristic finite quotients of nilpotency class at most two: centrality of the commutator subgroup makes the images of the chosen generators depend only on the cyclotomic exponent. This is **generatorwise powering**, not the assertion that taking a fixed power is a homomorphism on every element of a nonabelian group.

The C++ pentagon program computes modular ranks. The rational dimension conclusions also use the rational candidate calculation, the reduction certificate, and the arithmetic lower bound proved or cited in the paper. Similarly, the finite cover certificates are combined there with the integral lifting and descent arguments. Successful execution certifies the listed finite calculations; the source-dependent and infinite-group proofs remain in the paper.

## Recorded runner validation

Both modes were executed from a working directory outside the extracted-package directory on 11 November 2026, using the final quaternion source and records. All comparisons passed, every shipped output remained unchanged, and the temporary build trees were removed. Observed elapsed times in the tested environment were:

| Mode | Mathematical programs | Artifact comparisons | Elapsed time | Result |
|---|---:|---:|---:|---|
| Quick | 10 | 12 | 26.206 seconds | Passed |
| Full | 16 | 19 | 166.515 seconds | Passed |

The full run included two fresh C++17 compilations in addition to the sixteen mathematical programs.

## Rebuilding the paper

The document build is separate from mathematical reproduction. To assemble the supplied section sources and registers, then compile the PDF:

```sh
python /path/to/extracted-package/code/assemble.py
python /path/to/extracted-package/code/build_paper.py
```

`assemble.py` requires Pandoc and rewrites the assembled Markdown, TeX, registers, bibliography, and editorial audit data from `sections/`. `build_paper.py` uses LuaLaTeX, stores intermediate TeX files in `_build/`, and writes the PDF and build audit. These scripts resolve paths from their own locations. The TeX source can also be compiled directly on a suitably configured TeX installation.

The runner does not invoke these editorial commands. No network access or original attachment directory is needed to rerun the bundled calculations. Reviewing the manuscript scans or checking the cited literature is a separate source audit, documented in the paper and workstream reports.
