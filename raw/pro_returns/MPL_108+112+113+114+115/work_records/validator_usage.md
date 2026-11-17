# Mechanical packet validation

`validate_packet.py` checks file counts, filename order, page/cote markers,
balanced unescaped TeX braces (with comments ignored), the inventory columns
and allowed values, coverage of every scan, exact concatenation, and optional
SHA-256 immutability. It does not assess manuscript readings or completeness.

Run from any directory:

```bash
python /workspace/scratch/cb96d9ba0f27/deliverable/work_records/validate_packet.py
```

The combined fragment is expected to equal `b"".join(page_bytes)` in the
prescribed cote/scan order; do not add separators beyond those already present
in the individual page files.

Recommended frozen manifest: `work_records/frozen_sha256.json`, with one JSON
object mapping the forty root-relative `pages/...tex` paths and the combined
fragment filename to their SHA-256 digests. The validator also accepts
sha256sum format and an explicit `--hashes PATH`.

Exit code zero means the structural checks passed. A missing frozen manifest
is reported as a warning, because before freezing there is no immutability
claim to test. All checks are read-only.

The utility was self-checked on a temporary fabricated forty-page fixture.
The valid fixture passed; unmatched braces, changed concatenation and changed
frozen bytes were detected. No actual transcription or manuscript was read
for this infrastructure work.
