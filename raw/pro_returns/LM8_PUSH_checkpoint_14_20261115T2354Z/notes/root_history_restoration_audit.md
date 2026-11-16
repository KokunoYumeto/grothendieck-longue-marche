# Executed historical restoration verification

The complete materialization through checkpoint 11 checked all 8,391 actual historical ZIP entry hashes and CRCs, plus every archive hash. It created 1,761 exact distinct content objects and verified 169 current-file restoration dependencies. Three obsolete numerical encodings are individually superseded by completely verified exact decoded payloads or prefixes; every other historical entry is byte-exact.

Two actual complete historical tree restorations were then executed in new scratch directories outside the deliverable tree:

- Checkpoint 09: 1,469 exact historical entries copied and hashed, plus its boundary log and historical v5-prefix log reconstructed at their original source paths with complete decoded SHA-256 checks. Both superseded encoding files are individually recorded in the restoration accounting. Output: `notes/history_restore_checkpoint09_test.out`.
- Checkpoint 11: all 1,657 actual historical archive entries copied and hashed exactly. Output: `notes/history_restore_checkpoint11_test.out`.

Both completed successfully. No checkpoint ZIP was created, modified or uploaded by these restoration tests. The generated test trees are reproducible verification intermediates; the retained history objects, index, scripts and output ledgers suffice to reproduce them. The outer archive's exact-copy aliases are independently checked by the checkpoint archive verifier after capture.

## Extension through checkpoint 12

The history was subsequently extended through the actual successfully saved checkpoint 12. The new materialization verifies 10,759 historical entries, 2,039 distinct content objects, and 169 exact restoration dependencies. The same three superseded numerical encodings retain their explicitly checked mathematical payloads; no new historical omission was introduced.

An actual complete checkpoint-12 tree restoration was executed into a new scratch directory. All 2,368 historical archive entries were restored and hashed byte for byte against the archive with SHA-256 `447503322b6e3d00279d4ecddd4fe6f6e8c25e32ee78d7691c781d55214d9e6e`. The successful output is `notes/history_restore_checkpoint12_test.out`. The old ZIP wrapper was not recreated or modified. This test extends the previous checkpoint-09 and checkpoint-11 restorations, with every historical entry accounted for.
