# Checkpoint 24 archive verification

**Result: PASS.** Verified 2026-11-20T09:57:00.464958+00:00.

Archive: `SP02_CW_10+12_checkpoint_24.zip` — 5128974 bytes.

SHA-256: `2ebda86fef1b6eff9b87830aaaea6ec9981167017df75e9a7929897d0346905c`.

The exact captured preparation is `evidence/checkpoint24_preparation_106.json`, completed `2026-11-20 09:53:17 UTC`. Its archived bytes match the corresponding staging evidence. All protected-file comparisons use that captured snapshot; current mutable pages, records and logs were not used.

| Check | Result |
|---|---:|
| Archive members / manifest hashes verified | 940 |
| Captured protected inputs verified | 336 |
| Captured refreshed copies verified | 181 |
| Canonical pages / records | 106 / 106 |
| Cote 10 / cote 12 pages | 84 / 22 |
| Completed / started audit sessions | 14 / 1 |
| Receipt files / immutable history files | 30 / 72 |
| Root audit support / root scripts / library helpers | 59 / 120 / 2 |
| Duplicate / unsafe / excluded members | 0 / 0 / 0 |
| Uncompressed bytes | 23813901 |

ZIP CRC passed. Every manifest member has the expected path, byte count and SHA-256. Page and record membership exactly matches the pinned 106-page canonical map. The combined transcription matches the ordered concatenation of archived page bytes and the captured preparation hash.

The captured partial audit is `B10-02_10_scan047_audit001`, status `started`, begun `2026-11-20 09:47:27 UTC`. Its two before-history files, image-first/receipt pair, and three page-scoped support JSONs are retained. Fourteen other sessions are captured as completed. This is the saved checkpoint state, not a final-readiness claim.

Required packaging, readiness, preparation, refresh, image-first and freeze helpers and their selected regression tests are included. No prohibited source/scans/witness/context directories, images, earlier archives, unsafe paths, symlink entries, special files, encrypted members, or duplicate members were found.

No semantic page/record/notes/context reading, live audit/freeze operation, archive creation or upload was performed. The accompanying JSON records every verified member hash, helper hashes, captured audit metadata, checks and issues.

Issues: none.
