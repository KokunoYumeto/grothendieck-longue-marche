# SP41_CW_81 diplomatic second pass

## Scope and authority

The requested sequence is scans 027–030 and 032–055 of cote 81, twenty-eight pages. Scan 031 is outside this task. The supplied scan images are the reading authority. C and H are draft witnesses; S is the supplied sweep. This archive contains the consolidated text, its apparatus, and the work documenting the decisions. It deliberately excludes the user's original scans, witnesses, sweep/context files, and earlier checkpoint archives.

## Deliverables

- `pages/`: one consolidated LaTeX fragment per decided scan, named as in C.
- `SP41_CW_81_transcription.tex`: combined fragment in scan order, with one cote header.
- `SP41_CW_81_changes.md`: witness differences, C doubt decisions, three-reader comparisons, local ink evidence, confidence and remaining doubts.
- `SP41_CW_81_collation.tsv`: substantive differences from H's transcribed text. Declared equivalent notation/macro renderings are excluded.
- `SP41_CW_81_doubts.md`: common notation, remaining doubts, abbreviations and the final legibility assessment.
- `SP41_CW_81_inventory.csv`: represented page elements and their written states.
- `SP41_CW_81_notes.md` and `CHECK_EVENTS.tsv`: source-based reading notes and the exact kind of checks performed.
- `progress.log`: run start, page completions, scheduled checkpoints and final freezing/hash checks.
- `SP41_CW_81_workflow.md`, `briefs/`, `readers/`, `crops/`, `decisions/`, `scripts/`, `validation/`: retained instructions, independent raw returns, visual evidence, adjudication records and reproducibility documentation.

C change counts include decisions that remove a resolved uncertainty marker; they are not estimates of C's error rate. H rows concern the primary reading, omissions, written state, placement and graphics, not doubt-marker syntax alone.

## Reading and validation

Each page receives three fresh independent readers. Each views its whole page once for layout and both halves once for line-by-line reading; unsettled places receive one tight enlarged crop. The main reader compares all three complete returns and personally views local crops for disagreements. The main reader does not view whole-page or half-page images. Raw reader returns are independent evidence; the consolidated decision file is authoritative for the final text.

No OCR, text-recognition library, PDF text layer, external research or LaTeX compilation is used. Structural scripts check braces, environments, delimiters, headers, sequence, C-doubt coverage and apparatus enums. Such checks do not certify either an ink reading or a mathematical proof. Mathematical check events describe the work actually performed.

## Reconstruction and archive state

See `validation/checkpoint_policy.md` for rebuilding source-only inputs from the original attachment and resuming a checkpoint. A page is complete only when its decision, page file, apparatus rows and `scan NNN done` line exist. A checkpoint may also contain an active page's unfinished raw work. Draft alignment files are mechanical comparison aids and have no independent authority. Historical `.pending` files and per-page adjudication scripts are retained working records; the final `decisions/scanNNN.json`, page file and completion log take precedence. Later metadata or cross-page QA may supersede an earlier script’s initial choices. Resume from saved decisions; rerunning an old adjudication script requires replaying its documented subsequent QA changes.

`ARCHIVE_MANIFEST.json` lists the archived files and their hashes. It is generated while packaging the same bytes that are written into the ZIP. All evidence paths in final decisions are relative to the archive where possible; original absolute paths in raw reader returns identify the initial workspace and can be rebased after restoration.
