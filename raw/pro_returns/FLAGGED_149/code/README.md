# Reproduction and scope

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed.

The computation scripts check explicit examples and algebraic identities. Their outputs are attached. They do not establish a general assertion from finite data; the arguments that pass to profinite groups, inverse limits, or infinite valuations are in the paper.

## Mathematical checks

Use Python 3.10 or newer with SymPy (the recorded run used SymPy 1.14.0):

```bash
python code/AB_checks.py
python code/CF_checks.py
python code/CF_hyperplane.py
python code/CF_h2_checks.py
python code/DE_checks.py
python code/G_checks.py
python code/F7_test.py
python code/F7_test5.py
```

Each script writes or prints the exact result recorded in its neighboring output file. Read the script's header for the exact scope. No credentials, external accounts, or network calls are used by these checks.

## Paper

A complete TeX Live installation with LuaLaTeX, BibTeX, Latin Modern, fontspec, AMS packages, geometry, microtype, enumitem, needspace, fancyhdr, hyperref and xurl suffices. From the ZIP's root:

```bash
lualatex -interaction=nonstopmode -halt-on-error FLAGGED_149_paper.tex
bibtex FLAGGED_149_paper
lualatex -interaction=nonstopmode -halt-on-error FLAGGED_149_paper.tex
lualatex -interaction=nonstopmode -halt-on-error FLAGGED_149_paper.tex
```

The section files are inputs of the main TeX file and must remain under `sections/`.
The PDF is the compiled deliverable. The first page and report deliberately state INCOMPLETE because the Open results are not claimed solved.

## Ledgers

`assemble_ledgers.py` checks that each numbered result has exactly one metadata row and that every citation key has a bibliography entry. The original JSON inputs are retained under `audit/ledger_inputs/`. It synchronizes statement text with the TeX, keeping the full hypotheses in the CSV. The reading ledger preserves the distinction between an inspected image, first-pass evidence, and a mathematical correction.

`assemble_report.py` verifies the thirty required coverage rows and builds the report from the retained coverage inputs. Its counts are read from the ledger assembly output.
