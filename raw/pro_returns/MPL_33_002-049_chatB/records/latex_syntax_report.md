# LaTeX syntax smoke test

Run started: 2026-11-15T13:48:16.093601+00:00.

The existing smoke_latex.py wrapper compiled all 48 individual frozen page fragments with /usr/bin/xelatex. Exit status: **0**; compiler output: **48 pages**. The transcript contains every expected scan002–scan049 filename. No syntax errors, warnings, missing-character messages, or overfull/underfull-box warnings were reported.

The script's before/after SHA-256 comparison found no changed page input. The separate final validation verified all 49 entries in records/frozen_hashes.sha256 before and after, including the combined fragment.

The wrapper is a temporary syntax check with neutral editorial macros, not a diplomatic rendering or visual accuracy audit. No deliverable fragment received a preamble.

Diagnostics: records/latex_smoke/compiler_output.txt, records/latex_smoke/smoke.log, records/latex_smoke/run_metadata.json, and records/latex_smoke/smoke.tex. Reproducible binary/auxiliary outputs remain excluded by the packaging script.
