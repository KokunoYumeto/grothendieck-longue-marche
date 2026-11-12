# Reproducing the calculations and paper

The mathematical calculations use Python 3.12.14 and SymPy 1.14.0. They use exact integers, rational numbers, finite permutations, or exact algebraic-number arithmetic. None of the scripts simulates an unspecified arithmetic Galois element.

From the unpacked `CYCLOTOMIC_KERNEL` directory run:

```sh
python code/run_checks.py
python code/assemble_ledgers.py
python code/prepare_paper.py
bash code/build_pdf.sh
python code/validate_bundle.py
```

The first command runs all five finite mathematical certificate programs and records the output of each beside its source. `run_checks_output.json` records the runtime versions and exit statuses. The paper supplies the infinite and arithmetic arguments; the computations have only the scope stated in the corresponding proofs. The final validation command checks identifier coverage, compiler records, embedded fonts, the first-page notation table, and saved program outputs. It needs Poppler's `pdfinfo`, `pdffonts`, and `pdftotext`.

`assemble_ledgers.py` reads the authored statement records in `sections/`, writes the two CSV tables and report, and verifies that every numbered statement has exactly one results row. `prepare_paper.py` expands the preserved `sections/paper_master.tex` into a standalone main source, adds explicit manuscript-passage annotations from the results ledger where needed, combines the bibliography, and builds the consolidated source audit. Both scripts have their executed output in this directory.

The PDF needs LuaLaTeX, BibTeX, Latin Modern fonts, and the packages named in the source preamble. The main `.tex` file can be compiled directly with the supplied `.bib`, without regenerating it from the section files. The supplied PDF was compiled with LuaHBTeX 1.18.0 (TeX Live 2025/dev/Debian); final compiler and font checks are recorded in `build_output.txt` and `validate_bundle_output.json`.

The optional `fetch_root_sources.py` retrieves four opened primary-source PDFs and extracts their text with Poppler's `pdftotext`. Its archived output records URLs and SHA-256 hashes. Downloaded literature remains outside this ZIP. The other exact source versions, theorem numbers, and access limits are listed in `CYCLOTOMIC_KERNEL_source_audit.md` and the bibliography verification notes.

The three mandatory tasks marked unfinished in the report are not computationally certified by this bundle. The full-group and inverse-limit obstructions stated in E3, E4, and D15 remain as written in the paper.
