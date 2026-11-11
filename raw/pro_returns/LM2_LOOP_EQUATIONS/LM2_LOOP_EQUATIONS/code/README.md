# Computation and reproduction

All reported mathematical calculations have been executed. The `.out` files retain stdout; JSON and CSV files retain complete coefficients, residues, maps or certificates. The programs use Python 3; some additionally require SymPy. The run used Python 3.12 and the installed SymPy version recorded in `environment.json`.

## Exact mathematical programs

Run from this directory, using the same Python executable throughout:

```bash
python3 dictionary_matrices.py > dictionary_matrices.out
python3 arithmetic_checks.py > arithmetic_checks.out
python3 finite_congruence.py > finite_congruence.out
python3 finite_matrix_cycles.py > finite_matrix_cycles.out
python3 finite_shadows.py > finite_shadows.out
python3 finite_shadow_orders.py > finite_shadow_orders.out
python3 finite_s3_fields.py > finite_s3_fields.out
python3 arithmetic_s4.py > arithmetic_s4.out
python3 arithmetic_simple_audit.py > arithmetic_simple_audit.out
python3 finite_noncongruence.py > finite_noncongruence.out
python3 finite_phi.py > finite_phi.out
```

`finite_groups.py` is the shared exact group library and has no separate standalone output. The graded programs and their reproduction order are listed in `graded_README.md`. Their successful sequence computes dimensions, a pentagon witness, the first lifting obstruction, a class-twelve rational jet, its finite reduction, the actual braid transfer, and the specified preprint identities. Larger rational linear systems can require sustained CPU time and memory. No random sampling supports a claim of exhaustive enumeration.

Three exploratory programs are retained but excluded from the successful sequence: `graded_greedy_jets.py` (a particular coefficient choice fails) and the interrupted `graded_global_attempt.py` and `graded_block_attempt.py`. Their outputs are evidence of the attempts, not proofs of impossibility.

## Registers and source audit

```bash
python3 build_registers.py > register_audit.out
```

The included `ledger_inputs/` directory supplies the exact records. The audit expands the TeX input tree, checks a one-to-one match of all claim IDs and statuses, and writes the results, readings, new-conditions and complete-inventory CSV files. It is a consistency check, not a proof assistant. The source-audit notes preserve which theorem hypotheses and original scans were inspected.

`insert_manuscript_anchors.py` is an idempotent editorial utility for explicit locator lines. It does not infer manuscript folios and is unnecessary for the already assembled source.

## Paper build

From the package root:

```bash
python3 code/build_paper.py
```

This runs LuaLaTeX, BibTeX, and two more LuaLaTeX passes. It requires a standard TeX installation with the packages named in the preamble. Type 1 Latin Modern and AMS font maps are explicitly loaded. On the minimal Debian TeX tree used for this run, the filename database and prebuilt format were unavailable; the following documented fallback builds a workspace-local format and makes no system changes:

```bash
python3 code/build_paper.py --local-tex-tree
```

The local runtime lacks the optional OpenType loader and reports its standard fallback at startup. This document uses Type 1 fonts explicitly; the final checks require no TeX errors, unresolved citations/references or missing glyphs. The packaged PDF was rendered and visually inspected, including its first-page notation table and dense mathematical tables.

## Render and package checks

From the package root, `python3 code/render_pdf_qa.py` renders every PDF page with PyMuPDF and checks for empty pages and text outside the page boundary. It writes its JSON audit and page/contact-sheet images under `.build/qa/`. All four contact sheets and selected full-size pages were visually inspected for the delivered 60-page PDF.

`python3 code/package_artifacts.py` checks required files, parses all Python and JSON files, checks CSV counts and retained program outputs, writes `MANIFEST.sha256`, and creates the ZIP in the parent directory. The package includes its audit JSON and stdout. Temporary rendering images, Python caches and root-level TeX auxiliary logs are excluded; the generated bibliography and the final build logs are retained. These checks establish artifact consistency, not a machine-verified proof of the mathematical statements.

## Claims and non-claims

Finite shadow groups are not silently identified with the images of inverse limits. Raw finite cycle pairs are not asserted to lift. Matrix descent and generation are tested separately. The class-twelve finite BCH group is checked by an exact presentation, not by enumerating its 13^747 elements. Its pentagon obstruction is evaluated in an actual finite pure-braid quotient; it does not establish an infinite pro-13 or full profinite solution.
