# Package publication hardening

Completed: 2026-11-20 02:25:47 UTC

## Result

Fixed `PACKAGE-PARTIAL-NAME` in `scripts/package_output.py`. All four focused synthetic tests passed. No live archive was created by this task.

The helper now prepares an exclusive temporary ZIP in the destination directory, closes and flushes/fsyncs it, validates its CRC, and calculates its size and hash before publishing the final name with `os.link`. An existing final name is never replaced. A race in which another writer publishes first raises `FileExistsError` while preserving that writer's bytes.

Only the uniquely named, tool-owned temporary file is cleaned up. If the process is killed or cleanup fails, that temporary name may remain without reserving the final archive name. Once publication succeeds, a temporary cleanup failure is reported through the optional `temporary_cleanup_warning` field without misreporting the valid committed archive as a packaging failure. Existing CLI arguments, exclusions, manifest fields, naming and dry-run behavior are retained.

## Focused validation

Command: `PYTHONDONTWRITEBYTECODE=1 python /workspace/scratch/57a811ad3c84/SP02_CW_10+12/scripts/tests/test_package_publication.py`

Working directory: `/workspace/scratch/57a811ad3c84/work`

| Failure path | Result |
|---|---|
| Interrupted entry write leaves final name absent; unpatched retry succeeds | PASS |
| Existing archive remains byte-identical after refusal | PASS |
| CRC failure leaves final name absent | PASS |
| Another writer publishes during preparation; its bytes remain intact | PASS |

The four tests used isolated `TemporaryDirectory` fixtures containing dummy text and ZIPs. No broad test suite, live package, audit, freeze, compilation, image access, witness/context inspection or transcription operation ran.

## Files and hashes

| File | SHA-256 |
|---|---|
| `scripts/package_output.py` | `d149d5ac4da5f45c430dcfb85ec041285f9862779ed9e7cc4b15543121a01ea8` |
| `scripts/tests/test_package_publication.py` | `e3c90f69ef72cd635d529d575f764ae186d5c6850fc4ce42d83b256b173a7861` |

The existing checkpoint 14 archive remained 2,608,261 bytes with SHA-256 `46d22155081fbd6bc4b52f65f0bcd25c40c82c5001218f541ec1112e2aa25f88`. It was read only as raw bytes for hashing; its entries were not opened. No page, record, progress log or CHECK_EVENTS file was accessed or changed by this fix.

Evidence files: `evidence/package_publication_fix.json` and this Markdown report. Shared README and preflight reports were not edited.
