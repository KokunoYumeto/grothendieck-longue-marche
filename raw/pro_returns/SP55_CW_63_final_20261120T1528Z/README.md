# SP55_CW_63 — consolidated diplomatic transcription and audit records

This bundle documents the second-pass collation of 26 scans from cote 63 of the Montpellier archive: scans 21–34 and 41–52. Scans 35–40 belong to another task. The consolidated LaTeX follows the supplied diplomatic conventions; the scan images, not either earlier transcription, determine the readings.

## Completion status

All 26 first readings and all 26 second image readings are complete, in the requested order. The recurring notation was compared across both texts and folder boundaries. The 26 page files and combined fragment have been frozen with SHA-256 entries in `progress.log`; the closing verification entry records whether they remained unchanged through final packaging. `READING_STATUS.md` confirms that there is no next page to read.

The comparison records contain 102 distinct places: 14 against C and 89 against H, with one place counted against both. Their confidence counts are 82 high, 19 medium and 1 low. H's total includes 70 omitted blocks on its seven partially transcribed pages. There are 54 remaining doubt entries, 85 certainty/scope entries, 539 inventory elements and 73 check events. The 84 crop boxes are documented without returning images.

The primary reader performed every image reading and every textual decision in one ordered stream. Mechanical assistance checked structure, record consistency and specified finite computations. No OCR, other text-recognition software, external textual research or TeX compilation was used. An encoding repair in the alpha command on scan 46 is documented separately from reading changes.

## Contents

| File or directory | Purpose |
| --- | --- |
| `pages/` | One consolidated LaTeX fragment per scan, using the original witness C filenames. |
| `SP55_CW_63_transcription.tex` | All consolidated page fragments in scan order, without a preamble. |
| `SP55_CW_63_changes.md` | Differences from C and H, visible evidence, crop coordinates, confidence, counts and consequential corrections. |
| `SP55_CW_63_collation.tsv` | Differences from H on the seven scans for which H supplies source text. |
| `SP55_CW_63_doubts.md` | Notation table, unresolved readings, certainty-only decisions, abbreviations and legibility assessment. |
| `SP55_CW_63_inventory.csv` | Page elements and their transcription status. |
| `SP55_CW_63_notes.md` | Page-specific mathematical and documentary notes, with check-event identifiers where applicable. |
| `CHECK_EVENTS.tsv` | Events classified by the kind of checking actually performed. Reading a statement is not itself a proof check. |
| `SP55_CW_63_sheet_feedback.md` | Counts for all ten error-sheet categories, including zero counts. |
| `SP55_CW_63_hand_log.md` | Observed handwriting, notation and machine-form habits, their scope and witness consequences. |
| `progress.log` | UTC reading/audit events, transcription freeze and closing SHA-256 verification. |
| `CHECKPOINTS.md` | Checkpoint history and saved-file identities. Earlier checkpoint ZIPs are not embedded in this bundle. |
| `records/` | Structured editorial records used to regenerate the derived reports. |
| `scripts/` | Numerical checks, editorial bookkeeping, source/crop inspection helpers, structural validation and packaging. |

The transcription files are fragments using the macros in the supplied witness `PREAMBLE.tex`; they are not standalone TeX documents. The original scans, witnesses, context material, crop images and earlier ZIPs are intentionally excluded. Crop evidence is retained as scan numbers and original-image pixel boxes in the changes log.

## Read-only numerical checks

Run the following commands from the extracted bundle's root directory, the directory containing `scripts/`, `pages/` and `CHECK_EVENTS.tsv`.

These numerical scripts use **Python 3 and its standard library only**. They do not read the scans or witness files, use external tables, edit the bundle or require the sibling `input/` directory. They print their finite arithmetic results to standard output. The associated check-event IDs below refer to the existing editorial records; a script reproduces the stated finite calculation, not every theorem discussed on that page.

| Command | Associated `CHECK_EVENTS.tsv` statement ID | Finite calculation |
| --- | --- | --- |
| `python3 scripts/check_partition_243.py` | `S043-P243` | Partition coefficient at 243, the integer `24n-1`, and the indicated remainders. |
| `python3 scripts/check_modular_coefficients.py 0` | `S043-C0` | The constant coefficient of the normalized modular series. |
| `python3 scripts/check_modular_coefficients.py 13 91` | `S044-ACCIDENT` | Coefficients at indices 13 and 91 and their remainders modulo 13. |
| `python3 scripts/check_tau_13.py` | `S045-TAU13` | The coefficient `tau(13)` and its remainder modulo 13. |

