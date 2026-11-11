# LM3_TEICHMULLER_TOWER

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 11 November 2026. No priority is claimed.

## Contents

- LM3_TEICHMULLER_TOWER_paper.pdf — the paper, Parts A–F, with numbered and classified assertions.
- LM3_TEICHMULLER_TOWER_paper.tex and sections/ — complete LuaLaTeX source.
- LM3_TEICHMULLER_TOWER_results.csv — one row per numbered assertion.
- LM3_TEICHMULLER_TOWER_readings.csv — mathematical evidence for uncertain manuscript readings, with its strength and visual limitations.
- LM3_TEICHMULLER_TOWER_references.bib — opened-source verification notes and precise references.
- LM3_TEICHMULLER_TOWER_report.md — the research, computation, correction and remaining-gap audit.
- code/ — reproducible standard-library Python programs and saved outputs.
- audit/ — source fragments, proof-pack audit details, citation normalization and validation records.
- SHA256SUMS — checksums for the delivered files.

## Compile the paper

From this directory, with a normal TeX Live installation providing LuaLaTeX, Latin Modern, fontspec, mathrsfs, natbib, xurl and the standard AMS packages:

    lualatex -interaction=nonstopmode -halt-on-error LM3_TEICHMULLER_TOWER_paper.tex
    bibtex LM3_TEICHMULLER_TOWER_paper
    lualatex -interaction=nonstopmode -halt-on-error LM3_TEICHMULLER_TOWER_paper.tex
    lualatex -interaction=nonstopmode -halt-on-error LM3_TEICHMULLER_TOWER_paper.tex

The PDF is supplied; recompilation is optional. The archive does not bundle a TeX distribution or copies of the supplied copyrighted background papers.

## Rerun the computations

Python 3.10 or later, standard library only:

    python code/af_checks.py
    python code/bc_counterexamples.py
    python code/d_counterexamples.py
    python code/e_deletion_checks.py

The E program writes audit/E_computation.json; the D program writes code/d_counterexamples_output.json. The A/F and B/C programs write their reports to standard output.

To regenerate and validate the registers and normalized bibliography:

    python code/build_af_register.py
    python code/build_registers.py
    python code/build_report.py

## Status caveat

A proved conditional implication does not certify its antecedent. “Open” includes established open problems, unrefereed claims not independently certified here, and exact comparisons unresolved by this audit; each entry states which applies. “Verified” in the bibliography means the primary source was opened, not that its whole proof was independently re-proved. See the report before interpreting the aggregate counts.

