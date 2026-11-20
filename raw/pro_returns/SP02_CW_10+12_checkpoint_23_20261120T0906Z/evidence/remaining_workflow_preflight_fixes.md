# Remaining-workflow preflight fixes

Completed 2026-11-20 02:29:02 UTC.

All five authorized defects are fixed. Seventeen focused synthetic tests passed (9 audit metadata, 4 verification logging, 4 archive publication). The older full suites were not rerun.

| Finding | Implemented change |
|---|---|
| `AUDIT-UNKNOWN-FIELDS` | Reject unknown top-level audit payload keys in the shared revision path. First-pass-only notation_updates/inventory_overrides cannot be silently ignored. Optional key/folder/cote/scan assertions must agree; observations remains extensible. |
| `AUDIT-INVENTORY-IDS` | Shared metadata validation requires nonempty unique final inventory element IDs after all operations. Explicit noncolliding renames remain supported. |
| `AUDIT-CROP-REFERENCES` | Shared pure metadata resolver validates every change crop reference. Exact complete IDs take precedence; multiple groups and literal-plus IDs are supported. Established whole/both halves aliases remain accepted without image access. |
| `VERIFY-WRITE-STATUS` | Observe verification log bytes around append attempts and retain actual written status on failure, separately from hash-verification outcome and failure detail. |
| `PACKAGE-PARTIAL-NAME` | Build, close/fsync and CRC-check a uniquely named same-directory temporary ZIP before exclusive hard-link publication. Failed preparation cannot occupy the immutable final archive name; competing/existing archives are preserved. |

## Tests and protection

The audit regressions exercise preview/final rejection parity and preservation of the temporary output bytes; they also establish compatibility for noncolliding inventory renames, exact IDs containing `+`, grouped references and the existing whole-image aliases. Verification regressions distinguish hash success/failure from append/fsync failures. Packaging regressions cover interrupted writes and retry, existing/competing archives, and CRC refusal. All fixture operations use explicit temporary paths.

Compared 153 protected files with the saved pre-fix baseline. Changed paths: []. Critical page/record/archive/CHECK_EVENTS changes: []. Checkpoint14 unchanged: True.

Root reports scan128 finalized at 02:24:35 UTC and checkpoint14 upload/manifest/progress updates. Any listed progress-only difference belongs to that explicitly reported concurrent root activity; helper tests use temporary logs only.

## Changed files

| File | SHA-256 |
|---|---|
| `scripts/record_audit.py` | `60c5eba180982c607039f547e4b3b2414a5c6b06255f47584773337db6f14760` |
| `scripts/record_page.py` | `ba5e962b8102702843b2a5228c0457bf0411c8e6e76149633b6c7e7a3f4a4a37` |
| `scripts/freeze_transcription.py` | `5d52d1431f1ba0d9d13f3ce34e2c5ab31b7d4ce18a901fcf58ee8e0c6f6caed5` |
| `scripts/package_output.py` | `d149d5ac4da5f45c430dcfb85ec041285f9862779ed9e7cc4b15543121a01ea8` |
| `scripts/README_tools.md` | `3a46b18ab605b9854b0771e31aa76ddae18a06c7b49c106682a566d6d756c714` |
| `scripts/tests/test_audit_metadata_preflight.py` | `82a4c38f3f8e837449d82e27057fbc32511ee295f0beed0ac0f474c34771d992` |
| `scripts/tests/test_verify_write_status.py` | `f6e9bdcf5e2f83d788dbf7b5c4579c48a03f5800e7b52d0be2e8a6df776ec151` |
| `scripts/tests/test_package_publication.py` | `e3c90f69ef72cd635d529d575f764ae186d5c6850fc4ce42d83b256b173a7861` |

## Remaining root responsibilities

- Root must complete and explicitly document cross-page notation reconciliation; no new automatic semantic/completion gate was added.
- Final packaging still checks archive integrity, not the final notes/CHECK_EVENTS/schema/completion contract. Root must check those deliverables and run the required final hash verification before final packaging.

## Evidence and limits

Detailed verification/package test evidence remains in `verify_write_status_fix.json/.md` and `package_publication_fix.json/.md`; all initial preflight reports are preserved. The companion JSON includes exact commands, code locations and all protected hashes.

Five authorized helper defects only; code and isolated synthetic fixture checks. No live audit/freeze, images, witness prose, context, source edit replay or transcription decisions. Checkpoint14 was already created before these changes and was not rebuilt.

These fixes, regression files and their evidence postdate immutable checkpoint14 and will be included by a later checkpoint/final package. No archive was recreated.
