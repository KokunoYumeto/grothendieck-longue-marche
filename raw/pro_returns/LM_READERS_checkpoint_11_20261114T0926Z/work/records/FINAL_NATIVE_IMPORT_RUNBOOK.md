# Final native evidence import

`finalize_native_closure.py` installs completed native review evidence in `work/data/final_visual_issue_closure.json`. It does not inspect images visually or create observations. Its default operation checks the evidence and writes a proposed ledger; only an explicit `--commit` changes the central ledger.

## Prerequisites

Run this workflow after all seven publications are stable, their ordinary verification has completed, and the additive finding inventory and final repair records are installed.

The five primary books must each have a current queue under `work/data/final_native_closure_queues/`, a complete supplied observation file, and a complete validated file under `work/data/final_native_closure_validated/`. Validation must report `VALIDATED_OBSERVATIONS`, zero issues, and exactly one resolved observation for every finding that affects that book. Partial files and an unresolved `ISSUE` are rejected. New finding IDs remain pending until they receive the required evidence.

The source queues and observations are prepared, carried where eligible, reviewed, and validated through the commands in `CARRYOVER_AUDIT_RUNBOOK.md`. Every previously cited image must match for a historical native observation to carry; equal pixels alone do not suffice. Historical observations retain their original reviewer, text, page context and frozen provenance.

Both current all-page comparison reports must exist:

```sh
python -B work/scripts/compare_pdf_pixels.py work/build/LM_FR_corrige_apparat.pdf work/build/LM_FR_master_annotated.pdf --output work/verification/FR_MASTER_PIXEL_IDENTITY.json
python -B work/scripts/compare_pdf_pixels.py work/build/LM_EN_corrected_apparatus.pdf work/build/LM_EN_master_annotated.pdf --output work/verification/EN_MASTER_PIXEL_IDENTITY.json
```

These commands compare all corresponding pages at 900 pixels wide and record both PNG-file and decoded RGB identity. A difference is permitted only on the title page. An existing comparison can be used only when it already has the exact current PDF hashes and complete PNG and RGB fields; otherwise rerun it. Selected-page review transfer is a separate operation and is not performed by these two commands.

## Check the proposed import

```sh
python -B work/scripts/finalize_native_closure.py --check
```

The command writes:

- `work/data/native_closure_import_check.json`: the current check result, counts and complete pinned input manifest.
- `work/data/native_closure_import_proposal.json`: a proposed central ledger, explicitly marked `PROPOSED_NOT_COMMITTED`.
- Content-addressed master evidence PNGs under `work/visual_repair_proofs/native_master_identity/`, produced by actual rerendering at each cited page, crop and scale.

Successful checking reports `READY_TO_COMMIT` and `CHECK_ONLY`. This does not approve publication and does not change the central ledger.

The importer independently reconstructs every current source anchor and inspection requirement. It checks the actual common-body hash, edition form, language, scan map, source-mark identities, raw source hashes, repair IDs, exact queue scope and queue hash. It also reconstructs each validated row from its pinned supplied observation and the registered current images. Every cited primary PNG is rerendered from the current PDF and must match both encoded PNG bytes and decoded RGB pixels. Any historical carry is checked recursively against its frozen queue, validated record, images and unchanged per-finding identity.

For each master, the corresponding apparatus edition must have the same common body, form, language and source-page identities. The all-page comparison must name the exact current PDFs. In addition, every cited apparatus native crop and full image is rerendered from the master at the identical page, clip and scale. Both PNG bytes and decoded RGB must match. The confirmation preserves the exact apparatus reviewer and observation, labels its basis as image-identity transfer, and explicitly states that no new master visual inspection was performed.

All original finding fields are retained unchanged except `status` and `publication_confirmations`. This includes original definitions, candidate references, repair IDs, normalized detected evidence, and any verbatim `original_detected_in` list. The affected book set must be covered exactly once for every finding.

## Commit the complete import

After checking the proposal and report, run:

```sh
python -B work/scripts/finalize_native_closure.py --commit
```

This reruns the checks; it does not trust a previously written proposal. Under an exclusive ledger lock it rechecks every pinned input, confirms that the central ledger still has its original bytes, and creates an exclusive exact-byte backup:

```text
work/data/native_closure_ledger_backups/<prior-ledger-SHA256>.json
```

An existing backup is never overwritten. A deliberately chosen new relative backup path can be supplied with `--backup`; it must be distinct from every input and output. The complete ledger is replaced atomically only after all checks succeed. The check report then records `PASS`, `COMMITTED`, the new ledger SHA256 and the backup path/hash.

If a check fails, the command exits nonzero, reports `FAIL` and publication approval `PENDING`, and does not install partial confirmations. The original central ledger remains unchanged. A prior ledger that was already marked `PASS` is not sufficient evidence for a later publication: the release gate must require the current successful `COMMITTED` importer report, its exact current ledger hash, and unchanged pinned current inputs. A crash between atomic replacement and the final report leaves a check-only report, so the release gate still remains pending.

## Synthetic controls

```sh
python -B work/scripts/check_finalize_native_closure.py
```

The controls use temporary synthetic PDFs, sources, queues and observations. They never read or alter a publication PDF or publication observation. Results are written to `work/data/finalize_native_closure_controls.json`, with hashes of the importer and control script. They cover complete import and preservation, recursive exact-image carry, incomplete or duplicate observations, unresolved issues, stale source and repair identities, altered observation text, equal RGB with different PNG bytes, master form and native-image mismatches, exclusive backups, and input changes immediately before commit.
