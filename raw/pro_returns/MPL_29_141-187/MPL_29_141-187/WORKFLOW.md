# Working record

This package is a diplomatic, manually read transcription of cote 29, scans 141–187. No OCR was used. The primary reader alone viewed and transcribed every full image and both supplied halves in scan order, then personally reread all 47 pages against their images in a second audit. Mechanical support was limited to balanced-macro indexing, package checks and LaTeX compilation/rendering; no supporting agent read a scan or made a manuscript reading decision.

All 47 first-pass fragments, inventory rows and actual UTC completion entries are present. All 47 second visual audits are logged. The current combined fragment agrees exactly with the ordered page fragments. Recurring symbols were compared before context access, including the Gothic Z/F distinction on 141/143/152, Pi/Phi on165–170, and zeta/xi on185–186. The doubts file includes the common notation table, all current doubt macros, selected difficult loci, abbreviations and limitations; historical reading proposals remain in the auxiliary TSV files with their superseded status explained.

The 47-page compilation and visual layout QA are complete. All 48 SHA-256 hashes were recorded and the transcription was frozen at 2026-11-18 06:35:56 UTC. Context opening was logged after the freeze, at that same recorded second; the context was then extracted, and README and RESULTS_STATE were read before research drafting. No page or combined-transcription changes were made after that point. The complete supplied modern context was read collaboratively for research only. The primary reader wrote the late simplicial notes and integrated the report, while supporting agents compared the already-frozen text with assigned context ranges and checked selected mathematics; they did not read scans.

The consolidated research report is MPL_29_141-187_notes.md: 61 main notes, 10 entries on explicitly unverified manuscript steps, and 15 title/heading/count entries. All 86 items have actual context-query and search records. CHECK_EVENTS.tsv contains 69 mathematical check events, with proof attempts, counterexamples and external background distinguished; textual comparison and bibliographic checking are not counted as proof events. Detailed proof records, candidate drafts and historical reading records remain as work documentation, with the consolidated report and current doubts table authoritative. The final editorial review checked source quotations, context locators, one-to-four-sentence note prose and own-idea confidence fields.

The first hourly checkpoint was saved at 05:58:52 UTC, after local ZIP creation at05:58:46 UTC. Checkpoint02 was created at06:58:56 UTC and saved at06:59:28 UTC. Checkpoints contain all deliverables and work documentation available at the time, excluding supplied scans, source archives, complete context materials and previous checkpoints. The final package uses the same exclusions. The uploaded prompt controls the task throughout.

## Deliverable map

| File or directory | Content |
|---|---|
| MPL_29_141-187_transcription.tex | All47 scans in order as one LaTeX fragment, without a preamble. |
| pages/ | The47 individual diplomatic fragments. |
| MPL_29_141-187_doubts.md | Package notation table, current doubts, difficult loci, abbreviations and legibility limits. |
| MPL_29_141-187_inventory.csv | 787 inventoried elements, all marked yes; one consistent sheet kind per scan. |
| MPL_29_141-187_notes.md | The consolidated English research report; note IDs used by the check log. |
| CHECK_EVENTS.tsv | Actual mathematical check events and precise outcomes. |
| progress.log | Actual UTC completion/audit times, pre-context hashes, freeze, context opening, checkpoints and final hash verification. |
| records/ | Compilation/structural/editorial QA and per-item context-search evidence. |
| research_drafts/ | Supporting arguments, candidate records and research provenance; not an alternative transcription. |
| scripts/ | Reproducible indexing, fragment QA, context-query recording, research integration and packaging checks. |

The transcription uses the task's wrapper macros; their demonstration definitions and required LaTeX packages are in scripts/latex_qa.py. That script was used to compile the fragment for inspection, but the resulting PDF and rendered images are not deliverables and are not in the ZIP. Its role was syntax and layout QA, not OCR or automated manuscript reading. The final structural checks are scripts/validate_package.py and scripts/validate_research.py; neither script certifies the truth of the mathematics or substitutes for the visual reading.
