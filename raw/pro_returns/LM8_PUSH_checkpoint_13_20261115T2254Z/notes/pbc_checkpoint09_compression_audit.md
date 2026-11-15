# Checkpoint09 compression and exact payload reconstruction audit

Auditor: `/root/pbc_groups`, 2026-11-15 19:07UTC.

## Verdict and scope

**PASS for exact preservation of the mathematical proof-log content.** Checkpoint09's mathematics, source files, result statuses, and incomplete C31 calculation are unchanged. The immutable original archive is `LM8_PUSH_checkpoint_09.zip`, created from captured bytes at2026-11-15T18:55:35.266296+00:00. It remains untouched. The compact derivative may supersede compression-wrapper bytes and redundant encodings, with the original wrapper hashes retained. It must not describe C31 as proved.

Every original JSONL payload can be retained losslessly with XZ. Valid gzip logs must be decompressed BEFORE XZ encoding; compressing the gzip wrapper preserves avoidable redundancy. The two large redundant native payloads may alternatively be represented by the exact reconstruction rules below. These rules have now been checked AGAINST THE IMMUTABLE ORIGINAL09 ZIP itself, not against the subsequently growing live v5 log.

## Interrupted native streams

For each of native versions1,3,4, I streamed every raw `.incomplete_stream` byte through zlib, without an output-size cap, and flushed the decoder. Its entire decoded output is exactly the concatenation of the retained valid gzip's complete-record payload and its separately retained `.partial_record`. There are zero unused or unconsumed input bytes. No complete record or decoded trailing text is omitted. The incomplete compression-wrapper bits are a superseded serialization; their exact original hashes remain in the existing `.archive.json` manifests.

| Stream | Original interrupted wrapper bytes | Complete decoded record bytes | Trailing partial decoded bytes |
|---|---:|---:|---:|
| native v1 |369098752|978110408|33|
| native v4 |28311552|76192487|48|
| native v3 |0|0|0|

The complete decoded work (including the trailing partial record) has SHA256:

