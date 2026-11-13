# EXIT_ONE_TYPE

**Research status: INCOMPLETE.** The general comparison conjecture for good
projective compactifications in Part 3(c) is not proved or refuted. Its precise
formulation, the proved morphism case, the log-crepancy reduction, attempted
counterexamples, and the remaining gap are identified in the paper and report.
The unrestricted analytic and stack versions are refuted by explicit examples.

## Contents

- `EXIT_ONE_TYPE_paper.pdf`: LuaLaTeX paper, when the verified build is complete.
- `EXIT_ONE_TYPE_paper.tex` and `sections/`: complete mathematical source.
- `EXIT_ONE_TYPE_results.csv`: one row for each numbered mathematical statement,
  with status, actual theorem number, dependencies, and manuscript passages.
- `EXIT_ONE_TYPE_readings.csv`: mathematical support for manuscript readings,
  with paleographic uncertainty kept explicit.
- `EXIT_ONE_TYPE_references.bib`: verified bibliography and source-location notes.
- `EXIT_ONE_TYPE_report.md`: task-by-task result and source audit, limitations,
  computations actually executed, and proposed next steps.
- `code/`: all finite-check programs, complete identity expansions, and actual
  program outputs. These checks support the proofs; they are not proof assistants.
- `notes/`: detailed contribution and source-verification records.

## Rebuilding the paper

A normal installation of TeX Live with LuaLaTeX, `fontspec`, Latin Modern fonts,
AMS packages, `mathtools`, `natbib`, `hyperref`, `microtype`, and BibTeX suffices.
From this directory run:

```sh
lualatex -interaction=nonstopmode -halt-on-error EXIT_ONE_TYPE_paper.tex
bibtex EXIT_ONE_TYPE_paper
lualatex -interaction=nonstopmode -halt-on-error EXIT_ONE_TYPE_paper.tex
lualatex -interaction=nonstopmode -halt-on-error EXIT_ONE_TYPE_paper.tex
python3 code/assemble_delivery.py
```

`assemble_delivery.py` verifies that every numbered theorem, proposition,
counterexample, example, and conjecture has exactly one result row, that all
citations have bibliography entries, and that the final theorem numbers agree
with the LaTeX auxiliary file. The individual metadata registers under `notes/`
are its inputs.

## Repeating the finite checks

Python 3 with SymPy is required for the integer-matrix and symbolic checks.
Node.js is required for the independent JavaScript checks. Run the programs
from `code/` so that any relative output paths are reproduced there. Full
expanded identity products are supplied in JSON as well as in independently
generated Python and JavaScript versions.

The exact program names, outputs, and successful execution records are listed
in the report. The programs verify finite algebraic and combinatorial claims.
They do not establish infinite multicurve-poset connectivity, weak factorization,
exodromy, or mixed-Hodge theorems by computation.

## Conventions and attribution

The paper begins with its conventions. Exit arrows point from deeper strata to
more open strata. All stack homotopy types retain inertia. Algebraic and analytic
markings, ordinary categories and infinity-categories, normal boundaries and
global ends, and coarse dual complexes and graph homotopy quotients are kept
distinct. Citation notes specify whether a theorem location was verified in a
published article or a particular preprint version.

This is an AI-produced research draft. It makes no claim of priority or of
independent publication. A result marked `Proved` has a proof in this draft;
that label does not assert external peer review.
