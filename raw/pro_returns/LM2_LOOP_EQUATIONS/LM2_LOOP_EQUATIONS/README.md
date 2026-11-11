# LM2_LOOP_EQUATIONS

**The equation of loops in types (0,3) and (1,1): a proof audit, exact finite computations, and corrected comparisons for §§36–47 of Grothendieck's La Longue Marche.**

AI-produced by **GPT-6 Astra, OpenAI, ChatGPT Pro mode**, 11 November 2026. No priority is claimed.

## Start here

Read `LM2_LOOP_EQUATIONS_report.md` for the task-by-task outcome table and the detailed synthesis. Read `LM2_LOOP_EQUATIONS_paper.pdf` for the definitions, statements, proofs, source audits, and mathematical limitations. The paper has **60 pages and 79 numbered statements: 51 Proved, 12 Known, 10 Refuted, and 6 Open**. The six Open statements are explicit residual problems, not assertions of a completed proof.

The principal finite counterexample is an outer solution on a characteristic finite group of order **13^747**, with a pentagon obstruction in an actual finite pure-braid quotient. Its construction does not establish an infinite profinite element outside GT. The four remaining Part E records describe different formulations of one unresolved orbifold-compatibility family.

## Contents

| File or directory | Contents |
|---|---|
| `LM2_LOOP_EQUATIONS_paper.pdf` | The complete 60-page paper |
| `LM2_LOOP_EQUATIONS_paper.tex`, `sections/` | The complete LuaLaTeX source |
| `LM2_LOOP_EQUATIONS_references.bib` | Bibliography with source-verification notes |
| `LM2_LOOP_EQUATIONS_paper.bbl` | Generated bibliography retained for portability |
| `LM2_LOOP_EQUATIONS_results.csv` | One record per numbered statement, with its status |
| `LM2_LOOP_EQUATIONS_readings.csv` | 29 manuscript readings, corrections, and checks |
| `LM2_LOOP_EQUATIONS_new_conditions.csv` | Four remaining Part E condition records |
| `LM2_LOOP_EQUATIONS_condition_inventory.csv` | Supplementary complete inventory of 23 conditions |
| `LM2_LOOP_EQUATIONS_report.md` | Coverage table, findings, exact remaining obstructions, and audit scope |
| `code/` | All mathematical programs, outputs, exact data, audit records, and reproduction instructions |
| `MANIFEST.sha256` | SHA-256 hashes for every included file except the manifest itself |

## Reproduction

See `code/README.md` and `code/graded_README.md`. The mathematical programs use Python 3 and, where noted, SymPy. PDF rendering checks additionally use PyMuPDF. All reported successful calculations have saved outputs; interrupted and unsuccessful exploratory calculations are explicitly distinguished.

Build the paper from this directory with `python3 code/build_paper.py` using LuaLaTeX and BibTeX. The minimal-environment fallback used for the delivered build is documented. Verify the included file hashes from this directory with `sha256sum -c MANIFEST.sha256`.

The complete archive is self-contained for reading, checking the retained outputs, and reproducing its computations. The attached source scans and third-party preprints are referenced and audited but are not redistributed in this return.
