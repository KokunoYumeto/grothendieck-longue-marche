# WF-ROOT-CROP-COUNTS — proposal through scan025

Status: prepared only; no existing file was changed. Root applies after scan026 review. Prepared 2026-11-21T06:42:25.177994+00:00.

## Proposed reporting change

Replace the current workflow block's directory PNG count with a count of successfully displayed exact crop paths. The new table retains the independent A/B/C crop columns and the original Observations field, and adds Root crops shown (distinct), Root-created shown, Reader crops reused by root, and Root count evidence.

Formal audits on scans013–025 contain 293 successful distinct paths: 52 root-created and 241 reused reader crops. Each eligible row has successful_display_count equal to one; exact successful paths are unique. The stored declared totals agree with the row enumeration. The known flat-path omissions are scan017 (five root-created paths), scan023 (two), and scan024 (four); the current Main new crops cells for those pages are zero. Scan025 records 18 reused paths and zero root-created paths.

The precise path mapping is recorded in evidence.json. It uses the package README's location statement, each exact audited path, and created_by_root where that field exists. It does not inspect image files, derive views from file existence, rewrite paths, or add failed unseen attempts. A successful retry contributes the same exact path once. Scan025's one failed two-image batch remains in its original audit; the two later positive records contribute two distinct paths.

Earlier pages have no formal root_crop_audit. Their evidence is labeled as historical reports, journals or manifest enumerations. Complete successful-path lists support scans005–008 and010–012. Scans002 and004 retain their expressly reported totals. Scan003's journal and root-only manifest establish twelve root-created crops, while its complete reused/total count remains not fully recorded. No total is inferred from incidental image references. Scan009 has no current record/workflow row. Scan026 remains outside this review.

## Preservation and scope

The exact replacement affects only workflow report generation. Existing workflow_note values are still emitted unchanged, as are all brief texts and the complete workflow_assessment.md text. Earlier notes that describe a pending phase remain historical notes. All original records, pages, journals, audits and cumulative output are untouched. No new direct audit or manuscript event is created from historical evidence.

The proposed helper reads a formal root crop audit when one is present and accepts only its recognized positive-success array. It checks the scan identity, exact path owner mapping, explicit creator flags, duplicate-path identity and declared distinct total. It emits a named historical basis only for the reviewed older pages; absent evidence produces an explicit unrecorded value. Root still needs to inspect scan026's actual audit before final application; this proposal supplies no scan026 count.

## Exact source proposal and reversible patch

Target: `out/scripts/build_records.py`

Before SHA-256: `6724ab2ccd715f263f917e5b6af1c789058e13d118b009e5302cf4e032fb856a`

Proposed SHA-256: `fefa9810da89eaab4ff70a1729e83140d6bb1826ddd66b423102d0f6dc33c618`

The source replacement is one unique bounded block beginning with the workflow list and ending immediately before the Brief versions append. Its helper and historical fallback mapping are inserted within that replacement. Bytes before and after the replaced block are unchanged.

- `build_records.before.py`: exact current source snapshot.
- `build_records.proposed.py`: complete reviewable proposed source.
- `forward.patch.json` and `inverse.patch.json`: exact old/new text, expected occurrence count, and before/result whole-file hashes.
- `forward.diff` and `inverse.diff`: corresponding readable unified diffs.
- `evidence.json`: exact source identities, source excerpts, successful-path rows, classification and preserved failure records.
- `preview.md`: root-count columns through scan025, including evidence limits.
- `source_replay.json`: bounded replay and unchanged-target evidence.

The forward patch was replayed only in memory against the exact current source text, yielding the proposed bytes. The inverse recovered the original bytes exactly. Both replacement strings occur once. The actual target's bytes and hash remained unchanged. The builder and proposed source were never executed, imported or compiled. No image operation, rendering, internet, mathematical work, broad test, checkpoint action, history edit or upload occurred.
