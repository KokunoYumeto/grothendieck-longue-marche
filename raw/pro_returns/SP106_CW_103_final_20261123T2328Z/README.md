# SP106_CW_103 — second-pass diplomatic transcription

## Scope and result

This package contains the completed second pass of Montpellier archive cote 103, scans 015–018. The four finished page files and the combined LaTeX fragment are the final transcription. The supplied images were read directly against witnesses C and H, then selected difficult places received a blind image-only reading by a different reader. The root reader decided the witness disagreements, open places, and every difference in the blind comparison on the saved crops.

The edition preserves the surviving text, including clipped words, apparent mistakes, abbreviations, missing accents, cancellations, overwriting, additions, and uncertain marks. It does not reconstruct missing edge letters or correct the author's mathematics. Seventeen places remain explicitly doubtful; their readings, alternatives, and reasons are in the doubts file and the page text.

| Scan | Main logged places | Against C | Against H | High / medium / low | Blind boxes | Different boxes | Places changed after audit |
| --- | ---: | ---: | ---: | --- | ---: | ---: | ---: |
| 015 | 17 | 12 | 15 | 14 / 1 / 2 | 29 | 18 | 3 |
| 016 | 13 | 7 | 8 | 10 / 1 / 2 | 21 | 8 | 2 |
| 017 | 15 | 2 | 14 | 8 / 4 / 3 | 16 | 10 | 4 |
| 018 | 10 | 4 | 9 | 6 / 2 / 2 | 14 | 4 | 1 |
| **Total** | **55** | **25** | **46** | **38 / 8 / 9** | **80** | **40** | **10** |

These are localized editorial counts, not word-error rates. A place can count against both witnesses. The 25 places against C comprise 11 primary-reading changes and 17 crop-resolved doubts, with three places in both groups. A partly resolved doubt counts once; repeated context in another row is not a second resolution. The 46 H discrepancies are the rows in the H collation. Newly added uncertainty with an unchanged primary reading does not create an extra main correction row, but all changes after the blind audit, including uncertainty-only changes, are recorded in the audit section.

The 40 different boxes are the results of the documented canonical token comparison. They include differences of surrounding context, punctuation, scope, and uncertainty, as well as substantive alternative readings. They are not a count of 40 accepted errors. Ten places changed in the page text after adjudication.

## Main deliverables

| File or directory | Contents |
| --- | --- |
| `pages/H103-02_103_scan015.tex` through `scan018.tex` | Four finished pages, named as in witness C. |
| `SP106_CW_103_transcription.tex` | One fragment beginning with `\cotefile{103}`, followed by the four pages in scan order. |
| `SP106_CW_103_changes.md` | Counts, mathematically relevant correction, per-page C/H/final readings and stroke evidence, unresolved places, and all ten post-audit changes with both readings. |
| `SP106_CW_103_collation.tsv` | The 46 discrepancies from H, with the required fields, classifications, and confidence. H's page number is our scan number minus one. |
| `SP106_CW_103_doubts.md` | Checked notation, 17 remaining doubts, abbreviations, and an assessment of legibility and the witnesses. |
| `SP106_CW_103_inventory.csv` | Every recorded text block, display, insertion, deletion, and margin element, with `transcribed=yes`. No drawing or diagram occurs on these leaves. |
| `SP106_CW_103_notes.md` | English notes by scan, including source assertions, local mathematical checks, the author's apparent slips, and metadata carried by the pages. |
| `SP106_CW_103_sheet_feedback.md` | Counts by error-sheet category, locations, and observations for subsequent work. |
| `SP106_CW_103_hand_log.md` | Fifteen documented handwriting, type, and correction habits with their local limits. |
| `CHECK_EVENTS.tsv` | Actual reading, adjudication, background, refinement, proof-check, and artifact-validation events. |
| `progress.log` | Start, page completion, blind audits, scheduled checkpoint, freeze hashes, and final unchanged-hash verification. |

The page files are LaTeX fragments, without a preamble. They use the supplied C preamble and standard LaTeX commands. That preamble remains in the original input package and is deliberately not duplicated here. No TeX compilation was performed. The supplied `\unsure{...}` convention is retained; a vertical bar separates alternatives inside its argument, with the preferred reading first. The macro itself prints its argument rather than choosing an alternative. The unusual detached name accent and the small low mark on scan 018 are represented with standard LaTeX positioning and uncertainty, not a drawing of running text. The only page comments record archive sheet numbers 14–17; they are not autograph page numbers.

## Reading and audit evidence

| Scan | First reader | Blind reader | First-stage crops | Blind crops |
| --- | --- | --- | ---: | ---: |
| 015 | reader_a | reader_b | 24 | 29 |
| 016 | reader_b | reader_c | 11 | 21 |
| 017 | reader_c | reader_a | 15 | 16 |
| 018 | reader_a | reader_c | 12 | 14 |
| **Total** | | | **62** | **80** |

