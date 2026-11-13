# LM8_LIE_APPROXIMATIONS

**INCOMPLETE research return**, 13 November 2026. The report and paper retain
every unresolved obligation. This package does not claim to satisfy the
prompt's all-items completion criterion.

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority claimed.

The report states the exact proof, computation and verification scope.
The source manuscript, earlier AI returns, and reviews are inputs to be checked,
not authorities. Programs in `code/` carry their own scope descriptions.

## Contents

The paper is supplied as LuaLaTeX source and PDF. The results CSV has exactly
one row per numbered statement. The readings CSV, verified-source bibliography,
complete report, all component sources, and all research programs/outputs are
included. The audit directory records build checks and changes from every
immutable earlier checkpoint.

See code/README.md for reproducible computation commands and resource scope.
Finite tables are not promoted to infinite theorems, and conditional Selmer
tables are identified explicitly.

## Build

With a complete TeX Live installation, run LuaLaTeX, BibTeX, and two further
LuaLaTeX passes on LM8_LIE_APPROXIMATIONS_paper.tex.
The command below performs these passes and audits the result:

~~~sh
python code/build_paper.py
~~~

To regenerate the root-owned metadata, assembled ledgers and report:

~~~sh
python code/root_metadata.py
python code/assemble_package.py
~~~

Part-specific metadata generators are included separately. The assembly script
checks that the paper's statement IDs and the results ledger coincide exactly.
