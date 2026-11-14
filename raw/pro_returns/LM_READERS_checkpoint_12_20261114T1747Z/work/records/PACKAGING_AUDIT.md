# Packaging audit before the final rebuild

This is an independent, read-only audit of `work/scripts/package_release.py` and `work/scripts/restore_image_aliases.py` on 13 November 2026. It records the state immediately before verification of the final frozen-source rebuild. It does not certify the final PDF bytes or replace the release gates. No packaging or source file was modified during this audit.

## Findings

No blocking packaging, retention, alias-recovery, or actual privacy defect was found in the inspected snapshot. A subsequent publication-scope decision limits the final archives to exactly the seven complete edition PDFs. All development probe PDFs, including the curated source-local proof PDFs, are excluded as separate final deliverables; associated PNG evidence, TeX, logs, hash provenance and checkpoint history remain available.

The initial proposed archive maps resolved all 3,688 inputs: 11 entries in the French archive, 9 in the English archive, and 3,668 in the records archive before final deduplication and the additional generated inventories. All input files existed. At that time, every one of the 150 `probe_pdf`, `probe_image`, and `before_image` references in the then-50-row `VISUAL_REPAIRS.tsv` resolved to its proposed archive path. The proof PDF fields now identify historical verification artifacts rather than separate final publication PDFs; `work/data/development_pdf_exclusions.json` maps every excluded PDF path to its final full-book replacement and retained image evidence. The final row and archive counts are intentionally determined after the frozen rebuild.

The supplementary audit in `DEVELOPMENT_PDF_AUDIT.tsv` and `work/data/development_pdf_audit.json` checked all 104 formerly mapped non-publication PDF paths: 61 unique byte hashes, 510 pages, including 43 curated copies. Every file had a corresponding byte-matched compile log. There were zero compile errors, overfull boxes greater than 2pt, missing glyphs, off-sheet marks or type-area violations. The exclusion decision was therefore not based on a numerical failure. It prevents development extracts from being mistaken for complete editions whose entire current publication context has been reviewed.

The packager hashes the exact byte string passed to the ZIP writer, then reopens each archive, checks its CRCs, and independently verifies every inventory length and SHA-256. Successful checkpoints are opened exclusively and are not overwritten. ZIP entry paths beginning with `/` or containing a `..` path component are rejected. Checkpoint-specific manifests remain container inventories rather than being treated as edition source files.

## Exact-image aliases

A dry run of the current image-deduplication logic produced 2,585 stored PNGs and 139 duplicate aliases, saving 6,454,534 bytes before compression. Every alias pointed directly to an image retained in the proposed archive. There were no alias chains, absolute paths, or parent-directory components.

The restoration script verifies the stored file's byte length and SHA-256 before copying it. It accepts an already-existing alias only if its bytes are identical and refuses to overwrite conflicting content. The aliases therefore preserve exact bytes, including the PNG hashes used by the visual-review inventories. The final master renders will change these provisional counts and require a fresh inventory.

## Checkpoint retention

The read-only retention dry run yielded the following dispositions:

| Checkpoint | Preserved exactly | Superseded explicitly | Omitted |
| --- | ---: | ---: | ---: |
| `LM_READERS_checkpoint_01.zip` | 26 | 18 | 0 |
| `LM_READERS_checkpoint_02.zip` | 928 | 74 | 1 |

In that initial dry run, the sole omission was checkpoint 02's `MANIFEST.tsv`, whose replacement is each final archive's own manifest. Every other checkpoint file was either retained by exact content hash or mapped to an explicitly identified final replacement. Prior versions remain recoverable from their immutable checkpoint archives. This check used the initial maps in memory and did not write the release retention inventory. The final retention inventory additionally records the publication-scope exclusion of development PDFs, using the explicit replacement map in `work/data/development_pdf_exclusions.json`. That map initially covered 104 paths and has since been extended to preserve newly created probe artifacts and their replacement targets; `work/data/development_pdf_exclusions_refresh.json` records the current path count. The original numerical audit remains scoped to its original 104 byte-qualified path instances.

## Privacy evidence and scope

The packager's text-file checks found no local-path or email match in the inspected proposed archives. At the time of this initial audit, its direct PDF check covered extracted text and document metadata. The release workflow has since been strengthened: the strict report requires the expanded privacy audit to cover all seven current main PDF hashes, and the final packager requires matching current hashes for every mapped PDF. That expanded check is reproducible with `work/scripts/audit_pdf_privacy.py` and writes `work/data/pdf_privacy_audit.json`.

An additional independent check examined all 111 proposed PDF files, containing 9,386 pages and 232,582 non-stream PDF objects. This included annotation and action dictionaries. Its path patterns also covered the `mnt` and `Users` roots and both slash forms of common Windows paths. No local-path or email match was found. No PDF contained an embedded file. This independent check does not claim to interpret arbitrary binary font or image streams; the actual annotation/action dictionaries and attachment inventory contained no contrary evidence.

The final PDFs must be checked again after the final rebuild. The expanded script additionally decodes literal and hex PDF strings, checks XML metadata and percent-encoded URIs, and freezes all file hashes before and after its complete read pass. The final packager requires that expanded report rather than relying solely on its direct metadata/text scan. Arbitrary binary font and image streams remain outside the expressly stated scope.

## Operational limitations

`ARCHIVE_MANIFESTS.json` is written after the three final ZIPs and is excluded from their payloads. It can serve as an external delivery inventory. Each ZIP still contains its complete per-entry `MANIFEST.tsv`; an archive cannot contain a non-circular hash of its own final bytes.

The three final ZIPs are created sequentially. If a later archive fails, an earlier successful ZIP remains intact and a rerun refuses to overwrite it. This protects completed output, but recovery from a partial final packaging run requires the operator to identify those completed artifacts before retrying. It is not a content-integrity failure.

The visual gate establishes that required current page images have attributed observations and matching image hashes. Resolution of an observed defect remains a separate editorial responsibility: a row marked reviewed is evidence of inspection, not by itself proof that a reported collision was repaired. The pending final changed-page reviews and repair-ledger reconciliation must therefore precede release.

## Final actions still required

Run the final all-page PDF measurements and link checks on the frozen rebuild; inspect changed selected pages; compare every master page against its apparatus counterpart; retain transferred review only for exact current image identity; reconcile the visual finding records; regenerate the strict release report; and package only after its current PDF and TeX hashes pass. Re-run the privacy and retention checks on the final proposed archive maps. The provisional counts above must not be substituted for those final measurements.
