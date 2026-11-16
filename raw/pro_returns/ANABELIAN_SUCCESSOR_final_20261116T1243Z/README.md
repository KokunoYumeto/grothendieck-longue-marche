# ANABELIAN_SUCCESSOR

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 16 November 2026.
No human authorship or priority is claimed.

## Current mathematical return

Read `ANABELIAN_SUCCESSOR_report.md` first. Its first line is INCOMPLETE
because several requested statements remain undecided; its opening table
has every item A1–A10, F1–F6 and lead L0–L11.

`ANABELIAN_SUCCESSOR_paper.pdf` is the checked LuaLaTeX paper.
`ANABELIAN_SUCCESSOR_paper.tex` is its self-contained source.
`ANABELIAN_SUCCESSOR_results.csv` has the exact nine requested columns
and one row per numbered claim. The bibliography records whether each
entry was opened and verified.

The main injectivity theorem is A.3, with the finitely generated field
corollary in A.2. The independent fixed-prime cuspidal proof is in
A.88–A.90; it does not assume full prime-to-p configuration-fiber
injectivity. The full configuration-fiber obstruction is A.87.
The explicit nontrivial primitive-cover counterexample is A.86.
The fixed norm-module and full-section comparison is A.48.
The final higher-genus Kummer result is F.50.

## Reproducibility and retained history

`code/PROGRAM_INDEX.csv` lists the canonical retained programs and their
nearby outputs. `code/A4_quartic_witnesses.csv` is the consolidated
pointed-quartic witness table; the other exact census and certificate
tables are retained with their programs. Computational limitations and
the distinction between tested values and proved least primes are stated
in the paper and report.

`code/retained_agent_code/CONTENTS.csv` maps byte-identical delivery
copies of agent programs and outputs into `code/`. Their original
research paths are also preserved so that the documented invocations
and relative input paths continue to work. Run a program from its
original location unless its own instructions specify otherwise.

`notes/`, `qa/`, and the three agent directories preserve source checks,
independent mathematical audits, failed approaches, exact programs,
outputs, build logs and rendered-page checks. Historical drafts may use
provisional identifiers or superseded statuses. The assembled paper,
results register and report are the current authority within this
return; `notes/statement_map.json` translates the working identifiers.
The separate fixed-r drafts retained in the F directory were integrated
in Part A and do not add duplicate Part F claims.

`code/assemble_paper.py` assembles the owner sources and register;
`code/build_latex.py` records the complete LuaLaTeX/BibTeX build;
`code/verify_deliverables.py` checks the document and inventory.
These are reproducibility checks, not automatic proof verification.
The dependency-register audit excludes forward explanatory references
from the main proof premises and retains its before/after records.

The archive contains no supplied background attachment, third-party
source-paper cache, previous checkpoint ZIP, or runtime dependency cache.
The original background remains necessary to reproduce checks expressly
documented as readings or computations on the supplied material.
`ARCHIVE_MANIFEST.json` records the byte size and SHA256 of every
retained file.
