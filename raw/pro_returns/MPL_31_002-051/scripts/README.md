# Script roles

## Read-only checks

- validate_package.py: standard-library checks of page coverage, ordering, fragment syntax, required files, inventory values, doubt counts, procedural records and frozen digests. From the extracted package root, run the command shown below, or pass an explicit package-root argument.
- check_fragments.py: compiles existing page fragments through a temporary syntax wrapper. It requires an installed TeX environment and keeps compilation products outside the package; the recorded final compilation already covers all 46 frozen page files.

    python3 scripts/validate_package.py --phase final

## Recorded writing workflow

- save_page.py, audit_page.py, finalize_support.py, freeze_transcription.py and first_pass/: historical page-writing and support-generation steps. Several overwrite page files or rebuild the combined fragment. They belong to the completed, pre-context transcription workflow and should not be rerun on the frozen deliverables.
- build_research_notes.py and research/: research-note construction and context-query recording. This workflow reads the separately supplied context files, verifies the frozen transcription hashes, and writes only research deliverables and related records. Its original workspace paths document the run.
- finalize_package.py: verifies the completed dossier, writes final support records and a package manifest, and creates the final ZIP. It refuses to overwrite an existing output ZIP. Its transcript-integrity checks precede packaging, and it verifies archived bytes against the frozen digests.
- library_helpers/: helper scripts used for the requested durable hourly checkpoints and final file transfer.

The scripts preserve the operations actually used, including intermediate writing scripts. A rerun needs the corresponding inputs and runtime dependencies. The readable records and final files can be inspected without executing those historical writing steps.