The three first readers began on scans 015, 016, and 017 concurrently; scan 018 then went to reader_a. The first reader looked at the whole page and both supplied halves, then made the required first-stage crops. The root reader inspected the 62 first-stage crops, including the supplement on scan 016. After all four pages were first completed, each blind reader received only the images and a neutral box list for that page. The sealed first readings and witnesses were not included in those assignments. These are separate reader instances in one coordinated model workflow, not independent human examinations.

`second/` contains each page's neutral `_boxes.tsv`, sealed `_first.tsv`, blind `_second.tsv`, raw and canonical comparison files, adjudication table, and blind observations. The first and second TSVs are historical evidence and have not been rewritten to agree with the final page. `root_viewed=yes` records the root's personal examination of every differing second crop; the agreed raised `a` on scan 017 was also inspected to correct the H state collation. A matched box normally needs no new root image inspection. The root's original first-stage checking is separate.

`crops/` contains all **142** saved enlarged crops. `CROP_MANIFEST.tsv` identifies their original image boxes, source hashes, saved hashes, dimensions, transforms, reader assignments, and neutral box links. All lie inside the source bounds and occupy no more than 40% of the corresponding source width before enlargement. `SECOND_READING_COVERAGE.md` gives the membership of every required Method 7 category. Categories overlap and are not correction counts.

For scan 016's first-stage crops, the surviving first-reader records establish the transforms and target dimensions, but no original standalone first-crop generator survives. The manifest states that limitation. Coordinates and the actual enlarged images remain available; the other preserved crop scripts and all blind crop scripts are included.

`SOURCE_MANIFEST.tsv` contains paths and SHA-256 values for the supplied or derived input references. It identifies sources without copying them into this package. The original scans, witnesses, prompts, preambles, and source ZIP are excluded. No OCR, text-recognition library, external research, or extraction of an outside author's text was used.

## How to interpret the mathematics and confidence

The page's assertions are reported as assertions of the source. The local notes check two limited mathematical points: the degree shift on scan 015, and the conditional relative degree-zero kernel calculation on scan 016. The root and reader_c each checked these arguments, yielding four targeted-proof-check events for two arguments. No independent proof of the categorical classification or the displayed local complex is claimed.

The scan 016 slice denominator is an explicit case of a contextual tie-breaker: its cramped strokes admit `P`, `p`, or `\rho`; the same universal-torsor object is named `P` on scan 015 and its slice is identified with `X`. The final reading therefore puts `P` first while retaining the alternatives. A clear letter that conflicts with the expected mathematics would instead remain as written. The `e|c` subscript on scan 015 also remains doubtful despite the clear corresponding `B_e` on scan 016.

Confidence in the changes log describes the reading or the reported uncertainty, not the truth of the surrounding historical or mathematical claim. Broken type impressions, covered old letters, a detached accent, the phone digit, and a low isolated mark remain the least secure places. The doubts file identifies each one. Some apparently incorrect source forms, such as `intuile`, `cela un fait`, and `A toutes fin utile`, are deliberately preserved.

## Records, scripts, and authority

`records/NNN_final.json` is the final structured apparatus. `records/NNN_first.json`, the first crop records, and `NNN_root_review.md` preserve earlier stages; an earlier reading in those files is not an additional final reading. `drafts/` contains the readers' returned drafts, and `drafts/root_before_audit/` preserves the root page immediately before the blind audit was applied. Only `pages/` and the combined fragment are the finished edition.

The scripts are included to document the actual workflow. The report builders do not recognize or decide ink. To regenerate the present reports from final records, run `build_reports.py` followed by `build_support.py`, and then `build_events.py`. The first report builder produces a preliminary feedback file which the second replaces with the fuller final version. `compare_second.py` records raw token edits and the narrowly normalized comparison; it never changes the readings. `build_manifests.py` reads saved coordinate records and file headers and hashes, without rendering the images. `validate_package.py` performs static consistency checks, not TeX compilation or a new reading.

The first-reader, preparation, normalization, and application scripts are historical phase scripts. **Do not replay them over the final package**: they can recreate an earlier state. In particular, `apply_audit_decisions.py` was applied once, and `records/audit_applied.json` records that application. The later notation reconciliation is in the final page, final record, adjudication table, and progress log. The checkpoint script is likewise historical and must not be rerun to overwrite an existing checkpoint. Some early scripts retain the original workspace paths; replay would require the original inputs in the documented layout.

## Final validation and preservation

`VALIDATION.md` reports the bounded structural checks actually performed. `TRANSCRIPTION_SHA256.tsv` and the freeze entry in `progress.log` record the four page hashes and the combined-fragment hash. The same bytes are checked again immediately before packaging and against the ZIP contents. `PACKAGE_MANIFEST.tsv` lists each packaged file's size and SHA-256, excluding that manifest itself.

The scheduled checkpoint was saved under a new name 45 minutes after the start. Its receipt is retained in `records/checkpoint_01_receipt.json`; the checkpoint ZIP itself is not nested here. This final package retains the checkpoint's deliverables and documentation, with the final versions and later evidence added. Generated bytecode caches are not deliverables and are excluded.