The modular-coefficient helper also accepts other nonnegative integer indices. With no arguments, it prints indices 0, 13 and 91; the following command runs the two listed coefficient checks together:

```bash
python3 scripts/check_modular_coefficients.py 0 13 91
```

Other check events may record direct algebra, a targeted proof check, use of a statement as background or a refutation. Their event type and outcome should be read as recorded; the presence of these three numerical scripts does not turn those other events into computational certificates.

## Working layout and dependencies

The numerical checks and the structural validator work from the extracted bundle without the original inputs. The complete helper suite uses Python 3.10 or newer. `crop.py` additionally requires **Pillow** (`PIL`); the other supplied helpers use the Python standard library.

To use the editorial/source/crop helpers, preserve the following relative layout:

| Path relative to a common working directory | Contents |
| --- | --- |
| `work/` | This extracted bundle, including `scripts/`, `records/` and `pages/`. |
| `input/` | The original attached `SP55_CW_63.zip`, unpacked once. Its nested ZIP names already correspond to unpacked folders. |
| `input/SP55_CW_63_witnesses/page_map.tsv` | The supplied page mapping, loaded by `editorial.py`. |
| `input/SP55_CW_63_witnesses/` | The supplied witness and convention files. |
| `input/SP55_CW_63_scans/` | The supplied whole-page and half-page JPEGs. |
| `crops/` | An existing temporary output directory if `crop.py` is used. Crop images are not deliverables. |
| `output/` | ZIP output directory, created by the packaging helper when needed. |

`work` can have another name, but `input/`, `crops/` and the default `output/` are resolved relative to its parent. Input inspection is separate from numerical verification. `read_sources.py` displays the supplied witness material; it neither performs OCR nor decides readings. `crop.py` applies ordinary cropping, rotation, contrast adjustment and resampling to an image, without text recognition or generative editing.

## Report reconstruction

**Do not rerun `record_*.py` over final audited files.** Those scripts reproduce first-reading commits only. They write page files and replace the corresponding editorial records, and can therefore overwrite later audit corrections and timestamps. They are retained as documentation of the work, not as verification commands for the final frozen transcription.

In an editable working copy with the required sibling inputs, the derived reports can be regenerated from the current preserved page files and records with:

```bash
python3 scripts/editorial.py
```

This is a writing operation. It is not a new image reading, does not perform the audits, and does not freeze or certify the transcription. Preserve the authoritative audited page files and records when reconstructing reports.

## Structural validation

From the bundle root:

```bash
python3 scripts/validate_package.py .
```

The validator prints a JSON diagnostic and returns a nonzero exit status if a required structural check fails. In an unfinished working bundle, missing pages, audit entries, the freeze or final report sections are expected to fail until those steps are completed. Its checks concern filenames, page order, tables, enum values, inventory coverage, progress records, hashes and a brace-balance heuristic. They do not establish fidelity to the ink or mathematical correctness, and no TeX compilation is performed.

The validator currently has no automated correspondence check between doubts-table rows and in-place uncertainty marks, no complete whitelist of source-page macros, and no archive-footer inventory coverage test. The primary reader checked doubt scope and notation during the final image audit; mechanical review also checked the declared custom macros and all 26 footer inventory entries. Static checking is not a typeset-layout validation.

## Packaging

The packaging helper includes the current deliverables, editorial records, documentation and scripts. It excludes original inputs, witness/scan/context trees, images, PDFs, existing ZIPs, Python caches and bytecode, build artifacts and symbolic links. It does not save files to persistent storage or alter `progress.log`.

For a checkpoint, supply the next unused positive integer. For example:

```bash
python3 scripts/package_work.py --checkpoint 2
```

This example creates `../output/SP55_CW_63_checkpoint_02.zip`. Follow the requested 45-minute checkpoint schedule; packaging does not schedule checkpoints. Existing checkpoint names always cause failure and are never overwritten. A local checkpoint ZIP still needs to be saved to the authorized persistent destination.

When all readings, audits and reports are complete, create and validate the final ZIP:

```bash
python3 scripts/package_work.py --final
python3 scripts/validate_package.py . --zip ../output/SP55_CW_63.zip
```

The default final destination is `../output/SP55_CW_63.zip`. The helper refuses to overwrite an existing final ZIP unless `--final --overwrite-final` is explicitly supplied for replacement of a provisional final archive. This flag never permits checkpoint replacement. Packaging is not evidence that the pending reading or audit work has been completed; `progress.log` remains the record of that status.
