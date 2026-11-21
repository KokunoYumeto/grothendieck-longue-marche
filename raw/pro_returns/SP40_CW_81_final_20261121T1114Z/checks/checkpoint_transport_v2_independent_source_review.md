# Independent transport v2 source review

Reviewed: 2026-11-21 04:22:14 UTC. Reviewer: `/root/codec_v2`.

## Scope and source identity

Read all four complete transport scripts and both preparation/review JSON records. Read and hashed source text only. No image or manuscript inspection, codec execution, test, compilation, archive creation, rendering, installation, research, upload, or script change occurred. The findings below describe concrete paths accepted by the source; they do not assert that those inputs occurred in checkpoint25 or that v2 has run.

| File | SHA-256 |
| --- | --- |
| `out/scripts/checkpoint_transport_pack.py` | `4ea2ab7e5feb12944eeb785084c507ae900882b889062e6176494744474e5620` |
| `out/scripts/checkpoint_transport_restore.py` | `e00367d3a524a5d3bf607db494976858b0d634a868d0de93f8741e1548a422c5` |
| `out/scripts/checkpoint_transport_pack_v2.py` | `02cad84a6fe1eddc4d30c2d5ef2e10605146dfaf9b82986aeb113f66eca46a35` |
| `out/scripts/checkpoint_transport_restore_v2.py` | `cf721c734b4591c034ce6dab9a25df5f1ad1eb583bb4fb452e04d0403a559b12` |
| `out/checks/checkpoint_transport_v2_preparation.json` | `17e8008c92acccdcb4042984811350c182f778942fd4b387170777ecc441b86e` |
| `out/checks/checkpoint_transport_v2_root_source_review.json` | `323bd909da12ec29f2f660ebb98e6272ab15622a90f9d9665af9866ef160ddac` |

The preparation record identifies the initial v2 pack hash. The root review explicitly records the two subsequent edits and the current pack hash above. Both v1 hashes match the preserved hashes in those records.

## Findings

### R1 — High: the audit destination can replace the source or finished archive

`checkpoint_transport_pack_v2.py:196-208` validates the output against the source but never validates `args.audit`. Lines 326-327 check source size/hash; line 395 installs the completed transport; line 396 then calls `atomic_write(args.audit, audit_data)`. `atomic_write` uses `os.replace` at lines 55-59.

The accepted argument assignment `--audit = --source` therefore writes audit JSON over the original ZIP after the unchanged-source check. The accepted assignment `--audit = --output` writes audit JSON over the completed transport before its size and hash are reported. The same hole appears in v1 at lines 182-195 and 382-383. Root reports that the actual checkpoint25 invocation used distinct source, output, and audit paths; this review did not inspect its archive or rerun it.

**Bounded correction:** resolve and validate the audit path during v2 preflight, rejecting equality with the source or output. Requiring a new audit path also prevents overwriting an existing checkpoint or other frozen file. Preserve v1 unchanged unless separately directed.

### R2 — Medium: accepted original paths can collide during tree restoration

The packer rejects duplicate raw filename strings at lines 213-218. The restorer does the same at lines 113-117, while `safe_relative_path` returns `PurePosixPath(name)` at lines 99-104. Restoration joins its parts at lines 178-179 and replaces the target at line 187.

Two accepted raw names, `a.bin` and `./a.bin`, both produce the parts tuple `("a.bin",)` and therefore the same restoration target. Each entry can pass the in-memory byte comparison while the second target write replaces the first. A separate accepted entry order, `a.bin.restore-part` followed by `a.bin`, makes the second entry's fixed temporary path at line 184 equal the already restored first file; the exclusive open at line 185 aborts restoration. These mechanisms are inherited from v1. No affected source entry was observed because this review did not inspect checkpoint contents.

**Bounded correction:** preflight the exact mapping from every original name to its restoration target and reject target collisions before packaging and before writing a restored tree. Allocate exclusive temporary paths that cannot collide with any original target instead of fixing the suffix to `.restore-part`.

### R3 — Medium: parsed cache metadata of a non-object JSON type skips fresh encoding

In `checkpoint_transport_pack_v2.py:128-137`, `json.loads` may produce a list, scalar, or `None`; line 130 immediately calls `metadata.get`. For the concrete metadata text `null`, this raises `AttributeError`, which the inner exception tuple does not catch. Control reaches the outer codec exception handler at lines 173-176 and advances to the next codec, bypassing both the remaining cache location and the fresh encoder at lines 138-144.

The outer handler preserves recovery through the remaining candidate or the original bytes, but the intended cache-miss recovery recorded in the root review remains incomplete. The same mechanism applies to an otherwise valid v1 cache reached after the invalid v2 metadata.

**Bounded correction:** require `isinstance(metadata, dict)` before field lookup, treating every other parsed JSON type as an invalid cache record and continuing cache lookup/fresh encoding.

### R4 — Medium: statement IDs distinguish transport variants but repeat across executions

`checkpoint_transport_pack_v2.py:363` constructs the entire `statement_id` from the source digest and the constant `-MIXED-JXL7-EXACT-BYTE-RECOVERY`. The date at line 364 records a completion independently. Every invocation over the same source therefore assigns the same statement ID to its completed-run event. Source changes distinguish snapshots and the suffix distinguishes v1/v2, but neither identifies an individual execution. The v1 expression has the same repeated-execution property at line 350.

**Bounded correction:** add a per-run identifier to the v2 event ID and record that identifier in the audit as well, retaining the source digest and codec variant. No duplicate completed v2 event was observed; v2 remains unexecuted.

## Source checks without additional findings

The v2 candidate path requires a direct original PNG serialization comparison, direct decoded pixel comparison, direct reconstructed PNG comparison, and positive payload savings before adoption (`pack_v2.py:103-179`). Unsupported modes/metadata and source/codec failures retain original entry storage. Every original entry is assembled into the manifest and reconstructed from the staged archive for direct comparison with the source (`pack_v2.py:236-249, 308-327`). The restorer checks payload size/hash, decoded dimensions/pixel hash, and reconstructed original size/hash (`restore_v2.py:121-152`). These are source observations, not completed verification results.

FFmpeg calls use argument lists with input/output pipes and no shell invocation (`restore_v2.py:52-73, 83-88`). The versioned import, format number, bundled script names, and root restoration entry point agree between v2 pack and restore. The original archive is opened for reading, and its size/hash check precedes completion; R1 identifies the subsequent write that bypasses that protection.

## Selection status

V2 remains an unexecuted prepared option. It must remain unselected until a completed later v1 transport actually exceeds the cap. This review supplies no compression ratio, performance, codec equality, manuscript, mathematical, or ink result. It creates no manuscript check event and makes no script changes.
