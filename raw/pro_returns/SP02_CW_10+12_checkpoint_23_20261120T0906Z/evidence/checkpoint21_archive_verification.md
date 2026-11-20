# Checkpoint 21 archive verification

**PASS** — 2026-11-20 07:38:08 UTC

- Archive: `checkpoints/SP02_CW_10+12_checkpoint_21.zip`
- Created: `2026-11-20T07:35:08.459251+00:00`; due: `2026-11-20T07:35:07+00:00`.
- **4,082,926 bytes; 646 entries**.
- SHA256: `a7fff2bed88531bbf077c1d5fb09a8150a70322c1c799e15b20175871315d472`.
- CRC and all **646** member sizes/hashes match the manifest.
- All **202** staged protected files and **3** provisional files match archived bytes.
- The archive contains the exact latest staging evidence, `checkpoint21_preparation_098_provisional123.json`, completed at **2026-11-20 07:35:01 UTC**. All four associated staging evidence files are present.
- Exactly **98 pages and 98 records**, matching the map prefix through `B12-02_12_scan121`; identities and page hashes match.
- Combined transcription is the exact ordered concatenation: **406,060 bytes**, SHA256 `010cb6e9cc948f14da57569a1b6399ff165adf4f298a3cff5094f8d8e05cf67f`.
- Provisional crop snapshot: **62 recipes / 62 unique IDs**. Live work metadata was not compared.
- All **196** live staged page/record files and all staged provisional files remain unchanged.
- **20** earlier checkpoint metadata JSON files included.
- No prohibited inputs/images/context/nested archives, unsafe paths, duplicate/case-colliding names, symlinks or special-file entries.

## Earlier guard assertion

Root reported that its packaging guard inspected the earlier checkpoint21_preparation_098.json, whose provisional set was empty, and the assertion failed; the shell nevertheless proceeded to packaging. The revised staging completed at 07:35:01 UTC, before the archive was created at 07:35:08.459251 UTC. This check uses checkpoint21_preparation_098_provisional123.json and verifies the actual archived provisional bytes and latest staging evidence.

This verification independently compares the actual archive with the revised staging evidence. It does not retroactively claim that the earlier guard assertion passed.

## Scope

CRC and opaque member hashes plus permitted map/record identity/crop metadata. No images, witness prose, context, reading decisions, source-edit replay, audit, freeze, rebuilding, packaging or upload. Archived protected bytes compared with the latest staging snapshot; later live progress/receipts/reports were not required to equal staging. Current work crop metadata was not substituted.

## Issues

[]
