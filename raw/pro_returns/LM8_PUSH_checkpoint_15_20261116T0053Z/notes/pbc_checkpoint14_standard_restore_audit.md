# Standard-row trace: exact restoration and source audit

Status: PASS for exact lossless serialization; independent of the mathematical
meaning of any relation in the trace.

The fresh standard-GAP-row search wrote the closed gzip file
`code/pbc_quotient86_standard2_trace.jsonl.gz`, 118,419,863 bytes,
SHA256 `ad217972584ff96f7572a741abb27c9020a0e061438f0b04561c57317315299c`.
The complete decoded stream has 355,295,349 bytes and 8,975,111 newline-terminated
records, SHA256
`1a2ae63a7a1a3351e86f1f71a7d491d87418d79dcbb0d8ddbf3cbaccc11499a2`.

`code/pbc_verify_standard_row_replay.py` re-executed the exact original reducer
on its retained source DAT and all 9,000 retained standard-GAP identity rows.
It compared every decoded byte against the entire original trace, not just a
prefix, hash sample or final mathematical state. The whole comparison passed
in 43.31 seconds. Its output and all hashes are retained in
`code/pbc_quotient86_standard2_replay_verification.out` and the recipe.

I separately read the restore helper and recipe for self-contained extraction:

- The helper derives the archive root from its own path. Both source DAT and
  identity-row DAT are archive-relative and hash-checked before execution.
- The reducer source and its sole local include
  `pbc_positive_collector_control.hpp` are retained and hash-checked.
- A retained executable is used only if its executable bit and full hash match.
  Otherwise the helper compiles the retained C++17 source with the explicit
  standard compiler/GMP/zlib command. No source file or mathematical input is
  fetched from outside the extracted archive.
- The output and temporary certificate paths are placed under the requested
  destination; the helper refuses to overwrite an existing target.
- The helper checks the final decoded byte count, record count and full SHA256.
  Gzip wrapper bytes may differ; the original wrapper hash and byte count remain
  explicitly retained in the recipe. Every original proof-record byte is
  reproduced exactly.

The generic transformation ledger is
`code/pbc_quotient86_standard2_replay_transform.json`, with external mirror
`checkpoint14_standard_replay/pbc_quotient86_standard2_replay_transform.json`.
It has `codec=PBC_REPLAY01`, `kind=gzip_payload`, the mandatory complete decoded
verification flag, archive-relative stored recipe, and the generic restore argv.
All required inputs already exist as ordinary retained project files, so the
additional-payload list is empty.

The initial verification wrapper had a final provenance Path/string type issue
identified before completion. That attempt was deliberately stopped; its source,
stdout and stop record were preserved. The only fix was to wrap the hash input
in `Path`, after which the entire comparison was restarted and passed. The
reducer, source rows, original trace and proof arithmetic were unchanged.
