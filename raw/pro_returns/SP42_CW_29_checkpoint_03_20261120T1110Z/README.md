# SP42_CW_29 — consolidated diplomatic transcription

This package records a second reading of the 30 supplied scans of Montpellier archive cote 29. The scan identifiers follow the PDF page numbers; H page numbers are one lower. The input witnesses are unchecked AI drafts and are not treated as authority.

## Deliverables

- `pages/`: one consolidated LaTeX fragment per decided scan, named as in witness C.
- `SP42_CW_29_transcription.tex`: those fragments in archive scan order, without a preamble.
- `SP42_CW_29_changes.md`: witness differences, C doubt decisions, S adjudications, reader disagreements and crop evidence.
- `SP42_CW_29_collation.tsv`: substantive H differences only.
- `SP42_CW_29_doubts.md`: evolving notation, unresolved readings, abbreviations and legibility assessment.
- `SP42_CW_29_inventory.csv`: page elements and transcription coverage.
- `SP42_CW_29_notes.md`: page-derived notes, with mathematical claims distinguished from checks.
- `CHECK_EVENTS.tsv`: actual check events, with their limits.
- `SP42_CW_29_workflow.md`, `briefs/`, `readers/`, `decisions/`, `crops/` and `scripts/`: the work record.
- `progress.log`: UTC completion times, timed checkpoints and frozen hashes.

The original scans, full witness and sweep packages, and uploaded prompt are intentionally excluded. Derived evidence crops are included. The attached source ZIP remains necessary to reproduce a crop from its recorded coordinates. Its source paths may need to be changed after relocation.

The supplied PREAMBLE defines the required rendering conventions. The consolidated fragment does not silently supply missing typed symbols, normalize spelling, or correct mathematical slips. No external texts are researched. Static syntax validation is separate from palaeographic or mathematical confidence.

At checkpoints, the package contains only work actually completed or in progress as recorded; an undecided page's independent return is not a consolidated page. At final delivery, all 30 pages must have main-reader adjudications and frozen hashes.

## Source provenance supplied with the task

| Source | Supplied identification | Use in this run |
| --- | --- | --- |
| Scan images | Montpellier archive, Alexander Grothendieck papers, cote 29; 30 supplied scan pages with whole-page and overlapping half-page images | Authority for every reading |
| C | GPT-6 Astra, reasoning effort max; Codex web sessions dated 13–15 November 2026; folders A29-01 and C29-01 through C29-03 | Diplomatic draft, prior doubts and page notes; never treated as verified |
| H | Commutator project of Michel Hua, supplied commit aef7db2; stated models Claude Opus 5, Opus 5.5, and partial rereading by Claude Fable 5.2; effort not recorded | Independent draft; its page number is our scan minus one |
| S | Supplied sweep of 18–19 November 2026, c29a and c29b_c31; stated Claude Opus 5.5, effort max | Relevant CORRECTIONS rows treated as additional witnesses; editorial mathematics kept separate from ink |
| Present run | GPT-6 Astra Pro; configured effort not exposed | Three fresh independent readers per page, followed by main-reader crop adjudication |

These provenance statements reproduce the task’s supplied metadata; no external repository or publication was consulted to verify them. The task’s historical error-rate estimates are not used as substitutes for inspection or presented as measurements of this run.

Source packets are reconstructed by `scripts/prepare_page.py` from the original attached archive. Only a trailing H editorial heading with no subsequent page content is stripped; an internal section heading is preserved. Original-source copies and page excerpts are excluded from this deliverable package. The annotation snapshots and every independent return are retained.

Timed checkpoint upload uses the current platform-provided Library helper. After a workspace restoration, that helper can be refreshed through the Library skill; it is not bundled as part of the transcription source code. The checkpoint package itself contains the complete work record accumulated at its timestamp, including any explicitly unfinished adjudication journal.
