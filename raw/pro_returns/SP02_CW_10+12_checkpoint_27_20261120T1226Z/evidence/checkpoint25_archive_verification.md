# Checkpoint 25 archive verification

**PASS.** Checked 2026-11-20T10:43:24.426060Z. The 41 bounded core archive checks passed; separate receipt, strict image-first chronology, and documented relocation checks also passed. No genuine current gate issue was found.

## Archive and captured snapshot

- Archive: `SP02_CW_10+12_checkpoint_25.zip`
- Created: 2026-11-20T10:38:40.893064+00:00; saved: 2026-11-20T10:39:58.329759+00:00
- Size: **5,557,623 bytes**; **1,039 members**; **25,649,791 uncompressed bytes**.
- SHA-256: `4d821a3dff8f82f0bfcdab5667ef8439d1feeebad5c6fe2530e3b55b0f200dc6`
- CRC and every manifest member path, size, and SHA-256: **PASS**.
- Canonical map membership: **106 page files and 106 records** (84 cote 10; 22 cote 12).
- Captured protected inputs matched: **385**; refreshed source copies matched: **210**.
- Unsafe, duplicate, special, encrypted, or excluded members: **0**. No input scans, witness/context files, or nested archives.

The captured `evidence/checkpoint25_preparation_106.json` completed at **2026-11-20 10:38:39 UTC** and matches the work preparation summary. Combined transcription is **433,769 bytes**, SHA-256 `ce914f440f567600b796b2f1cfdcf5ad5ff506bb60881e84ae353a6251f7e3ba`, exactly matching the ordered archived page bytes.

## Audit state captured

There are **21 actual sessions**: **20 completed audits for scans 033–052** and active `B10-03_10_scan053_audit001`. The archive has 21 image-first/receipt pairs and 102 history files. Identity and hash links, adjacent-session order, and strict image-observation-before-text-open-before-completion/preparation chronology passed. CHECK_EVENTS is its exact 35-byte header with zero event rows; no freeze or context-open event is present.

## Separate post-save relocation

The documented working-observations file was **not counted as a session or receipt** and its observations were not parsed. The archived original at `documentation/audit_sessions/B10-03_10_scan053_audit001_working_observations.json` equals the current destination at `documentation/audit_working_notes/B10-03_10_scan053_audit001_working_observations.json` byte for byte: **1,426 bytes**, SHA-256 `fbab633014dc486de5206d0e0fdd0027b64cafff8720b2bdd9a5657ab8d27c21`. The old live path is absent. The relocation was recorded at 2026-11-20T10:39:58.337424+00:00, after upload; its two paths are safe and have no symlink components.

**Restore requirement:** checkpoint 25 remains immutable and retains the original working-note path. Apply the documented byte-preserving relocation before continuing audit bookkeeping from that archive. The live tree already has that relocation. The post-save receipt and relocation metadata correctly were not part of the earlier archive.

## Preservation and limits

All named archive/manifest/preparation/receipt/relocation inputs remained unchanged during verification. Captured page and record checks used the archive and staging metadata, not later mutable live audit state. Only this Markdown file and its companion JSON were written. No scans, image headers, witness or context content, semantic observations, live audit events, freeze, archive changes, or uploads were involved.
