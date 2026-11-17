ANABELIAN_A1 — research audit and continuation
AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority claimed.

Read ANABELIAN_A1_report.md first: it opens with the outcome of every task item and check. This return remains INCOMPLETE wherever that table says Open.

ANABELIAN_A1_paper.tex is the flattened standalone manuscript. Build in this directory with LuaLaTeX, BibTeX, then LuaLaTeX twice. Its bibliography is ANABELIAN_A1_references.bib. A verified PDF is included.
ANABELIAN_A1_results.csv has one row for every numbered statement and the exact requested columns.

sections/ contains editable source inclusions; notes/ contains audits, working-to-final number maps, metadata, source logs, and timing/QA records. code/ contains all programs, actual outputs, and finite certificates. Some .out files intentionally preserve failed intermediate attempts; the report identifies the successful independent verifiers. Third-party original source PDFs and the supplied attachments are not duplicated. Source URLs, hashes, and retrieval scripts are retained.

Rebuild assembly with python code/assemble_paper.py. Read code/requirements.txt for computational dependencies. Most finite verifiers use standard Python; polynomial computations use python-flint, sympy, or numpy as specified in the programs. Large polynomial certificates in code/primitive_certificates are complete data, not checksums alone.

No earlier checkpoint ZIP is included or overwritten. The package manifest gives hashes and sizes of its contents. The exact first-field or least-prime claims concern the curves and pointing specified in the paper and must not be expanded to the unresolved whole census.
