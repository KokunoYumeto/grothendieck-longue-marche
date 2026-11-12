# LM1_GROUP_SCHEMES

AI-produced by **GPT-6 Astra (OpenAI, ChatGPT Pro mode)**, 12 November 2026.
No priority is claimed.

## Read the result

Start with `LM1_GROUP_SCHEMES_paper.pdf`. Its first-page table fixes the
matrix and sign conventions. The paper follows Parts A–E of the supplied
prompt and labels every numbered statement Proved, Refuted, Known, or Open.

`LM1_GROUP_SCHEMES_report.md` opens with the complete task-coverage table.
Its partial outcomes identify the proved cases, executed computations,
and exact remaining questions. They do not assert that every original
question has been proved in its full scope.

The two CSV files use exactly the requested column names. The JSON
component registers and component reports are retained so that the
aggregate registers and report can be regenerated. The bibliography
records which primary source, version, and theorem were actually opened.

## Mathematical computation

The calculations were executed with Python 3.12.14, SymPy 1.14.0, and
mpmath 1.3.0. Except for SymPy and its transitive dependency mpmath, the
mathematical programs use the Python standard library. No Sage, GAP,
database, or network access is required. Exact finite arithmetic is used.

Install the computation dependencies in an environment of your choice:

```bash
python -m pip install sympy==1.14.0 mpmath==1.3.0
```

Run commands from the extracted `LM1_GROUP_SCHEMES` directory. The
programs resolve their output paths relative to their own files. The
following reproduces the main calculations and their captured output:

```bash
python code/AB_identities.py > code/AB_identities.out
python code/AB_enumerate.py > code/AB_enumerate.out
python code/AB_general_finite.py > code/AB_general_finite.out
python code/AB_signed_finite.py > code/AB_signed_finite.out
python code/AB_functoriality.py > code/AB_functoriality.out
python code/AB_modular_comparison.py > code/AB_modular_comparison.out
python code/B_late_sections.py > code/B_late_sections.out
python code/C_presentations.py > code/C_presentations.out
python code/D_finite.py > code/D_finite.out
python code/D_components.py > code/D_components.out
python code/D_gt.py > code/D_gt.out
python code/D_number_fields.py > code/D_number_fields.out
python code/D_arithmetic.py > code/D_arithmetic.out
python code/D_motives.py > code/D_motives.out
python code/E_integrality.py > code/E_integrality.out
python code/E_envelope.py > code/E_envelope.out
python code/E_automorphisms.py > code/E_automorphisms.out
```

`AB_core.py` is a helper imported by `AB_enumerate.py`; its checks are
exercised by that run. `D_finite.py` also supplies exact matrix routines
to other D programs. Run `E_envelope.py` before `E_automorphisms.py`,
which reads its JSON cocycle output. Programs that produce JSON files
write them automatically in `code/`. Finite enumeration may take longer
than the polynomial checks; the included output is from actual runs.

The late source-audit supplements have their own programs and outputs
alongside these. Their precise scope is recorded in the corresponding
B supplement reports; the restricted-conjugator example is retained
with its exact finite output as well.

## Registers and bibliography

```bash
python code/AB_registers.py > code/AB_registers.out
python code/AB_modular_comparison_registers.py > code/AB_modular_comparison_registers.out
python code/B_late_sections_registers.py > code/B_late_sections_registers.out
python code/D_registers.py > code/D_registers.out
python code/E_registers.py > code/E_registers.out
python code/assemble_package.py > code/assemble_package.out
```

The other component JSON files are explicit editorial input to the
assembly program. The program checks the actual TeX input tree,
statement order and status, internal dependencies, citation keys,
CSV schemas, and all 40 primary and six followup coverage rows.

## Build the PDF with LuaLaTeX

On a normal TeX Live installation:

```bash
lualatex --interaction=nonstopmode --halt-on-error LM1_GROUP_SCHEMES_paper.tex
bibtex LM1_GROUP_SCHEMES_paper
lualatex --interaction=nonstopmode --halt-on-error LM1_GROUP_SCHEMES_paper.tex
lualatex --interaction=nonstopmode --halt-on-error LM1_GROUP_SCHEMES_paper.tex
```

Or use the included build helper:

```bash
python code/build_pdf.py > code/build_pdf.out 2>&1
```

The supplied execution host has LuaHBTeX and the TeX Live source/font
files but lacks generated formats, font maps, and luaotfload. The helper
therefore also supports this specific minimal-host case: it creates a
local, separately named Type-1 LuaLaTeX format in the sibling
`.tex_runtime` directory, replacing only the optional OpenType-loader
startup hook. The document uses installed T1 Latin Modern fonts.
It changes no system file and downloads nothing. A standard host uses
its existing stock LuaLaTeX format instead. The helper and successful
final pass logs are included; generated format binaries are not needed
in the ZIP.

The final log must contain no undefined citations or references,
missing characters, or overfull boxes. The PDF metadata and visual
checks are recorded in `code/package_audit.out`.

## Visual and package audit

`code/render_audit.py` uses Poppler's `pdfinfo`, `pdftotext`, and
`pdftoppm`, plus Pillow, to extract searchable text and produce all-page
contact sheets outside the deliverable directory. The contact sheets
were inspected, with selected dense pages also checked at full size.
`code/visual_review.json` records the actual inspection after it is done.

`MANIFEST.sha256` covers the delivered files except itself. It can be
checked with `sha256sum -c MANIFEST.sha256` from this directory.
Temporary TeX auxiliary files, bytecode caches, extracted background
papers, and the host's local format binaries are excluded from the ZIP.
The complete supplied-background archive is not redistributed.
