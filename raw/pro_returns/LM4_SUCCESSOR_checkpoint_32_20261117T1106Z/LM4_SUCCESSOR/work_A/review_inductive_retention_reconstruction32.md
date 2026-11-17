# Entire-source review of the reconstructed 31-to-32 retention step

Reviewer: A/involutions. Scope: complete source read after recovery; neither helper was imported or executed by this reviewer. This record concerns new reconstruction bytes, not the lost earlier helper versions.

Reviewed in full:

- `code/preserve_checkpoint_versions_inductive.py`, SHA256 `dac20909bbce4d335e94202c002ca8286f44aaab71f316807442e8d769068d1f`.
- `code/verify_checkpoint_inductive_retention.py`, SHA256 `6a41db969ef148e36d8e3042687763112e68f04a64716d09d6d2970211d7f610`.
- `work_DE/checkpoint32_retention_parent_anchor.json`, SHA256 `77423a128a680fdb9e432e82e4473f4022ce60d4cc2ccc2ce719adeea62f236f`.
- The complete actual shared reader `code/checkpoint_archive_io.py`, SHA256 `e508fa3bae0cb845b5d02a0623aea6643a9981a7ade822fe87e7c539140e21e4`, exactly the pinned checkpoint31 reader.

## Result: PASS at the printed induction scope

The anchor explicitly identifies checkpoint31 by 526709584 bytes and SHA256 `98f1a6b74ae43dc4d09a1177a79c5e149fdf7530df52bc593964778172611d41`. The coverage of checkpoints1–30 is a declared, pinned previously verified induction base, not a purported new reread of those archives.

The producer verifies exact parent archive identity, complete logical manifest coverage (including the manifest as an independently retained logical entry), every payload byte/hash, all three standard TAR identities, and the pinned historical table, summary and reader. It checks all 123532 inherited identities and their actual parent targets, including uniqueness of logical keys, empty omission fields, per-checkpoint counts and tuple digest.

The map is total on all 9388 parent entries. Each unchanged current payload may be retained in place; each changed payload, and all three records to be rewritten, is retained at an exact historical path. Different existing bytes cause failure rather than replacement. Every target is subsequently compared byte-for-byte against its parent payload before publication. Paths are canonical relative paths and are checked against root escape. The reader rejects duplicate logical paths, overlapping containers, unexpected TAR members, forward or chained hardlinks, and unsafe parent paths; the new complete validator additionally checks canonical spelling.

The inherited map is composed literally through the total parent map, preserving checkpoint/archive/original-path/size/hash tuples. All 9388 checkpoint31 identities are appended, giving 132920 rows. The no-loss guard requires the current retention CSV, summary and history README to equal the archived31 bytes before work and again immediately before publication. Thus an unarchived current version is not silently overwritten.

Publication requires explicit `--commit`. The map is written first and the certificate last; the three mutable records are individually replaced atomically. This is not a multi-file transactional filesystem claim: an interruption can leave an incomplete publication, but the missing/mismatching final certificate and the no-blind-rerun guard make that state fail closed rather than certify it. The intended writer freeze remains an operational prerequisite against concurrent mutation.

The companion reads the immutable parent and closed child, not the current retention table. It revalidates both complete manifests and three bundle identities, the exact archived anchor, the total parent map, the inherited tuple sequence and literal composition, all appended parent identities, every closed-child retained target, and the published summary/README hashes. Thus a table-only claim cannot pass if a payload is absent or different in the actual child archive. Equal-byte storage sharing does not merge logical identity rows.

No helper execution, archive creation, retention publication, current archive verification, native TAR verification, or successful checkpoint32 capture is asserted by this source review.
