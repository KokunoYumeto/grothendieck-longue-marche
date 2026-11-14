# LM4_FINITE_GROUP_ACTIONS

**INCOMPLETE**

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority claimed.

The paper and its report retain every unresolved obligation. A successful
computation or PDF build does not change the mathematical status of a claim.
The report begins with the complete 39-obligation register.

## Main files

- `LM4_FINITE_GROUP_ACTIONS_paper.pdf` and `LM4_FINITE_GROUP_ACTIONS_paper.tex`: the self-contained paper.
- `LM4_FINITE_GROUP_ACTIONS_results.csv`: one row for each numbered statement.
- `LM4_FINITE_GROUP_ACTIONS_readings.csv`: doubtful manuscript readings and mathematical evidence.
- `LM4_FINITE_GROUP_ACTIONS_references.bib`: source metadata and individual verification notes.
- `LM4_FINITE_GROUP_ACTIONS_report.md`: proof, source, computation and remaining-obligation record.
- `manifest.csv`: exact size and SHA-256 hash of every other packaged file.

Registered statuses: Known=3, Open=3, Proved=239, Refuted=25.

## Complete finite-action index

Start with `code/part_b/low_complexity_catalogue_README.md` and
`code/part_b/low_complexity_catalogue_index.csv`. They route all 16 types,
882 mapping-class subgroup rows and 889 injective realization rows to their
exact section certificates. The exceptional realization fibers are retained.
All paths in the index are relative to this ZIP root.

The master assembler can be rerun from this directory:

```sh
python code/part_b/assemble_low_complexity_catalogues.py
```

Every required input is included. Packaging itself reruns this command and
compares all eight generated outputs byte for byte with the accepted outputs.

## Computation layout

`code/part_a`, `code/part_b`, `code/part_c`, `code/part_d_attack`, and
`code/root` contain the mathematical programs and their captured outputs.
Selected original `work/part_d_attack/code` paths are also retained so the
frozen review bindings remain literal. Isolated independent replays retain their
explicit `work/` directories. The archive also includes the finite presentation caches,
and the original machine-readable genus-two/genus-three census inputs.
The latter include their source attribution and hash verification. Individual
programs write their outputs beside themselves; invoke each by its file path.
Python 3.12 was used. The finite-presentation enumerators use SymPy; accepted exact checks also use
the Python standard library and the included modules. The explicitly marked
seven-point braid exploration uses NumPy and numerical crossing extraction;
it supplies no asserted relation or injectivity proof. Accepted certificates
use exact integer, rational, finite-field, permutation or free-word operations.
Every infinite assertion has its separate proof; exploratory files retain
their stated scope and are not promoted by inclusion in this archive.

## Paper build and source assembly

With LuaLaTeX and BibTeX installed, the root paper builds directly:

```sh
lualatex -interaction=nonstopmode -halt-on-error LM4_FINITE_GROUP_ACTIONS_paper.tex
bibtex LM4_FINITE_GROUP_ACTIONS_paper
lualatex -interaction=nonstopmode -halt-on-error LM4_FINITE_GROUP_ACTIONS_paper.tex
lualatex -interaction=nonstopmode -halt-on-error LM4_FINITE_GROUP_ACTIONS_paper.tex
```

The active modular sources and metadata are retained under `work/`.
Running `python work/root/assemble.py` regenerates the paper and registers
under a newly created `deliverable/` directory. The supplied
`work/root/build_pdf.py --full` configures writable TeX caches for the Linux
environment used here; an ordinary TeX installation can use the four commands
above instead. `pdf_qa.py` needs PyMuPDF and renders pages for visual review.
Its rendered images alone do not certify that they have been viewed.

`verification/` retains build logs, the assembly audit, PDF checks, visual
review records when present, and the packaged catalogue execution record.