- v1: `138b414059230e82d194ef412df277b449453b0610095dd0c84e7272c61ec690`.
- v4: `6b9f778a0efd75d9b211ca24b46c49ea4f02d29827cafad0ff1ffce157c65887`.
- v3: the SHA256 of the empty string, `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

Full report: `code/pbc_interrupted_stream_payload_equivalence.json`. Original wrapper hashes and the smaller partial-record hashes remain in the three original archive manifests. Removing the interrupted wrappers from the compact derivative therefore removes no mathematical work content. It does not claim to make the exact original compressed byte sequences recoverable from plaintext.

## Exact native-v1 prefix reconstruction

The immutable09 entry `code/pbc_iterated_modular_boundary_trace.jsonl` has1234834123 bytes and SHA256
`53ebf2c3c193e971f6b4ee9cef86f7ee1c9a85abf0a555db8085b8e9b673bb1b`.

Read its first16749555 records and remove ASCII space bytes from each record. The resulting bytes are EXACTLY the full decoded payload of `code/pbc_native_modular_iterated_trace.jsonl.gz`:

- complete records:16749555;
- decoded bytes:978110408;
- decoded SHA256: `291d3ba1f5b3ea1da57d4257386f4de25384721b04338ff4bf10bf7bda5980fa`.

The retained33-byte partial record is exactly the beginning of the next transformed source record. The original valid gzip wrapper was369101049 bytes with SHA256
`a52ad0ede0b48ed15f0337b753acb4fecf4c332e43538ba30d5a4782c35f993a`.
Thus BOTH that redundant gzip wrapper and its interrupted precursor may be superseded by the retained boundary JSONL payload, this exact prefix rule, the original wrapper manifests, and the tiny partial record. The full16749555-record equality was checked from the immutable09 ZIP.

## Exact native-v4 prefix reconstruction

The immutable09 entry `code/pbc_native_modular_v5_iterated_trace.jsonl.gz` was closed with a valid footer before capture. It has108803164 bytes and SHA256
`d6f6603fc702b8276587092e29539f6af9b2e75690168fe3b63bcb96f8a7deda`.
Use THIS frozen entry or its lossless XZ-decoded JSONL payload, not a later live v5 file.

Its first959651 decoded records are EXACTLY the full decoded payload of `code/pbc_native_modular_v4_iterated_trace.jsonl.gz`:

- complete records:959651;
- decoded bytes:76192487;
- decoded SHA256: `0acf3436e6ed2067c89c7655c66ab2d57328780358c20d4ba38569ff5e1479a7`.

The retained48-byte partial record is exactly the beginning of the next source record. The original valid v4 gzip wrapper was28310891 bytes with SHA256
`402e85ec7c098ecd27a6dbcaba1b2774e5f370fb55d1a3dae463a132065421f5`.
The full959651-record equality was checked from the immutable09 ZIP. Version3 has an empty payload and requires only its existing empty-work manifest.

## Reproduction files

- `code/pbc_checkpoint09_immutable_prefix_audit.json`: exact frozen ZIP entry hashes, record counts, and completed equality checks; explicitly records that no live source was read.
- `code/pbc_compact_trace_reconstruction.json`: machine-readable prefix transformations, payload hashes, original wrapper hashes, and the exact partial records in hexadecimal.
- `code/pbc_trace_reconstruction.py`: reconstructs either redundant payload from the retained source JSONL, gzip, or XZ file, checking all output bytes and the partial record. A fresh valid gzip wrapper may be requested, but no identity of wrapper bytes is claimed.
- `code/pbc_verify_pack_payloads.py`: repeats the interrupted-stream decoding and payload-prefix comparisons on a complete frozen extraction containing the original streams.
- `code/pbc_native_boundary_payload_prefix.json`, `code/pbc_native_v4_v5_payload_prefix.json`, and `code/pbc_interrupted_stream_payload_equivalence.json`: earlier complete comparison reports, now bound to the immutable snapshot by the new ZIP audit.

Example reconstruction after extracting the compact derivative (substitute the repacker's exact retained XZ pathname):

```sh
python code/pbc_trace_reconstruction.py code/pbc_compact_trace_reconstruction.json native_v1 code/pbc_iterated_modular_boundary_trace.jsonl.xz restored_native_v1.jsonl --partial-output restored_native_v1.partial_record
python code/pbc_trace_reconstruction.py code/pbc_compact_trace_reconstruction.json native_v4 code/pbc_native_modular_v5_iterated_trace.jsonl.xz restored_native_v4.jsonl --partial-output restored_native_v4.partial_record
```

The original frozen archive and all workspace originals remain available. The compact package is a lossless content representation with documented serialization changes, not a deletion of unsuccessful work or an alteration of mathematical status.

## Exact binary serialization after XZ alone exceeded the upload limit

The first XZ conversion and exact native-v1/v4 prefix deduplication still
produced a698,507,600-byte archive. A further reversible serialization
transform was therefore applied to the eight distinct large proof payloads.
It is called `PBCBIN01` and is implemented in
`code/pbc_trace_binary_codec.cpp`, with an independent portable decoder in
`code/pbc_trace_binary_decode.py`.

Canonical `sub`, `mul`, and `neg` operation records are stored by opcode,
output-ID increment, reference distance or ID, and an arbitrary-precision
integer magnitude. The coefficient may be stored as its exact signed
difference from zero, N, or minus N, with the choice explicitly tagged.
The modulus N is stored in the binary header. Every noncanonical or other
record, including all source and leaf records, is stored verbatim with its
length. Original whitespace and newlines are therefore reconstructed exactly;
no equation, coefficient, leaf, unsuccessful operation, or partial record is
discarded. Balanced-coefficient encoding is an invertible storage transform,
not reduction of a proof coefficient modulo N.

The compiled encoder and decoder processed every byte of each payload taken
directly from the immutable original09 ZIP. Each encoded XZ stream was then
decoded in full, and its byte count and SHA256 were compared to the original
decoded input. All eight comparisons passed. The frozen v5 input was used,
not the live continuation. Three initial samples also round-tripped exactly,
and the portable Python decoder independently restored a native sample.
Root independently audited the codec and decoded the entire40,968,905-byte
basic modular trace using the portable implementation; its original SHA256
matched. The Python decoder has unrestricted integer conversion and exactly
matches the encoder's unsigned64-bit raw-leaf ID check.

| Distinct original payload | Verified binary XZ bytes |
|---|---:|
| boundary |190738772|
| frozen native v5 |54249840|
| torsion |32145444|
| precollected |68033020|
| coordinates |5451192|
| scan |9030968|
| unit |7808060|
| basic modular |4744564|
| **Total** |**372201860**|

Exact individual hashes, decoded sizes, encoder/decoder record counts, and
whole-stream verification flags are in the frozen conversion manifest
`checkpoint09_binary/binary_conversion_manifest.json` and its individual
ledgers, copied by the final archive assembler into its compression mapping.
The executable provenance is `code/pbc_binary_codec_provenance.json`:
g++14.2.0, command
`g++ -std=c++17 -O3 LM8_PUSH/code/pbc_trace_binary_codec.cpp -lgmpxx -lgmp -o LM8_PUSH/code/pbc_trace_binary_codec`,
executable SHA256
`92da634c80253371fe186ab62471b1d1e0a11ae0c4d64cfb0e80ea155cac0263`.
The source SHA256 is
`70be54bff096e85fc11ca2ea647b55473886bb431212ddaaebe8c005d9076908`.
The exact-conversion driver is `code/pbc_binary_checkpoint09.py`.

After binary decoding restores the boundary and frozen-v5 payloads, the
previously verified prefix rules reconstruct native v1 and v4 exactly as
before. All complete and partial mathematical records remain available.
The original oversized archive, first XZ candidate, and prefix-deduplicated
candidate remain unchanged locally and are explicitly superseded containers.
The mathematical snapshot and the OPEN status of C31 are unchanged.
