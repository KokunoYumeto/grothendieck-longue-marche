# Checkpoint09 upload-limit recovery

The scheduled19:00UTC snapshot was captured once, packaged as the original
LM8_PUSH_checkpoint_09.zip, and passed the full ZIP CRC check. Its1,676,331,231
bytes exceeded the536,870,912-byte upload limit, so that upload was rejected.
The original archive remains unchanged. This compact package is a repackaging
of that SAME frozen snapshot; it is not a later or additional research checkpoint.

The392-page PDF,241-statement register, source files, proofs, audits, code,
and ordinary records are byte-for-byte unchanged. Large raw JSONL files are
stored as XZ streams; their exact original bytes were hashed, compressed,
decompressed again, and verified. Large gzip proof logs are stored as XZ of
their exact decoded contents, also fully verified. Compression wrappers are
serialization only: recreating a gzip stream preserves every proof record but
need not preserve its old gzip header or deflate bytes. Original hashes remain
recorded. Interrupted large gzip wrappers are superseded by their valid complete
record payload and separately retained partial record; the mapping lists both.
No complete or partial mathematical computation record is discarded.

CHECKPOINT_COMPRESSION_MAP.json lists every conversion and superseded wrapper,
with original and decoded hashes. ORIGINAL_PACKAGE_MANIFEST.json describes
the original frozen snapshot. PACKAGE_MANIFEST.json describes this actual
compact archive. RESTORE_LARGE_LOGS.py restores each compressed log at its
original path, verifies its decoded hash, and refuses to overwrite existing files.
All computations marked incomplete remain incomplete.

The failed oversized container is superseded by this compact checkpoint for
future checkpoint_history. The work inside it is retained here as specified
above; retaining redundant compression-wrapper bytes would exceed the upload
limit without preserving additional proof content. This is the explicit
accounting for that omitted intermediate container and its serialization files.

## Exact prefix deduplication in the saved compact checkpoint

Two redundant XZ payloads are represented by fully checked prefix rules instead
of duplicate bytes. The native-v1 complete log is the first16,749,555 records
of the retained boundary JSONL after ASCII-space removal; its33-byte partial
record remains separate. The native-v4 complete log is the first959,651 records
of the frozen native-v5 payload; its48-byte partial record remains separate.
Every complete and partial byte was compared directly against the immutable
original checkpoint09, and the reconstruction checks exact decoded SHA256.
The original gzip-wrapper hashes remain recorded. The saved archive includes
the executable reconstruction program and every independent equality audit.
RESTORE_LARGE_LOGS.py restores these two logs automatically after restoring
the distinct compressed payloads. The exact stored v5 input path is
code/pbc_native_modular_v5_iterated_trace.jsonl.gz.payload.xz.
This removes duplicate serialization only, with no omitted mathematical record.

## Reversible proof-record encoding used for the saved archive

Generic compression and exact prefix deduplication still produced698,507,600
bytes, above the536,870,912-byte upload limit. The eight distinct large proof
logs therefore use the documented PBCBIN01 reversible binary serialization,
followed by XZ. Sequential identifiers, references and arbitrary-size integer
coefficients are encoded compactly. Every unmatched or noncanonical record is
retained verbatim. This changes storage only, not any mathematical record.

Every complete decoded log was hashed directly from the immutable original
checkpoint09, encoded, decoded again in full, and checked for equal byte count
and SHA256. The portable Python decoder was independently run against one
entire log and likewise matched its original hash. Its code, the C++ codec,
the compiler/executable provenance, all per-file ledgers and the independent
verification result are included. RESTORE_LARGE_LOGS.py restores the original
paths, including the two exactly reconstructed duplicate prefixes. All partial
records remain separate. Regenerated gzip wrappers may differ from the old
serialization, as already explicitly accounted for above.

The earlier unreleased compact candidates and the oversized original container
are superseded by this exact representation of the same18:55:35UTC frozen
snapshot. The392-page PDF and241-statement register remain unchanged. Only
recovery programs, audits and this accounting were added after the capture.
The failed candidates are not additional hourly research checkpoints.
