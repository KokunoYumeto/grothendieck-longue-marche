# SECTION_GHOSTS — final incomplete research return

**INCOMPLETE.** Research stopped after the second consecutive hourly review without qualifying main-question movement, at 12:45:16 UTC (13:45:16 CET) on 18 November 2026.

AI-produced by **GPT-6 Astra (OpenAI, ChatGPT Pro mode)**. No human authorship or priority is claimed.

## Start here

- SECTION_GHOSTS_report.md gives the disposition of every requested task and lead, the main reductions, the precise remaining questions, and the stopping decision.
- SECTION_GHOSTS_paper.pdf is the current compiled research paper.
- SECTION_GHOSTS_paper.tex and sections/ contain its complete current source and the full stated proofs.
- SECTION_GHOSTS_results.csv is the authoritative result registry, using the literal requested column names.
- SECTION_GHOSTS_references.bib is the consolidated bibliography.
- CHECK_EVENTS.tsv records actual mathematical proof/source/computation events. It is not a count of external certifications.
- PROGRESS_LEDGER.md includes the recovered seventh review and the final eighth review.
- code/ contains the retained mathematical programs, outputs and reproduction tools.
- qa/ contains the actual final-page rendering and visual-review records.
- recovery_provenance/ distinguishes restored bytes, new transcriptions of reviewed proofs, and unpromoted notes.

The registry has **228 entries: 201 Proved, 15 Known, 3 Refuted and 9 Open**. These labels apply to the exact numbered statements, not to the full research request.

The Open entries are **A.2, A.7, B.1, B.2, B.3, C.7, D.3, E.120 and E.1**. Each Open row gives proved cases, actual computations, its exact remaining obstruction, a concrete outstanding instance, and failed approaches.

The historical audit has **90 entries: 87 confirmed, 2 repaired, 1 pending**. Its sole pending item is the literal numerical compiler in GT_TOWER_CHECK A4.57. The separate exact E.2 list of66 claims is audited.

## Main mathematical limits

We have neither proved finite support for every ordinary pair surviving the full pronilpotent tower nor constructed one ordinary infinite-support pair with a compatible full-tower section.

The strongest general reduction removes fixed-ramification H2 at every weight for regular odd coefficients. Simultaneous actual H1 support matching remains. The selected primitive-five family has off-five matched lifts through class seven and a global class-eight lift; weight-eight matching remains undecided. This follows from the already proved automatic nonresonant steps and does not change an Open status.

The fixed-class coefficient interpolation theorems are not nilpotency-class jumps. The finite-field point/cusp detector is not a global finite-support theorem. The full profinite rational-abelian case with actual ordinary local sections is settled by the cited Stix theorem, but merely abelian-local or pronilpotent data do not meet that theorem's hypotheses.

## Rebuild the current paper

On a complete TeX Live installation, use:

~~~sh
python3 code/build.py
~~~

For the stripped Debian runtime used for the final recovery, use:

~~~sh
python3 code/tex_recovery_bootstrap.py
~~~

See code/TEX_RECOVERY.md. The second command uses the bundled, hash-verified upstream dependency archives and requires no network download. It makes no system installation changes.

The final TeX sources are canonical. Integration and historical-update scripts record earlier production stages; they are not prerequisites for rebuilding the PDF. In particular, do not regenerate the final report from an earlier checkpoint without retaining the final verification appendix.

Run the source/CSV/citation consistency check with:

~~~sh
python3 code/recovery_registry_check.py
~~~

The recovery JavaScript verifier is standalone:

~~~sh
node code/verify_primitive_five_recovery.js
~~~

Its saved output is a JSON object in code/verify_primitive_five_recovery.json. The mathematical body was actually executed during the outage; no post-stop mathematical rerun is claimed.

## Recovery boundaries

Checkpoint08 was restored byte-for-byte and its archive SHA-256 verified. An exact copy is retained under checkpoints/. The current paper incorporates faithful mathematical transcriptions of later reviewed proof text. These transcriptions are not claimed byte-identical to the lost working files.

The exact original post-checkpoint E.214 and E.215 Python checker files and their original output-file bytes could not be restored into this final archive. Their actual earlier execution records and retained hashes are preserved. Earlier chat recovery blocks preserve the text that was still available; the separately executed JavaScript recovery verifier is included under its own name and provenance. No replacement is presented as the lost original.

The earlier post-E216 PDF and its final page count were not recovered. The present PDF was newly compiled from the consolidated current sources and separately visually checked. The old visual inspections are not used as evidence for this PDF.

The unpromoted class-five/class-six notes remain research notes and are not used to close an original Open task. The separately discussed class-nine calculation remained incompletely reviewed and is not promoted.

FILE_LIST.tsv inventories the final archive files with sizes and SHA-256 values, excluding its own self-referential hash. Final verification details are in FINAL_VERIFICATION.md and code/final_package_verification.json.
